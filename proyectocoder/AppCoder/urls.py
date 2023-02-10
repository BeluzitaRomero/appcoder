from django.urls import path, include
from AppCoder import views

#tambien podria hacer from .views import *
# y en el path('inicio/', inicio)
# y en el path('cursos', cursos)
#sin usar views.



urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('cursos/',views.cursos,name= 'cursos'),
    path('profesores/', views.profesores, name= 'profesores'),
    path('estudiantes/', views.estudiantes, name= 'estudiantes'),
    path('entregables/', views.entregables, name= 'entregables'),
]
