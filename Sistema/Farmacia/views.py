# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import random
from datetime import datetime
from decimal import Decimal
from io import BytesIO

from bootstrap_modal_forms.generic import BSModalCreateView
# REPORTES
from django.conf import settings
from django.contrib import messages
# Login
from django.contrib.auth.decorators import login_required
# Usuario
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from xhtml2pdf import pisa

from Farmacia.forms import PagoForm
from Farmacia.models import DetalleFactura, DetalleCompra
from Farmacia.models import Factura
from Farmacia.utils import link_callback
from .forms import CategoriaEditarForm
from .forms import CategoriaForm
from .forms import ClienteEditarForm
from .forms import ClienteForm
from .forms import CompraForm, CompraPagosFormSet, CompraPagosEditFormSet, DetalleCompraForm
from .forms import PresentacionEditarForm
from .forms import PresentacionForm
from .forms import ProductoEditarForm
from .forms import ProductoForm
from .forms import ProveedorEditarForm
from .forms import ProveedorForm
from .forms import ReporteProductosForm
from .forms import UsuarioEditarForm
from .forms import UsuarioForm
# Categoria
from .models import Categoria
# Cliente
from .models import Cliente
# Compra
from .models import Compra
# PERFIL
from .models import Empresa
from .models import Pago
# Presentacion
from .models import Presentacion
# Producto
from .models import Producto
# Proveedor
from .models import Proveedor


# API
# from .serializers import ClienteSerializer, ProveedorSerializer, CategoriaSerializer, PresentacionSerializer, ProductoSerializer
# from .serializers import DetalleFacturaSerializer, FacturaSerializer
# from rest_framework import  generics

# class ClienteList(generics.ListCreateAPIView):
# 	queryset = Cliente.objects.all()
# 	serializer_class = ClienteSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj
#
# class ProveedorList(generics.ListCreateAPIView):
# 	queryset = Proveedor.objects.all()
# 	serializer_class = ProveedorSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj
#
# class ProductoList(generics.ListCreateAPIView):
# 	queryset = Producto.objects.all()
# 	serializer_class = ProductoSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj
#
# class CategoriaList(generics.ListCreateAPIView):
# 	queryset = Categoria.objects.all()
# 	serializer_class = CategoriaSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj
#
# class PresentacionList(generics.ListCreateAPIView):
# 	queryset = Presentacion.objects.all()
# 	serializer_class = PresentacionSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj
#
# class DetalleFacturaList(generics.ListCreateAPIView):
# 	queryset = DetalleFactura.objects.all()
# 	serializer_class = DetalleFacturaSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj
#
# class FacturaList(generics.ListCreateAPIView):
# 	queryset = Factura.objects.all()
# 	serializer_class = FacturaSerializer
#
# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		obj = get_object_or_404(
# 			queryset,
# 			pk = self.kwargs['pk'],
# 		)
#
# 		return obj


# Create your views here.
@login_required
def base(request):
    return render(request, "Facturacion/base.html", {})


###########################################################
@csrf_exempt
def validar_rol(request):
    resultado = 0;
    loggedUser = request.POST['username']
    partes = loggedUser.split(':')
    loggedUser = partes[1]

    usuarios = User.objects.filter(is_active=1)
    for usuario in usuarios:
        if (usuario.username.lower() == loggedUser.lower()):
            resultado = usuario.is_superuser
    return HttpResponse(resultado)


# Configuracion
def perfil_empresa(request):
    return render(request, "Facturacion/Configuracion/perfil_empresa.html", {})


def perfil_usuario(request):
    return render(request, "Facturacion/Configuracion/perfil_usuario.html", {})


class PerfilEmpresa(SuccessMessageMixin, CreateView):
    model = Empresa
    template_name = "Facturacion/Configuracion/perfil_empresa.html"
    success_url = reverse_lazy('empresa')
    success_message = 'Actualización correcta'


# Cliente
class RegistroCliente(SuccessMessageMixin, CreateView):
    model = Cliente
    template_name = "Facturacion/Cliente/crear_cliente.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente')
    success_message = 'Cliente registrado con exito'


