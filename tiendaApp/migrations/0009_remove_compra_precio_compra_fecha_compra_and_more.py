# Generated by Django 5.0.1 on 2024-01-16 00:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0008_detallecompra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='precio',
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compra',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='compra',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='compra',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
