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
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request(**self.purchase)
        self.assertFalse(error)
        self.assertTrue(payment)
        self.assertIn("tpaga_payment_url", payment)
        self.assertIn("token", payment)
        self.assertEquals(transaction.token, payment["token"])

    def test_payment_transaction_state(self):
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request(**self.purchase)
        self.assertFalse(error)
        error, transaction_created =  PaymentTransactions().\
                                     payment_transaction_state(transaction.id)
        self.assertFalse(error)
        self.assertEquals(transaction_created.state, transaction.state)

       
