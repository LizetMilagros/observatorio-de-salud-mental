from django.db import models

# Create your models here.
class Atendidos(models.Model):
    Anio=models.IntegerField()
    NroMes=models.IntegerField()
    Ubigeo=models.IntegerField()
    Departamento=models.CharField(max_length =30)
    Provincia=models.CharField(max_length =30)
    Distrito=models.CharField(max_length =30)
    Sexo=models.CharField(max_length =3)
    Etapa=models.CharField(max_length =30)
    Diagnostico=models.CharField(max_length =30)
    Atendidos=models.IntegerField()
    Atenciones=models.IntegerField()
class Tamizajes (models.Model):
    Anio=models.IntegerField()
    NroMes=models.IntegerField()
    Ubigeo=models.IntegerField()
    Departamento=models.CharField(max_length =29)
    Provincia=models.CharField(max_length =30)
    Distrito=models.CharField(max_length =30)
    Sexo=models.CharField(max_length =3)
    Etapa=models.CharField(max_length =30)
    GrupoTamizaje=models.CharField(max_length =30)
    DetalleTamizaje=models.CharField(max_length =30)
    Casos=models.IntegerField()

class Noticia(models.Model):
    titulo = models.CharField('Titulo', max_length =150, blank=False, null=False)
    fuente = models.CharField('Fuente', max_length =300, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length =200, blank=False, null=False)
    imagen = models.URLField(max_length =255, blank=False, null=False)

    def __str__(self):
        return self.titulo

