from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserForm, CustomUserStaffForm
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # #autenticar al usuario y redirigirlo al inicio
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('index')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

class RegistrarUsuarioS(LoginRequiredMixin, generic.CreateView):
    model = User
    form_class = CustomUserStaffForm
    template_name = 'accounts/registerstaff.html'
    success_url = reverse_lazy("accounts:listar_usuarios")
    login_url = "login"

class ListadoUsuarios(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'accounts/listar_usuarios.html'
    login_url = "login"

    def get_queryset(self):
        return User.objects.filter(is_active = True).order_by('id')

# def ListadoUsuarios(request):
#     return render(request,'accounts/listar_usuarios.html',{'users': User.objects.all()})
#     # return render(self.model.objects.filter(is_active = True))
