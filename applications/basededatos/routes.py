from rest_framework.routers import DefaultRouter

from . import viewssets

router = DefaultRouter()

router.register(r'mrinnova/v2/clientes', viewssets.ClintesViewsetNew, basename='clientes')

urlpatterns = router.urls

# empty line
