# Generated by Django 3.2.9 on 2022-01-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededatos', '0012_auto_20220120_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='profile',
            field=models.ImageField(default='', upload_to='profile', verbose_name='profile'),
        ),
    ]
