import graphene

class UserOperatorInput(graphene.InputObjectType):
    """Nodo de entrada para la creación de un usuario operador."""

    #: numero de identificación del operador.
    identification = graphene.String(required=True)
    #: numero de identificación del operador.
    phone_number = graphene.String(required=True)
    #: contraseña del usuario.
    password = graphene.String(required=True)
    #: email del usuario.
    email = graphene.String(required=True)
    #: nombres  del usuario.
    first_name = graphene.String(required=True)
    #: apellidos del usuario.
    last_name = graphene.String(required=True)
    #: tipo de usuario
    user_type=graphene.Int(required=True)
