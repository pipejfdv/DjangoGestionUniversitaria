from django.db import models
import uuid

# Create your models here.
class Empleado(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    estado = models.BooleanField()
class Contrato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    empleado = models.OneToOneField(Empleado, 
                                 on_delete=models.PROTECT,
                                 related_name='contratos',
                                 related_query_name='contrato'
                                 )
    salario = models.IntegerField()
    cargo = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField()
    tipo_contrato = models.CharField(max_length=50)
class Asistencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    empleado = models.ForeignKey(Empleado, 
                                 on_delete=models.CASCADE,
                                 related_name='asistencias',
                                 related_query_name='asistencia'
                                 )
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

class Nomina(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    empleado = models.OneToOneField(Empleado, 
                                 on_delete=models.CASCADE,
                                 related_name='nominas',
                                 related_query_name='nomina'
                                 )
    hora_extra = models.IntegerField()
    horas_trabajadas = models.IntegerField()