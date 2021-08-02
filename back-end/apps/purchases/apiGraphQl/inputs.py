import graphene

class ProductPurchase(graphene.InputObjectType):
    """Nodo de entrada para cada producto de la compra."""

    #: Identificador unico del producto.
    product_id = graphene.String(required = True)
    #: Cantida del producto.
    amount = graphene.Int(required = True)
    

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

