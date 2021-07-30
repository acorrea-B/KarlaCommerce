import datetime
import socket
from django.test import TestCase
from .tpagaService import Tpaga

class ApiTpagaTestCase(TestCase):
    
    def setUp(self):
        self.expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=25)
        self.payment_request_data = { "cost":12312,
                                      "purchase_details_url":"https://www.youtube.com/",
                                      "idempotency_token":"ea0c98c5-e850-49c4-b7f9-24a9014a2339",
                                      "order_id":"qwesada",
                                      "terminal_id":"e-commerce",
                                      "purchase_description":"Compra desde Karla comercio",
                                      "user_ip_address":socket.gethostbyname(socket.gethostname()),
                                      "expires_at": self.expiration.isoformat()
                                    }
    
    def test_payment_request(self):
        print(self.payment_request_data)
        payment = Tpaga().payment_requests(self.payment_request_data)
        print(payment.status_code)
        print(payment.text)
    
    def test_payment_request_info(self):
        payment = Tpaga().payment_requests_info("pr-44afa9a48322dba1ab5fed3c003053066f180a12fdf8fd7e753e879e9000e6945ae4ba30")
        print(payment.status_code)
        print(payment.text)
