from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('user_list/', views.ListadoUsuarios.as_view(), name='listar_usuarios'),
    path('user_list_admin/', views.ListadoUsuariosS.as_view(), name='listar_usuarioss'),
    path('user_list_ban/', views.ListadoUsuariosB.as_view(), name='listar_usuariosb'),
    path('user_registerstaff/', views.RegistrarUsuarioS.as_view(), name="registerstaff"),
    path('user_ban/<int:pk>', views.banearUsuario.as_view(), name="userban"),
    path('user_delete/<int:pk>', views.delete.as_view(), name="user_delete"),
    path('user_update/<int:pk>', views.ActualizarUsuario.as_view(), name="user_update"),
    path('user_detail/<int:pk>', views.DetailUsuario.as_view(), name="user_detail"),
]
