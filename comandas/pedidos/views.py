from pedidos.models import *
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework.response import Response
from pedidos.serializers import *

# PEDIDO


class PedidosGET(generics.ListAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializers


class PedidosPOSTAndUpdate(generics.ListAPIView, generics.CreateAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializers


class PedidosGETAndUpdateAndDelete(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializers


class PedidosGETAndDelete(generics.ListAPIView, generics.DestroyAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializers


# # CLIENTE
# class ClienteGET(generics.ListAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializers


# class ClientePOSTAndUpdate(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializers


# class ClienteGETAndUpdateAndDelete(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializers


# class ClienteGETAndDelete(generics.ListAPIView, generics.DestroyAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializers
