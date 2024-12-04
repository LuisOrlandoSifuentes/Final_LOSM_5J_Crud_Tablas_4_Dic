from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    calidad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    id_sucursal=models.PositiveIntegerField()
    id_provedor=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre