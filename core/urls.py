from rest_framework.routers import DefaultRouter
from core.views.producto_views import ProductoViewSet, CategoriaViewSet, IngredienteViewSet
from core.views.pedido_views import PedidoViewSet, DetallePedidoViewSet
from core.views.combo_views import ComboViewSet, ComboProductoViewSet
from core.views.personalizacion_views import PersonalizacionViewSet, DetalleAdicionalViewSet
from core.views.dispositivo_views import DispositivoDeAutoservicioViewSet

router = DefaultRouter()

# producto, categoría, ingrediente
router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'ingredientes', IngredienteViewSet, basename='ingredientes')

# pedido
router.register(r'pedidos', PedidoViewSet, basename='pedidos')
router.register(r'detalle-pedidos', DetallePedidoViewSet, basename='detalle-pedidos')

# combo
router.register(r'combos', ComboViewSet, basename='combos')
router.register(r'combo-productos', ComboProductoViewSet, basename='combo-productos')

# personalizacion
router.register(r'personalizaciones', PersonalizacionViewSet, basename='personalizaciones')
router.register(r'detalle-adicionales', DetalleAdicionalViewSet, basename='detalle-adicionales')

# dispositivo
router.register(r'dispositivos', DispositivoDeAutoservicioViewSet, basename='dispositivos')

urlpatterns = router.urls
