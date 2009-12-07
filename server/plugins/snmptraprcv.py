# -*- coding: utf-8 -*-
import dbus, gobject, socket
from quinn.server.plugins import QuinnPlugin

from pysnmp.entity import engine, config
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv

from pysnmp.smi import builder

class SnmptraprcvPlugin(QuinnPlugin):
    """create a control socket and listen for commands coming in on it"""
    def __init__(self):
        self.snmpEngine = engine.SnmpEngine()
        
        config.addSocketTransport(
            self.snmpEngine,
            udp.domainName,
            udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162))
            )
            
        config.addV1System(self.snmpEngine, 'test-agent', 'public')
        
        config.addV3User(
            self.snmpEngine, 'test-user',
            config.usmHMACMD5AuthProtocol, 'authkey1',
            config.usmDESPrivProtocol, 'privkey1'
            #    '80004fb81c3dafe69'   # ContextEngineID of Notification Originator
            )
        # Apps registration
        ntfrcv.NotificationReceiver(self.snmpEngine, self.recvcallback)
        self.snmpEngine.transportDispatcher.jobStarted(1) # this job would never finish
        self.snmpEngine.transportDispatcher.runDispatcher()


    def recvcallback(self, snmpEngine,
        contextEngineId, contextName,
        varBinds,
        cbCtx):
        
        mibBuilder = builder.MibBuilder()
        mibBuilder.setMibPath('MIB', 
            '/usr/lib/pymodules/python2.5/pysnmp/v4/smi/mibs/', 
            '/usr/share/python-support/python-pysnmp4/pysnmp/v4/smi/mibs/')
        #mibBuilder.loadModules('CPQPOWER')
        
        print 'Notification from SNMP Engine \"%s\", Context \"%s\"' % (
            contextEngineId, contextName
        )
        for name, val in varBinds:
            print '%s = %s' % (name.prettyPrint(), val.prettyPrint())

