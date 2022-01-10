from rest_framework.routers import DefaultRouter

from . import viewssets

router = DefaultRouter()

router.register(r'mrinnova/v2/personal', viewssets.PersonalViewset, basename='personal')

urlpatterns = router.urls

# empty line
