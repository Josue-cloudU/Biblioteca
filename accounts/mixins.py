from django.shortcuts import redirect

#mixin personalizado
class AdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:#si el usuario es administrador/staff
            return super().dispatch(request,*args, **kwargs)#lo deja continuar
        return redirect('index')#de lo contrario lo redirecciona al index
