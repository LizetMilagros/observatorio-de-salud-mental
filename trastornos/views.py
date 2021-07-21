from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Noticia
from django.db.models import Q
from django.core.paginator import Paginator

from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string


def inicio(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'inicio.html')


def nosotros(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'nosotros.html')

def suscripcion(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')

	#registrar usuarios por formulario
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
			
			# Establecemos conexion con el servidor smtp de gmail
			mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
			mailServer.ehlo()
			mailServer.starttls()
			mailServer.ehlo()
			mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

			# Construimos el mensaje
			mensaje = MIMEMultipart()
			mensaje['From']=settings.EMAIL_HOST_USER
			mensaje['To']=email
			mensaje['Subject']="Suscripcion a SmartMind"

			content = render_to_string('mensaje.html', {'user': username})
			# Adjuntamos el texto
			mensaje.attach(MIMEText(content, 'html'))
			# Envio del mensaje
			mailServer.sendmail(settings.EMAIL_HOST_USER,
			                email,
			                mensaje.as_string())

			return redirect('suscripcion')

	#elif request.user.is_authenticated:
		#context = request.user.email

	return render(request, 'suscripcion.html')


def clasificacion(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'clasificacion.html')


def prueba(request):
	return render(request, 'mensaje.html')

def noticias(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	
	paginator = Paginator(noticia,9)
	page = request.GET.get('page')
	noticia = paginator.get_page(page)

	return render(request, 'noticias.html', {'noticia':noticia})

def resultado(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
	elif queryset=="":
		return render(request, 'resultado.html')

	return render(request, 'resultado.html', {'noticia':noticia})



#interfaces de trastornos mentales
def comportamiento(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/comportamiento.html')

def alcohol(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/alcohol.html')

def alimentario(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/alimentario.html')

def ansiedad(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/ansiedad.html')

def depresivo(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/depresivo.html')

def drogas(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/drogas.html')

def escolar(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/escolar.html')

def psicotico(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/psicotico.html')

def suicidio(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/suicidio.html')

def violencia(request):
	noticia = Noticia.objects.all()
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')
	return render(request, 'enfermedad/violencia.html')