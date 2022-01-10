from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


class PersonalModel(TimeStampedModel):
    name = models.CharField(
        'Nombres',
        max_length=20
    )
    lastnames = models.CharField(
        'Apellidos',
        max_length=30
    )
    address = models.CharField(
        'Direccion',
        max_length=50
    )
    email = models.EmailField()
    dni = models.CharField(
        'DNI',
        max_length=12
    )
    phone = models.CharField(
        'Telefono',
        max_length=10
    )
    contracts = models.CharField(
        'Contratos',
        max_length=20
    )
    
    class Meta:
        verbose_name = 'Personal'
        # verbose_name_plural = "Personal"

    def __str__(self):
        return "{} {} {}".format(self.name, self.lastnames, self.phone)