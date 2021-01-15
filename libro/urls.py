from django.urls import path
from libro import views

urlpatterns = [
    # path('crear_autor/', views.crearAutor, name='crear_autor'),
    path('crear_autor/', views.crearAutor.as_view(), name='crear_autor'),
    # path('listar_autor/', views.listarAutor, name='listar_autor'),
    path('listar_autor/', views.listarAutor.as_view(), name='listar_autor'),
    # path('editar_autor/<int:id>', editarAutor, name='editar_autor'),
    path('actualizar_autor/<int:pk>', views.ActualizarAutor.as_view(), name='actualizar_autor'),
    # path('eliminar_autor/<int:id>', views.eliminarAutor, name='eliminar_autor'),
    path('delete_autor/<int:id>', views.delete, name='delete_autor'),

]
