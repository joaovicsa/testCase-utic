from django.urls import path
from . import views


urlpatterns = [
    path("clientes/", views.ClienteListCreate.as_view(), name="cliente-list"),
    path("clientes/delete/<int:pk>/", views.ClienteDelete.as_view(), name="delete-cliente"),
    path("pedido/", views.PedidoListCreate.as_view(), name="pedido-list"),
    path("pedido/delete/<int:pk>/", views.PedidoDelete.as_view(), name="delete-pedido"),
    path("envio/", views.EnvioListCreate.as_view(), name="envio-list"),
    path("envio/delete/<int:pk>/", views.EnvioDelete.as_view(), name="delete-envio"),
    path("Categoria/", views.CategoriaListCreate.as_view(), name="envio-list"),
    path("Categoria/delete/<int:pk>/", views.CategoriaDelete.as_view(), name="delete-Categoria"),
]