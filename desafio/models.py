from django.db import models


class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    # atributo como texto, pois o CPF pode comecar com 0
    cpf = models.CharField(max_length=11, unique=True)
    # assumindo 9 digitos para celular + 2 para DDD
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome + " (" + self.cpf + ")"


class Teleconsultor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50)
    # nao esta descrito no PDF, mas em principio cada CRM
    # pode pertencer somente a um Teleconsultor
    crm = models.IntegerField(unique=True)
    data_formatura = models.DateField()

    def __str__(self):
        return self.nome + " (" + str(self.crm) + ")"


class Solicitacao(models.Model):
    texto = models.CharField(max_length=1000)
    data = models.DateField()
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    teleconsultor = models.ForeignKey(Teleconsultor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('solicitante', 'data',)

    def __str__(self):
        return self.solicitante.nome + " - " + str(self.data)
