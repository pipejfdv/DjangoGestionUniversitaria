from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def home(request):
    return render(request, 'Index.html')
    
def lista_empleados(request):
    try:
        data = models.Empleado.objects.all()
    except:
        data = None
    return render(request, 'paginas/lista-empleados.html', {'empleados': data})

def empleado(request, empleado_id):
    try:
        lista_empleados = models.Empleado.objects.all()
        data = models.Empleado.objects.get(id=empleado_id)
    except models.Empleado.DoesNotExist:
        data = None
    return render(request, 'paginas/lista-empleados.html', {'empleado': data,
                                                            'empleados': lista_empleados})


