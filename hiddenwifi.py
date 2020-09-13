from scapy.all import *
import os

iface ="wlan0"

def d_packet(packet):
    if packet.haslayer(Dot11ProbReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11Assoreq)
        print "SSID Identified" + packet.info


os.system("iwconfig " + iface + "monitor mode")
print "Sniffing traffic on interface" + iface
sniff(iface=iface, pri=h_packet)

