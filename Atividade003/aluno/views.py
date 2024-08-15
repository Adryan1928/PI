from django.shortcuts import render
from .models import aluno

def index(request):
    alunos = aluno.objects.all()

    return render(request, 'index.html', {
        "alunos": alunos
    })
