# importar UserCreate
from rest_framework.routers import DefaultRouter

from . import viewssets

router = DefaultRouter()

router.register('v3/usuarios/', viewssets.UserCreate, basename='usuario_crear')

urlpatterns = router.urls
