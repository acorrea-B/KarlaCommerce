import datetime
import socket
from django.test import TestCase
from .payment import PaymentTransactions
from apps.purchases.models import PurchaseModel

class PaymentTransactionsTestCase(TestCase):
    def setUp(self):
        self.purchase = PurchaseModel( total_value = 124236,
                                      products = [
                                                                {
                                                                    "name": "Aretes",
                                                                    "value": "6490"
                                                                },
                                                                {
                                                                    "name": "Manilla",
                                                                    "value": "6.000"
                                                                }
                                                            ],
                                        purchase_date = datetime.datetime.utcnow()
                                    )
        self.purchase = {
                         "value":124236,
                         "client_ip": socket.gethostbyname(socket.gethostname())
                        }

    def test_payment_request(self):
        self.purchase.save()
        self.purchase["purchase"] = self.purchase
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request(**self.purchase)
        self.assertFalse(error)
        self.assertTrue(payment)
        self.assertIn("tpaga_payment_url", payment)
        self.assertIn("token", payment)
        self.assertEquals(transaction.token, payment["token"])

    def test_payment_transaction_state(self):
        self.purchase.save()
        self.purchase["purchase"] = self.purchase
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request(**self.purchase)
        self.assertFalse(error)
        error, transaction_created =  PaymentTransactions().\
                                       payment_transaction_state(transaction.id)
        self.assertFalse(error)
        self.assertEquals(transaction_created.state, transaction.state)
        
