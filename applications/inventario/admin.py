from django.contrib import admin
from .models import ProductModel, ServiceModel, FacturaModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ServiceModel)
admin.site.register(FacturaModel)