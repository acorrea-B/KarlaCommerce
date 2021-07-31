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

    def payment_transaction_request(self, value, purchase_id, client_ip):
        """
            payment_transaction_request esta función se encarga de crear 
            una nueva transacción cada vez que se realiza una solicitud
            de pago, hace la petición de la solicitud de pagao a la 
            Api de Tpaga, registra la respuesta de la api y retorna 
            la respuesta de la api junto con transaccion, si se presenta un
            error en la solicitud a la api se retornara el correspondiente error
            Argumentos:
                transaction_id(str) - identificador de la transaccion que se requiere el estado
            Retorna:
                error(dict - None)
                request_payment_response(dict - {})
                transaction(TransactionModel - None)
        """
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
            new_transaction.expiration_date = datetime.datetime.\
                                              fromisoformat(response["expires_at"]) 
            new_transaction.save()
            return {}, response, new_transaction
        else:
            return error, {}, None



    def payment_transaction_state(self, transaction_id):
        """
            payment_transaction_state esta función se encarga de obtener
            y retornar el estado actualizado de una transacción de pago,
            en el caso tal de que haya una respuesta de la API de Tpaga
            de lo contrario retornara el correspondiente error
            Argumentos:
                transaction_id(str) - identificador de la transaccion que se requiere el estado
            Retorna:
                error(dict - None)
                transaction(TransactionModel - None)
        """
        transaction = TransactionModel.objects.get(id = transaction_id)
        error, result = self.service.payment_requests_info(transaction.token)
        if not error:
            return self.validate_payment(transaction, result.json())
        else: 
            return error, None

    def validate_payment(self, transaction, payment_requests_data):
        """
            validate_payment esta función se encarga de validar si un pago
            se ha realizado y actualizar estado de la transacción, 
            pone la fecha de cirre en caso de que se haya realizado el pago
            de lo contrario valida si ha expirado y si ha expirado cambia 
            el estado de latransacción a expired.
            Argumentos:
                transaction(TransactionModel) - transacción a la que corresponde el pago
                payment_requests_data(dict) - información del pago de tpaga
            Retorna:
                transaction(TransactionModel)
        """
        state = payment_requests_data.get("status", "failed") 
        expiration = datetime.datetime.\
                     fromisoformat(payment_requests_data.get("expires_at", "2018-11-05T15:10:57.549-05:00"))
        if state == "paid":
            transaction.state = state 
            transaction.close_date = datetime.datetime.utcnow()
            transaction.save()
        elif  expiration.replace(tzinfo=None) > datetime.datetime.utcnow():
            transaction.state = "expired" 
            transaction.save()
        return {}, transaction


    def payment_transaction_refund(self, transaction_id, operator):
        """
            payment_transaction_state esta función se encarga de obtener
            y retornar el estado actualizado de una transacción de pago,
            en el caso tal de que haya una respuesta de la API de Tpaga
            de lo contrario retornara el correspondiente error
            Argumentos:
                transaction_id(str) - identificador de la transaccion que se requiere el estado
                operator(User) - operador que realizo el reembolso
            Retorna:
                error(dict - None)
                transaction(TransactionModel - None)
        """
        transaction = TransactionModel.objects.get(id = transaction_id)
        error, result = self.service.payment_refund(transaction.token)
        if not error:
            result = result.json()
            transaction.state = result.get("status") 
            transaction.operator = operator
            transaction.close_date = datetime.datetime.utcnow()
            return {}, transaction
        else: 
            return error, None