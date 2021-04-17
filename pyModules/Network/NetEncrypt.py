import sys
import string
import random
import numpy as np
from scapy.all import *
from scapy.utils import PcapWriter
from scapy.arch import windows

def doTheJob(message, key, resultLoc):
    pktdump = PcapWriter(resultLoc, append=True, sync=True)
    
    key_list = []

    for char in key:
        key_list.append((ord(char)*80))

    randWindow = np.random.randint(33, 127)
    randIndex = np.random.randint(0, len(key_list))

    randWindow = randWindow*80
    key_list.insert(randIndex, randWindow)
    #IllInois
    for idx in range(0, len(key_list)):
        if(idx==randIndex):
            rawword = message
            salt = '$3%`/llllnois@'
            encr = salt + rawword + '$3%`/'
            pck = Ether()/IP(src="192.168.0.110", dst="192.168.0.111")/TCP(window=key_list[idx])/encr
        else:
            rawword = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k = len(message)))
            salt = '$3%`/IllInois@'
            encr = salt + rawword + '$3$`/'
            pck = Ether()/IP(src="192.168.0.110", dst="192.168.0.111")/TCP(window=key_list[idx])/encr

        pktdump.write(pck)

doTheJob("hullla hullare hulla hullaaaaaaa", "habibullaaaaaaaa", "./Final1.pcap")