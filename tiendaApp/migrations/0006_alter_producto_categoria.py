# Generated by Django 5.0.1 on 2024-01-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0005_delete_solicitudes_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(max_length=32),
        ),
    ]
