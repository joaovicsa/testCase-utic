from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

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

    def full_name(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"

class Pedido(models.Model):
    class StatusPedido(models.TextChoices):
        SOLICITADO = 'Solicitado', 'Solicitado'
        ENCAMINHADO = 'Encaminhado', 'Encaminhado'
        FINALIZADO = 'Finalizado', 'Finalizado'

    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
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

class Envio(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    metodo_envio = models.CharField(max_length=50, null=False)
    custo_envio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    data_envio = models.DateTimeField()
    data_entrega = models.DateTimeField()
    numero_rastreamento = models.CharField(max_length=100, editable=False)

    class Meta:
        db_table = 'envios'
        verbose_name = 'Envio'
        verbose_name_plural = 'Envios'

    def save(self, *args, **kwargs):
        if not self.numero_rastreamento:
            # Generate a random string with 32 characters
            self.numero_rastreamento = get_random_string(32)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Envio #{self.id} - Pedido: {self.pedido.id}"

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    nome_contato = models.CharField(max_length=100)
    email_contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, null=False)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome
