from django.db import models
# Create your models here.


""""
    Todas las tablas de una BD es un Modelo.
    Django - ORM - Object Related Manager

    Tabla Usuarios:
        pk = Autofield
        nombre
        apellido

    Usuario.nombre
    usuario.apellido

    1 - Crear el modelo
    2 - Crear la migracion - python manage.py makemigrations
    3 - Aplicar la migracion - python manage.py migrate


"""

class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    bandera = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.pk} - {self.nombre} {self.apellido}'
    # print(Autores)