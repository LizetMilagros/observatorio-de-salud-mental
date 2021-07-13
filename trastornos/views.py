from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
	if(queryset=="trastornos"):
		return render(request, 'clasificacion.html')
	return render(request, 'inicio.html')


def nosotros(request):
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
	if(queryset=="trastornos"):
		return render(request, 'clasificacion.html')
	return render(request, 'nosotros.html')

def suscripcion(request):
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
	if(queryset=="trastornos"):
		return render(request, 'clasificacion.html')

	#registrar usuarios
	if request.method == 'POST':
		username = request.POST['nombre']
		email = request.POST['email']

		if User.objects.filter(email=email).exists():
			messages.info(request, 'Usted ya esta suscrito')
			return redirect('suscripcion')

		else:
			user = User.objects.create_user(username=username, email=email)
			messages.info(request, f'{username}, gracias por suscribirte!')
			user.save()
			return redirect('suscripcion')
	else:
		return render(request, 'suscripcion.html')


def clasificacion(request):
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
	if(queryset=="trastornos"):
		return render(request, 'clasificacion.html')
	return render(request, 'clasificacion.html')