from django.db import models


class DeviceType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id } - {self.type}"

    class Meta:
        db_table = 'device_type'
