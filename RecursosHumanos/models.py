from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    tipo_documento = models.CharField(max_length=60)
    abreviatura = models.CharField(max_length=2)

class TipoContrato(models.Model):
    tipo_contrato = models.CharField(max_length=70)

class Cargo(models.Model):
    cargo = models.CharField(max_length=80)

class Area(models.Model):
    area = models.CharField(max_length=60)
class Empleado(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, null=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, null=True)
    documento = models.IntegerField(unique=True)
    estado = models.BooleanField(default=True)
    correo = models.EmailField(max_length=254, null=False, unique=True, default='Error@validation.com', blank=False)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)

class Contrato(models.Model):
    empleado = models.OneToOneField(Empleado, 
                                 on_delete=models.PROTECT,
                                 related_name='contratos',
                                 related_query_name='contrato'
                                 )
    salario = models.IntegerField()
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField(null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='cargos')
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, related_name='areas', null=True)
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.PROTECT)

class Novedades(models.Model):
    novedad = models.CharField(max_length=80)
    observaciones = models.TextField(null=True)
#intermediraria
class NovedadesEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='novedades_empleado')
    novedades = models.ForeignKey(Novedades, on_delete=models.PROTECT)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    fecha_creada = models.DateField(auto_now_add=True)
