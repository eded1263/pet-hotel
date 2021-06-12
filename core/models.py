from django.db import models


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    end1 = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    fone = models.CharField(max_length=14, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_clientes', blank=True, null=True)

    def __str__(self):
        return self.nome + '(' + str(self.id) + ')'


class Meta:
    verbose_name_plural = 'Clientes'


class Pet(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100, blank=True, null=True)
    idade = models.CharField(max_length=50, blank=True, null=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_clientes', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} ({self.raca})'

    class Meta:
        verbose_name_plural = 'Pets'


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome} ({self.descricao})'

    class Meta:
        verbose_name_plural = 'Planos'

