
from django.contrib import admin
from core.models.producto import Producto, Categoria, Ingrediente
from core.models.pedido import Pedido, DetallePedido
from core.models.combo import Combo, ComboProducto
from core.models.personalizacion import Personalizacion, DetalleAdicional
from core.models.dispositivo import DispositivoDeAutoservicio


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')  # Columnas visibles en la lista
    search_fields = ('nombre',)  # Campo de búsqueda


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'precio', 'id_categoria')
    search_fields = ('nombre',)
    list_filter = ('id_categoria',)  # Filtros en la barra lateral


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id_ingrediente', 'nombre', 'categoria', 'precio')
    search_fields = ('nombre', 'categoria')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'tipo', 'fecha', 'hora', 'estado', 'id_pago', 'id_dispositivo')
    search_fields = ('estado', 'tipo')
    list_filter = ('estado', 'tipo')


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('id_datallepedido', 'id_producto', 'id_pedido', 'cantidad', 'total')
    search_fields = ('id_pedido__id_pedido',)
    list_filter = ('id_pedido',)


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('id_combo', 'nombre', 'precio')
    search_fields = ('nombre',)


@admin.register(ComboProducto)
class ComboProductoAdmin(admin.ModelAdmin):
    list_display = ('id_combo', 'id_producto', 'cantidad')
    search_fields = ('id_combo__nombre', 'id_producto__nombre')


@admin.register(Personalizacion)
class PersonalizacionAdmin(admin.ModelAdmin):
    list_display = ('id_personalizacion', 'id_producto', 'tipo', 'precio_adicional')
    search_fields = ('tipo',)


@admin.register(DetalleAdicional)
class DetalleAdicionalAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_adicional', 'id_producto_ingrediente', 'id_personalizacion', 'precio_adicional_total')
    search_fields = ('id_personalizacion__id_producto__nombre',)


@admin.register(DispositivoDeAutoservicio)
class DispositivoDeAutoservicioAdmin(admin.ModelAdmin):
    list_display = ('id_dispositivo', 'estado', 'ubicacion', 'cliente')
    search_fields = ('ubicacion', 'cliente')
