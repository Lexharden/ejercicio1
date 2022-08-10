from django.forms import models


class Producto(models.Model):
    id = models.CharField(max_length=250, unique=True)
    marca = models.TextField(max_length=500, blank=True)
    nombre = models.TextField(max_length=500, blank=True)
    color = models.TextField(max_length=500, blank=True)

    class Marca(models.Model):
        id_marca = models.CharField(max_length=250, unique=True)
        nombre_marca = models.ForeignKey(Producto, max_length=500, blank=True)
