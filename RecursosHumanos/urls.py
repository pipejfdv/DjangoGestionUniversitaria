from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home)
    #ruta con parametros
    #path('home/<str:nombre>/<int:edad>', views.home)
]
