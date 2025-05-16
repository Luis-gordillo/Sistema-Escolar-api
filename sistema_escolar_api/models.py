from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Administradores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_admin = models.CharField(max_length=255,null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del admin "+self.first_name+" "+self.last_name
    
class Alumnos(models.Model):
    id = models.BigAutoField(primary_key=True)  # Clave primaria
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)  # Relación con el usuario
    matricula = models.CharField(max_length=255, null=True, blank=True)  # Matrícula del alumno
    fecha_nacimiento = models.DateField(null=True, blank=True)
    curp = models.CharField(max_length=18, null=True, blank=True)  # CURP
    rfc = models.CharField(max_length=13, null=True, blank=True)  # RFC
    edad = models.IntegerField(null=True, blank=True)  # Edad
    telefono = models.CharField(max_length=15, null=True, blank=True)  # Teléfono
    ocupacion = models.CharField(max_length=255, null=True, blank=True)  # Ocupación
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Fecha de creación
    update = models.DateTimeField(null=True, blank=True)  # Fecha de última actualización

    def __str__(self):
        return f"Perfil del alumno {self.first_name} {self.last_name} - Matrícula: {self.matricula}"

class Maestros(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    id_trabajador = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    cubiculo = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    area_investigacion = models.CharField(max_length=255,null=True, blank=True)
    materias_json = models.TextField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del maestro "+self.first_name+" "+self.last_name

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
    fecha_realizacion = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=300, blank=True)
    cupoAsistentes = models.PositiveIntegerField()
    programaEducativo = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    publico_objetivo = models.CharField(max_length=255)
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre