# -*- coding: utf-8 -*-
from django.db import models

class Profesor(models.Model):
	nombre = models.CharField(max_length = 70)
	def __unicode__(self):
		return self.nombre

class Curso(models.Model):
	nombre = models.CharField(max_length = 70)
	ciclo = models.IntegerField()
	profesores = models.ManyToManyField(Profesor, through='Dictado')
	def __unicode__(self):
		return self.nombre

class Dictado(models.Model):
	curso = models.ForeignKey(Curso)
	profesor = models.ForeignKey(Profesor)
	semestre = IntegerField() #El de 5 digitos : 20142
	def __unicode__(self):
		return self.curso+" - "+self.profesor+" - "+self.semestre

#class CursoDictado(models.Model):
#	nombre = models.CharField(max_length = 70)
#	ciclo = models.IntegerField() #Cuidado debe tener 5 digitos <ano><semestre>
#	profesores = models.ManyToManyField(Profesor)
#
#	def __unicode__(self):
#		return self.nombre

class Estudiante(models.Model):
	nombre = models.CharField(max_length = 70)
	#Codigo?
	escuela = models.CharField(max_length = 70) #Podría ser solo SW o S

	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
	contenido = models.CharField(max_length = 1000)
	cursoDictado = models.ForeignKey(Dictado)
	autor = models.ForeignKey(Estudiante)  
	fecha = models.DateTimeField('Fecha de comentario')

	def __unicode__(self):
		return self.autor+" - "+self.fecha
