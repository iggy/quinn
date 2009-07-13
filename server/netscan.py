import tempfile
from __future__ import with_statement
import xml.etree.ElementTree as ET

# FIXME hackish, won't be required when we start installing to the system
import sys, os.path
sys.path.append(os.path.abspath('../../django/'))

import django
from quinn.monitoring.models import Host, Service


def netscan(cidr):
    (tf, tfn) = tempfile.mkstemp('quinn')
    tf.close() # we don't want the file open, we just want a temp file name
    proc = subprocess.Popen("nmap %s -oX %s" % (cidr, tfn), shell=True, stdout=subprocess.PIPE)
    x = ET.parse('tfn')
    for host in x.findall('host'):
        if host.find('status').get('state') is 'up':
            
            h = Host(IP=host.find('address').get('addr'),
                name=host.find('hostnames')[0].get('name'),
                OperatingSystem=host.find('os').find('osmatch').get('name'))
            #h.save()
            for srvc in host.find('ports').findall('port'):
                s = Service(name=srvc.find('service').get('name')
                    host=h,
                    port=srvc.get('portid'))
                s.save()
    

if __name__=='__main__':
    import sys
    netscan(sys.argv[1])