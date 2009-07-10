from quinn.monitoring.models import *
from django.contrib import admin

class HostExtraDataInline(admin.StackedInline):
    model = HostExtraData
    extra = 3
    
class HostAdmin(admin.ModelAdmin):
    inlines = [HostExtraDataInline]

admin.site.register(Host, HostAdmin)

admin.site.register(HostGroup)

admin.site.register(ScanNetwork)

admin.site.register(Tester)

admin.site.register(Rack)

admin.site.register(Location)