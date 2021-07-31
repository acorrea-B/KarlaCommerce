import uuid
from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()

class PurchaseModel(models.Model):
    # Identificador unico de la compra
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    # Valor total de la compra
    total_value = models.IntegerField()
    # Listado de productos
    products = models.JSONField()
    # Cliente que realizo la compra
    costumer = models.OneToOneField( User,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank = True
                                    )
    # Fecha de la compra 
    purchase_date = models.DateField()


