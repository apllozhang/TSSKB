

<<<PAGE 1>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
OMNISWITCH LAN - R8 
CORE SWITCHING - EDITION 15 
PARTICIPANT'S GUIDE

<<<PAGE 2>>>
Proprietary Ownership Declaration 
I agree not to copy, produce, reproduce, transfer, distribute, decode and/or modify any 
ALE material (including any and all documentation, manuals, software presentation, 
student book and software files) made available and/or used as part of the ALE training. 
I acknowledge that sharing of any kind of courseware and media used are strictly forbidden 
without approval from ALE Training Services. 
I represent and warrant that I will not use or not permit to use the courseware and\or 
educational tools supplied by ALE to provide trainings in a private capacity or for my 
employer or any third party. 
I also acknowledge and agree that ALE owns and reserves all copyright in and all other 
intellectual property rights relating to the ALE training material (including courseware and 
all associated documentation) provided during the training. 
I understand that any breach or threat of breach of the above shall entitle ALE to injunctive 
and other appropriate equitable relief (without the necessity of proving actual damages), 
in addition to whatever remedies ALE may have at law. 
Furthermore, I acknowledge and agree that ALE will be entitled to cancel immediately all 
my certifications in case of any breach of the above.

<<<PAGE 3>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.
Agenda
DT00XTE216EN
OmniSwitch Core Switching
AOS OmniSwitch LAN

<<<PAGE 4>>>
2
Topics
Administration – Class schedule
Course agenda
Your opinion counts!
Reach the session evaluation

<<<PAGE 5>>>
Administration – Class schedule
Standard class hours
Break
Badges for participants
Internet access
9:00 AM to 5:00 PM
Lunch 12:00 to 1:30 PM
Morning & Afternoon 15 Min
Access to the classroom & 
the restaurant

<<<PAGE 6>>>
Day 1
• Accces to R-Lab Presentation
• Overview - L3 Modular Switch Portfolio
• Overview & Lab - Ethernet Ring Protection (ERP)
• Overview  & lab - Mac-Sec 
• Overview  & lab - Private VLAN
• Overview  & lab - Multiple Spanning Tree Protocol 
(MSTP)
• Overview  & lab - Multiple VLAN Registration 
Protocol

<<<PAGE 7>>>
Day 2
• Overview - AOS Network Security
- Lab – Port mapping
- Lab - Learned Port Security
• Overview - IP interfaces
• Overview - Open Shortest Path First (OSPF)
- (Fundamentals, Areas, Adv. Features & Troubleshooting, Global 
Routing Protocol Redistribution)
- Lab – OSPF
• Overview: Graceful Restart
• Lab - DHCP Server & DHCP Relay

<<<PAGE 8>>>
Day 3
• Overview & Lab - Multicast Introduction
• Overview - Distance Vector Multicast Routing 
Protocol (DVMRP)
• Overview & Lab - Protocol Independent Multicast
• Overview & Lab - Virtual Routing & Forwarding (VRF)

<<<PAGE 9>>>
Day 4
• Overview & Lab - Border Gateway Protocol (BGP)
• Overview - SPB Overview & Labs
- Lab: Deploying a network based on SPB-M technology
- Lab: Deploying SPB-M technology-L2 services 
• Session evaluation 
- Link available on KNOWLEDGE HUB last day of the session

<<<PAGE 10>>>
• OmniSwitch xxxx Series Hardware Users Guide
• Switch hardware components and basic switch hardware
• OmniSwitch AOS Switch Management Guide
• Describes basic attributes of the switch and basic switch administration tasks
• OmniSwitch AOS Network Configuration Guide
• Describes how to set up and monitor software features that will allow the switch to operate in a live network 
environment
• OmniSwitch AOS Advanced Routing Configuration Guide
• Describes how to set up and monitor advanced routing protocols for operation in a live network environment
• OmniSwitch CLI Reference Guide
• Comprehensive resource to all Command Line Interface (CLI) commands available on the OmniSwitch products
• OmniSwitch Transceivers Guide
• Provides specifications and compatibility information for the supported OmniSwitch SFP and XFP transceivers for all 
OmniSwitch AOS 6 Release Products
AOS – Technical Documentations

<<<PAGE 11>>>
Internet Ressources
• Alcatel-Lucent Enterprise Web Site
https://www.al-enterprise.com/en
• Training & Certification
https://www.al-enterprise.com/en/services/education-services
• RFC Technical documents
http://www.ietf.org

<<<PAGE 12>>>
• Partners Website
• MyPortal
• ALE Network Equipment
• www.al-enterprise.com/en/products/switches
• Spacewalkers Community
• www.spacewalkers.com
Internet Resources

<<<PAGE 13>>>
REMOTE LAB CONNECTION
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 14>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Remote-Labs (R-Labs) topology
• Connect to a Remote-Lab (R-Lab)

<<<PAGE 15>>>
CONNECT TO THE DATA RLAB
• A web browser is required to connect to the Rlab
• Recommended web browsers:
• Chrome
• Edge
https://rdp.al-mydemo.com/
- Username: LanpodXa ou LanpodXb (X = R-Lab Number)
- Password:  unique per session – Sent from our LMS to the Instructor
Notes: Other web browser may have some issue with copy/paste from a lab guide to the remote terminal 
session. Known workaround for FireFox: https://sudoedit.com/firefox-async-clipboard/

<<<PAGE 16>>>
REMOTE LABS > TOPOLOGY EXAMPLE
Please note some PODs are using 6360A/6360B 
with 10 ports or some other with 24 ports
1/1/29-30
1/1/9
1/1/9
1/1/9
1/1/9
1/1/8
1/1/8
1/1/27-28
1/1/27-28
1/1/23-24
1/1/23-24
OS6560-A 3
OS6360-A 5
OS6360-B 6
OS6870-A 7
OS6860-B 8
OS6900-A 1
OS6870-B
2
Client 1
Client 2
Client 3
Client 5
Client 6
Client 8
Client 7
Client 9
Client 10
1/1/1
1/1/1
1/1/1
1/1/2
1/1/1
1/1/1
1/1/1
1/1/1
A
A
A
A
A
A
A
EMP
EMP
EMP
EMP
EMP
EMP
EMP
1/1/27
1/1/27
Client 4
1/1/12
1/1/25-26

<<<PAGE 17>>>
REMOTE LABS > TOPOLOGY
1
2
3
4

<<<PAGE 18>>>
VIRTUAL MACHINES
• 10 VM (Clients)
• AAA Training Server POD x
• DHCP Server, Radius Server: 192.168.100.102
• Web Server: 192.168.100.102
• FTP Server: 192.168.100.102 
• login “admin” and password “switch”
• Podx_OV<ov_release>
• OmniVista 2500: 192.168.100.107
• Firewall/NAT server
• Podx_pfSense : 192.168.100.108

<<<PAGE 19>>>
DHCP SERVER
• A DHCP server is running with an IP address of 192.168.100.102 and has the following 
scopes (where x stands for the switch number):

<<<PAGE 20>>>
OMNIVISTA 2500 & INTERNET ACCESS
• An OmniVista 2500 server is configured with the IP address 192.168.100.107/24.
• The OmniVista 2500 is reachable
from RDP desktop through a WEB 
client at the URL:
https://10.4.pod#.208:8443
• DNS server on the client : 10.0.0.51
• If Internet access is required for VM clients,
a pre-configuration has to be done on the OS6900-A

<<<PAGE 21>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 22>>>
OMNISWITCH AND STELLAR ACCESS POINTS 
EQUIPMENT - PORTFOLIO
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 23>>>
NETWORK PORTFOLIO
OmniAccess Stellar
WLAN
TECHNOLOGY PARTNERS
OmniSwitch
Hardened
OS6860N
OS2x60*
OS6560/E
OS6900
AP136x
OS6360
AP1301
AP132x 
AP1331
AP1301H
Asset Tracking
NETWORK SERVICES
OmniVista
OmniVista
2500 / Terra 
Network as a Service
SD-WAN/SASE
MPLS, DWDM, GPON
OS6570M
AP1311
AP1351
LAN
OmniVista
Cirrus
OmniVista Network 
Advisor
Access
Core
Ruggedized
OS6465/T
OS6865
*except in the USA
AP1511
AP1521
AP1431
AP1451
AP1411
OS9912
OS9900
VMS plugins
AP1541/42
H2 2025
AP1571/72
H1 2026
OS6870
Private LTE/5G

<<<PAGE 24>>>
OMNISWITCH LAN FAMILY
High end modular core, 
aggregation, Data center 
switches L2-L3 
Entry level stackable L2+
Advanced stackable L2-L3
⚫
Virtual chassis
⚫
10/100/1000/2.5G
/5G, 10Gig
⚫
IPv4/IPv6
⚫
PoE++
⚫
Copper & fiber
⚫
Advanced routing
⚫
Green energy
⚫
Virtual chassis 
⚫
10/100, 1G, 2.5G 
Copper and Fiber
⚫
POE++
⚫
Basic routing
⚫
Green energy
OmniSwitch 9900
Modular Chassis
AOS Advanced L3 10/40GE
OmniSwitch 6900
AOS Advanced L2-L3  
Aggregation/Core
DC TOR 10/40 GE
⚫
High Availability
⚫
High  Performance
⚫
10/25/40 Gig high 
density
⚫
MPLS / SPB 
⚫
Virtual Chassis
⚫
Green energy
⚫
I.S.S.U
Edge
Aggregation
Core
OmniSwitch 6865
AOS Advanced L3 
OmniSwitch
6860N
AOS Advanced L3 
OmniSwitch 
2260/2360
AOS L2 WebSmart
OmniSwitch 6560/E
AOS Advanced L3+ 
1GE/2.5G/5G 10G 
uplinks
OmniSwitch 6465
AOS L2+ Basic L3 GE -
10G uplinks
PROFINET Class B 
Certified
OmniSwitch 6360
AOS L2+ Basic L3 GE
OmniSwitch 6570M
AOS L3+ Metro Ethernet 
1GE/2.5G 10G uplinks
OmniSwitch 6870
AOS Advanced L3
1GE/2.5G/5G/10G
10/25/40/50/100G uplinks
200G VFL
New!

<<<PAGE 25>>>
OMNISWITCH
Positioning in the Stackable portfolio
Gig
Small
Gig w/ 10G
Hardened
Large
OmniSwitch 6360
10/P10/24/P24/PH24/ 
48/P48/P24X/P48X
Value AOS L2+ GE
OmniSwitch 6860E/6860N
16/24/48 (POE+) ports
8 x 2.5G Multi-Gigabit ports
Advanced AOS L3 GE
OmniSwitch 6865
6/12/28 ports
POE+, HPOE, SFP
Advanced AOS L3 GE
OmniSwitch 6560/E
P24/P48
8/16/24 2.5G/5G ports
AOS Advanced L3 licensed 
10G Uplinks
AOS
R8
OmniSwitch 2260
10/P10/24/P24/48/P48
OmniSwitch 2360 
24/P24/48/P48/P24X/P48X
Value AOS L2 WebSmart
OmniSwitch 6570M
12/12D/U28/U28D
AOS L3+ Metro Ethernet 
1GE/10G uplinks
Metro Ethernet
OmniSwitch 6465
AOS L2+ Basic L3 GE 
- 10G uplinks
OmniSwitch 6870
AOS Advanced L3
1GE/2.5G/5G/10G
10/25/40/50/100G uplinks
200G VFL
New!

<<<PAGE 26>>>
OMNISWITCH DETAILS - PRODUCT DATA SHEETS
Management Platform
• OmniVista 2500 (on premises) datasheet
• OmniVista Cirrus (cloud) datasheet
LAN Switches
• OmniSwitch LAN : Matrix
• OmniSwitch LAN : Products
• OmniSwitch 2260 WebSmart switch: datasheet
• OmniSwitch 2360 WebSmart switch: datasheet
• OmniSwitch 6360 LAN switch: datasheet
• OmniSwitch 6465 L2+ Hardened LAN Switch datasheet
• OmniSwitch 6560 L3 Multigig LAN switch: datasheet
• OmniSwitch 6570M L3 Metro Ethernet LAN switch: datasheet
• OmniSwitch 6860E/N L3 LAN switch with multigig and DPI option datasheet
• OmniSwitch 6865 L3 Hardened Switch datasheet
• OmniSwitch 6870 Next Gen L3 LAN switch with MPLS datasheet
• OmniSwitch 6900 L3 core switch datasheet
• OmniSwitch 9900 Chassis core switch datasheet

<<<PAGE 27>>>
STELLAR ACCESS POINTS

<<<PAGE 28>>>
OVERVIEW
OMNIACCESS STELLAR LINEUP – WIFI 6
WiFi 6
Indoor
MLE
AP132x
WiFi 6
Outdoor
Rugged
AP136x
WiFi 6
Indoor
SMB
AP1311
WiFi 6
Indoor
SMB
AP1301
WiFi 6
Indoor
MLE
AP1351
WiFi 6
Indoor
MLE
AP1331
WiFi 6
Indoor
Hosp.
AP1301H

<<<PAGE 29>>>
OVERVIEW
OMNIACCESS STELLAR LINEUP – WIFI 6E
WiFi 6E
Indoor
MLE
AP1431
WiFi 6E
Indoor
SMB
AP1411
WiFi 6E
Indoor
MLE
AP1451

<<<PAGE 30>>>
OVERVIEW
OMNIACCESS STELLAR LINEUP – WIFI 7
WiFi 7
Indoor
MLE
AP1521
WiFi 7
Indoor
SMB
AP1511

<<<PAGE 31>>>
OMNIACCESS
STELLAR WIFI 6, WIFI 6E & WIFI 7 LINEUP
Hotels, Dorms
& RAP
AP1301H
2×2:2 @ 2.4GHz
2x2:2 @ 5GHz
1 GE Uplink
4xGE Down (1 PoE)
RJ45 Passthrough, *
Outdoors
AP1361/62/61D
2×2:2 @ 2.4GHz
4x4:4 @ 5GHz
1 scanning radio
BLE/Zigbee, DPI
1x2.5GE Uplink + 1 SFP Uplink
1 GE PoE port Down
Premium
High-End
AP1351
4×4:4 @ 2.4GHz
8×8:8 @ 5GHz
4×4:4 @ 5GHz
1 scanning radio
BLE/Zigbee, DPI
2x10GE Uplink
Premium
Mid-Range
AP1331
4x4:4 @ 2.4GHz
4x4:4 @ 5GHz
1 scanning radio
BLE/Zigbee, DPI
2x5GE Uplink
Mid-Range
AP1321/22
2×2:2 @ 2.4GHz
4x4:4 @ 5GHz
1 scanning radio
BLE/Zigbee, DPI
1x2.5GE + 1GE Uplink
Premium 
Entry Level
AP1311
2×2:2 @ 2.4GHz
2×2:2 @ 5GHz
1 scanning radio
BLE/Zigbee, DPI
2xGE Uplink, 1xGE Down
Entry Level
AP1301
2×2:2 @ 2.4GHz
2×2:2 @ 5GHz
DPI
2xGE Uplink port
AP1431
2×2:2 @ 2.4GHz
2×2:2 @ 5GHz
2×2:2 @ 6GHz
BLE/Zigbee, DPI
2x2.5GE Uplink
Premium
Mid-Range
AP1541/42
2×2:2 @ 2.4GHz
4×4:4 @ 5GHz
4×4:4 @ 6GHz
2G/5G/6G Scanning Radio
BLE/Zigbee, DPI, GPS
2x 5GE Uplink
High-End
AP1511
2×2:2 @ 2.4GHz
2×2:2 @ 5GHz
2×2:2 @ 6GHz
BLE/Zigbee, DPI
1x 5GE Uplink
Premium
Entry Level
Mid-Range
AP1521
2×2:2 @ 2.4GHz
4×4:4 @ 5GHz
2×2:2 @ 6GHz
2G/5G/6G Scanning Radio
BLE/Zigbee, DPI
1x 10GE Uplink+ 1GE 
Uplink/Downlink
AP1451
4×4:4 @ 2.4GHz
8×8:8 @ 5GHz
4×4:4 @ 6GHz
1 scan radio
BLE/Zigbee, DPI
2x10GE Uplink
Premium
High-End
AP1411
2×2:2 @ 2.4GHz
2×2:2 @ 5GHz or @ 6GHz
BLE/Zigbee, DPI
2x1GE Uplink
Premium 
Entry Level
AP1571/72
2×2:2 @ 2.4GHz
2×2:2 @ 5GHz
2×2:2 @ 6GHz- SW Conf
2G/5G/6G Scanning Radio
BLE/Zigbee, DPI, GPS
1 x 10GbE + 1 x SFP/SFP+
Uplink
4 x 2.5G Downlink
Outdoors
Mid-Range

<<<PAGE 32>>>
OMNIACCESS STELLAR DETAILS - PRODUCT DATA SHEETS
• OmniAccess Stellar product matrix
• OmniAccess Wireless LAN products
• OmniAccess Stellar AP1301 entry level WiFi 6 AP: datasheet
• OmniAccess Stellar AP1301H resident WiFi 6 AP: datasheet
• OmniAccess Stellar AP1311 high performance WiFi 6 AP: datasheet
• OmniAccess Stellar AP1320 high performance WiFi 6 AP: datasheet
• OmniAccess Stellar AP1331 high performance WiFi 6 AP: datasheet
• OmniAccess Stellar AP1351 premium high-end WiFi 6 AP: datasheet
• OmniAccess Stellar AP1360 hardened outdoor WiFi 6 AP: datasheet
• OmniAccess Stellar AP1411 high performance WiFi 6E AP: datasheet
• OmniAccess Stellar AP1431 high performance WiFi 6E AP: datasheet
• OmniAccess Stellar AP1451 premium high-end WiFi 6E AP: datasheet
• OmniAccess Stellar AP1511 high performance WiFi 7 AP: datasheet
• OmniAccess Stellar AP1521 high performance WiFi 7 AP: datasheet

<<<PAGE 33>>>
ACCESSORIES > EXTERNAL ANTENNAS
• The External Antennas models and details can also be found in the Product Line Matrix 
documentation:
Click on this icon to view the full Antennas Matrix documentation (p. 6)

<<<PAGE 34>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 35>>>
ETHERNET RING PROTOCOL (ERP)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 36>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• List & Identify the ERP concepts
• Summarize the ERP principle
• Identify a failure in the ERP Ring
• Explain the recovery process

<<<PAGE 37>>>
ETHERNET RING PROTOCOL (ERP) - OVERVIEW
• Protection switching mechanism
• Maintains a loop-free topology in a ring
• Fast recovery times (~50 ms)
• Dedicated Protocol 
• APS (Automatic Protection Switching)
• AOS OmniSwitch supports ERPv2
• Works on single and multiple independent and laddered rings
Ring 2
Ring 1
Main 
Ring
Sub - Ring
Ring 1

<<<PAGE 38>>>
CONCEPTS
• Ring Protection Link (RPL) 
• Link between 2 ring switches that is blocked to 
prevent a loop in the ring
• RPL Owner
• Switch hosting the RPL Port
• Blocks traffic on the RPL Port during normal ring 
operations
• R-APS (Ring-Automatic Protection Switching) 
Messages
• Signal Fail (SF) 
• Declared when a failed link or node is detected
• No Request (NR)
• Declared when there are no outstanding conditions
(ex. SF) on the node
• Service VLAN
• Ring-wide VLAN used for transmission of R-APS 
messages
• Protected VLAN
• VLAN(s) that is/are added to the ERP ring
• ERP determines the forwarding state of protected 
VLAN(s)

<<<PAGE 39>>>
CONCEPTS
• 2 ring ports are identified in each switch
• 1 link in the ring is identified as the Ring Protection Link (RPL)
• One of the switches terminating the RPL is identified as RPL Owner
Normal ring port
RPL port on RPL Owner
RPL port
RPL Owner
RPL Protection Link

<<<PAGE 40>>>
STEADY STATE (NO FAILURE)
Blocked RPL port
RPL Owner
RPL Protection Link
NR (No Request) 
RB (RPL blocked)
R-APS MESSAGE

<<<PAGE 41>>>
RING FAILURE 
• Failure!     (Ring Mode: Protection)
• Adjacent ports are blocked
• Signal Failure (SF) R-APS message is sent
• RPL Owner unblocks RPL port
• Ring is protection mode
Unblocked RPL port
RPL Owner
RPL Protection Link
SF (Signal Fail)
R-APS MESSAGE
SF (Signal Fail)
R-APS MESSAGE
1
2
2
3
3
4
1
2
3
4

<<<PAGE 42>>>
RECOVERY
• Recovered Link
• Adjacent nodes remove SF (Signal Failure) and send NR (No Request)
• RPL Owner starts a Wait To Restore (WTR) timer (default: 5 minutes)
• When WTR timer expires, RPL port is blocked
• RPL Owner sends NR/RB (No Request/RPL Blocked)
• Other nodes unblock their ring ports      (Ring Mode: Idle)
RPL Owner
NR (No Request)
NR (No Request)
1
6
6
2
2
3
4
NR/RB (No Request)
1
2
3
4
5
6
5

<<<PAGE 43>>>
LADDERED RINGS (ERPV2)
• Laddered rings are composed of: 
• A Main ring
• One or more Subtending ring(s)
• The Main ring is a fully closed ring (A-B-D-C-A)
• The Subtended ring does not include any shared 
links with the main ring
• The Main ring acts as a virtual channel to close 
the Subtended ring
• R-APS messages are sent over the virtual channel 
using the S-tag (Service VLAN) of the subtended ring
Main 
Ring
Subtended
Ring
A
B
C
D
E
F
Main 
Ring
A
B
C
D
Subtended
Ring
C
D
E
F

<<<PAGE 44>>>
ETHERNET RING PROTOCOL (ERP)
Specifications

<<<PAGE 45>>>
ERP CONFIGURATION

<<<PAGE 46>>>
ERP CONFIGURATION
Step by Step
Create ERP Ring, Service VLAN & MEG Level
Configure the RPL Port
Add Protected VLAN(s)
Enable the ERP Ring

<<<PAGE 47>>>
ERP CONFIGURATION
Step by Step
Create an ERP Ring
Declare a Service VLAN
For transmission of R-APS messages 
Define a MEG Level (Management Entity Group)
Value from 0 to 7
Must be identical on all the switches belonging to the ERP Ring
1/2
1
3
2
4
1/1
1/3
1/1
1/4
1/3
1/2
1/4
ERP Ring
Ring 1
SVLAN 1001
MEG Level 1
Create ERP Ring, Service VLAN & MEG Level

<<<PAGE 48>>>
The RPL port is unique in an ERP Ring
Declared on one switch (= RPL Owner)
ERP CONFIGURATION
Step by Step
1/2
1
3
2
4
1/1
1/3
1/1
1/4
1/3
1/2
1/4
ERP Ring
Ring 1
SVLAN 1001
MEG Level 1
RPL Owner
RPL Port
Configure the RPL Port

<<<PAGE 49>>>
VLAN that is added to the ERP ring
ERP determines the forwarding
state of protected VLANs
Administratively activate the ERP Ring
(admin-state enable)
ERP CONFIGURATION
Step by Step
1/2
1
3
2
4
1/1
1/3
1/1
1/4
1/3
1/2
1/4
ERP Ring
Ring 1
SVLAN 1001
MEG Level 1
Prot. VLAN(s)
• 2
• 3
RPL Owner
RPL Port
Enable the ERP Ring
Add Protected VLAN(s)

<<<PAGE 50>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 51>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Ethernet Ring Protection 
How to 
✓ Create an ERP Ring and check its behavior 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configure ERPv2 ring ......................................................................... 3 
2.1. Initialize switches .................................................................................. 3 
2.2. Configure VLANs on the switches ................................................................ 3 
2.3. Configure the ERP on all switches................................................................ 5 
2.4. Make the physical connections according to the lab diagram ................................ 5 
2.5. Check the ERP Ring 1 setup by performing some show commands. ......................... 6 
3 
Lab Check ...................................................................................... 7 
3.1. Connect clients to switches ....................................................................... 7 
3.2. Test the feature .................................................................................... 8 
4 
ERP Sub ring 2 configuration ................................................................ 8 
4.1. Connect clients to switches ...................................................................... 10 
4.2. Test the feature ................................................................................... 11 
5 
Access - Core resiliency .................................................................... 11 
5.1. VRRP Verification .................................................................................. 12 
6 
Restore ....................................................................................... 12 
6.1. Restore initial configuration by restarting them from "working directory". .............. 12

<<<PAGE 52>>>
2 
Ethernet Ring Protection 
 
 1 
Topology 
Ethernet Ring Protection (ERP) is a protection switching mechanism for Ethernet ring topologies, such as 
multi-ring and ladder networks. This implementation of ERP uses the Automatic Protection Switching (APS) 
protocol to coordinate the prevention of network loops within a bridged Ethernet ring. 
ERP is used to prevent formation of loops which would fatally affect the network operation and service 
availability. 
Configuring ERP requires several steps. These steps are outlined here and more described in relevant 
OmniSwitch AOS Release Network Configuration Guides. 
 
 
 
- For this lab, you will learn how to configure the ring network (including a major ring and a sub ring) 
parameters through the Command Line Interface (CLI).

<<<PAGE 53>>>
3 
Ethernet Ring Protection 
 
 2 
Configure ERPv2 ring 
2.1. 
Initialize switches 
 
Create a User-defined directories “labERP”, copy the contents of the labinit directory and boot the switches 
from the new user-defined directory labERP): 
 
 
sw5 (6360-A) -> mkdir labERP 
sw5 (6360-A) -> cp labinit/*.* labERP 
sw5 (6360-A) -> ls labERP 
sw5 (6360-A) -> reload from labERP no rollback-timeout 
                Confirm Activate (Y/N): y 
sw5 (6360-A) -> show running-directory 
 
sw7 (6870-A) -> mkdir labERP 
sw7 (6870-A) -> cp labinit/*.* labERP 
sw7 (6870-A) -> ls labERP 
sw7 (6870-A) -> reload from labERP no rollback-timeout 
                Confirm Activate (Y/N): y 
sw7 (6870-A) -> show running-directory 
 
sw8 (6860-B) -> mkdir labERP 
sw8 (6860-B) -> cp labinit/*.* labERP 
sw8 (6860-B) -> ls labERP 
sw8 (6860-B) ->reload from labERP no rollback-timeout 
               Confirm Activate (Y/N): y 
sw8 (6860-B) ->show running-directory 
 
sw3 (6560-A) -> mkdir labERP 
sw3 (6560-A) -> cp labinit/*.* labERP 
sw3 (6560-A) -> ls labERP 
sw3 (6560-A) -> reload from labERP no rollback-timeout 
               Confirm Activate (Y/N): y 
sw3 (6560-A) -> show running-directory 
 
sw6 (6360-B) -> mkdir labERP 
sw6 (6360-B) -> cp labinit/*.* labERP 
sw6 (6360-B) -> ls labERP 
sw6 (6360-B) -> reload from labERP no rollback-timeout 
               Confirm Activate (Y/N): y 
sw6 (6360-B) -> show running-directory 
2.2. 
Configure VLANs on the switches 
 
- On each node belonging to ERP ring, configure VLAN 30 and VLAN 20:

<<<PAGE 54>>>
4 
Ethernet Ring Protection 
 
 
sw7 (6870-A) -> vlan 1001 name “Ring1” 
sw7 (6870-A) -> vlan 20 name “subnet20” 
sw7 (6870-A) -> vlan 30 name “subnet30” 
 
sw8 (6860-B) -> vlan 1001 name "Ring1"  
sw8 (6860-B) -> vlan 20 name "subnet20" 
sw8 (6860-B) -> vlan 30 name "subnet30" 
 
sw5 (6360-A) -> vlan 1001 name “Ring1” 
sw5 (6360-A) -> vlan 20 name “subnet20” 
sw5 (6360-A) -> vlan 30 name “subnet30” 
 
sw6 (6360-B) -> vlan 1001 name “Ring1” 
sw6 (6360-B) -> vlan 20 name “subnet20” 
sw6 (6360-B) -> vlan 30 name “subnet30” 
 
 
Notes: VLAN 1001 is the Service VLAN for ERP Ring 1, VLAN 20 and 30 are Protected VLAN. 
Service VLAN is used for the transmission and reception of R-APS Channel (tagged R-APS 
messages) and the ETH CCM (tagged CCM) for a given ring.   
 
 
- On 6870-A, tag Vlan 1001, VLAN 20 and 30 to the assigned ring ports 1/1/3 and 1/1/27: 
 
sw7 (6870-A) -> vlan 1001 members port 1/1/3 tagged 
sw7 (6870-A) -> vlan 1001 members port 1/1/27 tagged 
sw7 (6870-A) -> vlan 20 members port 1/1/3 tagged 
sw7 (6870-A) -> vlan 20 members port 1/1/27 tagged 
sw7 (6870-A) -> vlan 30 members port 1/1/3 tagged 
sw7 (6870-A) -> vlan 30 members port 1/1/27 tagged 
 
 
- On 6860-B, tag Vlan 1001, VLAN 20 and 30 to the assigned ring ports 1/1/3 and 1/1/27: 
 
sw8 (6860-B) -> vlan 1001 members port 1/1/3 tagged 
sw8 (6860-B) -> vlan 1001 members port 1/1/27 tagged 
sw8 (6860-B) -> vlan 20 members port 1/1/3 tagged 
sw8 (6860-B) -> vlan 20 members port 1/1/27 tagged 
sw8 (6860-B) -> vlan 30 members port 1/1/3 tagged 
sw8 (6860-B) -> vlan 30 members port 1/1/27 tagged 
 
- On 6360-A, tag Vlan 1001, tag VLAN 20 and 30 to the assigned ring ports 1/1/3 and 1/1/27: 
 
sw5 (6360-A) -> vlan 1001 members port 1/1/3 tagged 
sw5 (6360-A) -> vlan 1001 members port 1/1/27 tagged 
sw5 (6360-A) -> vlan 20 members port 1/1/3 tagged 
sw5 (6360-A) -> vlan 20 members port 1/1/27 tagged 
sw5 (6360-A) -> vlan 30 members port 1/1/3 tagged 
sw5 (6360-A) -> vlan 30 members port 1/1/27 tagged 
 
- On 6360-B , tag Vlan 1001, VLAN 20 and 30 to the assigned ring ports 1/1/3 and 1/1/27: 
 
sw6 (6360-B) -> vlan 1001 members port 1/1/3 tagged 
sw6 (6360-B) -> vlan 1001 members port 1/1/27 tagged 
sw6 (6360-B) -> vlan 20 members port 1/1/3 tagged 
sw6 (6360-B) -> vlan 20 members port 1/1/27 tagged 
sw6 (6360-B) -> vlan 30 members port 1/1/3 tagged 
sw6 (6360-B) -> vlan 30 members port 1/1/27 tagged

<<<PAGE 55>>>
5 
Ethernet Ring Protection 
 
2.3. 
Configure the ERP on all switches.  
The RPL owner will be switch 6 in this ring. 
 
 
Notes 
One of the nodes in the ERP ring must be configured as RPL, and this node is responsible for blocking and 
unblocking the ring on link failure. The RPL port can be a physical or logical port, but only one of the ring ports 
can be configured as RPL port. The RPL node can be configured only on a preexisting disabled ring. 
The non-existence of a RPL node or the existence of multiple RPL nodes is considered as incorrect 
configuration. 
When a ring port is configured as RPL port, the node to which the port belongs becomes the RPL owner. 
 
- On 6870-A, configure the ERP as follows: 
 
sw7 (6870-A) -> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1001 level 2 
sw7 (6870-A) -> erp-ring 1 enable 
 
- On 6360-A, configure the ERP as follows: 
 
sw5 (6360-A) -> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1001 level 2 
sw5 (6360-A) -> erp-ring 1 enable 
 
- On 6360-B, configure the ERP as follows: 
 
sw6 (6360-B) -> erp-ring 1 port1 1/1/27 port2 1/1/3 service-vlan 1001 level 2 
sw6 (6360-B) -> erp-ring 1 rpl-node port 1/1/27 
sw6 (6360-B) -> erp-ring 1 wait-to-restore-timer 1 
sw6 (6360-B) -> erp-ring 1 enable 
 
- On 6860-B, configure the ERP as follows: 
 
sw8 (6860-B) -> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1001 level 2 
sw8 (6860-B) -> erp-ring 1 enable 
 
 
Notes 
- 
For ERP Ring 1, the RPL owner is switch 6360-B. Each ring must have its own RPL 
- 
Mandatory parameters for ring creation are a unique ring ID, two physical or logical ports, Service 
VLAN and MEG level. 
- 
The maximum number of rings per node that can be created depends on switch model (refer to the 
latest AOS Network Configuration guide) 
- 
A maximum number of 16 nodes per ring is recommended. 
- 
Physical switch ports and logical link aggregate ports can be configured as ERP ring ports. 
2.4. 
Make the physical connections according to the lab diagram 
 
- On 6870-A, activate interfaces: 
 
sw7 (6870-A) -> interfaces 1/1/3 admin-state enable 
sw7 (6870-A) -> interfaces 1/1/27 admin-state enable 
sw7 (6870-A) -> write memory 
 
- On 6860-B, activate interfaces: 
 
sw8 (6860-B) -> interfaces 1/1/3 admin-state enable 
sw8 (6860-B) -> interfaces 1/1/27 admin-state enable 
sw8 (6860-B) -> write memory 
 
- On 6360-A, activate interfaces: 
 
sw5 (6360-A) -> interfaces 1/1/3 admin-state enable 
sw5 (6360-A) -> interfaces 1/1/27 admin-state enable 
sw5 (6360-A) -> write memory 
 
- On 6360-B, activate interfaces:

<<<PAGE 56>>>
6 
Ethernet Ring Protection 
 
sw6 (6360-B) -> interfaces 1/1/3 admin-state enable 
sw6 (6360-B) -> interfaces 1/1/27 admin-state enable 
sw6 (6360-B) -> write memory 
2.5. 
Check the ERP Ring 1 setup by performing some show commands.  
- On all nodes, check the ERP setup: 
 
-> show erp 
-> show erp {<chassis/slot/portSubport> <chassis/slot/port> > |linkagg <aggId>}  
-> show erp statistics 
-> show erp statistics ring <ringId>  
-> show erp statistics ring <ringId> {<chassis/slot/portSubport> <chassis/slot/port> > |linkagg <aggId>} 
-> clear erp statistics  
-> clear erp statistics ring <ringId>  
-> clear erp statistics ring <ringId> {<chassis/slot/portSubport> <chassis/slot/port> > |linkagg <ag 
 
 
- Example:  
 
sw7 (6870-A) -> show erp 
Legends: WTR - Wait To Restore 
         MEG - Maintenance Entity Group 
 
  Ring      Ring    Ring       Ring    Serv  WTR  Guard   MEG     Ring      Ring     Ring     Remote 
   ID       Port1   Port2     Status   VLAN Timer Timer   Level    State     Node     Profile  System ID 
                                             (min) (csec)                        
----------+--------+--------+---------+-----+-----+------+-----+-----------+--------+--------+------------
--- 
         1    1/1/3   1/1/27   enabled  1001     5    50     2        idle  non-rpl      N/A             
N/A 
 
Total number of rings configured = 1 
 
sw6 (6360-B) -> sh erp 
Legends: WTR - Wait To Restore 
         MEG - Maintenance Entity Group 
 
  Ring      Ring    Ring       Ring    Serv  WTR  Guard   MEG     Ring      Ring     Ring     Remote 
   ID       Port1   Port2     Status   VLAN Timer Timer   Level    State     Node     Profile  System ID 
                                             (min) (csec)                        
----------+--------+--------+---------+-----+-----+------+-----+-----------+--------+--------+------------
--- 
         1   1/1/27    1/1/3   enabled  1001     1    50     2        idle      rpl      N/A             
N/A 
 
Total number of rings configured = 1 
 
 
 
Notes 
ERP Ring States:  
- 
idle: the RPL port is blocking, indicating that the topology is stable. the node is performing normally.  
- 
Protection: on link failure, NI down, or node down of erp nodes. The RPL node is now forwarding and 
the ring is said to be protected. 
- 
Pending:  The node is recovering from failure. When a node is in pending state, the WTR timer will be 
running. All nodes are in pending state till WTR timer expiry.

<<<PAGE 57>>>
7 
Ethernet Ring Protection 
 
 3 
Lab Check 
3.1. 
Connect clients to switches    
 
- Client 7: 
 
Assign IP address 192.168.20.107/24 
 
- On 6870-A: 
 
sw7 (6870-A) -> vlan 20 members port 1/1/1 untagged 
sw7 (6870-A) -> interfaces 1/1/1 admin-state enable 
sw7 (6870-A) -> write memory 
 
- Client 6: 
 
Assign IP address 192.168.20.106/24 
- Ping each other to test connection between them. 
 
- On 6360-B: 
 
sw6 (6360-B) -> vlan 20 members port 1/1/1 untagged 
sw6 (6360-B) -> interfaces 1/1/1 admin-state enable 
sw6 (6360-B) -> write memory 
- Client 8: 
 
Assign IP address 192.168.30.108/24 
 
- On 6860-B: 
 
sw8 (6860-B) -> vlan 30 members port 1/1/1 untagged 
sw8 (6860-B) -> interfaces 1/1/1 admin-state enable 
sw8 (6860-B) -> write memory 
 
- Client 9: 
 
Assign IP address 192.168.30.105/24 
 
- On 6360-A: 
 
sw5 (6360-A) -> vlan 30 members port 1/1/2 untagged 
sw5 (6360-A) -> interfaces 1/1/2 admin-state enable 
sw5 (6360-A) -> write memory 
- Ping each other to test connection between them.

<<<PAGE 58>>>
8 
Ethernet Ring Protection 
 
3.2. 
Test the feature 
 
- Launch a continuous ping running between client 7 and 6. 
 
- Then disconnect (disable) a link in ERP Ring 1. 
 
Sw7 (6870-A) -> interfaces 1/1/3 admin-state disable 
 
- Check the status of the ERP ring. 
What happens?  
  
  
  
 
- Re-connect (enable) the link in ERP Ring 1. Check status of ERP ring. What happens? 
 
Sw7 (6870-A) -> interfaces 1/1/3 admin-state enable 
 
  
  
 4 
ERP Sub ring 2 configuration

<<<PAGE 59>>>
9 
Ethernet Ring Protection 
 
- Create the ERP-Service VLAN  for Ring 2 
 
sw3 (6560-A) -> vlan 1002 
sw3 (6560-A) -> vlan 1002 members port 1/1/5-6 tagged 
sw3 (6560-A) -> interface 1/1/5-6 admin-state enable 
 
sw5 (6360-A) -> vlan 1002 
sw5 (6360-A) -> vlan 1002 members port 1/1/5 tagged 
sw5 (6360-A) -> interface 1/1/5 admin-state enable 
 
sw6 (6360-B) -> vlan 1002 
sw6 (6360-B) -> vlan 1002 members port 1/1/6 tagged 
sw6 (6360-B) -> interface 1/1/6 admin-state enable 
 
 
sw3 (6560-A) -> erp-ring 2 port1 1/1/5 port2 1/1/6 service-vlan 1002 level 2 
sw3 (6560-A) -> erp-ring 2 enable 
 
sw5 (6360-A) -> erp-ring 2 sub-ring-port 1/1/5 service-vlan 1002 level 2 
sw5 (6360-A) -> erp-ring 2 rpl-node port 1/1/5 
sw5 (6360-A) -> erp-ring 2 wait-to-restore-timer 1 
sw5 (6360-A) -> erp-ring 2 enable 
 
sw6 (6360-B) -> erp-ring 2 sub-ring-port 1/1/6 service-vlan 1002 level 2 
sw6 (6360-B) -> erp-ring 2 enable 
  
sw5 (6360-A) -> vlan 40 
sw5 (6360-A) -> vlan 40 members port 1/1/5 tagged 
sw5 (6360-A) -> vlan 40 members port 1/1/3 tagged 
sw5 (6360-A) -> vlan 40 members port 1/1/27 tagged 
sw5 (6360-A) -> write memory 
 
sw6 (6360-B) -> vlan 40 
sw6 (6360-B) -> vlan 40 members port 1/1/6 tagged 
sw6 (6360-B) -> vlan 40 members port 1/1/3 tagged 
sw6 (6360-B) -> vlan 40 members port 1/1/27 tagged 
sw6 (6360-B) -> write memory 
 
sw3 (6560-A) -> vlan 40 
sw3 (6560-A) -> vlan 40 members port 1/1/5 tagged 
sw3 (6560-A) -> vlan 40 members port 1/1/6 tagged 
sw3 (6560-A) -> write memory 
 
Sw7 (6870-A) -> vlan 40 
Sw7 (6870-A) -> vlan 40 members port 1/1/3 tagged 
Sw7 (6870-A) -> vlan 40 members port 1/1/27 tagged 
Sw7 (6870-A) -> write memory 
 
sw8 (6860-B) -> vlan 40 
sw8 (6860-B) -> vlan 40 members port 1/1/3 tagged 
sw8 (6860-B) -> vlan 40 members port 1/1/27 tagged 
sw8 (6860-B) -> write memory

<<<PAGE 60>>>
10 
Ethernet Ring Protection 
 
 
 
sw3 (6560-A) -> sh erp 
Legends: WTR - Wait To Restore 
         MEG - Maintenance Entity Group 
 
  Ring      Ring    Ring       Ring    Serv  WTR  Guard   MEG     Ring      Ring     Ring     Remote 
   ID       Port1   Port2     Status   VLAN Timer Timer   Level    State     Node     Profile  System ID 
                                             (min) (csec)                        
----------+--------+--------+---------+-----+-----+------+-----+-----------+--------+--------+------------
--- 
         2    1/1/5    1/1/6   enabled  1002     5    50     2        idle  non-rpl      N/A             
N/A 
 
Total number of rings configured = 1 
 
sw5 (6360-A) -> sh erp 
Legends: WTR - Wait To Restore 
         MEG - Maintenance Entity Group 
 
  Ring      Ring    Ring       Ring    Serv  WTR  Guard   MEG     Ring      Ring     Ring     Remote 
   ID       Port1   Port2     Status   VLAN Timer Timer   Level    State     Node     Profile  System ID 
                                             (min) (csec)                        
----------+--------+--------+---------+-----+-----+------+-----+-----------+--------+--------+------------
--- 
         1    1/1/3   1/1/27   enabled  1001     5    50     2        idle  non-rpl      N/A             
N/A 
         2    1/1/5       -    enabled  1002     1    50     2        idle      rpl      N/A             
N/A 
 
Total number of rings configured = 2 
 
 
sw6 (6360-B) -> sh erp 
Legends: WTR - Wait To Restore 
         MEG - Maintenance Entity Group 
 
  Ring      Ring    Ring       Ring    Serv  WTR  Guard   MEG     Ring      Ring     Ring     Remote 
   ID       Port1   Port2     Status   VLAN Timer Timer   Level    State     Node     Profile  System ID 
                                             (min) (csec)                        
----------+--------+--------+---------+-----+-----+------+-----+-----------+--------+--------+------------
--- 
         1   1/1/27    1/1/3   enabled  1001     1    50     2        idle      rpl      N/A             
N/A 
         2    1/1/6       -    enabled  1002     5    50     2        idle  non-rpl      N/A             
N/A 
 
Total number of rings configured = 2 
 
4.1. 
Connect clients to switches    
 
- Client 3: 
 
Assign IP address 192.168.40.103/24 
 
- On 6560-A: 
 
sw3 (6560-A) -> vlan 40 members port 1/1/1 untagged 
sw3 (6560-A) -> interfaces 1/1/1 admin-state enable 
sw3 (6560-A) -> write memory 
 
- Client 5:

<<<PAGE 61>>>
11 
Ethernet Ring Protection 
 
Assign IP address 192.168.40.105/24 
 
- On 6360-A: 
 
sw5 (6360-A) -> vlan 40 members port 1/1/1 untagged 
sw5 (6360-A) -> interfaces 1/1/1 admin-state enable 
sw5 (6360-A) -> write memory 
 
- Ping each other to test connection between them 
4.2. 
Test the feature 
 
- Launch a continuous ping running between client 3 and 5. 
 
- Then disconnect (disable) a link in ERP Ring 2. 
 
Sw3 (6560-A) -> interfaces 1/1/6 admin-state disable 
 
- Check the status of the ERP ring. 
What happens?  
  
  
  
 
- Re-connect (enable) the link in ERP Ring 1. Check status of ERP ring. What happens? 
 
Sw3 (6360-A) -> interfaces 1/1/6 admin-state enable 
 
  
  
 
 5 
Access - Core resiliency 
In order to provide resilient dual path to core, we will provide VRRP redundancy by eliminating the single 
point of failure inherent to the two routers which will be connected to the OSPF network. 
 
 
sw7 (6870-A) -> ip interface int_30 address 192.168.30.7/24 vlan 30 
 
sw7 (6870-A) -> ip interface int_20 address 192.168.20.7/24 vlan 20 
 
sw7 (6870-A) -> ip interface int_40 address 192.168.40.7/24 vlan 40 
 
 
sw8 (6860-B) -> ip interface int_30 address 192.168.30.8/24 vlan 30 
 
sw8 (6860-B) -> ip interface int_20 address 192.168.20.8/24 vlan 20 
 
sw8 (6860-B) -> ip interface int_40 address 192.168.40.8/24 vlan 40

<<<PAGE 62>>>
12 
Ethernet Ring Protection 
 
sw7 (6870-A) -> ip vrrp 1 interface int_20 
sw7 (6870-A) -> ip vrrp 1 interface int_20 address 192.168.20.254 
sw7 (6870-A) -> ip vrrp 1 interface int_20 priority 150 
sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state enable 
 
sw7 (6870-A) -> ip vrrp 2 interface int_30 
sw7 (6870-A) -> ip vrrp 2 interface int_30 address 192.168.30.254 
sw7 (6870-A) -> ip vrrp 2 interface int_30 admin-state enable 
 
sw7 (6870-A) -> ip vrrp 3 interface int_40 
sw7 (6870-A) -> ip vrrp 3 interface int_40 address 192.168.40.254 
sw7 (6870-A) -> ip vrrp 3 interface int_40 admin-state enable 
 
sw8 (6860-B) -> ip vrrp 1 interface int_20 
sw8 (6860-B) -> ip vrrp 1 interface int_20 address 192.168.20.254 
sw8 (6860-B) -> ip vrrp 1 interface int_20 admin-state enable 
 
sw8 (6860-B) -> ip vrrp 2 interface int_30 
sw8 (6860-B) -> ip vrrp 2 interface int_30 address 192.168.30.254 
sw8 (6860-B) -> ip vrrp 2 interface int_30 priority 150 
sw8 (6860-B) -> ip vrrp 2 interface int_30 admin-state enable 
 
sw8 (6860-B) -> ip vrrp 3 interface int_40 
sw8 (6860-B) -> ip vrrp 3 interface int_40 address 192.168.40.254 
sw8 (6860-B) -> ip vrrp 3 interface int_40 priority 150 
sw8 (6860-B) -> ip vrrp 3 interface int_40 admin-state enable 
 
sw7 (6870-A) -> show ip vrrp statistics 
sw8 (6860-B) -> show ip vrrp statistics 
 
 
 
5.1. 
VRRP Verification 
- Let’s check VRRP operation and switchover in case the Master switch fails. 
- The DHCP server has not been configured with these gateway addresses, so to perform this test we need 
to switch back to static addresses by setting the gateway for clients 
- From any client 3, begin a continuous ping on to client 5 or client 10 which do not belong to same vlan. 
- Then, reload the master switch (be care of the switch/vlan to determine the master to be rebooted).  
- Notice the pings are redirected to the backup routing instance and continue to be successful; the 
associated arp entry should remain the same.  
 
 
 
 
 
 
 
 
 6 
Restore 
6.1. 
Restore initial configuration by restarting them from "working directory". 
 
sw7 (6870-A) -> rm -r labERP 
rm: remove 'labERP/pkg/.pkgDB_Commit'? y 
rm: remove 'labERP/pkg/.appDB_Commit'? y 
rm: remove 'labERP/.boot.pkg.md5'? y

<<<PAGE 63>>>
13 
Ethernet Ring Protection 
 
rm: remove 'labERP/boot.md5'? y 
sw7 (6870-A) -> reload from working no rollback-timeout 
 
sw8 (6860-B) -> rm -r labERP 
rm: remove 'labERP/pkg/.pkgDB_Commit'? y 
rm: remove 'labERP/pkg/.appDB_Commit'? y 
rm: remove 'labERP/.boot.pkg.md5'? y 
rm: remove 'labERP/boot.md5'? y 
sw8 (6860-B) -> reload from working no rollback-timeout 
 
sw5 (6360-A) -> rm -r labERP 
rm: remove 'labERP/pkg/.pkgDB_Commit'? y 
rm: remove 'labERP/pkg/.appDB_Commit'? y 
rm: remove 'labERP/.boot.pkg.md5'? y 
rm: remove 'labERP/boot.md5'? y 
sw5 (6360-A) -> reload from working no rollback-timeout 
 
sw6 (6360-B) -> rm -r labERP 
rm: remove 'labERP/pkg/.pkgDB_Commit'? y 
rm: remove 'labERP/pkg/.appDB_Commit'? y 
rm: remove 'labERP/.boot.pkg.md5'? y 
rm: remove 'labERP/boot.md5'? y 
sw6 (6360-B) -> reload from working no rollback-timeout 
 
sw3 (6560-A) -> rm -r labERP 
rm: remove 'labERP/pkg/.pkgDB_Commit'? y 
rm: remove 'labERP/pkg/.appDB_Commit'? y 
rm: remove 'labERP/.boot.pkg.md5'? y 
rm: remove 'labERP/boot.md5'? y 
sw3 (6560-A) -> reload from working no rollback-timeout

<<<PAGE 64>>>
MACSEC
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 65>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand MACsec standard
• List AOS switches which Support MACsec
• Configure and monitor MACsec on
OmniSwitch
- Static Mode
- Dynamic mode
• Know software limitations

<<<PAGE 66>>>
MACSEC - OVERVIEW

<<<PAGE 67>>>
MACSEC OVERVIEW
• Goal
• Prevents DoS/ M-in-M/playback attacks, intrusion, 
wire-tapping, masquerading, etc
• Secure most of the traffic on Ethernet links – LLDP 
frames, LACP frames, DHCP/ARP packets, etc
• Functionalities
• IEEE 802.1AE  standard that provides encryption and 
packet Authentication to IEEE 802.1 frames 
• Point-to-point security on Ethernet links between 
directly connected nodes
(Data integrity and confidentiality)
• MACsec-enabled links are secured by matching 
security keys
• Available Modes
• Static SA Mode – Switch-to-Switch links
• Dynamic SA Mode 
• Switch-to-Switch links
• Switch-to-Host links (Using EAP)
MACsec enable 
Switch A
MACsec enable 
Switch B
MACsecDynamic
Mode Using EAP
Static or Dynamic SA Mode
Host (MACsec)

<<<PAGE 68>>>
MACSEC OVERVIEW
• Packet structure
• MACsec packet Specific EtherType (0x88E5) 
• 8-byte or 16-byte SecTag header containing 
information about the decryption key, a packet 
number and Secure Channel Identifier
• Payload (which may be optionally encrypted)
• Integrity Check Value (ICV) generated by GCM-AES of 
size 16 bytes
• Packets are numbered to avoid replay

<<<PAGE 69>>>
MACSEC OVERVIEW
• How it works
• Each node has at least one transmit, and one 
receive secure channel 
• Each associated with a Secure Channel Identifier 
(SCI)
• Need to Match receive secure channel, with an 
SCI corresponding to the SCI of the transmit
secure channel of the peer
• Within each secure channel,
secure associations (SA) are defined
• The SAs hold the encryption keys (SAK – Secure 
Association Key) identified by their association 
number (AN), along with a packet number (PN).
Key-Chain 1
key1
key2
Key- Chain 2
Key3
Key 4
1/1/25
MACsec enable 
Switch A
MACsec enable 
Switch B
sci-tx key-chain 1 
sci-rx key-chain 2
sci-tx key-chain 2 
sci-rx key-chain 1
1/1/26
SA
SA

<<<PAGE 70>>>
AOS SWITCHES – MACSEC SUPPORT

<<<PAGE 71>>>
MACSEC OVERVIEW
AOS Switches – MACsec Platform Support
OmniSwitch 9900
OS9900-CMM
4X10G (Static mode only)
OS9900-GNI-48/P48
10M/100M/1G ports
OS9900-XNI-48/P48
10G ports (Static mode only)
OS9900-XNI-U48
10G ports (Static mode only)
OS9900-XNI-P48Z16
1G/2.5G/5G/10G (16x) 
1G/10G (32x)
OS99-GNI-U48
1G ports
OS99-XNI-U24
10G ports (Static mode only)
OS99-XNI-P24Z8
1G/2.5G/5G/10G (8x) 
1G/10G (16x)
OS99-XNI-U12Q
10G / 4x10G Uplink (Static mode only)
OS99-XNI-UP24Q2
10G(Fiber)/4x10G Uplink (Static mode only)
10G (Copper) (Static mode only)
OmniSwitch 6900
OS6900-X48C4E
Dynamic mode only on all ports. Supports 256-bit 
key length.
OmniSwitch 6860(E)
OS6860(E)
All models support MACsec on 10G ports.
OS6860E-P24 
1G/10G ports.
OmniSwitch 6860N
Dynamic mode only.
OS6860N-U28
SFP (1-24), SFP+ (25-28) and SFP28 (31-34) ports
OS6860N-P48Z
SFP28 (51-54) ports
OS6860N-P48M
• Expansion modules (Not supported on any 4X10G 
splitter transceivers).
• Multi-rate Gigabit Ports (37-48)
OS6860N-P24Z
SFP28 (27-30) ports
OS6860N-P24M
• Expansion modules (Not supported on any 4X10G 
splitter transceivers)
• Multi-rate Gigabit Ports (1-24)
(MACsec site license required):
MACsec feature requires a site license, this license can be generated free of cost. 
•
Dynamic (128/256-bit) MACsec is supported on the OS6570M, OS6870, and 
OS99-CMM2
All other switches support 128-bit

<<<PAGE 72>>>
MACSEC OVERVIEW
AOS Switches - MACsec Platform Support
OmniSwitch 6560
OS6560-P24X4/24X4
Ports 1-24 (Static and Dynamic modes)
OS6560-P48X4/48X4
Ports 1-48 (Static and Dynamic modes)
Ports 49-52 (Dynamic mode only)
OS6560-P48Z16 
(904044-90 only)
Ports 1-32 (Static and Dynamic Modes)
Ports 33-48 (Static and Dynamic modes)
Ports 49-52 (Dynamic mode only)
OS6560-X10
Ports 1-8 (10G ports only. Dynamic mode only)
OmniSwitch 6465
OS6465-P28
Supported on all ports except ports 27 and 28.
OS6465T-12 and 
OS6465T-P12
Not supported on ports 11 and 12.
All other models
Support MACsec on all ports.
Note: 128-bit platforms (e.g. 6465 or 6860E) in the access-layer can work 
with the 6900-X48E supporting both 128 and 256-bit in the distribution/core.
OmniSwitch 6870
Advanced models
OS6870-24 / OS6870-48
OS6870-P24Z / OS6870-P48Z
All user and uplink ports support 256bit MACsec
MACsec not supported on OS6870-24 VFL stacking 
port 25/26 & OS6870-48 VFL stacking port 49/50
Premium models
OS6870-P48M /OS6870-P24M
OS6870-V12
All ports support 256bit MACsec

<<<PAGE 73>>>
MACSEC OVERVIEW
• MACsec Licensing Requirement
• MACsec feature requires a site license, this license can be generated free of cost
• There is no reboot required after applying the license.
How to generate a license or retrieve a license?

<<<PAGE 74>>>
MACSEC – CONFIGURATION

<<<PAGE 75>>>
MACSEC CONFIGURATION
MACsec Mode Static SAK – Management step
Switch A
Switch B
Static SA Mode
Up to 4 manually configured SA 
keys are used to secure traffic 
on the point-to-point link 
between two nodes
Get or generate Random Keys
Create security keys
(both switches)
Create key-chain
(both switches)
Associate security key to key-chain
(both switches)
Configure sci-tx/sci-rx for a port with 
key-chain Enabling option “encryption” 
if any and enable MACsec for the port (both 
switches)
* MACsec - Static mode is not supported on OS6860N.

<<<PAGE 76>>>
MACSEC CONFIGURATION
• MACsec Mode Dynamic (Using PSK)
• Secure-Channel (SCI-TX/SCI-RX) and 
Secure-Association-Key (SAK) are exchanged 
between
MACsec connected links dynamically using MKA
(MACsec Key Agreement Protocol)
• The MKA (IEEE 802.1X-2010) provides the required 
session keys and manages the required encryption 
keys
used by  the underlying MACsec protocol 
• The MKA protocol selects one of the nodes as 
the key server, which creates a dynamic SAK and
shares it with the node at the other end over 
the secure channel
• Once the other end also creates this dynamic 
SA key, subsequent traffic is secured using 
the new SA.
• Two Keys are used to secure the point-to-point 
Ethernet link
• A connectivity association key (CAK) that secures 
control plane traffic
• A randomly-generated secure association key (SAK) 
that secures data plane traffic
Switch A
Switch B

<<<PAGE 77>>>
MACSEC CONFIGURATION
• MKA Protocol Key Exchange based on time or 
data amount 
• MACsec supports protocol key-rotation based on:
• Session time (in min) for SAK regeneration
(5 minutes – 120 minutes)
• Exchange data (received or transmitted)
between the MACsec endpoints. (5GB –1000GB)
• Both values can be configurable in the same 
command, and whichever happens first will trigger 
the key exchange. 
Switch A
Switch B
-> interfaces 1/1/27 MACsec key-rotation max-session-time
-> interfaces 1/1/27 MACsec key-rotation max-exchange-data
-> show interfaces MACsec dynamic key-rotation

<<<PAGE 78>>>
MACSEC CONFIGURATION
MACsec Mode Dynamic (Using PSK) - Management steps
• A matching pre-shared key is configured on both switches which triggers MKA protocol to 
negotiate the cipher suite and generate necessary key (SAK) for authentication and 
encryption
Get Random Keys pre-shared key
Create security keys
Create key-chain
Associate security key to key-chain
Configure dynamic mode /port with
key-chain Enabling option “encryption”
if any and enable MACsec for the port

<<<PAGE 79>>>
MACSEC CONFIGURATION
• MACsec Mode Dynamic (Using EAP) – how it works 
• IEEE 802.1X authenticates the endpoint and transmits the necessary cryptographic keying material 
to both sides
• Endpoint undergoes authentication and the he switch relays the RADIUS server response and sniffs 
the Master key to program it on the connected port.
CAK:
The CAK is delivered in the RADIUS vendor-
specific attributes (VSAs) MS-MPPE-Send-Key and
MS-MPPE-Recv-Key.
The host must support MACsec and must run a software 
that allows to enable MACsec-secured connection with 
Switch.

<<<PAGE 80>>>
MACSEC CONFIGURATION
• MACsec Mode Dynamic (Using EAP) - Management steps
If Successful Radius 
Auth  returns UNP-
Profile “employee“ 
which ap the vlan
Enable MACsec for the port to use EAP
Enabled UNP on the port
Create necessary UNP Profile
for learning supplicant
Configure Radius Server used
for 802.1x-authentication

<<<PAGE 81>>>
MONITORING COMMANDS
Show command 
show interfaces capability
show configuration snapshot MACsec
show interfaces MACsec [<chassis>/<slot>/<port1>[-<port2>]]
show interfaces MACsec static [<chassis>/<slot>/<port>[-<port2>]]
show interfaces MACsec dynamic [<chassis>/<slot>/<port>[-<port2>]]
show interfaces MACsec dynamic details [<chassis>/<slot>/<port>[-<port2>]]
show interfaces MACsec statistics [ <chassis>/<slot>/<port>]

<<<PAGE 82>>>
MACSEC SECURITY ADMIN
User Account - How It Works
• MACsec feature is now part of the security domain when creating a new user account to 
configure the switch
• This allows the user to issue a MACsec security command compared to basic admin
user securityadmin password Switch@123 read-write MACsec OR
user securityadmin password Switch@123 read-write domain-security

<<<PAGE 83>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 84>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
MACsec 
How to 
✓ This lab is designed to familiarize you with the MACsec feature 
Contents 
1 
Overview ....................................................................................... 3 
2 
Topology ........................................................................................ 3 
3 
Prerequisite .................................................................................... 4 
3.1. Initialize both switches ............................................................................ 4 
3.2. Check available port for MACsec capability .................................................... 4 
3.3. Check available license MACsec capability on 6870-A......................................... 4 
3.4. Check available license MACsec capability on 6860-B ......................................... 4 
3.5. Implement a link between switches ............................................................. 5 
4 
Dynamic SA Mode – Switch-to-Switch links ................................................ 6 
4.1. Configure keychain 1 with pre-shared Master key ............................................. 6 
4.2. Configure keys and keychain and associate them in both switches ......................... 6 
4.3. Monitor Macsec implementation ................................................................. 7 
5 
Appendix ....................................................................................... 8 
5.1. Apply a licence Macsec on switch ................................................................ 8 
5.2. Static SA Mode – Switch-to-Switch links ......................................................... 9 
5.2.1. Configure the keys and keychains ........................................................................ 9 
5.2.2. Configure keys and keychain and associate them in both switches ................................. 9 
5.2.3. Configure sci-tx/sci-rx for a port......................................................................... 9 
5.2.4. Monitor Macsec implementation ....................................................................... 10 
5.2.5. Remove MACsec configuration .......................................................................... 11 
5.3. MACsec Mode Dynamic (Using EAP) - Management steps .................................... 11

<<<PAGE 85>>>
2 
MACsec

<<<PAGE 86>>>
3 
MACsec 
 
Implementation 
 1 
Overview 
MACSec provides point-to-point security on Ethernet links between directly connected nodes. 
- 
IEEE standard (802.1AE-2006) for encryption over Ethernet. Encrypt and authenticate all traffic in a LAN 
with GCM-AES-128. 
Using MACSec prevents DoS attacks, intrusion, wiretapping, masquerading, etc. MACSec can be used to secure 
most of the traffic on Ethernet links – LLDP frames, LACP frames, DHCP/ARP packets, etc 
MACSec-enabled links are secured by matching security keys. Data integrity checks are done. Optionally, traffic 
can also be encrypted, if enabled by user configuration 
Three modes are In AOS OmniSwitch: 
- 
Static SA Mode – Switch-to-Switch links 
- 
Dynamic SA Mode – Switch-to-Switch links 
- 
Dynamic SA Mode – Host-to-Switch links 
We are going to cover the second mode in this lab.  
- 
Only dynamic mode is available on 6860N. 
- 
Host-to-Switch links is not covered as Native Window supplicant doesn’t seem to support MACSec. 
- 
Nevertheless, two examples of configuration step are given at the end of the lab in appendix. 
 2 
Topology 
 
 
 
 
Notes 
We are going to Create a "User-defined directories" call “labmacsec” and boot both switches on it for this lab. 
At the end of the lab, we are going to restart to working directory to retrieve initial configuration.

<<<PAGE 87>>>
4 
MACsec 
 
 3 
Prerequisite  
3.1. 
Initialize both switches 
- 
Create a User-defined directories “labmacsec” , copy the contents of the labinit directory to it ,and 
boot the switches from the new user-defined directory (labmacsec): 
 
sw7 (6870-A) -> mkdir labmacsec 
sw7 (6870-A) -> cp labinit/*.* labmacsec 
sw7 (6870-A) -> ls labmacsec 
sw7 (6870-A) -> reload from labmacsec no rollback-timeout 
                Confirm Activate (Y/N): y 
sw7 (6870-A) -> show running-directory 
 
sw8 (6860-B) -> mkdir labmacsec 
sw8 (6860-B) -> cp labinit/*.* labmacsec 
sw8 (6860-B) -> ls labmacsec 
sw8 (6860-B) ->reload from labmacsec no rollback-timeout 
               Confirm Activate (Y/N): y 
sw8 (6860-B) ->show running-directory 
3.2. 
Check available port for MACsec capability 
sw7 (6870-A) -> show interfaces 1/1/27 capability 
                                                                                    Macsec      Macsec     Macsec 
 Ch/Slot/Port   AutoNeg       Pause       Crossover        Speed         Duplex     Supported   256-bit    XPN 
--------------+--------+----------------+-----------+------------------+----------+-----------+----------+--------- 
 1/1/27A  CAP       EN   Tx/Rx/Tx&Rx/DIS           -         1G/10G/25G       Full   YES         YES       YES 
 1/1/27A  DEF      DIS               DIS           -                10G       Full    -           -         - 
 
sw8 (6860-B) -> sh interfaces 1/1/27 capability 
                                                                                     Macsec    Macsec    Macsec 
 Ch/Slot/Port   AutoNeg       Pause       Crossover        Speed         Duplex     Supported   256-bit    XPN 
--------------+--------+----------------+-----------+------------------+----------+-----------+----------+--------- 
 1/1/27   CAP       EN   Tx/Rx/Tx&Rx/DIS           -         1G/10G/25G       Full   YES         YES        NO 
 1/1/27   DEF      DIS               DIS           -                10G       Full    -           -         - 
3.3. 
Check available license MACsec capability on 6870-A 
sw7 (6870-A) -> show license-info 
                                             Time (Days)       Upgrade      Expiration 
VC   device   License            Type        Remaining         Status       Date 
----+------+---------------+---------------+---------------+--------------+---------------- 
1       0    Advanced           PERM           NA             NA             NA 
1       0    MACSEC             PERM           NA             NA             NA 
3.4. 
Check available license MACsec capability on 6860-B 
sw8 (6860-B) -> show license-info 
                                             Time (Days)       Upgrade      Expiration 
VC   device   License            Type        Remaining         Status       Date 
----+------+---------------+---------------+---------------+--------------+---------------- 
1       0    Advanced           PERM           NA             NA             NA 
1       0    MACSEC             PERM           NA             NA             NA 
 
 
Notes 
If the licence MACsec is not available on the switch, refer to the appendix section to install it.

<<<PAGE 88>>>
5 
MACsec 
 
3.5. 
Implement a link between switches 
- 
Log in to switches and activate the interface 
 
sw7 (6870-A) -> interface 1/1/27 admin-state enable 
 
sw8 (6860-B) -> interface 1/1/27 admin-state enable 
 
- 
To begin, let’s create a new VLAN and assign an IP address to that VLAN as done previously 
 
sw7 (6870-A) -> vlan 90 
sw7 (6870-A) -> ip interface int_90 address 192.168.90.7/24 vlan 90 
 
sw8 (6860-B) -> vlan 90 
sw8 (6860-B) -> ip interface int_90 address 192.168.90.8/24 vlan 90 
 
- 
Assign port to VLAN 90 
 
sw7 (6870-A) -> vlan 90 members port 1/1/27 untagged 
sw7 (6870-A) -> show vlan 90 members 
 
sw8 (6860-B) -> vlan 90 members port 1/1/27 untagged 
sw8 (6860-B) -> show vlan 90 members 
- 
Test connectivity between the two switches. 
 
sw8 (6860-B) -> ping 192.168.90.7 
 
PING 192.168.90.7 (192.168.90.7) 56(84) bytes of data. 
64 bytes from 192.168.90.7: icmp_seq=1 ttl=64 time=12.3 ms 
64 bytes from 192.168.90.7: icmp_seq=2 ttl=64 time=0.609 ms 
64 bytes from 192.168.90.7: icmp_seq=3 ttl=64 time=0.682 ms 
64 bytes from 192.168.90.7: icmp_seq=4 ttl=64 time=0.627 ms 
64 bytes from 192.168.90.7: icmp_seq=5 ttl=64 time=0.643 ms

<<<PAGE 89>>>
6 
MACsec 
 
 4 
Dynamic SA Mode – Switch-to-Switch links  
4.1. 
Configure keychain 1 with pre-shared Master key 
- 
Pre-shared Master key have been already generated by the administrator. the step to generate them on 
a switch can be skipped. 
- 
Pre-shared Master key provided by the administrator are: 
 
hex-key 0x000102030405060708090a0b0c0d0e0f 
keyed-name 0x000102030405060708090a0b0c0d0eff 
4.2. 
Configure keys and keychain and associate them in both switches 
- 
Configure keys 
 
sw7 (6870-A) -> security key 1 algorithm aes-cmac-128 hex-key 0x000102030405060708090a0b0c0d0e0f keyed-
name 0x000102030405060708090a0b0c0d0eff 
 
sw8 (6860-B) -> security key 1 algorithm aes-cmac-128 hex-key 0x000102030405060708090a0b0c0d0e0f keyed-
name 0x000102030405060708090a0b0c0d0eff 
- 
Create key-chain 
 
sw7 (6870-A) -> security key-chain 1 
 
sw8 (6860-B) -> security key-chain 1 
- 
Associate security key to key-chain 
 
Sw7 (6870-A) -> security key-chain 1 key 1 
 
sw8 (6860-B) -> security key-chain 1 key 1 
- 
Configure dynamic mode on port with the above key-chain with Session time (10 min) and Exchange data 
(received or transmitted) between the MACSEC endpoints to 20G. 
 
sw7 (6870-A) -> interfaces port 1/1/27 macsec mode dynamic key-chain 1 encryption 
sw7 (6870-A) -> interfaces 1/1/27 macsec key-rotation max-session-time 10 
sw7 (6870-A) -> interfaces 1/1/27 macsec key-rotation max-exchange-data 20 
sw7 (6870-A) -> interfaces port 1/1/27 macsec admin-state enable 
 
sw8 (6860-B) -> interfaces port 1/1/27 macsec mode dynamic key-chain 1 encryption 
sw8 (6860-B) -> interfaces 1/1/27 macsec key-rotation max-session-time 10 
sw8 (6860-B) -> interfaces 1/1/27 macsec key-rotation max-exchange-data 20 
sw8 (6860-B) -> interfaces port 1/1/27 macsec admin-state enable 
 
sw7 (6870-A) -> show interfaces macsec dynamic key-rotation 
Chas/Slot/Port   Time to Rekey (Sec)   Data to Rekey (Byte) 
----------------+---------------------+------------------------ 
 1/1/27           556                   19998014

<<<PAGE 90>>>
7 
MACsec 
 
4.3. 
Monitor Macsec implementation 
- 
Show configuration snapshot macsec in both switches 
 
sw7 (6870-A) -> show configuration snapshot macsec 
! MAC Security: 
interfaces port 1/1/27 macsec mode dynamic key-chain 1 encryption key-rotation max-session-time 10 key-
rotation max-exchange-data 20M 
interfaces port 1/1/27 macsec admin-state enable 
 
sw8 (6860-B) -> show configuration snapshot macsec 
! MAC Security: 
interfaces port 1/1/27 macsec mode dynamic key-chain 1 encryption key-rotation max-session-time 10 key-
rotation max-exchange-data 20M 
interfaces port 1/1/27 macsec admin-state enable 
 
- 
Test connectivity between the two switches 
 
sw8 (6860-B) -> ping 192.168.90.7 
 
PING 192.168.90.7 (192.168.90.7) 56(84) bytes of data. 
64 bytes from 192.168.90.7: icmp_seq=1 ttl=64 time=12.3 ms 
64 bytes from 192.168.90.7: icmp_seq=2 ttl=64 time=0.609 ms 
64 bytes from 192.168.90.7: icmp_seq=3 ttl=64 time=0.682 ms 
64 bytes from 192.168.90.7: icmp_seq=4 ttl=64 time=0.627 ms 
64 bytes from 192.168.90.7: icmp_seq=5 ttl=64 time=0.643 ms 
--- 
sw7 (6870-A) -> ping 192.168.90.8 
PING 192.168.90.8 (192.168.90.8) 56(84) bytes of data. 
64 bytes from 192.168.90.8: icmp_seq=1 ttl=64 time=10.7 ms 
64 bytes from 192.168.90.8: icmp_seq=2 ttl=64 time=0.627 ms 
64 bytes from 192.168.90.8: icmp_seq=3 ttl=64 time=1.52 ms 
64 bytes from 192.168.90.8: icmp_seq=4 ttl=64 time=0.633 ms 
64 bytes from 192.168.90.8: icmp_seq=5 ttl=64 time=0.615 ms 
 
- 
Check MACsec interfaces 
 
sw7 (6870-A) -> show interfaces macsec 
 Chas/Slot/Port  Admin-State   Mode       Encryption     Exchange Data         Session Time (Min)      Cipher Suite 
---------------+-------------+----------+--------------+---------------------+-----------------------+----------------- 
 1/1/27A         Enabled       Dynamic    Enabled        20M                   10                      gcm-aes-128 
 
sw8 (6860-B) -> show interfaces macsec 
 Chas/Slot/Port  Admin-State   Mode       Encryption     Exchange Data         Session Time (Min)      Cipher Suite 
---------------+-------------+----------+--------------+---------------------+-----------------------+----------------- 
 1/1/27          Enabled       Dynamic    Enabled        20M                   10                      gcm-aes-128 
 
sw7 (6870-A) -> show interfaces macsec dynamic 
                                                                   Server     Transmit        Key      Operation 
 Chas/Slot/Port   Admin-State   Mode       Keychain   Encryption   Priority   Interval(Sec)   Server   Status 
----------------+-------------+----------+----------+------------+----------+---------------+--------+-------------- 
 1/1/27A          Enabled       keychain    1         Enabled       10          2             YES      UP 
 
sw8 (6860-B) -> show interfaces macsec dynamic 
                                                                   Server     Transmit        Key       
                                                                   Server     Transmit        Key      Operation 
 Chas/Slot/Port   Admin-State   Mode       Keychain   Encryption   Priority   Interval(Sec)   Server   Status 
----------------+-------------+----------+----------+------------+----------+---------------+--------+-------------- 
 1/1/27           Enabled       keychain    1         Enabled       10          2             YES      UP 
 
- 
At the end of this lab, restore both switches to initial configuration by restarting them from "working 
directory". 
 
sw7 (6870-A) -> rm -r labmacsec 
sw7 (6870-A) -> reload from working no rollback-timeout 
                Confirm Activate (Y/N) : y  
 
sw8 (6860-B) -> rm -r labmacsec 
sw8 (6860-B) -> reload from working no rollback-timeout 
          Confirm Activate (Y/N) : y

<<<PAGE 91>>>
8 
MACsec 
 
 
 5 
Appendix 
5.1. 
Apply a licence Macsec on switch 
 
- 
Example given on sw7:  
 
Sw7 (6870-A) -> show license-info 
                                             Time (Days)       Upgrade      Expiration 
VC   device   License            Type        Remaining         Status       Date 
----+------+---------------+---------------+---------------+--------------+---------------- 
1       0    Advanced           PERM           NA             NA             NA 
 
- 
Create the license.dat file and copy the License to it, then apply. 
 
Sw7 (6870-A) -> cat > licence.dat 
1ES2-4{v!-[AQy-hRrK-B$qF-5EGE-}oHt-NJ5K (Then enter and CTRL + D) 
 
Sw7 (6870-A) -> license apply file licence.dat order-id "05200622" 
 
Sw7 (6870-A) -> show license-info 
                                             Time (Days)       Upgrade      Expiration 
VC   device   License            Type        Remaining         Status       Date 
----+------+---------------+---------------+---------------+--------------+---------------- 
1       0    Advanced           PERM           NA             NA             NA 
1       0    MACSEC             PERM           NA             NA             NA 
 
 
- Do the same on the second switch if required 
 
sw8 (6860-B) -> show license-info 
                                             Time (Days)       Upgrade      Expiration 
VC   device   License            Type        Remaining         Status       Date 
----+------+---------------+---------------+---------------+--------------+---------------- 
1       0    Advanced           PERM           NA             NA             NA 
 
sw8 (6860-B) -> cat > licence.dat 
1ES2-4{v!-[AQy-hRrK-B$qF-5EGE-}oHt-NJ5K (Then enter and CTRL + D) 
sw8 (6860-B) -> 
 
sw8 (6860-B) -> license apply file licence.dat order-id "05200622" 
 
sw8 (6860-B) -> show license-info 
                                             Time (Days)       Upgrade      Expiration 
VC   device   License            Type        Remaining         Status       Date 
----+------+---------------+---------------+---------------+--------------+---------------- 
1       0    Advanced           PERM           NA             NA             NA 
1       0    MACSEC             PERM           NA             NA             NA

<<<PAGE 92>>>
9 
MACsec 
 
5.2. 
Static SA Mode – Switch-to-Switch links 
- 
This part is not working on remote lab. This is an example with 6860E connect to 6860 
5.2.1. Configure the keys and keychains 
- 
Random keys have been already generated by the administrator. The step to generate them on a switch 
can be skipped. 
- 
Random keys provided by the administrator are: 
Key 1: f514ab78a8f923225626dd6064d6d67a 
Key 2: 1937463f587115258ea8f0ed62f308e7 
Key 3: 0ad08a30ebdb532d4cb151dc1c0dafd9 
Key 4: b10f0a502c19f0c84acf798322f7efb8 
 
 
Tips 
If you do not have key, use the following command on a switch to generate it. 
 sw7 (6870-A) -> security key-chain gen-random-key 
5.2.2. Configure keys and keychain and associate them in both switches 
o 
Create security keys 
In this example, we used key generated above. If you generate new keys, do not forget to replace it below 
in command line 
 
sw7 (6870-A) -> security key 1 algorithm aes-gcm-128 encrypt-key ef68850d93b82fb494843f66f5864cc5 
 
sw7 (6870-A) -> security key 2 algorithm aes-gcm-128 encrypt-key 0641ef514da5c09feee8bf9a96fb22e1 
 
sw7 (6870-A) -> security key 3 algorithm aes-gcm-128 encrypt-key 58b554b11033d1d865ef35ba707e4767 
 
sw7 (6870-A) -> security key 4 algorithm aes-gcm-128 encrypt-key f167cc24fc78950f265a74edcf5cb344 
 
sw8 (6860-B) -> security key 1 algorithm aes-gcm-128 encrypt-key ef68850d93b82fb494843f66f5864cc5 
 
sw8 (6860-B) -> security key 2 algorithm aes-gcm-128 encrypt-key 0641ef514da5c09feee8bf9a96fb22e1 
 
sw8 (6860-B) -> security key 3 algorithm aes-gcm-128 encrypt-key 58b554b11033d1d865ef35ba707e4767 
 
sw8 (6860-B) -> security key 4 algorithm aes-gcm-128 encrypt-key f167cc24fc78950f265a74edcf5cb344 
 
 
Tips 
Up to 4 manually configured SA keys are used to secure traffic on the point-to-point link between two nodes) 
 
o 
Create key-chain 
 
sw7 (6870-A) -> security key-chain 1 
sw7 (6870-A) -> security key-chain 2 
 
sw8 (6860-B) -> security key-chain 1 
sw8 (6860-B) -> security key-chain 2 
- 
Associate security key to key-chain 
 
sw7 (6870-A) -> security key-chain 1 key 1-2 
sw7 (6870-A) -> security key-chain 2 key 3-4 
 
sw8 (6860-B) -> security key-chain 1 key 1-2 
sw8 (6860-B) -> security key-chain 2 key 3-4 
5.2.3. 
Configure sci-tx/sci-rx for a port 
- 
Configure sci-tx/sci-rx for a port with the above key-chain. Enabling option “encryption” if any and 
enable MACSEC for the port 
 
sw7 (6870-A)-> interface 1/1/25 macsec admin-state enable sci-tx key-chain 1 encryption sci-rx key-chain 2 encryption

<<<PAGE 93>>>
10 
MACsec 
 
sw8 (6860-B)-> interface 1/1/25 macsec admin-state enable sci-tx key-chain 2 encryption sci-rx key-chain 1 encryption 
5.2.4. 
Monitor Macsec implementation 
- 
Show configuration snapshot macsec in both switches 
 
sw7 (6870-A) -> show configuration snapshot macsec 
! MAC Security: 
interfaces port 1/1/25 macsec mode static 
interfaces port 1/1/25 macsec sci-tx key-chain 1 encryption 
interfaces port 1/1/25 macsec sci-rx key-chain 2 encryption 
interfaces port 1/1/25 macsec admin-state enable 
 
sw8 (6860-B) -> show configuration snapshot macsec 
! MAC Security: 
interfaces port 1/1/25 macsec mode static 
interfaces port 1/1/25 macsec sci-tx key-chain 2 encryption 
interfaces port 1/1/25 macsec sci-rx key-chain 1 encryption 
interfaces port 1/1/25 macsec admin-state enable 
 
- 
Test connectivity between the two switches 
 
sw8 (6860-B) -> ping 192.168.90.7 
PING 192.168.90.7 (192.168.90.7) 56(84) bytes of data. 
64 bytes from 192.168.90.7: icmp_seq=1 ttl=64 time=12.3 ms 
64 bytes from 192.168.90.7: icmp_seq=2 ttl=64 time=0.609 ms 
64 bytes from 192.168.90.7: icmp_seq=3 ttl=64 time=0.682 ms 
64 bytes from 192.168.90.7: icmp_seq=4 ttl=64 time=0.627 ms 
64 bytes from 192.168.90.7: icmp_seq=5 ttl=64 time=0.643 ms 
 
sw7 (6870-A) -> ping 192.168.90.8 
PING 192.168.90.8 (192.168.90.8) 56(84) bytes of data. 
64 bytes from 192.168.90.8: icmp_seq=1 ttl=64 time=10.7 ms 
64 bytes from 192.168.90.8: icmp_seq=2 ttl=64 time=0.627 ms 
64 bytes from 192.168.90.8: icmp_seq=3 ttl=64 time=1.52 ms 
64 bytes from 192.168.90.8: icmp_seq=4 ttl=64 time=0.633 ms 
64 bytes from 192.168.90.8: icmp_seq=5 ttl=64 time=0.615 ms 
 
- 
Check MACsec interfaces 
 
sw7 (6870-A) -> show interfaces macsec 
 Chas/Slot/Port  Admin-State     Mode          Encryption 
---------------+-------------+------------+----------------- 
     1/1/25       Enabled       Static          Enabled 
 
sw8 (6860-B) ->  show interfaces macsec 
 Chas/Slot/Port  Admin-State     Mode          Encryption 
---------------+-------------+------------+----------------- 
     1/1/25       Enabled       Static          Enabled 
 
sw7 (6870-A) -> show interfaces macsec static 
 Chas/Slot/Port  Admin-State           SCI          Type   Keychain     Encryption 
---------------+-------------+--------------------+------+-----------+-------------- 
     1/1/25       Enabled              -             TX        1          Enabled 
     1/1/25       Enabled              -             RX        2          Enabled 
 
sw8 (6860-B) -> show interfaces macsec static 
 Chas/Slot/Port  Admin-State           SCI          Type   Keychain     Encryption 
---------------+-------------+--------------------+------+-----------+-------------- 
     1/1/25       Enabled              -             TX        2          Enabled 
     1/1/25       Enabled              -             RX        1          Enable

<<<PAGE 94>>>
11 
MACsec 
 
5.2.5. Remove MACsec configuration 
sw7 (6870-A) -> interface port 1/1/25 macsec admin-state disable 
sw7 (6870-A) -> no interfaces port 1/1/25 macsec 
sw7 (6870-A) -> no security key-chain 1 
sw7 (6870-A) -> no security key-chain 2 
sw7 (6870-A) -> show configuration snapshot macsec 
sw7 (6870-A) -> write memory 
 
sw8 (6860-B) -> interface port 1/1/25 macsec admin-state disable 
sw8 (6860-B) -> no interfaces port 1/1/25 macsec 
sw8 (6860-B) -> no security key-chain 1 
sw8 (6860-B) -> no security key-chain 2 
sw8 (6860-B) -> show configuration snapshot macsec 
sw8 (6860-B) -> write memory 
 
 
Tips 
//Example for “no” format: 
// Un-configure  macsec sci-tx params 
-> no interface 1/1/25 macsec sci-tx key-chain 
-> no interface 1/1/25 macsec sci-tx encryption 
-> no interface 1/1/25 macsec sci-tx  
 
// Un-configure  macsec sci-rx params 
-> no interface 1/1/25 macsec sci-rx 0x2 key-chain 
-> no interface 1/1/25 macsec sci-tx 0x2 encryption 
-> no interface 1/1/25 sci-tx 0x02 
 
5.3. 
MACsec Mode Dynamic (Using EAP) - Management steps 
- 
This part is not working on remote lab as MACsec are not available on Window XP/7 client host. This is a 
n example of management step. 
 
- 
Enable MACSEC for the port to use EAP 
interfaces port 1/1/1 macsec mode dynamic radius 
interfaces port 1/1/1 macsec admin-state enable 
 
- 
Enabled UNP on the port 
unp port 1/1/1 port-type bridge 
unp port 1/1/1 802.1x-authentication

<<<PAGE 95>>>
12 
MACsec 
 
- 
Create necessary UNP Profile for learning supplicant. If Successful Radius Auth returns UNP-Profile 
“employee" which ap the vlan 30  
vlan 30 
unp profile “employee“ 
unp profile “employee” map vlan 30 
 
- 
Configure Radius Server used for 802.1x-authentication  
aaa radius-server radius host 192.168.100.102 key Alcatel 
aaa device-authentication 802.1x radius

<<<PAGE 96>>>
PRIVATE VLAN
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 97>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the Private VLAN implementation
on the OmniSwitches
• Learn the Different VLAN Port types
• Understand how the traffic flows between 
different VLAN’s
• Configure Private VLAN

<<<PAGE 98>>>
PRIVATE VLAN - OVERVIEW
• Physical isolation extension across the network per VLAN basis
Layer 2 
Network 
Isolation
Inter−switch
behaviour
Primary
Secondary  
VLAN
PVLAN
• Partitions single broadcast domain into 
several broadcast sub-domains
• Provides network-wide isolation per 
primary VLAN 
• Primary VLAN can have multiple 
secondary VLANs
• Provides scalable VLAN distribution 
and IP address management
• Common IP address space
• Works over VLANs, services (SPBM) and 
Ethernet-services (QinQ)
Scalability
This type of data isolation improves security and simplifies system configuration

<<<PAGE 99>>>
PRIVATE VLAN - VLAN TYPES
• PVlan divides the broadcast domain into sub-domains
PVLAN
Primary VLAN 
• VLAN referred as Private VLAN
Secondary VLAN
• VLAN associated with the Primary 
VLAN
−Same primary vlan IP space
−Same primary vlan SPT state
• 2 Vlan types
Isolated Vlan
• Cannot communicate with each 
other at L2
Community Vlan
Isolated Vlan
Community Vlan
• Can communicate each other at L2 
but not with other communities

<<<PAGE 100>>>
PRIVATE VLAN - PORT TYPES
PVLAN
Promiscuous ports
• Part of the primary VLAN
• Can communicate to all ports in all Vlans
Community Vlan
Isolated Vlan
Isolated ports
• Part of the isolated VLANs
• Can only communicate to promiscuous ports
Community ports
• Part of the community VLAN
• Can communicate to ports in the same 
community or promiscuous ports
PVLAN ISL Ports
• Extend a PVLAN domain across different 
switches
• Carries both primary and secondary traffic
PVLAN

<<<PAGE 101>>>
PRIVATE VLAN – USE CASE
Switch 3
Private VLAN 100
Switch 2
OV 2500
Promiscuous
port
Phone community
VLAN 103
Switch 1
ISL
All private VLANs tagged 
100,101,102,103
Phone community
VLAN 103
C1  C2
Community
VLAN 103
Community
VLAN 103
C3
I1 I2
Isolated
VLAN 101
IP services and 
internet
Community
VLAN 102
C4 C5
◼Ports C1,C2,C3 are UNP ports whose client is assigned to Community vlan 103
◼ISL ports connecting switches to extend ALL Private Vlans
◼Promiscuous port to whom everyone can communicate bi-directionally
◼Ports C4,C5 are UNP ports whose client is assigned to Community vlan 102

<<<PAGE 102>>>
PRIVATE VLAN – SPECIFICATIONS

<<<PAGE 103>>>
pvlan 100 admin-state enable
pvlan 100 secondary 101 type community
pvlan 100 secondary 103 type isolated
pvlan 100 members port 1/1/20 untagged
pvlan 101 members port 1/1/1 untagged
pvlan 101 members port 1/1/15 untagged
pvlan 103 members port 1/1/16-17 untagged
-> show pvlan mapping
Primary    Secondary
VLAN       VLAN
Type
----------+----------+------------
100        101        Community
100
103        Isolated
sw2> show pvlan members
pvlan
port      type               status       port-type
-------+---------+------------------+------------+------------
pvlan
port      type               status       port-type
-------+---------+------------------+------------+------------
100     1/1/20      default            forwarding   promiscuous
101     1/1/1       default            forwarding   community
101     1/1/15      default            forwarding   community
103     1/1/16      default            forwarding   isolated
103     1/1/17      default            forwarding   isolated
-> show mac-learning
VLAN       100   00:50:56:9e:2f:37     dynamic     bridging    1/1/1
VLAN       100   00:50:56:9e:a4:03     dynamic     bridging   1/1/15
VLAN       100   00:50:56:9e:85:68     dynamic     bridging   1/1/16
VLAN       100   00:50:56:9e:1f:9f     dynamic     bridging   1/1/17
VLAN       100   00:50:56:9e:05:2b     dynamic     bridging   1/1/20
VLAN       100   00:50:56:9e:73:25     dynamic     bridging   1/1/20
PRIVATE VLAN – CONFIGURATION EXAMPLE
PVLAN 100
Community Vlan 101
Isolated Vlan 103
1/1/1
1/1/20
1/1/15
1/1/16
1/1/17

<<<PAGE 104>>>
PRIVATE VLAN
Vlan Traffic
Community Vlan 101
Isolated Vlan 103
Community Vlan 101
Isolated Vlan 103
Primary 
Vlan
Primary Vlan
Traffic not authorized
Traffic authorized

<<<PAGE 105>>>
PRIVATE VLAN – CONFIGURATION
Example
PVLAN 100
Community Vlan 101
Isolated Vlan 103
1/1/1
1/1/20
1/1/15
1/1/16
1/1/17
PVLAN 100
Community Vlan 101
Isolated Vlan 103
1/3/1
1/3/20
1/3/12
1/3/14
1/3/15
Linkagg 1
linkagg lacp agg 1 size 2 admin-state enable
linkagg lacp agg 1 actor admin-key 1
linkagg lacp port 1/4/1 actor admin-key 1
linkagg lacp port 1/4/2 actor admin-key 1
pvlan 100 admin-state enable
pvlan 100 secondary 101 type community
pvlan 100 secondary 103 type isolated
pvlan 100 members port 1/3/20 untagged
pvlan 100 members linkagg 1 isl
pvlan 101 members port 1/3/1 untagged
pvlan 101 members port 1/3/12 untagged
pvlan 103 members port 1/3/14-15 untagged
1/4/1-2
1/2/1-2

<<<PAGE 106>>>
PRIVATE VLAN – UNP PORTS
• Can also be assigned to Secondary VLANs (isolated or community ports) 
PVLAN
Community Vlan
Isolated Vlan
IEEE 802.1x, MAC Auth or
UNP Classification Rules
UNP
IEEE 802.1x, MAC Auth or
UNP Classification Rules
UNP
• The UNP ports are designated as isolated or community ports during    
runtime based on the first MAC address learned on the port.
• If the first MAC address is learned on a UNP port is classified into an 
Isolated VLAN, the port is designated as an isolated port.
• If the first MAC address is learned on a UNP port is classified into a 
Community VLAN, the port is designated as a community port.
• If the first MAC address learned on the a UNP port is classified into  
any standard VLAN (non-PVLAN), then the UNP port cannot be 
designated as an isolated or community port.

<<<PAGE 107>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 108>>>
OmniSwitch AOS R8 
Private VLAN 
How to 
✓ Setup the Private VLAN feature on the OmniSwitch 
Contents 
1 
Objective ....................................................................................... 2 
2 
Private VLAN Overview ....................................................................... 2 
3 
Lab Diagram .................................................................................... 2 
4 
Configuring Link aggregation between 6870-A and 6860 ................................ 3 
5 
Configuring the Private VLAN ................................................................ 3 
5.1. Configuring the Private VLAN ..................................................................... 3 
5.2. Configuring the PC Clients ........................................................................ 4 
6 
Testing the Configuration .................................................................... 4 
6.1. Testing the Community VLAN ..................................................................... 4 
6.2. Testing the Isolated VLAN ......................................................................... 5 
7 
Deleting the Configuration ................................................................... 5

<<<PAGE 109>>>
2 
Private VLAN 
 
Implementation 
 1 
Objective 
This lab is designed to familiarize you with the concept of Private VLAN (PVLAN). This feature provides the 
ability to isolate Layer 2 data between devices that are on the same VLAN. This type of data isolation 
improves security and simplifies system configuration. 
 2 
Private VLAN Overview 
Private VLAN divides a single broadcast domain into smaller broadcast sub-domains while keeping the existing 
Layer 3 configuration. When a VLAN is configured as a PVLAN, this is referred to as the Primary VLAN, and any 
subsequent VLANs that are associated with the Primary VLAN are referred to as Secondary VLANs.  
 
There are two types of Secondary VLANs: 
- Isolated VLAN: In an Isolated VLAN, all hosts connected to a member port are Isolated at Layer 2. They 
can communicate only with the promiscuous port of the Primary VLAN. There can be only one Isolated 
VLAN within one Primary VLAN. 
- Community VLAN: A Community VLAN is associated to a group of ports that connect to a certain 
“community” of end devices with mutual trust relationships. Any switch port associated with a common 
Community VLAN can communicate with each other and with the promiscuous ports of the Primary VLAN 
but not with any other Secondary VLAN. There can be multiple distinct Community VLANs within one 
Primary VLAN. 
 3 
Lab Diagram

<<<PAGE 110>>>
3 
Private VLAN 
 
 4 
Configuring Link aggregation between 6870-A and 6860 
 
- Type on switches the following commands: 
 
sw7 (6870-A) -> linkagg lacp agg 78 size 2 actor admin-key 78  
sw7 (6870-A) -> show linkagg 
 
sw8 (6860-B) -> linkagg lacp agg 78 size 2 actor admin-key 78  
sw8 (6860-B) -> show linkagg 
 
sw7 (6870-A) -> linkagg lacp port 1/1/23-24 actor admin-key 78 
 
sw8 (6860-B) -> linkagg lacp port 1/1/23-24 actor admin-key 78 
 
sw7 (6870-A) -> interfaces 1/1/23-24 admin-state enable 
 
sw8 (6860-B) -> interfaces 1/1/23-24 admin-state enable 
- Check the result 
 
sw7 (6870-A) -> show linkagg 
sw7 (6870-A) -> show linkagg agg 78 
 
sw8 (6860-B) -> show linkagg 
sw7 (6870-A) -> show linkagg agg 78 
 5 
Configuring the Private VLAN 
5.1. 
Configuring the Private VLAN  
 
- Configure a Primary VLAN 250 on both switches and assign the link aggregation group 78 as an Inter-
Switch-Link for this VLAN:  
 
sw7 (6870-A) -> pvlan 250 admin-state enable 
sw7 (6870-A) -> pvlan 250 members linkagg 78 isl 
 
sw8 (6860-B) -> pvlan 250 admin-state enable 
sw8 (6860-B) -> pvlan 250 members linkagg 78 isl 
 
- Two Secondary VLAN’s are going to be created:  
o 
VLAN 251 as a Community VLAN  
o 
VLAN 252 as an Isolated VLAN 
 
- Configure both VLAN’s on both switches: 
 
sw7 (6870-A) -> pvlan 250 secondary 251 type community 
sw7 (6870-A) -> pvlan 250 secondary 252 type isolated 
 
sw8 (6860-B) -> pvlan 250 secondary 251 type community 
sw8 (6860-B) -> pvlan 250 secondary 252 type isolated

<<<PAGE 111>>>
4 
Private VLAN 
 
- Check that the Secondary VLAN’s are associated to the Primary VLAN on both switches: 
 
sw7 (6870-A) -> show pvlan mapping 
Primary    Secondary 
VLAN       VLAN       Type 
----------+----------+------------ 
250        251        Community 
250        252        Isolated 
 
sw8 (6860-B) -> show pvlan mapping 
Primary    Secondary 
VLAN       VLAN       Type 
----------+----------+------------ 
250        251        Community 
250        252        Isolated 
5.2. 
Configuring the PC Clients  
- Configure the following IP addresses on the PC Clients:  
 
Client 7: 192.168.250.7/24 >> def. GW: 192.168.250.1 
 
Client 8: 192.168.250.8/24 >> def. GW: 192.168.250.2 
 6 
Testing the Configuration 
6.1. 
Testing the Community VLAN 
 
- Move ports 1/1/1 on both switches to VLAN 251 which is the Community VLAN: 
 
sw7 (6870-A) -> pvlan 251 members port 1/1/1 untagged 
 
sw8 (6860-B) -> pvlan 251 members port 1/1/1 untagged 
 
- Enable the 1/1/1 interface on both switches:  
 
sw7 (6870-A) -> interface 1/1/1 admin-state enable 
 
sw8 (6860-B) -> interface 1/1/1 admin-state enable 
 
- Verify the configuration: 
 
sw7 (6870-A) -> show pvlan members 
pvlan   port      type               status       port-type 
-------+---------+------------------+------------+------------ 
250     0/78       qtagged           forwarding   isl  
251     1/1/1     default            forwarding   community 
 
sw8 (6860-B) -> show pvlan members 
pvlan   port      type               status       port-type 
-------+---------+------------------+------------+------------ 
250     0/78       qtagged           forwarding   isl  
251     1/1/1     default            forwarding   community 
 
- Ping from Client 7 to Client 8: 
 
Client 7> ping 192.168.250.8

<<<PAGE 112>>>
5 
Private VLAN 
 
 
This command should be successful as both PC’s now belong to the same community VLAN. Remember 
that all the ports that are part of the same community VLAN can communicate between each other. 
6.2. 
Testing the Isolated VLAN 
 
- Now, let’s check the Isolated VLAN by moving both ports to VLAN 252:  
 
sw7 (6870-A) -> no pvlan 251 members port 1/1/1 
sw7 (6870-A) -> pvlan 252 members port 1/1/1 untagged 
 
sw8 (6860-B) -> no pvlan 251 members port 1/1/1 
sw8 (6860-B) -> pvlan 252 members port 1/1/1 untagged 
 
- Verify the configuration: 
 
sw7 (6870-A) -> show pvlan members 
pvlan   port      type               status       port-type 
-------+---------+------------------+------------+------------ 
250     0/5       qtagged            forwarding   isl  
252     1/1/1     default            forwarding   isolated 
 
sw8 (6860-B) -> show pvlan members 
pvlan   port      type               status       port-type 
-------+---------+------------------+------------+------------ 
250     0/5       qtagged            forwarding   isl  
252     1/1/1     default            forwarding   isolated 
- Ping from Client 7 to Client 8: 
 
Client 7> ping 192.168.250.8 
 
This command should not work because both PC’s now belong to the same Isolated VLAN. Remember that 
in an Isolated VLAN hosts cannot communicate between each other. 
 7 
Deleting the Configuration  
 
- When the tests are completed, delete the PVLAN configuration with the following commands:  
 
sw7 (6870-A) -> no pvlan 252 members port 1/1/1 
sw7 (6870-A) -> no pvlan 250 members linkagg 78 
sw7 (6870-A) -> no pvlan 250 
 
sw8 (6860-B) -> no pvlan 252 members port 1/1/1 
sw8 (6860-B) -> no pvlan 250 members linkagg 78 
sw8 (6860-B) -> no pvlan 250 
 
 
- Save the configuration 
 
sw7 (6870-A) -> write memory flash-synchro 
 
sw8 (6860-B) -> write memory flash-synchro

<<<PAGE 113>>>
MULTIPLE SPANNING TREE PROTOCOL (MSTP)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 114>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the Multiple STP Protocol (MSTP) 
• Learn how to implement it

<<<PAGE 115>>>
CIST
MSTI
CST
MST Region3
MST Region1
MST Region2
MSTP REMINDER - GOAL
• Goal
• Possibility to map several VLANs to one instance 
(IEEE 802.1s standard)
• How it works
• Multiple Spanning Tree Region concept
(Based on RSTP)
• Allows to map one or more VLANs to a single 
Spanning Tree instance 
• Multiple Spanning Tree Instance (MSTI)
• Interoperates with IEEE Common Spanning Tree 
protocols
• FLAT 802.1D
• FLAT 802.1w
CIST
MSTI
CIST
MSTI

<<<PAGE 116>>>
MSTP REMINDER – STP INSTANCES
• How it works
• Instead of running one STP
Instance for every VLAN,
MSTP runs a number of
VLAN-independent STP instances 
(= logical topologies)
• The administrator maps each VLAN
to the most appropriate STP instance,
also called MSTI (MST Instance)
PHYSICAL TOPOLOGY
INSTANCE 0 (= MSTI 0)
INSTANCE 1 (= MSTI1)
INSTANCE 2 (= MSTI 2)
VLAN 1
VLAN 10
VLAN 20
VLAN 30
VLAN 40
VLAN 50
VLAN 60
VLAN 1
VLAN 10
VLAN 20
VLAN 30
VLAN 40
VLAN 50
VLAN 60
Note: If a VLAN is not mapped to any MSTI,
it is associated to the MSTI 0 (aka IST)
LOGICAL TOPOLOGIES

<<<PAGE 117>>>
CIST
MSTI
CSTI
MSTI
CST
MST Region3 
MST Region1
MST Region2 
MSTP REMINDER - REGION
• How it works
• A MSTP region is 
• A collection of switches
• Sharing the same view of physical topology 
• Partitioning into the same set of logical topologies
• MSTP Region seen as one switch for
the rest of the world
• Rest of the world only “aware” of the CST instance 0
• Forwards traffic for VLANs which are not covered by 
any MSTI
• CST interacts with STP outside the region Achieve 
this by representing the region as one Virtual 
spantree
• MST region sees the outside world via its CIST/ CST 
interaction only
IST
IST
IST
MSTI 0= IST <> VLAN 1
REGION 2 / 
REVISION NB: 1 
REGION 1 
REVISION NB: 1 
REGION 3 
REVISION NB: 1

<<<PAGE 118>>>
MSTP REMINDER - INTRA REGION 
• How it works
• BPDUs are carried through the network via the MSTI 
0 (aka IST, Internal Spanning Tree)
• Root switch sends out BPDUs with maximum hop 
count which is decremented at each switch as BPDUs 
are forwarded. At 0 hop, the BPDUs are discarded
• One BPDU is exchanged for all instances over default 
VLAN
• MSTP BPDUs are sent on every port
• The maximum hop count supported is 40, default is 
20
CIST 0 = VLAN 1
MSTI 1 = VLAN 11 to 13
MSTI 2 = VLAN 14 to 16
MSTI 3 = VLAN 17 to 20
Root spantree
CIST 0
MSTI 1
Root spantree
MSTI 2
Root spantree
MSTI 3
VLAN 11 to 20 tagged
Note: If a VLAN is not mapped to any MSTI, 
it is associated to the MSTI 0 (aka IST)

<<<PAGE 119>>>
MSTP REMINDER - SPECIFICATION
• Specification
• Instance 0
• Always configured on any 802.1s switch
• Common and Internal Spanning Tree instance
• CIST
• By default, all VLANs are mapped to the CIST
• Up to 16 other instances are supported by Alcatel-Lucent AOS
• Multiple Spanning Tree Instance – MSTI

<<<PAGE 120>>>
MSTP CONFIGURATION

<<<PAGE 121>>>
MSTP CONFIGURATION
Step by Step
Map VLANs to MSTI
Manage Switch Priority
Select the Flat Spanning Tree mode
Select the MSTP protocol
Configure MST regions (name, revision level)
Configure MSTIs

<<<PAGE 122>>>
MSTP CONFIGURATION
Step by Step
Change Spanning Tree mode to flat mode
Change Spanning Tree protocol to MSTP
SW1
SW2
SW3
-> spantree mode flat
-> spantree protocol mstp
Select the Flat Spanning Tree mode
Select the MSTP protocol

<<<PAGE 123>>>
MSTP CONFIGURATION
Step by Step
SW1
SW2
SW3
REGION_1
REVISION NB: 1 
Create a MSTP region
To belong to the same region, switches must 
have the same:
Region name
Revision level
VLAN to MSTI mapping
-> spantree mst region name {mst_region_name}
-> spantree mst region revision level 1
-> spantree msti {msti_id} 
-> spantree msti {msti_id} vlan {vlan_id}
Configure MST regions (name, revision level)

<<<PAGE 124>>>
MSTP CONFIGURATION
Step by Step
Every switch has a CIST (= MSTI 0)
Create additional MSTI 
Required to segment VLANs into separate instances
SW1
SW2
SW3
REGION_1
REVISION NB: 1 
MSTI 0 
MSTI 1
MSTI 2
-> spantree msti {msti_id} 
-> spantree msti {msti_id} vlan {vlan_id}
Configure MSTIs

<<<PAGE 125>>>
MSTP CONFIGURATION
Step by Step
Assign the VLANs to the MSTIs
Non assigned VLANs are mapped to 
the MSTI 0 (CIST)
SW1
SW2
SW3
REGION_1
REVISION NB: 1 
MSTI 1 <> VLAN 20
MSTI 2 <> VLAN 30
CIST 0 <> OTHER VLANS
-> spantree msti {msti_id} vlan {vlan_id}
Map VLANs to MSTI

<<<PAGE 126>>>
MSTP CONFIGURATION
Step by Step
Configure the switch priority value for
each switch 
Used to determine which switch will be
Root spantree
Tips: Manage switches priority values to have a 
different switch assumes the Root spantree role for each MSTI
Ex
SW1
SW2
SW3
REGION_1
REVISION NB: 1 
MSTI 1 <> VLAN 20
MSTI 2 <> VLAN 30
CIST 0 <> OTHER VLANS
RB
RB
RB
SW 1
SW 2 
SW 3
MSTI 0 (CIST)
32768
32768
16384
MSTI 1 
16384
32768
32768
MSTI 2 
32768
16384
32768
Manage Switch Priority

<<<PAGE 127>>>
CONFIGURING MSTP - MONITORING
-> show spantree msti 3
Spanning Tree Parameters for Msti 3
Spanning Tree Status:
ON,
Protocol:
IEEE Multiple STP,
mode:
FLAT (Single STP),
Priority:
4099 (0x1003),
spantree ID:
1003-00:d0:95:bd:2a:e2,
Designated Root:
1003-00:d0:95:bd:2a:e2,
Cost to Root spantree:
0,
Root Port:
None,
Next Best Root Cost:
0,
Next Best Root Port:
None,
Hold Time:
1,
Topology Changes:
5,
Topology age:
00:06:50,
Current Parameters (seconds)
Max Age
=
20,
Forward Delay
=
15,
Hello Time
=
2
Parameters system uses when attempting to become root
System Max Age
=
20,
System Forward Delay
=
15,
System Hello Time
=
2
-> show spantree mst region
Configuration Name       : myregion,
Revision Level          : 1,
Configuration Digest    : 0x45929389 64c56251 6c821b64 d0862c32,
Revision Max hops       : 20,
Cist Instance Number    :0
Monitoring

<<<PAGE 128>>>
CONFIGURING MSTP - EXAMPLE
Mapping:
VLAN 1 -> instance 0 (CIST)
VLAN 1 to 15 -> instance 1
VLAN 16 to 20 -> instance 2
1/1/1
1/1/2
1/1/11
1/1/22
Root spantree
CSTI 0
MSTI 1
Root spantree
MSTI 2
VLAN 1 to 20
-> spantree mode flat
-> spantree protocol mstp
-> spantree mst region name myregion
-> spantree mst region revision 1
-> spantree cist protocol mstp
-> spantree msti 1
-> spantree msti 1 VLAN 1-15
-> spantree msti 2
-> spantree msti 2 VLAN 16-20
-> spantree cist priority 4096
-> spantree msti 1 priority 4096
-> spantree msti 2 priority 8192
-> spantree msti 1 1/1/1 priority 1
-> spantree msti 2 1/1/1 priority 15
-> spantree msti 1 1/1/11 priority 15
-> spantree msti 2 1/1/11 priority 1
-> spantree mode flat
-> spantree protocol mstp
-> spantree mst region name myregion
-> spantree mst region revision 1
-> spantree cist protocol mstp
-> spantree msti 1
-> spantree msti 1 VLAN 1-15
-> spantree msti 2
-> spantree msti 2 VLAN 16-20
-> spantree cist priority 8192
-> spantree msti 1 priority 8192
-> spantree msti 2 priority 4096
-> spantree msti 1 1/1/2 priority 1
-> spantree msti 2 1/1/2 priority 15
-> spantree msti 1 1/1/22 priority 15
-> spantree msti 2 1/1/22 priority 1
Example 1

<<<PAGE 129>>>
SwitchB-> show spantree mst port 1/1/2
MST  Role  State Pth Cst
Edge Boundary Op Cnx Vlans
---+------+-----+--------+----+--------+------+---------
0  ROOT   FORW    20000   NO    NO
PTP
1  ROOT   FORW    20000   NO    NO
PTP    1-15
2  DESG   FORW    20000   NO    NO
PTP
SwitchB-> show spantree mst port 1/1/22
MST  Role  State Pth Cst
Edge Boundary Op Cnx Vlans
---+------+-----+--------+----+--------+------+---------
0   ALT    BLK    20000   NO    NO
PTP    100
1   ALT    BLK    20000   NO    NO
PTP
2  DESG   FORW    20000   NO    NO
PTP    16-20
CONFIGURING MSTP - EXAMPLE 
SwitchA-> show spantree mst port 1/1/1
MST  Role  State Pth Cst
Edge Boundary Op Cnx Vlans
---+------+-----+--------+----+--------+------+---------
0  DESG   FORW    20000   NO    NO
PTP
1  DESG   FORW    20000   NO    NO
PTP    1-15
2   ALT    BLK    20000   NO    NO
PTP
SwitchA-> show spantree mst port 1/1/11
MST  Role  State Pth Cst
Edge Boundary Op Cnx Vlans
---+------+-----+--------+----+--------+------+---------
0  DESG   FORW    20000   NO    NO
PTP    100
1  DESG   FORW    20000   NO    NO
PTP
2  ROOT   FORW    20000   NO    NO
PTP    16-20
1/1/1
1/1/2
1/1/11
1/1/22
VLAN 1 to 15
VLAN 16 to 20
Root spantree
CSTI 0
MSTI 1
Root spantree
MSTI 2
SwitchA
SwitchB
X
X
Example 1

<<<PAGE 130>>>
Mapping:
VLAN 1 -> instance 0 (CIST)
VLAN 2 and 3 -> instance 1
VLAN 4 and 5 -> instance 2  
Priority
Switch A
Switch B
Switch C
CIST
4096
32768
32768
MIST 1
32768
4096
32768
MIST 2
32768
32768
4096
1/1/2
3/1/2
1/1/3
3/1/1
Switch A
Switch B
Switch C
Root spantree
MSTI 1
2/1/1
2/1/3
1/1/2
3/1/2
1/1/3
3/1/1
Switch A
Switch B
Switch C
Root spantree
MSTI 2
2/1/1
2/1/3
VLAN 2 and 3
VLAN 4 and 5
CONFIGURING MSTP - EXAMPLE 
Traffic Load Sharing
Example 2

<<<PAGE 131>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 132>>>
OmniSwitch AOS R8 
Multiple Spanning Tree Protocol 
How to 
✓ This lab is designed to familiarize you with the Multiple Spanning Tree 
Protocol (MSTP) on an OmniSwitch. 
Contents 
1 
Topology ........................................................................................ 2 
2 
Manage a 6360 Virtual Chassis ............................................................... 3 
3 
Connect 6360 VC to 6870-A and 6860-B .................................................... 7 
3.1. Assign another default Vlan to the linkagg 78 .................................................. 7 
3.2. Manage a linkagg between 6360 VC and 6870-A ............................................... 8 
3.3. Connect 6360 VC and 6860-B ..................................................................... 8 
3.4. Create Additional users VLANs .................................................................... 9 
4 
Multiple Spanning Tree ..................................................................... 10

<<<PAGE 133>>>
2 
Multiple Spanning Tree Protocol 
 
 
 
 1 
Topology

<<<PAGE 134>>>
3 
Multiple Spanning Tree Protocol 
 
 2 
Manage a 6360 Virtual Chassis 
 
- 
Please note some PODs are using 6360A/6360B with 10 ports or 24 ports. 
 
- 
Type the following command to determine the type of switch used in the POD. 
 
 
sw5 (6360-A) -> show chassis 
Local Chassis ID 1 (Master) 
  Model Name:                    OS6360-P10, 
  Module Type:                   0xc0e2201, 
  Description:                   Chassis, 
  Part Number:                   904306-90, 
  Hardware Revision:             02, 
  Serial Number:                 WHS233501662, 
  Manufacture Date:              Aug 30 2023, 
  Admin Status:                  POWER ON, 
  Operational Status:            UP, 
  Number Of Resets:              12, 
  MAC Address:                   78:24:59:49:65:f5 
 
- 
In case of OS6360-P10 the VFL ports are 1/1/11-12 
- 
In case of OS6360-P24 the VFL ports are 1/1/27-28 
 
 
- 
Assign a globally unique chassis identifier to the switch 6360A and 6360-B and enable the switches to 
operate in virtual chassis mode 
 
sw5 (6360-A) -> show virtual-chassis topology 
sw5 (6360-A) -> virtual-chassis chassis-group 1 
sw5 (6360-A) -> virtual chassis-id 1 configured-chassis-priority 200 
sw5 (6360-A) -> write memory 
sw5 (6360-A) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y 
 
Notes: 
Wait until complete restart. 
 
 
Tue Jun 22 03:04:41 : qosNi Info INFO message: 
+++ VC Takeover in progress. 
+++ VC Takeover complete. 
Chassis Supervision: CMM has reached the ready state [L8]

<<<PAGE 135>>>
4 
Multiple Spanning Tree Protocol 
 
sw6 (6360-B) -> show virtual-chassis topology 
sw6 (6360-B) -> virtual-chassis chassis-id 1 configured-chassis-id 2 
sw6 (6360-B) -> virtual-chassis chassis-group 1 
sw6 (6360-B) -> show configuration vcm-snapshot chassis-id 2 
sw6 (6360-B) -> write memory 
WARNING - Virtual chassis topology change detected. Chassis 1 missing! 
          Configuration associated with missing chassis will be erased permanently! 
          Confirm to continue  (Y/N) : y 
sw6 (6360-B) -> reload from working no rollback-timeout  
Confirm Activate (Y/N) : y 
 
 
Notes: 
Wait until complete restart. 
 
 
Tue Jun 22 03:04:41 : qosNi Info INFO message: 
+++ VC Takeover in progress. 
+++ VC Takeover complete. 
Chassis Supervision: CMM has reached the ready state [L8]

<<<PAGE 136>>>
5 
Multiple Spanning Tree Protocol 
 
- 
Configure member ports for the VFL on 6360-A in case of OS6360-P24: 
 
sw5 (6360-A) -> virtual-chassis vf-link-mode auto 
sw5 (6360-A) -> virtual-chassis auto-vf-link-port 1/1/27 
sw5 (6360-A) -> virtual-chassis auto-vf-link-port 1/1/28 
sw5 (6360-A) -> write memory 
 
sw5 (6360-A) -> show configuration vcm-snapshot chassis-id 1 
! Virtual Chassis Manager: 
virtual-chassis chassis-id 1 configured-chassis-id 1 
virtual-chassis vf-link-mode auto 
virtual-chassis auto-vf-link-port 1/1/27 
virtual-chassis auto-vf-link-port 1/1/28 
virtual-chassis chassis-id 1 chassis-group 1 
virtual-chassis chassis-id 1 configured-chassis-priority 200 
! PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx] 
! [SAVED INFO VC IDs] 1 
 
- 
Configure member ports for the VFL on 6360-A in case of OS6360-P10: 
 
sw5 (6360-A) -> virtual-chassis vf-link-mode auto 
sw5 (6360-A) -> virtual-chassis auto-vf-link-port 1/1/11 
sw5 (6360-A) -> virtual-chassis auto-vf-link-port 1/1/12 
sw5 (6360-A) -> write memory 
 
sw5 (6360-A) -> show configuration vcm-snapshot chassis-id 1 
! Virtual Chassis Manager: 
virtual-chassis chassis-id 1 configured-chassis-id 1 
virtual-chassis vf-link-mode auto 
virtual-chassis auto-vf-link-port 1/1/11 
virtual-chassis auto-vf-link-port 1/1/12 
virtual-chassis chassis-id 1 chassis-group 1 
virtual-chassis chassis-id 1 configured-chassis-priority 200 
! PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx] 
! [SAVED INFO VC IDs] 1 
 
- 
Configure member ports for the VFL on 6360-B in case of 6360-P24: 
 
sw6 (6360-B) -> virtual-chassis vf-link-mode auto 
sw6 (6360-B) -> virtual-chassis auto-vf-link-port 2/1/27 
sw6 (6360-B) -> virtual-chassis auto-vf-link-port 2/1/28 
sw6 (6360-B) -> write memory 
 
 
sw6 (6360-B) -> show configuration vcm-snapshot chassis-id 2 
! Virtual Chassis Manager: 
virtual-chassis chassis-id 2 configured-chassis-id 2 
virtual-chassis vf-link-mode auto 
virtual-chassis auto-vf-link-port 2/1/27 
virtual-chassis auto-vf-link-port 2/1/28 
virtual-chassis chassis-id 2 chassis-group 1 
! PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx] 
! [SAVED INFO VC IDs] 2 
! IP: 
 
- 
Configure member ports for the VFL on 6360-B in case of 6360-P10: 
 
sw6 (6360-B) -> virtual-chassis vf-link-mode auto 
sw6 (6360-B) -> virtual-chassis auto-vf-link-port 2/1/11 
sw6 (6360-B) -> virtual-chassis auto-vf-link-port 2/1/12 
sw6 (6360-B) -> write memory

<<<PAGE 137>>>
6 
Multiple Spanning Tree Protocol 
 
sw6 (6360-B) -> show configuration vcm-snapshot chassis-id 2 
 
! Virtual Chassis Manager: 
virtual-chassis chassis-id 2 configured-chassis-id 2 
virtual-chassis vf-link-mode auto 
virtual-chassis auto-vf-link-port 2/1/11 
virtual-chassis auto-vf-link-port 2/1/12 
virtual-chassis chassis-id 2 chassis-group 1 
! PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx] 
! [SAVED INFO VC IDs] 2 
! IP: 
 
- 
Activate the corresponding interfaces. 
6360-P24 
sw5 (6360-A) -> interfaces 1/1/27-28 admin-state enable  
 
6360-P10 
sw5 (6360-A) -> interfaces 1/1/11-12 admin-state enable 
 
 
Notes: 
On the 6360-B, INTERFACE 2/1/27 and INTERFACE 2/1/28 (6360-P10 2/1/11 and 2/1/12) automatically LINK UP 
and the switch Reboot. 
 
- 
Wait for a moment after reboot (*reboot: close to 5 mn in lab context) 
o 
Message will be displayed on 6360-A. 
Chassis Supervision: CMM has reached the ready state [L8] 
 
Fri Oct  1 06:46:47 : intfCmm Mgr INFO message: 
+++ Link 2/1/27 operationally up 
+++ Link 2/1/28 operationally up 
 
Fri Oct  1 06:46:56 : isisVc vcprot INFO message: 
+++ isisVcUpdateVcNodes@7059: Adding peer chassisId 1 (mac 94:24:e1:7c:79:f5) 
+++ isisVcUpdateVcNodes@7421: New Master: chassisId 1 chassisMac 94:24:e1:7c:79:f5 
 
Fri Oct  1 06:46:57 : vcmCmm ipc INFO message: 
+++ CMM:vcmCMM_peer_connected@2494: Remote endpoint (chassis 1, slot 65) [L4] 
 
- 
Save the configuration and Check the virtual-chassis topology and Copy running to certified: 
sw5 (6360-A) -> show virtual-chassis topology 
sw5 (6360-A) -> write memory flash-synchro

<<<PAGE 138>>>
7 
Multiple Spanning Tree Protocol 
 
 3 
Connect 6360 VC to 6870-A and 6860-B 
 
 
 
 
 
 
3.1. 
Assign another default Vlan to the linkagg 78 
 
- 
By default, the linkagg 78 is associated with vlan 1. 
In order to increase security, assign another default vlan to it and an IP address to this VLAN : 
 
 
sw7 (6870-A) -> vlan 278 
sw7 (6870-A) -> ip interface int_278 address 172.16.78.7/24 vlan 278 
sw7 (6870-A) -> vlan 278 members linkagg 78 untagged 
sw7 (6870-A) -> show vlan 278 members 
sw7 (6870-A) -> show ip interface 
 
sw8 (6860-B) -> vlan 278 
sw8 (6860-B) -> ip interface int_278 address 172.16.78.8/24 vlan 278 
sw8 (6860-B) -> vlan 278 members linkagg 78 untagged 
sw8 (6860-B) -> show vlan 278 members 
sw8 (6860-B) -> show ip interface

<<<PAGE 139>>>
8 
Multiple Spanning Tree Protocol 
 
o 
Try to make a ping between both 6860 
 
sw7 (6870-A) -> ping 172.16.78.8 
sw8 (6860-B) -> ping 172.16.78.7 
 
3.2. 
Manage a linkagg between 6360 VC and 6870-A 
 
 
sw5 (OS6360-A) -> linkagg lacp agg 7 size 2 actor admin-key 7 
sw5 (OS6360-A) -> linkagg lacp port 1/1/3 actor admin-key 7 
sw5 (OS6360-A) -> linkagg lacp port 2/1/4 actor admin-key 7 
sw5 (OS6360-A) -> interfaces 1/1/3 admin-state enable 
sw5 (OS6360-A) -> interfaces 2/1/4 admin-state enable 
sw5 (OS6360-A) -> show linkagg 
 
sw7 (OS6870-A) -> linkagg lacp agg 7 size 2 actor admin-key 7 
sw7 (OS6870-A) -> linkagg lacp port 1/1/3-4 actor admin-key 7 
sw7 (OS6870-A) -> interface 1/1/3-4 admin-state enable 
sw7 (OS6870-A) -> show linkagg 
- 
For security reason, the client wants to avoid using the VLAN 1 as the network data VLAN. So, the VLAN 
associated with link aggregation 7 must be modified:  
 
sw5 (OS6360-A) -> vlan 57 
sw5 (OS6360-A) -> vlan 57 members linkagg 7 untagged 
 
sw7 (OS6870-A)-> vlan 57 
sw7 (OS6870-A)-> vlan 57 members linkagg 7 untagged 
3.3. 
Connect 6360 VC and 6860-B

<<<PAGE 140>>>
9 
Multiple Spanning Tree Protocol 
 
- 
Activate the port 2/1/3 on the 6360 Virtual Chassis (linked to the 6860-B):  
sw5 (6360-A) -> interfaces 2/1/3 admin-state enable 
 
- 
Create the VLAN 58, then modify the VLAN on the port 2/1/3 from the default VLAN (VLAN 1) to VLAN 
58: 
sw5 (6360-A) -> vlan 58 
sw5 (6360-A) -> vlan 58 members port 2/1/3 untagged 
 
sw5 (6360-A) -> show vlan 58 member 
   port      type        status 
----------+-----------+--------------- 
  2/1/3      default        inactive 
- 
Activate the port 1/1/3 on the 6860-B (linked to the 6360 Virtual Chassis):  
sw8 (6860-B) -> interfaces 1/1/3 admin-state enable 
 
- 
Create the VLAN 58, then modify the VLAN on the port 1/1/3 from the default VLAN to VLAN 58:  
sw8 (6860-B) -> vlan 58 
sw8 (6860-B) -> vlan 58 members port 1/1/3 untagged 
 
 
sw8 (6860-B) -> show vlan 58 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/3      default      forwarding 
 
3.4. 
Create Additional users VLANs  
 
- Currently, only 2 VLANs are bridged: 
▪ 
VLAN 57 between the 6870-A and the 6360 Virtual Chassis 
▪ 
VLAN 58 between the 6860-B and the 6360 Virtual Chassis 
 
- 
Create the VLANs 20 and 30 on the 3 switches (Virtual Chassis 6360-A, 6870-A and 6860-B) : 
sw5 (6360-A) -> vlan 20 
sw5 (6360-A) -> vlan 30 
 
sw7 (6870-A) -> vlan 20 
sw7 (6870-A) -> vlan 30 
 
sw8 (6860-B) -> vlan 20 
sw8 (6860-B) -> vlan 30 
 
• 
The gateway for the VLAN 20 will be created on the 6870-A. 
• 
The gateway for the VLAN 30 will be created on the 6860-B. 
 
- 
Assign an IP interface to these 2 new VLAN on the correspondent switches: 
sw7 (6870-A) -> ip interface int_20 address 192.168.20.7/24 vlan 20 
 
sw8 (6860-B) -> ip interface int_30 address 192.168.30.8/24 vlan 30 
 
- 
Tag the VLANs 20 and 30 on the link between the 3 switches:

<<<PAGE 141>>>
10 
Multiple Spanning Tree Protocol 
 
sw5 (6360-A) -> vlan 20 members linkagg 7 tagged  
sw5 (6360-A) -> vlan 30 members linkagg 7 tagged 
 
sw5 (6360-A) -> vlan 20 members port 2/1/3 tagged 
sw5 (6360-A) -> vlan 30 members port 2/1/3 tagged 
sw5 (6360-A) -> write memory 
 
sw7 (6870-A) -> vlan 20 members linkagg 78 tagged  
sw7 (6870-A) -> vlan 30 members linkagg 78 tagged 
 
sw7 (6870-A) -> vlan 20 members linkagg 7 tagged  
sw7 (6870-A) -> vlan 30 members linkagg 7 tagged 
sw7 (6870-A) -> write memory  
 
sw8 (6860-B) -> vlan 20 members linkagg 78 tagged 
sw8 (6860-B) -> vlan 30 members linkagg 78 tagged 
 
sw8 (6860-B) -> vlan 20 members port 1/1/3 tagged 
sw8 (6860-B) -> vlan 30 members port 1/1/3 tagged 
sw8 (6860-B) -> write memory  
 4 
Multiple Spanning Tree 
802.1s is an IEEE standard allowing for multiple STP instances to be configured on the switch. It is similar in 
operation to 1X1 mode, but allows for multiple VLANs to be assigned to a single STP instance. 
 
- 
To configure MSTP, spanning tree has to be configured first in flat mode: 
sw5 (6360-A) -> spantree mode flat 
sw7 (6870-A) -> spantree mode flat 
sw8 (6860-B) -> spantree mode flat 
- 
Then set the protocol to mstp : 
sw5 (6360-A) -> spantree mst region name lab_region 
sw5 (6360-A) -> spantree mst region revision-level 1 
sw5 (6360-A) -> spantree protocol mstp 
 
sw7 (6870-A) -> spantree mst region name lab_region 
sw7 (6870-A) -> spantree mst region revision-level 1 
sw7 (6870-A) -> spantree protocol mstp 
 
sw8 (6860-B) -> spantree mst region name lab_region 
sw8 (6860-B) -> spantree mst region revision-level 1 
sw8 (6860-B) -> spantree protocol mstp 
 
sw8 (6860-B) -> show spantree cist 
Spanning Tree Parameters for Cist 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32768 (0x8000), 
  Bridge ID            :   8000-e8:e7:32:b3:3c:f9, 
  CST Designated Root  :   8000-2c:fa:a2:aa:34:9f, 
  Cost to CST Root     :                20004, 
  Designated Root      :   8000-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                36000, 
  Root Port            :  Slot 0 Interface 78, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    7, 
  Topology age         :             00:00:08, 
  Last TC Rcvd Port    :  Slot 0 Interface 78,

<<<PAGE 142>>>
11 
Multiple Spanning Tree Protocol 
 
  Last TC Rcvd Bridge  :   8000-e8:e7:32:d9:b4:b9, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
 
sw5 (6360-A) -> show spantree cist 
Spanning Tree Parameters for Cist 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32768 (0x8000), 
  Bridge ID            :   8000-94:24:e1:7c:82:41, 
  CST Designated Root  :   8000-2c:fa:a2:aa:34:9f, 
  Cost to CST Root     :                20004, 
  Designated Root      :   8000-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                    0, 
  Root Port            :               1/1/24, 
  TxHoldCount          :                    3, 
  Topology Changes     :                   15, 
  Topology age         :             00:00:39, 
  Last TC Rcvd Port    :               1/1/24, 
  Last TC Rcvd Bridge  :   8000-e8:e7:32:7d:0e:40, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw7 (6870-A) -> show spantree cist 
Spanning Tree Parameters for Cist 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32768 (0x8000), 
  Bridge ID            :   8000-e8:e7:32:d9:b4:b9, 
  CST Designated Root  :   8000-2c:fa:a2:aa:34:9f, 
  Cost to CST Root     :                20004, 
  Designated Root      :   8000-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                18000, 
  Root Port            :   Slot 0 Interface 7, 
  TxHoldCount          :                    3, 
  Topology Changes     :                   13, 
  Topology age         :            00:01:41, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8000-94:24:e1:7c:82:41, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
Tips 
Notice the Cost to Root Bridge values in the example above. Multiple STP uses a 32-bit Path Cost value vs the 
16-bit path cost value that 802.1d/802.1w use by default.

<<<PAGE 143>>>
12 
Multiple Spanning Tree Protocol 
 
 
 
Notes 
The commands above set the switch to flat mode, configured a Multiple STP region name and revision level, 
and finally enabled the IEEE MSTP protocol. 1X1 and MSTP cannot be configured at the same time; and the 
switch must be configured in flat Spanning Tree mode. 
 
 
 
- 
Now, check to see how 802.1s operates with just the single default STP instance, called the Common 
and Internal Spanning Tree (CIST): 
sw5 (6360-A) -> show spantree cist vlan-map 
Cist 
  Name          : , 
  VLAN list     : 1-4094 
 
sw7 (6870-A) -> show spantree cist vlan-map 
Cist 
  Name          : , 
  VLAN list     : 1-4094 
 
sw8 (6860-B) -> show spantree cist vlan-map 
Cist 
  Name          : , 
  VLAN list     : 1-4094 
- 
You should see that all VLANs belong to the CIST instance, the CIST instance is created by default and all 
VLANs on the switch are mapped to it by default.  
- 
Now, create 2 additional STP instances and map the appropriate VLANs to them. Type the following: 
sw5 (6360-A) -> spantree msti 1 
sw5 (6360-A) -> spantree msti 2 
sw5 (6360-A) -> spantree msti 1 vlan 20 
sw5 (6360-A) -> spantree msti 2 vlan 30 
 
sw7 (6870-A) -> spantree msti 1 
sw7 (6870-A) -> spantree msti 2 
sw7 (6870-A) -> spantree msti 1 vlan 20 
sw7 (6870-A) -> spantree msti 2 vlan 30 
 
sw8 (6860-B) -> spantree msti 1 
sw8 (6860-B) -> spantree msti 2 
sw8 (6860-B) -> spantree msti 1 vlan 20 
sw8 (6860-B) -> spantree msti 2 vlan 30 
 
sw5 (6360-A) -> show spantree msti vlan-map 
Cist 
  Name          : , 
  VLAN list     : 1-19,21-29,31-4094 
Msti 1 
  Name          : , 
  VLAN list     : 20 
Msti 2 
  Name          : , 
  VLAN list     : 30 
 
sw7 (6870-A) -> show spantree msti vlan-map 
Cist 
  Name          : , 
  VLAN list     : 1-19,21-29,31-4094 
Msti 1 
  Name          : , 
  VLAN list     : 20 
Msti 2 
  Name          : , 
  VLAN list     : 30

<<<PAGE 144>>>
13 
Multiple Spanning Tree Protocol 
 
sw8 (6860-B) -> show spantree msti vlan-map 
 
Cist 
  Name          : , 
  VLAN list     : 1-19,21-29,31-4094 
Msti 1 
  Name          : , 
  VLAN list     : 20 
Msti 2 
  Name          : , 
  VLAN list     : 30 
 
 
Notes 
Vlan 20 and 30 have been removed from the CIST and associated with a Multiple Spanning Tree Instance (MSTI). 
We could have of course associate several VLAN to the same MSTI 
 
 
- 
Now, check the root bridge for the MSTI's : 
sw5 (6360-A) -> show spantree msti 1 
Spanning Tree Parameters for Msti 1 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32769 (0x8001), 
  Bridge ID            :   8001-94:24:e1:7c:82:41, 
  Designated Root      :   8001-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    9, 
  Topology age         :            00:09:55, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8001-e8:e7:32:d9:b4:b9, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw5 (6360-A) -> show spantree msti 2 
Spanning Tree Parameters for Msti 2 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32770 (0x8002), 
  Bridge ID            :   8002-94:24:e1:7c:82:41, 
  Designated Root      :   8002-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    9, 
  Topology age         :            00:10:24, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8002-e8:e7:32:d9:b4:b9, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2

<<<PAGE 145>>>
14 
Multiple Spanning Tree Protocol 
 
 
sw7 (6870-A) -> show spantree msti 1 
Spanning Tree Parameters for Msti 1 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32769 (0x8001), 
  Bridge ID            :   8001-e8:e7:32:d9:b4:b9, 
  Designated Root      :   8001-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                18000, 
  Root Port            :   Slot 0 Interface 7, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    4, 
  Topology age         :            00:11:04, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw7 (6870-A) -> show spantree msti 2 
Spanning Tree Parameters for Msti 2 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32770 (0x8002), 
  Bridge ID            :   8002-e8:e7:32:d9:b4:b9, 
  Designated Root      :   8002-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                18000, 
  Root Port            :   Slot 0 Interface 7, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    4, 
  Topology age         :            00:11:34, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw8 (6860-B) -> show spantree msti 1 
Spanning Tree Parameters for Msti 1 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32769 (0x8001), 
  Bridge ID            :   8001-e8:e7:32:b3:3c:f9, 
  Designated Root      :   8001-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                36000, 
  Root Port            :  Slot 0 Interface 78, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    1, 
  Topology age         :            00:11:49, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds)

<<<PAGE 146>>>
15 
Multiple Spanning Tree Protocol 
 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw8 (6860-B) -> show spantree msti 2 
Spanning Tree Parameters for Msti 2 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32770 (0x8002), 
  Bridge ID            :   8002-e8:e7:32:b3:3c:f9, 
  Designated Root      :   8002-94:24:e1:7c:82:41, 
  Cost to Root Bridge  :                36000, 
  Root Port            :  Slot 0 Interface 78, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    1, 
  Topology age         :            00:13:13, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
- 
Notice that both MSTIs have the same root bridge. Load balancing can be achieved by changing the 
priority of bridge for different MSTI as we have done with RSTP: 
sw7 (6870-A) -> spantree msti 1 priority 16384 
sw8 (6860-B) -> spantree msti 2 priority 16384  
 
 
Notes 
Priority has to be multiple of 4096 (8192, 12288, 16384, …, 61440) 
 
sw7 (6870-A) -> show spantree msti 1 
Spanning Tree Parameters for Msti 1 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       16385 (0x4001), 
  Bridge ID            :   4001-e8:e7:32:d9:b4:b9, 
  Designated Root      :   4001-e8:e7:32:d9:b4:b9, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    4, 
  Topology age         :            00:14:51, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2

<<<PAGE 147>>>
16 
Multiple Spanning Tree Protocol 
 
sw5 (6360-A) -> show spantree msti 1 
Spanning Tree Parameters for Msti 1 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32769 (0x8001), 
  Bridge ID            :   8001-94:24:e1:7c:82:41, 
  Designated Root      :   4001-e8:e7:32:d9:b4:b9, 
  Cost to Root Bridge  :                18000, 
  Root Port            :   Slot 0 Interface 7, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    9, 
  Topology age         :            00:15:29, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8001-e8:e7:32:d9:b4:b9, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw8 (6860-B) -> show spantree msti 1 
Spanning Tree Parameters for Msti 1 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32769 (0x8001), 
  Bridge ID            :   8001-e8:e7:32:b3:3c:f9, 
  Designated Root      :   4001-e8:e7:32:d9:b4:b9, 
  Cost to Root Bridge  :                18000, 
  Root Port            :  Slot 0 Interface 78, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    1, 
  Topology age         :            00:15:48, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw5 (6360-A) -> show spantree msti 2 
Spanning Tree Parameters for Msti 2 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32770 (0x8002), 
  Bridge ID            :   8002-94:24:e1:7c:82:41, 
  Designated Root      :   4002-e8:e7:32:b3:3c:f9, 
  Cost to Root Bridge  :                36000, 
  Root Port            :   Slot 0 Interface 7, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    9, 
  Topology age         :            00:16:54, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8002-e8:e7:32:d9:b4:b9, 
    Current Parameters (seconds) 
      Max Age              =    20,

<<<PAGE 148>>>
17 
Multiple Spanning Tree Protocol 
 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw7 (6870-A) -> show spantree msti 2 
Spanning Tree Parameters for Msti 2 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       32770 (0x8002), 
  Bridge ID            :   8002-e8:e7:32:d9:b4:b9, 
  Designated Root      :   4002-e8:e7:32:b3:3c:f9, 
  Cost to Root Bridge  :                18000, 
  Root Port            :  Slot 0 Interface 78, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    4, 
  Topology age         :            00:17:36, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw8 (6860-B) -> show spantree msti 2 
Spanning Tree Parameters for Msti 2 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Multiple STP, 
  mode                 :    FLAT (Single STP), 
  Auto-Vlan-Containment:           Enabled   , 
  Priority             :       16386 (0x4002), 
  Bridge ID            :   4002-e8:e7:32:b3:3c:f9, 
  Designated Root      :   4002-e8:e7:32:b3:3c:f9, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    1, 
  Topology age         :            00:17:29, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   0000-00:00:00:00:00:00, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
 
 
Tips 
Note, in Multiple Spanning Tree the bridge priority is the assigned Bridge Priority value PLUS the MSTI instance 
value

<<<PAGE 149>>>
18 
Multiple Spanning Tree Protocol 
 
- 
To continue with next labs, revert spanning tree in 1x1 mode : 
 
sw5 (6360-A) -> spantree mode per-vlan 
sw7 (6870-A) -> spantree mode per-vlan 
sw8 (6860-B) -> spantree mode per-vlan 
 
sw5 (6360-A) -> no spantree mst region name 
sw7 (6870-A) -> no spantree mst region name 
sw8 (6860-B) -> no spantree mst region name 
 
sw5 (6360-A) -> no spantree msti 1 
sw7 (6870-A) -> no spantree msti 1 
sw8 (6860-B) -> no spantree msti 1 
 
sw5 (6360-A) -> no spantree msti 2 
sw7 (6870-A) -> no spantree msti 2 
sw8 (6860-B) -> no spantree msti 2 
 
sw5 (6360-A) -> write memory 
sw7 (6870-A) -> write memory 
sw8 (6860-B) -> write memory

<<<PAGE 150>>>
M U LT I P L E  V L A N  R E G I S T R AT I O N  P R O TO C O L ( M V R P )
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 151>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Learn the MVRP Basics
• Implement MVRP in the OmniSwitches

<<<PAGE 152>>>
OVERVIEW
• MVRP 
• IEEE 802.1ak
• Implements the MRP Protocol
• Multiple Vlan Registration Protocol
• Controls and signals dynamic VLAN registration entries across the bridged network
• Close to the GVRP protocol
• Standards-based Layer 2 network protocol
• Re-declaration during topology change (only for affected VLANs)
• Flushing of learnt attributes during topology change

<<<PAGE 153>>>
DESCRIPTION
• Declarations & registrations follow the path 
defined by STP topology
• Once a port receives a MVRP PDU
• Becomes a member of the advertised VLAN
• Shares all information in the PDU with all switches 
participating in MVRP in the switching network by 
propagating/transmitting out of other forwarding ports in 
that STP instance
• MVRP sends one PDU that includes the state of 
all 4094 VLANs on a port
• MVRP VLAN advertisement can be triggered by 
group mobility VLANs
• MVRP also includes the transmission of a TCN for 
individual VLANs
VLAN10
VLAN11
VLAN10
VLAN11
•Static VLAN
•Dynamic  VLAN (GVRP/ MVRP)
•.1q
VLAN10
VLAN11
•TCN, VLAN11

<<<PAGE 154>>>
CLI CONFIGURATION
• MVRP is supported only in STP flat mode
• Enables/Disables MVRP on a switch globally
• Enables or disables MVRP on specific ports on the switch
• Enables or disables MVRP on specific aggregates on the switch
• Configures the maximum number of dynamic VLANs that can be created by MVRP. 
• Configures the MVRP registration mode for specific ports or aggregates.
-> mvrp {enable | disable}
-> mvrp port chassis/slot/port[–port2] {enable | disable}
-> mvrp linkagg agg_id[-agg_id2] {enable | disable}
-> mvrp maximum-vlan vlan_limit
-> mvrp {port chassis/slot/port[– port2] | linkagg agg_id[-agg_id2]} registration {normal | fixed | forbidden}

<<<PAGE 155>>>
CLI CONFIGURATION
• Configures the applicant mode of specific ports on the switch. The applicant mode 
determines whether MVRP PDU exchanges are allowed on a port depending on the Spanning 
Tree state of the port
-> mvrp {port chassis/slot/port[–port2] | linkagg agg_id[-agg_id2]} applicant {participant | non-participant | active}

<<<PAGE 156>>>
CLI CONFIGURATION
MVRP Timers
• mvrp timer join
* The valid range is 250 milliseconds to 1073741773 milliseconds.
• mvrp timer leave
* The valid range is 750 milliseconds to 2147483647 milliseconds.
• mvrp timer leaveall
* The valid range is 750 milliseconds to 2147483647 milliseconds.
• mvrp timer periodic-timer
* The valid range is 1 to 2147483647 milliseconds
-> mvrp {port chassis/slot/port[–port2] | linkagg agg_id[-agg_id2]} 
timer join timer_value
-> mvrp {port chassis/slot/port[–port2] | linkagg agg_id[-agg_id2]} 
timer leave timer_value
-> mvrp {port chassis/slot/port[–port2] | linkagg agg_id[-agg_id2]} 
timer leaveall timer_value
-> mvrp {port chassis/slot/port[–port2] | linkagg agg_id[-agg_id2]} 
timer periodic-timer timer_value

<<<PAGE 157>>>
CLI MONITORING
Summary of the commands used for verifying the MVRP configuration

<<<PAGE 158>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 159>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Multiple VLAN Registration Protocol 
How to 
✓ This lab is designed to familiarize you with the MVRP feature and learn 
how to configure it through the CLI. 
Contents 
1 
Topology ........................................................................................ 2 
2 
Use MVRP ....................................................................................... 3 
2.1. Configure the maximum number of VLANs ...................................................... 3 
2.2. Create some dynamic VLANs ...................................................................... 3 
2.3. Delete VLAN ......................................................................................... 5 
2.4. Revert to 1x1 RSTP mode ......................................................................... 6

<<<PAGE 160>>>
2 
Multiple VLAN Registration Protocol 
 
 1 
Topology 
 
 
MVRP has to be globally enabled on a switch before it can start forwarding MVRP frames.  
In order to have MVRP enabled, switch must be in spanning-tree flat mode. 
 
 
- At this step our network is configure with STP 1x1, but to enable MVRP we must be in flat mode.  
- To configure STP flat mode type: 
sw7 (6870-A) -> spantree mode flat 
sw8 (6860-B) -> spantree mode flat 
sw5 (6360-A) -> spantree mode flat 
- To enable MVRP type: 
all -> mvrp enable 
 
 
Tips 
MVRP can be enabled on ports regardless of whether it is globally enabled or not. However, for the port to 
become an active participant, MVRP must be globally enabled on the switch. By default, MVRP is disabled on 
the ports. To enable MVRP on a specified port, use the mvrp port command 
 
- Enable MVRP on trunk links of all switches: 
sw5 (6360-A) -> mvrp linkagg 7 enable 
sw5 (6360-A) -> mvrp port 2/1/3 enable 
 
sw7 (6870-A) -> mvrp linkagg 7 enable 
sw7 (6870-A) -> mvrp linkagg 78 enable 
 
sw8 (6860-B) -> mvrp port 1/1/3 enable 
sw8 (6860-B) -> mvrp linkagg 78 enable 
 
 
Notes 
MVRP can be configured only on fixed, 802.1 Q and aggregate ports. It cannot be configured on mirror, unp, 
VPLS Access, and VLAN Stacking User ports.

<<<PAGE 161>>>
3 
Multiple VLAN Registration Protocol 
 
 2 
Use MVRP 
2.1. 
Configure the maximum number of VLANs 
A switch can create dynamic VLANs using MVRP. By default, the maximum number of dynamic VLANs that 
can be created using MVRP is 256. If the VLAN limit to be set is less than the current number of dynamically 
learned VLANs, then the new configuration will take effect only after the MVRP is disabled and enabled 
again on the switch. If this operation is not done, the VLANs learned earlier are maintained. 
 
- To modify the maximum number of dynamic VLANs the switch is allowed to create, use the command: 
sw5 (6360-A) -> mvrp maximum-vlan 150 
sw7 (6870-A) -> mvrp maximum-vlan 150 
sw8 (6860-B) -> mvrp maximum-vlan 150 
2.2. 
Create some dynamic VLANs 
- On 6360-A, create a new VLAN 40 : 
 
sw5 (6360-A) -> vlan 40 
sw5 (6360-A) -> vlan 40 members linkagg 7 tagged 
sw5 (6360-A) -> vlan 40 members port 2/1/3 tagged 
 
- Now let’s have a look on the information on the 6870-A and 6860-B : 
 
sw7 (6870-A) -> show mvrp linkagg 7 statistics 
Aggregate ID 7: 
  New Received               : 22, 
  Join In Received           : 40, 
  Join Empty Received        : 156, 
  Leave Received             : 0, 
  In Received                : 0, 
  Empty Received             : 162820, 
  Leave All Received         : 1, 
  New Transmitted            : 20, 
  Join In Transmitted        : 47, 
  Join Empty Transmitted     : 192, 
  Leave Transmitted          : 0, 
  In Transmitted             : 0, 
  Empty Transmitted          : 188111, 
  LeaveAll Transmitted       : 0, 
  Failed Registrations       : 66, 
  Total Mrp PDU Received     : 42, 
  Total Mrp PDU Transmitted  : 46, 
  Total Mrp Msgs Received    : 654, 
  Total Mrp Msgs Transmitted : 1239, 
  Invalid Msgs Received      : 0 
 
sw8 (6860-B) -> show mvrp port 1/1/3 statistics 
Port 1/1/3: 
  New Received               : 2, 
  Join In Received           : 50, 
  Join Empty Received        : 124, 
  Leave Received             : 0, 
  In Received                : 0, 
  Empty Received             : 111328, 
  Leave All Received         : 1, 
  New Transmitted            : 22, 
  Join In Transmitted        : 48, 
  Join Empty Transmitted     : 124, 
  Leave Transmitted          : 0, 
  In Transmitted             : 0, 
  Empty Transmitted          : 147226, 
  LeaveAll Transmitted       : 0, 
  Failed Registrations       : 48,

<<<PAGE 162>>>
4 
Multiple VLAN Registration Protocol 
 
  Total Mrp PDU Received     : 29, 
  Total Mrp PDU Transmitted  : 36, 
  Total Mrp Msgs Received    : 528, 
  Total Mrp Msgs Transmitted : 981, 
  Invalid Msgs Received      : 0 
 
- Look at the port configuration : 
 
sw7 (6870-A) -> show mvrp linkagg 7 
MVRP Enabled          : yes, 
Registrar Mode        : normal, 
Applicant Mode        : active, 
Join Timer (msec)     : 600, 
Leave Timer (msec)    : 1800, 
LeaveAll Timer (msec) : 30000, 
Periodic Timer (sec)  : 1, 
Periodic Tx status    : disabled 
 
sw7 (6870-A) -> show mvrp linkagg 7 last-pdu-origin 
Port      Last-PDU Origin 
-------+-------------------- 
 0/7      94:24:e1:7c:75:f3 
 
- Notice that VLAN 40 has been automatically created : 
sw7 (6870-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Ena   Dis    1500    VLAN 1 
20     std       Ena     Ena   Ena    1500    VLAN 20 
30     std       Ena     Ena   Dis    1500    VLAN 30 
40     dyn       Ena     Ena   Dis    1500    VLAN 40 
57     std       Ena     Ena   Dis    1500    VLAN 57 
58     dyn       Ena     Ena   Dis    1500    VLAN 58 
217    std       Ena     Ena   Ena    1500    VLAN 217 
250    pvlan-p   Ena     Dis   Dis    1500    PVLAN 250 
251    pvlan-c   Ena     Dis   Dis    1500    PVLAN 251 
252    pvlan-i   Ena     Dis   Dis    1500    PVLAN 252 
278    std       Ena     Ena   Ena    1500    VLAN 278 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
sw8 (6860-B) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Ena   Dis    1500    VLAN 1 
20     std       Ena     Ena   Dis    1500    VLAN 20 
30     std       Ena     Ena   Ena    1500    VLAN 30 
40     dyn       Ena     Dis   Dis    1500    VLAN 40 
57     dyn       Ena     Ena   Dis    1500    VLAN 57 
58     std       Ena     Ena   Dis    1500    VLAN 58 
217    dyn       Ena     Ena   Dis    1500    VLAN 217 
250    pvlan-p   Ena     Dis   Dis    1500    PVLAN 250 
251    pvlan-c   Ena     Dis   Dis    1500    PVLAN 251 
252    pvlan-i   Ena     Dis   Dis    1500    PVLAN 252 
278    std       Ena     Ena   Ena    1500    VLAN 278 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
 
Notes 
The VLAN type is then Dynamic 
 
 
 
- And those ports have been dynamically tagged: 
 
sw7 (6870-A) -> show vlan 40 members 
   port      type        status 
----------+-----------+---------------

<<<PAGE 163>>>
5 
Multiple VLAN Registration Protocol 
 
  0/7       dynamic      forwarding 
  0/78      dynamic      forwarding 
 
sw8 (6860-B) -> show vlan 40 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/3       dynamic      forwarding 
  0/78        dynamic        blocking 
 
 
Notes 
VLAN are automatically created and port tagged, but of course, there’s no ip interface creation nor association 
with MSTI. 
 
2.3. 
Delete VLAN 
 
- Check the status of VLAN 40 on 6360: 
 
sw5 (6360-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Ena   Dis    1500    VLAN 1 
20     std       Ena     Ena   Dis    1500    VLAN 20 
30     std       Ena     Ena   Dis    1500    VLAN 30 
40     std       Ena     Ena   Dis    1500    VLAN 40 
57     std       Ena     Ena   Dis    1500    VLAN 57 
58     std       Ena     Ena   Dis    1500    VLAN 58 
278    dyn       Ena     Ena   Dis    1500    VLAN 278 
4094   vcm       Ena     Ena   Dis    1500    VCM IPC 
- It’s a standard VLAN (comparing with dynamic VLAN on 6860-B and 6870-A). 
 
- Now delete the VLAN 40 on 6360: 
 
sw5 (6360-A) -> no vlan 40 
 
- What happens to it ? Try to enter the command a second time: 
 
sw5 (6360-A) -> no vlan 40 
ERROR: Dynamic vlan 40 cannot be deleted 
 
 
Tips 
The mvrp status is equal to the dyn. That means the VLAN 40 has been automatically re-created. 
 
- Now disable mvrp on the 3 switches: 
 
sw5 (6360-A) -> mvrp port 2/1/3 disable 
sw5 (6360-A) -> mvrp linkagg 7 disable 
sw7 (6870-A) -> mvrp linkagg 7 disable 
sw7 (6870-A) -> mvrp linkagg 78 disable 
sw8 (6860-B) -> mvrp port 1/1/3 disable 
sw8 (6860-B) -> mvrp linkagg 78 disable 
all -> mvrp disable 
 
 
sw5 (6360-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Ena   Dis    1500    VLAN 1 
20     std       Ena     Ena   Dis    1500    VLAN 20 
30     std       Ena     Ena   Dis    1500    VLAN 30 
57     std       Ena     Ena   Dis    1500    VLAN 57 
58     std       Ena     Ena   Dis    1500    VLAN 58

<<<PAGE 164>>>
6 
Multiple VLAN Registration Protocol 
 
4094   vcm       Ena     Ena   Dis    1500    VCM IPC 
 
- The VLAN 40 has now disappeared as mvrp is disabled. 
2.4. 
Revert to 1x1 RSTP mode 
- For the next lab, it will be easier to continue with per-vlan STP : 
sw5 (6360-A) -> spantree mode per-vlan 
sw7 (6870-A) -> spantree mode per-vlan 
sw8 (6860-B) -> spantree mode per-vlan

<<<PAGE 165>>>
CONSISTENT AOS NETWORK SECURITY
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 166>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand and implement the following
features
- DOS Protection
- UDP Relay
- Authentication Trap Mode 
- ARP poisoning
- Port Mapping
- Storm Control
- Learned Port Security

<<<PAGE 167>>>
DOS PROTECTION

<<<PAGE 168>>>
DOS FILTERING
• Ability to filter the following DoS attacks
• Ping of Death, SYN attack, Land attack, Teardrop, Bonk, Boink, Pepsi
• Detect ARP flooding
• QoS rate-limits ARP packets to the CPU
• Detect any packet with invalid source or destination IP address
• A packet matching specific criteria well be marked at “Invalid-IP”
• Detect Multicast IP and MAC address mismatch
• Detect Ping overload
• System measures the rate of ICMP requests received over a period of 5 seconds,
and detects a DoS attack if the measured rate exceeds 100 pkts/sec
• Detect packets received with a source address of 127.0.0.1
• Traps can be configured or QM can be used to Quarantine device
• Ability to detect port scanning based on packet thresholds

<<<PAGE 169>>>
UDP RELAY

<<<PAGE 170>>>
GENERIC UDP PORT RELAY
• To enable UDP Relay for a specified UDP service ports
• To support for service name and custom ports
• To specify a VLAN on which traffic destined for the specified UDP service port is forwarded
• To specify the UDP server IP address to which traffic destined for a UDP port is forwarded 
as unicast packets.
-> ip udp relay port port_num [description description]
-> ip udp relay service {tftp | tacacs | ntp | nbns | nbdd | dns} [description description]
-> ip udp relay {service {tftp | tacacs | ntp | nbns | nbdd | dns} | port port_num
[description description]} vlan vlan_id[-vlan_id2]
-> ip udp relay {service {tftp | tacacs | ntp | nbns | nbdd | dns} | port port_num
[description description]} address ip_address

<<<PAGE 171>>>
GENERIC UDP PORT RELAY
• To display the generic UDP relay service configuration
• To display the current statistics for each UDP port relay service. 
-> show ip udp relay [service {tftp | tacacs | ntp | nbns | nbdd | dns} | port port_num]
-> show ip udp relay statistics [service {tftp | tacacs | ntp | nbns | nbdd | dns}] 
[port [port_num]]
-> show ip udp relay
Service Name         Port   IP Address       Vlans
Services
---------------------+------+--------------+---------+---------
DNS port                 53                     20
TFTP port                69
-> show ip udp relay statistics
Port   Service        Pkts Recvd
Pkts Sent   Dst Vlan/IP Address    Svc
-----+--------------+---------------+-----------+----------------------+------
53 DNS port                  0          0             20
69 TFTP port                 0

<<<PAGE 172>>>
AUTHENTICATION TRAP MODE

<<<PAGE 173>>>
AUTHENTICATION TRAP MODE 
• The OmniSwitch can be configured to send both a standard and private authentication 
trap. 
• If mode is set to standard (default): only the standard authenticationFailure notification will be sent.
• If mode is set to private: only alaAuthenticationFailure notification failure will be sent.
• If mode is set to both: authenticationFailure and alaAuthenticationFailure notifications will be sent.
• The alaAuthenticationFailure includes the IP address of the client causing the 
authentication failure.
• The following CLI command is associated with this feature:
snmp authentication-trap mode {standard | private | both}

<<<PAGE 174>>>
ARP

<<<PAGE 175>>>
ARP DEFENSE MECHANISM
• Prevents the CPU from receiving multiple unresolved next hop requests
• Creates a drop-entry as soon as it attempts to resolve an ARP for the purpose
of forwarding traffic
• The entry is removed either
when the ARP is resolved,
or 
after 12 attempts have been made, once every 5 secs. (~1 minute)
• Duplicate request received during the time the switch is attempting to resolve the ARP is 
dropped
• Avoids CPU utilization climb and destabilizing the switch while next-hop is being resolved

<<<PAGE 176>>>
ARP POISONING DETECTION
• Detects the presence of a ARP-Poisoning host on the network
• Identifies unsolicited ARP Replies from an attacker, false ARP requests and unsolicited 
ARP replies
• Sends out ARP Requests for certain configurable restricted addresses and its own interface 
addresses
• Reply to all ARP Requests for its IP Interface address, but will not learn the ARP mapping of the 
source from such packets
• ARP Reply will be accepted only if the Switch had originated a corresponding ARP Request
• Logs the event and send a trap 
ARP Poisoning Examples
MAC Flooding
Man in the middle
Impersonation
1. ARP Poisoning by a host that 
replies to all ARP Requests
2. ARP Requests from an Attacker
3. Unsolicited ARP Replies from an 
Attacker
THU JAN 24 16:34:38 : NS (123) alert message:
+++ +++++++++++++++++++++++++++++++++++++++++++++++
+++ ARPADDRESSSCAN source detected on 1/7...
+++   Trigger Operation...
+++     Interval    Count     Sensitivity
+++   ---------------------------------------------
+++            5        5              50
+++   Traffic Statistics...
+++     Packet-Type    Direction   Count
+++   ---------------------------------------------
+++     ARP_REP        OUT             0
+++     ARP_REQ        IN             71
+++ +++++++++++++++++++++++++++++++++++++++++++++++

<<<PAGE 177>>>
ARP POISONING DETECTION
• Adding  an ARP Poison restricted address
• Maximum of two IP addresses per IP interface
• Displaying the number of attacks detected for configured ARP poison restricted-addresses
-> show ip dos arp-poison
IP Address Attacks
Attacks
--------------------+-----------
192.168.1.1 0
0
192.168.1.2 0
0
192.168.60.100
2
WED JAN 30 16:15:35 : IP (15) info message:
+++ 1/0 ARP poisoning REPLY from 192.168.60.100.
-> ip dos arp-poison restricted-address 192.168.100.152
-> show ip dos arp-poison

<<<PAGE 178>>>
ADDRESS RESOLUTION PROTOCOL (ARP)
• The switch stores the hardware address in its ARP cache (ARP table) 
• The table contains a list of IP addresses and their corresponding MAC addresses 
• Entries in the table are used to translate 32-bit IP addresses into 48-bit Ethernet or IEEE 
802.3 hardware addresses
• Dynamic addresses remain in the table until they time out (Default 300 sec.)
• Static entries are permanent and are created using the IP address of the entry followed by 
its physical (MAC) address
• Use the alias keyword to specify that the switch will act as an alias (proxy) for this IP 
address. 
-> arp 171.11.1.1 00:05:02:c0:7f:11
-> arp 171.11.1.1 00:05:02:c0:7f:11 alias

<<<PAGE 179>>>
LOCAL PROXY ARP
• Allows the network administrator to configure proxy functionality on the switch
• Enables proxy ARP on a per VLAN basis
• All ARP requests received on VLAN member ports are answered with the MAC address of 
the VLAN’s virtual IP router port
192.168.10.101
192.168.10.102
ARP
Switch A
Switch B
Switch C
ARP
Normal ARP
Local Proxy ARP
PC 2
PC 1
-> ip interface name [address ip_address] [mask subnet_mask] [admin [enable | disable]] [vlan vid] 
[forward | no forward] [local-proxy-arp | no local-proxy-arp] [eth2 | snap] [primary | no primary]

<<<PAGE 180>>>
PROXY ARP FILTERING
• Extended Proxy ARP Filtering
• Blocks the switch from providing ARP replies for the specified IP address(es).
• It is generally used in conjunction with the Local proxy ARP application
• By default, no ARP filters exist in the switch 
-> arp filter ip_address [mask mask] [vid] [sender | target] [allow | block]
-> arp filter 198.0.0.0 mask 255.0.0.0 sender block
-> show arp filter

<<<PAGE 181>>>
PORT MAPPING
MAC FORCED FORWARDING

<<<PAGE 182>>>
PORT MAPPING
• Goal
• Defining 2 set of ports & controlling the 
communication within each set
• Up to 8 Port Mapping sessions 
• Ports can only belong to a single session - except uni. 
network pts
• Uni-directionnal
• User-port
• no direct user-to-user traffic
• only user-to-network
• Network-port
• network-to-user & network-to-network 
• Bi-directional
• User-port
• no direct user-to-user traffic
• only user-to-network
• Network-port
• no direct network-to-network traffic
• only network-to-user
1/3/1
1/3/2
1/3/3
1/3/4
2/1/16
2/1/17
Port Mapping Session 1
User
Ports
Network
Ports

<<<PAGE 183>>>
PORT MAPPING
• Creating a Mapping Session
• Enables, disables a port mapping session
• Creates a port mapping session with the user ports,
network ports, or both user ports and network ports
• Displaying the status of one or more port mapping sessions
• Displaying the configuration of one or more port mapping sessions
Examples
-> port-mapping 3 user-port 1/2/3 network-port 1/6/4 
-> port-mapping 4 user-port 1/2/5-8
-> port-mapping 5 user-port 1/2/3 network-port slot 3
-> port-mapping session_id [user-port {slot chassis/slot | chassis/slot/port[-port2] | linkagg agg_id}] 
[network-port {slot chassis/slot | chassis/slot/port[-port2] | linkagg agg_id}]
-> port-mapping session_id {enable | disable} 
-> port-mapping session_id [user-port {slot chassis/slot | chassis/slot/port[-port2] | linkagg agg_id}] 
[network-port {slot chassis/slot | chassis/slot/port[-port2] | linkagg agg_id}] 
-> show port-mapping [session_id] status
-> show port-mapping [session_id]

<<<PAGE 184>>>
MAC FORCED FORWARDING

<<<PAGE 185>>>
MAC FORCED FORWARDING
• Described in RFC 4562
• Control unwanted broadcast traffic and host-to-host 
communication
• Implements an ARP proxy function that
• Prohibits MAC address resolution between hosts located 
within the same subnet but at different customer 
premises
• In effect directs all upstream traffic to an IP gateway 
providing IP connectivity between these same hosts
• Dynamic Proxy ARP  uses:
• Port Mapping
• DHCP snooping
• Local proxy ARP
• Description
• Once a DHCP lease is offered to a L2 client, stores the 
router IP advertised in the DHCP ACK
• An ARP reply with the access router @MAC is sent for all 
subsequent ARP requests to the access router or to any 
other IPs in the same VLAN/subnet
DHCP Server
Aggregation
Access Router
Port Mapping
User/network ports
IP1-MAC1 mapping
Proxy ARP: MAC1
IP1-MAC1 mapping
Proxy ARP: MAC1
2 - ARP Reply
IP1 is MAC1
1- DHCP ACK – option 3
Router IP/Gateway = IP1
IP1 - MAC1
IPA 
MACA
IPB 
MACB
ARP cache
IPB -> MAC1
ARP cache
IPA -> MAC1
Subnet 
10.0.0.0/8

<<<PAGE 186>>>
MAC FORCED FORWARDING - CLI/WEBVIEW
-> port-mapping 1 user-port 1/1/1-2 network-port linkagg 8
-> port-mapping 1 dynamic-proxy-arp enable
-> dhcp-snooping vlan 20 admin-state enable 
-> port-mapping 1 enable
-> show port-mapping
SessionID
USR-PORT        NETWORK-PORT
-----------+----------------+------------------
1          1/1/1           0/8
1          1/1/2
-> show port-mapping status
SessionID
Direction       Status     Unknown Unicast    DPA Status
------------+-----------------+----------+------------------+------------
1           bi            enable      flood              enable
-> show ip dynamic-proxy-arp
Router IP            Vlan              Mac-Address         Port
-----------------+----------------+-------------------+------------------

<<<PAGE 187>>>
STORM CONTROL

<<<PAGE 188>>>
STORM CONTROL
• Configures the flood rate settings on a single port, a range of ports, or an entire Network 
Interface (NI)
• Configures the action on a single port, a range of ports, when the port reaches the storm 
violated state
• Refer to specification guide for the supported platform 
-> interfaces {slot chassis/slot| port chassis/slot/port[-port2]} flood-limit {bcast | mcast | uucast | all} rate 
{pps pps_num| mbps mbps_num | cap% cap_num | enable | disable | default} [low-threshold low_num]
interfaces {slot chassis/slot| port chassis/slot/port[-port2]} flood-limit {bcast | mcast | uucast | all} action
{shutdown | trap | default}

<<<PAGE 189>>>
LEARNED PORT SECURITY

<<<PAGE 190>>>
LEARNED PORT SECURITY 
• Mechanism for controlling network device access on one or more switch ports
• Limit the amount of time source learning occurs on all LPS ports
• Limit the max number of L2 addresses that can be learned on a port. (Dynamic or Static)
• Limit the L2 address learning for the specific period of time
• Supported on Fixed, Mobile, 802.1Q tagged, Authenticated, 802.1X
• Not supported on Link Aggregate ports
• Violation options
• Block only traffic that violates LPS port restrictions 
•
-> authorized traffic is forwarded on the port
• Shutdown the port 
• Steps to Configuring LPS:
• Enable LPS on a port
• Set the number of learned Mac’s
• Set the time limit for LPS
• Select the violation mode
MAC Limit
Or
MAC List
MAC-1
MAC-2

<<<PAGE 191>>>
LEARNED PORT SECURITY - CONFIGURATION
• Configuring LPS on a port
• Disables all learning on the port. Existing MAC addresses are retained but no additional learning of 
addresses, except for static MAC addresses, is allowed
• Disabling LPS on a port
• In case of violation, two possible actions can be taken: filtering or shutdown
• Shutdown. Stops all traffic on a port after violation
• Filtering. Only stops traffic from violating device
-> port-security port {chassis/slot/port[-port2] } [admin-state {enable | disable | locked}] 
-> no port-security port <chassis/slot/port>
-> port-security port <chassis/slot/port> violation [shutdown | restrict/ discard]

<<<PAGE 192>>>
LEARNED PORT SECURITY
• Specifying the maximum number of source MAC addresses that an LPS port is allowed to 
learn.
• Configures the amount of time, in minutes, to allow source learning on all LPS ports. 
• Configuring the maximum number of filtered MAC addresses that can be learned on the LPS 
port(s)
• Maximum number of mac address allowed is 1
• Maximum number of mac addresses filtered is 5
• Default violation is restricted
-> port-security port chassis/slot/port[-port2] max-filtering
-> port-security learning-window minutes
-> port-security {port chassis/slot/port[-port2] | sap {port | linkagg} sap_id} max-
filtering number

<<<PAGE 193>>>
LEARNED PORT SECURITY
• Configuring of a list of authorized source MAC addresses
• up to eight MAC ranges per port.
• Converting the dynamically learned MAC addresses on the LPS port(s) to static MAC 
addresses
• The following set of commands enables LPS on port 1/1/1, converting dynamically learned 
MAC address of currently attached device to static. When another device is connected to 
port 1/1, a violation occurs and this port will be shutdown
-> port-security port chassis/slot/port[-port2] mac-range [low mac_address | high mac_address]
-> port-security {port chassis/slot/port[-port2] | chassis} convert-to-static
-> port-security port 1/1/1 admin-state enable
-> port-security port 1/1/1 maximum 1 
-> port-security port 1/1/1 violation shutdown
-> port-security port 1/1/1 convert-to-static enable

<<<PAGE 194>>>
LEARNED PORT SECURITY
• Displays Learned Port Security configuration and table entries
• Clears all port violations on the switch for the given port
-> show port-security
Port                     : 1/1/15
Operation Mode           : DISABLED,
Max Bridged MAC allowed  : 1,
Max Filtered MAC allowed : 5,
Low End of MAC Range     : 00:00:00:00:00:00,
High End of MAC Range    : ff:ff:ff:ff:ff:ff,
Violation Setting        : RESTRICT,
MAC 
VLAN     MAC TYPE
-------------------+------+-------------------
00:20:95:00:fa:5c     1       STATIC
-> clear violation port { chassis/slot/port[-port2] | linkagg agg_id[-agg_id2]}

<<<PAGE 195>>>
LEARNED PORT SECURITY - L2 NOTIFICATION 
• Provides notification of newly learned bridged MAC addresses after the port matches the 
specified threshold amount 
• Sends a trap for every MAC learned after the threshold is reached. It contains:
• MAC address
• Slot/Port
• VLAN
• Date & Time
-> port-security port chassis/slot/port[-port2] learn-trap-threshold number

<<<PAGE 196>>>
LEARNED PORT SECURITY
Packet loss due to LPS port learning
• Objective 
• Avoids packet loss due to LPS port learning by reinjecting the packets received from clients back to 
the forwarding path of the switch.
• Hence by default all the packets trapped on LPS port will be reinjected back to the switch once the MAC is 
successfully learned. 
• Can also be customized to filter and inject packets matching specific protocol types or UDP source 
and destination ports.
[no] port-security [port <c/s/p1[-p2]>] pkt-relay Enables packet relay feature on a single or range of LPS ports.
port-security pkt-relay protocol {udp}|{icmp} |{igmp} Configures the protocol filter criteria for packet relay feature.
port-security pkt-relay protocol {udp [src-port <port1[-port2]>]} Configures the UDP source ports as the criteria for packet relay.
port-security pkt-relay protocol {udp [dst-port <port1[-port2]>]} Configures the UDP destination ports as the criteria for packet relay.
show port-security port
Displays the packet relay configuration on the port.lost in LPS. If the packet should be allowed. it must be re-injected 
into the forwarding path, currently, it is discarded.

<<<PAGE 197>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 198>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Port Mapping 
How to 
✓ This lab is designed to familiarize you with the concept of Port Mapping. 
Contents 
1 
Topology ........................................................................................ 2 
2 
Bi-Directional Port-Mapping ................................................................. 3 
2.1. Prerequisites configuration ....................................................................... 3 
2.2. Manage port mapping .............................................................................. 5 
3 
Configuring Multiple ports ................................................................... 5 
4 
Remove management ......................................................................... 6 
5 
Summary ........................................................................................ 6

<<<PAGE 199>>>
2 
Port Mapping 
 
 1 
Topology 
Port Mapping is a security feature, which controls communication between peer users. Each session comprises 
a session ID, a set of user ports, and/or a set of network ports. The user ports within a session cannot 
communicate with each other and can only communicate via network ports.  
 
A port mapping session can be configured in the unidirectional or bidirectional mode. In the unidirectional 
mode, the network ports can communicate with each other within the session. In the bidirectional mode, the 
network ports cannot communicate with each other. Network ports of a unidirectional port mapping session 
can be shared with other unidirectional sessions but cannot be shared with any sessions configured in the 
bidirectional mode.

<<<PAGE 200>>>
3 
Port Mapping 
 
 2 
Bi-Directional Port-Mapping 
2.1. 
Prerequisites configuration 
Manage a VLAN 50 on 6870-A, 6860-B and 6360-A. 
sw5 (6360-A) -> vlan 50 
sw7 (6870-A) -> vlan 50 
sw8 (6860-B) -> vlan 50 
 
Configure an IP interface for VLAN 50 on all switches in the 192.168.50.X/24 subnet replacing the 'X' with 
your switch number 
sw5 (6360-A) -> ip interface int_50 address 192.168.50.5/24 vlan 50 
sw7 (6870-A) -> ip interface int_50 address 192.168.50.7/24 vlan 50 
sw8 (6860-B) -> ip interface int_50 address 192.168.50.8/24 vlan 50 
 
Tag the vlan 50 on the linkagg 7 on 6360-A and 6870-A 
sw5 (6360-A) -> vlan 50 members linkagg 7 tagged 
sw7 (6870-A) -> vlan 50 members linkagg 7 tagged 
 
Tag vlan 50 on port 2/1/3 on 6360-A and port 1/1/3 on 6860-B 
sw5 (6360-A) -> vlan 50 members port 2/1/3 tagged 
sw8 (6860-B) -> vlan 50 members port 1/1/3 tagged 
 
Check your management 
sw5 (6360-A) -> show vlan 50 members 
   port      type        status 
----------+-----------+--------------- 
  2/1/3      tagged      forwarding 
  0/7        tagged      forwarding 
 
sw7 (6870-A) -> show vlan 50 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        tagged      forwarding 
 
sw8 (6860-B) -> show vlan 50 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/3      tagged      forwarding 
 
sw5 (6360-A) -> show ip interface 
Total 3 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_50                           192.168.50.5    255.255.255.0       UP     YES vlan 50 
 
sw7 (6870-A) ->  show ip interface 
Total 6 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.7      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_20                           192.168.20.7    255.255.255.0       UP     YES vlan 20 
int_278                          172.16.78.7     255.255.255.0       UP     YES vlan 278 
int_50                           192.168.50.7    255.255.255.0       UP     YES vlan 50

<<<PAGE 201>>>
4 
Port Mapping 
 
sw8 (6860-B) -> show ip interface 
Total 5 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.8       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_278                          172.16.78.8     255.255.255.0       UP     YES vlan 278 
int_30                           192.168.30.8    255.255.255.0       UP     YES vlan 30 
int_50                           192.168.50.8    255.255.255.0       UP     YES vlan 50 
 
Manage ports 1/1/1 and 1/1/2 on 6360-A as default to VLAN 50. 
sw5 (6360-A) -> vlan 50 members port 1/1/1-2 untagged 
 
sw5 (6360-A) -> show vlan 50 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      default        inactive 
  1/1/2      default        inactive 
  2/1/3      tagged      forwarding 
  0/7        tagged      forwarding 
 
sw5 (6360-A) -> interface 1/1/1-2 admin-state enable 
 
sw5 (6360-A) -> show vlan 50 members 
 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      default      forwarding 
  1/1/2      default      forwarding 
  2/1/3      tagged      forwarding 
  0/7        tagged      forwarding 
 
Manage Client 5 and Client 9 PC as following 
Client 5 
Client 9 
IP address: 192.168.50.105 
IP address: 192.168.50.109 
Subnet mask: 255.255.255.0 
Subnet mask: 255.255.255.0 
Default Gateway: 192.168.50.5 
Default Gateway: 192.168.50.5 
 
Ensure you can ping all IP interfaces from the clients PC  
From client 5 and client 9, ping 192.168.50.5, 192.168.50.7 and 192.168.50.8

<<<PAGE 202>>>
5 
Port Mapping 
 
2.2. 
Manage port mapping 
Check port mapping configuration on 6360-A 
sw5 (6360-A) -> show port-mapping 
 
SessionID       USR-PORT        NETWORK-PORT 
-----------+----------------+------------------ 
 
Create a first session which will map the linkagg 7 
sw5 (6360-A) -> port-mapping 1 user-port 1/1/1 network-port linkagg 7 
sw5 (6360-A) -> port-mapping 1 enable 
 
From client PC on port 1/1/1, ping both remote switches.  
You should find that you can only ping 6870-A as it is the one at the remote end of linkagg 7.  
 
Create a second session which will map port 1/1/2 to port 2/1/3: 
sw5 (6360-A) -> port-mapping 2 user-port 1/1/2 network-port 2/1/3 
sw5 (6360-A) -> port-mapping 2 enable 
 
From client 9   on port 1/1/2. You should now be able to ping 6860-B but not 6870-A.  
 3 
Configuring Multiple ports 
Ports can be added to existing mapping session 
sw5 (6360-A) -> show port-mapping 
SessionID       USR-PORT        NETWORK-PORT 
-----------+----------------+------------------ 
     1          1/1/1           0/7 
     2          1/1/2           2/1/3 
 
sw5 (6360-A) -> port-mapping 1 user-port 2/1/1 
sw5 (6360-A) -> show port-mapping 
 
SessionID       USR-PORT        NETWORK-PORT 
-----------+----------------+------------------ 
     1          1/1/1           0/7 
     1          2/1/1 
     2          1/1/2           2/1/3 
 
sw5 (6360-A) -> port-mapping 2 user-port 2/1/2 
 
sw5 (6360-A) -> show port-mapping 
SessionID       USR-PORT        NETWORK-PORT 
-----------+----------------+------------------ 
     1          1/1/1           0/7 
     1          2/1/1 
     2          1/1/2           2/1/3 
     2          2/1/2 
 
A port can only be a member of one mapping session: 
sw5 (6360-A) -> port-mapping 2 user-port 2/1/1 
ERROR: port user already part of an existing PMAP session

<<<PAGE 203>>>
6 
Port Mapping 
 
 4 
Remove management 
sw5 (6360-A) -> no port-mapping 1 
sw5 (6360-A) -> no port-mapping 2 
sw5 (6360-A) -> no ip interface int_50 
sw5 (6360-A) -> no vlan 50 
 
sw7 (6870-A) -> no vlan 50 
sw7 (6870-A) -> no ip interface int_50 
 
sw8 (6860-B) -> no vlan 50 
sw8 (6860-B) -> no ip interface int_50 
 5 
Summary 
Port Mapping is a security feature, which controls communication between peer users. Each session comprises 
a session ID, a set of user ports, and/or a set of network ports. The user ports within a session cannot 
communicate with each other and can only communicate via network ports.

<<<PAGE 204>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Learned Port Security 
How to 
✓ This lab is designed to familiarize yourself with Learned Port Security 
feature. 
Contents 
1 
Topology ........................................................................................ 2 
2 
Learned Port Security ........................................................................ 4 
2.1. Configure the switch to learn maximum one mac address ................................... 4 
2.2. Configure the switch port to accept the traffic only from currently attached device ... 5 
2.3. Port violation........................................................................................ 6

<<<PAGE 205>>>
2 
Learned Port Security 
 
 1 
Topology 
The LPS feature is used in networks to prevent employees to use small basic switches or hub in the enterprise 
network. This can grandly help IT stuff to efficiently manage network security. 
Learned Port Security provides controls over the source learning function on an OmniSwitch.   
 
- 
On the 6860B, create client VLAN and assign interfaces 
 
sw8 (6860-B) -> vlan 180 
sw8 (6860-B) -> ip interface int_180 address 192.168.180.8/24 vlan 180 
- 
On the 6860-B, assign port 1/1/8 and 1/1/1 to vlan 180 and activate the interfaces: 
 
sw8 (6860-B) -> vlan 180 members port 1/1/1 untagged 
sw8 (6860-B) -> vlan 180 members port 1/1/8 untagged 
sw8 (6860-B) -> interfaces 1/1/1 admin-state enable 
sw8 (6860-B) -> interfaces 1/1/8 admin-state enable 
- 
Start client 8 and configure as below: 
Client 8: 
IP address = 192.168.180.58 
Subnet mask = 255.255.255.0 
 
- 
On the 6560-A, activate the interfaces 1/1/1 and 1/1/8, and assign an IP address to VLAN 1: 
 
sw3 (6560-A) -> interfaces 1/1/1 admin-state enable 
sw3 (6560-A) -> interfaces 1/1/8 admin-state enable 
sw3 (6560-A) -> ip interface int_1 address 192.168.180.3/24 vlan 1 
sw3 (6560-A) -> vlan 1 members port 1/1/1 untagged 
 
- 
Start client 3 and configure as below: 
Client 3: 
IP address = 192.168.180.53 
Subnet mask = 255.255.255.0 
- 
Try to ping the client (192.168.180.58) from client 3 and 6560-A. 
 
OS6860-B 8
OS6560-A 3
1/1/8
1/1/8
LPS
1/1/1
Client 3
1/1/1
Client 8

<<<PAGE 206>>>
3 
Learned Port Security 
 
- 
On the 6860-B, check the MAC addresses learned on port 1/1/8: 
 
sw8 (6860-B) -> show mac-learning port 1/1/8 
 
 
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
        ID = ISID/Vnid/vplsid 
 
   Domain    Vlan/SrvcId[:ID]           Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+-----------------
-------- 
      VLAN                      180   00:0c:29:44:aa:3b            dynamic     bridging         1/1/8     
      VLAN                      180   2c:fa:a2:95:8f:9f            dynamic     bridging         1/1/8     
      VLAN                      180   2c:fa:a2:95:8f:ad            dynamic     bridging         1/1/8     
 
 Total number of Valid MAC addresses above = 3 
 
Notes 
In this example above, there’s 3 mac addresses: 1 from client 3 and 2 from 6560. The 6560 uses different mac 
addresses for Layer 2 traffic, like LLDP or STP and another one, the chassis base mac address for Layer3 traffic 
associated with VLAN 1 IP interface.

<<<PAGE 207>>>
4 
Learned Port Security 
 
 2 
Learned Port Security 
2.1. 
Configure the switch to learn maximum one mac address 
By default, port security allows the switch to learn only a single MAC address and then binds that MAC 
address to the port. When the number of filtered MAC addresses learned on the port reaches the maximum, 
either the port is disabled (Shutdown Violation mode) or MAC address learning is disabled (Restrict Violation 
mode). By default, MAC address learning is disabled (filtering). When LPS is enabled on switch ports with 
one single mac address, it will prevent users to plug a basic switch or hub to the network, please note that 
you can specify up to 100 mac addresses to be learned per port by LPS. 
 
- 
Enable LPS on port 1/1/8 of 6860-B: 
 
sw8 (6860-B) -> port-security port 1/1/8 admin-state enable 
 
- 
Once again try to ping client 8 from both client 3 and 6560 (it should fail). 
 
- 
Display information about port security and learned mac addresses: 
 
sw8 (6860-B) -> show port-security port 1/1/8 
 
        Mac Address: & = duplicate static address, 
 
 
Port:  1/1/8 
  Admin-State      :                ENABLED, 
  Operation Mode   :                ENABLED, 
  Max MAC bridged  :                      1, 
  Trap Threshold   :               DISABLED, 
  Violation        :               RESTRICT, 
  Max MAC filtered :                      5, 
  Violating MAC    :                   NULL, 
  Pkt-Relay        :               DISABLED 
 
            MAC             VLAN       MAC TYPE          OPERATION 
-------------------------+--------+-----------------+----------------- 
  2c:fa:a2:95:8f:ad          180           dynamic         bridging 
  00:0c:29:44:aa:3b          180           dynamic        filtering 
  2c:fa:a2:95:8f:9f          180           dynamic        filtering 
 
- 
The first mac address seen is normally bridged but the others are filtered. There’s more chance for  
Layer 2 traffic to be bridged than other Layer 3 traffic. 
 
- 
To ensure no Layer2 traffic, disable unnecessary protocols on 6560-A port 1/1/8: 
 
sw3 (6560-A) -> spantree vlan 1 port 1/1/8 disable 
sw3 (6560-A) -> show spantree ports active 
 
sw3 (6560-A) -> lldp all chassis lldpdu disable 
sw3 (6560-A) -> show lldp config 
- To Flush the mac-address from the mac-learning table on the 6860B port 1/1/8 
sw8 (6860-B) -> mac-learning flush vlan 180 port 1/1/8 dynamic

<<<PAGE 208>>>
5 
Learned Port Security 
 
- 
Once again try to ping client 8 from both client 3 and 6560-A 
 
- 
Now it should remain only 2 mac addresses: one from client 3 and another one from the IP interface of 
VLAN 1 in 6560-A. 
 
sw8 (6860-B) -> show mac-learning port 1/1/8 
 
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
        ID = ISID/Vnid/vplsid 
 
   Domain    Vlan/SrvcId[:ID]           Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+-----------------
-------- 
      VLAN                      180   00:0c:29:44:aa:3b            dynamic    filtering     1/1/8         
      VLAN                      180   2c:fa:a2:95:8f:ad            dynamic     bridging     1/1/8   
 
Total number of Valid MAC addresses above = 2      
 
 
Notes 
Here, the Client 3 mac address is bridged, the 6560-A MAC is filtered. Thus we can ping client 8 from client 3 
but not from 6560-A. 
2.2. 
Configure the switch port to accept the traffic only from currently attached device 
 
In order to allow only one dynamically learned mac address on a switch LPS port (only fixe ports), we will 
use convert-to-static parameter with port-security. The currently attached devices mac address will be 
associated to this LPS port and one static entry will be created in mac address table. This means that only 
this device will be allowed on that port. 
Please notice that the device must be learned on the LPS port before to enter the command port-security  
convert-to-static 
- 
To convert the dynamically learned MAC addresses to static addresses on a specific LPS port at any time 
irrespective of the source learning time window, use the port-security convert-to-static command as 
shown below: 
 
sw8 (6860-B) -> port-security port 1/1/8 convert-to-static 
 
- 
Carefully analyze the output of the command shown below, you can see that the currently attached 
device mac address is learned on the specified port and the type of the entry is permanent (static). 
 
sw8 (6860-B) -> show mac-learning port 1/1/8  
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation     Interface 
------------+----------------------+-------------------+------------------+-------------+----------- 
      VLAN                      180   00:50:56:90:ac:77             static     bridging      1/1/8      
      VLAN                      180   2c:fa:a2:aa:34:9f            dynamic    filtering      1/1/8       
                                                                                            
 Total number of Valid MAC addresses above = 2

<<<PAGE 209>>>
6 
Learned Port Security 
 
2.3. 
Port violation 
By default, the port violation is restricted, that means traffic from unallowed mac addresses is filtered. We 
can change it to shutdown, That means port is shutdown if more that one mac address is seen in our case. 
- 
Configure the shutdown of the port in case of violation and indicate the max number of filtered mac 
address to 0 (that means the port will be shutdown if more than 1 mac address is learned on it). 
 
sw8 (6860-B) -> port-security port 1/1/8 violation shutdown 
sw8 (6860-B) -> port-security port 1/1/8 max-filtering 0 
sw8 (6860-B) -> show port-security port 1/1/8 
 
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
 
 
Port:  1/1/8 
  Admin-State      :                ENABLED, 
  Operation Mode   :                ENABLED, 
  Max MAC bridged  :                      1, 
  Trap Threshold   :               DISABLED, 
  Violation        :               SHUTDOWN, 
  Max MAC filtered :                      0, 
  Violating MAC    :                   NULL, 
  Pkt-Relay        :               DISABLED 
 
            MAC             VLAN       MAC TYPE          OPERATION 
-------------------------+--------+-----------------+----------------- 
  00:50:56:90:ac:77          180            static         bridging 
 
 
Notes 
In the example above, the switch mac address age out, so as there’s only the client 3 mac address learnt on the 
port, is still forwarding 
 
- 
Try to ping again client 8 from both client 3 and 6560-A. You should see a warning message on the 6860-
B : 
 
Thu Jan  1 00:28:35 : AGCMM AG-Lps INFO message: 
+++ AGCMM_INFO:(1715.553)lpsPortViolation[554]Port-security Violation on PORT 1/1/8 : Shutting down port 
 
Thu Jan  1 00:28:35 : intfCmm Mgr INFO message: 
+++ Link 1/1/8 operationally down 
 
- 
By default, there’s a timer of 300 seconds to clear automatically the violation 
 
sw8 (6860-B) -> show violation 
* = Link Agg ID 
 LAG ID/                                                     Recovery       Recovery 
 Port       Source         Action            Reason    WTR   Time           Max/Remain 
----------+----------+------------------+-------------+-----+--------------+-------------- 
 1/1/8     AG         admin down          lps shutdown    0     300         10/10

<<<PAGE 210>>>
7 
Learned Port Security 
 
- 
To change this value of 300 seconds, type: 
 
sw8 (6860-B) -> show violation-recovery-configuration port 1/1/8 
Global Violation Trap   : Enabled 
Global Recovery Maximum : 10 
Global Recovery Time    : 300 
 Port       Recovery Max  Recovery Time 
----------+-------------+--------------- 
 1/1/8      10                300 
sw8 (6860-B) -> violation port 1/1/8 recovery-time 30 
sw8 (6860-B) -> show violation-recovery-configuration port 1/1/8 
Global Violation Trap   : Enabled 
Global Recovery Maximum : 10 
Global Recovery Time    : 300 
 Port       Recovery Max  Recovery Time 
----------+-------------+--------------- 
 1/1/8      10                30 
- 
You may also manually recover from a violation: 
 
sw8 (6860-B) -> clear violation port 1/1/8 
 
- 
Finally, to disable port security, enter: 
 
sw8 (6860-B) -> no port-security port 1/1/8 
sw8 (6860-B) -> interfaces 1/1/8 admin-state disable 
 
sw3 (6560-A) -> interfaces 1/1/8 admin-state disable

<<<PAGE 211>>>
IP INTERFACES
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 212>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand and implement the following
features
- IP interfaces
- Loopback0 Interface
- Static routes
- RIP
- Applying an ACL on the EMP port

<<<PAGE 213>>>
IP INTERFACE

<<<PAGE 214>>>
OVERVIEW
• IP is enabled by default on the OmniSwitch switches
• IP forwarding is enabled when at least one IP interface is configured on a VLAN
• IP Interfaces have the following characteristics: 
• The subnet mask can be expressed in dotted decimal notation (255.255.0.0) or with a slash (/) 
followed by the number of bits in the mask (192.168.10.1/24).
• A forwarding router interface sends IP frames to other subnets. A router interface that is not 
forwarding can receive frames from other hosts on the same subnet.
• The first interface bound to a VLAN becomes the primary interface for that VLAN.
• Create a new IP Interface
• Display the list of the IP Interfaces
-> ip interface <int_name> address <ip address/mask> vlan <vlan_id>
-> show ip interface

<<<PAGE 215>>>
LOOPBACK0

<<<PAGE 216>>>
LOOPBACK0
• Goal
• Identify a consistent address for network management purposes
• Not bound to any VLAN
• Always remain operationally active (as long as at least one VLAN is active)
• To identify a Loopback0 interface, enter Loopback0 for the interface name
• Automatically advertised by RIP and OSPF protocols when the interface is created (not by BGP)
• Use
• RP (Rendez-Vous Point) in PIMSM
• sFlow Agent IP address
• Source IP of RADIUS authentication
• NTP Client
• BGP peering
• OSPF router-id
• Switch and Traps Identification from an NMS station (i.e OmniVista)
-> ip interface Loopback0 address 100.10.1.1

<<<PAGE 217>>>
CUSTOM IP INTERFACE/LOOPBACK0 FOR IP SERVICE
• To configure a source IP address as the outgoing IP interface for an IP service
• Any IP interface/ loopback
• In the particular VRF based on an application specific command
[vrf vrf_name] ip service source-ip {Loopback0 | interface_name} [tftp] [telnet] [tacacs] 
[swlog] [ssh] [snmp] [sflow] [radius] [ntp] [ldap] [ftp] [dns] [all]
sw5 (6360-A) -> ip service source-ip loopback0 snmp
sw5 (6360-A) -> show  ip service source-ip
Legend: - no explicit configuration
Application   Interface-name
-------------+--------------------------------
dns
-
ftp           -
ldap
-
ntp
-
radius        -
sflow
-
snmp
Loopback0
ssh
-
swlog
-
tacacs
-
telnet        -
tftp
- -

<<<PAGE 218>>>
STATIC / DYNAMIC ROUTING

<<<PAGE 219>>>
STATIC VS DYNAMIC ROUTING
• Static Routes 
• Entered manually by the network administrator   
• Anytime the network topology changes, administrator must update the routes
• Static routes always have priority over dynamic routes
• Suitable for environments where network traffic is relatively predictable and where network 
design is relatively simple
• Dynamic Routing –( RIP, OSPF, …)
• Allows network to updates routes quickly and automatically without the administrator having to 
configure new routes
• Routing protocols describe
• How to send updates?
• What information is in the updates?
• When to send updates?
• How to locate the recipients of the updates?

<<<PAGE 220>>>
STATIC ROUTES

<<<PAGE 221>>>
STATIC ROUTES - OVERVIEW
• Gateway or NextHop address is mapped to a particular interface on the switch
• Associated interface needs to be up and running 
• By default, static routes have preference over dynamic routes
• Priority can be set by assigning a metric value
-> ip static-route <Destination Network>/<Mask> gateway <host> [METRIC | BFD-STATE | NAME | TAG | NO]

<<<PAGE 222>>>
STATIC ROUTES - CONFIGURATION
• Specify a static route to the destination IP address 134.1.21.0
• Specify a default route
• Configure a default-route metric
• Configure a backup default-route
-> ip static-route 134.1.21.0/24 gateway 10.1.1.1
-> ip static-route 0.0.0.0/0 gateway 10.1.1.1
-> ip static-route 0.0.0.0/0 gateway 1.1.1.1 metric 1
-> ip static-route 0.0.0.0/0 gateway 2.2.2.2 metric 2

<<<PAGE 223>>>
STATIC ROUTES - MONITORING
• Display the IP Router Database
• Display the IP Routes
-> show ip router database 
Legend: + indicates routes in-use
b indicates BFD-enabled static route
i indicates INTERFACE static route
r indicates recursive static route, with following address in brackets
Total IPRM IPv4 routes: 3
Destination         Gateway                   INTERFACE              Protocol  Metric     Tag      Misc-Info
---------------------+---------------+--------------------------------+--------+-------+----------+-----------
+  10.0.0.0/24        10.4.15.254     EMP                              STATIC         1          0  
+  10.4.15.0/24       10.4.15.1       EMP                              LOCAL          1          0  
+  127.0.0.1/32       127.0.0.1       Loopback                         LOCAL          1          0  
Inactive Static Routes
Destination       Gateway           Metric        Tag   Misc-Info
--------------------+-----------------+------+----------+-----------------
r 0.0.0.0/0          1.1.1.1                1          0 
-> show ip routes
+ = Equal cost multipath routes
Total 1 routes
Dest Address       Gateway Addr
Age        Protocol 
------------------+-------------------+----------+-----------
127.0.0.1/32         127.0.0.1         00:37:17   LOCAL

<<<PAGE 224>>>
RECURSIVE STATIC ROUTE 
• Assign static routes with the next hop being the same as a route learned through a routing 
protocol
• Recursive static routes
• Nexthop (or gateway) address no longer must be tied to a particular INTERFACE
• Capability to tie the destination route to the best route used to reach a particular host
• May be an INTERFACE or a dynamically learned route (i.e. BGP, OSPF, RIP, etc)
• May change over time
-> ip static-route <Destination Network>/<Mask> follows <host> [METRIC | NAME | TAG | NO]

<<<PAGE 225>>>
RECURSIVE STATIC ROUTE - CLI
Legend: + indicates routes in-use
* indicates BFD-enabled static route
r indicates recursive static route, with following address in brackets
Total IPRM IPv4 routes: 4
Destination         Gateway           Interface   Protocol  Metric   Tag     Misc-Info
-------------------+------------------+-----------+---------+--------+-------+-----------
+  2.2.2.2/32         192.168.100.253   vlan100      RIP        2        0
+  10.1.20.0/24       10.1.20.1         vlan20       LOCAL      1        0
+r 172.30.0.0/16      192.168.100.253   vlan100      STATIC     1        0    [2.2.2.2]
+  192.168.100.0/24   192.168.100.1     vlan100      LOCAL      1        0
Inactive Static Routes
Destination       Gateway           Metric
--------------------+-----------------+---------
r 172.20.0.0/16      3.3.3.3            1
+ = Equal cost multipath routes
* = BFD Enabled static route
Total 5 routes
Dest Address      Subnet Mask       Gateway Addr
Age       Protocol
----------------+------------------+------------------+---------+-----------
2.2.2.2         255.255.255.255    192.168.100.253   16:52:44   RIP
10.1.20.0       255.255.255.0      10.1.20.1         00:09:27   LOCAL
127.0.0.1       255.255.255.255    127.0.0.1         17:55:33   LOCAL
172.30.0.0      255.255.0.0        192.168.100.253   00:08:06   static
192.168.100.0   255.255.255.0      192.168.100.1     17:54:09   LOCAL
+r 172.30.0.0/16   10.1.20.2    vlan20    STATIC      1   0 [2.2.2.2]
2.2.2.2   255.255.255.255  10.1.20.2  00:07:28   RIP
-> ip static-route 172.30.0.0/16 follows 2.2.2.2 metric 1
-> show ip router database
The gateway to reach the 2.2.2.2 
network has changed through RIP; so, 
the gateway to reach the 172.30.0.0 
network has also changed
172.30.0.0      255.255.0.0        10.1.20.2 
00:08:06   static

<<<PAGE 226>>>
ROUTING INFORMATION PROTOCOL (RIP)

<<<PAGE 227>>>
ROUTING INFORMATION PROTOCOL - AOS SPECIFICATIONS
• RIP - Routing Information Protocol
• Supports IPv4
• Distance Vector Protocol (uses hop count to determine best path)
• Hop count limit of 16 is considered unreachable (prevents loops)
• Maximum network diameter = 15
• Generates updates every 30 seconds
•
Updates contain all of the router’s routing table
• Routes timeout after 180 seconds
• Uses UDP port 520
• Maximum packet size is 512 bytes
•
20 Route Updates
• Poison reverse increases size
of routing updates
•
Valid and poisoned routes are included in the updates
• Metrics only involve hop count

<<<PAGE 228>>>
ROUTING INFORMATION PROTOCOL - CLI COMMANDS
Minimum configuration
-> ip load rip
-> ip rip interface if_name admin-state enable
-> ip rip admin-state enable
-> ip route-map rip_1 sequence-number 50 action permit
-> ip route-map rip_1 sequence-number 50 match ip-address 0.0.0.0/0
-> ip redist local into rip route-map rip_1 admin-state enable
-> ip redist static into rip route-map rip_1 admin-state enable
More details in next chapter for Redistribution
Only learned RIP routes and Loopback0 interface are advertised by default.  
Local and or static routes must be redistributed.
STOP

<<<PAGE 229>>>
CLI COMMANDS
-> ip rip interface int_name send-version [v2 / v1 / v1compatible / none]
-> ip rip interface int_name recv-version [v1 / v2 / both / none]
-> ip rip interface int_name metric #
-> ip rip interface int_name auth-type [none / simple / MD5]
-> ip rip update-interval seconds
-> show ip rip
-> show ip rip peer
-> show ip rip interface
-> show ip rip interface int_name

<<<PAGE 230>>>
ROUTING INFORMATION PROTOCOL - MONITORING 
• Display the RIP Routes
• Display the RIP Peers
• Display the IP Interfaces redistributed in RIP
-> show ip rip routes
Destination        Mask               Gateway          Metric 
------------------+------------------+----------------+-------
50.50.50.0         255.255.255.0      50.50.50.1         1 
-> show ip rip peer
Total    Bad    Bad
Secs since
IP Address   Recvd
Packets Routes Version  last update
----------------+------+-------+------+-------+-----------
100.10.10.1         1       0     0       2        3
-> show ip rip interface
Intf Admin   IP Intf
Updates    
Interface     vlan
status      status
sent/recv(bad)
name
----------------+-----+----------+----------+---------------
30.30.30.1        30    enabled     enabled
5/5(0)

<<<PAGE 231>>>
ROUTING INFORMATION PROTOCOL - TIMERS
• Update
• Default at 30 - range 1..120
• The time interval between advertisements sent on an interface
• AOS to enforce the constraint that update cannot exceed 1/3 of invalid
• Invalid
• Default at 180 - range 3..360
• The time interval before an active route expires (and enters the “garbage” state)
• AOS to enforce the constraint that invalid cannot be less than 3x of update
-> ip rip update-timer 45
-> ip rip invalid-timer 270
Default 180
Default 30

<<<PAGE 232>>>
ROUTING INFORMATION PROTOCOL - TIMERS
• Garbage
• Default at 120 - range 0..180
• The time interval before an expired route (which is in the “garbage” state)
is removed from the RIB.
• During the “garbage” interval measured by the garbage timer,
the router advertises the prefix with a metric of INFINITY
• Hold-down
• Default at 0 - range 0..120
• The time interval during which a route remains in the hold-down state.
Whenever a route is seen from the same gateway with a higher metric
than the route in the RIB, the route goes into hold-down. 
• This excludes route updates with an INFINITY metric
-> ip rip garbage-timer 180
-> ip rip holddown-timer 10
Default 120
Default 0

<<<PAGE 233>>>
APPLYING AN ACL ON THE EMP PORT

<<<PAGE 234>>>
APPLYING AN ACL ON THE EMP PORT
• This feature allows for applying an ACL on the EMP port of the switch. 
• It enables policy-based routing on the EMP ports. 
• The configuration is enabled using the empacl policy-list type.
• Only for IP condition in PBR policy rule.
• The following condition and action are supported in this release:
• Policy condition with Source IPv4 and Destination IPv4 addresses
• Policy action with PBR
• Only a single empacl policy list with multiple policy rules is supported.
• The following CLI commands are associated with this feature:
-> policy list list_name type empacl

<<<PAGE 235>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 236>>>
OPEN SHORTEST PATH FIRST (OSPF) - FUNDAMENTALS
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 237>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the role of a Router ID
• Summarize the different states an OSPF router 
goes through

<<<PAGE 238>>>
OSPF > OVERVIEW
• Routing Protocol
• Interior Gateway Protocol
• Overcome RIP deficiencies & scalability problems
• Link-State Routing (LSR) Protocol
• Shortest Path First Algorithm
• Widely used in large enterprise networks
• RFC 2328

<<<PAGE 239>>>
SPECIFICATIONS

<<<PAGE 240>>>
ROUTER IDENTITIES
• Router Identities = Router ID
• Each OSPF router has a unique ID within the OSPF network
• ID included in any OSPF messages sent by the OSPF router
• Router ID can be (in order of priority):
• Manually defined
• The IP address of the router’s Loopback0 interface
• Highest IP address from one of its active interfaces
ID = 1.1.1.1
ID = 2.2.2.2
ID = 3.3.3.3
ID = 4.4.4.4
ID = 5.5.5.5

<<<PAGE 241>>>
FINDING NEIGHBOURS
• Exchange Process
• Down State
• Router have not exchanged any OSPF information 
• Init State
• A destination router has received a new router’s hello packet 
• Adds it to its neighbour list 
• 2-Way State
• The new router receives a unidirectional reply from the destination router
• Adds the destination router to its neighbour list
Hello
(cont. R1 ID)
R1
R2
Hello
Hello
Hello
(cont. R2 ID)
- Hello interval: 10 seconds
(keep-alive function)
- Dead interval: 40 seconds
R1 State
Down
Init
2-Way
Exstart
Exchange
Loading
Full
R2 State
Down
Init
2-Way
Exstart
Exchange
Loading
Full

<<<PAGE 242>>>
DESIGNATED & BACKUP DESIGNATED ROUTERS
• Once in 2-Way State, the routers elect a Designated Router (DR) and a Backup Designated 
Router (BDR)
• 1 DR and 1 BDR for each broadcast segment
• Role
• Maintaining the LSDB (Link State DataBase)
• Receiving and disseminating update 
to the routers on the segment
R4
DR
BDR
DROther
VLAN 1
New link!
DROther
R1
R2
R3
Update
Update (dst @: 224.0.0.5)
(dst @: 224.0.0.6)
1
2
3

<<<PAGE 243>>>
DESIGNATED & BACKUP DESIGNATED ROUTERS
• DR & BDR Election
• The DR & BDR are elected according to the following parameters: 
• IP interface priority (highest priority) 
• Router ID (highest value)
• If the DR fails, 
• The BDR is promoted to DR
• Another Router (DROther) is promoted to BDR
ID = 1.1.1.1
Priority = 250
ID = 2.2.2.2
Priority = 200
ID = 3.3.3.3
Priority = 150
ID = 4.4.4.4
Priority = 100
ID = 5.5.5.5
Priority = 50
DR
BDR
DROther
DROther
DROther
1
2

<<<PAGE 244>>>
DESIGNATED & BACKUP DESIGNATED ROUTERS
• Election > Exstart State
• DR & BDR form adjacencies with the other OSPF routers
• Highest router ID becomes the master and start the exchange process
• OSPF routers are ready to share link state information!
R1 State
Init
2-Way
Exstart
R2 State
Init
2-Way
Exstart
Hello
• Router ID 
• IP Int./Rtr Priority
Hello
• Router ID 
• IP Int./Rtr Priority
ID = 1.1.1.1
Priority = 250
ID = 2.2.2.2
Priority = 200
ID = 3.3.3.3
Priority = 150
ID = 4.4.4.4
Priority = 100
ID = 5.5.5.5
Priority = 50
DR
BDR
DROther
DROther
DROther
MASTER
SLAVE

<<<PAGE 245>>>
SHARING ROUTING INFORMATION
• Sharing Link State information > Exchange State
• Database Description (DBD) packets which contains
• ID of the advertising router
• Cost of the advertising router
• Sequence number of the link
R4
Init
2-Way
Exstart
Exchange
R1 (DR)
Init
2-Way
Exstart
Exchange
DBD
• ID Adv. Router
• Cost Adv Router
• Seq nb
LSAck
MASTER
SLAVE
R4
R1 (DR)

<<<PAGE 246>>>
SHARING ROUTING INFORMATION
• Loading information in the Database > Loading State
• If the master has more up-to-date information than the slave, 
• Slave sends a Link State Request (LSR) to the master
• Master then sends a Link State Update (LSU) with detailed information of the links
• Slave incorporate information in its local database 
• Slave sends a Link State Acknowledge (LSAck) to the master
• If slave has more up-to-date information, 
• It will repeat the Exchange and Loading states
R4
Init
2-Way
Exstart
Exchange
Loading
R1 (DR)
Init
2-Way
Exstart
Exchange
Loading
LSR
LSU
R4
R1 (DR)
MASTER
SLAVE
MORE 
UP-TO-DATE 
INFO
LSAck

<<<PAGE 247>>>
SHARING ROUTING INFORMATION
• Master & Slave synchronized > Full State
• Incremental updates after entering a full state
• In case of Update (ex. new route discovered)
State
Down
Init
2-Way
Exstart
Exchange
Loading
Full
R4
DR
BDR
DROther
VLAN 1
DROther
R1
R2
R3
1
2
3
A new network is discovered by R4
R4 sends a multicast to the DR and the BDR (destination @: 224.0.0.6)
The DR and the BDR update their LSDB (based on the received information)
The DR informs the other routers on the segment about the change 
(destination @: 224.0.0.5 = all OSPF routers)
1
2
3

<<<PAGE 248>>>
SHARING ROUTING INFORMATION
• Metrics/Cost
• Indicates the overhead required to send packets out a particular interface
• Cost is calculated: 
• From the root node to every other node in the network 
• Using the metric cost of the outgoing interfaces
• Cost can be set on a per-interface basis
• Routers can disagree about the cost on a network link
• Can result in asymmetric routing in the network

<<<PAGE 249>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 250>>>
O P E N  S H O RT E S T PAT H  F I R S T ( O S P F )  – A R E A S
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 251>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Define an OSPF Area
• Summarize the different LSA types
• List the OSPF Area types
• Learn how to redistribute local & external 
routes

<<<PAGE 252>>>
OVERVIEW

<<<PAGE 253>>>
• An OSPF network can be divided in sub-domains called areas
• A router within an area maintains a topological database for the area to which it belongs
• The router does not have information about the topology outside of its area
Without Areas
OVERVIEW
…
…
With Areas
CORE
DISTRIBUTION
ACCESS
THE SPF IS RUNNING
TOO OFTEN!
I’M RECEIVING TOO
MANY LSAS!
MY ROUTING TABLE IS TOO BIG
I’M RUNNING LOW ON MEMORY!
AREA 1
…
…
AREA 0
AREA 2

<<<PAGE 254>>>
OVERVIEW
• Main benefit of creating areas > reduce the number of routes to propagate
• If divided in areas, an OSPF network must have: 
• A Backbone Area
• Distributes information between areas
• Must be contiguous (if not, virtual links can be configured)
• Non-backbone area(s) directly connected to the backbone area
• Area are identified by an area ID (32 bits dotted decimal format):
• Backbone area > 0.0.0.0
• Other areas > W.X.Y.Z (ex. 1.1.1.1) 
…
AREA 0.0.0.0 (BACKBONE AREA)
…
AREA 1.1.1.1
AREA 2.2.2.2

<<<PAGE 255>>>
ROUTER TYPES

<<<PAGE 256>>>
BACKBONE ROUTER (BB) & INTERNAL ROUTER (IR)
• Routers that are entirely within the backbone area are called Backbone Router (BB)
• Routers that are wholly within an area are called Internal Routers (IR)
…
AREA 0.0.0.0 (BACKBONE AREA)
…
AREA 1.1.1.1
AREA 2.2.2.2
BB
IR
IR
IR
IR

<<<PAGE 257>>>
AREA BORDER ROUTER (ABR)
• Router that attaches multiples areas (backbone + other areas)
• Condense the topological information of their attached areas for distribution to the 
backbone
• The backbone in turn distributes the information to the other areas
• Main function
• Summarize sub networks found throughout the OSPF system
…
AREA 0.0.0.0
AREA 1.1.1.1
ABR

<<<PAGE 258>>>
AUTONOMOUS SYSTEM BOUNDARY ROUTER (ASBR)
• Router that is running multiple routing protocols
• Serves as a gateway 
• Able to import and translate different protocols into OSPF (redistribution)
…
ASBR
RIP
AREA 0.0.0.0
AREA 1.1.1.1
EXTERNAL DOMAIN

<<<PAGE 259>>>
LSA TYPES

<<<PAGE 260>>>
LSA – TYPE 1 > ROUTER LSA
• Each router within the area floods router LSA
• Aim: provide a list with all the directly connected links
• A router LSA always stays within the area
• Generated by every router
AREA 0.0.0.0
R1
R2
R3
Each router sends a LSA – Type 1 to each other with all its directly connected links

<<<PAGE 261>>>
LSA – TYPE 2 > NETWORK LSA
• Only generated by DR (multi-access network)
• A network LSA always stays within the area
• Aim: send ID of all the routers connected to the multi-access network
AREA 0.0.0.0
DR
R1
R3
R2
The DR generates a LSA – Type 2 in the Area 0 
Contains the directly connected routers:
R1
R3

<<<PAGE 262>>>
LSA – TYPE 3 > SUMMARY LSA
• Generated by the ABR
• Aim: inform other areas about networks from an area
…
ABR (2)
AREA 0.0.0.0
AREA 1.1.1.1
…
AREA 2.2.2.2
ABR (1)
R1
R2
R3
R4
R5
NEW
ROUTE
LSA – TYPE 1
LSA – TYPE 3
LSA – TYPE 3
R1 floods the new route information via a LSA – Type 1 (Router LSA) in the Area 2
Reminder: LSA – Type 1 stays within the area!
ABR (1) creates an LSA – Type 3 (Summary LSA) and flood it into the area 0
This LSA is flooded into all the other areas

<<<PAGE 263>>>
LSA – TYPE 5 > EXTERNAL LSA
• Generated by the ASBR
• Aim: redistribute external routes into OSPF
…
ABR (2)
AREA 0.0.0.0
AREA 1.1.1.1
…
AREA 2.2.2.2
ABR (1)
R2
R3
R4
R5
LSA – TYPE 5
LSA – TYPE 5
LSA – TYPE 5
ASBR
RIP
EXTERNAL DOMAIN
The ASBR redistributes the RIP routes into OSPF via a LSA – Type 5 – External LSA
The LSA – Type 5 – External LSA is flooded into all the other areas

<<<PAGE 264>>>
LSA – TYPE 4 > SUMMARY ASBR LSA
• Generated by the ABR
• Aim: inform other routers where to find the ASBR
• Includes the ASBR Router ID
…
ABR (2)
AREA 0.0.0.0
AREA 1.1.1.1
…
AREA 2.2.2.2
ABR (1)
R2
R3
R4
R5
LSA – TYPE 1
LSA – TYPE 4
LSA – TYPE 4
ASBR
RIP
EXTERNAL DOMAIN
The ASBR flips a bit in the LSA-Type 1 to identify itself as ASBR
When the ABR (1) receives the LSA, it creates a LSA Type 4 – Summary ASBR LSA and flood it into the area 0
This LSA is flooded into all the other areas

<<<PAGE 265>>>
LSA – TYPE 7 > NSSA LSA
• Used for specific area type: Not-So-Stubby-Area (explained later)
• LSA - Type 5 are not allowed in NSSA areas
• LSA – Type 7 carries exact same information as LSA – Type 5 but is not blocked in NSSA areas
…
ABR (2)
AREA 0.0.0.0
AREA 1.1.1.1
…
AREA 2.2.2.2
(NSSA AREA)
ABR (1)
R2
R3
R4
R5
LSA – TYPE 7
LSA – TYPE 5
LSA – TYPE 5
ASBR
RIP
EXTERNAL DOMAIN
The ASBR redistributes the RIP routes into OSPF via a LSA – Type 7 – External LSA (because Area 2 is NSSA)
The ABR (1) convert the LSA – Type 7 to LSA – Type 5, then flood it into all the other areas
*LSA-Type 6 are not explained in this course as they are not used in today’s infrastructures

<<<PAGE 266>>>
AREA TYPES

<<<PAGE 267>>>
STANDARD AREA
• Router Types
• R2 = Area Border Router (ABR)
• R3 = Autonomous System Boundary Router (ASBR)
• LSA Types
• Type 1 & 2 LSAs are flooded between routers in the same area
• Type 3 & 5 are flooded throughout the backbone and all standard areas
• Type 4 LSAs are injected into the backbone by the ABR of an area which contains an ASBR
R1
R2
R3
TYPE 1/2
TYPE 1/2
TYPE 3
TYPE 5
TYPE 4
AREA 0
STANDARD AREA 1
EXTERNAL
DOMAIN

<<<PAGE 268>>>
STUB AREA
• External routes are not forwarded in a stub area
• Router Types
• R2 = Area Border Router (ABR)
• R2 & R3 share a common stub area
• LSA Types
• Type 5 LSAs are not propagated into the stub area
• Instead, R2 (ABR) injects a Type 3 LSA containing a default route into the stub area (« through itself »)
• Type 4 LSAs are not propagated into the stub area
R1
R2
R3
TYPE 1/2
TYPE 1/2
DEFAULT
TYPE 3
AREA 0
STUB AREA 1

<<<PAGE 269>>>
TOTALLY STUBBY AREA
• External routes + Type 3 LSAs are not forwarded in a Totally Stubby area
• Router Types
• R2 = Area Border Router (ABR)
• R2 & R3 share a common stub area
• LSA Types
• Like stub areas, totally stubby areas do not receive Type 4 & Type 5 LSAs from their ABRs
• Neither do the Type 3 LSAs
• All routing out of the area relies on a single default route injected by the ABR 
R1
R2
R3
TYPE 1/2
TYPE 1/2
DEFAULT
AREA 0
TOTALLY STUBBY AREA 1

<<<PAGE 270>>>
NOT SO STUBBY AREA (NSSA)
• Stub & Totally Stubby Areas
• Pro: Convenient to reduce the resource utilization of routers (no external routes to process)
• Con: Neither type can contain an ASBR (as types 4 & 5 LSAs not authorized)
• Router Types
• R2 = Area Border Router (ABR)
• R3 = Autonomous System Boundary Router (ASBR)
• LSA Types
• Type 7 LSAs = Type 5 LSAs in disguise
• This allows an ASBR to advertise external links to an ABR
R1
R2
R3
TYPE 1/2
TYPE 1/2
TYPE 5
TYPE 4
AREA 0
NSSA 1
EXTERNAL
DOMAIN
TYPE 7
DEFAULT

<<<PAGE 271>>>
ROUTES REDISTRIBUTION

<<<PAGE 272>>>
ROUTES REDISTRIBUTION
• Allows to learn and advertise IPv4 routes between different protocols
• Uses route maps to:
• Determine which routes are allowed/denied access to the network
• Modify route parameters before they are redistributed
• STEP 1: Configuring Route Maps
• A Route Map is composed of 
• Action 
• Route map name
• Sequence number
• Action: permit/deny
• Match 
• Criteria that a route must match
• Action statement is applied to the route
• Set 
• Modify route information before being redistributed 
• Applied if
•
All the route-map criteria is met
•
The action permits redistribution
ASBR
RIP
AREA 0.0.0.0
192.168.1.0/24
192.168.2.0/24
EXAMPLE: REDISTRIBUTION OF 192.168.1.0 ONLY
ROUTE MAP
- ACTION: PERMIT
- MATCH: 192.168.1.0/24
- SET: NOT USED
- ACTION: DENY
- MATCH: 192.168.2.0/24
- SET: NOT USED
EXTERNAL DOMAIN

<<<PAGE 273>>>
ROUTES REDISTRIBUTION
• STEP 2: Configuring Route Redistribution
• Redistribution from source protocol to destination protocol
• Source protocol: from which the sources are learned
• Destination protocol: from which the sources are redistributed
• Redistribution configured > Router becomes ASBR
ASBR
RIP
AREA 0.0.0.0
192.168.1.0/24
192.168.2.0/24
EXAMPLE: REDISTRIBUTION OF 192.168.1.0 ONLY
STEP 1 > ROUTE MAP
- ACTION: PERMIT
- MATCH: 192.168.1.0/24
- SET: NOT USED
- ACTION: DENY
- MATCH: 192.168.2.0/24
- SET: NOT USED
STEP 2 > ROUTES REDISTRIBUTION
- RIP INTO OSPF
- ROUTE MAP (CONFIGURED IN STEP 1)
EXTERNAL DOMAIN
REDISTRIBUTION

<<<PAGE 274>>>
OSPF CONFIGURATION

<<<PAGE 275>>>
OSPF CONFIGURATION
Step by Step
Enabling OSPF
Loading the Software
Creating an Area
Specifying an Area Type
Creating an OSPF Interface
Assigning an Interface to an Area
Redistributing Local & External Routes

<<<PAGE 276>>>
OSPF CONFIGURATION
Step by Step
Load the OSPF Software into the running configuration
Create the OSPF area(s)
When creating an area, an area type can be specified (Normal/Stub/NSSA)
AREA 0
AREA 1
Loading the Software
Creating an Area
Specifying an Area Type

<<<PAGE 277>>>
OSPF CONFIGURATION
Step by Step
Once areas established, interfaces need to be created and assigned to the areas
Each Interface must then be assigned to an Area
AREA 0
AREA 1
AREA 0
AREA 1
Creating an OSPF Interface
Assigning an Interface to an Area

<<<PAGE 278>>>
OSPF CONFIGURATION
Step by Step
If necessary, configure the redistribution of local and/or external routes
Enable the OSPF Software previously loaded
AREA 0
AREA 1
RIP
EXTERNAL DOMAIN
REDIST.
REDIST.
Enabling OSPF
Redistributing Local & External Routes

<<<PAGE 279>>>
OSPF CONFIGURATION
0) CONFIGURING THE ROUTER-ID
SW-> ip router router-id 192.168.254.7
1) LOADING THE SOFTWARE
SW-> ip load ospf
2) CREATING AN AREA
SW-> ip ospf area 0.0.0.0
3) SPECIFYING AN AREA TYPE
SW-> ip ospf area 1.1.1.1 type normal
4) CREATING AN OSPF INTERFACE
SW-> ip ospf interface int_1
5) ASSIGNING AN INTERFACE TO AN AREA
SW-> ip ospf interface int_1 area 0.0.0.0
SW-> ip ospf interface int_1 admin-state enable (R8)
AREA 0
INT 1
INT 2

<<<PAGE 280>>>
OSPF CONFIGURATION
4) CREATING AN OSPF INTERFACE
SW-> ip ospf interface int_2
5) ASSIGNING AN INTERFACE TO AN AREA
SW-> ip ospf interface int_2 area 1.1.1.1
SW-> ip ospf interface int_2 admin-state enable
6) REDISTRIBUTING LOCAL & EXTERNAL ROUTES
SW-> ip route-map RipIntoOspf sequence-number 10 action permit
SW-> ip route-map RipIntoOspf sequence-number 10 match ip-address 192.168.254.0/24 permit
SW-> ip redist rip into ospf route-map RipIntoOspf admin-state enable
7) ENABLING OSPF
SW-> ip ospf admin-state enable
AREA 0
AREA 1
INT 1
INT 2
AREA 0
AREA 1
RIP
EXTERNAL DOMAIN
REDIST.
REDIST.

<<<PAGE 281>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 282>>>
O P E N  S H O RT E S T PAT H  F I R S T ( O S P F )
A D VA N C E D  F E AT U R E S  &  M O N I TO R I N G
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 283>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Identify the advantages of ECMP in OSPF
• Choose when to use the Summarization
• Choose when to use the Aggregation
• Summarize the Graceful Restart feature
• Enable the Simple/MD5 Authentication
• Determine when to use the Virtual Link feature 
• List the main OSPF monitoring commands

<<<PAGE 284>>>
OSPF FEATURES

<<<PAGE 285>>>
OSPF & ECMP 
• Aka ECMP (Equal Cost Multi-Path) Routing
• Next-hop packet forwarding to a single destination can occur over multiple “best paths”
• Works for routes with
• Same destination
• Same metric
• Different next-hops
• ECMP Per-Flow Load Balancing 
• Distributes packets across multiple links based on L3 routing information
• Router discovers multiple paths to a destination > Routing table updated with multiple entries 
• Multiple paths used for multiple sources-destination host pairs
• Up to 4 ECMP routes supported
*Per packet Load Balancing is not supported

<<<PAGE 286>>>
SUMMARIZATION
• By default, OSPF doesn’t summarize anything
• OSPF Summarization advantages
• Smaller routing tables
• Less LSA flooding 
• Less bandwith, memory & CPU usage
• Summary routes are carried by LSA – Type 3 (Summary LSA)
• Internal routes summarization done on the ABR
AREA 0.0.0.0
AREA 1.1.1.1
ABR
192.168.0.0/24
192.168.1.0/24
WITH SUMMARIZATION
192.168.0.0/23 VIA ABR
WITHOUT SUMMARIZATION
192.168.0.0/24 VIA ABR
192.168.1.0/24 VIA ABR

<<<PAGE 287>>>
AGGREGATION
• Internal routes: Summarization > External routes: Aggregation
• Same advantages as Summarization
• Smaller routing tables
• Less LSA flooding 
• Less bandwith, memory & CPU usage
• Aggregated routes are carried by LSA – Type 5 (External ASBR LSA)
• External routes aggregation done on the ASBR
AREA 0.0.0.0
EXTERNAL DOMAIN
ASBR
192.168.0.0/24
192.168.1.0/24
WITH SUMMARIZATION
192.168.0.0/23 VIA ABR
WITHOUT SUMMARIZATION
192.168.0.0/24 VIA ABR
192.168.1.0/24 VIA ABR

<<<PAGE 288>>>
OSPF INTERFACE AUTHENTICATION
• If authentication enabled, neighbours can communicate only if: 
• They use the same type of authentication  
• They have a matching password or key
• 2 types of authentication: 
• Simple
• Uses simple clear-text passwords
• MD5
• Encrypted authentication, uses a key and a password

<<<PAGE 289>>>
VIRTUAL LINK
• Reminder: all areas must be connected to the backbone area (Area 0)
• Not possible? Solution: Virtual Link
• A Virtual Link is used: 
• To connect an area to the backbone through a non-backbone area
• To connect 2 parts of a partitioned backbone through a non-backbone area
• The crossed area is called Transit Area
AREA 0.0.0.0
AREA 1.1.1.1 = TRANSIT AREA
AREA 2.2.2.2
VIRTUAL LINK
AREA 0.0.0.0
AREA 1.1.1.1 = TRANSIT AREA
AREA 0.0.0.0
VIRTUAL LINK
ip ospf virtual-link <transit-area> <router-id>

<<<PAGE 290>>>
MONITORING

<<<PAGE 291>>>
MONITORING
• OSPF Log levels can be modified: 
• To monitor the OSPF operation
• To troubleshoot an issue on OSPF
• Modifying Log levels allows to have more (or less) information about a specific 
protocol/feature (ex. OSPF) in the logs
SEVERITY LEVELS FOR AOS R8

<<<PAGE 292>>>
MONITORING
Example of Severity Level modification
• All OSPF sub applications 
• Only the Hello messages
• For information, below the list of the sub applications
SW-> swlog appid ospf_0 subapp all level 8 
[OR]
SW-> swlog appid ospf_0 subapp all level debug3
SW-> swlog appid ospf_0 subapp hello level debug3
SW-> swlog appid ospf_0 subapp ?
ALL <num> <string>
1=ERROR 2=WARNING 3=RECV 4=SEND 5=FLOOD 6=SPF 7=LSDB 
8=RDB 9=AGE 10=VLINK 11=REDIST 12=SUMMARY
13=DBEXCH 14=HELLO 15=AUTH 16=STATE 17=AREA 18=INTF 
19=CONFIG 20=INFO 21=SETUP 22=TIME 23=MIP 24=TM
25=RESTART 26=HELPER 27=HOST 28=AUTOCONFIG

<<<PAGE 293>>>
MONITORING
Example
• Infrastructure
• Problem: SW1 & SW2 are not in FULL state!
• Modify the log level to have the maximum verbosity 
SW1
SW2
# of Events                           = 4,
# of Init State Neighbors             = 0,
# of 2-Way State Neighbors            = 0,
# of Exchange State Neighbors         = 0,
# of Full State Neighbors             = 0,
# of type-9 LSAs on this interface    = 0,
# of Events                           = 4,
# of Init State Neighbors             = 0,
# of 2-Way State Neighbors            = 0,
# of Exchange State Neighbors         = 0,
# of Full State Neighbors             = 0,
# of type-9 LSAs on this interface    = 0,
SW1 -> swlog appid ospf_0 subapp all level debug3
SW1
SW2

<<<PAGE 294>>>
MONITORING
Example
• Check the logs
• Check the Hello Interval on both switches
• The Hello Interval value is not the same on both switches! 
• Solution: put the same value on both switches
• Result:
SW1 -> show log swlog | grep ospf_0
[TRUNCATED]
2017 Oct 20 09:58:57 SW1 swlogd: ospf_0 HELLO debug2(7) [1508493537.082626] 
(4226):(457): HELLO from 192.168.0.2 discarded...invalid helloInterval 10
[TRUNCATED]
Hello Interval (seconds)              = 20,
Hello Interval (seconds)              = 10,
SW1
SW2
# of Init State Neighbors             = 0,
# of 2-Way State Neighbors            = 0,
# of Exchange State Neighbors         = 0,
# of Full State Neighbors
= 1,
# of Init State Neighbors             = 0,
# of 2-Way State Neighbors            = 0,
# of Exchange State Neighbors         = 0,
# of Full State Neighbors
= 1,
SW1
SW2

<<<PAGE 295>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 296>>>
G L O B A L R O U T I N G  P R O TO C O L S  R E D I S T R I B U T I O N
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 297>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the layer 3 route redistribution 
concept on AOS based switches
• Implement an appropriate route redistribution 
in a network with its different options, then 
monitor the rule statements

<<<PAGE 298>>>
OVERVIEW OF ROUTE MAP
Route Redistribution
• Redistribute routes from a source protocol RIB to a destination protocol RIB
• Source protocol can be BGP, RIP, OSPF, Local or Static
• Destination protocol can be BGP, RIP or OSPF
RIB
IP ROUTE MANAGER
REDIST ROUTE MAP
Source 
Routing 
Protocol
Destination 
Routing 
Protocol

<<<PAGE 299>>>
OVERVIEW OF ROUTE MAP
Route Redistribution
RIB
(Routing Information 
Base)
IPRM 
(IP Route Manager)
Local
Static
RIP
OSPF
BGP
IS-IS
Source Routing 
Protocol
FIB
(Forwarding  Information 
Base)
-> show ip routes
+ = Equal cost multipath routes
Total 1 routes
Dest Address       Gateway Addr
Age        Protocol
------------------+-------------------+----------+-----------
-> show ip routes
-> show ip router database
Legend: + indicates routes in-use
b indicates BFD-enabled static route
i indicates interface static route
r indicates recursive static route, with following address in brackets
Total IPRM IPv4 routes: 4
Destination         Gateway           Interface  Protocol  Metric
Tag      Misc-Info
---------------------+---------------+-----------+--------+-------+----------+--------------
+  10.0.0.0/24        10.4.116.254    EMP          STATIC         1          0
+  10.4.16.0/24       10.4.116.254    EMP          STATIC         1          0
+  10.4.116.0/24      10.4.116.7      EMP          LOCAL          1          0
+  127.0.0.1/32       127.0.0.1       Loopback     LOCAL          1          0
Inactive Static Routes
Destination       Gateway           Metric
Tag   Misc-Info
--------------------+-----------------+------+----------+-----------------
-> show ip router database
1
Best (preferred) routes
-> show ip route-pref
Protocol    Route Preference Value
------------+------------------------
Local                 1
Static
2
OSPF                110
ISISL1              115
ISISL2              118
RIP                 120
EBGP                190
IBGP                200
Import              210
2
RIB - Routing Information Base
FIB – Forwarding Information Base
Destination Routing 
Protocol
Local
Static
RIP
OSPF
BGP
IS-IS
3
-> show ip redist
Redist
Route 
Map

<<<PAGE 300>>>
ROUTE MAP - DEFINITION
• Route map 
• Criteria that is used to control redistribution of routes between protocols 
• Defined by configuring route map statements
• Route Map and Statements
• Action 
• Route map name
• Sequence number
• Action, redistribution is permitted or denied based on criteria
• Match 
• Criteria that a route must match
• Action statement is applied to the route
• Set 
• Modify route information before redistributed into the receiving protocol
• Applied if
• All the route-map criteria is met and 
• The action permits redistribution

<<<PAGE 301>>>
ROUTE MAP - CONFIGURATION
• Match
• IP-ADDRESS 
• IP-NEXTHOP
• IPV4-INTERFACE
• IPV6-ADDRESS
• IPV6-INTERFACE 
• IPV6-NEXTHOP
• METRIC
• ROUTE-TYPE
• LEVEL2
• LEVEL1
• INTERNAL
• EXTERNAL
• TAG
• REDIST-CONTROL
• ALL-SUBNETS
• NO-SUBNETS
• AGGREGATE
ACTION MATCH SEQUENCE-NUMBER SET
Route-Map
Redist-
control
Set…
Match
Action
IP 
access-
list
• ACTION
•PERMIT
•DENY
• SET
•METRIC
1
• EFFECT
• ADD
• SUBTRACT
• REPLACE
• NONE
• METRIC-TYPE
• INTERNAL
• EXTERNAL
• TAG
• COMMUNITY
• LOCAL-PREFERENCE
• LEVEL
• LEVEL1-2
• LEVEL2
• LEVEL1
• IP ACCESS-LIST
• ACCESS-LIST-NAME
• IP-ADDRESS/MASK
-> ip route-map myroute-map?

<<<PAGE 302>>>
NEW REDISTRIBUTION - COMMANDS
• Route map criteria specification
• Rip redistribution
• OSPF redistribution
ip route-map route-map-name [sequence-number number] match ip-address {access-list-name |
ip-address/prefixLen} [redist-control {all-subnets | no-subnets | aggregate}] [permit | deny]
->ip redist {local | static | ospf | isis | bgp} into rip route-map route-map-name
->ip redist {local | static | rip | isis | bgp} into ospf route-map route-map-name
ip route-map route-map-name [sequence-number number] action {permit | deny}
ip route-map route-map-name [sequence-number number] set metric metric [effect {add |subtract | 
replace | none}]

<<<PAGE 303>>>
ROUTE MAP - ACCESS LIST CREATION
• Convenient way to add multiple IPv4 or IPv6 addresses to route-maps
• Maximum 200 per switch
• Create the Access List name 
• Define access-list statements
-> ip access-list ipaddr2
-> ip access-list ipaddr2 address 16.24.2.1/16
-> ip access-list ipaddr2 address 16.24.2.1/16 action deny redist-control allsubnets
-> ip route-map test sequence-number 50 match ip-address ipaddr2
-> ip access-list access-list-name
-> ip access-list access-list-name address address/mask [action {permit | deny}] 
[redist-control {all-subnets | no-subnets | aggregate}]

<<<PAGE 304>>>
ROUTE MAP - SEQUENCING & DENY STATEMENTS
• Operation
•
• Route 10.10.0.0/16 will match sequence-number 1
• Since one of the actions is deny, switch stops processing and does not redistribute the route 
• Route 11.11.0.0/16 will not match sequence-number 1
• Therefore, the processing goes to sequence-number 2 where there is a match and both actions are permit
• Switch stops processing and redistributes the route
-> ip route-map myroutemap sequence-number 1 action deny 
-> ip route-map myroutemap sequence-number 1 match ip-address 10.0.0.0/8 redist-control all-subnets permit 
-> ip route-map myroutemap sequence-number 2 action permit
-> ip route-map myroutemap sequence-number 2 match ip-address 0.0.0.0/0 redist-control all-subnets permit 
-> ip redist static into rip route-map myroutemap

<<<PAGE 305>>>
-> ip route-map routemap1 sequence-number 50 action permit
-> ip route-map routemap1 match ip-address 10.0.0.0/8
-> ip route-map routemap1 match tag 4
-> ip route-map routemap1 match tag 5
-> ip route-map routemap1 match ip-address 10.0.0.0/8 redist-control all-subnets permit
-> ip route-map routemap1 sequence-number 50 set metric 1 effect add
ROUTE MAP - SEQUENCING & DENY STATEMENTS
Means match the subnet 
10.0.0.0/8 and [tag 4 or tag 5]

<<<PAGE 306>>>
ROUTE MAP - MONITORING
Source       Destination
Protocol     Protocol
Status    Route Map
------------+------------+---------+--------------------
LOCAL4       OSPF         Enabled   ospf_ext
Access Lists: configured: 1 max: 200
Address /                  Redistribution
Name                 Prefix Length      Effect  Control
--------------------+------------------+-------+------------
extip                172.0.0.0/8        permit  aggregate
Route Maps: configured: 1 max: 200
Route Map: ospf_ext Sequence Number: 50 Action permit
match ip accesslist extip
-> show ip redist
-> show ip access-list
-> show ip route-map

<<<PAGE 307>>>
ROUTE MAP CONFIGURATION - EDITING & DELETING
• Deletes a specific route map set or match entry
• Deletes route map all sequence number of 50 in the rip_1 route map
• Deletes the route map rip_1
Notes: The “no” version of the command that specifies a match or set parameter only deletes that 
parameter from the route-map. If a sequence-number is included but no match or set 
parameters, then only that specific route-map is deleted. If the command only has a route-
map-name, then the entire  route-map is deleted.
-> no ip route-map rip_1 sequence-number 50 set metric 1 effect add
-> no ip route-map rip_1 sequence-number 50
-> no ip route-map rip_1

<<<PAGE 308>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 309>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
OSPF - Prerequisites 
How to 
✓ Prerequisites of the OSPF lab 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configuration prerequisites .................................................................. 3 
2.1. Core switches interconnexion .................................................................... 3 
2.1.1. Link Aggregation – Dynamic between 6870-A and 6900-A ............................................. 3 
2.1.2. Link Aggregation – Dynamic between 6900-A and 6870-B ............................................. 5 
2.2. Configuring the DHL active-active link .......................................................... 8

<<<PAGE 310>>>
2 
OSPF - Prerequisites 
 
 1 
Topology 
Open Shortest Path First routing (OSPF) is a shortest path first (SPF), or link state, protocol. OSPF is an interior 
gateway protocol (IGP) that distributes routing information between routers in a single Autonomous System 
(AS). OSPF chooses the least-cost path as the best path. OSPF is suitable for complex networks with large 
numbers of routers since it provides faster convergence where multiple flows to a single destination can be 
forwarded on one or more interfaces simultaneously.

<<<PAGE 311>>>
3 
OSPF - Prerequisites 
 
 2 
Configuration prerequisites 
 
2.1. 
Core switches interconnexion 
 
 
 
2.1.1. Link Aggregation – Dynamic between 6870-A and 6900-A 
 
 
 
 
- 
Now, we define a dynamic link aggregate on 6900-A and 6870-A , assign the group ID 17 and size it at 2 
ports even if there is only one port available. – (For future extension) 
 
- 
Manage linkagg 17 between 6900-A and 6870-A  
 
sw1 (6900-A) -> linkagg lacp agg 17 size 2 actor admin-key 17  
sw1 (6900-A) -> linkagg lacp port 1/1/5 actor admin-key 17 
 
sw1 (6900-A) -> show linkagg 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  17     Dynamic      40000017   2   ENABLED      DOWN            0   0 
 
sw7 (6870-A) -> linkagg lacp agg 17 size 2 actor admin-key 17  
sw7 (6870-A) -> linkagg lacp port 1/1/5 actor admin-key 17

<<<PAGE 312>>>
4 
OSPF - Prerequisites 
 
sw7 (6870-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  17     Dynamic      40000017   2   ENABLED      DOWN            0   0 
 
sw1 (6900-A) -> interfaces 1/1/5 admin-state enable 
 
sw7 (6870-A) -> interfaces 1/1/5 admin-state enable 
 
sw1 (6900-A) -> show linkagg agg 17 port 
 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
          1/1/5     Dynamic      1005   ATTACHED     17  UP   UP    YES 
 
sw7 (6870-A) -> show linkagg agg 17 port 
 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
          1/1/5     Dynamic      1005   ATTACHED     17  UP   UP    YES 
 
 
- 
Additional VLAN creation 
 
o 
Currently, only VLAN 1 is bridged between 6900-A and 6870-A  
o 
Change the default VLAN 
 
 
sw1 (6900-A) -> vlan 217 
sw1 (6900-A) -> ip interface int_217 address 172.16.17.1/24 vlan 217 
sw1 (6900-A) -> vlan 217 members linkagg 17 untagged 
 
sw1 (6900-A) -> show vlan 217 members 
   port      type        status 
----------+-----------+--------------- 
  0/17       default      forwarding 
 
sw1 (6900-A) -> show ip interface vlan 217 
Total 1 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
int_217                          172.16.17.1     255.255.255.0       UP     YES vlan 217 
 
sw7 (6870-A) -> vlan 217 
sw7 (6870-A) -> ip interface int_217 address 172.16.17.7/24 vlan 217 
sw7 (6870-A) -> vlan 217 members linkagg 17 untagged 
 
sw7 (6870-A) -> show ip interface vlan 217 
Total 1 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
int_217                          172.16.17.7     255.255.255.0       UP     YES vlan 217 
 
sw7 (6870-A) -> show vlan 217 members 
   port      type        status 
----------+-----------+--------------- 
  0/17       default      forwarding 
- 
Check the result

<<<PAGE 313>>>
5 
OSPF - Prerequisites 
 
sw1 (6900-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  17     Dynamic      40000017   2   ENABLED      UP              1   1 
 
sw7 (6870-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-----+-------------+---------+----+------------+--------------+------------- 
 7     Dynamic      40000007   2   ENABLED      UP              2   2 
17     Dynamic      40000017   2   ENABLED      UP              1   1 
78     Dynamic      40000078   2   ENABLED      UP              2   2 
- 
Test the configuration 
 
- 
Try to make a ping to 6900-A from 6870-A  
 
sw7 (6870-A) -> ping 172.16.17.1 
 
- 
Save the configuration 
 
sw1 (6900-A) -> write memory flash-synchro 
 
sw7 (6870-A) -> write memory flash-synchro 
 
2.1.2. Link Aggregation – Dynamic between 6900-A and 6870-B 
 
 
- 
Create a Dynamic Link Aggregation 
 
o 
Now, we define a dynamic link aggregate on 6900-A and 6870-B, assign the group ID 12 and size 
it at 2 ports. 
 
 
sw1 (6900-A) -> session cli timeout 300 
sw1 (6900-A) -> linkagg lacp agg 12 size 2 actor admin-key 12  
sw1 (6900-A) -> linkagg lacp port 1/1/25-26 actor admin-key 12

<<<PAGE 314>>>
6 
OSPF - Prerequisites 
 
- 
Then, check then the linkagg 
 
sw1 (6900-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  12     Dynamic      40000012   2   ENABLED      DOWN            0   0 
  17     Dynamic      40000017   2   ENABLED      UP              1   1 
 
- 
Manage the second switch 
 
sw2 (6870-B) -> session cli timeout 300 
sw2 (6870-B) -> linkagg lacp agg 12 size 2 actor admin-key 12  
sw2 (6870-B) -> linkagg lacp port 1/1/29 actor admin-key 12 
sw2 (6870-B) -> linkagg lacp port 1/1/30 actor admin-key 12 
 
sw2 (6870-B) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  12     Dynamic      40000012   2   ENABLED      DOWN            0   0 
    
- 
Now, connect the switches by activating the linkagg interfaces: 
 
sw1 (6900-A) -> interfaces 1/1/25-26 admin-state enable  
 
sw2 (6870-B) -> interfaces 1/1/29-30 admin-state enable 
 
sw1 (6900-A) -> show linkagg agg 12 port 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
         1/1/25     Dynamic      1025   ATTACHED     12  UP   UP    YES 
         1/1/26     Dynamic      1026   ATTACHED     12  UP   UP    NO 
 
sw2 (6870-B) -> show linkagg agg 12 port 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
          1/1/29     Dynamic      2001   ATTACHED     12  UP   UP    YES 
          1/1/30     Dynamic      2002   ATTACHED     12  UP   UP    NO 
- 
Additional VLAN creation 
 
o 
Currently, only VLAN 1 is bridged between 6900-A and 6870-A  
o 
Change the default VLAN 
 
sw1 (6900-A) vlan 212 
sw1 (6900-A) ip interface int_212 address 172.16.12.1/24 vlan 212 
sw1 (6900-A) vlan 212 members linkagg 12 untagged 
 
sw1 (6900-A) -> show vlan 212 members 
   port      type        status 
----------+-----------+--------------- 
  0/12       untagged     forwarding 
 
sw1 (6900-A) -> show ip interface vlan 212 
Total 1 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
int_212                          172.16.12.1     255.255.255.0   UP     YES     vlan 212

<<<PAGE 315>>>
7 
OSPF - Prerequisites 
 
 
sw2 (6870-B) -> vlan 212 
sw2 (6870-B) -> ip interface int_212 address 172.16.12.2/24 vlan 212 
sw2 (6870-B) -> vlan 212 members linkagg 12 untagged 
 
sw2 (6870-B) -> show ip interface vlan 212 
Total 1 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
int_212                          172.16.12.2     255.255.255.0   UP     YES     vlan 212 
 
sw2 (6870-B) -> show vlan 212 members 
   port      type        status 
----------+-----------+--------------- 
  0/12       untagged     forwarding 
- 
Check the result 
 
sw1 (6900-A) -> show linkagg 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  12     Dynamic      40000012   2   ENABLED      UP              2   2 
  17     Dynamic      40000017   2   ENABLED      UP              1   1 
 
sw2 (6870-B) -> show linkagg 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  12     Dynamic      40000012   2   ENABLED      UP              2   2 
 
- 
Try to make a ping between 6870-B to 6900-A 
 
sw2 (6870-B) -> ping 172.16.12.1 
 
- 
Save the configuration on both switches 
 
sw1 (6900-A) -> write memory flash-synchro 
sw2 (6870-B) -> write memory flash-synchro

<<<PAGE 316>>>
8 
OSPF - Prerequisites 
 
2.2. 
Configuring the DHL active-active link 
 
 
- 
For the purpose of the lab, create a link aggregation between the 6360 VC and the 6860-B:  
 
o 
6360 VC 
sw5 (6360-A) -> linkagg lacp agg 8 size 2 actor admin-key 8 
sw5 (6360-A) -> linkagg lacp port 2/1/3 actor admin-key 8 
ERROR: Port cannot be added to Linkagg, please remove other configuration on this port 
- 
Untagged the vlan on this port to be able to add it to the linkagg 
sw5 (6360-A) -> show vlan members port 2/1/3 
vlan           type   status 
--------+-----------+--------------- 
20           qtagged forwarding 
30           qtagged forwarding 
58          untagged forwarding 
 
sw5 (6360-A) -> no vlan 58 members port 2/1/3 
sw5 (6360-A) -> no vlan 20 members port 2/1/3 
sw5 (6360-A) -> no vlan 30 members port 2/1/3 
sw5 (6360-A) -> no vlan 58 
sw5 (6360-A) -> show vlan members port 2/1/3 
  vlan      type        status 
--------+-----------+--------------- 
     1    untagged    forwarding 
 
sw5 (6360-A) -> linkagg lacp port 1/1/4 actor admin-key 8 
sw5 (6360-A) -> linkagg lacp port 2/1/3 actor admin-key 8 
 
sw5 (6360-A) -> interfaces 1/1/4 admin-state enable 
sw5 (6360-A) -> interfaces 2/1/3 admin-state enable 
 
o 
6860-B 
sw8 (6860-B) -> show vlan members port 1/1/3 
vlan        type     status 
--------+-----------+--------------- 
20         qtagged forwarding 
30         qtagged forwarding 
58        untagged forwarding

<<<PAGE 317>>>
9 
OSPF - Prerequisites 
 
 
sw8 (6860-B) -> no vlan 58 members port 1/1/3 
sw8 (6860-B) -> no vlan 20 members port 1/1/3 
sw8 (6860-B) -> no vlan 30 members port 1/1/3 
sw8 (6860-B) -> no vlan 58 
 
sw8 (6860-B) -> linkagg lacp agg 8 size 2 actor admin-key 8 
 
sw8 (6860-B) -> linkagg lacp port 1/1/3 actor admin-key 8 
sw8 (6860-B) -> linkagg lacp port 1/1/4 actor admin-key 8 
 
sw8 (6860-B) -> interfaces 1/1/3-4 admin-state enable 
 
sw8 (6860-B) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
   8     Dynamic      40000008   2   ENABLED      UP              2   2 
  78     Dynamic      40000078   2   ENABLED      UP              2   2 
- 
Assigning VLANs on the Link Aggregations 
- 
Change default VLAN on the link aggregation (the client does not want to use the VLAN 1): 
 
sw8 (6860-B) -> vlan 57 
sw8 (6860-B) -> vlan 57 members linkagg 8 untagged 
 
sw8 (6860-B) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        untagged      forwarding 
  
sw5 (6360-A) -> vlan 57 members linkagg 8 untagged 
 
sw5 (6360-A) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        untagged      forwarding 
  0/8        untagged      forwarding 
- 
Tag the VLAN 20 and 30 on the link aggregation  
 
sw5 (6360-A) -> vlan 20 members linkagg 8 tagged 
sw5 (6360-A) -> vlan 30 members linkagg 8 tagged 
 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        qtagged      forwarding 
  0/8        qtagged      forwarding 
 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        qtagged      forwarding 
  0/8        qtagged      forwarding 
 
 
sw8 (6860-B) -> vlan 20 members linkagg 8 tagged 
sw8 (6860-B) -> vlan 30 members linkagg 8 tagged

<<<PAGE 318>>>
10 
OSPF - Prerequisites 
 
 
sw8 (6860-B) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        qtagged        blocking 
 
sw8 (6860-B) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        qtagged      forwarding 
 
- 
Tag the VLAN 57 on the link aggregation 78  
 
sw8 (6860-B) -> vlan 57 members linkagg 78 tagged 
 
sw8 (6860-B) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        untagged       blocking 
  0/78       qtagged      forwarding 
 
sw7 (6870-A) -> vlan 57 members linkagg 78 tagged 
 
sw7 (6870-A) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        untagged      forwarding 
  0/78       qtagged      forwarding 
 
- Configure a DHL session with the identifier 1 on the 6360-A (VC): 
 
sw5 (6360-A) -> dhl 1 
 
- Configure 2 links (link-A and link-B) for the DHL session: 
 
sw5 (6360-A) -> dhl 1 linka linkagg 7 linkb linkagg 8 
 
Notes 
Spanning Tree is disabled on all the DHL enabled ports 
 
- Map VLANs to link-B: 
 
sw5 (6360-A) -> dhl 1 vlan-map linkb 30 
 
- Activate the “RAW” MAC-Flushing method:  
 
sw5 (6360-A) -> dhl 1 mac-flushing raw 
-  
- Enable the DHL session: 
 
sw5 (6360-A) -> dhl 1 admin-state enable

<<<PAGE 319>>>
11 
OSPF - Prerequisites 
 
- Display the global status of the DHL configuration: 
 
sw5 (6360-A) -> show dhl 
Legends:  PE - Pre-Emption 
 Session            Session                  Admin   Oper     PE      MAC        Active MAC 
   ID                 Name                   State   State   Time   Flushing     Flushing 
                                                             (sec)  Technique    Technique 
----------+---------------------------------+-------+------+-------+----------+-------------- 
         1                           DHL-1     up     up     30      none         none 
 
Total number of sessions configured = 1 
- Display information about protected VLANs: 
 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        qtagged      forwarding 
  0/8        qtagged     dhl-blocking 
 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        qtagged     dhl-blocking 
  0/8        qtagged      forwarding 
 
- Manage Ip interface on 6860 
 
sw7 (6870-A) -> ip interface int_30 address 192.168.30.7/24 vlan 30 
sw8 (6860-B) -> ip interface int_20 address 192.168.20.8/24 vlan 20 
 
- Save configuration: 
sw5 (6360-A) -> write memory flash-synchro 
sw8 (6860-B) -> write memory flash-synchro

<<<PAGE 320>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
OSPF 
How to 
✓ Implement a OSPF backbone area configuration, different types of areas, 
authentication and virtual links on an OmniSwitch. 
Contents 
1 
Topology ........................................................................................ 3 
2 
Configuration .................................................................................. 4 
2.1. Client VLAN Configuration......................................................................... 4 
2.2. 
Configure connections between 6860-B and 6870-B ............................................... 4 
3 
OSPF Backbone ................................................................................ 5 
3.1. OSPF Backbone Logical Diagram .................................................................. 5 
3.2. Configuration ........................................................................................ 5 
3.2.1. Loopback interface configuration ........................................................................ 5 
3.3. Verification .......................................................................................... 8 
4 
OSPF Areas ................................................................................... 12 
4.1. OSPF Areas Logical Diagram ..................................................................... 12 
4.2. Configuration ....................................................................................... 13 
4.3. Verification ......................................................................................... 13 
4.4. Configuration ....................................................................................... 15 
4.5. Verification ......................................................................................... 15 
4.6. Virtual-link configuration (on both switches) ................................................. 18 
4.6.1. Configure the backbone area on switch 6870-B and 6860-B ........................................ 18 
4.6.2. Create Virtual-link ....................................................................................... 19 
4.6.3. Verify the working of the virtual-link .................................................................. 19

<<<PAGE 321>>>
2 
OSPF 
 
4.7. Let’s add VLANs 20 and 30 into our OSPF network in Area 3.3.3.3......................... 23 
4.8. On the 6870-A and 6860N create and configure Area 3.3.3.3: .............................. 23 
4.9. Verify the correct operation of the OSPF setup with the following commands: ......... 24 
5 
OSPF Redistribution ......................................................................... 28 
6 
Access to the DATA server ................................................................. 31 
7 
OSPF Authentication ........................................................................ 34 
7.1. Simple Authentication ............................................................................ 34 
7.2. MD5 Authentication ............................................................................... 34 
8 
Stub Area .................................................................................... 35 
8.1. OSPF Areas Logical diagram ...................................................................... 35 
8.2. Configuration ....................................................................................... 35 
8.3. Verification ......................................................................................... 37

<<<PAGE 322>>>
3 
OSPF 
 
 1 
Topology 
Open Shortest Path First routing (OSPF) is a shortest path first (SPF), or link state, protocol. OSPF is an interior 
gateway protocol (IGP) that distributes routing information between routers in a single Autonomous System 
(AS). OSPF chooses the least-cost path as the best path. OSPF is suitable for complex networks with large 
numbers of routers since it provides faster convergence where multiple flows to a single destination can be 
forwarded on one or more interfaces simultaneously.

<<<PAGE 323>>>
4 
OSPF 
 
 2 
Configuration 
2.1. 
Client VLAN Configuration 
- 
On the 6870-B, create client VLAN and assign an ip interface: 
 
sw2 (6870-B) -> vlan 120 
sw2 (6870-B) -> vlan 120 members port 1/1/1 untagged 
sw2 (6870-B) -> ip interface int_120 address 192.168.120.2/24 vlan 120 
sw2 (6870-B) -> interfaces 1/1/1 admin-state enable 
 
- 
ON the 6870-A and 6860-B, create client VLAN and assign ip interfaces: 
 
sw7 (6870-A) -> vlan 70 
sw7 (6870-A) -> vlan 70 members port 1/1/1 untagged 
sw7 (6870-A) -> ip interface int_70 address 192.168.70.7/24 vlan 70 
sw7 (6870-A) -> interfaces 1/1/1 admin-state enable 
 
sw8 (6860-B) ->vlan 80 
sw8 (6860-B) ->vlan 80 members port 1/1/1 untagged 
sw8 (6860-B) ->ip interface int_80 address 192.168.80.8/24 vlan 80 
sw8 (6860-B) ->interfaces 1/1/1 admin-state enable 
 
2.2. 
Configure connections between 6860-B and 6870-B 
 
- 
Configure a backbone VLAN 
 
sw2 (6870-B) -> vlan 228 
sw8 (6860-B) -> vlan 228 
 
- 
Create Link Aggregation 
 
sw2 (6870-B) -> linkagg lacp agg 28 size 2 actor admin-key 28 
sw2 (6870-B) -> linkagg lacp port 1/1/5 actor admin-key 28 
 
sw8 (6860-B) -> linkagg lacp agg 28 size 2 actor admin-key 28 
sw8 (6860-B) -> linkagg lacp port 1/1/5 actor admin-key 28 
 
- 
Assign Linkagg to VLAN 228  
- 
 
sw2 (6870-B) -> vlan 228 members linkagg 28 untagged 
 
sw8 (6860-B) -> vlan 228 members linkagg 28 untagged 
 
- 
Configure IP interface to VLAN 228 
- 
 
Sw2 (6870-B) -> ip interface int_228 address 172.16.28.2/24 vlan 228 
 
sw8 (6860-B) -> ip interface int_228 address 172.16.28.8/24 vlan 228 
 
 
 
 
- 
Enable interfaces

<<<PAGE 324>>>
5 
OSPF 
 
sw2 (6870-B) -> interfaces 1/1/5 admin-state enable 
 
sw8 (6860-B) -> interfaces 1/1/5 admin-state enable 
 
- 
Check that you can ping between 6860-B and 6900_B 
 
sw8 (6860-B) -> ping 172.16.28.2 
 
 3 
OSPF Backbone 
All OSPF networks must have an OSPF backbone area configured 
3.1. 
OSPF Backbone Logical Diagram 
 
 
 
3.2. 
Configuration 
- Enable OSPF protocol on 2 switches to advertise all local routes. In order to have a complete 
connectivity between all switches, OSPF will be used to advertise dynamically all the routes.  
 
- The first step is to load OSPF protocol and to enable OSPF on the newly created IP interfaces. As all 
OSPF networks must have a backbone area, this will be created with 0.0.0.0 as the area identifier. 
 
- Then, the relevant OSPF interfaces will be attached to the backbone. 
 
 
 
3.2.1. 
Loopback interface configuration

<<<PAGE 325>>>
6 
OSPF 
 
- Loopback0 is always advertised, even if there are no users on the switch; no route re-distribution is necessary. 
 
sw1 (6900-A) -> ip interface Loopback0 address 192.168.254.1 
 
sw7 (6870-A) -> ip interface Loopback0 address 192.168.254.7 
 
- Type the following on the 2 switches: 
 
-> ip load ospf 
 
- Let’s define the router-id and the backbone area on all switches: 
 
sw1 (6900-A) -> ip router router-id 192.168.254.1 
sw1 (6900-A) -> ip ospf area 0.0.0.0 
 
sw7 (6870-A) -> ip router router-id 192.168.254.7 
sw7 (6870-A) -> ip ospf area 0.0.0.0 
 
- Verify the configuration with the following commands: 
 
sw1 (6900-A) -> show ip ospf 
 
Router Id                        = 192.168.254.1, 
OSPF Version Number              = 2, 
Admin Status                     = Disabled, 
Area Border Router ?             = No, 
AS Border Router Status          = Disabled, 
Route Tag                        = 0, 
SPF Hold  Time (in seconds)      = 10, 
SPF Delay  Time (in seconds)     = 5, 
MTU Checking                     = Disabled, 
# of Routes                      = 0, 
# of AS-External LSAs            = 0, 
# of self-originated LSAs        = 0, 
# of LSAs received               = 0, 
External LSDB Limit              = -1, 
Exit Overflow Interval           = 0, 
# of SPF calculations done       = 0, 
# of Incr SPF calculations done  = 0, 
# of Init State Nbrs             = 0, 
# of 2-Way State Nbrs            = 0, 
# of Exchange State Nbrs         = 0, 
# of Full State Nbrs             = 0, 
# of attached areas              = 1, 
# of Active areas                = 0, 
# of Transit areas               = 0, 
# of attached NSSAs              = 0, 
Default Route Origination        = none, 
Default Route Metric-Type/Metric = type2 / 1, 
BFD Status                       = Disabled 
Opaque Transit Capability        = Enabled 
Redistribute internal BGP routes = Disabled 
 
sw1 (6900-A) -> show ip ospf area 0.0.0.0 
 
Area Identifier                          = 0.0.0.0, 
Admin Status                             = Enabled, 
Operational Status                       = Down, 
Area Type                                = normal, 
Area Summary                             = Enabled, 
Time since last SPF Run                  = 00h:06m:50s, 
# of Area Border Routers known           = 0, 
# of AS Border Routers known             = 0, 
# of Active Virtual Links                = 0, 
# of LSAs in area                        = 0, 
# of SPF Calculations done               = 0, 
# of Incremental SPF Calculations done   = 0,

<<<PAGE 326>>>
7 
OSPF 
 
# of Neighbors in Init State             = 0, 
# of Neighbors in 2-Way State            = 0, 
# of Neighbors in Exchange State         = 0, 
# of Neighbors in Full State             = 0, 
# of Interfaces attached                 = 0 
 
Attached Interfaces                      = 
 
- Verify that there are not any interfaces associated with the backbone area yet: 
 
sw1 (6900-A) -> show ip ospf interface 
    Interface                DR           Backup DR      Admin    Oper             BFD 
      Name                 Address         Address       Status  Status  State    Status 
---------------------+----------------+----------------+--------+------+-------+----------- 
 
- Repeat these commands on 6870-A to check your management. 
 
- Let’s assign the interfaces to the corresponding OSPF area. This is done in two steps. The first one is to 
enable the interfaces into OSPF, and then the interfaces are assigned to their corresponding area: 
 
sw1 (6900-A) -> ip ospf interface int_217 
sw1 (6900-A) -> ip ospf interface int_217 area 0.0.0.0 
sw1 (6900-A) -> ip ospf interface int_217 admin-state enable 
sw1 (6900-A) -> ip ospf admin-state enable 
 
sw7 (6870-A) -> ip ospf interface int_217 
sw7 (6870-A) -> ip ospf interface int_217 area 0.0.0.0 
sw7 (6870-A) -> ip ospf interface int_217 admin-state enable 
sw7 (6870-A) -> ip ospf admin-state enable

<<<PAGE 327>>>
8 
OSPF 
 
3.3. 
Verification 
 
- Now that the backbone area has been created on all switches, let’s verify some basic OSPF parameters 
on the 2 switches:   
 
sw1 (6900-A) -> show ip ospf 
Router Id                        = 192.168.254.1, 
OSPF Version Number              = 2, 
Admin Status                     = Enabled, 
Area Border Router ?             = No, 
AS Border Router Status          = Disabled, 
Route Tag                        = 0, 
SPF Hold  Time (in seconds)      = 10, 
SPF Delay  Time (in seconds)     = 5, 
MTU Checking                     = Disabled, 
# of Routes                      = 3, 
# of AS-External LSAs            = 0, 
# of self-originated LSAs        = 1, 
# of LSAs received               = 2, 
External LSDB Limit              = -1, 
Exit Overflow Interval           = 0, 
# of SPF calculations done       = 3, 
# of Incr SPF calculations done  = 0, 
# of Init State Nbrs             = 0, 
# of 2-Way State Nbrs            = 0, 
# of Exchange State Nbrs         = 0, 
# of Full State Nbrs             = 1, 
# of attached areas              = 1, 
# of Active areas                = 1, 
# of Transit areas               = 0, 
# of attached NSSAs              = 0, 
Default Route Origination        = none, 
Default Route Metric-Type/Metric = type2 / 1, 
BFD Status                       = Disabled 
Opaque Transit Capability        = Enabled 
Redistribute internal BGP routes = Disabled 
 
sw7 (6870-A) -> show ip ospf  
Router Id                        = 192.168.254.7, 
OSPF Version Number              = 2, 
Admin Status                     = Enabled, 
Area Border Router ?             = No, 
AS Border Router Status          = Disabled, 
Route Tag                        = 0, 
SPF Hold  Time (in seconds)      = 10, 
SPF Delay  Time (in seconds)     = 5, 
MTU Checking                     = Disabled, 
# of Routes                      = 3, 
# of AS-External LSAs            = 0, 
# of self-originated LSAs        = 2, 
# of LSAs received               = 1, 
External LSDB Limit              = -1, 
Exit Overflow Interval           = 0, 
# of SPF calculations done       = 3, 
# of Incr SPF calculations done  = 0, 
# of Init State Nbrs             = 0, 
# of 2-Way State Nbrs            = 0, 
# of Exchange State Nbrs         = 0, 
# of Full State Nbrs             = 1, 
# of attached areas              = 1, 
# of Active areas                = 1, 
# of Transit areas               = 0, 
# of attached NSSAs              = 0, 
Default Route Origination        = none, 
Default Route Metric-Type/Metric = type2 / 1, 
BFD Status                       = Disabled 
Opaque Transit Capability        = Enabled 
Redistribute internal BGP routes = Disabled

<<<PAGE 328>>>
9 
OSPF 
 
- Each switch has 1 neighbours in full state meaning there have been route updates exchanged between 
them. 
 
 
sw1 (6900-A) -> show ip ospf area 0.0.0.0 
Area Identifier                          = 0.0.0.0, 
Admin Status                             = Enabled, 
Operational Status                       = Up, 
Area Type                                = normal, 
Area Summary                             = Enabled, 
Time since last SPF Run                  = 00h:02m:40s, 
# of Area Border Routers known           = 0, 
# of AS Border Routers known             = 0, 
# of Active Virtual Links                = 0, 
# of LSAs in area                        = 3, 
# of SPF Calculations done               = 4, 
# of Incremental SPF Calculations done   = 0, 
# of Neighbors in Init State             = 0, 
# of Neighbors in 2-Way State            = 0, 
# of Neighbors in Exchange State         = 0, 
# of Neighbors in Full State             = 1, 
# of Interfaces attached                 = 1, 
Attached Interfaces                      = int_217 
 
 
 
Sw7 (6870-A) -> show ip ospf area 0.0.0.0 
Area Identifier                          = 0.0.0.0, 
Admin Status                             = Enabled, 
Operational Status                       = Up, 
Area Type                                = normal, 
Area Summary                             = Enabled, 
Time since last SPF Run                  = 01h:33m:24s, 
# of Area Border Routers known           = 2, 
# of AS Border Routers known             = 0, 
# of Active Virtual Links                = 0, 
# of LSAs in area                        = 8, 
# of SPF Calculations done               = 15, 
# of Incremental SPF Calculations done   = 0, 
# of Neighbors in Init State             = 0, 
# of Neighbors in 2-Way State            = 0, 
# of Neighbors in Exchange State         = 0, 
# of Neighbors in Full State             = 2, 
# of Interfaces attached                 = 2, 
Attached Interfaces                      = int_217 
 
- Now, let’s verify the routes that are seen by each switch.  
 
 
Notes 
The first command shows the routes learned by the switch using any static or dynamic routing protocol. This is 
the global routing table. In this example, only LOCAL and OSPF routes are present. 
The second one only shows the OSPF routes learned by the switch 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 5 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         23:50:27   LOCAL 
  172.16.12.0/24       172.16.12.1       23:48:39   LOCAL 
  172.16.17.0/24       172.16.17.1       23:48:36   LOCAL 
  192.168.254.1/32     192.168.254.1     18:42:00   LOCAL 
  192.168.254.7/32     172.16.17.7       18:31:05   OSPF 
 
sw1 (6900-A) -> show ip ospf routes  
 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type

<<<PAGE 329>>>
10 
OSPF 
 
---------------------+-----------------+--------+--------+--------+---------- 
172.16.17.0/24        172.16.17.1       1        Vlan     217        Intra 
192.168.254.1/32      0.0.0.0           0        N/A                 Intra 
192.168.254.7/32      172.16.17.7       1        Vlan     217        Intra 
 
sw7 (6870-A) -> show ip routes 
 
 
 + = Equal cost multipath routes 
 Total 8 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d20h   LOCAL 
  172.16.17.0/24       172.16.17.7          1d 0h   LOCAL 
  172.16.78.0/24       172.16.78.7          1d23h   LOCAL 
  192.168.20.0/24      192.168.20.7      23:51:30   LOCAL 
  192.168.30.0/24      192.168.30.7      20:40:51   LOCAL 
  192.168.70.0/24      192.168.70.7      20:08:47   LOCAL 
  192.168.254.1/32     172.16.17.1       19:35:34   OSPF 
  192.168.254.7/32     192.168.254.7     19:46:06   LOCAL 
 
sw7 (6870-A) -> show ip ospf routes 
 
Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
172.16.17.0/24        172.16.17.7       1        Vlan     217        Intra 
192.168.254.1/32      172.16.17.1       1        Vlan     217        Intra 
192.168.254.7/32      0.0.0.0           0        N/A                 Intra 
 
 
 
- Verify that all switches Loopback0 IP addresses are in the routing table. One is LOCAL to the switch 
whereas the other two are learned through OSPF. 
 
- Also verify that all other IP interfaces that were configured are also present in the routing table as 
well. 
 
- Type the following command to verify the Link State DataBase (LSDB) 
 
sw1 (6900-A) -> show ip ospf lsdb 
 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x8000002f    824 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x8000002f    818 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x8000002d    818 
- At this point, the LSDB should include 3 Link State Advertisements (LSA) 
 
- There are 2 routers in the network setup. Each router sends one LSA (rtr) 
 
- There are 1 network segments in the setup (VLANs 217) 
 
 
 
 
 
 
- There is a Designated Router elected on each network segment. This DR sends one LSA (net) 
- Remember that the switch with the highest priority, or in case of a tie, the highest router ID will be 
chosen as a Designated Router and the second highest will be the Backup DR. Let’s check the DR and 
BDR status on your switch:

<<<PAGE 330>>>
11 
OSPF 
 
sw1 (6900-A) -> show ip ospf interface 
 
 
    Interface          Domain   Domain         DR           Backup DR      Admin    Oper             BFD 
      Name              Name     ID          Address         Address       Status  Status  State    Status 
---------------------+--------+--------+----------------+----------------+--------+------+-------+--------
--- 
int_217               Vlan     217      172.16.17.7      172.16.17.1      enabled   up    BDR     disabled 
 
sw7 (6870-A) -> show ip ospf interface 
 
    Interface          Domain   Domain         DR           Backup DR      Admin    Oper             BFD 
      Name              Name     ID          Address         Address       Status  Status  State    Status 
---------------------+--------+--------+----------------+----------------+--------+------+-------+--------
--- 
int_217               Vlan     217      172.16.17.7      172.16.17.1      enabled   up    DR      disabled 
 
- Type the following to save your running configuration as the next labs are built on this configuration. 
  
-> write memory flash-synchro 
 
- You can also save your running configuration in a file on the flash that will be used for the OSPF virtual 
link lab. 
- Type the following on all Switches: 
 
-> configuration snapshot all save-ospf-backbone

<<<PAGE 331>>>
12 
OSPF 
 
 4 
OSPF Areas 
4.1. 
OSPF Areas Logical Diagram 
 
- This second part of the lab is designed to familiarize you with the configuration of an OSPF virtual link 
on an OmniSwitch. Virtual links can be used to create a virtual backbone connection on an OmniSwitch. 
 
The idea is to split the origin OSPF Backbone by forming two different independent OSPF Backbones 
and then by using the ospf virtual links, we will connect them back again. 
 
Switch1 will be configured with a virtual link to Switch 2 and Switch 7 will be configured with another 
virtual link to Switch 8. We will create two transit areas to connect the two ospf backbones. 
The area 1.1.1.1 using vlan 212 between the switches 1 and 2 and the area 2.2.2.2 using the vlan 278 
between the switches 7 and 8.

<<<PAGE 332>>>
13 
OSPF 
 
4.2. 
Configuration 
On the 6900-A and 6870-B create and configure Area 1.1.1.1: 
 
 
sw1 (6900-A) -> ip ospf area 1.1.1.1 
sw1 (6900-A) -> ip ospf interface int_212 
sw1 (6900-A) -> ip ospf interface int_212 area 1.1.1.1 
sw1 (6900-A) -> ip ospf interface int_212 admin-state enable 
 
sw2 (6870-B) -> ip load ospf 
sw2 (6870-B) -> ip interface Loopback0 address 192.168.254.2 
sw2 (6870-B) -> ip router router-id 192.168.254.2 
sw2 (6870-B) -> ip ospf area 1.1.1.1 
sw2 (6870-B) -> ip ospf interface int_212 
sw2 (6870-B) -> ip ospf interface int_212 area 1.1.1.1 
sw2 (6870-B) -> ip ospf interface int_212 admin-state enable 
sw2 (6870-B) -> ip ospf admin-state enable 
4.3. 
Verification 
- Verify the correct operation of the OSPF setup with the following commands: 
 
sw1 (6900-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
1.1.1.1           enabled      normal       up 
 
sw2 (6870-B) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
1.1.1.1           enabled      normal       up 
 
sw7 (6870-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
 
- Verify that the new routes have been learned by OSPF and are seen by switches:

<<<PAGE 333>>>
14 
OSPF 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 6 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            1d 1h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 1h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 1h   LOCAL 
  192.168.254.1/32     192.168.254.1     20:45:24   LOCAL 
  192.168.254.2/32     172.16.12.2       00:00:41   OSPF 
  192.168.254.7/32     172.16.17.7       20:34:29   OSPF 
 
sw2 (6870-B) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 8 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d21h   LOCAL 
  172.16.12.0/24       172.16.12.2          1d 1h   LOCAL 
  172.16.17.0/24       172.16.12.1       00:01:17   OSPF 
  172.16.28.0/24       172.16.28.2       21:03:12   LOCAL 
  192.168.120.0/24     192.168.120.2     21:09:07   LOCAL 
  192.168.254.1/32     172.16.12.1       00:01:17   OSPF 
  192.168.254.2/32     192.168.254.2     00:03:47   LOCAL 
  192.168.254.7/32     172.16.12.1       00:01:17   OSPF 
 
 
sw7 (6870-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 10 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d21h   LOCAL 
  172.16.12.0/24       172.16.17.1       00:07:47   OSPF 
  172.16.17.0/24       172.16.17.7          1d 1h   LOCAL 
  172.16.78.0/24       172.16.78.7          2d 0h   LOCAL 
  192.168.20.0/24      192.168.20.7         1d 0h   LOCAL 
  192.168.30.0/24      192.168.30.7      21:44:22   LOCAL 
  192.168.70.0/24      192.168.70.7      21:12:18   LOCAL 
  192.168.254.1/32     172.16.17.1       20:39:05   OSPF 
  192.168.254.2/32     172.16.17.1       00:05:09   OSPF 
  192.168.254.7/32     192.168.254.7     20:49:37   LOCAL 
 
 
- Verify that in the LSDB new LSAs have been added (sumnet). These LSAs have the information of the 
networks that belong to a different area: 
 
sw1 (6900-A) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x80000032    365 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000031   1201 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x8000002f   1201 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000003    201 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x80000002    186 
1.1.1.1          rtr     192.168.254.1    192.168.254.1    0x80000004    196 
1.1.1.1          rtr     192.168.254.2    192.168.254.2    0x80000002    207 
1.1.1.1          net     172.16.12.1      192.168.254.1    0x80000002    196 
1.1.1.1          sumnet  172.16.17.0      192.168.254.1    0x80000001    360 
1.1.1.1          sumnet  192.168.254.7    192.168.254.1    0x80000002    200 
 
sw2 (6870-B) -> show ip ospf lsdb

<<<PAGE 334>>>
15 
OSPF 
 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
1.1.1.1          rtr     192.168.254.1    192.168.254.1    0x80000004    254 
1.1.1.1          rtr     192.168.254.2    192.168.254.2    0x80000002    262 
1.1.1.1          net     172.16.12.1      192.168.254.1    0x80000002    254 
1.1.1.1          sumnet  172.16.17.0      192.168.254.1    0x80000001    418 
1.1.1.1          sumnet  192.168.254.7    192.168.254.1    0x80000002    257 
 
sw7 (6870-A) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x80000032    580 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000031   1414 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x8000002f   1414 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000003    415 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x80000002    400 
4.4. 
Configuration 
On the 6870-A and 6860-B create and configure Area 2.2.2.2: 
 
 
sw7 (6870-A) -> ip ospf area 2.2.2.2 
sw7 (6870-A) -> ip ospf interface int_278 
sw7 (6870-A) -> ip ospf interface int_278 area 2.2.2.2 
sw7 (6870-A) -> ip ospf interface int_278 admin-state enable 
 
sw8 (6860-B) -> ip load ospf 
sw8 (6860-B) -> ip interface Loopback0 address 192.168.254.8 
sw8 (6860-B) -> ip router router-id 192.168.254.8 
sw8 (6860-B) -> ip ospf area 2.2.2.2 
sw8 (6860-B) -> ip ospf interface int_278 
sw8 (6860-B) -> ip ospf interface int_278 area 2.2.2.2 
sw8 (6860-B) -> ip ospf interface int_278 admin-state enable 
sw8 (6860-B) -> ip ospf admin-state enable 
4.5. 
Verification 
- Verify the correct operation of the OSPF setup with the following commands: 
 
sw7 (6870-A) -> show ip ospf area

<<<PAGE 335>>>
16 
OSPF 
 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
2.2.2.2           enabled      normal       up 
 
sw8 (6860-B) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
2.2.2.2           enabled      normal       up 
 
sw1 (6900-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
1.1.1.1           enabled      normal       up 
 
sw2 (6870-B) -> sh ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
1.1.1.1           enabled      normal       up 
 
 
- Verify that the new routes have been learned by OSPF and are seen by switches: 
 
sw1 (6900-A) -> show ip routes 
 
+ = Equal cost multipath routes 
 Total 8 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            1d 2h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 2h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 2h   LOCAL 
  172.16.78.0/24       172.16.17.7       00:17:23   OSPF 
  192.168.254.1/32     192.168.254.1     21:15:14   LOCAL 
  192.168.254.2/32     172.16.12.2       00:30:31   OSPF 
  192.168.254.7/32     172.16.17.7       21:04:19   OSPF 
  192.168.254.8/32     172.16.17.7       00:14:45   OSPF 
 
sw2 (6870-B) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 10 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d22h   LOCAL 
  172.16.12.0/24       172.16.12.2          1d 2h   LOCAL 
  172.16.17.0/24       172.16.12.1       00:34:18   OSPF 
  172.16.28.0/24       172.16.28.2       21:36:13   LOCAL 
  172.16.78.0/24       172.16.12.1       00:21:14   OSPF 
  192.168.120.0/24     192.168.120.2     21:42:08   LOCAL 
  192.168.254.1/32     172.16.12.1       00:34:18   OSPF 
  192.168.254.2/32     192.168.254.2     00:36:48   LOCAL 
  192.168.254.7/32     172.16.12.1       00:34:18   OSPF 
  192.168.254.8/32     172.16.12.1       00:18:36   OSPF

<<<PAGE 336>>>
17 
OSPF 
 
sw7 (6870-A) -> show ip routes 
+ = Equal cost multipath routes 
 Total 11 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d22h   LOCAL 
  172.16.12.0/24       172.16.17.1       00:38:23   OSPF 
  172.16.17.0/24       172.16.17.7          1d 2h   LOCAL 
  172.16.78.0/24       172.16.78.7          2d 1h   LOCAL 
  192.168.20.0/24      192.168.20.7         1d 1h   LOCAL 
  192.168.30.0/24      192.168.30.7      22:14:58   LOCAL 
  192.168.70.0/24      192.168.70.7      21:42:54   LOCAL 
  192.168.254.1/32     172.16.17.1       21:09:41   OSPF 
  192.168.254.2/32     172.16.17.1       00:35:45   OSPF 
  192.168.254.7/32     192.168.254.7     21:20:13   LOCAL 
  192.168.254.8/32     172.16.78.8       00:20:00   OSPF 
 
 
sw8 (6860-B) -> show ip routes 
+ = Equal cost multipath routes 
 Total 12 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d21h   LOCAL 
  172.16.12.0/24       172.16.78.7       00:15:35   OSPF 
  172.16.17.0/24       172.16.78.7       00:15:35   OSPF 
  172.16.28.0/24       172.16.28.8       21:33:14   LOCAL 
  172.16.78.0/24       172.16.78.8          2d 1h   LOCAL 
  192.168.20.0/24      192.168.20.8      22:07:18   LOCAL 
  192.168.30.0/24      192.168.30.8         1d 1h   LOCAL 
  192.168.80.0/24      192.168.80.8      21:38:05   LOCAL 
  192.168.254.1/32     172.16.78.7       00:15:35   OSPF 
  192.168.254.2/32     172.16.78.7       00:15:35   OSPF 
  192.168.254.7/32     172.16.78.7       00:15:35   OSPF 
  192.168.254.8/32     192.168.254.8     00:16:58   LOCAL 
 
 
- Verify that in the LSDB new LSAs have been added (sumnet). These LSAs have the information of the 
networks that belong to a different area: 
 
sw1 (6900-A) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x80000035   1195 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000036    290 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x80000033    470 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000006   1015 
0.0.0.0          sumnet  172.16.78.0      192.168.254.7    0x80000006    111 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x80000006    295 
0.0.0.0          sumnet  192.168.254.8    192.168.254.7    0x80000005    111 
1.1.1.1          rtr     192.168.254.1    192.168.254.1    0x80000007   1076 
1.1.1.1          rtr     192.168.254.2    192.168.254.2    0x80000005    926 
1.1.1.1          net     172.16.12.1      192.168.254.1    0x80000005   1076 
1.1.1.1          sumnet  172.16.17.0      192.168.254.1    0x80000004   1195 
1.1.1.1          sumnet  172.16.78.0      192.168.254.1    0x80000005    115 
1.1.1.1          sumnet  192.168.254.7    192.168.254.1    0x80000006    295 
1.1.1.1          sumnet  192.168.254.8    192.168.254.1    0x80000004    115 
 
sw2 (6870-B) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
1.1.1.1          rtr     192.168.254.1    192.168.254.1    0x80000007   1110 
1.1.1.1          rtr     192.168.254.2    192.168.254.2    0x80000005    959 
1.1.1.1          net     172.16.12.1      192.168.254.1    0x80000005   1110 
1.1.1.1          sumnet  172.16.17.0      192.168.254.1    0x80000004   1230 
1.1.1.1          sumnet  172.16.78.0      192.168.254.1    0x80000005    150 
1.1.1.1          sumnet  192.168.254.7    192.168.254.1    0x80000006    330 
1.1.1.1          sumnet  192.168.254.8    192.168.254.1    0x80000004    150

<<<PAGE 337>>>
18 
OSPF 
 
 
sw7 (6870-A) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x80000035   1317 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000036    411 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x80000033    591 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000006   1138 
0.0.0.0          sumnet  172.16.78.0      192.168.254.7    0x80000006    231 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x80000006    418 
0.0.0.0          sumnet  192.168.254.8    192.168.254.7    0x80000005    231 
2.2.2.2          rtr     192.168.254.7    192.168.254.7    0x80000007    137 
2.2.2.2          rtr     192.168.254.8    192.168.254.8    0x80000005    100 
2.2.2.2          net     172.16.78.7      192.168.254.7    0x80000005    137 
2.2.2.2          sumnet  172.16.12.0      192.168.254.7    0x80000008    231 
2.2.2.2          sumnet  172.16.17.0      192.168.254.7    0x80000004    411 
2.2.2.2          sumnet  192.168.254.1    192.168.254.7    0x80000005    231 
2.2.2.2          sumnet  192.168.254.2    192.168.254.7    0x80000008    231 
 
sw8 (6860-B) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
2.2.2.2          rtr     192.168.254.7    192.168.254.7    0x80000007     92 
2.2.2.2          rtr     192.168.254.8    192.168.254.8    0x80000005     54 
2.2.2.2          net     172.16.78.7      192.168.254.7    0x80000005     92 
2.2.2.2          sumnet  172.16.12.0      192.168.254.7    0x80000008    187 
2.2.2.2          sumnet  172.16.17.0      192.168.254.7    0x80000004    367 
2.2.2.2          sumnet  192.168.254.1    192.168.254.7    0x80000005    187 
2.2.2.2          sumnet  192.168.254.2    192.168.254.7    0x80000008    187 
4.6. 
Virtual-link configuration (on both switches) 
 
- With the commands above, we have created the transit areas and attached the relevant interfaces to 
them. The next step is to configure the ospf virtual links using these ospf interfaces and areas. 
 
 
4.6.1. 
Configure the backbone area on switch 6870-B and 6860-B

<<<PAGE 338>>>
19 
OSPF 
 
sw2 (6870-B) -> ip ospf interface int_228 
sw2 (6870-B) -> ip ospf interface int_228 area 0.0.0.0 
sw2 (6870-B) -> ip ospf interface int_228 admin-state enable 
 
sw8 (6860-B) -> ip ospf interface int_228 
sw8 (6860-B) -> ip ospf interface int_228 area 0.0.0.0 
sw8 (6860-B) -> ip ospf interface int_228 admin-state enable 
4.6.2. 
Create Virtual-link  
 
sw1 (6900-A) -> ip ospf virtual-link 1.1.1.1 192.168.254.2 
- Where 192.168.254.2 is the Switch2 (6870-B) Loopback0 address, and it’s configured as the Switch2 
router-id. 
 
sw2 (6870-B) -> ip ospf virtual-link 1.1.1.1 192.168.254.1 
- Where 192.168.254.1 is the Switch1 (6900-A) Loopback0 address, and it’s configured as the Switch1 
router-id. 
 
sw7 (6870-A) -> ip ospf virtual-link 2.2.2.2 192.168.254.8 
- Where 192.168.254.8 is the Switch2 (6860-B) Loopback0 address, and it’s configured as the Switch8 
router-id. 
 
sw8 (6860-B) -> ip ospf virtual-link 2.2.2.2 192.168.254.7 
- Where 192.168.254.7 is the Switch7 (6870-A) Loopback0 address, and it’s configured as the Switch7 
router-id. 
 
4.6.3. 
Verify the working of the virtual-link 
 
sw1 (6900-A) -> show ip ospf virtual-link 
                                       State 
 Transit AreaId      Router-id    Link / Adjacency  AuthType   OperStatus 
----------------+----------------+----------------+----------+------------ 
1.1.1.1           192.168.254.2    P2P  / Full       none        up 
 
sw2 (6870-B) -> show ip ospf virtual-link 
                                       State 
 Transit AreaId      Router-id    Link / Adjacency  AuthType   OperStatus 
----------------+----------------+----------------+----------+------------ 
1.1.1.1           192.168.254.1    P2P  / Full       none        up 
 
sw7 (6870-A) -> show ip ospf virtual-link 
                                       State 
 Transit AreaId      Router-id    Link / Adjacency  AuthType   OperStatus 
----------------+----------------+----------------+----------+------------ 
2.2.2.2           192.168.254.8    P2P  / Full       none        up 
 
sw8 (6860-B) -> show ip ospf virtual-link 
                                       State 
 Transit AreaId      Router-id    Link / Adjacency  AuthType   OperStatus 
----------------+----------------+----------------+----------+------------ 
2.2.2.2           192.168.254.7    P2P  / Full       none        up 
 
Check connectivity to all routing instances throughout the network. 
 
sw1 (6900-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------

<<<PAGE 339>>>
20 
OSPF 
 
0.0.0.0           enabled      normal       up 
1.1.1.1           enabled      normal       up 
 
sw2 (6870-B) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
1.1.1.1           enabled      normal       up 
 
sw7 (6870-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
2.2.2.2           enabled      normal       up 
 
sw8 (6860-B) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
2.2.2.2           enabled      normal       up 
 
sw1 (6900-A) -> show ip ospf interface 
    Interface          Domain   Domain         DR           Backup DR      Admin    Oper             BFD 
      Name              Name     ID          Address         Address       Status  Status  State    Status 
---------------------+--------+--------+----------------+----------------+--------+------+-------+-------- 
int_212               Vlan     212      172.16.12.1      172.16.12.2      enabled   up    DR      disabled 
int_217               Vlan     217      172.16.17.7      172.16.17.1      enabled   up    BDR     disabled 
 
sw2 (6870-B) -> show ip ospf interface 
    Interface          Domain   Domain         DR           Backup DR      Admin    Oper             BFD 
      Name              Name     ID          Address         Address       Status  Status  State    Status 
---------------------+--------+--------+----------------+----------------+--------+------+-------+-------- 
int_212               Vlan     212      172.16.12.1      172.16.12.2      enabled   up    BDR     disabled 
int_228               Vlan     228      172.16.28.2      172.16.28.8      enabled   up    DR      disabled 
 
sw7 (6870-A) -> show ip ospf interface 
    Interface          Domain   Domain         DR           Backup DR      Admin    Oper             BFD 
      Name              Name     ID          Address         Address       Status  Status  State    Status 
---------------------+--------+--------+----------------+----------------+--------+------+-------+-------- 
int_217               Vlan     217      172.16.17.7      172.16.17.1      enabled   up    DR      disabled 
int_278               Vlan     278      172.16.78.7      172.16.78.8      enabled   up    DR      disabled 
 
sw8 (6860-B) -> show ip ospf interface 
    Interface          Domain   Domain         DR           Backup DR      Admin    Oper             BFD 
      Name              Name     ID          Address         Address       Status  Status  State    Status 
---------------------+--------+--------+----------------+----------------+--------+------+-------+-------- 
int_228               Vlan     228      172.16.28.2      172.16.28.8      enabled   up    BDR     disabled 
int_278               Vlan     278      172.16.78.7      172.16.78.8      enabled   up    BDR     disabled 
 
sw1 (6900-A) -> show ip ospf route 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
172.16.12.0/24        172.16.12.1       1        Vlan     212        Intra 
172.16.17.0/24        172.16.17.1       1        Vlan     217        Intra 
172.16.28.0/24        172.16.12.2       2        Vlan     212        Intra 
172.16.78.0/24        172.16.17.7       2        Vlan     217        Inter 
192.168.254.1/32      0.0.0.0           0        N/A                 Intra 
192.168.254.2/32      172.16.12.2       1        Vlan     212        Intra 
192.168.254.7/32      172.16.17.7       1        Vlan     217        Intra 
192.168.254.8/32      172.16.12.2       2        Vlan     212        Intra 
192.168.254.8/32      172.16.17.7       2        Vlan     217        Intra 
 
sw2 (6870-B) -> show ip ospf route 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type

<<<PAGE 340>>>
21 
OSPF 
 
---------------------+-----------------+--------+--------+--------+---------- 
172.16.12.0/24        172.16.12.2       1        Vlan     212        Intra 
172.16.17.0/24        172.16.12.1       2        Vlan     212        Intra 
172.16.28.0/24        172.16.28.2       1        Vlan     228        Intra 
172.16.78.0/24        172.16.28.8       2        Vlan     228        Inter 
192.168.254.1/32      172.16.12.1       1        Vlan     212        Intra 
192.168.254.2/32      0.0.0.0           0        N/A                 Intra 
192.168.254.7/32      172.16.12.1       2        Vlan     212        Intra 
192.168.254.7/32      172.16.28.8       2        Vlan     228        Intra 
192.168.254.8/32      172.16.28.8       1        Vlan     228        Intra 
 
sw7 (6870-A) -> show ip ospf route 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
172.16.12.0/24        172.16.17.1       2        Vlan     217        Inter 
172.16.17.0/24        172.16.17.7       1        Vlan     217        Intra 
172.16.28.0/24        172.16.78.8       2        Vlan     278        Intra 
172.16.78.0/24        172.16.78.7       1        Vlan     278        Intra 
192.168.254.1/32      172.16.17.1       1        Vlan     217        Intra 
192.168.254.2/32      172.16.78.8       2        Vlan     278        Intra 
192.168.254.2/32      172.16.17.1       2        Vlan     217        Intra 
192.168.254.7/32      0.0.0.0           0        N/A                 Intra 
192.168.254.8/32      172.16.78.8       1        Vlan     278        Intra 
 
sw8 (6860-B) -> show ip ospf route 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
172.16.12.0/24        172.16.28.2       2        Vlan     228        Inter 
172.16.17.0/24        172.16.78.7       2        Vlan     278        Intra 
172.16.28.0/24        172.16.28.8       1        Vlan     228        Intra 
172.16.78.0/24        172.16.78.8       1        Vlan     278        Intra 
192.168.254.1/32      172.16.78.7       2        Vlan     278        Intra 
192.168.254.1/32      172.16.28.2       2        Vlan     228        Intra 
192.168.254.2/32      172.16.28.2       1        Vlan     228        Intra 
192.168.254.7/32      172.16.78.7       1        Vlan     278        Intra 
192.168.254.8/32      0.0.0.0           0        N/A                 Intra 
 
sw1 (6900-A) -> show ip routes 
 + = Equal cost multipath routes 
 Total 10 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            1d 4h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 4h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 4h   LOCAL 
  172.16.28.0/24       172.16.12.2       00:06:59   OSPF 
  172.16.78.0/24       172.16.17.7       02:14:28   OSPF 
  192.168.254.1/32     192.168.254.1     23:12:19   LOCAL 
  192.168.254.2/32     172.16.12.2       02:27:36   OSPF 
  192.168.254.7/32     172.16.17.7       23:01:24   OSPF 
  192.168.254.8/32    +172.16.12.2       00:06:12   OSPF 
                      +172.16.17.7       02:11:50   OSPF

<<<PAGE 341>>>
22 
OSPF 
 
 
sw2 (6870-B) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 11 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d23h   LOCAL 
  172.16.12.0/24       172.16.12.2          1d 4h   LOCAL 
  172.16.17.0/24       172.16.12.1       00:31:41   OSPF 
  172.16.28.0/24       172.16.28.2       23:30:12   LOCAL 
  172.16.78.0/24       172.16.28.8       00:06:52   OSPF 
  192.168.120.0/24     192.168.120.2     23:36:07   LOCAL 
  192.168.254.1/32     172.16.12.1       02:28:17   OSPF 
  192.168.254.2/32     192.168.254.2     02:30:47   LOCAL 
  192.168.254.7/32    +172.16.12.1       00:31:41   OSPF 
                      +172.16.28.8       00:06:52   OSPF 
  192.168.254.8/32     172.16.28.8       00:06:52   OSPF 
 
sw7 (6870-A) -> sh ip routes 
 
 + = Equal cost multipath routes 
 Total 13 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d23h   LOCAL 
  172.16.12.0/24       172.16.17.1       02:31:16   OSPF 
  172.16.17.0/24       172.16.17.7          1d 4h   LOCAL 
  172.16.28.0/24       172.16.78.8       00:07:15   OSPF 
  172.16.78.0/24       172.16.78.7          2d 3h   LOCAL 
  192.168.20.0/24      192.168.20.7         1d 3h   LOCAL 
  192.168.30.0/24      192.168.30.7         1d 0h   LOCAL 
  192.168.70.0/24      192.168.70.7      23:35:47   LOCAL 
  192.168.254.1/32     172.16.17.1       23:02:34   OSPF 
  192.168.254.2/32    +172.16.17.1       02:28:38   OSPF 
                      +172.16.78.8       00:07:15   OSPF 
  192.168.254.7/32     192.168.254.7     23:13:06   LOCAL 
  192.168.254.8/32     172.16.78.8       02:12:53   OSPF 
 
sw8 (6860-B) -> sh ip routes 
 
 + = Equal cost multipath routes 
 Total 13 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            5d23h   LOCAL 
  172.16.12.0/24       172.16.28.2       00:07:30   OSPF 
  172.16.17.0/24       172.16.78.7       00:28:57   OSPF 
  172.16.28.0/24       172.16.28.8       23:30:43   LOCAL 
  172.16.78.0/24       172.16.78.8          2d 3h   LOCAL 
  192.168.20.0/24      192.168.20.8         1d 0h   LOCAL 
  192.168.30.0/24      192.168.30.8         1d 3h   LOCAL 
  192.168.80.0/24      192.168.80.8      23:35:34   LOCAL 
  192.168.254.1/32    +172.16.28.2       00:07:30   OSPF 
                      +172.16.78.7       00:28:57   OSPF 
  192.168.254.2/32     172.16.28.2       00:07:30   OSPF 
  192.168.254.7/32     172.16.78.7       02:13:04   OSPF 
  192.168.254.8/32     192.168.254.8     02:14:27   LOCAL

<<<PAGE 342>>>
23 
OSPF 
 
4.7. 
Let’s add VLANs 20 and 30 into our OSPF network in Area 3.3.3.3 
 
 
 
 
 
4.8. 
On the 6870-A and 6860N create and configure Area 3.3.3.3: 
 
sw7 (6870-A) -> ip ospf area 3.3.3.3 
sw7 (6870-A) -> ip ospf interface int_20 
sw7 (6870-A) -> ip ospf interface int_20 area 3.3.3.3 
sw7 (6870-A) -> ip ospf interface int_20 admin-state enable 
sw7 (6870-A) -> ip ospf interface int_30 
sw7 (6870-A) -> ip ospf interface int_30 area 3.3.3.3 
sw7 (6870-A) -> ip ospf interface int_30 admin-state enable 
 
sw8 (6860-B) -> ip ospf area 3.3.3.3 
sw8 (6860-B) -> ip ospf interface int_30 
sw8 (6860-B) -> ip ospf interface int_30 area 3.3.3.3 
sw8 (6860-B) -> ip ospf interface int_30 admin-state enable 
sw8 (6860-B) -> ip ospf interface int_20 
sw8 (6860-B) -> ip ospf interface int_20 area 3.3.3.3 
sw8 (6860-B) -> ip ospf interface int_20 admin-state enable

<<<PAGE 343>>>
24 
OSPF 
 
4.9. 
Verify the correct operation of the OSPF setup with the following commands: 
 
sw1 (6900-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
1.1.1.1           enabled      normal       up 
 
sw2 (6870-B) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
1.1.1.1           enabled      normal       up 
 
sw7 (6870-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
2.2.2.2           enabled      normal       up 
3.3.3.3           enabled      normal       up 
 
sw8 (6860-B) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
2.2.2.2           enabled      normal       up 
3.3.3.3           enabled      normal       up 
 
- Verify that the new routes have been learned by OSPF and are seen by all switches: 
 
sw1 (6900-A) -> show ip routes 
 
+ = Equal cost multipath routes 
 Total 12 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            1d 4h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 4h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 4h   LOCAL 
  172.16.28.0/24       172.16.12.2       00:27:15   OSPF 
  172.16.78.0/24       172.16.17.7       02:34:44   OSPF 
  192.168.20.0/24      172.16.17.7       00:05:47   OSPF 
  192.168.30.0/24      172.16.17.7       00:05:32   OSPF 
  192.168.254.1/32     192.168.254.1     23:32:35   LOCAL 
  192.168.254.2/32     172.16.12.2       02:47:52   OSPF 
  192.168.254.7/32     172.16.17.7       23:21:40   OSPF 
  192.168.254.8/32    +172.16.12.2       00:26:28   OSPF 
                      +172.16.17.7       02:32:06   OSPF 
 
sw2 (6870-B) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 13 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            6d 0h   LOCAL 
  172.16.12.0/24       172.16.12.2          1d 4h   LOCAL 
  172.16.17.0/24       172.16.12.1       00:52:02   OSPF 
  172.16.28.0/24       172.16.28.2       23:50:33   LOCAL 
  172.16.78.0/24       172.16.28.8       00:27:13   OSPF 
  192.168.20.0/24      172.16.28.8       00:06:37   OSPF 
                        
  192.168.30.0/24      172.16.28.8       00:06:23   OSPF 
  192.168.120.0/24     192.168.120.2     23:56:28   LOCAL 
  192.168.254.1/32     172.16.12.1       02:48:38   OSPF 
  192.168.254.2/32     192.168.254.2     02:51:08   LOCAL 
  192.168.254.7/32    +172.16.12.1       00:52:02   OSPF

<<<PAGE 344>>>
25 
OSPF 
 
                      +172.16.28.8       00:27:13   OSPF 
  192.168.254.8/32     172.16.28.8       00:27:13   OSP 
 
sw7 (6870-A) -> show ip routes 
 
+ = Equal cost multipath routes 
 Total 13 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            6d 0h   LOCAL 
  172.16.12.0/24       172.16.17.1       02:51:51   OSPF 
  172.16.17.0/24       172.16.17.7          1d 4h   LOCAL 
  172.16.28.0/24       172.16.78.8       00:27:50   OSPF 
  172.16.78.0/24       172.16.78.7          2d 3h   LOCAL 
  192.168.20.0/24      192.168.20.7         1d 3h   LOCAL 
  192.168.30.0/24      192.168.30.7         1d 0h   LOCAL 
  192.168.70.0/24      192.168.70.7      23:56:22   LOCAL 
  192.168.254.1/32     172.16.17.1       23:23:09   OSPF 
  192.168.254.2/32    +172.16.17.1       02:49:13   OSPF 
                      +172.16.78.8       00:27:50   OSPF 
  192.168.254.7/32     192.168.254.7     23:33:41   LOCAL 
  192.168.254.8/32     172.16.78.8       02:33:28   OSPF 
 
sw8 (6860-B) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 13 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            6d 0h   LOCAL 
  172.16.12.0/24       172.16.28.2       00:28:21   OSPF 
  172.16.17.0/24       172.16.78.7       00:49:48   OSPF 
  172.16.28.0/24       172.16.28.8       23:51:34   LOCAL 
  172.16.78.0/24       172.16.78.8          2d 3h   LOCAL 
  192.168.20.0/24      192.168.20.8         1d 0h   LOCAL 
  192.168.30.0/24      192.168.30.8         1d 3h   LOCAL 
  192.168.80.0/24      192.168.80.8      23:56:25   LOCAL 
  192.168.254.1/32    +172.16.28.2       00:28:21   OSPF 
                      +172.16.78.7       00:49:48   OSPF 
  192.168.254.2/32     172.16.28.2       00:28:21   OSPF 
  192.168.254.7/32     172.16.78.7       02:33:55   OSPF 
  192.168.254.8/32     192.168.254.8     02:35:18   LOCAL 
 
- Verify that in the LSDB new LSAs have been added (sumnet). These LSAs have the information of the 
networks that belong to a different area: 
 
sw1 (6900-A) -> show ip ospf lsdb 
 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x80000039   1522 
0.0.0.0          rtr     192.168.254.2    192.168.254.2    0x80000007     14 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000039   1337 
0.0.0.0          rtr     192.168.254.8    192.168.254.8    0x80000004   1757 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x80000035   1517 
0.0.0.0          net     172.16.28.2      192.168.254.2    0x80000003     14 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000009    442 
0.0.0.0          sumnet  172.16.12.0      192.168.254.2    0x80000002   1614 
0.0.0.0          sumnet  172.16.78.0      192.168.254.7    0x80000008   1158 
0.0.0.0          sumnet  172.16.78.0      192.168.254.8    0x80000002   1387 
0.0.0.0          sumnet  192.168.20.0     192.168.254.7    0x80000003    373 
0.0.0.0          sumnet  192.168.20.0     192.168.254.8    0x80000003    348 
0.0.0.0          sumnet  192.168.30.0     192.168.254.7    0x80000003    373 
0.0.0.0          sumnet  192.168.30.0     192.168.254.8    0x80000002    380 
0.0.0.0          sumnet  192.168.254.1    192.168.254.2    0x80000004   1747 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x8000000d     82 
0.0.0.0          sumnet  192.168.254.7    192.168.254.8    0x80000005    504 
0.0.0.0          sumnet  192.168.254.8    192.168.254.7    0x8000000c    514

<<<PAGE 345>>>
26 
OSPF 
 
1.1.1.1          rtr     192.168.254.1    192.168.254.1    0x8000000b   1583 
1.1.1.1          rtr     192.168.254.2    192.168.254.2    0x80000009   1613 
1.1.1.1          net     172.16.12.1      192.168.254.1    0x80000008    503 
1.1.1.1          sumnet  172.16.17.0      192.168.254.1    0x80000007    622 
1.1.1.1          sumnet  172.16.17.0      192.168.254.2    0x80000002   1614 
1.1.1.1          sumnet  172.16.28.0      192.168.254.1    0x80000003     82 
1.1.1.1          sumnet  172.16.28.0      192.168.254.2    0x80000003   1748 
1.1.1.1          sumnet  172.16.78.0      192.168.254.1    0x80000010     82 
1.1.1.1          sumnet  172.16.78.0      192.168.254.2    0x80000009   1737 
1.1.1.1          sumnet  192.168.20.0     192.168.254.1    0x80000002    417 
1.1.1.1          sumnet  192.168.20.0     192.168.254.2    0x80000002    418 
1.1.1.1          sumnet  192.168.30.0     192.168.254.1    0x80000002    417 
1.1.1.1          sumnet  192.168.30.0     192.168.254.2    0x80000002    418 
1.1.1.1          sumnet  192.168.254.7    192.168.254.1    0x8000000c     82 
1.1.1.1          sumnet  192.168.254.7    192.168.254.2    0x80000007   1737 
1.1.1.1          sumnet  192.168.254.8    192.168.254.1    0x8000000b     82 
1.1.1.1          sumnet  192.168.254.8    192.168.254.2    0x80000007   1737 
 
sw2 (6870-B) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x80000039   1614 
0.0.0.0          rtr     192.168.254.2    192.168.254.2    0x80000007    105 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000039   1429 
0.0.0.0          rtr     192.168.254.8    192.168.254.8    0x80000005     89 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x80000035   1609 
0.0.0.0          net     172.16.28.2      192.168.254.2    0x80000003    105 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000009    535 
0.0.0.0          sumnet  172.16.12.0      192.168.254.2    0x80000003     84 
0.0.0.0          sumnet  172.16.78.0      192.168.254.7    0x80000008   1250 
0.0.0.0          sumnet  172.16.78.0      192.168.254.8    0x80000002   1478 
0.0.0.0          sumnet  192.168.20.0     192.168.254.7    0x80000003    530 
0.0.0.0          sumnet  192.168.20.0     192.168.254.8    0x80000003    503 
0.0.0.0          sumnet  192.168.30.0     192.168.254.7    0x80000003    530 
0.0.0.0          sumnet  192.168.30.0     192.168.254.8    0x80000002    535 
0.0.0.0          sumnet  192.168.254.1    192.168.254.2    0x80000005     84 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x8000000d    175 
0.0.0.0          sumnet  192.168.254.7    192.168.254.8    0x80000005    595 
0.0.0.0          sumnet  192.168.254.8    192.168.254.7    0x8000000c    606 
1.1.1.1          rtr     192.168.254.1    192.168.254.1    0x8000000c     55 
1.1.1.1          rtr     192.168.254.2    192.168.254.2    0x8000000a     84 
1.1.1.1          net     172.16.12.1      192.168.254.1    0x80000008    595 
1.1.1.1          sumnet  172.16.17.0      192.168.254.1    0x80000007    715 
1.1.1.1          sumnet  172.16.17.0      192.168.254.2    0x80000003     84 
1.1.1.1          sumnet  172.16.28.0      192.168.254.1    0x80000003    175 
1.1.1.1          sumnet  172.16.28.0      192.168.254.2    0x80000004     84 
1.1.1.1          sumnet  172.16.78.0      192.168.254.1    0x80000010    175 
1.1.1.1          sumnet  172.16.78.0      192.168.254.2    0x8000000a     84 
1.1.1.1          sumnet  192.168.20.0     192.168.254.1    0x80000002    573 
1.1.1.1          sumnet  192.168.20.0     192.168.254.2    0x80000002    573 
1.1.1.1          sumnet  192.168.30.0     192.168.254.1    0x80000002    573 
1.1.1.1          sumnet  192.168.30.0     192.168.254.2    0x80000002    573 
1.1.1.1          sumnet  192.168.254.7    192.168.254.1    0x8000000c    175 
1.1.1.1          sumnet  192.168.254.7    192.168.254.2    0x80000008     84 
1.1.1.1          sumnet  192.168.254.8    192.168.254.1    0x8000000b    175 
1.1.1.1          sumnet  192.168.254.8    192.168.254.2    0x80000008     84

<<<PAGE 346>>>
27 
OSPF 
 
 
sw7 (6870-A) -> show ip ospf lsdb 
 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x8000003a     62 
0.0.0.0          rtr     192.168.254.2    192.168.254.2    0x80000007    174 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000039   1496 
0.0.0.0          rtr     192.168.254.8    192.168.254.8    0x80000005    157 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x80000036     56 
0.0.0.0          net     172.16.28.2      192.168.254.2    0x80000003    174 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000009    603 
0.0.0.0          sumnet  172.16.12.0      192.168.254.2    0x80000003    154 
0.0.0.0          sumnet  172.16.78.0      192.168.254.7    0x80000008   1316 
0.0.0.0          sumnet  172.16.78.0      192.168.254.8    0x80000002   1546 
0.0.0.0          sumnet  192.168.20.0     192.168.254.7    0x80000003    627 
0.0.0.0          sumnet  192.168.20.0     192.168.254.8    0x80000003    601 
0.0.0.0          sumnet  192.168.30.0     192.168.254.7    0x80000003    627 
0.0.0.0          sumnet  192.168.30.0     192.168.254.8    0x80000002    633 
0.0.0.0          sumnet  192.168.254.1    192.168.254.2    0x80000005    154 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x8000000d    243 
0.0.0.0          sumnet  192.168.254.7    192.168.254.8    0x80000005    663 
0.0.0.0          sumnet  192.168.254.8    192.168.254.7    0x8000000c    673 
2.2.2.2          rtr     192.168.254.7    192.168.254.7    0x8000000a   1582 
2.2.2.2          rtr     192.168.254.8    192.168.254.8    0x80000008   1545 
2.2.2.2          net     172.16.78.7      192.168.254.7    0x80000007   1222 
2.2.2.2          sumnet  172.16.12.0      192.168.254.7    0x80000017    629 
2.2.2.2          sumnet  172.16.12.0      192.168.254.8    0x8000000b    619 
2.2.2.2          sumnet  172.16.17.0      192.168.254.7    0x80000006   1496 
2.2.2.2          sumnet  172.16.17.0      192.168.254.8    0x80000002   1546 
2.2.2.2          sumnet  172.16.28.0      192.168.254.7    0x80000003    236 
2.2.2.2          sumnet  172.16.28.0      192.168.254.8    0x80000003    286 
2.2.2.2          sumnet  192.168.20.0     192.168.254.7    0x80000003    627 
2.2.2.2          sumnet  192.168.20.0     192.168.254.8    0x80000003    601 
2.2.2.2          sumnet  192.168.30.0     192.168.254.7    0x80000003    627 
2.2.2.2          sumnet  192.168.30.0     192.168.254.8    0x80000002    633 
2.2.2.2          sumnet  192.168.254.1    192.168.254.7    0x8000000b    674 
2.2.2.2          sumnet  192.168.254.1    192.168.254.8    0x80000005    664 
2.2.2.2          sumnet  192.168.254.2    192.168.254.7    0x8000000e    674 
2.2.2.2          sumnet  192.168.254.2    192.168.254.8    0x80000005    664 
3.3.3.3          rtr     192.168.254.7    192.168.254.7    0x80000002    639 
3.3.3.3          sumnet  172.16.12.0      192.168.254.7    0x80000017    629 
3.3.3.3          sumnet  172.16.17.0      192.168.254.7    0x80000006   1496 
3.3.3.3          sumnet  172.16.28.0      192.168.254.7    0x80000003    236 
3.3.3.3          sumnet  172.16.78.0      192.168.254.7    0x80000008   1316 
3.3.3.3          net     192.168.30.8     192.168.254.8    0x80000002    607 
3.3.3.3          sumnet  192.168.254.1    192.168.254.7    0x8000000b    674 
3.3.3.3          sumnet  192.168.254.2    192.168.254.7    0x8000000e    674 
3.3.3.3          sumnet  192.168.254.8    192.168.254.7    0x8000000c    673 
 
sw8 (6860-B) -> show ip ospf lsdb 
    Area Id       Type        LS Id        Orig Router-Id     SeqNo      Age 
----------------+-------+----------------+----------------+------------+----- 
0.0.0.0          rtr     192.168.254.1    192.168.254.1    0x8000003a    164 
0.0.0.0          rtr     192.168.254.2    192.168.254.2    0x80000007    275 
0.0.0.0          rtr     192.168.254.7    192.168.254.7    0x80000039   1598 
0.0.0.0          rtr     192.168.254.8    192.168.254.8    0x80000005    258 
0.0.0.0          net     172.16.17.7      192.168.254.7    0x80000036    158 
0.0.0.0          net     172.16.28.2      192.168.254.2    0x80000003    275 
0.0.0.0          sumnet  172.16.12.0      192.168.254.1    0x80000009    705 
0.0.0.0          sumnet  172.16.12.0      192.168.254.2    0x80000003    255 
0.0.0.0          sumnet  172.16.78.0      192.168.254.7    0x80000008   1419 
0.0.0.0          sumnet  172.16.78.0      192.168.254.8    0x80000003     26 
0.0.0.0          sumnet  192.168.20.0     192.168.254.7    0x80000003    810 
0.0.0.0          sumnet  192.168.20.0     192.168.254.8    0x80000003    783 
0.0.0.0          sumnet  192.168.30.0     192.168.254.7    0x80000003    810 
0.0.0.0          sumnet  192.168.30.0     192.168.254.8    0x80000002    815 
0.0.0.0          sumnet  192.168.254.1    192.168.254.2    0x80000005    255 
0.0.0.0          sumnet  192.168.254.2    192.168.254.1    0x8000000d    345 
0.0.0.0          sumnet  192.168.254.7    192.168.254.8    0x80000005    764 
0.0.0.0          sumnet  192.168.254.8    192.168.254.7    0x8000000c    775 
2.2.2.2          rtr     192.168.254.7    192.168.254.7    0x8000000b     64

<<<PAGE 347>>>
28 
OSPF 
 
2.2.2.2          rtr     192.168.254.8    192.168.254.8    0x80000009     26 
2.2.2.2          net     172.16.78.7      192.168.254.7    0x80000007   1324 
2.2.2.2          sumnet  172.16.12.0      192.168.254.7    0x80000017    731 
2.2.2.2          sumnet  172.16.12.0      192.168.254.8    0x8000000b    720 
2.2.2.2          sumnet  172.16.17.0      192.168.254.7    0x80000006   1599 
2.2.2.2          sumnet  172.16.17.0      192.168.254.8    0x80000003     26 
2.2.2.2          sumnet  172.16.28.0      192.168.254.7    0x80000003    339 
2.2.2.2          sumnet  172.16.28.0      192.168.254.8    0x80000003    386 
2.2.2.2          sumnet  192.168.20.0     192.168.254.7    0x80000003    810 
2.2.2.2          sumnet  192.168.20.0     192.168.254.8    0x80000003    783 
2.2.2.2          sumnet  192.168.30.0     192.168.254.7    0x80000003    810 
2.2.2.2          sumnet  192.168.30.0     192.168.254.8    0x80000002    815 
2.2.2.2          sumnet  192.168.254.1    192.168.254.7    0x8000000b    776 
2.2.2.2          sumnet  192.168.254.1    192.168.254.8    0x80000005    765 
2.2.2.2          sumnet  192.168.254.2    192.168.254.7    0x8000000e    776 
2.2.2.2          sumnet  192.168.254.2    192.168.254.8    0x80000005    765 
3.3.3.3          rtr     192.168.254.8    192.168.254.8    0x80000002    730 
3.3.3.3          sumnet  172.16.12.0      192.168.254.8    0x8000000b    720 
3.3.3.3          sumnet  172.16.17.0      192.168.254.8    0x80000003     26 
3.3.3.3          sumnet  172.16.28.0      192.168.254.8    0x80000003    386 
3.3.3.3          sumnet  172.16.78.0      192.168.254.8    0x80000003     26 
3.3.3.3          net     192.168.30.8     192.168.254.8    0x80000002    788 
3.3.3.3          sumnet  192.168.254.1    192.168.254.8    0x80000005    765 
3.3.3.3          sumnet  192.168.254.2    192.168.254.8    0x80000005    765 
3.3.3.3          sumnet  192.168.254.7    192.168.254.8    0x80000005    764 
 5 
OSPF Redistribution 
- It was demonstrated in the two previous parts of the lab how interfaces running OSPF participate in 
distributing routing information within the Autonomous System.  
- In this part we will manage the other interfaces. For example , int_120 on 6900_B, int_70 on 6870-A 
and  int_80 on 6860-B are seen are local routes. However, they will not run the OSPF protocol. For 
them to be reachable, redistribution will need to be configured. 
 
- To advertise its route, enter: 
 
sw2 (6870-B) -> ip route-map localIntoOspf sequence-number 10 action permit 
sw2 (6870-B) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.120.0/24 permit 
sw2 (6870-B) -> ip redist local into ospf route-map localIntoOspf admin-state enable 
- Check on the 6860 than this new route has been learnt: 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 13 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            1d 5h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 5h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 5h   LOCAL 
  172.16.28.0/24       172.16.12.2       00:57:07   OSPF 
  172.16.78.0/24       172.16.17.7       03:04:36   OSPF 
  192.168.20.0/24      172.16.17.7       00:35:39   OSPF 
  192.168.30.0/24      172.16.17.7       00:35:24   OSPF                
  192.168.120.0/24     172.16.12.2       00:01:25   OSPF 
  192.168.254.1/32     192.168.254.1        1d 0h   LOCAL 
  192.168.254.2/32     172.16.12.2       03:17:44   OSPF 
  192.168.254.7/32     172.16.17.7       23:51:32   OSPF 
  192.168.254.8/32    +172.16.12.2       00:56:20   OSPF 
                      +172.16.17.7       03:01:58   OSPF 
 
sw7 (6870-A) -> show ip routes 
 
+ = Equal cost multipath routes 
 Total 15 routes

<<<PAGE 348>>>
29 
OSPF 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            6d 0h   LOCAL 
  172.16.12.0/24       172.16.17.1       03:19:34   OSPF 
  172.16.17.0/24       172.16.17.7          1d 5h   LOCAL 
  172.16.28.0/24       172.16.78.8       00:55:33   OSPF 
  172.16.78.0/24       172.16.78.7          2d 3h   LOCAL 
  192.168.20.0/24      192.168.20.7         1d 4h   LOCAL 
  192.168.30.0/24      192.168.30.7         1d 0h   LOCAL 
  192.168.70.0/24      192.168.70.7         1d 0h   LOCAL 
  192.168.120.0/24    +172.16.17.1       00:00:37   OSPF 
                      +172.16.78.8       00:00:37   OSPF 
  192.168.254.1/32     172.16.17.1       23:50:52   OSPF 
  192.168.254.2/32    +172.16.17.1       03:16:56   OSPF 
                      +172.16.78.8       00:55:33   OSPF 
  192.168.254.7/32     192.168.254.7        1d 0h   LOCAL 
  192.168.254.8/32     172.16.78.8       03:01:11   OSPF 
 
sw8 (6860-B) -> show ip routes 
  
+ = Equal cost multipath routes 
 Total 14 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            6d 0h   LOCAL 
  172.16.12.0/24       172.16.28.2       00:57:01   OSPF 
  172.16.17.0/24       172.16.78.7       01:18:28   OSPF 
  172.16.28.0/24       172.16.28.8          1d 0h   LOCAL 
  172.16.78.0/24       172.16.78.8          2d 3h   LOCAL 
  192.168.20.0/24      192.168.20.8         1d 0h   LOCAL 
  192.168.30.0/24      192.168.30.8         1d 4h   LOCAL 
  192.168.80.0/24      192.168.80.8         1d 0h   LOCAL 
  192.168.120.0/24     172.16.28.2       00:02:07   OSPF 
  192.168.254.1/32    +172.16.28.2       00:57:01   OSPF 
                      +172.16.78.7       01:18:28   OSPF 
  192.168.254.2/32     172.16.28.2       00:57:01   OSPF 
  192.168.254.7/32     172.16.78.7       03:02:35   OSPF 
  192.168.254.8/32     192.168.254.8     03:03:58   LOCAL 
   
- Vlan 70 is not known by other switches except the 6870-A 
- Vlan 80 is not known by other switches except the 6860-B 
- to advertise these routes, enter: 
 
sw7 (6870-A) -> ip route-map localIntoOspf sequence-number 10 action permit 
sw7 (6870-A) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.70.0/24 permit  
sw7 (6870-A) -> ip redist local into ospf route-map localIntoOspf admin-state enable 
 
sw8 (6860-B) -> ip route-map localIntoOspf sequence-number 10 action permit 
sw8 (6860-B) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.80.0/24 permit 
sw8 (6860-B) -> ip redist local into ospf route-map localIntoOspf admin-state enable

<<<PAGE 349>>>
30 
OSPF 
 
- Check on the 6900 than this new route has been learnt: 
 
sw1 (6900-A) -> show ip routes 
 
+ = Equal cost multipath routes 
 Total 16 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            1d 5h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 5h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 5h   LOCAL 
  172.16.28.0/24       172.16.12.2       01:01:25   OSPF 
  172.16.78.0/24       172.16.17.7       03:08:54   OSPF 
  192.168.20.0/24      172.16.17.7       00:39:57   OSPF 
  192.168.30.0/24     +172.16.17.7       00:39:42   OSPF 
  192.168.70.0/24      172.16.17.7       00:01:49   OSPF 
  192.168.80.0/24     +172.16.12.2       00:01:20   OSPF 
                      +172.16.17.7       00:01:20   OSPF 
  192.168.120.0/24     172.16.12.2       00:05:43   OSPF 
  192.168.254.1/32     192.168.254.1        1d 0h   LOCAL 
  192.168.254.2/32     172.16.12.2       03:22:02   OSPF 
 
sw2 (6870-B) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 16 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            6d 0h   LOCAL 
  172.16.12.0/24       172.16.12.2          1d 5h   LOCAL 
  172.16.17.0/24       172.16.12.1       01:25:56   OSPF 
  172.16.28.0/24       172.16.28.2          1d 0h   LOCAL 
  172.16.78.0/24       172.16.28.8       01:01:07   OSPF 
  192.168.20.0/24     +172.16.28.8       00:40:31   OSPF 
  192.168.30.0/24      172.16.28.8       00:40:17   OSPF 
  192.168.70.0/24     +172.16.12.1       00:02:24   OSPF 
                      +172.16.28.8       00:02:24   OSPF 
  192.168.80.0/24      172.16.28.8       00:01:56   OSPF 
  192.168.120.0/24     192.168.120.2        1d 0h   LOCAL 
  192.168.254.1/32     172.16.12.1       03:22:32   OSPF 
  192.168.254.2/32     192.168.254.2     03:25:02   LOCAL 
  192.168.254.7/32    +172.16.12.1       01:25:56   OSPF 
                      +172.16.28.8       01:01:07   OSPF 
  192.168.254.8/32     172.16.28.8       01:01:07   OSPF 
 
- Interfaces should be enabled to see them on routing table 
 
sw7 (6870-A) -> interface 1/1/1 admin-state enable 
 
sw8 (6860-B) -> interface 1/1/1 admin-state enable

<<<PAGE 350>>>
31 
OSPF 
 
 6 
Access to the DATA server  
 
 
 
- To have an Internet access for VM clients, a pre-configuration must be done on the OS6900-A 
 
- Manage a VLAN 100 and associated interface on 6900-A  
 
sw1 (6900-A) -> vlan 100 
sw1 (6900-A) -> ip interface int_100 address 192.168.100.1/24 vlan 100 
sw1 (6900-A) -> vlan 100 members port 1/1/2 untagged 
sw1 (6900-A) -> interfaces 1/1/2 admin-state enable 
 
-  to advertise this route, enter: 
 
sw1 (6900-A) -> ip route-map localIntoOspf sequence-number 10 action permit 
sw1 (6900-A) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.100.0/24 permit 
sw1 (6900-A) -> ip redist local into ospf route-map localIntoOspf admin-state enable 
  
- Default route 0.0.0.0/0 on 6900-A is a static route which should be advertised to other switch  
Manage a Redistribution of Static routes 
 
sw1 (6900-A) -> ip static-route 0.0.0.0/0 gateway 192.168.100.108 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 19 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  0.0.0.0/0            192.168.100.108   00:00:09   STATIC 
  10.0.0.51/32         192.168.100.108   00:02:18   STATIC 
  127.0.0.1/32         127.0.0.1            1d 5h   LOCAL 
  172.16.12.0/24       172.16.12.1          1d 5h   LOCAL 
  172.16.17.0/24       172.16.17.1          1d 5h   LOCAL 
  172.16.28.0/24       172.16.12.2       01:07:37   OSPF 
                      +172.16.17.7       03:12:28   OSPF 
 
 ----| truncated] 
 
 
 
Notes 
The second static route has been managed previously on the conf download to the switch at the beginning of 
the training.      10.0.0.51 is the IP address of the DNS.

<<<PAGE 351>>>
32 
OSPF 
 
 
- 
The previous section showed how to redistribute a local route. The same can be applied to a static 
route.   
- 
To redistribute the static route into OSPF another filter must be created since static routes are not 
considered part of the OSPF Autonomous System. Type the following: 
 
sw1 (6900-A) -> ip route-map staticIntoOspf sequence-number 10 action permit 
sw1 (6900-A) -> ip route-map staticIntoOspf sequence-number 10 match ip-address 0.0.0.0/0 permit 
sw1 (6900-A) -> ip redist static into ospf route-map staticIntoOspf admin-state enable   
 
- 
Check the result on 6870-B and 6860’s 
 
sw2 (6870-B) -> show ip ospf routes 
 
Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
0.0.0.0/0             172.16.12.1       1        Vlan     212        AS-Ext (E2) 
10.0.0.51/32          172.16.12.1       1        Vlan     212        AS-Ext (E2) 
172.16.12.0/24        172.16.12.2       1        Vlan     212        Intra 
172.16.17.0/24        172.16.12.1       2        Vlan     212        Intra 
172.16.28.0/24        172.16.28.2       1        Vlan     228        Intra 
172.16.78.0/24        172.16.28.8       2        Vlan     228        Inter 
192.168.20.0/24       172.16.28.8       2        Vlan     228        Inter 
192.168.30.0/24       172.16.28.8       2        Vlan     228        Inter 
192.168.70.0/24       172.16.12.1       2        Vlan     212        AS-Ext (E2) 
192.168.70.0/24       172.16.28.8       2        Vlan     228        AS-Ext (E2) 
192.168.80.0/24       172.16.28.8       1        Vlan     228        AS-Ext (E2) 
192.168.100.0/24      172.16.12.1       1        Vlan     212        AS-Ext (E2) 
192.168.254.1/32      172.16.12.1       1        Vlan     212        Intra 
192.168.254.2/32      0.0.0.0           0        N/A                 Intra 
192.168.254.7/32      172.16.12.1       2        Vlan     212        Intra 
192.168.254.7/32      172.16.28.8       2        Vlan     228        Intra 
192.168.254.8/32      172.16.28.8       1        Vlan     228        Intra 
 
sw7 (6870-A) -> show ip ospf routes 
                                                  Domain  Domain 
Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
0.0.0.0/0             172.16.17.1       1        Vlan     217        AS-Ext (E2) 
10.0.0.51/32          172.16.17.1       1        Vlan     217        AS-Ext (E2) 
172.16.12.0/24        172.16.17.1       2        Vlan     217        Inter 
172.16.17.0/24        172.16.17.7       1        Vlan     217        Intra 
172.16.28.0/24        172.16.78.8       2        Vlan     278        Intra 
172.16.78.0/24        172.16.78.7       1        Vlan     278        Intra 
192.168.20.0/24       192.168.20.7      1        Vlan     20         Intra 
192.168.30.0/24       192.168.30.7      1        Vlan     30         Intra 
192.168.80.0/24       192.168.30.8      1        Vlan     30         AS-Ext (E2) 
192.168.100.0/24      172.16.17.1       1        Vlan     217        AS-Ext (E2) 
192.168.120.0/24      172.16.78.8       2        Vlan     278        AS-Ext (E2) 
192.168.120.0/24      172.16.17.1       2        Vlan     217        AS-Ext (E2) 
192.168.254.1/32      172.16.17.1       1        Vlan     217        Intra 
192.168.254.2/32      172.16.78.8       2        Vlan     278        Intra 
192.168.254.2/32      172.16.17.1       2        Vlan     217        Intra 
192.168.254.7/32      0.0.0.0           0        N/A                 Intra 
192.168.254.8/32      172.16.78.8       1        Vlan     278        Intra

<<<PAGE 352>>>
33 
OSPF 
 
 
sw8 (6860-B) -> show ip ospf routes 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
0.0.0.0/0             172.16.78.7       2        Vlan     278        AS-Ext (E2) 
0.0.0.0/0             172.16.28.2       2        Vlan     228        AS-Ext (E2) 
10.0.0.51/32          172.16.78.7       2        Vlan     278        AS-Ext (E2) 
10.0.0.51/32          172.16.28.2       2        Vlan     228        AS-Ext (E2) 
172.16.12.0/24        172.16.28.2       2        Vlan     228        Inter 
172.16.17.0/24        172.16.78.7       2        Vlan     278        Intra 
172.16.28.0/24        172.16.28.8       1        Vlan     228        Intra 
172.16.78.0/24        172.16.78.8       1        Vlan     278        Intra 
192.168.20.0/24       192.168.20.8      1        Vlan     20         Intra 
192.168.30.0/24       192.168.30.8      1        Vlan     30         Intra 
192.168.70.0/24       192.168.30.7      1        Vlan     30         AS-Ext (E2) 
192.168.100.0/24      172.16.78.7       2        Vlan     278        AS-Ext (E2) 
192.168.100.0/24      172.16.28.2       2        Vlan     228        AS-Ext (E2) 
192.168.120.0/24      172.16.28.2       1        Vlan     228        AS-Ext (E2) 
192.168.254.1/32      172.16.78.7       2        Vlan     278        Intra 
192.168.254.1/32      172.16.28.2       2        Vlan     228        Intra 
192.168.254.2/32      172.16.28.2       1        Vlan     228        Intra 
192.168.254.7/32      172.16.78.7       1        Vlan     278        Intra 
192.168.254.8/32      0.0.0.0           0        N/A                 Intra 
 
- 
The pfsense server has been configured with Rip protocol. 
- 
Manage RIP dynamic protocol on 6900 (int_100). And then let’s redistribute local route and static routes 
to rip. 
 
sw1 (6900-A) -> ip load rip 
sw1 (6900-A) -> ip rip interface int_100 admin-state enable 
sw1 (6900-A) -> ip rip admin-state enable 
sw1 (6900-A) -> ip route-map local sequence-number 10 action permit 
sw1 (6900-A) -> ip route-map local sequence-number 10 match ip-address 0.0.0.0/0 permit 
sw1 (6900-A) -> ip redist local into rip route-map local admin-state enable 
sw1 (6900-A) -> ip redist static into rip route-map local admin-state enable 
sw1 (6900-A) -> ip redist ospf into rip route-map local admin-state enable 
sw1 (6900-A) -> write memory flash-synchro 
 
- 
Check the result on 6900-A 
 
sw1 (6900-A) -> show ip rip routes 
Legends: State: A = Active, H = Holddown, G = Garbage 
Destination        Gateway          State Metric Proto 
------------------+-----------------+----+------+------ 
0.0.0.0/0          +192.168.100.108   A    1      Redist 
10.0.0.51/32       +192.168.100.108   A    1      Redist 
10.4.21.0/24       +192.168.100.108   A    2      Rip 
172.16.12.0/24     +172.16.12.1       A    1      Redist 
172.16.17.0/24     +172.16.17.1       A    1      Redist 
172.16.28.0/24     +172.16.12.2       A    1      Redist 
172.16.78.0/24     +172.16.17.7       A    1      Redist 
192.168.20.0/24    +172.16.17.7       A    1      Redist 
192.168.30.0/24    +172.16.17.7       A    1      Redist 
192.168.70.0/24    +172.16.17.7       A    1      Redist 
192.168.80.0/24    +172.16.12.2       A    1      Redist 
192.168.100.0/24   +192.168.100.1     A    1      Redist 
                    192.168.100.108   A    2      Rip 
192.168.120.0/24   +172.16.12.2       A    1      Redist 
192.168.254.1/32   +192.168.254.1     A    1      Redist 
192.168.254.2/32   +172.16.12.2       A    1      Redist 
192.168.254.7/32   +172.16.17.7       A    1      Redist 
192.168.254.8/32   +172.16.12.2       A    1      Redist

<<<PAGE 353>>>
34 
OSPF 
 
 7 
OSPF Authentication 
7.1. 
Simple Authentication 
- Let’s enable simple authentication between 6900-A and 6870-A. 
- Type the following:  
sw1 (6900-A) -> show ip ospf neighbor 
                                                    Domain   Domain 
  IP Address        Area Id          Router Id       Name     ID      State  Type 
----------------+----------------+----------------+--------+--------+-------+-------- 
172.16.12.2      1.1.1.1          192.168.254.2    Vlan     212        Full  Dynamic 
172.16.17.7      0.0.0.0          192.168.254.7    Vlan     217        Full  Dynamic 
 
sw1 (6900-A) -> ip ospf interface int_217 auth-type simple 
sw1 (6900-A) -> ip ospf interface int_217 auth-key alcatel 
 
sw1 (6900-A) -> show ip ospf neighbor 
Thu Jan 30 01:18:12 : ospf_0 AUTH ERR message: 
+++ ospfAuthCheck: Intf 172.16.17.1: Auth type 1 mismatch! recvd pkt = (0) 
                                                    Domain   Domain 
  IP Address        Area Id          Router Id       Name     ID      State  Type 
----------------+----------------+----------------+--------+--------+-------+-------- 
172.16.12.2      1.1.1.1          192.168.254.2    Vlan     212        Full  Dynamic 
 
sw7 (6870-A) -> ip ospf interface int_217 auth-type simple 
sw7 (6870-A) -> ip ospf interface int_217 auth-key alcatel 
sw7 (6870-A) -> show ip ospf interface int_217 
… 
Authentication Type                   = simple, 
Authentication Key                    = Set, 
 
- Verify that the switches have become neighbors once authentication was enabled on both ends of the link 
 
sw1 (6900-A) -> show ip ospf neighbor 
                                                    Domain   Domain 
  IP Address        Area Id          Router Id       Name     ID      State  Type 
----------------+----------------+----------------+--------+--------+-------+-------- 
172.16.12.2      1.1.1.1          192.168.254.2    Vlan     212        Full  Dynamic 
172.16.17.7      0.0.0.0          192.168.254.7    Vlan     217        Full  Dynamic 
7.2. 
MD5 Authentication 
 
MD5 is a more secure way of configuring authentication when using OSPF. By using MD5, the keys will be 
encrypted, unlike simple passwords. A key number and a key string must be supplied for MD5. 
 
- Let’s enable simple authentication between 6900-A and 6870-B 
 
- Type the following: 
 
sw1 (6900-A) -> ip ospf interface int_212 auth-type md5 
sw1 (6900-A) -> ip ospf interface int_212 md5 1 
sw1 (6900-A) -> ip ospf interface int_212 md5 1 key alcatel 
  
sw2 (6870-B) -> ip ospf interface int_212 auth-type md5 
sw2 (6870-B) -> ip ospf interface int_212 md5 1  
sw2 (6870-B) -> ip ospf interface int_212 md5 1 key alcatel 
- These two values will be combined and used in the MD5 hashing algorithm for authentication between the 
switches. Check your routing tables, neighbors, and interfaces and enable debugging to display any 
problems.

<<<PAGE 354>>>
35 
OSPF 
 
 
sw1 (6900-A) -> show ip ospf interface int_212 
… 
Authentication Type                   = md5, 
 
… 
 
sw1 (6900-A) -> show ip ospf neighbor 
                                                    Domain   Domain 
  IP Address        Area Id          Router Id       Name     ID      State  Type 
----------------+----------------+----------------+--------+--------+-------+-------- 
172.16.12.2      1.1.1.1          192.168.254.2    Vlan     212        Full  Dynamic 
172.16.17.7      0.0.0.0          192.168.254.7    Vlan     217        Full  Dynamic 
- Save the configuration; it will be used in the next lab. 
 
-> write memory flash-synchro 
 8 
Stub Area 
8.1. 
OSPF Areas Logical diagram 
 
 
8.2. 
Configuration 
- For this Lab, we will add a new 6560 switch to become an internal router for stub area 4.4.4.4 
- A router becomes an internal router when it doesn’t have a Backbone connection and is member of 
only a single area.  For the purposes of the lab, Stub-Switches will be used as an internal router.

<<<PAGE 355>>>
36 
OSPF 
 
 
Notes 
Switches in Stub Areas do not have external routes in their routing database 
 
- Create the connection between 6870-A and 6560-A: 
 
sw7 (6870-A) -> vlan 137 
sw7 (6870-A) -> vlan 137 members port 1/1/7 untagged 
sw7 (6870-A) -> ip interface int_137 address 172.16.137.7/24 vlan 137 
sw7 (6870-A) -> interfaces 1/1/7 admin-state enable 
 
sw3 (6560-A) -> ip interface Loopback0 address 192.168.254.3 
sw3 (6560-A) -> vlan 137 
sw3 (6560-A) -> vlan 137 members port 1/1/7 untagged 
sw3 (6560-A) -> ip interface int_137 address 172.16.137.3/24 vlan 137 
sw3 (6560-A) -> interfaces 1/1/7 admin-state enable 
- Create a client vlan on 6560-A: 
 
sw3 (6560-A) -> vlan 60 
sw3 (6560-A) -> vlan 60 members port 1/1/1 untagged 
sw3 (6560-A) -> ip interface int_60 address 192.168.60.3/24 vlan 60 
sw3 (6560-A) -> interfaces 1/1/1 admin-state enable 
 
- Configure stub area 4.4.4.4 in both 6860 and 6560: 
 
sw7 (6870-A) -> ip ospf area 4.4.4.4 
sw7 (6870-A) -> ip ospf area 4.4.4.4 type stub 
sw7 (6870-A) -> ip ospf interface int_137 
sw7 (6870-A) -> ip ospf interface int_137 area 4.4.4.4 
sw7 (6870-A) -> ip ospf interface int_137 admin-state enable 
 
sw3 (6560-A) -> ip load ospf 
sw3 (6560-A) -> ip router router-id 192.168.254.3 
sw3 (6560-A) -> ip ospf admin-state enable 
sw3 (6560-A) -> ip ospf area 4.4.4.4 
sw3 (6560-A) -> ip ospf area 4.4.4.4 type stub 
sw3 (6560-A) -> ip ospf interface int_137 
sw3 (6560-A) -> ip ospf interface int_137 area 4.4.4.4 
sw3 (6560-A) -> ip ospf interface int_137 admin-state enable 
sw3 (6560-A) -> ip ospf interface int_60 
sw3 (6560-A) -> ip ospf interface int_60 area 4.4.4.4 
sw3 (6560-A) -> ip ospf interface int_60 admin-state enable 
 
- Check areas: 
 
sw7 (6870-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
0.0.0.0           enabled      normal       up 
2.2.2.2           enabled      normal       up 
3.3.3.3           enabled      normal       up 
4.4.4.4           enabled      stub         up 
 
sw3 (OS6560-A) -> show ip ospf area 
    Area Id      AdminStatus      Type       OperStatus 
---------------+-------------+-------------+------------ 
4.4.4.4           enabled      stub         up

<<<PAGE 356>>>
37 
OSPF 
 
8.3. 
Verification 
- Type the following on 6560-A: 
 
sw3 (6560-A) -> show ip ospf routes 
 
                                                  Domain  Domain 
 Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
0.0.0.0/0             172.16.137.7      2        Vlan     137        Inter 
172.16.12.0/24        172.16.137.7      3        Vlan     137        Inter 
172.16.17.0/24        172.16.137.7      2        Vlan     137        Inter 
172.16.28.0/24        172.16.137.7      3        Vlan     137        Inter 
172.16.78.0/24        172.16.137.7      2        Vlan     137        Inter 
172.16.137.0/24       172.16.137.3      1        Vlan     137        Intra 
192.168.20.0/24       172.16.137.7      2        Vlan     137        Inter 
192.168.30.0/24       172.16.137.7      3        Vlan     137        Inter 
192.168.60.0/24       192.168.60.3      1        Vlan     60         Intra 
192.168.254.1/32      172.16.137.7      2        Vlan     137        Inter 
192.168.254.2/32      172.16.137.7      3        Vlan     137        Inter 
192.168.254.3/32      0.0.0.0           0        N/A                 Intra 
192.168.254.7/32      172.16.137.7      1        Vlan     137        Intra 
192.168.254.8/32      172.16.137.7      2        Vlan     137        Inter 
 
sw7 (6870-A) -> show ip ospf routes 
                                                  Domain  Domain 
Destination/Mask          Gateway       Metric   Name     ID         Type 
---------------------+-----------------+--------+--------+--------+---------- 
0.0.0.0/0             172.16.17.1       1        Vlan     217        AS-Ext (E2) 
10.0.0.51/32          172.16.17.1       1        Vlan     217        AS-Ext (E2) 
172.16.12.0/24        172.16.17.1       2        Vlan     217        Inter 
172.16.17.0/24        172.16.17.7       1        Vlan     217        Intra 
172.16.28.0/24        172.16.78.8       2        Vlan     278        Intra 
172.16.78.0/24        172.16.78.7       1        Vlan     278        Intra 
172.16.137.0/24       172.16.137.7      1        Vlan     137        Intra 
192.168.20.0/24       192.168.20.7      1        Vlan     20         Intra 
192.168.30.0/24       192.168.30.7      1        Vlan     30         Intra 
192.168.60.0/24       172.16.137.3      2        Vlan     137        Intra 
192.168.80.0/24       192.168.30.8      1        Vlan     30         AS-Ext (E2) 
192.168.100.0/24      172.16.17.1       1        Vlan     217        AS-Ext (E2) 
192.168.120.0/24      172.16.78.8       2        Vlan     278        AS-Ext (E2) 
192.168.120.0/24      172.16.17.1       2        Vlan     217        AS-Ext (E2) 
192.168.254.1/32      172.16.17.1       1        Vlan     217        Intra 
192.168.254.2/32      172.16.78.8       2        Vlan     278        Intra 
192.168.254.2/32      172.16.17.1       2        Vlan     217        Intra 
192.168.254.3/32      172.16.137.3      1        Vlan     137        Intra 
192.168.254.7/32      0.0.0.0           0        N/A                 Intra 
192.168.254.8/32      172.16.78.8       1        Vlan     278        Intra 
 
 
 
- Save the configuration in all switches: 
 
all-> write memory flash-synchro 
 
 
 
Notes 
On the stub-switch, there should be a default route with a next-hop pointing towards the IP interface of the 
backbone switch 
 
 
How would the stub area be changed into a totally stubby area?

<<<PAGE 357>>>
G R A C E F U L R E S TA RT
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 358>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the Graceful Restart feature
• Learn how to configure it

<<<PAGE 359>>>
BGP/OSPF/ISIS - GRACEFUL RESTART
• Router remains on forwarding path when restarting
• Neighbors must participate in graceful restart
• Reverts to normal routing protocol function if network topology change is detected during 
graceful restart
• Ex. Router Y continues to list Router X during restart
OSPF Graceful Restart Helping and Restarting Router
Network Segment S
Restarting Router X
Router A
Router C
Router B
Helping Router Y

<<<PAGE 360>>>
GRACEFUL RESTART
• Without  graceful restart
• If a router restarts:
• Neighbor reinitializes the adjacency and floods out 
updated LSAs showing that the restarting router is no 
longer part of the network
• All routers in the area must run SPF algorithm to compute 
new routes
• When the restarting router comes up:
• ISIS/OSPF adjacency is re-established.
• Neighbor floods out new LSAs including the routes from 
the restarting router
• All routers in the area must run SPF algorithm once again. 
This activity results in CMM stress for the routers.
• Possible loss of packets due to forwarding loops
Restarting 
Router
Session 
Down
Neighbor
Reinit. Adj
SPF recalc.
Updated LSA
SPF recalc.
Updated LSA
Restarting 
Router
Neighbor
SPF recalc.
Updated LSA
SPF recalc.
Updated LSA
Updated LSA

<<<PAGE 361>>>
GRACEFUL RESTART
• With graceful restart
• Grace LSAs are sent to neighbors either before (planned) or after (unplanned) restart.
• Contain a “grace period”; time in seconds for achieving the OSPF restart.
• May or may not be acknowledged by the neighbors.
• Are “link-local”; only sent to adjacent neighbors
• During the restart neighbors act as if nothing happened to the restarting router
• The restarting router is still listed as an adjacency.
• Traffic is forwarded to the restarting router
• The restarting router performs non-stop forwarding
GRACE LSA
GRACE LSA
R2
RESTARTING ROUTER
R1
R3
LSACK
LSACK
DATA
R2
R1
R3
RESTART PENDING…

<<<PAGE 362>>>
GRACEFUL RESTART
• With Graceful restart
• When the restarting router comes up:
• It discovers neighbors and re-establishes adjacencies.
• It synchronizes its LSDB
• It does not send any LSA/LSP because it still has incomplete routing information. If it sent outdated 
LSAs/LSPs the neighbors would think that the network had changed forcing them to run SPF calculations 
throughout the area
• When the restarting router has synchronized its LSDB:
• It sends out its updated LSAs/LSP. The neighbors do not run SPF algorithm based on these LSAs/LSPs.
• It purges the grace LSAs/LSPs by setting their age to the maximum value. The neighbors see these LSAs/LSPs 
as ‘expired’ and discard them
• In this way the graceful restart has successfully completed
R2
R1
R3
GRACE LSA FLUSH
GRACE LSA FLUSH
NEIGH. ADJ.
NEIGH. ADJ.
LSA
LSA
SPF

<<<PAGE 363>>>
CLI - GRACEFUL RESTART
• Enables graceful restart on the switch
• Initiates a planned graceful restart
• Configures support for the graceful restart feature on an OSPF router
• Enables or disables the capability of a router to operate in helper mode in response to a 
router performing a graceful restart
• Configures the grace period for achieving a graceful OSPF restart
->ip {ospf/ISIS/BGP} graceful-restart
Note: Graceful restart is disabled for OSPF and ISIS and enabled for BGP by default
->ip {ospf/ISIS/BGP} restart initiate
->ip {ospf/ISIS/BGP} restart-support planned-unplanned / planned-only
->ip {ospf/ISIS/BGP} restart-helper admin-state enable/disable
->ip {ospf/ISIS/BGP} restart-interval
->show ip {ospf/ISIS/BGP} restart

<<<PAGE 364>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 365>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
DHCP Server & DHCP Relay 
How to 
✓ Configure the DHCP Relay feature (aka IP Helper) 
Contents 
1 
Topology ........................................................................................ 2 
2 
Accessing the DHCP Server .................................................................. 3 
3 
Testing the DHCP Relay ...................................................................... 5

<<<PAGE 366>>>
2 
DHCP Server & DHCP Relay 
 
 1 
Topology 
A DHCP server provides dynamic IP addresses on lease for client interfaces on a network. It manages a pool of IP 
addresses and information about client configuration parameters. The DHCP server obtains an IP address 
request from the client interfaces.  
 
After obtaining the requests, the DHCP server assigns an IP address, a lease period, and other IP configuration 
parameters, such as the subnet mask and the default gateway. 
 
The DHCP Relay feature allows UDP broadcast packets to be forwarded across VLANs that have IP routing 
enabled.

<<<PAGE 367>>>
3 
DHCP Server & DHCP Relay 
 
 2 
Accessing the DHCP Server 
When DHCP clients and associated servers do not reside on the same IP network or subnet, a DHCP relay 
agent can transfer DHCP messages between them.  
- Check if there is a route from the 6870-A and 6860-B to the DHCP server (192.168.100.102): 
sw7 (6870-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 23 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  0.0.0.0/0            172.16.17.1       00:00:38   OSPF 
  10.0.0.51/32         172.16.17.1       00:00:38   OSPF 
  127.0.0.1/32         127.0.0.1         00:42:20   LOCAL 
  172.16.17.0/24       172.16.17.7       00:40:53   LOCAL 
  172.16.18.0/24      +172.16.17.1       00:40:09   OSPF 
                      +172.16.78.8       00:40:09   OSPF 
  172.16.78.0/24       172.16.78.7       00:40:53   LOCAL 
  192.168.20.0/24      192.168.20.7      00:40:56   LOCAL 
  192.168.30.0/24      192.168.30.7      00:40:56   LOCAL 
  192.168.100.0/24     172.16.17.1       00:25:03   OSPF 
  192.168.254.1/32     172.16.17.1       00:09:59   OSPF 
  192.168.254.7/32     192.168.254.7     00:09:56   LOCAL 
  192.168.254.8/32     172.16.78.8       00:09:45   OSPF 
  ---[ truncated] 
 
sw7 (6870-A) -> ping 192.168.100.102 
PING 192.168.100.102 (192.168.100.102) 56(84) bytes of data. 
64 bytes from 192.168.100.102: icmp_seq=1 ttl=127 time=2.08 ms 
64 bytes from 192.168.100.102: icmp_seq=2 ttl=127 time=0.983 ms 
64 bytes from 192.168.100.102: icmp_seq=2 ttl=127 time=0.983 ms 
 
sw8 (6860-B) -> show ip routes 
 
Total 25 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  0.0.0.0/0           +172.16.28.2       04:04:34   OSPF 
                      +172.16.78.7       00:54:01   OSPF 
  10.0.0.51/32        +172.16.28.2       04:04:34   OSPF 
                      +172.16.78.7       00:54:01   OSPF 
  127.0.0.1/32         127.0.0.1            1d 4h   LOCAL 
  172.16.12.0/24       172.16.28.2       05:43:00   OSPF 
  172.16.17.0/24       172.16.78.7       00:54:45   OSPF 
  172.16.28.0/24       172.16.28.8       05:54:09   LOCAL 
  172.16.78.0/24       172.16.78.8          1d 0h   LOCAL 
  172.16.137.0/24      172.16.78.7       03:40:30   OSPF 
  192.168.20.0/24      192.168.20.8      21:22:00   LOCAL 
  192.168.30.0/24      192.168.30.8      22:04:03   LOCAL 
---[ truncated] 
  192.168.60.0/24      172.16.78.7       03:39:36   OSPF 
  192.168.70.0/24      192.168.30.7      04:14:18   OSPF 
  192.168.80.0/24      192.168.80.8      05:54:09   LOCAL 
  192.168.100.0/24    +172.16.28.2       04:05:56   OSPF   
---[ truncated] 
 
sw8 (6860-B) -> ping 192.168.100.102 
 
PING 192.168.100.102 (192.168.100.102) 56(84) bytes of data. 
64 bytes from 192.168.100.102: icmp_seq=1 ttl=127 time=1.98 ms 
64 bytes from 192.168.100.102: icmp_seq=2 ttl=127 time=0.733 ms 
64 bytes from 192.168.100.102: icmp_seq=3 ttl=127 time=0.769 ms

<<<PAGE 368>>>
4 
DHCP Server & DHCP Relay 
 
- Configure an IP DHCP relay on each switch: 
- On the 6870-A: 
sw7 (6870-A) -> ip dhcp relay destination 192.168.100.102 
sw7 (6870-A) -> ip dhcp relay admin-state enable 
sw7 (6870-A) -> show ip dhcp relay 
IP DHCP Relay : 
  DHCP Relay Admin Status        = Enable, 
  Forward Delay(seconds)         = 0, 
  Max number of hops             = 16, 
  Relay Agent Information        = Disabled, 
  Relay Agent Information Policy = Drop, 
  DHCP Relay Opt82 Format  =  Base MAC, 
  DHCP Relay Opt82 String  =  e8:e7:32:d4:88:95, 
  PXE support                    = Disabled, 
  Relay Mode                     = Global, 
  Bootup Option                  = Disable, 
 
- On the 6860-B: 
Sw8 (6860-B) -> ip dhcp relay destination 192.168.100.102 
Sw8 (6860-B) -> ip dhcp relay admin-state enable 
sw8 (6860-B) -> show ip dhcp relay 
IP DHCP Relay : 
  DHCP Relay Admin Status        = Enable, 
  Forward Delay(seconds)         = 0, 
  Max number of hops             = 16, 
  Relay Agent Information        = Disabled, 
  Relay Agent Information Policy = Drop, 
  DHCP Relay Opt82 Format  =  Base MAC, 
  DHCP Relay Opt82 String  =  e8:e7:32:cd:57:f3, 
  PXE support                    = Disabled, 
  Relay Mode                     = Global, 
  Bootup Option                  = Disable, 
 
- Check that VLANs 20 or 30 are correctly mapped to ports for clients connected to the 6360 virtual chassis. 
 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      default      forwarding 
  2/1/1      default      forwarding 
  0/7        tagged      forwarding 
  0/8        tagged     dhl-blocking 
 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/2      default      forwarding 
  2/1/2      default      forwarding 
  0/7        tagged     dhl-blocking 
  0/8        tagged      forwarding

<<<PAGE 369>>>
5 
DHCP Server & DHCP Relay 
 
 
Notes 
If ports are not assigned to the correct VLAN, type the following commands 
 
- Assign the VLAN 20 or 30 to the clients connected to the 6360 virtual chassis: 
 
sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged 
sw5 (6360-A) -> vlan 20 members port 2/1/1 untagged 
sw5 (6360-A) -> vlan 30 members port 1/1/2 untagged 
sw5 (6360-A) -> vlan 30 members port 2/1/2 untagged 
 
sw5 (6360-A) -> interfaces 1/1/1-2 admin-state enable 
sw5 (6360-A) -> interfaces 2/1/1-2 admin-state enable 
 3 
Testing the DHCP Relay 
Configure clients 5, 6, 9 and 10 to obtain an IP address and DNS server address automatically: 
 
 
Tips 
The IP DHCP relay feature can also be configured 
on a per-VLAN basis.  
This can be interesting if different DHCP servers 
must serve IP addresses for different subnets. 
Here, as we have a unique DHCP server, it’s not 
necessary. 
 
 
- Check the IP DHCP relay statistics: 
sw7 (6870-A) -> show ip dhcp relay statistics 
Global Statistics : 
    Reception From Client : 
      Total Count =         43, Delta =         43 
    Forw Delay Violation : 
      Total Count =          0, Delta =          0 
    Max Hops Violation : 
      Total Count =          0, Delta =          0 
    Agent Info Violation : 
      Total Count =          0, Delta =          0 
    Invalid Gateway IP : 
      Total Count =          0, Delta =          0 
Server Specific Statistics : 
    From Interface Any to Server 192.168.100.102 
        Tx Server : 
          Total Count =         43, Delta =         43 
        InvAgentInfoFromServer: 
          Total Count =          0, Delta =          0 
 
sw8 (6860-B) -> show ip dhcp relay statistics 
Global Statistics : 
    Reception From Client : 
      Total Count =         40, Delta =         40 
    Forw Delay Violation : 
      Total Count =          0, Delta =          0 
    Max Hops Violation : 
      Total Count =          0, Delta =          0 
    Agent Info Violation : 
      Total Count =          0, Delta =          0 
    Invalid Gateway IP : 
      Total Count =          0, Delta =          0 
Server Specific Statistics : 
    From Interface Any to Server 192.168.100.102 
        Tx Server : 
          Total Count =         40, Delta =         40 
        InvAgentInfoFromServer: 
          Total Count =          0, Delta =          0

<<<PAGE 370>>>
M U LT I C A S T I N T R O D U C T I O N
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 371>>>
Upon completion this module, you will be
able to understand and setup the following 
features:
OBJECTIVES
• Multicast overview
• IP Multicast Switching (IPMS)
• Internet Group Management Protocol (IGMP) 
• Configuration and Monitoring
• Layer 2 Static Multicast & IGMP Relay and 
Throttling
• Storm Control & Load balancing multicast on 
Link Aggregation

<<<PAGE 372>>>
MULTICAST - OVERVIEW
• Similar to broadcast traffic
• Like selective broadcast
• Only those that request the traffic get it
• Allows a one to many communication rather 
than one to one
• Unicast sends one packet per destination
• Multicast sends one packet for many 
destinations
Multicast
Unicast

<<<PAGE 373>>>
MULTICAST  - ADVANTAGES & USE
• Conserves Bandwidth
• Uses for multicast
• Resource discovery (OSPF, RIP2, Bootp)
• VLC for video netcasting
• Multipoint file transfer (Starburst Com.)
• Redundant systems (parallel databases)
• Ghosting Software 
• Information distribution in data warehousing

<<<PAGE 374>>>
MULTICAST - GROUP
• Multicast group
• Set of receivers for a multicast transmission 
• Identified by a multicast address
• A user that wants to receive multicast transmissions joins the corresponding multicast group, and 
becomes a member of that group
• IP Multicast service is unreliable
• A network must have mechanisms to support such applications in an efficient manner
• After a user joins, the network builds the necessary routing paths so that the user receives 
the data sent to the multicast group

<<<PAGE 375>>>
224.0.0.xxx – Routing protocols and other low level topology discovery and maintenance protocols
Well-Known Class D Address examples
224.0.0.1 
All Systems on this Subnet
224.0.0.2 
All Routers on this Subnet
224.0.0.4 
DVMRP Routers 
224.0.0.5 
OSPFIGP OSPFIGP All Routers
224.0.0.6 
OSPFIGP OSPFIGP Designated Routers 
224.0.0.9 
RIP2 Routers 
224.0.0.13 All PIM Routers 
224.0.0.18 VRRP 
224.0.0.22 IGMP 
224.0.0.19 IPAllL1ISs
224.0.0.20 IPAllL2ISs 
224.0.1.xxx – Internetwork control block
232.0.0.0-232.255.255.255 (232/8) Source-Specific Multicast Block 
239.xxx.xxx.xxx - Administratively scoped address block
……… (http://www.iana.org/assignments/multicast-addresses)
MULTICAST - ADDRESSING
• Based on Class “D” IP address values
• From 224.0.0.0 to 239.255.255.255
• Allocated by sending application MAC address derived from IP address
• Least Significant 23 bits of IP address mapped onto MAC address
• IP MultiCast address 224.1.2.3   =  01:00:5E:01:02:03

<<<PAGE 376>>>
MULTICAST - ROUTING
• Multicast router knows who wants traffic
• Finds out who is sending the traffic
• Delivers traffic only to those who want it
• Routers communicate with each other and users 
to gather the information
• Send traffic where it needs to go
• Multicast Routing deals with networks, not 
switch ports
• If one host on a network joins that group, all hosts 
on that network receive the traffic
• In the switch, a network=router port=a VLAN, so 
the traffic is broadcast on all ports of each 
network
Video 
Server
SUBNET
IGMP
Join
Multicast
Switching
Network 
Backbone

<<<PAGE 377>>>
MULTICAST - SWITCHING - IPMS
• Only the client which join a multicast group 
received the multicast packet, and the multicast 
packet stream will not flood to other ports 
where no client joins
• More efficient than multicast routing
• NI Tables contain:
• IP Source Address
• IP Destination Address (group address)
• Parent source port number
• List of ports that need to receive packet
• NIs verify that packet for given destination 
address from a certain source arrives on the 
parent port
• If true, switch/route packet to all ports in 
forwarding list
• If false, drop it
Video 
Server
SUBNET
IGMP
Join
Multicast
Switching
Network 
Backbone

<<<PAGE 378>>>
IGMP

<<<PAGE 379>>>
IGMP PROTOCOL
• The Internet Group Management Protocol (IGMP) is a simple protocol for the support of IP 
multicast
• IGMP is defined in RFC 1112
• IGMP operates on a physical network
• IGMP is used by multicast routers to keep track of membership in a multicast group
• Support for
• Joining a multicast group
• Query membership
• Send membership reports

<<<PAGE 380>>>
MULTICAST IGMP IN A NUTSHELL
Receiver_B
Receiver_C
Receiver_A
One Router (Per LAN) is  querier;
sends periodic query messages
Multicast stream is offered by one or more multicast servers
Multicast stream is required by one or more multicast clients
Server offers stream on a
multicast address e.g  225.0.0.1
Client sends report requesting
multicast group e.g  225.0.0.1
Router detects the match and
transmits multicast stream 
225.0.0.1 to the client

<<<PAGE 381>>>
IGMP VERSIONS
• Protocol used by hosts to send control frames to inform router of the desire to receive 
traffic from a MC group
• IGMP v1
• Membership Query
• Membership Report
• IGMP v2
• Membership Query
•
General Query
•
Group-Specific Query
• V2 Membership report (Fast Leave)
• Leave group
• V1 Membership Report
• IGMP v3
• Membership query
• V3 Membership report (Explicit Host Tracking)
• V2 Leave group
• V2 Membership report
• V2 Leave group
• V1 Membership report
IGMP Leave Group (v2 only)
IGMP membership report group
IGMP Member Report
IGMP membership query
IGMP Query Group (v2 only)
IGMP Source-Specific Join (v3 only)

<<<PAGE 382>>>
IGMP - USEFUL TECHNICAL DETAILS
• IGMP is a protocol confined to the local segment of the LAN
• Is never forwarded by any router and thus always has a Time-To-Live (TTL) of 1
• IGMP Host Membership Queries are sent to the "All Systems on this Subnet" class D address 
(224.0.0.1)
• IGMP "Leave Group" messages are sent to the "All Routers on this Subnet" class D address 
(224.0.0.2)

<<<PAGE 383>>>
IPV6 MULTICAST - OVERVIEW
• Multicast Listener Discovery (MLD)
• Used by IPv6 systems (hosts and routers) 
• Reporting of  IPv6 multicast group memberships to any neighboring multicast routers 
• Similar to IGMP for IPv4
• MLD messages are sent with
• Link-local IPv6 Source address
• Hop limit of one
• IPv6 Destination address FF02:0:0:0:0:0:0:16
• MLD Version 1 
• Forwarding by IPv6 multicast destination addresses
• MLD Version 2
• Forwarding by source IPv6 addresses and IPv6 multicast destination addresses
• OmniSwitch version supported
• MLDv1 and MLDv2

<<<PAGE 384>>>
IPMS

<<<PAGE 385>>>
MULTICAST - SWITCHING VS. ROUTING DECISION
• Port list is a combination of hosts and peer routers
• Destination Slot/Port can be is a downstream router or a client
• Destination port could be in same or different VLAN
• If in same VLAN, switch packet
• Use IPMS forwarding table to forward packets to ports
• If in different VLAN, route packet
• Use DVMRP/PIM forwarding table to deliver packets to downstream routers
• Change source MAC address to router port MAC address
• Send packet on destination port
• IPMS
• Intercepts IGMP packets to track membership by port rather than by network 
• Two sets of information are combined to tell switches how to forward/route traffic
• Performance is significantly improved because forwarding decisions are made by hardware
• Forwarding tables created by DVMRP, PIM-SM, PIM-DM and IPMS

<<<PAGE 386>>>
HOW DOES MULTICAST SWITCHING WORK?
• IP Multicast Switching
• Based on the IGMP query and report messages 
that are snooped, the switch forwards multicast
traffic only to the ports that requested it
• Forwarding Tables created by IGMP Snooping
Without multicast switching, multicast traffic would be forwarded to the entire VLAN
1/2/4
1/5/22
Group
Port
Src IP
Vlan
226.0.0.4
228.1.1.1
1/5/22
1/2/4
1.1.1.2
2.2.2.3
2
34
IGMP Join (228.1.1.1)

<<<PAGE 387>>>
HOW DOES MULTICAST SWITCHING WORK?
• By maintaining this multicast forwarding table, the switch dynamically forward multicast 
traffic only to those interfaces that want to receive it as nominal unicast forwarding does
Video 
Server
L3 Multicast
Switch
Forward Mcast 
traffic to port on 
which the join 
message was 
received
Without multicast switching, multicast traffic would be forwarded to the entire VLAN

<<<PAGE 388>>>
CONFIGURING IPMS
• The minimum configuration
• Enables or disables IP Multicast Switching and Routing on a specific VLAN or globally
• Enables or disables IP Multicast Switching and Routing on a specific VLAN or globally
IPMS is disabled by default
-> ip multicast admin-state enable
-> ip multicast vlan 10 admin-state enable

<<<PAGE 389>>>
CONFIGURING IPMS
• The minimum configuration
• Enables or disables IGMP querying on a specific VLAN or globally
• Refers to requesting the network's IGMP group membership information by sending out IGMP queries
• Enables or disables IGMP querier forwarding on the specified VLAN or on the system if no VLAN is specified
• Querier-forwarding feature should be enabled if a streaming device is connected to a switch, which is not a 
querier
• All multicast traffic is sent to the "Querier" switch
-> ip multicast querying enable
-> ip multicast querier-forwarding enable

<<<PAGE 390>>>
CONFIGURING IPMS - OPTIONS
• Configuring IGMP Version
• Configuring IGMP Query Interval
• Modifying IGMP Query Response Interval
• Modifying IGMP Last Member Query Interval
• Configuring IGMP Expire Router Timeout
• Enabling Multicast Zapping
-> ip multicast [vlan vid] version [version]
-> ip multicast [vlan vid] query-response-interval [tenths-of-seconds]
-> ip multicast [vlan vid] query-interval [seconds]
-> ip multicast [vlan vid] last-member-query-interval [tenths-of-seconds]
-> ip multicast [vlan vid] router-timeout [seconds]
-> ip multicast [vlan vid] zapping [{enable | disable}]

<<<PAGE 391>>>
IPMS MONITORING
IGMP Group Membership Table Entries
• Group Address 
• IP address of the IP multicast group
• Source Address 
• IP address of the IP multicast source
• VLAN
• VLAN associated with the IP multicast group
• Port
• Slot and port number of the IP multicast group
• Mode 
• IGMP source filter mode
• Static 
• Whether it is a static multicast group or not
• Count 
• Number of IGMP membership requests made
• Life 
• Life time of the IGMP group membership
-> show ip multicast group
Total 2 Groups
Group Address   Source Address  VLAN  Port  Mode     Static  Count  Life
---------------+---------------+-----+-----+--------+-------+------+-----
225.0.0.101     0.0.0.0          1    1/1/1   exclude  no      49     239
225.0.0.102     0.0.0.0          1    1/1/1   exclude  no      49     243
239.255.255.250 0.0.0.0          1    1/1/1   exclude  no      48     241
239.255.255.250 0.0.0.0          1    1/1/24  exclude  no      45     239

<<<PAGE 392>>>
IPMS MONITORING
IGMP Neighbor Table Entries 
• Host Address
• IP address of the IP multicast neighbor
• VLAN
• VLAN associated with the IP multicast neighbor
• Port
• Slot and port number of the IP multicast neighbor
• Static
• Whether it is a static IP multicast neighbor or not
• Count
• Displays the count of IP multicast neighbor
• Life
• Life time of the IP multicast neighbor
-> show ip multicast neighbor
Total 2 Neighbors
Host Address    VLAN  Port   Static  Count  Life
---------------+-----+-----+-------+------+-----
192.168.10.2    10    1/1/9   no      76     61
192.168.10.3    10    1/1/24  no      75     60

<<<PAGE 393>>>
IPMS MONITORING
Forwarding Table
• Group Address 
• IP group address of the IP multicast forward
• Host Address 
• IP host address of the IP multicast forward
• Tunnel Address
• IP source tunnel address of the IP multicast 
forward
• VLAN
• VLAN associated with the IP multicast forward
• Port
• Slot and port number of the IP multicast forward
-> show ip multicast forward
Total 2 Forwards
Ingress     Egress
Group Address   Host Address    Tunnel Address  VLAN  Port  VLAN   Port
---------------+---------------+---------------+-----+-----+-----+-----
225.0.0.101     192.168.100.10  0.0.0.0          1    2/1/1   1    1/2/24
225.0.0.102     192.168.100.10  0.0.0.0          1    2/1/1   1    1/2/24

<<<PAGE 394>>>
L2 STATIC MULTICAST
• Configures a static multicast MAC address and assigns the address to one or more egress 
ports 
• Packets received on ports associated with the specified VLAN that contain a destination MAC 
address that matches the static multicast address are forwarded to the specified egress ports
• Static multicast MAC addresses maintained in the Source Learning MAC address table
• Assigns the multicast address 01:25:9a:5c:2f:10 to port 1/1/24 in VLAN 20
• Assigns a static multicast MAC address to link aggregate ID 2 associated with VLAN 455
mac-learning {vlan vlan_id {port chassis/slot/port | linkagg agg_id }} 
multicast mac-address multicast_address [group group_id] 
mac-learning flush [vlan vlan_id [port chassis/slot/port | linkagg agg_id ]]
multicast [mac-address multicast_address] 
-> mac-learning vlan 20 port 1/1/24 multicast mac-address 01:25:9a:5c:2f:10
-> mac-learning vlan 455 linkagg 2 multicast mac-address 01:95:2A:00:3E:4c

<<<PAGE 395>>>
IGMP - RELAY
• IGMP Forwarding to Specific Host in L3 
Environment
• Encapsulates IGMP packets in an IP packet
to a special device/server
• Specifies the destination IP address of a relay host where 
IGMP host reports and Leave messages are to be sent
• Notified multicast server forwards a new multicast stream 
when a subscriber has joined the new group without 
relying on the L3 multicast network (e.g. PIM) to 
propagate this event
• Create the helper address
• Display Helper address information
-> show ip multicast 
Status                                          
= enabled,
Querying                                        
= enabled,
Proxying
= disabled,
Spoofing                                       
= enabled,
Zapping                                         
= disabled,
Querier Forwarding                              
= enabled,
Flood Unknown                                   
= enabled,
Version                                         
= 3,
Robustness                                      
= 2,
Query Interval (seconds)                       
= 125,
Query Response Interval (tenths of seconds)    
= 100,
Last Member Query Interval (tenths of seconds)  
= 10,
Unsolicited Report Interval (seconds)           
= 1,
Router Timeout (seconds)                        
= 90,
Source Timeout (seconds)                        
= 30,
Max-group                                       
= 0,
Max-group action                                
= none
Helper-address                                  
= 11.107.61.132
-> ip multicast helper-address 11.107.61.132

<<<PAGE 396>>>
IGMP THROTTLING
• Configures the maximum group limit learned per VLAN, per port or globally
• Global
• VLAN
• Port
• Applicable for all VLAN instances of the port
• Per port limit overrides VLAN and global configuration
• Actions
• None. Disables the maximum group limit configuration
• Drop. Drops the incoming membership request
• Replace. Replaces an existing membership with the incoming membership request
-> ip multicast port slot|port max-group [num] [action {none | drop | replace}]
-> ip multicast vlan vid max-group [num] [action {none | drop | replace}]
-> ip multicast max-group [num] [action {none | drop | replace}]

<<<PAGE 397>>>
STORM CONTROL 
• Configuration of different thresholds for each type of storm/flood traffic
• Broadcast
• Multicast
• Unknown Unicast
• Thresholds configuration
• rate % num: rate in % of the port speed 
• rate mbps num:  rate in true mbits per sec 
• rate pps num: rate in packet per sec
• Configures the action on a single port, a range of ports, when the port reaches the storm 
violated state
interfaces {slot chassis/slot| port chassis/slot/port[-port2]} flood-limit {bcast | mcast | uucast | all} 
rate {pps pps_num| mbps mbps_num | cap% cap_num | enable | disable | default} [low-threshold low_num] 
interfaces {slot chassis/slot| port chassis/slot/port[-port2]} flood-
limit {bcast | mcast | uucast | all} action {shutdown | trap | default}

<<<PAGE 398>>>
LOAD BALANCING MULTICAST ON LINK AGGREGATION
• Multicast traffic is by default forwarded through the primary port of the Link Aggregation 
Group
• Option to enable hashing for non-unicast traffic, which will load balance the non-unicast 
traffic across all ports in the Link Aggregation
• If non-ucast option is not specified, link aggregation will only load balance unicast packets
-> hash-control {brief | extended [udp-tcp-port] | load-balance non-ucast {enable | disable}}
-> show hash-control
Hash Mode    = brief,
Udp-Tcp-Port = disabled
-> show hash-control non-ucast
Non-ucast Hash Status = Disabled

<<<PAGE 399>>>
INITIAL MULTICAST PACKET BUFFERING
• Avoids loss of first multicast packets in a routed environment
• Maximum number of multicast packets that can be buffered by multicast stream
• Enables or disables initial packet buffering for IPv4 and IPV6 multicast flows on the 
specified VLAN or globally on the switch.
-> ip multicast initial-packet-buffer admin-state enable
(default: disable)
-> ipv6 multicast initial-packet-buffer admin-state enable
-> ip multicast initial-packet-buffer max-packet
(1 to 10) (default: 4)
-> ipv6 multicast initial-packet-buffer max-packet
-> ip multicast [vlan vlan_id[-vlan_id2]] initial-packet-buffer admin-state {enable | disable}
-> ipv6 multicast [vlan vlan_id[-vlan_id2]] initial-packet-buffer admin-state {enable | disable}

<<<PAGE 400>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 401>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
AOS OmniSwitch 
Prior Configuration 
How to 
✓ Set up a network topology 
Contents 
1 
Introduction .................................................................................... 2 
2 
Prior Configuration ............................................................................ 2 
2.1. OS6360-A............................................................................................. 2 
2.2. OS6860-A............................................................................................. 2 
2.3. OS6860-B ............................................................................................. 2 
2.4. OS6900-A............................................................................................. 2 
2.5. Client 1 .............................................................................................. 2

<<<PAGE 402>>>
2 
Prior Configuration 
 
 1 
Introduction 
In this lab, we will perform a configuration on the OmniSwitch switches to test features.  
 2 
Prior Configuration 
Enter the following commands on the switches: 
2.1. 
OS6360-A 
sw5 (OS6360-A) -> ip interface Loopback0 address 192.168.254.5 
sw5 (OS6360-A) -> ip interface int_57 address 192.168.57.5/24 vlan 57 
sw5 (OS6360-A) -> ip static-route 0.0.0.0/0 gateway 192.168.57.7 metric 1 
sw5 (OS6360-A) -> ip static-route 0.0.0.0/0 gateway 192.168.57.8 metric 2 
2.2. 
OS6860-A 
sw7 (6860-A) -> ip interface int_57 address 192.168.57.7/24 vlan 57 
sw7 (6860-A) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.57.0/24 permit 
sw7 (6860-A) -> ip static-route 192.168.254.5/32 gateway 192.168.57.5 
sw7 (6860-A) -> ip route-map "staticIntoOspf" sequence-number 10 action permit 
sw7 (6860-A) -> ip route-map staticIntoOspf sequence-number 10 match ip-address 192.168.254.5/32 permit 
sw7 (6860-A) -> ip redist static into ospf route-map "staticIntoOspf" admin-state enable 
2.3. 
OS6860-B 
sw8 (6860-B) -> ip interface int_57 address 192.168.57.8/24 vlan 57 
sw8 (6860-B) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.57.0/24 permit 
sw8 (6860-B) -> ip static-route 192.168.254.5/32 gateway 192.168.57.5 
2.4. 
OS6900-A 
sw1 (6900-A) -> vlan 110  
sw1 (6900-A) -> vlan 110 members port 1/1/1 untagged 
sw1 (6900-A) -> ip interface int_110 address 192.168.110.1/24 vlan 110 
sw1 (6900-A) -> interfaces 1/1/1 admin-state enable 
sw1 (6900-A) -> ip route-map localIntoOspf sequence-number 10 match ip-address 192.168.110.0/24 permit 
2.5. 
Client 1  
In the next lab the client 1 will be used. Configure the following IP settings for this client:  
IP address = 192.168.110.51 
Subnet mask = 255.255.255.0 
Default gateway = 192.168.110.1 
Preferred DNS server = 10.0.0.51

<<<PAGE 403>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Multicast switching 
How to 
✓ This lab is designed to familiarize you with the IP multicast switching 
capability on the OmniSwitch family of products 
Contents 
1 
Toplogy ......................................................... Erreur ! Signet non défini. 
2 
IP Multicast Switching ........................................................................ 3 
2.1. Without IPMS enable ............................................................................... 3 
2.2. IP Multicast Switching (IPMS) enable ............................................................ 5

<<<PAGE 404>>>
2 
Multicast switching 
 
 1 
Topology 
Multicast switching is used to efficiently handle multicast traffic by forwarding multicast packets only to the 
switch ports that need to receive them 
 
- The configuration for multicast switching is simple, requiring only that the switches be bridged together. 
A multicast stream(s) will then be started at the multicast server 
- For this lab, we will have 3 clients connected on the same VLAN.  
- Check vlan 30 members on 6360-A 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/2      default      forwarding 
  2/1/2      default      forwarding 
  0/7        tagged     dhl-blocking 
  0/8        tagged      forwarding 
 
sw8 (6860-B) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        tagged      forwarding 
  0/78       tagged      forwarding 
 
sw8 (6860-B) -> vlan 30 members port 1/1/1 untagged 
 
sw8 (6860-B) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      default      forwarding 
  0/7        tagged      forwarding 
  0/78       tagged      forwarding 
 
- Get IP addresses from the clients (ipconfig /all) retrieved from dhcp server. 
Client 8:  
 
Client 9:  
 
Client 10:  
 
- Try to ping each client from each other to ensure L2 connectivity

<<<PAGE 405>>>
3 
Multicast switching 
 
 2 
IP Multicast Switching 
2.1. 
Without IPMS enable  
Before you begin, notice that Multicast Switching is disabled by default: 
sw5 (6360-A) -> show ip multicast 
Profile                                          = default, 
Status                                           = disabled, 
Flood Unknown                                    = disabled, 
----- 
 
sw7 (6870-A) -> show ip multicast 
Profile                                          = default, 
Status                                           = disabled, 
Flood Unknown                                    = disabled, 
 
sw8 (6860-B) -> show ip multicast 
Profile                                          = default, 
Status                                           = disabled, 
Flood Unknown                                    = disabled, 
 
Resets all Layer 2 statistics counters 
sw5 (6360-A) -> clear interfaces 2/1/2 l2-statistics 
sw5 (6360-A) -> clear interfaces 1/1/2 l2-statistics 
 
sw8 (6860-B) -> clear interfaces 1/1/1 l2-statistics 
 
sw5 (6360-A) ->  show interfaces 2/1/2 
Chassis/Slot/Port          : 2/1/2 
 Operational Status        : up, 
 Port-Down/Violation Reason: None, 
 Last Time Link Changed    : Sat Jul  3 04:16:15 2021, 
 Number of Status Change   : 1, 
 Type                      : Ethernet, 
 SFP/XFP                   : N/A, 
 Interface Type            : Copper, 
 EPP                       : Disabled, 
 Link-Quality              : N/A, 
 MAC address               : 94:24:e1:7c:79:6c, 
 BandWidth (Megabits)      :      100,                  Duplex           : Full, 
 Autonegotiation           :   1  [ 1000-F 100-F 100-H 10-F 10-H ], 
 Long Frame Size(Bytes)    : 1552, 
 Inter Frame Gap(Bytes)    : 12, 
 loopback mode             : N/A, 
 Rx              : 
 Bytes Received  :                    0, Unicast Frames :                    0, 
 Broadcast Frames:                    0, M-cast Frames  :                    0, 
 UnderSize Frames:                    0, OverSize Frames:                    0, 
 Lost Frames     :                    0, Error Frames   :                    0, 
 CRC Error Frames:                    0, Alignments Err :                    0, 
 Tx              : 
 Bytes Xmitted   :                    0, Unicast Frames :                    0, 
 Broadcast Frames:                    0, M-cast Frames  :                    3, 
 UnderSize Frames:                    0, OverSize Frames:                    0, 
 Lost Frames     :                    0, Collided Frames:                    0, 
 Error Frames    :                    0, Collisions     :                    0, 
 Late collisions :                    0, Exc-Collisions :                    0

<<<PAGE 406>>>
4 
Multicast switching 
 
Open the “send” application from the client's desktop 8. And fill up as below the tool window. 
This tool generates multicast IP packets, with Destination IP address (multicast group) 231.1.1.5 on stream01. 
Click on start  
 
 
As the packets are sent check the counters on the VLAN 30 interfaces of 6360-A  
sw5 (6360-A) -> show interfaces 2/1/2 
Chassis/Slot/Port          : 2/1/2 
 Operational Status        : up, 
 Port-Down/Violation Reason: None, 
 Last Time Link Changed    : Tue Jul  6 23:03:13 2021, 
 Number of Status Change   : 3, 
 Type                      : Ethernet, 
 SFP/XFP                   : N/A, 
 Interface Type            : Copper, 
 EPP                       : Disabled, 
 Link-Quality              : N/A, 
 MAC address               : 94:24:e1:7c:79:6d, 
 BandWidth (Megabits)      :      100,                  Duplex           : Full, 
 Autonegotiation           :   1  [ 1000-F 100-F 100-H 10-F 10-H ], 
 Long Frame Size(Bytes)    : 1552, 
 Inter Frame Gap(Bytes)    : 12, 
 loopback mode             : N/A, 
 Rx              : 
 Bytes Received  :                 1811, Unicast Frames :                   13, 
 Broadcast Frames:                    1, M-cast Frames  :                    0, 
 UnderSize Frames:                    0, OverSize Frames:                    0, 
 Lost Frames     :                    0, Error Frames   :                    0, 
 CRC Error Frames:                    0, Alignments Err :                    0, 
 Tx              : 
 Bytes Xmitted   :                33985, Unicast Frames :                   15, 
 Broadcast Frames:                    5, M-cast Frames  :                  387, 
 UnderSize Frames:                    0, OverSize Frames:                    0, 
 Lost Frames     :                    0, Collided Frames:                    0, 
 Error Frames    :                    0, Collisions     :                    0, 
 Late collisions :                    0, Exc-Collisions :                    0

<<<PAGE 407>>>
5 
Multicast switching 
 
sw5 (6360-A) -> show interfaces 1/1/2 
Chassis/Slot/Port          : 1/1/2 
 Operational Status        : up, 
 Port-Down/Violation Reason: None, 
 Last Time Link Changed    : Tue Jul  6 02:14:48 2021, 
 Number of Status Change   : 1, 
 Type                      : Ethernet, 
 SFP/XFP                   : N/A, 
 Interface Type            : Copper, 
 EPP                       : Disabled, 
 Link-Quality              : N/A, 
 MAC address               : 94:24:e1:7c:82:25, 
 BandWidth (Megabits)      :      100,                  Duplex           : Full, 
 Autonegotiation           :   1  [ 1000-F 100-F 100-H 10-F 10-H ], 
 Long Frame Size(Bytes)    : 1552, 
 Inter Frame Gap(Bytes)    : 12, 
 loopback mode             : N/A, 
 Rx              : 
 Bytes Received  :                 4020, Unicast Frames :                   21, 
 Broadcast Frames:                    2, M-cast Frames  :                    0, 
 UnderSize Frames:                    0, OverSize Frames:                    0, 
 Lost Frames     :                    0, Error Frames   :                    0, 
 CRC Error Frames:                    0, Alignments Err :                    0, 
 Tx              : 
 Bytes Xmitted   :                49924, Unicast Frames :                   18, 
 Broadcast Frames:                   13, M-cast Frames  :                  705, 
 UnderSize Frames:                    0, OverSize Frames:                    0, 
 Lost Frames     :                    0, Collided Frames:                    0, 
 Error Frames    :                    0, Collisions     :                    0, 
 Late collisions :                    0, Exc-Collisions :                    0 
As you can see in the capture below, by default multicast traffic is flooded on all the port on the same VLAN 
as the source. 
2.2. 
IP Multicast Switching (IPMS) enable 
Next, enable IP Multicast Switching (IPMS). With IPMS enabled only ports with devices that requested to see 
the stream will have it forwarded. Without it, multicast traffic would be treated as a broadcast and sent to 
all ports in the VLAN.  
Enable Multicast Switching: 
sw5 (6360-A) -> ip multicast admin-state enable 
sw7 (6870-A) -> ip multicast admin-state enable 
sw8 (6860-B) -> ip multicast admin-state enable 
 
Reset all Layer 2 statistics counters 
sw5 (6360-A) -> clear interfaces 2/1/1-2 l2-statistics 
sw5 (6360-A) -> clear interfaces 1/1/2 l2-statistics 
 
sw8 (6860-B) -> clear interfaces 1/1/1 l2-statistics 
 
Check the configuration on the three switches:  
sw5 (6360-A) -> show ip multicast 
Profile                                          = default, 
Status                                           = enabled, 
 
sw7 (6870-A) -> show ip multicast 
Profile                                          = default, 
Status                                           = enabled, 
 
sw8 (6860-B) -> show ip multicast 
Profile                                          = default, 
Status                                           = enabled, 
 
sw5 (6360-A) -> clear interfaces 2/1/1-2 l2-statistics 
sw5 (6360-A) -> clear interfaces 1/1/2 l2-statistics

<<<PAGE 408>>>
6 
Multicast switching 
 
 On 6860--B enable Multicast Querying (the switch where the multicast server is connected to): 
6860-B -> ip multicast querying enable 
 
On 6360-A, 6870-A and 6860, enable Querier Forwarding: 
6360-A -> ip multicast querier-forwarding enable 
6870-A -> ip multicast querier-forwarding enable 
6860-B -> ip multicast querier-forwarding enable 
From client 8, restart the application “send” to send multicast traffic. 
 
Open the “receive” application from the client's desktop 9 to subscribe to multicast traffic. (IP address 
(multicast group) 231.1.1.5)

<<<PAGE 409>>>
7 
Multicast switching 
 
Check multicast forward and group on 6360-A switch 
sw5 (6360-A) -> show ip multicast forward 
Total 0 Forwards 
 
                                                  Ingress               Egress 
Group Address   Host Address    Tunnel Address  Vlan/Service   Vlan/Service   Interface 
---------------+---------------+---------------+--------------+--------------+---------------------- 
 
sw5 (6360-A) -> show ip multicast group 
Total 4 Groups 
 
Group Address   Source Address  Vlan/Service   Interface              Mode     Static  Count  Life 
---------------+---------------+--------------+----------------------+--------+-------+------+----- 
231.1.1.5       0.0.0.0         vlan 30        1/1/2                  exclude  no      3      254 
239.255.255.250 0.0.0.0         vlan 30        1/1/2                  exclude  no      3      227 
239.255.255.250 0.0.0.0         vlan 30        2/1/1                  exclude  no      3      226 
239.255.255.250 0.0.0.0         vlan 30        2/1/2                  exclude  no      4      231 
 
This shows all IGMP requests seen by the switch 
 
 
Notes 
239.255.255.250 is the multicast address of SSDP (Simple Service Discovery Protocol), basis of the discovery 
protocol of universal Plug& Play (UPnP) 
 
Check also multicast forward and group on 6860-B: 
sw8 (6860-B) -> show ip multicast forward 
Total 1 Forwards 
                                                  Ingress               Egress 
Group Address   Host Address    Tunnel Address  Vlan/Service   Vlan/Service   Interface 
---------------+---------------+---------------+--------------+--------------+---------------------- 
231.1.1.5       0.0.0.0         0.0.0.0         vlan 30        vlan 30        0/8 
 
sw8 (6860-B) -> show ip multicast group 
 
Total 4 Groups 
 
Group Address   Source Address  Vlan/Service   Interface              Mode     Static  Count  Life 
---------------+---------------+--------------+----------------------+--------+-------+------+----- 
239.255.255.250 0.0.0.0         vlan 20        0/78                   exclude  no      7      239 
239.255.255.250 0.0.0.0         vlan 30        1/1/1                  exclude  no      7      245 
231.1.1.5       0.0.0.0         vlan 30        0/8                    exclude  no      5      245 
239.255.255.250 0.0.0.0         vlan 30        0/8                    exclude  no      14     245 
 
Check also multicast forward and group on 6870-A : 
sw7 (6870-A) -> show ip multicast forward 
Total 0 Forwards 
 
                                                  Ingress               Egress 
Group Address   Host Address    Tunnel Address  Vlan/Service   Vlan/Service   Interface 
---------------+---------------+---------------+--------------+--------------+---------------------- 
 
sw7 (6870-A) -> show ip multicast group 
Total 1 Groups 
 
Group Address   Source Address  Vlan/Service   Interface              Mode     Static  Count  Life 
---------------+---------------+--------------+----------------------+--------+-------+------+----- 
239.255.255.250 0.0.0.0         vlan 20        0/7                    exclude  no      6      196

<<<PAGE 410>>>
DISTANCE VECTOR MULTICAST ROUTING PROTOCOL
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 411>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the Distance Vector Multicast Routing 
Protocol (DVMRP)

<<<PAGE 412>>>
AOS SPECIFICATIONS
• Distance Vector Multicast Routing Protocol
• Similar to RIP
• Infinity = 32 hops
• Subnet masks in route advertisements
• 1 Multicast Protocol per Interface (PIM or DVMRP)
• 128 interfaces
• 256 neighbors
• RFCs Supported
• 2667 – IP Tunnel MIB
• DVMRP Attributes
• Reverse Path Multicasting
• Neighbor Discovery 
• Multicast Source Location
• Route Report Messages
• Distance Metrics
• Dependent Downstream Routers
• Poison Reverse
• Pruning
• Grafting
• DVMRP Tunnels

<<<PAGE 413>>>
OVERVIEW
• DVMRP Version 3.255 supported
• V3 backward compatible with V1
• Supports IP Tunneling
• Unicast connection between two IP Multicast routers for traversing non-multicast devices
• Reverse Path Multicasting
• If a packet arrived on an upstream interface that would be used to transmit packets back to the 
source, it is forwarded to the appropriate list of downstream interfaces. 
• Otherwise, it is not on the optimal delivery tree and is discarded. In this way, duplicate packets 
can be filtered when loops exist in the network topology.
• Source location
• Look up route to source to determine which interface to accept traffic on
• The Unicast routing table is propagated
• Split horizon is used (don’t propagate routes on the interface that you learned them from)

<<<PAGE 414>>>
SPECIFICATIONS

<<<PAGE 415>>>
NEIGHBOR DISCOVERY
• DVMRP Probe packet
• Periodic multicast group address packet
• Multicast address packets via 224.0.0.4 (All-DVMRP Routers)
-> show ip dvmrp neighbor
Neighbor Address Vlan    Uptime     Expires     GenID
Version   State
---------------+-----+-----------+-----------+---------+---------+-------
143.209.92.214    2   00h:09m:12s 00h:00m:06s 546947509  3.255    active
R1
R2
R3
Probe for neighbor 
discovery
Server
Client

<<<PAGE 416>>>
FLOOD AND PRUNE 
• Flood and Prune Protocol
• Multicast traffic is flooded to all downstream routers
• This can be efficient if there are a large number of recipients.
• Routers that do not have clients registered to receive traffic will send a DVMRP prune message
Flood
Prune
Traffic
Flood
Prune

<<<PAGE 417>>>
GRAFT 
• Grafting:
• Adding a branch to multicast traffic delivery
• If new IGMP membership requests are received, the router sends a “graft” message
• Graft is only used after a prune  
• Waits for “graft ack”
If no ack, re-send
• When prune times out, upstream router starts flooding traffic again (7200 sec.)
• Router receives message, duplicates and sends it to local subscribers, and sends it on (if necessary)
New Tree
New Client
Graft
Graf
t
New Client

<<<PAGE 418>>>
ROUTING TABLE
-> show ip dvmrp route
Address/Mask    Gateway  Metric   Age        Expires   Flags
--------------+---------+------+------------+---------+-----
11.0.0.0/       55.0.0.5    2    00h:13m:14s 02m:07s     R
22.0.0.0/8      44.0.0.4    2    10h:33m:14s 02m:15s     R
44.0.0.0/8         -
10     5h:24m:59s    -
L
R1
R2
Server
Client
R3
Route Exchange
Route Exchange

<<<PAGE 419>>>
CLI CONFIGURATION
• Minimum configuration
• Summary of the show commands used for verifying the DVMRP configuration
-> ip load dvmrp
-> ip dvmrp interface <interface_name>
-> ip dvmrp admin-state enable 
-> write memory

<<<PAGE 420>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 421>>>
PROTOCOL INDEPENDENT MULTICAST (PIM)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 422>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the PIM Dense Mode protocol 
• Describe the PIM Sparse Mode protocol
• Learn how to configure and monitor them

<<<PAGE 423>>>
PIM - SPARSE MODE (PIM-SM)

<<<PAGE 424>>>
AOS SPECIFICATIONS
• Protocol Independent Multicast – Sparse Mode version 2
• RFCs Supported 
• 2362 - Protocol Independent Multicast-Sparse Mode (PIM-SM) Protocol Specification
• 2934 - Protocol Independent Multicast MIB for Ipv4
• 2932 - Ipv4 Multicast Routing MIB
• 3973 - Protocol Independent Multicast-Dense Mode (PIM-DM)
• 3376 - Internet Group Management Protocol
• 4601 - Protocol Independent
• 128 interfaces
• Maximum RPs allowed in a PIM-SM domain
• 100 (default value is 32)
• 1 multicast protocol per interface (PIM or DVMRP)

<<<PAGE 425>>>
AOS SPECIFICATIONS
Specifications

<<<PAGE 426>>>
PIM-SM - PROTOCOL OVERVIEW
• PIM-SM is not a flood and prune mechanism.
It requires explicit joins.
• PIM-SM relies on the underlying IGP protocols
to make its routing decisions.
• It uses a Rendezvous Point (RP) as a shared 
tree where sources send data to the RP who 
distributes the data to receivers using a shared 
tree.
• PIM-SM, like all multicast protocols, uses 
Reverse Path Forwarding (RPF).
• RPF = Forward a multicast packet only if it is 
received on an interface that is used by the 
router to route to the source.
A
B
C
D
100
100
1000
100
A1
C1
D1
Source 1

<<<PAGE 427>>>
NEIGHBOR DISCOVERY & DESIGNATED ROUTER
• Neighbor Discovery
• PIM Hello
• Periodic multicast group address packet
(224.0.0.13= ALL-PIM-ROUTERS group) 
• TTL= 1
• Default = 30 seconds
• Designated Router (DR)
• One per subnet, sends join messages to RP
• Election based on:
• Highest Priority
• Highest IP address
• If the “DR” times-out, a new “DR” is elected
• Interface is added to egress interface list for all groups when first neighbor is heard
PIM
router
PIM
router
PIM
router
PIM Hello
PIM Hello
PIM Hello

<<<PAGE 428>>>
-> show ip multicast forward
PIM-SM - RENDEZ-VOUS POINT TREE RPT  
• Rendezvous Point (RP)
• Common forwarding router for a shared distribution 
tree
• Each group has a RP
• Receivers send explicit join message to RP
• Each source sends multicast data packets 
encapsulated in unicast packets to RP (Register 
message).
• RP can be configured statically
• Or dynamically through a Bootstrap router
• Robustness: When the primary RP goes down, 
bootstrap protocol can select an alternate RP
• A Candidate Rendezvous Point (C-RP) sends periodic 
C-RP advertisements to the BSR
• Shared Distribution Tree/ Rendezvous Point Tree 
(RPT)
• The distribution tree for multicast traffic
Register message
Multicast Traffic
PIM Join
R1
R2
Client
R3
RP
IGMP 
R4
1/1/15
1/2/5
224.2.190.33
Server
172.39.2.2
PIM Join
PIM Join

<<<PAGE 429>>>
PIM-SM - SHORTEST PATH TREE (SPT) 
• Once the last-hop router receives traffic form the RP along the RPT, it sends a PIM join 
message towards the source of traffic.
• This forms the shortest path tree (SPT), which is rooted at the first-hop router closest to 
the source.
R1
R2
R3
RP
R4
PIM Join
Multicast Traffic
Server
172.39.2.2
Client
(S,G) join

<<<PAGE 430>>>
PIM-SM - SPT SWITCHOVER 
• Once the multicast traffic goes along the SPT, 
the last-hop router generates a PIM prune 
message towards the RP.
• The RP stops sending multicast traffic along the 
RPT and generates a Register-Stop message that 
is sent to the first-hop router
• The first-hop router stops the encapsulation of 
the multicast traffic that was sent to the RP and 
forwards the traffic along the SPT.
The switchover is initiated automatically by the last DR
SPT status is enabled by default
PIM Prune
Multicast Traffic
Prune
Prune
Register-Stop
R1
R2
R3
RP
R4
Server
172.39.2.2
Client

<<<PAGE 431>>>
BOOTSTRAP ROUTER
• BootStrap Router (BSR)
• Keeps routers in network up to date on reachable C-
RPs
• Candidate Bootstrap Router (C-BSR)
• Eligible to become a BSR
• Bootstrap election mechanism
• Multiple routers configured with a priority
• While only a single BSR can be operational at one 
time, other routers are available to take over in the 
event of a failure
• C-RP periodically sends out C-RP advertisements
• When a BSR receives one of these advertisements, 
the associated C-RP is considered reachable (if it has 
a valid route)
• BSR then periodically sends its RP set to neighboring 
routers in the form of a Bootstrap message 
Bootstrap (I want to be BSR)
1
Bootstrap (I am the new BSR )
2
C-RP (I want to be RP for this group)
3

<<<PAGE 432>>>
BOOTSTRAP ROUTER
• Calculation steps for selecting the RP
• RP set = list of reachable C-RPs
• Locate all RPs in RP-Set associated with the most specific advertised group range for the specific 
group in the PIM Join message
• All devices with the best priority (lowest value)
• Highest Hash value using the group address, the RP address, and the advertised then elect the RP with the 
highest hash value
• RP with the highest IP address
RP-Set (list of CRP/Group)
5
RP-SET
RP
Group
4

<<<PAGE 433>>>
PIM
DENSE MODE (PIM –DM)

<<<PAGE 434>>>
PIM-DM - OVERVIEW
• Protocol Independent Multicast – Dense Mode 
• Designed for networks with many receivers
• Flood and Prune operation similar to DVMRP
• Does flood all multicast traffic initially
• Performs reverse path forwarding (RPF)
• Fully integrated with the existing PIM Sparse Mode
• Still relies on unicast routing protocols such as RIP and OSPF
• Same packet formats as PIM-SM
• Re-using “pim” configuration
• No periodic joins transmitted, only explicitly triggered prunes and grafts
• No Rendezvous Point (RP)

<<<PAGE 435>>>
PIM-DM - FLOOD AND PRUNE
• PIM Prunes are sent to stop unwanted traffic
• Multicast Traffic flows through network
• The tree is pruned
• Prunes timeout in 3 minutes
• Traffic is flooded throughout the entire network
• Prune process takes place
• Traffic is flooded throughout the entire network
• Routers receive multicast traffic on RPF interfaces
• Routers forward to their neighbors
• Packets received on non RPF interfaces are dropped
Flood & Prune process
repeats every 3 minutes
Server
Client
Client
Client
Server
Client
Client
Client

<<<PAGE 436>>>
OPERATION AND CONFIGURATION

<<<PAGE 437>>>
PIM - CLI
Minimum configuration
-> ip load pim
-> ip pim interface <interface_name > 
-> ip pim ssm group group_address/prefix_length [[no] override] [priority priority]
-> ip pim candidate-rp rp_address group-address/prefix_length [priority priority] [interval seconds]
-> ip pim cbsr <interface_address > 
-> ip pim sparse admin-state enable
-> ip load pim
-> ip pim interface <interface_name > 
-> ip pim dense group group_address/prefix_length [[no] override] [priority priority]
-> ip pim dense admin-state enable
PIM-SM & SSM
PIM-DM

<<<PAGE 438>>>
PIM-SM - ADVANCED CONFIGURATION
• Candidate Bootstrap Routers (C-BSRs)
•
Highest Priority value (0 to 255, default=64) –> Highest IP address
• Static RP
• Interface
•
Designated Router (DR)
•
Highest Priority value (default=1) –> Highest IP address
•
Stub
•
Specifies to not send any PIM packets via this interface, and to ignore received PIM packets
• SPT Switchover
•
Last hop DR switching to the SPT begins once the first data packet is received
• Source-specific (S, G) Join message
•
Specifies the data rate, in bits per second (bps), at which the RP will attempt to switch to native forwarding by issuing a source-specific (S, G) Join message toward the 
source
-> ip pim cbsr 192.168.3.1 priority 0
-> ip pim static-rp group_address/prefix_length rp_address [[no] override] [priority priority]
-> ip pimsm interface int_name stub
-> ip pimsm interface int_name dr-priority priority
-> ip pim spt admin-state enable
-> ip pim rp-threshold value           (default=1)

<<<PAGE 439>>>
PIM - MONITORING
-> show ip pim?
BSR
CANDIDATE-RP
CBSR 
DENSE
GROUP-MAP
GROUTE
INTERFACE
NEIGHBOR
NOTIFICATIONS
SGROUTE
SPARSE
SSM
STATIC-RP
-> show ip pim sparse
Status                     = enabled,
Keepalive Period           = 210,
Max RPs                    = 32,
Probe Time                 = 5,
Register Checksum          = header,
Register Suppress Timeout  = 60,
RP Threshold               = 1000,
SPT Status                 = enabled
sw7 (6860-A) -> show ip pim candidate-rp
RP Address       Group Address       Priority  Interval  Mode  Status
----------------+-------------------+---------+---------+-----+---------
192.168.70.7     231.5.5.0/24        192       60        asm
enabled
192.168.70.7     231.7.7.0/24        192       60        asm
enabled
-> show ip pim dense
Status                       = enabled,
Source Lifetime              = 210,
State Refresh Interval       = 60,
State Refresh Limit Interval = 0,
State Refresh TTL            = 16
-> show ip pim cbsr
CBSR Address               = 192.168.70.7,
Status                     = enabled,
CBSR Priority              = 64,
Hash Mask Length           = 30,
Elected BSR                = False,
Timer                      = 00h:00m:00s,

<<<PAGE 440>>>
PIM - MONITORING 
-> show ip pim?
BSR
CANDIDATE-RP
CBSR 
DENSE
GROUP-MAP
GROUTE
INTERFACE
NEIGHBOR
NOTIFICATIONS
SGROUTE
SPARSE
SSM
STATIC-RP
-> show ip pim neighbor
Total 1 Neighbors
Neighbor Address  Interface Name       Uptime      Expires     DR Priority
-----------------+--------------------+-----------+-----------+-----------
192.168.3.2       vlan3                22h:52m:32s 00h:01m:44s    1
-> show ip pim group-map
Origin      Group Address/Prefix  RP Address      Mode  Precedence
-----------+---------------------+---------------+-----+-----------
Static RP   228.0.0.0/8           192.168.3.2     asm
none
Static SSM  226.0.0.0/8                           dm    none
Static SSM  231.0.0.0/8                           ssm
none
BSR         225.0.0.0/8           192.168.3.1     asm
20
BSR         225.0.0.0/8           192.168.3.2     asm
30
-> show ip pim ssm group
Group Address/Prefix RP Address   Mode  Override Precedence Status
--------------------+-----------+-----+--------+----------------------
231.0.0.0/8          0.0.0.0      ssm
false    none       enabled
RP-set

<<<PAGE 441>>>
PIM - MONITORING
-> show ip pim groute
Total 1 (*,G)
Group Address   RP Address     RPF Interface       Upstream Neighbor UpTime
---------------+--------------+-------------------+-------------------+---------
225.0.0.101     192.168.3.1                         00h:12m:09s
-> show ip pim?
BSR
CANDIDATE-RP
CBSR 
DENSE
GROUP-MAP
GROUTE
INTERFACE
NEIGHBOR
NOTIFICATIONS
SGROUTE
SPARSE
SSM
STATIC-RP
-> show ip pim sgroute
Legend: Flags: D = Dense, S = Sparse, s = SSM Group,
L = Local, R = RPT, T = SPT, F = Register,
P = Pruned, O = Originator
Total 2 (S,G)
Source Address  Group Address   RPF Interface      Upstream Neighbor UpTime
Flags
---------------+---------------+----------------+-------------------+--------+------
192.168.100.100 225.0.0.101     vlan100            
00h:52m:21s        STL
192.168.100.100 226.0.0.102     vlan100            
00h:52m:21s        DOL
-> show ip mroute
Total 2 Mroutes
Group Address   Src Address        Upstream Nbr
Route Address       Proto
---------------+------------------+---------------+-------------------+------
225.0.0.101     192.168.100.100/32 0.0.0.0         192.168.100.1/24    PIM-SM
226.0.0.102     192.168.100.100/32 0.0.0.0         192.168.100.0/24    PIM-DM

<<<PAGE 442>>>
PIM - MONITORING
-> show ip pim groute 225.0.0.101
(*,225.0.0.101)
UpTime
= 00h:32m:53s
RP Address              = 192.168.3.1,
PIM Mode                = ASM,
PIM Mode Origin         = Static RP,
Upstream Join State     = Not Joined,
Upstream Join Timer     = 00h:00m:00s,
Upstream Neighbor       = none,
Interface Specific State:
vlan3
UpTime
= 00h:32m:53s,
Local Membership          = False,
Join/Prune State          = Joined,
Prune Pending Timer       = 00h:00m:00s,
Join Expiry Timer         = 00h:02m:37s,
Assert State              = No Info,
Assert Timer              = 00h:00m:00s,
vlan100
UpTime
= 00h:00m:00s,
Local Membership          = False,
Join/Prune State          = No Info,
Prune Pending Timer       = 00h:00m:00s,
Join Expiry Timer         = 00h:00m:00s,
Assert State              = No Info,
Assert Timer              = 00h:00m:00s,
-> show ip pim sgroute 192.168.100.100 
225.0.0.101
(192.168.100.100,225.0.0.101)
UpTime
= 01h:15m:49s
PIM Mode                = ASM,
Upstream Join State     = Not Joined,
Upstream RPT State      = Not Joined,
Upstream Join Timer     = 00h:00m:00s,
Upstream Neighbor       = none,
SPT Bit                 = True,
DR Register State       = Pruned,
DR Register Stop Timer  = 00h:00m:00s,
Interface Specific State:
vlan3
UpTime
= 01h:15m:49s,
Local Membership          = False,
Join/Prune State          = Joined,
RPT State                 = No Info,
Prune Pending Timer       = 00h:00m:00s,
Join Expiry Timer         = 00h:02m:49s,
Assert State              = No Info,
Assert Timer              = 00h:00m:00s,
vlan100
UpTime
= 00h:00m:00s,
Local Membership          = False,
Join/Prune State          = No Info,
RPT State                 = No Info,
Prune Pending Timer       = 00h:00m:00s,
Join Expiry Timer         = 00h:00m:00s,
Assert State              = No Info,
Assert Timer              = 00h:00m:00s,

<<<PAGE 443>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 444>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
PIM-SM 
How to 
✓ This lab is designed to familiarize you with the PIM-SM capability on an 
OmniSwitch. 
Contents 
1 
Topology ........................................................................................ 2 
2 
PIM-SM Configuration ......................................................................... 4

<<<PAGE 445>>>
2 
PIM-SM 
 
 1 
Topology 
Protocol-Independent Multicast (PIM) is an IP multicast routing protocol that uses routing information 
provided by unicast routing protocols such as RIP and OSPF. PIM is “protocol-independent” because it does 
not rely on any particular unicast routing protocol. 
 
 
In the multicast switching lab, all requesting devices in the same VLAN received the multicast stream. Now 
let’s move the receivers into different VLANs. This will require the multicast traffic to be routed in order to 
reach each receiver. PIM-SM gives us the capability to route multicast traffic. 
- A multicast router is by default an IGMP querier, we can disable the querier forwarding on 6870-A and 
6860-B 
sw7 (6870-A) -> ip multicast querier-forwarding disable 
 
sw8 (6860-B) -> ip multicast querier-forwarding disable 
 
- Move back client 8 to vlan 80 
sw8 (6860-B) -> vlan 80 members port 1/1/1 untagged 
 
- Configure an IP DHCP relay on each switch 6900-A and 6870-B: 
On the 6900-A: 
sw1 (6900-A) -> ip dhcp relay destination 192.168.100.102 
sw1 (6900-A) -> ip dhcp relay admin-state enable 
sw1 (6900-A) -> show ip dhcp relay 
IP DHCP Relay : 
  DHCP Relay Admin Status        = Enable, 
  Forward Delay(seconds)         = 0, 
  Max number of hops             = 16, 
  Relay Agent Information        = Disabled, 
  Relay Agent Information Policy = Drop, 
  DHCP Relay Opt82 Format  =  Base MAC, 
  DHCP Relay Opt82 String  =  e8:e7:32:d4:88:95, 
  PXE support                    = Disabled, 
  Relay Mode                     = Global, 
  Bootup Option                  = Disable,

<<<PAGE 446>>>
3 
PIM-SM 
 
- Configure an IP DHCP relay on each switch 6900-A and 6870-B: 
On the 6870-B: 
sw2 (6870-B) -> ip dhcp relay destination 192.168.100.102 
sw2 (6870-B) -> ip dhcp relay admin-state enable 
sw2 (6870-B) -> show ip dhcp relay 
IP DHCP Relay : 
  DHCP Relay Admin Status        = Enable, 
  Forward Delay(seconds)         = 0, 
  Max number of hops             = 16, 
  Relay Agent Information        = Disabled, 
  Relay Agent Information Policy = Drop, 
  DHCP Relay Opt82 Format  =  Base MAC, 
  DHCP Relay Opt82 String  =  e8:e7:32:d4:88:95, 
  PXE support                    = Disabled, 
  Relay Mode                     = Global, 
  Bootup Option                  = Disable, 
 
- On the 6900, check that OSPF still runs properly and that all client vlans are reachable: 
sw1 (6900-A) -> show ip routes 
 
+ = Equal cost multipath routes 
 Total 25 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  0.0.0.0/0            192.168.100.108      3d 4h   STATIC 
  10.0.0.51/32         192.168.100.108      3d 4h   STATIC 
  127.0.0.1/32         127.0.0.1            4d 4h   LOCAL 
  172.16.12.0/24       172.16.12.1          3d 6h   LOCAL 
  172.16.17.0/24       172.16.17.1          3d 1h   LOCAL 
  172.16.28.0/24       172.16.12.2          3d 6h   OSPF 
  172.16.78.0/24       172.16.17.7          3d 1h   OSPF 
  172.16.137.0/24      172.16.17.7          3d 1h   OSPF 
  192.168.20.0/24      172.16.17.7          3d 1h   OSPF 
  192.168.30.0/24      172.16.17.7          3d 1h   OSPF 
  192.168.57.0/24      172.16.17.7          3d 1h   OSPF 
  192.168.60.0/24      172.16.17.7          3d 1h   OSPF 
  192.168.70.0/24      172.16.17.7          3d 1h   OSPF 
  192.168.80.0/24     +172.16.12.2          3d 4h   OSPF 
                      +172.16.17.7          3d 1h   OSPF 
  192.168.100.0/24     192.168.100.1        3d 4h   LOCAL 
  192.168.110.0/24     192.168.110.1     00:00:11   LOCAL 
  192.168.120.0/24     172.16.12.2          3d 5h   OSPF 
  192.168.254.1/32     192.168.254.1        3d 6h   LOCAL 
  192.168.254.2/32     172.16.12.2          3d 6h   OSPF 
  192.168.254.3/32     172.16.17.7          3d 1h   OSPF 
  192.168.254.5/32     172.16.17.7          3d 0h   OSPF 
  192.168.254.7/32     172.16.17.7          3d 1h   OSPF 
  192.168.254.8/32    +172.16.12.2          3d 6h   OSPF 
                      +172.16.17.7          3d 1h   OSPF

<<<PAGE 447>>>
4 
PIM-SM 
 
 2 
PIM-SM Configuration 
Enable PIM-SM in the core routers: 
sw1 (6900-A) -> ip load pim 
sw1 (6900-A) -> ip pim sparse admin-state enable 
 
sw2 (6870-B) -> ip load pim 
sw2 (6870-B) -> ip pim sparse admin-state enable 
 
sw7 (6870-A) -> ip load pim 
sw7 (6870-A) -> ip pim sparse admin-state enable 
 
sw8 (6860-B) -> ip load pim 
sw8 (6860-B) -> ip pim sparse admin-state enable 
 
Now, we must enable PIM-SM on the necessary interfaces.  
sw1 (6900-A) -> ip pim interface int_217 
sw1 (6900-A) -> ip pim interface int_212 
sw1 (6900-A) -> ip pim interface int_110 
sw1 (6900-A) -> ip pim cbsr 192.168.110.1 
 
sw2 (6870-B) -> ip pim interface int_228 
sw2 (6870-B) -> ip pim interface int_212 
sw2 (6870-B) -> ip pim interface int_120 
sw2 (6870-B) -> ip pim cbsr 192.168.120.2 
 
sw7 (6870-A) -> ip pim interface int_217 
sw7 (6870-A) -> ip pim interface int_278 
sw7 (6870-A) -> ip pim interface int_70 
sw7 (6870-A) -> ip pim interface int_20 
sw7 (6870-A) -> ip pim interface int_30 
sw7 (6870-A) -> ip pim cbsr 192.168.70.7 
 
sw8 (6860-B) -> ip pim interface int_228 
sw8 (6860-B) -> ip pim interface int_278 
sw8 (6860-B) -> ip pim interface int_80 
sw8 (6860-B) -> ip pim interface int_20 
sw8 (6860-B) -> ip pim interface int_30 
sw8 (6860-B) -> ip pim cbsr 192.168.80.8 
 
- Now, we must define a CRP for a multicast group. 
6900-A-> ip pim candidate-rp 192.168.110.1 231.1.1.0/24 
 
6870-B-> ip pim candidate-rp 192.168.120.2 231.1.1.0/24 
 
sw7 (6870-A) -> ip pim candidate-rp 192.168.70.7 231.5.5.0/24 
sw7 (6870-A) -> ip pim candidate-rp 192.168.70.7 231.7.7.0/24 
 
sw8 (6860-B) -> ip pim candidate-rp 192.168.80.8 231.10.10.0/24 
sw8 (6860-B) -> ip pim candidate-rp 192.168.80.8 231.8.8.0/24 
 
Check connectivity status on all 3 switches: 
sw1 (6900-A) -> show ip pim interface 
 
Total 3 Interfaces 
 
Interface Name                   IP Address      Designated      Hello    J/P      Oper     BFD 
                                                 Router          Interval Interval Status   Status 
--------------------------------+---------------+---------------+--------+--------+--------+-------- 
int_217                          172.16.17.1     172.16.17.7     30       60       enabled  disabled 
int_212                          172.16.12.1     172.16.12.2     30       60       enabled  disabled 
int_110                          192.168.110.1   192.168.110.1   30       60       enabled  disabled

<<<PAGE 448>>>
5 
PIM-SM 
 
sw2 (6870-B) -> show ip pim interface 
 
Total 3 Interfaces 
 
Interface Name                   IP Address      Designated      Hello    J/P      Oper     BFD 
                                                 Router          Interval Interval Status   Status 
--------------------------------+---------------+---------------+--------+--------+--------+-------- 
int_120                          192.168.120.2   192.168.120.2   30       60       enabled  disabled 
int_228                          172.16.28.2     172.16.28.8     30       60       enabled  disabled 
int_212                          172.16.12.2     172.16.12.2     30       60       enabled  disabled 
 
sw7 (6870-A) -> show ip pim interface 
 
Total 5 Interfaces 
 
Interface Name                   IP Address      Designated      Hello    J/P      Oper     BFD 
                                                 Router          Interval Interval Status   Status 
--------------------------------+---------------+---------------+--------+--------+--------+-------- 
int_278                          172.16.78.7     172.16.78.8     30       60       enabled  disabled 
int_217                          172.16.17.7     172.16.17.7     30       60       enabled  disabled 
int_20                           192.168.20.7    192.168.20.7    30       60       enabled  disabled 
int_30                           192.168.30.7    192.168.30.8    30       60       enabled  disabled 
int_70                           192.168.70.7    192.168.70.7    30       60       enabled  disabled 
 
sw8 (6860-B) -> show ip pim interface 
 
Total 5 Interfaces 
 
Interface Name                   IP Address      Designated      Hello    J/P      Oper     BFD 
                                                 Router          Interval Interval Status   Status 
--------------------------------+---------------+---------------+--------+--------+--------+-------- 
int_278                          172.16.78.8     172.16.78.8     30       60       enabled  disabled 
int_30                           192.168.30.8    192.168.30.8    30       60       enabled  disabled 
int_20                           192.168.20.8    192.168.20.8    30       60       enabled  disabled 
int_80                           192.168.80.8    192.168.80.8    30       60       enabled  disabled 
int_228                          172.16.28.8     172.16.28.8     30       60       enabled  disabled 
 
Check the Pim neighbor and group-map 
sw1 (6900-A) -> show ip pim neighbor 
 
Total 2 Neighbors 
 
Neighbor Address  Interface Name                   Uptime         Expires        DR Priority 
-----------------+--------------------------------+--------------+--------------+----------- 
172.16.17.7       int_217                             00h:07m:01s    00h:01m:43s 1 
172.16.12.2       int_212                             00h:07m:22s    00h:01m:22s 1 
 
sw2 (6870-B) -> show ip pim neighbor 
 
Total 2 Neighbors 
 
Neighbor Address  Interface Name                   Uptime         Expires        DR Priority 
-----------------+--------------------------------+--------------+--------------+----------- 
172.16.28.8       int_228                             00h:08m:09s    00h:01m:37s 1 
172.16.12.1       int_212                             00h:08m:02s    00h:01m:44s 1 
 
sw7 (6870-A) -> show ip pim neighbor 
 
Total 4 Neighbors 
 
Neighbor Address  Interface Name                   Uptime         Expires        DR Priority 
-----------------+--------------------------------+--------------+--------------+----------- 
172.16.78.8       int_278                             00h:07m:59s    00h:01m:16s 1 
172.16.17.1       int_217                             00h:08m:38s    00h:01m:39s 1 
192.168.20.8      int_20                              00h:07m:42s    00h:01m:33s 1 
192.168.30.8      int_30                              00h:07m:42s    00h:01m:33s 1

<<<PAGE 449>>>
6 
PIM-SM 
 
sw8 (6860-B) -> show ip pim neighbor 
 
Total 4 Neighbors 
 
Neighbor Address  Interface Name                   Uptime         Expires        DR Priority 
-----------------+--------------------------------+--------------+--------------+----------- 
172.16.78.7       int_278                             00h:08m:29s    00h:01m:37s 1 
192.168.20.7      int_20                              00h:08m:12s    00h:01m:23s 1 
192.168.30.7      int_30                              00h:08m:12s    00h:01m:23s 1 
172.16.28.2       int_228                             00h:09m:41s    00h:01m:34s 1 
 
sw1 (6900-A) -> show ip pim group-map 
 
Origin      Group Address/Prefix  RP Address      Mode  Precedence 
-----------+---------------------+---------------+-----+----------- 
BSR         231.1.1.0/24          192.168.110.1   asm   192 
BSR         231.1.1.0/24          192.168.120.2   asm   192 
BSR         231.5.5.0/24          192.168.70.7    asm   192 
BSR         231.7.7.0/24          192.168.70.7    asm   192 
BSR         231.8.8.0/24          192.168.80.8    asm   192 
BSR         231.10.10.0/24        192.168.80.8    asm   192 
 
Manage the client 1, client 6 and 9 to send and receive multicast traffic as indicated in the tables below.  
Use the application multicast tool from the desktop to do it. 
PC Client  
Send 
Receive 
Client 1 
grps: 231.1.1.1 
grps: 231.10.10.10 
Client 6 
grps: 231.10.10.10 
grps: 231.5.5.5 
Client 9 
grps: 231.5.5.5 
grps: 231.1.1.1 
 
Example:  
PC Client  
Send 
PC Client 
Receive 
Client 6 (Vlan 20) 
grps: 231.10.10.10 
Client 1 (vlan 110) 
grps: 231.10.10.10 
 
 
 
Check the multicast routing table: 
sw1 (6900-A) -> show ip pim sgroute 
 
Legend: Flags: D = Dense, S = Sparse, s = SSM Group, 
               L = Local, R = RPT, T = SPT, F = Register, 
               P = Pruned, O = Originator 
 
Total 1 (S,G) 
Source Address  Group Address   RPF Interface                    Upstream Neighbor UpTime         Flags 
---------------+---------------+--------------------------------+-----------------+--------------+-------- 
192.168.20.70   231.10.10.10    int_217                          172.16.17.7          00h:00m:48s ST

<<<PAGE 450>>>
7 
PIM-SM 
 
 
sw7 (6870-A) -> show ip pim sgroute 
 
Legend: Flags: D = Dense, S = Sparse, s = SSM Group, 
               L = Local, R = RPT, T = SPT, F = Register, 
               P = Pruned, O = Originator 
Total 1 (S,G) 
Source Address  Group Address   RPF Interface                    Upstream Neighbor UpTime         Flags 
---------------+---------------+--------------------------------+-----------------+--------------+-------- 
192.168.20.70   231.10.10.10    int_20                           192.168.20.8         00h:02m:18s ST 
 
sw8 (6860-B) -> show ip pim sgroute  
 
Legend: Flags: D = Dense, S = Sparse, s = SSM Group, 
               L = Local, R = RPT, T = SPT, F = Register, 
               P = Pruned, O = Originator 
Total 1 (S,G) 
Source Address  Group Address   RPF Interface                    Upstream Neighbor UpTime         Flags 
---------------+---------------+--------------------------------+-----------------+--------------+-------- 
192.168.20.70   231.10.10.10    int_20                                                00h:00m:15s STL 
 
Do the same with client 6 and 9 
PC Client  
Send 
Receive 
Client 1 
grps: 231.1.1.1 
grps: 231.10.10.10 
Client 6 
grps: 231.10.10.10 
grps: 231.5.5.5 
Client 9 
grps: 231.5.5.5 
grps: 231.1.1.1

<<<PAGE 451>>>
VIRTUAL ROUTING AND FORWARDING
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 452>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the concept of VRF
• Configure VRF in an OmniSwitch
• Learn the VRF route Leak feature

<<<PAGE 453>>>
VRF - VIRTUAL ROUTING AND FORWARDING
• Multiple routing instances within the same physical switch
• Multiple instances of IP routing protocols, such as static, RIP, IPv4, BGPv4, and OSPFv2 on 
the same physical switch
• Ability to use duplicate IP addresses across VRF instances
• Separate IP routing domains for customer networks
OR
VRF 3
VRF 2
VRF 1

<<<PAGE 454>>>
VRF - VIRTUAL ROUTING AND FORWARDING

<<<PAGE 455>>>
VRF - VIRTUAL ROUTING AND FORWARDING
• VRF Interaction With Other Features
VRF Aware. Switch applications that are configurable independently and separately within one or more VRF instances. All VRF aware 
applications can be enabled or disabled on each VRF instance
Default VRF. Switch applications that are VRF aware but only use the default VRF instance when IP connectivity is needed; these applications 
are not supported across multiple VRF instances.
Non-VRF Aware. Switch applications that have no association with any VRF instance, even the default instance. Note that configuration of this 
type of application is only allowed when the default instance is the active CLI context

<<<PAGE 456>>>
Service Provider
IP Network
Customer A
Site 1
Provider
Edge 1
Customer B
Site 1
Customer C
Site 1
Provider
Edge 2
Provider
Edge 3
Customer A
Site 3
Customer B
Site 2
Customer A
Site 2
Customer B
Site 2
VRF A
VRF A
VRF B
VRF B
VRF C
VRF C
VRF B
VRF - VIRTUAL ROUTING AND FORWARDING
• Provides the ability to configure separate 
routing instances on the same switch.
• Segments layer 3 traffic.
• Each Provider Edge (PE) maintains more 
than one routing table, in addition to the 
default routing instance.
• One VRF instance is configured on the PE for 
each customer network to which the PE is 
connected.
• When an IP packet for customer A is 
received on a PE; the VRF A determines how 
to route the packet trough the provider 
backbone so that it reaches the intended 
customer A destination

<<<PAGE 457>>>
VRF - VIRTUAL ROUTING AND FORWARDING
Customer
Edge
Provider
Edge
Enterprise class MPLS
DHCP Server 1
VRRP
DHCP Server 2
VRRP
DHCP Server 3
VRRP
OR
VRF
VRF
VRF 1
VRF 2
VRF 3
Per VRF QoS

<<<PAGE 458>>>
VRF - CLI COMMANDS
• Creating a VRF Instance
• Selecting a VRF Instance
• View a list of the Configured VRF’s
• Assigning IP Interfaces to a VRF Instance
• Removing a VRF Instance
*removes associated ip interfaces as well
• Returning to the default VRF instance
Note: VRF names are case sensitive 
Virtual Routers 
Protocols
---------------------------------------
default
IpOne
RIP
IpTwo
BGP
Total Number of Virtual Routers: 3
▪A default VRF instance is automatically configured and available on system startup
▪VRF names to be 32 characters long and contain letters, minus signs and numbers
-> vrf create vrpIpOne
IpOne: ->
IpOne: -> vrf IpTwo
IpTwo: ->
-> show vrf
-> vrf IpOne
IpOne: -> ip interface intf100 address 100.1.1.1/24 vlan 100
IpOne: ->
-> no vrf IpTwo
IpOne: -> vrf default
->

<<<PAGE 459>>>
VRF - CLI COMMANDS
• View a list of the Configured VRF interfaces
-> vrf create IpOne
IpOne: -> show ip interface
Total 1 interfaces
Name 
IP Address 
Subnet Mask     Status    Forward    Device
-------------+---------------+---------------+----------+----------+----------
intfone
200.1.1.1 
255.255.255.0   DOWN        NO        vlan 200
IpOne: -> vrf default
-> show ip interface
Total 6 interfaces
Name 
IP Address 
Subnet Mask      Status   Forward  Device
------------+----------------+------------------+---------+-------+----------
EMP 
192.168.10.1 
255.255.255.0 
DOWN 
NO      EMP
Loopback 
127.0.0.1 
255.0.0.0 
UP 
NO      Loopback
vlan 130 
192.168.130.161
255.255.255.0 
DOWN 
NO      vlan 130
vlan 2 
10.255.11.161 
255.255.255.0 
UP 
YES     vlan 2
vlan-2000 
172.20.0.1 
255.255.0.0 
UP 
YES     vlan 2000
vlan-2100 
172.21.0.1 
255.255.0.0 
UP 
YES     vlan 2100
Number of Virtual Routers: 3

<<<PAGE 460>>>
VRF - GUIDELINES
• A single IP interface, as well as the VLAN associated with the interface, can only belong to 
one VRF instance at a time
• Once a VLAN is associated with a specific VRF instance, configuring an interface for that 
VLAN within the context of any other instance, is not allowed
• For example, if the first IP interface configured for VLAN 100 was associated with the VRF IpOne
instance, then any subsequent IP interface configuration for VLAN 100 is only allowed within the 
context of the IpOne instance
• Use of Duplicate VLAN numbers is not supported
• A VRF instance can have multiple VLAN associations
• even though a VLAN can only have one VRF association
• VRF CLI context is used to determine the association between a specific routing 
configuration and a VRF instance

<<<PAGE 461>>>
VRF ROUTE LEAK
• VRF Route Leak forwards routes from one VRF routing table to another VRF routing table, 
allowing routing from one VRF to a gateway in another VRF.
• Route maps are used to import and export routes from the VRFs to the GRT (Global Routing 
Table).  
6860E/N, 6900, 9900
VRF
VRF 1
VRF 2
VRF 3
200.1.1.0
192.168.130.0
10.255.11.0
172.20.0.0 
172.21.0.0
192.168.1.0
192.168.140.0
10.255.12.0
192.168.1.0
200.1.1.0
192.168.130.160
10.255.11.160
172.20.0.0 
172.21.0.0
192.168.140.0
10.255.12.0
192.168.1.0
GRT

<<<PAGE 462>>>
CONFIGURING VRF ROUTE LEAK
• Create a route-map to use as a filter for exporting or importing routes
• Define protocol preference for export policy route map. This route map controls the export of 
routes from the VRF FDB (Forwarding Routing Database) to the GRT (Global Routing Table) 
• Export routes from the source VRF to the GRT 
• Define protocol preference for import policy route map. This route map controls the import of 
routes from the GRT. 
• Import the leaked routes from the GRT
• Configure route preference for imported routes
-> ip route-map R1 action permit
-> ip route-map R1 match protocol static
-> ip export route-map R1
-> ip route-map R2 match protocol static
-> ip import vrf V1 route-map R2
-> ip route-pref import 100

<<<PAGE 463>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 464>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Multiple VRF 
How to 
✓ Configure the Multiple VRF feature in Release 8 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configuring the Multiple VRF ................................................................ 2 
2.1. Configure two VRF on 6900: ...................................................................... 2 
2.2. VRF route leaking between two different networks ........................................... 5 
2.3. VRF route-leak to leak the routes between 'default' VRF and a another VRF .............. 7

<<<PAGE 465>>>
2 
Multiple VRF 
 
 1 
Topology 
 
Multiple Virtual Routing and Forwarding (VRF) provides a mechanism for segmenting Layer 3 traffic into 
virtual routing domains (instances) on the same switch. Each routing instance independently maintains its 
own routing and forwarding table, peer, and interface information. 
 
 
 
 
 
 2 
Configuring the Multiple VRF 
2.1. 
Configure two VRF on 6900: 
 
- Create two vlan and untagged them on port 1/1/1 and 1/1/12 
 
sw1 (6900-A) -> vlan 190 
 
sw1 (6900-A) -> vlan 200 
 
sw1 (6900-A) -> interfaces 1/1/1 admin-state enable 
 
sw1 (6900-A) -> vlan 190 members port 1/1/1 untagged 
 
sw1 (6900-A) -> interfaces 1/1/12 admin-state enable 
 
sw1 (6900-A) -> vlan 200 members port 1/1/12 untagged 
 
sw1 (6900-A) -> show vlan 190 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged      forwarding 
 
sw1 (6900-A) -> show vlan 200 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/12      untagged      forwarding

<<<PAGE 466>>>
3 
Multiple VRF 
 
- Check the ip route on default vfr 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 24 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  0.0.0.0/0            192.168.100.108      3d 3h   STATIC 
  10.0.0.51/32         192.168.100.108      3d 3h   STATIC 
  127.0.0.1/32         127.0.0.1            4d 3h   LOCAL 
  172.16.12.0/24       172.16.12.1          3d 4h   LOCAL 
  172.16.17.0/24       172.16.17.1          3d 0h   LOCAL 
  172.16.28.0/24       172.16.12.2          3d 4h   OSPF 
  172.16.78.0/24       172.16.17.7          3d 0h   OSPF 
  172.16.137.0/24      172.16.17.7          3d 0h   OSPF 
  192.168.20.0/24      172.16.17.7          3d 0h   OSPF 
  192.168.30.0/24      172.16.17.7          3d 0h   OSPF 
  192.168.57.0/24      172.16.17.7          3d 0h   OSPF 
  192.168.60.0/24      172.16.17.7          3d 0h   OSPF 
  192.168.70.0/24      172.16.17.7          3d 0h   OSPF 
  192.168.80.0/24     +172.16.12.2          3d 3h   OSPF 
                      +172.16.17.7          3d 0h   OSPF 
  192.168.100.0/24     192.168.100.1        3d 3h   LOCAL 
  192.168.120.0/24     172.16.12.2          3d 3h   OSPF 
  192.168.254.1/32     192.168.254.1        3d 5h   LOCAL 
  192.168.254.2/32     172.16.12.2          3d 4h   OSPF 
  192.168.254.3/32     172.16.17.7          3d 0h   OSPF 
  192.168.254.5/32     172.16.17.7          2d23h   OSPF 
  192.168.254.7/32     172.16.17.7          3d 0h   OSPF 
  192.168.254.8/32    +172.16.12.2          3d 4h   OSPF 
                      +172.16.17.7          3d 0h   OSPF 
 
sw1 (6900-A) -> sh ip global-route-table 
Type  Source               Destination        Gateway         Metric     Tag 
------+--------------------+------------------+---------------+----------+---------- 
sw1 (6900-A) -> 
 
- Create a “ipone” VRF and manage an ip interface on it 
 
sw1 (6900-A) -> vrf create ipone 
Wed Feb 23 14:48:06 : ChassisSupervisor MipMgr INFO message: 
+++ VRF:ipone created 
   
ipone::sw1 (6900-A) -> ip interface int_190 address 192.168.190.1/24 vlan 190 
   
ipone::sw1 (6900-A) -> show ip interface 
Total 1 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
int_190                          192.168.190.1   255.255.255.0       UP     YES vlan 190 
 
ipone::sw1 (6900-A) -> show ip routes 
 + = Equal cost multipath routes 
 Total 2 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:00:30   LOCAL 
  192.168.190.0/24     192.168.190.1     00:00:16   LOCAL 
   
ipone::sw1 (6900-A) -> exit

<<<PAGE 467>>>
4 
Multiple VRF 
 
-  Check the ip route list on default VRF 
sw1 (6900-A) -> show ip routes |grep 190 
sw1 (6900-A) -> 
 
- 
Create a second VRF as “iptwo” 
sw1 (6900-A) -> vrf create iptwo 
 
Wed Feb 23 14:49:11 : ChassisSupervisor MipMgr INFO message: 
+++ VRF:iptwo created 
 
 iptwo::sw1 (6900-A) -> ip interface int_200 address 192.168.200.1/24 vlan 200 
  
 iptwo::sw1 (6900-A) -> show ip interface 
Total 1 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
int_200                          192.168.200.1   255.255.255.0       UP     YES vlan 200 
 
iptwo::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 2 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:03:59   LOCAL 
  192.168.200.0/24     192.168.200.1     00:00:36   LOCAL 
   
iptwo::sw1 (6900-A) -> exit 
 
- Check the ip route list on default VRF 
sw1 (6900-A) -> show ip routes |grep 200 
sw1 (6900-A) -> 
 
- Manage Client 1 and Client 4 Ip addresses as below: 
o 
Client 1: 
 
Assign IP address : 192.168.190.50/24 
Subnet :255.255.255.0 
Gateway : 192.168.190.1      
o 
Client 4: 
 
Assign IP address : 192.168.200.50/24 
Subnet :255.255.255.0 
Gateway : 192.168.200.1      
 
- Ping each other to test connection between them. What happens and why? 
------------------------------------------------------------------------------------------------------------------------------ 
------------------------------------------------------------------------------------------------------------------------------

<<<PAGE 468>>>
5 
Multiple VRF 
 
- Check the ip route list on VRF 
 
sw1 (6900-A) -> vrf ipone 
ipone::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 2 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:03:37   LOCAL 
  192.168.190.0/24     192.168.190.1     00:03:23   LOCAL 
 
ipone::sw1 (6900-A) -> exit 
 
sw1 (6900-A) -> vrf iptwo 
 
iptwo::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 2 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:01:57   LOCAL 
  192.168.200.0/24     192.168.200.1     00:01:49   LOCAL 
 
iptwo::sw1 (6900-A) -> exit 
 
2.2. 
VRF route leaking between two different networks  
 
Manage VRF route leaking between two different networks which are present in different VRF's 
We will not be able to ping an IP interface of another VRF instance from one VRF instance within the same switch even 
the leaked routes are existed. This is due to security reason 
However, clients in two different VRF's can ping each other using the route-map filtering option 
 
- Manage Route filtering in VRF1 
 
In this ipone, using rout-map ("vlan190") local route (192.168.190.0/24) is exported to GRT. Only those FDB 
(Forwarding Routing Database) routes that match the conditions of the route map are exported to GRT. 
 And allowing leaked route 192.168.200.0/24  to ingress in the VRF1 using the route-map " vlan200". 
 
sw1 (6900-A) -> vrf ipone 
 
ipone::sw1 (6900-A) -> ip route-map "vlan190" sequence-number 50 action permit 
 
ipone::sw1 (6900-A) -> ip route-map "vlan190" sequence-number 50 match ip-address 192.168.190.0/24 redist-
control all-subnets permit 
 
ipone::sw1 (6900-A) -> ip route-map "vlan200" sequence-number 50 action permit 
 
ipone::sw1 (6900-A) -> ip route-map "vlan200" sequence-number 50 match ip-address 192.168.200.0/24 redist-
control all-subnets permit 
 
ipone::sw1 (6900-A) -> ip export route-map vlan190 
 
ipone::sw1 (6900-A) -> ip import vrf iptwo route-map vlan200

<<<PAGE 469>>>
6 
Multiple VRF 
 
ipone::sw1 (6900-A) -> show ip route-map 
 
Route Maps: configured: 2 max: 30 
Route Map: vlan170 Sequence Number: 50 Action permit 
  match ip-address 192.168.190.0/24 redist-control all-subnets permit 
Route Map: vlan180 Sequence Number: 50 Action permit 
  match ip-address 192.168.200.0/24 redist-control all-subnets permit 
 
ipone::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 2 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:05:30   LOCAL 
  192.168.190.0/24     192.168.190.1     00:05:16   LOCAL 
 
ipone::sw1 (6900-A) -> exit 
 
- Check the route map are exported to GRT 
 
sw1 (6900-A) -> show ip global-route-table 
 
Type  Source               Destination        Gateway         Metric     Tag 
------+--------------------+------------------+---------------+----------+---------- 
vrf    ipone                192.168.190.0/24   192.168.190.1            1          0 
 
 
- Manage Route filtering in VRF2 
 
In this vrf “ iptwo “, using rout-map (vlan200) local route (192.168.200.0/24) is exported to GRT. Only those FDB 
(Forwarding Routing Database) routes that match the conditions of the route map are exported to GRT. 
And allowing leaked route 192.168.190.0/24 to ingress in the VRF” iptwo” using the route-map " vlan190". 
 
sw1 (6900-A) -> vrf iptwo 
 
iptwo::sw1 (6900-A) -> ip route-map "vlan200" sequence-number 50 action permit 
iptwo::sw1 (6900-A) -> ip route-map "vlan200" sequence-number 50 match ip-address 192.168.200.0/24 redist-
control all-subnets permit 
iptwo::sw1 (6900-A) -> ip route-map "vlan190" sequence-number 50 action permit 
iptwo::sw1 (6900-A) -> ip route-map "vlan190" sequence-number 50 match ip-address 192.168.190.0/24 redist-
control all-subnets permit 
iptwo::sw1 (6900-A) -> ip export route-map vlan200 
iptwo::sw1 (6900-A) -> ip import vrf ipone route-map vlan190 
 
iptwo::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 3 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:04:42   LOCAL 
  192.168.190.0/24     192.168.190.1     00:00:04   IMPORT 
  192.168.200.0/24     192.168.200.1     00:04:34   LOCAL 
 
iptwo::sw1 (6900-A) -> exit

<<<PAGE 470>>>
7 
Multiple VRF 
 
sw1 (6900-A) -> show ip global-route-table 
Type  Source               Destination        Gateway         Metric     Tag 
------+--------------------+------------------+---------------+----------+---------- 
vrf    ipone                192.168.190.0/24   192.168.190.1            1          0 
vrf    iptwo                192.168.200.0/24   192.168.200.1            1          0 
 
sw1 (6900-A) -> vrf ipone 
 
ipone::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 3 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:07:42   LOCAL 
  192.168.190.0/24     192.168.190.1     00:07:28   LOCAL 
  192.168.200.0/24     192.168.200.1     00:00:57   IMPORT 
 
ipone::sw1 (6900-A) -> exit 
 
- 
Ping client 1 from client 4 to test connection between them.  
- 
With this above configuration the clients in two different VRF can ping each other. 
2.3. 
VRF route-leak to leak the routes between 'default' VRF and a another VRF  
 
sw1 (6900-A) -> ip route-map "vlan100" sequence-number 50 action permit 
sw1 (6900-A) -> ip route-map "vlan100" sequence-number 50 match ip-address 192.168.100.0/24 redist-control 
all-subnets permit 
 
sw1 (6900-A) -> ip route-map "vlan190" sequence-number 50 action permit 
sw1 (6900-A) -> ip route-map "vlan190" sequence-number 50 match ip-address 192.168.190.0/24 redist-control 
all-subnets permit 
 
sw1 (6900-A) -> ip export route-map vlan100 
sw1 (6900-A) -> ip import vrf ipone route-map vlan190 
 
sw1 (6900-A) -> show ip global-route-table 
Type  Source               Destination        Gateway         Metric     Tag 
------+--------------------+------------------+---------------+----------+---------- 
vrf    default              192.168.100.0/24   192.168.100.1            1          0 
vrf    ipone                192.168.190.0/24   192.168.190.1            1          0 
vrf    iptwo                192.168.200.0/24   192.168.200.1            1          0 
 
sw1 (6900-A) -> vrf ipone 
ipone::sw1 (6900-A) -> ip route-map " vlan100" sequence-number 50 action permit 
ipone::sw1 (6900-A) -> ip route-map " vlan100" sequence-number 50 match ip-address 192.168.100.0/24 
redist-control all-subnets permit 
ipone::sw1 (6900-A) -> ip import vrf default all-routes 
ipone::sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 4 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:10:34   LOCAL 
  192.168.100.0/24     192.168.100.1     00:00:57   IMPORT 
  192.168.190.0/24     192.168.190.1     00:10:26   LOCAL 
  192.168.200.0/24     192.168.200.1     00:05:29   IMPORT 
 
 
- 
Ping from client 1 ping 192.168.100.102 and do the same from client 4. 
- 
With this above configuration only the client1 should be able to ping the 192.168.100.102.

<<<PAGE 471>>>
BORDER GATEWAY PROTOCOL (BGP)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 472>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the basic BGP concepts
• Perform a basic BGP implementation on an AOS 
switch-based network
• BGP Synchronization
• BGP Policy routing

<<<PAGE 473>>>
BGP CONCEPTS AND BASIC SETUP - AOS SPECIFICATIONS

<<<PAGE 474>>>
BGP CONCEPTS

<<<PAGE 475>>>
IGP VS EGP
• Two different classes of routing protocols
• IGP  – Internal Gateway Protocol
• EGP – External Gateway Protocol
• IGP do not scale well
• SPF algorithm runs slow on big routing table
• Not sized for internet routing table
• No policy routing mechanisms
ISP
AS
AS
IGP
EGP

<<<PAGE 476>>>
BGP4
• Border Gateway Protocol
• Current version: 4
• Exterior routing protocol used to make policy 
routing decisions between autonomous systems 
(AS)
• Standardized: RFC 4271
• Listens on port 179 / TCP
• Optional authentication
• MD5: adds an option to TCP
(digest based on pseudo Header + header + data + 
shared password)
• Point-to-point over directly connected 
interfaces or Multi-hop between non-adjacent 
routers
• Routing information is exchanged in BGP Update 
messages
• Used to:
• See the Internet Network (received IP routes)
• Advertise our own network (announce IP routes)
• Influence the inbound traffic flow
• Influence the outbound traffic flow
AS 100
AS 1
AS 999
BGP
BGP
BGP
IGP
IGP
IGP

<<<PAGE 477>>>
AS DEFINITION
• Autonomous Systems
• An autonomous system (AS) is a set of routers 
that are under a single technical administration 
• Normally, use a single interior gateway protocol 
and a common set of metrics to propagate 
routing information within the set of routers
• To other ASs, an AS appears to have a single, 
coherent interior routing plan and presents a 
consistent picture of what destinations are 
reachable through it
• An OmniSwitch with the BGP support for 4-octet 
ASN capability automatically advertises itself as 
being capable of handling 4-octet ASNs and path 
attribute interoperability as per RFC 6793.
• OmniSwitch AOS is backward-compatible with 
other BGP devices that are not capable of 4-
octet ASNs. 
Destination reachable
194.10.10.0 /24
194.12.10.0 /23
194.13.10.0 /24
Etc….
OSPF
OSPF
OSPF
OSPF
OSPF

<<<PAGE 478>>>
BGP PEERING AND BGP NEIGHBORS
• Internal BGP Neighbor
• A router that falls under the administrative control 
of a single AS and is assumed to follow a consistent 
policy with other BGP speakers of that AS
• Internal BGP neighbors are reachable by static 
routes, internal routing protocol, or directly 
connected
• Peering
• Two routers with a BGP connection are neighbors or 
peers
• Peers can be external (EBGP) or internal (IBGP)
• No need of direct connection between IBGP peers
• EBGP peers are usually directly connected
• External BGP Neighbor
• A router whose administrative and policy control is 
outside of your AS
• Send and receive BGP information to or from 
other AS
RIP
OSPF
BGP
BGP
BGP
IBGP peering
EBGP peering

<<<PAGE 479>>>
BGP PEER/NEIGHBOR
• No dynamic discovery
• (Selective) Route exchange
• Keepalive mechanism
• 4 four message types
• Open
•
Keepalive
•
Update
•
Notification
• Connection State 
• Idle – waiting for incoming connection TCP port 179
• Connect – setting up a TCP session
• Active – unable to create a TCP session
• OpenSent  - sending out  its OPEN message
• OpenConfirm – waiting for the KEEPALIVE message
• Established – BGP session is up
AS 54
AS 4

<<<PAGE 480>>>
BGP ROUTE INFORMATION
• Path Vector Protocol
• BGP advertisement is made of:
•
Prefix
• Attribute
AS 54
AS 4
AS 25
192.168.1.0
R2
R1
R3

<<<PAGE 481>>>
BGP UPDATE
• Between BGP neighbors
• To advertise new route/prefix
• To withdraw previously advertised route/prefix
AS 54
AS 25
192.168.1.0
R1
R3
BGP UPDATE

<<<PAGE 482>>>
BGP ATTRIBUTE (1)
• Part of the update message
• Variable length
• Can be:
• Well-known mandatory
• Well-known discretionary
• Optional transitive
• Optional nontransitive
AS 54
AS 25
192.168.1.0
R1
R3

<<<PAGE 483>>>
BGP ATTRIBUTES OVERVIEW

<<<PAGE 484>>>
AS-PATH ATTRIBUTE
• Well-known mandatory attribute
• List of traversed ASes
AS 54
AS 401
AS 25
192.168.1.0
R1
R2
R3
AS 23
R4
AS 4
R5
192.168.1.0
AS ( 23,401,54,25)

<<<PAGE 485>>>
NEXT-HOP ATTRIBUTE (1)
• Well-known mandatory attribute
• IP address of the next node towards destination
AS 25
192.168.1.0
R1
R2
192.168.1.0
AS (25)
10.1.1.3
10.1.1.3
10.1.1.2
R3

<<<PAGE 486>>>
NEXT-HOP ATTRIBUTE (2)
• IBGP conserves the next hop attribute learned over EBGP   
• When BGP Synchronization if off, “next-hop-self” can act as a workaround to validate the BGP path
192.168.1.0
AS (25)
31.0.0.3/8
10.1.1.3/24
10.1.1.2/24
R3
31.0.0.3/8
31.0.0.1/8
R1
R2
AS 25
192.168.1.0

<<<PAGE 487>>>
ORIGIN ATTRIBUTE
• Well-known mandatory attribute
• Defines the origin of the path information :
•
IGP - the prefix was learned from an IGP
•
EGP - the prefix was learned via EGP
•
Incomplete - the prefix was learned through redistribution or static routing or unknown

<<<PAGE 488>>>
LOCAL PREFERENCE ATTRIBUTE
• Well-known discretionary attribute
• Specify a most preferred path to exit an AS
AS 54
AS 250
172.18.0.0
172.18.0.0 /8
Local pref = 200
172.18.0.0 /8
Local pref = 100
AS 3400
R1
R2
AS 100

<<<PAGE 489>>>
BGP LOCAL PREFERENCE METRIC
198.101.24.0
AS 600
200.100.50.1
198.100.28.1
AS 400
AS 500
AS 200
AS 300
Local
Preference = 300
Local
Preference = 200
Chicago
New York
Atlanta

<<<PAGE 490>>>
ATOMIC AGGREGATE ATTRIBUTE
• Well-known discretionary attribute
• CIDR support (Only BGP 4)
• Informs that routes are aggregated
AS 54
150.215.30.8 /30
150.215.30.4 /30
150.215.30.12 /30
AS 650
AS 20
AS 10
150.215.30.0 /28

<<<PAGE 491>>>
MULTI EXIT DISCRIMINATOR (MED)ATTRIBUTE
• Optional non-transitive attribute
• Specify a most preferred path to an AS
AS 54
AS 250
172.18.0.0/16
MED = 200
172.18.0.0/16
MED = 100
R1
R2
R3
R4
172.18.0.0/16

<<<PAGE 492>>>
BGP MULTI-EXIT DISCRIMINATOR
• Inbound Metric
• Meaning: “How I prefer receiving the traffic from you”
• When two autonomous systems have multiple links with each other,
the MED (Multi-Exit Discriminator) informs the other AS of recommended entrance points
• Lower MED value is preferred 
• Default setting for MED = 0
• Metric is non-transitive
• Only shared between two autonomous systems
• Passed from one AS to a second AS
• When the second AS advertises the networks from the first AS, MED value is set back to 0 before 
leaving second AS

<<<PAGE 493>>>
BGP MULTI-EXIT DISCRIMINATOR
AS 100
200.100.50.1
AS 200
198.101.24.0
MED for
198.101.24.0 = 300
MED for
198.101.24.0 = 100
198.100.28.1
I’ll go through 200.100.50.1 to get to 
network 198.101.24.0 because it has a 
lower MED, but I’ll remember the other 
route in case the pathway though 
200.100.50.1 becomes unavailable

<<<PAGE 494>>>
BGP COMMUNITIES
• Provides a way of grouping destinations (called communities) to which routing decisions (such as 
acceptance, preference, and redistribution) can be applied
• Can be passed through and to other AS
• Allows tagging various networks and grouping them into communities
• A few predefined communities are listed:
• No-export (networks are not announced to outside AS)
• No-Export-subconed (sub-confederations)
• No advertise (networks are not announced to any BGP speakers)

<<<PAGE 495>>>
BGP COMMUNITY EXAMPLE
Internet
200.100.50.1
AS 100
AS 300
198.101.24.0
198.101.25.0
198.101.26.0
198.101.27.0
198.101.28.0
198.101.29.0
198.101.30.0
198.101.31.0
AS 200
ISP A
Router A
Router B
198.101.24.0 /21 
198.101.24.0 /21

<<<PAGE 496>>>
COMMUNITY ATTRIBUTE
• Optional transitive attribute
• Permits to tag routes with an indicator
• Filtering can be implemented based on tags
Community
Action
NO-EXPORT
NO-ADVERTISE
<AS:Community#>
No adv. to EBGP peers
No adv. to Any peers
User defined policy

<<<PAGE 497>>>
BGP ROUTE SELECTION
• Recursive lookup validates the route
• Route selection process 
• Highest Local preference
•
Shortest AS-Path
•
lowest origin (IGP>EGP>Incomplete)
•
Lowest MED
•
Closer Next-Hop
•
EBGP > IBGP > IGP
•
Lowest RID

<<<PAGE 498>>>
BGP AOS CONFIGURATION

<<<PAGE 499>>>
-> show ip bgp neighbors
Nbr address     As  Admin state  Oper state
BgpId
--------------+----+-----------+------------+-------------
192.40.4.29     3    enabled      estab
192.40.4.29
192.40.4.121    5    disabled     idle 
0.0.0.0
CLI - IBGP/EBGP BASIC SETUP
• Define Router ID
• Load and activate BGP
• Define AS
• Create a BGP peer entry
• Create Peer relationship with authentication
-> ip router router-id
-> ip load BGP
-> ip bgp admin-state enable
-> ip bgp autonomous-system 100
-> ip bgp neighbor 100.10.1.1
-> ip bgp neighbor 100.10.1.1 > remote-as
-> ip bgp neighbor < 100.10.1.1 > md5 key
-> ip bgp neighbor < 100.10.1.1 > status enable

<<<PAGE 500>>>
BGP PEER SESSION WITH LOOPBACK0
• BGP peering is based on the Loopback0 IP interface address of the peering router
• binding the source (i.e., outgoing IP interface for the TCP connection) to its own configured Loopback0 
interface
• Loopback0 IP interface address can be used for both Internal and External BGP peer sessions
• ebgp-multihop parameter
• For EBGP sessions, if the External peer router is multiple hops away 
-> ip bgp neighbor 100.10.1.1 update-source Loopback0
-> ip bgp neighbor 100.10.1.1 ebgp-multihop

<<<PAGE 501>>>
BGP SPLIT HORIZON
AS 4
R1
R2
R4
R5
AS 4
R3
Routes learned via IBGP should never be 
Propagated to other IBGP peers

<<<PAGE 502>>>
BGP SYNCHRONIZATION
AS 4
AS 54
IBGP
peers
EBGP peers
172.31.0.0
EBGP peers
10.3.0.0
R1
R2
R3
R4
R5
23.0.0.0/8
-> ip bgp synchronization
A BGP router should not advertise, a route learned by IBGP,
to an EBGP peer unless the route is local or is learned from an IGP

<<<PAGE 503>>>
ROUTING TABLE
• AOS Protocol preference for choosing which routes go into the routing table
• Local =1
• Static =2
• OSPF = 10
• RIP = 100
• BGP = 200
Routing table
BGP Path table
Local/Static Routes
OSPF  Routes
-> show ip route-pref
Protocol          Route
Preference Value
------------+------------------
Local               1
Static              2
OSPF               10
RIP               100
BGP               200
-> ip route-pref BGP 8

<<<PAGE 504>>>
BGP POLICY ROUTING

<<<PAGE 505>>>
BGP POLICY ROUTING
• AS Path, Community and Prefix lists
• Route map
-> ip bgp policy aspath-list “100 300 150” permit/deny
-> ip bgp policy community-list  600:1 permit/deny
-> ip bgp policy prefix-list 172.31.0.0 /16 permit/deny
Route-map example
If BGP update matches aspath-list
If prefix-list = <value>
Set network local_preference = <value>

<<<PAGE 506>>>
BGP POLICY MATCHING FLOWCHART
ip bgp policy aspath-list
ip bgp policy prefix-list
ip bgp policy community-list
Route-map aspath-list
Route-map prefix-list
Route-map community-list
Route-map regexp match
Route-map prefix match
Route-map community match
Policy
Route-map
2
1
3
4
5
6
7
8
9
Match ?
Action?
Denied-> 
Evaluation stopped
Permitted ->
Route-maps evaluation
Yes
Route-maps ?
Match?
NO-> 
Routes dropped +
Evaluation stopped
Yes
NO-> 
Evaluation stopped
Yes

<<<PAGE 507>>>
BGP POLICIES
• looks for routes with an AS path with the next hop AS 100, and originating from AS 200
• permits routes that match the regular expression ^100 200$
• looks for routes in the community 600:1
• permits routes in community 600:1 to be advertised
• looks for routes that only belong to the community 600:1
• Routes with a high priority number are applied first
• denies routes that match the network address 12.0.0.0/8
-> ip bgp policy aspath-list aspathfilter “^100 200$” action permit
-> ip bgp policy community-list commfilter 600:1 < action permit / match-type exact /priority 3
-> ip bgp policy prefix-list prefixfilter 12.0.0.0 255.0.0.0 action deny

<<<PAGE 508>>>
ROUTE-MAP POLICY
• Create a route map policy
• Set the policy action
• mapfilter now denies routes that are filtered
• Add conditions to the route map policy
• Assigning a Policy to a Peer
• To assign the same policy to route advertisements to the peer
• To filter routes learned from a peer by the route map
-> ip bgp policy route-map mapfilter1
-> ip bgp policy route-map mapfilter1 aspath-list aspathfilter
-> ip bgp policy route-map mapfilter1 community-list commfilter
-> ip bgp policy route-map mapfilter1 action deny
-> ip bgp neighbor 172.22.2.0 route-map mapfilter1 in
-> ip bgp neighbor 172.22.2.0 route-map mapfilter1 out

<<<PAGE 509>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 510>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
BGP 
How to 
✓ Configure a BGP connection 
Contents 
1 
Topology ........................................................................................ 2 
2 
Create a User-defined directory ............................................................ 3 
3 
Lab Prerequisites .............................................................................. 3 
3.1. Configure VLANs on all switches ................................................................. 3 
3.2. Configure ospf on all switches .................................................................... 4 
3.3. “WAN” Configuration .............................................................................. 6 
3.4. WAN Connectivity .................................................................................. 6 
3.5. BGP Connectivity ................................................................................... 6 
3.6. Redistributing Routes .............................................................................. 7 
3.7. Gathering Routing Information ................................................................... 8

<<<PAGE 511>>>
2 
BGP 
 
 1 
Topology

<<<PAGE 512>>>
3 
BGP 
 
 2 
Create a User-defined directory 
- Create a User-defined directories “labbgp” and boot the switches from the new user-defined directory 
(labbgp): 
 
- Type the following to create a user defined directory, copy the contents of the labinit directory to it and 
once the switch boots, verify that it booted from the “labbgp” directory: 
 
 
sw1 (6900-A) -> mkdir labbgp 
sw1 (6900-A) -> cp labinit/*.* labbgp 
sw1 (6900-A) -> ls labbgp 
sw1 (6900-A) -> reload from labbgp no rollback-timeout 
                Confirm Activate (Y/N): y 
sw1 (6900-A) -> show running-directory 
 
sw2 (6870-B) -> mkdir labbgp 
sw2 (6870-B) -> cp labinit/*.* labbgp 
sw2 (6870-B) -> ls labbgp 
sw2 (6870-B) -> reload from labbgp no rollback-timeout 
                Confirm Activate (Y/N): y 
sw2 (6870-B) -> show running-directory 
 
sw7 (6870-A) -> mkdir labbgp 
sw7 (6870-A) -> cp labinit/*.* labbgp 
sw7 (6870-A) -> ls labbgp 
sw7 (6870-A) -> reload from labbgp no rollback-timeout 
                Confirm Activate (Y/N): y 
sw7 (6870-A) -> show running-directory 
 
sw8 (6860-B) -> mkdir labbgp 
sw8 (6860-B) -> cp labinit/*.* labbgp 
sw8 (6860-B) -> ls labbgp 
sw8 (6860-B) -> reload from labbgp no rollback-timeout 
                Confirm Activate (Y/N): y 
sw8 (6860-B) -> show running-directory 
 3 
Lab Prerequisites 
3.1. 
Configure VLANs on all switches 
 
- On Switch 6900-A: 
 
sw1 (6900-A) -> vlan 10 
sw1 (6900-A) -> vlan 12 
sw1 (6900-A) -> vlan 13 
sw1 (6900-A) -> vlan 10 members port 1/1/1 untagged 
sw1 (6900-A) -> vlan 12 members port 1/1/25 untagged 
sw1 (6900-A) -> vlan 13 members port 1/1/5 untagged 
sw1 (6900-A) -> interfaces 1/1/1 admin-state enable 
sw1 (6900-A) -> interfaces 1/1/25 admin-state enable 
sw1 (6900-A) -> interfaces 1/1/5 admin-state enable 
sw1 (6900-A) -> ip interface vl10 address 192.168.10.254/24 vlan 10 
sw1 (6900-A) -> ip interface vl12 address 192.168.12.1/24 vlan 12 
sw1 (6900-A) -> ip interface vl13 address 192.168.13.1/24 vlan 13

<<<PAGE 513>>>
4 
BGP 
 
- On Switch 6870-B: 
 
sw2 (6870-B) -> vlan 20 
sw2 (6870-B) -> vlan 12 
sw2 (6870-B) -> vlan 24 
sw2 (6870-B) -> vlan 20 members port 1/1/1 untagged 
sw2 (6870-B) -> vlan 12 members port 1/1/29 untagged 
sw2 (6870-B) -> vlan 24 members port 1/1/5 untagged 
sw2 (6870-B) -> interfaces 1/1/1 admin-state enable 
sw2 (6870-B) -> interfaces 1/1/29 admin-state enable 
sw2 (6870-B) -> interfaces 1/1/5 admin-state enable 
sw2 (6870-B) -> ip interface vl20 address 192.168.20.254/24 vlan 20 
sw2 (6870-B) -> ip interface vl12 address 192.168.12.2/24 vlan 12 
sw2 (6870-B) -> ip interface vl24 address 192.168.24.2/24 vlan 24 
 
- On Switch 6870-A: 
 
sw7 (6870-A) -> vlan 30 
sw7 (6870-A) -> vlan 13 
sw7 (6870-A) -> vlan 34 
sw7 (6870-A) -> vlan 30 members port 1/1/1 untagged  
sw7 (6870-A) -> vlan 13 members port 1/1/5 untagged 
sw7 (6870-A) -> vlan 34 members port 1/1/23 untagged  
sw7 (6870-A) -> interfaces 1/1/1 admin-state enable 
sw7 (6870-A) -> interfaces 1/1/5 admin-state enable 
sw7 (6870-A) -> interfaces 1/1/23 admin-state enable 
sw7 (6870-A) -> ip interface vl30 address 192.168.30.254/24 vlan 30 
sw7 (6870-A) -> ip interface vl13 address 192.168.13.7/24 vlan 13 
sw7 (6870-A) -> ip interface vl34 address 192.168.34.7/24 vlan 34 
 
- On Switch 6860-B: 
 
sw8 (6860-B) -> vlan 40 
sw8 (6860-B) -> vlan 24 
sw8 (6860-B) -> vlan 34 
sw8 (6860-B) -> vlan 40 members port 1/1/1 untagged  
sw8 (6860-B) -> vlan 24 members port 1/1/5 untagged 
sw8 (6860-B) -> vlan 34 members port 1/1/23 untagged  
sw8 (6860-B) -> interfaces 1/1/1 admin-state enable 
sw8 (6860-B) -> interfaces 1/1/5 admin-state enable 
sw8 (6860-B) -> interfaces 1/1/23 admin-state enable 
sw8 (6860-B) -> ip interface vl40 address 192.168.40.254/24 vlan 40 
sw8 (6860-B) -> ip interface vl24 address 192.168.24.8/24 vlan 24 
sw8 (6860-B) -> ip interface vl34 address 192.168.34.8/24 vlan 34 
3.2. 
Configure ospf on all switches 
 
- On Switch 6900-A: 
 
sw1 (6900-A) -> ip load ospf 
sw1 (6900-A) -> ip router router-id 1.1.1.1 
sw1 (6900-A) -> ip ospf area 0.0.0.0 
sw1 (6900-A) -> ip ospf area 1.1.1.1 
sw1 (6900-A) -> ip ospf admin-state enable 
sw1 (6900-A) -> ip ospf interface vl10 
sw1 (6900-A) -> ip ospf interface vl13 
sw1 (6900-A) -> ip ospf interface vl10 area 1.1.1.1 
sw1 (6900-A) -> ip ospf interface vl13 area 0.0.0.0 
sw1 (6900-A) -> ip ospf interface vl10 admin-state enable 
sw1 (6900-A) -> ip ospf interface vl13 admin-state enable

<<<PAGE 514>>>
5 
BGP 
 
- On Switch 6870-A: 
 
sw7 (6870-A) -> ip load ospf 
sw7 (6870-A) -> ip router router-id 3.3.3.3 
sw7 (6870-A) -> ip ospf area 0.0.0.0 
sw7 (6870-A) -> ip ospf area 3.3.3.3 
sw7 (6870-A) -> ip ospf admin-state enable 
sw7 (6870-A) -> ip ospf interface vl30 
sw7 (6870-A) -> ip ospf interface vl13 
sw7 (6870-A) -> ip ospf interface vl30 area 3.3.3.3 
sw7 (6870-A) -> ip ospf interface vl13 area 0.0.0.0 
sw7 (6870-A) -> ip ospf interface vl30 admin-state enable 
sw7 (6870-A) -> ip ospf interface vl13 admin-state enable 
 
- On Switch 6870-B: 
 
sw2 (6870-B) -> ip load ospf 
sw2 (6870-B) -> ip router router-id 2.2.2.2 
sw2 (6870-B) -> ip ospf area 0.0.0.0 
sw2 (6870-B) -> ip ospf area 2.2.2.2 
sw2 (6870-B) -> ip ospf admin-state enable 
sw2 (6870-B) -> ip ospf interface vl20 
sw2 (6870-B) -> ip ospf interface vl24 
sw2 (6870-B) -> ip ospf interface vl20 area 2.2.2.2 
sw2 (6870-B) -> ip ospf interface vl24 area 0.0.0.0 
sw2 (6870-B) -> ip ospf interface vl20 admin-state enable 
sw2 (6870-B) -> ip ospf interface vl24 admin-state enable 
 
- On Switch 6860-B: 
 
sw8 (6860-B) -> ip load ospf 
sw8 (6860-B) -> ip router router-id 4.4.4.4 
sw8 (6860-B) -> ip ospf area 0.0.0.0 
sw8 (6860-B) -> ip ospf area 4.4.4.4 
sw8 (6860-B) -> ip ospf admin-state enable 
sw8 (6860-B) -> ip ospf interface vl40 
sw8 (6860-B) -> ip ospf interface vl24 
sw8 (6860-B) -> ip ospf interface vl40 area 4.4.4.4 
sw8 (6860-B) -> ip ospf interface vl24 area 0.0.0.0 
sw8 (6860-B) -> ip ospf interface vl40 admin-state enable 
sw8 (6860-B) -> ip ospf interface vl24 admin-state enable 
 
 
With the commands above, we have now two independent networks (two AS), each network runs an 
separate IGP protocol (here we use ospf) within its AS.  
 
Next, configure BGP to advertise routes between each of two Autonomous Systems.

<<<PAGE 515>>>
6 
BGP 
 
3.3. 
“WAN” Configuration 
 
We are using the network 192.168.12.0/24 between the switches 1 and 2, and network 
192.168.34.0/24 between the switches 3 and 4. The network should be complete and up now. 
3.4. 
WAN Connectivity   
  Ensure you can ping your neighbor switch from each of the “WAN” connections. 
3.5. 
BGP Connectivity 
Two Autonomous Systems have now been connected using the “WAN” connection. Now BGP can be 
configured to advertise routes between them. 
 
- On Switch 6900-A: 
 
sw1 (6900-A) -> ip load bgp 
sw1 (6900-A) -> ip bgp autonomous-system 100 
sw1 (6900-A) -> ip bgp neighbor 192.168.12.2 
sw1 (6900-A) -> ip bgp neighbor 192.168.12.2 remote-as 200 
sw1 (6900-A) -> ip bgp neighbor 192.168.12.2 admin-state enable 
sw1 (6900-A) -> ip bgp admin-state enable 
sw1 (6900-A) -> show ip bgp 
sw1 (6900-A) -> show ip bgp neighbors 
 
- On Switch 6870-B: 
 
sw2 (6870-B) -> ip load bgp 
sw2 (6870-B) -> ip bgp autonomous-system 200 
sw2 (6870-B) -> ip bgp neighbor 192.168.12.1 
sw2 (6870-B) -> ip bgp neighbor 192.168.12.1 remote-as 100 
sw2 (6870-B) -> ip bgp neighbor 192.168.12.1 admin-state enable 
sw2 (6870-B) -> ip bgp admin-state enable 
sw2 (6870-B) -> show ip bgp 
sw2 (6870-B) -> show ip bgp neighbors 
 
- On Switch 6870-A: 
 
sw7 (6870-A) -> ip load bgp 
sw7 (6870-A) -> ip bgp autonomous-system 100 
sw7 (6870-A) -> ip bgp neighbor 192.168.34.8 
sw7 (6870-A) -> ip bgp neighbor 192.168.34.8 remote-as 200 
sw7 (6870-A) -> ip bgp neighbor 192.168.34.8 admin-state enable 
sw7 (6870-A) -> ip bgp admin-state enable 
sw7 (6870-A) -> show ip bgp 
sw7 (6870-A) -> show ip bgp neighbors 
 
- On Switch 6860-B: 
 
sw8 (6860-B) -> ip load bgp 
sw8 (6860-B) -> ip bgp autonomous-system 200 
sw8 (6860-B) -> ip bgp neighbor 192.168.34.7 
sw8 (6860-B) -> ip bgp neighbor 192.168.34.7 remote-as 100 
sw8 (6860-B) -> ip bgp neighbor 192.168.34.7 admin-state enable 
sw8 (6860-B) -> ip bgp admin-state enable 
sw8 (6860-B) -> show ip bgp 
sw8 (6860-B) -> show ip bgp neighbors

<<<PAGE 516>>>
7 
BGP 
 
The commands above created an AS identifier for each switch. Additionally, the switch’s BGP neighbor 
was configured using its neighbor’s IP address as well as its neighbor’s AS identifier.  
By now ‘show ip bgp neighbors’ should display all your neighbors in an established operational state. You 
will talk iBGP with neighbours in your AS and eBGP with neighbors outside your AS.  
At this point you have only the routes from your AS network, type the following on all switches to check 
the routing table: 
all-> show ip ospf routes 
all-> show ip bgp routes 
all-> show ip routes 
 
+ = Equal cost multipath routes 
 Total 5 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:33:30   LOCAL 
  192.168.10.0/24      192.168.10.254    00:11:17   LOCAL 
  192.168.12.0/24      192.168.12.1      00:10:44   LOCAL 
  192.168.13.0/24      192.168.13.1      00:08:53   LOCAL 
  192.168.30.0/24      192.168.13.3      00:08:08   OSPF 
Please notice that, at this step, there are no routes from the AS100 advertised to the AS200. 
3.6. 
Redistributing Routes 
Now that the network configuration is complete, configure BGP to distribute the routes to the other 
Autonomous Systems. Create the following filter. 
 
Type the following on switches 1, 2, 7 and 8:  
 
ip route-map switch1bgp sequence-number 10 action permit 
ip redist ospf into bgp route-map switch1bgp 
ip redist local into bgp route-map switch1bgp  
 
ip route-map switch2bgp sequence-number 10 action permit 
ip redist ospf into bgp route-map switch2bgp 
ip redist local into bgp route-map switch2bgp  
 
ip route-map switch7bgp sequence-number 10 action permit 
ip redist ospf into bgp route-map switch7bgp 
ip redist local into bgp route-map switch7bgp  
 
ip route-map switch8bgp sequence-number 10 action permit 
ip redist ospf into bgp route-map switch8bgp 
ip redist local into bgp route-map switch8bgp

<<<PAGE 517>>>
8 
BGP 
 
3.7. 
Gathering Routing Information 
You should now begin to see routes from the other Autonomous Systems.  
Do another ping to your neighbor AS switch 4 (or other bgp peers) and check the routing table again, you 
will see that the BGP advertises the routes from AS100. 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 8 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:42:57   LOCAL 
  192.168.10.0/24      192.168.10.254    00:04:48   LOCAL 
  192.168.12.0/24      192.168.12.1      00:04:36   LOCAL 
  192.168.13.0/24      192.168.13.1      00:04:09   LOCAL 
  192.168.20.0/24      192.168.12.2      00:00:16   EBGP 
  192.168.24.0/24      192.168.12.2      00:00:16   EBGP 
  192.168.30.0/24      192.168.13.7      00:02:36   OSPF 
  192.168.40.0/24      192.168.12.2      00:00:16   EBGP 
 
sw2 (6870-B) -> sh ip routes 
 
 + = Equal cost multipath routes 
 Total 8 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:44:32   LOCAL 
  192.168.10.0/24      192.168.12.1      00:01:55   EBGP 
  192.168.12.0/24      192.168.12.2      00:06:02   LOCAL 
  192.168.13.0/24      192.168.12.1      00:01:55   EBGP 
  192.168.20.0/24      192.168.20.254    00:05:59   LOCAL 
  192.168.24.0/24      192.168.24.2      00:05:17   LOCAL 
  192.168.30.0/24      192.168.12.1      00:01:55   EBGP 
  192.168.40.0/24      192.168.24.8      00:03:22   OSPF 
 
 
sw7 (6870-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 8 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:43:51   LOCAL 
  192.168.10.0/24      192.168.13.1      00:03:27   OSPF 
  192.168.13.0/24      192.168.13.7      00:04:54   LOCAL 
  192.168.20.0/24      192.168.34.8      00:01:03   EBGP 
  192.168.24.0/24      192.168.34.8      00:01:03   EBGP 
  192.168.30.0/24      192.168.30.254    00:04:57   LOCAL 
  192.168.34.0/24      192.168.34.7      00:04:33   LOCAL 
  192.168.40.0/24      192.168.34.8      00:01:03   EBGP 
 
 
sw8 (6860-B) -> sh ip routes 
 
 + = Equal cost multipath routes 
 Total 8 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1         00:34:15   LOCAL 
  192.168.10.0/24      192.168.34.7      00:02:06   EBGP 
  192.168.13.0/24      192.168.34.7      00:02:06   EBGP 
  192.168.20.0/24      192.168.24.2      00:03:42   OSPF 
  192.168.24.0/24      192.168.24.8      00:05:37   LOCAL 
  192.168.30.0/24      192.168.34.7      00:02:06   EBGP 
  192.168.34.0/24      192.168.34.8      00:05:37   LOCAL 
  192.168.40.0/24      192.168.40.254    00:05:34   LOCAL

<<<PAGE 518>>>
9 
BGP 
 
- At the end of this lab, restore the four switches to initial configuration by restarting them from "working 
directory". 
 
sw1 (6900-A) -> rm -r labbgp 
 
rm: remove 'labbgp/pkg/.pkgDB_Commit'? y 
rm: remove 'labbgp/pkg/.appDB_Commit'? y 
rm: remove 'labbgp/.boot.pkg.md5'? y 
rm: remove 'labbgp/boot.md5'? y 
sw1 (6900-A) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y 
 
sw2 (6870-B) -> rm -r labbgp 
rm: remove 'labbgp/pkg/.pkgDB_Commit'? y 
rm: remove 'labbgp/pkg/.appDB_Commit'? y 
rm: remove 'labbgp/.boot.pkg.md5'? y 
rm: remove 'labbgp/boot.md5'? y 
sw2 (6870-B) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y 
 
sw7 (6870-A) -> rm -r labbgp 
rm: remove 'labbgp/pkg/.pkgDB_Commit'? y 
rm: remove 'labbgp/pkg/.appDB_Commit'? y 
rm: remove 'labbgp/.boot.pkg.md5'? y 
rm: remove 'labbgp/boot.md5'? y 
sw7 (6870-A) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y 
 
sw8 (6860-B) -> rm -r labbgp 
rm: remove 'labbgp/pkg/.pkgDB_Commit'? y 
rm: remove 'labbgp/pkg/.appDB_Commit'? y 
rm: remove 'labbgp/.boot.pkg.md5'? y 
rm: remove 'labbgp/boot.md5'? y 
sw8 (6860-B) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y

<<<PAGE 519>>>
S H O RT E S T PAT H  B R I D G I N G  ( S P B )
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 520>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the Shortest Path Bridging (SPB) 
protocol
• Identify the control and data planes in SPB
• Understand IP Routing mechanisms over SPB

<<<PAGE 521>>>
STP VS. SPB-M
• Unused links: 
• loop-free topology by disabling network links
• inefficient bandwidth use
• low Return on Investment (ROI)
• Sub-optimal paths:
• A single tree, the traffic always must pass through the ‘Root’ bridge bridges 
• May need to traverse a sub-optimal route transiting the root-bridge 
• Lack of a coordinated control plane
• Flooding: Ethernet’s “flood and learn” address learning floods unknown-unicast traffic until the destination 
address is learned from return traffic 
• MAC Learning: All nodes in the LAN learn all end-device MAC addresses thus posing a scalability challenge
• Slow convergence: 
• Typical convergence times are in the order of seconds.
• Transient loops may form, resulting in packet drops, link saturation, and session timeouts
IEEE 802.1ad (Provider Bridging, or Q-in-Q)
maximum of 4096 service instances.

<<<PAGE 522>>>
SPB-M VS STP
Data path with Spanning Tree
Source
Cannot use these 
links
2
1
Inefficient routes
3
All the nodes on the 
route need to learn 
MAC’s Source1-
Source100
Root Bridge
MACs
Source 1
….
Source100
Destination-1
Destination-2
High @MAC tables
+
Link redundancy
-
Convergence time
-
Centralized Root Bridge
-
Scalability
-
High number of unused links
-

<<<PAGE 523>>>
SHORTEST PATH BRIDGING (SPB-M)
• Network requirements
• Fast reconvergence
• Increase bandwidth utilization
• Reduce latency
• High availability
• Security
• Applications requirements
• Fast network reconvergence
• High bandwidth
• Low latency
SPB-M provides following advantages 
•
All network links are use with no loops
•
Spanning Tree Protocol replacement
•
Uses the shortest path end to end
•
100’s ms convergence times 
•
Natively protect failures and reroute
•
End-point provisioning
•
Mesh topologies
•
Deterministic traffic flows
•
Symmetrical and congruent paths
•
Address isolation through mac-in-mac
•
OAM capabilities
•
Flexible and scalable service separation
•
Traffic separation
IEEE standard (802.1aq)
OS6860N
OS6865
OS6870
OS6900
OS9900

<<<PAGE 524>>>
SPB-M VS STP
Data path with SPB-M
MACs
Source 1
….
Source100
Destination-1
All the links are 
usable
2
1
Multiple shortest 
paths
3
MAC’s Source1-
Source100 learning 
restricted to the edges
Destination-2
PBB 
encapsulation 
at the edges
PBB encapsulation 
at the edges
PBB encapsulation 
at the edges
No High @MAC tables in core
+ Link redundancy
+ Convergence time
+ No Centralized Root Bridge
+
Scalability
+ 
All links usable
+
No need IGP in the core for routing
+

<<<PAGE 525>>>
SHORTEST PATH BRIDGING
Control and Data Planes
Control Plane
IEEE 802.1aq
ISIS–L1
Data Plane
SPB-M
Constructs Shortest Path Trees (SPT)
Distributes « reachability » information 
between SPB-M switches
No learning of Access LAN @MAC and 
paths accross core SPB-M switches
ISIS–L1
Edge network @MACs dynamically learnt 
and propagated accross SPB-M core
Access
Bridge
Access
Bridge
ISIS-SPB control packets
Populates SPB-M bridging/forwarding tables

<<<PAGE 526>>>
SPB - DATA FORWARDING
MAC :00:01
MAC :00:02
SPB Network
I-SID
Ethertype 802.1ah 
B-VID
Ethertype 802.1 ad
00:03
00:04
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
00:01
00:02
MAC :00:03
MAC :00:04
Backbone Bridge Network
Customer Network
Customer Network
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
00:01
00:02
Service 
Identifiers
Tunnel 
Identifiers
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
00:01
00:02
Service 
Identifiers
SA = Source MAC address
DA = Destination MAC address
C-VID = Customer VlanID
I-SID = Service ID
B-VID = Backbone VID
B-DA = Backbone DA
B-SA = Backbone SA

<<<PAGE 527>>>
SPB COMPONENTS
SPB Access Port
Where the customer traffic 
ingresses or egresses
BEB
BEB
BEB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
BEB = Backbone Edge Bridge
BCB = Backbone Core Bridge
C-VID = Customer VlanID
BVLAN=Backbone VLAN
I-SID = Service ID
SAP=Service Access Point
B-VID = Backbone VID
BMAC= Backbone switch MAC address
Backbone Core Bridge
BCB is unaware of services 
Performs forwarding only by 
looking at  BMAC header
Access
Node
Access
Node
Backbone Vlan (BVLAN)
Special VLAN provides the physical path and 
propagation of network control
Expansion of Layer 2 Ethernet domains
No source @mac learning of Customer data traffic 
Each B-VLAN calculates its own Shortest Path Tree
BVLAN
1001
BVLAN
1002
SAP
SAP
Service Access Point (SAP)
Used to specify what type of CVLAN traffic is
allowed to enter/exit from/to the SPB network
Associate a traffic to a SPB service based on Vlan-TAG
SAP
SAP
SAP
C-VID
802.1Q
Customer VLAN (CVLAN)
A traditional VLAN with MAC learning 
& flooding where users connect to
Backbone Edge Bridge
Edge nodes of the SPBM network
Service termination
Service Instance Identifier
Backbone services instance identifier 
Identifies a MAC-in-MAC service instance
Used to identify and transmit any virtualized 
traffic in an encapsulated SPB-M frame
Delivers service abstraction
ISID
1001
ISID
1002
ISID
1001
ISID
1002
ISID
1001
Service
A flooding domain 
for customer traffic

<<<PAGE 528>>>
SPB – SERVICE FRAMEWORK
SAP
SDP ID
I-SID 66
I-SID 77
Service 
I-SID 66
SAP
Service 
I-SID 77
SAP
SAP
DEMUX
I-SID 66
I-SID 77
SDP ID
I-SID 66
I-SID 77
DEMUX
I-SID 66
I-SID 77
Service 
I-SID 66
Service 
I-SID 77
SPB-M
BACKBONE
Service Distribution Point (SDP)
Far-End Node (Unicast SDP) or group of far-end nodes (Multicast SDP)

<<<PAGE 529>>>
MACRO AND MICRO-SEGMENTATION
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓
Authenticate
✓
Classify
✓
Provision
Users
✓
Authenticate
✓
Classify
✓
Provision
HVAC
✓
Authenticate
✓
Classify
✓
Provision
Access Security
✓
Zero-trust framework
✓
Software-defined segmentation
SPB iFab

<<<PAGE 530>>>
SPB – VIRTUAL PRIVATE NETWORK
BEB
BEB
BCB
BCB
CMAC :00:01 / IP.1
CMAC :00:02/ IP.2
CMAC :00:20 / IP.20
CMAC :00:10 / IP.10
DC
Building 2
BEB
BEB
I-SID1 – Video
I-SID2 – Data
Building 1
Building 3

<<<PAGE 531>>>
Communication
Private Network
Separate Departments
AUTOMATED PROVISIONING
INTO SPB VIRTUAL CONTAINERS
Separate Storage 
Separate Computing
Facilities Department
Private Network
Security Department
Private Network
Administration 
Department
Private Network
A Virtual Private Network for 
every department

<<<PAGE 532>>>
SPB – IP ROUTING
Routing L3 traffic over a L2 SPBM backbone network
Access
Bridge
Access
Bridge
“Default Gateway”  Point To Point routing
Multi-point routing ative to IPv4/IPv6 formats
Routing to CVLANs 
IP interfaces 
attached to an end 
of the SPB-M tunnel 
Run routing protocols 
on L3 VPN IP interfaces
Subnet 1
Subnet 2
Subnet 3
Layer 3 routing advertisements sent 
through SPB BVLAN
->
SPB-M network acts as a physical network
No need IGP in the 
Core/Aggregation 
for routing

<<<PAGE 533>>>
IP ROUTING OVER SPB-M CONCEPT
AOS supported two mechanisms: IP-VPN Lite / L3/IP-VPN
VRF
VRF
VRF
I-SID Mapping to IP Interface 
Operates on BEB Bridges 
in a SPB-M backbone
AOS supported mechanisms
L3/IP-VPN routing over SPB-M
IP-VPN Lite over SPB-M
ISID
BVLAN
VRFs on different BEBs are tied together by 
ISIDs across SPB-M backbone

<<<PAGE 534>>>
IP-VPN LITE
• Routing L3 traffic over a L2 SPBM backbone network
• Run routing protocols on L3VPN IP interfaces

<<<PAGE 535>>>
SPB IP ROUTING – IP-VPN LITE
VPN-Lite
“Default Gateway”
Point To Point routing
Multi-point routing
native to IPv4/IPv6 formats
Routing to CVLANs IP 
interfaces attached to an 
end of the SPB-M tunnel 
Run routing protocols 
on L3 VPN IP interfaces
L3 routing advertisements 
sent through SPB BVLAN
No need IGP in the 
Core/Aggregation for routing
IP
IP
DC
IP
IP
Building 1
IP
IP
Building 2
SPB-M network acts as a physical network

<<<PAGE 536>>>
L3/IP-VPN
• Routing L3 traffic over a L2 SPBM backbone network
• VRF L3 routes exchanged via dedicated ISIS/SPB TLV

<<<PAGE 537>>>
SPB IP ROUTING – L3/IP-VPN
L3/IP-VPN
Routes can be selectively imported into ISIS- SPB 
and advertised across the SPB-M domain
ISIS-SPB protocol acts as an IP-IGP protocol
No need to run routing protocols 
on L3 VPN IP interfaces
No need IGP in the 
Core/Aggregation for routing
IP
IP
DC
IP
IP
Building 1
IP
IP
Building 2
L3 routes exchanged via ISIS/SPB TLV

<<<PAGE 538>>>
SPB DEPLOYMENT IN LAN NETWORK
OS9900
OS6900
OS6570M
OS6465
OS6560/E
OS6360
OS9900
OS6900
OS6870
OS6860N
OS6865
DC
BEB
BEB
BEB
BEB
BCB
BCB
Core
Backbone Core Bridge (BCB) role
Learns BEB addresses
IS-IS SPB for paths
PBB for data plane
L3 routing
Aggregation
Backbone edge bridge (BEB) role
VLAN to I-SID
IS-IS for MAC learning
IS-IS for SPB paths
PBB for data plane
Loopback Detection Feature
Access
IEEE 802.1Q VLAN on uplinks (port or LAG)
STP towards BEB
ALE Switch 
proposal
ALE Switch 
proposal
ALE Switch 
proposal

<<<PAGE 539>>>
BUM TRAFFIC FORWARDING METHODS 
• Head-End (default mode)
• Customer BUM traffic is encapsulated in the corresponding destination unicast B-MAC address and 
send to ALL destinations
• Tandem
• Customer BUM traffic is a special B-MAC Destination Address that encodes the source of the traffic 
and send out
OS6900
OS6900
VM
VM
VM
VM
OS6900
OS6900
VM
VM
VM
VM
MC mode can be specified on a per I-SID basis or globally

<<<PAGE 540>>>
IP MULTICAST OPTIMIZATION
• IP multicast snooping at service level
ISID 1000
SAP 1/1/1:1000
SAP 1/1/2:1000
SAP 1/1/3:1000
10005
10006
10007
Dynamic 
Querier
Q
Without Optimization
Tandem
Head-End
ISID 1000
SAP
MCAST
SDP
SAP
SAP
• Prevents flooding SAPs and SDPs
•
IPv4 and IPv6(MLD) 
•
IGMP/MLD snooping and proxy per service
•
Spoofing, zapping, robustness controls
•
Querier forwarding
•
Zero based queries
•
Flood unknown controls

<<<PAGE 541>>>
DHCP SNOOPING OVER SERVICES
• DHCP snooping at service level
• Starting with 8.9R4 DHCP Snooping is supported at service level, including SPB (but also VXLAN or 
L2GRE, VPLS depending on switch model)
• Can be enabled either on global level or service and VLAN level
• Port configuration cannot be changed and is as such :
• SAP ports are “client-only”
• SDP ports are “trust”
• Is supported only on static services

<<<PAGE 542>>>
SPB BENEFITS IN THE CAMPUS
Resiliency / Scalability
• Fast reconvergence (~300ms)
• Path diversity / Increase bandwidth utilization
• Low latency
• High availability
• Scalability (up to 1000 nodes)
• Multi-tenancy
Security
• L2/L3 Virtual Private Networks 
• SPB IOT containment
• Automated access profile provisioning 
with UNP
Manageability
• Management 
• Out of Band (EMP or port)
• In Band Map VLAN to ISID
• Standard VLAN
• Inline
• Spanning Tree Replacement
• SPB iFab Technology
• Automated SPB-M (L2) domains creation
• SPB-M auto-discovery of I-SID, BEB services
• UNP based auto-provisioning at BEB of VLAN-ISID
• Simpler than MPLS
Advantages
https://www.al-enterprise.com/en/solutions/shortest-path-bridging

<<<PAGE 543>>>
SPB – IFYOU WANT TO KNOW MORE

<<<PAGE 544>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 545>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Deploying a network based on SPB-M technology 
Contents 
1 
Objectives ...................................................................................... 2 
2 
Physical diagram .............................................................................. 3 
3 
LAB Prerequisites .............................................................................. 3 
4 
Configure a SPB network for extending L2 connectivity. ................................ 3 
4.1. Creating the Backbone VLANs .................................................................... 4 
4.2. Defining the Control BVLAN ....................................................................... 4 
4.3. Configuring ISIS on network ports ................................................................ 4 
4.4. Activating ISIS protocol ............................................................................ 5 
4.5. Understanding SPB-M protocol operations ...................................................... 5

<<<PAGE 546>>>
2 
Lab: Deploying a network based on SPB-M technology 
 
 1 
Objectives 
 
This lab is designed to familiarize you with SPBM deployment and have a good understanding of SPBM 
configuration with the Alcatel-Lucent OmniSwitch family. 
 
First, you'll configure an example SPB backbone, using the figure below as a topology example. 
We will continue using this sample topology throughout the rest of this eBook. 
 
Nodes BEB-7 and BEB-8 are called “BEB” nodes because we will add services to these nodes later.  
Node BCB-1 and BCB-2 will remain a pure transit node and not terminate any service on first labs. 
 
A scenario for extending Layer 2 connections across a SPB-M service backbone network for Customer VLAN 2 
and VLAN 3 will be done on next lab. 
 
The SPB network is setup as a partial mesh, mainly to demonstrate the different flows that are possible.

<<<PAGE 547>>>
3 
Lab: Deploying a network based on SPB-M technology 
 
 2 
Physical diagram 
 
 
 
 3 
LAB Prerequisites 
Ask your trainer to reinitialize the pod with LAN configuration with his web too. Otherwise, your previous 
configuration will be present, and you won't be able to create the spb configuration. 
 4 
Configure a SPB network for extending L2 connectivity. 
 
If you observe this topology, you will notice that it provides up to 2 shortest paths, for example, 
between nodes BEB-7 and BEB-8, To take advantage of those 2 diverse paths for traffic load balancing, we      
     need to create a minimum of 2 BVLANs. In this example, we will however, dedicate one BVLAN purely for  
     control traffic and therefore we will create a total of 3 BVLANs. However, it should be noted that this is not  
     strictly necessary, the control BVLAN can also be used for services. 
 
Backbone configuration entails the following tasks: 
 
• Creating one or more BVLANs with their associated ECT-IDs. ECT-IDs need not be explicitly defined,  
        default ECT-IDs are applied 
 
• Defining the control BVLAN 
 
• Defining one or more SPB IS-IS interfaces 
 
• Enabling the SPB IS-IS protocol

<<<PAGE 548>>>
4 
Lab: Deploying a network based on SPB-M technology 
 
4.1. 
Creating the Backbone VLANs 
 
- On each node, create three backbone VLANs (BVLAN) 
Switch 1, 2, 7 and 8 
-> spb bvlan 2000 
-> spb isis bvlan 2000 ect-id 1 
-> spb bvlan 2001 
 
-> spb isis bvlan 2001 ect-id 2 
-> spb bvlan 2002 
-> spb isis bvlan 2002 ect-id 3 
 
 
Notes 
BVLAN configuration and ECT algorithm assignment must match on each SPB bridge to ensure proper ISIS-SPB 
neighbour discovery and shortest path calculations throughout the backbone SPB network..  
When creating multiple BVLANs for each node, it is best practice to use different ECT algorithm for each BVLAN 
to maximize the traffic distribution.  
4.2. 
Defining the Control BVLAN 
 
- On each switch, configure the control BVLAN for management.  
Switch 1, 2, 7 and 8 
-> spb isis admin-state disable  
-> spb isis control-bvlan 2000 
 
 
Notes 
Control BVLAN carries the ISIS PDUs which are single tagged with the chosen BVLAN ID. 
Control BVLAN can only be changed when protocol is disabled.  
There is no Spanning Tree on BVLANs 
Through this configuration, VLANs 2000 through 2002 are defined as SPB backbone VLANs and 
will therefore not use any form of spanning tree protocol.  
 
AOS automatically assigns a different ECT-ID to each BVLAN and this maximizes the chance that different 
BVLANs will create different SPTs, up to the maximum number of shortest paths supported by the 
physical topology. 
Nodes will exchange IS-IS “Hello” messages over the control BVLAN (such as, 2000 in this example) and 
form point-to-point adjacencies. LSPs are exchanged, a topology database is created and one SPT 
is built for each BVLAN. 
 
4.3. 
Configuring ISIS on network ports 
 
Setup the ISIS protocol on appropriate network ports on every switch participating in SPB core network, 
accordingly to the physical connection between each node: 
 
 
Notes 
On system startup, ISIS is automatically loaded on the system without the need to enable the 
protocol like we do with OSPF and other protocols. 
Switch 1 
-> spb isis interface port 1/1/5  
-> spb isis interface port 1/1/6 
-> spb isis interface port 1/1/25 
-> interface port 1/1/5-6 admin-state enable 
-> interface port 1/1/25 admin-state enable

<<<PAGE 549>>>
5 
Lab: Deploying a network based on SPB-M technology 
 
Switch 2 
-> spb isis interface port 1/1/5  
-> spb isis interface port 1/1/6 
-> spb isis interface port 1/2/1 
-> interface port 1/1/5-6 admin-state enable 
-> interface port 1/2/1 admin-state enable 
 
Switch 7 
-> spb isis interface port 1/1/5 
-> spb isis interface port 1/1/6 
-> interface port 1/1/5-6 admin-state enable 
Switch 8 
-> spb isis interface port 1/1/5  
-> spb isis interface port 1/1/6 
-> interface port 1/1/5-6 admin-state enable 
 
 
 
 
 
 
Notes 
The ISIS interface can be a fixed port or a logical port (linkagg). When you configure the port as an ISIS SPB 
interface, it becomes the SPB network port, and the system will automatically add all BVLANs configured to the 
port. 
 
 
 
Question 
These interfaces are called « Network port » in SPB context. Before you enable ISIS in the next step, what is 
happening to these 4 nodes now in terms of L2 connectivity and Spanning Tree?  Is there a loop?  Should there 
be a blocking somewhere? 
4.4. 
Activating ISIS protocol  
 
On every SPB nodes, enable globally IS-IS SPB protocol: 
Switch 1, 2, 7 and 8 
-> spb isis admin-state enable 
 
 
Notes 
Enabling ISIS-SPB on a switch starts the process of ISIS-SPB discovery, adjacency building, and shortest path 
tree calculations. Make sure that the SPBM configuration is set up first, then enable ISIS-SPB on each switch 
that will participate in the SPBM network. 
4.5. 
Understanding SPB-M protocol operations 
 
Let’s review this configuration with some show commands. 
 
 
Notes 
Refer to the CLI reference and Network Configuration Guides for detailed information about 
outputs. 
 
- Check the BVLANs and the associated ECT algorithm on each of the system.  
-> show spb isis bvlans 
-> show vlan id 
 
- Display the list of all the SPB interfaces configured for the system and their states.  
-> show spb isis interface

<<<PAGE 550>>>
6 
Lab: Deploying a network based on SPB-M technology 
 
 
 
- Displays the information about the SPB adjacencies on the system. 
Determine if ISIS SPB is in “UP” state then check the ISIS SPB neighbors on each of the equipment. 
-> show spb isis adjacency 
-> show spb isis adjacency detail 
 
- Display the global ISIS-SPB status and configuration information for the SPB bridge. 
-> show spb isis info 
 
- Verify the unicast addresses learned on each SPB switch in the ISIS-SPB backbone topology as well the 
outbound interface used when sending unicast traffic to other nodes. 
-> show spb isis unicast-table bvlan 2000 
-> show spb isis unicast-table bvlan 2001 
-> show spb isis unicast-table bvlan 2002 
 
- Checks the shortest path first (SPF) information to all known SPB bridges for a specific BVLAN (the 
outbound interface, the next hop node as well as the SPB metric and total number of hops 
required to reach a destination node) 
-> show spb isis spf bvlan 2000 
-> show spb isis spf bvlan 2000 bmac <BMAC> 
-> show spb isis spf bvlan 2001 
-> show spb isis spf bvlan 2001 bmac <BMAC> 
-> show spb isis spf bvlan 2002 
-> show spb isis spf bvlan 2002 bmac <BMAC> 
 
- Display information about the ISIS SPB topology database 
-> show spb isis database [lsp-id <lspid>] 
 
- Display the discovered node for all SPBM bridges participating in the topology 
-> show spb isis nodes

<<<PAGE 551>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Deploying a network based on SPB-M technology-L2 services 
Contents 
1 
Objectives ...................................................................................... 2 
2 
Physical diagram .............................................................................. 2 
3 
Logical diagram ................................................................................ 3 
4 
Configure a SPB network for extending L2 connectivity ................................. 4 
4.1. Creating VLANs on access switches .............................................................. 4 
4.2. Creating two SPB services ......................................................................... 5 
4.3. Configuring SPB access ports...................................................................... 5 
4.4. Setting up the SAP services ....................................................................... 6 
5 
Analysis and understanding the concept of SPB services ................................ 7 
5.1. Checking the configuration ....................................................................... 7 
5.2. Testing end device connectivity .................................................................. 7

<<<PAGE 552>>>
2 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 
 1 
Objectives 
In this lab, you will configure a scenario for extending Layer 2 connections across a SPB-M service backbone 
network for Customer VLAN 2 and VLAN 3. 
 
 2 
Physical diagram

<<<PAGE 553>>>
3 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 3 
Logical diagram 
Here is a simple SPB network to provide a good foundation to understand how SPBM works on the 
OmniSwitches. 
The SPB network is setup as a partial mesh, mainly to demonstrate the different flows that are possible.

<<<PAGE 554>>>
4 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 4 
Configure a SPB network for extending L2 connectivity 
A L2 service refers to a type of VPN service connecting multiple sites in a single any-to-any bridging domain. 
In this lab, we continue building upon the previous example and create a L2 service on top of the previously 
created backbone configuration. 
Services need only be created on BEBs, not on BCBs, and only on those BEBs where the service needs to be 
delivered.  
Creating an SPB service entails the following tasks: 
- Creating a service and associating the service to an IS-IS and BVLAN – the specified BVLAN’s SPF will be 
used for the service traffic. 
- Defining a Service Access Port (SAP) 
- Defining SAPs matching specific customer traffic 
 
- So, Configuration steps will be: 
1. Creating VLANs on access switches 
2. Create the Service Access Port 
3. Create the Service Access Profile (Optional) 
4. Create the Service I-SID 
5. Create the Service SAP 
4.1. 
Creating VLANs on access switches 
We will create two VLAN (2 and 3) on access switches OS6360 and on OS6560-A VLAN (2) distributed over SPB 
backbone network. 
These VLANs will be tagged over uplinks towards the backbone. So, proceed as follow: 
Switch 5 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> ip interface vlan2 address 192.168.2.5/24 vlan 2 
-> vlan 3  
-> vlan 3 members port 1/1/2 untagged 
-> ip interface vlan3 address 192.168.3.5/24 vlan 3 
-> vlan 2 members port 1/1/3 tagged  
-> vlan 3 members port 1/1/3 tagged 
-> interfaces 1/1/1-3 admin-state enable 
Switch 6 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> ip interface vlan2 address 192.168.2.6/24 vlan 2 
-> vlan 3  
-> vlan 3 members port 1/1/2 untagged 
-> ip interface vlan3 address 192.168.3.6/24 vlan 3 
-> vlan 2 members port 1/1/3 tagged  
-> vlan 3 members port 1/1/3 tagged 
-> interfaces 1/1/1-3 admin-state enable 
Switch 3 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> vlan 2 members port 1/1/7 tagged 
-> ip interface vlan2 address 192.168.2.3/24 vlan 2 
-> interfaces 1/1/1 admin-state enable 
-> interfaces 1/1/7 admin-state enable

<<<PAGE 555>>>
5 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
4.2. 
Creating two SPB services 
This step consists in configuring a Shortest Path Bridging (SPB) service and associates that service with a 
backbone service instance identifier (I-SID) and BVLAN. 
 
 
Notes 
- 
The service number is only locally significant and can differ across different BEBs. 
- 
The ISID number is globally significant and must match across all BEBs connecting a given service. 
- 
The BVLAN that the service is mapped must also match across all BEBs connecting a given service. 
- 
Different services can be mapped to different BVLANs to achieve traffic load balancing 
On each of the BEB nodes, create two instances ISID 2001 and 2002 that will be associate respectively with 
the BVLANs 2001 and 2002. 
Switch 7 & 8 
-> service spb 2001 isid 2001 bvlan 2001 description vlan2 
admin-state enable 
-> service spb 2002 isid 2002 bvlan 2002 description vlan3 
admin-state enable 
 
 
Notes 
- 
ISID and BVLAN must be defined on all SPB network for network consistency. 
- 
Each SPB service is capable of learning customer MAC addresses from the access side (SAPs) and from the 
network side (Mesh SDP) and then switching the traffic based on this information. 
- 
Each ISID can be attached to one BVLAN only. 
4.3. 
Configuring SPB access ports 
On each BEB nodes (OS6860-A and OS6860-B), configure the service access port(s) accordingly to the lab 
diagram.  The service access port(s) is the entry point of the LAN Access switch. (OS6360-A et OS6360-B vlan 
2 and 3) 
 
 
Notes 
Access ports are required to configure a SAP. The access port can be either a fixed port or logical port 
(linkagg). 
A SAP is the point at which customer traffic enters and exits the service. SAPs are not configurable on other 
port types. 
Switch 7  
-> service access port 1/1/3 
-> interfaces 1/1/3 admin-state enable 
-> service access port 1/1/7 
-> interfaces 1/1/7 admin-state enable 
Switch 8 
-> service access port 1/1/3 
-> interfaces 1/1/3 admin-state enable

<<<PAGE 556>>>
6 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
4.4. 
Setting up the SAP services 
This will define the type of customer traffic that can enter the SPBM network.  
 
In this exercise, we will associate the Vlan2 traffic to the service 2001 and Vlan3 to the service 2002 on the 
BEB nodes. 
Classify the Vlan2 and Vlan3 traffic with the identifier 2 and 3 on the uplink port 
Switch 7  
-> service spb 2001 sap port 1/1/3:2 admin-state enable stats 
enable 
-> service spb 2002 sap port 1/1/3:3 admin-state enable stats 
enable 
-> service spb 2001 sap port 1/1/7:2 admin-state enable stats 
enable 
Switch 8 
-> service spb 2001 sap port 1/1/3:2 admin-state enable stats 
enable 
-> service spb 2002 sap port 1/1/3:3 admin-state enable stats  
Enable 
 
 
Notes 
A SAP ID is comprised of a customer-facing port (referred to as an access port) and an encapsulation value that 
is used to identify the type of customer traffic to map to the associated service. 
Configuring SAPs with different encapsulation types for the same access port is allowed.

<<<PAGE 557>>>
7 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 5 
Analysis and understanding the concept of SPB services 
5.1. 
Checking the configuration 
Display the information of the services configured 
Switch 7 & 8 
-> show spb isis services 
-> show service 
-> show service access 
-> show service spb 
-> show service sdp spb 
-> show service spb ServiceId ports  
-> show service mesh-sdp 
-> show service spb ServiceId counters 
-> show service spb ServiceId debug-info 
-> show mac-learning 
 
 
Notes 
Refer to the CLI reference and Network Configuration Guides for detailed information about outputs. 
5.2. 
Testing end device connectivity 
From Virtual machines connected on the access switch, run some connectivity test between machines sharing 
the same SPB service (members of same Vlan). 
In addition to the ping requests and use of tracert application, use the following commands on BEB systems to 
verify the @MAC classified as well as the associated SAP. 
Test scenario 
- Open the clients (shortcut 
 on access POD desktop) 
- Use following VMs 
- PodXClient5 on OS6360-A port 1/1/1 
- PodXClient6 on OS6360-B port 1/1/1 
- PodXClient9 on OS6360-A port 1/1/2 
- PodXClient10 on OS6360-B port 1/1/2 
- PodXClient3 on OS6560-A port 1/1/1 
 
- Right-click on it then select Open console 
- For each of the VM client 
- Note the @MAC  
- Assign an IP address 
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.5 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.6 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.5 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.6 
PodXClient3 
Switch 3 
1/1/1 
2 
192.168.2.103 
192.168.2.3

<<<PAGE 558>>>
8 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
- In addition to the ping requests and use of tracert application, use the following commands on BEB 
systems to verify the @MAC classified as well as the associated SAP. 
 
-> show mac-learning domain spb 
-> show service spb 2001 sap port 1/1/3:2 
-> show service spb 2001 sap port 1/1/3:2 counters 
-> show service spb 2002 sap port 1/1/3:3 
-> show service spb 2002 sap port 1/1/3:3 counters 
... 
 
- Example: 
 
sw7 (6860-A) -> show mac-learning domain spb 
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
        ID = ISID/Vnid/vplsid 
 
   Domain    Vlan/SrvcId[:ID]           Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
       SPB                2001:2001   00:0c:29:1a:13:68            dynamic    servicing               sap:1/1/3:2 
       SPB                2001:2001   94:24:e1:f0:f6:39            dynamic    servicing               sap:1/1/3:2 
       SPB                2001:2001   00:0c:29:44:aa:3b            dynamic    servicing               sap:1/1/7:2 
       SPB                2001:2001   2c:fa:a2:95:8f:9f            dynamic    servicing               sap:1/1/7:2 
       SPB                2001:2001   2c:fa:a2:95:8f:ac            dynamic    servicing               sap:1/1/7:2 
       SPB                2001:2001   00:0c:29:83:6f:85            dynamic    servicing            sdp:32775:2001 
       SPB                2001:2001   94:24:e1:f6:65:95            dynamic    servicing            sdp:32775:2001 
       SPB                2001:2001   94:24:e1:f6:65:9e            dynamic    servicing            sdp:32775:2001 
       SPB                2002:2002   00:0c:29:31:0f:97            dynamic    servicing               sap:1/1/3:3 
       SPB                2002:2002   94:24:e1:f0:f6:39            dynamic    servicing               sap:1/1/3:3 
       SPB                2002:2002   94:24:e1:f0:f6:42            dynamic    servicing               sap:1/1/3:3 
       SPB                2002:2002   00:0c:29:ed:d0:4a            dynamic    servicing            sdp:32776:2002 
       SPB                2002:2002   94:24:e1:f6:65:95            dynamic    servicing            sdp:32776:2002 
       SPB                2002:2002   94:24:e1:f6:65:9e            dynamic    servicing            sdp:32776:2002 
 
 Total number of Valid MAC addresses above = 14 
 
 
What commands would be used to determine the following? 
- 
SAP identifiers list 
>  ____________________________________________________  
- 
Counters per Service 
>  ____________________________________________________  
- 
List of Service Distribution Points (SDP) 
>  ____________________________________________________  
- 
List of SAP for a specific port 
>  ____________________________________________________  
- 
Status of Service Access Points 
>  ____________________________________________________  
- 
@MAC addresses learned on a SAP 
>  ____________________________________________________

<<<PAGE 559>>>
Tech Brief
Shortest Path Bridging Architecture guide
Shortest Path Bridging 
Architecture guide

<<<PAGE 560>>>
2
Tech Brief
Shortest Path Bridging Architecture guide
Table of Contents
1.  About this architecture guide........................................................................................4
1.1  Purpose..........................................................................................................................4
1.2  Audience........................................................................................................................4
1.3  Glossary.........................................................................................................................4
1.4  References.....................................................................................................................5
2.  The network needs to evolve........................................................................................5
3.  Introducing SPB...................................................................................................................6
3.1  Scalable, fast-converging, multi-path fabric....................................................7
3.2  Multi-tenancy...............................................................................................................7
3.3  Dynamic service instantiation..............................................................................8
3.4  Edge-only service provisioning............................................................................8
3.5  Micro-segmentation..................................................................................................8
3.6  Non-IP core...................................................................................................................9
4.  The Data Plane: IEEE 802.1ah Provider backbone bridging..............................9
5.  The Control Plane: RFC 6329 IS-IS Equal-cost trees..........................................11
6.  The service framework..................................................................................................13
7. BUM traffic..........................................................................................................................15
8.  Creating an SPB backbone...........................................................................................16
9.  L2 services.........................................................................................................................20
10.  Routing concepts...........................................................................................................26
11.  L3 services.......................................................................................................................29
11.1  VPN Lite...................................................................................................................29
11.2  L3 VPN......................................................................................................................30
11.3  VPN Lite versus L3 VPN....................................................................................34
12.  Shared Services VPN and Route Leaking.............................................................34
13.  Automation......................................................................................................................36
13.1  Auto-Fabric.............................................................................................................36
13.2  Dynamic SAPs........................................................................................................38
13.3  Dynamic Services.................................................................................................42

<<<PAGE 561>>>
3
Tech Brief
Shortest Path Bridging Architecture guide
14.  Management...................................................................................................................43
15.  Operation and Maintenance......................................................................................45
15.1  Connectivity Fault Management: 802.1ag..................................................45
15.2  Network performance: Service Assurance Agent ...................................47
15.3  Network maintenance.........................................................................................48
16.  Service attachment redundancy.............................................................................48
17.  Loop avoidance and suppression...........................................................................51
18.  General design guidelines..........................................................................................52
18.1  BVLANs.....................................................................................................................52
18.2  VLAN-to-Service mapping.................................................................................52
18.3  Virtual Chassis.......................................................................................................53
18.4  Link Aggregation...................................................................................................53
18.5  Link Metric..............................................................................................................54
18.6  QoS.............................................................................................................................54
19.  Security guidelines.......................................................................................................54
19.1  Management VRF..................................................................................................55
19.2  MACSec.....................................................................................................................55
19.3  NAC............................................................................................................................55
19.4  Router authentication.........................................................................................55
20.  Conclusion........................................................................................................................56

<<<PAGE 562>>>
4
Tech Brief
Shortest Path Bridging Architecture guide
1.  About this architecture guide
1.1  Purpose
The purpose of this architecture guide is to present SPB (802.1aq) networking concepts along 
with design and deployment guidelines. It does not attempt to cover every aspect, nor every 
possible architecture option, only the most common, validated and recommended architectures. 
You are encouraged to refer to the Alcatel-Lucent Operating Software (AOS) documentation for 
additional details, options and guidelines.
1.2  Audience
The intended audience for this document includes customer and business partner networking 
professionals involved in the design and deployment of enterprise networks.
1.3  Glossary
AG	
Access Guardian
BCB	
Backbone Core Bridge
B-DA	
Backbone Destination Address
BEB	
Backbone Edge Bridge
BGP	
Border Gateway Protocol
BMAC	
Backbone MAC
B-SA	
Backbone Source Address
BSN	
Base Service Number
B-VID	
Backbone VLAN ID
BVLAN	
Backbone VLAN
CMAC	
Customer MAC
CP	
Control Plane
DoS	
Denial of Service
DP	
Data Plane
ECT	
Equal-Cost Tree
FDB	
Forwarding Data Base
IETF	
Internet Engineering Task Force
iFab	
Intelligent Fabric
IGP	
Interior Gateway Protocol
ISID	
Instance Service Identifier
IS-IS	
Intermediate System to Intermediate System
LDP	
Label Distribution Protocol
MAC	
Media Access Control
MACs	
Moves Adds and Changes
MP-BGP	 Multi-Protocol BGP

<<<PAGE 563>>>
5
Tech Brief
Shortest Path Bridging Architecture guide
MSTP	
IEEE 802.1s Multiple Spanning Tree Protocol
NAC	
Network Admission Control
OSPF	
Open Shortest Path First
PBB	
IEEE 802.1ah Provider Backbone Bridging
Q-in-Q	
IEEE 802.1ad Provider Bridging
RADIUS	
Remote Access Dial-In User Service
ROI	
Return on Investment
RSTP	
IEEE 802.1w Rapid Spanning Tree Protocol
SAP	
Service Access Point
SDP	
Service Distribution Point
SPB	
IEEE 802.1aq Shortest Path Bridging
SPB-M	
SPB MAC-in-MAC
SPB-V	
SPB Q-in-Q
SPF	
Shortest Path First
STP	
IEEE 802.1D Spanning Tree Protocol
TLV	
Type, Length, Value
UNP 	
User Network Profile
1.4  References
[1]	 IP/IPVPN services with IEEE 802.1aq SPB networks - draft-unbehagen-spb-ip-ipvpn-00.txt
[2]	 Alcatel-Lucent OmniSwitch® Template Based Provisioning with Alcatel-Lucent OmniVista®  
2500 Network Management System (NMS)
[3]	 Network infrastructure security best practices
2.  The network needs to evolve
Local Area Networks (LAN) have traditionally relied on Spanning Tree Protocol (STP), and its 
variants (RSTP, MSTP), collectively referred to as “STP” for simplicity, for loop prevention. STP 
achieves a loop-free topology by electing a “root bridge” and building a least-cost tree linking 
the root bridge with other non-root nodes. This least-cost tree is created by pruning (disabling) 
all branches (links) which are not in the least-cost path towards the root. STP’s design principle 
presents several drawbacks for modern Enterprise networks:
•	 Unused links: Creating a loop-free topology by disabling network links results in inefficient 
bandwidth use and low Return on Investment (ROI)
•	 Sub-optimal paths: While communication to-and-from the root bridge follows the least- 
cost path, communication between non-root bridges may need to traverse a sub-optimal  
route transiting the root-bridge instead of alternative better routes over links that have  
been disabled
•	 Slow convergence: STP is a decades-old protocol designed when network devices were far less 
powerful than they are today. Even with the “rapid” version of STP, typical convergence times 
are in the order of seconds. While STP re-converges to a new topology, transient loops may 
form, resulting in packet drops, link saturation, and session timeouts.

<<<PAGE 564>>>
6
Tech Brief
Shortest Path Bridging Architecture guide
Figure 1. The problems with STP
Destination 2
Inefﬁcient
routes
Cannot use
these links
All the nodes on
the route need to
learn MAC’s M1-M100
Destination 1
MACs
M1 ... M100
Source
Root bridge
 
In addition to STP’s weaknesses, Ethernet’s scalability beyond the LAN is limited by its lack of 
a coordinated control plane and use of a flat (as opposed to hierarchical) address space. Legacy 
Ethernet networks present the following challenges:
•	 Flooding: Ethernet’s “flood and learn” address learning floods unknown-unicast traffic until  
the destination address is learned from return traffic
•	 MAC Learning: All nodes in the LAN learn all end-device MAC addresses thus posing a 
scalability challenge
Lastly, IEEE 802.1ad (Provider Bridging, or Q-in-Q) is limited to a maximum of 4096  
service instances. 
3.  Introducing SPB
802.1aq Shortest Path Bridging (SPB) is an IEEE networking standard whose primary focus was 
addressing the challenges in STP. But SPB is much more than STP’s evolution: SPB provides 
MPLS-like VPN services but is significantly simpler to deploy and maintain. And unlike MPLS, 
which requires a “stack” of protocols (for example: LDP, OSPF, MP-BGP, among others), SPB relies 
on a single protocol to provide this functionality: IS-IS (Intermediate System to Intermediate 
System). IS-IS is the only control plane protocol required to build a multi-path topology, perform 
address learning, and carry VPN routes across the backbone. Alcatel-Lucent Enterprise’s 
Intelligent Fabric (iFab) brings further simplification by automating network node provisioning, 
client device attachment, and dynamic service instantiation. Because of this simplicity and 
automation, an ALE-powered SPB solution offers high-end services for a lower total cost of 
ownership (TCO). Let’s analyse SPB’s benefits in further detail.

<<<PAGE 565>>>
7
Tech Brief
Shortest Path Bridging Architecture guide
3.1  Scalable, fast-converging, multi-path fabric
Figure 2. Addressing STP’s challenges
Destination 2
Multiple
shortest
paths
All the links
are usable
MACs M1-M100
learning restricted
to the edges
Destination 1
MACs
M1 ... M100
PBB
encapsulation
at the edges
PBB
encapsulation
at the edges
PBB
encapsulation
at the edges
3
2
1
SPB’s loop-free topology is built by a link-state routing protocol running Dijkstra’s Shortest 
Path First (SPF) algorithm: IS-IS. With IS-IS, no network link is disabled, all paths are available 
and traffic between any pair of nodes follows the shortest path. In addition, with MAC-in-MAC 
encapsulation, backbone nodes do not learn any end-device MAC addresses, thus increasing  
the network scalability and stability. With IS-IS and MAC-in-MAC encapsulation, SPB creates an,  
any-to-any, scalable and fast-converging “fabric” supporting multiple active optimal paths for 
both bridged and routed traffic.
3.2  Multi-tenancy
SPB natively supports multi-tenancy: The physical network is partitioned into multiple virtual 
“slices” referred to as VPNs, “containers” or “communities”. Customers, or IoT device groups, 
segregated into different VPNs are isolated and do not interfere with one another. In fact, they 
can use overlapping address space without conflict. Inter-VPN communication, if needed, is 
tightly controlled by firewall policies. This multi-tenancy capability makes SPB suitable for use 
cases such as smart cities, transportation, higher education, video surveillance or data centres, 
to name a few. SPB’s scalability is not limited to 4096 tenants because its service identifier, the 
ISID, is a 24-bit field which can differentiate up to 16M services.
Figure 3. Multi-tenancy

<<<PAGE 566>>>
8
Tech Brief
Shortest Path Bridging Architecture guide
3.3  Dynamic service instantiation
SPB services do not need to be statically bound to a switch port. SPB is tightly integrated with 
Alcatel-Lucent Enterprise’s classification and Network Admission Control (NAC) framework 
known as Access Guardian (AG). Upon connection, end devices can be classified (for example; 
based on the MAC OUI or IoT “fingerprint” rules) or authenticated (for example; through 802.1x 
or MAC) against a RADIUS server. The appropriate service is dynamically instantiated according 
to the device or user classification, or role attribute returned by the RADIUS server. In the same 
manner, this user-to-service binding is removed when the user/device disconnects. This dynamic 
service instantiation has the following advantages:
•	 User/Device mobility: The network configuration dynamically adapts to mobile users and 
devices or Virtual Machines (VMs) migrations without need for Move, Add or Change requests
•	 Increased security: Services are instantiated on an as-needed basis only, and for authenticated 
devices/users only, if applicable. This association is maintained for as long as the user/device 
remains connected and/or authenticated, and is brought down on disconnection/log-off. These 
ephemeral services are inherently more secure: they cannot be scanned, DoSd, or otherwise 
hacked, while they’re not active.
•	 Device templates: This dynamic instantiation of network services easily lends itself into 
template-based configuration of network nodes. Edge nodes can all share the same base 
configuration template and dynamically adjust the service configurations on the fly.
3.4  Edge-only service provisioning
Whether statically or dynamically instantiated, SPB services need only be provisioned on edge 
nodes, not on core nodes. Core nodes are effectively isolated from service Moves, Adds and 
Changes and require no touch while these activities are performed. In fact, service MACs can  
be conducted during business hours and do not require a maintenance window to be scheduled, 
reducing time-to-service. 
3.5  Micro-segmentation
Firewalls filter and control communication between different VPN “tenants” or “containers”. 
But, how do you secure communication within the same VPN? For instance, if one device were 
compromised, how do you prevent lateral movement to other resources within the same VPN? 
When users/devices are dynamically bound to a service, they are also mapped to a User Network 
Profile (UNP). The UNP is a set of Access Control Lists (ACLs) and Quality of Service (QoS) policies 
which are applied to the device/user according to the device category or user role. Let’s take 
CCTV cameras as an example: ACLs contained in the UNP can allow communication between  
the camera and surveillance servers but at the same time block camera-to-camera communication, 
preventing the spread of malware, “pivoting” and other hacking techniques which rely on  
lateral movement.

<<<PAGE 567>>>
9
Tech Brief
Shortest Path Bridging Architecture guide
Figure 4. Micro-segmentation
Authenticate
Classify
Auto provision
Audio/visual proﬁle
✓ Container
✓ Quality
✓ Security
Authenticate
Classify
Auto provision
Campus operation proﬁle
✓ Container
✓ Quality
✓ Security
Authenticate
Classify
Auto provision
Security proﬁle
✓ Container
✓ Quality
✓ Security
 
3.6  Non-IP core
Even when providing L3 services to IP packets, SPB core nodes do not route traffic, they bridge 
it. In fact, SPB core nodes do not have IP addresses and the IS-IS control protocol, unlike OSPF 
and BGP, does not run on top of IP. This makes the network core inherently more secure and 
protects it from IP-based attacks such as scanning, spoofing, DoS and others. Of course, SPB 
nodes still need an IP address for management purposes, but the management IP interface is 
isolated in its own service and VRF, not in-line with user traffic.
4.  The Data Plane: IEEE 802.1ah Provider backbone bridging
The Data Plane’s (DP) mission is to forward user traffic between different ports. The DP makes 
no decisions as to what port a frame should be forwarded to. It simply performs lookups on 
the Forwarding Data Base (FDB). FDB entries indicate what port, or group of ports, each frame 
should be forwarded to and what encapsulation to use. Building, or populating entries in the 
FDB, is a function of the Control Plane (CP), which is discussed in the next section.
The SPB data plane utilizes IEEE 802.1ah Provider Backbone Bridging (PBB), aka MAC-in-MAC, 
encapsulation. The PBB header includes de following fields:
B-VID: Or Backbone VLAN (BVLAN) ID. A VLAN that serves as a transport VLAN for the SPB 
service instances and to connect SPB bridges together through SPT sets. Unlike the standard 
VLAN domain which uses “flood and learn” or source learning in the DP to populate the FDB,  
the BVLAN domain’s FDB is pre-populated by the CP. 
ISID: Service Instance Identifier. The ISID is a 24-bit number that designates the service instance, 
tenant, container or VPN. Different SPB services are assigned different ISIDs and isolated from 
one another. Each SPB service or ISID is bound to a BVLAN.
B-SA and B-DA: Or Backbone source and destination MAC addresses. The MAC addresses associated 
with SPB nodes (BMACs). Within the SPB backbone, traffic is forwarded based on the destination 
BMAC (B-DA). Inner customer MACs are not learnt or used for forwarding within the backbone.

<<<PAGE 568>>>
10
Tech Brief
Shortest Path Bridging Architecture guide
Ethertype: 0x88E7
Upon entering the SPB domain, the PBB header is wrapped around the incoming frame which 
can be un-tagged, single-tagged (IEEE 802.1q) or double-tagged (IEEE 802.1ad). Figure 5 
illustrates the case of a double-tagged (Q-in-Q) frame. Note that MAC and BMAC addresses  
are shortened to 2 bytes for simplicity in this diagram.
Figure 5. PBB Data Plane
MAC :00:01
Customer
network
Customer
network
Provider bridge
network
Provider bridge
network
Provider backbone
bridge network
MAC :00:02
MAC :00:0B
MAC :00:0A
Ethertype 802.1ad
00:01
Ethertype 802.1q
S-VID
C-VID
Ethertype (IP)
Payload
00:02
Ethertype 802.1ad
00:01
Ethertype 802.1q
S-VID
C-VID
Ethertype (IP)
Payload
00:02
Ethertype 802.1ad
00:0A
Ethertype 802.1ah
B-VID
Ethertype 802.1q
Ethertype (IP)
C-VID
I-SID
Payload
00:0B
Ethertype 802.1ad
00:01
S-VID
00:02
Ethertype 802.1q
00:01
Ethertype (IP)
C-VID
Payload
00:02
Ethertype 802.1q
00:01
Ethertype (IP)
C-VID
Payload
00:02
 
Let’s define a few key terms.
BEB: An SPB switch positioned at the edge of the PBB network that learns and encapsulates 
(adds an 802.1ah backbone header to) “customer” frames for transport across the backbone 
network. The BEB interconnects the customer network space with PBB network space.
BCB: An SPB node that resides inside the PBB network core. The BCB employs the same BVLAN 
on two or more network ports. This BVLAN does not terminate on the switch itself; traffic 
received on an SPB network port is switched to other SPB network ports. As a result, the BCB 
does not have to learn any of the customer MAC addresses. It mainly serves as a transit bridge 
for the PBB network.
Within the SPB domain, that is, between BEB and BCB nodes, frame forwarding depends entirely 
on the outer PBB 802.1ah header (BMAC and BVLAN) and not on the inner header or “customer” 
MAC addresses (CMAC). In fact, the SPB backbone nodes do not learn CMACs and this makes 
SPB networks more scalable and stable (CMACs are not learnt and therefore do not need to be 
flushed and re-learnt when they change or move). 
The DP implements an additional loop mitigation mechanism by which a node will not accept 
unexpected frames from their neighbours. This additional loop mitigation mechanism is faster 
during topology changes. In summary, SPB implements two loop avoidance mechanisms: loop 
prevention and loop mitigation.

<<<PAGE 569>>>
11
Tech Brief
Shortest Path Bridging Architecture guide
5.  The Control Plane: RFC 6329 IS-IS Equal-cost trees
As stated earlier, the role of the CP is to populate the FDB tables used by the DP. SPB uses IS-IS, 
or Intermediate System to Intermediate System (ISO/IEC 10589:2002); a well-known, proven 
and widely-deployed protocol, particularly in service-provider backbones. IS-IS is responsible 
for topology and service discovery. IS-IS is an extensible link-state protocol which implements 
Dijkstra’s Shortest Path algorithm for path computation. IS-IS extensions for SPB are described 
in RFC 6329 and include a new Network Layer Protocol Identifier (NLPID), as well as a set of 
Type-Length-Values (TLVs). In a nutshell, these extensions add support for multiple topologies, 
allowing load sharing over multiple equal-cost paths, and service-membership discovery, or in 
other words: Communicating what services are enabled on each SPB node.
Figure 6. RFC 6329 IS-IS extensions
SPB-ISIS
New!
Existing!
SPB extensions
Discovery and computation
NLPI, TLVs, PDUs
Discovery – Hello and LSP packets, Computation – SPF and SPT
 
Unlike STP which creates a single tree rooted at the root bridge, in SPB networks, every node 
builds a topology tree rooted on itself. This is the key reason why, in an SPB network, traffic 
between any pair of nodes always travels along the shortest path. When using STP, traffic 
between two nodes does not necessarily travel over the shortest path unless one of the two 
nodes involved is the root bridge. This is illustrated in figure 7 in which B1 is the root bridge. 
Traffic between nodes B5 and B2 for instance, none of which is the root bridge, cannot use the 
direct single-hop path because that link is disabled by STP. Traffic between these two nodes 
must take a 3-hop detour traversing the root bridge.
Figure 7. Multiple trees
B5
B2
B4
B1
Spanning Tree
SPB
B5
B2
Single root bridge
Every bridge is the root
Path B5 to B2 = B5 – B3 – B1 – B2
Path B5 to B2 = B5 – B2
B4
B1
B3
B3
 
In contrast, when using SPB, no link is disabled: each node is the root of its own tree. Nodes B2 
and B5 can simply communicate over the direct single-hop path while at the same time they can 
communicate with other nodes over different paths (for example; between B4 and B5). SPB’s 
support for multiple trees and multiple active paths unlocks utilization of bandwidth in optimal 
paths that would otherwise be wasted, increasing throughput and reducing latency.
An SPB network supports up to 16 BVLANs and each node builds a SPF tree for each BVLAN. 
Load balancing is accomplished by mapping different tenant services (ISIDs) to different BVLANs.  
Service traffic between any node pair uses a single path and this path only changes if the 
topology changes, for instance, on node or link failure and subsequent path re-computation. In 
other words: SPB networks do not balance loads on a packet-by-packet basis like IP networks 
do. Provided the physical topology supports multiple shortest paths (same cost and same hop

<<<PAGE 570>>>
12
Tech Brief
Shortest Path Bridging Architecture guide
count) between two nodes, different BVLANs can build different trees and services mapped to 
those BVLANs can use different paths. And, those paths will remain the same for as long as the 
topology remains the same. An important property of SPB networks is that network paths are 
deterministic and frames are delivered in the order they were sent. This property is important 
for certain applications such as storage and real-time application traffic.
Figure 8. One tree per node and per BVLAN
B5
B2
B4
B1
B1’s tree on BVLAN A
B1’s tree on BVLAN B
B1’s tree on BVLAN C
B5
B2
B4
B1
B3
B5
B2
B4
B1
B3
B3
B5
B2
B4
B1
B5’s tree on BVLAN A
B5’s tree on BVLAN B
B5’s tree on BVLAN C
B5
B2
B4
B1
B3
B5
B2
B4
B1
B3
B3
 
The trees shown in figure 8 are SPB’s equal-cost trees (ECTs). Each node builds a tree per 
BVLAN and the cost to reach other nodes is the same across all BVLANs. The ECT-ID is a number 
assigned to each BVLAN at the time of BVLAN creation and is used for tie breaking during path 
computation. Assigning different ECT-IDs to different BVLANs helps those BVLANs build different 
trees, provided the underlying topology supports multiple equal-cost, or shortest paths.
Another important property of SPB networks is path symmetry. If you closely examine the 
picture above, you will notice that the path from node X to node Y is identical to the path from 
node Y to node X. Path symmetry is key to Operations and Maintenance (OAM). For instance, 
one-way delay calculations can be easily derived from roundtrip delay measurements. Note  
that this is not the case for other IP-based technologies such as MPLS in which the reverse  
path may differ.

<<<PAGE 571>>>
13
Tech Brief
Shortest Path Bridging Architecture guide
Figure 9. Symmetric paths, per-BVLAN load balancing
B5
B2
B4
B1
B5
B2
B4
B1
B3
B5
B2
B1 <–> B5 path BVLAN B
B1 <–> B5 path BVLAN A
B1 <–> B5 path BVLAN C
B4
B1
B3
B3
 
The result of IS-IS path computation for each BVLAN and node is the FDB which is used by the 
data plane for frame forwarding. Figure 10 shows BEB5’s unicast FDB. The multicast FDB will  
be discussed in Section 7.
Figure 10. B5’s Unicast FDB
B5
B2
B4
B1
B3
Outbound port
Node
BVID
Port 1
B1
BVID A
Port 2
B1
BVID B
Port 3
B1
BVID C
Port 1
B2
BVID A
Port 1
B2
BVID B
Port 1
B2
BVID C
Port 2
B3
BVID A
Port 2
B3
BVID B
Port 2
B3
BVID C
Port 3
B4
BVID A
Port 3
B4
BVID B
Port 3
B4
BVID C
 
6.  The service framework
An SPB service represents a VPN, or tenant, and is uniquely identified by its service identifier, 
the ISID. An SPB service needs only be created, or instantiated, on BEB nodes, not on BCB 
nodes, and only on those BEB nodes servicing locations associated to the service. SPB service 
membership information is shared across the SPB backbone by way of IS-IS TLVs such that all 
SPB nodes have a consistent view of the services which are active on each BEB. Each node  
then builds a service database.
Figure 11. The service database
B5
B2
B4
B1
B3
Node
BVID
ISID
B1
BVID A
66
B2
BVID A
66
B4
BVID A
66
B5
BVID A
66
B1
BVID B
77
B5
BVID B
77
ISID 66
ISID 77
ISID 66
ISID 66
ISID 66
ISID 77

<<<PAGE 572>>>
14
Tech Brief
Shortest Path Bridging Architecture guide
In each BEB node there are two kinds of virtual ports:
Service Access Point: The SAP is a UNI-side logical port which binds a physical port and specific 
customer traffic types (untagged, single-tagged, double-tagged or all) to an SPB service. Multiple 
SAPs can be associated to the same physical port thus multiplexing and mapping different 
customer traffic encapsulations to different SPB services.
Service Distribution Point: The SDP is an NNI-side logical port which binds an SPB service to  
a far-end BEB on which the service is instantiated. SDPs are dynamically created in the CP and 
only for those far-end BEBs with SAPs for the specific service. 
Let’s look at figure 12. In this diagram, B5 terminates 2 SPB services: One is associated to  
ISID 66 and the other to ISID 77. There are two SAP ports, one for each service. SAP 1:1 is 
defined on port 1, matches traffic tagged with VLAN 1, and binds it to service 66. SAP 2:2  
is defined on port 2, matches traffic tagged with VLAN 2, and binds it to ISID 77. 
ISID 66 is also enabled on nodes B1, B2 and B4 while ISID 77 is also enabled on node B1. 
Figure 12. The service framework
B5
B2
B4
B1
Node
BVID
Identiﬁer
—
—
SAP 1:1
—
—
SAP 2:2
B1
BVID A
SDP 32769: 66
B2
BVID A
SDP 32768: 66
B4
BVID A
SDP 32767: 66
B1
BVID B
SDP 32766: 77
ISID 66
ISID 77
SAP 1:1
SAP 2:2
ISID 66
ISID 66
ISID 66
ISID 77
SDP Y:66
SDP X:66
SDP X:77
SDP Z:66
 
It should be noted that while BMAC address learning is performed in the CP (for example; not 
through “flood and learn”) CMAC address learning is performed in the BEB’s DP through flood 
and learn. Near-end CMACs are bound to SAP ports and far-end CMACs are bound to SDP ports. 
BCB nodes have neither SAP nor SDP ports and therefore do not learn any CMACs.
Let’s expand this example by adding some end customer sites and CMACs associated to those 
customers. We will keep using 2-byte MAC addresses for simplicity. In figure 13, near-end CMAC 
addresses are bound to SAP ports while far-end CMAC addresses are bound to SDP ports. Within 
the service domain, a BEB performs CMAC source address learning like a standard Ethernet 
switch, except there is no “flooding” of BUM traffic. BUM traffic is discussed in the next section.
Figure 13. Customer MAC address learning
B5
B2
MAC B:B
MAC D:D
MAC E:E
MAC A:A
MAC C:C
MAC G:G
B4
B1
CMAC
ISID
Identiﬁer
A:A
66
SAP 1:1
E:E
77
SAP 2:2
C:C
66
SDP 32769: 66
B:B
66
SDP 32768: 66
D:D
66
SDP 32767: 66
G:G
77
SDP 32766: 77
ISID 66
ISID 77
ISID 66
ISID 66
ISID 66
ISID 77
SDP Y:66
SDP X:66
SDP X:77
SDP 1:1
SDP 2:2
SDP Z:66

<<<PAGE 573>>>
15
Tech Brief
Shortest Path Bridging Architecture guide
7. BUM traffic
SPB supports 3 BUM (broadcast, unknown unicast, and multicast) traffic replication and 
forwarding methods:
Head-end: In this mode, BUM traffic received on a SAP port is replicated at the ingress BEB and 
converted to multiple unicast frames: A replica is created for every other BEB in the same ISID 
and these replicas have the BEB BMACs as the B-DA and are forwarded using the unicast FDB. 
For this reason, Head-End replication can be inefficient in terms of bandwidth consumption but 
is efficient in terms of resource usage because it does not require a separate tree. However, 
Head-end replication can be optimal in some circumstances, particularly when combined with 
IGMP Snooping. Head-end replicated BUM traffic simply uses the unicast FDB and therefore 
travels along the same path. This property is known as congruency.
Figure 14. Head-end BUM replication
BEB4
BCB7
BEB3
BCB5
BEB1
Port
B-MAC
Type
Port 2
00:02
U
Port 7
00:03
U
Port 7
00:04
U
Port 7
00:05
U
Port 6
00:06
U
Port 7
BVID
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
00:07
U
ISID 77
ISID 77
ISID 77
ISID 77
BCB2
BCB6
 
Tandem (S,G): In this mode, a separate multicast SPT and FDB are created. The multicast SPT is also 
congruent with the unicast SPT however the B-DAs in the multicast FDB are multicast addresses 
constructed as a combination of ISID and source BEB BMAC. When a BUM frame is received on a 
BEB, it is MAC-in-MAC encapsulated with this special BMAC as the B-DA and forwarded according 
to the multicast FDB. A B node can use the unicast FDB to check if it is in the SPT between a source 
BEB and other BEBs in the same ISID. If the B node happens to be in the SPT, it will populate the 
multicast FDB such that the frame is replicated and forwarded as needed, to other BEBs connecting 
the same service (ISID). Tandem Replication is very efficient in terms of bandwidth use because it 
will only send a single replica on any given link; however, it is less efficient in terms of resource 
use because it requires an additional SPT and multicast FDB per ISID.
Figure 15. Tandem (S,G) BUM replication 
BEB4
BCB7
BEB3
BCB5
BEB1
Port
B-MAC
Type
Port 1
00:01
U
Port 2
00:02
U
Port 3
00:03
U
Port 4
00:04
U
Port 1
00:0W
M
Port 3
00:0X
M
Port 4
00:0Y
M
Port 5
00:0Z
M
Port 5
00:05
U
Port 6
BVID
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
Out Intf
Port 3/4/5
Port 1/5
Port 1
Port 1/3
00:06
U
ISID 77
ISID 77
ISID 77
ISID 77
BCB2
BCB6

<<<PAGE 574>>>
16
Tech Brief
Shortest Path Bridging Architecture guide
Tandem (*,G): In this mode, a separate multicast tree is created. This tree is not a Shortest Path 
tree and is not congruent with the unicast SPT. A multicast (*,G) is created for every BVLAN using 
Tandem (*,G) multicast replication. This (*,G) tree is similar to a Spanning Tree and is rooted at one 
B node according to the bridge priority. In this mode, there is a single tree for the BVLAN and not 
one tree for every node. Therefore, traffic will not generally follow the shortest path. This mode 
is a compromise between bandwidth and resource usage, however, it can be a good option when 
all traffic is sourced or destined towards the root bridge.
Refer to Table 1 to compare these three modes.
Table 1. Multicast replication modes and suggested uses
Head-end 
Tandem (S,G) 
Tandem (*,G)
Operation 
BUM traffic replicated at 
ingress BEB and forwarded 
using the unicast FDB. 
BUM traffic forwarded per the 
multicast FDB and replicated 
as needed at the SPT’s fork-out 
points. 
BUM traffic forwarded using 
a shared, non-SP tree and 
replicated at fork-out points.
Bandwidth efficiency 
Low 
High 
High 
Resource efficiency 
High
Low
Medium 
Congruency 
Yes 
Yes 
No 
Suggested use 
•	 Low multicast bandwidth
•	 Many sources and few 
receivers*
•	 High multicast bandwidth
•	 Few sources and many receivers
•	 When root bridge is 
source or receiver of 
most multicast traffic 
and congruency is not 
required
•	 When required to inter-
operate with third-party 
equipment
* When combined with IGMP Snooping.
8.  Creating an SPB backbone
In this section, we provide a sample SPB Backbone configuration and refer to figure 16 as 
a sample topology. We will continue using this sample topology throughout the rest of this 
document. Nodes BEB-1 through BEB-4 are called “BEB” nodes because we will add services 
to these nodes later. Node BCB will remain a pure transit node and not terminate any service.
If you observe this topology, you will notice that it provides up to 3 shortest paths, for example, 
between nodes BEB-1 and BEB-3, or between nodes BEB-2 and BEB-4. To take advantage of 
those 3 diverse paths for traffic load balancing, we need to create a minimum of 3 BVLANs. In 
this example, we will however, dedicate one BVLAN purely for control traffic and therefore we 
will create a total of 4 BVLANs. However, it should be noted that this is not strictly necessary, 
the control BVLAN can also be used for services.
Backbone configuration entails the following tasks:
•	 Creating one or more BVLANs with their associated ECT-IDs. ECT-IDs need not be explicitly 
defined, default ECT-IDs are applied
•	 Defining the control BVLAN
•	 Defining one or more SPB IS-IS interfaces
•	 Enabling the SPB IS-IS protocol

<<<PAGE 575>>>
17
Tech Brief
Shortest Path Bridging Architecture guide
Figure 16. Sample backbone topology
BEB3
BCB
BEB1
BEB2
1/1/50A
1/1/50A
1/1/50A
1/1/49A
1/1/49A
1/1/49A
1/1/49A
1/1/49A
1/1/52A
1/1/50A
1/1/54A
1/1/53A
1/1/54A
1/1/49A
1/1/54A
1/1/54A
BEB4
 
Following are the configuration snippets for all nodes.
Snippet 1. BEB-1’s backbone configuration
 
Snippet 2. BEB-2’s backbone configuration
 
Snippet 3. BEB-3’s backbone configuration
 
Snippet 4. BEB-4’s backbone configuration

<<<PAGE 576>>>
18
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 5. BCB backbone configuration
 
Through this configuration, VLANs 4000 through 4003 are defined as SPB backbone VLANs and 
will therefore not use any form of spanning tree protocol. AOS automatically assigns a different 
ECT-ID to each BVLAN and this maximises the chance that different BVLANs will create different 
SPTs, up to the maximum number of shortest paths supported by the physical topology. Nodes 
will exchange IS-IS “Hello” messages over the control BVLAN (such as, 4000 in this example) and 
form point-to-point adjacencies. LSPs are exchanged, a topology database is created and one SPT 
is built for each BVLAN. 
Let’s review this configuration with some show commands.
Snippet 6. “show SPB isis interface”
 
In the “show spb isis interface” command output we can observe three interfaces are SPB-IS-
IS enabled for L1 adjacencies. All three interfaces are both administratively and operationally 
up. By default, the link metric is 10 regardless of link speed. “Hello” messages are sent at nine 
second intervals and adjacencies are declared lost if no “Hello” message is received for three 
consecutive intervals (for example; 27 seconds).
Snippet 7. “show SPB isis nodes”
 
In the “show spb isis nodes” command output we can observe all discovered SPB IS-IS nodes 
including the local node. For each node, we can see the system or host name, the system ID 
(the BMAC), as well as the source ID and the bridge priority. The source ID is a 20-bit identifier 
which designates the node as the origin of BUM traffic and is derived from the system ID’s least 
significant bytes. The source ID is relevant when using tandem BUM replication. The bridge 
priority is 16-bit identifier and is used as a tie breaker during path computation.

<<<PAGE 577>>>
19
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 8. “show SPB isis adjacency”
 
In the “show spb isis adjacency” command output we can observe all SPB IS-IS adjacencies 
established by the local node. For each adjacency, we can see the system or host name,  
the system ID (the BMAC), as well as type (always L1 for SPB IS-IS), the state, the hold timer  
(number of seconds until the adjacency is declared lost if no “Hello” messages are received)  
and the interface over which the adjacency is formed. 
Snippet 9. “show SPB isis bvlans”
 
In the “show spb isis bvlans” command output we can observe, for each configured BVLAN, the 
ECT algorithm in use and whether the BVLAN is in use and has services mapped to it. So far, we 
have not configured any service, therefore the only BVLAN in use is the control BVLAN, which is 
used for IS-IS CP messaging. We can also observe the number of ISIDs mapped to the BVLAN. For 
services using tandem BUM replication, we can observe whether this is (S,G), which is the default, 
or (*,G). Note that while the choice of head-end versus tandem replication is done on a per-service 
basis, the choice between (S,G) and (*,G) tandem replication is done on a per-BVLAN basis. Lastly, 
the root bridge BMAC is shown only for those BVLANs using (*,G) tandem replication.
Snippet 10. “show SPB isis unicast-table”

<<<PAGE 578>>>
20
Tech Brief
Shortest Path Bridging Architecture guide
In the “show spb isis unicast-table” command output we can observe, for each node, the 
outbound interface used when sending unicast traffic to that node. Note that the outbound 
interface can be different for different BVLANs because different BVLANs can build different 
SPTs. For example, the path to BEB-3 goes through interface 1/1/49A in the case of BVLAN 
4000, interface 1/1/54A in the case of BVLANs 40001 and 4002, and interface 1/1/50A in the 
case of BVLAN 4003.
Snippet 11. “show SPB isis spf bvlan”
 
In the “show spb isis spb bvlan” command output we can observe, for a given BVLAN, the 
outbound interface, the next hop node, as well as the SPB metric and total number of hops 
required to reach a destination node. We can observe in this output that traffic destined towards 
BEB-3 will transit BEB-2 in the case of BVLAN 4000, BCB in the case of BVLANs 4001 and 4002, 
and BEB-4 in the case of BVLAN 4003.
9.  L2 services
A L2 service refers to a type of VPN service connecting multiple sites in a single any-to-any 
bridging domain. In this section, we continue building upon the previous example and create a 
L2 service on top of the previously created backbone configuration.
Services need only be created on BEBs, not on BCBs, and only on those BEBs where the service 
needs to be delivered. Creating an SPB service entails the following tasks:
•	 Creating a service and associating the service to an IS-IS and BVLAN – the specified BVLAN’s 
SPF will be used for the service traffic
•	 Defining a Service Access Port (SAP)
•	 Defining SAPs matching specific customer traffic

<<<PAGE 579>>>
21
Tech Brief
Shortest Path Bridging Architecture guide
Figure 17. L2 service
BEB3
BEB1
Site 2
Site 1
Site 3
Site 4
1/1/48
1/1/48
1/1/48
1/1/48
1/1/54A
BEB4
BEB2
ISID 1001
BVLAN 4001
 
With regard to figure 17, we provide BEB configurations in the snippets that follow.  
As well, please note:
•	 The service number is only locally significant and can differ across different BEBs
•	 The ISID number is globally significant and must match across all BEBs connecting  
a given service
•	 The BVLAN that the service is mapped must also match across all BEBs connecting  
a given service
•	 Different services can be mapped to different BVLANs to achieve traffic load balancing
Snippet 12. BEB-1’s service configuration
 
Snippet 13. BEB-2’s service configuration
 
Snippet 14. BEB-3’s service configuration
 
Snippet 15. BEB-4’s service configuration

<<<PAGE 580>>>
22
Tech Brief
Shortest Path Bridging Architecture guide
In the four configuration snippets above we can observe the following:
•	 Service 1 is associated to ISID 1001 and mapped to BVLAN 4001’s SPF tree
•	 Port 1/1/48 is defined as a SAP
•	 A SAP is defined on port 1/1/48 mapping untagged traffic (:0) to service 1
Let’s now proceed to verify the service status.
Snippet 16. “show service spb” – BEB view
 
In the “show service spb” command output we can observe, for a given BEB, the locally defined 
SPB services, their administrative and operational status, the number of (local) SAPs and (remote) 
SDPs along with the ISID and BVLAN number that the service is mapped to. We can also observe 
the multicast replication mode, which is head-end by default. The multicast replication mode can 
be changed to tandem on a per-service basis.
Snippet 17. “show service spb” – BCB view
 
In the “show service spb” command output we can observe that, by definition, a BCB does not 
have locally defined services.
Snippet 18. “show spb isis services” – BEB view
 
In the “show spb isis services” command output we can observe SPB services known to the node 
along with their ISID and BVLAN number and the node name, and BMACs that the service is 
enabled on. We should note that these services are learnt thanks to the IS-IS CP. A “*” denotes 
that the service also matches a service locally created on the BEB.

<<<PAGE 581>>>
23
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 19. “show spb isis services” – BCB view
 
In the “show spb isis services” command output we can observe the same output now from the 
perspective of a BCB. We should note that a BCB is still aware of all existing services with the 
IS-IS CP.
Snippet 20. “show service spb”
 
The “show service spb” command output provides some additional details about a given SPB 
service. We can highlight the following:
•	 RemoveIngressTag: As explained in section 3, by default, a PBB frame includes all the frame’s 
original tags. However, we can choose to remove those tags with the “service service_id 
remove-ingress-tag enable” command.
•	 VLAN Translation: A given service may require different encapsulations on different SAPs. 
For instance, a server may tag traffic with a specific VLAN while client devices may require 
untagged SAPs. In such situation, VLAN translation can be enabled to allow both devices  
to communicate. We should note that VLAN translation must be enabled both at service  
level with the command “service service_id vlan-translation enable” and on the SAP with  
the command “service access port vlan-xlation enable”.
•	 Allocation Type: Services can be either statically or dynamically created. We will cover 
dynamic service creation in section 13.3.
Snippet 21. “show service access”

<<<PAGE 582>>>
24
Tech Brief
Shortest Path Bridging Architecture guide
In the “show service access” command output we can observe, for a given BEB, the list of SAPs 
along with their type (manual or dynamic), the number of defined SAPs and whether VLAN 
translation is enabled or not. We will cover dynamic SAP creation in section 12.2. We can also 
observe the L2Profile assigned to the SAP. The L2Profile defines how L2 control protocol frames 
received on a SAP will be handled. Traffic can be peered, dropped, or tunnelled. Default L2 
profile settings are shown in Table 2. Additional L2 profiles can be created with the command 
“service l2profile name stp action 802.1x action 802.3ad action mvrp action gvrp action amap 
action 802.1ab action” and assigned to the SAP with the command “service access l2profile 
name”. We will cover unp SAPs and profiles in section 12.2.
Table 2. Default L2 profiles
Protocol
def-access-profile
unp-def-access-profile
STP
tunnel
drop
802.1x
drop
peer
802.3ad
peer
peer
MVRP
tunnel
tunnel
GVRP
tunnel
tunnel
AMAP
drop
drop
802.1ab
drop
drop
Snippet 22. “show service spb ports”
 
In the “show service spb ports” command output, we can observe local (SAP) as well remote 
(SDP) ports for a given service. For each port, we can see administrative and operational status, 
the system ID (BMAC) and BVLAN, as well as the system name and associated local interface. SDP 
ports will always display a “*” next to them because SDP ports are always dynamically created 
by the IS-IS CP. The name of an SDP is a combination of a dynamically generated number, 
followed by a colon and the service number.

<<<PAGE 583>>>
25
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 23. “show service mesh-sdp spb”
In the “show service mesh-sdp spb” command output we can observe far-end SDPs for each 
service along with the ISID number and the far-end system ID (BMAC), BVLAN, system name  
and associated interface.
Snippet 24. “show mac-learning domain spb” – BEB view
 
In the “show mac-learning domain spb” command output we can observe the list of CMAC 
addresses learnt in the SPB domain along with the service number and ISID, as well as the 
interface (SAP or SDP) port that the CMAC address is bound to. 
Snippet 25. “show mac-learning domain spb” – BCB view
 
In the “show mac-learning domain spb” command output we can observe the same output now 
from the point of view of a BCB node. As expected, BCB nodes do not learn any CMACs.

<<<PAGE 584>>>
26
Tech Brief
Shortest Path Bridging Architecture guide
10.  Routing concepts
Before delving into L3 services, which are covered in the next section, we need to discuss certain 
routing concepts in relation to SPB. The Alcatel-Lucent OmniSwitch® product line has supported 
SPB since AOS 7.3.1, released in 2012. Since then, multiple SPB-enabled platforms have been 
launched and each new platform incorporated new advancements in ASICs. 
First generation ASICs were not capable of routing and performing MAC-in-MAC encapsulation in 
a single-pass operation. Consequently, routing between IP interfaces associated to two different 
SPB services, or to a VLAN and an SPB service, had to traverse the switch fabric twice. This 
required an external physical loopback connecting two different switch ports: one port in the 
VLAN domain and another SAP in the SPB domain. IP interfaces could only be associated to a 
VLAN, not directly to an SPB service. It should be noted that these physical loopbacks can be 
either physical ports or linkaggs. When using VC, linkagg member ports can span different units 
in the VC for redundancy. We refer to this as two-pass routing with external physical loopback.
Newer generation ASICs support a concept similar to an external physical loopback without 
requiring a cable connection. One or more physical ports’ bandwidth is dedicated to the 
loopback function without requiring a cable to be attached. Multiple ports can be dedicated to 
this function for additional bandwidth and redundancy. When using multiple ports, ports are 
configured as a linkagg and, when using VC, linkagg member ports can span different units in 
the VC. We refer to this as two-pass routing with internal front-panel loopback. One additional 
difference between the internal front-panel loopback and the external physical loopback 
described in the previous paragraph is that the internal front-panel loopback is a single logical 
port, not two ports (a VLAN port and a SAP) as in the case of the external physical loopback. 
However, even in the single logical port, there is a “VLAN” function and a “SAP” function. This  
will become clearer when looking at the configuration snippets later in this section.
Latest generation ASICs support integrated routing and bridging in the SPB domain in the exact 
same manner as in the VLAN domain. This means that IP interfaces can be associated to an  
SPB service directly and traffic can be routed between two SPB services or between a VLAN 
and an SPB service in a single-pass operation without loopbacks. We refer to this as single-pass 
inline routing.
Figure 18. Routing options – Physical view
Single-pass
or inline
Two-pass with external
physical loopback
ISID 1
VLAN 1
ISID 2
VLAN 11
VLAN 1
VLAN port
1/1/1
SAP port
1/1/2
VLAN + SAP
all in one
port or LAG
ISID 1
Two-pass with internal
physical loopback
VLAN 11
VLAN 1
ISID 1
 
Figure 18 provides a physical view of these routing options. The leftmost diagram represents a 
switch supporting single-pass inline routing. This example shows a bridge with 2 SPB services, 
designated by their ISIDs, and one VLAN. IP interfaces are represented by dots. As we can see, 
the IP interfaces are bound to either VLANs or services and the switch performs inter-VLAN, 
inter-Service or inter-VLAN-Service routing directly in a single operation.

<<<PAGE 585>>>
27
Tech Brief
Shortest Path Bridging Architecture guide
The diagram in the middle illustrates the case of two-pass routing with a physical hairpin. In this 
diagram, you can observe that IP interfaces are bound to VLAN 1 and VLAN 11, but not directly 
to the service. The external physical loopback cable creates the link between the service and the 
“dummy” VLAN, VLAN 11 in this example, where the IP interface resides. This external physical 
loopback is configured with a SAP-side, where SAPs are defined for each service requiring 
routing, and a VLAN-side, where dummy VLANs mapping to those services are tagged. 
The right diagram illustrates the case of two-pass routing with internal front-panel loopback. 
In this diagram, the dotted line represents an imaginary physical external loopback, which is 
not required. In addition to not requiring an external physical loopback cable, the front-panel 
loopback requires a minimum of one port only. CLI configuration is different between physical 
external loopback and front-panel internal loopback. However, the concepts are very similar.  
You should still think about the front-panel internal loopback port or ports as having a SAP 
function and a VLAN function all in one port or linkagg.
Figure 19. Routing Options - Logical view
Single-pass
or inline
Two-pass with external
physical loopback
ISID 1
VLAN 1
ISID 2
VLAN 1
VLAN 1
VLAN 11
VLAN port
SAP port
VLAN + SAP
all in one port
ISID 1
Two-pass with internal
physical loopback
VLAN 1
ISID 1
VLAN 1
VLAN 11
 
Figure 19 provides a logical representation of these options. The left diagram represents the 
case of single-pass or inline routing. In these products, routing and bridging functions are fully 
integrated in the service domain in the exact same manner as they are integrated in the VLAN 
domain. For this reason, these products are represented with a router icon. 
The diagram in the middle represents the case of two-pass routing with an external physical 
loopback. In these products, routing and bridging functions are separate and represented by 
router and bridge icons. You can observe that the router function, where dots representing IP 
interfaces exist, connects to the bridge function using a VLAN port and a SAP. 
The right diagram illustrates the case of two-pass routing with internal front-panel loopback. 
As you can see, this case is almost the same to the case of two-pass routing with an external 
physical loopback from a logical standpoint. However, the routing function attaches to the 
bridging function using a single port or group of ports. This front-panel loopback port or group 
of ports still performs a SAP function and a VLAN function. In addition, this connection between 
routing and bridging functions is created internally in the switch ASIC and does not require an 
external cable.
Let’s review some configuration examples to commit these concepts.
Snippet 26. Single-pass or inline routing example

<<<PAGE 586>>>
28
Tech Brief
Shortest Path Bridging Architecture guide
The configuration snippet 26 shows that, in products supporting single-pass or inline routing, 
IP interfaces can be bound to services just like they can be bound to VLANs. The switch simply 
performs routing in the same domain (VLAN or Service) or between different domains (VLAN  
and Service). Note that the backbone and service configuration is not shown in this example.
Snippet 27. Two-pass routing with external physical loopback example
 
The configuration snippet 27 shows the equivalent configuration for products supporting two-
pass routing with external physical loopback. Since IP interfaces cannot be bound to a service 
directly, we create 2 additional “dummy” VLANs to bind these interfaces to. VLAN 11 will be 
associated to service 1 and VLAN 12 will be associated to service 2. The external physical 
loopback uses port 1/1/1 as VLAN port and port 1/1/2 as SAP. When creating the IP interfaces 
bound to those dummy VLANs, we use the rtr-port option. This prevents those VLANs from 
being bound to other ports and disables STP on those VLANs. Note that as explained previously, 
linkaggs can be used instead of single ports and linkagg member ports can span diverse units in 
a VC for redundancy.
Snippet 28. Two-pass routing with internal front-panel loopback example
 
The configuration snippet 28 shows the equivalent configuration for products supporting two-
pass routing with internal front-panel loopback. Firstly, port 1/1/51A is designated as the front-
panel loopback port. Dummy VLANs are created and SAPs linking those dummy VLANs to their 
associated services are defined on the loopback port. When creating the IP interfaces bound 
to the dummy VLANs, we use the rtr-port option and reference the loopback port. Once again, 
the example shows the case of single front-panel loopback port but linkaggs can be used for 
additional bandwidth and resiliency in the case of VC.

<<<PAGE 587>>>
29
Tech Brief
Shortest Path Bridging Architecture guide
11.  L3 services
A L3 service refers to a type of VPN service connecting multiple sites in a single any-to-any 
routing domain. Different sites utilize different subnets and require routing to communicate. 
For multi-tenancy, and to keep different customers isolated at L3, each customer service is 
associated to its own VRF instance.
Figure 20. Customer A’s L3 service
BEB1
BEB2
Site 1
10.0.1.0/24
.254
10.0.0.0/24
SPB Service A
VRF A
.254
.2
.1
Site 2
10.0.2.0/24
BEB3
BEB4
Site 3
10.0.3.0/24
.254
.254
.4
.3
Site 4
10.0.4.0/24
 
Figure 20 illustrates an example of a L3 Service connecting four of customer A’s sites: Sites 1 through 
4. You will notice that each site uses a different subnet and therefore, inter-site routing is required. 
BEB nodes connecting customer sites are represented with router icons for simplicity. These BEBs 
have a “LAN”-facing interface which acts as the local site default gateway, as well as a “WAN”-facing 
interface to reach remote sites. All “WAN” interfaces are bound to a single SPB service and are on the 
same “WAN” subnet. Lastly, all the LAN and WAN IP interfaces associated to customer A are bound  
to the same customer A VRF to provide L3 isolation between different customers.
SPB-based L3 VPN services rely on edge routing: Routing is only performed at ingress and egress 
BEBs and bridged between these. At L3, the WAN represents a single L3 hop regardless of the 
number of intermediate L2 hops (BCBs) in between. SPB simply bridges traffic from ingress BEB 
to egress BEB along the shortest path.
Up to this point, we have only described the DP. What about the CP? At the CP level, L3 VPN 
services come in two variants: VPN Lite and L3 VPN. Let’s elaborate on these two variants.
11.1  VPN Lite
A VPN Lite L3 Service is created by overlaying a L3 routing protocol on top of the L2 WAN SPB 
service. This routing protocol can be OSPF, BGP, or even static routing. The routing protocol runs 
inside the customer’s VRF and a separate instance and associated configuration is created for 
each customer. Figure 21 shows an example of how customer A’s L3 service can be created  
as a VPN Lite service by running OSPF on BEB nodes.
Figure 21. Customer A’s VPN Lite service
BEB1
BEB2
Site 1
10.0.1.0/24
.254
SPB Service A
VRF A
OSPF area 0
10.0.0.0/24
.254
.2
.1
Site 2
10.0.2.0/24
BEB3
BEB4
Site 3
10.0.3.0/24
.254
.254
.4
.3
Site 4
10.0.4.0/24

<<<PAGE 588>>>
30
Tech Brief
Shortest Path Bridging Architecture guide
We should highlight that, in a VPN Lite type of L3 service, the L2 SPB service simply provides 
L2 connectivity to the “WAN” IP interfaces. Continuing with OSPF as an example, this means that 
OSPF is configured as usual. Also, since all WAN IP interfaces are connected to a single L2 SPB 
service, in the case of OSPF, a DR/BDR election will take place as usual.
11.2  L3 VPN
SPB L3 VPN leverages the existing SPB IS-IS instance to carry customer VPN routes without 
requiring an additional routing protocol such as OSPF. This is accomplished with additional  
IS-IS TLVs extensions. We should note that each customer or tenant is still associated to its  
own VRF and IS-IS TLVs reference the customer’s ISID to preserve L3 isolation between different 
customers or tenants. This mechanism is described in an IETF draft [1]. Refer to figure 22.
For those familiar with MPLS or EVPN, those technologies rely on an IGP (for example; OSPF or 
IS-IS) for backbone node reachability, and MP-BGP (RFC 4760) for customer VPN route transport. 
In SPB L3 VPN, IS-IS can play both of those roles; backbone node reachability and customer VPN 
route transport. Using a single protocol instead of two, results in a network that is simpler to 
deploy and operate. 
In addition, when comparing SPB and MPLS, SPB BEB nodes play a role similar to MPLS PE nodes 
while SPB BCB nodes are similar to MPLS P nodes. In particular, SPB BCB nodes do not learn any 
customer VPN routes and require no VRFs to be created on them. VRFs need only be created on 
BEB nodes and customer VPN routes are only learnt on the BEBs that those customers connect to.
Figure 22. Customer A’s L3 VPN service
BEB1
BEB2
Site 1
10.0.1.0/24
.254
SPB Service A
VRF A
SPB IS-IS
10.0.0.0/24
.254
.2
.1
Site 2
10.0.2.0/24
BEB3
BEB4
Site 3
10.0.3.0/24
.254
.254
.4
.3
Site 4
10.0.4.0/24
 
Unlike the case of a VPN Lite, an SPB L3 VPN does not require the addition of any routing 
protocol. Customer’s VRF routes are exported to the SPB IS-IS instance, associated to the 
customer’s ISID, and bound to the WAN IP as a gateway address. Far-end BEBs will import those 
routes into their local VRF routing table. Therefore, those routes will point to the WAN IP address 
as next-hop. We should note that this mechanism is applicable and identical for both IPv4 and 
IPv6. This is illustrated in figure 23 from the perspective of BEB-1. We should note that route-
maps can be used for fine-grained route filtering.
Figure 23. Route Import/Export
BEB1
Site 1
10.0.1.0/24
.254
SPB Service A
VRF A
SPB IS-IS
10.0.0.0/24
Export local customer VRF routes to SPB IS-IS,
associate to customer’s ISID and bind to WAN address
Import far-end SPB IS-IS routes associated with the customer’s ISID
into the customer’s VRF and set the far-end WAN IP address as next hop
.1

<<<PAGE 589>>>
31
Tech Brief
Shortest Path Bridging Architecture guide
A L3 VPN service builds upon a L2 service and involves the following steps:
•	 Creating an L2 SPB service
•	 Creating a tenant VRF
•	 Creating LAN-side and WAN-side IP interfaces on the tenant VRF. LAN-side IP interfaces 
normally reside on a VLAN. WAN-side IP interfaces can reside directly on the SPB services 
itself on products supporting single-pass inline routing, or on a “dummy” VLAN on products 
requiring external physical or internal front-panel loopback.
•	 Binding the WAN IP interface to the L2 SPB service’s ISID
•	 Route import/export between local VRF routing table and SPB IS-IS ISID instance
Let’s go back to the sample topology used for L2 services in section 9 and configure a L3 VPN 
service so we can have a look at the configuration. We will look at devices supporting internal 
front-panel loopback.
Figure 24. L3 VPN service example
BEB3
BEB1
ISID 1002
VRF A
BVLAN 4002
192.168.30.0/24
.254
.254
1/1/48
1/1/48
1/1/48
.3
.1
Site 3
192.168.23.0/24
10.0.2.0/24
Site 1
192.168.21.0/24
BEB4
BEB2
.254
.4
.2
1/1/48
.254
Site 4
192.168.24.0/24
Site 2
192.168.22.0/24
 
We will now provide configuration snippets for all BEBs. Like their L2 counterpart, L3 VPN 
services require no configuration on BCBs. Let’s provide some details about this example:
•	 Customer sites connect to their local BEB though interface 1/1/48
•	 LAN-side, or site default-gateway IP interfaces are bound to VLAN 3001, which is the default 
VLAN on port 1/1/48
•	 Port 1/1/54A is designated as a loopback port
•	 WAN-side IP interfaces are bound to dummy VLAN 3100

<<<PAGE 590>>>
32
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 29. L3 VPN example – BEB-1
 
Snippet 30. L3 VPN example – BEB-2
 
Snippet 31. L3 VPN example – BEB-3

<<<PAGE 591>>>
33
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 32. L3 VPN example – BEB-4
 
Having created the L3 VPN service on all nodes, we can now proceed to verify it with show 
commands. Let’s start by verifying correct route import and export. Snippet 33 shows routes in  
BEB-1’s VRF “Customer_A”. Both local LAN and WAN subnets are LOCAL routes while far-end LAN 
subnets are IMPORT routes whose next hop gateway address is the WAN address of the remote BEB.
Snippet 33. L3 VPN example – Verifying route import/export
 
Snippet 34 shows arp entries in BEB-1’s VRF “Customer_A”. Far-end WAN gateway addresses are 
dynamically learnt.
Snippet 34. L3 VPN example – Verifying gateway L2 reachability
 
In addition to these L3-related verification steps, all steps covered in section 9 can be used to 
verify the underlying L2 service.

<<<PAGE 592>>>
34
Tech Brief
Shortest Path Bridging Architecture guide
11.3  VPN Lite versus L3 VPN
Having presented VPN Lite and L3 VPN, we can now discuss the pros and cons and provide 
guidelines to help you choose one versus the other.
Let’s start with the advantages of L3 VPN:
•	 Simplicity: L3 VPN does not require routing protocol configuration as it simply leverages the 
existing SPB IS-IS instance. VPN Lite on the other hand requires one routing protocol instance 
per tenant/VRF and BEB. For example, if using OSPF, 4 customer services spanning 8 BEB 
nodes require 4 x OSPF instances per node: A total of 32 x OSPF configurations across all 
nodes. In case dual stack IPv4 and IPv6 support is required, this translates to an OSPFv2 and 
an OSPFv3 instance per BEB and VRF: A total of 64 x OSPF configurations all nodes included. 
More routing protocol configurations result in longer service provisioning times and increased 
chances of making mistakes.
•	 Scalability: L3 VPN is significantly more efficient than VPN Lite from a CP point of view as it 
uses a single routing instance. This results in lighter CP load and allows for greater scalability 
than VPN Lite.
•	 Convergence: L3 VPN convergence can be faster than VPN Lite because it relies on a single 
protocol. VPN Lite convergence can be slower because the stacking of routing protocols has  
a compounding effect over convergence time: IS-IS must converge before OSPF can converge.
With such compelling arguments in favour of L3 VPN, you may wonder why anyone would 
choose to use VPN Lite instead. The reason is that, while L3 VPN is the recommended option 
within the SPB domain, L3 VPN relies on SPB IS-IS and cannot directly interoperate with external 
networks. This is where VPN Lite comes in. VPN Lite can be configured on border BEB nodes 
linking the SPB domain to external, non-SPB capable networks. These border BEB nodes use L3 
VPN to communicate with other BEB nodes and VPN Lite to interoperate with external non-SPB 
nodes through common routing protocols such as OSPF or BGPv4.
In short, L3 VPN is recommended within the SPB domain and VPN Lite is needed only on border 
nodes connecting to the outside world.
12.  Shared Services VPN and Route Leaking
In L3 VPN designs in which each VPN maps to its own VRF, it is common for certain services 
such as DHCP, DNS and Internet access to be shared across two or more of those VPNs. This  
can be implemented through VRF leaking.
Figure 25 shows the same familiar diagram that we have been using so far, but now with two 
customers, A and B. Each customer is associated to its own ISID (1002 for Customer A and  
1003 for Customer B) and VRF (Customer_A and Customer_B) on BEBs 1 through 4. Routes  
are propagated across the backbone as explained in section 11.2. 
Let’s now imagine that these customers need to also access some shared services and Internet 
access. An additional L3_VPN is created on BEB1 and BEB2, the “border” BEBs. These are 
the nodes that those shared services are accessed through. The “shared_services” L3VPN is 
associated to its own ISID (1004) and VRF (shared_services). Note that this L3VPN need not  
be stretched to BEBs 2 and 4. 
BEB1 and BEB2 can exchange routes with external entities, such as the firewalls, using a 
standard protocol, such as BGP4. Those routes can be leaked to customer A’s and B’s VRFs. In 
turn, customer A’s and B’s VRF routes can be leaked to the “shared_services” VRF. As a pre-
requisite, customer A’s and B’s address space must not overlap with each other nor with the 
shared services.

<<<PAGE 593>>>
35
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 35. Route leaking
 
Snippet 35 provides the commands required to accomplish this on the border BEBs, BEB1  
and BEB2.
We can summarize the process as below:
•	 Shared routes are exported from the shared_services VRF and into the global IP routing table. 
When doing so, a route-map filters routes such that only external routes are exported. This is 
to prevent re-export of routes imported from the other border BEB.
•	 Shared routes are imported from the global IP routing table and into the customer VRFs. Note 
that this step is only necessary if customer sites are connected to the border BEBs.
•	 Customer routes are imported from the global IP routing table and into the shared_services 
VRF. Note that this step is only necessary if customer sites are connected to the border BEBs.
•	 Remote customer routes are imported from the SPB IS-IS instance and ISID associated to those 
customers and into the shared_services VRF.
•	 Shared routes are redistributed from the shared_services VRF to the SPB IS-IS instance and 
ISIDs associated to customers. These routes will then be propagated across the backbone and 
imported into customer VRFs at remote BEBs.
Figure 25. Shared services
BEB3
SPB
IS-IS
BEB4
BEB1
Customer A
Site 3
Customer A
Site 4
Customer B
Site 3
Customer B
Site 4
Customer A
Site 2
Customer B
Site 2
Customer A
Site 1
Customer B
Site 1
BEB2

<<<PAGE 594>>>
36
Tech Brief
Shortest Path Bridging Architecture guide
13.  Automation
Up to this point, we have explained SPB concepts and configured the SPB backbone and 
services manually. However, AOS incorporates features that can build both the SPB backbone 
and services automatically. In this section, we will explain the various mechanisms that make a 
near zero-touch SPB network possible. A factory-default Alcatel-Lucent OmniSwitch has these 
mechanisms enabled by default and will automatically attempt to create an SPB backbone 
and services as explained in the subsequent subsections, unless these automation features are 
explicitly disabled. This set of features is sometimes referred to as “Intelligent Fabric” or “iFab” 
for short. In this section, we provide a simplified, high-level overview of these features. For a 
detailed description, please refer to the Alcatel-Lucent OmniSwitch Switch Management Guide.
13.1  Auto-Fabric
Figure 26 is a simplified view of a factory-default OmniSwitch bootup process. For a more 
detailed flow chart, please refer to the Alcatel-Lucent OmniSwitch Switch Management Guide.
This process involves the following stages:
•	 Auto Virtual Chassis (VC)
•	 Auto Remote Configuration Download (RCD)
•	 Auto LACP
•	 Auto SPB
•	 Auto MVRP
•	 Auto IP
Auto-Fabric features are enabled by default on a factory-default OmniSwitch. These features 
can however be disabled in their entirety, or, on a per-protocol or per-port basis. By default, 
automatically learnt and created configuration is not saved to the vcboot.cfg file but this option 
can be enabled.
Figure 26. Bootup state diagram
Fails or
succeeds with
AF enabled
As soon as IP
interface is up
if AF is enabled
Succeeds
with AF
disabled
Auto-RCD
Auto-IP
Auto-SPB
Auto-LACP
Auto-MVRP
Auto-VC
Link ﬂap
STOP
 
Let’s describe these stages one-by-one. 
13.1.2  Auto-VC
On bootup, and in absence of the vcsetup.cfg file, an OmniSwitch uses LLDP to detect other 
VC-compatible nodes connected to the default auto-VFL ports. Default auto-VFL ports depend 
on the product family. Some families such as the Alcatel-Lucent OmniSwitch® 6860 Stackable 
LAN Switch have 2 designated VFL ports which default to this role. In other families such as 
the Alcatel-Lucent OmniSwitch® 6900 Stackable LAN Switch, which support VC of up to 6 units, 
the last 5 VFL-eligible ports default to auto-VFL ports. If other products in the same family are 
detected at the other end, they will attempt to automatically create a VC. A Master node will 
be chosen through an election mechanism and non-Master nodes will reboot. Since this process 
creates a vcsetup.cfg file on all involved nodes, auto-VC will not kick-in in subsequent node 
reboot events.

<<<PAGE 595>>>
37
Tech Brief
Shortest Path Bridging Architecture guide
13.1.3  Auto-RCD
Next, and in absence of a vcboot.cfg file, an OmniSwitch attempts to obtain an IP address 
through DHCP on any of its operational non-VFL ports. It will try this using the untagged default 
VLAN and tagged VLAN 127 and it will retry three times. If the switch succeeds in obtaining 
an IP address, and depending on the DHCP options in the lease, the switch will subsequently 
attempt to fetch an instruction file from a TFTP server or it will contact the Alcatel-Lucent 
OmniVista® 2500 Network Management System. Next, the switch will attempt to download 
firmware and vcboot.cfg from either an FTP/SFTP server or OmniVista. If the switch succeeds  
at obtaining its firmware and configuration, it will reboot and load its configuration. Depending 
on the configured options, the switch may or may not continue with the subsequent stages. 
Please refer to the AOS Switch Management Guide and to [2] for further details.
13.1.4  Auto-LACP
All non-VFL ports are auto-LACP enabled by default. Auto-LACP kicks in on a factory-default 
switch or a non-factory-default switch, unless explicitly disabled. Auto-LACP can be disabled 
globally or only on specific ports.
During the auto-LACP stage, a switch uses LLDP to identify switches connected to auto-
LACP-enabled ports. Any LACP-compatible ports linking the same pair of switches will be 
automatically added to a linkagg. Even if there is only a single link connecting two nodes, it 
will still be configured as a linkagg because this allows additional links to be added later on 
without requiring configuration changes. For instance, by creating a linkagg of 1 member port 
and by referencing the (logical) linkagg as opposed to the (physical) port in other configuration 
commands, those configuration commands do not need to change when additional member  
ports are added to the linkagg. This is a best practice.
Note that, even if the remote switch is not an OmniSwitch, but is (manually) configured for LACP, 
the OmniSwitch detects LACP PDUs and automatically configures its side of the linkagg. This 
simplifies deployment even when 3rd party switches are used.
13.1.5  Auto-SPB
All non-VFL ports and linkaggs are auto-SPB enabled by default. Auto-SPB kicks in on a factory-
default switch or a non-factory-default switch, unless explicitly disabled. Auto-SPB can be 
disabled globally or only on specific ports or linkaggs.
Auto-SPB also uses LLDP to detect presence of SPB-capable switches. When an SPB-capable 
switch is detected, the switch will attempt to configure the port or linkagg as an SPB backbone 
interface. When doing so it will use certain defaults.
On switches running AOS release 8.7R1 and later these defaults are:
•	 BVLANs 4000 through 4003 are created and mapped to ECT IDs 1 through 4 respectively
•	 BVLAN 4000 is designated as the control BVLAN
If the switch succeeds in establishing at least one SPB adjacency, all remaining non-VFL and 
non-SPB backbone ports are automatically configured as auto UNP access ports, unless explicitly 
disabled. Please refer to section 13.3 for details on auto UNP access ports.
13.1.6  Auto-MVRP
Auto-MVRP is enabled on factory-default switches. On switches booting from a vcboot.cfg 
file however, this feature needs to be explicitly enabled. When auto-MVRP is enabled, and 
if the switch fails to establish any SPB adjacency, MVRP will be enabled on all remaining 
and operational non-VFL ports. This enables the dynamic instantiation of VLANs learnt from 
neighbouring switches.

<<<PAGE 596>>>
38
Tech Brief
Shortest Path Bridging Architecture guide
13.1.7  Auto-IP
The Auto-IP features runs in parallel with other features described in this section and, when 
enabled, it kicks-in as soon as an IP interface is created. Auto-IP listens for routing protocol 
(OSPFv2, OSPFv3 or IS-IS) “Hello” packets from neighbour devices and automatically creates local 
routing configuration matching parameters in the received “Hello” packets such that an adjacency 
can be formed. For example, reception of an OSPF “Hello” packet with area 1, Hello timer of  
5 and Dead timer of 20 will result in matching configuration on the local device such that the 
two devices become neighbours and an adjacency is established.
13.2  Dynamic SAPs
Up to this point, we have shown how to configure SAPs statically and manually. However, SAPs 
can be automatically and dynamically configured using the User Network Profile (UNP) feature  
in conjunction with authentication (802.1x, MAC) or classification rules (for example VLAN tag).
Dynamically-created SAPs can map traffic to a manually created service. Dynamically-created 
SAPs can also map traffic to a dynamically-created service for a fully dynamic configuration, 
which is covered in the next section.
Let’s analyse the sample configuration in snippet 36 . This example refers to the case of L2 
Services in which any required routing, such as default gateway, DHCP relay, is performed on a 
central node, which can be a switch or a Firewall. Either way, service and SAP configuration on 
the central L3 device is static. Dynamic configuration is useful at the edge nodes where client 
devices are added, moved, and changed on a regular basis.
Six UNP profiles named “EMPLOYEE”, “IoT”, “GUEST”, “WLAN”, “CCTV”, and “RESTRICTED” are 
created, each mapping to a different ISID. There are a total of four BVLANs, 4000 through 4003. 
BVLAN 4000 is reserved as control BVLAN and therefore services can be mapped to BVLANs 
4001 through 4003. As a result, each BVLAN carries traffic for two different services. These 
UNP profiles use head-end replication and have VLAN translation enabled; these are default 
behaviours which are explained elsewhere in this document.
So far, this describes the services but does not describe how ports or client devices will be 
mapped to those services. This mapping can be either static or dynamic. Let’s start by analysing 
the dynamic case. Ports 1/1/10 through 1/1/16 are defined as UNP “access” ports. This means 
that they map traffic to an SPB service, as opposed to a UNP “bridge” port which maps traffic to  
a VLAN. These ports utilise the “SAMPLE_FLOW” port template. This template is defined such that:
•	 802.1x supplicants are authenticated against the “UPAM” radius server. If successful, the 
radius server returns a “filter-id” attribute which matches one of the locally defined UNPs  
(for example; EMPLOYEE, IoT, among others). 
•	 As a fall-back mechanism for non-802.1x capable devices, such devices can use MAC 
authentication. If successful, the radius server also returns a “filter-id” attribute which  
matches one of the locally defined UNPs (for example; EMPLOYEE, IoT, among others).
•	 In both 802.1x or MAC authentication cases, it may happen that the radius server does not 
return a “filter-id” or that the returned “filter-id” value does not match any of the locally 
defined UNPs. In such case, those devices are bound to a “RESTRICTED” UNP. 
•	 The RESTRICTED UNP is also defined as the default UNP which is used in case of 
authentication failure. When bound to this RESTRICTED UNP, devices will receive an IP address 
through DHCP but will be very limited in their access to network resources. This is controlled 
at the central L3 node or firewall. This allows for these devices to have minimal network 
connectivity such that they can be onboarded (for example a digital certificate can be applied) 
and they can successfully authenticate next time they connect.
With this configuration in place, devices connected to ports 1/1/10 through 1/1/16 will be 
authenticated and dynamically bound to an SPB service according to their type or user identity. 
This means that the SPB service will automatically adapt and change as devices connect, 
disconnect, move, or otherwise change without manual intervention.

<<<PAGE 597>>>
39
Tech Brief
Shortest Path Bridging Architecture guide
In some cases, it may be necessary to statically bind these UNP services to a port. This is 
particularly useful if authentication is not used or when the device is a “silent” device. A “silent” 
device is a device that does not transmit traffic for extended periods of time because it goes into 
power-save mode for instance. These periods of inactivity can result in a loss of service binding, 
thus making the device effectively unreachable (for example for a WAKE-ON-LAN packet). This 
problem can be avoided by statically binding the UNP profile to the port. We have applied static 
UNP binding to ports 1/1/5 through 1/1/9 such that the service is statically bound to those ports 
even if the device disconnects or stops communicating for extended periods of time.
It should be noted that statically binding a SAP, as opposed to a UNP, also offers a solution to 
the silent device problem. However, by statically binding a UNP instead of a SAP, the exact 
same UNP constructs can be used for both silent and non-silent devices. This results in a more 
standardized configuration which is easier to create and maintain with fewer mistakes when 
configurations need to change. This is considered a best practice.
Snippet 36. Dynamic SAPs – L2 services

<<<PAGE 598>>>
40
Tech Brief
Shortest Path Bridging Architecture guide
Let’s analyse the L3 Service case for this example. What this means is that, rather than routing  
at a centralized switch or firewall, edge routing is performed. Furthermore, let’s consider the case 
of devices which attach to a standard VLAN port (for example not a SAP) and BEBs supporting 
front-end-panel loopback routing. Since VLAN-to-Service mapping happens at the loopback 
port, in this case we need to create bridge-type (VLAN) UNPs instead of access-type UNPs. 
The SPB configuration will be statically defined. Configuration snippets are split in three parts 
for convenience. Snippet 37 contains the VLAN-domain part of the configuration, snippet 38 
contains the IP-domain part of the configuration, and  snippet 39 contains the Service-domain 
part of the configuration. 
We should note that devices placed in the “RESTRICTED” role do not normally need to 
communicate with other such devices. However, the configuration snippet allows for all routes 
in the RESTRICTED VRF to be imported. This can be modified with the addition of a route-map 
permitting routes to a central BEB or firewall only. Furthermore, a policy list can be attached t 
o the RESTRICTED UNP definition such that those devices can only communicate with certain  
head-end resources and can only use certain ports or applications. We will leave this exercise  
for you to complete.
Snippet 37. Dynamic SAPs – L3 services – VLAN Domain

<<<PAGE 599>>>
41
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 38. Dynamic SAPs – L3 services – IP Domain
 
Snippet 39. Dynamic SAPs – L3 services – Service Domain

<<<PAGE 600>>>
42
Tech Brief
Shortest Path Bridging Architecture guide
13.3  Dynamic Services
In the preceding section, we explained how SAPs can be dynamically configured to accommodate 
mobile users and devices, and highly dynamic environments. This same mechanism is applicable 
to VMs in a data centre. As VMs are created, turned-on or off, or migrated from one hypervisor 
to another, SAPs can be automatically and dynamically created to adapt to those events on the 
fly without network manager intervention. 
For instance, classification rules can match VM traffic based on the VLAN tag (configured in the 
hypervisor) and create the required SAPs dynamically and automatically. This is a best practice 
compared to statically enabling all possible SAPs on all access ports because it reduces the 
broadcast domain footprint to only the required ports, thus eliminating unnecessary broadcast 
traffic and MAC learning.
However, with the features that we have described so far, even if the SAPs can dynamically 
adapt, this would require that the service UNP be manually created. In certain scenarios, the 
network administrator does not know the required parameters beforehand. For instance, the 
server manager may create, change, and delete VLANs on the hypervisor’s vswitch on a regular 
basis. It may be tempting to pre-provision services for all 4096 VLANs. But this is a poor practice 
as it creates an unnecessary load on the control plane. 
The best practice for that type of environment is to use AOS’ Dynamic Services feature. With 
Dynamic Services, UNPs can be dynamically created, on the fly, based on the VLAN tag seen on 
UNP ports. This feature is enabled by default on factory-default switches.
Upon receiving a frame on a UNP access port, the OmniSwitch automatically creates a dynamic 
SAP and a dynamic UNP profile defining the SPB service that traffic will be mapped to. Snippet 
40 provides an example of such a dynamically created UNP profile. The profile in the snippet is 
created upon reception of traffic tagged with VLAN 101. How does the AOS select the ISID and 
BVLAN to be used in the newly created service? It uses the formulas below where ‘%’ denotes 
the “modulo” division: the reminder of the integer division.
•	 ISID Number = Base Service Number + Domain ID + (VLAN Number % Service Modulo)
•	 BVLAN Index = ISID Number % (Total number of BVLANs)
By default:
•	 Base Service Number = 10,000,000
•	 Domain ID = 0
•	 Service Modulo = 512
Let’s also assume that BVLANs 4000-4003 are created and calculate the ISID and BVLAN  
number manually.
ISID Number = 10,000,000 + 0 + (101 % 512) = 10,000,000 + 101 = 10,000,101
BVLAN Index = 10,000,101 % 4 = 1
The formula does not provide the BVLAN number directly but the BVLAN index: the position  
in a BVLAN array sorted in ascending order where the lowest numbered BVLAN is in position 0  
and the highest numbered BVLAN is in position N-1. Therefore, in our example, with BVLANs 
4000-4003, BVLAN index 1 maps to BVLAN 4001. 
Snippet 40. Dynamic services – Dynamic UNP

<<<PAGE 601>>>
43
Tech Brief
Shortest Path Bridging Architecture guide
It is important to understand that with 4096 possible VLAN tags, using the default Service 
Modulo of 512 can result in up to 8 different VLAN tags being mapped to the same service. This 
is not the desired outcome most of the time because it will result in different VLAN traffic being 
bridged in the same L2 domain. To ensure L2 isolation, we can change the Service Modulo to 
4096 as shown in Snippet 41.
Snippet 41. Dynamic services – Dynamic UNP – Service Modulo
 
Let’s now focus on another parameter used in the ISID calculation formula: Domain ID. The 
Domain ID is useful in a multi-tenanted environment. For example, let’s consider a network 
providing services to three different customers: A, B, and C. These customers can use multiple 
VLANs and some of those VLANs may overlap. How do you ensure customer traffic isolation 
in the SPB domain? Isolation is achieved by creating a Domain ID for each customer and by 
the mapping customer’s UNI ports to the Domain. The example in Snippet 42 illustrates this 
configuration. Domains 1 through 3 are created for customers A through C. Ports 1/1/1-10 
connecting customer A’s devices are mapped to domain 1, ports 1/1/11-21 connecting customer 
B’s devices are mapped to domain 2, and so on. This configuration preserves customer isolation 
even when services and SAPs are dynamically and automatically configured on the fly in 
response to VLAN tags in incoming traffic.
Snippet 42. Dynamic services – Dynamic UNP – Multi-tenancy
 
Lastly, the Base Service Number (BSN) enables manual and dynamic service coexistence without 
conflict. Dynamically created services map to ISIDs greater than or equal to the BSN. Manually 
created services should use ISID numbers lower than the BSN.
14.  Management
As explained in section 3.6, SPB IS-IS is not an IP protocol. BCB nodes do not require IP 
interfaces. BEB nodes supporting L2 services only do not require IP interfaces either. BEB nodes 
require IP interfaces only when supporting an L3 service (for example, L3 VPN or VPN Lite). 
However, all SPB nodes whether BCB or BEB, require IP interfaces for management purposes. 
There are different ways of managing SPB nodes:
•	 Out of Band Management (OOBM): OOBM is applicable to any network architecture and will 
not be discussed further 
•	 Dedicated Management Service: An SPB service and VRF are dedicated to management. This 
is a good option if all nodes support single-pass inline routing. However, nodes that do not 
support single-pass inline routing will require an external physical or internal front-panel 
loopback for this purpose even if they would not require it otherwise (for example, because 
they are BCBs). 
•	 In-band Management: In-band management is applicable to all SPB nodes regardless of their 
routing capabilities (such as, single-pass inline, external physical, or internal front-panel 
loopback). Management IP interfaces can be created directly on the control BVLAN, therefore,

<<<PAGE 602>>>
44
Tech Brief
Shortest Path Bridging Architecture guide
no loopback of any kind is required. The management network or stations attach to one or 
more gateway nodes through VLAN-domain interfaces. We should note that IP interfaces 
created on the control BVLAN do not support configuration of any routing protocol or function 
(for example, OSPF or VRRP) and do not rely on ARP for IP-to-MAC resolution because there 
are no broadcasts on the SPB domain. IP-to-MAC mapping is resolved through IS-IS TLVs. IS-IS 
TLVs also carry management routes through the SPB backbone. VLAN-domain and SPB-domain 
management routes can be cross-redistributed at gateways nodes. The “spb-mgmt” protocol is 
associated to SPB-domain management routes.
Figure 27. In-band management
BEB3
1/1/1
1/1/1
BVLAN 4000
172.16.1.0/24
SPB IS-IS
Management VRF
172.16.0.0/24
OSPF area 0
BCB
BEB4
BEB1
BEB2
 
Let’s examine the in-band management example in figure 27. In this example, nodes BEB-1 and 
BEB-2 are gateways nodes linking the SPB-management domain and the VLAN-management 
domain. The VLAN-management subnet is 172.16.0.0/24 and the SPB-management subnet is 
172.16.1.0/24. OSPF is used in the Management network. Nodes BEB-1 and BEB-2 redistribute 
routes between OSPF and SPB-MGMT protocols. Route maps prevent circular route redistribution 
between these two protocols.
Snippet 43. In-band management – BEB-1
 
Snippet 44. In-band management – BEB-2

<<<PAGE 603>>>
45
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 45. In-band management – BEB-3
 
Snippet 46. In-band management – BEB-4
 
Snippet 47. In-band management – BCB
 
In-band management configuration examples are provided in snippets Snippet 43 through 
Snippet 47. OSPF and route-map configuration in BEBs 1 and 2 is excluded from these snippets.
15.  Operation and Maintenance
15.1  Connectivity Fault Management: 802.1ag
CFM in an SPB network is most useful to perform L2 trace and L2 ping for analysis and 
troubleshooting. Other aspects of CFM such as fault detection, which are important in PBB,  
are less important in SPB because SPB has an IS-IS control plane. These functions (CCM) are  
not currently supported in conjunction with SPB.
OAM is supported at the BVLAN level, refer to figure 28. Virtual MEPs must be configured for 
all BVLANs and BEBs and, optionally, also for BCBs (such that a L2 PING or L2 trace test can be 
initiated from any node to any other node). MIPs are automatically created and do not need to 
be explicitly configured.
Since there is no CCM function to map system names, link trace commands and output will 
reference the BMACs.
Figure 28. OAM in BVLAN and VLAN Domains
SPBM
BVLAN maintenance domain
V
MEP
V
MEP
(V)
MEP
(V)
MEP
MIP
MIP
MIP
VLAN maintenance domain

<<<PAGE 604>>>
46
Tech Brief
Shortest Path Bridging Architecture guide
OAM is also supported at the VLAN level or between L2 access switches connected to BEBs over 
SAP UNIs. This is useful in a L2 deployment for testing end-to-end service connectivity between 
sites. OAM at the VLAN level must be set at a higher maintenance domain level than BVLAN OAM.
Figure 29 shows a practical example of how OAM can be used to verify connectivity between 
BEBs by means of Loopback message (LBM) and loopback reply (LBR) and checking the route 
with link trace message (LTM) and link trace reply (LTR).
Figure 29. L2 ping and L2 trace
BEB
BCB
BCB
BEB
(V)
MEP
(V)
MEP
LBM
LBR
BEB
BCB
BCB
BEB
(V)
MEP
(V)
MEP
LTM
LTR
LTR
LTR
MIP
MIP
 
Configuration Snippet 48 provides a sample OAM configuration for service BVLANs 4001-4003. 
Snippet 48. OAM

<<<PAGE 605>>>
47
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 49 provides sample configuration and output for an L2 trace test. As shown in the 
snippet, the trace provides, among other elements, BMACs for all transit nodes as well as  
ingress and egress interfaces used. 
Snippet 49. L2 trace
 
15.2  Network performance: Service Assurance Agent 
Latency, jitter and packet loss SAA tests are automatically set-up between all BEBs and BCBs 
and across all BVLANs with the “saa auto-create” command. Refer to Snippet 50 showing the 
configuration and Snippet 51 showing sample statistics.
Snippet 50. Service Assurance Agent configuration

<<<PAGE 606>>>
48
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 51. Service Assurance Agent stats
 
15.3  Network maintenance
Two features in SPB can assist in network maintenance tasks: Overload state and graceful restart.
15.3.1  Overload state
SPB provides a graceful way to remove a node from service for maintenance and transition 
traffic to an alternate path (if there is one) with minimal disruption. This is the “overload state.”
Setting the overload state on the node will signal other nodes not to use it as a transit node and 
use alternate paths instead. This is similar to increasing the metric on all the links but is a much 
quicker way of achieving this outcome. Note, however, once the overload state is enabled on a 
node no traffic will transit through the node even if there are no alternative paths.
The overload state can be set indefinitely (until removed) or it can revert after a timer expires.
15.3.2  Graceful restart
SPB IS-IS supports graceful restart in a virtual chassis or physical chassis with redundant  
control modules. 
Without graceful restart, a VC master or CMM takeover event would require neighbour nodes 
to tear down and re-establish adjacencies with the restarting node and re-build the topology 
database, resulting in some disruption to traffic flows.
When graceful restart is enabled, and with the help of a neighbour node, the node undergoing 
a takeover will announce this condition to its neighbours by setting the RR (restart request) in 
a TLV message and continue using its existing FDB while restarting. The neighbour nodes will 
maintain their adjacencies with the restarting node during this process and send their complete 
LSP database information to the restarting node once the process is complete.
This makes the transition a much smoother process because disruption to traffic forwarding is 
minimized and the topology database is re-built in a much shorter time.
16.  Service attachment redundancy
When redundant links and nodes exist in the SPB domain, path computation in the event of a 
failure or restoration event is handled by the IS-IS protocol. But, access or Customer Edge (CE) 
devices connected to BEB nodes do not run SPB IS-IS and therefore other solutions are required 
when redundancy is needed. In this section we will present the different options for the different 
service types.
We start by highlighting that the simplest way of achieving redundant CE to BEB attachment 
is to use VC at the BEB and to attach the CE device to the BEB through a LAG. This redundancy 
option is applicable to any service type (L2 or L3).

<<<PAGE 607>>>
49
Tech Brief
Shortest Path Bridging Architecture guide
We will now present alternate redundancy options other than VC+LAG. 
Let’s start with L2 Services in figure 30 below. We can consider the following options:
•	 Non-redundant: The CE is attached to a single BEB through a single link. Link, BEB or CE 
failure will result in loss of service to the site
•	 Redundant links: The CE is attached to a single BEB through a link aggregate (LAG). This adds 
protection from single-link failure. Note that fibre runs should use diverse physical paths to 
protect against fibre cuts which would typically interrupt both links otherwise.
•	 Redundant links and nodes: The CE is attached to two different BEBs through two different 
links. This adds protection from BEB failure. When possible, both links should use physically 
diverse paths such that link failure events are not correlated. Dual-Home Link (DHL) is a high 
availability feature that provides fast failover without implementing Spanning Tree or Link 
Aggregation. Please refer to the “AOS 8 Network Configuration Guide” for further details. 
•	 Fully redundant: This option adds CE device redundancy. MSTP (Multiple Spanning Tree 
Protocol) can be used to avoid loops in this redundant connection. By default, SPB floods STP 
BPDUs messaging over SPB services. When using MSTP, different sites must use different 
MSTP regions to avoid creating a large MSTP region spanning all sites.
Note that Virtual Chassis (VC) can be combined with all the options above to increase resiliency.
Figure 30. L2 Service attachment
1. Non-redundant
SPB
2. Redundant links
SPB
BEB
DHL
CE
3. Redundant links and nodes
SPB
MSTP
4. Fully redundant
SPB
 
Let’s now continue with L3 services. We can distinguish two sub-variants: L3 CE and L2 CE. A L3 
CE can exchange routes with the BEBs by using any supported routing protocol as well as static 
or default routes. A L2 CE on the other hand will completely delegate routing to the BEB, which 
will act as a default gateway for local devices. These two sub-variants are illustrated in figure 31 
and figure 32. Note that hairpins, when required, are not shown for simplicity. 
L3 Service attachment with L3 CE options:
•	 Non-redundant: The site is attached to a single BEB through a single link. Link, BEB or CE 
failure will result in loss of service to the site.
•	 Redundant links: The site is attached to a single BEB through a link aggregate (LAG). This adds 
protection from single-link failure. Note that fibre runs should use diverse physical paths to 
protect against fibre cuts which would typically interrupt both links otherwise.
•	 Redundant links and nodes: The site is attached to two different BEBs through two different 
links. This adds protection from BEB failure. When possible, both links should use physically 
diverse paths such that link failure events are not correlated. A dynamic routing protocol such 
as OSPF is used between BEBs and CEs to exchange routing information. Import/Export and 
re-distribution of routes must be carefully planned to avoid circular re-distribution of routes. 
This is accomplished with route maps.
•	 Fully redundant: This option adds CE device redundancy

<<<PAGE 608>>>
50
Tech Brief
Shortest Path Bridging Architecture guide
Figure 31. L3 Service attachment - L3 CE
1. Non-redundant
SPB
2. Redundant links
SPB
BEB
CE
Routing
protocol
3. Redundant links and nodes
SPB
Routing
protocol
4. Fully redundant
SPB
Routing
protocol
 
You may notice that the case of L3 Service attachment with a L2 CE is almost identical to the 
case of L2 Service attachment. However, since the routing function is delegated to the BEB, 
VRRP is required when CEs attach to redundant BEBs. This requires access VLANs to be extended 
across both BEBs. If BEBs are directly connected, the access VLANs can be simply tagged on the 
link interconnecting both BEBs. However, if there is no direct connection between the BEB pair,  
a dedicated SPB service can be created to this effect. 
In addition, note that when using a L2 CE in a L3 Service, there is no routing protocol between CE 
and BEB. In such a case, the associated VRF can be configured as a “low profile” VRF. Low profile 
VRFs have routing capabilities restricted to static and/or imported routes, which is sufficient for 
such a situation. Low profile VRFs take up less BEB resources than “max profile” VRFs allowing 
for creation of more VRFs on the BEB.
As in the case of L2 Service attachment, all options can be combined with VC and LAG.
Figure 32. L3 service attachment - L2 CE
1. Non-redundant
SPB
2. Redundant links
SPB
BEB
CE
3. Redundant links and nodes
SPB
MSTP
4. Fully redundant
SPB
DHL
VRRP
VRRP

<<<PAGE 609>>>
51
Tech Brief
Shortest Path Bridging Architecture guide
17.  Loop avoidance and suppression
In the CP, loops are avoided with IS-IS, a link-state routing protocol. In the DP, a node will not 
accept unexpected frames from its neighbours.
However, short-lived transient loops may form in the event of a topology change and until 
network convergence is attained. Loops pose a serious threat to the network stability. 
In the DP, SPB incorporates an additional loop mitigation technique to detect and break these 
transient loops:
•	 Reverse-path Forwarding Check (RPFC): RPFC exploits SPB’s symmetry and congruence 
properties. RPFC verifies that incoming traffic’s source BMAC is indeed reachable over the 
ingress interface according to the local FDB and discards non-conforming frames. 
In addition, the SPB backbone must be protected from loops that may be created due to failures 
and misconfiguration at the VLAN-domain access layer. By default, SAPs forward STP BPDUs 
allowing redundantly-attached VLAN-domain access layer to use STP for loop prevention. 
There is always a chance however that STP may be misconfigured, fail, or not be enabled at all. 
Configuration faults in customer networks can result in loops spanning both the SPB backbone 
and customer access network. This can result in broadcast storms. To protect the SPB backbone 
from broadcast storms, loops involving SAPs must be detected and broken. 
AOS supports an additional loop mitigation mechanism to detect and break access layer loops: 
Loopback Detection (LBD). LBD can detect and protect the backbone network from forwarding 
loops created at the VLAN-domain customer-access layer. LBD operates in addition to other 
mechanisms such as DHL or STP. When a loop is detected, the port is disabled and goes into a 
shutdown state. A trap is sent and the event is logged.
The switch periodically sends out LBD frames from LBD-enabled ports and concludes that the 
port is looped back if it receives the frame on any of the LBD-enabled ports.
LBD can be used on both VLAN UNI and SAP UNI ports. In the case of SAP UNI ports, LBD frames 
will be sent on all SAPs because different access VLANs may have different logical topologies. 
However, if a loop is detected on a SAP, the entire physical port will be shut down. 
LBD should be enabled on all UNI ports.
Figure 33 illustrates situations in which LBD can detect and break loops.
Figure 33. Loopback detection
SPB
Port in switch with highest
BridgeID is shut down
BEB-A
BEB-B
SPB
Port in switch with highest
BridgeID is shut down
BEB-A
BEB-B
SPB
Port in switch with highest
PortID is shut down
BEB-A
BEB-B
 
By default, LBD is disabled for the switch and on all service-access ports. Enable LBD globally  
on the switch and in specific service-access ports or linkaggs as shown in Snippet 52.

<<<PAGE 610>>>
52
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 52. Loopback detection
 
AOS incorporates storm control through flood rate limiting of broadcast, multicast and unknown 
unicast traffic. A high threshold rate is configured in megabits-per-second (mbps), packets-per-
second (pps), or as a percentage of the port speed. When the threshold value is reached, packets 
are dropped or, the port is shutdown. Storm control is enabled by default with pre-defined rates. 
Please refer to the AOS Network Configuration Guide for further details.
18.  General design guidelines
Design guidelines have been provided throughout this document. In this section, we provide 
additional design guidelines to assist the network architect in designing SPB networks.
18.1  BVLANs
As described in section 5, SPB networks load balance traffic on a per-service basis. This load 
balancing is achieved by mapping different services to different BVLANs. An SPB network 
supports up to 16 BVLANs, however, most real-world physical topologies do not support 16 
equal-cost-paths. There is no advantage in creating more BVLANs than the number of equal-cost-
paths in the physical topology. Moreover, since a SPT must be computed for each BVLAN, having 
more BVLANs than equal-cost-paths in the physical topology creates an additional unnecessary 
load in the CP which results in increased resource utilization and convergence times. 
In short: Only create as many BVLANs as there are equal-cost-paths in the physical topology. As 
of AOS 8.7R1 and later releases, only four BVLANs are created by default when using auto-SPB.
18.2  VLAN-to-Service mapping
When creating a SAP, AOS allows mapping multiple or all VLAN tags to the same SPB service.  
We want to stress that, as a general guideline, to preserve L2 isolation between VLANs, different 
VLANs should be mapped to different services (for example, through different SAPs).
Mapping different VLANs to the same SPB service makes inter-VLAN bridging possible, thus 
defeating the purpose of having different VLANs in the first place.
In addition, there is a risk of having duplicate MAC addresses. In theory, there should be no 
duplicate MAC addresses; in reality, it can happen, particularly in virtualized environments. 
Duplicate MAC addresses in different VLANs do not collide, however, if these VLANs are mapped 
to the same SPB service and the client devices are connected to different SAPs, those MACs will 
be constantly learned, re-learned and flushed. This is known as a “mac-move” and should be 
avoided to maintain stability. To avoid mac-move, we strongly recommend mapping different 
VLANs to different SPB services (ISIDs). This will require one SAP and ISID per access VLAN.
There are some situations in which mapping different VLANs to the same SPB service (ISID) is 
acceptable, but we will not elaborate on those situations. 
In short: As a general guideline, map different VLANs to different SPB services by using specific 
SAPs for each VLAN.

<<<PAGE 611>>>
53
Tech Brief
Shortest Path Bridging Architecture guide
18.3  Virtual Chassis
Virtual chassis (VC) is a feature that combines multiple “stackable” switches into a single logical 
“virtual chassis” such that each physical switch becomes a virtual “slot” in the virtually modular 
chassis. A virtual chassis is a single logical entity managed as one device and with single control 
and management planes.  
Virtual chassis provides many benefits such as network architecture and management 
simplification. VC greatly simplifies redundant service attachment. Customer CE access devices 
can be dual-homed to diverse slots in a BEB through a link aggregate. This eliminates the need  
to configure other L2 or L3 redundancy mechanisms such as DHL or VRRP.
When using virtual chassis in the SPB backbone, logical link aggregates (LAGs) are recommended 
to interconnect the VC to all its SPB neighbours such that one member (physical) port connects 
to every slot in the VC as seen in figure 34. This is not mandatory but is recommended and will 
improve the network convergence time in the event of slot failure because the need to update 
tables during the control plane takeover is greatly reduced. In addition, dual homing nodes to 
a VC reduces the need to forward traffic across the VFL because traffic forwarding in a LAG 
prioritizes the use of local linkagg member ports over remote (across the VFL) member ports.
Figure 34. VC and SPB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
 
18.4  Link Aggregation
Combining multiple physical links into a LAG improves resiliency and increases total available 
bandwidth on the logical link.
In a LAG, traffic is load balanced across member ports in one of two ways:
•	 MAC hash (brief mode)
•	 IP + TCP/UDP port hash (extended mode)
However, SPB backbone ports use MAC-in-MAC encapsulation which means MAC addresses are 
the BMACs of BEB and BCB nodes while IP addresses and port numbers are not visible to the 
hashing logic. In most cases this does not create enough entropy and the load will not be spread 
evenly across all different physical links.
Since AOS 8.3.1R01, a “tunnel-protocol” option can be selected such that the hashing can use 
CMACs or IP addresses + TCP/UDP ports.
It is recommended that this option be enabled on all SPB nodes using LAG. The choice of MAC 
(brief) or IP+TCP/UDP ports (extended) is a global setting which will apply to all LAGs. Please 
refer to the AOS Command Line Interface Guide for further details.

<<<PAGE 612>>>
54
Tech Brief
Shortest Path Bridging Architecture guide
18.5  Link Metric
SPB uses the link metric as a measure of a link’s cost to reach another node. By default, all link 
metrics are set to 10 regardless of link speed. The link metric is an integer in the 1-16M range.
The link metric can be adjusted to influence the SPT calculations. For instance, the metric can be 
changed to reflect the link speed. It should be noted that the metric must be adjusted on both 
sides of a link. Nodes will become adjacent even when the metrics are different, but the highest 
metric will be used in the SPT calculations.
Changing the link metric to reflect the link speed will help steer traffic towards links with 
higher capacity and away from lower capacity ones, making the best use of the total available 
bandwidth and improving performance. Table 3 shows a way in which the metric can be set to 
be inversely proportional to the link speed.
Table 3. Recommended Link Metric
Speed 
Suggested Metric 
100G 
1000 
50G 
2000 
40G 
2500 
25G 
4000 
10G 
10000 
1G 
100000 
100M 
1000000
18.6  QoS
In an SPB network, traffic is classified at the SAP and the classification does not change as traffic 
traverses the backbone and until it exits through another SAP at the destination BEB.
Trusted SAPs copy CoS markings from the incoming VLAN tag onto the BVLAN tag. If incoming 
traffic is not tagged, then the port’s default priority is used. Un-trusted SAPs set the CoS 
markings to a user-defined value.
No further classification based on inner L2-L4 conditions is possible within the SPB backbone 
due to the MAC-in-MAC encapsulation.
When using an external or two-pass routing (external physical or internal front-panel loopback), 
the standard VLAN port must best set to trust and use CoS and not DSCP to preserve CoS 
markings end-to-end.
19.  Security guidelines
In this section, we will provide some additional design guidelines specific to the security domain. 
This is not an exhaustive list of recommendations, rather, we will focus on certain guidelines 
specific to SPB deployments. We will go through different AOS features and how they can be 
used to improve security in an SPB network. Other more general security guidelines can be 
found in [3].

<<<PAGE 613>>>
55
Tech Brief
Shortest Path Bridging Architecture guide
19.1  Management VRF
As explained in section 3.6, SPB relies on a non-IP protocol for path computation. For this reason, 
BCB nodes and BEB nodes supporting L2 services only do not require an IP address. The only 
case in which an SPB node requires an IP address is the case of a BEB node supporting a L3 
service or feature such as L3 VPN, VPN Lite, or VRRP, among others.
We have covered different SBP management options in section 14. Management IP addresses 
can be bound to:
•	 The EMP port, in case of OOBM
•	 To a standard VLAN port, in the case of OOBM
•	 The control BVLAN, in the case of in-band management
•	 A Management SPB service, directly in the case of products supporting single-pass  
inline routing
•	 A Management SPB service, indirectly in the case of products supporting external physical  
or internal front-panel loopback
We want to point out that no matter what management option is chosen, management IP 
addresses should use a different VRF from the VRF used for service or customer traffic. This 
is already the case when using the EMP port for OOBM. One possibility is creating a dedicated 
management VRF and enabling the required management protocols on this VRF as shown in 
Snippet 43 through Snippet 47.
Another possibility is using the default VRF for management, under the condition of not using  
it for anything other than management.
19.2  MACSec
Data integrity and confidentiality must be protected while in transit through the network. 
MACSec is an IEEE standard (802.1AE) which provides point-to-point authentication and optional 
encryption between MACSec-capable devices such as switches. MACSec can prevent various 
threats such as man-in-the-middle, sniffing, spoofing, and playback attacks.
Because MACSec operates at the MAC layer, it transparently secures all upper layer traffic 
transiting through MACSec-enabled links. This includes both application-layer data, as well 
as control-plane and management-plane communication. In addition, unlike IPSec, MACSec is 
implemented in hardware at wire-speed and does not introduce additional latency or bandwidth 
limitations.
19.3  NAC
In section 13.2, we explained how users and devices can be dynamically mapped to their 
services based on their identity. Enabling authentication on every front-panel port ensures only 
authorized users and devices can access network services. One additional benefit of creating 
dynamic SAPs through NAC is that no service is instantiated on a BEB until an authorized user 
successfully authenticates and is mapped to the service: The service is instantiated on demand. 
This is an additional layer of security compared to static SAPs because no service is connected  
if no authorized user is connected. It is clearly more difficult to hack, attack, or otherwise disrupt 
a service when it is not even connected. 
19.4  Router authentication
As explained in section 11.1, an SPB network can exchange routes with external non-SPB entities 
by using the VPN Lite feature. This means that one or more SPB BEB nodes will run a routing 
protocol such as OSPF or BGP with external entities. Any learnt route may be imported into the 
SPB backbone and propagated to other BEB nodes by way of IS-IS TLVs.

<<<PAGE 614>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license  
by ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.
com/en/legal/trademarks-copyright. All other trademarks are the property of their respective owners.  
The information presented is subject to change without notice. Neither ALE Holding nor any of 
its affiliates assumes any responsibility for inaccuracies contained herein. © Copyright 2021 ALE 
International, ALE USA Inc. All rights reserved in all countries. DID21040501EN (April 2021)
This creates an opportunity for a bad actor to inject malicious routes and poison the routing 
table to carry out DoS, MITM, or other attacks.
This risk can be mitigated by enabling routing protocol authentication (e.g. MD5 for OSPF or BGP).
20.  Conclusion
Shortest Path Bridging is a powerful technology yet simple when compared to others such as 
MPLS or EVPN. SPB is broadly supported across the Alcatel-Lucent OmniSwitch portfolio with 
products in multiple formats, from stackable to modular chassis and even industrial-grade 
ruggedized variants. This product breadth, coupled with SPB’s service-oriented framework, 
results in a network architecture that can deliver the required service to the right location  
with minimal network configuration changes, or even in a fully automated manner.

<<<PAGE 615>>>
CONSOLE CONNECTIONS
ALE NETWORK PRODUCTS

<<<PAGE 616>>>
Console Server
Straight UTP cable
Console Server
Console Server
OS6900 CONSOLE
OS6900 T20/T40/X20/X40 
@ 9600 Baud Rate
USB A
console
Straight UTP cable
RJ45 to DB9 Female 
Serial to USB 
RJ45
console
OS6900 X72/Q32 
@ 9600 Baud Rate
Straight UTP cable
RJ45 to DB9 Female 
Serial to USB 
OS6900 
V72/C32/X48C6/T48C6/V48C8
@ 115200 Baud Rate
RJ45
console
RJ45 to DB9 Female 
Serial to USB 
RJ45 to DB9 Female 
OS6900-USB-RJ45
OS6900-USB-RJ45
* Connections to Console servers may need Straight or Roll-over UTP cable depending on Console Server model
Comes in the box
Comes in the box
Comes in the box
Comes in the box
Male-Male DB9 Adapter

<<<PAGE 617>>>
OS6900 CONSOLE
OS6900 T20/T40/X20/X40 
@ 9600 Baud Rate
USB A
console
RJ45
console
OS6900 X72/Q32 
@ 9600 Baud Rate
OS6900 
V72/C32/X48C6/T48C6/V48C8
@ 115200 Baud Rate
RJ45
console
Console Roll-over cable  with USB Type A
Console Roll-over Adapter
Console Roll-over cable  with USB Type C
Console Roll-over Adapter
OR
OS6900-USB-RJ45
Comes in the box

<<<PAGE 618>>>
Console Server
OS6860 CONSOLE
OS6860/OS6860E
@ 9600 Baud Rate
Micro USB
console
Straight UTP cable
RJ45 to DB9 Female 
Serial to USB 
OS6860N/OS6870
@ 115200 Baud Rate
* Connections to Console servers may need Straight or Roll-over UTP cable depending on Console Server model
Micro USB to DB9
Console Server
Straight UTP cable
RJ45 to DB9 Female 
Serial to USB 
OS6860-RS232CBL
Micro USB
console
Needs to be 
ordered separately
Male-Male DB9 Adapter

<<<PAGE 619>>>
OS6860 CONSOLE
Console Roll-over cable  with USB Type A
Console Roll-over Adapter
Console Roll-over cable  with USB Type C
OR
OS6860/OS6860E
@ 9600 Baud Rate
OS6860N/OS6870
@ 115200 Baud Rate
OS6860-RS232CBL
Needs to be 
ordered 
separately
Requires installation of a driver on PC
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers
OR
Micro USB
console
Console Roll-over Adapter
OS6860-RS232CBL
Needs to be 
ordered 
separately
Comes in the box
Micro USB
console

<<<PAGE 620>>>
Console Server
OTHER SWITCHES
RJ45
console
Straight UTP cable
RJ45 to DB9 Female 
Serial to USB 
OS6900-USB-RJ45
* Connections to Console servers may need Straight or Roll-over UTP cable depending on Console Server model
Comes in the box
Legacy/New Switches 
@ 9600 Baud Rate
6350
6360
6450
6465
6560
6570M
6850
6855
6865
9900
10K
Console Roll-over cable  with USB Type A
Console Roll-over cable  with USB Type C
Console Roll-over Adapter

<<<PAGE 621>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 622>>>
I N T E L L I G E N T FA B R I C
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 623>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the auto fabric feature
• Mount automatically a Virtual Chassis
• Mount automatically a LACP
• Automate the Routing, SPB, MVRP

<<<PAGE 624>>>
• Discover SPB neighbor
• Pre-defined defaults
• If not established configuration deleted & disabled
AUTO-FABRIC - PLUG-N-PLAY ZERO TOUCH DEPLOYMENT
1- Auto-VC
2- Automatic remote configuration
3- Auto-LACP 
4- Auto-Routing
5- Auto-SPB Fabric
6- Auto-Network Profiling 
7- Auto-MVRP
• First time bootup
• Elements of same family discovered
• Virtual Chassis created
• Download remote configuration
• Discover LACP
• Discover OSPF & IS-IS
• IP interface must exist
• Neighbor relationship must establish
• Pre-defined defaults
• If not established configuration deleted & disabled
• If fabric successful, user & network port profiles creation
• Enable VLAN propagation with MVRP

<<<PAGE 625>>>
AUTO-FABRIC - START UP
Switch Power on
Or reload without any config file
Starting 6900 Boot Process
Mount /dev/sda1
FS is EXT2
Do you want to disable auto-configurations on this switch [Y/N]?
N
Auto-Configurations enabled
Preparing Flash..
10s
N
If no response or input is [N], then it is assumed to be false.
Meaning to use auto-VC, RCL and auto-fabric
Y
If input is [Y] then auto-VC, RCL and auto-fabric are disabled

<<<PAGE 626>>>
AUTO-VC
• Auto VFL
• Auto VFL Default ports
• Auto Chassis ID
• Auto vs Static
• Demo License enabled by default
Valid Advanced or 
Demo license
boot.cfg
exists?
vcsetup.cfg
exists
VC Mode
• VFL: Auto or Static
Standalone Mode
VC Mode
• Auto VFL
• Auto Chassis ID
Y
Y
N
N
Y
N
1- Auto-VC

<<<PAGE 627>>>
AUTO VFL FEATURE – AUTO VFL PORTS
1
Auto VFL Ports
10G and 40G
No copper
Auto VFL Detection Process
Automatically detect whether an 
auto VFL port can become VFL
2
Assign VFL ID
3
Aggregate 
multiple auto 
VFL ports
Assign VFL ID automatically
OS6900: id= 0, 1, 2, 3, 4, 5
Aggregate Auto VFL ports in aggregate 
N
Auto VFL process runs only on port explicitly configured 
as auto VFL port in vcsetup.cfg or runtime configuration
Y
OS6900-X / T
• Last 5 ports of each chassis
• Including ports in expansion slots
• Regardless of SFP+/QSFP presence on those ports 
OS6900-Q32
• Last 5 ports of each chassis
• In case of 4x10G splitter cables is used
• Ports with 4x10G splitter is counted as 4 ports
• Ports with 40G QSFP are counted as 1 port
• Ports with no SFP+/QSFP are counted as 1 port
vcsetup.cfg
exists

<<<PAGE 628>>>
AUTO-VC - AUTO-CHASSIS ID
• Auto Chassis ID selection only occurs when there is no vcsetup.cfg
• Master selection is then run based on lowest MAC address
• Upon receiving their new chassis ID, non master units reboot and apply their new ID
• In case of a new chassis insertion, Master Chassis assigns the chassis id of the new member
vcsetup.cfg
! Virtual Chassis Manager:
virtual-chassis chassis-id 1 configured-chassis-id 1
virtual-chassis vf-link-mode auto
virtual-chassis auto-vf-link-port 1/1/31A
virtual-chassis auto-vf-link-port 1/1/32A
virtual-chassis auto-vf-link-port 1/1/32B
virtual-chassis auto-vf-link-port 1/1/32C
virtual-chassis auto-vf-link-port 1/1/32D
virtual-chassis chassis-id 1 chassis-group 77

<<<PAGE 629>>>
INTELLIGENT FABRIC
AUTOMATIC REMOTE CONFIGURATION
• RCL is run after Auto VC, and before the rest of Auto Fabric 
• May result in no Auto Fabric being run depending on the RCL result
• May be used to enhance Auto Fabric
• The linkagg created by the RCL will be retained for use later and not modified by regular Auto 
Linkagg
• RCL tries 6 times, 3 each on VLAN 1 and 127 to get DHCP and download instruction file
• To cancel RCL, run command “auto-config-abort”
• At the end of RCL, if a vcboot.cfg is downloaded, the box will be reset
• Auto Fabric will only run if the config file has the commands to do so
2-Auto-Predefined config template

<<<PAGE 630>>>
INTELLIGENT FABRIC  - AUTOMATIC FABRIC PROTOCOLS 
3- Auto-LACP 
4- Auto-Routing
5- Auto-SPB Fabric
6- Auto-Network Profiling 
7- Auto-MVRP

<<<PAGE 631>>>
AUTO-DISCOVERY - AUTO-LACP
• LLDP enhancement
• Propriatery TLV used to detect the peer and, in return, receive peer’s system ID
• If LACP negotiation succeeds, form a link aggregation on a detected set of ports
3- Auto-LACP 
-> show linkagg port
Chassis/Slot/Port  Aggregate  SNMP Id  Status    Agg  Oper
Link  Prim
-----------------+----------+--------+----------+----+-----+-----+-----
1/1/1C     Dynamic      1003  ATTACHED  127   UP    UP
NO 
2/1/15     Dynamic    101015  ATTACHED  127   UP    UP
NO
3/1/14     Dynamic    201014  ATTACHED  127   UP    UP
YES
! Link Aggregate:
linkagg lacp agg 127 size 16 admin-state enable 
linkagg lacp agg 127 actor admin-key 65535
linkagg lacp port 1/1/1c actor admin-key 65535
linkagg lacp port 2/1/15 actor admin-key 65535
linkagg lacp port 3/1/14 actor admin-key 65535
vcboot.cfg

<<<PAGE 632>>>
AUTO-DISCOVERY - IP AUTO PROTOCOL CONFIGURATION
• Supports IP protocols (OSPFv2, OSPFv3, IS-IS)
• IP Interface or VRF configuration is not
concerned
• DHCP, RCL or user configuration CLI 
• Active during and after the normal auto fabric 
discovery time
• Runs in parallel with no interdependency
• Can be started by the following
• No boot.cfg (out of box)
• Auto fabric discovery started by CLI or boot.cfg 
• IP auto protocol started by CLI or boot.cfg
• Protocol network configuration is learned
through Hello packets
• Determine area, area type, and timers
• Protocols are loaded when the first valid hello is 
received
• Configure the critical parts in order to form 
adjacencies and share routes
• Will automatically create route-maps to redistribute 
local subnet routes into OSPF/ISIS as internal routes
4- Auto-Routing
! IP Route Manager:
ip static-route 135.118.225.0/24 gateway 172.25.167.193 metric 1
ip route-map "auto-configure" sequence-number 50 action permit
ip route-map "auto-configure" sequence-number 50 set metric-type internal
ip redist local into ospf route-map "auto-configure" admin-state enable
vcboot.cfg

<<<PAGE 633>>>
AUTO-DISCOVERY - AUTO SPB FABRIC
• SPB configuration
• To apply a set of default SPB Backbone port 
configuration on a port or aggregate (configured
during LACP phase)
• Network port configuration
• If adjacencies not formed during 4 Hello intervals
(4x9 sec) – NOT a part of SPB
• Default SPB configuration
• BVLANs 4000-4015 mapped to ECT-IDs 1-16 
respectively
• Control BVLAN: 4000 
• Bridge priority: 0x8000
vcboot.cfg
5- Auto-SPB Fabric
-> show vlan
vlan
type   admin   oper
ip
mtu
name
------+-------+-------+------+------+------+------------------
. . . . 
14     dyn
Ena
Ena
Dis
1500    VLAN 14
15     dyn
Ena
Ena
Dis
1500    VLAN 15
200    std       Ena
Ena
Ena
1500    VLAN 200
4000   spb
Ena
Ena
Dis
1524    AutoFabric BVLAN
4001   spb
Ena
Ena
Dis
1524    AutoFabric BVLAN
4002
spb
Ena
Ena
Dis
1524    AutoFabric BVLAN
. . . 
! VLAN:
spb bvlan 4000-4015 admin-state enable
spb bvlan 4000-4015 name "AutoFabric BVLAN"
mac-learning vlan 4000-4015 disable
! SPB-ISIS:
!spb isis bvlan 4000 ect-id 1
spb isis bvlan 4001 ect-id 2
spb isis bvlan 4002 ect-id 3
spb isis bvlan 4003 ect-id 4
spb isis bvlan 4004 ect-id 5
spb isis bvlan 4005 ect-id 6
spb isis bvlan 4006 ect-id 7
spb isis bvlan 4007 ect-id 8
spb isis bvlan 4008 ect-id 9
spb isis bvlan 4009 ect-id 10
spb isis bvlan 4010 ect-id 11
spb isis bvlan 4011 ect-id 12
spb isis bvlan 4012 ect-id 13
spb isis bvlan 4013 ect-id 14
spb isis bvlan 4014 ect-id 15
spb isis bvlan 4015 ect-id 16
spb isis control-bvlan 4000
spb isis interface linkagg 127
spb isis admin-state enable

<<<PAGE 634>>>
AUTO-DISCOVERY - AUTO-NETWORK PROFILING 
• Access port configuration 
• User profiles creation
• Single service
•
Defines a single service SAP binding that will accept 
untagged frames
• Auto VLAN service
• Automatically generate SAP bindings for the VLANs 
concerned by the traffic coming on port as well as a 
default untagged service by default
6- Auto-Network Profiling

<<<PAGE 635>>>
AUTO-NETWORK PROFILING - LOOPBACK DETECTION
• Eliminate the formation of data loops that are created by people attaching networks  or 
devices to multiple access ports that offer an open path for data to flow between the 
access ports
• Edge loop detection available on service access interfaces and LACP links
• Even in case of the absence of other loop-detection mechanisms like STP/RSTP/MSTP 
• LBD transmits periodic proprietary Multicast MAC frames on the LBD enabled ports
• Loop detected when receive the frame back on any of the Loop-back detection enabled port
• Port is disabled (forced down)
• Error Log is issued
• SNMP trap
• Can be re-enabled by user

<<<PAGE 636>>>
AUTO-NETWORK PROFILING - LOOPBACK DETECTION
• Loop Back Detection for SPB-M access ports
• LBD frames extended for Service Access ports
• ISID
•
Detect loops on a per ISID basis
•
Topology of services and VLANs vary from access port to access port
•
More LBD frames may be sent per port depending on SAP binding 
• Port Path Cost
• Ability to block the slower port
! Loopback Detection:
loopback-detection enable
loopback-detection service-access port 2/1/1 enable
loopback-detection service-access port 3/1/1 enable
vcboot.cfg

<<<PAGE 637>>>
LOOPBACK DETECTION- SERVICE ACCESS PORT
OS6900
OS6900
SPB Network
L2 switch
• 1/2 and 2/2 are SAP ports having same ISID and path cost
• Loopback-detection is enabled with option ‘service-access’ on ports 
1/2 and 2/2
• Traffic loops through 1/2 and 2/2
• Port 2/2 is shutdown in case B has higher bridge identifier, since 1/2 
and 2/2 has equal path costs
AOS Switch with
Loopback-detection 
enable
Legacy or non AOS 
switch
2/1
1/1
1/2
2/2
OS6900
OS6900
SPB Network
L2 switch
• 1/2 and 1/3 are SAP ports having same ISID and path cost
• Loopback-detection is enabled with option ‘service-access’ on ports 1/2 
and 1/3
• Traffic loops through 1/2 and 1/3
• Port 1/3 is shutdown as this  interface has higher port identifier, since 
1/2 and 1/3 has equal path costs
AOS Switch with
Loopback-detection enable
Legacy or non AOS 
switch
2/1
1/1
1/2
1/3

<<<PAGE 638>>>
AUTO-DISCOVERY - AUTO MVRP
• MVRP  enabled globally after LACP and SPB discovery process
• Spanning Tree mode switch to flat
7- Auto-MVRP
-> show vlan
vlan
type   admin   oper
ip
mtu
name
------+-------+-------+------+------+------+------------------
. . . . 
11      dyn
Ena     Ena
Dis    1500    VLAN 11
12      dyn
Ena     Ena
Dis    1500    VLAN 12
13      dyn
Ena     Ena
Dis    1500    VLAN 13
14      dyn
Ena     Ena
Dis    1500    VLAN 14
15      dyn
Ena     Ena
Dis    1500    VLAN 15
200     std       Ena     Ena
Ena
1500    VLAN 200
4000    spb
Ena     Ena
Dis    1524    AutoFabric BVLAN
4001    spb
Ena     Ena
Dis    1524    AutoFabric BVLAN
4002
spb
Ena     Ena
Dis    1524    AutoFabric BVLAN
. . . 
MVRP VLANs

<<<PAGE 639>>>
AUTO FABRIC- ADMINISTRATION
! Dynamic auto-fabric:
auto-fabric protocols lacp admin-state disable
auto-fabric protocols spb admin-state disable
auto-fabric protocols mvrp admin-state disable
auto-fabric protocols loopback-detection admin-state disable
auto-fabric protocols ip ospfv2 admin-state disable
auto-fabric protocols ip ospfv3 admin-state disable
auto-fabric protocols ip isis admin-state disable
vcboot.cfg
-> show auto-fabric config
Auto-fabric Status          : Disable,
Config Save Timer Status    : Disabled,
Config Save Timer Interval  : 300 seconds,
Default UNP SAP Profile     : Auto-vlan,
Discovery Interval          : 0 minute(s),
Discovery Status            : Idle,
LACP Discovery Status       : Enabled,
LBD Discovery Status        : Enabled,
MVRP Discovery Status       : Enabled,
OSPFv2 Discovery Status     : Enabled,
OSPFv3 Discovery Status     : Enabled,
ISIS Discovery Status       : Enabled,
SPB Discovery Status        : Enabled
-> auto-fabric discovery start
-> auto-fabric admin-state enable
-> auto-fabric config-save admin-state enable

<<<PAGE 640>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 641>>>
A N Y C A S T R P
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 642>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Anycast RP functionality
• Summarize PIM Anycast-RP configuration step

<<<PAGE 643>>>
ANYCAST RP
• Goal
• Provide fast convergence when a PIM rendezvous
point (RP) router fails and RP load-sharing
• Anycast addressing is a generic concept and
is used in PIM sparse mode to add load balancing
and service reliability to RPs
• RFC
• RFC 4610 Anycast-RP Using Protocol Independent
Multicast (PIM)
• RFC 7761 Protocol Independent Multicast –
Sparse Mode (PIM-SM)
• RFC 5060 Protocol Independent Multicast MIB
Source
Client
Receiver 1
Client
Receiver 2
RP1
RP2
OSPF
Server
Client
Receiver 1
Client
Receiver 2
RP1
RP2
OSPF
Register
Register
Register
Register
Register
Register

<<<PAGE 644>>>
ANYCAST RP
How it works
• Uses a single statically defined RP address 
(set on a Loopback interface)
• The RP routers share this Loopback unicast IP 
address announced as a host address
• Senders and Receivers exchange messages 
with the nearest RP
• Determined by the Unicast routing table (IGP).)
• In case of a failure, the convergence is the same as the IGP
• Sources from one RP are known to other
Source
Client
Receiver 1
Client
Receiver 2
OSPF
(IGP)
“Loopback1”
10.10.10.1
“Loopback1” 10.10.10.1
RP2
RP1
Register
ip pim static-rp 231.0.0.0/8 10.10.10.1
Register
Register

<<<PAGE 645>>>
ANYCAST RP
• Hardware Requirements
• Software Requirements as specified in RFC 4610
• This feature will only be supported with PIM-SM 
• not supported with PIM-DM, PIM-BIDIR or PIM-SSM
• Maximum of 8 Anycast RP routers to be configured statically
• SPT must be enabled when supporting Anycast-RP

<<<PAGE 646>>>
ANYCAST RP CONFIGURATION

<<<PAGE 647>>>
Configure Non-RP Router
ANYCAST RP CONFIGURATION
Step by Step
• Here, we define the specific configuration need to manage Anycast-RP
• The rest of the network configuration including additional IP interfaces, PIM Interfaces and 
OSPF configuration to complete the network setup is outside the scope of this example
Configure a static RP for a range of multicast groups
Configure a dedicated Loopback interface
Set of router that will act as RPs for the Anycast-RP address

<<<PAGE 648>>>
Configure a static RP
Statically configure the RP address used with Anycast-RP Unique ID
• RP address is 10.10.10.1, which is configured on a Loopback1 interface on both routers
• OSPF has been configured on both routers, so this Loopback1 address is then be
advertised in OSPF to all routers in the network
ANYCAST RP CONFIGURATION
Step by Step
Non-RP
RP1
ip interface “Loopback1” address 10.10.10.1
ip interface “Loopback1” address 10.10.10.1
RP2
Non-RP
RP1
ip pim static-rp 231.0.0.0/8 10.10.10.1
ip pim static-rp 231.0.0.0/8 10.10.10.1
RP2
Sw1
Sw7
Sw8
ip pim static-rp 231.0.0.0/8 10.10.10.1
Configure a static RP for a range of multicast groups
Configure a dedicated Loopback interface
The group address range that the  Anycast-RPs will be
responsible for
The Anycast-RP address 
Note: This static configuration should exist on all PIM routers in the 
PIM domain, not just those routers that are participating in the Anycast-RP set.

<<<PAGE 649>>>
ANYCAST RP CONFIGURATION
Step by Step
Non-RP
RP1
ip pim anycast-rp 10.10.10.1 192.168.254.1
ip pim anycast-rp 10.10.10.1 192.168.254.7
ip pim anycast-rp 10.10.10.1 192.168.254.1
ip pim anycast-rp 10.10.10.1 192.168.254.7
RP2
Switch Loopback0 manged previously on each switch
Sw1
Sw7
Sw8
Loopback0 : 192.168.254.1
Loopback0 : 192.168.254.7
Loopback0 : 192.168.254.8
Non-RP
RP1
RP2
Sw1
Sw7
Sw8
Loopback0 : 192.168.254.1
Loopback0 : 192.168.254.7
Loopback0 : 192.168.254.7
ip pim static-rp 231.0.0.0/8 10.10.10.1
Configure the RP set
• This is the set of all routers which would act as the RP
• Need a LoopbackX interface on each prospective RP router, 
which is different than the LoopbackX that is being used as 
the RP address
Eg; Loopback0 : 192.168.354.x (x identified the router)
All other PIM routers that are NOT participating in the Anycast-RP set will still have the 
PIM configuration defining the RP, but will not have the anycast-rp specific configuration
Configure Non-RP Router
Set of router that will act as RPs for the Anycast-RP address

<<<PAGE 650>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 651>>>
SERVER LOAD BALANCING (SLB)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 652>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Sum up the concept & characteristics of SLB
• Configure the SLB feature 
• Understand the Distribution algorithm
• Learn about the Server Cluster types
• Monitor the Health
• Configure a SLB Probe

<<<PAGE 653>>>
CONCEPT
• Method to logically manage a group of physical servers as one large virtual server (SLB 
cluster)
• Cluster is identified and accessed at layer 3 by using a Virtual IP (VIP) address or a QoS policy 
condition
• Benefits:
• Cost savings: no costly hardware upgrade to servers
• Scalability: allows up to 16 clusters per switch
• Reliability: provides load-sharing and redundancy
• Flexibility: QoS may be applied to servers
192.168.0.3
192.168.0.5
192.168.0.10
192.168.0.9
192.168.0.8

<<<PAGE 654>>>
CHARACTERISTICS
• Virtual IP address
• Must be an address in the same subnet as the servers
• SLB cluster automatically creates a proxy ARP for the VIP with the switch’s MAC address
• Designed to work at IP layer or bridge
• Capability to specify if SLB is enforced at L2 or L3 
• Distribution based on wire-rate load balancing
• Load balancing is based on L3/L4 information
• Using IPSA and IPDA pairs (optionally UDP/TCP ports)
• Policies for server load balancing can be assigned for the purpose of applying ACLs
• Servers can belong to multiple clusters
• Servers can be distributed on several Nis
• All servers must be part of the same VLAN/subnet. Servers do not need to be physically 
connected to the SLB switch/router, they can be connected through L2 switches for that 
SLB VLAN.

<<<PAGE 655>>>
CONFIGURATION
• Create a loopback adapter in the server
• Define the Virtual IP address to the loopback adapter
• Enable SLB globally
• policy condition, action and rule are automatically created
• Configure the SLB cluster
• Assign physical servers to the SLB cluster
• Modify optional parameters, if necessary
• SLB traffic distribution algorithm
• Load balance hashing control algorithm
• Health monitoring
-> ip slb admin-state enable
-> ip slb cluster Web vip 128.241.130.204
-> ip slb server ip 128.241.130.127 cluster Web
-> ip slb server ip 128.241.130.109 cluster Web

<<<PAGE 656>>>
DISTRIBUTION ALGORITHM
• Default
• Round-robin based on IPSA, SLB-VIP and a random generated number of the SLB-MAC
• Alternative
• Weighted Round Robin (WRR)
• SLB cluster distributes traffic according to the relative “weight” a server has within an SLB cluster
• Aggregate weight of all servers should not exceed 32
-> ip slb server ip <ip-addr> cluster <clstr> admin-state
<enable | disable> probe <probe> weight <weight> 
192.168.100.102
Weight = 3
192.168.100.109
Weight = 2
192.168.100.99
Weight = 1
192.168.100.103
Weight = 0
Cluster
192.168.100.200

<<<PAGE 657>>>
BACKUP SERVER SCENARIO
• If Server 192.168.100.102 goes down, Server 192.168.100.99 will start receiving all the 
traffic 
-> ip slb cluster cl1 vip 192.168.100.200
-> ip slb server ip 192.168.100.102 cluster cl1 weight 1
-> ip slb server ip 192.168.100.99 cluster cl1 weight 0
192.168.100.102
Weight = 1
192.168.100.99
Weight = 0
Cluster cl1
192.168.100.200

<<<PAGE 658>>>
WEIGHTED ROUND ROBIN
• Server A handles three times the traffic of Server C, and Server B twice the traffic of 
Server C.
• Server D is a backup server
-> ip slb cluster cl1 vip 192.168.100.200
-> ip slb server ip 192.168.100.99 cluster cl1 weight 1
-> ip slb server ip 192.168.100.109 cluster cl1 weight 2
-> ip slb server ip 192.168.100.102 cluster cl1 weight 3
-> ip slb server ip 192.168.100.103 cluster cl1 weight 0
=> use for backup
Server A: 192.168.100.102
Weight = 3
Server B:192.168.100.109
Weight = 2
Server C: 192.168.100.99
Weight = 1
Server D: 192.168.100.103
Weight = 0
Cluster cl1
192.168.100.200

<<<PAGE 659>>>
HASHING CONTROL ALGORITHM
• Hashing Control
• Control over the hashing mode
• Link Aggregation
• ECMP
• Server Load Balancing
• Two hashing algorithms available
• Brief Mode: 
• UDP/TCP ports not included
• Only Source IP and destination IP addresses are 
considered
• Extended 
• UDP/TCP ports to be included
in the hashing algorithm
• Result in more efficient
load balancing
Source
Address
Destination
Address
AA
AA
AA
AA
Server #
Source
Address
Destination
Address
AA
AA
AA
AA
Server #
UDP/TCP
Port
Brief Mode
Extended Mode
Switch
Default Hasing Mode
9900
extended
6900
brief
6860
extended
6865
extended
6560
extended
6465
brief
6360
brief
-> hash-control brief
-> hash-control extended [udp-tcp-port | no]

<<<PAGE 660>>>
CLUSTER MODES
• SLB Cluster VIP
• Traffic destined to the Virtual IP of the Server Farm
• Each server is also configured with a Loopback Interface for the Virtual IP
• A server can be configured with more than one VIP
• Therefore, a server can belong to more than one SLB cluster
• SLB Cluster QoS Condition
• Traffic not destined to the server
• i.e : firewall server simply inspects the packet and sends it back if accepted by the Firewall policies

<<<PAGE 661>>>
VIP MODE (L3 ONLY)
• Configuring VIP SLB cluster in a routed network
L3 Network
VLAN
10
Access the VIP
Route to reach VIP
VLAN 11
Switch Router
SLB enabled
L2 switch
VLAN 10
IP@ 10.0.0.254
Server 10.0.0.1
Server 10.0.0.2
Server 10.0.0.3
VIP 10.0.0.250 (WebServer)
-> ip slb cluster WebServer vip 10.0.0.250
-> ip slb server ip 10.0.0.1 cluster WebServer
-> ip slb server ip 10.0.0.2 cluster WebServer
-> ip slb server ip 10.0.0.3 cluster WebServer
Routing from VLAN 11 to Server VLAN 10
-> ip slb cluster <cluster_name> vip <vip_address>

<<<PAGE 662>>>
VIP MODE (L3 ONLY)
• Configuring VIP SLB cluster in a Bridged network
L3 Network
VLAN
10
Access the VIP
Route to reach VIP
Switch 
SLB enabled
L2 switch
VLAN 10
IP@ 10.0.0.254
Server 10.0.0.1
Server 10.0.0.2
Server 10.0.0.3
VIP 10.0.0.250 (WebServer)
-> ip slb cluster WebServer vip 10.0.0.250
-> ip slb server ip 10.0.0.1 cluster WebServer
-> ip slb server ip 10.0.0.2 cluster WebServer
-> ip slb server ip 10.0.0.3 cluster WebServer
Proxy ARP to 10.0.0.250 is used in a bridged network and will force the 
bridged packet to be routed
Bridging in VLAN 10
-> ip slb cluster <cluster_name> vip <vip_address>

<<<PAGE 663>>>
QOS CONDITION MODE
• Configuring QoS Condition SLB cluster in a Routed network
L3 Network
VLAN
10
Access the VIP
Route to reach VIP
VLAN 11
Switch Router
SLB enabled
VLAN 10
IP@ 10.0.0.254
Server 10.0.0.1
Server 10.0.0.2
Cluster « Firewall »
-> policy condition cond1 source port 1/1 destination tcp port 80
-> ip slb cluster Firewall condition cond1 L3
-> ip slb server ip 10.0.0.1 cluster WebServer
-> ip slb server ip 10.0.0.2 cluster WebServer
Routing from VLAN 11 to Server VLAN 10
The server must be configure to receive packet with a destination 
IP address that may not match any addresses known to the server.
1/1
-> ip slb cluster <cluster_name> condition <condition name> L3

<<<PAGE 664>>>
QOS CONDITION MODE
• Configuring QoS Condition SLB cluster in a Bridged network
L3 Network
VLAN
10
Access the VIP
Route to reach VIP
Switch 
SLB enabled
VLAN 10
IP@ 10.0.0.254
Server 10.0.0.1
Server 10.0.0.2
Cluster « Firewall »
1/1
Bridged Network
The server must be configure to receive packet with a destination MAC address
that is different than the MAC address of the server (i.e. promiscuous mode)
-> policy condition cond1 source port 1/1 destination tcp port 80
-> ip slb cluster Firewall condition cond1 L2
-> ip slb server ip 10.0.0.1 cluster WebServer
-> ip slb server ip 10.0.0.2 cluster WebServer
-> ip slb cluster <cluster_name> condition <condition name> L2
Server Load Balancing Presentation
DATA82038P01TEEN

<<<PAGE 665>>>
SLB NEW FEATURES (8.9R4)
• Configuring multiple Conditions in a QoS SLB cluster
-> policy condition cond1 source port 1/1 destination tcp port 80
-> policy condition cond2 source ip 192.168.0.1
-> ip slb cluster Firewall condition cond1 condition cond2 L2
-> ip slb server ip 10.0.0.1 cluster WebServer
-> ip slb server ip 10.0.0.2 cluster WebServer
-> ip slb cluster <cluster_name> condition <condition name> condition <condition2 name>
This allows to use two different hashing methods to distribute traffic towards the cluster
• Activating auto-bypass
When all servers or a given set of servers of a cluster are down, traffic will be routed using normal routes
• Activating wait-to-restore
When an active server comes back online, a timer will be initiated to avoid immediate switchover of traffic to the server
-> ip slb cluster auto-bypass admin-state
-> ip slb cluster auto-bypass inactive-servers
-> ip slb cluster wait-to-restore

<<<PAGE 666>>>
HEALTH MONITORING
• Health Monitoring of the servers based on
• Ethernet link state detection
• IPv4 ICMP ping
• Content Verification Probe
• 20 probes per switch
• Basic Probe - PING
• Application probes: ftp, http, https, mail (imap, imaps, pop, pops, smtp), nntp)
• Custom probes - tcp, udp
• Can specify interval, time-out, and retries
• Server States 
• Disabled server has been administratively disabled by the user
• No Answer server has not responded to ping requests from the switch
• Link Down bad connection to the server
• Discovery switch is pinging a physical server
• In Service server can be used for client connections
• Retrying switch is making another attempt to bring up the server

<<<PAGE 667>>>
SERVER LOAD BALANCING - PROBE CONFIGURATION
• Creating SLB Probes
• Associating a Probe with a Cluster or Server
• Options
• Probe timeout (ms) and Period (sec)
• TCP/UDP Port
• URL / User Name / Password
• sent to a server as credentials for an HTTP(S) GET operation
• Send
• An ASCII string sent to a server to invoke a response
• Expect
• An ASCII string used to compare a response from a server
-> ip slb probe http_test http
-> ip slb probe http http_test period 10
-> ip slb cluster C1 vip 192.168.160.201
-> ip slb server ip 192.160.160.4 cluster C1 weight 2 probe http_test
-> ip slb server ip 192.160.160.4 cluster C1 weight 4 probe http_test
-> ip slb probe <probe_name> {ftp | http | https | imap | imaps | nntp | ping | 
pop | pops | smtp | tcp | udp}
-> ip slb cluster <cluster_name> probe <probe_name>

<<<PAGE 668>>>
PROBE CONFIGURATION
• ping
• TIMEOUT
• RETRIES 
• PORT
• PERIOD
• tcp / udp
• TIMEOUT
• SSL
• SEND
• RETRIES
• PORT
• PERIOD
• NO 
• EXPECT
• ftp / imap / imaps / pop / pops / smtp / nntp
• TIMEOUT
• RETRIES 
• PORT
• PERIOD
• http / https
• USERNAME
• URL
• TIMEOUT
• STATUS
• RETRIES
• PORT   
• PERIOD
• PASSWORD
• EXPECT

<<<PAGE 669>>>
SPECIFICATIONS

<<<PAGE 670>>>
APPENDIX

<<<PAGE 671>>>
ADDING AND CONFIGURING LOOPBACK ADAPTER
ON WINDOWS SERVER
• Device Manager > Add Legacy Hardware
• Install the hardware that I manually select from a list (Advanced)
• Network adapters
• Microsoft > Microsoft KM-Test Loopback Adapter (Win 2k12)
• Microsoft > Microsoft Loopback Adapter (Win 2k8 r2)
• Starting with Windows Server 2008, Microsoft has implemented a strong host model which 
disallowed the host to receive packets on an interface not assigned as the destination IP 
address. To configure weak host mode, enter the following commands:
• Assign VIP address to the Loopback adapter
netsh interface ipv4 set interface <LAN Interface Name> weakhostreceive=enabled
netsh interface ipv4 set interface <Loopback Interface Name> weakhostreceive=enabled
netsh interface ipv4 set interface <Loopback Interface Name> weakhostsend=enabled
Appendix

<<<PAGE 672>>>
ADDING AND CONFIGURING LOOPBACK ADAPTER 
ON LINUX SERVER
• Add Loopback adapter
• Disable ARP replies
• In /etc/sysctl.conf add the following lines:
ifconfig lo:1 <VIPAddress> broadcast <VIPAddress> netmask 255.255.255.255
net.ipv4.conf.eth0.arp_ignore=1
net.ipv4.conf.eth0.arp_announce=2
Appendix

<<<PAGE 673>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 674>>>
UPGRADE SOFTWARE IMAGE
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 675>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe how to upgrade a Software image on a 
switch

<<<PAGE 676>>>
U p g r a d e  t h e  i m a g e  f i l e
UPGRADE SOFTWARE IMAGE
Step by Step
F T P  t h e  U p g r a d e  F i l e s  t o  t h e  S w i t c h
D o w n l o a d  t h e  U p g r a d e  F i l e s
V e r i f y t h e  S o f t w a r e  U p g r a d e
C e r t i f y t h e  S o f t w a r e  U p g r a d e
U p g r a d e  u b o o t a n d / o r  F G PA  i f  m a n d a t o r y
A n a l y s e  R e q u i r e m e n t s o n  t h e  r e l e a s e  n o t e

<<<PAGE 677>>>
UPGRADE SOFTWARE IMAGE
Step by Step
From BPWS
Download and unzip the upgrade files for the appropriate model and release
D o w n l o a d  t h e  U p g r a d e  F i l e s
OS6360
OS6465
OS6560
OS6570
OS6860
OS6865
OS6860N
0S6870
0S6900
0S9900
Configuration 
files
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
vcboot.cfg
vcsetup.cfg
image files 
(AOS)
Nosa.img
Nos.img
Wos.img
Uos.img
Uosn.img
kaos.img
Tos.img
Yos.img
(V72/C32/X48C6/
T48C6/
X48C4E/V48C8
T24C2 …
Mhost.img
Mos.img
Meni.img

<<<PAGE 678>>>
Memory Requirements
UBoot and FPGA Requirements
Upgrade Instructions
…
FTP/SFTP/SCP Client or Server
TFTP client
USB
WebView
OmniVista 2500
UPGRADE SOFTWARE IMAGE
Step by Sep
Note: Running directory ; working or user defined directory
F T P  t h e  U p g r a d e  F i l e s  t o  R u n n i n g  d i r e c t o r y  o f  t h e  s w i t c h  
A n a l y s e  R e q u i r e m e n t s o n  t h e  r e l e a s e  n o t e

<<<PAGE 679>>>
Display version installed
Display the version running in CMM
UPGRADE SOFTWARE IMAGE
Step by Step
Note: If there are any issues after upgrading the switch can be rolled back to the previous certified version
U p g r a d e  t h e  i m a g e  f i l e
V e r i f y t h e  S o f t w a r e  U p g r a d e

<<<PAGE 680>>>
UPGRADE SOFTWARE IMAGE
Step by Step
In addition to the AOS images, archive will also contain an uboot and FPGA upgrade kit.
If require (Release note)
FTP (Binary) the FPGA upgrade kit and /or Uboot upgrade tar.gz to the /flash directory (primary CMM)
Reload from running directory
Verifying the software and that the network is stable
Certify the new software 
-> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz
-> update fpga-cpld cmm all file fpga_kit_3312
-> reload from working no rollback-timeout
Note: The command show hardware-info is used 
-> copy running certified
-> show running-directory
C e r t i f y t h e  S o f t w a r e  U p g r a d e
U p g r a d e  u b o o t a n d / o r  F G PA  i f  m a n d a t o r y

<<<PAGE 681>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 682>>>
I S - I S
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 683>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the characteristics of the IS-IS Routing 
protocol

<<<PAGE 684>>>
IS-IS CONCEPTS AND BASIC SETUP - AOS SPECIFICATIONS
• Maximum number of (per router)
• Areas - 3
• Maximum number of L1 adjacencies 70
• Maximum number of L2 adjacencies 70
• Maximum number of IS-IS interfaces 70
• Maximum number of Link State Packet Entries 255
• Maximum number of IS-IS routes 24000
• Maximum number of IS-IS L1 routes 12000
• Maximum number of IS-IS L2 routes 12000
• RFCs Supported
• 1142-OSI IS-IS Intra-domain Routing Protocol
• 1195-OSI IS-IS for Routing in TCP/IP and Dual 
Environments
• 3373-Three-Way Handshake for Intermediate 
System to Intermediate System (IS-IS) Point-to-
Point Adjacencies
• 3567-Intermediate System to Intermediate
• System (IS-IS) Cryptographic Authentication
• 2966-Prefix Distribution with two-level IS-IS (Route 
Leaking) support
• 2763-Dynamic Host name exchange support
• 3719-Recommendations for Interoperable 
Networks using IS-IS
• 3787-Recommendations for Interoperable IP
• Networks using IS-IS draft-ietf-isis-igp-p2p-over-
lan-05.txt-Point-topoint operation over LAN in 
link-state routing protocols
• 5308-IS-IS support for IPv6 (Routing IPv6 with IS-IS)

<<<PAGE 685>>>
• IS-IS uses SPF for path determination.
• SPF uses cost values to determine the best 
path to a destination.
IS-IS BASICS
• IS-IS Overview
• OmniSwitch based on RFC 3787
• Link-state driven updates, periodic hellos
• Uses the SPF algorithm to determine routes
• Area hierarchy, ASs use a two-level hierarchy
• Support for authentication
• Support for VLSM and CIDR
• Routing interface parameters 
• Layer 2 multicast addressing
• IS-IS TE extensions
Router A
10.0.0.0: cost 30 via Router C
*10.0.0.0: cost 20 via Router B
* = Best path
IS-IS Routes 
Cost:10
A
<
10.0.0.0
B
Cost:10
Cost:10
C
Packet Flow

<<<PAGE 686>>>
IS-IS - ISO NETWORK ADDRESSING
• Each IS-IS Router is known as an “Intermediate System”
• IS-IS uses unique addressing (OSI NSAP addresses) 
• Each address identifies the area, system, and selector.
• Level 1 routing uses the system ID.
• Level 2 routing uses the area address.
• 2 nodes cannot have the same NSAP address.
• 2 nodes within an area cannot have the same system ID.
• The minimum NSAP using local authority is 8 bytes (1 for area, 6 for system, 1 for SEL).
• The area ID must be minimum 1 byte.
• The AFI should be set to 49 for locally administered IS-IS configurations. 
Area ID
System Address
NSEL
49.0002
18B6.A345.0BF1
00
AFI
IDI
High Order-DSP
System ID
NSEL

<<<PAGE 687>>>
NSAP ADDRESSING 
• Red - the locally administered area ID of each router.
• Blue - the system ID of each router.
• Black - the NSEL default of “00”.
00:d0:95:f3:c8:ba
L1/L2
Area 49.0003
Area 49.0002
L1/L2
L1
L1
49.0002.00D0.9501.0101.00
49.0002.00D0.9501.0102.00
49.0003.00D0.9501.0104.00
49.0003.00D0.9501.0103.00
{Area-ID}
{System-ID}
{NSEL}

<<<PAGE 688>>>
IS-IS — PACKET FORMAT
• IS-IS packets use layer 2 encapsulation of the media.
• IS-IS uses Ethernet 802.3/802.2 instead of the Ethernet II used for IP traffic.
• The TLV identifies the type of information in the IS-IS packet.
• IS-IS packets are called PDUs.
• PDUs are encapsulated directly into the layer 2 frame.
• There are 4 types of PDUs:
• Hello (ESH, ISH, and IIH) — Maintain adjacencies
• LSP (link-state packet) — Information about neighbors and links, generated by all L1 and L2 routers
• PSNP (Partial Sequence Number PDU) — Specific requests and responses about links, generated by 
all L1 and L2 routers
• CSNP — Complete list of LSPs exchanged to maintain database  consistency
MAC 
Header
FCS
IS-IS TLV
IS-IS 
Header
LLC 
Header

<<<PAGE 689>>>
IS-IS - TERMS
• DIS
• The IS in a LAN that is designated to perform additional duties. In particular, the DIS generates 
link-state PDUs on behalf of the LAN, and treats the LAN as a pseudo node.
• Pseudo node 
• When a broadcast subnetwork has n connected ISs, the broadcast subnetwork itself is considered to 
be a pseudo node. The pseudo node has links to each of the n ISs and each of the ISs has a single 
link to the pseudo node (rather than n-1 links to each of the other ISs). Link-state PDUs are 
generated on behalf of the pseudo node by the DIS.

<<<PAGE 690>>>
IS-IS - HELLO PACKET FORMAT
• Used to discover neighbors and elect the DIS
• Sent every 9 seconds from L1 and L2 routers, if they are not the DIS
• Sent every 3 seconds from the DIS in broadcast multi-access networks
• 3 different formats:
• Level 1 and Level 2 in broadcast subnetworks
• Point-to-point in general topology subnetworks
• Highest priority elects the DIS for both L1 and L2 in broadcast networks
• Highest interface MAC address is the tiebreaker if priorities are equal
• DIS assigns the subnetwork ID (DIS NET + SEL)

<<<PAGE 691>>>
LINK-STATE PDU (LSP) FORMAT
• Slightly different formats for L1 and L2 LSPs
• LSP Identifier indicates which router created the LSP
• Sequence number indicates relative age of the LSP
• When a router creates a new LSP, the sequence number is incremented.
• Reachability information is provided for all local networks from the router that created the 
LSP:
• Network prefix
• Metrics
• IP mask
• An L1 LSP is flooded to all other L1 routers in the area.
• An L2 LSP is flooded to all other L2 routers in the network.

<<<PAGE 692>>>
COMPLETE SEQUENCE NUMBER PDU FORMAT
• CSNPs used to maintain consistency of link-state database
• Contains list of router’s LSPs and their sequence numbers.
• A router that receives a CSNP that includes out-of-date LSPs will transmit up-to-date LSPs.
• CSNPs are exchanged at router initialization and periodically afterward to maintain 
synchronization.
• Every 10 seconds on broadcast network
• Every 5 seconds on point-to-point link
• For each LSP in its database, the CSNP contains:
• Remaining life of the LSP, in seconds
• LSP ID
• LSP sequence number
• Checksum value

<<<PAGE 693>>>
PARTIAL SEQUENCE NUMBER PDU FORMAT
• PSNPs are used by routers to request a specific LSP.
• PSNPs are also used on point-to-point links to acknowledge the receipt of an LSP (but not 
on a broadcast link).
• A PSNP is similar to a CSNP except that it is a subset of the LSPs from the database.
• A PSNP describes one or more LSPs and contains the following information for each:
• Remaining life of the LSP, in seconds
• LSP ID
• LSP sequence number
• Checksum value

<<<PAGE 694>>>
IS-IS – NETWORK TYPES
• IS-IS only supports:
• Broadcast for LAN and multipoint WAN topologies
• Point-to-point for all other topologies
• When IS-IS implemented in an NBMA network:
• Broadcast mode assumes fully meshed connectivity.
• Point-to-point assumes true point-to-point connectivity.
• LAN and multipoint WAN topologies require the election of a Designated Intermediate 
System DIS.
• Hellos are used to create adjacencies and determine router priority.
• The DIS is elected based on the following criteria:
• Only routers with adjacencies are eligible.
• Highest interface priority
• Highest interface MAC address

<<<PAGE 695>>>
IS-IS – DIS ELECTION FOR L1 AND L2 ROUTERS
• L1 and L2 routers can elect separate DIS routers.
• DIS election is based on priority and/or the highest MAC address and is preemptive.
• L1 and L2 can have separate priorities set.
• The DIS creates the pseudo node and floods updates over the LAN.
L1/L2
L1
L2
L1
L1
L2

<<<PAGE 696>>>
IS-IS — PACKET EXCHANGE
• L1 and L2 adjacencies use the same procedure.
• Adjacency is established when a valid IIH is received:
• L1 adjacency if area IDs are the same and the circuit is L1
• L2 adjacency if the circuit is L2
• The initial exchange of IIHs establishes the type of adjacency.
• The 2-way handshake depends on a reliable circuit.
• A unique local circuit ID is determined by each IS configuration.
• The link’s circuit ID is set by the system with the higher source ID.
• Concatenation of system ID and local circuit ID
• Both sides exchange CSNPs.
• Update reliability is accomplished by:
• Sending PSNP for all new and duplicate LSPs
• Answering older LSPs with newer LSPs

<<<PAGE 697>>>
CONFIGURING IS-IS
• Minimum configuration (single area)
-> ip load isis
-> ip isis admin-state enable
-> ip isis area-id 49.0001
-> ip isis activate-ipv4
-> ip isis vlan 5
-> ip isis vlan 5 address-family v4
-> ip isis vlan 5 admin-state enable

<<<PAGE 698>>>
IS-IS - CLI COMMANDS 
• Interface configuration
• Monitoring
-> ip isis level-capability level-1
-> ip isis level-capability level-2
-> ip isis level-capability level-1/2
-> ip isis vlan 10 level-capability level-1/2
-> show isis status
-> show ip isis vlan
-> show ip isis vlan detail
-> show ip isis route
-> show ip isis spf
-> show ip isis adjacency

<<<PAGE 699>>>
IS-IS - AREA TYPES
Area 03
Area 02
Area 01
Area 04
L1
L1/L2
L1/L2
L1/L2
L1/L2
L1
L1
L1
L1
L1
L1

<<<PAGE 700>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 701>>>
OVERVIEW AND BASIC SET-UP
FLEET SUPERVISION
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 702>>>
LESSON SUMMARY
✓Overview
• Explain the principles of Fleet Supervision
• Discover the application
✓Basic set-up
• Learn how-to set up a fleet supervision 
account with OV 2500, OV Cirrus or a list of 
devices

<<<PAGE 703>>>
OVERVIEW

<<<PAGE 704>>>
ASSESS AND CONTROL COMPLIANCE WITH 
NETWORK FLEET SUPERVISION
• One View. All Assets. Every Status
• Register your serial numbers or OmniVista 
Management platform ID to track your fleet 
effortless, no matter how your infrastructure 
evolves.
• Access support and warranty levels, coverage dates, 
lifecycle status, and recommended releases in one 
place.
• Assess your security and compliance 
• Ensure devices are up-to-date, supported, 
and ready for refresh
• Plan budgets to maintain service, security, and 
compliance.
• Accelerate Operations with Service Kiosk
• Identify device with no or expiring support 
• Request coverage from your partner.
Stay secure & compliant
Proactively
Free of charge
OmniSwitch & OmniAccess Stellar
Services Kiosk 
https://myfleet.ovcirrus.com/

<<<PAGE 705>>>
NETWORK FLEET SUPERVISION
Software Version Visibility 
(for managed devices only)
• Show Running software version
Inventory visualization
• Inventory management  with Drill down 
and Sorting flexibility
• Individual Device view
• Key info- Summary and detailed view of 
OmniSwitch chassis, power supplies, 
transceivers and Stellar access points
• Service/Support status , device life cycle 
Warranty, Software Version
Dashboard, KPIs & Delegation
• Service & support entitlement ratio/%
• Device lifecycle & Warranty  Ratio/%
• All software versions displayed at a glance
• Easy Reports export
• Delegation to Supervisor
Asset Collection from Different Sources
• Automatic asset inventory for OmniVista Management platforms
• Manual option to  import Serial numbers
Software 
version 
visibility
Inventory 
Visualization
Dashboard 
KPIs & 
Delegation
Asset 
Collection

<<<PAGE 706>>>
KPI DASHBOARD
Hardware Lifecycle
•
General Availability/End of Sales/ End of Life
Switch Models & Versions
•
Running software version per model
Maintenance & Support contract
•
Active/Expired/None
AP Models and Versions
•
Running software version per model
Hardware Support
•
AVR/RTF/None
Device Type 
•
Quantity of devices per model
1
2
3

<<<PAGE 707>>>
GRAPHS
Search models
•
Select and graph of top 10 models
•
Display of running software versions

<<<PAGE 708>>>
BASIC SET-UP

<<<PAGE 709>>>
HOW TO START FLEET SUPERVISION
• Sign up and sign in
• https://myfleet.ovcirrus.com/signup
• Account: enter your email @ + password 
• Declare 
• an OmniVista Management system
• OV 2500 on premise
• Legacy OV Cirrus 4.X
• New OV Cirrus (10.5 and upwards)
• OR Import your device list using the template file

<<<PAGE 710>>>
ADDING A MANAGEMENT SYSTEM
• Go to « Management System » and click on « Create Management System »
• Then depending on which management system you choose, follow the steps in the next 
slide to gather the appropriate information.

<<<PAGE 711>>>
HOW TO DECLARE OV 2500
• Declare your OV 2500 and use your own records
• Specifying your OV2500 ID 
• Fleet will pull device inventory from OV2500 backend. 
• Refer to Administration -> Preferences -> System Settings -> Fleet Supervision for OV2500 ID and observing 
the sync status of inventory to OV backend

<<<PAGE 712>>>
HOW TO DECLARE OV CIRRUS 4.X
• To declare an OV Cirrus 4.X in Fleet supervision, you will need
• The URL of your Cirrus 4.X instance: e.g. https://customer1.ov.ovcirrus.com/
• The API Key of your Cirrus 4.X instance, found under Security > External Apps:

<<<PAGE 713>>>
HOW TO DECLARE OV CIRRUS (10.5.X AND UPWARDS)
• To declare an OV Cirrus in Fleet supervision, you will need:
• The URL of your OV Cirrus instance, and its Organization ID
• The Application ID and Application secret of your Cirrus instance, found in Applications, under your account:
1
2
2
1
2

<<<PAGE 714>>>
HOW TO DECLARE DEVICES MANUALLY IN FLEET
• Last option when your devices are not managed by any OmniVista, is to import your device 
list directly in Fleet Supervision, through a CSV or XLSX file

<<<PAGE 715>>>
TAKEAWAY
• Watch the Fleet Supervision videos playlist to get a more thorough view on the application

<<<PAGE 716>>>
QUIZ
Quiz
Click the Quiz button to edit this object

<<<PAGE 717>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 718>>>
CLASSROOM SESSION 
OR VIRTUAL CLASS SESSION
END OF TRAINING EVALUATIONS
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 719>>>
YOUR FEEDBACKS ARE 
IMPORTANT!
Thank you to complete the training 
evaluation online survey before 
leaving your session. This will take 
you 2 minutes! 
You must complete the end of 
training evaluation to be able to 
download your training certificate of 
attendance.

<<<PAGE 720>>>
LOGIN TO ALE KNOWLEDGE HUB
• Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual 
credentials

<<<PAGE 721>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (1/2)
• Click on My Training on the home page
• Search for the training course by the reference provided by your instructor

<<<PAGE 722>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (2/2)
• From the session, select Evaluate in the dropdown menu and follow the instructions
• OR
• From the curriculum, select Open Curriculum
• Then select Evaluate in the dropdown menu associated to the session and follow 
the instructions

<<<PAGE 723>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 724>>>
Find a Course 
Browse our catalog available on https://enterprise-education.csod.com/ to find your training path 
and course detail. 
Feedback 
In order to improve the quality of the documentation, please report any feedback and address to: 
Alcatel-Lucent Enterprise 
115-225 rue Antoine de Saint-Exupéry 
ZAC Prat Pip – Guipavas 
29806 BREST CEDEX 9 – France 
FAX: (33) 2 98 28 50 03 
or mail to: 
training-services@al-enterprise.com