from django.db import models

class Profesor(models.Model):
	nombre = models.CharField(max_length = 70)

class CursoDictado(models.Model):
	nombre = models.CharField(max_length = 70)
	ciclo = models.IntegerField() #Cuidado debe tener 5 digitos <año><semestre>
	profesor = models.ManyToManyField(Profesor)

class Estudiante(models.Model):
	nombre = models.CharField(max_length = 70)
	escuela = models.CharField(max_length = 70) #Podría ser solo SW o S

class Comentario(models.Model):
	contenido = models.CharField(max_length = 1000)
	curso = models.ForeignKey(CursoDictado)
	autor = models.ForeignKey(Estudiante)  


