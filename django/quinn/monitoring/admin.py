from quinn.monitoring.models import *
from django.contrib import admin

class HostExtraDataInline(admin.StackedInline):
    model = HostExtraData
    extra = 3
    
class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1
class IPInline(admin.StackedInline):
    model = IP
    extra = 1
class MacInline(admin.StackedInline):
    model = Mac
    extra = 1
    
class HostAdmin(admin.ModelAdmin):
    inlines = [HostExtraDataInline,ServiceInline,IPInline,MacInline,]

admin.site.register(Host, HostAdmin)

admin.site.register(IP)
admin.site.register(Mac)

admin.site.register(HostGroup)

admin.site.register(ScanNetwork)

admin.site.register(Tester)

class RackLocationInline(admin.TabularInline):
    model = RackLocation
class RackAdmin(admin.ModelAdmin):
    inlines = [RackLocationInline,]

admin.site.register(Rack, RackAdmin)

class HostInline(admin.TabularInline):
    model = Host
class LocationAdmin(admin.ModelAdmin):
    inlines = [HostInline,]

admin.site.register(Location)

admin.site.register(Notification)
admin.site.register(Service)
admin.site.register(RackU)
admin.site.register(RackLocation)