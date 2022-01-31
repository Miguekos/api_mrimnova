from rest_framework.routers import DefaultRouter

from . import viewssets

router = DefaultRouter()


router.register(r'mrinnova/v2/servicios', viewssets.ServiceViewset, basename='servicios')
router.register(r'mrinnova/v2/productos', viewssets.ProductViewset, basename='productos')
router.register(r'mrinnova/v2/facturas', viewssets.InvoiceViewset, basename='facturas')
router.register(r'mrinnova/v2/proveedores', viewssets.ProveeViewset, basename='proveedores')

urlpatterns = router.urls

# empty line
