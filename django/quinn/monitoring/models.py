from django.db import models
from tagging.fields import TagField

# Create your models here.

class Host(models.Model):
    '''
    a device connected to the network that we care about
    relationships: Rack, ScanNetwork, Test, Location
    '''
    IP = models.IPAddrField()
    name = models.CharField(max_length=200)
    tags = TagField()
    location = models.ForeignKey('Location') # a host should only be in 1 location... it's physics
    
class HostGroups(models.Model):
    name = models.CharField(max_length=200)
    hosts = models.ManyToManyField(Host)

class ScanNetwork(models.Model):
    '''a network to be scanned by nmap'''
    name = models.CharField(max_length=200)
    cidr = models.CharField(max_length=20)
    
    
class Test(models.Model):
    '''
    a test we run against a host (i.e. ping, service test, etc)
    relationships: host
    '''
    host = models.ForeignKey(Host)
    name = models.CharField(max_length=200)
    last_status = models.CharField(max_length=200) # FIXME charfield?
    
class TestStatus(models.Model):
    test = models.ForeignKey(Test)
    status = models.CharField(max_length=200) # FIXME same as Test.last_status

# FIXME do we want to do it like this or give each host a list of rack locations
class Rack(models.Model):
    ''' represents a physical rack'''
    host = models.ManyToManyField(Host)
    
class Location(models.Model):
    '''a physical location (i.e. branch office, HQ, data center, colo, etc)'''
    name = models.CharField(max_length=200)
    
    
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
    hostgroups = models.ManyToManyField(HostGroups)
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey(Host)
    port = models.IntegerField()
    monitored = models.BooleanField(default=False)

