import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

class UserCostumerNode(DjangoObjectType):
    """
    Nodo de Graphql para el usuario Operador.

    Implementa los siguiente filtro:
        id:exacto
    Atributos que retorna la consulta:
     id, firstName, lastName, email, cellPhoneNumber
    
    """
    class Meta:

        model = get_user_model()
        exclude_fields = ("password",
        "is_superuser",
        "date_joined",
        "last_login",
        "user_type"
        )
        interfaces = (graphene.relay.Node,)