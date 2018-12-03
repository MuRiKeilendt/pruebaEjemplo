from django.db import models

# Create your models here.
class EstadoCivil(models.Model):
    nombre=models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre=models.CharField(max_length=45)
    edad=models.IntegerField()
    sexo=models.CharField(max_length=1)
    estadoCivil=models.ForeignKey(EstadoCivil,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
