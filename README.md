# GatewayBleeding

Tools for attacks on FHRP domains

## Disclaimer
**These tools are designed to attack HSRP and VRRP protocols. With them, you can intercept traffic within the network by intercepting the main role of the router in the FHRP domain. 
The author has nothing to do with those who will use these tools for personal purposes to destroy other people's computer networks. The tools are presented for training purposes to help engineers improve the security of their network.**

**!!! HSRPWNv2.py - this script is designed to attack the HSRP protocol version 2.**

**ᛝ**

```
python3 HSRPWN.py --help

MMMMMMMMMMMМ МММММММММMM MMMMMMMMMMMМ MMMMMMMMMMMМ MMMMMMMMMMMМММ MММММММММММ 
M  MMMMM  MM M  mmmmm..M MM  mmmm,  M MM  mmmmm  M M  MMM  MMM  M M  mmmm.  M 
M         `M M.      `YM M'        .M M'        .M M  MMP  MMP  M M  MMMMM  M 
M  MMMMM  MM MMMMMMM.  M MM  MMMb. "M MM  MMMMMMMM M  MM'  MM' .M M  MMMMM  M 
M  MMMMM  MM M. .MMM'  M MM  MMMMM  M MM  MMMMMMMM M  `' . '' .MM M  MMMMM  M 
M  MMMMM  MM Mb.     .dM MM  MMMMM  M MM  MMMMMMMM M    .d  .dMMM M  MMMMM  M 
MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMMMM MMMMMMMMMMM
    
HSRP packet injection tool for traffic interception

Author: necreas1ng, <necreas1ng@protonmail.com>

usage: HSRPWN.py [-h] --interface INTERFACE --group GROUP --ip ATTACKERIP --vip VIP --auth AUTH

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Select your network interface
  --group GROUP         Choose HSRP group ID value
  --ip ATTACKERIP       Specify your IP address
  --vip VIP             Specify HSRP Virtual IP address
  --auth AUTH           Enter the auth HSRP passphrase

```

```
python3 HSRPWNv2.py --help

MMMMMMMMMMMМ МММММММММMM MMMMMMMMMMMМ MMMMMMMMMMMМ MMMMMMMMMMMМММ MММММММММММ 
M  MMMMM  MM M  mmmmm..M MM  mmmm,  M MM  mmmmm  M M  MMM  MMM  M M  mmmm.  M 
M         `M M.      `YM M'        .M M'        .M M  MMP  MMP  M M  MMMMM  M 
M  MMMMM  MM MMMMMMM.  M MM  MMMb. "M MM  MMMMMMMM M  MM'  MM' .M M  MMMMM  M 
M  MMMMM  MM M. .MMM'  M MM  MMMMM  M MM  MMMMMMMM M  `' . '' .MM M  MMMMM  M 
M  MMMMM  MM Mb.     .dM MM  MMMMM  M MM  MMMMMMMM M    .d  .dMMM M  MMMMM  M 
MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMMMM MMMMMMMMMMM
    
HSRP packet injection tool for traffic interception (For HSRPv2 version)

Author: @necreas1ng, <necreas1ng@protonmail.com>

usage: HSRPWNv2.py [-h] --interface INTERFACE --group GROUP --ip ATTACKERIP --vip VIP --auth AUTH

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Select your network interface
  --group GROUP         Choose HSRP group ID value
  --ip ATTACKERIP       Specify your IP address
  --vip VIP             Specify HSRP Virtual IP address
  --auth AUTH           Enter the auth HSRP passphrase
```

```
python3 VRRPWN.py --help

МММММММММММ ММММММММММММ ММММММММММММ ММММММММММММ МММММММММММММММ ММММММММММ
M  MMMMM  M MM  mmmm,  M MM  mmmm,  M MM  mmmmm  M M  MMM  MMM  M M  mmmm.  M 
M  MMMMP  M M'        .M M'        .M M'        .M M  MMP  MMP  M M  MMMMM  M 
M  MMMM' .M MM  MMMb. "M MM  MMMb. "M MM  MMMMMMMM M  MM'  MM' .M M  MMMMM  M 
M  MMP' .MM MM  MMMMM  M MM  MMMMM  M MM  MMMMMMMM M  `' . '' .MM M  MMMMM  M 
M     .dMMM MM  MMMMM  M MM  MMMMM  M MM  MMMMMMMM M    .d  .dMMM M  MMMMM  M 
MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMMMM MMMMMMMMMMM  
    
VRRP packet injection tool for traffic interception

Author: necreas1ng, <necreas1ng@protonmail.com>

usage: VRRPWN.py [-h] --interface INTERFACE --group GROUP --ip ATTACKERIP --vip VIP

options:
  -h, --help            show this help message and exit
  --interface INTERFACE
                        Select your network interface
  --group GROUP         Choose VRRP group ID value
  --ip ATTACKERIP       Specify your IP address
  --vip VIP             Specify VRRP Virtual IP address
  ```
