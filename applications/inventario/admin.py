from django.contrib import admin
from .models import ProductModel, ServiceModel, FacturaModel, ProveedoresModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ServiceModel)
admin.site.register(FacturaModel)
admin.site.register(ProveedoresModel)