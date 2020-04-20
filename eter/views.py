from django.shortcuts import render, HttpResponse

def home( request ):
    HttpResponse("Hola")
    #render( request, 'eter/index.html' )