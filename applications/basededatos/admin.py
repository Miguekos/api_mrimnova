from django.contrib import admin
from .models import ClientModel, MonitoreoModel
# Register your models here.


admin.site.register(ClientModel)
admin.site.register(MonitoreoModel)
