from django.contrib import admin
from . import models

admin.site.register(models.Avaliacao)
admin.site.register(models.Emprestimo)
admin.site.register(models.Livro)
admin.site.register(models.Usuario)
admin.site.register(models.Categoria)