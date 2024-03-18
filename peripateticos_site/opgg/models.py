from django.db import models
# Create your models here.


class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    visualizacion = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.pk} - {self.nombre} {self.apellido}'
    # print(Autores)