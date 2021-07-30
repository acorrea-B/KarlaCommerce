import datetime
import socket
import uuid
from unittest import result
from django.http import response
from django.test import TestCase
from .tpagaService import Tpaga

class ApiTpagaTestCase(TestCase):
    
    def setUp(self):
        self.expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=25)
        self.payment_request_data = { "cost":12312,
                                      "purchase_details_url":"https://www.youtube.com/",
                                      "idempotency_token": str(uuid.uuid4().hex),
                                      "order_id":str(uuid.uuid4().hex),
                                      "terminal_id":"e-commerce",
                                      "purchase_description":"Compra desde Karla comercio",
                                      "user_ip_address":socket.gethostbyname(socket.gethostname()),
                                      "expires_at": self.expiration.isoformat()
                                    }

    def test_payment_request(self):
        error, result = Tpaga().payment_requests(self.payment_request_data)
        self.assertFalse(error)
        self.assertEqual(result.status_code, 201)
        data = result.text
        self.assertIn("token", data)
    
    def test_payment_request_info(self):
        error, result = Tpaga().payment_requests(self.payment_request_data)
        data = result.json()
        error, result = Tpaga().payment_requests_info(data["token"])
        self.assertFalse(error)
        self.assertEqual(result.status_code, 200)
        data = result.text
        self.assertIn("token", data)
    """
    Se comenta esta prueba debido a que no se puede 
    emular el pago durante el tiempo de ejcucion de los test
    solo se debe correr cuando se cuente con un token de un pago realizado
    def test_payment_refund(self):
        error, result = Tpaga().payment_requests(self.payment_request_data)
        data = result.json()
        error, result = Tpaga().payment_refund("pr-3fbec67b8711a715e72151469f6f6cd558f39a09950a6241d4e379383435cc2f8af7ac65")
        self.assertFalse(error)
        self.assertEqual(result.status_code, 200)
        data = result.text
        self.assertIn("token", data)"""
    

