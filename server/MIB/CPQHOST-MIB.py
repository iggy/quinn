# PySNMP SMI module. Autogenerated from smidump -f python CPQHOST-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Nov 18 11:33:04 2009,
# Python version (2, 6, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( MibScalar, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("RFC-1212", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
( NotificationType, ) = mibBuilder.importSymbols("RFC-1215", "NotificationType")
( IpAddress, enterprises, ) = mibBuilder.importSymbols("RFC1155-SMI", "IpAddress", "enterprises")
( DisplayString, sysName, ) = mibBuilder.importSymbols("RFC1213-MIB", "DisplayString", "sysName")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Objects

compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqHostOs = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11))
cpqHoMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 1))
cpqHoMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
cpqHoMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoMibCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("ok", 2), ("degraded", 3), ("failed", 4), ))).setMaxAccess("readonly")
cpqHoComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2))
cpqHoInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 1))
cpqHoOsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4))
cpqHoOsCommonPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
cpqHoOsCommonModuleTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2))
cpqHoOsCommonModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoOsCommonModuleIndex"))
cpqHoOsCommonModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoOsCommonModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoOsCommonModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
cpqHoOsCommonModuleDate = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
cpqHoOsCommonModulePurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 2))
cpqHoName = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoVersion = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoDesc = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoOsType = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(12,19,3,14,18,2,13,7,10,1,5,21,23,17,15,4,8,22,11,20,16,6,9,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("windows98", 10), ("open-vms", 11), ("nsk", 12), ("windowsCE", 13), ("linux", 14), ("windows2000", 15), ("tru64UNIX", 16), ("windows2003", 17), ("windows2003-x64", 18), ("solaris", 19), ("netware", 2), ("windows2003-ia64", 20), ("windows2008", 21), ("windows2008-x64", 22), ("windows2008-ia64", 23), ("windowsnt", 3), ("sco-unix", 4), ("unixware", 5), ("os-2", 6), ("ms-dos", 7), ("dos-windows", 8), ("windows95", 9), ))).setMaxAccess("readonly")
cpqHoTelnet = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("available", 2), ("notavailable", 3), ))).setMaxAccess("readonly")
cpqHoSystemRole = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
cpqHoSystemRoleDetail = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 7), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
cpqHoCrashDumpState = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,2,3,)).subtype(namedValues=namedval.NamedValues(("completememorydump", 1), ("kernelmemorydump", 2), ("smallmemorydump", 3), ("none", 4), ))).setMaxAccess("readonly")
cpqHoCrashDumpCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4), ))).setMaxAccess("readonly")
cpqHoCrashDumpMonitoring = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
cpqHoMaxLogicalCPUSupported = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 3))
cpqHoCpuUtilTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1))
cpqHoCpuUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoCpuUtilUnitIndex"))
cpqHoCpuUtilUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoCpuUtilMin = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
cpqHoCpuUtilFiveMin = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
cpqHoCpuUtilThirtyMin = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
cpqHoCpuUtilHour = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
cpqHoCpuUtilHwLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoFileSys = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 4))
cpqHoFileSysTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1))
cpqHoFileSysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoFileSysIndex"))
cpqHoFileSysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoFileSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoFileSysSpaceTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
cpqHoFileSysSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
cpqHoFileSysPercentSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
cpqHoFileSysAllocUnitsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
cpqHoFileSysAllocUnitsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
cpqHoFileSysStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("ok", 2), ("degraded", 3), ("failed", 4), ))).setMaxAccess("readonly")
cpqHoFileSysCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("ok", 2), ("degraded", 3), ("failed", 4), ))).setMaxAccess("readonly")
cpqHoIfPhysMap = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 5))
cpqHoIfPhysMapTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1))
cpqHoIfPhysMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoIfPhysMapIndex"))
cpqHoIfPhysMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoIfPhysMapSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoIfPhysMapIoBaseAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
cpqHoIfPhysMapIrq = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoIfPhysMapDma = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
cpqHoIfPhysMapMemBaseAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
cpqHoIfPhysMapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
cpqHoIfPhysMapDuplexState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("half", 2), ("full", 3), ))).setMaxAccess("readonly")
cpqHoIfPhysMapCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4), ))).setMaxAccess("readonly")
cpqHoIfPhysMapOverallCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4), ))).setMaxAccess("readonly")
cpqHoSWRunning = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 6))
cpqHoSWRunningTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1))
cpqHoSWRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoSWRunningIndex"))
cpqHoSWRunningIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoSWRunningName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoSWRunningDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoSWRunningVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoSWRunningDate = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 5), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
cpqHoSWRunningMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,2,1,4,6,7,3,8,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("start", 2), ("stop", 3), ("startAndStop", 4), ("count", 5), ("startAndCount", 6), ("countAndStop", 7), ("startCountAndStop", 8), ))).setMaxAccess("readonly")
cpqHoSWRunningState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("started", 2), ("stopped", 3), ))).setMaxAccess("readonly")
cpqHoSWRunningCount = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoSWRunningCountMin = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
cpqHoSWRunningCountMax = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
cpqHoSWRunningEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 11), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
cpqHoSWRunningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,5,3,6,1,2,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("normal", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6), ("disabled", 7), ))).setMaxAccess("readonly")
cpqHoSWRunningConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,5,3,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("starting", 2), ("initialized", 3), ("configured", 4), ("operational", 5), ))).setMaxAccess("readonly")
cpqHoSWRunningIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 14), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoSWRunningRedundancyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 15), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("master", 2), ("backup", 3), ("slave", 4), ))).setMaxAccess("readonly")
cpqHoSwRunningTrapDesc = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoSwVer = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 7))
cpqHoSwVerNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 1), Integer32()).setMaxAccess("readonly")
cpqHoSwVerTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2))
cpqHoSwVerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoSwVerIndex"))
cpqHoSwVerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoSwVerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("loaded", 2), ("notloaded", 3), ))).setMaxAccess("readonly")
cpqHoSwVerType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,3,5,1,6,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("driver", 2), ("agent", 3), ("sysutil", 4), ("application", 5), ("keyfile", 6), ))).setMaxAccess("readwrite")
cpqHoSwVerName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
cpqHoSwVerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
cpqHoSwVerDate = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
cpqHoSwVerLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 7), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
cpqHoSwVerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 8), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
cpqHoSwVerVersionBinary = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 9), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
cpqHoSwVerAgentsVer = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
cpqHoGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 8))
cpqHoGenericData = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 8, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 254))).setMaxAccess("readwrite")
cpqHoCriticalSoftwareUpdateData = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 8, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
cpqHoSwPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 9))
cpqHoSwPerfAppErrorDesc = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 9, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 254))).setMaxAccess("readonly")
cpqHoSystemStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 10))
cpqHoMibStatusArray = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 256))).setMaxAccess("readonly")
cpqHoConfigChangedDate = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
cpqHoGUID = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(16, 17))).setMaxAccess("readwrite")
cpqHoCodeServer = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 4), Integer32()).setMaxAccess("readonly")
cpqHoWebMgmtPort = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 5), Integer32()).setMaxAccess("readonly")
cpqHoGUIDCanonical = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(32, 36))).setMaxAccess("readwrite")
cpqHoTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 11))
cpqHoTrapFlags = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 11, 1), Integer32()).setMaxAccess("readonly")
cpqHoClients = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 12))
cpqHoClientLastModified = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
cpqHoClientDelete = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
cpqHoClientTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3))
cpqHoClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoClientIndex"))
cpqHoClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
cpqHoClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
cpqHoClientIpxAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
cpqHoClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
cpqHoClientCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
cpqHoClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
cpqHoMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 13))
cpqHoPhysicalMemorySize = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 1), Integer32()).setMaxAccess("readonly")
cpqHoPhysicalMemoryFree = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 2), Integer32()).setMaxAccess("readonly")
cpqHoPagingMemorySize = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 3), Integer32()).setMaxAccess("readonly")
cpqHoPagingMemoryFree = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 4), Integer32()).setMaxAccess("readonly")
cpqHoBootPagingFileSize = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
cpqHoBootPagingFileMinimumSize = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
cpqHoBootPagingFileVolumeFreeSpace = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 7), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
cpqHoFwVer = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 14))
cpqHoFwVerTable = MibTable((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1))
cpqHoFwVerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1)).setIndexNames((0, "CPQHOST-MIB", "cpqHoFwVerIndex"))
cpqHoFwVerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 1), Integer32()).setMaxAccess("readonly")
cpqHoFwVerCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,5,1,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("storage", 2), ("nic", 3), ("rib", 4), ("system", 5), ))).setMaxAccess("readonly")
cpqHoFwVerDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(8,22,5,13,18,19,4,15,17,23,1,11,3,10,25,6,12,20,24,7,14,21,2,9,16,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("scsiDiskDrive-ScsiAttached", 10), ("scsiTapeDrive-ScsiAttached", 11), ("scsiTapeLibrary-ScsiAttached", 12), ("scsiDiskDrive-ArrayAttached", 13), ("scsiTapeDrive-ArrayAttached", 14), ("scsiTapeLibrary-ArrayAttached", 15), ("scsiDiskDrive-FibreAttached", 16), ("scsiTapeDrive-FibreAttached", 17), ("scsiTapeLibrary-FibreAttached", 18), ("scsiEnclosureBackplaneRom-ScsiAttached", 19), ("internalArrayController", 2), ("scsiEnclosureBackplaneRom-ArrayAttached", 20), ("scsiEnclosureBackplaneRom-FibreAttached", 21), ("scsiEnclosureBackplaneRom-ra4x00", 22), ("systemRom", 23), ("networkInterfaceController", 24), ("remoteInsightBoard", 25), ("fibreArrayController", 3), ("scsiController", 4), ("fibreChannelTapeController", 5), ("modularDataRouter", 6), ("ideCdRomDrive", 7), ("ideDiskDrive", 8), ("scsiCdRom-ScsiAttached", 9), ))).setMaxAccess("readonly")
cpqHoFwVerDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
cpqHoFwVerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
cpqHoFwVerLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoFwVerXmlString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 7), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
cpqHoFwVerKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 8), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
cpqHoFwVerUpdateMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("noUpdate", 2), ("softwareflash", 3), ("replacePhysicalRom", 4), ))).setMaxAccess("readonly")
cpqHoHWInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 15))
cpqHoHWInfoPlatform = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 15, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,5,1,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("cellular", 2), ("foundation", 3), ("virtualMachine", 4), ("serverBlade", 5), ))).setMaxAccess("readonly")
cpqPwrThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 11, 2, 16))
cpqPwrWarnType = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 254))).setMaxAccess("readwrite")
cpqPwrWarnThreshold = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 2), Integer32()).setMaxAccess("readwrite")
cpqPwrWarnDuration = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 3), Integer32()).setMaxAccess("readwrite")
cpqSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 254))).setMaxAccess("readwrite")
cpqServerUUID = MibScalar((1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 254))).setMaxAccess("readwrite")

