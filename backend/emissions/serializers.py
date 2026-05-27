from rest_framework import serializers

from .models import (
    Company,
    DataSource,
    RawEmissionData,
    NormalizedEmission,
    AuditLog
)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class DataSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSource
        fields = '__all__'


class RawEmissionDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = RawEmissionData
        fields = '__all__'


class NormalizedEmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = NormalizedEmission
        fields = '__all__'


class AuditLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditLog
        fields = '__all__'