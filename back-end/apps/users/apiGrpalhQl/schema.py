from .mutations import CreateUserOperator


class UserMutation():
    createUserOperator=CreateUserOperator.Field()