# Generated by Django 5.0.2 on 2024-03-02 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opgg', '0002_autores_bandera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autores',
            old_name='bandera',
            new_name='visualizacion',
        ),
    ]
