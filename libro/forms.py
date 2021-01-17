from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellidos', 'nacionalidad', 'descripcion', 'estado')
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre o nombres del autor'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellido o apellidos del autor'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nacionalidad del autor'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'rows': 8,
                    'placeholder': 'Informacion adicional de autor'
                }
            )
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'fecha_publicacion', 'autor_id', 'estado')
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Titulo del libro'
                }
            ),
            'fecha_publicacion': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'yyyy-mm-dd'
                }
            )
        }