# Augmentions

# Notifications

cpqHo2GenericTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11003)).setObjects(("CPQHOST-MIB", "cpqHoGenericData"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2NicStatusOk = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11005)).setObjects(("CPQHOST-MIB", "cpqHoIfPhysMapSlot"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2NicStatusFailed2 = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11009)).setObjects(("CPQHOST-MIB", "cpqHoIfPhysMapSlot"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoIfPhysMapPort"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoProcessCountWarning = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11012)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoSWRunningName"), ("CPQHOST-MIB", "cpqHoSWRunningCountMax"), ("CPQHOST-MIB", "cpqHoSWRunningEventTime"), ("CPQHOST-MIB", "cpqHoSWRunningCountMin"), ("CPQHOST-MIB", "cpqHoSWRunningCount"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoGenericTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11001)).setObjects(("CPQHOST-MIB", "cpqHoGenericData"), )
cpqHoBootPagingFileOrFreeSpaceTooSmallTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11019)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoBootPagingFileVolumeFreeSpace"), ("CPQHOST-MIB", "cpqHoBootPagingFileSize"), ("CPQHOST-MIB", "cpqHoBootPagingFileMinimumSize"), ("CPQHOST-MIB", "cpqHoCrashDumpState"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2NicSwitchoverOccurred2 = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11010)).setObjects(("CPQHOST-MIB", "cpqHoIfPhysMapSlot"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoIfPhysMapPort"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2NicSwitchoverOccurred = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11007)).setObjects(("CPQHOST-MIB", "cpqHoIfPhysMapSlot"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2AppErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11004)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoSwPerfAppErrorDesc"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoCriticalSoftwareUpdateTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11014)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoCriticalSoftwareUpdateData"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2NicStatusOk2 = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11008)).setObjects(("CPQHOST-MIB", "cpqHoIfPhysMapSlot"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoIfPhysMapPort"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoAppErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11002)).setObjects(("CPQHOST-MIB", "cpqHoSwPerfAppErrorDesc"), )
cpqHo2NicStatusFailed = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11006)).setObjects(("CPQHOST-MIB", "cpqHoIfPhysMapSlot"), ("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoBootPagingFileTooSmallTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11016)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoBootPagingFileMinimumSize"), ("CPQHOST-MIB", "cpqHoBootPagingFileSize"), ("CPQHOST-MIB", "cpqHoCrashDumpState"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoCrashDumpNotEnabledTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11015)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoCrashDumpState"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoProcessEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11011)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoSwRunningTrapDesc"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHo2PowerThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11018)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqSerialNum"), ("CPQHOST-MIB", "cpqServerUUID"), ("CPQHOST-MIB", "cpqPwrWarnThreshold"), ("CPQHOST-MIB", "cpqPwrWarnType"), ("CPQHOST-MIB", "cpqPwrWarnDuration"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoProcessCountNormal = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11013)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoSWRunningName"), ("CPQHOST-MIB", "cpqHoSWRunningCountMax"), ("CPQHOST-MIB", "cpqHoSWRunningEventTime"), ("CPQHOST-MIB", "cpqHoSWRunningCountMin"), ("CPQHOST-MIB", "cpqHoSWRunningCount"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )
cpqHoSWRunningStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 0, 11017)).setObjects(("RFC1213-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoSWRunningConfigStatus"), ("CPQHOST-MIB", "cpqHoSwRunningTrapDesc"), ("CPQHOST-MIB", "cpqHoSWRunningIdentifier"), ("CPQHOST-MIB", "cpqHoSWRunningDesc"), ("CPQHOST-MIB", "cpqHoSWRunningRedundancyMode"), ("CPQHOST-MIB", "cpqHoSWRunningVersion"), ("CPQHOST-MIB", "cpqHoSWRunningStatus"), ("CPQHOST-MIB", "cpqHoSWRunningName"), ("CPQHOST-MIB", "cpqHoTrapFlags"), )

