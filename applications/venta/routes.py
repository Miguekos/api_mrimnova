from rest_framework.routers import DefaultRouter

from django.conf.urls.static import static
from django.conf import settings

from . import viewssets

router = DefaultRouter()

router.register(r'mrinnova/v2/ventas', viewssets.VentasViewsetNew, basename='ventas')

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# empty line
