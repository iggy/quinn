from django.db import models
#from tagging.fields import TagField
import tagging

# Create your models here.

class Host(models.Model):
    '''
    a device connected to the network that we care about
    relationships: Rack, ScanNetwork, Test, Location
    '''
    # FIXME some boxes have more than 1 IP, more than 1 MAC, etc.
    # what exactly is going to be unique and singular on a box?
    # going to use the IP as the unique thing, then the user can manually merge
    # hosts and the IP's will go into the IP model as additioinal_ips
    name = models.CharField(max_length=200)
    IP = models.IPAddressField(unique=True)
    mac = models.CharField(max_length=12,blank=True,null=True)
    OS_vendor = models.CharField(max_length=200,blank=True,null=True)
    OS_class = models.CharField(max_length=200,blank=True,null=True)
    OS_name = models.CharField(max_length=200,blank=True,null=True)
    #tags = TagField()
    location = models.ForeignKey('Location',null=True) # a host should only be in 1 location... it's physics
    
    def __unicode__(self):
        return "%s - %s" % (self.IP, self.name)

tagging.register(Host)

class IP(models.Model):
    host = models.ForeignKey(Host,related_name="additional_ips")
    IP = models.IPAddressField(unique=True)
class Mac(models.Model):
    host = models.ForeignKey(Host,related_name="additional_macs")
    mac = models.CharField(max_length=12)

class HostExtraData(models.Model):
    '''
    any extra info about a host... used during parsing netscans and also 
    available for custom note entry, etc
    '''
    host = models.ForeignKey(Host)
    key = models.CharField(max_length=60)
    value = models.TextField()
    
class HostGroup(models.Model):
    name = models.CharField(max_length=200)
    hosts = models.ManyToManyField(Host)
    def __unicode__(self):
        return self.name

class ScanNetwork(models.Model):
    '''a network to be scanned by nmap'''
    name = models.CharField(max_length=200)
    cidr = models.CharField(max_length=20)
    def __unicode__(self):
        return "%s - %s" % (self.name, self.cidr)
    
    
class Tester(models.Model):
    '''
    a test we run against a host (i.e. ping, service test, etc)
    relationships: host
    '''
    name = models.CharField(max_length=200)
    host = models.ForeignKey(Host)
    name = models.CharField(max_length=200)
    last_status = models.CharField(max_length=200) # FIXME charfield?
    def __unicode__(self):
        return self.name

    
class TestStatus(models.Model):
    test = models.ForeignKey(Tester)
    status = models.CharField(max_length=200) # FIXME same as Test.last_status

# FIXME do we want to do it like this or give each host a list of rack locations
class Rack(models.Model):
    ''' represents a physical rack'''
    name = models.CharField(max_length=200)
    hosts = models.ManyToManyField(Host,through='RackLocation')
    how_many_U = models.IntegerField(default="42")
    def __unicode__(self):
        return self.name
    def get_hosts_in_order(self):
        d = []
        for u in range(self.how_many_U,0,-1):
            try:
                host = self.racklocation_set.get(rack_Us__U=u).host
            except:
                host = ''
            d.append(host)
        return d
    
class RackLocation(models.Model):
    host = models.ForeignKey(Host)
    rack = models.ForeignKey(Rack)
    rack_Us = models.ManyToManyField('RackU')
    def __unicode__(self):
        return "%s - %s" % (self.rack_Us,self.host)
    class Meta:
        ordering = ['rack_Us']
        #order_with_respect_to = 'rack_Us'

class RackU(models.Model):
    U = models.IntegerField()
    def __unicode__(self):
        return str(self.U)
    class Meta:
        ordering = ['-U']

class Location(models.Model):
    '''a physical location (i.e. branch office, HQ, data center, colo, etc)'''
    name = models.CharField(max_length=200)
    #TODO scannetworks = models.ManyToManyField(ScanNetwork)
    def __unicode__(self):
        return self.name
    
    
class UserEmail(models.Model):
    '''an email address the user can use for notifications, etc.'''
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
class UserExtension(models.Model):
    '''hold extra info about a user since we can get users from active directory'''
    emails = models.ManyToManyField(UserEmail)
    
class Notification(models.Model):
    teststatus = models.ForeignKey(TestStatus)
    error_status = models.CharField(max_length=200) # FIXME same as Test.last_status
    hosts = models.ManyToManyField(Host)
    hostgroups = models.ManyToManyField(HostGroup)
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey(Host)
    port = models.IntegerField()
    monitored = models.BooleanField(default=False)
    def __unicode__(self):
        return "%s (%s) on %s" % (self.name, self.port, self.host.IP)

