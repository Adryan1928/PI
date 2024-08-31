from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {"alunos": alunos})

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('matricula:listar_alunos')
    else:
        form = AlunoForm()
        return render(request, 'cadastrar_aluno.html', {"form": form})