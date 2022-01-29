from django.db import models
from django.db.models import ForeignKey
from .managers import VentasManager
from applications.basededatos.models import ClientModel
from applications.inventario.models import ProductModel, ServiceModel


# Create your models here.

class VentasModelo(models.Model):
    type_method_products_choise = (
        ('0', 'Contado'),
        ('1', 'Credito')
    )
    type_method_services_choise = (
        ('0', 'Contado'),
        ('1', 'Credito')
    )
    type_sales_choise = (
        ('0', 'Servicios Generales (Obras)'),
        ('1', 'Productos y Servicios (Video Vigilancia)')
    )
    client = models.ForeignKey(ClientModel, related_name='ventas_cliente', on_delete=models.CASCADE)
    type_sales = models.CharField(
        'Tipo de venta',
        max_length=2,
        choices=type_sales_choise
    )
    contracts = models.ImageField(
        'Contrato Firmado',
        upload_to='contratos',
        default=None
    )  # imagen principal del producto
    address = models.CharField(
        'Direccion',
        max_length=20
    )
    products = models.ManyToManyField(
        ProductModel,
        blank=True
    )
    type_method_products = models.CharField(
        'Tipo pago producto',
        max_length=2,
        choices=type_method_products_choise,
        null=True,
        blank=True
    )
    down_payment_producto_cre = models.CharField(
        'Cuota Inicial Productos',
        max_length=20,
        null=True,
        blank=True
    )
    quotas_producto_cre = models.CharField(
        'Cant. Cuotas Productos',
        max_length=20,
        null=True,
        blank=True
    )
    services = models.ManyToManyField(
        ServiceModel,
        blank=True
    )
    type_method_services = models.CharField(
        'Tipo pago Servicio',
        max_length=2,
        choices=type_method_services_choise,
        null=True,
        blank=True
    )
    down_payment_servicios_cre = models.CharField(
        'Cuota Inicial Servicio',
        max_length=20,
        null=True,
        blank=True
    )
    quotas_servicios_cre = models.CharField(
        'Cant. Cuotas Servicio',
        max_length=20,
        null=True,
        blank=True
    )
    bills_receivable = models.IntegerField(
        null=True,
        blank=True
    )
    payment_notifications = models.BooleanField(default=False)
    # la logica a continuacion es para la Obras
    details = models.CharField(
        'Detalle',
        max_length=350,
        null=True,
        blank=True
    )
    descriptions = models.CharField(
        'Descripcion',
        max_length=350,
        null=True,
        blank=True
    )
    materials = models.CharField(
        'Materiales',
        max_length=350,
        null=True,
        blank=True
    )
    cost = models.DecimalField(
        'Costo',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    quote = models.IntegerField(
        'Cotización',
        null=True,
        blank=True
    )
    date_received = models.DateTimeField(auto_now_add=True)

    objects = VentasManager()

    def __str__(self):
        return 'Monitoreo: {} - {} - Documento: {} - Direccion: {}'.format(self.id, self.client.name, self.client.document, self.address)

    class Meta:
        verbose_name_plural = "Ventas"
