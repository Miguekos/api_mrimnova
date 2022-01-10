from django.db import models
from applications.basededatos.models import ClientModel
from applications.inventario.models import ProductModel, ServiceModel
# Create your models here.

class VentasModelo(models.Model):
    client = models.ForeignKey(ClientModel, related_name='ventas_cliente', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        ProductModel
    )
    services = models.ManyToManyField(
        ServiceModel
    )
    client_visits_report = models.CharField(
        'Reporte de Visitas de Clientes',
        max_length=350
    )
    commissions = models.CharField(
        'Comisiones',
        max_length=50
    )
    # TODO: modelo de factura
    reference_guides = models.CharField(
        'Guias de remisión',
        max_length=50
    )
    date_received = models.DateTimeField(auto_now_add=True)