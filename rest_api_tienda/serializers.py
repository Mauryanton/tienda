from rest_framework import serializers 
from tiendaApp.models import Producto,Compra,DetalleCompra,DetalleBoleta,Boleta


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = '__all__'
        
class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'