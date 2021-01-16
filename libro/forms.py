from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellidos', 'nacionalidad', 'descripcion')

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'fecha_publicacion', 'autor_id')
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
