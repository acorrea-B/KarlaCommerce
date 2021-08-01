from apps import purchases
import graphene
from .nodes import PurchasesNode, PaymentNode
from .inputs import PurchaseInput, CostumerPurchaseInput
from apiGraphQl.nodes import ErrorNode
from ..purchasesManager import Purchases
from graphql_jwt.decorators import login_required

class NewPurchase(graphene.relay.ClientIDMutation):
    
    purchase = graphene.Field(PurchasesNode)
    payment = graphene.Field(PaymentNode)
    error = graphene.Field(ErrorNode)
    class Input:
        purchase = graphene.Argument(PurchaseInput, required=True)
        costumer = graphene.Argument(CostumerPurchaseInput, required=True)

    #@login_required
    def mutate_and_get_payload(cls, root, **input):
        # Registra una nueva compra
        error, payment, purchase = Purchases().new_purchase_payment( user_data = input.get("costumer"),
                                                **input.get("purchase"))
        return NewPurchase(purchase = purchase, payment = payment, error = error)