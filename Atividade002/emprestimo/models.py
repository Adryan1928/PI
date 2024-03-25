from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    categorias = models.ManyToManyField(Categoria)

class Avaliacao(models.Model):
    pontuacao = models.IntegerField()
    comentario = models.CharField(max_length=255)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

class Emprestimo(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
