#from __future__ import with_statement
import tempfile, subprocess, Queue, threading
import xml.etree.ElementTree as ET

# FIXME hackish, won't be required when we start installing to the system
import sys, os
sys.path.append(os.path.abspath('../django/'))

from django.core.management import setup_environ
import quinn.settings
setup_environ(quinn.settings)
#import django
from quinn.monitoring.models import Host, Service

#print quinn.settings.DATABASE_NAME

from pprint import pprint

if os.geteuid() != 0:
    print sys.argv[0], " must be run as root for scanning to work"
    sys.exit(1)

def netscan(cidr):
    """
    do a quick network scan to see what's up or down
    something else will coma along behind this and scan the hosts that are up 
    or down and haven't already been scanned and don't need a rescan
    """
    proc = subprocess.Popen("nmap %s -sP -oX -" % (cidr), shell=True, stdout=subprocess.PIPE)
    xmlstr = proc.stdout.read()
    x = ET.fromstring(xmlstr)
    for host in x.findall('host'):
        # this scan we only get host, status, ip addr, mac addr (sometimes)
        if host.find('status').get('state') != "up":
            print "Host not up: ", host.find('address').get('addr')
        else:
            print "Host up: ", host.find('address').get('addr')
            hip = ''
            hmac = ''
            hmacvnd = ''
            for addr in host.findall('address'):
                if addr.get('addrtype') == 'ipv4':
                    hip = addr.get('addr')
                if addr.get('addrtype') == 'mac':
                    hmac = addr.get('addr')
                    hmacvnd = addr.get('vendor')
                    
            #hip = host.find('address').get('addr')
            try:
                hname = host.find('hostnames')[0].get('name')
            except:
                hname = "unknown"
            #try:
                #hmac = host.find('address')[0].get('mac')
            #except:
                #hmac = ''
            try:
                print "Attempting to find Host record with IP: ", host.find('address').get('addr')
                h = Host.objects.get(IP=hip)
                h.name = hname
                h.mac = hmac
                h.macvnd = hmacvnd
            except:
                # TODO only create a new record if it's not in additional_ips
                print "No record found, creating new Host record for ", host.find('address').get('addr')
                h = Host(IP=hip,name=hname,mac=hmac,macvnd=hmacvnd)
            h.save()
            
        
    
    
def hostscan(host):
    #(tf, tfn) = tempfile.mkstemp('quinn')
    #os.close(tf) # we don't want the file open, we just want a temp file name
    #proc = subprocess.Popen("nmap %s -oX %s" % (cidr, tfn), shell=True, stdout=subprocess.PIPE)
    proc = subprocess.Popen("nmap %s -O -sV -oX -" % (host), shell=True, stdout=subprocess.PIPE)
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
    
    sys.exit(0)
    
    def worker():
        while True:
            item = q.get()
            hostscan(item)
            q.task_done()
            
    q = Queue.Queue()
    for i in range(4):
        t = threading.Thread(target=worker)
        t.setDaemon(True)
        t.start()
    
    for host in Host.objects.filter(OS_vendor__isnull=True):
        q.put(host.IP)
    
    q.join()
    