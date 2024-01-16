# Generated by Django 5.0.1 on 2024-01-16 02:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0010_boleta'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.boleta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.producto')),
            ],
        ),
    ]
