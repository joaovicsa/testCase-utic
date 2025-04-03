from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    primeiro_nome = models.CharField(max_length=50, null=False)
    ultimo_nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    senha = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"

class Pedido(models.Model):
    class StatusPedido(models.TextChoices):
        SOLICITADO = 'Solicitado', 'Solicitado'
        ENCAMINHADO = 'Encaminhado', 'Encaminhado'
        FINALIZADO = 'Finalizado', 'Finalizado'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    data_pedido = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=StatusPedido.choices,
        default=StatusPedido.SOLICITADO
    )
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"Pedido #{self.id} - Cliente: {self.cliente.full_name()}"