def listar_clientes(request):
    lista_clientes = Cliente.objects.all()
    contexto = {'clientes': lista_clientes}
    return render(request, "Facturacion/Cliente/listar_clientes.html", contexto)


class ListarClientes(ListView):
    model = Cliente
    template_name = "Facturacion/Cliente/listar_clientes.html"


def editar_clientes(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'GET':
        form = ClienteEditarForm(instance=cliente)
    else:
        form = ClienteEditarForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save
        return redirect('listaclientes')
    return render(request, 'Facturacion/Cliente/editar_cliente.html', {'form': form})


class ActualizarClientes(UpdateView):
    model = Cliente
    form_class = ClienteEditarForm
    template_name = "Facturacion/Cliente/editar_cliente.html"
    success_url = reverse_lazy('listaclientes')


def eliminar_clientes(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listaclientes')
    return render(request, 'Facturacion/Cliente/eliminar_clientes.html', {'cliente': cliente})


class DetalleCliente(DetailView):
    model = Cliente
    template_name = 'Facturacion/Cliente/detalle_cliente.html'


######################################################################################################
# Proveedor
class RegistroProveedor(SuccessMessageMixin, CreateView):
    model = Proveedor
    template_name = "Facturacion/Proveedor/crear_proveedor.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor')
    success_message = 'Proveedor registrado con exito'


def listar_proveedores(request):
    lista_proveedores = Proveedor.objects.all()
    contexto = {'proveedores': lista_proveedores}
    return render(request, "Facturacion/Proveedor/listar_proveedores.html", contexto)


class ListarProveedores(ListView):
    model = Proveedor
    template_name = "Facturacion/Proveedor/listar_proveedores.html"


def editar_proveedores(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == 'GET':
        form = ProveedorEditarForm(instance=proveedor)
    else:
        form = ProveedorEditarForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save
        return redirect('listaproveedores')
    return render(request, 'Facturacion/Proveedor/editar_proveedor.html', {'form': form})


class ActualizarProveedores(UpdateView):
    model = Proveedor
    form_class = ProveedorEditarForm
    template_name = "Facturacion/Proveedor/editar_proveedor.html"
    success_url = reverse_lazy('listaproveedores')


def eliminar_proveedores(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listaproveedores')
    return render(request, 'Facturacion/Proveedor/eliminar_proveedor.html', {'proveedor': proveedor})


class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = 'Facturacion/Proveedor/detalle_proveedor.html'


##########################################################################################################
# Producto
class RegistroProducto(SuccessMessageMixin, CreateView):
    model = Producto
    template_name = "Facturacion/Producto/crear_producto.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto')
    success_message = 'Producto registrado con exito'


def listar_productos(request):
    lista_productos = Producto.objects.all()
    contexto = {'productos': lista_productos}
    return render(request, "Facturacion/Producto/listar_productos.html", contexto)


class ListarProductos(ListView):
    model = Producto
    template_name = "Facturacion/Producto/listar_productos.html"


def editar_productos(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        form = ProductoEditarForm(instance=producto)
    else:
        form = ProductoEditarForm(request.POST, instance=producto)
        if form.is_valid():
            form.save
        return redirect('listaproductos')
    return render(request, 'Facturacion/Producto/editar_producto.html', {'form': form})


def eliminar_productos(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('listaproductos')
    return render(request, 'Facturacion/Producto/eliminar_producto.html', {'producto': producto})


class ActualizarProductos(UpdateView):
    model = Producto
    form_class = ProductoEditarForm
    template_name = "Facturacion/Producto/editar_producto.html"
    success_url = reverse_lazy('listaproductos')


class DetalleProducto(DetailView):
    model = Producto
    template_name = 'Facturacion/Producto/detalle_producto.html'


#################################################################################################################
# Categoria
class RegistroCategoria(SuccessMessageMixin, CreateView):
    model = Categoria
    template_name = "Facturacion/Categoria/crear_categoria.html"
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria')
    success_message = 'Categoria registrada con exito'


def listar_categorias(request):
    lista_categorias = Categoria.objects.all()
    contexto = {'categorias': lista_categorias}
    return render(request, "Facturacion/Categoria/listar_categorias.html", contexto)


class ListarCategorias(ListView):
    model = Categoria
    template_name = "Facturacion/Categoria/listar_categorias.html"


def editar_categorias(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'GET':
        form = CategoriaEditarForm(instance=categoria)
    else:
        form = CategoriaEditarForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save
        return redirect('listacategorias')
    return render(request, 'Facturacion/Categoria/editar_categoria.html', {'form': form})


def eliminar_categorias(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listacategorias')
    return render(request, 'Facturacion/Categoria/eliminar_categoria.html', {'categoria': categoria})


class ActualizarCategorias(UpdateView):
    model = Categoria
    form_class = CategoriaEditarForm
    template_name = "Facturacion/Categoria/editar_categoria.html"
    success_url = reverse_lazy('listacategorias')


####################################################################################################
# Presentacion
class RegistroPresentacion(SuccessMessageMixin, CreateView):
    model = Presentacion
    template_name = "Facturacion/Presentacion/crear_presentacion.html"
    form_class = PresentacionForm
    success_url = reverse_lazy('presentacion')
    success_message = 'Presentacion registrada con exito'


def listar_presentaciones(request):
    lista_presentaciones = Presentacion.objects.all()
    contexto = {'presentaciones': lista_presentaciones}
    return render(request, "Facturacion/Presentacion/listar_presentaciones.html", contexto)


class ListarPresentaciones(ListView):
    model = Presentacion
    template_name = "Facturacion/Presentacion/listar_presentaciones.html"


def editar_presentaciones(request, id_presentacion):
    presentacion = Presentacion.objects.get(id=id_presentacion)
    if request.method == 'GET':
        form = PresentacionEditarForm(instance=presentacion)
    else:
        form = PresentacionEditarForm(request.POST, instance=presentacion)
        if form.is_valid():
            form.save
        return redirect('listapresentaciones')
    return render(request, 'Facturacion/Presentacion/editar_presentacion.html', {'form': form})


def eliminar_presentaciones(request, id_presentacion):
    presentacion = Presentacion.objects.get(id=id_presentacion)
    if request.method == 'POST':
        presentacion.delete()
        return redirect('listapresentaciones')
    return render(request, 'Facturacion/Presentacion/eliminar_presentacion.html', {'presentacion': presentacion})


class ActualizarPresentaciones(UpdateView):
    model = Presentacion
    form_class = PresentacionEditarForm
    template_name = "Facturacion/Presentacion/editar_presentacion.html"
    success_url = reverse_lazy('listapresentaciones')


#######################################################################################################
# Usuario
class RegistroUsuario(SuccessMessageMixin, CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "Facturacion/Usuarios/crear_usuario.html"
    success_url = reverse_lazy('usuario')
    success_message = 'Usuario registrado con exito'


def listar_usuarios(request):
    lista_usuarios = User.objects.all()
    contexto = {'user': lista_usuarios}
    return render(request, "Facturacion/Usuarios/listar_usuarios.html", contexto)


class ListarUsuarios(ListView):
    model = User
    template_name = "Facturacion/Usuarios/listar_usuarios.html"


def editar_usuarios(request, id_user):
    usuario = User.objects.get(id=id_user)
    if request.method == 'GET':
        form = UsuarioEditarForm(instance=usuario)
    else:
        form = UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save
        return redirect('listausuarios')
    return render(request, 'Facturacion/Usuarios/editar_usuario.html', {'form': form})


def eliminar_usuarios(request, id_user):
    usuario = User.objects.get(id=id_user)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listausuarios')
    return render(request, 'Facturacion/Usuarios/eliminar_usuario.html', {'usuario': usuario})


class ActualizarUsuarios(UpdateView):
    model = User
    form_class = UsuarioEditarForm
    template_name = "Facturacion/Usuarios/editar_usuario.html"
    success_url = reverse_lazy('listausuarios')


##############################################################################
###########						 		COMPRAS						##########
##############################################################################
class RegistroCompra(SuccessMessageMixin, CreateView):
    model = Compra
    template_name = "Facturacion/Compra/crear_compra.html"
    form_class = CompraForm
    success_url = reverse_lazy('compra')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        compra_pagos_form_set = CompraPagosFormSet()
        return self.render_to_response(self.get_context_data(form=form,
                                                             compra_pagos_form_set=compra_pagos_form_set))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        compra_pagos_form_set = CompraPagosFormSet(request.POST)
        if form.is_valid() and compra_pagos_form_set.is_valid():
            messages.success(request, 'Compra registrada con exito')
            return self.form_valid(form, compra_pagos_form_set)
        else:
            return self.form_invalid(form, compra_pagos_form_set)

    def form_valid(self, form, compra_pagos_form_set):
        self.object = form.save()
        compra_pagos_form_set.instance = self.object
        compra_pagos_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, compra_pagos_form_set):
        return self.render_to_response(self.get_context_data(form=form,
                                                             compra_pagos_form_set=compra_pagos_form_set))


class ListarCompras(ListView):
    model = Compra
    template_name = "Facturacion/Compra/listar_compras.html"


class DetalleCompraView(DetailView):
    model = Compra
    template_name = 'Facturacion/Compra/detalle_compra.html'


class AgregarDetalleCompra(BSModalCreateView):
    template_name = 'Facturacion/Compra/agregar_detalle_compra.html'
    form_class = DetalleCompraForm
    print("LLamada al metodo del views.py")
    success_url = reverse_lazy('compra')


@csrf_exempt
def agregaProductoTabla(request):
    cantidad = int(request.POST['cantidad'])
    pkProducto = int(request.POST['pkProducto'])
    producto = Producto.objects.get(pk=pkProducto)
    resul = [{
        'pk': producto.pk,
        'nombre_producto': producto.nombre_producto,
        'cantidad': cantidad,
    }]

    data = json.dumps(resul, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


class ActualizarCompra(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = "Facturacion/Compra/editar_compra.html"
    success_url = reverse_lazy('listacompras')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        compra_pagos_form_set = CompraPagosEditFormSet(instance=self.object)
        messages.success(request, '')
        return self.render_to_response(self.get_context_data(form=form,
                                                             compra_pagos_form_set=compra_pagos_form_set))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        compra_pagos_form_set = CompraPagosEditFormSet(self.request.POST, instance=self.object)
        if form.is_valid() and compra_pagos_form_set.is_valid():
            messages.success(request, 'Compra actualizada con exito')
            return self.form_valid(form, compra_pagos_form_set)
        else:
            return self.form_invalid(form, compra_pagos_form_set)

    def form_valid(self, form, compra_pagos_form_set):
        self.object = form.save()
        compra_pagos_form_set.instance = self.object
        compra_pagos_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, compra_pagos_form_set):
        return self.render_to_response(self.get_context_data(form=form,
                                                             compra_pagos_form_set=compra_pagos_form_set))


def eliminar_compra(request, id_compra):
    compra = Compra.objects.get(id=id_compra)
    if request.method == 'POST':
        compra.delete()
        messages.success(request, 'Compra eliminada con exito')
        return redirect('listacompras')
    return render(request, 'Facturacion/Compra/eliminar_compra.html', {'compra': compra})


def generarCodigo7():
    code = str(int(random.random() * 10000000))
    if len(code) < 7:
        for i in range(7 - len(code)):
            code = '0' + code
    return code


class BuscarProveedor(ListView):
    model = Proveedor
    template_name = "Facturacion/Compra/compra.html"


def realizarCompra(request, template_name='Facturacion/Compra/compra.html'):
    productos = Producto.objects.filter().exclude(stock=0)
    data = {'productos': productos, 'numeroCompra': generarCodigo7()}
    return render(request, template_name, data)


@csrf_exempt
def cargarProveedor(request):
    ruc = request.POST['ruc']
    proveedor = Proveedor.objects.filter(ruc=ruc).values()
    data = json.dumps(list(proveedor), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


##############################################################################
###########						 		PAGOS						##########
##############################################################################
class ListarPagos(ListView):
    model = Pago
    template_name = "Facturacion/Pago/listar_pagos.html"


class DetallePago(DetailView):
    model = Pago
    template_name = 'Facturacion/Pago/detalle_pago.html'


class ActualizarPago(SuccessMessageMixin, UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = "Facturacion/Pago/editar_pago.html"
    success_url = reverse_lazy('listapagos')
    success_message = 'Pago actualizado con exito'


def eliminar_pago(request, id_pago):
    pago = Pago.objects.get(id=id_pago)
    if request.method == 'POST':
        pago.delete()
        messages.success(request, 'Pago eliminado con exito')
        return redirect('listapagos')
    return render(request, 'Facturacion/Pago/eliminar_pago.html', {'pago': pago})


#####################################################################################################
# Venta
def generarCodigo8():
    code = str(int(random.random() * 10000000))
    if len(code) < 8:
        for i in range(8 - len(code)):
            code = '0' + code
    return code


class BuscarCliente(ListView):
    model = Cliente
    template_name = "Facturacion/Factura/factura.html"


def realizarVenta(request, template_name='Facturacion/Factura/factura.html'):
    productos = Producto.objects.filter().exclude(stock=0)
    data = {'productos': productos, 'numeroFactura': generarCodigo8()}
    return render(request, template_name, data)


def listarVentas(request, template_name='Facturacion/Factura/listar_facturas.html'):
    facturas = Factura.objects.all()
    data = {'facturas': facturas}
    return render(request, template_name, data)


@csrf_exempt
def cargarCliente(request):
    cedula = request.POST['cedula']
    cliente = Cliente.objects.filter(cedula=cedula).values()
    data = json.dumps(list(cliente), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def cargarProductos(request):
    productos = Producto.objects.filter().exclude(stock=0).values('id', 'nombre_producto', 'codigo_producto', 'stock')
    data = json.dumps(list(productos), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def obtenerProducto(request):
    cantidad = int(request.POST['cantidad'])
    presentacion = int(request.POST['presentacion'])
    pkProducto = int(request.POST['pkProducto'])
    producto = Producto.objects.get(pk=pkProducto)
    tipoArticulo = request.POST['tipoArticulo']

    valorUnit = 0
    # valorUnit= producto.precio_producto

    # seleciono unidad
    if (presentacion == 0):
        valorUnit = producto.precio_producto
    # caso contrario selecciono caja
    else:
        valorUnit = producto.valor_venta_cajas

    # valorCajas = producto.valor_venta_cajas
    valorIva = valorUnit * Decimal(0.12)
    # valorIvaCaja = valorCajas * Decimal(0.12)
    valoUnitSinIva = valorUnit
    # valorCajasSinIva = valorCajas - valorIvaCaja

    if (tipoArticulo == 'OTRO'):
        sTotal = round(cantidad * valoUnitSinIva, 2)
        iva = round(sTotal * 0.12, 2)
        pvpIva = round(sTotal + iva, 2)
    else:
        sTotal = round(cantidad * valoUnitSinIva, 2)
        iva = 0
        pvpIva = round(sTotal + iva, 2)

    # calcular el valor del IVA de la cantidad*precio_venta

    resul = [{
        'pk': producto.pk, 'cantidad': cantidad,  # 'presentacion': presentacion,
        'nombre_producto': producto.nombre_producto,
        'precio_producto': round(valoUnitSinIva, 2, ), 'valorIva': round(valorIva, 2),
        # 'valor_venta_cajas': round(valorCajasSinIva, 2,), 'valorIvaCaja':round(valorIvaCaja, 2),
        'valor_venta': round(cantidad * valoUnitSinIva, 2),
        'IVA': iva,
        'PVP_IVA': pvpIva,
        # 'valor_venta': producto.valor_venta_cajas,
        'valtotalIva': round(cantidad * valorUnit, 2),
    }]
    data = json.dumps(resul, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def guardarVenta(request):
    pkCliente = int(request.POST['pkCliente'])

    tipoPago = request.POST['tipoPago']

    nroFactura = Decimal(request.POST['nroFactura'])
    detalleVenta = json.loads(request.POST['detalleVenta'])
    subtotal = Decimal(request.POST['subtotal'])
    descuento = Decimal(request.POST['descuento'])
    iva12 = Decimal(request.POST['iva12'])
    valorTotal = Decimal(request.POST['valorTotal'])

    factura = Factura(numero=nroFactura, tipoPago=tipoPago, cliente_id=pkCliente,
                      subtotal=subtotal, descuento=descuento, iva12=iva12,
                      valorTotal=valorTotal, pagado=True)
    factura.save()

    for det in detalleVenta:
        pro = Producto.objects.get(pk=det[1])
        detFac = DetalleFactura(cantidad=det[0], concepto=pro.nombre_producto, valorUnitario=pro.precio_producto,
                                valorTotal=Decimal(det[2]), producto=pro)
        detFac.save()
        pro.stock = pro.stock - detFac.cantidad  # Se reduce del stock
        pro.save()

        factura.detalleFactura.add(detFac)

    data = json.dumps(list(), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def imprimirFactura(request, pk, template_name='Facturacion/Factura/pdf_factura.html'):
    factura = Factura.objects.get(pk=pk)
    detallesFactura = factura.detalleFactura.all()
    data = {'factura': factura, 'detallesFactura': detallesFactura}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Factura' + factura.numero + '.pdf"'
    # find the template and render it.
    template = get_template(template_name)
    html = template.render(data)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html.encode("ISO-8859-1"), dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class AnularFactura(DetailView):
    model = Factura
    template_name = 'Facturacion/Factura/anular_factura.html'


# REPORTES
def reporte_ventas(request):
    return render(request, "Facturacion/Reportes/reporte_ventas.html", {})


@csrf_exempt
def listar_reporte_ventas(request):
    facturas = Factura.objects.all()
    ventas = [ventas_serializer(factura) for factura in facturas]
    return HttpResponse(json.dumps(ventas, cls=DjangoJSONEncoder), content_type='application/json')


@csrf_exempt
def generar_reporte_ventas(request):
    fInicio = datetime.strptime(request.POST['fInicio'], '%Y-%m-%d')
    fFin = datetime.strptime(request.POST['fFin'], '%Y-%m-%d')
    facturas = Factura.objects.filter(fecha__range=(fInicio, fFin))
    ventas = [ventas_serializer(factura) for factura in facturas]
    return HttpResponse(json.dumps(ventas, cls=DjangoJSONEncoder), content_type='application/json')


def ventas_serializer(venta):
    return {'numFactura': venta.numero, 'cliente': venta.cliente.apellidos + ' ' + venta.cliente.nombres,
            'fecha': venta.fecha, 'total': venta.valorTotal}


def reporte_producto(request):
    form = ReporteProductosForm()
    return render(request, "Facturacion/Reportes/reporte_productos.html", {'form': form})


@csrf_exempt
def generar_reporte_productos(request):
    proveedor = request.POST['proveedor']
    productos = Producto.objects.filter(casa_comercial__id=proveedor)
    productosSer = [productos_serializer(producto) for producto in productos]
    return HttpResponse(json.dumps(productosSer, cls=DjangoJSONEncoder), content_type='application/json')


def productos_serializer(producto):
    return {'nombreComercial': producto.nombre_producto, 'nombreGenerico': producto.nombre_generico,
            'fechaExpiracion': producto.fecha_expiracion, 'stock': producto.stock}


@csrf_exempt
def listar_reporte_productos(request):
    productos = Producto.objects.all()
    inventario = [inventario_serializer(productos) for producto in productos]
    return HttpResponse(json.dumps(inventario, cls=DjangoJSONEncoder), content_type='application/json')


def inventario_serializer(venta):
    return {'nombreco': inventario.nombre_producto, 'nombrege': inventario.nombre_generico,
            'fechaex': inventario.fecha_expiracion, 'stock': inventario.stock}


class ReporteClientesPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.MEDIA_ROOT + '/Imagenes/farmacia1.png'
        pdf.drawImage(archivo_imagen, 50, 740, 200, 80, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(300, 780, u"REPORTE DE CLIENTES")

    def tabla(self, pdf, y):
        encabezados = ('Cédula/Ruc', 'Nombres', 'Apellidos', 'Dirección', 'Teléfono')
        detalles = [(cliente.cedula, cliente.nombres, cliente.apellidos, cliente.direccion, cliente.telefono) for
                    cliente in Cliente.objects.all()]
        detalle_orden = Table([encabezados] + detalles, colWidths=[3 * cm, 3 * cm, 3 * cm, 5 * cm, 2.5 * cm, ])
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60, y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Reporte Clientes' + '.pdf"'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=landscape(A4))
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


class ReporteProveedores(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.MEDIA_ROOT + '/Imagenes/farmacia1.png'
        pdf.drawImage(archivo_imagen, 50, 740, 200, 80, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(300, 780, u"REPORTE DE PROVEEDORES")

    def tabla(self, pdf, y):
        encabezadospro = ('Ruc', 'Distribuidora', 'Empresa', 'Dirección', 'Teléfono empresa')
        detallespro = [
            (proveedor.ruc, proveedor.distribuidora, proveedor.empresa, proveedor.direccion, proveedor.telefono_empresa)
            for proveedor in Proveedor.objects.all()]
        detalle_ordenpro = Table([encabezadospro] + detallespro,
                                 colWidths=[3 * cm, 3 * cm, 2.5 * cm, 8 * cm, 3.5 * cm, ])
        detalle_ordenpro.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_ordenpro.wrapOn(pdf, 500, 90)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_ordenpro.drawOn(pdf, 20, y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment: filename=Clientes Registrados.pdf'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


class ReporteVentasPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.MEDIA_ROOT + '/Imagenes/farmacia1.png'
        pdf.drawImage(archivo_imagen, 50, 740, 200, 80, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(300, 780, u"REPORTE DE VENTAS")

    def tabla(self, pdf, y, fInicio, fFinal):
        encabezados = ('Factura N°', 'Cliente', 'Fecha', 'Total')
        detalles = [(factura.numero, factura.cliente.apellidos + ' ' + factura.cliente.nombres, factura.fecha,
                     factura.valorTotal) for factura in Factura.objects.filter(fecha__range=(fInicio, fFinal))]

        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 7 * cm, 6 * cm, 2.5 * cm, ])
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60, y)

    def get(self, request, *args, **kwargs):
        fInicio = datetime.strptime(request.GET['fInicio'], '%Y-%m-%d')
        fFinal = datetime.strptime(request.GET['fFinal'], '%Y-%m-%d')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Reporte Ventas' + '.pdf"'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y, fInicio, fFinal)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


# Order purchase business


def create_purchase(request):
    if request.POST:
        if (request.POST.get('provider_select') is not None and
                request.POST.get('order_number') is not None):
            details_purchase = json.loads(request.POST.get('details_hidden'))
            purchase = Compra()
            provider = Proveedor.objects.get(id=request.POST.get('provider_select'))

            purchase.descripcion = ''
            purchase.estadoPago = request.POST.get('status')
            purchase.fechaCompra = request.POST.get('purchase_date')
            purchase.fechaLimite = request.POST.get('date_limit_to_pay')
            purchase.formaPago = request.POST.get('how_to_pay_select')
            purchase.numCompra = request.POST.get('order_number')
            purchase.numFactura = request.POST.get('invoice_number')
            purchase.plazoPago = request.POST.get('payment_deadline')
            purchase.proveedor_id = provider.id
            purchase.totalCompra = request.POST.get('purchase_total')
            purchase.save()

            for detail_purchase in details_purchase:
                detail = DetalleCompra()
                detail.cantidad = int(detail_purchase[u'detail_quantity'])
                detail.compra_id = purchase.id
                detail.producto_id = int(detail_purchase[u'product_id'])
                detail.save()
            messages.success(request, 'Orden de compra exitosa.')

    details = []
    providers = Proveedor.objects.all()
    how_to_pay_list = ['CONTADO', 'CREDITO']
    status = ['REGISTRADO', 'PAGADO']
    products = Producto.objects.filter(stock__gte=0)
    return render(request, 'Facturacion/Compra/create_order_purchase.html', locals())


@csrf_exempt
def add_detail_to_order_purchase(request):
    if request.POST:
        product = Producto.objects.get(id=request.POST.get('product_id'))
        detail_quantity = request.POST.get('detail_quantity')
        if product is None and detail_quantity > 0:
            return JsonResponse({})
        detail_total = product.precio_producto * int(detail_quantity)
        detail = {
            "detail_quantity": detail_quantity,
            "product_name": product.nombre_producto,
            "product_price": product.precio_producto,
            "detail_total": detail_total,
            "product_id": product.id
        }
    return JsonResponse(detail)
