from django.contrib import admin
from Ranking.models import *

#class CursoDictadoInLine(admin.TabularInline):
#	model = CursoDictado

#class ProfesorAdmin(admin.ModelAdmin):
#	fieldsets = [
#		('Nombre',{'fields':[('nombre')]}),
#	]
#	inlines = [CursoDictadoInLine]

#admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Profesor)
admin.site.register(CursoDictado)
admin.site.register(Estudiante)