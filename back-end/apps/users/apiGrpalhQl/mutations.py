import graphene
from .nodes import UserOperatorNode
from .inputs import UserOperatorInput
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required

class CreateUserOperator(graphene.relay.ClientIDMutation):
    
    new_user = graphene.Field(UserOperatorNode)

    class Input:
        operator = graphene.Argument(UserOperatorInput, required=True)

    @login_required
    def mutate_and_get_payload(cls, root, **input):
        # Registra un usuario operador en la base de datos.
        user_data = input.get("operator")
        user = get_user_model().objects.create_user( **user_data)
        return CreateUserOperator(new_user=user)




