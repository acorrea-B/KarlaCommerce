import socket
from django.test import TestCase
from .purchasesManager import Purchases

class PurchasesTestCase(TestCase):
    def setUp(self):
        self.customer = {"first_name":"pepito",
                         "last_name":"perez",
                         "identification":"3245645",
                         "email":"asdas@example.com"
                        }
        self.products = [  {
                                "name": "Aretes",
                                "value": "6490"
                            },
                            {
                                "name": "Manilla",
                                "value": "6.000"
                            }
                        ]
        self.total_value = 124236
        self.client_ip = socket.gethostbyname(socket.gethostname())
    
    def test_new_purchase(self):
        error, payment, transaction = Purchases().\
                                      new_purchase(self.customer, self.products, 
                                                    self.total_value, self.client_ip
                                                  )
        self.assertFalse(error)
        self.assertIn("tpaga_payment_url", payment)
        self.assertIn("token", payment)
        self.assertEquals(transaction.token, payment["token"])
        
