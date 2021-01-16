from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import AutorForm
from .models import Autor

class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    login_url = "accounts/login"

class crearAutor(LoginRequiredMixin, generic.CreateView):
    template_name = "libro/crear_autor.html"
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "accounts/login"


class listarAutor(LoginRequiredMixin, generic.ListView):
    model = Autor
    template_name = "libro/listar_autor.html"
    context_object_name = 'autores'
    queryset = Autor.objects.all().order_by('id')
    login_url = "accounts/login"


class ActualizarAutor(LoginRequiredMixin, generic.UpdateView):
    model = Autor
    template_name = 'libro/actualizar_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "accounts/login"



def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    # Recuperamos la instancia de la persona y la borramos
    instancia = Autor.objects.get(id = id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect("libro:listar_autor")
