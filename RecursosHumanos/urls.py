from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('editar_empleado/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/<int:empleado_id>/', views.eliminar_empleado, name='empleado'),
]
