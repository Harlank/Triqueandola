# -*- coding: utf-8 -*-
from django.db import models

class Profesor(models.Model):
	nombre = models.CharField(max_length = 70)
	exigenciaP = models.DecimalField(max_digits=4,decimal_places=2,null=True)#Why null true :(
	pedagogiaP = models.DecimalField(max_digits=4,decimal_places=2,null=True)
	conocimientoP = models.DecimalField(max_digits=4,decimal_places=2,null=True)
	pasabilidadP = models.DecimalField(max_digits=4,decimal_places=2,null=True)
	#Comin soon : to be continued
	def __unicode__(self):
		return self.nombre

class Curso(models.Model):
	nombre = models.CharField(max_length = 70)
	ciclo = models.IntegerField()
	escuela = models.CharField(max_length = 20,null=True)
	profesores = models.ManyToManyField(Profesor, through='Dictado')
	def __unicode__(self):
		return self.nombre

class Dictado(models.Model):
	curso = models.ForeignKey(Curso)
	profesor = models.ForeignKey(Profesor)
	semestre = models.IntegerField() #El de 5 digitos : 20142

	exigenciaP = models.DecimalField(max_digits=4,decimal_places=2,null=True)
	pedagogiaP = models.DecimalField(max_digits=4,decimal_places=2,null=True)
	conocimientoP = models.DecimalField(max_digits=4,decimal_places=2,null=True)	
	pasabilidadP = models.DecimalField(max_digits=4,decimal_places=2,null=True)

	def __unicode__(self):
		return str(self.curso)+" - "+str(self.semestre /10)+" "+str(self.semestre%10)

class Estudiante(models.Model):
	nombre = models.CharField(max_length = 70)
	#Codigo?
	def __unicode__(self):
		return self.nombre

class Comentario(models.Model):
	contenido = models.CharField(max_length = 1000)
	autor = models.ForeignKey(Estudiante)  
	fecha = models.DateTimeField('Fecha de comentario')
	cursoDictado = models.ForeignKey(Dictado, null=True)

	exigencia = models.IntegerField(default=0)
	pedagogia = models.IntegerField(default=0)
	conocimiento = models.IntegerField(default=0)
	pasabilidad = models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.autor)+" - "+str(self.fecha)
