from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import CustomUserForm
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

class ListadoUsuarios(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'accounts/listar_usuarios.html'
    queryset = User.objects.filter(is_active = True).order_by('id')
    login_url = "login"
