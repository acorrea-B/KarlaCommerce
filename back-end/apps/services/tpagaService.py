from logging import error
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from apps.logger.manager import ManagerLogging

class Tpaga:
    def __init__(self):
        self.commerce = settings.COMMERCE
        self.password = settings.PASSWORDCOMMERCE
        self.url = "https://stag.wallet.tpaga.co/merchants/api/v1/"
        self.auth = HTTPBasicAuth(self.commerce, self.password)
        self.loggin = ManagerLogging().get_logger()
        
    def get_session(self):
        session = requests.Session()
        session.aut = (self.commerce, self.password)
        return session

    def payment_requests(self, data):
        error = {"status": 400,
                    "message":"""!Ooops no pudimos procesar el pago¡ 
                                  Intentalo de nuevo en un momento""" 
                }, None
        try:
            response = requests.post(self.url + "payment_requests/create", 
                                        auth=self.auth,
                                        data = data
                                    )
        except requests.exceptions.RequestException as e:
            self.logging.error(e, extra = { "info": self.payment_requests.__name__})
            return error
        except requests.exceptions.HTTPError as e:
            return e, None
        except requests.exceptions.ConnectionError as e:
            self.logging.error(e, extra = { "info": self.payment_requests.__name__})
            return error
        except requests.exceptions.Timeout as e:
            self.logging.info(e, extra = { "info": self.payment_requests.__name__})
            return error
        else:
            return None, response

    def payment_requests_info(self, token):
        error = {"status": 400,
                    "message":"""!Ooops no pudimos confirmar el pago¡ 
                                  Pronto te notificaremos por correo eléctronico el estado de tu pago""" 
                }, None
        try:
            response = requests.get(self.url + "payment_requests/{0}/info".format(token), 
                                        auth = self.auth
                                    )
        except requests.exceptions.RequestException as e:
            self.logging.error(e, extra = { "info": self.payment_requests.__name__})
            return error
        except requests.exceptions.HTTPError as e:
            return e, None
        except requests.exceptions.ConnectionError as e:
            self.logging.error(e, extra = { "info": self.payment_requests.__name__})
            return error
        except requests.exceptions.Timeout as e:
            self.logging.info(e, extra = { "info": self.payment_requests.__name__})
            return error
        else:
            return None, response

    def payment_requests_refund(self):
        pass

