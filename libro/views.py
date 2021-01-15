from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import AutorForm
from .models import Autor

# Create your views here.
# def Home(request):
#     return render(request, 'index.html')

class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    login_url = "accounts/login"

# def crearAutor(request):
#     if request.method == 'POST':
#         autor_form = AutorForm(request.POST)
#         if autor_form.is_valid():
#             autor_form.save()
#             return redirect('libro:listar_autor')
#     else:
#         autor_form = AutorForm()
#         print(autor_form)
#     return render(request, 'libro/crear_autor.html',{'autor_form':autor_form})

class crearAutor(LoginRequiredMixin, generic.CreateView):
    template_name = "libro/crear_autor.html"
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")

# def listarAutor(request):
#     autores = Autor.objects.all()
#     return render(request, 'libro/listar_autor.html', {'autores':autores})

class listarAutor(LoginRequiredMixin, generic.ListView):
    model = Autor
    template_name = "libro/listar_autor.html"
    context_object_name = 'autores'
    queryset = Autor.objects.all().order_by('id')


# def editarAutor(request, id):
#     autor_form = None
#     error = None
#     try:
#         autor = Autor.objects.get(id = id)
#         if request.method == 'GET':
#             autor_form = AutorForm(instance = autor)
#         else:
#             autor_form = AutorForm(request.POST, instance = autor)
#             if autor_form.is_valid():
#                 autor_form.save()
#             return redirect('libro:listar_autor')
#     except ObjectDoesNotExist as e:
#         error = e
#
#     return render(request, 'libro/crear_autor.html', {'autor_form':autor_form, 'error':error})

class ActualizarAutor(LoginRequiredMixin, generic.UpdateView):
    model = Autor
    template_name = 'libro/actualizar_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")

# def eliminarAutor(request, id):
#     autor = Autor.objects.get(id = id)
#     if request.method == 'POST':
#         autor.delete()
#         return redirect('libro:listar_autor')
#     return render(request, 'libro/eliminar_autor.html', {'autor':autor})

def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    # Recuperamos la instancia de la persona y la borramos
    instancia = Autor.objects.get(id = id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect("libro:listar_autor")
