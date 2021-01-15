from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
        # path('', login,{'template_name':'login.html'}, name='login' ),
        path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
        path('logout/', auth_views.LogoutView.as_view(template_name="login.html"), name="logout"),
        # path('signup/', views.Signup, name="signup"),
]