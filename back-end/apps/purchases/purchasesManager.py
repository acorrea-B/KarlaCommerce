from logging import error
from apps.transactions.models import TransactionModel
import datetime
from apps.purchases.models import PurchaseModel
from apps.transactions.payment import PaymentTransactions
from apps.users.usersManager import UserManager
from apps.purchases.models import PurchaseModel


class Purchases:
    
    def new_purchase_payment(self, user_data, products, 
                            total_value, client_ip):
        """
            new_purchase_payment esta función se encarga de registrar una 
            una nueva compra, en el comercio, ademas de crear la 
            transacción en la que se vera el estado del pago de la compra 
            Argumentos:
                user_data(dict) - datos del comprador
                products(json) - productos de la compra
                total_value(int) - valor total de la compra
                client_ip(str) - ip desde la cual se realiza la compra
            Retorna:
                error(dict - None)
                payment(dict - None)
                purchase(PurchaseModel - None)
        """
        costumer = UserManager().\
                    get_or_create_costumer(**user_data)
        purchase = PurchaseModel( total_value = total_value,
                                  costumer = costumer,
                                  state = "pending",
                                  purchase_date = datetime.datetime.utcnow()
                                )
        purchase.save()
        purchase.products.add(*products)
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
        """
            get_purchases esta función retorna una lista
            de las compras que se han realizado en el comercio
            Retorna:
                purchases(list - [])
        """
        return PurchaseModel.objects.all().order_by("-id")
    
    def confirm_purchase_payment(self, purchase_id):
        """
            confirm_purchase_payment esta función obtiene el estado actualizado
            de una compra y de la ultima transacción correspondiente al pago de la misma.
            Argumentos:
                purchase_id(str) - identificador unico de la compra
            Retorna:
                error(dict - None)
                purchase(PurchaseModel - None)
        """
        purchase = PurchaseModel.objects.get( id = purchase_id)
        transaction = TransactionModel.objects.filter(purchase = purchase_id ).last()
        error, transaction = PaymentTransactions().\
                             payment_transaction_state(transaction)
        if not error:
            purchase.state = transaction.state
            if purchase.state == "paid":
                purchase.purchase_confirmation_date = transaction.close_date
            purchase.save()
            return {}, purchase
        else:
            return error, None

    

    def refund_purchase(self, purchase_id, operator):
        """
            refund_purchase esta función obtiene el estado actualizado
            de una compra y de la ultima transacción correspondiente al pago de la misma.
            Argumentos:
                purchase_id(str) - identificador unico de la compra
                operator(User) - operdor que realiza el reembolso del dinero 
            Retorna:
                error(dict - None)
                purchase(PurchaseModel - None)
        """
        purchase = PurchaseModel.objects.get( id = purchase_id)
        transaction = TransactionModel.objects.filter(purchase = purchase_id ).last()
        if transaction.state == "paid":
            error, refund_transaction = PaymentTransactions().\
                                        payment_transaction_refund(transaction,
                                                                operator)
            if not error:
                purchase.state = refund_transaction.state
                purchase.save()
                return {}, purchase
            else:
                return error, None
        else:
            return {"status": 400,
                    "message":"!opsss¡ no puedes reembolsar el dinero de esta compra porque aun no han realizado el pago"
                    }, None

        
    
                        


        