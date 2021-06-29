from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def inicio(request):
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
	if(queryset=="transtornos"):
		return render(request, 'clasificacion.html')
	return render(request, 'inicio.html')
def nosotros(request):
	return render(request, 'nosotros.html')

def suscripcion(request):
	return render(request, 'suscripcion.html')

def clasificacion(request):
	return render(request, 'clasificacion.html')