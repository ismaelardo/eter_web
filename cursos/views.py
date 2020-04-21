from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Taller, Noticia
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def listadoDeCursos( request ):
    talleres = Taller.objects.all().order_by('-fecha_inicio')  
    contexto = {
        'talleres' : talleres
    }
    return render( request, 'cursos/listadoCursos.html', contexto )

def formularioContacto( request ):
    if request.method == 'POST':
        autor = request.POST['Nombre']
        correo = request.POST['Email']
        mensaje = request.POST['Mensaje']
        mensaje = "Nombre: " + autor + " Correo: " + correo + " Mensaje: " + mensaje

        send_mail( 
            autor + ' Formulario de contacto', 
            mensaje, 
            settings.EMAIL_HOST_USER, 
            ['escuelaether@gmail.com'], 
            fail_silently = False )
        
        messages.success( request, 'Mensaje recibido, te responderemos a la brevedad!' )
        return redirect( '../../' )

    return render( request, 'cursos/formularioContacto.html' )

def homeView( request ):
    noticias = Noticia.objects.all()
    contexto = {
        'noticias': noticias
    }
    return render( request, 'cursos/home.html', contexto )

