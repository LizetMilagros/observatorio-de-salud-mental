from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Noticia,Atendidos
from django.db.models import Q, Sum
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
	violenciaM = Atendidos.objects.filter(Diagnostico = 'VIOLENCIA FAMILIAR/MALTRATO INFANTIL', Sexo='M').aggregate(Sum('Atendidos'))
	violenciaF = Atendidos.objects.filter(Diagnostico = 'VIOLENCIA FAMILIAR/MALTRATO INFANTIL', Sexo='F').aggregate(Sum('Atendidos'))

	ansiedadM = Atendidos.objects.filter(Diagnostico = 'ANSIEDAD', Sexo='M').aggregate(Sum('Atendidos'))
	ansiedadF = Atendidos.objects.filter(Diagnostico = 'ANSIEDAD', Sexo='F').aggregate(Sum('Atendidos'))

	depresionM = Atendidos.objects.filter(Diagnostico = 'TRASTORNO DEPRESIVO', Sexo='M').aggregate(Sum('Atendidos'))
	depresionF = Atendidos.objects.filter(Diagnostico = 'TRASTORNO DEPRESIVO', Sexo='F').aggregate(Sum('Atendidos'))

	comportamientoM = Atendidos.objects.filter(Diagnostico = 'TRASTORNO DEL COMPORTAMIENTO (F90 - F91)', Sexo='M').aggregate(Sum('Atendidos'))
	comportamientoF = Atendidos.objects.filter(Diagnostico = 'TRASTORNO DEL COMPORTAMIENTO (F90 - F91)', Sexo='F').aggregate(Sum('Atendidos'))

	alcoholM = Atendidos.objects.filter(Diagnostico = 'TRASTORNO CONSUMO DE ALCOHOL', Sexo='M').aggregate(Sum('Atendidos'))
	alcoholF = Atendidos.objects.filter(Diagnostico = 'TRASTORNO CONSUMO DE ALCOHOL', Sexo='F').aggregate(Sum('Atendidos'))

	drogasM = Atendidos.objects.filter(Diagnostico = 'TRASTORNO CONSUMO DE OTRAS DROGAS', Sexo='M').aggregate(Sum('Atendidos'))
	drogasF = Atendidos.objects.filter(Diagnostico = 'TRASTORNO CONSUMO DE OTRAS DROGAS', Sexo='F').aggregate(Sum('Atendidos'))

	suicidioM = Atendidos.objects.filter(Diagnostico = 'INTENTO DE SUICIDIO', Sexo='M').aggregate(Sum('Atendidos'))
	suicidioF = Atendidos.objects.filter(Diagnostico = 'INTENTO DE SUICIDIO', Sexo='F').aggregate(Sum('Atendidos'))

	psicoM = Atendidos.objects.filter(Diagnostico = 'SINDROME Y/O TRASTORNO PSICOTICO', Sexo='M').aggregate(Sum('Atendidos'))
	psicoF = Atendidos.objects.filter(Diagnostico = 'SINDROME Y/O TRASTORNO PSICOTICO', Sexo='F').aggregate(Sum('Atendidos'))

	alimentacionM = Atendidos.objects.filter(Diagnostico = 'TRASTORNOS ALIMENTARIOS (F500 - F508 ANOREXIA, BULIMIA)', Sexo='M').aggregate(Sum('Atendidos'))
	alimentacionF = Atendidos.objects.filter(Diagnostico = 'TRASTORNOS ALIMENTARIOS (F500 - F508 ANOREXIA, BULIMIA)', Sexo='F').aggregate(Sum('Atendidos'))

	escolarM = Atendidos.objects.filter(Diagnostico = 'VIOLENCIA ESCOLAR (Y062 - BULLYING)', Sexo='M').aggregate(Sum('Atendidos'))
	escolarF = Atendidos.objects.filter(Diagnostico = 'VIOLENCIA ESCOLAR (Y062 - BULLYING)', Sexo='F').aggregate(Sum('Atendidos'))

	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')


	return render(request, 
		'clasificacion.html',
		{
			'violenciaM':violenciaM, 'violenciaF':violenciaF,
			'ansiedadM':ansiedadM, 'ansiedadF':ansiedadF,
			'depresionM':depresionM, 'depresionF':depresionF,
			'comportamientoM':comportamientoM, 'comportamientoF':comportamientoF,
			'alcoholM':alcoholM, 'alcoholF':alcoholF,
			'drogasM':drogasM, 'drogasF':drogasF,
			'suicidioM':suicidioM, 'suicidioF':suicidioF,
			'psicoM':psicoM, 'psicoF':psicoF,
			'alimentacionM':alimentacionM, 'alimentacionF':alimentacionF,
			'escolarM':escolarM, 'escolarF':escolarF,
		}
	)


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

def mapaCalor(request):
	noticia = Noticia.objects.all()
	casos = Atendidos.objects.all()
	
	queryset= request.GET.get("Buscar")
	if queryset:
		noticia = Noticia.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset)
		).distinct()
		return render(request, 'resultado.html', {'noticia':noticia})
	elif queryset=="":
		return render(request, 'resultado.html')

	return render(request, 'mapaCalor.html',{"casos":casos})

def testFormulario(request):
	return render(request, 'test.html')

def testAnsiedad(request):
	return render(request, 'testsForms/test1.html')

def testComportamiento(request):
	return render(request, 'testsForms/test2.html')

def testDepresivo(request):
	return render(request, 'testsForms/test3.html')

def testPsicotico(request):
	return render(request, 'testsForms/test4.html')