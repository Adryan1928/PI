from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
