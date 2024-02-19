from django.db import models


class ServiceProviderService(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'services'
