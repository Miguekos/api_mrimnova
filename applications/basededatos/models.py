from django.db import models
from applications.inventario.models import ProductModel, ServiceModel
# Create your models here.

class ClientModelOld(models.Model):
    type_document_choise = (
        ('0', 'DNI'),
        ('1', 'RUC')
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
    # cash_payment = models.BooleanField(default=False)
    # payment_to_credit = models.BooleanField(default=False)
    # bills_receivable= models.IntegerField()
    # payment_notifications= models.BooleanField(default=False)
    # media_files= models.FieldFile()
    # geolocation= models.CharField()

    def __str__(self) -> str:
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Clientes"


class ClientModel(models.Model):
    type_document_choise = (
        ('0', 'DNI'),
        ('1', 'RUC')
    )
    name = models.CharField(
        max_length=20,
        help_text='Nombre del producto',
        unique=True
    )
    address_main = models.CharField(
        max_length=20,
        help_text='Direccion Principal'
    )
    email = models.EmailField(
        max_length=254
    )
    type_document = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=type_document_choise
    )
    document = models.CharField(
        max_length=20,
        help_text='Documento',
        unique=True
    )
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Clientes"


class MonitoreoModel(models.Model):
    type_method_products_choise = (
        ('0', 'Contado'),
        ('1', 'Credito')
    )
    type_method_services_choise = (
        ('0', 'Contado'),
        ('1', 'Credito')
    )
    client = models.ForeignKey(ClientModel, related_name='monitoreo_cliente', on_delete=models.CASCADE)
    contracts = models.CharField(
        'Contratos',
        max_length=20
    )
    address = models.CharField(
        'Direccion',
        max_length=20,
        unique=True
    )
    # cash_payment = models.BooleanField(default=False)
    # payment_to_credit = models.BooleanField(default=False)
    payment_notifications = models.BooleanField(default=False)
    products= models.ManyToManyField(
        ProductModel
    )
    type_method_products= models.CharField(
        'Tipo pago producto',
        max_length=2,
        choices=type_method_products_choise
    )
    services= models.ManyToManyField(
        ServiceModel
    )
    type_method_services= models.CharField(
        'Tipo pago servicio',
        max_length=2,
        choices=type_method_services_choise
    )
    bills_receivable = models.IntegerField()
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} - Documento: {} - Direccion: {}'.format(self.client.name, self.client.document, self.address)

    class Meta:
        verbose_name_plural = "Monitoreos"