# Generated by Django 3.2.4 on 2021-07-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trastornos', '0003_alter_noticia_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fuente',
            field=models.CharField(max_length=300, verbose_name='Fuente'),
        ),
    ]
