from django.contrib import admin
from .models import Experiencia, Proyecto, Certificacion
from .models import Educacion   
from .models import CV

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'actualmente')
    list_filter = ('actualmente', 'empresa')
    search_fields = ('cargo', 'empresa', 'descripcion')


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'tecnologias')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'descripcion', 'tecnologias')


@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'fecha')
    list_filter = ('institucion', 'fecha')
    search_fields = ('titulo', 'institucion')

@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'fecha')
    search_fields = ('titulo', 'institucion')

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_actualizacion')