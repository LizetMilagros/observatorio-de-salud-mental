from django.urls import path
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
]
