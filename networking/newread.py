import sys
from scapy.all import *

rawkey=[]
key=[]

readpack=rdpcap("Test5.pcap")
print(len(readpack))
for eachpack in readpack:
    rawkey.append(eachpack['TCP'].window)

for val in rawkey[:-1]:
    key.append(int((val/80)))

key_char=''.join(chr(i) for i in key)
print(key_char)
print(readpack[-1]['Raw'].load)


