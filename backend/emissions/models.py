from django.db import models
class Company(models.Model):

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_TYPES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    uploaded_file_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"


class RawEmissionData(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("PROCESSED", "PROCESSED"),
        ("FAILED", "FAILED"),
    ]

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    raw_data = models.JSONField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    error_message = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Raw Data {self.id}"


class NormalizedEmission(models.Model):

    SCOPE_CHOICES = [
        ("SCOPE_1", "SCOPE_1"),
        ("SCOPE_2", "SCOPE_2"),
        ("SCOPE_3", "SCOPE_3"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    category = models.CharField(max_length=100)

    activity_value = models.FloatField()

    activity_unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    emission_factor = models.FloatField()

    co2e_emission = models.FloatField()

    source_row = models.ForeignKey(
        RawEmissionData,
        on_delete=models.SET_NULL,
        null=True
    )

    is_suspicious = models.BooleanField(default=False)

    approved = models.BooleanField(default=False)

    locked_for_audit = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.scope}"


class AuditLog(models.Model):

    emission = models.ForeignKey(
        NormalizedEmission,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=100)

    old_value = models.JSONField(
        null=True,
        blank=True
    )

    new_value = models.JSONField(
        null=True,
        blank=True
    )

    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action