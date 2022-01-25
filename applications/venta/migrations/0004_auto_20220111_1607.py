# Generated by Django 3.2.9 on 2022-01-11 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basededatos', '0011_clientmodel_profile'),
        ('inventario', '0005_proveedoresmodel'),
        ('venta', '0003_auto_20220111_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentasModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contracts', models.ImageField(upload_to='contratos', verbose_name='Contrato Firmado')),
                ('address', models.CharField(max_length=20, unique=True, verbose_name='Direccion')),
                ('type_method_products', models.CharField(choices=[('0', 'Contado'), ('1', 'Credito')], max_length=2, verbose_name='Tipo pago producto')),
                ('down_payment_producto_cre', models.CharField(max_length=20, verbose_name='Cuota Inicial Productos')),
                ('quotas_producto_cre', models.CharField(max_length=20, verbose_name='Cant. Cuotas Productos')),
                ('type_method_services', models.CharField(choices=[('0', 'Contado'), ('1', 'Credito')], max_length=2, verbose_name='Tipo pago Servicio')),
                ('down_payment_servicios_cre', models.CharField(max_length=20, verbose_name='Cuota Inicial Servicio')),
                ('quotas_servicios_cre', models.CharField(max_length=20, verbose_name='Cant. Cuotas Servicio')),
                ('bills_receivable', models.IntegerField()),
                ('payment_notifications', models.BooleanField(default=False)),
                ('details', models.CharField(max_length=350, verbose_name='Detalle')),
                ('descriptions', models.CharField(max_length=350, verbose_name='Descripcion')),
                ('materials', models.CharField(max_length=350, verbose_name='Materiales')),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Costo')),
                ('quote', models.CharField(max_length=350, verbose_name='Cotización')),
                ('date_received', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas_cliente', to='basededatos.clientmodel')),
                ('products', models.ManyToManyField(to='inventario.ProductModel')),
                ('services', models.ManyToManyField(to='inventario.ServiceModel')),
            ],
            options={
                'verbose_name_plural': 'Ventas Por Video Vigilancia',
            },
        ),
        migrations.RemoveField(
            model_name='ventasvideovigilanciamodelo',
            name='client',
        ),
        migrations.RemoveField(
            model_name='ventasvideovigilanciamodelo',
            name='products',
        ),
        migrations.RemoveField(
            model_name='ventasvideovigilanciamodelo',
            name='services',
        ),
        migrations.DeleteModel(
            name='VentasObrasModelo',
        ),
        migrations.DeleteModel(
            name='VentasVideoVigilanciaModelo',
        ),
    ]