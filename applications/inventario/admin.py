from django.contrib import admin
from .models import ProductModel, ServiceModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ServiceModel)