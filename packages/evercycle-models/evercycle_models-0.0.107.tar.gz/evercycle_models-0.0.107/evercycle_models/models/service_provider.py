from django.db import models
from evercycle_models.models.organization import Organization
from .address import Address
from .data_erasure import DataErasure
from .processor import Processor
from .processor_security import ProcessorSecurity
from .service_provider_service import ServiceProviderService
from .certification import Certification


class ServiceProvider(models.Model):
    class ReportService(models.TextChoices):
        provided_serialized = 'serialized', 'Provide serialized receipt confirmation'
        locked_device = 'device', 'Report locked devices before data erasure for unlocking opportunity'

    class SLA(models.TextChoices):
        two_days = '2', '< 48 hours'
        five_days = '5', '< 5 business days'
        two_weeks = '14', '< 2 weeks'
        month = '30', '< 30 days'

    class PaymentTerms(models.TextChoices):
        five_days = '5', '5 business days'
        two_weeks = '14', '2 weeks'
        month = '30', '30 days'

    class PaymentMethods(models.TextChoices):
        ach = 'ach', 'ACH',
        wire = 'wire', 'Wire',
        check = 'check', 'Check'

    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=50)
    logo = models.BinaryField(blank=True, null=True)
    description = models.CharField(max_length=50)
    device_specialization = models.CharField(max_length=255)
    industry_specialization = models.CharField(max_length=255)

    sample_audit_report = models.BinaryField(blank=True, null=True)
    device_audit_pictures = models.TextField()
    service_provider_workflow_email = models.EmailField(max_length=50)
    headquarters_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='headquarter_service_providers'
    )
    warehouse_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='warehouse_service_providers'
    )
    organization = models.ForeignKey(Organization, models.DO_NOTHING)
    processor = models.ForeignKey(Processor, models.DO_NOTHING)
    data_erasure = models.ForeignKey(DataErasure, models.DO_NOTHING, null=True)
    service_provider_services = models.ManyToManyField(ServiceProviderService)
    certifications = models.ManyToManyField(Certification)
    processor_security = models.ManyToManyField(ProcessorSecurity)

    audit_report_sla = models.CharField(
        choices=SLA.choices
    )

    payment_terms = models.CharField(
        choices=PaymentTerms.choices
    )

    payment_methods = models.CharField(
        choices=PaymentMethods.choices
    )

    report_services = models.CharField(
        choices=ReportService.choices
    )

    def __str__(self):
        return f"{self.id} {self.name}"

    class Meta:
        db_table = 'service_provider'
