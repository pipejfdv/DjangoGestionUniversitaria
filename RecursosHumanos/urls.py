from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('lista-empleados/', views.lista_empleados, name='empleados'),
    path('empleado/<str:empleado_id>/', views.empleado, name='empleado'),
]
