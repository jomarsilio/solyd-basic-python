from jnpr.junos import Device

dev = Device( user='sgi', host='idc-aru-bng01.int.cont.net', password='pass' )

dev.open()

print dev.facts

dev.close()
