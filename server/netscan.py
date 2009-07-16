#from __future__ import with_statement
import tempfile, subprocess
import xml.etree.ElementTree as ET

# FIXME hackish, won't be required when we start installing to the system
import sys, os.path
sys.path.append(os.path.abspath('../django/'))

from django.core.management import setup_environ
import quinn.settings
setup_environ(quinn.settings)
#import django
from quinn.monitoring.models import Host, Service

#print quinn.settings.DATABASE_NAME

from pprint import pprint

def netscan(cidr):
    #(tf, tfn) = tempfile.mkstemp('quinn')
    #os.close(tf) # we don't want the file open, we just want a temp file name
    #proc = subprocess.Popen("nmap %s -oX %s" % (cidr, tfn), shell=True, stdout=subprocess.PIPE)
    proc = subprocess.Popen("nmap %s -O -oX -" % (cidr), shell=True, stdout=subprocess.PIPE)
    xmlstr = proc.stdout.read()
    x = ET.fromstring(xmlstr)
    for host in x.findall('host'):
        #pprint(host)#, host.find('status'))#, host.find('status').get('state'))
        if host.find('status').get('state') != "up":
            print "Host not up: ", host.find('address').get('addr')
        else:
            print "Host up: ", host.find('address').get('addr')
            hip = host.find('address').get('addr')
            try:
                hname = host.find('hostnames')[0].get('name')
            except:
                hname = "unknown"
            try:
                osvnd = host.find('os').find('osclass').get('vendor')
            except:
                osvnd = "unknown"
            try:
                oscls = host.find('os').find('osclass').get('family')
            except:
                oscls = "unknown"
            try:
                osname = host.find('os').find('osmatch').get('name')
            except:
                osname = "unknown"
            
            print hip, hname, osvnd, oscls, osname
            
            try:
                print "Attempting to find Host record with IP: ", host.find('address').get('addr')
                h = Host.objects.get(IP=hip)
                h.name = hname
                h.OS_vendor = osvnd
                h.OS_class = oscls
                h.OS_name = osname
            except:
                print "No record found, creating new Host record for ", host.find('address').get('addr')
                h = Host(IP=hip,name=hname,OS_vendor=osvnd,OS_class=oscls,OS_name=osname)
            h.save()
            pprint(h)
            for srvc in host.find('ports').findall('port'):
                s = Service(name=srvc.find('service').get('name'),
                    host=h,
                    port=srvc.get('portid'))
                s.save()
                pprint(s)
    

if __name__=='__main__':
    import sys
    if len(sys.argv) == 1:
        print "\nUsage: %s <cidr>\nExample: %s 192.168.100.1/24\n" % (sys.argv[0], sys.argv[0])
        sys.exit()
    netscan(sys.argv[1])