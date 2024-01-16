from django.shortcuts import render
from rest_framework.response import Response
from tiendaApp.models import Producto
from .serializers import ProductoSerializer,CompraSerializer, DetalleCompraSerializer,BoletaSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from tiendaApp.models import Compra, DetalleCompra,Boleta



# Create your views here.
@csrf_exempt #para que no pida token.
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def lista_productos(request):
    # 1 mostrar los productos
    # 2 crear un producto
    if request.method == 'GET':
        # Obtener todos los productos
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Crear un nuevo producto
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt #para que no pida token.
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])  # Para evitar que pida el token CSRF
def vista_producto(request, id):
    # 2. Mostrar un producto en particular
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        producto = get_object_or_404(Producto, id=id)
        serializer = ProductoSerializer(producto, data=request.data)
        #actualizar el producto
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_compras(request):
    if request.method == 'GET':
        compras = Compra.objects.all()
        serializer = CompraSerializer(compras, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def detalle_compra(request, id):
    if request.method == 'GET':
        compra = get_object_or_404(Compra, id=id)
        serializer = CompraSerializer(compra)
        return Response(serializer.data)

    elif request.method == 'PUT':
        compra = get_object_or_404(Compra, id=id)
        serializer = CompraSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        compra = get_object_or_404(Compra, id=id)
        compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_detalles_compra(request):
    if request.method == 'GET':
        detalles_compra = DetalleCompra.objects.all()
        serializer = DetalleCompraSerializer(detalles_compra, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DetalleCompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def detalle_detalle_compra(request, id):
    if request.method == 'GET':
        detalle_compra = get_object_or_404(DetalleCompra, id=id)
        serializer = DetalleCompraSerializer(detalle_compra)
        return Response(serializer.data)

    elif request.method == 'PUT':
        detalle_compra = get_object_or_404(DetalleCompra, id=id)
        serializer = DetalleCompraSerializer(detalle_compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detalle_compra = get_object_or_404(DetalleCompra, id=id)
        detalle_compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_boletas(request):
    if request.method == 'GET':
        boletas = Boleta.objects.all()
        serializer = BoletaSerializer(boletas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def detalle_boleta(request, id):
    if request.method == 'GET':
        boleta = get_object_or_404(Boleta, id=id)
        serializer = BoletaSerializer(boleta)
        return Response(serializer.data)

    elif request.method == 'PUT':
        boleta = get_object_or_404(Boleta, id=id)
        serializer = BoletaSerializer(boleta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        boleta = get_object_or_404(Boleta, id=id)
        boleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)