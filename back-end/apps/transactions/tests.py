import datetime
import socket
from django.test import TestCase
from .payment import PaymentTransactions
from apps.purchases.models import PurchaseModel
from apps.products.models import PurchaseProduct, Product

class PaymentTransactionsTestCase(TestCase):
    def setUp(self):
        
        self.data = {
                         "value":124236,
                         "client_ip": socket.gethostbyname(socket.gethostname())
                        }
    def purchase(self):
        new_product_1 = Product(**{"name": "Aretes",
                                    "value": 15200,
                                    "image": "aretes.png"})
        new_product_1.save()
        new_product_2 =  Product(**{"name": "Anillos de oro",
                                    "value": 150999,
                                    "image": "anillo.png"})
        new_product_2.save()
        product_1 = PurchaseProduct(product = new_product_1, amount=2)
        product_1.save()
        product_2 = PurchaseProduct(product = new_product_2, amount=2)
        product_2.save()
        purchase = PurchaseModel( total_value = product_1.product.value + product_2.product.value ,
                                  purchase_date = datetime.datetime.utcnow()
                                )
        purchase.save()
        purchase.products.add(product_1, product_2)
        return purchase

    def test_payment_request(self):
        
        self.data["purchase"] = self.purchase()
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request(**self.data)
        self.assertFalse(error)
        self.assertTrue(payment)
        self.assertIn("tpaga_payment_url", payment)
        self.assertIn("token", payment)
        self.assertEquals(transaction.token, payment["token"])

    def test_payment_transaction_state(self):
        self.data["purchase"] = self.purchase()
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request(**self.data)
        self.assertFalse(error)
        error, transaction_created =  PaymentTransactions().\
                                       payment_transaction_state(transaction)
        self.assertFalse(error)
        self.assertEquals(transaction_created.state, transaction.state)
        
