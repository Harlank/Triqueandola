from django.contrib import admin
from Ranking.models import *

class CursoDictadoInLine(admin.TabularInline):
	model = Dictado

class ProfesorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nombre',{'fields':[('nombre')]}),
	]
	inlines = [CursoDictadoInLine]


class ComentarioInLine(admin.TabularInline):
	model = Comentario

class EstudianteAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nombre',{'fields':[('nombre')]}),
	]
	inlines = [ComentarioInLine]

admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Curso)
admin.site.register(Estudiante,EstudianteAdmin)