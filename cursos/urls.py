from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
	# ej: /cursos/ 
    path ( '', views.listadoDeCursos, name='lista-cursos' ),
    path ( 'contacto/', views.formularioContacto, name='formulario-contacto'),
]