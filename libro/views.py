from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import AutorForm, LibroForm
from .models import Autor, Libro, Reservas
from django.contrib.auth.models import User
# mixin personalizado
class AdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:#si el usuario es administrador/staff
            return super().dispatch(request,*args, **kwargs)#lo deja continuar
        return redirect('index')#de lo contrario lo redirecciona al index


class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"
    login_url = "login"

class crearAutor(LoginRequiredMixin, AdminMixin, generic.CreateView):
    template_name = "libro/crear_autor.html"
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "login"


class listarAutor(LoginRequiredMixin, AdminMixin, generic.ListView):
    model = Autor
    template_name = "libro/listar_autor.html"
    context_object_name = 'autores'
    queryset = Autor.objects.all().order_by('id')
    login_url = "login"


class ActualizarAutor(LoginRequiredMixin, AdminMixin, generic.UpdateView):
    model = Autor
    template_name = 'libro/modal/modaledita.html'
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "login"

class delete(LoginRequiredMixin, AdminMixin, generic.DeleteView):
    model = Autor
    template_name = 'libro/modal/modalelima.html'
    success_url = reverse_lazy("libro:listar_autor")
    login_url = "login"

# #Eliminacion total del objeto autor sin plantilla
# def delete(request, id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     # Recuperamos la instancia de la persona y la borramos
#     instancia = Autor.objects.get(id = id)
#     instancia.delete()#eliminacion total de labase de datos
#     # Después redireccionamos de nuevo a la lista
#     return redirect("libro:listar_autor")

class eliminarAutor(LoginRequiredMixin, AdminMixin, generic.DeleteView):
    model = Autor
    template_name = 'libro/modal/modalelimal.html'
    login_url = "login"

    def post(self,request,pk,*args,**kwargs):
        autor = Autor.objects.get(id = pk)
        autor.estado = False
        autor.save()
        return redirect("libro:listar_autor")

# #Eliminacion logia de las listas de autor sin plantillas
# def eliminarAutor(request, id):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     autor = Autor.objects.get(id = id)
#     autor.estado = False
#     autor.save()
#     return redirect("libro:listar_autor")

class ListarLibro(LoginRequiredMixin, AdminMixin, generic.ListView):
    model = Libro
    template_name = "libro/listar_libro.html"
    context_object_name = 'libros'
    queryset = Libro.objects.all().order_by('id')
    login_url = "login"

class crearLibro(LoginRequiredMixin, AdminMixin, generic.CreateView):
    template_name = "libro/crear_libro.html"
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")
    login_url = "login"

class ActualizarLibro(LoginRequiredMixin, AdminMixin, generic.UpdateView):
    model = Libro
    template_name = 'libro/modal/modaleditl.html'
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")
    login_url = "login"

class deleteLibro(LoginRequiredMixin, AdminMixin, generic.DeleteView):
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

class eliminarLibro(LoginRequiredMixin, AdminMixin, generic.DeleteView):
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

# seccion para vistas de los usuarios normales ------------------------------------------------------------------------
class listarlibrosdisponibles(LoginRequiredMixin, generic.ListView):
    model = Libro
    template_name = "libro/listar_libro_disponibles.html"
    context_object_name = 'libros'
    queryset = Libro.objects.filter(estado = True, cantidad__gte = 1).order_by('id')
    login_url = "login"

class libroDetailView(LoginRequiredMixin, generic.DetailView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro_detail.html'
    login_url = "login"

    def get(self, request, *args, **kwargs):
        if self.get_object().cantidad > 0:
            return render(request, self.template_name, 'object':self.get_object())

class registrarReserva(LoginRequiredMixin, generic.CreateView):
    model = Reservas
    success_url = reverse_lazy("libro:listar_libro_disponibles")

    def post(self,request,pk,*args,**kwargs):
        if request.method == 'POST':
            libro = Libro.objects.get(id = pk)
            user = User.objects.get(id = request.user.id)
            if libro and user:
                nueva_reserva = self.model(
                     libro = libro,
                     user = user
                )
                nueva_reserva.save()
                print(request.POST)#pruebas de verificacion de datos en consola
                print(libro, user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
