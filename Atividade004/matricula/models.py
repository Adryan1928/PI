from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + "/" + self.estado

class Curso(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome