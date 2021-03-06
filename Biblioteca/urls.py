"""Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from libro.views import Index
from accounts.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include(('libro.urls', 'libro'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('', Index.as_view(), name="index"),

    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/login.html"), name="logout"),
    path('user_register/', Register, name="register"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name="reset_password"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

# serve servidor para mostrar las imagenes en el navegador cuando sea necesario
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
