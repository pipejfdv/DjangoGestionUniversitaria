from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import redirect
from xhtml2pdf import pisa
from django.template.loader import get_template
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

def areas(request):
    data = models.Empleado.objects.all()
    documento = models.TipoDocumento.objects.all()
    cargos = models.Cargo.objects.all()
    tipo_contrato = models.TipoContrato.objects.all()
    areas = models.Area.objects.annotate(total_empleados=Count('areas__empleado'))
    return render(request, 'paginas/areas_trabajo.html', {'areas': areas , 'empleados': data, 'documentos': documento, 'cargos': cargos, 'tipos_contrato': tipo_contrato})

def editar_area(request, area_id):
    area = models.Area.objects.get(id=area_id)
    if request.method == 'POST':
        area.area = request.POST.get('area')
        area.save()
        return redirect('areas')

def agregar_area(request):
    if request.method == 'POST':
        models.Area.objects.create(area=request.POST['area'])
        return redirect('areas')
def eliminar_area(request, area_id):
    area = models.Area.objects.get(id=area_id)
    area.delete()
    return redirect('areas')

#novedades
def novedades(request, empleado_id):
    empleado = models.Empleado.objects.get(id=empleado_id)
    novedades_empleado = empleado.novedades_empleado.all()
    documento = models.TipoDocumento.objects.all()
    cargos = models.Cargo.objects.all()
    tipo_contrato = models.TipoContrato.objects.all()
    areas = models.Area.objects.all()
    novedades = models.Novedades.objects.all()
    return render(request, 'paginas/novedades.html', {'novedades_empleado': novedades_empleado, 
                                                      'empleado': empleado, 
                                                      'novedades': novedades,
                                                      'documentos': documento,
                                                      'cargos': cargos,
                                                      'tipos_contrato': tipo_contrato,
                                                      'areas': areas})

def agregar_novedad(request):
    if request.method == 'POST':
        fecha_inicial = datetime.datetime.strptime(request.POST['fecha_inicial'], '%Y-%m-%d').date()
        duracion = int(request.POST['dias_duracion'])
        duracion = datetime.timedelta(days=duracion)
        fecha_final = fecha_inicial + duracion
        models.NovedadesEmpleado.objects.create(
            empleado=models.Empleado.objects.get(id=request.POST['empleado']),
            novedades=models.Novedades.objects.get(id=request.POST['novedad']),
            fecha_inicial=fecha_inicial,
            fecha_final=fecha_final
        )
        return redirect('novedades', empleado_id=request.POST['empleado'])
    
def certificado_laboral(request, empleado_id):
    empleado = models.Empleado.objects.get(id=empleado_id)
    contrato = empleado.contratos
    hoy = datetime.date.today()

    template = get_template('documentos/certificado_laboral.html')
    html = template.render({'empleado': empleado, 
                            'contrato': contrato, 
                            'hoy': hoy})
    respuesta = HttpResponse(content_type='application/pdf')
    respuesta['Content-Disposition'] = 'attachment; filename="certificado_laboral.pdf"'
    pisa.CreatePDF(html, dest=respuesta)
    return respuesta