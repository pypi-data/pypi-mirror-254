from django.db import models


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    location_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return (f"{self.address1} {self.address2} {self.city} "
                f"{self.state} {self.postal_code} {self.country}")

    class Meta:
        db_table = 'address'
