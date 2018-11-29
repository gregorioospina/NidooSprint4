from rest_framework import serializers
from . import models


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'parqueadero', 'idParqueadero', 'placa', 'telefono', 'time',)
        model = models.Usuario