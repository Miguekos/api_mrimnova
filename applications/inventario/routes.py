from rest_framework.routers import DefaultRouter

from . import viewssets

router = DefaultRouter()

# router.register(r'mobilestore/v2/colors', viewssets.ColorViewset, basename='colors')
router.register(r'mrinnova/v2/productos', viewssets.ProductViewset, basename='productos')

urlpatterns = router.urls

# empty line
