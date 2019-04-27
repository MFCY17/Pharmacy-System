from .models import Cliente, Proveedor, Categoria, Presentacion, Producto, DetalleFactura, Factura
from rest_framework import serializers
from django.contrib.auth.models import User


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id', 'cedula', 'nombres', 'apellidos', 'direccion', 'telefono', 'email')

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Proveedor
		fields = ('ruc', 'distribuidora', 'empresa', 'nombre_responsable', 'direccion', 'telefono_empresa', 'telefono_responsable', 'email')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('nombre_categoria', 'descripcion')

class PresentacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Presentacion
		fields = ('nombre_presentacion',)

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
	categoria = CategoriaSerializer()
	presentacion = PresentacionSerializer()
	casa_comercial = ProveedorSerializer()
	class Meta:
		model = Producto
		fields = ('codigo_producto', 'nombre_producto', 'nombre_generico', 'casa_comercial', 'presentacion', 'categoria', 'fecha_expiracion', 'fecha_elaboracion', 'detalle_producto', 'stock', 'valor_Compra', 'precio_producto', 'valor_venta_cajas', 'descuento')

class DetalleFacturaSerializer(serializers.HyperlinkedModelSerializer):
	producto = ProductoSerializer()
	class Meta:
		model = DetalleFactura
		fields = ('cantidad', 'concepto', 'valorUnitario', 'valorTotal', 'producto')

class FacturaSerializer(serializers.HyperlinkedModelSerializer):
	cliente = ClienteSerializer()
	detalleFactura = DetalleFacturaSerializer()

	class Meta:
		model = Factura
		fields = ('serie', 'numero', 'tipoPago', 'pagado', 'fecha', 'cliente', 'detalleFactura', 'subtotal', 'descuento', 'iva0', 'iva12', 'valorTotal')




 

 


 


  

 









	#id = serializers.ReadOnlyField()
	#firts_name = serializers.CharField()
	#last_name = serializers.CharField()
	#username = serializers.CharField()
	#email = serializers.EmailField()
	#password = serializers.CharField()

	#def create(self, validate_data):
	#	instance  = User()
	#	instance.firts_name = validate_data.get('firts_name')
	#	instance.last_name = validate_data.get('last_name')
	#	instance.username = validate_data.get('username')
	#	instance.email = validate_data.get('email')
	#	instance.set_password(validate_data.get('password'))
	#	instance.save()
	#	return instance

#	def validate_username(self, data):
#		users = User.objects.filter(username = data)
#		if len(users) ! = 0:
#			raise serializers.validationError("Este nombre de usuario ya existe, ingrese uno nuevo")
#		else:
#			return data
		

	 