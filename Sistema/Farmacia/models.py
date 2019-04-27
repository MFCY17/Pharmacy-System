# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
TIPO_PAGO = (
    ('EFECTIVO','EFECTIVO'),
    ('CRÉDITO','CRÉDITO'),
)

#Modelo Perfil Empresa
class Empresa(models.Model):

	nombre_empresa = models.CharField(max_length = 50)
	ruc = models.CharField(max_length = 13)
	direccion = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 100)
	logo = models.ImageField(upload_to="Logos", null=True)
	
#Modelo del Cliente
class Cliente(models.Model):
	
	cedula = models.CharField(max_length = 13, unique=True, null=False, blank=False)
	nombres = models.CharField(max_length = 100, null=False, blank=False)
	apellidos = models.CharField(max_length = 100, null=False, blank=False)
	direccion = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 100)

	def __str__(self):
		return '{0} - {1}'.format(self.cedula, self.nombres)
		
#Modelo del Proveedor 
class Proveedor(models.Model):
	
	ruc= models.CharField(max_length = 13, unique=True, null=False, blank=False)
	distribuidora= models.CharField(max_length = 50)
	empresa= models.CharField(max_length = 100, null=False, blank=False)
	nombre_responsable= models.CharField(max_length = 100, null=False, blank=False)
	direccion= models.CharField(max_length = 100)
	telefono_empresa= models.CharField(max_length = 10)
	telefono_responsable= models.CharField(max_length = 10)
	email= models.EmailField(max_length = 50)
	

	def __str__(self):
		return self.distribuidora



#Modelo Categoria
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, unique=True, null=False, blank=False)
    descripcion = models.TextField()

    def __unicode__(self):
        return '{0}'.format(self.nombre_categoria)

#Modelo Presentación
class Presentacion(models.Model):
	nombre_presentacion = models.CharField(max_length = 60, unique=True, null=False, blank=False)

	def __unicode__(self):
		return '{0}'.format(self.nombre_presentacion)

#Modelo Producto
class Producto(models.Model):
	
	codigo_producto = models.CharField(max_length = 10, unique=True, null=False)
	nombre_producto = models.CharField(max_length = 100, null=False)
	nombre_generico = models.CharField(max_length = 100)
	casa_comercial = models.ForeignKey(Proveedor, on_delete = models.PROTECT)
	presentacion = models.ForeignKey(Presentacion, on_delete = models.PROTECT)	
	categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT)
	fecha_expiracion = models.DateField()
	fecha_elaboracion = models.DateField()
	detalle_producto = models.TextField()
	stock = models.IntegerField(default=0)		
	valor_Compra = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	precio_producto = models.DecimalField(default=0, max_digits = 10, decimal_places = 2, null=False)
	valor_venta_cajas = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	descuento = models.DecimalField(default=0, decimal_places=2, max_digits=6) 

	def __unicode__(self):
		return '{0} - {1}'.format(self.codigo_producto, self.nombre_producto)


#Modelo DetalleCompra
class DetalleCompra(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
	cantidad = models.IntegerField(default=0)

#Modelo Compra
class Compra(models.Model):
	numCompra = models.IntegerField(verbose_name="Compra Nro.", default=0)
	numFactura = models.IntegerField(verbose_name="Nro. Factura Proveedor", default=0)
	fechaCompra = models.DateField(default=timezone.now)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
	totalCompra = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	descripcion = models.CharField(max_length=200, default="")
	comprobante = models.ImageField(upload_to="Comprobantes", null=True)

	# Informacion del pago
	formaPago = models.CharField(default="CONTADO", max_length=7)
	plazoPago = models.IntegerField(default=0)
	estadoPago = models.CharField(default="REGISTRADO", max_length=10)
	fechaLimite = models.DateField(default=timezone.now)

	# DetalleCompra
	detalleCompra = models.ManyToManyField(DetalleCompra)

	def __unicode__(self):
		return 'Compra {0} - {1}'.format(self.fechacompra, self.ruc)

#Modelo Pago
class Pago(models.Model):
	valorPago = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=0)
	fechaPago = models.DateField(default=timezone.now)

	def __unicode__(self):
		return '{0} {1}'.format(self.valorPago, self.fechaPago)


#Modelo Venta
class DetalleFactura(models.Model):
    cantidad = models.IntegerField(verbose_name="Cantidad", default=1)
    concepto = models.CharField(max_length=100, verbose_name="Concepto")
    valorUnitario = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Valor Unitario")
    valorTotal = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Valor Total")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    def __unicode__(self):
        return '{0} {1}'.format(self.cantidad, self.concepto)

    def suma(self):
        return self.cantidad * self.producto.valorUnitario


class Factura(models.Model):
    serie = models.IntegerField(default=0)
    numero = models.CharField(max_length=7, verbose_name="N° de Factura", unique=True, null=False)
    tipoPago = models.CharField(max_length=50, choices=TIPO_PAGO)
    pagado = models.BooleanField(default=False)

    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    detalleFactura = models.ManyToManyField(DetalleFactura)

    subtotal = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    descuento = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    iva0 = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    iva12 = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    valorTotal = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    class Meta:
        unique_together = (('serie', 'numero'),)

    def __unicode__(self):
        return 'Factura {0} - {1}'.format(self.serie, self.numero)


