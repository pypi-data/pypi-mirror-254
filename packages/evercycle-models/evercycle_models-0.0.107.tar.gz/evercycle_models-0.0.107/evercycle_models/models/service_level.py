from django.db import models
from .carrier_type import CarrierType


class ServiceLevel(models.Model):
    name = models.CharField(max_length=100)
    f_id = models.CharField(max_length=100)
    carrier_type = models.ForeignKey(CarrierType, models.DO_NOTHING)

    class Meta:
        db_table = 'service_level'
