from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now

class Parceiro(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='parceiros/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Esporte(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='esportes/', blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clientes/', blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    nome = models.CharField(max_length=100)
    valor_sugerido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qr_code = models.ImageField(upload_to='doacoes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.valor_sugerido}"


class Socio(models.Model):

    nome = models.CharField(max_length=200)
    numero_socio = models.CharField(max_length=50)

    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)

    ativo = models.BooleanField(default=True)

    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )

    status_pagamento = models.CharField(
        max_length=10,
        choices=STATUS,
        default='Inativo'
    )

    investimento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    foto = models.ImageField(
        upload_to='fotos/',
        blank=True,
        null=True
    )

    data_cadastro = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):

        if not self.senha.startswith('pbkdf2'):
            self.senha = make_password(self.senha)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome



class HistoricoPagamento(models.Model):

    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    ano = models.IntegerField()

    jan = models.BooleanField(default=False)
    fev = models.BooleanField(default=False)
    mar = models.BooleanField(default=False)
    abr = models.BooleanField(default=False)
    mai = models.BooleanField(default=False)
    jun = models.BooleanField(default=False)
    jul = models.BooleanField(default=False)
    ago = models.BooleanField(default=False)
    set = models.BooleanField(default=False)
    out = models.BooleanField(default=False)
    nov = models.BooleanField(default=False)
    dez = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.socio.nome} - {self.ano}"



class Noticia(models.Model):

    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, null=True)

    imagem = models.ImageField(
        upload_to='noticias/',
        blank=True,
        null=True
    )

    data = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo



class Historia(models.Model):

    texto = models.TextField()

    def __str__(self):
        return "História"



class Diretoria(models.Model):

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    foto = models.ImageField(
        upload_to='diretoria/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome



class Evento(models.Model):

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)

    data = models.DateField()

    imagem = models.ImageField(
        upload_to='eventos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo



class Curso(models.Model):

    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)

    carga_horaria = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome