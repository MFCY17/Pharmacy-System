#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from django import forms
#Cliente
from .models import DetalleCompra
from .models import Cliente
#Proveedor
from .models import Proveedor
#Producto
from .models import Producto
#Categoria
from .models import Categoria
#Presentacion
from .models import Presentacion
#Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Compra
from .models import Compra, Pago, DetalleCompra
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea, Select
from django.forms.formsets import BaseFormSet
from django.forms.models import inlineformset_factory
from django.forms import fields
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.admin import widgets



#########################################################
#Cliente
class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields =[
		         'cedula',
		         'nombres',
		         'apellidos',
		         'direccion',
		         'telefono',
		         'email',
		]
		labels ={
		        'cedula' : 'Ingrese la cédula',
		        'nombres':'Ingrese los nombres',
		        'apellidos':'Ingrese los apellidos',		        
		        'direccion':'Ingrese la dirección',		        
		        'telefono':'Ingrese el teléfono ',
		        'email':'Ingrese el correo electrónico',	        
		}

class ClienteEditarForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
				'cedula',
				'nombres',
				'apellidos',
				'direccion',
				'telefono',
				'email',
		]

		labels = {
				'cedula' : 'Ingrese su cédula',
				'nombres' : 'Inrgese sus nombres',
				'apellidos' : 'Ingrese sus apellidos',
				'direccion' : 'Ingrese su dirección',
				'telefono' : 'Ingrese su teléfono',
				'email' : 'Ingrese el correo electrónico',
		}
##########################################################################
#Proveedor
class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields =[
		         'ruc',
		         'distribuidora',
		         'empresa',
		         'nombre_responsable',
		         'direccion',
		         'telefono_empresa',
		         'telefono_responsable',
		         'email',
		          
		]
		labels ={
		        'ruc' : 'Ingrese el ruc',
		        'distribuidora':'Ingrese la distribuidora',
		        'empresa':'Ingrese la casa comercial',		        
		        'nombre_responsable':'Ingrese el nombre del responsable',		        
		        'direccion':'Ingrese la dirección ',
		        'telefono_empresa':'Ingrese el teléfono de la empresa',	    
		        'telefono_responsable':'Ingrese el teléfono del responsable',	  
		        'email':'Ingrese el correo  electrónico',	  
		        	      
		}

class ProveedorEditarForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
				 'ruc',
		         'distribuidora',
		         'empresa',
		         'nombre_responsable',
		         'direccion',
		         'telefono_empresa',
		         'telefono_responsable',
		         'email',
		          
		]

		labels = {
				'ruc' : 'Ingrese el ruc',
		        'distribuidora':'Ingrese la distribuidora',
		        'empresa':'Ingrese la empresa',		        
		        'nombre_responsable':'Ingrese el nombre del responsable',		        
		        'direccion':'Ingrese la dirección ',
		        'telefono_empresa':'Ingrese el teléfono de la empresa',	    
		        'telefono_responsable':'Ingrese el teléfono del responsable',	  
		        'email':'Ingrese el correo electrónico',	  
		        	     
		}
##################################################################################################
#Producto
class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields =[
			'codigo_producto',
			'nombre_producto',
			'nombre_generico',
			'casa_comercial', 
			'presentacion',
			'categoria',
			'fecha_expiracion',
			'fecha_elaboracion',
			'detalle_producto',
			'stock',
			'valor_Compra', 
			'precio_producto',
			'valor_venta_cajas',
			'descuento',
			
		]

		labels ={
			'codigo_producto' : 'Código',
			'nombre_producto' : 'Nombre comercial',
			'nombre_generico': 'Nombre genérico',
			'precio_producto': 'Precio del producto',
			'casa_comercial': 'Proveedor',
			'presentacion':'Presentación',
			'categoria':'Categoria',
			'fecha_expiracion':'Fecha de expiracion (dd/mm/aaaa)',
			'fecha_elaboracion':'Fecha de elaboración (dd/mm/aaaa)',
			'detalle_producto':'Descripción',
			'stock':'Stock',
			'valor_Compra': 'Valor de compra',
			'precio_producto':'Valor de venta unitario',
			'valor_venta_cajas':'Valor cajas',
			'descuento':'Valor cajas con descuento',
		}
		
		
        

		widgets ={
		    'presentacion':forms.Select(attrs={'class':'form-control'}), 
			'fecha_expiracion':forms.SelectDateWidget(attrs={'class':'form-control'}), 
			'fecha_elaboracion':forms.SelectDateWidget(attrs={'class':'form-control'}), 
			
			
		}

class ProductoEditarForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields =[
			'codigo_producto',
			'nombre_producto',
			'nombre_generico',
			'casa_comercial', 
			'presentacion',
			'categoria',
			'fecha_expiracion',
			'fecha_elaboracion',
			'detalle_producto',
			'stock',
			'valor_Compra', 
			'precio_producto',
			'valor_venta_cajas',
			'descuento',
			
		]

		labels ={
			'codigo_producto' : 'Codigo',
			'nombre_producto' : 'Nombre comercial',
			'nombre_generico': 'Nombre generico',
			'precio_producto': 'Precio del producto',
			'casa_comercial': 'Casa comercial',
			'presentacion':'Presentacion',
			'categoria':'Categoria',
			'fecha_expiracion':'Fecha de expiracion  dd/mm/aaaa',
			'fecha_elaboracion':'Fecha de elaboracion dd/mm/aaaa',
			'detalle_producto':'Descripcion',
			'stock':'Stock',
			'valor_Compra': 'Valor de compra',
			'precio_producto':'Valor de venta unitario',
			'valor_venta_cajas':'Valor cajas',
			'descuento':'Valor caja con descuento',
		}
#######################################################################################
#Categoria
class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields =[
			'nombre_categoria',
			'descripcion',
		]

		labels ={
			'nombre_categoria' : 'Ingrese nombre de la Categoría',
			'descripcion':'Ingrese una descripción',
		}

class CategoriaEditarForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
			'nombre_categoria',
			'descripcion',
		]

		labels = {
			'nombre_categoria' : 'Ingrese nombre de la Categoría',
			'descripcion' : 'Ingrese una descripción',
		}
###################################################################################################
#Presentacion
class PresentacionForm(forms.ModelForm):
	class Meta:
		model = Presentacion
		fields =[
			'nombre_presentacion',
		]
		labels ={
			'nombre_presentacion' : 'Ingrese nombre de la presentación',
		}
class PresentacionEditarForm(forms.ModelForm):
	class Meta:
		model = Presentacion
		fields = [
			'nombre_presentacion',
		]

		labels = {
			'nombre_presentacion' : 'Ingrese nombre de la presentación',
		}
##################################################################################################
#Usuario 
class UsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields =[
		         'username',
		         'first_name',
		         'last_name',
		         'email',
		         'is_staff',
		         'date_joined', 
		         'is_active', 
		         'is_superuser',
		         

		]

		labels ={
		        'username' : 'Ingrese el nombre de Usuario',
		        'first_name':'Ingrese el Nombre',
		        'last_name':'Ingrese el Apellido',
		        'email':'Ingrese su correo electronico',
		        'is_staff':'Dar permiso de administrador',
		        'is_active':'Estado activo',
		}

class UsuarioEditarForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
				 'username',
		         'first_name',
		         'last_name',
		         'email',
		         'is_staff',
		         'date_joined', 
		         'is_active', 
		         'is_superuser',
		]

		labels = {
				'username' : 'Ingrese el nombre de Usuario',
		        'first_name':'Ingrese el Nombre',
		        'last_name':'Ingrese el Apellido',
		        'email':'Ingrese su correo electronico',
		        'is_staff':'Dar permiso de administrador',
		        'is_active':'Estado activo',
		}

##################################################################################################
#Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields =[
			'numCompra',
			'numFactura',
			'fechaCompra',
			'proveedor',
            'totalCompra',
            'descripcion',
			'comprobante',
            #Informacion del pago
            'formaPago',
            'plazoPago',
            'estadoPago',
            'fechaLimite'

		]
        labels ={
			'numCompra' : 'Compra Nro.:',
			'numFactura' : 'Nro. Factura Proveedor:',
			'fechaCompra' : 'Fecha de compra:',
			'proveedor' : 'RUC Proveedor:',
            'totalCompra' : 'Total compra',
            'descripcion' : 'Descripcion',
			'comprobante' : 'Ingrese el comprobante correspondiente',
            'formaPago' : 'Forma de pago',
            'plazoPago' : 'Plazo (meses)',
            'estadoPago' : 'Estado',
            'fechaLimite' : 'Fecha limite',
		}
        widgets = {
            'fechaCompra': SelectDateWidget(),
            'formaPago' : Select(choices= (('CONTADO', 'CONTADO',), ('CREDITO', 'CREDITO',))),
            'estadoPago': Select(choices=(('REGISTRADO', 'REGISTRADO',), ('PAGADO', 'PAGADO',))),
            'descripcion': Textarea(attrs={'cols': 100, 'rows': 7, 'class':'form-control'}),
            'fechaLimite': SelectDateWidget(),
        }


##################################################################################################
# DetalleCompra

class DetalleCompraForm(BSModalForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad']
        labels = {'producto':'Producto: ', 'cantidad':'Cantidad: ',}


##################################################################################################
# Pago
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields =[
			'valorPago',
			'fechaPago',
		]
        labels ={
			'valorPago' : 'Valor pago:',
			'fechaPago' : 'Fecha de pago:',
		}
        widgets = {
            'fechaPago': SelectDateWidget(),
        }

##################################################################################################

CompraPagosFormSet = inlineformset_factory(Compra, Pago, form=PagoForm, can_delete=True, extra=1)
CompraPagosEditFormSet = inlineformset_factory(Compra, Pago, form=PagoForm, can_delete=True, extra=0)


##################################################################################################
#Reporte de productos
class ReporteProductosForm(forms.Form):
	proveedores = Proveedor.objects.all()
	opciones = fields.ChoiceField(choices=[(proveedor.id, proveedor.distribuidora) for proveedor in proveedores],required=True)
