from django.urls import path
from libro import views

urlpatterns = [
    # urls autor
    path('crear_autor/', views.crearAutor.as_view(), name='crear_autor'),
    path('listar_autor/', views.listarAutor.as_view(), name='listar_autor'),
    path('actualizar_autor/<int:pk>/', views.ActualizarAutor.as_view(), name='actualizar_autor'),
    path('delete_autor/<int:pk>/', views.delete.as_view(), name='delete_autor'),
    path('eliminar_autor/<int:pk>/', views.eliminarAutor.as_view(), name='eliminar_autor'),
    # urls libros
    path('listar_libro/', views.ListarLibro.as_view(), name='listar_libro'),
    path('crear_libro/', views.crearLibro.as_view(), name='crear_libro'),
    path('actualizar_libro/<int:pk>/', views.ActualizarLibro.as_view(), name='actualizar_Libro'),
    path('delete_libro/<int:pk>/', views.deleteLibro.as_view(), name='delete_libro'),
    path('eliminar_libro/<int:pk>/', views.eliminarLibro.as_view(), name='eliminar_libro'),
    # urls para usuarios generales y con gion para que en los navegadores se interprete como url amigable
    path('listar-libro-disponibles/', views.listarlibrosdisponibles.as_view(), name='listar_libro_disponibles'),
    path('detalles-libro/<int:pk>/', views.libroDetailView.as_view(), name='detalle_libro'),
    path('reservar-libro/<int:pk>/', views.registrarReserva.as_view(), name='reserva_libro'),
]
