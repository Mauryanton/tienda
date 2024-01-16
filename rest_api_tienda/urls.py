from django.urls import path
from . import views

urlpatterns = [
    path('productos/',views.lista_productos, name='lista_productos'),
    path('productos/<id>',views.vista_producto, name= 'vista_producto'),
    
    # Rutas para el modelo Compra
    path('compras/', views.lista_compras, name='lista_compras'),
    path('compras/<int:id>/', views.detalle_compra, name='detalle_compra'),

    # Rutas para el modelo DetalleCompra
    path('detalle_compras/', views.lista_detalles_compra, name='lista_detalles_compra'),
    path('detalle_compras/<int:id>/', views.detalle_detalle_compra, name='detalle_detalle_compra'),
    
    # Rutas para el modelo Boleta
    path('boletas/', views.lista_boletas, name='lista_boletas'),
    path('boletas/<int:id>/', views.detalle_boleta, name='detalle_boleta'),

]