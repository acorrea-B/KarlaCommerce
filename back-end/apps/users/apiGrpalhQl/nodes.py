import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

class UserOperatorNode(DjangoObjectType):
    """
    Nodo de Graphql para el usuario Operador.


    Atributos que retorna la consulta:
     identification, firstName, lastName, email, phoneNumber
    
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

class UserCostumerNode(DjangoObjectType):
    """
    Nodo de Graphql para el usuario cliente.


    Atributos que retorna la consulta:
     identification, firstName, lastName, email, phoneNumber
    
    """
    class Meta:

        model = get_user_model()
        exclude_fields = ("password",
                          "is_superuser",
                          "is_staff",
                          "is_active",
                          "date_joined",
                          "last_login",
                          "user_type"
                        )
                        
        interfaces = (graphene.relay.Node,)