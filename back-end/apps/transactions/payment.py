import datetime
from apps.transactions.models import TransactionModel 
from services.tpagaService import Tpaga
from django.conf import settings


class PaymentTransactions:
    
    def __init__(self):
        self.service = Tpaga()
        self.request = { "purchase_details_url":settings.WEBCLIENT,
                         "terminal_id":"Karla e-commerce",
                         "purchase_description":"""Gracias por comprar en Karla Accesorios, a continuación,
                                                   encontraras el valor de tu compra.
                                                """
                       }

    def payment_request(self, value, purchase_id, client_ip):
        new_transaction = TransactionModel(value = value,
                                      state = "pending",
                                      creation_date = datetime.datetime.utcnow()
                                      )
        expiration = new_transaction.creation_date + datetime.timedelta(minutes=25)
        self.request["cost"] = value                  
        self.request["idempotency_token"] = new_transaction.id                  
        self.request["order_id"] = purchase_id                 
        self.request["user_ip_address"] = client_ip                 
        self.request["expires_at"] = expiration.isoformat()                
        error, response = self.service.payment_requests(self.request)
        if not error:
            response = response.json()
            new_transaction.state = response["status"]
            new_transaction.token = response["token"]
            new_transaction.expiration_date = datetime.datetime.fromisoformat(response["expires_at"]) 
            new_transaction.save()
            return {}, response
        else:
            return error, None



    def payment_state(self, transaction_id):
        transaction = TransactionModel.objects.get(id = transaction_id)
        
        pass

    def payment_refund(self):
        pass