from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
	# ej: /canvan/ 
    path ( '', views.listadoDeCursos, name='lista-cursos' ),
]