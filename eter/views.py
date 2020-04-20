from django.shortcuts import render

def home( request ):
    render( request, 'eter/index.html' )