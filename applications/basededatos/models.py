from django.db import models
from applications.inventario.models import ProductModel, ServiceModel
# Create your models here.

class ClientModel(models.Model):
    type_document_choise = (
        ('0', 'DNI'),
        ('1', 'RUC')
    )
    type_method_products_choise = (
        ('0', 'Contado'),
        ('1', 'Credito')
    )
    type_method_services_choise = (
        ('0', 'Contado'),
        ('1', 'Credito')
    )
    name = models.CharField(
        max_length=20,
        help_text='Nombre del producto',
        unique=True
    )
    address = models.CharField(
        max_length=20,
        help_text='Direccion'
    )
    email = models.EmailField(
        max_length=254
    )
    document = models.CharField(
        max_length=20,
        help_text='Documento',
        unique=True
    )
    type_document = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=type_document_choise
    )
    cash_payment = models.BooleanField(default=False)
    payment_to_credit = models.BooleanField(default=False)
    bills_receivable= models.IntegerField()
    payment_notifications= models.BooleanField(default=False)
    # media_files= models.FieldFile()
    # geolocation= models.CharField()
    products= models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='productos_cliente'
    )
    type_method_products= models.CharField(
        'Tipo pago producto',
        max_length=2,
        choices=type_method_products_choise
    )
    services= models.ForeignKey(
        ServiceModel,
        on_delete=models.CASCADE,
        related_name='servicios_cliente'
    )
    type_method_services= models.CharField(
        'Tipo pago servicio',
        max_length=2,
        choices=type_method_services_choise
    )
    date_received = models.DateTimeField()

    def __str__(self) -> str:
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Clientes"