from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"Nombre del curso: {self.nombre} - Nombre de comision: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"Nombre del estudiante: {self.nombre} - Apellido del alumno: {self.apellido} - Email del alumno: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"Nombre del profesor: {self.nombre} - Apellido del profesor: {self.apellido} - Email del profesor: {self.email} - Profesion del profesor: {self.profesion}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str:
        return f"Nombre del entregable: {self.nombre} - Fecha del entregable: {self.fecha_de_entrega} - Entregado: {self.entregado}"
    
