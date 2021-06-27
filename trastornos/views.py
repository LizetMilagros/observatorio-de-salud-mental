from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def inicio(request):
	return render(request, 'inicio.html')

def nosotros(request):
	return render(request, 'nosotros.html')

def suscripcion(request):
	return render(request, 'suscripcion.html')