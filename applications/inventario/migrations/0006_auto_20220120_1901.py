# Generated by Django 3.2.9 on 2022-01-21 00:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_proveedoresmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedoresmodel',
            options={'verbose_name_plural': 'Proveedores'},
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='code_type',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='plans',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='product_address',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='type_of_services',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='marca',
            field=models.CharField(default='', max_length=20, verbose_name='Marca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='modelo',
            field=models.CharField(default='', max_length=20, verbose_name='Modelo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='bar_code',
            field=models.IntegerField(verbose_name='Codigo de barra'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='code',
            field=models.CharField(max_length=20, verbose_name='Codigo de articulo'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo de Venta'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='date_of_entry',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de entrega'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='date_received',
            field=models.DateTimeField(verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='internal_product_code',
            field=models.IntegerField(verbose_name='Codigo interno de producto'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='quantity',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='serial_number',
            field=models.IntegerField(verbose_name='Numeros de Series / Segun Cantidad'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='tickets_purchases',
            field=models.CharField(max_length=12, verbose_name='Stock Minino'),
        ),
    ]