from django.urls import path, include
from rest_framework.routers import DefaultRouter
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

}

from .views import (
    CompanyViewSet,
    DataSourceViewSet,
    RawEmissionDataViewSet,
    NormalizedEmissionViewSet,
    AuditLogViewSet,
    upload_emission_csv,
    dashboard_summary,
    monthly_emissions,
    suspicious_emissions,
    ai_recommendations
)

router = DefaultRouter()

router.register('companies', CompanyViewSet)
router.register('data-sources', DataSourceViewSet)
router.register('raw-data', RawEmissionDataViewSet)
router.register('normalized-emissions', NormalizedEmissionViewSet)
router.register('audit-logs', AuditLogViewSet)

urlpatterns = [

    path('', include(router.urls)),

    path(
        'upload-csv/',
        upload_emission_csv
    ),

    path(
        'dashboard-summary/',
        dashboard_summary
    ),
    path(
        'monthly-emissions/',
        monthly_emissions
    ),
    path(
        'suspicious-emissions/',
        suspicious_emissions
    ),
    path(
        'ai-recommendations/',
        ai_recommendations
    ),
]