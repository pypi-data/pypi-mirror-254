from django.db import models
from .address import Address
from .contact import Contact


class Processor(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)

    class Meta:
        db_table = 'processor'
