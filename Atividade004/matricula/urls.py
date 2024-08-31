from django.urls import path
from .views import listar_alunos, cadastrar_aluno

app_name = 'matricula'

urlpatterns = [
    path('', listar_alunos, name='listar_alunos'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
]