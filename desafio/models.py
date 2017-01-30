from django.db import models


class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    # atributo como texto, pois o CPF pode comecar com 0
    cpf = models.CharField(max_length=11, unique=True)
    # assumindo 9 digitos para celular + 2 para DDD
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.cpf
