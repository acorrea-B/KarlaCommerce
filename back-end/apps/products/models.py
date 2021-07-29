import uuid
from django.db import models

class Product(models.Model):
    # Identificador unico del producto
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    # Nombre del producto
    name = models.CharField(max_length = 200)
    # Valor del producto
    value = models.DecimalField(max_digits = 10, decimal_places = 2)
    # Breve descripcion del producto
    description = models.TextField(blank = True)
    # Nombre de la imagen almacenada en S3
    image = models.CharField(max_length = 200)

