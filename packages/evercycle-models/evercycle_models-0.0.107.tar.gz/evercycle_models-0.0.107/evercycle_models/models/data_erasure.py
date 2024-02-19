from django.db import models

from evercycle_models.models import Certification


class DataErasure(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    website_url = models.CharField(max_length=50)
    certificate_example = models.BinaryField(blank=True, null=True)
    certifications = models.ManyToManyField(Certification)
    policy = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.name}"
