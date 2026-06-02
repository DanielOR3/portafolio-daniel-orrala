from django.shortcuts import render
from .models import Experiencia, Proyecto, Certificacion, Educacion, CV   # ← Agrega Educacion

def home(request):
    experiencias = Experiencia.objects.all().order_by('-actualmente', '-fecha_inicio')
    proyectos = Proyecto.objects.all().order_by('-fecha')
    certificaciones = Certificacion.objects.all().order_by('-fecha')
    educacion = Educacion.objects.all().order_by('-fecha')   
    cv = CV.objects.first()
    
    context = {
        'cv': cv,
        'experiencias': experiencias,
        'proyectos': proyectos,
        'certificaciones': certificaciones,
        'educacion': educacion,         
    }
    return render(request, 'core/home.html', context)