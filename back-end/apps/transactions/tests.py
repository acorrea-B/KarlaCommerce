import uuid
import socket
from django.test import TestCase
from .payment import PaymentTransactions

class PaymentTransactionsTestCase(TestCase):
    def setUp(self):
        self.purchase = {"purchase_id":str(uuid.uuid4().hex),
                         "value":124236,
                         "client_ip": socket.gethostbyname(socket.gethostname())
                        }
    def test_payment_request(self):
        error, result = PaymentTransactions().payment_request(**self.purchase)
        self.assertFalse(error)
        self.assertTrue(result)
        self.assertIn(result["tpaga_payment_url"])
        self.assertIn(result["token"])
