from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User

from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from trastornos.models import Tamizajes


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
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
	if(queryset=="trastornos"):
		return render(request, 'clasificacion.html')
	return render(request, 'clasificacion.html')


def prueba(request):
	return render(request, 'mensaje.html')

def mapaCalor(request):
	queryset= request.GET.get("Buscar")
	print(queryset)
	if(queryset=="nosotros"):
		return render(request, 'nosotros.html')
		
	if(queryset=="trastornos"):
		return render(request, 'clasificacion.html')

	casos = Tamizajes.objects.all()
	return render(request, 'mapaCalor.html',{"casos":casos})