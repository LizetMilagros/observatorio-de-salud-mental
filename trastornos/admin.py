from django.contrib import admin
from .models import Atendidos
from .models import Tamizajes
from .models import Noticia

admin.site.register(Atendidos)
admin.site.register(Tamizajes)
admin.site.register(Noticia)