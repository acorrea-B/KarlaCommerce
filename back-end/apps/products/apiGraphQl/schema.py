import graphene
from .nodes import ProductNode
from ..models import Product

class ProductQuery(graphene.ObjectType):
    
    list_products = graphene.List( ProductNode )

    def resolve_list_products(root, info, **kwargs):
        """
            Este resolve retorna el listado de productos del 
            commercio sin ningun tipo de filtro o paginado
        """
        
        return Product.objects.all()