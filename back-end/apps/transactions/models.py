import uuid
from django.db import models
from django.contrib.auth import get_user_model 
User = get_user_model()

class TransactionModel(models.Model):
    # Identificador unico de la transacción
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    # Valor de la transaccion
    value = models.IntegerField()
    # Estado de la transacción
    state = models.CharField(max_length = 200)
    # Token de la transacción
    token = models.CharField(blank = True, max_length = 250)
    # Fecha de creación de la transacción
    creation_date = models.DateField()
    # Fecha de cierre de la transacción
    close_date = models.DateField(blank = True, null=True)
    # Fecha de expiración de la transacción
    expiration_date = models.DateField(blank = True)
    # Direccion ip desde la cual se solicita la transacción
    client_ip = models.CharField(max_length=25)
    # Operador que realiza el reembolso
    operator = models.OneToOneField( User,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank = True
                                    )
