from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from . import viewssets

router = DefaultRouter()

# router.register(r'mobilestore/v2/colors', viewssets.ColorViewset, basename='colors')
router.register(r'mrinnova/v2/usuarios', viewssets.UserCreate, basename='create_usuarios')
router.register(r'mrinnova/v2/login', viewssets.LoginViewset, basename='login_usuarios')
# router.register(r'mrinnova/v2/loing-drf', views.obtain_auth_token, basename='obtain_auth_token')

urlpatterns = router.urls

# empty line
