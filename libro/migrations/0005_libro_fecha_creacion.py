# Generated by Django 3.1.5 on 2021-01-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_libro_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha_creacion'),
        ),
    ]
