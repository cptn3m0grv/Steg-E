import sys
from scapy.all import *
from scapy.arch import windows

a="""vousPXab9rd4VajKBPml@#
1qyInYhgxLaDhu8YFApT!4
p6MJYZUx2UHWvqqvXwXa1~3
AXY665wOHyWjsRF4AE5B&%
JSVrcKubMq7cWOF7k7ci:
zyCEzR2XkfdH7ZQg0lEN
HYJ0GdLGRkeo701Tl2RO
RcT0EPv2B0QyS2mDtTlJ
xYbvcYtKKHQEjHociOpV
VsC84NoMcw260MGwRa0N
0NDFttHzcX9aDVL7YPsA
rgt2K82RaYT4KVKFUbW9
Y3d6TDCDJdBQM2oQQgAB
73q2vXdPGS5D2xsasySj
EEdzosTi98DsTGsJm06j
fxfhhBvA46ZH5pHM4GtX
lpmvGScqeaH7v0JxRkip
yfBQ899d5PiXiruLLCAf
86guJXm81z2cUhi88Pae
17VgOw4vnQhSZsZkDjmT
se6ZBx2WPNa4dUOTezcy
SYNFrgVpfo1J3sTenRup
P8pI2LxqVsEXnxnC9w0O
FW03fDLKvaBr1GXAQtxP
732yEmqf7Bfi832oREYf"""

asffghhhhhhhhhhhfgl

pck=Ether()/IP(src="127.0.0.1",dst="127.0.0.1")/TCP(window=1234)/a
print("showing packet")


wrpcap('new3.pcap',pck)

#p=rdpcap('my.pcap')
#k=len(p)
#print(k)
#print(p[5])