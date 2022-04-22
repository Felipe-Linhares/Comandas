from pedidos.models import *
from rest_framework import serializers


class PedidosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


# class ClienteSerializers(serializers.ModelSerializer):
#     pedidos = PedidosSerializers(many=True, read_only=True)

#     class Meta:
#         model = Cliente
#         fields = ['id', 'nome_cliente', 'pedidos', 'email']
#         extra_kwargs = {'pedidos': {'required': False}}
