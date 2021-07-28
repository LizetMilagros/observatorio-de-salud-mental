from django.urls import path
from django.views.generic.base import View
from . import views
from trastornos.views import *

urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('nosotros', views.nosotros, name='nosotros'),
	path('suscripcion', views.suscripcion, name='suscripcion'),
	path('clasificacion', views.clasificacion, name='clasificacion'),
	path('resultado', views.resultado, name='resultado'),
	path('noticias', views.noticias, name='noticias'),
	path('alcohol', views.alcohol, name='alcohol'),
	path('alimentario', views.alimentario, name='alimentario'),
	path('ansiedad', views.ansiedad, name='ansiedad'),
	path('comportamiento', views.comportamiento, name='comportamiento'),
	path('depresivo', views.depresivo, name='depresivo'),
	path('drogas', views.drogas, name='drogas'),
	path('escolar', views.escolar, name='escolar'),
	path('psicotico', views.psicotico, name='psicotico'),
	path('suicidio', views.suicidio, name='suicidio'),
	path('violencia', views.violencia, name='violencia'),
	path('mapa', views.mapaCalor, name='mapa'),
	path('tests', views.testFormulario, name='tests'),
	path('testAnsiedad', views.testAnsiedad, name='testAnsiedad'),
	path('testComportamiento', views.testComportamiento, name='testComportamiento'),
	path('testDepresivo', views.testDepresivo, name='testDepresivo'),
	path('testPsicotico', views.testPsicotico, name='testPsicotico'),
	path('graficas', views.graficas, name='graficas'),
]
