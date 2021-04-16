import sys
import gibberish
from scapy.all import *
from scapy.utils import PcapWriter
from scapy.arch import windows
from gibberish import Gibberish

pktdump = PcapWriter("Test5.pcap", append=True, sync=True)

key="Tst@!@#$Tsdkjfksdfdsgldglfgkjlkajlskjdas"
message="holla I am te encrypted message"


key_array=[]
gib=Gibberish()
for char in key:
    p=(ord(char)*80)
    key_array.append(p)

for int_key in key_array:
    rawword=gib.generate_word(12)
    print(len(rawword))
    pck1=Ether()/IP(src="127.0.0.1",dst="127.0.0.1")/TCP(window=int_key)/rawword
    pktdump.write(pck1)

pck2=Ether()/IP(src="127.0.0.1",dst="127.0.0.1")/TCP()/message
pktdump.write(pck2)

#print("pcap file made")


#p=rdpcap('my.pcap')
#k=len(p)
#print(k)
#print(p[5])
