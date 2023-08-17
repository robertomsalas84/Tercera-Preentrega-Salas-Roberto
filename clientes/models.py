from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=70)
    dni = models.IntegerField()
    ciudad = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    producto = models.CharField(max_length=70)
    meses_garantia = models.IntegerField()
    promocion = models.BooleanField()

    def __str__(self):
        return f"{self.producto}"

class Sucursal(models.Model):
    numero_sucursal = models.IntegerField()
    ciudad = models.CharField(max_length=30)
    metros_cuadrados = models.IntegerField()

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return f"{self.numero_sucursal}"