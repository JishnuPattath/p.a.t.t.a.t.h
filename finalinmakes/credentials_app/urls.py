from django.urls import path
from . import views

app_name = 'credentials_app'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('courses/', views.courses, name='courses'),
    path('modules/', views.modules, name='modules')
    ]