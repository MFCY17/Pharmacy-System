# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cliente
from .models import Proveedor
from .models import Producto
from .models import Categoria
from .models import Presentacion
from .models import Pago
from .models import Compra
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Presentacion)
admin.site.register(Pago)
admin.site.register(Compra)