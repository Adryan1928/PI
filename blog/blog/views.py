from django.shortcuts import render
from .models import Curso, RedeSocial

def blog(request):
    redes_sociais = RedeSocial.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'blog.html', {'redes_sociais': redes_sociais, "cursos": cursos})
