from django.db import models
from django.utils import timezone, dateformat


class VentasManager(models.Manager):

    def get_sales_for_id(self, client_id):
        return self.filter(
            client__id=client_id
        )
