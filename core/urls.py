from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.views.producto_views import ProductoViewSet, CategoriaViewSet, IngredienteViewSet
from core.views.pedido_views import PedidoViewSet, DetallePedidoViewSet
from core.views.combo_views import ComboViewSet, ComboProductoViewSet
from core.views.personalizacion_views import PersonalizacionViewSet, DetalleAdicionalViewSet
from core.views.dispositivo_views import DispositivoViewSet
from core.views.producto_ingrediente_views import ProductoIngredienteViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalle-pedidos', DetallePedidoViewSet)
router.register(r'combos', ComboViewSet)
router.register(r'combo-productos', ComboProductoViewSet)
router.register(r'personalizaciones', PersonalizacionViewSet)
router.register(r'detalle-adicionales', DetalleAdicionalViewSet)
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'producto-ingredientes', ProductoIngredienteViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
