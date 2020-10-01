from django.urls import path
from django.contrib.auth import views as auth_views

from principal import views

urlpatterns = [
    # The home page
    path('', views.Index, name='Index'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    #path('registro', views.registro, name='registro'),
    #path('login',auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    #path('logout',auth_views.LogoutView.as_view(template_name='login/login.html'), name='logout'),
    
]