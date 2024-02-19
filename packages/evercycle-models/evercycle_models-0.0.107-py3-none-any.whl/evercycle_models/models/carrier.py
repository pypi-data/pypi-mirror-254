from django.db import models

from .carrier_type import CarrierType


class Carrier(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    reference = models.CharField(max_length=50)
    carrier_id = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.ForeignKey(CarrierType, models.DO_NOTHING)

    class Meta:
        db_table = 'carrier'
