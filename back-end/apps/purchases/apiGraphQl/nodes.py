import graphene
from apps.purchases.models import PurchaseModel
from graphene_django import DjangoObjectType

class PurchasesNode(DjangoObjectType):
    """
    Nodo de Graphql para las compras.


    Atributos que retorna la consulta:
        __all_
    
    """
    class Meta:

        model = PurchaseModel
        interfaces = (graphene.relay.Node,)

class PaymentNode(graphene.ObjectType):
    #: Link de pago de la billetera Tpaga
    tpaga_payment_url = graphene.String()
    #: Fecha de expiracion del link
    expires_at = graphene.String()