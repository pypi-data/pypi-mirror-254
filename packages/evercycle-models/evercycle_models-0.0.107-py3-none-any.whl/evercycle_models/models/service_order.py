from django.db import models


class ServiceOrder(models.Model):
    id = models.IntegerField(primary_key=True)
