import graphene
from graphene_django import DjangoObjectType
from ..models import Product
from apps.aws.s3Service import Photos
from apps.logger.manager import ManagerLogging

class ProductNode(DjangoObjectType):
    """
    Nodo de Graphql para los productos del comercio.

    Atributos que retorna la consulta:
        id, name, value, description, image
    
    """
    class Meta:

        model = Product              
        interfaces = (graphene.relay.Node,)

    def resolve_image(self, info):
        """ 
            Esta función sobre escribe el nombre la imagen
            por la url de la misma que se encuentra en s3
        """
        print(self.value)
        url = Photos(ManagerLogging().get_logger()).get_presigned_url(self.image, 800)
        if type(url) == str:
            return url
        return ""