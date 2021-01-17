from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import CustomUserForm, CustomUserStaffForm
# Create your views here.

# registrar usuarios desde login
def Register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # #autenticar al usuario y redirigirlo al inicio
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_passwyyord)
            # login(request, user)
            return redirect('index')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

# registrar usuarios con posibilidad de ser staff
class RegistrarUsuarioS(LoginRequiredMixin, generic.CreateView):
    model = User
    form_class = CustomUserStaffForm
    template_name = 'accounts/registerstaff.html'
    success_url = reverse_lazy("accounts:listar_usuarios")
    login_url = "login"

# listar usuarios no baneados y no staff
class ListadoUsuarios(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'accounts/listar_usuarios.html'
    login_url = "login"

    def get_queryset(self):
        return User.objects.filter(is_active = True, is_staff = False).order_by('id')

# def ListadoUsuarios(request):
#     return render(request,'accounts/listar_usuarios.html',{'users': User.objects.all()})
#     # return render(self.model.objects.filter(is_active = True))

# listar usuarios staff
class ListadoUsuariosS(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'accounts/listar_usuarios.html'
    login_url = "login"

    def get_queryset(self):
        return User.objects.filter(is_active = True, is_staff = True).order_by('id')

# listar usuarios baneados
class ListadoUsuariosB(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'accounts/listar_usuarios.html'
    login_url = "login"

    def get_queryset(self):
        return User.objects.filter(is_active = False).order_by('id')

# banear usuarios
class banearUsuario(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'accounts/modal/userban.html'
    login_url = "login"

    def post(self,request,pk,*args,**kwargs):
        object = User.objects.get(id = pk)
        object.is_active = False
        object.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# eliminar usuarios
class delete(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'accounts/modal/userelim.html'
    login_url = "login"

    def post(self,request,pk,*args,**kwargs):
        object = User.objects.get(id = pk)
        object.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
