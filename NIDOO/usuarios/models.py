from django.db import models

# Create your models here.

class Parqueadero(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Usuario(models.Model):
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE)
    idParqueadero = models.FloatField(null=True, blank=True, default=None)
    placa = models.CharField(max_length=6)
    telefono = models.CharField(max_length=15)
    time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return '%s' % (self.idParqueadero)

class Capacidad(models.Model):
    capacidadMax = models.FloatField(null=True, blank=True, default=None)
    capacidadMin = models.FloatField(null=True, blank=True, default=None)
    parqueadero = models.OneToOneField(Parqueadero, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '%s %s' % (self.capacidadMax, self.parqueadero.name)