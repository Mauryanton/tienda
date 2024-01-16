"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from tiendaApp.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito,proceso_pago,webpay_redirect,procesar_compra,detalle_boleta

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Tienda API",
      default_version='v1',
      description="API para la tienda",
      terms_of_service="https://www.tu-terminos-de-servicio.com/",
      contact=openapi.Contact(email="tu@email.com"),
      license=openapi.License(name="Tu Licencia"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('api/tienda/v1/', include('rest_api_tienda.urls')),
    path('proceso_pago/', proceso_pago, name='pago'),
    path('webpay_redirect/', webpay_redirect, name='webpay_redirect'),
    path('procesar_compra/', procesar_compra, name='procesar_compra'),
    path('tienda/', tienda, name='tienda'),
    path('procesar_compra/boleta/<int:boleta_id>/', detalle_boleta, name='detalle_boleta'),
    # Agregar las siguientes líneas para la documentación con DRF-YASG
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

