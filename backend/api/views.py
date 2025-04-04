from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ClienteSerializer, PedidoSerializer, EnvioSerializer, CategoriaSerializer, FornecedorSerializer, ProdutoSerializer, ItemPedidoSerializer, MetodoPagamentoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Cliente, Pedido, Envio, Categoria, Fornecedor, Produto, ItemPedido, MetodoPagamento


class ClienteListCreate(generics.ListCreateAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class ClienteDelete(generics.DestroyAPIView):
    serializer_class = ClienteSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(author=user)


class PedidoListCreate(generics.ListCreateAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pedido.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class PedidoDelete(generics.DestroyAPIView):
    serializer_class = PedidoSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pedido.objects.filter(author=user)


class EnvioDelete(generics.DestroyAPIView):
    serializer_class = EnvioSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Envio.objects.filter(author=user)


class EnvioListCreate(generics.ListCreateAPIView):
    serializer_class = EnvioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Envio.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class CategoriaListCreate(generics.ListCreateAPIView):
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Categoria.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class CategoriaDelete(generics.DestroyAPIView):
    serializer_class = CategoriaSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Categoria.objects.filter(author=user)


class FornecedorListCreate(generics.ListCreateAPIView):
    serializer_class = FornecedorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Fornecedor.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class FornecedorDelete(generics.DestroyAPIView):
    serializer_class = FornecedorSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Fornecedor.objects.filter(author=user)


class ProdutoListCreate(generics.ListCreateAPIView):
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Produto.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class ProdutoDelete(generics.DestroyAPIView):
    serializer_class = ProdutoSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Produto.objects.filter(author=user)


class ItemPedidoListCreate(generics.ListCreateAPIView):
    serializer_class = ItemPedidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ItemPedido.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class ItemPedidoDelete(generics.DestroyAPIView):
    serializer_class = ItemPedidoSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ItemPedido.objects.filter(author=user)


class MetodoPagamentoListCreate(generics.ListCreateAPIView):
    serializer_class = MetodoPagamentoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return MetodoPagamento.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class MetodoPagamentoDelete(generics.DestroyAPIView):
    serializer_class = MetodoPagamentoSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return MetodoPagamento.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
