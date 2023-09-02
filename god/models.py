from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length= 20)
    autor = models.CharField(max_length=12)

class Clientes(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.IntegerField()
