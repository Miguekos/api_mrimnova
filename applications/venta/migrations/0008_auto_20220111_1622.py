# Generated by Django 3.2.9 on 2022-01-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0007_auto_20220111_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventasmodelo',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='descriptions',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='details',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Detalle'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='down_payment_producto_cre',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cuota Inicial Productos'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='down_payment_servicios_cre',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cuota Inicial Servicio'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='materials',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Materiales'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='quotas_producto_cre',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cant. Cuotas Productos'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='quotas_servicios_cre',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cant. Cuotas Servicio'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='quote',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Cotización'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='type_method_products',
            field=models.CharField(blank=True, choices=[('0', 'Contado'), ('1', 'Credito')], max_length=2, null=True, verbose_name='Tipo pago producto'),
        ),
        migrations.AlterField(
            model_name='ventasmodelo',
            name='type_method_services',
            field=models.CharField(blank=True, choices=[('0', 'Contado'), ('1', 'Credito')], max_length=2, null=True, verbose_name='Tipo pago Servicio'),
        ),
    ]
