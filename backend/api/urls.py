from django.urls import path
from . import views


urlpatterns = [
    path("clientes/", views.ClienteSerializer().as_view(), name="cliente-list"),
    path("clientes/delete/<int:pk>/", views.ClienteDelete.as_view(), name="delete-cliente")
]