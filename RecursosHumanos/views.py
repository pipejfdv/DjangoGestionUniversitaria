from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.db import IntegrityError
import datetime
from . import models
# Create your views here.
def home(request):
    return render(request, 'Index.html')
    
def inicio(request):
    data = models.Empleado.objects.all()
    areas = models.Area.objects.all()
    cargos = models.Cargo.objects.all()
    tipo_contrato = models.TipoContrato.objects.all()
    return render(request, 'paginas/inicio.html', {'empleados': data, 'areas': areas, 'cargos': cargos, 'tipos_contrato': tipo_contrato})

def eliminar_empleado(request, empleado_id):
    try:
        lista_empleados = models.Empleado.objects.all()
        data = models.Empleado.objects.get(id=empleado_id).delete()
    except models.Empleado.DoesNotExist:
        data = None
    return render(request, 'paginas/inicio.html', {'empleado': data,
                                                            'empleados': lista_empleados})
def editar_empleado(request, empleado_id):
    empleado = models.Empleado.objects.get(id=empleado_id)
    areas = models.Area.objects.all()
    cargos = models.Cargo.objects.all()
    documentos = models.TipoDocumento.objects.all()
    tipo_contrato = models.TipoContrato.objects.all()
    return render(request, 'paginas/editar_empleado.html', {'empleado': empleado, 'areas': areas, 'cargos': cargos, 'tipos_contrato': tipo_contrato, 'documentos': documentos})

def actualizar_empleado(request, empleado_id):
    empleado = models.Empleado.objects.get(id=empleado_id)
    contrato = empleado.contratos
    if request.method == 'POST':
        empleado.primer_nombre = request.POST.get('primer_nombre')
        empleado.segundo_nombre = request.POST.get('segundo_nombre')
        empleado.primer_apellido = request.POST.get('primer_apellido')
        empleado.segundo_apellido = request.POST.get('segundo_apellido')
        empleado.correo = request.POST.get('correo')

        contrato.salario = request.POST.get('salario')
        contrato.cargo_id = request.POST.get('cargo')
        contrato.area_id = request.POST.get('area')
        contrato.tipo_contrato_id = request.POST.get('tipo_contrato')

        fecha_ingreso = request.POST.get('fecha_ingreso')
        contrato.fecha_ingreso = datetime.datetime.strptime(
            fecha_ingreso, '%Y-%m-%d'
        ).date()

        fecha_retiro = request.POST.get('fecha_retiro')
        if fecha_retiro:
            contrato.fecha_retiro = datetime.datetime.strptime(
                fecha_retiro, '%Y-%m-%d'
            ).date()
        else:
            contrato.fecha_retiro = None

        if contrato.fecha_retiro == None:
            empleado.estado = True
        else:
            empleado.estado = False
        contrato.save()
        empleado.save()
        return redirect('inicio')

def crear_empleado(request):
    if request.method == 'POST':
        documento_id = request.POST['tipo_documento']
        tipo = models.TipoDocumento.objects.get(id=documento_id)        
        fecha_ingreso = datetime.datetime.strptime(request.POST['fecha_ingreso'], '%Y-%m-%d').date()
        
        models.Empleado.objects.create(
            primer_nombre=request.POST['primer_nombre'],
            segundo_nombre=request.POST['segundo_nombre'],
            primer_apellido=request.POST['primer_apellido'],
            segundo_apellido=request.POST['segundo_apellido'],
            correo=request.POST['correo'],
            documento=request.POST['documento'],
            tipo_documento=tipo,
        )
        models.Contrato.objects.create(
            empleado=models.Empleado.objects.get(documento=request.POST['documento']),
            salario=request.POST['salario'],
            fecha_ingreso=fecha_ingreso,
            cargo=models.Cargo.objects.get(id=request.POST['cargo']),
            area=models.Area.objects.get(id=request.POST['area']),
            tipo_contrato=models.TipoContrato.objects.get(id=request.POST['tipo_contrato'])
        )
        return redirect('inicio')

    