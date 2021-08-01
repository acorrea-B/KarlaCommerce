from apps import purchases
import graphene
from .nodes import PurchasesNode, PaymentNode
from .inputs import CostumerPurchaseInput, ProductPurchase 
from apiGraphQl.nodes import ErrorNode
from ..purchasesManager import Purchases
from graphql_jwt.decorators import login_required
from apps.products.productsManager import ProductPruchase

class NewPurchase(graphene.relay.ClientIDMutation):
    
    purchase = graphene.Field(PurchasesNode)
    payment = graphene.Field(PaymentNode)
    error = graphene.Field(ErrorNode)
    class Input:
        costumer = graphene.Argument(CostumerPurchaseInput, required=True)
        products = graphene.List(ProductPurchase, required = True)
        total_value = graphene.Int(required=True)

    #@login_required
    def mutate_and_get_payload(cls, root, **input):
        # Obtienen la ip del cliente
        x_forwarded_for = root.context.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = root.context.META.get('REMOTE_ADDR')
        # Valida que existan los productos de la compra
        error, purchase_products = ProductPruchase().puchase_get_products_by_list(input.get("products"))
        
        if not error:
            # Registra una nueva compra
            error, payment, purchase = Purchases().new_purchase_payment( user_data = input.get("costumer"),
                                                                         products = tuple(purchase_products),
                                                                         total_value = input.get("total_value"),
                                                                         client_ip = ip
                                                                         )
            return NewPurchase(purchase = purchase, payment = payment, error = error)
        else:
            return NewPurchase(purchase = None, payment = None, error = error)