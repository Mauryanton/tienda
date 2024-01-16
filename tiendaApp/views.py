from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from tiendaApp.carrito import Carrito
from tiendaApp.models import Producto,Compra,DetalleCompra,Boleta
from .forms import CompraForm

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    print(carrito.carrito)  # Imprime el contenido del carrito
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

def proceso_pago(request):
    carrito = Carrito(request)
    items_carrito = carrito.carrito.values()
    total_carrito = carrito.obtener_total_carrito()

    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            # Guardar la información de la compra en la sesión
            request.session['compra'] = {
                'nombre': compra_form.cleaned_data['nombre'],
                'direccion': compra_form.cleaned_data['direccion'],
                'telefono': compra_form.cleaned_data['telefono'],
                'correo_electronico': compra_form.cleaned_data['correo_electronico'],
            }

            # Aquí puedes agregar la lógica de procesamiento de la compra si es necesario
            # ...

            # Redirigir a la página de confirmación o procesamiento de pago
            return redirect('detalle_boleta')
    else:
        compra_form = CompraForm()

    return render(request, "pago.html", {'items_carrito': items_carrito, 'total_carrito': total_carrito, 'compra_form': compra_form})

def webpay_redirect(request):
    # Lógica para la redirección a WebPay
    # ...

    return HttpResponse("Redirección a WebPay")

def procesar_compra(request):
    carrito = Carrito(request)
    total_carrito = carrito.obtener_total_carrito()

    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            # Crear un objeto Compra y guardarlo en la base de datos
            nueva_compra = Compra(
                nombre=compra_form.cleaned_data['nombre'],
                direccion=compra_form.cleaned_data['direccion'],
                telefono=compra_form.cleaned_data['telefono'],
                correo_electronico=compra_form.cleaned_data['correo_electronico'],
                total=total_carrito  # Asegúrate de que este campo esté presente
            )
            nueva_compra.save()

            # Guardar los detalles de la compra en la base de datos
            for producto_id, info_producto in carrito.carrito.items():
                producto = Producto.objects.get(id=producto_id)
                detalle_compra = DetalleCompra(
                    compra=nueva_compra,
                    producto=producto,
                    cantidad=info_producto['cantidad'],
                    precio_unitario=producto.precio
                )
                detalle_compra.save()

            # Crear una nueva boleta asociada a la compra
            nueva_boleta = Boleta.objects.create(
                numero=nueva_compra.id,  # Usamos el ID de la compra como número de boleta
                cliente=nueva_compra.nombre,
                total=nueva_compra.total
            )
            nueva_boleta.productos.set([detalle.producto for detalle in nueva_compra.detallecompra_set.all()])

            # Limpiar el carrito después de la compra
            carrito.limpiar()

            # Redirigir a la página de confirmación o a donde desees
            return redirect('detalle_boleta', boleta_id=nueva_boleta.id)

    else:
        compra_form = CompraForm()

    return render(request, "pago.html", {'total_carrito': total_carrito, 'compra_form': compra_form})


def pagina_pago(request):
    # ... tu lógica actual ...

    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            # Guardar la información de la compra en la sesión
            request.session['compra'] = {
                'nombre': compra_form.cleaned_data['nombre'],
                'direccion': compra_form.cleaned_data['direccion'],
                'telefono': compra_form.cleaned_data['telefono'],
                'correo_electronico': compra_form.cleaned_data['correo_electronico'],
            }

            # Redirigir a la página de confirmación o procesamiento de pago
            return redirect('pagina_confirmacion_pago')
    else:
        compra_form = CompraForm()

    # ... tu lógica actual ...

    return render(request, 'tu_app/pagina_pago.html', {
        'compra_form': compra_form,
        # ... otros contextos ...
    })

def detalle_boleta(request, boleta_id):
    boleta = get_object_or_404(Boleta, id=boleta_id)
    return render(request, 'boleta.html', {'boleta': boleta})