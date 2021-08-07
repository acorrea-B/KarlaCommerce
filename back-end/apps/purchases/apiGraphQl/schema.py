import graphene
import uuid
import base64
from apps.purchases.apiGraphQl.nodes import PurchasesNode
from apps.purchases.apiGraphQl.mutations import NewPurchase, RefundPaymentPurchase
from ..purchasesManager import Purchases
from graphql_jwt.decorators import login_required

class PurchaseQuery(graphene.ObjectType):
    
    purchase = graphene.Field( PurchasesNode, 
                                purchase_id = graphene.String(required = True) 
                            )
    purchases = graphene.List(PurchasesNode)

    def resolve_purchase(root, info, purchase_id):
        """
            Este resolve retorna el estado actualizado de
            de una compra
        """
        id =  uuid.UUID(purchase_id)
        error, purchase = Purchases().confirm_purchase_payment(id)
        if not error:                                                   
            return purchase
        else:
            return None
    
    @login_required
    def resolve_purchases (self, info, *args, **kwargs):
        """
            resolve_purchases obtiene un listado de compras realizadas 
            en el comercio que solo pueden realizar los operadores
            ya que cuenta con la restriccion de login
            
            Retorna:
                purchases(PurchasesNode)
        """
        
        return Purchases().get_purchases()


class PurchaseMutation():
    newPurchase = NewPurchase.Field()
    refundPaymentPurchase = RefundPaymentPurchase.Field()