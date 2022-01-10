from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.


class ProductModel(TimeStampedModel):
    name = models.CharField(
        max_length=20,
        help_text='Nombre del producto',
        unique=True
    )
    code_type_choise = (
        ('0', 'Factura'),
        ('1', 'Boleta'),
        ('2', 'Guia de Remisión'),
    )
    code_type = models.CharField('Tipo de registro', choices=code_type_choise, max_length=2, default='Factura')
    code = models.CharField(
        'Codigo',
        max_length=20
    )
    date_of_entry = models.DateTimeField(
        'Fecha de Entrada',
        blank=True,
        null=True
    )
    internal_product_code = models.IntegerField()
    bar_code = models.IntegerField()
    product_address = models.CharField(
        'Direccion del producto',
        max_length=50,
    )
    serial_number = models.IntegerField()
    quantity = models.IntegerField()
    purchase_cost = models.DecimalField(
        'Costo de Compra',
        max_digits=10,
        decimal_places=2
    )
    obervations = models.CharField(
        'Observaciones',
        max_length=100,
        default='Sin observaciones'
    )
    tickets_purchases = models.CharField(
        'Entrada',
        max_length=12,
    )
    outflows_sales = models.CharField(
        'Ventas',
        max_length=12,
        default=0
    )
    type_of_services = models.CharField(
        'Tipo de servicio',
        max_length=20
    )
    cost = models.DecimalField(
        'Costo',
        max_digits=10,
        decimal_places=2
    )
    description = models.CharField(
        'Descripcion',
        max_length=100,
        default='Sin descripcion'
    )
    plans = models.CharField(
        'Planes',
        max_length=20,
        default='Sin planes'
    )
    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Productos"


class ServiceModel(TimeStampedModel):
    name = models.CharField(
        max_length=20,
        help_text='Nombre del servicio',
        unique=True
    )
    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Servicios"


class FacturaModel(TimeStampedModel):
    type_invoice_choise = (
        (0, 'Factura'),
        (1, 'Boleta')
    )
    type_invoice = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=type_invoice_choise
    )
    codigo = models.CharField(
        max_length=20,
        help_text='Id de la factura o boleta'
    )
    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.codigo)

    class Meta:
        verbose_name_plural = "Facturas"


class ProveedoresModel(TimeStampedModel):
    type_invoice_choise = (
        (0, 'Factura'),
        (1, 'Boleta')
    )
    type_invoice = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=type_invoice_choise
    )
    codigo = models.CharField(
        max_length=20,
        help_text='Id de la factura o boleta'
    )
    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.codigo)

    class Meta:
        verbose_name_plural = "Facturas"