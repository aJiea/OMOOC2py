import SimpleHTTPServer
import socket
import struct
from os import chdir

import androidhelper
droid = androidhelper.Android()

ipdec = droid.wifiGetConnectionInfo().result['ip_address']
ipstr = socket.inet_ntoa(struct.pack('L', ipdec))

chdir('/sdcard')

print "Connect to %s" % ipstr

SimpleHTTPServer.test()
