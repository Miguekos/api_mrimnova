from django.db import models

# Create your models here.


class ProductModel(models.Model):
    name = models.CharField(
        max_length=20,
        help_text='Nombre del producto',
        unique=True
    )
    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Productos"


class ServiceModel(models.Model):
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


class FacturaModel(models.Model):
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
