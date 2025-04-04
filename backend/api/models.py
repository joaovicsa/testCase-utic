from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    senha = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clientes'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"

    def full_name(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField()

    class Meta:
        db_table = 'categorias'
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
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=1 ,null=False)

    class Meta:
        db_table = 'fornecedores'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantidade_estoque = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.RESTRICT, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produtos'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    class StatusPedido(models.TextChoices):
        SOLICITADO = 'Solicitado', 'Solicitado'
        ENCAMINHADO = 'Encaminhado', 'Encaminhado'
        FINALIZADO = 'Finalizado', 'Finalizado'

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_DEFAULT, default=1)
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

    def update_valor_total(self):
        """Calculate and update the total value of the order based on its items"""
        total = sum(
            item.quantidade * item.preco_unitario
            for item in self.itempedido_set.all()
        )
        self.valor_total = total
        self.save()


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_DEFAULT, default=1, null=False)
    produto = models.ForeignKey(Produto, on_delete=models.SET_DEFAULT, default=1, null=False)
    quantidade = models.IntegerField(null=False)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        db_table = 'itens_pedido'
        verbose_name = 'Item do Pedido '
        verbose_name_plural = 'Itens do Pedido'

    def __str__(self):
        return f"Pedido: ({self.pedido.id}) -> Item #{self.id} - Produto: {self.produto.nome} - Quantidade: {self.quantidade}"

    def save(self, *args, **kwargs):
        # Set preco_unitario from produto.preco when creating the item
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco

        super().save(*args, **kwargs)

        # Update pedido valor_total
        self.pedido.update_valor_total()


class MetodoPagamento(models.Model):
    class Metodo(models.TextChoices):
            CREDITO = 'Crédito', 'Crédito'
            PAYPAL = 'Paypal', 'Paypal'
            BOLETO = 'Boleto', 'Boleto'

    nome = models.CharField(
        max_length=50,
        choices=Metodo.choices,
        default=Metodo.CREDITO
    )
    descricao = models.TextField()

    class Meta:
        db_table = 'metodos_pagamento'
        verbose_name = 'Método de Pagamento'
        verbose_name_plural = 'Métodos de Pagamento'

    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    class StatusPagamento(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        APROVADO = 'Aprovado', 'Aprovado'
        REJEITADO = 'Rejeitado', 'Rejeitado'

    pedido = models.ForeignKey(Pedido, on_delete=models.SET_DEFAULT, default=1, null=False)
    metodo_pagamento = models.ForeignKey(MetodoPagamento, on_delete=models.SET_DEFAULT, default=1, null=False)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(
        max_length=20,
        choices=StatusPagamento.choices,
        default=StatusPagamento.PENDENTE,
        null=False
    )

    class Meta:
        db_table = 'pagamentos'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return f"Pagamento #{self.id} - Pedido: {self.pedido.id}"


class Envio(models.Model):
    class MetodoEnvio(models.TextChoices):
            TRANSPORTADORA = 'Transportadora', 'Transportadora'
            CORREIOS = 'Correios', 'Correios'
            RETIRADA = 'Retirada', 'Retirada'

    pedido = models.ForeignKey(Pedido, on_delete=models.SET_DEFAULT, default=1, null=False)
    metodo_envio = models.CharField(
        max_length=20,
        choices=MetodoEnvio.choices,
        default=MetodoEnvio.TRANSPORTADORA,
        null=False
    )

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


class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_DEFAULT, default=1, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_DEFAULT, default=1, null=False)
    avaliacao = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(1, message="A avaliação deve ser entre 1 e 5"),
            MaxValueValidator(5, message="A avaliação deve ser entre 1 e 5")
        ]
    )
    comentario = models.TextField(blank=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        # Ensure a client can only review a product once
        unique_together = ['cliente', 'produto']

    def __str__(self):
        return f"Avaliação de {self.cliente.full_name()} para {self.produto.nome}"

    def clean(self):
        # Additional validation to ensure rating is between 1 and 5
        if self.avaliacao < 1 or self.avaliacao > 5:
            raise ValidationError({
                'avaliacao': 'A avaliação deve ser entre 1 e 5'
            })
