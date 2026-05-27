from django.contrib import admin



from .models import (
    Company,
    DataSource,
    RawEmissionData,
    NormalizedEmission,
    AuditLog
)

admin.site.register(Company)
admin.site.register(DataSource)
admin.site.register(RawEmissionData)
admin.site.register(NormalizedEmission)
admin.site.register(AuditLog)