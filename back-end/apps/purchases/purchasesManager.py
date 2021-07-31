import datetime
from apps.purchases.models import PurchaseModel
from apps.transactions.payment import PaymentTransactions
from apps.users.usersManager import UserManager

class Purchases:
    
    def new_purchase(self, user_data, products, 
                      total_value, client_ip):
        costumer = UserManager().\
                    get_or_create_costumer(**user_data)
        purchase = PurchaseModel( total_value = total_value,
                                  products = products,
                                  costumer = costumer,
                                  purchase_date = datetime.datetime.utcnow()
                                )
        purchase.save()
        error, payment, transaction = PaymentTransactions().\
                                      payment_transaction_request( purchase = purchase,
                                                   value = total_value,
                                                   client_ip = client_ip
                                                  )
        if error:
            return error, None, None
        else:
            return {}, payment, purchase
        

    def get_purchases(self):
        pass
    
    def refund_purchase(self, purchsae_id):
        pass