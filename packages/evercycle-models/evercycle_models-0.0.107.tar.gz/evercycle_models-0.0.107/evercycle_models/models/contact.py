from django.db import models


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(blank=True, null=True, max_length=100)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'contact'
