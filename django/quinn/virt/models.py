from django.db import models
import tagging

from quinn.monitoring import Host

class KSMStat(models.Model):
    host = models.ForeignKey(Host)
    full_scans = models.IntegerField()
    max_kernel_pages = models.IntegerField()
    pages_shared = models.IntegerField()
    pages_sharing = models.IntegerField()
    pages_to_scan = models.IntegerField()
    pages_unshared = models.IntegerField()
    pages_volatile = models.IntegerField()
    run = models.IntegerField()
    sleep_millisecs = models.IntegerField()