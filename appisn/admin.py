from django.contrib import admin
from appisn.models import Curso, Estudiante, Profesor, Entregable

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")
    list_per_page = 1
    list_filter = ("nombre",)
    ordering = ("nombre",)
# Register your models here
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
