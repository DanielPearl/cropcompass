from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DjangoMigrations)
admin.site.register(Metadata)
admin.site.register(NassCropAnimals)
admin.site.register(NassCropArea)
admin.site.register(NassCropFarms)
admin.site.register(OainHarvestAcres)
admin.site.register(RawNassCensusData)
admin.site.register(RawOainData)
admin.site.register(RawSubsidyData)
admin.site.register(RegionLookup)
admin.site.register(SubsidyDollars)
admin.site.register(SubsidyRecipients)
