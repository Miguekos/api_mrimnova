# Generated by Django 3.2.9 on 2022-02-01 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombres', max_length=20, unique=True)),
                ('address_main', models.CharField(help_text='Direccion Principal', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('type_document', models.CharField(choices=[('0', 'DNI'), ('1', 'RUC')], max_length=2, verbose_name='Tipo de documento')),
                ('document', models.CharField(help_text='Documento', max_length=20, unique=True)),
                ('profile', models.ImageField(default='https://cdn.quasar.dev/img/boy-avatar.png', upload_to='profile', verbose_name='profile')),
                ('date_received', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='ClientModelOld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del producto', max_length=20, unique=True)),
                ('address', models.CharField(help_text='Direccion', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('document', models.CharField(help_text='Documento', max_length=20, unique=True)),
                ('type_document', models.CharField(choices=[('0', 'DNI'), ('1', 'RUC')], max_length=2, verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='ProveedorModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombres', max_length=20, unique=True)),
                ('address_main', models.CharField(help_text='Direccion', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('type_document', models.CharField(choices=[('0', 'DNI'), ('1', 'RUC')], max_length=2, verbose_name='Tipo de documento')),
                ('document', models.CharField(help_text='Documento', max_length=20, unique=True)),
                ('profile', models.ImageField(upload_to='profile', verbose_name='profile')),
                ('date_received', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitoreoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_sales', models.CharField(choices=[('0', 'Servicios Generales (Obras)'), ('1', 'Productos y Servicios (Video Vigilancia)')], max_length=2, verbose_name='Tipo de venta')),
                ('contracts', models.CharField(max_length=20, verbose_name='Contratos')),
                ('address', models.CharField(max_length=20, unique=True, verbose_name='Direccion')),
                ('payment_notifications', models.BooleanField(default=False)),
                ('type_method_products', models.CharField(choices=[('0', 'Contado'), ('1', 'Credito')], max_length=2, verbose_name='Tipo pago producto')),
                ('type_method_services', models.CharField(choices=[('0', 'Contado'), ('1', 'Credito')], max_length=2, verbose_name='Tipo pago servicio')),
                ('bills_receivable', models.IntegerField()),
                ('date_received', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitoreo_cliente', to='basededatos.clientmodel')),
                ('products', models.ManyToManyField(to='inventario.ProductModel')),
                ('services', models.ManyToManyField(to='inventario.ServiceModel')),
            ],
            options={
                'verbose_name_plural': 'Monitoreos',
            },
        ),
    ]
