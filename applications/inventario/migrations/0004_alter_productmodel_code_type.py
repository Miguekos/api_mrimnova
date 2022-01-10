# Generated by Django 3.2.9 on 2021-11-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20211121_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='code_type',
            field=models.CharField(choices=[('0', 'Factura'), ('1', 'Boleta'), ('2', 'Guia de Remisión')], default='Factura', max_length=2, verbose_name='Tipo de registro'),
        ),
    ]
