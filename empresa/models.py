from django.db import models

# Create your models here.
class Navbar(models.Model):
    id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

class Empresa(models.Model):
    rut              = models.CharField(primary_key=True, max_length=13)
    nombre           = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=100)
    fecha_constitucion = models.DateField(blank=False, null=False)  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

class Servicio(models.Model):
    id_servicio         = models.AutoField(db_column="idServicio", primary_key=True)
    nombre_servicio     = models.CharField(max_length=50)
    descripcion         = models.CharField(max_length=500)


class Trabajador(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    fecha_ingreso = models.DateField(blank=False, null=False) 
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()