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
]
