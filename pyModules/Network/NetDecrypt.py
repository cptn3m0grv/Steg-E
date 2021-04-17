import sys
from scapy.all import *
import re

def doTheDecryption(key, resultLoc):

    readpack = rdpcap(resultLoc)
    key_char = ""
    for eachpack in readpack:
        mm = eachpack['Raw'].load.decode('utf-8')
        ml = re.findall(r'\$3%`\/llllnois@.*\$3%`\/', mm)
        if(len(ml) == 0):
            val = eachpack['TCP'].window
            # print(val)
            key_char = key_char + chr(int(int(val)/80))
        else:
            dcr = mm[14:-5]

    if(key_char == key):
        print(dcr)
    else:
        print("Enter the right key!!!!")

doTheDecryption("habibullaaaaaa", "./Final1.pcap")