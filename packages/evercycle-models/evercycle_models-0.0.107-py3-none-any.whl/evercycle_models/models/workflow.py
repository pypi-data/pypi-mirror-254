from django.db import models
from evercycle_models.models.organization import Organization
from .processor import Processor
from .carrier import Carrier
from .workflow_type import WorkflowType
from .service_provider import ServiceProvider
from .service_level import ServiceLevel


class Workflow(models.Model):

    class Status(models.TextChoices):
        APPROVED = 'ap', 'Approved',
        PENDING = 'pe', 'Pending'
        ARCHIVED = 'ar', 'Archived'

    class Frequency(models.TextChoices):
        WEEK = 'w', 'WEEK'
        DAY = 'd', 'DAY',
        MONTH = 'm', 'MONTH'

    class DeviceLocation(models.TextChoices):
        CONTIGUOUS_US_ONLY = 'co', 'Contiguous Us Only'
        ALL_USA = 'al', 'All USA',
        OUTSIDE_CONTIGUOUS_ONLY = 'ou', 'Outside contiguous Only'

    class DeviceLocationConus(models.TextChoices):
        ALASKA = 'ak', 'Alaska'
        HAWAII = 'hw', 'Hawaii'

    class Meta:
        db_table = 'workflow'

    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    organization = models.ForeignKey(Organization, models.DO_NOTHING)
    processor = models.ForeignKey(Processor, models.DO_NOTHING)
    type = models.ForeignKey(WorkflowType, models.DO_NOTHING)
    service_provider = models.ForeignKey(ServiceProvider, models.DO_NOTHING)
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField()
    three_tier_grade = models.BooleanField()
    gradescaletype = models.CharField(max_length=50)
    notify_locks = models.BooleanField()
    disable_email_notification = models.BooleanField()
    carrier = models.ForeignKey(Carrier, models.DO_NOTHING)
    service_level_out = models.ForeignKey(
        ServiceLevel,
        on_delete=models.CASCADE,
        related_name='workflow_service_out'
    )
    service_level_return = models.ForeignKey(
        ServiceLevel,
        on_delete=models.CASCADE,
        related_name='workflows_service_return'
    )
    test = models.BooleanField()
    device_location_type = models.CharField(
        max_length=2,
        choices=DeviceLocation.choices,
        default=DeviceLocation.ALL_USA
    )
    device_location_type_conus_choice = models.CharField(
        choices=DeviceLocationConus.choices,
        null=True,
        blank=True
    )
    workflow_poc = models.CharField(max_length=50)
    workflow_poc_email = models.CharField(max_length=50)
    workflow_status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )
    device_sample = models.CharField(max_length=50)
    frequency_type = models.CharField(
        max_length=5,
        choices=Frequency.choices,
        default=Frequency.MONTH
    )
    frequency = models.IntegerField()
