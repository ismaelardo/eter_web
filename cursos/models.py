from django.db import models

# Create your models here.

class Taller( models.Model ):
    titulo = models.CharField( max_length = 200 )
    fecha_inicio = models.DateTimeField()
    descripcion = models.TextField( max_length = 400 )

    def __str__( self ):
        return self.titulo


class Noticia( models.Model ):
    titulo = models.CharField( max_length = 200 )
    imagen = models.ImageField( upload_to='img_slider' )
    enlace = models.URLField()

    def __str__( self ):
        return self.titulo