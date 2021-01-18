from django.contrib import admin
from .models import Autor, Libro, Reservas

# actions para el admin site de el modelo autor
class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre','apellidos','nacionalidad')
    list_display = ('nombre','apellidos','nacionalidad','estado')
    actions = ['eliminacion_logica_autores', 'activacion_logica_autores']
    def eliminacion_logica_autores(self, request, queryset):
        for autor in queryset:
            autor.estado = False
            autor.save()

    def activacion_logica_autores(self, request, queryset):
        for autor in queryset:
            autor.estado = True
            autor.save()

    def get_actions(self,request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

# actions para el admin site de el modelo autor
class LibroAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'estado')
    list_display = ('titulo','fecha_publicacion', 'fecha_creacion','estado')
    actions = ['eliminacion_logica_libros', 'activacion_logica_libros']
    def eliminacion_logica_libros(self, request, queryset):
        for libro in queryset:
            libro.estado = False
            libro.save()

    def activacion_logica_libros(self, request, queryset):
        for libro in queryset:
            libro.estado = True
            libro.save()

    def get_actions(self,request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Reservas)