# Exports

# Objects
mibBuilder.exportSymbols("CPQHOST-MIB", compaq=compaq, cpqHostOs=cpqHostOs, cpqHoMibRev=cpqHoMibRev, cpqHoMibRevMajor=cpqHoMibRevMajor, cpqHoMibRevMinor=cpqHoMibRevMinor, cpqHoMibCondition=cpqHoMibCondition, cpqHoComponent=cpqHoComponent, cpqHoInterface=cpqHoInterface, cpqHoOsCommon=cpqHoOsCommon, cpqHoOsCommonPollFreq=cpqHoOsCommonPollFreq, cpqHoOsCommonModuleTable=cpqHoOsCommonModuleTable, cpqHoOsCommonModuleEntry=cpqHoOsCommonModuleEntry, cpqHoOsCommonModuleIndex=cpqHoOsCommonModuleIndex, cpqHoOsCommonModuleName=cpqHoOsCommonModuleName, cpqHoOsCommonModuleVersion=cpqHoOsCommonModuleVersion, cpqHoOsCommonModuleDate=cpqHoOsCommonModuleDate, cpqHoOsCommonModulePurpose=cpqHoOsCommonModulePurpose, cpqHoInfo=cpqHoInfo, cpqHoName=cpqHoName, cpqHoVersion=cpqHoVersion, cpqHoDesc=cpqHoDesc, cpqHoOsType=cpqHoOsType, cpqHoTelnet=cpqHoTelnet, cpqHoSystemRole=cpqHoSystemRole, cpqHoSystemRoleDetail=cpqHoSystemRoleDetail, cpqHoCrashDumpState=cpqHoCrashDumpState, cpqHoCrashDumpCondition=cpqHoCrashDumpCondition, cpqHoCrashDumpMonitoring=cpqHoCrashDumpMonitoring, cpqHoMaxLogicalCPUSupported=cpqHoMaxLogicalCPUSupported, cpqHoUtil=cpqHoUtil, cpqHoCpuUtilTable=cpqHoCpuUtilTable, cpqHoCpuUtilEntry=cpqHoCpuUtilEntry, cpqHoCpuUtilUnitIndex=cpqHoCpuUtilUnitIndex, cpqHoCpuUtilMin=cpqHoCpuUtilMin, cpqHoCpuUtilFiveMin=cpqHoCpuUtilFiveMin, cpqHoCpuUtilThirtyMin=cpqHoCpuUtilThirtyMin, cpqHoCpuUtilHour=cpqHoCpuUtilHour, cpqHoCpuUtilHwLocation=cpqHoCpuUtilHwLocation, cpqHoFileSys=cpqHoFileSys, cpqHoFileSysTable=cpqHoFileSysTable, cpqHoFileSysEntry=cpqHoFileSysEntry, cpqHoFileSysIndex=cpqHoFileSysIndex, cpqHoFileSysDesc=cpqHoFileSysDesc, cpqHoFileSysSpaceTotal=cpqHoFileSysSpaceTotal, cpqHoFileSysSpaceUsed=cpqHoFileSysSpaceUsed, cpqHoFileSysPercentSpaceUsed=cpqHoFileSysPercentSpaceUsed, cpqHoFileSysAllocUnitsTotal=cpqHoFileSysAllocUnitsTotal, cpqHoFileSysAllocUnitsUsed=cpqHoFileSysAllocUnitsUsed, cpqHoFileSysStatus=cpqHoFileSysStatus, cpqHoFileSysCondition=cpqHoFileSysCondition, cpqHoIfPhysMap=cpqHoIfPhysMap, cpqHoIfPhysMapTable=cpqHoIfPhysMapTable, cpqHoIfPhysMapEntry=cpqHoIfPhysMapEntry, cpqHoIfPhysMapIndex=cpqHoIfPhysMapIndex, cpqHoIfPhysMapSlot=cpqHoIfPhysMapSlot, cpqHoIfPhysMapIoBaseAddr=cpqHoIfPhysMapIoBaseAddr, cpqHoIfPhysMapIrq=cpqHoIfPhysMapIrq, cpqHoIfPhysMapDma=cpqHoIfPhysMapDma, cpqHoIfPhysMapMemBaseAddr=cpqHoIfPhysMapMemBaseAddr, cpqHoIfPhysMapPort=cpqHoIfPhysMapPort, cpqHoIfPhysMapDuplexState=cpqHoIfPhysMapDuplexState, cpqHoIfPhysMapCondition=cpqHoIfPhysMapCondition, cpqHoIfPhysMapOverallCondition=cpqHoIfPhysMapOverallCondition, cpqHoSWRunning=cpqHoSWRunning, cpqHoSWRunningTable=cpqHoSWRunningTable, cpqHoSWRunningEntry=cpqHoSWRunningEntry, cpqHoSWRunningIndex=cpqHoSWRunningIndex, cpqHoSWRunningName=cpqHoSWRunningName, cpqHoSWRunningDesc=cpqHoSWRunningDesc, cpqHoSWRunningVersion=cpqHoSWRunningVersion, cpqHoSWRunningDate=cpqHoSWRunningDate, cpqHoSWRunningMonitor=cpqHoSWRunningMonitor, cpqHoSWRunningState=cpqHoSWRunningState, cpqHoSWRunningCount=cpqHoSWRunningCount, cpqHoSWRunningCountMin=cpqHoSWRunningCountMin, cpqHoSWRunningCountMax=cpqHoSWRunningCountMax, cpqHoSWRunningEventTime=cpqHoSWRunningEventTime, cpqHoSWRunningStatus=cpqHoSWRunningStatus, cpqHoSWRunningConfigStatus=cpqHoSWRunningConfigStatus, cpqHoSWRunningIdentifier=cpqHoSWRunningIdentifier, cpqHoSWRunningRedundancyMode=cpqHoSWRunningRedundancyMode, cpqHoSwRunningTrapDesc=cpqHoSwRunningTrapDesc, cpqHoSwVer=cpqHoSwVer, cpqHoSwVerNextIndex=cpqHoSwVerNextIndex, cpqHoSwVerTable=cpqHoSwVerTable, cpqHoSwVerEntry=cpqHoSwVerEntry, cpqHoSwVerIndex=cpqHoSwVerIndex, cpqHoSwVerStatus=cpqHoSwVerStatus, cpqHoSwVerType=cpqHoSwVerType, cpqHoSwVerName=cpqHoSwVerName, cpqHoSwVerDescription=cpqHoSwVerDescription, cpqHoSwVerDate=cpqHoSwVerDate, cpqHoSwVerLocation=cpqHoSwVerLocation, cpqHoSwVerVersion=cpqHoSwVerVersion, cpqHoSwVerVersionBinary=cpqHoSwVerVersionBinary, cpqHoSwVerAgentsVer=cpqHoSwVerAgentsVer, cpqHoGeneric=cpqHoGeneric, cpqHoGenericData=cpqHoGenericData, cpqHoCriticalSoftwareUpdateData=cpqHoCriticalSoftwareUpdateData, cpqHoSwPerf=cpqHoSwPerf, cpqHoSwPerfAppErrorDesc=cpqHoSwPerfAppErrorDesc, cpqHoSystemStatus=cpqHoSystemStatus, cpqHoMibStatusArray=cpqHoMibStatusArray, cpqHoConfigChangedDate=cpqHoConfigChangedDate, cpqHoGUID=cpqHoGUID, cpqHoCodeServer=cpqHoCodeServer, cpqHoWebMgmtPort=cpqHoWebMgmtPort, cpqHoGUIDCanonical=cpqHoGUIDCanonical, cpqHoTrapInfo=cpqHoTrapInfo, cpqHoTrapFlags=cpqHoTrapFlags, cpqHoClients=cpqHoClients, cpqHoClientLastModified=cpqHoClientLastModified, cpqHoClientDelete=cpqHoClientDelete, cpqHoClientTable=cpqHoClientTable, cpqHoClientEntry=cpqHoClientEntry, cpqHoClientIndex=cpqHoClientIndex, cpqHoClientName=cpqHoClientName, cpqHoClientIpxAddress=cpqHoClientIpxAddress, cpqHoClientIpAddress=cpqHoClientIpAddress, cpqHoClientCommunity=cpqHoClientCommunity, cpqHoClientID=cpqHoClientID, cpqHoMemory=cpqHoMemory, cpqHoPhysicalMemorySize=cpqHoPhysicalMemorySize, cpqHoPhysicalMemoryFree=cpqHoPhysicalMemoryFree, cpqHoPagingMemorySize=cpqHoPagingMemorySize, cpqHoPagingMemoryFree=cpqHoPagingMemoryFree)
mibBuilder.exportSymbols("CPQHOST-MIB", cpqHoBootPagingFileSize=cpqHoBootPagingFileSize, cpqHoBootPagingFileMinimumSize=cpqHoBootPagingFileMinimumSize, cpqHoBootPagingFileVolumeFreeSpace=cpqHoBootPagingFileVolumeFreeSpace, cpqHoFwVer=cpqHoFwVer, cpqHoFwVerTable=cpqHoFwVerTable, cpqHoFwVerEntry=cpqHoFwVerEntry, cpqHoFwVerIndex=cpqHoFwVerIndex, cpqHoFwVerCategory=cpqHoFwVerCategory, cpqHoFwVerDeviceType=cpqHoFwVerDeviceType, cpqHoFwVerDisplayName=cpqHoFwVerDisplayName, cpqHoFwVerVersion=cpqHoFwVerVersion, cpqHoFwVerLocation=cpqHoFwVerLocation, cpqHoFwVerXmlString=cpqHoFwVerXmlString, cpqHoFwVerKeyString=cpqHoFwVerKeyString, cpqHoFwVerUpdateMethod=cpqHoFwVerUpdateMethod, cpqHoHWInfo=cpqHoHWInfo, cpqHoHWInfoPlatform=cpqHoHWInfoPlatform, cpqPwrThreshold=cpqPwrThreshold, cpqPwrWarnType=cpqPwrWarnType, cpqPwrWarnThreshold=cpqPwrWarnThreshold, cpqPwrWarnDuration=cpqPwrWarnDuration, cpqSerialNum=cpqSerialNum, cpqServerUUID=cpqServerUUID)

