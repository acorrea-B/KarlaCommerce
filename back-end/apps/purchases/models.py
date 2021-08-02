import uuid
from django.db import models
from django.contrib.auth import get_user_model 
from apps.products.models import PurchaseProduct

User = get_user_model()

class PurchaseModel(models.Model):
    # Identificador unico de la compra
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    # Valor total de la compra
    total_value = models.IntegerField()
    # Listado de productos
    products = models.ManyToManyField(PurchaseProduct)
    # Cliente que realizo la compra
    costumer = models.ForeignKey( User,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank = True
                                    )
    # Fecha de la compra 
    purchase_date = models.DateField()
    # Fecha de la confirmación de la compra 
    purchase_confirmation_date = models.DateField(null=True,
                                                   blank = True)
    # Estado de la compra
    state = models.CharField(max_length = 50)


