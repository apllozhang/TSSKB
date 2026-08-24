

<<<PAGE 1>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
OMNISWITCH LAN - R8 
ACCESS SWITCHING - EDITION 19 
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
DT00XTE215EN
Access switching
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
• Course introduction
‐
Training course agenda & Access to remote lab
• OmniSwitch Portfolio 
‐
Overview
• AOS OmniSwitch Management
‐
Log into the switch
‐
Managing Files/Directories
‐
Labs :
Working/Running/Certified Directory 
Remote Switch Access
• Virtual Chassis
‐
Overview
‐
Lab: Virtual chassis
• VLANs Management
‐ Overview
‐ Labs : VLAN

<<<PAGE 7>>>
Day 2
• Basic Switch Management & Diagnostic
‐
Overview
‐
Lab: Switch maintenance and Diagnostics tools
• Link Aggregation Groups
‐
Overview
‐
Lab : Link Aggregation and 802.1Q
• Spanning Tree Protocol (STP)
‐
Overview
‐
Lab : STP
• Dual Home Link (DHL)
‐
Overview
‐
Lab : Dual Home Link Active-Active
• IP interfaces
‐
Overview (DHCP, Static Routing)
‐
Lab : DHCP Server & DHCP Relay
• VRRP 
‐
Overview
‐
Lab : Virtual router redundancy Protocol

<<<PAGE 8>>>
Day 3
• Quality of Service
‐
Overview
‐
Lab : Quality of Service
• Flow Based Filtering (ACL)
‐
Overview
‐
Lab : Access Control List - Prior Configuration
‐
Lab : Security Network Access Control
• Security Network
‐ Overview Access Guardian
‐ Lab : Access Guardian Implementation
• Link Layer Discovery Protocol (LLDP)
‐
Overview
• Power over Ethernet (PoE)
‐ Overview

<<<PAGE 9>>>
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

<<<PAGE 10>>>
Internet Ressources
• Alcatel-Lucent Enterprise Web Site
https://www.al-enterprise.com/en
• Training & Certification
https://www.al-enterprise.com/en/services/education-services
• RFC Technical documents
http://www.ietf.org

<<<PAGE 11>>>
• Partners Website
• MyPortal
• ALE Network Equipment
• www.al-enterprise.com/en/products/switches
• Spacewalkers Community
• www.spacewalkers.com
Internet Resources

<<<PAGE 12>>>
REMOTE LAB CONNECTION
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 13>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Remote-Labs (R-Labs) topology
• Connect to a Remote-Lab (R-Lab)

<<<PAGE 14>>>
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

<<<PAGE 15>>>
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

<<<PAGE 16>>>
REMOTE LABS > TOPOLOGY
1
2
3
4

<<<PAGE 17>>>
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

<<<PAGE 18>>>
DHCP SERVER
• A DHCP server is running with an IP address of 192.168.100.102 and has the following 
scopes (where x stands for the switch number):

<<<PAGE 19>>>
OMNIVISTA 2500 & INTERNET ACCESS
• An OmniVista 2500 server is configured with the IP address 192.168.100.107/24.
• The OmniVista 2500 is reachable
from RDP desktop through a WEB 
client at the URL:
https://10.4.pod#.208:8443
• DNS server on the client : 10.0.0.51
• If Internet access is required for VM clients,
a pre-configuration has to be done on the OS6900-A

<<<PAGE 20>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 21>>>
OMNISWITCH AND STELLAR ACCESS POINTS 
EQUIPMENT - PORTFOLIO
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 22>>>
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

<<<PAGE 23>>>
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

<<<PAGE 24>>>
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

<<<PAGE 25>>>
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

<<<PAGE 26>>>
STELLAR ACCESS POINTS

<<<PAGE 27>>>
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

<<<PAGE 28>>>
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

<<<PAGE 29>>>
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

<<<PAGE 30>>>
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

<<<PAGE 31>>>
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

<<<PAGE 32>>>
ACCESSORIES > EXTERNAL ANTENNAS
• The External Antennas models and details can also be found in the Product Line Matrix 
documentation:
Click on this icon to view the full Antennas Matrix documentation (p. 6)

<<<PAGE 33>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 34>>>
CONNECTING TO THE SWITCH
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 35>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the different possibilities of connection 
to the switch

<<<PAGE 36>>>
OVERVIEW
• Goal
• How it works
• Allow or deny access available management
• On Console, Telnet, HTTP, HTTPS, FTP, SSH, and SNMP 
• Authenticated Switch Access (ASA) feature
• Lock or Unlock session types
(aaa authentication command)
AOS OmniSwitch
OXO R > 9.1 
R.1
Authentication Server
Local or external database
Local User
Login via  console port 
Remote user
Login via SSH, telnet, 
HTTP/HTTPS (WebView) 
or SNMP (OV)
EMP (Outbound IP 
interface)
-> no aaa authentication http
-> show aaa authentication
Service type = Default
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Console
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Telnet
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Ftp
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Http
Authentication = denied
Service type = Snmp
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
...

<<<PAGE 37>>>
LOCAL OR REMOTE CONNECTION TO THE SWITCH
• Example: Allow or deny access available management
-> show aaa authentication
Service type = Default
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Console
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Telnet
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Ftp
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Http
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Snmp
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
---
-> no aaa authentication http
-> no aaa authentication http
-> show aaa authentication
Service type = Default
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Console
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Telnet
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Ftp
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
Service type = Http
Authentication = denied
Service type = Snmp
Authentication = Use Default,
1st authentication server  = local
Authentication exit-on-fail: Enabled
...

<<<PAGE 38>>>
SWITCH USER ACCOUNT
• How it works
• Stored in the local user database and / or on external authentication servers
AOS OmniSwitch
Authentication Server
RADIUS or LDAP
Local User
Login via  console port 
The Local userDB file is named userTable9
Path:  flash/system directory
By default : 2 users “admin and default”
Default login name and password
Login : admin
Password : switch
*User login information and user privileges 
can be stored on the servers.
* Up to 64 users can be configured in the local switch database
* User Privileges : read and write access to command domains and families

<<<PAGE 39>>>
PASSWORD FOR ADMIN
• Beginning in 8.10R3 a warning message will be displayed urging for the default password to be
changed when logging in using the ‘admin’ account. Beginning in 8.10R4 changing the default 
password will be mandatory. 
Webview

<<<PAGE 40>>>
SECURITY
• IEC62443-3-3 Level 2 Ready in 8.10R3
• The IEC 62443 standard, which is focused on the security of industrial automation and control systems (IACS)
• This enhance allows and administrator to enforce a password refresh                                                          
for a specific user or all users upon their next login.
• user password-refresh
• user <string> password-refresh 
• This enhancement provides the ability to convert certificates in DER, PEM, PKCS#12, and P7B to PEM format.
• aaa certificate convert-cert
• This enhance provides the ability to check a certificate's revocation status using either CRL (Certificate 
Revocation List) or OCSP (Online Certificate Status Protocol). Currently supported for Radius and Syslog over 
TLS.
• ssl pki check-revocation

<<<PAGE 41>>>
CONNECTING TO THE SWITCH
Declaring multiple servers with fail-through
• Use aaa command to allow multiple servers for AAA authentication
• Fail-through now possible
-> aaa authentication default Radius01 Radius02 local
Auth
request
No user 
information
Auth
request
Success / 
Failure
aaa authentication {console | telnet | ftp | http | snmp | ssh | default} server1 [server2...] [local] [exit-on-fail {enable | disable}]
exit-on-fail Configures if the switch must authenticate using all servers in the list or only the first available server. When enabled, the switch 
uses only the first available server in the list to check for user information. When disabled, the switch uses all the available servers in the list to 
check for user information.

<<<PAGE 42>>>
ACCESS VIA THE CONSOLE PORT 
• Goal
• By default, single user management account is available at the first bootup of the switch
• How it works
AOS OmniSwitch
Login to the Console Port
1
RJ45 – Port console
2
USB - RS232
3
Micro-USB - RS232
4
Micro-USB - USB
* USB Adapter with Bluetooth Technology supported on an OS6465, 6560, 6860, 6865, 6900-V72 /C32
USB adapters supported are listed on release note
More information about 
cable used are available on 
the eBook below in section 
“If you want to know more”
* By default, DCE console connection
* Except for 6900 V72/C32   (cross cable)

<<<PAGE 43>>>
ACCESS VIA THE CONSOLE PORT 
• CLI: Command Line Interface 
• Use software like Tera Term, Putty, HyperTerminal …
Default settings
Note: the configuration for the latest generation 
6900 and 6860N switches is different:
Speed (baud) : 115200
Parity: None
Stop bits : 1
Flow control : none

<<<PAGE 44>>>
ACCESS VIA THE EMP PORT
• Goal
• Bypass the network interface modules (NI)
• Remotely manage the switch directly via the CMM  
(not available in all switches)
• The EMP port IP address of the master chassis 
(Virtual Chassis)
ip interface master emp address 172.25.167.203 mask 255.255.255.224
OS6860N
USB Ethernet Dongle (8.9.R1)
• This feature allows for a USB-to-Ethernet interface for switches that 
lack an EMP port. This interface is treated just like an EMP interface. 
• All functions and CLIs related to EMP are applicable to the USB-to-
Ethernet dongle.
Notes:
• USB 3.0 version dongles are supported on OS6360/6465/6560 models. 
• USB 2.0 version dongles are supported on all models.
• All the chassis of a VC should have a USB-to-Ethernet dongle for proper VC EMP functionality.

<<<PAGE 45>>>
TELNET, SSH, HTTP, SNMP
Session specification
* Extract from OmniSwitch AOS Release 8  Specifications Guide
Session
AOS OmniSwitch
Telnet (V4 or V6)
6
FTP (V4 or V6)
4
SSH + SFTP (V4 or V6 secure session)
8
HTTP
4
Total sessions (Secure Shell, Telnet, FTP, HTTP, and console)
20
SNMP
50
Secure Shell public key authentication
Password
DSA/RSA/ECSDA Public Key
Secure Shell public key authentication
Password
DSA/RSA Public Key
RFCs Supported for SSHv2
RFC 4253 – SSH Transport Layer Protocol
RFC 4418 – UMAC: message Authentication Code Universal Hashing

<<<PAGE 46>>>
ACCESS VIA WEBVIEW
• Goal
• The switch can be monitored and configured using WebView
• View is limited to one switch 
• Access can be secured 
• How it works
• The WebView application is embedded in the switch and is accessible via a web browser

<<<PAGE 47>>>
CONNECTING TO THE SWITCH: ACCESS VIA WEBVIEW
• Webview configuration
-> show webview
WebView Server = Enabled,
WebView Access = Enabled,
WebView Force-SSL = Enabled,
WebView HTTP-Port = 80,
WebView HTTPS-Port = 443
webview server enable
• Enables the WebView Application (default= enabled)
webview force-ssl enable
• Forces SSL connection between browser and switch (default=enabled)
webview http(s) port
• Changes the port number for the embedded Web server
aaa authentication http local
• Checks the local database for HTTP authentication

<<<PAGE 48>>>
ACCESS VIA SNMP
• SNMP - IPv4 & IPv6 
• Versions 
• SNMPv1
• SNMPv2 
• SNMPv3
• Main applications to manage and supervise
• Discovery
• Topology
• Access Guardian, UNP
• Performance
• Traps/Events
• VLAN Manager
• Locator
• Policy Mgt
• …
Analytics
Displays Application Traffic Patterns
Quarantine Manager and Remediation
Provides Global device containment
Topology
On premise or on Cloud (OV Cirrus)
OmniVista 2500 Series
Infrastructure
OmniVista Advanced
Applications

<<<PAGE 49>>>
EASY CONFIGURATION WITH LIGHTNING CONFIGURATION
• The goal is to improve Ease of Configuration on AOS OS6360-P10/P24/P48, 6465, 6560 and 
6570M 
• The switch  starts with default IP address, VLAN 1, lightning-config interface, IP 192.168.0.1/24 
Connection to Webview
Configuration Wizard
Port 1/1/1-2
DHCP Client
Default IP interface VLAN1
192.168.0.1

<<<PAGE 50>>>
EASY CONFIGURATION WITH LIGHTNING CONFIGURATION
• Access from user copper ports 1/1/1-2, no need to get a console cable
• Configuration from a PC/Tablet/Mobile with Ethernet interface (with IP or DHCP 
configuration) and a bowser 
• When login on Webview
• A Quick Config Dashboard window opens 
• We get access of the mandatory and pre-selected options (NTP, IP, GTW, DNS, Services, cli Prompt, 
LLDP, IPMS,DDM…)
• VMS options are available (Video Management System), multicast parameters
• Ability to save parameters as a file 
• Ability to import a configuration file

<<<PAGE 51>>>
EASY CONFIGURATION WITH LIGHTNING CONFIGURATION
• The easy configuration process (Lightning configuration) starts if :
• Only first or second physical port connected with the client, no other ports connected
• No prior switch configuration exist
• No DHCP address assignment occurs after boot up
• No remote configuration load (RCL) server and OmniVista NMS connection exists
• Connected device should have an IP address assigned to its Ethernet connection (manual setup) or 
DHCP client configuration the the switch will assign an IP to the client 192.168.0.200 
• AOS will allow local authentication and enables HTTPS access to WebView ONLY via physical port 
#1/1-2 (on VLAN 1).
• Once switch configuration is saved (i.e. write memory), the default IP address is no longer 
available (i.e. will be internally removed)

<<<PAGE 52>>>
LIGHTNING CONFIGURATION INTERFACE

<<<PAGE 53>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 54>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Remote Switch Access 
How to 
✓ Administrate the OmniSwitches remotely 
Contents 
1 
Accessing to the Switch Remotely .......................................................... 2 
2 
Authenticating to the Switch ................................................................ 4 
2.1. Enabling the SSH connection ...................................................................... 4 
2.2. Testing the SSH connection ....................................................................... 4 
2.2.1. Configuring the OmniSwitch .............................................................................. 5 
3 
Accessing to the WebView ................................................................... 6 
3.1. Setting up the HTTP Session ...................................................................... 6 
3.2. Opening the WebView ............................................................................. 6 
3.3. Configuring the OmniSwitch from the WebView ............................................... 7 
3.4. Visualize your chassis .............................................................................. 8 
3.5. Creating a VLAN from the WebView ............................................................. 9 
3.6. Deleting a VLAN from the WebView ............................................................ 10

<<<PAGE 55>>>
2 
Remote Switch Access 
 
Implementation 
 1 
Accessing to the Switch Remotely 
The OmniSwitches have been reinitialized with a minimum Network configuration. Please note this is not an 
empty configuration. 
- A static route is configured to reach the administration network 10.0.0.0, allowing you to have IP 
connectivity from your remote desktop to any switch of your R-Lab. 
 
 
 
 
- If the switch has an EMP interface (OS6900, OS6870, OS6860N), an IP address will be assigned to it.  
- If the switch does not have an EMP interface (OS6560, OS6360), a USB-to-Ethernet dongle is connected to 
the usb port of the switch. This creates a USB-to-Ethernet interface for switches that do not have an EMP 
port. This interface is treated as an EMP interface, and all EMP-related functions and CLIs are applicable 
to the USB-to-Ethernet dongle. 
 
 
 
Switch 
Interface 
IP address 
6900-A 
EMP 
10.4.Pod#.1 
6870-B 
EMP 
10.4.Pod#.2 
6560-A 
EMP 
10.4.Pod#.3 
6360-A 
EMP 
10.4.Pod#.5 
6360-B 
EMP 
10.4.Pod#.6 
 
 
 
6870-A 
EMP 
10.4.100+Pod#.7 
6860-B 
EMP  
10.4.100+Pod#.8 
OR 
 
 
6870-A 
EMP 
10.4.Pod#.7 
6860-B 
EMP  
10.4.Pod#.8

<<<PAGE 56>>>
3 
Remote Switch Access 
 
 
- For example, check the IP interface of one switch which has an EMP interface (ex. 6900-A): 
 
sw1 (6900-A) -> show ip interface 
 
Total 3 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.X.1        255.255.255.0      UP      NO   EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN     NO   EMP 
Loopback                         127.0.0.1       255.255.255.255    UP      NO   Loopback 
---[truncated]--- 
 
- For example, check the IP interface of one switch which doesn’t have an EMP interface and uses the 
dongle USB-to-Ethernet (ex. 6360-A): 
 
sw5 (6360-A) -> show ip interface 
Total 3 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.X.5       255.255.255.0      UP      NO     EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN    NO     EMP 
Loopback                         127.0.0.1       255.255.255.255   UP      NO     Loopback 
 
 
- From your Windows Desktop, open a console and try to ping the 7 switches:   
 
C:\>ping 10.4.Pod#.1 
C:\>ping 10.4.Pod#.2 
C:\>ping 10.4.Pod#.3 
C:\>ping 10.4.Pod#.5 
C:\>ping 10.4.Pod#.6 
C:\>ping 10.4.Pod#+100.7 or C:\>ping 10.4.Pod#.7 
C:\>ping 10.4.Pod#+100.8 or C:\>ping 10.4.Pod#.8

<<<PAGE 57>>>
4 
Remote Switch Access 
 
 2 
Authenticating to the Switch  
Authenticated Switch Access (ASA) provides the ability to restrict which users can configure the switch 
remotely. Switch login attempts can be challenged via the local database, or a remote database such as RADIUS 
or LDAP. ASA applies to Telnet, FTP, SNMP, SSH, HTTP, and the console and modem ports. 
2.1. 
Enabling the SSH connection 
- Log into the OS6560-A, then use the command to verify that the switch is checking its local database when 
an SSH connection is attempted:  
 
sw3 (6560-A) -> show aaa authentication 
Service type = Default 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
Service type = Console 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
Service type = Telnet 
  Authentication = Use Default, 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
Service type = Ftp 
  Authentication = Use Default, 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
Service type = Http 
  Authentication = Use Default, 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
Service type = Snmp 
  Authentication = Use Default, 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
Service type = Ssh 
  Authentication = Use Default, 
  1st authentication server  = local 
  Authentication exit-on-fail: Enabled 
 
Notes > Why “local”? 
The keywork “local” in “1st authentication server = local” means that the local database will be the first 
database to be polled for authentication information.  
 
 
Tips 
If the SSH service type has Authentication = denied, type the command: 
-> aaa authentication ssh local 
2.2. 
Testing the SSH connection 
- Test the SSH connection (by using the Teraterm software available in Windows Start button> Tera Term > 
Tera Term):  
 
* Example with switch 3 pod 5

<<<PAGE 58>>>
5 
Remote Switch Access 
 
- Enter the following credentials: 
 
 
 
- You are now connected to the OS6560-A via SSH:  
 
 
 
2.2.1. 
Configuring the OmniSwitch  
- First, we are going to change the Inactivity Timer  
 
- 
Change the value of Inactivity Timer to “60”  
 
- Save the modification in the running directory  
sw3 (6560-A) -> session cli timeout 60 
 
sw3 (6560-A) -> write memory 
 
File /flash/working/vcsetup.cfg replaced. 
File /flash/working/vcboot.cfg replaced. 
 
 
sw3 (6560-A) -> show session config 
Cli Default Prompt               = sw3 (6560-A) ->, 
Cli Banner File Name             = , 
Cli Inactivity Timer in minutes  = 60, 
Ftp Banner File Name             = , 
Ftp Inactivity Timer in minutes  = 4, 
Http Inactivity Timer in minutes = 4, 
Http Banner File Name            = , 
Login Timer in seconds           = 55, 
Maximum number of Login Attempts = 3,

<<<PAGE 59>>>
6 
Remote Switch Access 
 
 3 
Accessing to the WebView 
The OmniSwitch can also be monitored and configured by using the WebView (Alcatel-Lucent Enterprise’s web-
based device management tool). The WebView application is embedded in the OmniSwitch and is accessible via 
a web browser. 
3.1. 
Setting up the HTTP Session  
- Check that the HTTP service is enabled (ex. 6560-A): 
Pod11sw3 login: admin 
Password: switch 
 
Sw3 (6560-A) -> show aaa authentication 
[/TRUNCATED] 
Service type = Http 
  Authentication = Use Default, 
  1rst authentication server = local 
  Authentication exit-on-fail: Enabled 
[/TRUNCATED] 
 
- 
As you can see here, HTTP authentication is enabled, and the first authentication server to be polled is 
the local database.  
 
 
Notes 
By default, the WebView is enabled on the OmniSwitch, but you are not allowed to authenticate.  
On the Remote-Lab, the WebView access has already been enabled. 
It is possible to disable it with the command: no aaa authentication http 
 
- Check the WebView status:  
 
sw3 (6560-A) -> show webview 
WebView Server = Enabled, 
WebView Access = Enabled, 
WebView Force-SSL = Enabled, 
WebView HTTPS-Port = 443 
 
 
Tips 
SSL is forced by default in Release 8. It means that you can’t connect with plain HTTP on R8 OmniSwitches, you 
will be automatically redirected to an HTTPS connection. 
3.2. 
Opening the WebView  
- From the Windows Desktop, open a Web Browser (ex. Firefox, Chrome) 
- In the URL area, type https://<IP address of OS6560-A> (10.4.Pod#.3)

<<<PAGE 60>>>
7 
Remote Switch Access 
 
- Login to the WebView with the admin credentials: 
 
User Name : admin 
Password : switch 
Language : English 
 
After a successful connection, the dashboard page appears 
The switch configuration is divided into seven main configuration groups 
- Physical,  
- Layer 2,  
- Networking 
- Service management, 
- Security 
- Quality of service 
- Device management. 
3.3. 
Configuring the OmniSwitch from the WebView 
- First, we are going to change the Inactivity Timer from the WebView. 
- From the horizontal menu bar at the top of the page, select Security > ASA, then click Session and then 
Configuration. 
 
 
 
Change the value to "45 for the CLI interface and “15” for the Webview" then click on Apply at the 
bottom of the page 
 
- From the CLI, check that the modification has been taken into account: 
sw3 (6560-A) -> show session config 
Cli Default Prompt               = sw3 (6560-A) ->, 
Cli Banner File Name             = , 
Cli Inactivity Timer in minutes  = 45, 
Ftp Banner File Name             = , 
Ftp Inactivity Timer in minutes  = 4, 
Http Inactivity Timer in minutes = 15, 
Http Banner File Name            = , 
Login Timer in seconds           = 55, 
Maximum number of Login Attempts = 3, 
 
- Return to the Webview application. In the horizontal icon bar at the top of the page, select the third icon 
from the left (write memory).

<<<PAGE 61>>>
8 
Remote Switch Access 
 
- Click yes to save the modification in the active directory (running). 
 
3.4. 
Visualize your chassis 
- In the horizontal menu bar at the top of the page, select Physical, then in the "Chassis management" 
column, click on "Chassis visualization". 
 
- You can hover with your mouse over the ports to get more information By clicking on a port you will be 
redirected to the chassis port configuration page.

<<<PAGE 62>>>
9 
Remote Switch Access 
 
3.5. 
Creating a VLAN from the WebView 
- Select Layer 2 > VLAN in the VLAN management column or in the left menu. 
- Click on the "+" icon to create a new VLAN 
- The table of the vlan created on the switch is displayed. 
 
 
 
Vlan :  59 
Description : Student 
- Click on SUBMIT and the new VLAN 59 is displayed in the table 
 
- Connect to the OmniSwitch 6560-A and verify that the VLAN has been created on the OmniSwitch: 
 
sw3 (6560-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Dis   Dis    1500    VLAN 1 
59     std       Ena     Dis   Dis    1500    student 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC

<<<PAGE 63>>>
10 
Remote Switch Access 
 
3.6. 
Deleting a VLAN from the WebView 
- Select Layer 2 > VLAN Mgmt in the left-hand me 
- Select the VLAN(s) to be deleted from the table (e.g. VLAN 59) 
- Click on the " trashbin " icon to the right 
 
 
- Click on yes 
 
- In the CLI of the OmniSwitch 6560-A, verify that the VLANs have been deleted and save it on flash running 
directory 
 
sw3 (6560-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Dis   Dis    1500    VLAN 1 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
sw3 (6560-A) -> write memory 
 
File /flash/working/vcsetup.cfg replaced. 
File /flash/working/vcboot.cfg replaced.

<<<PAGE 64>>>
MANAGING FILES/DIRECTORIES
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 65>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the specificities of the OmniSwitch 
switch bootup process
• Describe the OmniSwitch directories 
architecture
• List the OmniSwitch Command Line Interface 
(CLI) specificities

<<<PAGE 66>>>
RELEASE 8 OMNISWITCHES
AOS RELEASE 8
OMNISWITCH 6860E/N
OMNISWITCH 6560
OMNISWITCH 6360
OMNISWITCH 6865
OMNISWITCH 9900
OMNISWITCH 6900
OMNISWITCH 6465
HARDENED SWITCHES
OS6570M (GIGABIT METRO ETHERNET)
OMNISWITCH 6870

<<<PAGE 67>>>
AOS MANAGING FILES/DIRECTORIES 
• Rollback Based on the working, certified and User-defined 
directories
• Additional User-defined directories
•
Created by the user (any name)
•
Can be used to store additional switch configurations.
•
Configuration changes CAN be saved directly to any user-
defined directory
R8
FLASH MEMORY
WORKING
CERTIFIED
NETWORK
Uosn.img
vcboot.cfg
vcsetup.cfg
Uosn.img
vcboot.cfg
vcsetup.cfg
Policy.cfg
log_Files *
USER. DIR.
Uosn.img
vcboot.cfg
vcsetup.cfg
USER DEFINED DIR
* swlog_chassis1. to 1.6 
files and swlog_archive
(max 40 files)
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

<<<PAGE 68>>>
AOS MANAGING FILES/DIRECTORIES 
• System Boot Sequence 
• Bootstrap Basic Operation (U-Boot)
• Hardware Initialization
• Memory Diagnostics
• Image selection 
• AOS is copied and loaded into RAM
• The image contains its own copy of 
the kernel specific to the SW version
BOOTROM
ROOT DIR
WORKING
DIR.
CERTIFIED
DIR.
Flash
RAM
BOOT (KERNEL)
1
2
4
3
IMAGE
SELECTION
KERNEL.LNK FROM
OS PACKAGE
KERNEL.LNK FROM
OS PACKAGE
KERNEL.LNK FROM
OS PACKAGE
USER DEFINED
DIR.
RUNNING DIRECTORY
R8

<<<PAGE 69>>>
AOS MANAGING FILES/DIRECTORIES 
FLASH MEMORY
WORKING
USER. DIR.
OR
RAM
WORKING
RUNNING CONFIGURATION
BOOT FROM THE
WORKING DIRECTORY
OR FROM THE USER
DEFINED DIRECTORY
FLASH MEMORY
WORKING
CERTIFIED
≠
RAM
CERTIFIED
DIFFERENT CONTENT
Command to force reboot from CERTIFIED  directory: 
-> reload all
CERTIFIED
=
USER. DIR.
OR
Command to force reboot from WORKING directory or user defined directory:
-> reload from working no rollback-timeout
-> reload from <userdefined> no rollback-timeout
FLASH MEMORY
USER. DIR.
CERTIFIED
≠
RAM
CERTIFIED
DIFFERENT CONTENT
RUNNING CONFIGURATION
RUNNING CONFIGURATION
R8

<<<PAGE 70>>>
AOS MANAGING FILES/DIRECTORIES 
Configuration Rollback
WORKING & CERTIFIED directory are different
RAM content is different from the WORKING 
directory content
WORKING and CERTIFIED directories content are 
still different
The content of the RAM memory and WORKING 
directory are similar (synchronized)
sw7 (OS6860-A) -> write memory
For example : a configuration done on RAM but not save on flash. Lost in 
case of reboot
* Running configuration (RAM): current operating configuration of the switch retrieved from the running 
directory in addition to any configuration changes made by the user.
* Except when the Running directory is the Certified directory
Directory which the switch booted from and 
where the configuration changes will be 
saved
R8

<<<PAGE 71>>>
AOS MANAGING FILES/DIRECTORIES 
Configuration Rollback
sw7 (OS6860-A) -> copy running certified
WORKING and CERTIFIED directory are still
different
WORKING and CERTIFIED directory are similar
sw7 (OS6860-A) -> write memory flash-synchro  = write memory + copy running certified
R8

<<<PAGE 72>>>
AOS MANAGING FILES/DIRECTORIES 
Loads and certifies the images in the WORKING directory on the next reload 
or power cycle : certify-on-reboot
At next login only,                            to have it persistent
R8

<<<PAGE 73>>>
AOS MANAGING FILES/DIRECTORIES 
• When the switch boots from the CERTIFIED
directory, changes made to the switch cannot
be saved and files cannot be moved between
directories. 
FLASH MEMORY
WORKING
CERTIFIED
≠
RAM
RUNNING CONFIGURATION
CERTIFIED
DIFFERENT CONTENT
FLASH MEMORY
USER. DIR.
CERTIFIED
≠
RAM
RUNNING CONFIGURATION
CERTIFIED
DIFFERENT CONTENT
1
1
2
2
3
4
5
R8

<<<PAGE 74>>>
CONFIGURATION BACKUP & RESTORE
• Configuration Backup
• Backup of the session banner, userTable* and vcboot.cfg files
• The configuration backup command creates a .tar file where are stored the collected files 
• The tar file name is “configuration_backup.tar” and will be placed in “/flash/config-backup-
recovery” folder
• Up to 10 .tar files can be stored in the /flash/config-backup-recovery directory
• Configuration Restore
• When the “restore” option is used, the switch: 
• Selects the “configuration_backup.tar” file in “/flash/config-backup-recovery” folder 
• Extract the .tar file to get the userTable, session banner, and vcboot.cfg files. 
R8

<<<PAGE 75>>>
AOS MANAGING FILES/DIRECTORIES 
• USB Backup and Restore
• If a USB drive is plugged in, switch will store image files, power supply and system configuration 
files to USB storage drive automatically upon user commands “write memory” or “copy running-
certified” “copy flash-synchro” if USB backup is enabled on switch. 
• The USB drive can be used to restore images and config (power supply and system) from the USB 
drive on a switch with usb auto-copy command enabled.
• If the user configures a password at the time of enabling the back-up and restore, then the 
corresponding back-up and restore content will be encrypted and decrypted.
R8
usb backup admin-state {enable | disable}  [key <> | hash-key<>]
usb auto-copy <enable | disable> copy-config <enable| disable> from <directory-path> 
[key <> | hash-key<>]

<<<PAGE 76>>>
THIN CLIENT OMNISWITCH 
• No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the 
config.
• Thin-client mode is configured through the activation process. 
• Switch boots up normally and registers to OV 2500 as part of the activation process. 
• Thin-client mode must be configured as part of the activation response message.
• In thin-client mode, no configuration is saved in the ‘running’ directory
• But there will be vcboot.cfg with the minimal network reachability configuration.
• ‘write memory’ can be executed but configurations will not be saved to the vcboot,cfg file. 
• All configuration changes should be done in OV 2500.
OmniVista 2500
Callhome
Sends Config
R8

<<<PAGE 77>>>
CLI – HELP > QUICK WALKTHROUGH
• Command Line Interface (CLI) specifications
• Configuration methods
• Online Configuration via real-time session using CLI commands
• Offline configuration using text file containing CLI commands
• Command Capture Feature
• Snapshot feature captures switch configuration in a text file
Directory management commands
pwd – shows current directory.
cd – changes directory.
mkdir – creates a new directory.
ls – lists contents of a directory.
dir – lists contents of a directory.
mv – moves a file. 
cp – copies a file.
rm – removes a file.
CLI Line Editor and History
-> history
1 write memory
2 show running-directory
3 ls /flash/working
4 show microcode working
5 show microcode certified
6 ls /flash/working
Completion
Recognize partial keywords to CLI command syntax.
Eg : sh vl for show vlan
Built-in Filtering
-> show vlans | more
-> show mac-learning | grep 00:20:da:55:56:76
-> show ip ospf routes | egrep "^10\.10.*" | sort | less
Online Help
A ‘?’ can be used to get a list of all possible commands
or
-> v?
VIEW VI
-> vlan ? 
PORT NO IPMVLAN 802.1Q <vid> <vlan1-vlan2>
R8

<<<PAGE 78>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 79>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
OmniSwitches Directories Content (R8) 
How to 
✓ Manage the OmniSwitches R8 main directories content 
Contents 
1 
Introduction .................................................................................... 2 
2 
Viewing the Image & Configuration Files .................................................. 2 
3 
Checking the working and certified Directories .......................................... 2 
3.1. Displaying the working and certified directories content .................................... 2 
3.2. Displaying the microcode version ................................................................ 3 
4 
Booting behavior in Release 8 ............................................................... 3 
5 
Determining from which directory the switch was loaded? ............................. 3 
6 
Synchronizing RAM and Running Directory ................................................. 4 
7 
Saving the Running Configuration to Working Directory ................................. 5 
8 
Creating a User-Defined Directory .......................................................... 7 
9 
Deleting the User Directory .................................................................. 8 
10 
Annex: USB Backup & Restore ............................................................... 8

<<<PAGE 80>>>
2 
OmniSwitches Directories Content (R8) 
 
 1 
Introduction 
In Release 8, the management of an OmniSwitch is controlled by 2 types of files: 
- 
Images files, which are proprietary code developed by Alcatel-Lucent Enterprise to run the hardware.  
- 
A configuration files, named vcboot.cfg and vcsetup.cfg, in text format, sets and controls the 
configurable functions. 
 
The directory structure that store the image and configuration files is divided in several parts:  
- 
The certified directory contains files that have been certified by an authorized user as the default files 
for the switch.  
- 
The working directory is a holding place for new files. Files in the working directory must be tested 
before committing them to the certified directory.  
- 
The user-defined directories are created by the user and are like the working directory in that they can 
contain image and configuration files.  
 
- 
The running directory is the directory where the configuration changes will be saved.  
- 
The running configuration, stored in the RAM, contains the current operating parameters of the 
OmniSwitch obtained from the image and configuration files.  
 2 
Viewing the Image & Configuration Files 
- 
Logging into the OmniSwitch 
o 
Open the OS6560-A serial console (shortcut available on the Windows desktop). 
o 
Use following authentication credentials: 
Login: admin 
Password: switch 
 3 
Checking the working and certified Directories 
3.1. 
Displaying the working and certified directories content 
- 
Check the files that are in each directory by entering the following: 
sw3 (6560-A) -> ls -l /flash/working |or| ls -l /flash/certified    
total 109220 
-rw-r--r--    1 admin    user     111683640 Sep 26 01:04 Nos.img 
-rw-------    1 root     root            46 Nov  3 03:17 boot.md5 
-rwxr-xr-x    1 admin    user           153 Nov  3 03:17 cloudagent.cfg 
-rw-r--r--    1 admin    user           237 Jun 11  2016 cspbroker.conf 
-rw-r--r--    1 admin    user            74 Sep  1  2015 imgsha256sum 
drwxr-xr-x    4 admin    user          4096 Jun  1 02:18 pkg 
- rw-r--r--    1 admin    user          2787 Nov  3 03:15 vcboot.cfg 
-rw-r--r--    1 admin    user           209 Nov  3 03:15 vcsetup.cfg

<<<PAGE 81>>>
3 
OmniSwitches Directories Content (R8) 
 
3.2. 
Displaying the microcode version 
- 
To display the microcode version installed on the OmniSwitch: 
sw3 (6560-A) -> show microcode working |or| show microcode certified |or| show microcode loaded 
   /flash/working 
   Package           Release                 Size     Description 
-----------------+-------------------------+---------+----------------------------------- 
Nos.img           8.7.98.R03                111683640 Alcatel-Lucent OS 
 
Notes: “Loaded”? 
- Loaded displays the currently active microcode versions.  
- Entering the command show microcode also displays the currently active microcode version.  
 4 
Booting behavior in Release 8 
 
- 
At the time of a normal boot (cold start):  
- 
The switch will reboot from certified directory if contents (images and vcboot.cfg) are different from 
the running directory (which can be the working directory, or a user-defined directory).  
- 
If contents are the same, the switch will reboot from the running directory (which can be the working 
directory, or a user-defined directory). 
 
 
Warning > The “reload all” command particularity 
IF THE OMNISWITCH IS REBOOTED WITH THE “RELOAD ALL” COMMAND, IT WILL REBOOT FROM THE CERTIFIED 
DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS (SAME/DIFFERENT THAN THE 
CERTIFIED DIRECTORY CONTENT)  
 
- If the running directory is the certified directory, you will not be able to save any changes made to the 
running directory. If the switch reboots, any configuration changes will be lost. In order to save 
configuration changes, the running directory cannot be the certified directory. 
 5 
Determining from which directory the switch was loaded? 
When a switch boots the RUNNING CONFIGURATION will come from either the certified, working, or 
a user-defined directory. A switch can be rebooted to run from any directory using the reload from command. 
 
To check from which directory the OmniSwitch is running, and the content comparison between the WORKING 
and CERTIFIED directories:  
sw3 (6560-A) -> show running-directory 
 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : WORKING, 
  Certify/Restore Status   : CERTIFIED 
SYNCHRONIZATION STATUS 
  Running Configuration    : SYNCHRONIZED 
 
 
- 
Running configuration: WORKING > the OmniSwitch is running from the working directory.  
- 
Certify/Restore Status: CERTIFIED > the working directory content matches the certified directory 
content.  
- 
Running Configuration: SYNCHRONIZED > the running configuration matches the WORKING configuration.

<<<PAGE 82>>>
4 
OmniSwitches Directories Content (R8) 
 
 6 
Synchronizing RAM and Running Directory 
Perform some configuration to make the running configuration different from the configuration stored in the 
working and certified directories. Observe what happens.  
 
- 
Performing modifications in the configuration 
o 
Create 3 new VLANs (2, 3, and 99): 
 
sw3 (6560-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Dis   Dis    1500    VLAN 1 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
 
sw3 (6560-A) -> vlan 2 
sw3 (6560-A) -> vlan 3 
sw3 (6560-A) -> vlan 99 
 
sw3 (6560-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Dis   Dis    1500    VLAN 1 
2      std       Ena     Dis   Dis    1500    VLAN 2 
3      std       Ena     Dis   Dis    1500    VLAN 3 
99     std       Ena     Dis   Dis    1500    VLAN 99 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
 
 
- 
3 new VLANs are now created. Changes are made to the configuration file in RAM. These changes take 
effect immediately but are not written permanently; they will be lost if the OmniSwitch reboots.  
 
sw3 (6560-A) -> show running-directory 
 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : WORKING, 
  Certify/Restore Status   : CERTIFIED 
SYNCHRONIZATION STATUS 
  Running Configuration    : NOT SYNCHRONIZED 
 
- 
Running configuration: WORKING > the OmniSwitch is running from the WORKING directory.  
- 
Certify/Restore Status: CERTIFIED > the working directory content matches the certified directory 
content. 
- 
Running Configuration: NOT SYNCHRONIZED > the running configuration does not match the 
configuration of the working directory. 
 
 
Warning > What if the OmniSwitch reboots now? 
IF THE OMNISWITCH IS REBOOTED NOW (VIA A COMMAND RELOAD FROM WORKING … OR IF POWER TO THE 
OMNISWITCH IS INTERRUPTED), THE OMNISWITCH WILL BOOT, ALL THE CHANGES IN THE RUNNING 
CONFIGURATION WILL BE OVERWRITTEN, AND THE OMNISWITCH WILL ROLL BACK TO THE WORKING DIRECTORY, 
SINCE THE WORKING AND CERTIFIED DIRECTORIES ARE THE SAME.  
 
IN OUR CASE, THE VLAN 2, 3 AND 99 WILL BE LOST, AS THEY ARE NOW STORED IN THE RUNNING 
CONFIGURATION.

<<<PAGE 83>>>
5 
OmniSwitches Directories Content (R8) 
 
 7 
Saving the Running Configuration to Working Directory 
Save the configuration (VLANs created previously) from the running directory to the working directory. Verify it 
by using CLI commands.  
 
- 
To save the running configuration to the working directory: 
sw3 (6560-A) -> write memory 
 
File /flash/working/vcsetup.cfg replaced. 
 
File /flash/working/vcboot.cfg replaced. 
 
 
- 
To check that:  
sw3 (6560-A) -> show running-directory 
 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : WORKING, 
  Certify/Restore Status   : CERTIFY NEEDED 
SYNCHRONIZATION STATUS 
  Running Configuration    : SYNCHRONIZED 
 
- 
Running configuration: WORKING > the OmniSwitch is running from the working directory.  
- 
Certify/Restore Status: CERTIFY NEEDED > the WORKING directory does not match the CERTIFIED 
directory. 
- 
Running Configuration: SYNCHRONIZED > the running configuration matches the configuration of the 
working directory. 
 
 
 
 
Warning > What if the OmniSwitch reboots now? 
IF THE OMNISWITCH IS REBOOTED NOW (VIA A COMMAND RELOAD ALL OR IF POWER TO THE OMNISWITCH IS 
INTERRUPTED), THE OMNISWITCH WILL BOOT FROM THE CERTIFIED DIRECTORY, ALL THE CHANGES IN THE 
RUNNING CONFIGURATION WILL BE OVERWRITTEN, AND THE OMNISWITCH WILL ROLL BACK TO THE CERTIFIED 
DIRECTORY.  
 
HOWEVER, SINCE THE CONFIGURATION FILE WAS SAVED TO THE WORKING DIRECTORY, THAT FILE IS STILL IN 
THE WORKING DIRECTORY AND CAN BE RETRIEVED.  
 
SINCE THE WORKING AND CERTIFIED DIRECTORIES ARE NOT THE SAME, THE OMNISWITCH WILL BE RUNNING 
FROM THE CERTIFIED DIRECTORY.  
 
 
- 
Let’s reboot the OmniSwitch and see what happens: 
sw3 (6560-A) -> reload all 
Only one reload may be active in VC mode, other scheduled reloads will be canceled 
Confirm Reload All (Y/N) : y 
 
This operation will verify and copy images before reloading. 
It may take several minutes to complete.

<<<PAGE 84>>>
6 
OmniSwitches Directories Content (R8) 
 
sw3 (6560-A) -> show running-directory 
 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : CERTIFIED, 
  Certify/Restore Status   : CERTIFIED 
SYNCHRONIZATION STATUS 
  Running Configuration    : SYNCHRONIZED 
 
sw3 (6560-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Dis   Dis    1500    VLAN 1 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
- Note that when an OmniSwitch is running from the CERTIFIED directory, it is not possible to manipulate 
files in the directory structure (i.e. a configuration will be applied in the running configuration, but it 
will not be possible to save it neither in the working nor the certify directory):  
sw3 (6560-A) -> vlan 4 
sw3 (6560-A) -> write memory 
ERROR: Write memory is not permitted when switch is running in certified mode 
- 
Let’s reboot the OmniSwitch on Working directory where vlan have been recorded: 
sw3 (6560-A) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y 
This operation will verify and copy images before reloading. 
It may take several minutes to complete... 
- 
Let’s check if the vlan are present 
sw3 (6560-A) -> show running-directory 
 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : WORKING, 
  Certify/Restore Status   : CERTIFY NEEDED 
SYNCHRONIZATION STATUS 
  Running Configuration    : SYNCHRONIZED 
 
sw3 (6560-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Dis   Dis    1500    VLAN 1 
2      std       Ena     Dis   Dis    1500    VLAN 2 
3      std       Ena     Dis   Dis    1500    VLAN 3 
99     std       Ena     Dis   Dis    1500    VLAN 99 
4094     cm       Ena     Dis   Dis    1500    VCM IPC

<<<PAGE 85>>>
7 
OmniSwitches Directories Content (R8) 
 
 8 
Creating a User-Defined Directory 
User-defined directories are like the working directory in that they can contain image and configuration files. 
These directories can have any name and can be used to store additional switch configurations. Configuration 
changes CAN be saved directly to any user-defined directory. 
 
 
- 
Create a user defined directory and copy the contents of the WORKING directory to it: 
 
sw3 (6560-A) -> mkdir lab 
sw3 (6560-A) -> cp working/*.* lab 
cp: can't open 'working/boot.md5': Permission denied 
 
 
Tips 
The lab directory may have been already created, ignore error and proceed on. 
During the copy; it tries to copy the boot.md5 file but a “permission denied” message is displayed. This file is 
auto generated so ignore this error and proceed. 
- 
Now let’s see what files are stored in the newly created directory: 
sw3 (6560-A) -> ls lab 
Nos.img         cspbroker.conf  vcboot.cfg.sav 
cloudagent.cfg  vcboot.cfg      vcsetup.cfg 
 
- 
Boot the switch from the new user-defined directory (lab): 
sw3 (6560-A) -> reload from lab no rollback-timeout 
Confirm Activate (Y/N): y 
 
- 
Once the switch boots, verify that it booted from the lab directory:  
sw3 (6560-A) -> show running-directory 
 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : lab, 
  Certify/Restore Status   : CERTIFY NEEDED 
SYNCHRONIZATION STATUS 
  Running Configuration    : SYNCHRONIZED 
 
- 
Running configuration: lab > the OmniSwitch is running from the user-defined lab.  
- 
Certify/Restore Status: CERTIFY NEEDED > the running directory (“lab”) does not match the CERTIFIED 
directory.  
- 
Running Configuration: SYNCHRONIZED > the running configuration matches the configuration stored in 
the running directory (here the user-defined “lab” directory) 
 
 
 
Warning > What if the OmniSwitch reboots now? 
IF THE OMNISWITCH IS REBOOTED (IF THE POWER TO THE OMNISWITCH IS INTERRUPTED), THE OMNISWITCH 
WILL BOOT FROM THE CERTIFIED DIRECTORY, SINCE THE RUNNING (LAB) AND CERTIFIED DIRECTORIES ARE NOT 
THE SAME (Certify/Restore Status: CERTIFY NEEDED).  
 
- 
Overwrite the contents of the certified directory with the configuration from the running directory 
(“lab” directory here):  
sw3 (6560-A) -> copy running certified 
Wed Apr  2 04:22:40 : flashManager FlashMgr Main INFO message: 
+++ Verifying image directory lab on CMM flash 
Wed Apr  2 04:23:04 : ChassisSupervisor MipMgr INFO message: 
+++ Copy running to certified succeeded

<<<PAGE 86>>>
8 
OmniSwitches Directories Content (R8) 
 
 
 
Notes  
The copy running certified command should only be done if the running configuration has been verified. 
 
- Check the synchronization status: 
sw3 (6560-A) -> show running-directory 
CONFIGURATION STATUS 
  Running CMM              : MASTER-PRIMARY, 
  CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
  Current CMM Slot         : CHASSIS-1 A, 
  Running configuration    : lab, 
  Certify/Restore Status   : CERTIFIED 
SYNCHRONIZATION STATUS 
  Running Configuration    : SYNCHRONIZED 
 
- 
Running configuration: lab > the OmniSwitch is running from the user-defined lab.  
- 
Certify/Restore Status: CERTIFIED > the running directory (“lab”) matches the CERTIFIED directory.  
- 
Running Configuration: SYNCHRONIZED > the running configuration matches the configuration stored in 
the running directory (here the user-defined “lab” directory) 
 
Warning > What if the OmniSwitch reboots now? 
IF THE OMNISWITCH IS REBOOTED (IF THE POWER TO THE OMNISWITCH IS INTERRUPTED), THE OMNISWITCH 
WILL BOOT FROM THE “LAB” DIRECTORY, SINCE THE RUNNING (LAB) AND CERTIFIED DIRECTORIES ARE THE SAME 
(Certify/Restore Status: CERTIFIED).  
 9 
Deleting the User Directory 
- Delete lab directory  : 
sw3 (6560-A) -> rm -Rf lab 
sw3 (6560-A) -> ls -l lab 
ls: lab: No such file or directory 
- Reload the switch from « working » directory  : 
sw3 (6560-A) -> reload from working no rollback-timeout 
 10 
Annex: USB Backup & Restore 
In Release 8, it is also possible to backup the images and configuration from certified and running directories 
into a USB key (/uflash/6860/certified and /uflash/6860/running directories). 
 
Here is an example of a USB backup. This exercise cannot be done on the remote lab. The USB port is used to 
connect the USB-to-Eth dongle 
 
- 
To enable access to the device connected to the USB port: 
sw3 (6560-A) -> usb enable 
 
Tue Aug 14 14:00:26 : uflash uflashMain INFO message: 
+++ /uflash interface enable 
Mounting /dev/sdb1 
+++ /uflash mounted 
 
Tue Aug 14 14:00:26 : SSAPP main INFO message: 
+++ CAUTION: Do usb disable before removing usb 
WARNING: CAUTION: Do usb disable before removing usb

<<<PAGE 87>>>
9 
OmniSwitches Directories Content (R8) 
 
 
- 
To enable the USB backup feature on the switch:  
sw3 (6560-A) -> usb backup admin-state enable 
 
Tue Aug 14 14:01:00 : SSAPP main INFO message: 
+++ Received SET for Admin State 
+++ Just before calling /bin/uflashUtils usbBackUpEnable 
 
Tue Aug 14 14:01:00 : uflash uflashMain INFO message: 
+++ /uflash back up enable 
+++ USB back-up Started 
+++ /flash/certified backup to USB  started 
 
sw3 (6560-A) -> 
Tue Aug 14 14:01:50 : uflash uflashMain INFO message: 
+++ /flash/certified backup completed 
+++ /flash/working backup to USB  started 
 
Tue Aug 14 14:02:39 : uflash uflashMain INFO message: 
+++ /flash/working backup completed 
+++ USB backup completed 
 
- 
When this command is enabled, the images and configuration from certified and running directories are 
copied into /uflash/6560/certified and /uflash/6560/running directories. 
 
 
 
 
 
 
- 
When write memory is executed and backup is enabled, the configuration files and images from 
/flash/<running-directory> are copied to /uflash/6560/<running-directory name> (ex. lab) 
 
sw3 (6560-A) -> write memory 
 
File /flash/working/vcsetup.cfg replaced. 
 
File /flash/working/vcsetup.cfg saved to USB. 
 
Tue Aug 14 14:03:20 : SSAPP main INFO message: 
+++ Received SET for Admin State 
 
File /flash/working/vcboot.cfg replaced. 
 
File /flash/working/vcboot.cfg saved to USB.

<<<PAGE 88>>>
10 
OmniSwitches Directories Content (R8) 
 
- 
When usb backup admin-state is enabled and copy running certified and write memory flash-synchro 
commands are executed, the configuration and images from /flash/certified will be copied to 
/uflash/6560/certified: 
sw3 (6560-A) -> write memory flash-synchro 
 
File /flash/working/vcsetup.cfg replaced. 
 
File /flash/working/vcsetup.cfg saved to USB. 
 
Tue Aug 14 14:03:32 : SSAPP main INFO message: 
+++ Received SET for Admin State 
 
File /flash/working/vcboot.cfg replaced. 
 
File /flash/working/vcboot.cfg saved to USB. 
 
Tue Aug 14 14:03:32 : flashManager FlashMgr Main INFO message: 
+++ Verifying image directory working on CMM flash 
Please wait... 
 
Tue Aug 14 14:03:48 : flashManager FlashMgr Main INFO message: 
+++ Image file Nos.img differs - copying file 
 
Tue Aug 14 14:04:10 : flashManager FlashMgr Main INFO message: 
+++ Starting USB backup 
 
Tue Aug 14 14:04:10 : ChassisSupervisor MipMgr INFO message: 
+++ Copy running to certified succeeded 
- 
To check the USB (uflash directory) content:  
sw3 (6560-A) -> cd /uflash 
sw3 (6560-A) -> ls 
6560                       System Volume Information 
sw3 (6560-A) -> cd 6560 
sw3 (6560-A) -> ls 
certified  working 
sw3 (6560-A) -> cd working 
sw3 (6560-A) -> ls 
Nos.img      vcboot.cfg   vcsetup.cfg 
sw3 (6560-A) -> cd .. 
sw3 (6560-A) -> ls 
certified  working 
sw3 (6560-A) -> cd certified 
sw3 (6560-A) -> ls 
Nos.img      vcboot.cfg   vcsetup.cfg

<<<PAGE 89>>>
VIRTUAL CHASSIS
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 90>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• List the Virtual Chassis benefits
• Identify the Virtual Chassis specificities per 
switch model
• List the different start up use case
• Summarize the Virtual Chassis configuration 
steps
• List the synchronization steps occurring on a 
switch which is part of a Virtual Chassis

<<<PAGE 91>>>
VIRTUAL CHASSIS – OVERVIEW 
• Goal
• Virtual Chassis = Group of switches which appears
as a single router or bridge
• Key Points
• Single Point of management 
• Single Logical Switch
• Redundancy and resiliency supported across the 
switches
• No STP/VRRP between Access and Core switches
• Optimized bandwidth usage
• Upgrade via ISSU (to minimize network impact)
• No license needed
• How It Works?
• Switches inter-connected via dedicated or optional 
SFP+, QSFP ports
• Mesh or Ring topology
4
5
3
6
1
2
2
3
4
5
1
8
7
8
VFL
VFL
Master
Master
Slave

<<<PAGE 92>>>
VIRTUAL CHASSIS - TOPOLOGIES
OS6465
Up to 2 VFL stacking ports 
1G SFP ports (model P6/P12)
1G/10G SFP+ ports
(model P28, TE28)
4 x OS6465
OS6560
Up to 2 VFL member ports 
Local stacking via dedicated 
20G VFL ports 
and/or Remote stacking via 
the 2 last 10G SFP+ ports
8 x OS6560
8 x OS6865/OS6860/E/N
2 x OS9900
OS6570M
6570M-12(D)/-U28
2x1G/10G SFP+ uplink
ports/VFL
8 x OS6570
OS6360
Up to 2 stacking SFP ports
10G VFL ports
4 x OS6360
8 x OS6360
On 24/48 
ports models
OS9900
Up to 8 VFL member 
ports
For 10Gbps 
OS99-XNI-U24/48
Native 40G QSFP on CMM with
40G-to-10G splitter cable
For 40Gbps 
OS99-CNI-U8/U20
OS99-XNI-U12Q
OS99-XNI-P12Q
Native 40G QSFP ports on 
CMM
2 x 2 ports
For 100Gbps
OS99-CNI-U8/U20
Native QSFP28 ports
Up to 8 VFL member ports 
Local stacking via 
dedicated 20/40/100G VFL ports 
and/or Remote stacking via 
10G SFP+ ports (non N-models)
OS6860E/N/OS6865
On 10 ports 
models
8 x OS6870
VFL ports 2 x 40G/100G/200G 
QSFP56
OS6870

<<<PAGE 93>>>
VIRTUAL CHASSIS - TOPOLOGIES
Up to 16 VFL member ports
For 10Gbps
Native 10G SFP+ ports
4 x 10G SFP+ with 40G-to-10G splitter cable on native QSFP 
ports
For 40Gbps 
Native 40G QSFP ports
OS6900
Support of 2,3,.. up to 6 in Partial or fully Mesh topology
OS6900-Q32  /  OS6900-X72
VFL
Up to 16 VFL member ports
For 40Gbps 
Native 40G QSFP+
For 100Gbps
Native QSFP28 ports
OS6900-V72  /  OS6900-C32
•
OS6900-X20/X40/T20/T40/Q32/X72
models can be mixed in a VC of up to 6 elements
•   OS6900-V72/C32(E)/X48C6/T48C6/V48C8/X24C2/T24C2/X48C4E*                                                           
models can be mixed in a VC of up to 6 elements
OS6900-X/T48C6/X48C6/V48C8/C32E/X24C2/T24C2/X48C4E
Up to 16 VFL member ports
10G SFP+ or 40Gbps 
Native 40G QSFP+
For 100Gbps
Native QSFP28 ports
* requires AOS 8.9R4 minimum
New command introduced when adding a 6900-X48C4E to a VC :
capability vfl-type {standard | mixed}

<<<PAGE 94>>>
VIRTUAL CHASSIS TOPOLOGY MANAGER
• VC topology managed by ISIS-VC
• Private TLV report the switch’s capability and numbering
• Exchange IS-IS HELLO for adjacencies and updates
• Maintains a loop-free topology for BUM traffic
• Determines the shortest path to each other element
• Builds the topology and maintains a forwarding database 
• Break equal-cost ties in a deterministic manner ala SPBM
I’m Chassis-2, my status is up, my 
role is slave, my master is 1, type X
IS-IS HELLO
OK, chassis-2 is type X. 
Then all work in X mode.
I’m Chassis-1, my status is up, 
type X, my role is master
Master
Slave
1
2
4
5
3
6
Slave
Slave
Slave
Slave

<<<PAGE 95>>>
ROLES AND ELECTIONS
• Master and slaves communicate to ensure that the slaves have up-to date copies of the 
master’s image files and configuration files.
• Reboot required after a slave update (new images and configuration files).
IS-IS VC
Master
Slave
1
2
4
5
3
6
Slave
Slave
Slave
Slave
Master/Slave election 
based on virtual chassis 
protocol (ISIS-VC)
Highest chassis priority value
Longest chassis uptime
(if difference in uptime >10 mn)
Smallest Chassis ID value
Smallest chassis MAC address

<<<PAGE 96>>>
VIRTUAL CHASSIS TAKEOVER/FAILOVER
• Takeover/Failover
• Only master reloads, no impact on slaves, no traffic impact except related to master
• “MAC retention” is always enabled
• When the master reloads or fails, the slaves reelect a new master 
• New master election is locally computed based on known partner keys
• The new master will confirm to its slaves the decision
• When the “original” master comes back, no election will be processed, and the “new” Master will 
retain its Master role
Master
Slave
Master Fails
4
5
3
6
Slave
Slave
Slave
Slave
1
Slave
Master
Recovery of the original Master
4
5
3
6
Slave
Slave
Slave
Slave
2
2
1
Master
New Master elected
4
5
3
6
Slave
Slave
Slave
Slave
2

<<<PAGE 97>>>
VIRTUAL CHASSIS SPECIFICATIONS
Extract from the technical documentation
« OmniSwith AOS Release 8 Specifications Guide »

<<<PAGE 98>>>
VIRTUAL CHASSIS - AUTO VFL PORT
• Goal
• Automatically detect whether an auto VFL port can 
become VFL
• Dynamically assign VFL ID to auto VFL port which can 
become VFL
• Aggregate multiple auto VFL ports that can become 
VFL and are connected to the same remote chassis
• Default set of auto VFL eligible ports
* Auto VFL detection process will run only on auto VFL ports. Both ends 
of the link must be auto VFL ports for an auto VFL port to be able to 
become VFL.
vcsetup.cfg 
exists?
Default set of auto 
VFL eligible ports
(First bootup of brand-new 
chassis from factory)
Auto VFL process 
runs only on port 
explicitly configured 
as auto VFL port
N
Y
Switch Model
Auto VFL eligible ports
OS9900
Static VFL only
OS6900 X and T
Last 5 ports of each chassis (including ports in expansion 
slots) regardless of SFP/QSFP presence on those ports. 
OS6900-V72/C32/X/T48C6 -
The last 5 ports of the chassis.
OS6860 - OS6860N 
Dedicated VFL ports.
OS6465-P28
Ports 27/28.
OS6560-24X4/-P24X4/-48X4/-P48X4 
Dedicated VFL ports and last two 10G SFP+ ports on 
(P)24X4/(P)48X4.
OS6360-24 - OS6360-48
OS6360-24 ports models - Ports 27/28.
OS6360-48 ports models - Ports 51/52.

<<<PAGE 99>>>
VIRTUAL CHASSIS - SPLIT CHASSIS
• Failures on VFL links cause potential MAC/IP  
duplication
• 2 mechanisms
• Out of Band: EMP Remote Chassis Detection (RCD)
• In Band: VC Split Protocol
• EMP Remote Chassis Detection (RCD
• A switch sends an announcement whenever its 
chassis VC information changes
• RCD protocol will detect this split topology.
Virtual Chassis
Master
Slave
Master
RCD use the following IP addresses in order of preference
1. CMM IP address stored in NVRAM (if configured)
2. Chassis EMP IP address
Virtual Chassis
Master
Slave
Reboot with all 
Interfaces 
down
EMP 
port
Management network
RCD 
protocol
Master
EMP 
port
OS6870
OS6860E/N
OS6900
OS9900
The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP 
and chassis MAC addresses in the network.
The Slave's chassis status will be modified from Running to Split-Topology to indicate this 
second pseudo-master chassis is not operational at this point
If the VFL comes back up, the former Slave chassis will reboot and rejoin the virtual chassis 
topology assuming its Slave role again

<<<PAGE 100>>>
VIRTUAL CHASSIS - SPLIT CHASSIS
In Band: VC Split Protocol
SLAVE
MASTER
Link Aggregation
ACCESS
Helper Switch
AOS support
VSCP
Building 1
Building 2
• Requires an upstream or downstream device to act as helper switch
• Proprietary protocol called “VC Split Protocol”
• VCSP LAG towards the helper switch
• Every VC member switch recommended to have one port as part of the 
VCSP LAG to the helper device
SLAVE
MASTER
Link Aggregation
OS6860
ACCESS
MASTER
Building 1
Building 2
Protection Mode
Master role
All Interfaces 
shutdown
Except VFL & LAG
Potential 
duplicate MAC/IP
Helper Switch
Extract from AOS 8.9 R03 CLI Guide
Use the virtual-chassis split-protection admin-state and virtual-chassis split-
protection linkagg commands to enable VCSP and create the VCSP link aggregate 
on the VC.
Use the virtual-chassis split-protection helper admin-state and virtual-chassis 
split-protection helper linkagg commands to enable the VCSP helper and create 
the VCSP helper link aggregate on the helper switch 
Platforms Supported in R8
Extract from OmniSwitch AOS Release 8 Switch Management Guide

<<<PAGE 101>>>
IN SERVICE SOFTWARE UPGRADE (ISSU)
• Goal
• Used to upgrade the software on a VC with minimal 
network disruption
• Each element is upgraded individually
• Step by Step
• Upload new code, vcsetup.cfg and vcboot.cfg
in a new directory (ex. issu_dir)
• Launch the dedicated issu command 
• The image and configuration files are then 
copied to all of the Slaves
• The Slaves are then reloaded from the ISSU 
directory in order from lowest to highest 
chassis ID
Master – Chassis ID 1
issu-dir Directory
vcboot.cfg
vcsetup.cfg
code
Slave – Chassis ID = 2
Issu_dir Directory
vcboot.cfg
vcsetup.cfg
code
Slave – Chassis ID = 3 
Issu_dir Directory
vcboot.cfg
vcsetup.cfg
code
3
2
1

<<<PAGE 102>>>
REMOTE CLI ACCESS THROUGH ANY MEMBER ON A VC
• A user can access to remote CLI console of any 
VC with secure shell protocol (SSH).
ssh-chassis <username>@<chassis-id> 
1
2
User is connected to master chassis (ID =1)
User tries to access chassis ID 2
-> ssh-chassis admin@2
Executing: ssh admin@127.10.2.65
(guest@127.10.2.65) Password: 
-> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology
Local Chassis: 2
Oper
Config   Oper
Chas  Role         Status         Chas ID  Pri
Group   MAC-Address      
-----+------------+---------------+--------+-----+------+------------------
1     Master       Running          1       100   0      2c:fa:a2:61:3a:2d
2     Slave        Running          2       100   0      2c:fa:a2:60:ff:6b

<<<PAGE 103>>>
VIRTUAL CHASSIS - CONFIGURATION

<<<PAGE 104>>>
VIRTUAL CHASSIS CONFIGURATION
Step by Step
• Main use case
N
Y
vcsetup.cfg exists?
AUTO-VC
VC Mode 
VFL : AUTO or 
Static Management
Disable Auto 
configuration
on boot
Auto VC consists of the following: 
1. Auto VFL
2. Auto Chassis ID Assignment
N
Y
Auto Vcsetup
created 
Switch Bootup
VC created automatically 
• Chassis ID and Group ID
(Start in certified mode)

<<<PAGE 105>>>
VIRTUAL CHASSIS CONFIGURATION
Step by Step
• VFL: AUTO or STATIC Management 
Assign a Chassis ID
Assign a Chassis Group ID and a Priority
Configure VFL link & ports -Automatic or static
Restart Chassis to Virtual-Chassis Directory

<<<PAGE 106>>>
VIRTUAL CHASSIS CONFIGURATION
Step by Step
Assign a Chassis Group number
Must be the same on all the switches belonging to the Virtual Chassis
Define a Priority
Between 0 to 255, switch with the highest priority is elected Master
1
2
Chassis 1
Chassis 2
1
2
Chassis 1 (Priority: 200)
Chassis 2 (Priority: 100)
1
Assign a Chassis ID
Assign a Chassis Group ID and a Priority
Assign a Chassis ID
Must be different for each switch belonging to the Virtual Chassis

<<<PAGE 107>>>
Reload both chassis from the directory containing the vcsetup.cfg & vcboot.cfg files
VIRTUAL CHASSIS CONFIGURATION
Step by Step
Create VFL ID
Specify its member ports
Specify ports that are designated as VFLs
and software will automatically assign VFL IDs.
Configure Automatic VFL mode
Reload the switches
Configure Static VFL link & ports
1
2
Chassis 1 (Priority: 100)
Chassis 2 (Priority: 200)
1
VFL
1
2
Chassis 1 (Priority: 100)
Chassis 2 (Priority: 200)
1
VFL
1/2/1
1/2/2
2/2/1
2/2/2

<<<PAGE 108>>>
VIRTUAL CHASSIS SYNCHRONIZATION

<<<PAGE 109>>>
VIRTUAL CHASSIS SYNCHRONIZATION- EXAMPLE
-> write memory
CERTIFIED
RAM
RUNNING
CONFIGURATION
CERTIFIED
CERTIFIED
MASTER
SLAVE
SLAVE
-> show running-directory
CONFIGURATION STATUS
Running CMM              : MASTER-PRIMARY,
CMM Mode                 : VIRTUAL-CHASSIS 
MONO CMM,
Current CMM Slot         : CHASSIS-1 A,
Running configuration    : WORKING,
Certify/Restore Status
: CERTIFY NEEDED
SYNCHRONIZATION STATUS
Flash Between CMMs
: NOT SYNCHRONIZED,
Running Configuration    : SYNCHRONIZED
…
…
WORKING
WORKING
WORKING

<<<PAGE 110>>>
VIRTUAL CHASSIS SYNCHRONIZATION - EXAMPLE
WORKING
CERTIFIED
RAM
RUNNING
CONFIGURATION
…
MASTER
SLAVE
SLAVE
…
-> copy running certified
This command can also be used to synchronize the virtual chassis
-> write memory flash-synchro
-> show running-directory
CONFIGURATION STATUS
Running CMM            : MASTER-PRIMARY,
CMM Mode               : VIRTUAL-CHASSIS 
MONO CMM,
Current CMM Slot       : CHASSIS-1 A,
Running configuration  : WORKING,
Certify/Restore Status : CERTIFIED
SYNCHRONIZATION STATUS
Flash Between CMMs
: SYNCHRONIZED,
Running Configuration  : SYNCHRONIZED
WORKING
CERTIFIED
WORKING
CERTIFIED

<<<PAGE 111>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 112>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Virtual Chassis-6360 
How to 
✓ This lab is designed to familiarize you with the Virtual Chassis feature (VC) 
and its configuration. 
Contents 
1 
Configure a Virtual Chassis of two switches ............................................... 2 
1.1. Objective ............................................................................................ 2 
1.2. Management ......................................................................................... 3 
2 
Virtual Chassis Monitoring .................................................................... 7

<<<PAGE 113>>>
2 
Virtual Chassis-6360 
 
 1 
Configure a Virtual Chassis of two switches 
1.1. 
Objective 
 
- 
Please note some PODs are using 6360A/6360B with 10 ports or 24 ports. 
 
 
- 
For OS6360-P10, using VFL ports 1/1/11-12 
 
 
- 
Type the following command to determine the type of switch used in the POD.

<<<PAGE 114>>>
3 
Virtual Chassis-6360 
 
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
1.2. 
Management 
 
- 
Assign a globally unique chassis identifier to the switch 6360A and enable the switch to operate in virtual 
chassis mode 
sw5 (6360-A) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        100   0      94:24:e1:7c:82:1d 
 
sw5 (6360-A) -> virtual-chassis chassis-group 1 
 
sw5 (6360-A) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        100   1      94:24:e1:7c:82:1d 
 
sw5 (6360-A) -> show configuration vcm-snapshot chassis-id 1 
! Virtual Chassis Manager: 
virtual-chassis chassis-id 1 configured-chassis-id 1 
virtual-chassis vf-link-mode static 
virtual-chassis chassis-id 1 chassis-group 1 
! 
! PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx] 
! [SAVED INFO VC IDs] 1 
! 
! IP: 
 
- 
Force the 6360-A to be the master chassis, assign a highest chassis priority to it: 
 
sw5 (6360-A) -> virtual-chassis chassis-id 1 configured-chassis-priority 200 
 
sw5 (6360-A) -> write memory 
 
File /flash/working/vcsetup.cfg replaced. 
 
File /flash/working/vcboot.cfg replaced.

<<<PAGE 115>>>
4 
Virtual Chassis-6360 
 
 
sw5 (6360-A) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        100   1      94:24:e1:7c:82:1d 
 
 
Notes: 
A reload is mandatory to consider the chassis priority 
 
sw5 (6360-A) -> reload from working no rollback-timeout 
Confirm Activate (Y/N) : y 
This operation will verify and copy images before reloading. 
It may take several minutes to complete.. 
 
Notes: 
Wait until complete restart. (* close to 4 mn in lab context) 
 
 
Tue Jun 22 03:04:41 : qosNi Info INFO message: 
+++ VC Takeover in progress. 
+++ VC Takeover complete. 
Chassis Supervision: CMM has reached the ready state [L8] 
 
sw5 (6360-A) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        200   1      94:24:e1:7c:82:1d 
 
 
- 
Assign a globally unique chassis identifier to the switch 6360B and enable the switch to operate in virtual 
chassis mode 
 
sw6 (6360-B) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        100   0      94:24:e1:7c:79:65 
 
sw6 (6360-B) -> virtual-chassis chassis-id 1 configured-chassis-id 2 
sw6 (6360-B) -> virtual-chassis chassis-group 1 
 
sw6 (6360-B) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             2        100   1      94:24:e1:7c:79:65 
 
- 
Check the result

<<<PAGE 116>>>
5 
Virtual Chassis-6360 
 
 
sw6 (6360-B) -> show configuration vcm-snapshot chassis-id 2 
! Virtual Chassis Manager: 
! IP: 
 
 
Notes: 
A reload is mandatory to take into account the new chassis -id 
 
sw6 (6360-B) -> write memory 
 
WARNING - Virtual chassis topology change detected. Chassis 1 missing! 
          Configuration associated with missing chassis will be erased permanently! 
          Confirm to continue  (Y/N) : y 
 
File /flash/working/vcsetup.cfg replaced. 
 
File /flash/working/vcboot.cfg replaced. 
 
The command write memory is protected by issuing a warning to prevent or warn purging the configuration of 
the elements that are missing. Chassis id has been changed in this case. 
 
sw6 (6360-B) -> reload from working no rollback-timeout  
Confirm Activate (Y/N) : y 
This operation will verify and copy images before reloading. 
It may take several minutes to complete.. 
 
 
Notes: 
Wait until complete restart. 
Tue Jun 22 03:04:41 : qosNi Info INFO message: 
+++ VC Takeover in progress. 
+++ VC Takeover complete. 
Chassis Supervision: CMM has reached the ready state [L8] 
 
sw6 (6360-B) -> show virtual-chassis topology 
 
Legend: Status suffix "+" means an added unit after last saved topology 
Local Chassis: 2 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 2     Master       Running             2        100   1      94:24:e1:7c:79:65 
 
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
! IP:

<<<PAGE 117>>>
6 
Virtual Chassis-6360 
 
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
! IP: 
 
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

<<<PAGE 118>>>
7 
Virtual Chassis-6360 
 
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
 
 2 
Virtual Chassis Monitoring 
 
- 
Check the virtual-chassis topology: 
 
sw5 (6360-A) -> show virtual-chassis topology 
 
Legend: Status suffix "+" means an added unit after last saved topology 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        200   1      94:24:e1:7c:82:1d 
 2     Slave        Running+            2        100   1      94:24:e1:7c:79:65 
 
 
 
Notes: 
suffix “+”, if any VC element is detected as “Running” but not configuration saved 
 
 
 
 
- 
Save the configuration and check the virtual-chassis topology and copy running to certified: 
 
sw5 (6360-A) -> write memory flash-synchro 
 
File /flash/working/vcsetup.cfg replaced. 
File /flash/working/vcboot.cfg replaced. 
 
Tue Jun 22 04:00:05 : flashManager Main INFO message: 
+++ Verifying image directory working on CMM flash 
Please wait...

<<<PAGE 119>>>
8 
Virtual Chassis-6360 
 
Tue Jun 22 04:00:41 : ChassisSupervisor bootMgr INFO message: 
+++ Copy running to certified: Synchronizing chassis 2 
Tue Jun 22 04:00:49 : ChassisSupervisor MipMgr INFO message: 
+++ Copy running to certified succeeded; Secondary synchronization succeeded 
 
- 
Check the result 
 
sw5 (6360-A) -> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 1 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        200   1      94:24:e1:7c:82:1d 
 2     Slave        Running             2        100   1      94:24:e1:7c:79:65 
 
 
 
- 
Display the vcsetup.cfg file content on the master  
sw5 (6360-A) -> cat /flash/working/vcsetup.cfg 
!========================================! 
! File: /flash/working/vcsetup.cfg       ! 
!========================================! 
! Virtual Chassis Manager: 
virtual-chassis chassis-id 1 configured-chassis-id 1 
virtual-chassis vf-link-mode auto 
virtual-chassis auto-vf-link-port 1/1/27 (6360-P10 port 1/1/11) 
virtual-chassis auto-vf-link-port 1/1/28 (6360-P10 port 1/1/12) 
virtual-chassis chassis-id 1 chassis-group 1 
virtual-chassis chassis-id 1 configured-chassis-priority 200 
! 
! PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx] 
! [SAVED INFO VC IDs] 3 
! 
 
! IP: 
 
- 
Display the different ports belonging to the VFL link 6360-P24, type: 
 
sw5 (6360-A) -> show virtual-chassis vf-link 
 
VFLink mode: Auto 
 
                               Primary   Config  Active  Def       Speed 
 Chassis/VFLink ID  Oper       Port      Port    Port    Vlan      Type 
-------------------+----------+---------+-------+-------+---------+----------- 
 1/0                Up         1/1/27    2       2       1         10G 
 2/0                Up         2/1/27    2       2       1         10G 
 
sw5 (6360-A) -> show virtual-chassis vf-link member-port 
 
VFLink mode: Auto 
 
 Chassis/VFLink ID  Chassis/Slot/Port  Oper       Is Primary 
-------------------+------------------+----------+------------- 
 1/0                1/1/27             Up         Yes 
 1/0                1/1/28             Up         No 
 2/0                2/1/27             Up         Yes 
 2/0                2/1/28             Up         No 
 
 
Notes: 
The “Is Primary” field defines the primary port of the virtual fabric link.

<<<PAGE 120>>>
9 
Virtual Chassis-6360 
 
- 
Display the different ports belonging to the VFL link 6360-P10, type: 
 
sw5 (6360-A) -> show virtual-chassis vf-link 
 
VFLink mode: Auto 
 
                               Primary   Config  Active  Def       Speed 
 Chassis/VFLink ID  Oper       Port      Port    Port    Vlan      Type 
-------------------+----------+---------+-------+-------+---------+----------- 
 1/0                Up         1/1/11    2       2       1         1G 
 2/0                Up         2/1/11    2       2       1         1G 
 
 
sw5 (6360-A) -> show virtual-chassis vf-link member-port 
VFLink mode: Auto 
 
 Chassis/VFLink ID  Chassis/Slot/Port  Oper       Is Primary 
-------------------+------------------+----------+------------- 
 1/0                1/1/11             Up         Yes 
 1/0                1/1/12             Up         No 
 2/0                2/1/11             Up         Yes 
 2/0                2/1/12             Up         No 
 
 
Verify the consistency of system-level mandatory parameters between the two chassis: 
 
sw5 (6360-A) -> show virtual-chassis consistency 
Legend: * - denotes mandatory consistency which will affect chassis status 
        licenses-info - A: Advanced; B: Data Center; 
 
       Config           Oper                   Oper     Config 
       Chas             Chas    Chas   Hello   Control  Control 
 Chas* ID     Status    Type*   Group* Interv  Vlan*    Vlan     License* 
------+------+---------+-------+------+-------+--------+--------+---------- 
 1     1      OK        OS6360  1      15      4094     4094     A 
 2     2      OK        OS6360  1      15      4094     4094     A 
 
 
 
 
Notes: 
The two chassis in the same Virtual-Chassis group must maintain identical configuration and operational 
parameters. 
 
- You can access to the secondary VC by typing the following: 
 
sw5 (6360-A)-> ssh-chassis admin@2 
Executing: ssh admin@127.10.2.65 
(admin@127.10.2.65)                        
*********************** 
*                     * 
* Welcome To Rlab LAN * 
*    Pod 20 Switch 6  * 
*        6360-B       * 
*                     * 
*********************** 
                        
Password: switch

<<<PAGE 121>>>
10 
Virtual Chassis-6360 
 
- Although the prompt is the same, you are now connected to the secondary VC. Type the following: 
 
sw5 (6360-A)-> show virtual-chassis topology 
Legend: Status suffix "+" means an added unit after last saved topology 
 
Local Chassis: 2 
 Oper                                   Config   Oper 
 Chas  Role         Status              Chas ID  Pri   Group  MAC-Address 
-----+------------+-------------------+--------+-----+------+------------------ 
 1     Master       Running             1        200   1      2c:fa:a2:05:cd:71 
 2     Slave        Running             2        100   1      2c:fa:a2:05:cd:a9 
 
- Look at the Local Chassis parameter. Now it says 2, which means you are connected to the secondary VC. 
log 
 
 
- Type the following to return to the master VC: 
 
sw5 (6360A) -> logout 
logout 
Connection to 127.10.2.65 closed. 
 
- 
Disable all unused interfaces for 6360-P24:   
sw5 (6360-A) -> interfaces 1/1/1-26 admin-state disable 
sw5 (6360-A) -> interfaces 2/1/1-26 admin-state disable 
- 
Disable all unused interfaces for 6360-P10:  
sw5 (6360-A) -> interfaces 1/1/1-10 admin-state disable 
sw5 (6360-A) -> interfaces 2/1/1-10 admin-state disable 
 
- 
Check that the HTTP service is enabled (ex. 6360-A): 
Pod11sw3 login: admin 
Password: switch 
 
Sw5 (6360-A) -> show aaa authentication 
[/TRUNCATED] 
Service type = Http 
  Authentication = Use Default, 
  1rst authentication server = local 
[/TRUNCATED] 
 
- 
As you can see here, HTTP authentication is enabled, and the first authentication server to be polled is 
the local database. If it is not, enable it via the command : aaa authentication http local 
 
 
Notes 
By default, the WebView is enabled on the OmniSwitch but you are not allowed to authenticate. On the 
Remote-Lab, the WebView access has already been enabled. 
- 
Check the WebView status:  
 
Sw5 (6360-A) -> show webview 
WebView Server = Enabled, 
WebView Access = Enabled, 
WebView Force-SSL = Enabled, 
WebView HTTPS-Port = 443 
 
- 
Opening the WebView from the Windows Desktop, open a Web Browser (ex. Firefox, Chrome) 
 
- 
In the URL area, type : https://10.4.pod#.5 
-

<<<PAGE 122>>>
11 
Virtual Chassis-6360 
 
Login to the WebView with the admin credentials: 
- 
 
User Name : admin 
Password : switch 
Language : English 
 
- 
After a successful connection, the dashboard page appears 
- 
Visualize your chassis In the horizontal menu bar at the top of the page, select Physical, then in the 
"Chassis management" column, click on "Chassis visualization". 
 
- 
6360-P24 
 
 
 
- 
6360-P10

<<<PAGE 123>>>
V L A N  M A N A G E M E N T
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 124>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the VLAN features
• Setup Static and Dynamic VLAN 
• Configure Static and dynamic Ports assignment 
• Configure inter VLAN routing
• Configure VLAN Tagging

<<<PAGE 125>>>
VLAN MANAGEMENT
• Goal
• Logically segment a Local Area Network (LAN) into 
different broadcast domains
• Ease of network management
• Provides a more secure network
• How it works
• Ports become members of VLANs by
• Static Configuration
• Mobility/with or without Authentication *
• 802.1q
Vlan10
Vlan 60
Vlan 50
Vlan 30
* With authentication : Seen in the following chapter (Access Guardian)

<<<PAGE 126>>>
VLAN MANAGEMENT - STATIC VLAN MEMBERSHIP
• Goal
• The initial configuration for all OmniSwitch consists 
of a default VLAN 1 and all switch ports are initially 
assigned to this VLAN
• Ports can be statically assigned to VLANs.
• When a port is assigned to a VLAN, a VLAN port 
association (VPA) is created and tracked by VLAN 
management switch software 
1/1/2
1/1/4
1/1/6
VLAN 1
VLAN 3
VLAN 4
VLAN 5
VLAN 6
1/1/1

<<<PAGE 127>>>
VLAN MANAGEMENT - STATIC VLAN MEMBERSHIP
Configuration –Step by step
Defining a VLAN
Assigning Ports to a VLAN
Optional commands
Monitoring
-> vlan 2
-> vlan 2 members port <chassis/slot/port> untagged
-> vlan 4 admin-state enable
-> vlan 4 name Engineering
Use quotes around string if the VLAN name contains multiple words with spaces between them
-> vlan 10-15 100-105 200 name “Training Network”
-> show vlan 4
-> show vlan members
-> show ip interface

<<<PAGE 128>>>
VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
• Goal
• VLAN is assigned depending on the device or the 
user
• Device oriented : VLAN according to traffic criteria 
(MAC@, etc…)
• User oriented: Authenticated VLAN (IEEE 802.1x  for 
enhanced security) *
VLAN 1
VLAN 2
VLAN 3
VLAN 4
VLAN 5
VLAN 6
* With authentication : Seen in the following chapter (Access Guardian)

<<<PAGE 129>>>
VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
• How it works
• When traffic is received on a unp port: 
• The packets are examined to determine if their content matches any of the VLAN rules configured on the 
switch . If so, the mobile port is assigned to that VLAN
• Upon receiving a frame, Source Learning compares the frame with VLAN Policies in Order
Classification
Rules
UNP Port classification rules 
1. Port/Linkagg
2. Domain
3. MAC address 
4. MAC-OUI
5. MAC address range
6. LLDP
7. Auth-type
8. IP address
9. VLAN tag
Precedence

<<<PAGE 130>>>
VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
• Device oriented : VLAN according to traffic criteria (MAC@, etc…)
• Unp classification rules Configuration (R8) – step by step
-> unp port 1/1/1 port-type bridge
-> unp profile employee
unp profile employee map vlan 20
UNP profile
VLAN ID
Policy List
ACL
QoS
Location
Period
* Policy list, location and period will be seen 
in the following chapter (Access Guardian)
*
Enabling a mobile port
Configure UNP profile
Map the vlan to UNP

<<<PAGE 131>>>
VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
• Device oriented : unp according to traffic criteria (MAC@, etc…)
• unp classification rules Configuration – step by step
• When classification is enabled but authentication is disabled or fails,UNP classification rules are appliedto
the traffic received on the UNP port.
• MAC Address rule
• Ip adress rule
• Mac range rule
unp classification mac-address mac_address profile1 profile_name
Eg: -> unp classification mac-address 00:11:22:33:44:55 profile1 employee
unp classification mac-address-range low_mac_address high_mac_address profile1 profile_name
Eg: -> unp classification mac-address-range 00:11:22:33:44:55 00:11:22:33:44:66 profile1 employee
unp classification ip-address ip_address mask mask profile1 profile_name
Eg: -> unp classification ip-address 10.0.0.20 mask 255.255.0.0 profile1 employee
UNP Port classification rules 
1. Port/Linkagg
2. Domain
3. MAC address 
4. MAC-OUI
5. MAC address range
6. LLDP
7. Auth-type
8. IP address
9. VLAN tag

<<<PAGE 132>>>
VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
• Device oriented: unp according to traffic criteria (MAC@, etc…)
• unp classification rules Configuration (R8) – step by step
• Configuring Binding Rules for UNP Profiles
• Combination of one or more individual rules all of which a device has to match
•
Eg : Binding rule that combines a MAC address rule, an IP address rule, and a port rule
• Configuring Extended Classification Rules for UNP Profiles
•
List of individual rules and assigns the list a name and a precedence value.
A device must match all of the rules specified in the extended rule list.
•
“ext-r1” rule combines a port rule and vlan tag type rule
• Precedence: Extended rule > Binding Rule > Simple Rule
1 Port + MAC address + IP address
2 Port + MAC address
3 Port + IP address
4 Domain ID + MAC address + IP address
-> unp classification mac-address 00:11:22:33:44:55 ip-address 10.0.0.20 mask 255.255.0.0 port 1/1/1 profile1 employee
-> unp classification-rule ext-r1 precedence 255
-> unp classification-rule ext-r1 profile1 employee 
-> unp classification-rule ext-r1 port 1/1/10
-> unp classification-rule ext-r1 vlan-tag 10

<<<PAGE 133>>>
VLAN MANAGEMENT - DYNAMIC VLAN MEMBERSHIP
Example of Device oriented: unp according to traffic criteria (MAC@ range)
No Auth
UNP Port 
Default
UNP Profile
Block
Classification
Rules
UNP Profile
Employee
-> vlan 10 admin-state disable name vlan10-block
-> vlan 20 admin-state enable name vlan20-corporate
• Create the required VLANs
• Create the required UNP profile and map the profile to VLAN 20
• Create another UNP profile that will serve as a default profile 
and map the profile to VLAN 10
• Create a MAC range classification rule and associate the rule to 
the “corporate” UNP profile
• Enable UNP on the user port that will connect to user device
• Set the default UNP profile on the user port
-> unp profile corporate
-> unp profile corporate map vlan 20
-> unp profile def_unp
-> unp profile def_unp map vlan 10
-> unp classification-rule rule1 mac-address-range 08:00:27:00:98:0A 08:00:27:00:98:FF
-> unp classification-rule rule1 profile1 corporate
-> unp port 1/1/1 port-type bridge
-> unp port 1/1/1 default-profile def_unp

<<<PAGE 134>>>
INTER VLAN ROUTING

<<<PAGE 135>>>
INTER VLAN ROUTING
• IP interfaces are associated with VLANs
• IP routing is active as soon as at least one IP interface is associated with a VLAN
-> ip interface <int_name> address <ip address/mask> vlan <vlan_id>
1/1/2
1/1/6
VLAN 20
VLAN 60
Virtual Router
The operational status of a VLAN 
remains inactive as long as no active 
port is associated with this VLAN

<<<PAGE 136>>>
INTER VLAN ROUTING
• Virtual Router
1/1/2
1/1/6
VLAN 20
VLAN 60
Virtual Router
Gateway for Device VLAN 20
ip interface Data address 10.1.20.254 mask 255.255.255.0 vlan 20
Gateway for Device VLAN 60
ip interface Voice address 10.1.60.254 mask 255.255.255.0 vlan 60
-> show ip interface
Total 2 interfaces
Name            IP Address    Subnet Mask      Status   Forward  Device
--------------+-------------+----------------+--------+--------+--------
Data            10.1.20.254     255.255.255.0     UP      NO     vlan 20
Voice           10.1.60.254     255.255.255.0     UP      NO     vlan 60
-> show vlan 20
Name                     : data,
Type                     : Static Vlan,
Administrative State     : enabled,
Operational State        : enabled,
IP Routing               : enabled,
IP MTU                   : 1500
-> show vlan 20 members
port      type      status
---------+---------+--------------
1/1/2     untagged     forwarding

<<<PAGE 137>>>
802.1Q – VLAN TAGGING

<<<PAGE 138>>>
802.1Q – VLAN TAGGING
• Aggregates multiple VLANs across Ethernet links
• Combines traffic from multiple VLANs over a single link
• Encapsulates bridged frames within standard IEEE 802.1Q frame
• Enabled on fixed ports
• Tags port traffic for destination VLAN
Tagged Frames

<<<PAGE 139>>>
IEEE 802.1Q – TAGGED VLANS
• VLAN Tag
• 802.3 MAC header change
• 4096 unique VLAN Tags (addresses)
• VLAN ID == GID == VLAN Tag
• 802.1P
• Three-bit field within 802.1Q header
• Allows up to 8 different priorities
• Feature must be implemented in hardware
802.1p (3 bits)
DA
SA
VLAN ID (12 Bits)
4 Bytes
“Modified 802.3 MAC”
Ethertype, Priority, Tag

<<<PAGE 140>>>
802.1Q - CONFIGURATION
-> vlan 2-4
-> vlan 2-4 members port 1/1/24 tagged
VLAN 4
VLAN 3
VLAN 2
VLAN 4
VLAN 3
VLAN 2
1/1/24
-> show vlan members
1/1/24
VLAN 278
VLAN 278

<<<PAGE 141>>>
DYNAMIC VLAN MEMBERSHIP

<<<PAGE 142>>>
DYNAMIC VLAN MEMBERSHIP - AUTHENTICATED METHOD
How it works
• Applies to users connected on 
authenticated ports
• Users must authenticate through 802.1x 
client
• Authentication is based on either RADIUS, 
LDAP or TACACS+
• Successful login: 
The client is associated 
with the correct UNP
Authentication Method
• MAC-based (non-supplicant)
or 
• 802.1x-based (supplicant)
{ "user"
User-Password="xxxxxx"
Filter-ID = "UNP-name"
}
RADIUS Access-Accept + UNP name
RADIUS Access-Request
VLAN
30
INTERNET 
ONLY
MEDIUM 
BWDTH
LOW 
PRIORITY
GUEST
VLAN
20
NO HR, 
FINANCE DB
MEDIUM 
BWDTH
MEDIUM 
PRIORITY
EMPLOYEE
Specifies the days and times during 
which a device can access the network
Restrict the network access based on 
the location of the user/device
Chassis/Slot/Port on which the user is 
attached Switch Name on which the 
user is attached 
Switch Location String, identifying a 
group of Switches 
* 802.1X and Mac  authentication  will be seen in more details in the following chapter (Access Guardian)
UNP R8
VLAN ID
Policy List
ACL
QoS
Location
Period

<<<PAGE 143>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 144>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
VLANs 
How to 
✓ Manage VLANs on the OmniSwitches 
Contents 
1 
Topology ........................................................................................ 2 
2 
Creating a VLAN ............................................................................... 2 
3 
Creating Additional VLANs ................................................................... 7 
4 
Dynamic VLAN Membership ................................................................ 11 
5 
Deleting VLANs & IP interfaces ............................................................ 13

<<<PAGE 145>>>
2 
VLANs 
 
 1 
Topology 
Below the topology that will be used during this lab: 
 
 
 
 
 
 
 2 
Creating a VLAN 
VLANs provide the ability to segregate a network into multiple broadcast domains. Additionally, Virtual Router 
ports (or IP Interfaces) can be assigned to VLANs to allow traffic to be switched at Layer 3. 
 
- In its untagged configuration, the switch has only one VLAN, the VLAN 1. This is the default VLAN and all 
ports are initially associated with it. This VLAN CANNOT be deleted, but it can be disabled if desired. 
- Let’s run the command to see the VLANs that exist on the switch as well as information on a single VLAN 
(ex. 6360-A):  
sw5 (OS6360-A) -> show vlan 
                              stree                 mble   src 
 vlan  type  admin   oper   1x1   flat   auth   ip   tag   lrn   name 
-----+-----+------+------+------+------+----+-----+-----+------+---------- 
   1    std   on    off     on    on     off   off   off     on   VLAN 1

<<<PAGE 146>>>
3 
VLANs 
 
- To display information on a specific VLAN: 
sw5 (6360-A) -> show vlan 1 
Name                     : VLAN 1, 
Type                     : Static Vlan, 
Administrative State     : enabled, 
Operational State        : disabled, 
IP Routing               : disabled, 
IP MTU                   : 1500 
 
- Notice the VLAN Administrative State is enabled, however its Operational State is disabled. Without 
members the VLAN will be Operationally down.  
 
 
Notes 
You can also list the ports and their associated VLAN (notice that the status of all the ports is “inactive”, so the 
Vlan is operationally down):  
-> show vlan members 
 
- Enter the following command on the switch (OS6360-A): 
sw5 (6360-A) -> show vlan members 
  vlan       port         type         status 
--------+------------+------------+-------------- 
  1         1/1/1        untagged    inactive 
  1         1/1/2        untagged    inactive 
  1         1/1/3        untagged    inactive 
  1         1/1/4        untagged    inactive 
  1         1/1/5        untagged    inactive 
  1         1/1/6        untagged    inactive 
  1         1/1/7        untagged    inactive 
  1         1/1/8        untagged    inactive 
  1         1/1/9        untagged    inactive 
  1         1/1/10       untagged    inactive 
  1         1/1/11       untagged    inactive 
  1         1/1/12       untagged    inactive 
  1         1/1/13       untagged    inactive 
  1         1/1/14       untagged    inactive 
  1         1/1/15       untagged    inactive 
  1         1/1/16       untagged    inactive 
  1         1/1/17       untagged    inactive 
  1         1/1/18       untagged    inactive 
  1         1/1/19       untagged    inactive 
  1         1/1/20       untagged    inactive 
  1         1/1/21       untagged    inactive 
  1         1/1/22       untagged    inactive 
  1         1/1/23       untagged    inactive 
  1         1/1/24       untagged    inactive 
  1         1/1/25       untagged    inactive 
  1         1/1/26       untagged    inactive 
  1         1/1/27       untagged    inactive 
  1         1/1/28       untagged    inactive 
   
 
- Display the VLAN assignment on a specific port (ex. port 1/1): 
sw5 (6360-A) -> show vlan members port 1/1/1 
  vlan      type        status 
--------+-----------+--------------- 
     1    untagged       inactive 
 
 
- In order to have IP connectivity to a VLAN interface (not required for connectivity to other clients/servers 
within a VLAN), an IP address (IP interface) must be assigned to a Virtual Router port and associated to 
that VLAN. This IP address can then be used for IP connectivity as well as Layer 3 switching.  
- To create the IP interface (ex. int_1 = IP interface name, 192.168.10.5 = IP@ of the IP Interface):  
sw5 (6360-A) -> ip interface int_1 address 192.168.10.5/24 
 
sw5 (6360-A) -> show ip interface 
Total 3 interfaces 
 Flags (D=Directly-bound)

<<<PAGE 147>>>
4 
VLANs 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_1                            192.168.10.5    255.255.255.0     DOWN      NO unbound 
- The Device status is unbound. It is because the IP interface has not been associated to a VLAN yet.  
- To bind the IP Interface (ex. int 1) to a VLAN (ex. VLAN 1): 
sw5 (6360-A) -> ip interface int_1 vlan 1 
 
 
Notes 
The last 2 commands can be merged into a single command: 
 
-> ip interface int_1 address 192.168.10.5/24 vlan 1 
 
- Check that the IP Interface is now associated to the VLAN 1:  
sw5 (6360-A) -> show ip interface 
Total 3 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0             DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_1                            192.168.10.5    255.255.255.0       DOWN     YES vlan 1 
 
- If Status = DOWN, it indicates no active ports or devices have been associated with the VLAN that the IP 
interface has been assigned to. If an IP interface is DOWN, it cannot be connected to, will not reply to 
PING requests nor will it be advertised in any router updates. This will not affect the Layer 2 broadcast 
domain, however. 
- Let’s activate a port in VLAN 1 to change the status to enable: 
sw5 (6360-A) -> interfaces 1/1/1 admin-state enable 
 
sw5 (6360-A) -> 
Mon Jun 21 23:31:44 : intfCmm Mgr INFO message: 
+++ Link 1/1/1 operationally up 
 
 
Tips 
The equipment connected to the port 1/1/1 of the 6360-A is the Client 5 virtual machine: 
 
 
- Then check the port status: 
sw5 (6360-A) -> show vlan members port 1/1/1 
  vlan      type        status 
--------+-----------+--------------- 
     1    untagged     forwarding 
-  
- By default, all ports (including the port 1/1/1) belong to VLAN 1, so the VLAN 1 will become active. 
- Run the command to check that the status of the IP interface is UP: 
sw5 (6360-A) -> show ip interface 
Total 3 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback

<<<PAGE 148>>>
5 
VLANs 
 
int_1                            192.168.10.5    255.255.255.0       UP     YES vlan 1 
 
Now that the VLAN has an active port, let’s modify the IP information of the Client 5, and ping the IP 
interface associated with VLAN 1.  
 
- Open the virtual machine Client 5 and set its IP address: 
Windows Desktop  
Double-click on VMware 
vSphere 
 
Select the Client5 in the list 
 
Click on Console tab 
 
Double click on Network 
Connections

<<<PAGE 149>>>
6 
VLANs 
 
Select the network connection 
Pod 
 
Click on Internet Protocol 
(TCP/IP) 
 
 
 
Select Use the following IP 
address 
 
- IP address: 192.168.10.105 
- Subnet mask: 
255.255.255.0 
- Default gateway: 
192.168.10.5 (The IP address 
of VLAN 1 virtual router) 
 
 
- From Client 5, open a command prompt and ping the switch’s VLAN 1 Virtual Router IP address. You 
should now have IP connectivity:

<<<PAGE 150>>>
7 
VLANs 
 
 3 
Creating Additional VLANs 
Currently, there is only the default VLAN created on the switch. The following steps will provide information on 
creating another VLAN, enabling IP on the VLAN, moving ports into the VLAN, and forwarding IP packets 
between VLANs. 
 
- To begin, let’s create a new VLAN and assign an IP address to that VLAN as done previously: 
sw5 (6360-A) -> vlan 50 
sw5 (6360-A) -> ip interface int_50 address 192.168.50.5/24 vlan 50 
 
- Let's look at what we have configured so far: 
sw5 (6360-A) -> show ip interface 
Total 4 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_1                            192.168.10.5    255.255.255.0       UP     YES vlan 1 
int_50                           192.168.50.5    255.255.255.0     DOWN      NO vlan 50 
 
sw5 (6360-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Ena   Ena    1500    VLAN 1 
50     std       Ena     Dis   Ena    1500    VLAN 50 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
- Why the status of the IP interface int_50 is DOWN?  
> ___________________________________________________________________________________ 
 
- Assign the VLAN 50 to the port 1/1/2 where Client 9 is connected: 
sw5 (6360-A) -> vlan 50 members port 1/1/2 untagged 
 
sw5 (6360-A) -> show ip interface 
Total 4 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_1                            192.168.10.5    255.255.255.0       UP     YES vlan 1 
int_50                           192.168.50.5    255.255.255.0     DOWN      NO vlan 50 
 
sw5 (6360-A) -> show vlan members port 1/1/2 
  vlan      type        status 
--------+-----------+--------------- 
    50    untagged       inactive 
 
sw5 (6360-A) -> interface 1/1/2 admin-state enable 
 
Mon Jun 21 23:38:46 : intfCmm Mgr INFO message: 
+++ Link 1/1/2 operationally up 
 
 
sw5 (6360-A) -> show ip interface 
Total 4 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags

<<<PAGE 151>>>
8 
VLANs 
 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_1                            192.168.10.5    255.255.255.0       UP     YES vlan 1 
int_50                           192.168.50.5    255.255.255.0       UP     YES vlan 50 
 
 
- Assign an IP address to the Client 9: 
Windows Desktop  
Double-click on VMware 
vSphere 
 
Select the Client9 in the list 
 
Click on Console tab 
 
Double click on Network 
Connections

<<<PAGE 152>>>
9 
VLANs 
 
Select the network connection 
Pod 
 
Click on Internet Protocol 
(TCP/IP) 
 
 
 
Select Use the following IP 
address 
 
- IP address: 192.168.50.105 
- Subnet mask: 
255.255.255.0 
- Default gateway: 
192.168.50.5 (The IP address 
of VLAN 50 virtual router)

<<<PAGE 153>>>
10 
VLANs 
 
The following diagram represents the current configuration. 
 
 
 
 
 
 
By default, the switch will route packets between VLAN 1 and VLAN 50 using the IP interfaces that you have 
created. 
 
- Check the routing table on the switch: 
sw5 (6360-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 5 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  127.0.0.1/32         127.0.0.1            3d16h   LOCAL 
  192.168.10.0/24      192.168.10.5      00:11:04   LOCAL 
  192.168.50.0/24      192.168.50.5      00:04:03   LOCAL 
 
- From client 9, open a command prompt and ping the client 5. You should now have IP connectivity:

<<<PAGE 154>>>
11 
VLANs 
 
 4 
Dynamic VLAN Membership 
- In this exercise, VLAN is assigned depending on the device. 
- Device oriented: VLAN according to traffic criteria (In this example base on MAC@). 
 
- To begin, let’s create a new VLAN: 
sw5 (6360-A) -> vlan 40 
 
- As we haven't yet managed the DHCP server at this stage in the training, we'll assign a static IP address to 
client 6. Assign an IP address to the Client 6: 
Windows Desktop  
Double-click on VMware 
vSphere 
 
Select the Client 6 in the list. 
Power on if need. (Right click) 
 
Click on Console tab 
 
Double click on Network 
Connections 
 
Or

<<<PAGE 155>>>
12 
VLANs 
 
Select the network connection 
Pod 
 
Click on Internet Protocol 
(TCP/IP) 
 
Select Use the following IP 
address 
 
- IP address: 192.168.40.106 
- Subnet mask: 
255.255.255.0 
 
And click on OK 
 
 
 
 
Click on Support and details 
 
And note the mac adress 
 
 
- Enable interface 2/1/1 where is connected the client 6 
sw5 (6360-A) -> interface 2/1/1 admin-state enable 
 
 
- Check Vlan and status on the port  
sw5 (6360-A) -> sh vlan members port 2/1/1 
  vlan      type        status 
--------+-----------+--------------- 
     1    untagged    forwarding 
 
- Check Mac-learning table for the port 2/1/1. (example with pod 5 client 6) 
sw5 (6360-A) -> show mac-learning port 2/1/1 
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
      VLAN                        1   00:50:56:90:ee:0a            dynamic     bridging                     2/1/1 
 Total number of Valid MAC addresses above = 1 
 
- Configure UNP profile 
sw5 (6360-A) -> unp profile employee 
 
- Map the vlan to UNP

<<<PAGE 156>>>
13 
VLANs 
 
sw5 (6360-A) -> unp profile employee map vlan 40 
 
- Configure a unp classification rule based on mac address. In this command, mac address is the client 6 of 
pod5.in your case, check result on show mac-learning command done previously 
sw5 (6360-A) -> unp classification mac-address 00:50:56:90:ee:0a profile1 employee 
 
- Check unp user 
sw5 (6360-A) -> sh unp user 
No UNP Ports found 
 
- Enable UNP on the user port that will connect to user device 
sw5 (6360-A) -> unp port 2/1/1 port-type bridge 
 
- Flush the port 
sw5 (6360-A) -> unp user flush port 2/1/1 
 
- Check unp user 
sw5 (6360-A) -> sh unp user 
                                               User                                                                 
Port    Username             Mac address       IP (V4/V6)                               Vlan Profile                 Type         Status 
-------+--------------------+-----------------+------------------------+----+--------------------------------+----+----------- 
2/1/1   00:50:56:90:ee:0a    00:50:56:90:ee:0a -                                        40   employee                Bridge       Active 
 
sw5 (6360-A) -> sh vlan members port 2/1/1 
  vlan      type        status 
--------+-----------+--------------- 
     1    untagged    forwarding 
    40    unpUntag    forwarding 
 5 
Deleting VLANs & IP interfaces 
- Before continuing with the other labs, remove the previous configuration: delete the VLAN 50, and the IP 
interfaces (int_1 and int_50). 
sw5 (6360-A) -> no ip interface int_50 
sw5 (6360-A) -> no vlan 50 
sw5 (6360-A) -> no ip interface int_1 
 
 
Notes 
VLAN 1 cannot be deleted. It is only possible to deactivate. 
 
- Check that the VLAN 50 and the IP interfaces have been correctly deleted:  
sw5 (6360-A) -> show vlan 
 vlan    type   admin   oper    ip    mtu          name 
------+-------+-------+------+------+------+------------------ 
1      std       Ena     Ena   Dis    1500    VLAN 1 
4094   vcm       Ena     Dis   Dis    1500    VCM IPC 
 
sw5 (6360-A) -> show ip interface 
Total 2 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.5       255.255.255.0       UP      NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback

<<<PAGE 157>>>
14 
VLANs 
 
- Remove the previous configuration about unp classification 
 
sw5 (6360-A) -> sh configuration snapshot DA-UNP 
! DA-UNP: 
unp profile "employee" 
unp profile "employee" map vlan 40 
unp port 2/1/1 port-type bridge 
unp port 2/1/1 port-template bridgeDefaultPortTemplate 
unp classification mac-address 00:50:56:90:ee:0a profile1 "employee" 
 
sw5 (6360-A) -> no unp classification  mac-address 00:50:56:90:ee:0a 
 
sw5 (6360-A) -> no unp port 2/1/1 
 
sw5 (6360-A) -> no unp profile "employee" 
 
sw5 (6360-A) -> sh configuration snapshot DA-UNP 
! DA-UNP: 
 
sw5 (6360-A) -> sh vlan members port 2/1/1 
  vlan      type        status 
--------+-----------+--------------- 
     1    untagged    forwarding

<<<PAGE 158>>>
DIAGNOSTIC TOOLS
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 159>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Use the Switch & Command Logging utilities
• Use the Remote MONitoring (RMON) application
• Enable the Port Mirroring feature
• Enable the Port Monitoring feature
• Check the Switch Health
• Use the sFlow Application

<<<PAGE 160>>>
SWITCH LOGGING

<<<PAGE 161>>>
SWITCH LOGGING OUTPUT
• Event logging utility 
• Useful in maintaining and servicing the switch
• Switch events can be logged to
• Switch console
• Local text file
• Configurable default file size 1250 Kbytes
• Multiple remote devices (syslog) 12 max 
•
Loopback0 have to be configured 
sw1 (6900-A) -> show swlog
Operational Status
File Size per file
Log Device 1
Syslog FacilityID
Hash Table entries age limit
Switch Log Preamble
Switch Log Debug,
Switch Log Duplicate Detection
Console Display Level
RFC5424 Format Logging
Swlog Threshold
: Running
: 1250 Kbytes,
: console flash,
: local0(16),
: 60 seconds,
: Enabled,
: Disabled
: Enabled,
: info,
: Disabled,
: 90 percent
When this command is enabled, syslog server
will be restarted and allowing send Console 
log to remote Syslog servers
-> swlog output console
-> swlog output flash
-> swlog output socket ipaddr 168.23.9.100
swlog output socket console enable

<<<PAGE 162>>>
SWITCH LOGGING FILES
• Switch logging are stored in /flash directory
• Up to 8 Swlog logs files can be stored in the
/flash directory starting (from swlog_chassis1 to 1.6)
• An Swlog archive can store up to 40 files 
• Configuring the Switch Logging File Size
(in bytes)
sw1 (6900-A) -> ls -l
drwxr-xr-x    2 admin    user       4096 Jun  7 09:15 app-signature
drwxr-xr-x    2 admin    user       4096 Jun  7 07:57 certified
-rw-r--r--
1 admin    user        255 Jun  7 09:11 hwinfo
-drwxr-xr-x   2 admin    user      16384 Dec 18  2013 lost+found
drwxr-xr-x    2 admin    user       4096 Feb 10  2016 network
drwxr-xr-x    3 admin    user       4096 Apr 23  2015 pmd
drwxr-xr-x    7 admin    user       4096 Jun  7 07:57 switch
drwxr-xr-x    2 admin    user       4096 Jun  8 10:53 swlog_archive
-rw-r--r--
1 root     root
560111 Jun 10 12:50 swlog_chassis1
-rw-r--r--
1 root     root
1280031 Jun 10 12:44 swlog_chassis1.0
-rw-r--r--
1 root     root
1280067 Jun 10 12:28 swlog_chassis1.1
-rw-r--r--
1 root     root
1280027 Jun 10 12:12 swlog_chassis1.2
-rw-r--r--
1 root     root
1280041 Jun 10 11:56 swlog_chassis1.3
-rw-r--r--
1 root     root
1280094 Jun 10 11:41 swlog_chassis1.4
-rw-r--r--
1 root     root
1280125 Jun 10 11:26 swlog_chassis1.5
-rw-r--r--
1 root     root
1280100 Jun 10 11:12 swlog_chassis1.6
-> swlog output flash-file-size 12500

<<<PAGE 163>>>
DISPLAYING SWITCH LOGGING RECORDS
• Clear the log files contents
• Clear both the log files contents and event logs
• Displaying Switch Logging Records
sw1 (6900-A) -> show swlog
Operational Status
File Size per file
Log Device 1
Syslog FacilityID
Hash Table entries age limit       
Switch Log Preamble                
Switch Log Debug,
Switch Log Duplicate Detection    
Console Display Level              
RFC5424 Format Logging            
Swlog Threshold                    
: Running
: 1250 Kbytes,
: console flash,
: local0(16),
: 60 seconds,
: Enabled,
: Disabled
: Enabled,
: info,
: Disabled,
: 90 percent
sw1 (6900-A) -> show log swlog
/flash/swlog_chassis1.7 not found!
Displaying file contents for '/flash/swlog_chassis1.6'
2017 Jun 10 10:43:46 Pod18sw1 Switch log file reached 100%, overwritten !!!
2017 Jun 10 10:43:46 Pod18sw1 swlogd: ospf_0 INFO debug2(7) (11654):(3157):ENTER select 
usec=870000, lastMs=264773690, curMs=264773820.
2017 Jun 10 10:43:46 Pod18sw1 swlogd: SSAPP main info(5) sending trap for swlog failure trap
2017 Jun 10 10:43:47 Pod18sw1 swlogd: rip_0 INFO debug2(7) (9046):(1779):ripRun: ENTER select 
usec=998000, lastMs=264774578, curMs=264774630.
-> swlog clear
-> swlog clear all
-> show swlog
-> show log swlog

<<<PAGE 164>>>
SWITCH LOGGING SEVERITY LEVEL 
• Default severity level is “info”. The numeric equivalent for the level “info” is 6
• It is also possible to assign different severity levels to different switch applications (some 
of the events will be filtered out of the display)

<<<PAGE 165>>>
SWITCH LOGGING APPLICATION ID LEVELS OF REPORTING
• Specific applications may have different levels of reporting and can be specified by their 
application ID or by their numeric equivalent
show swlog appid ?
^
ALL <string>
SWLOG PMD ChassisSupervisor flashManager MIP_GATEWAY
ConfigManager capManCmm vc_licManager vcmCmm SSTIME SSAPP
mrvld capManSig fabric portMgrCmm vfcm intfCmm dafcCmm
linkAggCmm VlanMgrCmm ipmscmm pvlanCmm isis_spb_0 isisVc
stpCmm AGCMM slCmm mirMonSFlowCmm ipv4 ipv6 ipsecSys ipsec
tcamCmm qosCmm vstkCmm eoamCmm erpCmm NTP udpRelay
remoteConfig AAA havlanCmm SES rmon WEBVIEW trapmgr radCli
ldapClientCmm tacClientCmm healthCmm svcCmm lldpCmm udldCmm
evbCmm mpls saaCmm SNMP csEventMonitor bfdcmm mvrpCmm
dhcp6r messageService dhcpv6Srv dhcpSrv grm bcdcmm lpCmm
DG_CMM qmrCmm iprm_0 vrrp_0 ospf_0 flashManagerNI capManNi
vcmNi portMgrNi bcd vfcn intfNi dafcNi linkAggNi VlanMgrNi
stpNi erpNi vstkNi fdbmgr1 slNi healthNi ipni ip6ni
mirMonSFlowNi tcamni qosNi ipmsni svcNi evbNi lldpNi udldNi
bfdni mvrpNi AGNI DG_NI nipktrly loamNi eoamNi fdbmgr4 lpNi
fdbmgr3

<<<PAGE 166>>>
SWITCH LOGGING APPLICATION ID
• Example of levels of reporting management for OSPF  
• All sub application
• Only for the hello message
sw1 (6900-A) -> swlog appid ospf_0 subapp all level 8
sw1 (6900-A) -> swlog appid ospf_0 subapp all level debug3
sw1 (6900-A) -> swlog appid ospf_0 subapp hello level debug3
sw1 (6900-A) -> swlog appid ospf_0 subapp ?
ALL <num> <string>
1=ERROR 2=WARNING 3=RECV 4=SEND
5=FLOOD 6=SPF 7=LSDB 8=RDB 9=AGE
10=VLINK 11=REDIST 12=SUMMARY
13=DBEXCH 14=HELLO 15=AUTH 16=STATE
17=AREA 18=INTF 19=CONFIG 20=INFO
21=SETUP 22=TIME 23=MIP 24=TM
25=RESTART 26=HELPER 27=HOST
28=AUTOCONFIG
or

<<<PAGE 167>>>
DISPLAYING SWITCH LOGGING RECORDS
• Timestamps 
• show log swlog [timestamp mm/dd/yyyy hh:mm:ss]
• Application
• show log swlog |grep [appid] |grep [subapp] …
2017 Jun 10 10:43:59 Pod18sw1 swlogd: ospf_0 AREA debug2(7) (11654):(3254):[curTime=251171s] Flooding area 0.0.0.0
2017 Jun 10 10:43:59 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 172.16.17.1, curTime = 251171, helloTimer = 251497, deadTimer = 75447
2017 Jun 10 10:43:59 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 172.16.18.1, curTime = 251171, helloTimer = 251180, deadTimer = 66940
2017 Jun 10 10:43:59 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 192.168.110.1, curTime = 251171, helloTimer = 251180, deadTimer = 66940
sw1 (6900-A) -> show log swlog |grep ospf
2017 Jun 10 10:43:46 Pod18sw1 swlogd: ospf_0 INFO debug2(7) (11654):(3157):ENTER select usec=870000, lastMs=264773690, curMs=264773820.
2017 Jun 10 10:43:47 Pod18sw1 swlogd: ospf_0 INFO debug2(7) (11654):(3163):EXIT select with n=0, lastMs=264773690, curMs=264773820, drcTimeGetMs=264774691
2017 Jun 10 10:43:47 Pod18sw1 swlogd: ospf_0 AREA debug2(7) (11654):(3254):[curTime=251159s] Flooding area 0.0.0.0
2017 Jun 10 10:43:47 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 172.16.17.1, curTime = 251159, helloTimer = 251497, deadTimer = 75447
2017 Jun 10 10:43:47 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 172.16.18.1, curTime = 251159, helloTimer = 251160, deadTimer = 66940
2017 Jun 10 10:43:47 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 192.168.110.1, curTime = 251159, helloTimer = 251160, deadTimer = 66940
2017 Jun 10 10:43:47 Pod18sw1 swlogd: ospf_0 INFO debug2(7) (11654):(3157):ENTER select usec=999000, lastMs=264774690, curMs=264774691.

<<<PAGE 168>>>
DISPLAYING SWITCH LOGGING RECORDS
• Reverse 
• To display logs from the most recent to the oldest
• show log swlog [timestamp mm/dd/yyyy hh:mm:ss] [slot chassis/slot] [reverse]
2022 Jun 10 11:43:59 Pod18sw1 swlogd: ospf_0 AREA debug2(7) (11654):(3254):[curTime=251171s] Flooding area 0.0.0.0
2022 Jun 10 11:43:59 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 172.16.17.1, curTime = 251171, helloTimer = 251497, deadTimer = 75447
2022 Jun 10 11:43:58 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 172.16.18.1, curTime = 251171, helloTimer = 251180, deadTimer = 66940
2022 Jun 10 11:43:58 Pod18sw1 swlogd: ospf_0 TIME debug2(7) (11654):(1259):Intf addr 192.168.110.1, curTime = 251171, helloTimer = 251180, deadTimer = 66940

<<<PAGE 169>>>
READABLE CUSTOMER EVENT LOGS
• OmniSwitch is now designed to provide Readable Customer Event information about 
important events on the Switch 
• User-friendly, consistent and customer readable format.
• Use the following CLI commands to view Readable Customer Events.
• swlog appid command with level event to filter switch logging information for events
• To display customer event logs, enter the following command:
• The log output is in the following format:
• <SWLOG TIMESTAMP> : <CMM>/<NI> : <MODULE_NAME> : <LOG_DESCRIPTION>
swlog appid all subapp all level event
show log events
2019 Apr 28 19:17: 8.83 : CMM : ChassisSupervisor : chassisTrapsAlert - CERTIFY w/ FLASH SYNCHRO process started

<<<PAGE 170>>>
COMMAND LOGGING

<<<PAGE 171>>>
OVERVIEW
• Command Logging
• Logs commands and output
• Different than command history 
• Displays additional information
• Creates command.log file in /flash directory
• Command results stored in command.log
• Deleting command.log deletes log history
• Cannot be deleted while command logging is enabled
• Stores 100 most recent commands
• Must be enabled
-> command-log enable/disable

<<<PAGE 172>>>
EXAMPLE
-> show command-log
Command    : vlan 68 router ip 168.14.12.120 
UserName : admin 
Date     : MON APR 28 01:42:24 
Ip Addr
: 128.251.19.240 
Result   : SUCCESS
Command : vlan 68 router ip 172.22.2.13 
UserName : admin 
Date     : MON APR 28 01:41:51 
Ip Addr
: 128.251.19.240 
Result   : ERROR: Ip Address must not belong to IP VLAN 67 subnet
Command : command-log enable 
UserName : admin 
Date     : MON APR 28 01:40:55 
Ip Addr
: 128.251.19.240 
Result   : SUCCESS
Command : command-log enable
UserName : admin
Date     : MON APR 28 11:13:13
Ip Addr
: console
Result   : SUCCESS
-> show command-log status
CLI command logging: Enable

<<<PAGE 173>>>
PORT MIRRORING

<<<PAGE 174>>>
PORT MIRRORING
• Overview
• Copies all incoming and outgoing traffic from one 
switch port to another
• Destination port could be local (same switch) or 
remote (different switch)
• Provides the ability to perform a packet capture
• Specifications, check the specifications Guide to 
check the capacity of each switch’s model
• Ports supported
• Ethernet, Fast/ Gigabit Ethernet, 10/ 40 Gigabit 
Ethernet
• Port requirements - must be of identical capacity
-> port-mirroring <id> source port <s/s/p> destination port <s/s/p>
-> port-mirroring 1 source port 1/1/2-6 1/1/9 1/3/5 destination port 1/2/4

<<<PAGE 175>>>
PORT MIRRORING
• Port-mirroring Sessions and Destination Ports 
• On the 6860(E), 6860N, 6865, 6900 (all) in 8.9R3. 
• The same destination port can be used in different port mirroring sessions and the maximum port-mirroring 
sessions has been increased from 2 to 4. 
• There is a limit of 4 Mirror-to-port (MTP) indexes. 
• Bi-directional counts as two MTP indexes for each destination port in the session. 
• If a destination port is configured on multiple sessions and has the same source port mirror direction as those sessions the 
MTP index will only be counted once.
• Port Mirroring - Remote Over Linkagg 
• Remote port mirroring over a link aggregate is now supported on the OS6560. (in 8.9R3)
-> port-mirroring source destination
-> port-mirroring destination linkagg

<<<PAGE 176>>>
PORT MONITORING

<<<PAGE 177>>>
PORT MONITORING
• Captures data and stores in Sniffer format on switch
• Ports supported
• Ethernet, Fast/ Gigabit Ethernet, 10/40 Gigabit Ethernet
• Captures first 64-bytes of frame
• Session supported per switch or stack: 1
• Default file size:
• R8: 64 KB (max = 2 MB)
• Round-Robin or stop capture when max storage reached
• Cannot use port monitoring and mirroring on same port
• Characteristics in the specification guide.
• Data stored in compliance with the ENC file format (Network General Sniffer Format)
• 6 – session ID
• Session can be paused, resumed, disabled and associated with a timeout
-> port-monitoring 6 source port 1/2/3 enable
-> show port-monitoring file

<<<PAGE 178>>>
REMOTE MONITORING

<<<PAGE 179>>>
REMOTE MONITORING - RMON
• RMON probes are used to collect, interpret and forward statistical data about network 
traffic from designated active ports in a LAN segment
• Can be monitored using OmniVista
• 4 groups supported:
• Ethernet Statistics – Gather Ethernet port statistics (e.g. port utilization, error statistics)
• History Group - Stores sampling such as utilization and error count
• Alarms Group – Compare samplings to thresholds (e.g. absolute or relative, rising and falling thresholds)
• Events Group – Controls generation a notification to NMS station
Probe’s Owner: Analyzer-p:128.251.18.166 on Slot 1, Port 35
History Control Buckets Requested = 2
History Control Buckets Granted = 2
History Control Interval = 30 seconds
History Sample Index = 5859
Entry 10325
Flavor = History, Status = Active
Time = 48 hrs 53 mins,
System Resources (bytes) = 601
-> rmon probes alarm enable
-> rmon probes stats enable
-> show rmon probes history 30562

<<<PAGE 180>>>
SYSTEM HEALTH

<<<PAGE 181>>>
OVERVIEW
• Monitors switch resource utilization and thresholds
• Switch-level Input/Output
• Memory and CPU Utilization Levels
• Most recent utilization level (percentage)
• Average utilization level over the last minute (percentage)
• Average utilization level over the last hour (percentage)
• Maximum utilization level over the last hour (percentage)
• Threshold level
-> show health
sw8 (6860-B) -> show health
CMM                  Current   1 Min    1 Hr
1 Day
Resources                       Avg      Avg
Avg
--------------------+---------+-------+-------+-------
CPU                   11       13      11       0
Memory                57       57      57       0

<<<PAGE 182>>>
SFLOW

<<<PAGE 183>>>
Network
SFLOW - NETWORK MONITORING TECHNOLOGY
• Industry standard with many vendors
• Delivering products with sFlow support (RFC 3176)
• Gives visibility in to the activity of the network
• Provides network usage information and network 
wide view of usage and active routes
• Used for measuring network traffic, collecting, 
storing and analyzing the traffic data
• sFlow data applications
• Detecting, diagnosing and fixing network problems
• Real time congestion management
• detecting unauthorized network activity (DOS)  
• Usage accounting and billing
• Understanding application mix (web, DNS etc.) 
• Route profiling and peering optimization
• Capacity planning
Forwarding tables
Interface counters
Switching ASICs
sFlow Agent
Sampling
OmniSwitch

<<<PAGE 184>>>
OVERVIEW
• Traffic flows monitoring and sampling technology embedded within switches
• sFlow Agent software process running as part of the switch software
• sFlow Collector which receives, analyses the monitored data (3rd Party software)
• sFlow Collector makes use of SNMP to communicate with a sFlow agent in order to configure sFlow
monitoring on the device (switch)
Packet Header
In/out if
Sampling params
Forwarding
User ID
URL
Counters
Rate
pool
Src 802.1p/Q
Dst 802.1p/Q
Next hop
Src/dst mask
AS path
Communities
Src/Dst
Radius
TACACS
sFlow
sFlow
sFlow
sFlow

<<<PAGE 185>>>
SWITCH CONFIGURATION
• One agent to represent whole switch
•
•
• Represents the remote collector {destination IP address + port}
• Encodes samples into UDP datagrams
•
• One Sampler for each interface
• Collects packet samples
• One Poller for each interface
• Collects counter samples
RECEIVER
SAMPLER
AGENT
POLLER
-> ip service source-ip {Loopback0 | interface-name} sflow
-> show sflow agent
-> sflow receiver 1 name Server1 address 192.168.1.100
-> sflow receiver 2 name server2 address 172.30.130.102
-> sflow sampler 1 port 1/1/6 receiver 1 rate 5 sample-hdr-size 64
-> sflow poller 1 port 1/1/6 receiver 1 interval 20
-> show sflow receiver
-> show sflow sampler
-> show sflow poller

<<<PAGE 186>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 187>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Switch maintenance and Diagnostics tools 
How to 
✓ This lab is designed to familiarize you with some basic troubleshooting and 
debugging tools on an OmniSwitch. 
Contents 
1 
Switch Logging ................................................................................. 2 
2 
Readable Customer Event Logs .............................................................. 3 
3 
Command Logging ............................................................................. 4 
4 
Port Mirroring .................................................................................. 5 
5 
Port Monitoring ................................................................................ 5 
6 
Health ........................................................................................... 8 
7 
RMON ............................................................................................ 8

<<<PAGE 188>>>
2 
Switch maintenance and Diagnostics tools 
 
 1 
Switch Logging 
Switch Logging can be used to track informational or debugging messages from the switch. This is 
dependent upon the severity level set for a particular process. Logging can be configured to send its output 
to flash, console, or an external server.  By default, switch logging is enabled 
 
- On the 6870-A, type the following: 
sw7 (6870-A)-> show swlog 
Operational Status                 : Running, 
File Size per file                 : 1250 Kbytes, 
Log Device 1                       : console flash, 
Syslog FacilityID                  : local0(16), 
Hash Table entries age limit       : 60 seconds, 
Switch Log Preamble                : Enabled, 
Switch Log Debug                   : Disabled, 
Switch Log Duplicate Detection     : Enabled, 
Console Display Level              : info, 
RFC5424 Format Logging             : Disabled, 
Swlog Threshold                    : 90 percent, 
Swlog over TLS                     : Disabled, 
Output Socket Console              : Disabled, 
Swlog Default Level                : info, 
 
- You should see that logging is running and sending its output to both flash and the console. It does not 
mean that all messages will be displayed on the console, only messages matching the severity level, by 
default, informational (6). Logging can be disabled if desired.  
 
- Type the following: 
sw7 (6870-A) -> swlog disable 
 
sw7 (6870-A)-> show swlog 
Operational Status                 : Not Running, 
File Size per file                 : 1250 Kbytes, 
Log Device 1                       : console flash, 
Syslog FacilityID                  : local0(16), 
Hash Table entries age limit       : 60 seconds, 
Switch Log Preamble                : Enabled, 
Switch Log Debug                   : Disabled, 
Switch Log Duplicate Detection     : Enabled, 
Console Display Level              : info, 
RFC5424 Format Logging             : Disabled, 
Swlog Threshold                    : 90 percent, 
Swlog over TLS                     : Disabled, 
Output Socket Console              : Disabled, 
Swlog Default Level                : info, 
- To re-enable logging enter : 
sw7 (6870-A)-> swlog enable 
 
- The logging feature has a number of application IDs. These IDs are used to determine which process 
generated the logging message and at what severity level. Consult the user guide for a list of processes 
and associated severity levels. By default all processes are set to a severity level of 6, which is 
informational, as indicated above. All logging messages are stored in the swlog*.log files and can be 
viewed right on the switch. 
sw7 (6870-A)-> show log swlog 
 
 
Notes 
Use CTRL+C keys to stop the display of the file. 
You may also use show log swlog | grep “string to find” or show log swlog timestamp mm/dd/yy 
hh:mm:ss to find specific information on the log file.

<<<PAGE 189>>>
3 
Switch maintenance and Diagnostics tools 
 
 2 
Readable Customer Event Logs 
 
AOS is now designed to provide Readable Customer Event information about important events on the 
OmniSwitch in a user-friendly, consistent and customer readable format. A new set of CLI commands are 
introduced to view Readable Customer Events. Unlike AOS Syslog, Readable Customer Event feature provides 
logs for the most significant switch events 
 
- On the 6870-A, type the following: 
 
sw7 (6870-A)-> swlog appid all subapp all level event 
 
- To display customer event logs, enter the following command. 
sw7 (6870-A)-> show log events 
2019 Jul 15 20:26:27.515 : CMM : vc_licManager : Demo License will expire on date: 7/14/2019 
2019 Jul 15 20:26:53.212 : CMM : ChassisSupervisor : chassisTrapsAlert - Power supply is OK: PS 1 
2019 Jul 15 20:26:53.213 : CMM : ChassisSupervisor : chassisTrapsAlert - All power supplies OK 
2019 Jul 15 20:26:53.213 : CMM : ChassisSupervisor : The switch was restarted by the user 
2019 Jul 15 20:26:53.213 : CMM : ChassisSupervisor : chassisTrapsAlert - CMM startup completed 
2019 Jul 15 20:27:35.755 : CMM : stpCmm : STP instance 1: Bridge has become new Root 
2019 Jul 15 20:27:50.148 : CMM : vcmCmm : Virtual Chassis: Chassis 1 Role changed to Master 
2019 Jul 15 20:27:50.148 : CMM : vcmCmm : Virtual Chassis: Chassis 1 Status changed to Running 
2019 Jul 15 20:27:50.149 : CMM : ChassisSupervisor : Sending VC Takeover to NIs and applications [L6] 
2019 Jul 15 20:27:52.299 : CMM : ChassisSupervisor : System Ready 
2019 Jul 15 20:37:21.569 : CMM : stpCmm : STP instance 112: Bridge has become new Root 
2019 Jul 15 20:39:47.696 : CMM : intfCmm : Link 1/2/1 operationally up 
2019 Jul 15 20:39:51.772 : CMM : stpCmm : STP instance 112: Root port change detected 
2019 Jul 15 20:47: 3.234 : CMM : intfCmm : Link 1/2/1 operationally down 
2019 Jul 15 20:47: 4.370 : CMM : stpCmm : STP instance 112: Bridge has become new Root 
2019 Jul 15 20:49:32.102 : CMM : intfCmm : Link 1/2/1 operationally up 
... 
 
- Compare the output of this command with the show log swlog from the previous section 
Notice the difference in the output of both commands 
The show log events command has the following output: 
 
<SWLOG TIMESTAMP>: <CMM>/<NI>: <MODULE_NAME>: <LOG_DESCRIPTION>

<<<PAGE 190>>>
4 
Switch maintenance and Diagnostics tools 
 
 3 
Command Logging 
Like switch logging, commands entered on the OmniSwitch can captured to a log file. These can then be 
reviewed later to see what changes have been made. This is a very valuable tool, especially when modifying 
the switch configuration.  
 
- Type the following: 
 
sw7 (6870-A)-> show command-log 
 
sw7 (6870-A)-> command-log enable 
-  
- Let's create and delete a couple of VLAN's to demonstrate: 
 
sw7 (6870-A)-> vlan 4-5 
 
sw7 (6870-A)-> no vlan 4-5 
 
sw7 (6870-A)-> show command-log 
Command : no vlan 4-5 
  UserName : admin 
  Date     : Tue Feb 11 03:54:58 
  Ip Addr  : console 
  Result   : SUCCESS 
 
Command : vlan 4-5 
  UserName : admin 
  Date     : Tue Feb 11 03:54:53 
  Ip Addr  : console 
  Result   : SUCCESS 
 
Command : command-log enable 
  UserName : admin 
  Date     : Tue Feb 11 03:53:33 
  Ip Addr  : console 
  Result   : SUCCESS 
 
- You should now see the commands you entered displayed on the screen with information about the time 
and where they were entered from, such as a console or TELNET session. 
- To disable it enter : 
sw7 (6870-A)-> command-log disable

<<<PAGE 191>>>
5 
Switch maintenance and Diagnostics tools 
 
 4 
Port Mirroring 
Port mirroring can be configured to copy traffic from one or multiple ports to another. The destination port 
would normally have a traffic analyzer connected.   
 
- Let’s create a mirroring session to copy traffic from one port to another.  
 
sw7 (6870-A)-> port-mirroring 1 source port 1/1/1 destination port 1/1/10 
 
sw7 (6870-A)-> port-mirroring 1 enable 
 
sw7 (6870-A)-> show port-mirroring status 1 
 
 Session    Mirror        Mirror      Unblocked   RPMIR              Config    Oper 
           Destination    Direction     Vlan       Vlan      Mode    Status    Status 
----------+-----------+--------------+----------+---------+---------+----------+---------- 
   1.        1/1/10           -         NONE      NONE         NONE   Enable     Off 
----------+-----------+--------------+----------+---------+---------+--------------------- 
           Mirror 
           Source 
----------+-----------+--------------+----------+----------+--------+--------------------- 
   1.         1/1/1      bidirectional     -         -                Enable      Off 
 
- To remove a port mirroring session, enter : 
 
sw7 (6870-A)-> no port-mirroring 1 
 
 
The maximum number of mirroring sessions is limited to two. 
 5 
Port Monitoring 
Port Monitoring makes it possible to capture traffic being sent to and from a port and store it in  /flash in 
".enc" (or Sniffer) format. The data is stored in a file named pmonitor.enc by default, but this can be 
modified. The file can then be transferred off the switch and viewed in detail using a traffic analyzer. It is 
also possible to display the output directly to the console or to a telnet session.  
 
- Start a port monitoring session : 
 
sw7 (6870-A)-> interfaces 1/1/1 admin-state enable 
 
sw7 (6870-A)-> port-monitoring 1 source port 1/1/1 enable 
 
sw7 (6870-A)-> show port-monitoring status 
 
 Sess Mon.    Mon. Over  Oper.  Admin  Capt.   Max.   File 
      Src     Dir  write Stat   Stat   Type    Size   Name 
-----+-------+----+-----+------+------+-------+------+----------------------- 
  1.   1/1/1  Bi    ON     ON    ON   Brief     64K  /flash/pmonitor.enc 
 
- Generate traffic from client by issuing pings to any reachable address. 
 
- The session can be paused and resumed if necessary, type the following: 
 
sw7 (6870-A)-> port-monitoring 1 pause 
 
sw7 (6870-A) -> show port-monitoring status

<<<PAGE 192>>>
6 
Switch maintenance and Diagnostics tools 
 
 Sess Mon.    Mon. Over  Oper.  Admin  Capt.   Max.   File 
      Src     Dir  write Stat   Stat   Type    Size   Name 
-----+-------+----+-----+------+------+-------+------+----------------------- 
  1.    1/1/1  Bi    ON    OFF    ON   Brief      64K  /flash/pmonitor.enc 
 
 
sw7 (6870-A)-> port-monitoring 1 resume 
-  
sw7 (6870-A) -> show port-monitoring status 
 
 Sess Mon.    Mon. Over  Oper.  Admin  Capt.   Max.   File 
      Src     Dir  write Stat   Stat   Type    Size   Name 
-----+-------+----+-----+------+------+-------+------+----------------------- 
  1.    1/1/1  Bi    ON     ON    ON   Brief      64K  /flash/pmonitor.enc 
 
sw7 (6870-A)-> port-monitoring 1 disable 
WARNING: 
Monitored data is available in file /flash/pmonitor.enc 
 
- You should now see a message indicating that it has finished writing the capture file. The data is stored in 
a file called pmonitor.enc in the /flash directory.  
 
sw7 (6870-A)-> ls -l 
total 7948 
-rw-r--r--    1 admin    user       4053444 Jan  1  2021 UAppSig.upgrade_kit 
drwxr-xr-x    2 admin    user          4096 Jan  5  2021 bootflash 
drwxr-xr-x    2 admin    user          4096 Jan  1 00:06 certified 
-rw-r--r--    1 admin    user         66402 Feb 11 03:54 command.log 
drwxr-xr-x    2 admin    user          4096 Dec  4 17:20 diags 
-rw-r--r--    1 admin    user        526184 Dec  4 17:20 eeprom 
drwxr-xr-x    5 admin    user          4096 Jan  1 00:04 externalCPU 
drwxr-xr-x    2 admin    user          4096 Feb  8 01:19 foss 
-rw-r--r--    1 admin    user           239 Feb  8 01:20 hwinfo 
drwxr-xr-x    2 admin    user          4096 Jan  1  2021 labinit 
drwxr-xr-x    2 admin    user         16384 Dec  4 17:21 lost+found 
drwxr-xr-x    2 admin    user          4096 Jan  5  2021 network 
drwxr-xr-x    3 admin    user          4096 Jan  5  2021 pmd 
-------r--    1 root     root          4835 Feb 11 04:09 pmonitor.enc 
drwxrwx---    2 root     admins        4096 Jan  1 00:00 python 
-rw-r--r--    1 admin    user          2848 Jan  2 21:45 snapall 
drwxr-xr-x    6 admin    user          4096 Jan  1 00:01 switch 
-rw-r--r--    1 admin    user        735660 Jan  1  2021 swlog 
drwxr-xr-x    2 admin    user          4096 Feb  8 01:21 swlog_archive 
-rw-r--r--    1 admin    user        740893 Feb 11 04:09 swlog_chassis1 
-rw-r--r--    1 admin    user       1280009 Feb  7 19:13 swlog_chassis1.0 
drwxr-xr-x    2 admin    user          4096 Jan  5  2021 system 
-------r--    1 root     root          4835 Feb 11 02:06 test.cap 
-rw-r--r--    1 admin    user        594809 Jan  1  2021 u-boot.8.2.1.R01.255.tar.gz 
-rw-r--r--    1 admin    user          3453 Jan  1  2021 u-boot_copy 
drwxr-xr-x    2 admin    user          4096 Feb  8 01:20 working

<<<PAGE 193>>>
7 
Switch maintenance and Diagnostics tools 
 
- To display the capture, enter : 
 
sw7 (6870-A)-> show port-monitoring file 
Destination       | Source            |  Type  | Data 
------------------------------------------------------------------------------- 
01:80:C2:00:00:00 | E8:E7:32:F6:16:20 |  2700  | 00:27:42:42:03:00:00:02:02:7C 
 
01:80:C2:00:00:00 | E8:E7:32:F6:16:20 |  2700  | 00:27:42:42:03:00:00:02:02:7C 
 
01:80:C2:00:00:00 | E8:E7:32:F6:16:20 |  2700  | 00:27:42:42:03:00:00:02:02:7C 
 
01:80:C2:00:00:00 | E8:E7:32:F6:16:20 |  2700  | 00:27:42:42:03:00:00:02:02:7C 
 
01:80:C2:00:00:00 | E8:E7:32:F6:16:20 |  2700  | 00:27:42:42:03:00:00:02:02:7C 
 
- Use the ‘?’ to display additional parameters. How would you change the name of the capture file? 
 
sw7 (6870-A)-> show port-monitoring ? 
                                    ^ 
                                    STATUS FILE 
 
- When done, delete the monitoring session. 
 
sw7 (6870-A)-> show port-monitoring status 
 
 Sess Mon.    Mon. Over  Oper.  Admin  Capt.   Max.   File 
      Src     Dir  write Stat   Stat   Type    Size   Name 
-----+-------+----+-----+------+------+-------+------+----------------------- 
  1.   1/1/1  Bi    ON    OFF   ON    Brief     64K  /flash/pmonitor.enc 
 
sw7 (6870-A)-> no port-monitoring 1

<<<PAGE 194>>>
8 
Switch maintenance and Diagnostics tools 
 
 6 
Health 
The Health feature can be used to gather basic information on the state of the switch such as CPU, memory 
and traffic utilization information. 
 
sw7 (6870-A)-> show health 
CMM                  Current    1 Min    1 Hr   1 Day 
Resources                         Avg      Avg    Avg 
----------------------+---------+-------+-------+------- 
CPU                      7        7       7       6 
Memory                  64       64      64      64 
 
sw7 (6870-A)-> show health slot 1/1 
Slot  1/ 1             Current    1 Min    1 Hr   1 Day 
Resources                         Avg      Avg    Avg 
----------------------+---------+-------+-------+------- 
CPU                      9        7       7       6 
Memory                  65       65      65      65 
Receive                  0        0       0       0 
Receive/Transmit         0        0       0       0 
 7 
RMON 
Remote Monitoring can be used to gather statistics for displaying in OmniVista or other NMS solutions.  
 
 
Make sure that interface 1/1/1 is enabled so you can get these statistics. 
-> interfaces 1/1/1 admin-state enable 
 
sw7 (6870-A)-> show rmon probes 
 
        Chassis/ 
 Entry  Slot/Port  Flavor    Status      Duration     System Resources 
-------+----------+---------+-----------+------------+---------------- 
     24 1/1/24     Ethernet  Active      01:20:37     301 bytes 
     23 1/1/23     Ethernet  Active      01:20:36     301 bytes 
      5 1/1/5      Ethernet  Active      01:20:33     300 bytes 
      1 1/1/1      Ethernet  Active      00:37:10     300 bytes 
 
sw7 (6870-A)-> show rmon probes history 
 
        Chassis/ 
 Entry  Slot/Port  Flavor    Status      Duration     System Resources 
-------+----------+---------+-----------+------------+---------------- 
      2 1/1/24     History   Active      01:21:39     5471 bytes 
      3 1/1/23     History   Active      01:21:38     5471 bytes 
      4 1/1/5      History   Active      01:21:35     5470 bytes 
      5 1/1/1      History   Active      00:38:12     5470 bytes 
 
 
sw7 (6870-A)-> show rmon probes stats 
 
 
        Chassis/ 
 Entry  Slot/Port  Flavor    Status      Duration     System Resources 
-------+----------+---------+-----------+------------+---------------- 
     24 1/1/24     Ethernet  Active      01:22:22     301 bytes 
     23 1/1/23     Ethernet  Active      01:22:21     301 bytes 
      5 1/1/5      Ethernet  Active      01:22:18     300 bytes 
      1 1/1/1      Ethernet  Active      00:38:55     300 bytes 
 
 
 
 
sw7 (6870-A)-> show rmon probes stats 1

<<<PAGE 195>>>
9 
Switch maintenance and Diagnostics tools 
 
Probe's Owner: Switch Auto Probe on Chassis 1, Slot 1, Port 1, ifindex 1001 
    Entry    1 
      Flavor = Ethernet, Status = Active, 
      Time = 74 hrs 23 mins, 
      System Resources (bytes) = 300 
 
 
You can also use “show rmon probes history 1” and “show rmon probes alarm 1” to display related 
information.

<<<PAGE 196>>>
LINK AGGREGATION GROUPS
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 197>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the Link Aggregation operation on 
AOS based switches
• Learn how to configure
• Static Link Aggregation
• Dynamic Link Aggregation
• Load Balancing Control

<<<PAGE 198>>>
OVERVIEW
• Goal
• Method of aggregating (combining) more than 2 ports/links so that the switch will “see” them as 
one logical link
• Advantages of Link Aggregation
• Scalability
• Reliability
• Ease of Migration
• Provides an aggregated link
(multiple physical links combined into one logical link)
Logical Link can be statically assigned to any VLAN
802.1q can be configured on the logical aggregated link

<<<PAGE 199>>>
STATIC VS. DYNAMIC
• Difference between Static and Dynamic
• Static
• Port parameters MUST be exactly the same at both ends and within the group
• same speed (e.g., all 10 Mbps, all 100 Mbps, all 1 Gigabit, or all 10 Gigabit)
• Only works between Alcatel-Lucent OmniSwitches
• Dynamic
• IEEE 802.3ad LACP
• LACP will negotiate the optimal parameters for both ends using LACPDU (Link Aggregation Control Protocol 
Data Unit)
• Ports must be of the same speed within the same aggregate group 
• It also works between two different devices such as switches, servers and storage systems.
• Refer to specification guide for the characteristics

<<<PAGE 200>>>
STATIC LINK AGGREGATION GROUPS - CLI
• Creating a Static Aggregate Group
• Adding Ports to a Static Aggregate Group
• Removing Ports from a Static Aggregate Group
-> linkagg static agg <agg_num> size <size> admin-state enable
-> no linkagg static port <Chassis/slot/port>
-> linkagg static port < Chassis/slot/port> agg <agg_num>

<<<PAGE 201>>>
DYNAMIC LINK AGGREGATION GROUPS - CLI
• Configuring a Dynamic Link Aggregation Group
• Assigning ports to the Dynamic Link Aggregation Group
-> linkagg lacp agg <agg_num> size <size> admin-state enable
-> linkagg lacp agg <agg_num>
actor admin-key <actor_admin_key>
-> linkagg lacp port <chassis/slot/port> actor admin-key <actor_admin_key>

<<<PAGE 202>>>
MONITORING
• Static & Dynamic Link Aggregation Groups can be used for VLAN tagging (802.1q)
• Useful monitoring commands:
-> vlan <vlan_id> members linkagg <agg_num> untagged
-> vlan <vlan_id> members linkagg <agg_num> tagged
-> show linkagg
Number Aggregate
SNMP Id  Size  Admin State   Oper State  Att/Sel Ports
------+----------+--------+-----+-------------+------------+-------------
1 
Static
40000001  8    ENABLED        UP           2 2
2 
Dynamic     40000002  4    ENABLED        DOWN         0 0
3 
Dynamic     40000003  8    ENABLED        DOWN         0 2
4
Static
40000005  2    DISABLED       DOWN         0 0
-> show linkagg <agg_num> port </Chassis/slot/port>

<<<PAGE 203>>>
LINK AGGREGATION STATISTICS

<<<PAGE 204>>>
LINK AGGREGATION STATISTICS
• To display the statistics for a linkagg, all the physical ports in the linkagg are identified, 
and relevant statistics are aggregated and displayed for various show commands. 
Command
Usage 
show linkagg counters
Displays statistics collected for the type and number of packets 
transmitted and received on link aggregate ports.
show linkagg traffic
Displays the total number of packets and bytes that are received and 
transmitted on link aggregate ports.
show linkagg accounting
Displays statistics collected for packets transmitted and received on 
link aggregate ports.
show linkagg port 
Displays information about link aggregation ports.

<<<PAGE 205>>>
LOAD BALANCING CONTROL

<<<PAGE 206>>>
HASHING CONTROL ALGORITHM
• Hashing Control
• Control over the hashing mode
• Link Aggregation
• ECMP
• Server Load Balancing
• Two hashing algorithms available
• Brief Mode 
• UDP/TCP ports not included
• Only Source IP and destination IP addresses 
are considered
• Extended 
• UDP/TCP ports to be included in the hashing 
algorithm
• Result in more efficient load balancing
Source
Address
Destination
Address
Server #
Brief Mode
Source
Address
Destination
Address
Server #
UDP/TCP
Port
Extended Mode
Switch
Default Hashing Mode
9900
extended
6900
brief
6870
extended
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
-> hash-control extended [ udp-tcp-port | no]

<<<PAGE 207>>>
LOAD BALANCING MULTICAST ON LINK AGGREGATION 
GROUPS
• Multicast traffic is by default forwarded through the primary port of the Link Aggregation 
Group
• User has the option to enable hashing for non-unicast traffic, which will load balance the 
non-unicast traffic across all ports in the Link Aggregation Group
• If non-ucast option is not specified, link aggregation will only load balance unicast packets

<<<PAGE 208>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 209>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Link Aggregation 
How to 
✓ Create Dynamic Aggregation Links 
Contents 
1 
Topology ........................................................................................ 2 
2 
Creating a Dynamic Link Aggregation ...................................................... 3 
2.1. Creating a Dynamic Link Aggregation between the 6360 virtual chassis and the 6870-A 3 
2.1.1. On the 6360 virtual chassis ................................................................................ 3 
2.1.2. On the 6870-A ............................................................................................... 4 
3 
Testing the configuration .................................................................... 7

<<<PAGE 210>>>
2 
Link Aggregation 
 
 1 
Topology 
Link Aggregation provides the ability to combine multiple physical ports into a single logical port for added 
throughput and redundancy. In this lab, you will create dynamic link aggregation using the IEEE 802.3ad (LACP) 
protocol. 
In this lab, you are going to create a new link aggregation between the 6360 Virtual Chassis and 6870-A. The link 
aggregation 78 (Vlan 278) has been already created between the OS6870-A and the 6860-B. 
Furthermore, for security reason, the client wants to avoid using the VLAN1 (the default VLAN). Thus, the 
default VLAN on the link aggregation will be the VLAN 57.

<<<PAGE 211>>>
3 
Link Aggregation 
 
 2 
Creating a Dynamic Link Aggregation 
2.1. 
Creating a Dynamic Link Aggregation between the 6360 virtual chassis and the 6870-A 
2.1.1. 
On the 6360 virtual chassis 
 
 
 
- Now, we will define a dynamic link aggregate, assign the group ID 7 and configure its size to 2: 
sw5 (OS6360-A) -> linkagg lacp agg 7 size 2 actor admin-key 7 
 
 
Notes: Actor Admin Key 
The link aggregation number and ports are associated to a dynamic link aggregation using the actor admin key. 
Although in the above example the actor admin key matches the link aggregation number, this is not a 
requirement as the admin key has local significance only. 
 
- Check the link aggregation status on the OS6360-A: 
sw5 (6360-A) -> show linkagg 
                                   
Number  Aggregate  SNMP Id   Size  Admin State  Oper State     Att/Sel Ports 
-------+----------+---------+----+------------+--------------+------------- 
 
- Notice we have no ports associated to the link aggregation 7 : 
 
- Using the actor admin key assigned to the link aggregation, associate the ports 1/1/3 and 2/1/4 to the 
linkagg 7: 
sw5 (6360-A) -> linkagg lacp port 1/1/3 actor admin-key 7 
sw5 (6360-A) -> linkagg lacp port 2/1/4 actor admin-key 7 
 
- Enable the ports:  
sw5 (6360-A) -> interfaces 1/1/3 admin-state enable 
sw5 (6360-A) -> interfaces 2/1/4 admin-state enable

<<<PAGE 212>>>
4 
Link Aggregation 
 
- Now 2 ports are linked to the link aggregation, but the link aggregation is still DOWN, because the 
configuration on the other side (on the 6870-A) has not been done yet.  
sw5 (6360-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
   7     Dynamic      40000007   2   ENABLED      DOWN             0      0 
 
 
sw5 (6360-A) -> show linkagg agg 7 port 
 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
2.1.2. 
On the 6870-A 
 
- Create the link aggregation 7: 
sw7 (OS6870-A) -> linkagg lacp agg 7 size 2 actor admin-key 7 
 
 
Notes: Actor Admin Key 
The link aggregation number and ports are associated to a dynamic link aggregation using the actor admin key. 
Although in the above example the actor admin key matches the link agg number, this is not a requirement as 
the admin key has local significance only. 
 
- Associate the port 1/1/3 and 1/1/4 to the link aggregation 7: 
sw7 (OS6870-A) -> linkagg lacp port 1/1/3-4 actor admin-key 7 
 
- Enable the ports:  
sw7 (OS6870-A) -> interface 1/1/3-4 admin-state enable 
 
- Check the link aggregation status on the OS6870-A: 
sw7 (OS6870-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
   7     Dynamic      40000007   2   ENABLED      UP              2   2 
  17     Dynamic      40000017   2   ENABLED      UP              1   1 
  78     Dynamic      40000078   2   ENABLED      UP              2   2 
 
 
Notes: Link Aggregation 17? 78?  
On the 6870-A, 3 link aggregations are available: the new one you created (linkagg 7), plus 2 other link 
aggregations (17 and 78) used to connect the switch to the 6900 and 6860-B (Core network part). These two 
other aggregations have already been created on a previous lab or via a configuration download at the 
beginning of the course depending on the course you are taking.

<<<PAGE 213>>>
5 
Link Aggregation 
 
 
- Check the link aggregation properties on the 6870-A: 
sw7 (6870-A) -> show linkagg agg 7 
 
Dynamic Aggregate 
  SNMP Id                  : 40000007, 
  Aggregate Number         : 7, 
  SNMP Descriptor          : Dynamic Aggregate Number 7 ref 40000007 size 2, 
  Name                     : , 
  Admin State              : ENABLED, 
  Operational State        : UP, 
  Aggregate Size           : 2, 
  Number of Selected Ports : 2, 
  Number of Reserved Ports : 2, 
  Number of Attached Ports : 2, 
  Primary Port             : 1/1/3, 
  Port Selection Hash      : Source Destination Ip, 
  Wait To Restore Time     : 0 Minutes 
LACP 
  MACAddress               : [2c:fa:a2:0e:62:49], 
  Actor System Id          : [00:00:00:00:00:00], 
  Actor System Priority    : 0, 
  Actor Admin Key          : 7, 
  Actor Oper Key           : 7, 
  Partner System Id        : [00:00:00:00:00:00], 
  Partner System Priority  : 0, 
  Partner Admin Key        : 0, 
  Partner Oper Key         : 7 
  Agg-Down/Violation Reason: None,

<<<PAGE 214>>>
6 
Link Aggregation 
 
- Check the link aggregation properties on the 6360 Virtual Chassis: 
sw5 (6360-A) -> show linkagg agg 7 
 
Dynamic Aggregate 
  SNMP Id                  : 40000007, 
  Aggregate Number         : 7, 
  SNMP Descriptor          : Dynamic Aggregate Number 7 ref 40000007 size 2, 
  Name                     : , 
  Admin State              : ENABLED, 
  Operational State        : UP, 
  Aggregate Size           : 2, 
  Number of Selected Ports : 2, 
  Number of Reserved Ports : 2, 
  Number of Attached Ports : 2, 
  Primary Port             : 1/1/3, 
  Port Selection Hash      : Source Destination Ip, 
  Wait To Restore Time     : 0 Minutes 
LACP 
  MACAddress               : [94:24:e1:7c:79:6f], 
  Actor System Id          : [00:00:00:00:00:00], 
  Actor System Priority    : 0, 
  Actor Admin Key          : 7, 
  Actor Oper Key           : 7, 
  Partner System Id        : [00:00:00:00:00:00], 
  Partner System Priority  : 0, 
  Partner Admin Key        : 0, 
  Partner Oper Key         : 7 
  Agg-Down/Violation Reason: None, 
 
- By default, a link aggregation is associated with the VLAN 1 (default VLAN). 
- For security reason, the client wants to avoid using the VLAN 1 as the network data VLAN. So, the VLAN 
associated with link aggregation 7 must be modified:  
o 
On the 6360-A: 
sw5 (6360-A) -> vlan 57 
sw5 (6360-A) -> vlan 57 members linkagg 7 untagged 
 
sw5 (6360-A) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/7         untagged     forwarding  
 
 
o 
On the 6870-A: 
sw7 (OS6870-A)-> vlan 57 
sw7 (OS6870-A)-> vlan 57 members linkagg 7 untagged 
 
sw7 (6870-A) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        untagged     forwarding

<<<PAGE 215>>>
7 
Link Aggregation 
 
 3 
Testing the configuration 
To test the link aggregation, we will launch a ping between 2 clients connected on each side (Client 5 on the 
6360 Virtual Chassis, Client 7 on the 6870-A), then we will simulate a failure on the link aggregation. 
 
Infrastructure  
 
 
 
- Put the Client 7 in the VLAN 57 (6870-A): 
sw7 (OS6870-A)-> vlan 57 members port 1/1/1 untagged 
sw7 (OS6870-A)-> interfaces 1/1/1 admin-state enable 
 
- Put the Client 5 in the VLAN 57 (6360-A): 
Sw5 (OS6360-A)-> vlan 57 members port 1/1/1 untagged 
Sw5 (OS6360-A)-> interfaces 1/1/1 admin-state enable 
 
Client 5  
Double-click on VMware vSphere 
 
Select the Client5 in the list 
 
Click on Console tab 
Double click on Network 
Connections

<<<PAGE 216>>>
8 
Link Aggregation 
 
Select the network connection 
Pod 
 
Click on Internet Protocol 
(TCP/IP) 
 
Select Use the following IP 
address 
 
- IP address: 192.168.57.105 
- Subnet mask: 255.255.255.0 
 
 
 
 
Client 7 
Double-click on VMware vSphere 
 
Select the Client7 in the list 
 
Click on Console tab 
 
Double click on Network 
Connections 
 
Select the network connection 
Pod 
 
Click on Internet Protocol 
(TCP/IP) 
 
Select Use the following IP 
address 
 
- IP address: 192.168.57.107 
- Subnet mask: 255.255.255.0 
 
 
 
 
- From client 5, launch a continuous ping (-t option) to the Client 7:  
C:\Program Files […]\Tools> ping -t 192.168.57.107

<<<PAGE 217>>>
9 
Link Aggregation 
 
- To demonstrate the redundancy capabilities, put a port (belonging to the link aggregation) down, and 
monitor the results of your pings tests.  
sw7 (6870-A) -> interface 1/1/3 admin-state disable 
 
 
 
sw7 (6870-A) -> show linkagg port 
 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
          1/1/3     Dynamic      1003   CONFIGURED NONE  DOWN DOWN  UNK 
          1/1/4     Dynamic      1004   ATTACHED      7  UP   UP    YES 
          1/1/5     Dynamic      1005   ATTACHED     17  UP   UP    YES 
         1/1/23     Dynamic      1023   ATTACHED     78  UP   UP    YES 
         1/1/24     Dynamic      1024   ATTACHED     78  UP   UP    NO 
 
- Once finished, reactivate the port 1/1/3: 
sw7 (6870-A) -> interface 1/1/3 admin-state enable

<<<PAGE 218>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
802.1q 
How To 
✓ Apply 802.1q tagging on link aggregation and ports 
Content 
1 
Topology ........................................................................................ 2 
2 
Enabling the 802.1Q Tagging ................................................................ 2 
2.1. Tagging a Link ....................................................................................... 2 
2.1.1. On the 6360 Virtual Chassis ............................................................................... 2 
2.1.2. On the 6860-B ............................................................................................... 2 
2.2. Creating Additional VLANs ........................................................................ 3 
2.3. Configuring 802.1Q on Ports ...................................................................... 4 
3 
Testing the Configuration .................................................................... 6

<<<PAGE 219>>>
2 
802.1q 
 
 1 
Topology 
In a Layer 2 environment the Ports is used for bridging traffic across a physical connection between switches. In 
an IEEE 802.1Q environment, the Default VLAN for the port is bridged, and all the other VLANs will have the 
IEEE 802.1Q tag inserted for proper VLAN association at the remote side. 
 
 2 
Enabling the 802.1Q Tagging 
2.1. 
Tagging a Link 
In this part, we are going to configure the link between the 6360 Virtual Chassis and the 6860-B. 
2.1.1. 
On the 6360 Virtual Chassis 
- Activate the port 2/1/3 on the 6360 Virtual Chassis (linked to the 6860-B):  
sw5 (6360-A) -> interfaces 2/1/3 admin-state enable 
- Create the VLAN 58, then modify the VLAN on the port 2/1/3 from the default VLAN to VLAN 58: 
sw5 (6360-A) -> vlan 58 
sw5 (6360-A) -> vlan 58 members port 2/1/3 untagged 
 
sw5 (6360-A) -> show vlan 58 member 
   port      type        status 
----------+-----------+--------------- 
  2/1/3      untagged        inactive 
2.1.2. 
On the 6860-B 
- Activate the port 1/1/3 on the 6860-B (linked to the 6360 Virtual Chassis):  
sw8 (6860-B) -> interfaces 1/1/3 admin-state enable 
- Create the VLAN 58, then modify the VLAN on the port 1/1/3 from the default VLAN to VLAN 58:  
sw8 (6860-B) -> vlan 58 
sw8 (6860-B) -> vlan 58 members port 1/1/3 untagged 
 
sw8 (6860-B) -> show vlan 58 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/3      untagged      forwarding

<<<PAGE 220>>>
3 
802.1q 
 
2.2. 
Creating Additional VLANs 
Currently, only 2 VLANs are bridged: 
- VLAN 57 between the 6870-A and the 6360 Virtual Chassis 
- VLAN 58 between the 6860-B and the 6360 Virtual Chassis 
- Create the VLANs 20 and 30 on the 3 switches (Virtual Chassis of 6360-A, 6870-A et 6860-B) : 
sw5 (6360-A) -> vlan 20 
sw5 (6360-A) -> vlan 30 
 
sw7 (6870-A) -> vlan 20 
sw7 (6870-A) -> vlan 30 
 
sw8 (6860-B) -> vlan 20 
sw8 (6860-B) -> vlan 30 
 
The gateway for the VLAN 20 will be created on the 6870-A. 
The gateway for the VLAN 30 will be created on the 6860-B. 
 
- Assign an IP interface to these 2 new VLAN on the correspondent switches: 
sw7 (6870-A) -> ip interface int_20 address 192.168.20.7/24 vlan 20 
 
sw8 (6860-B) -> ip interface int_30 address 192.168.30.8/24 vlan 30 
 
- Check the configuration: 
sw8 (6860-B) -> show ip interface 
Total 6 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.8      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
Loopback0                        192.168.254.8   255.255.255.255     UP     YES Loopback0 
--- 
int_278                          172.16.78.8     255.255.255.0       UP     YES vlan 278 
int_30                           192.168.30.8    255.255.255.0     DOWN      NO vlan 30 
 
sw7 (6870-A) -> show ip interface 
Total 7 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.7      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
Loopback0                        192.168.254.7   255.255.255.255     UP     YES Loopback0 
--- 
int_20                           192.168.20.7    255.255.255.0     DOWN      NO vlan 20 
int_217                          172.16.17.7     255.255.255.0       UP     YES vlan 217 
int_278                          197.16.78.7     255.255.255.0       UP     YES vlan 278 
- The IP interfaces status is DOWN. Why? 
---------------------------------------------------------------------------------------------------------------------------- 
----------------------------------------------------------------------------------------------------------------------------

<<<PAGE 221>>>
4 
802.1q 
 
2.3. 
Configuring 802.1Q on Ports 
- Our VLAN 20 and 30 IP interfaces are currently down because we have no members in the two VLANs. 
Remember, if there are no members of a VLAN the IP interface is not only down but will not be advertised 
to the Layer 3.  
- Normally, to have Layer 2 connectivity between the two switches for all three VLANs, three physical links 
would be required. However, we will configure 802.1Q tagging to carry data from all VLANs over physical 
link. 
 
- For now, no port has been assigned neither to VLAN 20 nor VLAN 30. 
- Tag the VLANs 20 and 30 on the link between the 3 switches (in red on the diagram below): 
 
 
sw5 (6360-A) -> vlan 20 members linkagg 7 tagged  
sw5 (6360-A) -> vlan 30 members linkagg 7 tagged 
 
sw5 (6360-A) -> vlan 20 members port 2/1/3 tagged 
sw5 (6360-A) -> vlan 30 members port 2/1/3 tagged 
 
sw7 (6870-A) -> vlan 20 members linkagg 78 tagged  
sw7 (6870-A) -> vlan 30 members linkagg 78 tagged 
 
sw7 (6870-A) -> vlan 20 members linkagg 7 tagged  
sw7 (6870-A) -> vlan 30 members linkagg 7 tagged 
 
sw8 (6860-B) -> vlan 20 members linkagg 78 tagged 
sw8 (6860-B) -> vlan 30 members linkagg 78 tagged 
 
sw8 (6860-B) -> vlan 20 members port 1/1/3 tagged 
sw8 (6860-B) -> vlan 30 members port 1/1/3 tagged 
 
- Check the VLAN-port association on each switch: 
 
 
Notes 
The ports status available in the tables below depend on the STP root bridge election. Could be different on 
your pod.

<<<PAGE 222>>>
5 
802.1q 
 
- On the 6360-A: 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  2/1/3      tagged      forwarding 
  0/7        tagged      forwarding 
 
 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  2/1/3      tagged      forwarding 
  0/7        tagged      forwarding 
 
 
sw5 (6360-A) -> show vlan members port 2/1/3 
  vlan      type        status 
--------+-----------+--------------- 
    20    tagged       forwarding 
    30    tagged       forwarding 
    58    untagged     forwarding 
 
o 
On the 6870-A: 
sw7 (6870-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        tagged      forwarding 
  0/78       tagged      forwarding 
 
sw7 (6870-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        tagged      forwarding 
  0/78       tagged      forwarding 
 
o 
On the 6860-B: 
sw8 (6860-B) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/3      tagged        blocking 
  0/78       tagged      forwarding 
 
sw8 (6860-B) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/3      tagged        blocking 
  0/78       tagged      forwarding 
 
sw8 (6860-B) -> show vlan members port 1/1/3 
  vlan      type        status 
--------+-----------+--------------- 
    20    tagged       blocking 
    30    tagged       blocking 
    58    untagged     forwarding 
 
If we take, for example, the port 1/1/3 on the 6860-B, we can see that it is carrying tagged information for 
VLANs 20 and 30 and bridging the VLAN 58. 
 
 
Reminder 
A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)

<<<PAGE 223>>>
6 
802.1q 
 
 3 
Testing the Configuration 
Let’s see what happens when we modify the Client VM IP addresses, move them to the VLAN  20 and VLAN 30, 
and ping them each other.  
 
 
- Let’s assign the port of each Client VM to the appropriate VLAN, and modify their IP addresses as 
described below:  
 
Client 5: 
sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged 
sw5 (6360-A) -> interfaces 1/1/1 admin-state enable 
sw5 (6360-A) -> show vlan members port 1/1/1 
  vlan      type        status 
--------+-----------+--------------- 
    20    untagged     forwarding 
 
Modify the IP information of client 5 to match the following: 
IP Address: 192.168.20.105 
Mask: 255.255.255.0 
Default Gateway: 192.168.20.7 (VLAN 20 IP Interfaces) 
 
Client 6: 
sw5 (6360-A) -> vlan 30 members port 2/1/1 untagged 
sw5 (6360-A) -> interfaces 2/1/1 admin-state enable 
sw5 (6360-A) -> show vlan members port 2/1/1 
  vlan      type        status 
--------+-----------+--------------- 
    30    untagged     forwarding 
 
Modify the IP information of client 6 to match the following: 
IP Address – 192.168.30.106 
Mask – 255.255.255.0 
Default Gateway – 192.168.30.8 (VLAN 30 IP Interfaces) 
 
- Check that the Client 5 (VLAN 20) can reach its gateway (ping 192.168.20.7) 
- Check that the Client 6 (VLAN 30) can reach its gateway (ping 192.168.30.8) 
 
- How are the Clients VM exchange between each other (Layer 2 or Layer 3)? 
------------------------------------------------------------------------------------------------------------------------------ 
------------------------------------------------------------------------------------------------------------------------------

<<<PAGE 224>>>
7 
802.1q 
 
- 
Are packets being bridged? Routed? Both?  
------------------------------------------------------------------------------------------------------------------------------ 
------------------------------------------------------------------------------------------------------------------------------ 
 
- Save the configuration and Copy running to certify all the switches managed 
 
sw7 (6870-A) -> write memory flash-synchro 
sw8 (6860-B) -> write memory flash-synchro 
sw5 (6360-A) -> write memory flash-synchro

<<<PAGE 225>>>
SPANNING TREE
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 226>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the implementation of Spanning 
Tree on AOS-based switches
- STP modes
- STP protocols
• Learn how to implement
- 1x1 and FLAT mode
- Spanning Tree Protocol 802.1D/802.1w

<<<PAGE 227>>>
STP REMINDER
• Goal
• Self-configuring algorithm that
maintains a loopfree topology
on a network
• Provides helps to provide data 
path redundancy and network 
scalability
• How it works 
• Supports two Spanning Tree operating modes:
• flat (single STP instance per switch)
• per-VLAN (single STP instance per VLAN)
(By default on OmniSwitch)
• Supports three Spanning Tree operating protocols:
• STP (802.1d): Convergence time :  50 secs
• RSTP (802.1w): Convergence time : < 1 sec
• MSTP (802.1s): < 1 sec 
1/1/3        VLAN 3 
1/1/3
X
X
1/1/2        VLAN 2         1/1/2
1/1/1        VLAN 1
1/1/1
flat
1/1/3        VLAN 3
1/1/3
1/1/2        VLAN 2        1/1/2
1/1/1        VLAN 1
1/1/1
Per-VLAN
SW-A (MAC@: aa)
SW-B (MAC@: bb)
SW-C (MAC@: cc)
PRIORITY: 32768
PRIORITY: 32768
PRIORITY: 32768
ROOT BRIDGE
1/1/1
1/1/2
1/1/1
1/1/1
1/1/2
1/1/5
SW-A (MAC@: aa)
SW-B (MAC@: bb)
SW-A (MAC@: aa)
SW-B (MAC@: bb)
BLK- ALT
F - RP
F - RP
DP
F - DP
F - DP
X
F -

<<<PAGE 228>>>
STP REMINDER
• Specification 
• IEEE 802.1d/w and 802.1s - Default Port Path Costs 
Link Speed
IEEE Recom.
Value – 16 bit
10 Mbps
100
100 Mbps
19
1 Gbps
4
10 Gbps
2
802.1d/w 16-bit Port Path Cost PPC
Link Speed
IEEE Recom.
Value – 32 bit
10 Mbps
2,000,000
100 Mbps
200,000
1 Gbps
20,000
10 Gbps
2,000
802.1s 32-bit Port Path Cost PPC

<<<PAGE 229>>>
STP REMINDER
per vlan (1x1) - load balancing
SW-A (MAC@: aa)
PRIORITY: 32768
MAC@ : E8:E7:32:56:45:C4
MAC@: E8:E7:32:D4:85:0D
PRIORITY: 32768
MAC@ : E8:E7:32:CD:63:D3
PRIORITY: 32768
ROOT BRIDGE
1/1/1
1/1/2
1/1/1
1/1/1
1/1/2
1/1/5
ALT- BLK
RP -FW
RP - FW
D- FW
D -FW
D -FW
X
SW-B (MAC@: cc)
SW-C (MAC@: bb)
VLAN 1, 20, 30
-> show spantree
Spanning Tree Path Cost Mode : AUTO
VLAN  STP Status   Protocol  Priority
-----+-------------+---------+--------------
1     ON         RSTP      32768 (0x8000)
20     ON         RSTP      32768 (0x8000)
30     ON         RSTP      32768 (0x8000)
-> show spantree
VLAN    STP   Protocol   Priority
-----+--------+---------+---------------
1    ON     RSTP      32768 (0x8000)
20    ON     RSTP      32768 (0x8000)
30    ON     RSTP      20000 (0x4e20)
SW-A (MAC@: aa)
1/1/1
1/1/2
1/1/1
1/1/1
1/1/2
1/1/5
ALT - BLK
DP FW
RP-FW
RP -FW
DP FW
DP FW
SW-B (MAC@: cc)
SW-C (MAC@: bb)
SW-A (MAC@: aa)
1/1/1
1/1/2
1/1/1
1/1/1
1/1/2
1/1/5
DP-FW
ALT -BLK
DP FW
DP-FW
RP -FW
RP-FW
SW-B (MAC@: cc)
SW-C (MAC@: bb)
MAC@: E8:E7:32:D4:85:0D
PRIORITY: 32768
MAC@ : E8:E7:32:CD:63:D3
PRIORITY: 20000
PRIORITY: 32768
MAC@ : E8:E7:32:56:45:C4
ROOT BRIDGE
VLAN 20
ROOT BRIDGE
MAC@: E8:E7:32:D4:85:0D
PRIORITY: 20000
MAC@ : E8:E7:32:CD:63:D3
PRIORITY: 32768
PRIORITY: 32768
MAC@ : E8:E7:32:56:45:C4
-> show spantree
VLAN    STP   Protocol   Priority
-----+--------+---------+--------------
1      ON    RSTP    32768 (0x8000)
20      ON    RSTP    20000 (0x4e20)
30      ON    RSTP    32768 (0x8000)
VLAN 30

<<<PAGE 230>>>
STP CONFIGURATION

<<<PAGE 231>>>
STP CONFIGURATION
STEP BY STEP
Bridge ID, Priority and Path Cost 
Mode selection
Protocol selection
Set the path cost mode

<<<PAGE 232>>>
Select Mode
Monitor
STP CONFIGURATION
STEP BY STEP
-> spantree mode {flat | per-vlan}
-> show spantree mode
Spanning Tree Global Parameters
Current Running Mode  : Per VLAN,
Current Protocol      : N/A (Per VLAN),
Path Cost Mode        : AUTO,
Auto VLAN Containment : N/A
Cisco PVST+ mode      : Disabled
VLAN Consistency check: Disabled
Mode selection

<<<PAGE 233>>>
STP CONFIGURATION
STEP BY STEP
-> spantree [cist | vlan vlan_id] protocol {stp | rstp | mstp} 
-> show spantree
Spanning Tree Path Cost Mode : AUTO
VLAN    STP Status
Protocol    Priority
-----+--------------- +--------+--------------
1      ON            RSTP      32768 (0x8000)
20      ON            RSTP      32768 (0x8000)
30      ON            RSTP      32768 (0x8000)
Protocol selection
Select protocol
Check the protocol selected

<<<PAGE 234>>>
STP CONFIGURATION
STEP BY STEP
spantree [cist | msti msti_id | vlan vlan_id] [port chassis/slot/port[-port2] 
| linkagg agg_id[-agg_id2]] priority priority
A bridge or port priority value. The valid range for the 
bridge priority is 0–65535.
The valid range for the port priority is 0–15. 
If MSTP is the active flat mode protocol, enter a value that 
is a multiple of 4096 (for example, 4096, 8192, 12288). 
spantree cist {port chassis/slot/port[-port2] | linkagg agg_id[-agg_id2]} 
path-cost path_cost
Path cost 0 -> 65535 for 16-bit
0 –> 200000000 for 32-bit - Default:0
Ex: ->spantree vlan 20 priority 20000
Ex: ->spantree vlan 200 port 2/1/1 priority 15 
Bridge ID, Priority and Path Cost 
Configure the bridge and port priority
Configure the path cost

<<<PAGE 235>>>
STP CONFIGURATION
STEP BY STEP
-> show spantree vlan 20 ports active
Spanning Tree Port Summary for VLAN 20
Oper
Path  Desig
Prim. Op  Op
Port   St    Cost  Cost
Role  Port  Cnx Edg
Desig Bridge ID         Note
------+----+------+------+----+-----+---+---+------------------------+----
1/1/3   BLK  4      3    ALT   1/1/3 PTP  NO  8000-e8:e7:32:cd:63:d3
1/1/4  FORW  4      0    ROOT  1/1/4 PTP  NO  4E20-e8:e7:32:d4:85:0d
-> show spantree ports [forwarding | blocking | active | configured]
Learning
Forwarding // Discarding
Disabled
Blocking
< 1 sec
Displays Spanning Tree port information
Displays Spanning Tree bridge information for a per-VLAN mode VLAN instance
-> show spantree vlan [vlan_id] 
-> show spantree ports
VLAN  Port   Oper Status  Path Cost  Role  Loop Guard Note
-----+-------+------------+---------+------+----------+------
1   1/1/1     FORW         4      DESG   DIS
1   1/1/2     DIS          0      DIS    DIS
Spanning Tree Port Status

<<<PAGE 236>>>
STP CONFIGURATION
STEP BY STEP
-> spantree path-cost-mode auto
-> spantree path-cost-mode 32bit
spantree path-cost-mode {auto | 32bit} 
16-bit when STP/RSTP protocol is active
32-bit when MSTP protocol is active
32-bit regardless of which protocol is active
Set the path cost mode

<<<PAGE 237>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 238>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Spanning Tree Protocol (STP) 
How to 
✓ Configure the Spanning Tree Protocol (STP) options on an OmniSwitch. 
Contents 
1 
Topology ........................................................................................ 2 
2 
Managing the Spanning Tree Protocol ...................................................... 2 
2.1. Changing the priority of the 6870-A ............................................................. 2 
2.2. Identifying the port status ........................................................................ 3 
2.3. Testing the redundancy ........................................................................... 6 
3 
Using the 1x1 Spanning Tree Mode ......................................................... 8 
3.1. Configuring the Priority ............................................................................ 9 
3.2. Verifying the Configuration ....................................................................... 9 
3.2.1. Verifying the VLAN 20 Configuration..................................................................... 9 
3.2.2. Verifying the VLAN 30 Configuration................................................................... 11

<<<PAGE 239>>>
2 
Spanning Tree Protocol (STP) 
 
 1 
Topology 
The Spanning Tree Protocol (STP) is an important concept to understand in a bridged network.  
 
 
 2 
Managing the Spanning Tree Protocol 
2.1. 
Changing the priority of the 6870-A 
 
- Customer wants to have the 6870-A as root bridge for vlan 20 and vlan 30  
To achieve this, change the priority of the 6870-A to ensure that: 
 
sw7 (6870-A) -> spantree vlan 20 priority 20000 
sw7 (6870-A) -> spantree vlan 30 priority 20000  
 
sw7 (6870-A) -> sh spantree 
  Spanning Tree Path Cost Mode : AUTO 
 Vlan STP Status Protocol Priority 
-----+----------+--------+-------------- 
    1      ON       RSTP   32768 (0x8000) 
   20      ON       RSTP   20000 (0x4e20) 
   30      ON       RSTP   20000 (0x4e20) 
   57      ON       RSTP   32768 (0x8000) 
  217      ON       RSTP   32768 (0x8000) 
  278      ON       RSTP   32768 (0x8000) 
 4094     OFF       RSTP   32768 (0x8000)

<<<PAGE 240>>>
3 
Spanning Tree Protocol (STP) 
 
2.2. 
Identifying the port status 
- Check the Spanning Tree Protocol Status for VLAN 20 on the 3 switches (6360, 6870-A and 6860-B): 
o 
On the 6360-A: 
sw5 (6360-A) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       32768 (0x8000), 
  Bridge ID            :   8000-94:24:e1:7c:82:1d, 
  Designated Root      :   4E20-2c:fa:a2:0e:62:3f, 
  Cost to Root Bridge  :                    3, 
  Root Port            :   Slot 0 Interface 7, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    6, 
  Topology age         :             02:56:49, 
  Last TC Rcvd Port    :                2/1/3, 
  Last TC Rcvd Bridge  :   4E20-e8:e7:32:d4:84:03, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
o 
On the 6870-A: 
sw7 (6870-A) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       20000 (0x4E20), 
  Bridge ID            :   4E20-2c:fa:a2:0e:62:3f, 
  Designated Root      :   4E20-2c:fa:a2:0e:62:3f, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    5, 
  Topology age         :             03:00:02, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8000-94:24:e1:7c:82:1d, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
o 
On the 6860-B: 
sw8 (6860-B) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       32768 (0x8000) 
  Bridge ID            :   8000-e8:e7:32:d4:84:03, 
  Designated Root      :   4E20-2c:fa:a2:0e:62:3f, 
  Cost to Root Bridge  :                    3, 
  Root Port            :  Slot 0 Interface 78, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    5, 
  Topology age         :             03:01:19, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   8000-2c:fa:a2:0e:62:3f, 
    Current Parameters (seconds) 
      Max Age              =    20,

<<<PAGE 241>>>
4 
Spanning Tree Protocol (STP) 
 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
This gives you the configured STP parameters of VLAN 20. Notice the mode (Per VLAN or 1X1), meaning 
each VLAN runs a separate STP instance.  
 
Additionally, take note of the Bridge ID and the Designated Root. If they are the same, your switch is the 
Root Bridge for VLAN 20.  
 
According to the information retrieved from the commands above:  
- The root bridge switch is the 6870-A.  
- The 6860-B is at a cost of 3 away the root bridge switch, we can deduce that the Root Bridge is the 
upstream neighbor on port 0 /78.(linkagg) 
 
 
- We can also deduce from the above output that our STP is relatively stable, it has been 03:01:19 hours 
since the last topology change (Topology Age) and we have only had 5 Topology changes. 
 
By default, the bridge priority is 32768 (0x8000). Since all priorities are identical by default, the switch 
with the lowest MAC address is selected as the root bridge (in this example, the 6870-A has the lowest 
MAC address). 
 
- One port should be in blocking mode to prevent a loop:  
sw5 (6360-A) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
         Oper  Path   Desig         Prim.   Op  Op  Loop 
Port      St   Cost    Cost   Role  Port    Cnx Edg Guard  Desig Bridge ID        Note 
--------+----+-------+-------+----+--------+---+---+------+----------------------+------ 
   1/1/1 FORW       4       3 DESG    1/1/1 PTP EDG  DIS   8000-94:24:e1:f0:f6:39 
   2/1/3  BLK       4       3  ALT    2/1/3 PTP  NO  DIS   8000-94:24:e1:e8:b4:13 
     0/7 FORW       3       0 ROOT    1/1/3 PTP  NO  DIS   4E20-e8:e7:32:d4:88:23 
 
 
sw7 (6870-A) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
         Oper  Path   Desig         Prim.   Op  Op  Loop 
Port      St   Cost    Cost   Role  Port    Cnx Edg Guard  Desig Bridge ID        Note 
--------+----+-------+-------+----+--------+---+---+------+----------------------+------ 
     0/7 FORW       3       0 DESG    1/1/3 PTP  NO  DIS   4E20-e8:e7:32:d4:88:23 
    0/78 FORW       3       0 DESG   1/1/23 PTP  NO  DIS   4E20-e8:e7:32:d4:88:23 
 
sw8 (6860-B) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
         Oper  Path   Desig         Prim.   Op  Op  Loop 
Port      St   Cost    Cost   Role  Port    Cnx Edg Guard  Desig Bridge ID        Note 
--------+----+-------+-------+----+--------+---+---+------+----------------------+------ 
   1/1/3 FORW       4       3 DESG    1/1/3 PTP  NO  DIS   8000-94:24:e1:e8:b4:13 
    0/78 FORW       3       0 ROOT   1/1/23 PTP  NO  DIS   4E20-e8:e7:32:d4:88:23

<<<PAGE 242>>>
5 
Spanning Tree Protocol (STP) 
 
 
sw5 (6360-A) -> show spantree ports blocking 
 Vlan  Port     Oper Status  Path Cost  Role   Loop Guard   Note 
-----+--------+-------------+---------+-------+----------+------ 
  20    2/1/3     BLK             4    ALT    DIS 
  30    2/1/3     BLK             4    ALT    DIS 
Also, notice that only one side of the link(s) has a port or link aggregation with the status BLK (blocking). 
This ensures the neighbor(s) are still able to initiate a topology change in the event of a failure. 
- Fill up the following diagrams: 
 
For VLAN 20 
 
  
 
For VLAN 30 
 
 
- What determines which side of the link is blocking? 
-----------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------

<<<PAGE 243>>>
6 
Spanning Tree Protocol (STP) 
 
2.3. 
Testing the redundancy 
 
 
 
- Put the client 8 is in the VLAN 20.  
sw8 (6860-B) -> vlan 20 members port 1/1/1 untagged 
 
 
Notes 
The Client 5 is already in the VLAN 20. If not, type: sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged 
 
- Activate the interface: 
sw8 (6860-B) -> interfaces 1/1/1 admin-state enable 
 
- Configure the network interface of the Client 8 with the following information: 
Client 8: 
IP address = 192.168.20.108 
Subnet mask = 255.255.255.0 
Default Gateway = 192.168.20.7  
 
- Start a continuous ping between client connected across an uplink (e.g between client 8 and client 5): 
Client 8: 
C:\> ping –t 192.168.20.105 
 
- Once your ping is successful, remove the connection between the 6360 virtual Chassis and the 6870-A: 
sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable 
 
- Relaunch the commands above, and notice how quickly Rapid STP recovers from a link failure:  
sw7 (6870-A) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       20000 (0x4E20), 
  Bridge ID            :   4E20-2c:fa:a2:0e:62:3f, 
  Designated Root      :   4E20-2c:fa:a2:0e:62:3f, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    8, 
  Topology age         :             00:00:08, 
  Last TC Rcvd Port    :  Slot 0 Interface 78, 
  Last TC Rcvd Bridge  :   8000-e8:e7:32:d4:84:03, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15,

<<<PAGE 244>>>
7 
Spanning Tree Protocol (STP) 
 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw5 (6360-A) -> show spantree ports blocking 
 Vlan  Port     Oper Status  Path Cost  Role   Loop Guard   Note 
-----+--------+-------------+---------+-------+----------+------ 
 
sw7 (6870-A) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
        Oper  Path   Desig        Prim.   Op  Op  Loop 
Port     St   Cost    Cost   Role Port    Cnx Edg Guard  Desig Bridge ID        Note 
-------+----+-------+-------+----+-------+---+---+------+----------------------+------ 
    0/7  DIS       0       0  DIS   1/1/1  NS  NO  DIS   0000-00:00:00:00:00:00 
   0/78 FORW       3       0 DESG  1/1/23 PTP  NO  DIS   4E20-2c:fa:a2:0e:62:3f 
 
sw8 (6860-B) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
        Oper  Path   Desig        Prim.   Op  Op  Loop 
Port     St   Cost    Cost   Role Port    Cnx Edg Guard  Desig Bridge ID        Note 
-------+----+-------+-------+----+-------+---+---+------+----------------------+------ 
  1/1/1 FORW       4       3 DESG   1/1/1 PTP EDG  DIS   8000-e8:e7:32:d4:84:03 
  1/1/3 FORW       4       3 DESG   1/1/3 PTP  NO  DIS   8000-e8:e7:32:d4:84:03 
   0/78 FORW       3       0 ROOT  1/1/23 PTP  NO  DIS   4E20-2c:fa:a2:0e:62:3f 
 
sw5 (6360-A) ->  show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
        Oper  Path   Desig        Prim.   Op  Op  Loop 
Port     St   Cost    Cost   Role Port    Cnx Edg Guard  Desig Bridge ID        Note 
-------+----+-------+-------+----+-------+---+---+------+----------------------+------ 
 1/1/1  DIS       0       0  DIS   1/1/1  NS  NO  DIS   0000-00:00:00:00:00:00  
 2/1/3 FORW       4       3 ROOT   2/1/3 PTP  NO  DIS   8000-e8:e7:32:d4:84:03 
   0/7  DIS       0       0  DIS   1/1/1  NS  NO  DIS   0000-00:00:00:00:00:00 
 
- Has our Topology age changed?  
----------------------------------------------------------------------------------------------------------------------------------- 
 
- Has the Root port changed?  
----------------------------------------------------------------------------------------------------------------------------------- 
 
 
 
Tips 
Remember that anytime there is a physical change, the STP will make the network infrastructure re-converge.

<<<PAGE 245>>>
8 
Spanning Tree Protocol (STP) 
 
- What will happen when we re-connected the disconnected port?  
 ------------------------------------------------------------------------------------------------------------------------------ 
 
sw5 (6360-A) -> show spantree ports blocking 
 Vlan  Port     Oper Status  Path Cost  Role   Loop Guard   Note 
-----+--------+-------------+---------+-------+----------+------ 
 
sw5 (6360-A) -> linkagg lacp agg 7 admin-state enable 
 
sw5 (6360-A) -> show spantree ports blocking 
 Vlan  Port     Oper Status  Path Cost  Role   Loop Guard   Note 
-----+--------+-------------+---------+-------+----------+------ 
   20    2/1/3     BLK             4    ALT    DIS 
   30      0/7     BLK             3    ALT    DIS 
 
 3 
Using the 1x1 Spanning Tree Mode 
By default, an OmniSwitch uses the 1x1 or Per VLAN Spanning Tree mode. That means there’s a separate 
instance of Spanning Tree for each VLAN. 
 
As the default parameters are the same for each VLAN (base MAC address, cost links, etc…), the status of 
each port is the same for each VLAN. To take advantage of the 1x1 mode and provide load-balancing, it may 
be necessary to modify bridge priority to have a predictable behavior. 
 
For example, this design would be interesting, considering that the blocked port for each VLAN is different: 
 
 
 
 
Here, the 6360 VC is the access switch and 6860 and 6870 are core switches. The 6360 VC has a dual 
attachment to the 6870 and 6860 to provide redundancy. The goal is to have one of the uplinks up for VLAN 
20 and the other one for VLAN 30.

<<<PAGE 246>>>
9 
Spanning Tree Protocol (STP) 
 
3.1. 
Configuring the Priority 
- To achieve this, change the priority of the 6870-A and 6860-B to ensure that: 
- The 6870-A is root bridge for VLAN 20. (Already done on part 2.1), restore default priority for VLAN 30 
sw7 (6870-A) -> spantree vlan 30 priority 32768 
 
- The 6860-B root bridge for VLAN 30. 
Sw8 (6860-B)-> spantree vlan 30 priority 20000  
3.2. 
Verifying the Configuration 
3.2.1. 
Verifying the VLAN 20 Configuration 
- Check the priority for the instance VLAN 20:  
o 
On the 6870-A: 
sw7 (6870-A) -> show spantree 
  Spanning Tree Path Cost Mode : AUTO 
 Vlan STP Status Protocol Priority 
-----+----------+--------+-------------- 
    1      ON       RSTP   32768 (0x8000) 
   20      ON       RSTP   20000 (0x4e20) 
   30      ON       RSTP   32768 (0x8000) 
   57      ON       RSTP   32768 (0x8000) 
  217      ON       RSTP   32768 (0x8000) 
  278      ON       RSTP   32768 (0x8000) 
 4094     OFF       RSTP   32768 (0x8000) 
 
sw7 (6870-A) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       20000 (0x4E20), 
  Bridge ID            :   4E20-2c:fa:a2:0e:62:3f, 
  Designated Root      :   4E20-2c:fa:a2:0e:62:3f, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                    9, 
  Topology age         :            00:14:48, 
  Last TC Rcvd Port    :   Slot 0 Interface 7, 
  Last TC Rcvd Bridge  :   8000-94:24:e1:7c:82:1d, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
                      ---- 
 
sw7 (6870-A) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
        Oper  Path   Desig        Prim.   Op  Op  Loop 
Port     St   Cost    Cost   Role Port    Cnx Edg Guard  Desig Bridge ID        Note 
-------+----+-------+-------+----+-------+---+---+------+----------------------+------ 
    0/7 FORW       3       0 DESG   1/1/4 PTP  NO  DIS   4E20-2c:fa:a2:0e:62:3f 
0/78 FORW       3       0 DESG  1/1/23 PTP  NO  DIS   4E20-2c:fa:a2:0e:62:3f

<<<PAGE 247>>>
10 
Spanning Tree Protocol (STP) 
 
o 
On the 6860-B:  
sw8 (6860-B) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       20000 (0x4E20), 
  Bridge ID            :   8000-e8:e7:32:d4:84:03, 
  Designated Root      :   4E20-94:24:e1:e8:b4:13, 
  Cost to Root Bridge  :                    0, 
  Root Port            :                 None, 
  TxHoldCount          :                    3, 
  Topology Changes     :                   10, 
  Topology age         :            00:04:57, 
  Last TC Rcvd Port    :                1/1/3, 
  Last TC Rcvd Bridge  :   4E20-94:24:e1:f0:f6:39, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw8 (6860-B) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
        Oper  Path   Desig        Prim.   Op  Op  Loop 
Port     St   Cost    Cost   Role Port    Cnx Edg Guard  Desig Bridge ID        Note 
-------+----+-------+-------+----+-------+---+---+------+----------------------+------ 
  1/1/1 FORW       4       3 DESG   1/1/1 PTP EDG  DIS   8000-e8:e7:32:d4:84:03 
  1/1/3  BLK       4       3  ALT   1/1/3 PTP  NO  DIS   8000-94:24:e1:7c:82:1d 
   0/78 FORW       3       0 ROOT  1/1/23 PTP  NO  DIS   4E20-2c:fa:a2:0e:62:3f 
o 
On the 6360:  
sw5 (6360-A) -> show spantree vlan 20 
Spanning Tree Parameters for Vlan 20 
  Spanning Tree Status :                   ON, 
  Protocol             :       IEEE Rapid STP, 
  mode                 : Per VLAN (1 STP per Vlan), 
  Priority             :       32768 (0x8000), 
  Bridge ID            :   8000-94:24:e1:f0:f6:39, 
  Designated Root      :   4E20-94:24:e1:e8:b4:13, 
  Cost to Root Bridge  :                    4, 
  Root Port            :                2/1/3, 
  TxHoldCount          :                    3, 
  Topology Changes     :                   16, 
  Topology age         :            00:04:04, 
  Last TC Rcvd Port    :                2/1/3, 
  Last TC Rcvd Bridge  :   4E20-94:24:e1:e8:b4:13, 
    Current Parameters (seconds) 
      Max Age              =    20, 
      Forward Delay        =    15, 
      Hello Time           =     2 
    Parameters system uses when attempting to become root 
      System Max Age       =    20, 
      System Forward Delay =    15, 
      System Hello Time    =     2 
 
sw5 (6360-A) -> show spantree vlan 20 ports 
Spanning Tree Port Summary for Vlan 20 
        Oper  Path   Desig        Prim.   Op  Op  Loop 
Port     St   Cost    Cost   Role Port    Cnx Edg Guard  Desig Bridge ID        Note 
-------+----+-------+-------+----+-------+---+---+------+----------------------+------ 
  1/1/1  DIS       0       0  DIS   1/1/1  NS  NO  DIS   0000-00:00:00:00:00:00     
  2/1/3 FORW       4       3 DESG   2/1/3 PTP  NO  DIS   8000-94:24:e1:7c:82:1d 
    0/7 FORW       3       0 ROOT   2/1/4 PTP  NO  DIS   4E20-2c:fa:a2:0e:62:3f

<<<PAGE 248>>>
11 
Spanning Tree Protocol (STP) 
 
3.2.2. 
Verifying the VLAN 30 Configuration 
o 
On the 6860-B: 
sw8 (6860-B) -> show spantree 
sw8 (6860-B) -> show spantree vlan 30 
sw8 (6860-B) -> show spantree vlan 30 ports 
 
 
o 
On the 6870-A: 
Sw7 (6870-A) -> show spantree 
sw7 (6870-A) -> show spantree vlan 30 
sw7 (6870-A) -> show spantree vlan 30 ports 
 
o 
On the 6360-A (VC): 
Sw5 (6360-A) -> show spantree 
Sw5 (6360-A) -> show spantree vlan 30 
Sw5 (6830-A) -> show spantree vlan 30 ports

<<<PAGE 249>>>
DUAL-HOME LINKS (DHL)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 250>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• List the Dual-Home Link (DHL) advantages
• Identify the Dual-Home Link (DHL) specification 
per switch model
• Summarize the Dual-Home Link (DHL) 
configuration step

<<<PAGE 251>>>
DUAL-HOME LINK REMINDER
• Goal
• High availability feature
• Provides fast failover between Core/Aggregation and 
Access switches without using STP
• How it works
• DHL Active-Active splits VLANs between two active 
links 
• The forwarding status of each VLAN is modified by 
DHL to prevent network loops and maintain 
connectivity to the core when one of the links 
•LinkB VLANs
•LinkA VLANs
•ACCESS LAYER
•AGGREGATION OR CORE LAYER
•DHL
•NORMAL STATE (BOTH LINKS UP)
•LinkA & LinkB VLANs
•LinkA VLANs
•ACCESS LAYER
•AGGREGATION OR CORE LAYER
•DHL
•FAILED STATE (ONE LINK DOWN)

<<<PAGE 252>>>
DUAL-HOME LINK SPECIFICATIONS
• Only one session per switch is allowed.
• Each session has only two links (linkA and linkB). 
• A physical port or a link aggregate (linkagg) ID 
could be a DHL link. 
• The same port or link aggregate is not 
configurable as both linkA or linkB. 
• DHL is not supported on mobile, 802.1x-enabled, 
GVRP, or UNI ports
• Refer to specification guide for the 
characteristics
•LinkB VLANs
•LinkA VLANs
•ACCESS LAYER
•AGGREGATION OR CORE LAYER
•DHL
•NORMAL STATE (BOTH LINKS UP)

<<<PAGE 253>>>
DHL TIMERS & MAC-FLUSHING
• Pre-Emption timer
• Amount of time to wait before a failed link that has 
recovered can resume servicing VLANs
• 0 to 600 seconds
• Mac Address Flushing
• Spanning Tree is automatically disabled on DHL ports
• Problem: No topology change after changeover of DHL 
links
• 3 options are available to avoid staling MAC address 
entries
•LinkB VLANs
•LinkA VLANs
•ACCESS LAYER
•AGGREGATION OR CORE LAYER
•DHL
•NORMAL STATE (BOTH LINKS UP)
• RAW Flooding
•
List of MAC addresses learned on non-DHL port for all VLAN assigned to DHL links
•
Send a broadcast frame with source MAC address from that list on redundant 
DHL links in case of   failure, or on the primary in case of recovery.
• MVRP Enhanced: 
•
Joins only VLAN that are maps on DHL link
•
When DHL link fails, the other link issues joins message with « new » flags set
•
When DHL link recovers, the link issues new joins to reestablish connectivity
• None (default): The staled MAC address entries are kept in the MAC table

<<<PAGE 254>>>
MAC ADDRESS FLUSHING
•VLAN 2
•VLAN 1
•DHL
SW1
SW2
SW3
1/1
1/1
•(VLAN 2)
•VLAN 2
•VLAN 1
SW1
SW2
SW3
•(VLAN 2)
1/3
1/2
1/1
1/1
1/3
1/2
SW 2
@MAC
Port
VLAN
1/3
2
SW 3
@MAC
Port
VLAN
1/1
2
•MVRP Join +
• « New » flag
MVRP ENHANCED
•VLAN 2
•VLAN 1
SW1
SW2
SW3
•(VLAN 2)
1/1
1/1
1/3
1/2
•Bdcst
•
@SRC: 
RAW FLOODING

<<<PAGE 255>>>
DUAL-HOME LINK REMINDER
Comparison between different solutions
Link redundancy
50% Bandwidth
Convergence time
Switch redundancy
Link redundancy
100% Bandwidth
Convergence time
Switch redundancy
STP
802.3Ad LACP
DHL Active-Active 
Link redundancy
100% Bandwidth
Convergence time
Switch redundancy

<<<PAGE 256>>>
DHL CONFIGURATION

<<<PAGE 257>>>
DHL CONFIGURATION
Step by Step
Create a DHL session
Map the Link A/B & Ports/Linkagg
Map the VLANs to the LinkB
Enable the DHL Session
Activate the “RAW” MAC-Flushing or MVRP Enhanced

<<<PAGE 258>>>
DHL CONFIGURATION
Step by Step
-> dhl
1
-> dhl 1 linka port 1/1/3 linkb port 1/1/4 
-> dhl 1 linka linkagg 1 linkb linkagg 2
Create a DHL session
Map the VLANs to the LinkB
Create the DHL Session 
Unique ID
Identify 2 ports/link aggregates
Map one to LinkA
Map the other one to LinkB
Example with port
Example with linkagg
SW1
1/1/2
Linkagg 1
LinkA
LinkB
-> dhl 1 linka linkagg 1 linkb port 1/1/2

<<<PAGE 259>>>
Map a set of VLANs to LinkB
The other VLANs will be automatically mapped to LinkA
Enable the DHL session (admin-state enable)
Activate the “RAW” MAC-Flushing or MVRP Enhanced
DHL CONFIGURATION
Step by Step
SW1
1/1/2
Linkagg 1
LinkB: 30
LinkA: all the other VLANs
-> dhl  1 vlan-map linkb 30
-> dhl
1 admin-state enable
-> dhl 1 mac-flushing raw
-> dhl 1 mac-flushing mvrp
Map the VLANs to the LinkB
Enable the DHL Session
Activate the “RAW” MAC-Flushing or MVRP Enhanced

<<<PAGE 260>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 261>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Dual Home Link Active-Active 
How to 
✓ Setup the high availability Dual-Home Link Active-Active feature. 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configuring the Prerequisites ............................................................... 3 
2.1. Prerequisite ......................................................................................... 3 
2.2. Assigning VLANs on the Link Aggregations ...................................................... 4 
2.2.1. Change default VLAN on the link aggregation: ......................................................... 4 
2.2.2. Tag the VLAN 20 and 30 on the link aggregation ....................................................... 4 
2.2.3. Tag the VLAN 57 on the link aggregation 78 ............................................................ 4 
3 
Configuring the DHL Active-Active link .................................................... 5 
3.1. DHL session Creation ............................................................................... 5 
4 
DHL Active-Active Monitoring ............................................................... 5

<<<PAGE 262>>>
2 
Dual Home Link Active-Active 
 
 1 
Topology 
The customer wants to configure the dual home link solution instead of the STP. 
Dual-Home Link (DHL) provides fast failover between core and edge switches without implementing Spanning 
Tree. 
A DHL Active-Active configuration consists of the following components: 
- A DHL session. Only one session per switch is allowed. 
- Two DHL links associated with the session (link A and link B). 
- A physical switch port or a logical link aggregation (linkagg) ID are configurable as a DHL link. 
- A group of VLANs (or pool of common VLANs) in which each VLAN is associated (802.1q tagged) with both 
link A and link B. 
- A VLAN-to-link mapping that specifies which of the VLANs each DHL link will service.  
This mapping prevents network loops by designating only one active link for each VLAN, even though both 
links remain active and are associated with each of the common VLANs. 
 
When one of the 2 active DHL links fails or is brought down, the VLANs mapped to that link are then 
forwarded on the remaining active link to maintain connectivity to the core. When the failed link comes back 
up, DHL waits a configurable amount of time before the link resumes forwarding of its assigned VLAN traffic. 
DHL linkA and linkB must belong to the same default VLAN.

<<<PAGE 263>>>
3 
Dual Home Link Active-Active 
 
 2 
Configuring the Prerequisites 
2.1. 
Prerequisite 
Creating a linkagg from 6360 VC to 6860-B 
On 6360 add port 1/1/1 in VLAN 20 
sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged 
 
For the lab, create a link aggregation between the 6360 VC and the 6860-B:  
On 6360 VC 
sw5 (6360-A) -> linkagg lacp agg 8 size 2 actor admin-key 8 
 
sw5 (6360-A) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
   7     Dynamic      40000007   2   ENABLED      UP              2   2 
   8     Dynamic      40000008   2   ENABLED      DOWN            0   0 
 
sw5 (6360-A) -> linkagg lacp port 2/1/3 actor admin-key 8 
ERROR: Port cannot be added to Linkagg, please remove other configuration on this port 
 
Untag the vlan on this port to be able to add it to the linkagg 
sw5 (6360-A) -> show vlan members port 2/1/3 
  vlan      type        status 
--------+-----------+--------------- 
    20    tagged     forwarding 
    30    tagged     forwarding 
    58    untagged    forwarding 
 
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
 
6860-B 
sw8 (6860-B) -> show vlan members port 1/1/3 
  vlan      type        status 
--------+-----------+--------------- 
    20    tagged     forwarding 
    30    tagged     forwarding 
    58    untagged    forwarding 
 
sw8 (6860-B) -> no vlan 58 members port 1/1/3 
 
sw8 (6860-B) -> no vlan 20 members port 1/1/3 
 
sw8 (6860-B) -> no vlan 30 members port 1/1/3 
 
sw8 (6860-B) -> no vlan 58 
 
sw8 (6860-B) -> linkagg lacp agg 8 size 2 actor admin-key 8 
 
sw8 (6860-B) -> linkagg lacp port 1/1/3-4 actor admin-key 8 
 
sw8 (6860-B) -> interfaces 1/1/3-4 admin-state enable 
 
sw8 (6860-B) -> show linkagg 
 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
   8     Dynamic      40000008   2   ENABLED      UP              2   2 
  28     Dynamic      40000028   2   ENABLED      UP              1   1 
  78     Dynamic      40000078   2   ENABLED      UP              2   2

<<<PAGE 264>>>
4 
Dual Home Link Active-Active 
 
2.2. 
Assigning VLANs on the Link Aggregations 
2.2.1. 
Change default VLAN on the link aggregation: 
 
Notes 
client does not want to use the VLAN 1 for security reason. 
 
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
2.2.2. 
Tag the VLAN 20 and 30 on the link aggregation  
sw5 (6360-A) -> vlan 20 members linkagg 8 tagged 
sw5 (6360-A) -> vlan 30 members linkagg 8 tagged 
 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  0/7        tagged      forwarding 
  0/8        tagged      forwarding 
 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        tagged      forwarding 
  0/8        tagged      forwarding 
 
sw8 (6860-B) -> vlan 20 members linkagg 8 tagged 
sw8 (6860-B) -> vlan 30 members linkagg 8 tagged 
sw8 (6860-B) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  0/8        tagged       forwarding 
  0/78       tagged       forwarding 
 
sw8 (6860-B) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        tagged       forwarding 
  0/78       tagged       forwarding 
2.2.3. 
Tag the VLAN 57 on the link aggregation 78  
sw8 (6860-B) -> vlan 57 members linkagg 78 tagged 
 
sw8 (6860-B) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/8        untagged     forwarding 
  0/78       tagged      forwarding 
 
sw7 (6870-A) -> vlan 57 members linkagg 78 tagged 
 
sw7 (6870-A) -> show vlan 57 members 
   port      type        status 
----------+-----------+--------------- 
  0/7        untagged     blocking 
  0/78       tagged      forwarding

<<<PAGE 265>>>
5 
Dual Home Link Active-Active 
 
 3 
Configuring the DHL Active-Active link 
3.1. 
DHL session Creation 
Configure a DHL session with the identifier 1 on the 6360-A (VC): 
sw5 (6360-A) -> dhl 1 
 
Configure 2 links (link-A and link-B) for the DHL session: 
sw5 (6360-A) -> dhl 1 linka linkagg 7 linkb linkagg 8 
 
 
Notes 
Spanning Tree is disabled on all the DHL enabled ports 
 
Map VLANs to link-B: 
sw5 (6360-A) -> dhl 1 vlan-map linkb 30 
 
Enable the DHL session: 
sw5 (6360-A) -> dhl 1 admin-state enable 
 4 
DHL Active-Active Monitoring 
Display the global status of the DHL configuration: 
sw5 (6360-A) -> show dhl 
Legends:  PE - Pre-Emption 
 Session            Session                  Admin   Oper     PE      MAC        Active MAC 
   ID                 Name                   State   State   Time   Flushing     Flushing 
                                                             (sec)  Technique    Technique 
----------+---------------------------------+-------+------+-------+----------+-------------- 
         1                           DHL-1     up     up     30      none         none 
 
Total number of sessions configured = 1 
 
Displays information about specific DHL session 1: 
sw5 (6360-A) -> show dhl 1 
DHL session name        : DHL-1 
  Admin state             : up, 
  Operational state       : up, 
  Pre-emption time(sec)   : 30, 
  Mac Flushing            : none, 
  Active MAC flushing     : none, 
  LinkB Vlan Map          : 30, 
  Protected Vlans         : 20 30 57 
    LinkA: 
      Port                  : 0/7, 
      Operational State     : up, 
      Unprotected Vlans     : none, 
      Active  Vlans         : 20 57 
    LinkB: 
      Port                  : 0/8, 
      Operational State     : up, 
      Unprotected Vlans     : none, 
      Active  Vlans         : 30 
 
Displays information about a specific DHL link: 
sw5 (6360-A) -> show dhl 1 linka 
LinkA: 
  Port                 : 0/7, 
  Operational State    : up, 
  Protected Vlans      : 20 30 57, 
  Unprotected Vlans    : none, 
  Active Vlans         : 20 57 
 
sw5 (6360-A) -> show dhl 1 linkb 
LinkB: 
  Port                 : 0/8, 
  Operational State    : up, 
  Protected Vlans      : 20 30 57, 
  Unprotected Vlans    : none, 
  Active  Vlans         : 30

<<<PAGE 266>>>
6 
Dual Home Link Active-Active 
 
Display information about protected VLANs: 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  0/7        tagged      forwarding 
  0/8        tagged     dhl-blocking 
 
sw5 (6360-A) -> show vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  2/1/1      untagged    forwarding 
  0/7        tagged     dhl-blocking 
  0/8        tagged      forwarding 
 
Check the Client 5 configuration with the following parameters: 
Client 5: 
 
IP address = 192.168.20.105 
Subnet mask = 255.255.255.0 
Default Gateway = 192.168.20.7 
 
Activate the “RAW” MAC-Flushing method:  
sw5 (6360-A) -> dhl 1 mac-flushing raw 
 
From Client 5, start a continuous ping to the VLAN 20 IP interface (created on the 6870-A): 
C:\> ping –t 192.168.20.7 
 
The VLAN 20 is blocked on the link aggregation to avoid a loop. Thus, the traffic goes from 6360-A to 6870-A 
via the link aggregation 7:  
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  0/7        tagged      forwarding 
  0/8        tagged     dhl-blocking 
 
Now disable the link aggregation 7 on the 6360-A while the ping is still running: 
sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable 
 
Did you notice any packet loss? --------------------------------------------------------------------------------------- 
 
Check VLAN 20 members:  
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  0/7        tagged        inactive 
  0/8        tagged      forwarding 
 
Stop the ping and enable the link aggregation 7 on the 6360-A: 
sw5 (6360-A) -> linkagg lacp agg 7 admin-state enable 
 
Check VLAN 20 members: 
sw5 (6360-A) -> show vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  0/7        tagged      forwarding 
  0/8        tagged     dhl-blocking 
 
 
Notes 
It can takes a few seconds for the VLAN 20 to be forwarded back on the link aggregation 8: when the failed link 
comes back up, DHL waits a configurable amount of time (default: 30 secs) before the link resumes forwarding 
of its assigned VLAN traffic. 
 
Save configuration: 
sw5 (6360-A) -> write memory flash-synchro 
sw8 (6860-B) -> write memory flash-synchro

<<<PAGE 267>>>
IP INTERFACES
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 268>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand and implement the following 
features
- IP interfaces
- DHCP Client
- DHCP Relay
- Loopback0 Interface
- Static routes

<<<PAGE 269>>>
IP INTERFACE

<<<PAGE 270>>>
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

<<<PAGE 271>>>
DHCP CLIENT IP INTERFACE

<<<PAGE 272>>>
IP INTERFACE
• Goal
• The OmniSwitch can be configured with a DHCP Client interface that allows the switch to obtain an 
IP address dynamically from a DHCP server
• The DHCP Client interface is configurable on any one VLAN in any VRF instance. 
• The DHCP Client interface supports the release and renew functionality according to RFC-2131. 
• The Option-60 string can be configured on the OmniSwitch and sent as part of the DHCP discover/request 
packet.
-> ip interface dhcp-client [vlan vid] [release | renew] [option-60 string]
-> show ip interface
Total 4 interfaces
Name
IP Address
Subnet Mask
Status Forward
Device
-------------------+---------------+----------------+------+-------+--------
Loopback
127.0.0.1
255.0.0.0
UP
NO
Loopback
Loopback0
1.1.1.1
255.255.255.255
UP
YES
Loopback0
dhcp-client
0.0.0.0
0.0.0.0
UP
YES
vlan 12
vlan1000
172.25.167.212
255.255.255.224
DOWN
NO
vlan 1000

<<<PAGE 273>>>
DHCP CLIENT IP INTERFACE
• When the switch receives a valid IP address 
lease from a DHCP server:
• The IP address and the subnet mask (DHCP Option-1) 
are assigned to the DHCP Client IP interface
• A default static route is created according to DHCP 
Option-3 (Router IP Address)
• The lease is periodically renewed and rebound 
according to the renew time (DHCP Option-58) and 
rebind time (DHCP Option-59) returned by the DHCP 
server
• If the lease cannot be renewed within the lease 
time (DHCP Option-51) returned by the DHCP server, 
the IP address is released 
• The DHCP Client-enabled IP address serves as the 
primary IP address when multiple addresses are 
configured for a VLAN.
-> show ip interface dhcp-client
Interface Name = dhcp-client
SNMP Interface Index
=
13600001,
IP Address
=
172.16.12.11,
Subnet Mask
=
255.255.255.0,
Broadcast Address
=
172.16.12.255,
Device
=
vlan 12,
Encapsulation
=
eth2,
Forwarding
=
enabled,
Administrative State
=
enabled,
Operational State
=
up,
Router MAC
=
00:e0:b1:80:00:f0,
Local Proxy ARP
=
disabled,
Maximum Transfer Unit
=
1500,
Primary (config/actual)
=
yes/yes
DHCP-CLIENT Parameter Details
Client Status
=
Active,
Server IP
=
172.16.12.102,
Router Address
=
172.16.12.1,
Lease Time Remaining
=
0 days 5 hour 58 min 14 sec,
Option-60
=
OmniSwitch-OS6860,
HostName
=
vxTarget
-> ip interface dhcp-client vlan 12
-> show ip routes
+ = Equal cost multipath routes
* = BFD Enabled static route
Total 15 routes
Dest Address
Subnet Mask
Gateway Addr
Age
Protocol
------------------+-----------------+----------------+----------+-----------
0.0.0.0
0.0.0.0
172.16.12.1
00:00:10
NETMGMT
2.2.2.2
255.255.255.255
2.2.2.2
03:54:09
LOCAL
127.0.0.1
255.255.255.255
127.0.0.1
03:55:13
LOCAL
172.16.12.0
255.255.255.0
172.16.12.11
00:00:10
LOCAL

<<<PAGE 274>>>
DHCP RELAY

<<<PAGE 275>>>
DHCP RELAY
• Two types of DHCP relay agents: global and per-interface.
• A global relay agent forwards DHCP packets
to a global destination IP address
• A per-interface relay agent is configured on
a specific IP interface that is bound to a VLAN.
• Only DHCP packets originating from the VLAN
that is associated with the interface are forwarded
to a destination IP address defined for the interface relay agent.
• They are mutually exclusive
DHCP
CLIENT
DHCP
CLIENT
DHCP
CLIENT
DHCP
SERVER
LAN
LAN
ROUTER
DHCP RELAY
AGENT
LAN SWITCH
LAN SWITCH

<<<PAGE 276>>>
DHCP RELAY
• By default, the DHCP Relay feature is disabled. 
• When the DHCP Relay feature is enabled, DHCP
packets are relayed on a global basis or on a per-interface basis.
• Global basis configuration
• Configuring the Global Relay Agent
• Removing  the Global Relay Agent
ip dhcp relay admin-state {enable | disable
ip dhcp relay destination 192.168.100.102
sw8 (6860-B) -> show ip dhcp relay statistics
Global Statistics :
Reception From Client :
Total Count =          0, Delta =          0
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
Total Count =          0, Delta =      0
InvAgentInfoFromServer:
Total Count =          0, Delta =      0
sw8 (6860-B) -> show ip dhcp relay
IP DHCP Relay :
DHCP Relay Admin Status
= Enable,
Forward Delay(seconds)         = 0,
Max number of hops
= 16,
Relay Agent Information        = Disabled,
Relay Agent Information Policy = Drop,
DHCP Relay Opt82 Format  =  Base MAC,
DHCP Relay Opt82 String  =  e8:e7:32:b3:3c:f9,
PXE support                    = Disabled,
Relay Mode                     = Global,
Bootup Option                  = Disable,
ip dhcp relay destination 
ip_address
no ip dhcp relay destination ip_address

<<<PAGE 277>>>
DHCP RELAY
• Configuring a Relay Agent for an IP Interface
• To enable/disable the DHCP Relay per-interface mode
• To Configure the DHCP relay destination address for 
the specified IP interface
-> ip dhcp relay per-interface-mode
-> no ip dhcp relay per-interface-mode
-> ip dhcp relay interface if_name destination ip_address
sw8 (6860-B) -> show ip dhcp
relay statistics
Global Statistics :
Reception From Client :
Total Count =          0, Delta =          0
Forw Delay Violation :
Total Count =          0, Delta =          0
Max Hops Violation :
Total Count =          0, Delta =          0
Agent Info Violation :
Total Count =          0, Delta =          0
Invalid Gateway IP :
Total Count =          0, Delta =          0
Server Specific Statistics :
From Interface int_20 to Server 192.168.100.102
Tx Server :
Total Count =          0, Delta =      0
InvAgentInfoFromServer:
Total Count =          0, Delta =      0
sw8 (6860-B) -> show ip dhcp relay
IP DHCP Relay :
DHCP Relay Admin Status
= Enable,
Forward Delay(seconds)         = 0,
Max number of hops
= 16,
Relay Agent Information        = Disabled,
Relay Agent Information Policy = Drop,
DHCP Relay Opt82 Format  =  Base MAC,
DHCP Relay Opt82 String  =  e8:e7:32:b3:3c:f9,
PXE support                    = Disabled,
Relay Mode                     = Per Interface,
Bootup Option                  = Disable,
ip dhcp relay interface int_20 destination 192.168.100.102

<<<PAGE 278>>>
UDP RELAY

<<<PAGE 279>>>
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

<<<PAGE 280>>>
GENERIC UDP PORT RELAY
• To display the generic UDP relay service configuration
• To display the current statistics for each UDP port relay service. 
-> show ip udp relay [service {tftp | tacacs | ntp | nbns | nbdd | dns} | port port_num]
-> show ip udp relay statistics [service {tftp | tacacs | ntp | nbns | nbdd | dns}] [port [port_num]]
-> show ip udp relay
Service Name         Port   IP Address       Vlans
Services
---------------------+------+----------------+---------+-----------
DNS port                53                      20
TFTP port               69
-> show ip udp relay statistics
Port   Service        Pkts Recvd
Pkts Sent   Dst Vlan/IP Address    Svc
-----+--------------+---------------+-----------+---------------------+--------
53 DNS port              0          0             20
69 TFTP port             0

<<<PAGE 281>>>
LOOPBACK0

<<<PAGE 282>>>
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

<<<PAGE 283>>>
CUSTOM IP INTERFACE/LOOPBACK0 FOR IP SERVICE
• To configure a source IP address as the outgoing IP interface for an IP service
• Any IP interface/ loopback
• In the particular VRF based on an application specific command
[vrf vrf_name] ip service source-ip {Loopback0 | interface_name} [tftp] [telnet] [tacacs] [swlog] [ssh] 
[snmp] [sflow] [radius] [ntp] [ldap] [ftp] [dns] [all]
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

<<<PAGE 284>>>
STATIC ROUTING

<<<PAGE 285>>>
OVERVIEW
• Gateway or NextHop address is mapped to a particular interface on the switch
• Associated interface needs to be up and running 
• By default, static routes have preference over dynamic routes
• Priority can be set by assigning a metric value
-> ip static-route <Destination Network>/<Mask> gateway <host> [METRIC | BFD-STATE | NAME | TAG | NO]

<<<PAGE 286>>>
CONFIGURATION
• Specify a static route to the destination IP address 134.1.21.0
• Specify a default route
• Configure a default-route metric
• Configure a backup default-route
-> ip static-route 134.1.21.0/24 gateway 10.1.1.1
-> ip static-route 0.0.0.0/0 gateway 10.1.1.1
-> ip static-route 0.0.0.0/0 gateway 1.1.1.1 metric 1
-> ip static-route 0.0.0.0/0 gateway 2.2.2.2 metric 2

<<<PAGE 287>>>
MONITORING
• Display the IP Router Database
• Display the IP Routes
-> show ip router database 
Legend: + indicates routes in-use
b indicates BFD-enabled static route
i indicates INTERFACE static route
r indicates recursive static route, with following address in brackets
Total IPRM IPv4 routes: 3
Destination         Gateway                   INTERFACE              Protocol  Metric     Tag      Misc-Info
---------------------+---------------+--------------------------------+--------+-------+----------+------------
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

<<<PAGE 288>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 289>>>
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

<<<PAGE 290>>>
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

<<<PAGE 291>>>
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

<<<PAGE 292>>>
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

<<<PAGE 293>>>
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

<<<PAGE 294>>>
V I RT U A L R O U T E R  R E D U N D A N C Y P R O TO C O L  ( V R R P )
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 295>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the VRRP feature on AOS switch
• List the management step to implement it

<<<PAGE 296>>>
VRRP REMINDER

<<<PAGE 297>>>
VRRP REMINDER
• Goal
• Business continuity solution for default gateway 
redundancy
• Protocol for electing a switch as the master virtual 
router
• Dynamic fail over in the forwarding responsibility
if the Master becomes unavailable
• RFCs Supported
• RFC 2338 – Virtual Router Redundancy Protocol
• RFC 2787 – Definitions of Managed Objects for
the Virtual
Subnet
Virtual Router IP 
Default gateway = Virtual Router IP
Master
Backup
Multicast - 224.0.0.18
Virtual MAC address:  00-00-5E-00-01-{VRID}

<<<PAGE 298>>>
VRRP REMINDER
Load balancing Outgoing Traffic
Def GW =
VR 1 IP address
Virtual Router ID = 2
Virtual Router ID = 1
Def GW =
VR 2 IP address 
Subnet
Backup 1
Master 2
Master 1
Backup 2
* Two virtual routers with their hosts splitting traffic between them

<<<PAGE 299>>>
VRRP REMINDER
• VRRP Tracking
• Base set of tracking policies supported:
• ADDRESS
• IPV4-INTERFACE                                  
• IPV6-INTERFACE 
• PORT 
• VLAN
Default Route
New route if port 1/1/3 goes down 
1/1/3
1/1/1
Master 1 Pri = 100
Virtual Router ID = 1
VLAN 20 (int_20)
Backup 1 Pri = 80
R2
R1
Backup 1 Pri = 70
Master 1 Pri = 80
1
2
3
4
5

<<<PAGE 300>>>
VRRP CONFIGURATION STEPS

<<<PAGE 301>>>
VRRP – BASIC CONFIGURATION STEP
Step by step
ip vrrp 1 interface int_20 
* At least two virtual routers must be configured on the LAN—a master router and a backup router.
ip vrrp 1 interface int_20 address 192.168.20.254
ip vrrp 1 interface int_20 admin-state enable
show ip vrrp
show ip vrrp 1 
show ip vrrp statistics
Creates a VRRP virtual router for IP addresses
Specifying an IP Address for a Virtual Router
Enabling a Virtual Router
Monitor the result

<<<PAGE 302>>>
VRRP – FULL CONFIGURATION STEP
Step by step
-
Role of each router 
-
Selection of backup routers
-
Allow by default 
-
may be disabled “no pre-empt” 
-
In VRRP version 2 virtual routers (same VRID) may 
configured to use the same interval value
ip vrrp 1 interface int_20 address 192.168.20.254
ip vrrp 1 interface int_20 admin-state enable
ip vrrp 1 interface int_20 priority 100 preempt interval 100
Creates a VRRP virtual router for IP addresses
Specifying an IP Address for a Virtual Router
Configuring the Advertisement Interval
Configuring Virtual Router Priority
Setting Pre-emption
Enabling a Virtual Router

<<<PAGE 303>>>
VRRP – CREATING VRRP TRACKING POLICIES
VRRP Tracking Policies
-> ip vrrp track 3 admin-state enable priority 30 port 1/1/3
-> ip vrrp 1 interface int_20 track-association 3
-> ip vrrp track 4 admin-state enable priority 50 address 20.1.1.3
-> ip vrrp 6 interface ipv4-100 track-association 4
1/1/3
1/1/1
Master 1 Pri = 100
Virtual Router ID = 1
VLAN 20 (int_20)
Backup 1 Pri = 80
R2
R1
Backup 1 Pri = 70
Master 1 Pri = 80
1
2
3
3
4
Create tracking Policy ID (3)
Enabled for a port or IP  address, 
or Vlan, or address
Associated a Tracking Policy with 
VRRP a Virtual Router

<<<PAGE 304>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 305>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Virtual Router Redundancy Protocol (VRRP) 
How to 
✓ Configure the VRRP protocol in Release 8 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configuring the VRRP ......................................................................... 3 
3 
Configuring the Master / Backup ............................................................ 8

<<<PAGE 306>>>
2 
Virtual Router Redundancy Protocol (VRRP) 
 
 1 
Topology 
The Virtual Router Redundancy Protocol is a standard router redundancy protocol which provides redundancy by 
eliminating the single point of failure inherent in a default route environment. The VRRP router, which controls 
the IP address associated with a virtual router is called the master router and is responsible for forwarding 
virtual router advertisements. If the master router becomes unavailable, the highest priority backup router 
transitions to the master state.

<<<PAGE 307>>>
3 
Virtual Router Redundancy Protocol (VRRP) 
 
 2 
Configuring the VRRP  
- Check Vlan ports member for vlan 20 and vlan 30 : 
sw5 (6360-A) -> sh vlan 20 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      untagged     forwarding 
  2/1/1      untagged     forwarding 
  0/7        tagged       forwarding 
  0/8        tagged      dhl-blocking 
 
sw5 (6360-A) -> sh vlan 30 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/2      untagged     forwarding 
  2/1/2      untagged     forwarding 
  0/7        tagged      dhl-blocking 
  0/8        tagged       forwarding 
-  Note :  If it is not correct, manage them as following : 
 
Ex : sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged 
… 
 
o 
On 6870-A 
sw7 (6870-A) -> show ip interface 
Total 7 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.7      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
Loopback0                        192.168.254.7   255.255.255.255     UP     YES Loopback0 
--- 
int_20                           192.168.20.7    255.255.255.0       UP     YES vlan 20 
int_217                          172.16.17.7     255.255.255.0       UP     YES vlan 217 
int_278                          197.16.78.7     255.255.255.0       UP     YES vlan 278 
--- 
 
sw7 (6870-A) -> ip interface int_30 address 192.168.30.7/24 vlan 30 
 
sw7 (6870-A) ->  show ip interface 
Total 10 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.7      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
--- 
int_20                           192.168.20.7    255.255.255.0       UP     YES vlan 20 
int_217                          172.16.17.7     255.255.255.0       UP     YES vlan 217 
int_278                          172.16.78.7     255.255.255.0       UP     YES vlan 278 
int_30                           192.168.30.7    255.255.255.0       UP     YES vlan 30 
--- 
 
sw7 (6870-A) -> ip vrrp 1 interface int_20 
sw7 (6870-A) -> ip vrrp 1 interface int_20 address 192.168.20.254 
sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state enable 
Thu Nov 14 16:53:50 : vrrp_0 proto INFO message: 
+++ Virtual router enabled IPv4 VRID=1 
 
sw7 (6870-A) -> ip vrrp 2 interface int_30 
sw7 (6870-A) -> ip vrrp 2 interface int_30 address 192.168.30.254 
sw7 (6870-A) -> ip vrrp 2 interface int_30 admin-state enable

<<<PAGE 308>>>
4 
Virtual Router Redundancy Protocol (VRRP) 
 
Thu Nov 14 16:56:45 : vrrp_0 proto INFO message: 
+++ Virtual router enabled IPv4 VRID=2 
 
 
o 
On 6860-B 
 
sw8 (6860-B) -> show ip interface 
Total 6 interfaces 
 Flags (D=Directly-bound) 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.8      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
Loopback0                        192.168.254.8   255.255.255.255     UP     YES Loopback0 
-- 
int_218                          172.16.18.8     255.255.255.0       UP     YES vlan 218 
int_278                          172.16.78.8     255.255.255.0       UP     YES vlan 278 
int_30                           192.168.30.8    255.255.255.0       UP     YES vlan 30 
 
sw8 (6860-B) -> ip interface int_20 address 192.168.20.8/24 vlan 20 
 
sw8 (6860-B) -> show ip interface 
Total 9 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CHAS1                        10.4.21.8      255.255.255.0       UP       NO EMP 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
Loopback0                        192.168.254.8   255.255.255.255     UP     YES Loopback0 
--- 
int_20                           192.168.20.8    255.255.255.0       UP     YES vlan 20 
int_218                          172.16.18.8     255.255.255.0       UP     YES vlan 218 
int_278                          172.16.78.8     255.255.255.0       UP     YES vlan 278 
int_30                           192.168.30.8    255.255.255.0       UP     YES vlan 30 
--- 
 
sw8 (6860-B) -> ip vrrp 1 interface int_20 
sw8 (6860-B) -> ip vrrp 1 interface int_20 address 192.168.20.254 
sw8 (6860-B) -> ip vrrp 1 interface int_20 admin-state enable 
 
Thu Nov 14 17:00:12 : vrrp_0 proto INFO message: 
+++ Virtual router enabled IPv4 VRID=1 
 
sw8 (6860-B) -> ip vrrp 2 interface int_30 
sw8 (6860-B) -> ip vrrp 2 interface int_30 address 192.168.30.254 
sw8 (6860-B) -> ip vrrp 2 interface int_30 admin-state enable 
 
Thu Nov 14 17:01:54 : vrrp_0 proto INFO message: 
+++ Virtual router enabled IPv4 VRID=2

<<<PAGE 309>>>
5 
Virtual Router Redundancy Protocol (VRRP) 
 
- Check the VRRP status: 
sw7 (6870-A) -> show ip vrrp 1 
Virtual Router VRID = 1 on INTERFACE = int_20 
  Version       = V2 
  Admin. Status = Enabled 
  Priority      = 100 
  Preempt       = Yes 
  Adv. Interval = 100 
  Virtual MAC   = 00-00-5E-00-01-01 
  IP Address(es) 
 
sw7 (6870-A) -> show ip vrrp 2 
Virtual Router VRID = 2 on INTERFACE = int_30 
  Version       = V2 
  Admin. Status = Enabled 
  Priority      = 100 
  Preempt       = Yes 
  Adv. Interval = 100 
  Virtual MAC   = 00-00-5E-00-01-02 
  IP Address(es) 
    192.168.30.254 
 
sw8 (6860-B) -> show ip vrrp 1 
Virtual Router VRID = 1 on INTERFACE = int_20 
  Version       = V2 
  Admin. Status = Enabled 
  Priority      = 100 
  Preempt       = Yes 
  Adv. Interval = 100 
  Virtual MAC   = 00-00-5E-00-01-01 
  IP Address(es) 
    192.168.20.254 
 
sw8 (6860-B) -> show ip vrrp 2 
Virtual Router VRID = 2 on INTERFACE = int_30 
  Version       = V2 
  Admin. Status = Enabled 
  Priority      = 100 
  Preempt       = Yes 
  Adv. Interval = 100 
  Virtual MAC   = 00-00-5E-00-01-02 
  IP Address(es) 
    192.168.30.254 
 
- In the steps above, we have created 2 VRRP instances 1 and 2 (VRRP 1, VRRP 2), and associated it with 
respectively VLAN 20 and 30 (VRRP 1 > VLAN 20, VRRP 2 > VLAN 30). We have then associated a Virtual IP 
address of 192.168.20.254 to VRRP 1 and 192.168.30.254 to VRRP 2 which both VRRP instances will share.  
- Also take note of the Virtual MAC address. This is the address that the router will use in the active state 
for all the responses. This prevents end stations from having to re-arp to their router in the event of a 
failure: 
sw7 (6870-A) -> show ip vrrp statistics 
Checksum Errors :          0, 
Version Errors  :          0, 
VRID Errors     :          0 
 
                Interface 
VRID              Name                  State      UpTime   Become Master Adv. Rcvd 
----+--------------------------------+----------+----------+-------------+---------- 
   1 int_20                           Master          98575            1           0 
   2 int_30                           Master          81058            1           0

<<<PAGE 310>>>
6 
Virtual Router Redundancy Protocol (VRRP) 
 
sw8 (6860-B) -> show ip vrrp statistics 
Checksum Errors :          0, 
Version Errors  :          0, 
VRID Errors     :          0 
 
                Interface 
VRID              Name                  State      UpTime   Become Master Adv. Rcvd 
----+--------------------------------+----------+----------+-------------+---------- 
   1 int_20                           Backup          44764            0         448 
   2 int_30                           Backup          34581            0         346 
 
- From the “statistics” command, we can see that the 6870-A is the active virtual router. Since all priorities 
are equal, the lowest router ID is the selection criteria.  
- The DHCP server has not been configured with these gateway addresses, so to perform this test we need 
to switch back to static addresses by setting the gateway for clients 5 and 9. 
- Now let's change our default gateway for clients 5 and 9 : 
Client 5: 
IP address = 192.168.20.105 
Subnet mask = 255.255.255.0 
Default Gateway = 192.168.20.254 
Client 9: 
IP address = 192.168.30.109 
Subnet mask = 255.255.255.0 
Default Gateway = 192.168.30.254 
 
 
 
 
- Check the table on the switches 
sw5 (6360-A) -> show mac-learning port 1/1/1 
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+----------------- 
      VLAN                       20   00:50:56:90:22:3c            dynamic     bridging          1/1/1             
 
 Total number of Valid MAC addresses above = 1           
 
sw5 (6360-A) -> show mac-learning port 1/1/2 
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+----------------- 
      VLAN                       30   00:50:56:90:05:d4            dynamic     bridging      1/1/2                
 
 Total number of Valid MAC addresses above = 1 
 
 
Tips > MAC address table empty 
If the MAC address table is empty, generate some traffic from the client connected on the switch (ex. 6360 
MAC@ table empty > from the Client 9, launch a ping to its gateway (192.168.30.8).

<<<PAGE 311>>>
7 
Virtual Router Redundancy Protocol (VRRP) 
 
- From the client 5, try to ping the client 9: 
C:\> ping 192.168.30.109 
 
- Now check the content of the client 5 ARP cache: 
C:\> arp -a 
 
 
 
- Notice that the “Physical Address” which corresponds to the IP address 192.168.20.254 is the VRRP 
interface MAC address (VRRP instance 1 > VLAN 20).  
- Now start a continuous ping to VRRP interface (192.168.20.254) from the client 5 …  
C:\> ping –t 192.168.20.254 
 
- … Then remove the master VRRP gateway (in this example 6870-A). We will simply reboot the switch 
(don’t forget to save!):  
6870-A -> write memory 
6870-A -> reload from working no rollback-timeout 
 
- Notice how quickly the DHL switch from one link to the other, and how fast the Backup VRRP becomes 
master. Check the VRRP status on 6860-B: 
sw8 (6860-B) -> show ip vrrp statistics 
Checksum Errors :          0, 
Version Errors  :          0, 
VRID Errors     :          0 
 
                Interface 
VRID              Name                  State      UpTime   Become Master Adv. Rcvd 
----+--------------------------------+----------+----------+-------------+---------- 
   1 int_20                           Master        6205571            1       62003 
   2 int_30                           Master        6195388            1       61900

<<<PAGE 312>>>
8 
Virtual Router Redundancy Protocol (VRRP) 
 
 3 
Configuring the Master / Backup 
The recommendation at customer site is to manually configure which will be the Master and which will be the 
Backup, the priority of the VRRP instance will be modified here. The higher the value, the higher the priority 
will be to be elected as Master.  
 
- To provide load balancing between the SW7 and SW8, we will configure the 6870-A to be Master on VLAN 
20, and the 6860-B to be Master on VLAN 30. 
- The default priority is 100. Let’s put a priority of 150 for VRRP 1 on 6870-A, and a priority of 150 for VRRP 
2 on 6860-B:  
 
Warning  
THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY 
 
sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state disable  
sw7 (6870-A) -> ip vrrp 1 interface int_20 priority 150 
sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state enable 
 
sw7 (6870-A) -> show ip vrrp statistics 
Checksum Errors :          0, 
Version Errors  :          0, 
VRID Errors     :          0 
 
                Interface 
VRID              Name                  State      UpTime   Become Master Adv. Rcvd 
----+--------------------------------+----------+----------+-------------+---------- 
   1 int_20                           Master           1895            1           3 
   2 int_30                           Backup         112204            0        1122 
 
sw8 (6860-B) -> ip vrrp 2 interface int_30 admin-state disable 
sw8 (6860-B) -> ip vrrp 2 interface int_30 priority 150 
sw8 (6860-B) -> ip vrrp 2 interface int_30 admin-state enable 
 
sw8 (6860-B) -> show ip vrrp statistics 
Checksum Errors :          0, 
Version Errors  :          0, 
VRID Errors     :          0 
 
                Interface 
VRID              Name                  State      UpTime   Become Master Adv. Rcvd 
----+--------------------------------+----------+----------+-------------+---------- 
   1 int_20                           Backup        6356865            1       62164 
   2 int_30                           Master           2228            1           3

<<<PAGE 313>>>
QUALITY OF SERVICE (QOS)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 314>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the Quality of Service main principle
• Configure the OmniSwitch for QoS
- Condition
- Action
- Rules
• Monitor the QoS
• Prioritize automatically the IP Phone Traffic
• Policy based routing
• Remote Port Mirroring (RPM)

<<<PAGE 315>>>
QOS REMINDER
• Goal
• Decide which traffic needs preferential treatment 
and which traffic can be adequately served with 
best effort
• How it works
• QoS is implemented on the switch through 
the use of:
• Port-based QoS configuration
• User-defined policies
• Integration with virtual output queuing to manage egress 
congestion
• Auto-QOS configuration
Basic QOS
* Traffic prioritization
* Bandwidth shaping
* Queuing management
QOS
Policy Based Routing
* Routed traffic redirecting
Policy Based Mirroring
* Mirror traffic based on QoS 
policies 
802.1p/ToS/DSCP
* Marking
* Stamping
Filtering
* Layer 2 and
Layer 3/4  ACLs
ICMP Policies
* Filtering
* Prioritizing
* Rate limiting traffic (security) 
Access Guardian
* User Network Profile

<<<PAGE 316>>>
QOS CONFIGURATION

<<<PAGE 317>>>
QOS CONFIGURATION
Step by Step
Global Parameters 
Configuring Congestion Management
Configuring QoS Port Parameters 
Setting Up Policies
Monitoring Policies
Auto-QOS configuration

<<<PAGE 318>>>
QOS CONFIGURATION
Description
Command/keyword
By default, QoS is enabled on the switch. If QoS policies are 
configured and applied, the switch attempts to classify and apply 
relevant policy actions
qos enable/disable
Displays global information about QoS configuration
show qos config
Resets the QoS configuration to its defaults
qos reset
Deletes the pending configuration
qos revert
Flushes the configuration
qos flush
Apply the configuration
qos apply
Global Parameters

<<<PAGE 319>>>
QOS CONFIGURATION
Step by Step
QSI
QSI for port 1/1
1
2
3
4
5
6
7
8
Egress 
Ports
QSets
Slot 1
1
2
3
4
.
.
20
.
.
Slot 2
1
2
3
4
.
. 
12
Port 1/1
1
2
3
4
5
6
7
8
Queue Set Profile
QSet Profile 1
Q1 = SP7, 100% BW
Q2 = SP6, 100% BW
Q3 = SP5, 100% BW
Q4 = SP4, 100% BW
Q5 = SP3, 100% BW
Q6 = SP2, 100% BW
Q7 = SP1, 100% BW
Q8 = SP0, 100% BW
Strict Priority (SP)
SP0
SP0
100%
a
b
100%
a
b
50%
50%
Port 1/1/1
Port 1/1/3
Port 1/1/2
SP4
SP0
100%
a
b
100%
a
100%
Port 1/1/1
Port 1/1/3
Eg: QSet Profile 1 ( 8SP)
Port 1/1/2
Configuring Congestion Management

<<<PAGE 320>>>
To change the QSP for a specific QSet instance (QSI)
To change the default QSet profile (QSP 1) to one of the other supported profiles (QSP 2, 3, or 4)
QOS CONFIGURATION
Step by Step
-> qos qsi port 1/2/1 qsp 2
-> qos qsi linkagg 5 qsp 2
qos qsp system-default 2
EF
SP5
100%
a
b
20%
b
a
80%
20%
Port 1/1/1
Port 1/2/1
Port 1/2
EF
SP5
100%
a
b
0%
b
100%
Port 1/1/1
Port 1/2/1
Port 1/2
* Eg: QSet Profile 2 (1 EF + 7 SP)
The following Qset profiles (QSP) are supported:
Configuring Congestion Management

<<<PAGE 321>>>
QOS CONFIGURATION
Step by Step
-> qos port [chassis]/slot/port
[trusted]
[maximum egress-bandwidth]
[maximum ingress-bandwidth]
[default 802.1p value]
[default dscp value]
[default classification {802.1p | tos | dscp}]
[dei {ingress | egress}]
-> qos port 1/1/1 maximum egress-bandwidth 10M
-> qos port 1/1/1 default 802.1p 7
-> qos port 1/1/1 trusted
To limit the ingress or egress bandwidth for a QoS port
Change the 802.1p value to 7 for the port 1/1/1
Configure individual ports to recognize 802.1p or ToS
Configuring QoS Port Parameters 
Examples

<<<PAGE 322>>>
QOS CONFIGURATION
Step by Step
----
…
…
----
CONDITION
ACTION
CLASSIFIER (POLICY DATABASE)
FORWARDING ENGINE
INCOMING PACKET
H
E
A
D
E
R
PACKET CLASSIFICATION
L2 (source & dest)
• MAC, VLAN, 
• Slot/Port, IPMS Filtering
L3/L4
• SIP, DIP,
• TCP,UDP,IP proto
• Source TCP/UDP port
• Destination TCP/UDP port
• Prioritization, Bandwidth 
shaping
• ICMP filtering
• ICMP prioritizing, ICMP rate 
limiting
• 802.1p/ToS/DSCP marking and 
mapping
• Policy Based Routing PBR for 
redirecting
• Routed traffic
• Policy Based Mirroring
• Advanced Layer 2 to 4 Filtering
• Server Load Balancing
ACTION
A policy (or a policy rule) is made up of: 
1.
a condition
2.
an action
Setting Up Policies
Gets Policies from
• CLI
• Webview 
• PolicyView (OV)

<<<PAGE 323>>>
QOS CONFIGURATION
Step by Step
• Source port, source port group, destination port, 
destination port group
Layer 1
• Source MAC, source MAC group, destination MAC, 
destination MAC group, 802.1p, 802.1p range, 
Ethertype, source VLAN, destination VLAN
Layer 2
• IP protocol, source IP, multicast IP, destination IP,
• Source network group, destination network group, 
multicast network group
• ToS, DSCP, ICMP type, ICMP code
Layer 3
• Source TCP/UDP port
• Destination TCP/UDP port
• Service, service group, TCP flags
Layer 4
policy condition cond3 source ip 10.10.2.3
policy condition client_traffic source vlan 20
-> policy condition condition_name
[source ip ip_address [mask netmask]]
[source ipv6 {any | ipv6_address [mask netmask]}
[destination ip ip_address [mask netmask]]
[destination ipv6 {any | ipv6_address [mask netmask]}
[multicast ip ip_address [mask netmask]]
[source network group network_group]
[destination network group network_group]
[multicast network group multicast_group]
[destination ip-port port[-port]]
[source tcp-port  port[-port]] 
[destination tcp-port  port[-port]]
[source udp-port port[-port]]
[destination udp-port port[-port]]
[ethertype etype]
[established]
[tcpflags {any | all} flag [mask flag]
[service service]
[service group service_group]
[icmptype type]
[icmpcode code]
[ip protocol protocol] ip protocol 
[ipv6]
[tos tos_value tos_mask]
[dscp {dscp_value[-value} [dscp_mask]]
[source mac mac_address [mask mac_mask]]
[destination mac mac_address [mask mac_mask]]
[source mac group group_name]
[destination mac group mac_group]
[source vlan vlan_id]
[destination vlan vlan_id]
[802.1p 802.1p_value]
[source port slot/port[-port]]
[source port group group_name}
[destination port slot/port[-port]]
[destination port group group_name]
…
Examples
Setting Up Policies
Create a policy condition

<<<PAGE 324>>>
QOS CONFIGURATION
Step by Step
Group
Description
Command/keyword
Policy port group
Slot and port number combinations
policy port group group_name slot/port[-port] [slot/port[-port]...]
Policy mac group
Multiple MAC addresses that may be 
attached to a condition
policy mac group mac_group mac_address [mask mac_mask] [mac_address2 
[mask mac_mask2]...] 
Policy network group
IPv4 source or destination addresses
Default “switch” group
Includes all IPv4 addresses 
configured on the switch 
policy network group net_group ip_address [mask net_mask] 
[ip_address2 [mask net_mask2]...] 
Policy service group
TCP or UDP ports or port ranges
(source or destination)
policy service group service_group service_name1 [service_name2...] 
-> policy port group techports 1/1/1 3/1/1 3/2/1 3/3/1       
-> policy condition cond4 source port group techports
-> policy mac group macgrp2 08:00:20:00:00:00 mask ff:ff:ff:00:00:00 00:20:DA:05:f6:23
-> policy condition cond6 source mac group macgrp2
-> policy network group netgroup3 173.21.4.0 mask 255.255.255.0 10.10.5.3
-> policy condition cond5 destination network group netgroup3
Create a policy group to include into policy condition 
Setting Up Policies
Examples

<<<PAGE 325>>>
QOS CONFIGURATION
Step by Step
-> policy action action_name
[disposition {accept | drop | deny}]
[shared]
[priority priority_value]
[maximum bandwidth bps]
[maximum depth bytes]
[tos tos_value]
[802.1p 802.1p_value]
[dcsp dcsp_value]
[map {802.1p | tos | dscp} to {802.1p | tos| dscp} using map_group]
[permanent gateway ip ip_address]
[port-disable]
[redirect port slot/port]
[redirect linkagg link_agg]
[no-cache]
[{ingress | egress | ingress egress | no} mirror slot/port]
[cir bps [cbs byte] [pir bps] [pbs byte] [counter-color [red-
nonred | green-nongreen | green-red |green-yellow | red- yellow]]
policy action action2 priority 7
policy action SetBits 802.1p 7
ACL (disposition drop)
Change queuing priority
Update TOS/Diffserv and/or 802.1p priority tags
802.1p/TOS/Diffserv marking
802.1p/TOS/Diffserv mapping
Per COS max bandwidth (64K bps)
Maximum depth
Statistics (# of packets, # of bytes)
Ingress policing / Egress shaping
Port Redirection
Routed Traffic Redirection
Link Aggregate Redirection
Port Disable
Mirroring 
Multi-actions support
Ingress Rate Limiting
Create a policy action 
Setting Up Policies
Examples

<<<PAGE 326>>>
QOS CONFIGURATION
Step by Step
Does it Match Condition?
Use higher Action policy 
Use Default Action 
Mark, Prioritize,
Shape Filter, Mirror,…
Description
Keyword
Default
Whether the flow matching the rule 
should be accepted or Denied
disposition
Accept
Actions Defaults
Setting Up Policies
Policy action – Action default

<<<PAGE 327>>>
QOS CONFIGURATION
Step by Step
----
----
CONDITION
ACTION
INCOMING PACKET
H
E
A
D
E
R
ACTION
POLICY RULE
applies to 
outgoing 
traffic
PACKET CLASSIFICATION
-> policy rule rule_name [enable | disable] [precedence precedence] [condition condition] 
[action action] [validity period name | no validity period] [save] [log [log-interval seconds]] 
[count {packets | bytes}] [trap | no trap] [default-list | no default-list]
Sets the precedence for rule r1 and turns on logging
-> policy rule r1 precedence 200 condition c1 action a1 log
policy action a1 redirect port 1/1/2
policy condition c1 source ip 10.10.2.3
Setting Up Policies
Create a policy rule
Examples

<<<PAGE 328>>>
Maps traffic destined for port 3/2 with and 802.1p value of 4 to an 802.1p value of 7
-> policy condition Traffic destination port 1/1/1 802.1p 4
-> policy action SetBits 802.1p 7
-> policy rule Rule2 condition Traffic action SetBits
QOS CONFIGURATION
Step by Step
802.1P MAPPING
Sets traffic from 10.10.2.3 to a priority of 7
-> policy condition cond3 source ip 10.10.2.3
-> policy action action2 priority 7
-> policy rule my_rule condition cond3 action action2
SETTING PRIORITY
Configures a validity period for rule r1
-> policy validity-period vp01 hours 13:00 to 19:00 days monday Friday
-> policy rule r1 validity-period vp01 
Setting Up Policies
Examples

<<<PAGE 329>>>
QOS CONFIGURATION
Step by Step
Monitoring Policies
-> show active policy rule
Displaying the actual number of matches for the configured rules
2 options to configure rule count
Every packet matching a rule will be counted in the “matches” column
Same but count number of bytes instead of number of packets
Rule match counting (on OmniSwitch 6860(E), 6865 and 6900-X72)
-> policy rule <name> count packets (default)
-> policy rule <name> count bytes

<<<PAGE 330>>>
QOS CONFIGURATION
Step by Step
-> show qos config
-> show qos statistics
-> show qos log
Display the QoS statistics
Display  global information on the QoS configuration
Displays the QoS event log. This command also 
displays packets dropped by IP source filter entries
Monitoring Policies

<<<PAGE 331>>>
QOS SPECIFICATION

<<<PAGE 332>>>
AUTOMATIC PRIORITIZATION
FOR IP PHONE TRAFFIC

<<<PAGE 333>>>
QOS CONFIGURATION
• Automatic Prioritization for IP Phone Traffic
• Enable by default on the switch
• To prioritize the phone traffic instead of merely trusting it
• To disable automatic IP phone traffic prioritization for the switch
• Additional MAC group
• The alaPhones mac group must be redefined
MAC Address Range
Description
00:80:9F:00:00:00 to 00:80:9F:FF:FF:FF
Enterprise IP Phones Range
78:81:02:00:00:00 to 78:81:02:FF:FF:FF
Communications IP Phones Range
00:13:FA:00:00:00 to 00:13:FA:FF:FF:FF
Lifesize IP Phones Range
48-7A-55-00-00-00 to 48-7A-55-FF-FF-FF
ALE 8008 IP Phone MAC Range
Mac adress = ALE Phone > Priority 5
Non ALE Phone > Default
On trusted and 
un-trusted ports
Switch detects traffic coming from ALU phones
(based on MAC address)
policy mac group alaPhones
00:80:9f:00:00:00 mask ff:ff:ff:00:00:00
-> qos phones [priority priority_value | trusted]
-> qos no phones

<<<PAGE 334>>>
POLICY BASED ROUTING

<<<PAGE 335>>>
POLICY BASED ROUTING (PBR)
• QoS policies that will override the normal routing mechanism for traffic matching the 
policy condition
• Redirect untrusted traffic to a proxy firewalling server
• i.e specific source traffic (e.g. HTTP, FTP) can be redirected to a cache engine 
• Virtual inline deployment
• Done in hardware
Redirect traffic from source 20.0.0.0/8  to Firewall
R2
R3
R1
24.0.0.0/8
150.21.0.0/16
10.0.0.0/8
191.24.0.0/16
190.27.3.0/24
20.0.0.0/8

<<<PAGE 336>>>
POLICY BASED ROUTING (PBR) 
• Conditions
• IP Protocol (i.e. ICMP, TCP, ICMP)
• Source IP address (or network group)
• Destination IP address (or network group)
• Source TCP/UDP port
• Destination TCP/UDP port
• Source TCP/UDP service
• Destination TCP/UDP service
• Source TCP/UDP service group
• Destination TCP/UDP service group
• TOS, DSCP
• Source VLAN
• Source slot/port
• Source slot/port group
• Action
• Define gateway to be used overriding the routing 
database
• Can be set to local next hop IP or remote hop IP
• PBR is supported on OmniSwitch 6570M, 6860, 
6865, 6900 and 9900
-> policy action <action_name> permanent gateway ip <ip address>

<<<PAGE 337>>>
POLICY BASED ROUTING - EXAMPLE
• All traffic originating in the 10.10.0.0 network is routed through the firewall,
regardless of whether a route exists
Internet
2/1/1
192.168.10.0
192.168.99.0
20.10.0.0
10.10.0.0
Unknown DA
192.168.99.254
Firewall/Gateway
Routed back   OR   Other destinations
-> policy condition Traffic10 source ip 10.10.0.0 mask 255.255.0.0 
-> policy action Firewall permanent gateway ip 192.168.99.254 
-> policy rule Redirect_All condition Traffic10 action Firewall

<<<PAGE 338>>>
POLICY BASED ROUTING - EXAMPLE
• Traffic from the firewall is sent back to the switch to be re-routed
• Adding the source port to the condition allows traffic to not get caught in a loop
Internet
2/1/1
192.168.10.0
192.168.99.0
20.10.0.0
10.10.0.0
Unknown DA
192.168.99.254
Firewall/Gateway
Routed back   OR   Other destinations
-> policy condition TrafficFromFW source IP 10.10.0.0 mask 255.255.0.0 source port 2/1/1
-> policy action To_Internet permanent gateway IP 192.168.10.254
-> policy rule Redirect_Internet condition TrafficFromFW action To_Internet

<<<PAGE 339>>>
REMOTE PORT MIRRORING (RPM)

<<<PAGE 340>>>
REMOTE PORT MIRRORING (RPM) 
• Allows traffic to be carried over the network to a remote switch
• Achieved by using a dedicated remote port mirroring VLAN 
• RPM VLAN has to be configured on the source, destination and intermediate switches 
• No other traffic is allowed on that VLAN
• The following types of traffic will not be mirrored:
• Link Aggregation Control Packets (LACP), 802.1AB (LLDP), 802.1x port authentication,  802.3ag 
(OAM), Layer 3 control packets, Generic Attribute Registration Protocol (GARP)
SOURCE PORT
DESTINATION PORT
INTERMEDIATE SWITCH
SOURCE SWITCH
DESTINATION SWITCH

<<<PAGE 341>>>
POLICY BASED MIRRORING
• Mirroring is done based on a QoS policy instead of a specific port
• 1 session supported at any given time
• Port Based Mirroring. It can be done on incoming or outgoing traffic or both.
• Policy action mirror
• Mirror traffic based on
• Source & Destination addresses
• Address pairs
• Protocols
• VLAN classification
• Port mirroring and monitoring cannot be configured on the same port
MIRRORING POLICY
INGRESS, EGRESS, OR BOTH INGRESS & EGRESS PACKETS
POLICY ACTION & PORT ASSIGNMENT
DIRECT TRAFFIC TO MIRROR PORT

<<<PAGE 342>>>
POLICY BASED MIRRORING
• Example 1
• Example 2
-> policy condition c1 source ip 1.1.1.1
-> policy action a2 ingress egress mirror 1/1/1 disposition drop 
-> policy rule r2 condition c1 action a2
-> qos apply
-> policy condition c1 source ip 1.1.1.1
-> policy action a1 ingress egress mirror 1/1/1 
-> policy rule r1 condition c1 action a1
-> qos apply
Policy rule r1 will cause all packets with a source IP of 1.1.1.1 to be ingress and egress 
mirrored to port 1/1/1
Policy rule r2 drops traffic with a source IP of 1.1.1.1, but the mirrored traffic from 
this source is not dropped and is forwarded to port 1/1/1

<<<PAGE 343>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 344>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Quality of Service (QoS) 
How to 
✓ Configure Quality of Service rules on the OmniSwitches R8 
Contents 
1 
Introduction .................................................................................... 2 
2 
Configuring Port Default 802.1P/ToS/DSCP ............................................... 3 
3 
Configuring Trusted Ports .................................................................... 3 
3.1. Example 1 ........................................................................................... 3 
3.2. Example 2 ........................................................................................... 4 
4 
Configuring the Policies ...................................................................... 4

<<<PAGE 345>>>
2 
Quality of Service (QoS) 
 
 1 
Introduction 
By default, the QoS feature is enabled on an OmniSwitch. If QoS policies are configured and applied, the switch 
will attempt to classify traffic and apply relevant policy actions.  
 
 
Diagram containing all the devices that will be used during this lab:  
 
 
- 
Before beginning, reset all the QoS parameters back to default (6360-A): 
sw5 (6360-A) -> qos flush 
sw5 (6360-A) -> qos apply  
sw5 (6360-A) -> show qos config 
QoS Configuration 
  Admin                          = enable, 
  Trust ports                    = no, 
  Log lines                      = 10240, 
  Log level                      = 6, 
  Log console                    = no, 
  Forward log                    = no, 
  User-port filter               = spoof , 
  User-port shutdown             = none, 
  Phones                         = trusted, 
  DEI Mapping                    = disable, 
  DEI Marking                    = disable, 
  Pending changes                = none 
 
 
 
Notes 
In this lab, we will not cover all the QoS features. The main objective of this lab is to provide an overview 
about how to configure the QoS. For more information, read the Policy Condition Combination table in the 
Network Configuration Guide for a list of valid combinations.

<<<PAGE 346>>>
3 
Quality of Service (QoS) 
 
 2 
Configuring Port Default 802.1P/ToS/DSCP  
By default, the port default values for 802.1p and ToS/DSCP are 0. To change the default 802.1p or ToS/DSCP 
settings for a port, use the qos port default 802.1p or qos port default dscp command.  
- 
Change the 802.1p value to 7 for the port 1/1/1: 
sw5 (6360-A) -> show qos port 1/1/1 
Slot/                 Default    Default               Bandwidth           DEI 
Port    Active  Trust P/DSCP Classification  Physical  Ingress Egress    Map Mark   Type 
-------+-------+-----+------+--------------+----------+-------+------+------+------+------------- 
1/1/1     Yes      No  0/ 0           DSCP       100M       -       -    No    No   ethernet-100M 
 
sw5 (6360-A) -> qos port 1/1/1 default 802.1p 7 
 
sw5 (6360-A) -> show qos port 1/1/1 
Slot/                 Default    Default               Bandwidth           DEI 
Port    Active  Trust P/DSCP Classification  Physical  Ingress Egress    Map Mark   Type 
-------+-------+-----+------+--------------+----------+-------+------+------+------+------------- 
1/1/1     Yes      No  7/ 0           DSCP       100M       -       -    No    No   ethernet-100M 
 
 
Notes 
In this example above:  
- Any untagged traffic (traffic without any 802.1p settings) arriving on port 1/1/1 will be tagged with an 
802.1p value of 7 (highest priority).  
- If the port is configured to be untrusted, any tagged traffic will be tagged with an 802.1p value of 7. 
- If the port is configured to be trusted, any tagged traffic will preserve the 802.1p value in the flow.  
 
By default, switched ports are untrusted. 
 
 3 
Configuring Trusted Ports 
3.1. 
Example 1 
 
- 
To configure individual ports to recognize 802.1p or ToS, use the qos port trusted command with the 
desired slot/port number: 
 
sw5 (6360-A) -> qos port 1/1/1 trusted 
 
sw5 (6360-A) -> qos apply 
 
sw5 (6360-A) -> show qos port 1/1/1 
 
Slot/                 Default    Default               Bandwidth           DEI 
Port    Active  Trust P/DSCP Classification  Physical  Ingress Egress    Map Mark   Type 
-------+-------+-----+------+--------------+----------+-------+------+------+------+------------- 
1/1/1     Yes    +Yes  7/ 0           DSCP       100M       -       -   Yes    No   ethernet-100M 
 
 
Notes 
In this example above, the qos port trusted command specifies that port will be able to recognize and trust 
the 802.1p bits. The global setting is active immediately; however, modifying a port configuration requires qos 
apply to activate the change.

<<<PAGE 347>>>
4 
Quality of Service (QoS) 
 
3.2. 
Example 2 
- 
In the following example:  
o 
A policy condition “Traffic” is then created to classify traffic containing 802.1p bits set to 4.  
o 
The policy action “SetBits” specifies that the bits will be changed to 7 when the traffic leaves 
the switch  
o 
A policy rule called 802.1p_rule puts the condition and the action together.  
 
sw5 (6360-A) -> policy condition Traffic 802.1p 4 
 
sw5 (6360-A) -> policy action SetBits 802.1p 7 
 
sw5 (6360-A) -> policy rule 802.1p_rule condition Traffic action SetBits 
 
sw5 (6360-A) -> qos apply 
 
 
Notes 
802.1p mapping may also be set for Layer 3 traffic, which typically has the 802.1p bits set to 0. 
 
- 
In the above example, what would happen if ingress traffic on chassis 1 slot 1 port 1 was tagged with an 
802.1p value of 5? 
----------------------------------------------------------------------------------------------------------------------------------- 
 
- 
To view the QoS configuration: 
sw5 (6360-A) -> show policy condition 
Condition name                   : Traffic 
  802.1p                         = 4 
 
sw5 (6360-A) -> show policy action 
Action name                      : SetBits 
  802.1p                         = 7 
 
sw5 (6360-A) -> show policy rule 
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
 4 
Configuring the Policies 
 
Let’s consider that the devices located in the VLAN 20 are employees, and the devices located in the VLAN 30 
are contractors. We want to prioritize employees’ traffic over contractors’ traffic.  
 
- 
To create a policy rule to prioritize the traffic from VLAN 20:  
o 
Create a condition for the traffic that you want to prioritize (ex. client_traffic) 
o 
Create an action to prioritize the traffic as highest priority (ex. priority_5)  
o 
Combine the condition and the action into a policy rule (ex. rule1)  
 
sw5 (6360-A) -> policy condition client_traffic source vlan 20 
sw5 (6360-A) -> policy action priority_5 802.1p 5 
sw5 (6360-A) -> policy rule rule1 condition client_traffic action priority_5

<<<PAGE 348>>>
5 
Quality of Service (QoS) 
 
- 
The rule is not active on the switch until it has been applied: 
sw5 (6360-A) -> show active policy rule 
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
 
sw5 (6360-A) -> qos apply 
 
sw5 (6360-A) -> show active policy rule 
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
 
Rule name                        : rule1 
  Condition name                 = client_traffic, 
  Action name                    = priority_5, 
  Packets                        = 163, 
  Bytes                          = 10249 
 
- 
In this following example, any flow coming from the VLAN 20 is sent to a queue supporting its maximum 
bandwidth requirement. Via the QoS feature, it is also possible to modify the policy action that you have 
created earlier to limit the maximum bandwidth: 
sw5 (6360-A) -> policy action priority_5 maximum bandwidth 100k 
sw5 (6360-A) -> qos apply 
 
sw5 (6360-A) -> show policy action priority_5 
Action name                      : priority_5 
  Maximum bandwidth              =  100K, 
  802.1p                         = 5 
 
- 
The bandwidth can be specified in abbreviated units, in this case, 100k (= 100 kbps).  
- 
Check the management: 
sw5 (6360-A) -> show policy condition 
Condition name                   : Traffic 
  802.1p                         = 4 
 
Condition name                   : client_traffic 
  Source VLAN                    = 20 
 
sw5 (6360-A) -> show policy action 
Action name                      : SetBits 
  802.1p                         = 7 
 
Action name                      : priority_5 
  Maximum bandwidth              =  100K, 
  802.1p                         = 5 
 
sw5 (6360-A) -> show policy rule 
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
 
Rule name                        : rule1 
  Condition name                 = client_traffic, 
  Action name                    = priority_5 
 
- 
To specify a precedence value for a rule, use the policy rule command with the precedence keyword: 
sw5 (6360-A) -> policy rule rule1 precedence 1000 condition client_traffic action priority_5 
 
- 
Launch a ping from client 5 (which is in the VLAN 20) to client 9: 
C:\> ping 192.168.30.xx (check ip address allocated dynamically to client 9)

<<<PAGE 349>>>
6 
Quality of Service (QoS) 
 
- Check the active rule result:  
sw5 (6360-A) -> show active policy rule 
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
Rule name                        : rule1 
  Condition name                 = client_traffic, 
  Action name                    = priority_5, 
  Packets                        = 12555, 
  Bytes                          = 756988, 
  Green Packets                  = 6982 
 
As it doesn’t exceed the maximum bandwidth, it should work. 
- 
Now, try to launch a ping by specifying a greater datagram size: 
Client5 C:\> ping –l 65000 192.168.30.xx (check ip address allocated dynamically to client 9) 
 
- Check the active rule result:  
sw5 (6360-A) -> show active policy rule 
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
Rule name                        : rule1 
  Condition name                 = client_traffic, 
  Action name                    = priority_5, 
  Packets                        = 13527, 
  Bytes                          = 1068548, 
  Green Packets                  = 7386, 
  Red Packets                    = 148 
 
 
Notes: Green, Yellow, Red?  
Tri-Color Marking (TCM) statistics; the number of packets/bytes that are marked Green (low drop precedence), 
Yellow (high drop precedence), and Red (always drop).  
 
- 
Your ping is now using a greater bandwidth, so it shouldn’t work. 
- 
To remove an action parameter or return the parameter to its default, use no with the relevant 
keyword: 
sw5 (6360-A) -> policy action priority_5 no maximum bandwidth 
 
- 
By default, rules are enabled. Rules may be disabled or re-enabled through the policy rule command: 
sw5 (6360-A) -> policy rule rule1 disable 
sw5 (6360-A) -> qos apply 
sw5 (6360-A) -> show active policy rule  
Rule name                        : 802.1p_rule 
  Condition name                 = Traffic, 
  Action name                    = SetBits 
 
sw5 (6360-A) -> policy rule 802.1p_rule disable 
sw5 (6360-A) -> policy rule rule1 disable 
sw5 (6360-A) -> qos apply 
sw5 (6360-A) -> show active policy rule 
No active rules 
 
- 
Once testing is complete, remove the condition, action and rule: 
sw5 (6360-A) -> no policy rule rule1 
sw5 (6360-A) -> no policy rule 802.1p_rule 
sw5 (6360-A) -> no policy action priority_5 
sw5 (6360-A) -> no policy action SetBits 
sw5 (6360-A) -> no policy condition Traffic 
sw5 (6360-A) -> no policy condition client_traffic 
sw5 (6360-A) -> qos apply

<<<PAGE 350>>>
7 
Quality of Service (QoS) 
 
 
sw5 (6360-A) ->show policy rule 
No pending rules 
 
 
Tips > Logs 
- Logging a rule may also be useful for determining such things as the source of attacks. Often, at least when 
initially configuring your rules, it is recommended to use the log option to monitor how your policies are being 
used. To log information about flows that match the policy rule rule1: sw5 (6360-A) -> policy rule rule1 log 
- To check the logs: sw5 (6360-A) -> show qos log

<<<PAGE 351>>>
ACCESS CONTROL LISTS (ACL)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 352>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the benefits of using ACLs
• Implement ACL on an OmniSwitch switch
• Advanced ACL Groups

<<<PAGE 353>>>
ACCESS CONTROL LISTS (ACL)
• Goal
• QoS policies used to control whether or not packet 
flows are allowed or denied at the switch or router 
interface
• How it works
• Policies for ACLs are created in the same manner as 
QoS policies
• Customizable Groups for conditions
• Network group
• MAC group
• Service group
• Port group
Basic QOS
* Traffic prioritization
* Bandwidth shaping
* Queuing management
QOS
Policy Based Routing
* Routed traffic redirecting
Policy Based Mirroring
* Mirror traffic based on QoS 
policies 
802.1p/ToS/DSCP
* Marking
* Stamping
Filtering
* Layer 2 and
Layer 3/4  ACLs
ICMP Policies
* Filtering
* Prioritizing
* Rate limiting traffic (security) 
Access Guardian
* User Network Profile

<<<PAGE 354>>>
ACCESS CONTROL LISTS (ACL)
Packet classification
----
DISPOSITION
accept | drop | deny
CONDITION
ACTION
POLICY RULE
PACKET CLASSIFICATION
policy condition
LAYER 2 ACL 
CONDITION KEYWORDS
LAYER 3 ACL 
CONDITION KEYWORDS
MULTICAST ACL 
CONDITION KEYWORDS
source mac
source mac group
destination mac
destination mac group
source vlan
source port
source port group
destination port
destination port group
ethertype
802.1p
source ip
source ipv6
source network group
destination ip
destination ipv6
destination network 
group
source ip port
destination ip port
service
service group
ip protocol
ipv6
nh
flow-label
destination port
destination port group
icmptype
icmpcode
TOS  DSCP
source tcp port
destination tcp port
source udp port
destination udp port
established
Tcpflags
multicast ip
multicast network 
group
destination ip
destination vlan
destination port
destination port group
destination mac
destination mac group
policy action
accept | drop | deny
INCOMING PACKET
FORWARD / BLOCK
OUTGOING TRAFFIC
policy rule rule_name no {validity-period | save | log | trap | default-list}
policy rule rule_name [enable | disable] [precedence precedence] [condition condition]
[action action] [validity-period name] [save][log [log-interval seconds]]
[count {packets | bytes}] [trap] [default-list]
no policy rule rule_name

<<<PAGE 355>>>
ACCESS CONTROL LISTS (ACL)
Step by Step
Global Parameters 
Setting Up Policies
Configuration Examples
Monitoring Policies

<<<PAGE 356>>>
ACCESS CONTROL LISTS (ACL)
Step by Step
Description
Command/keyword
By default, QoS is enabled on the switch. If QoS policies are 
configured and applied, the switch attempts to classify and 
apply relevant policy actions
qos enable/disable
Resets the QoS configuration to its defaults
qos reset
Deletes the pending configuration
qos revert
Flushes the configuration
qos flush
Apply the configuration
qos apply
* By default, flows that do not match any policies are accepted on the switch
Global Parameters

<<<PAGE 357>>>
ACCESS CONTROL LISTS (ACL)
Step by Step
----
DISPOSITION ACCEPT OR DENIED
CONDITION
ACTION
POLICY RULE
PACKET CLASSIFICATION
LAYER 2 ACL 
CONDITION KEYWORDS
LAYER 3 ACL 
CONDITION KEYWORDS
MULTICAST ACL 
CONDITION KEYWORDS
source mac
source mac group
destination mac
destination mac group
source vlan
source port
source port group
destination port
destination port group
ethertype
802.1p
source ip
source ipv6
source network group
destination ip
destination ipv6
destination network group
source ip port
destination ip port
service
service group
ip protocol
ipv6
nh
flow-label
destination port
destination port group
icmptype
icmpcode
TOS  DSCP
source tcp port
destination tcp port
source udp port
destination udp port
established
Tcpflags
multicast ip
multicast network 
group
destination ip
destination vlan
destination port
destination port group
destination mac
destination mac group
-> policy port group pgroup1 1/1/1-5 2/1/1-2
policy action a1 disposition accept
1
2
-> policy condition c2 source port group pgroup1
3
4
policy rule rule7 precedence 65535 condition c2 action a1 
qos apply
5
Setting Up Policies

<<<PAGE 358>>>
ACCESS CONTROL LISTS (ACL)
Step by Step
-> policy condition Cond-Deny-Host1 source mac D4:85:64:EC:33:EF source vlan 5
-> policy action Act-deny-Host1 disposition deny
-> policy rule Rule-Deny-Host1 condition Cond-Deny-Host1 action Act-deny-Host1 log
-> qos apply
-> policy network group netgroup1 192.168.82.0 mask 255.255.255.0
-> policy condition lab1 source network group netgroup1
-> policy action deny_traffic disposition deny
-> policy rule lab_rule1 condition lab1 action deny_traffic precedence 65535
-> qos apply
Configuration Examples
Layer 2 ACL
Allows all bridged traffic except for traffic matching the source MAC address and VLAN 5
Layer 3 ACL
Deny traffic from source IP address included in netgroup1

<<<PAGE 359>>>
ACCESS CONTROL LISTS (ACL)
Step by Step
-> policy condition addr2 source ip 192.68.82.0 destination tcp-port 23
-> policy action Block disposition deny
-> policy rule FilterL31 condition addr2 action Block 
-> policy network group GroupA 192.60.22.1 192.60.22.2 192.60.22.1
-> policy condition cond7 destination network group GroupA
-> policy action Ok disposition accept
-> policy rule FilterL32 condition cond7 action Ok
Configuration Examples
Layer 3 ACL
Drop the Traffic with a source IP address of 192.68.82.0, a source IP port of 23, using 
protocol 6 on the switch
Layer 3 ACL
Flows coming into the switch destined for any of the specified IP in GroupA is allowed 
on the switch

<<<PAGE 360>>>
Monitoring Policies
ACCESS CONTROL LISTS (ACL)
Step by Step
-> show qos config
-> show qos statistics
-> show qos log
-> show active policy rules

<<<PAGE 361>>>
ADVANCED ACL SECURITY FEATURES

<<<PAGE 362>>>
QOS CONFIGURATION - SECURITY FEATURES
• UserPorts
• Reserved Group
• Used by default to prevent spoofed IP addresses on ports
• Packets received on the port are dropped if they contain a source IP network address that does not match 
the IP subnet for the port
• Done by creating a port group called UserPorts and adding the ports to that group
• Profiles can be configured to drop additional traffic such as RIP, OSPF,VRRP, DHCP, DNS,… or BPDUs
• To configure filtering of spoof, rip, ospf , bgp packets
-> show qos log
…
12/17/10 14:27:39 12/17/16 14:27:39 Spoofed traffic triggered user-port shutdown of interface 1/1/21
…
-> policy port group UserPorts 1/1-24 2/1-24 3/1/1 4/1/1
-> qos user-port filter spoof rip ospf bgp
-> policy port group UserPorts slot/port[-port] [slot/port[-port]...]
-> qos user-port  {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|dvmrp|pim|isis|dhcpserver|dns-reply}

<<<PAGE 363>>>
ADVANCED ACL SECURITY FEATURES
• DropServices
• Reserved Group
• Used in conjunction with UserPorts to drop TCP/UDP packets
• Any services belonging to this group will be dropped if seen on ports included in the UserPorts
group
• Drops all defined traffic seen on ports 1/1/1-24 in the UserPorts group
• Port Disable rule
• Used to administratively disable an interface when matching a policy rule
• To shutdown ports when packet with source tcp port 1-1023 is received
-> policy service tcp135 destination tcp 135
-> policy service tcp445 destination tcp 445
-> policy service udp137 destination udp 137
-> policy service group DropServices tcp135 tcp445 udp137
-> policy port group UserPorts 1/1/1-24
-> policy condition c1 source tcp 1-1023
-> policy action a1 port-disable
-> policy rule r1 condition c1 action a1

<<<PAGE 364>>>
ADVANCED ACL SECURITY FEATURES
• ICMP drop rules
• Allows for configuring rules to drop ICMP requests and replies (Pings)
• TCP connection rules
• Established. Allows established TCP connections
• Tcpflags. Allows examination of specific TCP flags
• Configurable recovery timer that automatically re-enables the port
• When not configured, or configured to 0, the port will not be automatically re-enabled
•
Time interval to re-enable the UserPort ports automatically after the UserPort ports are disabled administratively due to receiving a specified 
type of traffic
•
UserPort ports to send out a port violation recovery trap when the UserPorts ports get reenabled after a timeout
-> interfaces violation-recovery-time <num>
-> policy condition pingEchoRequest source vlan 10 icmptype 8
-> policy action drop disposition drop
-> policy rule noping10 condition pingEchoRequest action drop
Drops all ICMP requests from vlan 10
-> interfaces violation-recovery-trap {enable | disable}

<<<PAGE 365>>>
ADVANCED ACL SECURITY FEATURES
• Early ARP discard
• Limitation of  number of ARP packets sent to CPU
• ARP packets not destined for switch are not processed
• Enabled by default
• ARPs intended for use by a local subnet, AVLAN, VRRP, and Local Proxy ARP are not discarded
• ARP ACLs
• Source IP address examination in the header of ARP packets
• Directed Broadcasts
• IP datagram sent to broadcast address of subnet the user is not on
• Generates large number of responses to a spoofed host
-> ip directed-broadcast disable

<<<PAGE 366>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 367>>>
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

<<<PAGE 368>>>
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

<<<PAGE 369>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Access Control Lists (ACLs) 
How to 
✓ Setting up Access Control Lists (ACLs) on the OmniSwitches R8 
Contents 
1 
Introduction .................................................................................... 2 
1.1. Retrieving client’s information ................................................................... 2 
2 
Filtering L2 traffic ............................................................................ 3 
3 
Using the ICMP Filter ......................................................................... 3 
4 
Filtering HTTP & FTP Traffic ................................................................ 4 
4.1. Filtering the FTP Traffic (OmniSwitch 6360 VC) ............................................... 4 
4.1.1. Checking the access to the FTP Server .................................................................. 4 
4.1.2. Testing the FTP Access .................................................................................... 4 
4.2. Filtering the HTTP Traffic ......................................................................... 4 
4.3. Filtering the HTTP Traffic ......................................................................... 5 
4.4. Testing the Configuration ......................................................................... 5 
5 
Configuring User ports Security ............................................................. 5

<<<PAGE 370>>>
2 
Access Control Lists (ACLs) 
 
 1 
Introduction 
 
 
1.1. 
Retrieving client’s information 
For this lab, you will need some information about client 5 and client 9. 
- Retrieve the MAC address of the client 5 and 9 available in the 6360 VC MAC address table:  
(example the mac address of your client may differ) 
 
sw5 (6360-A) -> show mac-learning  port 1/1/1 
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+----------------- 
      VLAN                       20   00:50:56:90:22:3c            dynamic     bridging          1/1/1  
           
 
sw5 (6360-A) -> show mac-learning  port 1/1/2 
Legend: Mac Address: * = address not valid,

<<<PAGE 371>>>
3 
Access Control Lists (ACLs) 
 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+-----------------  
      VLAN                       30   00:50:56:90:05:d4            dynamic     bridging             1/1/2  
        
 2 
Filtering L2 traffic 
- First, reset the ACL/QoS configuration to its default settings: 
sw5 (6360-A) -> qos reset 
sw5 (6360-A) -> qos flush 
sw5 (6360-A) -> qos apply 
 
- Perform a permanent ping test from Client 5 to the gateway (192.168.20.254): 
 
 
- Deny all the Layer 2 traffic coming from the Client 5: 
sw5 (6360-A) -> policy condition cond1 source mac <Client 5 MAC address> 
sw5 (6360-A) -> policy action DenyTraffic disposition deny 
sw5 (6360-A) -> policy rule Filter1 condition cond1 action DenyTraffic 
sw5 (6360-A) -> qos apply 
 
- Is the ping still working? 
-------------------------------------------------------------------------------------------------------------------------- 
 
- Once the test is done, reset the default bridged disposition: 
sw5 (6360-A) -> qos flush 
sw5 (6360-A) -> qos reset 
sw5 (6360-A) -> qos apply 
 3 
Using the ICMP Filter 
In the following example, we want to forbid an ICMP connection (ping) from the client 5 to the database 
server (192.168.110.51).  
 
- Launch a permanent ping from the Client 5 to the database server (192.168.110.51): 
 
 
- Configure the ICMP filter: 
sw5 (6360-A) -> policy condition icmpCondition source mac <Client 5 Mac address> ip-protocol 1 destination 
ip 192.168.110.51 
 
sw5 (6360-A) -> policy action icmpAction disposition deny 
sw5 (6360-A) -> policy rule icmpRule condition icmpCondition action icmpAction  
sw5 (6360-A) -> qos apply 
 
- Check the ping on the Client 5. What is the result? 
-----------------------------------------------------------------------------------------------------------------------------------

<<<PAGE 372>>>
4 
Access Control Lists (ACLs) 
 
 4 
Filtering HTTP & FTP Traffic  
Let’s get back to the use case where the VLAN 20 is dedicated for the employees, and the VLAN 30 is 
dedicated for the contractors. Here are the rules that needs to be applied: 
 
User Type 
VLAN 
Service Grp = 
HTTP 
Service Grp = 
FTP 
Employees 
20 
ALLOW 
DENY 
Contractors 
30 
DENY 
ALLOW 
 
4.1. 
Filtering the FTP Traffic (OmniSwitch 6360 VC) 
4.1.1. 
Checking the access to the FTP Server 
- Before configuring the policies, check the FTP access (192.168.100.102):  
o 
From the client 5 (VLAN 20) 
o 
From the client 9 (VLAN 30) 
 
From the Windows Command Prompt:  
C:\> ftp 192.168.100.102 
 
Client 5 
Client 9 
 
 
 
 
- 
To deny the FTP access for the employees (VLAN 20):  
sw5 (6360-A) -> policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6  
sw5 (6360-A) -> policy action deny disposition deny 
sw5 (6360-A) -> policy rule deny_ftp_employee condition ftpfromvlan20 action deny precedence 65535 
sw5 (6360-A) -> qos apply 
 
- 
Check that you don’t have FTP access from the Client 5 (employee, VLAN 20), but it is still working fine 
from the Client 9 (contractor, VLAN 30): 
4.1.2. 
Testing the FTP Access 
- 
Check that you don’t have FTP access from the Client 5 (employee, VLAN 20), but it is still working fine 
from the Client 9 (contractor, VLAN 30): 
/ 
Client 5 
Client 9 
FTP 
 
 
4.2. 
Filtering the HTTP Traffic 
- Before configuring the policies, check the HTTP access:  
o 
From the client 5 (VLAN 20)

<<<PAGE 373>>>
5 
Access Control Lists (ACLs) 
 
o 
From the client 9 (VLAN 30) 
- Notes: Needed to add DNS server or check that the clients have the DNS server entry in the NIC. 
Should be ok, provided via dhcp server. 
 
From a web browser (ex. Firefox, Chrome):  
URL: www.google.com 
Client 5 
Client 9 
 
 
4.3. 
Filtering the HTTP Traffic 
- 
To deny the HTTP access for the contractors (VLAN 30), create the policy services to identify the port 
used by the HTTP protocol:  
sw5 (6360-A) -> policy service http1 destination ip-port 80 protocol 6 
sw5 (6360-A) -> policy service http2 destination ip-port 8080 protocol 6 
sw5 (6360-A) -> policy service http3 destination ip-port 8000 protocol 6 
sw5 (6360-A) -> policy service http4 destination ip-port 443 protocol 6 
sw5 (6360-A) -> policy service http5 destination ip-port 4343 protocol 6 
 
- 
Regroup the policy services created in a policy group:  
sw5 (6360-A) -> policy service group http from cli http1 http2 http3 http4 http5 
 
- Create the policy condition and the policy rule: 
sw5 (6360-A) -> policy condition httpfromvlan30 source vlan 30 destination ip any service group http  
sw5 (6360-A) -> policy action deny disposition deny 
 
sw5 (6360-A) -> policy rule deny_http_contractor condition httpfromvlan30 action deny precedence 65535 
sw5 (6360-A) -> qos apply 
- 
Check that you don’t have HTTP access from the Client 9 (contractor, VLAN 30), but it is still working 
fine from the Client 5 (employee, VLAN 20): 
4.4. 
Testing the Configuration 
- 
Check that you don’t have HTTP access from the Client 9 (contractor, VLAN 30), but it is still working 
fine from the Client 5 (employee, VLAN 20): 
 
/ 
Client 5 
Client 9 
HTTP 
 
 
 5 
Configuring User ports Security 
If network protocols, like STP, are not blocked from user ports, a rogue device can use these protocols and 
disrupt normal network operation. 
 
- To prevent IP source address spoofing, add ports to the port group called UserPorts:

<<<PAGE 374>>>
6 
Access Control Lists (ACLs) 
 
sw5 (6360-A) -> policy port group Userports 1/1/1-2 
 
 
Notes 
This port group does not need to be used in a condition or rule to be effective on flows and only applies to 
routed traffic. Ports added to the UserPorts group will block spoofed traffic while still allowing normal traffic 
on the port 
 
- To avoid any loop in the network, any user access port used will be blocked if a Spanning Tree frame is 
received: 
sw5 (6360-A) -> qos user-port shutdown bpdu

<<<PAGE 375>>>
A C C E S S  G U A R D I A N
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 376>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Access Guardian 
• Setup Access Guardian 
- Port
- User Network Profile
- Classification Rule / policy
- Port-Templates 
- Authentication server (Radius Server)
• Monitor the management

<<<PAGE 377>>>
OVERVIEW
Goal
• Role Based Access Control with UNP (Universal Network Profile)
• Auto-sensing, multi-client authentication on a port

<<<PAGE 378>>>
OVERVIEW
How it works
Authentication Method
MAC-based (non-supplicant)
or 
802.1x-based (supplicant)
{ "user"
User-Password="xxxxxx"
Filter-ID = "UNP-name"
}
RADIUS Access-Accept + UNP name
RADIUS Access-Request
UNP R8
VLAN
10
ACCESS
ALL
HIGH 
BWDTH
HIGH 
PRIORITY
EXECUTIVE
VLAN
30
INTERNET 
ONLY
MEDIUM 
BWDTH
LOW 
PRIORITY
GUEST
VLAN
20
NO HR, 
FINANCE DB
MEDIUM 
BWDTH
MEDIUM 
PRIORITY
EMPLOYEE
Period
Location
VLAN ID
Policy List
ACL
QoS
VLAN ID
Policy List
ACL
QoS
Specifies the days and times during 
which a device can access the network
Restrict the network access based on the 
location of the user/device
Chassis/Slot/Port on which the user is attached 
Switch Name on which the user is attached 
Switch Location String, identifying a group of 
Switches

<<<PAGE 379>>>
OVERVIEW
Example: Access control via UNP - Campus
Student
1 - Non-802.1X frame sent
2 - Non-802.1X frame intercepted by switch
3 - Switch builds auth. Request using source MAC as login/password
4 - Authentication frame is sent to RADIUS Server
5 - MAC validated
6 - Device moved to appropriate UNP
7 - MAC failed
> Device moved to Default UNP for registration
Student
UNP
Default 
UNP
Admin/Teacher
UNP
Admin
Teacher
1 – 802.1X/EAP Auth. frame sent with user/login
2 - EAP intercepted by switch
3 – Switch modifies Radius frame with source MAC
4 - Relays authentication frame to Server
5 - Login/password validated
6 - Device moved to appropriate UNP
7 - Login/password failed
> Device moved to Default UNP for registration
802.1X - Supplicant
Non - Supplicant
Admin and teachers use 802.1X 
authentication
Students can be authenticated via 
either 802.1X or MAC based

<<<PAGE 380>>>
ACCESS GUARDIAN FLOW
Device classification policies - Policies conceptual flow
Yes
802.1X 
enabled ?
802.1x
Pass 
L2 Authentication 
UNP Selection
Supplicant?
Yes
Same branch as 
802.1x
MAC 
Enabled?
No
No
Yes
No
No Auth
Server Down
UNP Port 
Block
No UNP
Alternate
UNP Profile
Not valid UNP
Block
Server Down
UNP Profile
Timeout
UNP Profile
RADIUS Filter-Id
Default
UNP Profile
Block
Fail
Classification
Rules
UNP Profile
No

<<<PAGE 381>>>
CONFIGURATION STEPS

<<<PAGE 382>>>
CONFIGURATION STEPS
Step by Step
-> unp {port chassis/slot/port1[-port2] | linkagg agg_id1[-agg_id2]} port-type bridge
-> unp {port chassis/slot/port1[-port2] | linkagg agg_id[-agg_id2]} 802.1x-authentication
-> unp {port chassis/slot/port1[-port2] | linkagg agg_id[-agg_id2]} mac-authentication
Bridge Port
UNP profile
VLAN ID
MAC or 802.1x
or
Classification rules
Policy List
ACL
QoS
-> unp port 1/1/1 port-type bridge
-> unp port 1/1/1 802.1x-authentication
-> unp port 1/1/1 mac-authentication
Example
Configure ports

<<<PAGE 383>>>
CONFIGURATION STEPS
Step by Step
-> unp policy validity-location policy_name [port chassis/slot/port[-port2] |
linkagg agg_id[-agg_id2] [system-name system_name] [system-location system_location]
-> unp policy validity-location ALE-Brest port 1/1/10
-> unp policy validity-location ALE-Brest port 1/1/1-5
Configure UNP policy validity-location
Example
UNP profile
VLAN ID
Policy List
ACL
QoS
Location
Period

<<<PAGE 384>>>
CONFIGURATION STEPS
Step by Step
-> unp policy validity-period policy_name [days days] [months months] [hours
hh:mm to hh:mm] [interval mm:dd:yy hh:mm to mm:dd:yy hh:mm] [timezone zones]]
unp policy validity-period “Office-Time” 
unp policy validity-period “Office-Time” days MONDAY
unp policy validity-period “Office-Time” days MONDAY time-zone CET
unp policy validity-period “Office-Time” hours 9:00 to 17:00
Configure UNP policy validity-period
Example
UNP profile
VLAN ID
Policy List
ACL
QoS
Location
Period

<<<PAGE 385>>>
CONFIGURATION STEPS
Step by Step
policy list list_name type unp [enable | disable]
-> policy list deny_employees type unp enable
-> policy list deny_employees rules deny_ftp_employee
policy list list_name rules rule_name [rule_name2...]
policy condition NoFtp destination ip-port 20-21 ip-protocol 6
policy action deny disposition deny
policy rule deny_ftp_employee condition NoFtp action deny no default-list
Configure UNP policy list
Assigns existing QoS policy rules to the specified QoS policy list 
Example of policy
UNP profile
VLAN ID
Policy List
ACL
QoS
Location
Period

<<<PAGE 386>>>
CONFIGURATION STEPS
Step by Step
-> unp profile employee qos-policy-list deny_employees location-policy ALE-Brest period-policy Office-Time
-> unp profile employee map vlan 20
-> unp profile profile-name qos-policy-list list_name location-policy policy_name period-policy policy_name
-> unp profile profile_name map vlan vlan_id
Configure UNP profile
Example

<<<PAGE 387>>>
CONFIGURATION STEPS
Step by Step
Not valid 
UNP
Classification
Rules
UNP Profile
-> unp port chassis/slot/port 802.1X-
authentication [pass-alternate profile_name]
-> unp port chassis/slot/port mac-
authentication [pass-alternate profile_name]
Configure supplicant device classification policies
Configure mac-authentication device classification policies
Yes
802.1X 
enabled ?
802.1x
Pass 
L2 Authentication 
UNP Selection
Supplicant?
Yes
Same branch as 
802.1x
MAC 
Enabled?
No
No
Yes
No
No Auth
Server Down
UNP Port 
Block
No UNP
Alternate
UNP Profile
Block
Server Down
UNP Profile
Timeout
UNP Profile
RADIUS Filter-Id
Default
UNP Profile
Block
Fail
Classification
Rules
UNP Profile

<<<PAGE 388>>>
ACCESS GUARDIAN -CONFIGURATION STEPS
Step by Step
UNP-Template
MAC authent.
Default
UNP Profile
VLAN
Policy List
AAA Profile
Authentication
Accounting
Alternate
UNP Profile
VLAN
Policy List
Classification
Rules
802.1x
authent.
Parameters
UNP Template Properties
Name
802.1x authentication
802.1x authentication tx-period
802.1x authentication max_req
802.1x authentication supp-timeout
Pass-alternate UNP-profile
Mac-authentication
Mac-authentication pass-alternate
UNP-profile
Allow-eap
Classification
Group-id
AAA-profile
Bypass
Failure-policy
AAA Profile
802.1x authentication
Captive-portal authentication
Mac authentication
Radius authentication/accounting servers
Syslog servers
Specify the configuration parameters that 
could be enabled on the UNP port/linkagg
AAA profiles to define a custom, pre-defined AAA 
configuration that can be applied to a specific set 
of UNP ports or through a Captive Portal profile. 
-> aaa profile ap-1
-> aaa profile ap-1 device-authentication mac rad1 rad2
-> aaa profile ap-1 device-authentication 802.1x rad1 rad2
-> unp port 1/1/5 aaa-profile ap-1
-> unp port 1/2/1-5 aaa-profile ap-1
-> unp linkagg 10 aaa-profile ap-1
-> unp linkagg 2-5 aaa-profile ap-1
-> unp port-template 802.1X-template
-> unp port-template 802.1x-template 802.1x-authentication
-> unp port-template 802.1x-template 802.1x-authentication pass-alternate corporate
-> unp port 2/1/1 port-template 802.1x-template
Example
UNP profile Templates

<<<PAGE 389>>>
CONFIGURATION STEPS
Step by Step
-> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent
Configure a server as a RADIUS server on the switch
Configure the switch “my_radius” for 802.1X device authentication /server accounting
Create the required VLANs
Create the required UNP profile and map the profile to VLAN 10 and 20
Enable UNP on ports that will connect to user devices
Set the default UNP profile on the port
Create an edge template to apply UNP port configuration parameters.
Configure the template and define an alternate UNP profile to use if the RADIUS server 
does not return a UNP profile
Assign the port template to a UNP port
-> unp port-template 802.1x-template 802.1x-authentication
-> unp port-template 802.1x-template 802.1x-authentication pass-alternate corporate
-> aaa accounting 802.1x my_radius
-> aaa authentication 802.1x my_radius
Yes
802.1x
Supplicant?
Yes
UNP Port 
802.1X 
enabled ?
Pass 
Block
No UNP
Alternate
UNP Profile
UNP Profile
RADIUS Filter-Id
Block
Fail
Mac Auth
no
Classification
no
no
Default
UNP Profile
Block
Teacher
-> vlan 10 admin-state enable name vlan10-block
-> vlan 20 admin-state enable name vlan20-corporate
-> unp profile corporate
-> unp profile corporate map vlan 20
-> unp profile def_unp
-> unp profile def_unp map vlan 10
-> unp port 1/1/1 port-type bridge
-> unp port 1/1/1 default-profile def_unp
-> unp port-template 802.1X-template
-> unp port 1/1/1 port-template 802.1x-template

<<<PAGE 390>>>
Display information about ports configured for 802.1X
Display a list of all users (supplicants) for one or more 802.1X ports
Display a list of all non-802.1X users (non-supplicants) learned on one or more 802.1X ports
Display the Access Guardian status of all users learned on 802.1X ports
Displays a list of RADIUS servers configured for MAC based authentication
CONFIGURATION STEPS
Step by Step
show unp port chassis/slot/port config
show unp user port chassis/slot/port
show unp user port chassis/slot/port
show unp user details port chassis/slot/port
show unp user port chassis/slot/port statistics
Monitoring

<<<PAGE 391>>>
Displays information about the global 802.1X configuration on the switch
Displays information about accounting servers configured for 802.1X port-
based network access control
Display the Access Guardian status of all users learned on 802.1X ports
CONFIGURATION STEPS
Step by Step
show aaa device-authentication 802.1x
show aaa accounting 802.1x 
Show unp user
Monitoring

<<<PAGE 392>>>
AUTHENTICATION SERVER CONFIGURATION

<<<PAGE 393>>>
AUTHENTICATION SERVER CONFIGURATION
Step by Step
Configure the RADIUS server to use for device authentication (802.1X, MAC, or Captive Portal)
Enable the MAC authentication session timer to determine the amount of time the user session 
remains active after a successful login (the default time is set to 12 hours).
Example
aaa radius-server server_name host {hostname | ip_address | ipv6_address} [hostname2 | ip_address2 | 
ipv6_address2] {key secret | hash-key hash_secret | prompt-key}[salt salt | hash-salt hash_salt] [retransmit 
retries] [timeout seconds] [auth-port auth_port] [acct-port acct_port] [vrf-name name] [ssl | no ssl]
Parameters
Default
retries
3
seconds
2
auth_port
1812
acct_port
1813
ssl | no ssl
No ssl
-> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent
-> aaa authentication 802.1x my_radius
-> aaa authentication mac my_radius
-> aaa accounting 802.1x my_radius
-> aaa accounting mac my_radius
-> aaa mac session-timeout enable
aaa mac session-timeout enable
Configure Authentication Server

<<<PAGE 394>>>
AUTHENTICATION SERVER CONFIGURATION
Step by Step
Choose the source IP interface used by the application
Example
-> ip service source-ip {Loopback0 | interface-name} [ldap] [tacacs] [radius] [snmp] [sflow] 
[ntp] [swlog] [dns] [telnet] [ftp] [ssh] [tftp] [all]
ip service source-ip loopback0 radius
-> show ip service source-ip
Application           Interface-Name
-----------------+------------------------
tacacs
-
ntp
Loopback0
syslog           
-
ldap-server       
-
radius            
Loopback0
ftp               
-
Choose the source IP interface

<<<PAGE 395>>>
AUTHENTICATION SERVER CONFIGURATION
Step by Step
Users are moved to a specific profile when RADIUS server is not available.
Configures the policy for classifying the device when the authentication server is 
not reachable.
Sets re-authentication time for the device to authenticate again with the RADIUS 
server when it is classified according to the auth-server-down policy.
unp auth-server-down profile1 profile_name
unp auth-server-down-timeout seconds
show unp global configuration
Auth Server Down Profile1 = ag_SrvDownPrf,
Auth Server Down Timeout = 60,
* When authentication server becomes reachable Users are re-authenticated
Manage Authentication server down

<<<PAGE 396>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 397>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Access Guardian 
How to 
✓ Configure the Access Guardian on OmniSwitch 
Contents 
1 
Introduction .................................................................................... 2 
2 
Configuring the Access Guardian on the 6360 VC ......................................... 3 
3 
Managing the Access Guardian feature on the 6360 VC ................................. 4 
3.1. Declaring the RADIUS Server ...................................................................... 4 
3.2. Creating the Policies ............................................................................... 4 
3.3. Creating the Policy Lists ........................................................................... 4 
3.4. Creating the User Network Profiles .............................................................. 5 
3.5. Configuring the User Ports ........................................................................ 5 
3.6. Testing the Configuration ......................................................................... 5 
3.7. Testing the Radius Configuration ................................................................. 6 
3.8. Testing the Access Guardian ...................................................................... 6

<<<PAGE 398>>>
2 
Access Guardian 
 
 1 
Introduction 
During this lab, we will configure the Access Guardian feature on the access switches, the 6360 VC.  
Use ACL rules created in the previous lab and apply it in UNP Profiles.  
 
The authentication of the network users will be done via a RADIUS server. On our infrastructure, the RADIUS 
server is installed on a virtual machine (name: AAA Training Server), and its IP address is 192.168.100.102. 
 
Once authenticated, a Universal Network Profile (UNP) will be applied to the network users. More 
information about the UNP profiles to create is provided in the following pages of this lab.

<<<PAGE 399>>>
3 
Access Guardian 
 
 2 
Configuring the Access Guardian on the 6360 VC 
In the following parts, we will perform the following tasks on the 6360 VC:  
- Declaration of the RADIUS server in the OmniSwitch 
- Configure the User Network Profiles which will be applied to the network users: 
 
USER TYPE 
AUTHENTICATION 
VLAN 
UNP 
POLICY LIST 
Employee 
802.1x 
20 
UNP-employee 
deny_employee 
Contractor 
802.1x 
30 
UNP-contractor 
deny_contractor 
 
 
 
 
Notes: 
@MAC Auth: as there are no MAC addresses configured on the RADIUS server, the user will be blocked from 
accessing the network via a MAC address authentication. 
 
During this lab, we will use the policies (ACLs) on the 6360 VC configured in the ACLs lab, and apply them to 
the employee or contractor once authenticated: 
 
User Type 
VLAN 
Service Grp = 
HTTP 
Service Grp = 
FTP 
Employees 
20 
ALLOW 
DENY 
Contractors 
30 
DENY 
ALLOW

<<<PAGE 400>>>
4 
Access Guardian 
 
 3 
Managing the Access Guardian feature on the 6360 VC 
3.1. 
Declaring the RADIUS Server  
- Declare the RADIUS Server on the 6360-A: 
sw5 (6360-A) -> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent 
sw5 (6360-A) -> aaa device-authentication 802.1x my_radius 
sw5 (6360-A) -> aaa device-authentication mac my_radius 
sw5 (6360-A) - >aaa accounting 802.1x my_radius 
sw5 (6360-A) -> aaa accounting mac my_radius 
sw5 (6360-A) -> ip service source-ip Loopback0 radius 
3.2. 
Creating the Policies  
- We have already created some policies during ACLs lab on the 6560. To check the currently active 
policies:  
sw5 (6360-A) -> show active policy rule 
Rule name                        : deny_ftp_employee 
  Precedence                     = 65535, 
  Condition name                 = ftpfromvlan20, 
  Action name                    = deny 
Rule name                        : deny_http_contractor 
  Precedence                     = 65535, 
  Condition name                 = httpfromvlan30, 
  Action name                    = deny 
- We are going to recreate the rules deny_ftp_employee and deny_http_contractor to have the rules only 
applied for some users associated to an UNP:  
sw5 (6360-A) -> qos flush 
sw5 (6360-A) -> qos apply 
 
sw5 (6360-A) -> show active policy rule 
No active rules 
sw5 (6360-A) -> 
 
sw5 (6360-A) -> policy condition NoFtp destination ip-port 20-21 ip-protocol 6 
sw5 (6360-A) -> policy action deny disposition deny 
sw5 (6360-A) -> policy rule deny_ftp_employee condition NoFtp action deny no default-list 
 
sw5 (6360-A) -> policy condition httpfromvlan30 destination ip-port 80 ip-protocol 6 
sw5 (6360-A) -> policy action deny disposition deny 
sw5 (6360-A) -> policy rule deny_http_contractor condition httpfromvlan30 action deny no default-list 
 
sw5 (6360-A) -> qos apply 
 
OS6360-> show policy rule 
Rule name                        : deny_http_contractor 
  Condition name                 = httpfromvlan30, 
  Action name                    = deny, 
  Default Group                  = no 
 
Rule name                        : deny_employee 
  Condition name                 = NoFtp, 
  Action name                    = deny, 
  Default Group                  = no 
3.3. 
Creating the Policy Lists 
- Create a policy list to deny the FTP access for the employees (VLAN 20):  
sw5 (6360-A) -> policy list deny_employees type unp enable 
sw5 (6360-A) -> policy list deny_employees rules deny_ftp_employee 
 
- Create a policy list to deny the HTTP access for the contractors (VLAN 30):  
sw5 (6360-A) -> policy list deny_contractors type unp enable 
sw5 (6360-A) -> policy list deny_contractors rules deny_http_contractor

<<<PAGE 401>>>
5 
Access Guardian 
 
- Apply the modifications: 
sw5 (6360-A) -> qos apply 
3.4. 
Creating the User Network Profiles 
- Create the UNP edge profiles: 
sw5 (6360-A) -> unp profile UNP-employee 
sw5 (6360-A) -> unp profile UNP-contractor 
sw5 (6360-A) -> unp profile UNP-employee qos-policy-list deny_employees 
sw5 (6360-A) -> unp profile UNP-contractor qos-policy-list deny_contractors 
sw5 (6360-A) -> unp profile UNP-employee map vlan 20 
sw5 (6360-A) -> unp profile UNP-contractor map vlan 30 
 
 
Notes: 
A supplicant user (that seeks to authenticate) is authenticated by the RADIUS Server which sends 
back the UNP profile name as Filter-Id attibutes (UNP-employee or UNP-contractor). 
3.5. 
Configuring the User Ports  
- Configure authentication on port 1/1/1 (Client 5) : 
sw5 (6360-A) -> unp port 1/1/1 port-type bridge 
sw5 (6360-A) -> unp port 1/1/1 802.1x-authentication 
sw5 (6360-A) -> unp port 1/1/1 mac-authentication 
3.6. 
Testing the Configuration 
- To verify the profile configuration for a UNP profile (ex. UNP-contractor): 
sw5 (6360-A) -> show unp profile UNP-contractor 
Profile Name: UNP-contractor 
    Qos Policy      = deny_contractors, 
    Location Policy = -, 
    Period Policy   = -, 
    CP Profile      = -, 
    CP State        = Dis, 
    Authen Flag     = Dis, 
    Mobile Tag      = Dis, 
    SAA Profile     = -, 
    Ingress BW      = -, 
    Egress BW       = -, 
    Ingress Depth   = -, 
    Egress Depth    = -, 
    Inact Interval  = 10, 
    Mac-Mobility    = Dis, 
    Kerberos Auth   = Dis 
 
- To verify the VLAN mapping for each profile, type: 
sw5 (6360-A) -> show unp profile map vlan 
Profile Name                     Vlan 
UNP-employee                     20 
UNP-contractor                   30 
Total Profile Vlan-Map Count: 2

<<<PAGE 402>>>
6 
Access Guardian 
 
3.7. 
Testing the Radius Configuration  
- Check that the RADIUS server is properly configured and reachable: 
-> aaa test-radius-server my_radius type authentication user employee password password 
Testing Radius Server <192.168.100.102/My_radius> 
Access-Challenge from 192.168.100.102 Port 1812 Time: 174 ms 
    Filter-ID = UNP-employee 
Access-Challenge from 192.168.100.102 Port 1812 Time: 16 ms 
    Filter-ID = UNP-employee 
Access-Accept from 192.168.100.102 Port 1812 Time: 18 ms 
Returned Attributes 
    Filter-ID = UNP-employee 
    User Name = employee 
3.8. 
Testing the Access Guardian 
- Open the Client 5 console from vSphere: 
Client 5 
Open the Networks 
Connections and right-click 
on the Pod connection 
 
Click on Properties 
 
Select the Authentication tab 
 
 
 
Tips 
If the Authentication tab is not available, click on the Start button, Run…, type services.msc and 
click Ok. Look for Wired AutoConfig service and start it. Now the Authentication should be

<<<PAGE 403>>>
7 
Access Guardian 
 
available 
 
- Check the box Enable IEEE 
802.1X authentication  
 
- Uncheck the box Cache user 
information for subsequent 
connections to this network 
 
Click on Settings and uncheck 
Validate server certificate. 
 
Keep default authentication 
method (Secured password 
EAP-MSCHAP v2) and click on 
Configure… 
 
Uncheck the box 
Automatically use my 
windows logon name and 
password 
 
Click on OK three times to leave LAN connections properties. 
 
- Reinitialize the port 1/1/1 (where is connected the Client 5): 
sw5 (6360-A) -> unp user flush port 1/1/1 
 
- Disable and re-enable the network interface from client 5. 
 
- You should get a pop-up asking to connect on the network. 
 
 
 
- Logon now with the following credentials: 
User name = employee 
Password = password

<<<PAGE 404>>>
8 
Access Guardian 
 
- Check the user status: 
sw5 (6360-A) -> show unp user 
                                               User 
Port    Username      Mac address       IP              Vlan Profile        Type         Status 
-------+-------------+-----------------+---------------+----+-------------+------------+----------- 
1/1/1   employee      00:50:56:90:f7:ad 192.168.20.86   20   UNP-employee   Bridge       Active 
 
sw5 (6360-A) -> show unp user status 
Port    Mac address       Profile Name    Source  Type    Status        Role Name      Role Source   CP Kerberos Redirect 
Access 
-------+-----------------+---------------+-------+------+-------------+---------------+-------------+--+--------+-------- 
1/1/1   00:50:56:90:f7:ad UNP-employee    Radius  802.1x Authenticated deny_employees  L2-Profile    N  N        Y        
 
sw5 (6360-A) -> show unp user details 
Port: 1/1/1 
    MAC-Address: 00:50:56:90:f7:ad 
      SAP                             = -, 
      Service ID                      = 0, 
      VNID                            = 0 ( 0. 0. 0), 
      VPNID                           = 0 ( 0. 0. 0), 
      ISID                            = 0, 
      Access Timestamp                = 08/01/2015 03:00:21, 
      User Name                       = employee, 
      IP-Address                      = 192.168.20.86, 
      Vlan                            = 20, 
      Authentication Type             = 802.1x, 
      Authentication Status           = Authenticated, 
      Authentication Failure Reason   = -, 
      Authentication Retry Count      = 0, 
      Authentication Server IP Used   = 192.168.100.102, 
      Authentication Server Used      = my_radius, 
      Server Reply-Message            = -, 
      Profile                         = UNP-employee, 
      Profile Source                  = Auth - Pass - Server UNP, 
      Profile From Auth Server        = UNP-employee, 
      Session Timeout                 = 0, 
      Classification Profile Rule     = -, 
      Role                            = deny_employees, 
      Role Source                     = L2-Profile, 
      User Role Rule                  = -, 
      Restricted Access               = No, 
      Location Policy Status          = -, 
      Time Policy Status              = -, 
      QMR Status                      = Passed, 
      Redirect Url                    = -, 
      SIP Call Type                   = Not in a call, 
      ---                             = - 
 
- Reinitialize the port 1/1/1 (where is connected the Client 5): 
sw5 (6360-A) -> unp user flush port 1/1/1 
 
- Disable and re-enable the network interface from client 5. 
- Logon now with the following credentials: 
User name = contractor 
Password = password 
 
- Check the user status: 
sw5 (6360-A) -> show unp user 
                                               User 
Port    Username      Mac address       IP              Vlan Profile                Type         Status 
-------+-------------+-----------------+---------------+----+----------------------+------------+--------- 
1/1/1   contractor    00:50:56:90:f7:ad 192.168.30.81   30   UNP-contractor         Bridge       Active 
 
sw5 (6360-A) -> show unp user status 
Port    Mac address       Profile Name   Source  Type    Status        Role Name         Role Source CP Kerberos Redirect 
Access 
-------+-----------------+--------------+-------+-------+-------------+-----------------+--+--+--------+--------+-------- 
1/1/1   00:50:56:90:f7:ad UNP-contractor  Radius  802.1x Authenticated deny_contractors  L2-Profile    N  N        Y

<<<PAGE 405>>>
9 
Access Guardian 
 
 
sw5 (6360-A) -> show unp user details 
Port: 1/1/1 
    MAC-Address: 00:50:56:90:f7:ad 
      SAP                             = -, 
      Service ID                      = 0, 
      VNID                            = 0 ( 0. 0. 0), 
      VPNID                           = 0 ( 0. 0. 0), 
      ISID                            = 0, 
      Access Timestamp                = 08/01/2015 03:14:52, 
      User Name                       = contractor, 
      IP-Address                      = 192.168.30.81, 
      Vlan                            = 30, 
      Authentication Type             = 802.1x, 
      Authentication Status           = Authenticated, 
      Authentication Failure Reason   = -, 
      Authentication Retry Count      = 0, 
      Authentication Server IP Used   = 192.168.100.102, 
      Authentication Server Used      = my_radius, 
      Server Reply-Message            = -, 
      Profile                         = UNP-contractor, 
      Profile Source                  = Auth - Pass - Server UNP, 
      Profile From Auth Server        = UNP-contractor, 
      Session Timeout                 = 0, 
      Classification Profile Rule     = -, 
      Role                            = deny_contractors, 
      Role Source                     = L2-Profile, 
      User Role Rule                  = -, 
      Restricted Access               = No, 
      Location Policy Status          = -, 
      Time Policy Status              = -, 
      QMR Status                      = Passed, 
      Redirect Url                    = -, 
      SIP Call Type                   = Not in a call, 
      SIP Media Type                  = None, 
      Applications                    = None, 
      Encap Value                     = - 
- On client 5 
- Go back to the network connection Pod properties, then disable 802.1x on the network interface (from 
authentication tab of the LAN connection properties)  
 
 
 
- Reinitialize the port 1/1/1 (where is connected the Client 5): 
 
sw5 (6360-A) -> unp user flush port 1/1/1 
 
 
- Disable and re-enable the network interface from client 5. 
 
- On the switch check the user status: 
 
sw5 (6360-A) -> show unp user 
                                               User

<<<PAGE 406>>>
10 
Access Guardian 
 
Port    Username             Mac address       IP (V4/V6)                Vlan Profile  Type         Status 
-------+--------------------+-----------------+-------------------+----+---------------+------------+-----
------ 
1/1/1   00:50:56:90:22:3c    00:50:56:90:22:3c 192.168.20.105             20   -       Bridge       Block 
 
 
- As there are not any MAC addresses configured on the RADIUS server, then the user is blocked from 
accessing the network. 
 
- Save the configuration 
 
sw5 (6360-A) -> write memory flash-synchro

<<<PAGE 407>>>
L I N K  L AY E R  D I S C O V E RY P R O TO C O L S  ( L L D P )
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 408>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe how the Link Layer Discovery Protocols 
(LLDP) works
• Enable LLDP-MED

<<<PAGE 409>>>
OVERVIEW
Goal
• IEEE 802.1AB – Link Layer Discovery Protocol (LLDP)
• Accurate physical topology and device inventory simplifies management and maintenance 
L2 discovery protocol
• Exchange information with neighboring devices to build a database of adjacent devices
• Enabled by default on the OmniSwitches
xxxx
Switch
1/3
xxxx
PC
1/2
xxxx
IP-phone
1/1
info
device
port
xxxx
Switch
1/3
xxxx
PC
1/2
xxxx
IP-phone
1/1
info
device
port
xxxx
IP-PBX
2/13
xxxx
IP-Phone
2/12
xxxx
IP-Phone
2/1
xxxx
Switch
2/22
info
device
port
xxxx
IP-PBX
2/13
xxxx
IP-Phone
2/12
xxxx
IP-Phone
2/1
xxxx
Switch
2/22
info
device
port
I’m a Switch
I’m a Switch
I’m a Switch
I’m a Switch
I’m a Switch
I’m a PC
I’m a PC
I’m an IP-Phone
I’m an IP-Phone
I’m a PBX
I’m a Switch
I’m a Switch

<<<PAGE 410>>>
PROTOCOL DATA UNIT (LLDP-PDU)
Ethernet Header
Link Layer Discovery Protocol Protocol Data Unit (LLDP-PDU)
Standard: IEEE 802.1AB
01:80:c2:00:00:0e
Port mac 
addr.
88:cc
Destination             Source          Ethertype
addr.                   addr.          For LLDP
Chassis ID
TLV
Port ID
TLV
Time To
Live TLV
Optional
TLV
…
Optional
TLV
End Of
LLDPPDU TLV
M                   M
M
O                                 O
M
TLV
Type
TLV information
string length
TLV information string
Basic Type Length Value (TLV) format
7 bits              9 bits                                         0 – 511 octets
TLV header
LLDP PDUs
Extensions optional fields
• 802.1: Vlan name, port vlan
• 802.3: MAC Phy
• MED: Power and Capability
• Inventory Management
• Network Policy

<<<PAGE 411>>>
MEDIA ENDPOINT DEVICES (LLDP-MED)
NETWORK
POLICY
LOCATION ID
EXTENDED
POWER-VIA-MDI
INVENTORY

<<<PAGE 412>>>
CONFIGURATION
• Enabling LLDP PDU flow on a port, slot, or all ports on a switch
• Enabling LLDP notification status
• Displaying LLDP information
-> lldp {slot/port | slot | chassis} lldpdu {tx | rx | tx-and-rx | disable}
-> lldp {slot/port | slot | chassis} notification {enable | disable}
-> show lldp port 1/1/3 remote-system
Remote LLDP nearest-bridge Agents on Local Port 1/1/3:
Chassis e8:e7:32:f6:15:81, Port 1003:
Remote ID                   = 4,
Chassis Subtype             = 4 (MAC Address),
Port Subtype                = 7 (Locally assigned),
Port Description            = Alcatel-Lucent OS6860 GNI 1/1/3,
System Name                 = (null),
System Description          = (null),
Capabilities Supported      = Bridge Router,
Capabilities Enabled        = Bridge Router

<<<PAGE 413>>>
MONITORING
Displaying LLDP information
-> show lldp system-statistics
-> show lldp [slot|slot/port] statistics
-> show lldp local-system
-> show lldp [slot/port | slot] local-port
-> show lldp local-management-address
-> show lldp config
-> show lldp 1/9 config
----------+-------------------------------------------+---------------------+----------
|  Admin   |  Notify  |  Std TLV |   Mgmt
|  802.1   |  802.3   |   MED
Slot/Port|  Status  |   Trap   |   Mask   | Address  |   TLV    |   Mask   |   Mask
----------+----------+----------+----------+----------+----------+----------+----------
1/9      Rx + Tx
Enabled      0xf0     Enabled    Enabled
0x80       0xd0

<<<PAGE 414>>>
IP PHONE
(LLDP NETWORK POLICY TLV/MOBILE TAG)

<<<PAGE 415>>>
LLDP-MED
• Provides VoIP-specific extensions to base LLDP protocol
• TLVs (Type, Length, Value) for
• Device location discovery to allow creation
of location databases, including the support
for Emergency Call Service
• LAN policy discovery
(VLAN, Layer 2 priority, Layer 3 QoS)
• Extended and automated power management
for Power over Ethernet devices
• Inventory management
IP Phone
1
2
Admin
Policy: Defin
Tagged: Yes
VLAN ID :10
L2 priority:6
DSCP: 46
Policy:
Unkn
Tagged:
No
VLAN ID:
0
L2 priority:
5
DSCP:
46

<<<PAGE 416>>>
LLDP-MED
Mobile Tag versus 802.1Q Tag
Mobile Tag
802.1Q Tag
Allows mobile ports to receive 802.1Q tagged 
packets
Not supported on mobile ports
Enabled on the VLAN that will receive tagged 
mobile port traffic
Enabled on fixed ports; tags port traffic for 
destination VLAN
Triggers dynamic assignment of tagged mobile 
port traffic to one or more VLANs
Statically assigns (tags) fixed ports to one or 
more VLANs

<<<PAGE 417>>>
LLDP NETWORK POLICY TLV/MOBILE TAG
OS6860-A
1/1/20
1/1/4
7
151.1.1.0
151.1.1.0
IP Phone 31001
(OS6860-A) -> vlan 151
(OS6860-A) -> unp profile "voip-temp" mobile-tag
(OS6860-A) -> unp profile "voip-temp" map vlan 151
(OS6860-A) -> unp port 1/1/20 port-type bridge
(OS6860-A) -> unp port 1/1/20 direction both classification trust-tag dynamic-service none
(OS6860-A) -> unp classification lldp med-endpoint ip-phone  profile1 "voip-temp"
(OS6860-A) -> lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46
(OS6860-A) -> lldp chassis med network-policy 1
(OS6860-A) -> lldp nearest-bridge port 1/1/20 tlv med network-policy enable
(OS6860-A) -> lldp nearest-bridge port 1/1/20 tlv med capability enable
Switch send a LLDP Frame 
46
5

<<<PAGE 418>>>
LLDP NETWORK POLICIES
• Specifying whether or not LLDP-MED TLVs are included in transmitted LLDPDUs
• Configuring a local Network Policy on the switch for a specific application type
• Associating an existing network policy to a port, slot, or chassis
-> lldp {slot/port | slot | chassis} tlv med {power | capability | network policy} 
{enable | disable}
-> lldp network-policy policy_id application { voice | voice-signaling | guest-voice 
| guest-voice-signaling | softphone-voice | video-conferencing | streaming-video | 
video-signaling } vlan { untagged | priority-tag | vlan-id } l2-priority 802.1p_value
dscp dscp_value
-> lldp {slot/port | slot | chassis} med network-policy policy_id

<<<PAGE 419>>>
EXAMPLE – LLDP-MED
Display the LLDP information of the equipment(s) connected to the switch
-> show lldp remote-system
Remote LLDP Agents on Local Slot/Port 1/14:
Chassis 80:4e:53:c6:00:00, Port 00:80:9f:8e:a4:ab:
Remote ID                   
= 3,
Chassis Subtype             
= 4 (MAC Address),
Port Subtype                
= 3 (MAC address),
Port Description            
= (null),
System Name                 
= (null),
System Description          
= (null),
Capabilities Supported      
= Telephone,
Capabilities Enabled        
= Telephone,
MED Device Type             
= Endpoint Class III,
MED Capabilities            
= Capabilities | Power via MDI-PD(33),
MED Extension TLVs Present  
= Network Policy| Inventory,
MED Power Type              
= PD Device,
MED Power Source            
= PSE,
MED Power Priority          
= Low,
MED Power Value             
= 5.6 W,
Remote port MAC/PHY AutoNeg
= Supported Enabled Capability 0xc036,
Mau Type                   
= 1000BaseTFD - Four-pair Category 5 UTP full duplex mode
-> show lldp remote-system med inventory
Remote LLDP Agents on Local Slot/Port 1/14:
Chassis 80:4e:53:c6:00:00, Port 00:80:9f:8e:a4:ab:
Remote ID                = 3,
Hardware Revision        = "3GV23021JCDA060921",
Firmware Revision        = "NOE 4.20.60",
Software Revision        = "NOE 4.20.60",
Serial Number            = "FCN00913901069",
Manufacturer Name        = "Alcatel-Lucent Enterprise",
Model Name               = "IP Touch 8068",
Asset Id                 = "00:80:9f:8e:a4:ab"

<<<PAGE 420>>>
LLDP NETWORK POLICY TLV/MOBILE TAG
(OS6860-A) -> vlan 151
(OS6860-A) -> unp profile "voip-temp" mobile-tag
(OS6860-A) -> unp profile "voip-temp" map vlan 151
(OS6860-A) -> unp port 1/1/20 port-type bridge
(OS6860-A) -> unp port 1/1/20 direction both classification trust-tag dynamic-service none
(OS6860-A) -> unp classification lldp med-endpoint ip-phone  profile1 "voip-temp"
(OS6860-A) -> lldp network-policy 1 application voice vlan 151 l2-priority 7 dscp 14
(OS6860-A) -> lldp chassis med network-policy 1
(OS6860-A) -> lldp nearest-bridge port 1/1/20 tlv med network-policy enable
(OS6860-A) -> lldp nearest-bridge port 1/1/20 tlv med capability enable
IP phone send Multicast LLPD frame
Switch send a LLDP Frame 
OS6860-A
1/1/20
1/1/4
7
151.1.1.0
151.1.1.0
IP Phone 31001
1
2

<<<PAGE 421>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 422>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Link Layer Discovery Protocol 
How to 
✓ This lab is designed to familiarize you with the Link Layer Discovery 
Protocol (LLDP). 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configure LLDP ................................................................................ 2

<<<PAGE 423>>>
2 
Link Layer Discovery Protocol 
 
 1 
Topology 
Link Layer Discovery Protocol (LLDP) is a standard that provides a solution for the configuration issues 
caused by expanding networks. LLDP supports the network management software used for complete 
network management. LLDP is implemented as per the IEEE 802.1AB standard. 
 
The exchanged information, passed as LLDPDU, is in TLV (Type, Length, Value) format. The information 
available to the network management software must be as new as possible; hence, remote device 
information is periodically updated. 
 
 
Notes 
LLDP is enabled by default in reception and transmission 
 
 
 2 
Configure LLDP 
- To control per port notification status about a change in a remote device associated to a port, use the 
following command: 
sw5 (6360-A) -> lldp port 1/1/3 notification enable 
sw5 (6360-A) -> lldp port 2/1/3 notification enable 
sw5 (6360-A) -> lldp port 1/1/4 notification enable 
sw5 (6360-A) -> lldp port 2/1/4 notification enable 
 
 
sw7 (6870-A) -> lldp port 1/1/3 notification enable 
sw7 (6870-A) -> lldp port 1/1/4 notification enable 
sw7 (6870-A) -> lldp port 1/1/23 notification enable 
sw7 (6870-A) -> lldp port 1/1/24 notification enable 
 
sw8 (6860-B) -> lldp port 1/1/3 notification enable 
sw8 (6860-B) -> lldp port 1/1/4 notification enable 
sw8 (6860-B) -> lldp port 1/1/23 notification enable 
sw8 (6860-B) -> lldp port 1/1/24 notification enable 
 
 
Tips 
LLDP is configured at port level (or NI or chassis), but not at linkagg level. 
 
 
 
- To control per port management TLV to be incorporated in the LLDPDUs, use the following command

<<<PAGE 424>>>
3 
Link Layer Discovery Protocol 
 
sw5 (6360-A) -> lldp port 1/1/3 tlv management port-description enable 
sw5 (6360-A) -> lldp  port 2/1/3 tlv management port-description enable 
sw5 (6360-A) -> lldp port 1/1/4 tlv management port-description enable 
sw5 (6360-A) -> lldp  port 2/1/4 tlv management port-description enable 
 
sw7 (6870-A) -> lldp port 1/1/3 tlv management port-description enable 
sw7 (6870-A) -> lldp port 1/1/4 tlv management port-description enable 
sw7 (6870-A) -> lldp port 1/1/23 tlv management port-description enable 
sw7 (6870-A) -> lldp port 1/1/24 tlv management port-description enable 
 
sw8 (6860-B) -> lldp port 1/1/3 tlv management port-description enable 
sw8 (6860-B) -> lldp port 1/1/4 tlv management port-description enable 
sw8 (6860-B) -> lldp port 1/1/23 tlv management port-description enable 
sw8 (6860-B) -> lldp port 1/1/24 tlv management port-description enable 
 
 
- Verify the LLDP per port statistics by entering the following command: 
sw7 (6870-A) -> show lldp statistics 
  Chas/     LLDPDU      LLDPDU      LLDPDU     LLDPDU     LLDPDU      TLV       TLV       Device 
 Slot/Port    Tx        TxLenErr      Rx       Errors    Discards    Unknown   Discards   Ageouts 
----------+----------+----------+----------+----------+----------+----------+----------+---------- 
  1/1/1     65         0          0          0          0          0          0          0 
  1/1/3     65         0          65         0          0          0          0          0 
  1/1/4     66         0          64         0          0          0          0          0 
  1/1/5     65         0          65         0          0          0          0          0 
  1/1/6     65         0          65         0          0          0          0          0 
  1/1/23    65         0          64         0          0          0          0          0 
  1/1/24    64         0          63         0          0          0          0          0 
- To verify the remote system information, use the following command: 
sw5 (6360-A) -> show lldp remote-system 
 
Remote LLDP nearest-bridge Agents on Local Port 1/1/3: 
 
    Chassis e8:e7:32:f6:15:81, Port 1003: 
      Remote ID                   = 4, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/3, 
      System Name                 = (null), 
      System Description          = (null), 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router 
 
Remote LLDP nearest-bridge Agents on Local Port 1/1/4: 
 
    Chassis e8:e7:32:fc:23:b3, Port 1004: 
      Remote ID                   = 7, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/4, 
      System Name                 = (null), 
      System Description          = (null), 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router 
 
Remote LLDP nearest-bridge Agents on Local Port 2/1/3: 
 
    Chassis e8:e7:32:fc:23:b3, Port 1003: 
      Remote ID                   = 10, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/3, 
      System Name                 = (null), 
      System Description          = (null), 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router 
 
Remote LLDP nearest-bridge Agents on Local Port 2/1/4: 
 
    Chassis e8:e7:32:f6:15:81, Port 1004:

<<<PAGE 425>>>
4 
Link Layer Discovery Protocol 
 
      Remote ID                   = 4, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/4, 
      System Name                 = (null), 
      System Description          = (null), 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router 
 
[truncated] 
 
- To display local system information, type the following command:  
sw7 (6870-A) -> show lldp local-system 
Local LLDP Agent System Data: 
  Chassis ID Subtype           = 4 (MAC Address), 
  Chassis ID                   = e8:e7:32:f6:15:81, 
  System Name                  = Pod20sw7, 
  System Description           = Alcatel-Lucent Enterprise OS6860E-P24 8.7.98.R03 GA, July 05, 2021., 
  Capabilities Supported       = Bridge Router, 
  Capabilities Enabled         = Bridge Router, 
  LLDPDU Transmit Interval     = 30 seconds, 
  TTL Hold Multiplier          = 4, 
  Reintialization Delay        = 2 seconds, 
  Maximum Transmit Credit      = 5 , 
  LLDPDUs in Fast Transmission = 4 , 
  LLDPDU Fast Transmit Interval= 1 , 
  MIB Notification Interval    = 5 seconds, 
  LLDP Nearest-edge Mode       = Disabled, 
  Management Address Type      = 1 (IPv4), 
  Management IP Address        = 192.168.254.7, 
- The commands below specify the switch to control per port management TLVs to be incorporated in the 
LLDPDUs. This will allow to have additional information such as system description, name, capabilities and 
management IP address of neighbouring devices.

<<<PAGE 426>>>
5 
Link Layer Discovery Protocol 
 
- Type the following on all 3 switches: 
all -> lldp chassis tlv management system-name enable 
all -> lldp chassis tlv management system-description enable 
all -> lldp chassis tlv management system-capabilities enable 
all -> lldp chassis tlv management management-address enable 
- To display remote system information, enter the following command: 
sw5 (6360-A) -> show lldp remote-system 
 
Remote LLDP nearest-bridge Agents on Local Port 1/1/3: 
 
    Chassis e8:e7:32:f6:15:81, Port 1003: 
      Remote ID                   = 4, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/3, 
      System Name                 = Pod20sw7, 
      System Description          = Alcatel-Lucent Enterprise OS6860E-P24 8.7.98.R03 GA, July 05, 2021., 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router, 
      Management IP Address       = 192.168.254.7 
 
Remote LLDP nearest-bridge Agents on Local Port 1/1/4: 
 
    Chassis e8:e7:32:fc:23:b3, Port 1004: 
      Remote ID                   = 7, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/4, 
      System Name                 = Pod20sw8, 
      System Description          = Alcatel-Lucent Enterprise OS6860-24 8.7.98.R03 GA, July 05, 2021., 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router, 
      Management IP Address       = 192.168.254.8 
 
Remote LLDP nearest-bridge Agents on Local Port 2/1/3: 
 
    Chassis e8:e7:32:fc:23:b3, Port 1003: 
      Remote ID                   = 10, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/3, 
      System Name                 = Pod20sw8, 
      System Description          = Alcatel-Lucent Enterprise OS6860-24 8.7.98.R03 GA, July 05, 2021., 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router, 
      Management IP Address       = 192.168.254.8 
 
Remote LLDP nearest-bridge Agents on Local Port 2/1/4: 
 
    Chassis e8:e7:32:f6:15:81, Port 1004: 
      Remote ID                   = 4, 
      Chassis Subtype             = 4 (MAC Address), 
      Port Subtype                = 7 (Locally assigned), 
      Port Description            = Alcatel-Lucent OS6860 GNI 1/1/4, 
      System Name                 = Pod20sw7, 
      System Description          = Alcatel-Lucent Enterprise OS6860E-P24 8.7.98.R03 GA, July 05, 2021., 
      Capabilities Supported      = Bridge Router, 
      Capabilities Enabled        = Bridge Router, 
      Management IP Address       = 192.168.254.7 
 
[truncated] 
 
 
 
 
Tips 
Compare the output of this command with the same command that was entered before

<<<PAGE 427>>>
POWER OVER ETHERNET (POE)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 428>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Setup the Power over Ethernet (PoE) feature
• Monitor the Power over Ethernet (PoE) 
information

<<<PAGE 429>>>
INTRODUCTION
• The PoE (Power over Ethernet) passes a voltage 
in addition to the data on an ethernet cable.
•
With PoE
•
No power supply, no power cable
•
Devices: AP, IP phones, cameras… 
•
Without PoE 
•
Power injector, or power cable needed
With POE
Without POE
Data
Power
Data
External Power Supply

<<<PAGE 430>>>
MONITORING THE POE STATUS - LEDS
• Objective
• Monitor the PoE status from the LEDs on the OmniSwitches front panel
• Operation
• 1 LED per port
• 2 different colors to visualize easily the PoE status on each port
Amber
•
Device connected
•
Device powered with PoE
Green
•
Device connected
•
Device not powered with PoE

<<<PAGE 431>>>
POE POWER MANAGEMENT
• Fast PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870
• Note: OS6360 – P10A does not support FPoE
• Used to provide PoE power a few seconds after powering up the chassis 
• Allows the chassis to immediately provide PoE power to any connected device after powering up 
without waiting for the chassis to finish booting
• Fast PoE requires an upgraded FPGA/CPLD, refer to the release note. 
-> lanpower fpoe {enable | disable}

<<<PAGE 432>>>
POE POWER MANAGEMENT
• Perpetual PoE : 2X60, 6360, 6860E, 6860N, 6865, 6870
• Note: OS6360 – P10A does not support PPoE.
• Provides uninterrupted power to the connected device (PD) even when the switch is restarting or 
recharging, such as during a soft restart
• Perpetual PoE requires an upgraded FPGA/CPLD, refer to the release note
-> lanpower ppoe {enable | disable}

<<<PAGE 433>>>
ENERGY EFFICIENT ETHERNET (EEE) – IEEE 802.3AZ 
STANDARD
• Protocol to allow chipset to go to a low power 
mode state when idle (i.e. no traffic sent)
• Compatibles with OmniSwitches models except
« U » models (optical fiber models).
• EEE is only applicable to OmniSwitch copper 
ports operating at 100/1000 Mbps speed
• Switch compatibility refer to specifications 
guide 
EEE activé
EEE activé

<<<PAGE 434>>>
POWER OVER ETHERNET
• OmniSwitch switches with PoE capabilities can provide power to a large range of 
equipments (ex: IP phones, access points, PTZ cameras,…)
• PoE priority and configurable maximum power per port for power allocation 
• Dynamic PoE Allocation: Provide only the amount of power needed by powered devices (PD) up to 
the total energy budget for the most efficient power consumption possible
Property
802.3af
(802.3at Type 1) "PoE"
802.3at Type 2 
"PoE+"
802.3bt Type 3 
"4PPoE"]/"PoE++"
802.3bt Type 4
"4PPoE"/"PoE++"
Power available at the PD
12.95 W
25.50 W
51 W
71 W
Maximum power delivered by the EPS
15.40 W
30.0 W
60 W
100 W
Maximum current Imax
350 mA
600 mA
600 mA per pair
960 mA per pair
Energy Management
Three power class levels 
(1-3)
Four power class 
levels (1-4)
Six power class levels 
(1-6) 
Eight power class levels 
(1-8)
Supported cabling
Category 3 and
Category 5
Category 5
Category 5
Category 5

<<<PAGE 435>>>
POWER SUPPLIES SPECIFICATIONS
• PoE budget is different on each OmniSwitch model, refer to specification guide or 
datasheet.
• OmniSwitches models compatibles with the PoE protocol have the « P » letter in their
reference.
• Examples of specifications

<<<PAGE 436>>>
POE MANAGEMENT ON AOS R8

<<<PAGE 437>>>
POE MANAGEMENT
• Displays the power supplies hardware information and current status:
• Setting the PoE Operational Status
• Reactivating / Deactivating power to one port
• Setting the maximum amount of inline power
-> show powersupply
Total     PS
Chassis/PS    Power    Type     Status    Location
-----------+---------+--------+--------+-----------
1/1         920       AC       UP       Internal
Total 920
-> lanpower slot 1/1 service start
-> lanpower port 1/1/1 admin-state enable
-> lanpower port 1/1/24 power 18000
-> lanpower slot 1/1 maxpower 400
for one port (in mW)
for a slot (in W)

<<<PAGE 438>>>
POE MANAGEMENT
• Setting the PoE Operational Status on a Port
• Disabled by default
• Setting Port Priority Levels (Low, High, Critical)
• Default priority level for a port is low
• Low: In the event of a power management issue, inline power to low-priority ports is interrupted 
first 
• High: This value is used for port(s) that have important, but not mission-critical, devices attached. 
If other ports in the chassis have been configured as critical, inline power to high-priority ports is 
given second priority.
• Critical: In the event of a power management issue, inline power to critical ports is maintained as 
long as possible 
-> lanpower port 1/1/1 admin-state enable
-> lanpower port 1/1/6 priority critical

<<<PAGE 439>>>
POE MANAGEMENT
• Setting the Capacitor Detection Method
• Not compatible with IEEE specification 802.3af
• It should only be enabled to support legacy IP phones
• Setting Priority Disconnect Status
• Used by the system software in determining whether an incoming PD will be granted or denied 
power when there are too few watts remaining in the PoE power budget for an additional device
-> lanpower slot 1/1 capacitor-detection enable
-> lanpower slot 1/1 priority-disconnect enable

<<<PAGE 440>>>
POE MONITORING
-> show lanpower slot 1/1
Port Maximum(mW) Actual Used(mW)   Status    Priority  On/Off   Class
----+-----------+---------------+-----------+---------+-------+--------
1     60000        12500       Powered On     Low      ON       *
2     60000         1800       Powered On     Low      ON       *
6     60000         3500       Powered On     Low      ON       *
7     60000         9800       Powered On     Low      ON       *
8     30000        25000       Powered On     Low      ON       *
--------------------------------------------------------------------
15     30000            0       Powered Off    Low      OFF
16     30000            0       Powered Off    Low      OFF
17     30000            0       Searching      Low      ON
--------------------------------------------------------------------
23     30000            0       Searching      Low      ON
24     30000            0       Searching      Low      ON
ChassisId 1 Slot 1 Max Watts 450
56.5 Watts Actual Power Consumed
450 Watts Total Power Budget Used
393,5 Watts Total Power Budget Available
1 Power Supply Available
BPS power: Not Available

<<<PAGE 441>>>
POE POWER MANAGEMENT
• Delayed-feature – 6360, 6560, 6465 and 6870
• This feature is used to introduce a delay in lanpower on system bootup.This delay is used 
to start a lanpower after some specific delay to leave some time for system stability.
• To enable Delayed – start feature with specific delay value
• To disable the Delayed- start feature
• To display the delayed-start configurations
-> lanpower slot 1/1 delayed-start enable seconds <num>
->lanpower slot 1/1 delayed-start disable
->show lanpower slot <chassis/slot> / all  delayed-start
<num> - specific delay value in seconds in multiples of 5. Value should be within 120 to 600 seconds
Notes 
• Start the lanpower service before enabling the 
delay start feature.  
• It is mandatory to do write memory to reflect this 
command on bootup. 
• Lanpower service starts after the delay timer 
expiry
• User can force stop the delay timer by applying 
lanpower service stop command on boot while 
on the period of delay-timer is activated
• Fpoe and Ppoe is not supported on enabling this 
feature.
On boot while delayed lanpower timer is running, status in “Show lanpower slot </>/all status” is updated 
with “Delayed” with time

<<<PAGE 442>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 443>>>
CONSOLE CONNECTIONS
ALE NETWORK PRODUCTS

<<<PAGE 444>>>
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

<<<PAGE 445>>>
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

<<<PAGE 446>>>
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

<<<PAGE 447>>>
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

<<<PAGE 448>>>
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

<<<PAGE 449>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 450>>>
UPGRADE SOFTWARE IMAGE
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 451>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe how to upgrade a Software image on a 
switch

<<<PAGE 452>>>
U p g r a d e  t h e  i m a g e  f i l e
UPGRADE SOFTWARE IMAGE
Step by Step
F T P  t h e  U p g r a d e  F i l e s  t o  t h e  S w i t c h
D o w n l o a d  t h e  U p g r a d e  F i l e s
V e r i f y t h e  S o f t w a r e  U p g r a d e
C e r t i f y t h e  S o f t w a r e  U p g r a d e
U p g r a d e  u b o o t a n d / o r  F G PA  i f  m a n d a t o r y
A n a l y s e  R e q u i r e m e n t s o n  t h e  r e l e a s e  n o t e

<<<PAGE 453>>>
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

<<<PAGE 454>>>
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

<<<PAGE 455>>>
Display version installed
Display the version running in CMM
UPGRADE SOFTWARE IMAGE
Step by Step
Note: If there are any issues after upgrading the switch can be rolled back to the previous certified version
U p g r a d e  t h e  i m a g e  f i l e
V e r i f y t h e  S o f t w a r e  U p g r a d e

<<<PAGE 456>>>
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

<<<PAGE 457>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 458>>>
I N T E L L I G E N T FA B R I C
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 459>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the auto fabric feature
• Mount automatically a Virtual Chassis
• Mount automatically a LACP
• Automate the Routing, SPB, MVRP

<<<PAGE 460>>>
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

<<<PAGE 461>>>
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

<<<PAGE 462>>>
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

<<<PAGE 463>>>
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

<<<PAGE 464>>>
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

<<<PAGE 465>>>
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

<<<PAGE 466>>>
INTELLIGENT FABRIC  - AUTOMATIC FABRIC PROTOCOLS 
3- Auto-LACP 
4- Auto-Routing
5- Auto-SPB Fabric
6- Auto-Network Profiling 
7- Auto-MVRP

<<<PAGE 467>>>
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

<<<PAGE 468>>>
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

<<<PAGE 469>>>
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

<<<PAGE 470>>>
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

<<<PAGE 471>>>
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

<<<PAGE 472>>>
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

<<<PAGE 473>>>
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

<<<PAGE 474>>>
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

<<<PAGE 475>>>
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

<<<PAGE 476>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 477>>>
OVERVIEW AND BASIC SET-UP
FLEET SUPERVISION
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 478>>>
LESSON SUMMARY
✓Overview
• Explain the principles of Fleet Supervision
• Discover the application
✓Basic set-up
• Learn how-to set up a fleet supervision 
account with OV 2500, OV Cirrus or a list of 
devices

<<<PAGE 479>>>
OVERVIEW

<<<PAGE 480>>>
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

<<<PAGE 481>>>
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

<<<PAGE 482>>>
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

<<<PAGE 483>>>
GRAPHS
Search models
•
Select and graph of top 10 models
•
Display of running software versions

<<<PAGE 484>>>
BASIC SET-UP

<<<PAGE 485>>>
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

<<<PAGE 486>>>
ADDING A MANAGEMENT SYSTEM
• Go to « Management System » and click on « Create Management System »
• Then depending on which management system you choose, follow the steps in the next 
slide to gather the appropriate information.

<<<PAGE 487>>>
HOW TO DECLARE OV 2500
• Declare your OV 2500 and use your own records
• Specifying your OV2500 ID 
• Fleet will pull device inventory from OV2500 backend. 
• Refer to Administration -> Preferences -> System Settings -> Fleet Supervision for OV2500 ID and observing 
the sync status of inventory to OV backend

<<<PAGE 488>>>
HOW TO DECLARE OV CIRRUS 4.X
• To declare an OV Cirrus 4.X in Fleet supervision, you will need
• The URL of your Cirrus 4.X instance: e.g. https://customer1.ov.ovcirrus.com/
• The API Key of your Cirrus 4.X instance, found under Security > External Apps:

<<<PAGE 489>>>
HOW TO DECLARE OV CIRRUS (10.5.X AND UPWARDS)
• To declare an OV Cirrus in Fleet supervision, you will need:
• The URL of your OV Cirrus instance, and its Organization ID
• The Application ID and Application secret of your Cirrus instance, found in Applications, under your account:
1
2
2
1
2

<<<PAGE 490>>>
HOW TO DECLARE DEVICES MANUALLY IN FLEET
• Last option when your devices are not managed by any OmniVista, is to import your device 
list directly in Fleet Supervision, through a CSV or XLSX file

<<<PAGE 491>>>
TAKEAWAY
• Watch the Fleet Supervision videos playlist to get a more thorough view on the application

<<<PAGE 492>>>
QUIZ
Quiz
Click the Quiz button to edit this object

<<<PAGE 493>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 494>>>
CLASSROOM SESSION 
OR VIRTUAL CLASS SESSION
END OF TRAINING EVALUATIONS
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 495>>>
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

<<<PAGE 496>>>
LOGIN TO ALE KNOWLEDGE HUB
• Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual 
credentials

<<<PAGE 497>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (1/2)
• Click on My Training on the home page
• Search for the training course by the reference provided by your instructor

<<<PAGE 498>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (2/2)
• From the session, select Evaluate in the dropdown menu and follow the instructions
• OR
• From the curriculum, select Open Curriculum
• Then select Evaluate in the dropdown menu associated to the session and follow 
the instructions

<<<PAGE 499>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 500>>>
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