from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('listar_usuarios/', views.ListadoUsuarios.as_view(), name='listar_usuarios'),
]
