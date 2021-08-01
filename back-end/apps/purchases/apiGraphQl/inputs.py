from typing_extensions import Required
import graphene

class ProdcutPurchase(graphene.InputObjectType):
    """Nodo de entrada para cada producto de la compra."""
    #: Valor  del producto.
    value = graphene.Int(required = True)
    #: Nombre  del producto.
    name = graphene.String(required = True)
    #: Cantida del producto.
    amount = graphene.String(required = True)


class PurchaseInput(graphene.InputObjectType):
    """Nodo de entrada para la creación de una compra."""

    #: Valor total de la compra.
    total_value = graphene.Int(required=True)
    #: Direccion ip desde la cual se realiza la compra.
    client_ip = graphene.String(required=True)
    #: Json de la compra compra.
    products = graphene.List(ProdcutPurchase, required = True)
    

class CostumerPurchaseInput(graphene.InputObjectType):
    """Nodo de entrada de los datos de un usuario cliente."""
    #: numero de identificación del operador.
    identification = graphene.String(required=True)
    #: email del usuario.
    email = graphene.String(required=True)
    #: nombres  del usuario.
    first_name = graphene.String(required=True)
    #: apellidos del usuario.
    last_name = graphene.String(required=True)

