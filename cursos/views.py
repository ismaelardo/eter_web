from django.shortcuts import render
from django.http import HttpResponse
from .models import Taller
# Create your views here.

def listadoDeCursos( request ):
    talleres = Taller.objects.all().order_by('-fecha_inicio')
    
    contexto = {
        'talleres' : talleres
    }
    return render( request, 'cursos/listadoCursos.html', contexto )

