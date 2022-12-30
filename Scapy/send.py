#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.getLogger("scapy").setLevel(logging.CRITICAL)
from scapy.all import *
print(get_if_list())
print(conf.ifaces)
print(conf.route)
conf.route.add(host=('127.0.0.1'), gw="192.168.29.1")
print(get_if_list())
print(conf.ifaces)
print(conf.route)

#send(IP(dst="1.2.3.4")/ICMP())
#sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface="eth1")
#sendp("I'm travelling on Ethernet", iface="eth1", loop=1, inter=0.2)
#sendp(rdpcap("smtp.pcap")) 
# tcpreplay
send(IP(dst='127.0.0.1'), return_packets=True)
#send(IP(dst="target")/fuzz(UDP()/NTP(version=4)),loop=1)
