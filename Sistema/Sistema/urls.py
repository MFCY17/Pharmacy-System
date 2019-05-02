"""Sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
# Login
from django.contrib.auth.views import logout_then_login

from Farmacia import views
from Farmacia.views import ActualizarCategorias
from Farmacia.views import ActualizarClientes
from Farmacia.views import ActualizarCompra
from Farmacia.views import ActualizarPago
from Farmacia.views import ActualizarPresentaciones
from Farmacia.views import ActualizarProductos
from Farmacia.views import ActualizarProveedores
from Farmacia.views import ActualizarUsuarios
from Farmacia.views import AgregarDetalleCompra
from Farmacia.views import AnularFactura
from Farmacia.views import DetalleCliente
from Farmacia.views import DetalleCompra
from Farmacia.views import DetallePago
from Farmacia.views import DetalleProducto
from Farmacia.views import DetalleProveedor
from Farmacia.views import ListarCategorias
from Farmacia.views import ListarClientes
# Compra
from Farmacia.views import ListarCompras
# Pago
from Farmacia.views import ListarPagos
from Farmacia.views import ListarPresentaciones
from Farmacia.views import ListarProductos
from Farmacia.views import ListarProveedores
from Farmacia.views import ListarUsuarios
# Categoria
from Farmacia.views import RegistroCategoria
# Cliente
from Farmacia.views import RegistroCliente
from Farmacia.views import RegistroCompra
# Presentacion
from Farmacia.views import RegistroPresentacion
# Producto
from Farmacia.views import RegistroProducto
# Proveedor
from Farmacia.views import RegistroProveedor
# Usuario
from Farmacia.views import RegistroUsuario
# REPORTES
from Farmacia.views import ReporteClientesPDF
from Farmacia.views import ReporteProveedores
from Farmacia.views import ReporteVentasPDF
from Farmacia.views import agregaProductoTabla
from Farmacia.views import cargarCliente
from Farmacia.views import cargarProductos
from Farmacia.views import cargarProveedor
from Farmacia.views import generar_reporte_productos
from Farmacia.views import generar_reporte_ventas
from Farmacia.views import guardarVenta
from Farmacia.views import imprimirFactura
from Farmacia.views import listarVentas
from Farmacia.views import listar_reporte_productos
from Farmacia.views import listar_reporte_ventas
from Farmacia.views import obtenerProducto
from Farmacia.views import realizarCompra
# Venta
from Farmacia.views import realizarVenta
from Farmacia.views import validar_rol

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Login
    url(r'^$', login, {'template_name': 'Facturacion/Login/login.html'}, name='login'),
    url(r'^accounts/login', login, {'template_name': 'Facturacion/Login/login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),

    # Restablecer Contrasena
    url(r'^reset/password_reset$', password_reset,
        {'template_name': 'Facturacion/Login/registration/password_reset_form.html',
         'email_template_name': 'Facturacion/Login/registration/password_reset_email.html'},
        name='password_reset'),
    url(r'^reset/password_reset_done$', password_reset_done,
        {'template_name': 'Facturacion/Login/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'Facturacion/Login/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete,
        {'template_name': 'Facturacion/Login/registration/password_reset_complete.html'},
        name='password_reset_complete'),

    # Base
    url(r'^administracion/', views.base, name='base'),
    # Configuracion
    url(r'^perfil_empresa/', views.perfil_empresa, name='perfil_empresa'),
    url(r'^perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    # Cliente
    url(r'^crear_cliente/', RegistroCliente.as_view(), name='cliente'),
    url(r'^listar_clientes/$', ListarClientes.as_view(), name='listaclientes'),
    url(r'^editar_clientes/(?P<pk>\d+)/$', ActualizarClientes.as_view(), name='editarclientes'),
    url(r'^eliminar_clientes/(?P<id_cliente>\d+)/$', views.eliminar_clientes, name='eliminarclientes'),
    url(r'^detalle_cliente/(?P<pk>\d+)/$', DetalleCliente.as_view(), name='detallecliente'),
    # Proveedor
    url(r'^crear_proveedor/', RegistroProveedor.as_view(), name='proveedor'),
    url(r'^listar_proveedor/$', ListarProveedores.as_view(), name='listaproveedores'),
    url(r'^editar_proveedores/(?P<pk>\d+)/$', ActualizarProveedores.as_view(), name='editarproveedores'),
    url(r'^eliminar_proveedores/(?P<id_proveedor>\d+)/$', views.eliminar_proveedores, name='eliminarproveedores'),
    url(r'^detalle_proveedor/(?P<pk>\d+)/$', DetalleProveedor.as_view(), name='detalleproveedor'),
    # PRODUCTO
    url(r'^crear_producto/', RegistroProducto.as_view(), name='producto'),
    url(r'^listar_producto/$', ListarProductos.as_view(), name='listaproductos'),
    url(r'^editar_productos/(?P<pk>\d+)/$', ActualizarProductos.as_view(), name='editarproductos'),
    url(r'^eliminar_productos/(?P<id_producto>\d+)/$', views.eliminar_productos, name='eliminarproductos'),
    url(r'^detalle_producto/(?P<pk>\d+)/$', DetalleProducto.as_view(), name='detalleproducto'),
    # Categoria
    url(r'^crear_categoria/', RegistroCategoria.as_view(), name='categoria'),
    url(r'^listar_categoria/$', ListarCategorias.as_view(), name='listacategorias'),
    url(r'^editar_categorias/(?P<pk>\d+)/$', ActualizarCategorias.as_view(), name='editarcategorias'),
    url(r'^eliminar_categorias/(?P<id_categoria>\d+)/$', views.eliminar_categorias, name='eliminarcategorias'),
    # Presentacion
    url(r'^crear_presentacion/', RegistroPresentacion.as_view(), name='presentacion'),
    url(r'^listar_presentacion/$', ListarPresentaciones.as_view(), name='listapresentaciones'),
    url(r'^editar_presentacion/(?P<pk>\d+)/$', ActualizarPresentaciones.as_view(), name='editarpresentaciones'),
    url(r'^eliminar_presentaciones/(?P<id_presentacion>\d+)/$', views.eliminar_presentaciones,
        name='eliminarpresentaciones'),
    # Usuario
    url(r'^validar_rol/$', validar_rol, name='validar_rol'),
    url(r'^crear_usuario/', RegistroUsuario.as_view(), name='usuario'),
    url(r'^listar_usuarios/$', ListarUsuarios.as_view(), name='listausuarios'),
    url(r'^editar_usuario/(?P<pk>\d+)/$', ActualizarUsuarios.as_view(), name='editarusuarios'),
    url(r'^eliminar_usuario/(?P<id_user>\d+)/$', views.eliminar_usuarios, name='eliminarusuarios'),
    # Compra
   # url(r'^crear_compra/', RegistroCompra.as_view(), name='compra'),
    url(r'^listar_compras/$', ListarCompras.as_view(), name='listacompras'),
    url(r'^editar_compra/(?P<pk>\d+)/$', ActualizarCompra.as_view(), name='editarcompra'),
    url(r'^eliminar_compra/(?P<id_compra>\d+)/$', views.eliminar_compra, name='eliminarcompra'),
    url(r'^detalle_compra/(?P<pk>\d+)/$', DetalleCompra.as_view(), name='detallecompra'),
    url(r'^cargar_proveedor/$', cargarProveedor, name='cargarproveedor'),
    url(r'^realizar_compra/$', realizarCompra, name='realizarcompra'),
    url(r'^agregar_detalle_compra/$', AgregarDetalleCompra.as_view(), name='agregardetallecompra'),
    url(r'^agregar_producto_tabla/$', agregaProductoTabla, name='agregarproductotabla'),
    # Pago
    url(r'^listar_pagos/$', ListarPagos.as_view(), name='listapagos'),
    url(r'^editar_ppago/(?P<pk>\d+)/$', ActualizarPago.as_view(), name='editarpago'),
    url(r'^eliminar_pago/(?P<id_pago>\d+)/$', views.eliminar_pago, name='eliminarpago'),
    url(r'^detalle_pago/(?P<pk>\d+)/$', DetallePago.as_view(), name='detallepago'),
    # Venta
    url(r'^realizar_venta/$', realizarVenta, name='realizarventa'),
    url(r'^cargar_cliente/$', cargarCliente, name='cargarcliente'),
    url(r'^cargar_productos/$', cargarProductos, name='cargarproductos'),
    url(r'^obtener_producto/$', obtenerProducto, name='obtenerproducto'),
    url(r'^listar_ventas/$', listarVentas, name='listarventas'),
    url(r'^guardar_venta/$', guardarVenta, name='guardarventa'),
    url(r'^imprimir_factura/(?P<pk>\d+)/$', imprimirFactura, name='imprimirfactura'),
    url(r'^anular_factura/(?P<pk>\d+)/$', AnularFactura, name='anularfactura'),
    # REPORTES
    url(r'^reporte_ventas/', views.reporte_ventas, name='reporte_ventas'),
    url(r'^reporte_productos/', views.reporte_producto, name='reporteproductos'),
    url(r'^generar_reporte_productos/$', generar_reporte_productos, name='generar_reporte_productos'),
    url(r'^listar_reporte_ventas/$', listar_reporte_ventas, name='listar_reporte_ventas'),
    url(r'^generar_reporte_ventas/$', generar_reporte_ventas, name='generar_reporte_ventas'),
    url(r'^reporte__cliente$', login_required(ReporteClientesPDF.as_view()), name="reporteclientes"),
    url(r'^reporte__proveedor$', login_required(ReporteProveedores.as_view()), name="reporteproveedores"),
    url(r'^reporte__venta$', login_required(ReporteVentasPDF.as_view()), name="reporteventas"),
    url(r'^api/v1/', include('Farmacia.urls', namespace="Farmacia")),
    url(r'^listar_reporte_productos/$', listar_reporte_productos, name='listar_reporte_productos'),
    #order purchase
    url(r'^create_purchase/$', views.create_purchase, name='crear_orden_compra'),

]

urlpatterns += [
    # url(r'^api/v1/auth', include('rest_framework.urls', namespace = 'rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
