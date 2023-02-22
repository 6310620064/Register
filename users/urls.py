from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include("django.contrib.auth.urls")),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register' , view=views.register , name = 'register'),
]