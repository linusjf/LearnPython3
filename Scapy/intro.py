#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from scapy.layers.inet import IP
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

a = IP(ttl=10)
print(a)
print(a.src)
a.dst="192.168.1.1"
print(a)
print(a.src)
del(a.ttl)
print(a)
print(a.ttl)

a = IP(dst="www.slashdot.org/30")
print(a)
print([p for p in a])
b=IP(ttl=[1,2,(5,9)])
print(b)
print([p for p in b])
c=TCP(dport=[80,443])
print([p for p in a/c])

p = PacketList(a)
print(p)
p = PacketList([p for p in a/c])
print(p)
print(p.summary())
print(p.nsummary())
print(p.conversations())
print(p.show())
print(p.hexdump())
print(p.hexraw())
print(p.padding())
print(p.nzpadding())
