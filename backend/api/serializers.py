from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cliente

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