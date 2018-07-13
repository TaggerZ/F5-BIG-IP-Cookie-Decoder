# -*- coding: utf-8 -*-
import struct
import sys
class Colors:
    BLUE 		= '\033[94m'
    GREEN 		= '\033[32m'
    RED 		= '\033[0;31m'
    DEFAULT		= '\033[0m'
    ORANGE 		= '\033[33m'
    WHITE 		= '\033[97m'
    BOLD 		= '\033[1m'
    BR_COLOUR 	= '\033[1;37;40m'
if len(sys.argv) != 2:
    print("[*] python f5decoder.py 185903296.21520.0000" % sys.argv[0])
    exit(1)
encoded_string = sys.argv[1]
(host, port, end) = encoded_string.split('.')
(a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]
decIp = "%s.%s.%s.%s"%(a,b,c,d)
(e) = [ord(e) for e in struct.pack("<H", int(port))]
decPort = str(int("0x%02X%02X" % (e[0],e[1]),16))
result = Colors.GREEN + "[*] success \t " + Colors.WHITE+"| " + Colors.DEFAULT + encoded_string +Colors.WHITE+ " \t | "+ Colors.BLUE + decIp +Colors.BLUE+ " : " + Colors.BLUE + decPort + Colors.DEFAULT
print(result)