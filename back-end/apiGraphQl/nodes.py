  
from graphene import  String,ObjectType,Int

class ErrorNode(ObjectType):
    status =  Int()
    message  =  String()