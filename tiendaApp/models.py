from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Compra(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)



class Boleta(models.Model):
    numero = models.IntegerField()  # Número de boleta
    cliente = models.CharField(max_length=255)  # Cliente asociado a la boleta
    productos = models.ManyToManyField(Producto)  # Lista de productos incluidos en la boleta
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la boleta

    def imprimir_boleta(self):
        print("Boleta Número:", self.numero)
        print("Cliente:", self.cliente)
        print("Productos:")
        for producto in self.productos.all():
            print(f"- {producto.nombre}: {producto.precio}")
        print("Total:", self.total)

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)