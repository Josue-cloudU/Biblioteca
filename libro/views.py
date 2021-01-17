from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import AutorForm, LibroForm
from .models import Autor, Libro

class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    login_url = "login"

class crearAutor(LoginRequiredMixin, generic.CreateView):
    template_name = "libro/crear_autor.html"
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "login"


class listarAutor(LoginRequiredMixin, generic.ListView):
    model = Autor
    template_name = "libro/listar_autor.html"
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True).order_by('id')
    login_url = "login"


class ActualizarAutor(LoginRequiredMixin, generic.UpdateView):
    model = Autor
    template_name = 'libro/actualizar_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "login"

#Eliminacion total del objeto autor sin plantilla
def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    # Recuperamos la instancia de la persona y la borramos
    instancia = Autor.objects.get(id = id)
    instancia.delete()#eliminacion total de labase de datos
    # Después redireccionamos de nuevo a la lista
    return redirect("libro:listar_autor")

#Eliminacion logia de las listas de autor sin plantillas
def eliminarAutor(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    autor = Autor.objects.get(id = id)
    autor.estado = False
    autor.save()
    return redirect("libro:listar_autor")

class ListarLibro(LoginRequiredMixin, generic.ListView):
    model = Libro
    template_name = "libro/listar_libro.html"
    context_object_name = 'libros'
    queryset = Libro.objects.filter(estado = True).order_by('id')
    login_url = "login"

class crearLibro(LoginRequiredMixin, generic.CreateView):
    template_name = "libro/crear_libro.html"
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")
    login_url = "login"

class ActualizarLibro(LoginRequiredMixin, generic.UpdateView):
    model = Libro
    template_name = 'libro/modal/modaleditl.html'
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")
    login_url = "login"

class deleteLibro(LoginRequiredMixin, generic.DeleteView):
    model = Libro
    template_name = 'libro/modal/modaleliml.html'
    success_url = reverse_lazy("libro:listar_libro")
    login_url = "login"

# #Eliminacion total del objeto libro sin plantilla
# def deleteLibro(request, id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     # Recuperamos la instancia de la persona y la borramos
#     instancia = Libro.objects.get(id = id)
#     instancia.delete()#eliminacion total de la base de datos
#     # Después redireccionamos de nuevo a la lista
#     return redirect("libro:listar_libro")

class eliminarLibro(LoginRequiredMixin, generic.DeleteView):
    model = Libro
    template_name = 'libro/modal/modalelimll.html'
    login_url = "login"

    def post(self,request,pk,*args,**kwargs):
        libro = Libro.objects.get(id = pk)
        libro.estado = False
        libro.save()
        return redirect("libro:listar_libro")

# #Eliminacion logia de las listas de libros sin plantilla
# def eliminarLibro(request, id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     libro = Libro.objects.get(id = id)
#     libro.estado = False
#     libro.save()
#     return redirect("libro:listar_libro")
