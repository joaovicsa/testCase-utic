from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cliente, Pedido, Envio, Categoria, Fornecedor, Produto, ItemPedido, MetodoPagamento, Pagamento, Avaliacao


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "primeiro_nome", "ultimo_nome", "email", "senha", "telefone", "endereco", "criado_em", "atualizado_em"]
        extra_kwargs = {"criado_em": {"read_only": True}}


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "cliente", "data_pedido", "status", "valor_total", "criado_em", "atualizado_em"]
        extra_kwargs = {"criado_em": {"read_only": True}}


class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = ["id", "pedido", "metodo_envio", "custo_envio", "data_envio", "data_entrega", "numero_rastreamento"]
        extra_kwargs = {"numero_rastreamento": {"read_only": True}}


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome", "descricao"]


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ["id", "nome_contato", "email_contato", "telefone", "endereco", "categoria"]


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "preco", "quantidade_estoque", "categoria", "fornecedor", "criado_em", "atualizado_em"]
        extra_kwargs = {"criado_em": {"read_only": True}}


class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = ItemPedido
        fields = ["id", "pedido", "produto", "quantidade", "preco_unitario"]


class MetodoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPagamento
        fields = ["id", "nome", "descricao"]


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['id', 'pedido', 'metodo_pagamento', 'valor', 'data_pagamento', 'status']


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'produto', 'cliente', 'avaliacao', 'comentario', 'data_avaliacao']
        extra_kwargs = {"data_avaliacao": {"read_only": True}}