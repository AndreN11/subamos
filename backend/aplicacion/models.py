from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 nombre = models.CharField(max_length=50)
 apellido = models.CharField(max_length=50)
 correo = models.CharField(max_length=50)
 fecha_nacimiento = models.DateField()
 perfil = models.TextField(max_length=500, blank=True)

class Categoria(models.Model):
  nombrecategoria = models.TextField(max_length=500, blank=True)

class Cliente(models.Model):
  nombrecategoria = models.TextField(max_length=500, blank=True)


