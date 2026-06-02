from django.db import models
from django.utils import timezone

class Experiencia(models.Model):
    cargo = models.CharField(max_length=150, verbose_name="Cargo")
    empresa = models.CharField(max_length=150, verbose_name="Empresa")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(blank=True, null=True, verbose_name="Fecha de Fin")
    actualmente = models.BooleanField(default=False, verbose_name="Trabajo Actual")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['-actualmente', '-fecha_inicio']

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    tecnologias = models.CharField(max_length=300, verbose_name="Tecnologías")
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True, verbose_name="Imagen")
    enlace_github = models.URLField(blank=True, null=True, verbose_name="GitHub")
    enlace_repo = models.URLField(blank=True, null=True, verbose_name="Repositorio")
    enlace_demo = models.URLField(blank=True, null=True, verbose_name="Demo")
    fecha = models.DateField(default=timezone.now, verbose_name="Fecha")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class Certificacion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    institucion = models.CharField(max_length=150, verbose_name="Institución")
    fecha = models.DateField(verbose_name="Fecha")
    enlace = models.URLField(blank=True, null=True, verbose_name="Enlace")

    class Meta:
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

class Educacion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    institucion = models.CharField(max_length=150, verbose_name="Institución")
    fecha = models.CharField(max_length=50, verbose_name="Año / Fecha")  # Ej: "2024"
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    
    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educación"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"
        
class CV(models.Model):
    titulo = models.CharField(max_length=100, default="Curriculum Vitae")
    archivo = models.FileField(upload_to='cv/', verbose_name="Archivo PDF")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Curriculum Vitae"
        verbose_name_plural = "Curriculum Vitae"