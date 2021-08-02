import socket
from django.test import TestCase
from .purchasesManager import Purchases
from apps.products.models import Product
from apps.products.productsManager import ProductPruchase

class PurchasesTestCase(TestCase):
    def setUp(self):
        self.customer = {"first_name":"pepito",
                         "last_name":"perez",
                         "identification":"3245645",
                         "email":"asdas@example.com"
                        }
        self.total_value = 124236
        self.client_ip = socket.gethostbyname(socket.gethostname())
    
    def products(self):
        new_product_1 = Product(**{"name": "Cadenilla",
                                    "value": 15200,
                                    "image": "aretes.png"})
        new_product_1.save()
        new_product_2 =  Product(**{"name": "Anillo de plata",
                                    "value": 150999,
                                    "image": "anillo.png"})
        new_product_2.save()
        list_products = [{"product_id":new_product_1.id, "amount":2 },
                         {"product_id":new_product_2.id, "amount":1 }]
        error, purchase_products = ProductPruchase().puchase_get_products_by_list(list_products)
        return tuple(purchase_products)

    def test_new_purchase_payment(self):
        error, payment, purchase = Purchases().\
                                    new_purchase_payment(self.customer, self.products(), 
                                                    self.total_value, self.client_ip
                                                  )
        self.assertFalse(error)
        self.assertIn("tpaga_payment_url", payment)
        self.assertIn("token", payment)
        self.assertIn("tpaga_payment_url", payment)
        self.assertEquals(purchase.state, "pending")
    
    def test_confirm_purchase_payment(self):
        error, payment, purchase = Purchases().\
                                    new_purchase_payment(self.customer, self.products(), 
                                                            self.total_value, self.client_ip
                                                            )
        error, puchase_info = Purchases().\
                              confirm_purchase_payment( purchase.id )
        self.assertFalse(error)
        self.assertEquals(puchase_info.state, "created")
        
        
