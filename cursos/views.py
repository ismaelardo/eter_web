from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def listadoDeCursos( request ):
    return render( request, 'cursos/listadoCursos.html' )

