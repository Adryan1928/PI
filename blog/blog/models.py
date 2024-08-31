from django.db import models

class RedeSocial(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()
    nome_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_final = models.DateField(null=True, blank=True)
    logo = models.ImageField(upload_to='cursos/logos')

    def __str__(self):
        return self.nome