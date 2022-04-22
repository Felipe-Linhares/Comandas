from django.db import models


class Pedidos(models.Model):
    mesa = models.TextField()
    pedido = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
