from django.contrib import admin
from core.models.producto import Producto, Categoria, Ingrediente
from core.models.pedido import Pedido, DetallePedido
from core.models.combo import Combo, ComboProducto
from core.models.personalizacion import Personalizacion, DetalleAdicional
from core.models.dispositivo import DispositivoDeAutoservicio


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'precio', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')
    search_fields = ('nombre',)


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id_ingrediente', 'nombre', 'precio', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'tipo', 'fecha', 'hora', 'estado', 'pago', 'dispositivo')
    search_fields = ('tipo',)
    list_filter = ('estado', 'fecha')


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('id_datallepedido', 'pedido', 'producto', 'cantidad', 'total')
    search_fields = ('pedido__id_pedido',)
    list_filter = ('producto',)


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('id_combo', 'nombre', 'precio')
    search_fields = ('nombre',)


@admin.register(ComboProducto)
class ComboProductoAdmin(admin.ModelAdmin):
    list_display = ('combo', 'producto', 'cantidad')
    search_fields = ('combo__nombre', 'producto__nombre')


@admin.register(Personalizacion)
class PersonalizacionAdmin(admin.ModelAdmin):
    list_display = ('id_personalizacion', 'producto', 'tipo', 'precio_adicional')
    search_fields = ('tipo',)


@admin.register(DetalleAdicional)
class DetalleAdicionalAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_adicional', 'producto_ingrediente', 'personalizacion', 'combo', 'precio_adicional_total')
    search_fields = ('personalizacion__tipo',)


@admin.register(DispositivoDeAutoservicio)
class DispositivoDeAutoservicioAdmin(admin.ModelAdmin):
    list_display = ('id_dispositivo', 'estado', 'ubicacion', 'cliente')
    search_fields = ('ubicacion', 'cliente')
    list_filter = ('estado',)
