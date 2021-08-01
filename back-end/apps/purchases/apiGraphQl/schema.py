import graphene
import uuid
import base64
from apps.purchases.apiGraphQl.nodes import PurchasesNode
from apps.purchases.apiGraphQl.mutations import NewPurchase
from ..purchasesManager import Purchases

class PurchaseQuery(graphene.ObjectType):
    
    purchase = graphene.Field( PurchasesNode, 
                                purchase_id = graphene.String(required = True) 
                            )

    def resolve_purchase(root, info, purchase_id):
        """
            Este resolve retorna el estado actualizado de
            de una compra
        """
        product_id = base64.b64decode(purchase_id).decode("utf8").split(':')[1]
        id =  uuid.UUID(product_id)
        error, purchase = Purchases().confirm_purchase_payment(id)
        if not error:                                                   
            return purchase
        else:
            return None


class PurchaseMutation():
    newPurchase = NewPurchase.Field()