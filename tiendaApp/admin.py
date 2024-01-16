from django.contrib import admin
from .models import Producto,Compra,DetalleCompra,Boleta
# Register your models here.

admin.site.register((Producto, Compra, DetalleCompra, Boleta))