# Notifications
mibBuilder.exportSymbols("CPQHOST-MIB", cpqHo2GenericTrap=cpqHo2GenericTrap, cpqHo2NicStatusOk=cpqHo2NicStatusOk, cpqHo2NicStatusFailed2=cpqHo2NicStatusFailed2, cpqHoProcessCountWarning=cpqHoProcessCountWarning, cpqHoGenericTrap=cpqHoGenericTrap, cpqHoBootPagingFileOrFreeSpaceTooSmallTrap=cpqHoBootPagingFileOrFreeSpaceTooSmallTrap, cpqHo2NicSwitchoverOccurred2=cpqHo2NicSwitchoverOccurred2, cpqHo2NicSwitchoverOccurred=cpqHo2NicSwitchoverOccurred, cpqHo2AppErrorTrap=cpqHo2AppErrorTrap, cpqHoCriticalSoftwareUpdateTrap=cpqHoCriticalSoftwareUpdateTrap, cpqHo2NicStatusOk2=cpqHo2NicStatusOk2, cpqHoAppErrorTrap=cpqHoAppErrorTrap, cpqHo2NicStatusFailed=cpqHo2NicStatusFailed, cpqHoBootPagingFileTooSmallTrap=cpqHoBootPagingFileTooSmallTrap, cpqHoCrashDumpNotEnabledTrap=cpqHoCrashDumpNotEnabledTrap, cpqHoProcessEventTrap=cpqHoProcessEventTrap, cpqHo2PowerThresholdTrap=cpqHo2PowerThresholdTrap, cpqHoProcessCountNormal=cpqHoProcessCountNormal, cpqHoSWRunningStatusChangeTrap=cpqHoSWRunningStatusChangeTrap)

