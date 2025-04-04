from django.urls import path
from . import views


urlpatterns = [
    path("clientes/", views.ClienteListCreate.as_view(), name="cliente-list"),
    path("clientes/delete/<int:pk>/", views.ClienteDelete.as_view(), name="delete-cliente"),
    path("pedido/", views.PedidoListCreate.as_view(), name="pedido-list"),
    path("pedido/delete/<int:pk>/", views.PedidoDelete.as_view(), name="delete-pedido"),
    path("envio/", views.EnvioListCreate.as_view(), name="envio-list"),
    path("envio/delete/<int:pk>/", views.EnvioDelete.as_view(), name="delete-envio"),
    path("categoria/", views.CategoriaListCreate.as_view(), name="categoria-list"),
    path("categoria/delete/<int:pk>/", views.CategoriaDelete.as_view(), name="delete-categoria"),
    path("fornecedor/", views.FornecedorListCreate.as_view(), name="fornecedor-list"),
    path("fornecedor/delete/<int:pk>/", views.FornecedorDelete.as_view(), name="delete-fornecedor"),
    path("produto/", views.ProdutoListCreate.as_view(), name="produto-list"),
    path("produto/delete/<int:pk>/", views.ProdutoDelete.as_view(), name="delete-produto"),
    path("item_pedido/", views.ItemPedidoListCreate.as_view(), name="item_pedido-list"),
    path("item_pedido/delete/<int:pk>/", views.ItemPedidoDelete.as_view(), name="delete-item_pedido"),
    path("metodo_pagamento/", views.MetodoPagamentoListCreate.as_view(), name="metodo_pagamento-list"),
    path("metodo_pagamento/delete/<int:pk>/", views.MetodoPagamentoDelete.as_view(), name="delete-metodo_pagamento"),
    path("pagamento/", views.PagamentoListCreate.as_view(), name="pagamento-list"),
    path("pagamento/delete/<int:pk>/", views.PagamentoDelete.as_view(), name="delete-pagamento"),
]