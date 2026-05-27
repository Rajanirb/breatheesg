from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import pandas as pd

from .utils import calculate_emission

from .models import (
    Company,
    DataSource,
    RawEmissionData,
    NormalizedEmission,
    AuditLog
)

from .serializers import (
    CompanySerializer,
    DataSourceSerializer,
    RawEmissionDataSerializer,
    NormalizedEmissionSerializer,
    AuditLogSerializer
)


class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class DataSourceViewSet(viewsets.ModelViewSet):

    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RawEmissionDataViewSet(viewsets.ModelViewSet):

    queryset = RawEmissionData.objects.all()
    serializer_class = RawEmissionDataSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class NormalizedEmissionViewSet(viewsets.ModelViewSet):

    queryset = NormalizedEmission.objects.all()
    serializer_class = NormalizedEmissionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AuditLogViewSet(viewsets.ModelViewSet):

    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def upload_emission_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        })

    df = pd.read_csv(file)

    processed_data = []

    for _, row in df.iterrows():

        activity_type = row['activity_type']
        activity_value = row['activity_value']

        emission = calculate_emission(
            activity_type,
            activity_value
        )

        company, _ = Company.objects.get_or_create(
            name="Breathe ESG Demo Company"
        )

        source, _ = DataSource.objects.get_or_create(
            company=company,
            source_type="UTILITY"
        )

        raw_entry = RawEmissionData.objects.create(
            source=source,
            raw_data={
                "activity_type": activity_type,
                "activity_value": activity_value
            },
            status="PROCESSED"
        )

        NormalizedEmission.objects.create(
            company=company,
            scope="SCOPE_2",
            category=activity_type,
            activity_value=activity_value,
            activity_unit="kWh",
            normalized_unit="kgCO2e",
            emission_factor=0.82,
            co2e_emission=emission,
            source_row=raw_entry
        )

        processed_data.append({
            "activity_type": activity_type,
            "activity_value": activity_value,
            "co2e_emission": emission
        })

    return Response({
        "message": "CSV processed successfully",
        "data": processed_data
    })
@api_view(['GET'])
def dashboard_summary(request):

    total_emission = (
        NormalizedEmission.objects.aggregate(
            total=Sum('co2e_emission')
        )['total'] or 0
    )

    scope1 = (
        NormalizedEmission.objects.filter(
            scope='SCOPE_1'
        ).aggregate(
            total=Sum('co2e_emission')
        )['total'] or 0
    )

    scope2 = (
        NormalizedEmission.objects.filter(
            scope='SCOPE_2'
        ).aggregate(
            total=Sum('co2e_emission')
        )['total'] or 0
    )

    scope3 = (
        NormalizedEmission.objects.filter(
            scope='SCOPE_3'
        ).aggregate(
            total=Sum('co2e_emission')
        )['total'] or 0
    )

    suspicious_count = (
        NormalizedEmission.objects.filter(
            is_suspicious=True
        ).count()
    )

    return Response({
        "total_emissions": total_emission,
        "scope_1": scope1,
        "scope_2": scope2,
        "scope_3": scope3,
        "suspicious_records": suspicious_count
    })

@api_view(['GET'])
def monthly_emissions(request):

    emissions = NormalizedEmission.objects.all()

    monthly_data = {}

    for emission in emissions:

        month = emission.created_at.strftime("%Y-%m")

        if month not in monthly_data:
            monthly_data[month] = 0

        monthly_data[month] += emission.co2e_emission

    return Response(monthly_data)

@api_view(['GET'])
def suspicious_emissions(request):

    suspicious = NormalizedEmission.objects.filter(
        co2e_emission__gt=100
    )

    data = []

    for item in suspicious:

        data.append({
            "company": item.company.name,
            "category": item.category,
            "emission": item.co2e_emission
        })

    return Response(data)

@api_view(['GET'])
def ai_recommendations(request):

    recommendations = [
        "Reduce diesel usage",
        "Switch to renewable electricity",
        "Optimize logistics transport",
        "Encourage virtual meetings"
    ]

    return Response({
        "recommendations": recommendations
    })