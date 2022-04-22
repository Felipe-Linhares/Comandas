from django.urls import path
from pedidos.views import *

urlpatterns = [
    path('GET/', PedidosGET.as_view()),
    path('POST/', PedidosPOSTAndUpdate.as_view()),
    path('PUT/<int:pk>/', PedidosGETAndUpdateAndDelete.as_view()),
    path('DELETE/<int:pk>/', PedidosGETAndDelete.as_view()),

    # path('cliente/GET/', ClienteGET.as_view()),
    # path('cliente/POST/', ClientePOSTAndUpdate.as_view()),
    # path('cliente/PUT/<int:pk>/', ClienteGETAndUpdateAndDelete.as_view()),
    # path('cliente/DELETE/<int:pk>/', ClienteGETAndDelete.as_view()),

]
