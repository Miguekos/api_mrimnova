# Generated by Django 3.2.9 on 2022-02-01 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20220130_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='invoice_relation',
            new_name='id_invoice',
        ),
    ]
