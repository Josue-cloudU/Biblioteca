from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres', max_length =200, blank = False, null=False)
    apellidos = models.CharField('Apelidos', max_length =220, blank = False, null=False)
    nacionalidad= models.CharField('Nacionalidad', max_length =100, blank = False, null=False)
    descripcion = models.CharField('Descripcion', max_length = 200, blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha_creacion', auto_now = True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre#muestra el nombre del objeto tal como fue creado

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 200, blank = False, null= False)
    fecha_publicacion = models.DateField('Fecha de publicacion', blank = False, null = False)
    descripcion = models.TextField('Description', null = True, blank = True)
    cantidad = models.IntegerField('Cantidad o Stock', default = 1)
    imagen = models.ImageField('Imagen', upload_to='libros/', max_length=255, null = True, blank = True)
    autor_id = models.ManyToManyField(Autor)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha_creacion', auto_now = True, auto_now_add=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Reservas(models.Model):
    id = models.AutoField(primary_key = True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad_dias = models.IntegerField('Cantidad de dias a reservar',default = 7)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_vencimiento = models.DateField('Fecha de vencimiento de la reserva', auto_now=False, auto_now_add=False, null = True, blank = True)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva de Libro {self.libro} por {self.user}'

# signal para reducir la cantidad del libro cuando hay una reserva
def reducir_cantidad_libro(sender, instance, **kwargs):
    libro = instance.libro
    if libro.cantidad > 0:
        libro.cantidad = libro.cantidad - 1
        libro.save()

# para que no se pueda realizar reservas desde el admin cuando no hay libros disponibles
def validar_creacion_reserva(sender, instance, **kwargs):
    libro = instance.libro
    if libro.cantidad < 1:
        raise Exception ("No se puede reservar ya que no hay libros disponibles")

post_save.connect(reducir_cantidad_libro, sender = Reservas)
pre_save.connect(validar_creacion_reserva, sender = Reservas)
