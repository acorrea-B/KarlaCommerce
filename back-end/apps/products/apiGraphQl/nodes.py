import graphene
from graphene_django import DjangoObjectType
from ..models import Product

class ProductNode(DjangoObjectType):
    """
    Nodo de Graphql para los productos del comercio.

    Atributos que retorna la consulta:
        id, name, value, description, image
    
    """
    class Meta:

        model = Product()                 
        interfaces = (graphene.relay.Node,)

    def resolve_image(self):
        pass