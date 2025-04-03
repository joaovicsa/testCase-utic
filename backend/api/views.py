from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ClienteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Cliente

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

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
