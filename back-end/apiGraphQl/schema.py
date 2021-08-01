from django.dispatch import receiver
from graphene import ObjectType, Schema
from graphql_jwt import ObtainJSONWebToken, Refresh, Revoke, Verify
from graphql_jwt.refresh_token.signals import refresh_token_rotated
from apps.users.apiGrpalhQl.schema import UserMutation
from apps.products.apiGraphQl.schema import ProductQuery
from apps.purchases.apiGraphQl.schema import PurchaseMutation

class Query( ProductQuery, ObjectType):
    pass

class Mutation( ObjectType, UserMutation, PurchaseMutation ):
    #: el operador debe autenticarse por medio de JWT.
    token_auth = ObtainJSONWebToken.Field()
    #: verifica la validez de un token.
    verify_token = Verify.Field()
    #: obtiene un nuevo token alargando la vida de la sesión.
    refresh_token = Refresh.Field()
    #: invalida un token.
    revoke_token = Revoke.Field()




ROOT_SCHEMA = Schema(query = Query, mutation=Mutation)
