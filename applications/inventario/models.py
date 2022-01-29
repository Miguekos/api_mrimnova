from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.


class ServiceModel(TimeStampedModel):
    name = models.CharField(
        max_length=20,
        help_text='Nombre del servicio',
        unique=True
    )
    quantity = models.CharField(
        max_length=20,
        help_text='Cantidad',
    )
    term = models.CharField(
        max_length=20,
        help_text='Plazo',
    )
    quota = models.CharField(
        max_length=20,
        help_text='Cuota',
    )
    active = models.BooleanField(
        help_text='Activo',
        default=True
    )

    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Servicios"


class ProveedoresModel(TimeStampedModel):
    type_document_choise = (
        ('0', 'DNI'),
        ('1', 'RUC')
    )
    name = models.CharField(
        max_length=20,
        help_text='Nombres',
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
    date_received = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Proveedores"


class FacturaModel(TimeStampedModel):
    type_invoice_choise_factura = (
        ('0', 'Factura'),
        ('1', 'Boleta')
    )
    proveedor = models.ForeignKey(ProveedoresModel, related_name='factura_producto', on_delete=models.CASCADE)
    type_invoice = models.CharField(
        'Tipo de pedido',
        max_length=2,
        choices=type_invoice_choise_factura
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


class ProductModel(TimeStampedModel):
    name = models.CharField(
        max_length=20,
        help_text='Nombre del producto',
        unique=True
    )
    # code_type_choise = (
    #     ('0', 'Factura'),
    #     ('1', 'Boleta'),
    #     ('2', 'Guia de Remisión'),
    # )
    # code_type = models.CharField('Tipo de registro', choices=code_type_choise, max_length=2, default='Factura')
    invoice_relation = models.ForeignKey(FacturaModel, on_delete=models.CASCADE, related_name='producto_factura')
    marca = models.CharField(
        'Marca',
        max_length=20
    )
    modelo = models.CharField(
        'Modelo',
        max_length=20
    )
    code = models.CharField(
        'Codigo de articulo',
        max_length=20
    )
    # TODO: Marca
    # TODO: Modelo

    date_of_entry = models.DateTimeField('Fecha de entrega')
    internal_product_code = models.CharField(
        'Codigo interno de producto',
        max_length=100
    )
    bar_code = models.CharField(
        'Codigo de barra',
        max_length=100
    )
    # product_address = models.CharField(
    #     'Direccion del producto',
    #     max_length=50,
    # )
    quantity = models.IntegerField('Cantidad')
    serial_number = models.CharField(
        'Numeros de Series',
        max_length=100
    )
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
        'Stock Minino',
        max_length=12,
    )
    outflows_sales = models.CharField(
        'Ventas',
        max_length=12,
        default=0
    )
    # type_of_services = models.CharField(
    #     'Tipo de servicio',
    #     max_length=20
    # )
    cost = models.DecimalField(
        'Costo de Venta',
        max_digits=10,
        decimal_places=2
    )
    description = models.CharField(
        'Descripcion',
        max_length=100,
        default='Sin descripcion'
    )
    # plans = models.CharField(
    #     'Planes',
    #     max_length=20,
    #     default='Sin planes'
    # )
    date_received = models.DateTimeField('Creado')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Productos"
