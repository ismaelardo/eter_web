from django.shortcuts import render
from django.http import HttpResponse
from .models import Taller, Noticia
# Create your views here.

def listadoDeCursos( request ):
    talleres = Taller.objects.all().order_by('-fecha_inicio')  
    contexto = {
        'talleres' : talleres
    }
    return render( request, 'cursos/listadoCursos.html', contexto )

def formularioContacto( request ):
    return render( request, 'cursos/formularioContacto.html' )

def homeView( request ):
    noticias = Noticia.objects.all()
    contexto = {
        'noticias': noticias
    }
    return render( request, 'cursos/home.html', contexto )

