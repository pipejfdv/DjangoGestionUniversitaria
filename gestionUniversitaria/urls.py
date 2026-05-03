from django.contrib import admin
from django.urls import path, include
#ruta para llamar los views de los demás modulos
#from RecursosHumanos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #manera en la se incluyen todas las rutas de los demás modulos
    path('rrhh/', include('RecursosHumanos.urls')),
    path('contabilidad/', include('Contabilidad.urls')),
]
