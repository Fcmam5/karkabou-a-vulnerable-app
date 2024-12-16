from django.contrib import admin
from .models import Musician,Band
import logging

logger = logging.getLogger(__name__)

class MusicianAdmin(admin.ModelAdmin):
    # I I want to exclude fields, not make them readonly

    exclude = ('groups', 'user_permissions', 'is_superuser', 'is_staff')
    readonly_fields = ('date_joined', 'last_login')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.band:
            logger.info(f"Adding Musician ({obj.email} {obj.full_name()}) to band {obj.band.name}")

class BandAdmin(admin.ModelAdmin):
    pass
admin.site.register(Band, BandAdmin)
admin.site.register(Musician, MusicianAdmin)
