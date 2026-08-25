<<<PAGE 1>>>
Part No. 060972-00, Rev. A
December 2025 
OmniSwitch AOS Release 8
Specifications Guide
8.10R4
www.al-enterprise.com

<<<PAGE 2>>>
ii
OmniSwitch AOS Release 8 Specifications Guide
December 2025
This user guide documents AOS Release 8.10R4.
The functionality described in this guide is subject to change without notice.
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trade-
marks-copyright. All other trademarks are the property of their respective owners. The information 
presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any 
responsibility for inaccuracies contained herein. © Copyright 2025 ALE International, ALE USA Inc. All 
rights reserved in all countries.
ALE USA Inc.
2000 Corporate Center Drive
Thousand Oaks, CA 91320
(818) 880-3500
Service & Support Contact Information
North America: 800-995-2696
Latin America: 877-919-9526
EMEA: +800 00200100 (Toll Free) or +1(650)385-2193
Asia Pacific: +65 6240 8484
Web: myportal.al-enterprise.com

<<<PAGE 3>>>
OmniSwitch AOS Release 8 Specifications Guide
December 2025
3
Contents
About This Guide ........................................................................................................ vii
Supported Platforms .........................................................................................................vii
Who Should Read this Manual? .......................................................................................vii
When Should I Read this Manual? ...................................................................................vii
What is Not in this Manual? ............................................................................................viii
How is the Information Organized? ................................................................................viii
Documentation Roadmap ................................................................................................viii
Related Documentation ...................................................................................................... x
Technical Support ............................................................................................................. xi
Chapter 1
Switch Management Specifications .......................................................................1-1
In This Chapter ................................................................................................................1-2
Getting Started Specifications .........................................................................................1-3
Login Specifications ........................................................................................................1-3
File Management Specifications .....................................................................................1-4
CMM Specifications .......................................................................................................1-5
USB Flash Drive Specifications ......................................................................................1-6
CLI Specifications ...........................................................................................................1-6
Configuration File Specifications ...................................................................................1-7
User Database Specifications ..........................................................................................1-8
WebView Specifications .................................................................................................1-8
SNMP Specifications ......................................................................................................1-9
Web Services Specifications .........................................................................................1-10
OpenFlow Specifications ..............................................................................................1-11
Virtual Chassis Specifications .......................................................................................1-12
Automatic Remote Configuration Specifications .........................................................1-14
Automatic Fabric Specifications ...................................................................................1-15
NTP Specifications ........................................................................................................1-15
Chapter 2
Network Configuration Specifications ..................................................................2-1
In This Chapter ................................................................................................................2-2

<<<PAGE 4>>>
Contents
4
OmniSwitch AOS Release 8 Specifications Guide
December 2025
Ethernet Specifications ....................................................................................................2-3
UDLD Specifications ......................................................................................................2-4
Source Learning Specifications .......................................................................................2-4
VLAN Specifications ......................................................................................................2-5
High Availability VLANs Specifications .......................................................................2-6
Spanning Tree Specifications ..........................................................................................2-6
Shortest Path Bridging Specifications .............................................................................2-7
Loopback Detection Specifications .................................................................................2-9
Static Link Aggregation Specifications ..........................................................................2-9
Dynamic Link Aggregation Specifications ...................................................................2-10
Dual-Home Link Specifications ....................................................................................2-10
ERP Specifications ........................................................................................................2-11
MVRP Specifications ....................................................................................................2-12
VXLAN Specifications .................................................................................................2-13
EVPN Specifications .....................................................................................................2-14
LLDP Specifications .....................................................................................................2-15
SIP Snooping Specifications .........................................................................................2-15
IP Specifications ............................................................................................................2-16
VRF Specifications .......................................................................................................2-18
IPv6 Specifications ........................................................................................................2-19
IPsec Specifications ......................................................................................................2-21
RIP Specifications .........................................................................................................2-22
BFD Specifications .......................................................................................................2-23
DHCP Relay / Snooping Specifications ........................................................................2-24
DHCPv6 Relay / Snooping Specifications ....................................................................2-25
DHCP Server Specifications .........................................................................................2-27
VRRP Specifications .....................................................................................................2-28
Server Load Balancing Specifications ..........................................................................2-29
IPMS Specifications ......................................................................................................2-30
IPMSv6 Specifications ..................................................................................................2-31
QoS Specifications ........................................................................................................2-32
LDAP Policy Server Specifications ..............................................................................2-33
Authentication Server Specifications ............................................................................2-34
UNP Specifications .......................................................................................................2-35
Access Guardian Specifications ....................................................................................2-36

<<<PAGE 5>>>
Contents
OmniSwitch AOS Release 8 Specifications Guide
December 2025
5
AppMon Specifications .................................................................................................2-37
Application Fingerprinting Specifications ....................................................................2-38
Port Mapping Specifications .........................................................................................2-39
Learned Port Security Specifications ............................................................................2-39
Port Mirroring Specifications ........................................................................................2-40
Port Monitoring Specifications .....................................................................................2-40
sFlow Specifications .....................................................................................................2-42
RMON Specifications ...................................................................................................2-43
Switch Health Specifications ........................................................................................2-44
VLAN Stacking Specifications .....................................................................................2-45
Switch Logging Specifications .....................................................................................2-46
Ethernet OAM Specifications .......................................................................................2-46
Link OAM Specifications .............................................................................................2-47
CPE Testhead Specifications ........................................................................................2-48
PPPoE-IA Specifications ..............................................................................................2-49
SAA Specifications .......................................................................................................2-49
MRP Specifications .......................................................................................................2-50
Chapter 3
Advanced Routing Configuration Specifications ...............................................3-1
In This Chapter ................................................................................................................3-2
OSPF Specifications ........................................................................................................3-3
OSPFv3 Specifications ....................................................................................................3-4
IS-IS Specifications .........................................................................................................3-5
BGP Specifications .........................................................................................................3-6
Multicast Boundary Specifications .................................................................................3-7
DVMRP Specifications ...................................................................................................3-8
PIM Specifications ..........................................................................................................3-9
MBR Specifications ......................................................................................................3-10
Chapter 4
TCAM Profiles ..............................................................................................................4-1
In This Chapter ................................................................................................................4-2
OmniSwitch 6870 TCAM Profile Specifications ...........................................................4-3
OmniSwitch 6570 TCAM Profile Specifications ...........................................................4-4
OmniSwitch 6575 TCAM Profile Specifications ...........................................................4-6
Index ...................................................................................................................... Index-1
Appendix A
Software License and Copyright Statements .....................................................A-1

<<<PAGE 6>>>
Contents
6
OmniSwitch AOS Release 8 Specifications Guide
December 2025
ALE USA, Inc. License Agreement ...............................................................................A-1
ALE USA, Inc. SOFTWARE LICENSE AGREEMENT ......................................A-1
Third Party Licenses and Notices ..................................................................................A-4

<<<PAGE 7>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025
vii
About This Guide
This OmniSwitch AOS Release 8 Specifications Guide provides Specification tables for all the 
OmniSwitch AOS Release 8 Products.
Supported Platforms
The information in this guide applies only to the following products:
• OmniSwitch 6360 Series
• OmniSwitch 6465 Series
• OmniSwitch 6560 Series
• OmniSwitch 6570M Series
• OmniSwitch 6575 Series
• OmniSwitch 6860 Series
• OmniSwitch 6865 Series
• OmniSwitch 6870 Series
• OmniSwitch 6900 Series
• OmniSwitch 6920 Series
• OmniSwitch 9900 Series
Who Should Read this Manual?
The audience for this user guide are network administrators and IT support personnel who need to 
configure, maintain, and monitor switches and routers in a live network. 
When Should I Read this Manual?
Read this guide as soon as you are ready to integrate your OmniSwitch into your network. You should 
already be familiar with the basics of managing a single OmniSwitch as described in the OmniSwitch AOS 
Release 8 Switch Management Guide. 
The information provided in the Specification tables in this guide assume a basic understanding of 
OmniSwitch administration commands and procedures.

<<<PAGE 8>>>
What is Not in this Manual?
About This Guide
viii
OmniSwitch AOS Release 8 Specifications Guide 
December 2025
What is Not in this Manual?
Procedures for switch management methods, such as CLI, web-based (WebView or OmniVista) or SNMP, 
are outside the scope of this guide. 
For information on WebView and SNMP switch management methods consult the OmniSwitch AOS 
Release 8 Switch Management Guide. Information on using WebView and OmniVista can be found in the 
context-sensitive on-line help available with those network management applications.
This guide is designed to provide feature specification information only and is not intended as a reference 
for any CLI commands or configuration information. Refer to the Documentation Roadmap for a list of 
available user guides.
How is the Information Organized?
Each chapter in this guide corresponds to an OmniSwitch software user manual:
• Chapter 1, “Switch Management Specifications,” applies to the features described in the OmniSwitch 
AOS Release 8 Switch Management Guide.
• Chapter 2, “Network Configuration Specifications,” applies to the features described in the 
OmniSwitch AOS Release 8 Network Configuration Guide.
• Chapter 3, “Advanced Routing Configuration Specifications,” applies to the features described in the 
OmniSwitch AOS Release 8 Advanced Routing Configuration Guide.
• Chapter 4, “Data Center Switching Specifications,” applies to the features described in the OmniSwitch 
AOS Release 8 Data Center Switching Guide.
Documentation Roadmap
The OmniSwitch user documentation suite was designed to supply you with information at several critical 
junctures of the configuration process.The following section outlines a roadmap of the manuals that will 
help you at each stage of the configuration process. Under each stage, we point you to the manual or 
manuals that will be most helpful to you.
Stage 1: Using the Switch for the First Time
Pertinent Documentation: OmniSwitch Hardware Users Guide
Release Notes
This guide provides all the information you need to get your switch up and running the first time. It 
provides information on unpacking the switch, rack mounting the switch, installing NI modules, unlocking 
access control, setting the switch’s IP address, and setting up a password. It also includes succinct 
overview information on fundamental aspects of the switch, such as hardware LEDs, the software 
directory structure, CLI conventions, and web-based management.
At this time you should also familiarize yourself with the Release Notes that accompanied your switch. 
This document includes important information on feature limitations that are not included in other user 
guides.

<<<PAGE 9>>>
About This Guide
Documentation Roadmap
OmniSwitch AOS Release 8 Specifications Guide 
December 2025
ix
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: OmniSwitch Hardware Users Guide
OmniSwitch AOS Release 8 Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the Hardware Guide. This guide 
provide specifications, illustrations, and descriptions of all hardware components, such as chassis, power 
supplies, Chassis Management Modules (CMMs), Network Interface (NI) modules, and cooling fans. It 
also includes steps for common procedures, such as removing and installing switch components.
The OmniSwitch AOS Release 8 Switch Management Guide is the primary users guide for the basic 
software features on a single switch. This guide contains information on the switch directory structure, 
basic file and directory utilities, switch access security, SNMP, and web-based management. It is 
recommended that you read this guide before connecting your switch to the network.
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: OmniSwitch AOS Release 8 Network Configuration Guide
OmniSwitch AOS Release 8 Advanced Routing Configuration Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The OmniSwitch AOS Release 8 Network Configuration Guide contains overview information, 
procedures, and examples on how standard networking technologies are configured on the OmniSwitch.
The OmniSwitch AOS Release 8 Advanced Routing Configuration Guide includes configuration 
information for networks using advanced routing technologies (OSPF and BGP) and multicast routing 
protocols (DVMRP and PIM-SM).
The OmniSwitch AOS Release 8 Data Center Switching Guide includes configuration information for data 
center networks using virtualization technologies (SPBM, VXLAN, UNP), Data Center Bridging 
protocols (PFC, ETC, and DCBX), and FCoE/FC gateway functionality.
Anytime
The OmniSwitch AOS Release 8 CLI Reference Guide contains comprehensive information on all CLI 
commands supported by the switch. This guide includes syntax, default, usage, example, related CLI 
command, and CLI-to-MIB variable mapping information for all CLI commands supported by the switch. 
This guide can be consulted anytime during the configuration process to find detailed and specific 
information on each CLI command.

<<<PAGE 10>>>
Related Documentation
About This Guide
x
OmniSwitch AOS Release 8 Specifications Guide 
December 2025
Related Documentation
The following are the titles and descriptions of all the related OmniSwitch user manuals:
• OmniSwitch 6360/6465/6560/6570M/6860/6865/6900/9900 Hardware Users Guides
Describes the hardware and software procedures for getting an OmniSwitch up and running as well as 
complete technical specifications and procedures for all OmniSwitch chassis, power supplies, fans, and 
Network Interface (NI) modules.
• OmniSwitch AOS Release 8 CLI Reference Guide
Complete reference to all CLI commands supported on the OmniSwitch. Includes syntax definitions, 
default values, examples, usage guidelines and CLI-to-MIB variable mappings.
• OmniSwitch AOS Release 8 Switch Management Guide
Includes procedures for readying an individual switch for integration into a network. Topics include the 
software directory architecture, image rollback protections, authenticated switch access, managing 
switch files, system configuration, using SNMP, and using web management software (WebView).
• OmniSwitch AOS Release 8 Network Configuration Guide
Includes network configuration procedures and descriptive information on all the major software 
features and protocols included in the base software package. Chapters cover Layer 2 information 
(Ethernet and VLAN configuration), Layer 3 information (routing protocols, such as RIP and IPX), 
security options (authenticated VLANs), Quality of Service (QoS), link aggregation, and server load 
balancing.
• OmniSwitch AOS Release 8 Advanced Routing Configuration Guide
Includes network configuration procedures and descriptive information on all the software features and 
protocols included in the advanced routing software package. Chapters cover multicast routing 
(DVMRP and PIM-SM), Open Shortest Path First (OSPF), and Border Gateway Protocol (BGP).
• OmniSwitch AOS Release 8 Transceivers Guide
Includes SFP and XFP transceiver specifications and product compatibility information.
• OmniSwitch AOS Release 8 Specifications Guide
Includes Specifications table information for the features documented in the Switch Management 
Guide, Network Configuration Guide, Advanced Routing Guide, and Data Center Switching Guide.
• Technical Tips, Field Notices
Includes information published by Alcatel-Lucent’s Customer Support group.
• Release Notes
Includes critical Open Problem Reports, feature exceptions, and other important information on the 
features supported in the current release and any limitations to their support.
Technical Support
An Alcatel-Lucent service agreement brings your company the assurance of 7x24 no-excuses technical 
support. You’ll also receive regular software updates to maintain and maximize your Alcatel-Lucent

<<<PAGE 11>>>
About This Guide
Technical Support
OmniSwitch AOS Release 8 Specifications Guide 
December 2025
xi
product’s features and functionality and on-site hardware replacement through our global network of 
highly qualified service delivery partners. 
With 24-hour access to Alcatel-Lucent’s Enterprise Service and Support web page, you’ll be able to view 
and update any case (open or closed) that you have reported to Alcatel-Lucent Enterprise technical 
support, open a new case or access helpful release notes, technical bulletins, and manuals. 
Access additional information on Alcatel-Lucent Enterprise Service Programs:
Web: myportal.al-enterprise.com
Phone: 1-800-995-2696

<<<PAGE 12>>>
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 1-1
1   Switch Management
Specifications
This chapter provides Specifications tables for the following switch management applications and 
procedures that are used for readying an individual OmniSwitch for integration into a network:
• The switch directory structure, basic file and directory utilities, switch access security, SNMP, and 
web-based management.
• The software directory architecture.
• Image rollback protections.
• Authenticated switch access.
• Managing switch files.
• System configuration.
• Using SNMP.
• Using web management software (WebView).
For information about how to configure switch management applications, refer to the OmniSwitch AOS 
Release 8 Switch Management Guide.
Note. The maximum limit values provided in the Specifications tables included in this chapter are subject 
to available system resources. 
Note. A Virtual Chassis is a group of switches managed as a single logical chassis. Any maximum 
limitation values documented apply to the entire Virtual Chassis and not to each individual switch unless 
stated otherwise.

<<<PAGE 13>>>
Switch Management Specifications
In This Chapter
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 1-2
In This Chapter
This chapter contains the following switch management Specifications tables:
• “Getting Started Specifications” on page 1-3.
• “Login Specifications” on page 1-3.
• “File Management Specifications” on page 1-4.
• “CMM Specifications” on page 1-5.
• “USB Flash Drive Specifications” on page 1-6.
• “CLI Specifications” on page 1-6.
• “Configuration File Specifications” on page 1-7.
• “User Database Specifications” on page 1-8.
• “WebView Specifications” on page 1-8.
• “SNMP Specifications” on page 1-9.
• “Web Services Specifications” on page 1-10.
• “OpenFlow Specifications” on page 1-11
• “Virtual Chassis Specifications” on page 1-12.
• “Automatic Remote Configuration Specifications” on page 1-14.
• “Automatic Fabric Specifications” on page 1-15.
• “NTP Specifications” on page 1-15.

<<<PAGE 14>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-3
Switch Management Specifications 
         
Getting Started Specifications
Getting Started Specifications
Login Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6, 
X48C4E,
V48C8, 
C32E, 
X/T24C2
OS6920
OS9900
Virtual Chassis 
Configuration Files
vcboot.cfg 
vcsetup.cfg
Image Files
Nosa.img
Nos.img
Nos.img
Wos.img
Dos.img
Uos.img
Uosn.img
Uos.img
Kaos.img
Yos.img
Yos.img
Ypos.img
Mhost.img
Mos.img
Meni.img
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Login Methods
Telnet, SSH, HTTP, SNMP
Number of concurrent 
Telnet sessions
6
Number of concurrent 
SSH sessions
8
Number of concurrent 
HTTP (WebView) 
sessions
4
Secure Shell public key 
authentication
Password
DSA/RSA/ECSDA Public Key
RFCs Supported for 
SSHv2
RFC 4253 - SSH Transport Layer Protocol 
RFC 4418 - UMAC: Message Authentication Code using Universal Hashing
Notes:

<<<PAGE 15>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-4
Switch Management Specifications 
         
File Management Specifications
File Management Specifications
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
File Transfer Methods
FTP (v4/v6), SFTP (v4/v6), SCP (v4/v6), TFTP
Client/Server Support
FTP—Client (IPv4 Only) or Server
SFTP—Client or Server
SCP—Client or Server
TFTP—Client
Number of concurrent 
FTP/SFTP sessions
4
Configuration Recovery
The flash/certified directory holds configurations that are certified as the default start-up files for the switch. They will be used in the event of a non-specified reload.
Default Switch Directory 
- /flash
Contains the certified, working, switch, network, and user-defined directories.
File/Directory Name 
Metrics
255 character maximum. File and directory names are case sensitive.
30 character maximum if being used the RUNNING directory.
File/Directory Name 
Characters
Any valid ASCII character except ‘/’.
Sub-Directories
Additional user-defined directories created in the /flash directory.
Text Editing
Standard Vi editor
System Clock
Set local date, time and time zone, Universal Time Coordinate (UTC), Daylight Savings (DST or summertime).
Notes:
N/A

<<<PAGE 16>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-5
Switch Management Specifications 
         
CMM Specifications
CMM Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900- 
V72/C32
OS6900-
X/T48C6, 
X48C4E,
V48C8, 
C32E, 
X/T24C2
OS6920
OS9900
RAM Memory
1 GB
1 GB
2 GB
2 GB
2 GB
2 GB
4 GB
2 GB
8 GB
8 GB
8 GB
16 GB 
(V48C8/
C32E)
32 GB
16 GB
Flash Memory
1 GB
1 GB
1 GB / 2 
GB
8 GB
4 GB
2 GB
16 GB
2 GB
32 GB
32 GB
32 GB*
64 GB* 
(V48C8/
C32E)
64 GB
2 GB 
(9907)
32GB 
(9912)
Maximum Length of File 
Names (in Characters)
255
Maximum Length of 
Directory Names (in 
Characters)
255
30 (maximum if being used as RUNNING directory).
Maximum Length of 
System Name (in 
Characters)
64
Notes:
*Size of physical memory. Partitioned to 16GB flash memory.

<<<PAGE 17>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-6
Switch Management Specifications 
         
USB Flash Drive Specifications
USB Flash Drive Specifications
CLI Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
USB Flash Drive Support
Alcatel-Lucent Enterprise Certified USB Flash Drive
Automatic Software 
Upgrade
Supported
N/S
N/S
N/S
Disaster Recovery
Narescue.img
file required
Nrescue.img 
file required
Nrescue.img 
file required
Wrescue.img 
file required
Drescue.img 
file required
Urescue.img 
file required
ONIE-based
Urescue.img 
file required
ONIE-based
ONIE-based
ONIE-based
ONIE-based
Mrescue.img 
file required
Notes:
•
The format of the Alcatel-Lucent certified USB Flash Drive must be FAT32. To avoid file corruption issues, the USB Drive should be stopped before removing from a PC. 
•
Directory names are case sensitive and must be lower case.
OS6360
OS6465
OS6560
OS6570M
OS6575 OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Configuration Methods
•
Online configuration via real-time sessions using CLI commands.
•
Offline configuration using text file containing CLI commands.
Command Capture 
Feature
Snapshot feature captures switch configurations in a text file.
User Service Features
•
Command Line Editing
•
Command Prefix Recognition
•
CLI Prompt Option
•
Command Help
•
Keyword Completion
•
Command Abbreviation
•
Command History
•
Command Logging 
•
Syntax Error Display
•
More Command

<<<PAGE 18>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-7
Switch Management Specifications 
         
Configuration File Specifications
Configuration File Specifications
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Methods for Creating 
Configuration Files
•
Create a text file on a word processor and upload it to the switch.
•
Invoke the switch’s snapshot feature to create a text file.
•
Create a text file using the switch’s text editor.
Timer Functions
Files can be applied immediately or by setting a timer on the switch.
Command Capture 
Feature
Snapshot feature captures switch configurations in a text file.
Error Reporting
Snapshot feature includes error reporting in the text file.
Text Editing on the 
Switch
Vi standard editor. 
Default Error File Limit
1
Notes:
N/A

<<<PAGE 19>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-8
Switch Management Specifications 
         
User Database Specifications
User Database Specifications
WebView Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of 
alphanumeric characters 
in a username
63
Maximum number of 
alphanumeric characters 
in a user password
30
Maximum number of 
local user accounts
50
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
WebView Versions
WebView 2.0
Notes:
N/A

<<<PAGE 20>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-9
Switch Management Specifications 
         
SNMP Specifications
SNMP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575 OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported for 
SNMPv2
1902 through 1907 - SNMPv2c Management Framework
1908 - Coexistence and transitions relating to SNMPv1 and SNMPv2c
RFCs Supported for 
SNMPv3
2570—Version 3 of the Internet Standard Network Management 
Framework
2571—Architecture for Describing SNMP Management Frameworks
2572—Message Processing and Dispatching for SNMP
2573—SNMPv3 Applications
2574/3414—User-based Security Model (USM) for version 3 SNMP
2575—View-based Access Control Model (VACM) for SNMP
2576—Coexistence between SNMP versions
3586—The Advanced Encryption Standard (AES) Cipher Algorithm in the SNMP User-based Security Model
SNMPv1, SNMPv2, 
SNMPv3
The SNMPv3 protocol is ascending compatible with SNMPv1 and v2 and supports all the SNMPv1 and SNMPv2 PDUs
SNMPv1 and SNMPv2 
Authentication
Community Strings
SNMPv1, SNMPv2 
Encryption
None
SNMPv1 and SNMPv2 
Security requests 
accepted by the switch
Sets and Gets
SNMPv3 Authentication
SHA, MD5
SNMPv3 Encryption
DES, AES
SNMPv3 Security 
requests accepted by the 
switch
Non-authenticated Sets, Non-authenticated Gets and Get-Nexts, Authenticated Sets, Authenticated Gets and Get-Nexts, Encrypted Sets, Encrypted Gets and Get-Nexts
SNMP traps
For a list and description of system MIBs and Traps refer to Appendix B, “SNMP Trap Information,” in the OmniSwitch AOS Release 8 Switch Management Guide.
Notes:
N/A

<<<PAGE 21>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-10
Switch Management Specifications 
         
Web Services Specifications
Web Services Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Configuration Methods
•
HTTP/HTTPS
•
Python API
Response Formats
•
Extensible Markup language (XML)
•
JavaScript Object Notation (JSON)
Maximum Web Services 
Sessions
4
Alcatel-Lucent Example 
Python Library
consumer.py (Python version 2.X/3.X compatible)
This file is available on the Service & Support Website. It is being provided as an example application to help with Web Services familiarization but is 
not an officially supported part of the Web Services solution.
Embedded Python /Event 
based CLI Scripting
Python 3
AOS Micro Services 
(AMS)
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Notes:
N/A

<<<PAGE 22>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-11
Switch Management Specifications 
         
OpenFlow Specifications
OpenFlow Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Modes Supported
N/S
N/S
N/S
N/S
N/S
Normal
Hybrid 
(API)
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Versions Supported
N/S
N/S
N/S
N/S
N/S
1.0/
1.3.1
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Maximum number of 
logical switches
N/S
N/S
N/S
N/S
N/S
3
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Maximum number of 
controllers per logical 
switch
N/S
N/S
N/S
N/S
N/S
3
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Maximum number of 
logical switches in Hybrid 
mode
N/S
N/S
N/S
N/S
N/S
1
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Support for Virtual 
Chassis
N/S
N/S
N/S
N/S
N/S
Supported
N/S
N/S
N/S
N/S
N/S
N/S
N/S
OpenFlow 1.0/1.3.1 TCP 
port.
N/S
N/S
N/S
N/S
N/S
6633
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Flow Matching Table
N/S
N/S
N/S
N/S
N/S
1535
N/S
N/S
N/S
N/S
N/S
N/S
N/S
MAC Table
N/S
N/S
N/S
N/S
N/S
48K
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Notes:
N/A

<<<PAGE 23>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-12
Switch Management Specifications 
         
Virtual Chassis Specifications
Virtual Chassis Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6, 
X48C4E
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of 
physical switches in a 
Virtual Chassis
8 (all 24/48 
port 
models)
4 (10 port 
models)
4
8
8
4
8
8
8
8
6
6
N/S
2 (OS9907)
Valid chassis identifier
1-8 (24/48)
1-4 (10)
1-4
1–8
1-8
1-4
1–8
1–8
1–8
1–8
1–6
1–6
N/S
1 or 2
Valid chassis group 
identifier
0-255
0-255
0-255
0-255
0-255
0–255
0–255
0-255
0-255
0–255
0–255
N/S
0-255
Valid chassis priority
0-255
0-255
0-255
0-255
0-255
0–255
0–255
0-255
0-255
0–255
0–255
N/S
0-255
Maximum number of 
Virtual Fabric Link peers 
per chassis
2
2
2
2
2
2
2
2
2
5
5
N/S
1
Maximum number of 
member ports per Virtual 
Fabric Link
2
8
8
8
8
8
8
8
8
16
16
N/S
8
Valid Virtual Fabric Link 
identifier
0 or 1
0 or 1
0 or 1
0 or 1
0 or 1
0 or 1
0-1
0 or 1
0 or 1
0–4
0–4
N/S
0
VFL Supported Port 
Types
10G SFP+
SFP 
(10/P10 
Only)
SFP/SFP+
Dedicated 
VFL ports, 
10G SFP+ 
10G SFP+ 
SFP+
Dedicated 
VFL ports, 
10G SFP+ 
Dedicated 
VFL ports, 
40G QSFP+
100G 
QSFP28
10G SFP+ 
10G SFP+
25G SFP28
40G QSFP+
100G 
QSFP28
200G 
QSFP56
10G SFP+
25G SFP28
40G QSFP+
100G 
QSFP28
10G SFP+
25G SFP28
40G QSFP+
100G 
QSFP28
N/S
10G SFP+ 
40G QSFP+
100G 
QSFP28
Valid control VLAN
2-4094
Valid Virtual Chassis 
protocol hello interval
1-65535
Remote Chassis Detection 
(RCD)
N/S
N/S
N/S
N/S
N/S
Supported
Supported
N/S
Supported
N/S
Supported
N/S
Supported
Notes:

<<<PAGE 24>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-13
Switch Management Specifications 
         
Virtual Chassis Specifications
•
The OS9912 chassis does not support a VC configuration. 
•
The OS9907 supports a VC-of-2 depending on the CMM/CFM combinations. Refer to the OS9900 Hardware Guide for a list of supported combinations.
•
OS6900-V72/C32(E)/X48C6/T48C6/V48C8/X24C2/T24C2 models can be mixed in a VC of up to 6 elements.
•
OS6900-X48C4E can be mixed with OS6900-X48C6/T48C6/V48C8/C32E/T24C2/X24C2 when they are configured in mixed VFL mode.
•
MAC Learning Mode is not supported on OS6900 Virtual Chassis.
•
OS6860 and OS6865 models can be mixed in Virtual Chassis.
•
OS6465-P6/P12, OS6465-P28 and 6465T models can be mixed in Virtual Chassis using the 1G SFP ports.
•
OS6860N and OS686x models should not be mixed in a Virtual Chassis.
•
OS6360 10-port models support a VC of up to 4 elements using SFP ports.
•
VFLs are supported on 4X10G or 4X25G splitter ports. For 4X25G ports the inter-frame gap must be configured to 13 on both ends. Refer to the Switch Management Guide for additional details.

<<<PAGE 25>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-14
Switch Management Specifications 
         
Automatic Remote Configuration Specifications
Automatic Remote Configuration Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
DHCP Specifications
DHCP Server required DHCP Client on:
- VLAN 1
- Tagged VLAN 127
- LLDP Management VLAN
- Automatic LACP (tagged VLAN 127, untagged VLAN 1)
File Servers
TFTP
FTP/SFTP
Clients supported
TFTP
FTP/SFTP
Instruction file
Maximum length of:
•
Pathname: 255 characters
•
Filename: 63 characters
Maximum length of 
username for FTP/SFTP 
file server. 
15 characters
Maximum DHCP lease 
tries
6
Unsupported Features
•
ISSU and IPv6 are not supported.
•
Upgrade of uboot, miniboot, or FPGA files is not supported.
OK LED
Flashing amber during Automatic Remote Configuration process
Notes:
N/A

<<<PAGE 26>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 1-15
Switch Management Specifications 
         
Automatic Fabric Specifications
Automatic Fabric Specifications
NTP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Ports Supported
Any switch port that is not already configured in such a way as to prevent the port from participating in the Automatic Fabric discovery and configuration process.
IP Protocols Supported 
for Automatic IP 
Configuration
OSPFv2, OSPFv3, IS-IS IPv4, IS-IS IPv6
Notes:
Advanced routing protocols not supported on the OS6360 or OS6465.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs supported
5905–Network Time Protocol v4
NTP Key File Location
/flash/network
Maximum number of 
NTP servers per client
12
Maximum number of 
associations
512
Notes:
N/A

<<<PAGE 27>>>
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 2-1
2   Network Configuration
Specifications
This chapter provides Specifications tables for the following OmniSwitch network configuration 
applications and procedures that are used for readying a switch for integration into a live network 
environment:
• Layer 2 features (Ethernet, source learning, and VLAN configuration).
• Layer 3 features (routing protocols, such as IP and RIP)
• Security options (MAC and 802.1x authentication)
• Quality of Service (QoS)
• Link aggregation
• Server load balancing.
For information about how to implement the fundamental software features and protocols for network 
configuration, refer to the OmniSwitch AOS Release 8 Network Configuration Guide.
Note. The maximum limit values provided in the Specifications tables included in this chapter are subject 
to available system resources.
Note. A Virtual Chassis is a group of switches managed as a single logical chassis. Any maximum 
limitation values documented apply to the entire Virtual Chassis and not to each individual switch unless 
stated otherwise.

<<<PAGE 28>>>
Network Configuration Specifications
In This Chapter
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 2-2
In This Chapter
This chapter contains the following network configuration Specifications tables:
•
“Ethernet Specifications” on page 2-3
•
“UDLD Specifications” on page 2-4
•
“Source Learning Specifications” on page 2-4
•
“VLAN Specifications” on page 2-5
•
“High Availability VLANs Specifications” on 
page 2-6
•
“Spanning Tree Specifications” on page 2-6
•
“Shortest Path Bridging Specifications” on page 2-7
•
“Loopback Detection Specifications” on page 2-9
•
“Static Link Aggregation Specifications” on page 2-9
•
“Dynamic Link Aggregation Specifications” on 
page 2-10
•
“Dual-Home Link Specifications” on page 2-10
•
“ERP Specifications” on page 2-11.
•
“MVRP Specifications” on page 2-12.
•
“VXLAN Specifications” on page 2-13
•
“EVPN Specifications” on page 2-14
•
“LLDP Specifications” on page 2-15.
•
“SIP Snooping Specifications” on page 2-15.
•
“IP Specifications” on page 2-16.
•
“VRF Specifications” on page 2-18.
•
“IPv6 Specifications” on page 2-19.
•
“IPsec Specifications” on page 2-21.
•
“RIP Specifications” on page 2-22.
•
“BFD Specifications” on page 2-23.
•
“DHCP Relay / Snooping Specifications” on 
page 2-24.
•
“DHCPv6 Relay / Snooping Specifications” on 
page 2-25.
•
“DHCP Server Specifications” on page 2-27
•
“VRRP Specifications” on page 2-28.
•
“Server Load Balancing Specifications” on page 2-29.
•
“IPMS Specifications” on page 2-30.
•
“IPMSv6 Specifications” on page 2-31.
•
“QoS Specifications” on page 2-32.
•
“LDAP Policy Server Specifications” on page 2-33.
•
“Authentication Server Specifications” on page 2-34.
•
“UNP Specifications” on page 2-35.
•
“Access Guardian Specifications” on page 2-36.
•
“AppMon Specifications” on page 2-37.
•
“Application Fingerprinting Specifications” on 
page 2-38.
•
“Port Mapping Specifications” on page 2-39.
•
“Learned Port Security Specifications” on page 2-39.
•
“Port Mirroring Specifications” on page 2-40.
•
“Port Monitoring Specifications” on page 2-40.
•
“sFlow Specifications” on page 2-42.
•
“RMON Specifications” on page 2-43.
•
“Switch Health Specifications” on page 2-44.
•
“VLAN Stacking Specifications” on page 2-45.
•
“Switch Logging Specifications” on page 2-46.
•
“Ethernet OAM Specifications” on page 2-46.
•
“Link OAM Specifications” on page 2-47.
•
“CPE Testhead Specifications” on page 2-48.
•
“PPPoE-IA Specifications” on page 2-49
•
“SAA Specifications” on page 2-49.
•
“MRP Specifications” on page 2-50

<<<PAGE 29>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-3
Network Configuration Specifications 
         
Ethernet Specifications
Ethernet Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Standards 
Supported
802.3 Carrier Sense Multiple Access with Collision Detection (CSMA/CD)
802.3u (100BaseTX)
802.3ab (1000BaseT)
802.3z (1000Base-X)
802.3bz (2.5Base-T)
802.3ae (10GBase-X)
802.3ba (40GBase-X)
802.3az (Energy Efficient Ethernet)
Ports Supported
Ethernet (10 Mbps)
Fast Ethernet (100 Mbps)
Gigabit Ethernet (1 Gbps)
10/40/100 Gigabit Ethernet (10/40/100 Gbps)
802.1Q Hardware 
Tagging
Supported
Jumbo Frame 
Configuration
1/10/40/100 Gigabit Ethernet ports
Maximum Frame Size
1553 bytes (10/100 Mbps)
9216 bytes (1/10/40/100 Gbps)
MACsec
N/S
Supported
Supported
Supported
Supported
Supported
Supported
N/S
Supported
N/S
X48C4E
N/S
Supported
PoE
Supported
Supported
Supported
N/S
Supported
Supported
Supported
Supported
Supported
N/S
N/S
N/S
Supported
Fast/ Perpetual PoE
Supported
N/S
N/S
N/S
N/S
Supported
Supported
Supported
Supported
N/S
N/S
N/S
N/S
1588v2 End-to-End
N/S
Supported
Supported1
Supported
Supported
Supported
Supported
Supported
Supported
N/S
Supported
N/S
N/S
1588v2 Peer-to-Peer
N/S
Supported
Supported1
Supported
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Notes:
• Supported port speeds are chassis and module dependent. 
• OS6570M, OS6860, OS6865, OS6870 do not support 10/100 half-duplex (CSMA/CD).
• MACsec site license required.
• Refer to the latest release notes for a detailed list of MACsec platform and module support.
• 1588v2 is supported on a VC-of-1 only.
1. Supported on OS6560-48X4/P48X4/P48Z16 1G and 10G ports only. Not supported on 2.5G ports. Requires proper FPGA, see release notes.

<<<PAGE 30>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-4
Network Configuration Specifications 
         
UDLD Specifications
UDLD Specifications
Source Learning Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
Number of UDLD ports 
per system
128
128
128
128
128
128
128
128
128
N/S
128
(X48C4E Only)
128
N/S
Number of UDLD 
neighbors per port
32
32
32
32
32
32
32
32
32
N/S
32
(X48C4E Only)
32
N/S
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
2674—Definitions of Managed Objects for Bridges with Traffic Classes, Multicast Filtering and Virtual LAN Extensions
Maximum number of 
learned MAC addresses 
when centralized MAC 
source learning mode is 
enabled
16K
16K
16K
32K
16K
48K
64K (SM)
16K (RM)
32K (ER)
48K
128K (SM)
80K (ER)
64K (RM)
V72 - 104K 
(SM)
V72 - 8K 
(RM)
C32 - 104K 
(SM)
C32 - 8K 
(RM)
228K (SM)
128K (ER)
32K (RM) 
X/T24C2 - 64K (SM)
X/T24C2 - 32K (ER)
X/T24C2 - 16K (RM)
-
128K
128K (SM)1
80K (ER)1
Notes:
SM = Switch Mode
RM = Router Mode 
ER - Edge-router mode
(Values are indicative maximum values based on hardware specifications. They are subject to change per use case or IP Routing configurations) 
1. OS99-CMM2 and OS99-CNI-U20.

<<<PAGE 31>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-5
Network Configuration Specifications 
         
VLAN Specifications
VLAN Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
2674 - Definitions of Managed Objects for Bridges with Traffic Classes, Multicast Filtering and Virtual LAN Extensions
5517 - Private VLAN
IEEE Standards 
Supported
802.1Q - Virtual Bridged Local Area Networks
802.1D - Media Access Control Bridges
Maximum VLANs per 
VC
4094
4094
4094
4094
4094
4094
4094
4094
4094
4094
4094
4094
4094
Maximum Tagged 
VLANs per Port
4093
4093
4093
4093
4093
4093
4093
4093
4093
4093
4093
4093
4093
Maximum Untagged 
VLANs per Port
One untagged VLAN (default VLAN) per port.
Maximum number of 
ports or link aggregates 
per PVLAN supported
N/S
N/S
256
256
256
1
1
1
1
1
1
256
N/S
Maximum Number of 
Secondary VLANs with a 
Primary VLAN that can 
co-exist on a port
N/S
N/S
1
1
1
1
1
1
1
1
1
1
N/S
Maximum number of
IPCL and EPCL rules per
VLAN
N/S
N/S
256
256
256
256
256
256
*
256
256
1
N/S
Maximum number of 
PVLAN per promiscuous 
port
N/S
N/S
256
256
1
1
1
1
1
1
1
1
N/S
Notes:
*See “OS6870 TCAM Profiles” on page 4-1.

<<<PAGE 32>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-6
Network Configuration Specifications 
         
High Availability VLANs Specifications
High Availability VLANs Specifications
Spanning Tree Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum high 
availability VLANs per 
VC
N/S
N/S
N/S
16
16
16
16
32
16
16
16
N/S
N/S
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Standards supported 802.1d—Media Access Control (MAC) Bridges
802.1s—Multiple Spanning Trees
802.1w—Rapid Spanning Tree Protocol
Spanning Tree operating 
modes supported
Flat mode—one spanning tree instance per VC
Per-VLAN mode—one spanning tree instance per VLAN
Spanning Tree port 
eligibility
Fixed ports
802.1Q tagged ports
Link aggregate of ports
Maximum VLAN 
Spanning Tree instances 
per VC
100
100
100
100
100
100 
100
100
100
128
128
128
128
Maximum flat mode 
Multiple Spanning Tree 
Instances (MSTI) per VC
16 MSTI, in addition to the Common and Internal Spanning Tree instance (also referred to as MSTI 0).
Notes:
Maximum VLAN Spanning Tree instances per VC—values based on per-VLAN mode.

<<<PAGE 33>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-7
Network Configuration Specifications 
         
Shortest Path Bridging Specifications
Shortest Path Bridging Specifications
The following Specifications table contains information for the OmniSwitch implementation of Shortest Path Bridging (SPB). Note that any maximum limits provided in the table are subject to available system 
resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Standards 
Supported
802.1aq/D3.6: Draft February 10, 2011—Virtual Bridged Local Area Networks-Amendment 9: Shortest Path Bridging 
802.1ah/D4.2: DRAFT March 26, 2008— Virtual Bridged Local Area Networks–Amendment 6: Provider Backbone Bridging
IETF Internet-Drafts 
Supported
draft-ietf-isis-ieee-aq-05.txt—ISIS Extensions Supporting IEEE 802.1aq Shortest Path Bridging 
IETF draft—IP/IPVPN services with IEEE 802.1aq SPBB networks
IETF draft—IP/IPVPN services with IEEE 802.1aq SPB networks
SPB mode supported
N/S
N/S
N/S
SPBM (MAC-in-MAC)
IP over SPBM
N/S
N/S
N/S
IPv4 (VPN-Lite and L3 VPN)
VRF-to-ISID mapping (one-to-one, one-to-many)
N/S
IPV4(VPN-
Lite and L3 
VPN)VRF-
to-ISID 
mapping 
(one-to-one, 
one-to-
many)
Maximum number of 
ISIS-SPB instances per 
VC.
N/S
N/S
N/S
1
Maximum number of 
BVLANs per VC
N/S
N/S
N/S
16
16
16
Maximum number of IS-
IS adjacencies
N/S
N/S
N/S
70
70
70
128
70
128
128
128
128
128
Maximum number of IS-
IS interfaces
N/S
N/S
N/S
70
70
70
128
70
128
128
128
128
128
Number of equal cost tree 
(ECT) algorithm IDs 
supported.
N/S
N/S
N/S
16 (Can select any ID between 1 and 16 to assign to a BVLAN)
Maximum number of 
service instance 
identifiers (I-SIDs) per 
VC
N/S
N/S
N/S
512
512
2K
2K
2K
2K
8K
8K
X/T24C2 - 
2K
8K
1K

<<<PAGE 34>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-8
Network Configuration Specifications 
         
Shortest Path Bridging Specifications
Maximum number of 
VLANs or SVLANs per 
I-SID
N/S
N/S
N/S
2K
2K
2K
2K
2K
2K
4K
4K
X/T24C2 - 
2K
4K
4K
Maximum number of 
SAPs
N/S
N/S
N/S
512
512
2K
2K
2K
*
8K
8K
X/T24C2 - 
2K
8K
8K
Maximum Transmission 
Unit (MTU) size for SPB 
services.
N/S
N/S
N/S
9K
9K
9K (not configurable at this time)
Maximum number of 
Remote Fault Propagation 
(RFP) domains.
N/S
N/S
N/S
N/S
N/S
8 (or less if 
there are 
other 
Ethernet 
OAM
domains 
already 
configured)
N/S
8 (or less if 
there are 
other 
Ethernet 
OAM
domains 
already 
configured)
N/S
N/S
N/S
N/S
N/S
Inline Routing
N/S
N/S
N/S
Supported
Supported
N/S
Supported
N/S
Supported
N/S
Supported
N/S
Supported
Inline Routing 
(front panel)
N/S
N/S
N/S
Supported
Supported
N/S
N/S
N/S
N/S
Supported
N/S
N/S
N/S
External Loopback 
Routing
N/S
N/S
N/S
N/S
N/S
Supported
Supported
Supported
N/S
Supported
Supported
N/S
Supported
Notes:
*See “OS6870 TCAM Profiles” on page 4-1.

<<<PAGE 35>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-9
Network Configuration Specifications 
         
Loopback Detection Specifications
Loopback Detection Specifications
Static Link Aggregation Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Edge (Bridge)
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
SAP (Access)
N/S
N/S
N/S
N/S
N/S
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Transmission Timer
5–600 seconds
Auto-recovery Timer
30–86400 seconds
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of link 
aggregation groups
32
32
32
32
128
128
128
252
128
128
128
253
Maximum number of 
ports per link aggregate 
group
8
8
8
8
16
16
16
16
16
16
16
16
Notes:
On an OS9900 linkagg IDs 0, 126, and 127 are reserved

<<<PAGE 36>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-10
Network Configuration Specifications 
         
Dynamic Link Aggregation Specifications
Dynamic Link Aggregation Specifications
Dual-Home Link Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Specifications 
Supported
802.1ax/802.3ad—Aggregation of Multiple Link Segments
Maximum number of link 
aggregation groups
32
32
32
96
32
128
128
128
252
128
128
128
253
Maximum number of 
ports per link aggregate 
group
8
8
8
8
8
16
16
16
16
16
16
16
16
Notes:
On an OS9900 linkagg IDs 0, 126, and 127 are reserved.
OS6360
OS6465
OS6560
OS6570M
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
DHL sessions supported
1
1
1
1
1
1
1
1
1
N/S
1
1
N/S
Notes:
N/A

<<<PAGE 37>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-11
Network Configuration Specifications 
         
ERP Specifications
ERP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
ITU-T G.8032 03/2010
Ethernet Ring Protection version 2
(Multi Rings and Ladder networks supported)
(Hold off timer, Lockout, Signal degrade SD, RPL Replacement, Forced Switch, Manual Switch, Clear for Manual/Forced Switch, Dual end blocking not supported)
ITU-T Y.1731/IEEE 
802.1ag
ERP packet compliant with OAM PDU format for CCM
Maximum number of 
rings per node
64
Maximum number of 
nodes per ring
16 (recommended)
Maximum number of 
VLANs per port
4094
Range for ring ID
1–2147483647
Range for remote MEPID
1–8191
Range for wait-to-restore 
timer
1–12 minutes
Range for guard timer
1–200 centi-seconds
Notes:
N/A

<<<PAGE 38>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-12
Network Configuration Specifications 
         
MVRP Specifications
MVRP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Standards 
Supported
IEEE 802.1ak-2007 Amendment 7: Multiple Registration Protocol
IEEE 802.1Q-2005 Corrigendum 2008
Maximum MVRP 
VLANs
256
256
512
512
512
512
512
512
512
512
512
512
512
Notes:
N/A

<<<PAGE 39>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-13
Network Configuration Specifications 
         
VXLAN Specifications
VXLAN Specifications
The following Specifications table contains information for the OmniSwitch implementation of the Virtual eXtensible LAN (VXLAN) feature. Note that any maximum limits provided in the table are subject to 
available system resources.
OS6860N/OS6870/OS6900
RFCs Supported
7348—VXLAN: A Framework for Overlaying Layer 2 
Virtualized Networks over Layer 3 Networks.
VXLAN segments (L2 overlay networks)
16 million
VXLAN service instances
8K
VXLAN Tunnel End Points in a VXLAN 
network.
500
VXLAN UDP destination ports
8 (including the default UDP port number, which is 4789).
VXLAN Service Access Points (SAPs)
8K (per device or per Virtual Chassis)
VXLAN SAPs with a VLAN ID range
8 SAPs per service access port
Service access ports with SAPs that 
contain a VLAN ID range
255
VXLAN Network IDs (VNIs)
4K
Multicast Groups
500
Multicast protocol supported
Bidirectional PIM (BIDIR-PIM)
Notes:
VXLAN is supported on OS6860N, OS6870 and OS6900 platforms only.
*See “OS6870 TCAM Profiles” on page 4-1

<<<PAGE 40>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-14
Network Configuration Specifications 
         
EVPN Specifications
EVPN Specifications
The following Specifications table contains information for the OmniSwitch implementation of Ethernet Virtual Private Network (EVPN). 
Note that any maximum limits provided in the table are subject to available system resources.
OS6900
RFCs Supported
7432 - BGP MPLS-Based Ethernet VPN
9161 - Operational Aspects of Proxy ARP/ND in Ethernet Virtual Private Networks
9135 - Integrated Routing and Bridging in Ethernet VPN (EVPN)
9136 - IP Prefix Advertisement in Ethernet VPN (EVPN)
9251 - Internet Group Management Protocol (IGMP) and Multicast Listener 
Discovery (MLD) Proxies for Ethernet VPN (EVPN)
9625 - EVPN Optimized Inter-Subnet Multicast (OISM) Forwarding
Host Devices
10K
- This will generate 20K RT2 routes (10K MAC+IP and 10K MAC+0 RT2 routes)
EVPN Services
50
- All services are IRB/L3 enabled
- The 10K hosts are distributed across the 50 services
VRFs
4
- The 50 IRB services are distributed across the 4 VRFs
Fabric VPNs
 4
- One Fabric VPN per VRF
Prefix routes
500
- The prefix routes are distributed across the 4 VRFs
- The prefix routes are sourced from an external-facing VLAN domain
Multicast Groups
200
- The Multicast Groups are distributed across the 4 VRFs
- 100 Groups are sourced from the internal EVPN network
- 100 Groups are sourced from the external PIM gateway
- 140 Receivers in the internal network
- OISM capability and PIM Gateway is enabled on all 4 Fabric VPN services
Access Connections
140
- 100 Single-Homed connections
- 40 Multi-Homed connections
Notes:
N/A

<<<PAGE 41>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-15
Network Configuration Specifications 
         
LLDP Specifications
LLDP Specifications
SIP Snooping Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Specification
IEEE 802.1AB-2005 Station and Media Access Control Connectivity Discovery
Maximum number of 
network policies that can 
be associated with a port
8
8
8
8
8
8
8
8
8
8
8
8
8
Maximum number of 
network policies that can 
be configured on a VC
8
8
32
32
32
32
32
32
32
32
32
32
32
Nearest Edge MAC 
Address
01:20:da:02:01:73
Nearest Bridge MAC 
Address
01:80:c2:00:00:0e
Nearest Customer MAC 
Address
01:80:C2:00:00:00
Non-TPMR Address
01:80:C2:00:00:03
Notes:
N/A
OS6860
RFCs Supported
3261–SIP session initiation protocol
6337–SIP USAGE of offer/answer model
4566–SDP session description Protocol
3551–RTP profile for audio and video conferences with minimal control
3311–The Session Initiation Protocol (SIP) UPDATE Method
3262–Reliability of Provisional Responses in SIP
Notes:
Supported on OS6860 only.

<<<PAGE 42>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-16
Network Configuration Specifications 
         
IP Specifications
IP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
791–Internet Protocol
792–Internet Control Message Protocol 
826–An Ethernet Address Resolution Protocol
2784–Generic Routing Encapsulation (GRE)
2890–Key and Sequence Number Extensions to GRE (extensions defined are not supported)
1701–Generic Routing Encapsulation (GRE)
1702–Generic Routing Encapsulation over IPV4 Networks
2003-IP Encapsulation within IP
4292 - IP Forwarding Table MIB
4293 - Management Information Base for the Internet Protocol (IP)
Maximum router 
interfaces per system
128
24
128
128
4K1
4K
4K
4K
4K
4K
4K
4K
4K
4K
Maximum router 
interfaces per VLAN
8
8
16
8
161
16
16
16
16
16
16
16
16
32
Maximum HW routes
256
32
2048
256
16K1
13K
12K
12K (SM)
144K (RM)
96K (ER)
12K
113K (SM)
113K (ER)
312K (RM)
V72 - 12K (SM)
V72 - 128K (RM)
C32 - 12K (SM)
C32 - 128K (RM)
32K (SM)
384K (RM)
192K (ER)
X/T24C2 - 32K (SM)
X/T24C2 - 144K (RM)
X/T24C2 -  96K (ER)
-
128K
116K2
Maximum HW ARP 
entries
256
256
2048
2048
8K1
1536
16K
24K (SM)
16K (RM)
24K (ER)
16K
24K (SM)
64K (ER)
24K (RM)
V72 - 32K (SM)
V72 - 8K (RM)
C32 - 32K (SM)
C32 - 8K (RM)
64K (SM)
16K (RM)
48K (ER)
X/T24C2 - 24K (SM)
X/T24C2 - 16K (RM)
X/T24C2 - 24K (ER)
-
24K
24K(SM)2
64K (ER)2
Maximum HW ARP 
entries in VC of OS6900s 
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
Equal to capacity of 
module with lowest 
number of supported 
ARPs.
Equal to capacity of 
module with lowest 
number of supported 
ARPs.
-
N/A
Maximum number of 
GRE tunnel interfaces per 
VC
N/S
N/S
N/S
1271
127
127
127
127
127
127
127
-
N/S
Maximum number of IPIP 
tunnel interfaces per VC
N/S
N/S
N/S
1271
127
127
127
127
127
127
127
-
N/S

<<<PAGE 43>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-17
Network Configuration Specifications 
         
IP Specifications
Maximum ECMP 
gateways
4
4
4
4
161
-
16
16
16
16
16
16
-
16
Maximum Static Routes 
(Including Black Hole 
Routes)
256
256
256
256
4K1
-
4094
4094
4094
4094
4094
4094
-
4094
Notes:
Values are indicative maximum values based on hardware specifications. They are subject to change per use case or IP Routing configurations)
SM - Switch mode
RM - Router mode 
ER - Edge-router mode
1. With Advanced Routing License
2. OS99-CMM2 and OS99-CNI-U20.
The OmniSwitch can support a higher number of routes than what is documented in the hardware routing limits. This is done by moving older unused routes into software and more recent active routes into hardware. The total number of 
routes supported is dependent upon the switch configuration and the total amount of memory available. Exceeding the maximum hardware routes will result in some traffic being routed in software.

<<<PAGE 44>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-18
Network Configuration Specifications 
         
VRF Specifications
VRF Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of 
MAX profile VRF 
instances per VC (no 
LOW profiles)
N/S
1
1
8
8
64
64
64
64
64
64
64
64
Maximum number of 
LOW profile VRF 
instances per VC (no 
MAX profiles)
N/S
N/S
N/S
16
16
128
128
128
128
128
128
28
300
Maximum VRF instances 
per VLAN
N/S
N/S
N/S
1
1
1
1
1
1
1
1
1
1
Maximum OSPFv2/v3 
VRF routing instances per 
VC
N/S
N/S
1
8
8
16
16
16
16
16
16
16
16
Maximum RIPv2/ng VRF 
routing instances per VC 
N/S
1
1
8
8
16
16
16
16
16
16
16
16
Maximum BGP VRF 
routing instances per VC
N/S
N/S
N/S
N/S
N/S
32
32
32
32
32
32
32
32
Notes:
• OS6570M requires Advanced Routing license.
• Refer to the Configuring Multiple VRF chapter for information on VRF aware applications.

<<<PAGE 45>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-19
Network Configuration Specifications 
         
IPv6 Specifications
IPv6 Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
1981—Path MTU Discovery for IP version 6
2375—IPv6 Multicast Address Assignments
2460—Internet Protocol, Version 6 (IPv6) Specification
2464—Transmission of IPv6 Packets over Ethernet Networks
2465—Management Information Base for IP Version 6: Textual Conventions and General Group
2466—Management Information Base for IP Version 6: ICMPv6 Group
2711—IPv6 Router Alert Option
3056—Connection of IPv6 Domains via IPv4 Clouds
3484—Default Address Selection for Internet Protocol version 6 (IPv6)
3493—Basic Socket Interface Extensions for IPv6
3542—Advanced Sockets Application Program Interface (API) for IPv6
3587—IPv6 Global Unicast Address Format
3595—Textual Conventions for IPv6 Flow Label
3596— DNS Extensions to Support IP Version 6
4007—IPv6 Scoped Address Architecture
4022—Management Information Base for the Transmission Control Protocol (TCP)
4113—Management Information Base for the User Datagram Protocol (UDP)
4193—Unique Local IPv6 Unicast Addresses
4213—Basic Transition Mechanisms for IPv6 Hosts and Routers
4291—IP Version 6 Addressing Architecture
4294—IPv6 Node Requirements
4443—Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6) Specification
4861—Neighbor Discovery for IP version 6 (IPv6)
4862—IPv6 Stateless Address Autoconfiguration
5095—Deprecation of Type 0 Routing Headers in IPv6 
5453—Reserved IPv6 Interface Identifiers
5722—Handling of Overlapping IPv6 Fragments
Maximum IPv6 interfaces 4
4
64
16
4K1
4K
4096
4096
4096
4096
4096
4096
4096
4096
Maximum 6to4 tunnels
N/S
N/S
N/S
11
1
1
1
1
1
1
1
N/S
1
Maximum Configured 
tunnels
N/S
N/S
N/S
2551
255
255
255
255
255
255
255
N/S
255
Maximum IPv6 Hosts 
(Neighbor Discovery)
64
64
128
128
3K1
1536
3K
12K (SM)
8K (RM)
12K (ER)
3K
12K (SM)
16K (ER)
12K (RM)
V72 - 16K (SM)
V72 - 4K (RM)
C32(E) - 16K (SM)
C32(E) - 4K (RM)
32K (SM)
8K (RM)
24K (ER)
X/T24C2 - 12K (SM)
X/T24C2 - 8K (RM)
X/T24C2 - 12K (ER)
-
24K
16K (SM)2
16K (ER)2

<<<PAGE 46>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-20
Network Configuration Specifications 
         
IPv6 Specifications
Maximum IPv6 global 
unicast or anycast 
addresses
4
4
16
16
4K1
-
10K
10K
10K
10K
10K
10K
-
10K
Maximum IPv6 global 
unicast addresses per IPv6 
interface
1
1
1
1
501
1
50
50
50
50
50
50
-
50
Maximum IPv6 hardware 
routes when there are no 
IPv4 routes present 
(includes dynamic, static, 
black hole routes)
32
32
1024
128
8K1
-
1K
(128-bit)
6K
(64-bit)
1K
(128-bit 
SM)
6K
(64-bit SM)
48K
(128-bit 
RM)
72K
(64-bit RM)
1K
(128-bit)
6K (64-bit)
56K (SM)
56K (ER)
156K (RM)
6K (64-bit SM)
64K (64-bit RM)
- 1K (128-bit SM)
64K (128-bit RM)
1K (128-bit SM)
16K (64-bit SM)
X/T24C2 -1K (128-bit 
SM)
6K (64-bit SM)
128K (128-bit RM)
192K (64-bit RM) 
X/T24C2 - 48K (128-bit 
RM)
72K (64-bit RM)
-
32K
58K2
Maximum IPv6 static 
routes (Including black 
hole routes)
4
16
128
128
5121
-
512
512
512
512
512
512
512
512
Maximum number of 
RIPng Peers
N/S
4
10
10
201
20
20
20
20
20
20
20
20
20
Maximum number of 
RIPng Interfaces
N/S
4
10
10
201
20
20
20
20
20
20
20
20
20
Maximum number of 
RIPng Routes
N/S
40
128
128
5K1
2.5K
5K
5K
5K
5K
5K
5K
5K
5K
Maximum ECMP 
gateways
4
4
4
4
161
-
16
16
16
16
16
16
16
16
Notes:
SM - Switch mode
RM - Router mode 
ER - Edge-router mode
(Values are indicative maximum values based on hardware specifications. They are subject to change per use case or IP Routing configurations)
Exceeding the maximum IPv6 hardware routes or having IPv4 routes will result in some traffic being routed in software.
1. With Advanced Routing license.
2. OS99-CMM2 and OS99-CNI-U20 only.

<<<PAGE 47>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-21
Network Configuration Specifications 
         
IPsec Specifications
IPsec Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IP Version Supported
N/S
N/S
N/S
N/S
IPv4, IPv6
RFCs Supported
N/S
N/S
N/S
N/S
4301—Security Architecture for the Internet Protocol
4302—IP Authentication Header (AH)
4303—IP Encapsulating Security Payload (ESP)
4305—Cryptographic Algorithm Implementation Requirements for ESP and AH
4308—Cryptographic Suites for IPsec
Encryption Algorithms 
Supported for ESP
N/S
N/S
N/S
N/S
NULL, 3DES-CBC, and AES-CBC
Key lengths supported for 
Encryption Algorithms
N/S
N/S
N/S
N/S
3DES-CBC - 192 bits
AES-CBC - 128, 192, or 256 bits
Authentication 
Algorithms Supported for 
AH
N/S
N/S
N/S
N/S
HMAC-SHA1-96, HMAC-MD5-96, and AES-XCBC-MAC-96, HMAC-SHA256, HMAC-SHA384, HMAC-
SHA512
Key lengths supported for 
Authentication 
Algorithms
N/S
N/S
N/S
N/S
HMAC-MD5 - 128 bits
HMAC-SHA1 - 160 bits
AES-XCBC-MAC - 128 bits
Master Security Key 
formats
N/S
N/S
N/S
N/S
Hexadecimal (16 bytes) or String (16 characters)
Priority value range for 
IPsec Policy 
N/S
N/S
N/S
N/S
1–1000 (1=highest priority, 1000=lowest priority)
Index value range for 
IPsec Policy Rule
N/S
N/S
N/S
N/S
1–10
SPI Range
N/S
N/S
N/S
N/S
256–999999999
Modes Supported
N/S
N/S
N/S
N/S
Transport
Notes:
N/A

<<<PAGE 48>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-22
Network Configuration Specifications 
         
RIP Specifications
RIP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 1058 - RIP v1
RFC 2453 - RIP v2
RFC 1722 - RIP v2 Protocol Applicability Statement
RFC 1724 - RIP v2 MIB Extension
RFC 2080 - RIPng for IPv6
RFC 2082 - RIP-2 MD5 Authentication
RFC 4822 - RIPv2 Cryptographic Authentication
Maximum Number of 
Interfaces
N/S
8
10
10
10
10
10
10
10
10
10
10
16
Maximum Number of 
Peers
N/S
8
8
8
100*
100
100
100
100
100
100
100
100
16
Maximum Number of 
Routes
N/S
128
256 (1024#) 256 (1024#)
10K*
-
10K
10K
10K
10K
10K
10K
10K
10K
Notes
* With Advanced Routing license.
# With ECMP
Maximum number of routes includes routes redistributed into RIP.

<<<PAGE 49>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-23
Network Configuration Specifications 
         
BFD Specifications
BFD Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
N/S
N/S
5880—Bidirectional Forwarding Detection 
5881—Bidirectional Forwarding Detection for IPv4 and IPv6 (Single Hop)
5882—Generic Application of Bidirectional Forwarding Detection
Maximum Number of 
BFD Sessions
N/S
N/S
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32
VC - 100
Chassis - 32 Chassis - 32
VC - 100
Protocols Supported
N/S
N/S
BGP, OSPF, VRRP Remote Address Tracking only, and Static Routes.
IPv6 protocols not supported.
Modes Supported
N/S
N/S
Asynchronous Echo
(Demand Mode not supported)
Notes:
N/A

<<<PAGE 50>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-24
Network Configuration Specifications 
         
DHCP Relay / Snooping Specifications
DHCP Relay / Snooping Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
0951–Bootstrap Protocol
1534–Interoperation between DHCP and BOOTP
1541–Dynamic Host Configuration Protocol
1542–Clarifications and Extensions for the Bootstrap Protocol
2132–DHCP Options and BOOTP Vendor Extensions
3046–DHCP Relay Agent Information Option, 2001
DHCP Relay 
Implementation
Global DHCP
Per-VLAN DHCP
DHCP Relay Service
BOOTP/DHCP (Bootstrap Protocol/Dynamic Host Configuration Protocol)
UDP Port Numbers
67 for Request
68 for Response
IP addresses supported for 
each Relay Service
256
256
256
256
256
1536
1536
1536
1536
1536
1536
1536
1536
IP addresses supported for 
the Per-interface mode
256
256
256
256
256
1536
1536
1536
1536
1536
1536
1536
1536
Maximum number of 
UDP relay services 
allowed per VC
12
30
30
30
30
30
30
30
30
30
30
30
30
Maximum number of 
VLANs to which 
forwarded UDP service 
port traffic is allowed
256
256
256
256
256
256
256
256
256
256
256
256
256

<<<PAGE 51>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-25
Network Configuration Specifications 
         
DHCPv6 Relay / Snooping Specifications
DHCPv6 Relay / Snooping Specifications
Maximum VLAN level IP 
source filtering entries*
15 VLANs 
with  93 
clients
16 VLANs 
with 31 
clients
32 VLANs 
with 223 
clients
16 VLANs 
with 239 
clients
8 VLANs 
with 247 
clients
4 VLANs 
with 251 
clients
32 VLANs 
with 223 
clients
16 VLANs 
with 239 
clients
8 VLANs 
with 247 
clients
4 VLANs 
with 251 
clients
32 VLANs 
with 223 
clients
16 VLANs 
with 239 
clients
8 VLANs 
with 247 
clients
4 VLANs 
with 251 
clients
32 VLANs 
with 160 
clients
16 VLANs 
with 208 
clients
8 VLANs 
with 232 
clients
4 VLANs 
with 244 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
32 VLANs 
with 160 
clients
16 VLANs 
with 208 
clients
8 VLANs 
with 232 
clients
4 VLANs 
with 244 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239
clients
8 VLANs
with 247
clients
4 VLANs
 with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239
clients
8 VLANs
with 247
clients
4 VLANs
 with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239
clients
8 VLANs
with 247
clients
4 VLANs
 with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239
clients
8 VLANs
with 247
clients
4 VLANs
 with 251 
clients
32 VLANs 
with 223 
clients
16 VLANs 
with 239 
clients
8 VLANs 
with 247 
clients
4 VLANs 
with 251 
clients
Maximum port level IP 
source filtering entries
107 clients
46 clients
254 clients
254 clients
254 clients
253 clients
254 clients
253 clients
254 clients
254 clients
254 clients
254 clients
254 clients
Notes:
*Maximum VLAN-based entries for a VC is equal to the documented values multiplied by the number of VC elements.
*OS6465 - For a linkagg there is one binding entry per member port(s) of the linkagg.
*Other platforms - For a linkagg, there is one binding entry per NI on which there are member port(s) of the linkagg.
*See “OmniSwitch 6870 TCAM Profile Specifications” on page 4-3.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 3315 - Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
DHCP Relay 
Implementation
Per-VLAN DHCP
UDP Destination Port 
Numbers
547 - DHCPv6 messages to a DHCPv6 Server or Relay Agent
546 - DHCPv6 messages to a Client
Maximum Relay 
Destinations per DHCPv6 
Relay Interface
5
Maximum DHCPv6 
snooping VLANs (per 
VLAN mode)
64
64
64
64
64
64
64
64
64
64
64
64
64

<<<PAGE 52>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-26
Network Configuration Specifications 
         
DHCPv6 Relay / Snooping Specifications
Maximum VLAN 
snooping / source filtering 
entries*
8 VLANs 
with 30 
clients.
N/S
16 VLANs
with 64 
clients
8 VLANs
with 72 
clients
4 VLANs
with 76 
clients
1 VLANs
with 79 
clients
16 VLANs
with 64 
clients
8 VLANs
with 72 
clients
4 VLANs
with 76 
clients
1 VLANs
with 79 
clients
16 VLANs
with 64 
clients
8 VLANs
with 72 
clients
4 VLANs
with 76 
clients
1 VLANs
with 79 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
X/T24C2 - 
32 VLANs
with 223 
clients
4 VLANs
with 251 
clients
32 VLANs
with 223 
clients
16 VLANs
with 239 
clients
8 VLANs
with 247 
clients
4 VLANs
with 251 
clients
16 VLANs
with 64 
clients
8 VLANs
with 72 
clients
4 VLANs
with 76 
clients
1 VLANs
with 79 
clients
Maximum port level IP 
source filtering entries
37 clients
N/S
79 clients
79 clients
79 clients
254 clients
254 clients
254 clients
254 clients
254 clients
254 clients
254 clients
79 clients
Maximum DHCPv6 
Guard VLANs
64
64
64
64
64
64
64
64
64
64
X/T24C2 - 
64
64
N/S
Maximum IPv6 Generic 
UDP Relay Services
4
4
8
8
8
8
8
8
8
8
8
8
8
Maximum IPv6 UDP 
Relay Ports
4
4
8
8
8
8
8
8
8
8
8
8
8
Maximum IPv6 UDP 
Destinations per Port
8
8
8
8
8
8
8
8
8
8
8
8
8
Notes:
*Maximum VLAN-based entries for a VC is equal to the documented values multiplied by the number of VC elements.
* See “OmniSwitch 6870 TCAM Profile Specifications” on page 4-3.
Platform specific specifications in other areas may have an impact on these values.

<<<PAGE 53>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-27
Network Configuration Specifications 
         
DHCP Server Specifications
DHCP Server Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 2131—Dynamic Host Configuration Protocol
RFC 3315—Dynamic Host Configuration Protocol for IPv6
RFC 950—Internet Standard Subnetting Procedure
RFC 868—Time Protocol
RFC 1035—Domain Implementation and Specification 
RFC 1191—Path MTU Discovery
DHCP Server 
Implementation
BOOTP/DHCP
UDP Port Numbers
67 for Request and Response (IPv4)
547 for Request (IPv6)
546 for Response (IPv6)
IP address lease allocation 
mechanisms
Static BootP: 
IP address is allocated using the BootP configuration when the MAC address of the client is defined. 
Static DHCP:
The network administrator assigns an IP address to the client. DHCP conveys the address assigned by the DHCP server to the client.
Dynamic DHCP:
The DHCP server assigns an IP address to a client for a limited period of time or until the client explicitly releases the address.
OmniSwitch IPv4 
Configuration Files
dhcpd.conf
dhcpd.pcy
dhcpsrv.db
OmniSwitch IPv6 
Configuration Files
dhcpdv6.conf
dhcpdv6.pcy
dhcpv6srv.db
Maximum number of 
leases
8000
Maximum lease 
information file size
375K
Notes:
N/A

<<<PAGE 54>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-28
Network Configuration Specifications 
         
VRRP Specifications
VRRP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 3768 - Virtual Router Redundancy Protocol
RFC 2787 - Definitions of Managed Objects for the Virtual Router Redundancy Protocol
RFC 5798 - Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6
RFC 6527 - Definitions of Managed Objects for VRRP Version 3 (VRRPv3) IPv6
Maximum number of 
VRRPv2 and VRRPv3 
virtual routers
255
255
255
255
255
255
255
255
255
255
255
255
255
Maximum number of IP 
addresses per instance
16
16
16
16
16
16
16
16
16
16
16
16
16
Notes:
N/A

<<<PAGE 55>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-29
Network Configuration Specifications 
         
Server Load Balancing Specifications
Server Load Balancing Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of 
clusters
N/S
N/S
N/S
N/S
N/S
32
32
32
32
N/S
32
32
N/S
Max. number of physical 
servers per cluster
N/S
N/S
N/S
N/S
N/S
32
32
32
32
N/S
32
32
N/S
Layer-3 classification
Destination IP address
QoS policy condition
Layer-2 classification
QoS policy condition
Server health checking
Ping, link checks
High availability support
Hardware-based failover, VRRP, Chassis Management Module (CMM) redundancy
Networking protocols 
supported
Virtual IP (VIP) addresses
Notes:
N/A

<<<PAGE 56>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-30
Network Configuration Specifications 
         
IPMS Specifications
IPMS Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 1112—Host Extensions for IP Multicasting
RFC 2236—Internet Group Management Protocol, Version 2
RFC 2710—Multicast Listener Discovery (MLD) for IPv6
RFC 2933—Internet Group Management Protocol MIB
RFC 3019—IP Version 6 Management Information Base for The Multicast Listener Discovery Protocol
RFC 3376—Internet Group Management Protocol, Version 3
RFC 3810—Multicast Listener Discovery Version 2 (MLDv2) for IPv6
RFC 4541—Considerations for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Snooping Switches
RFC 4604—Using Internet Group Management Protocol Version 3 (IGMPv3) and Multicast Listener Discovery Protocol Version 2 (MLDv2) for Source-Specific Multicast
IGMP Versions 
Supported
IGMPv1, IGMPv2, IGMPv3
Maximum number of 
IPv4 multicast flows 
(switched)
1K
1K
1K
1K
1K
12K
40K
12K
12K
20K
40K
40K
128K
Maximum number of 
IPv4 multicast flows (*,G 
routed)
N/S
N/S
N/S
1K
1K
12K
12K
12K
12K
20K
40K
X/T24C2 - 12K
40K
16K
Maximum number of 
IPv4 multicast flows (S,G 
routed)
N/S
N/S
N/S
1K
1K
12K
12K
12K
12K
20K
40K
X/T24C2 - 12K
40K
16K
Notes:
N/A

<<<PAGE 57>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-31
Network Configuration Specifications 
         
IPMSv6 Specifications
IPMSv6 Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 2710—Multicast Listener Discovery for IPv6
RFC 3019—IPv6 MIB for Multicast Listener Discovery Protocol
RFC 3306—Unicast-Prefix-based IPv6 Multicast Addresses
RFC 3810—Multicast Listener Discovery Version 2 for IPv6
RFC 4541—Considerations for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Snooping Switches
RFC 4604—Using Internet Group Management Protocol Version 3 (IGMPv3) and Multicast Listener Discovery Protocol Version 2 (MLDv2) for Source-Specific Multicast
MLD Versions Supported
MLDv1, MLDv2
MLD Query Interval
1–65535 in seconds
MLD Router Timeout
1–65535 in seconds
MLD Source Timeout
1–65535 in seconds
MLD Query Response 
Interval
1–65535 in milliseconds
MLD Last Member Query 
Interval
1–65535 in milliseconds
Maximum number of 
IPv6 multicast flows 
(switched)
1K
1K
1K
1K
1K
6K
20K
6K
6K
10K
20K
20K
128K
Maximum number of 
IPv6 multicast flows (*,G 
routed)
N/S
N/S
N/S
1K
1K
6K
6K
6K
6K
10K
20K
X/T24C2 - 6K
20K
16K
Maximum number of 
IPv6 multicast flows (S,G 
routed)
N/S
N/S
N/S
1K
1K
6K
6K
6K
6K
10K
20K
X/T24C2 - 6K
20K
16K
Notes:
N/A

<<<PAGE 58>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-32
Network Configuration Specifications 
         
QoS Specifications
QoS Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of 
policy rules
128
128
384
384
384
3072
3072
3072
2K (4K*)
4K
4K
X/T24C2 - 3072
4K
1024
Max. number of policy 
conditions
128
128
384
384
384
3072
3072
3072
2K (4K*)
4K
4K
X/T24C2 - 3072
4K
1024
Maximum number of 
policy actions
128
128
384
384
384
3072
3072
3072
2K (4K*)
4K
4K
X/T24C2 - 3072
4K
1024
Maximum number of 
groups (network, MAC, 
service, port)
2047
2047
2047
2047
2047
1024
1024
1023
2047
2047
2047
X/T24C2 - 1024
2047
2047
Maximum number of 
group entries
128
128
384 per 
group (256 
per service 
group)
384 per 
group (256 
per service 
group)
384 per 
group (256 
per service 
group)
1024 per 
group (256 
per service 
group)
1024 per 
group (256 
per service 
group)
1024 per 
group (256 
per service 
group)
1024 per 
group (256 
per service 
group)
1024 per 
group
1024 per group
1024 per 
group
1024 per 
group (256 
per service 
group)
Maximum number of 
Class of Service (CoS) 
queues per port.
8
8
8
8
8
8
8
8
8
8
8
8
8
Queue Set Profiles (QSP)
2
2
2
2
2
4
4
4
2
4
4
NBDC-2, 
DCB-4
4
Weighted Random Early 
Detection profiles 
(WRED)
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Maximum number of QoS 
policy lists
32 (does not include the default list)
Maximum number of QoS 
policy lists per Universal 
Network Profile (UNP)
1
Notes:
*Refer to the qos-acl TCAM profile for 4K support of User Policy Rules. See “TCAM Profiles” on page 4-1.

<<<PAGE 59>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-33
Network Configuration Specifications 
         
LDAP Policy Server Specifications
LDAP Policy Server Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 2251–Lightweight Directory Access Protocol (v3)
RFC 3060–Policy Core Information Model—Version 1 Specification
Maximum number of 
policy servers (supported 
on a VC)
5
Maximum number of 
policy servers (supported 
by PolicyView)
1
Notes:
N/A

<<<PAGE 60>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-34
Network Configuration Specifications 
         
Authentication Server Specifications
Authentication Server Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RADIUS RFCs 
Supported
RFC 2865–Remote Authentication Dial In User Service (RADIUS)
RFC 2866–RADIUS Accounting
RFC 2867–RADIUS Accounting Modifications for Tunnel Protocol Support
RFC 2868–RADIUS Attributes for Tunnel Protocol Support
RFC 2809–Implementation of L2TP Compulsory Tunneling through RADIUS
RFC 2869–RADIUS Extensions
RFC 2548–Microsoft Vendor-specific RADIUS Attributes
RFC 2882–Network Access Servers Requirements: Extended RADIUS Practices
TACACS+ RFCs 
Supported
RFC 1492–An Access Control Protocol
LDAP RFCs Supported
RFC 1789–Connectionless Lightweight X.5000 Directory Access Protocol
RFC 2247–Using Domains in LDAP/X.500 Distinguished Names
RFC 2251–Lightweight Directory Access Protocol (v3)
RFC 2252–Lightweight Directory Access Protocol (v3): Attribute Syntax Definitions
RFC 2253–Lightweight Directory Access Protocol (v3): UTF-8 String Representation of Distinguished Names
RFC 2254–The String Representation of LDAP Search Filters
RFC 2256–A Summary of the X.500(96) User Schema for Use with LDAPv3
Other RFCs
RFC 2574–User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3)
RFC 2924–Accounting Attributes and Record Formats
RFC 2975–Introduction to Accounting Management
RFC 2989–Criteria for Evaluating AAA Protocols for Network Access
Maximum number of 
authentication servers in 
single authority mode
4
8
Maximum number of 
authentication servers in 
multiple authority mode
4
8
Maximum number of 
servers per Authenticated 
Switch Access type
4
8
Notes:
N/A

<<<PAGE 61>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-35
Network Configuration Specifications 
         
UNP Specifications
UNP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Number of UNPs 
(profiles) per VC
4K
4K
4K
4K
4K
4K
4K
4K
4K
4K
4K
4K
2K
Number of UNP users per 
chassis
128
80
256
256
300*
2K
2K
2K
2K*
2K
2K
1K
1K
Number of UNP users per 
VC
10241
3201
2K1
2K1
1.2K*
2K2
2K2
2K2
2K*, 2
2K2
2K2
1K
2K1
Authentication type
MAC and 802.1x authentication
Profile type
VLAN
VLAN and SPB service
VLAN, SPB and VXLAN service
VLAN, 
SPB
UNP port type
Bridge
Bridge, Access
Bridge, 
Access
Number of QoS policy 
lists per VC
32 (includes the default list)
Number of QoS policy 
lists per UNP
1
Notes:
• Number of UNPs per VC includes static and dynamic profiles.
• The maximum entries may be lower depending on any LPS or QoS configuration. 
*UNP users supported with default TCAM Profile. See “TCAM Profiles” on page 4-1.
1. Number of users per chassis multiplied by the maximum number of chassis in VC.
2. The maximum number of users per VC does not increase with additional chassis. The combined total for each chassis cannot exceed this value.

<<<PAGE 62>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-36
Network Configuration Specifications 
         
Access Guardian Specifications
Access Guardian Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC 2284–PPP Extensible Authentication Protocol (EAP)
RFC 2865–Remote Authentication Dial In User Service (RADIUS)
RFC 2866–RADIUS Accounting
RFC 2867–RADIUS Accounting Modifications for Tunnel Protocol Support
RFC 2868–RADIUS Attributes for Tunnel Protocol Support
RFC 2869–RADIUS Extensions 
RFC 3576--Change of Authorization-Request (COA) and Disconnect request (DM) for BYOD. RFC support is limited to ClearPass solution. 
RFC 3579–RADIUS Support for EAP
IEEE Standards 
Supported
IEEE 802.1X-2001–Standard for Port-based Network Access Control
802.1X RADIUS Usage Guidelines
Authentication methods 
supported
802.1X, MAC address, Captive Portal
Maximum number of 
Access Guardian users 
(system)
512
320
1K
1K
-
1K
1K
1K
1K (NI)
2K (VC)
1K
1K
-
1K
Maximum number of 
users quarantined by 
QMR
N/S
256
256
256
-
1K
1K
1K
1K (NI)
2K (VC)
1K
1K
-
256
Average number of users 
allowed to login to 
Captive portal Web pages 
at any given time
40
Maximum number of 
Captive Portal profiles
8
Maximum number of 
AAA profiles
8
Maximum number of 
authentication servers
4 per authentication type (MAC, 802.1X, Captive Portal)
Maximum number of 
accounting servers
4 per authentication type (MAC, 802.1X, Captive Portal)
BYOD Solution Server
ClearPass Policy Manager (CPPM) / UPAM
mDNS GRE Tunnel 
Supported Protocol
IPv4
IPv4
IPv4
IPv4
-
IPv4
IPv4
IPv4
IPv4
IPv4
IPv4
-
IPv4

<<<PAGE 63>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-37
Network Configuration Specifications 
         
AppMon Specifications
AppMon Specifications
SSDP GRE Tunnel 
Supported Protocol
IPv4
IPv4
IPv4
IPv4
-
IPv4
IPv4
IPv4
IPv4
IPv4
IPv4
-
IPV4
Maximum L2 GRE 
Access Tunnels 
N/S
N/S
8
8
-
1
1
1
1
1
1
-
1
Maximum L2 GRE 
Aggregation Tunnels 
N/S
N/S
N/S
N/S
-
2K
2K
2K
2K
8K
8K
2K 
(X/T24C2)
-
1K
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Packet types sampled
N/S
N/S
N/S
N/S
N/S
TCP and 
UDP
TCP and 
UDP
N/S
TCP and 
UDP
N/S
N/S
N/S
N/S
Notes:
AppMon is supported in a virtual chassis of OmniSwitch 6860 and OmniSwitch 6860E platforms where at least one OmniSwitch 6860E is mandatory for the feature to work.

<<<PAGE 64>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-38
Network Configuration Specifications 
         
Application Fingerprinting Specifications
Application Fingerprinting Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS9900
Packet sampling rate
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Packet types sampled
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Notes:
Currently not supported.

<<<PAGE 65>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-39
Network Configuration Specifications 
         
Port Mapping Specifications
Port Mapping Specifications
Learned Port Security Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Port Mapping Sessions
8
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Ports eligible for Learned 
Port Security
Fixed and 802.1Q tagged
Ports not eligible for 
Learned Port Security
Link aggregate ports.
802.1Q (trunked) link aggregate ports.
Maximum number of 
learned MAC addresses 
allowed per LPS port
1000
Maximum number of 
filtered MAC addresses 
allowed per LPS port
100
Maximum number of 
configurable MAC 
address ranges per LPS 
port
8
Notes:
N/A

<<<PAGE 66>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-40
Network Configuration Specifications 
         
Port Mirroring Specifications
Port Mirroring Specifications
Port Monitoring Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Mirroring Sessions 
Supported
2
7
7
7
7
4
4
4
7
4
4
4
7
Combined Mirroring/
Monitoring Sessions per 
Chassis
2
7
7
7
7
4
4
4
7
4
4
4
7
N-to-1 Mirroring 
Supported
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
128 to 1
Maximum No. of 
mirroring destinations per 
session supported 
1
1
1
1
1
2
2
2
1
2
2
2
128
Number of RPMIR 
VLANs per session
1
1
1
1
1
1
1
1
1
1
1
1
1
Notes:
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Monitoring Sessions 
Supported
1
1
1
1
1
1
1
1
1
1
1
1
1
Combined Mirroring/
Monitoring Sessions per 
Chassis
2
7
7
7
7
2
2
2
7
2
2
2
7
File Type Supported
ENC file format (Network General Sniffer Network Analyzer Format)

<<<PAGE 67>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-41
Network Configuration Specifications 
         
Port Monitoring Specifications
Notes:
N/A

<<<PAGE 68>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-42
Network Configuration Specifications 
         
sFlow Specifications
sFlow Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
3176—sFlow Management Information Base
Receiver/Sampler/Polling 
Instances
2
Sampling
length of packet
type of frame
source and destination MACs
source and destination VLANs
source and destination priorities
source and destination IP addresses 
source and destination ports
tcp flags and tos
Polling
In octets
Out octets
Number of Rx Unicast packets
Number of Tx Unicast packets
Number of Rx Multicast packets
Number of Tx Multicast packets
Number of Rx Broadcast packets
Number of Tx Broadcast packets
In Errors
Out Errors
Notes:
N/A

<<<PAGE 69>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-43
Network Configuration Specifications 
         
RMON Specifications
RMON Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
2819 - Remote Network Monitoring Management Information Base
RMON Functionality 
Supported
Basic RMON 4 group implementation
–Ethernet Statistics group
–History (Control and Statistics) group
–Alarms group
–Events group
RMON Functionality Not 
Supported
RMON 10 group*
RMON2*
–Host group
–HostTopN group
–Matrix group
–Filter group
–Packet Capture group
(*An external RMON probe that includes RMON 10 group and RMON2 be used where full RMON probe functionality is required.)
Flavor (Probe Type)
Ethernet/History/Alarm
Status
Active/Creating/Inactive
History Control Interval 
(seconds)
1–3600
History Sample Index 
Range
1–65535
Alarm Interval (seconds)
1–2147483647
Alarm Startup Alarm
Rising Alarm/Falling Alarm/
RisingOrFalling Alarm
Alarm Sample Type
Delta Value/Absolute
RMON Traps Supported
RisingAlarm/FallingAlarm
These traps are generated whenever an Alarm entry crosses either its Rising Threshold or its Falling Threshold and generates an event configured for sending SNMP traps.
Notes:
N/A

<<<PAGE 70>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-44
Network Configuration Specifications 
         
Switch Health Specifications
Switch Health Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Health Functionality 
Supported
–Switch level CPU Utilization Statistics (percentage);
–Switch/module/port level Input Utilization Statistics (percentage);
–Switch/module/port level Input/Output Utilization Statistics (percentage);
–Switch level Memory Utilization Statistics (percentage);
–Device level (for example, Chassis/CMM) Temperature Statistics (Celsius).
Monitored Resource 
Utilization Levels
–Most recent utilization level;
–Average utilization level during last minute;
–Average utilization level during last hour;
–Maximum utilization level during last hour.
Resource Utilization Raw 
Sample Values
Saved for previous 60 seconds.
Resource Utilization 
Current Sample Values
Stored.
Resource Utilization 
Maximum Utilization 
Value
Calculated for previous 60 seconds and stored.
Utilization Value = 0
Indicates that none of the resources were measured for the period.
Utilization Value = 1
Indicates that a non-zero amount of the resource (less than 2%) was measured for the period.
Percentage Utilization 
Values
Calculated based on Resource Measured During Period/Total Capacity.
Resource Threshold 
Levels
Apply automatically across all levels of switch (switch/module/port).
Rising Threshold 
Crossing
A Resource Threshold was exceeded by its corresponding utilization value in the current cycle.
Falling Threshold 
Crossing
A Resource Threshold was exceeded by its corresponding utilization value in the previous cycle, but is not exceeded in the current cycle.
Threshold Crossing Traps 
Supported
Device, module, port-level threshold crossings.
Notes:
N/A

<<<PAGE 71>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-45
Network Configuration Specifications 
         
VLAN Stacking Specifications
VLAN Stacking Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Standards supported IEEE 802.1Q, 2003 Edition, IEEE Standards for Local and Metropolitan Area Networks—Virtual Bridged Local Area Networks
P802.1ad/D6.0 (C/LM) Standard for Local and Metropolitan Area Networks—Virtual Bridged Local Area Networks–Amendment 4: Provider Bridges
Maximum number of 
services
N/S
4
4
4
4
4
4
4
4
4
4
4
N/S
Maximum number of 
SVLANs
N/S
4K
4K
4K
4K
4K
4K
4K
4K
4K
4K
4K
N/S
Maximum number of 
SAPs
N/S
8K
8K
8K
8K
8K
8K
8K
8K
8K
8K
8K
N/S
Maximum number of 
SAP profiles
N/S
8K
8K
8K
8K
8K
8K
8K
8K
8K (1K if 
profiles 
assign 
priority or 
bandwidth)
8K (1K if 
profiles 
assign 
priority or 
bandwidth)
8K (1K if 
profiles 
assign 
priority or 
bandwidth)
N/S
Maximum number of 
SAP profile VLAN 
translation or double 
tagging rules
N/S
-
-
-
-
-
-
-
-
8K
8K
8K
N/S
Maximum number of 
customer VLANs 
(CVLANs) associated 
with a SAP
N/S
4K
4K
4K
4K
4K
3.5K
4K
4K
4K
4K
4K
N/S
Maximum number of 
customer VLANs 
(CVLANs) per VC.
N/S
-
-
-
-
-
-
-
-
8192
8192
8192
-
Maximum number of 
service-to-SAP 
associations
N/S
1K
1K
1K
1K
1K
1K
1K
1K
-
-
-
N/S
Maximum supported 
SAP-UNI-CVLAN 
N/S
127
127
127
127
4K
480
4K
4K
512
3072
X24C2/
T24C2 - 
512
3072
N/S
Notes:
N/A

<<<PAGE 72>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-46
Network Configuration Specifications 
         
Switch Logging Specifications
Switch Logging Specifications
Ethernet OAM Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
RFC-5424 Syslog Protocol
Functionality Supported
High-level event logging mechanism that forwards requests from applications to enabled logging devices.
Number of Syslog Servers 
Supported
12
Logging Devices
Flash Memory/Console/IP Address
Severity Levels/Types 
Supported
2 (Alarm - highest severity), 3 (Error), 
4 (Alert), 5 (Warning) 6 (Info - default), 
7 (Debug 1), 8 (Debug 2), 9 (Debug 3 - lowest severity)
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Standards Supported
N/S
IEEE 802.1ag Version 8.1–Connectivity Fault Management
IEEE 802.1D–Media Access Control (MAC) Bridges
IEEE 802.1Q–Virtual Bridged Local Area Networks
ITU-T Y.1731–OAM Functions and Mechanisms for Ethernet-Based Networks
N/S
Maximum Maintenance 
Domains (MD) per Bridge
N/S
8
N/S
Maximum Maintenance 
Associations (MA) per Bridge
N/S
128
N/S
Maximum Maintenance End 
Points (MEP) per Bridge
N/S
256
N/S

<<<PAGE 73>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-47
Network Configuration Specifications 
         
Link OAM Specifications
Link OAM Specifications
Maximum MEP CMM 
Database Size
N/S
1K
N/S
Minimum CCM interval
N/S
100ms
N/S
Notes:
Ethernet OAM is not supported on the OS6360 or OS9900.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
IEEE Standards 
Supported
IEEE 802.3ah–EFM LINK OAM
RFC 4878 - Definitions and Managed Objects for Operations, Administration, and Maintenance (OAM) functions on Ethernet-Like Interfaces.
Platforms Supported
N/S
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
N/S
N/S
N/S
N/S
Maximum LINK OAM 
instances per VC
N/S
-
Maximum loopback 
sessions
N/S
- 
Maximum event logs
N/S
-
Mirroring ports
LINK OAM is not supported on mirroring ports.
Notes:
N/A

<<<PAGE 74>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-48
Network Configuration Specifications 
         
CPE Testhead Specifications
CPE Testhead Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Test Supported
N/S
Unidirection
al and 
bidirectional 
ingress test
Unidirectio
nal and 
bidirectiona
l ingress 
test
Unidirectio
nal and 
bidirectiona
l ingress 
test
Unidirectio
nal and 
bidirectiona
l ingress 
test
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Maximum number of test 
ID per switch
N/S
32
32
32
32
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Number of active tests 
allowed per switch
N/S
1
1
1
1
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Supported test roles
N/S
Generator or 
Analyzer or 
Loopback
Generator 
or Analyzer 
or 
Loopback
Generator 
or Analyzer 
or 
Loopback
Generator 
or Analyzer 
or 
Loopback
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Test mode supported
N/S
Ingress UNI
Ingress UNI Ingress UNI Ingress UNI N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Test traffic direction 
supported 
N/S
Unidirection
al and 
bidirectional
Unidirectio
nal and 
bidirectiona
l
Unidirectio
nal and 
bidirectiona
l
Unidirectio
nal and 
bidirectiona
l
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Notes:
N/A

<<<PAGE 75>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-49
Network Configuration Specifications 
         
PPPoE-IA Specifications
PPPoE-IA Specifications
SAA Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Maximum number of 
options 
supported for Circuit-
Identifier
N/S
5
5
5
5
N/S
N/S
5
N/S
N/S
N/S
N/S
N/S
Maximum Circuit-
Identifier
length supported
N/S
63 Bytes
63 Bytes
63 Bytes
63 Bytes
N/S
N/S
63 Bytes
N/S
N/S
N/S
N/S
N/S
Maximum Remote-
Identifier length 
supported
N/S
63 Bytes
63 Bytes
63 Bytes
63 Bytes
N/S
N/S
63 Bytes
N/S
N/S
N/S
N/S
N/S
Notes:
N/A
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Platforms Supported
Supported
Supported
N/S
N/S
Supported
Supported
Supported
Supported
Supported
Supported
Supported
Supported
N/S
Maximum number of 
SAAs
128
128
N/S
N/S
128
128
128
128
128
128
128
128
N/S
Maximum SAA SPB 
sessions
N/S
N/S
N/S
N/S
128
(per 
BVLAN)
128
(per 
BVLAN)
128
(per 
BVLAN)
128
(per 
BVLAN)
128
(per 
BVLAN)
128
(per 
BVLAN)
128
(per 
BVLAN)
128
(per 
BVLAN)
320
(per 
BVLAN)
Notes:
N/A

<<<PAGE 76>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 2-50
Network Configuration Specifications 
         
MRP Specifications
MRP Specifications
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
Platforms Supported
N/S
Supported
N/S
N/S
Supported
N/S
N/S
Supported
N/S
N/S
N/S
N/S
N/S
IEEE Standards 
Supported
IEC 62439-2:2016 Media Redundancy Protocol
Maximum Number of 
rings 
N/S
3
N/S
N/S
3
N/S
N/S
3
N/S
N/S
N/S
N/S
N/S
Maximum Nodes in Ring N/S
50
N/S
N/S
50
N/S
N/S
50
N/S
N/S
N/S
N/S
N/S
Maximum Reconfig Time N/S
200Ms and 
500Ms
N/S
N/S
200Ms and 
500Ms
N/S
N/S
200Ms and 
500Ms
N/S
N/S
N/S
N/S
N/S
Notes:
N/A

<<<PAGE 77>>>
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 3-1
3   Advanced Routing
Configuration Specifications
This chapter provides Specifications tables for the following OmniSwitch features that are used to set up 
and monitor advanced routing protocols for operation in a live network environment:
• Routing technologies.
– Open Shortest Path First (OSPF), version 2 and version 3.
– Intermediate System-to-Intermediate System (IS-IS).
– Border Gateway Protocol (BGP).
• Multicast routing protocols.
– Multicast boundaries that are used to confine scoped multicast addresses to a specific domain.
– Distance Vector Multicast Routing Protocol (DVMRP)
– Protocol-Independent Multicast (PIM)
– Multicast Border Router (MBR) functionality as defined in the PIM-SM specification (RFC 4601)
For information about how to configure advanced routing protocols, refer to the OmniSwitch AOS Release 
8 Advanced Routing Configuration Guide.
Note. The OmniSwitch can support a higher number of routes than what is documented in the protocol 
routing tables. The values documented are based on typical scenarios and validated during the AOS test 
phase. The total number of routes supported is dependent upon the switch configuration and the total 
amount of memory available.
Note. A Virtual Chassis is a group of switches managed as a single logical chassis. Any maximum 
limitation values documented apply to the entire Virtual Chassis and not to each individual switch unless 
stated otherwise.

<<<PAGE 78>>>
Advanced Routing Configuration Specifications
In This Chapter
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 3-2
In This Chapter
This chapter contains the following Advanced Routing Specifications tables:
• “OSPF Specifications” on page 3-3.
• “OSPFv3 Specifications” on page 3-4.
• “IS-IS Specifications” on page 3-5.
• “BGP Specifications” on page 3-6.
• “Multicast Boundary Specifications” on page 3-7.
• “DVMRP Specifications” on page 3-8.
• “PIM Specifications” on page 3-9.
• “MBR Specifications” on page 3-10.

<<<PAGE 79>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-3
Advanced Routing Configuration Specifications 
         
OSPF Specifications
OSPF Specifications
The following Specifications table contains information for the OmniSwitch implementation of Open Shortest Path First (OSPF) routing protocol. Note that any maximum limits provided in the table are subject 
to available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs supported
1370 - Applicability Statement for OSPF
4750 - OSPF Version 2 Management Information Base
2328 - OSPF Version 2
5250 - The OSPF Opaque LSA Option
3101 - The OSPF Not-So-Stubby Area (NSSA) Option
3623 - Graceful OSPF Restart
5709 - OSPFv2 HMAC-SHA Cryptographic Authentication
Maximum number of 
areas
N/S
N/S
2
8
8
4
10
4
10
10
10
10
15
Maximum number of 
interfaces
N/S
N/S
8
128
128
128
200
128
200
128
128
128
200
Maximum number of 
passive interfaces
N/S
N/S
8
200
200
200
200
200
200
200
200
200
200
Maximum number of 
Link State Database 
entries
N/S
N/S
1K
20K
20K
20K
100K
20K
100K
100K
100K
100K
100K
Maximum number of 
neighbors
N/S
N/S
8
128
128
128
254
128
254
254
254
254
200
Maximum number of 
routes
N/S
N/S
512
32K
32K
32K
32K
32K
32K
32K
32K
32K
64K
Maximum number of 
ECMP next hop entries
N/S
N/S
16
16
16
16
16
16
16
16
16
16
16
Notes:
• The maximum number of routes value may vary depending on the number of interfaces/neighbors.
• OS6570M requires Advanced Routing license.

<<<PAGE 80>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-4
Advanced Routing Configuration Specifications 
         
OSPFv3 Specifications
OSPFv3 Specifications
The following Specifications table contains information for the OmniSwitch implementation of Open Shortest Path First version 3 (OSPFv3) routing protocol. Note that any maximum limits provided in the table 
are subject to available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs supported
RFC 1826—IP Authentication Header
RFC 1827—IP Encapsulating Security Payload
RFC 2553—Basic Socket Interface Extensions for IPv6
RFC 2373—IPv6 Addressing Architecture
RFC 2374—An IPv6 Aggregatable Global Unicast Address Format
RFC 2460—IPv6 base specification
RFC 2740—OSPF for IPv6
RFC 5643—Management Information Base for OSPFv3
Maximum number of 
areas
N/S
N/S
2
5
5
4
5
4
5
5
5
5
5
Maximum number of 
interfaces
N/S
N/S
8
128
128
128
128
128
128
128
128
128
128
Maximum number of 
Link State Database 
entries
N/S
N/S
-
20K
20K
20K
20K
20K
20K
20K
20K
20K
20K
Maximum number of 
neighbors
N/S
N/S
8
128
128
128
128
128
128
128
128
128
128
Maximum number of 
routes
N/S
N/S
256
32K
32K
32K
32K
32K
32K
10K
10K
10K
10K
Maximum number of 
ECMP next hop entries
N/S
N/S
16
16
16
16
16
16
16
16
16
16
Notes:
The maximum number of routes may vary depending on the number of interfaces/neighbors.
OS6570M requires Advanced Routing license.

<<<PAGE 81>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-5
Advanced Routing Configuration Specifications 
         
IS-IS Specifications
IS-IS Specifications
The following Specifications table contains information for the OmniSwitch implementation of the Intermediate System-to-Intermediate System (IS-IS) routing protocol. Note that any maximum limits provided 
in the table are subject to available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
1142-OSI IS-IS Intra-domain Routing Protocol
1195-OSI IS-IS for Routing in TCP/IP and Dual Environments
3373-Three-Way Handshake for Intermediate System to Intermediate System (IS-IS) Point- to-Point Adjacencies 
3567-Intermediate System to Intermediate System (IS-IS) Cryptographic Authentication 
2966-Prefix Distribution with two-level IS-IS (Route Leaking) support 
2763-Dynamic Host name exchange support
3719-Recommendations for Interoperable Networks using IS-IS 
3787-Recommendations for Interoperable IP Networks using IS-IS
5308-IS-IS support for IPv6 (Routing IPv6 with IS-IS)
IETF Internet-Drafts 
Supported
draft-ietf-isis-igp-p2p-over-lan-05.txt-Point-to-point operation over LAN in link-state routing protocols 
Maximum number of 
areas
N/S
N/S
N/S
3
N/S
3
3
3
3
3
3
3
3
Maximum number of L1 
adjacencies per interface
N/S
N/S
N/S
70
N/S
70
70
70
70
70
70
70
70
Maximum number of L2 
adjacencies per interface
N/S
N/S
N/S
70
N/S
70
70
70
70
70
70
70
70
Maximum number of IS-
IS interfaces
N/S
N/S
N/S
70
N/S
70
70
70
70
70
70
70
70
Maximum number of 
Link State Packet entries 
(per adjacency)
N/S
N/S
N/S
255
N/S
255
255
255
255
255
255
255
255
Maximum number of IS-
IS routes
N/S
N/S
N/S
24K
N/S
24K
24K
24K
24K
24K
24K
24K
24K
Maximum number of IS-
IS L1 routes
N/S
N/S
N/S
12K
N/S
12K
12K
12K
12K
12K
12K
12K
12K
Maximum number of IS-
IS L2 routes
N/S
N/S
N/S
12K
N/S
12K
12K
12K
12K
12K
12K
12K
12K
Notes:
- OS6570M requires Advanced Routing license.

<<<PAGE 82>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-6
Advanced Routing Configuration Specifications 
         
BGP Specifications
BGP Specifications
The following Specifications table contains information for the OmniSwitch implementation of the Border Gateway Protocol (BGP) routing protocol. Note that any maximum limits provided in the table are 
subject to available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
1771/4271–A Border Gateway Protocol 4 (BGP-4)
2439–BGP Route Flap Damping
3392/5492–Capabilities Advertisement with BGP-4
2385–Protection of BGP Sessions via the TCP MD5 Signature Option
1997–BGP Communities Attribute
4456–BGP Route Reflection: An Alternative to Full Mesh Internal BGP (IBGP)
3065–Autonomous System Confederations for BGP
4273–Definitions of Managed Objects for BGP-4
4486–Subcodes for BGP Cease Notification
4760–Multiprotocol Extensions for BGP-4
2545–Use of BGP-4 Multiprotocol Extensions for IPv6 Inter-Domain Routing
2918 - Route Refresh Capability for BGP-4
4724 - Graceful Restart Mechanism for BGP
6793 - BGP 4-octet ASN
5668 - 4-Octet AS Specific BGP Extended Community
2042 - Registering New BGP Attribute Types
5396 -Textual Representation of Autonomous System (AS) Numbers
BGP Attributes Supported Origin, AS Path, Next Hop (IPv4), MED, Local Preference, Atomic Aggregate, Aggregator (IPv4), Community, Originator ID, Cluster List, Multiprotocol Reachable NLRI (IPv6), 
Multiprotocol Unreachable NLRI (IPv6), AS4 Path, AS4 Aggregator (IPv4), and AS Specific Extended Community.
Maximum number of 
peers (32 peers per VRF)
N/S
N/S
32
512
N/S
512
512
512
512
512
512
512
512
Maximum number of 
networks
N/S
N/S
1K
4K
N/S
4K
4K
4K
4K
4K
4K
4K
4K
Maximum number of 
aggregation addresses
N/S
N/S
512
2K
N/S
2K
2K
2K
2K
2K
2K
2K
2K
Maximum number of 
routes
N/S
N/S
2K
32K
N/S
128K
128K
128K
128K
128K
128K
128K
256K
Maximum number of 
policies
N/S
N/S
512
1K
N/S
1K
1K
1K
1K
1K
1K
1K
1K
Notes:
OS6560 and OS6570M require Advanced Routing license.

<<<PAGE 83>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-7
Advanced Routing Configuration Specifications 
         
Multicast Boundary Specifications
Multicast Boundary Specifications
The following Specifications table contains information for the OmniSwitch implementation of multicast address boundary functionality. Note that any maximum limits provided in the table are subject to 
available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
N/S
N/S
N/S
N/S
2365—Administratively Scoped IP Multicast
5132 - IP Multicast MIB
Valid Scoped Address 
Range
N/S
N/S
N/S
N/S
239.0.0.0 to 239.255.255.255
Valid extended Multicast 
route boundary Address 
Range
N/S
N/S
N/S
N/S
224.0.0.0 to 239.255.255.255
Notes:
• If software routing is used, the number of total flows supported is variable, depending on the number of flows and the number of routes per flow.

<<<PAGE 84>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-8
Advanced Routing Configuration Specifications 
         
DVMRP Specifications
DVMRP Specifications
The following Specifications table contains information for the OmniSwitch implementation of the Distance Vector Multicast Routing Protocol (DVMRP). Note that any maximum limits provided in the table are 
subject to available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
N/S
N/S
N/S
N/S
N/S
1075—Distance Vector Multicast Routing Protocol, Version1
4087—IP Tunnel MIB
2715—Interoperability Rules for Multicast Routing Protocols
N/S
N/S
IETF Internet-Drafts 
Supported
N/S
N/S
N/S
N/S
N/S
draft-ietf-idmr-dvmrp-v3-09.txt - Distance Vector Multicast Routing Protocol, 
Version 3
N/S
N/S
DVMRP version 
supported
N/S
N/S
N/S
N/S
N/S
DVMRPv3.255
N/S
N/S
DVMRP attributes 
supported
N/S
N/S
N/S
N/S
N/S
Reverse Path Multicasting, Neighbor Discovery, Multicast Source Location, 
Route Report Messages, Distance metrics, Dependent Downstream Routers, 
Poison Reverse, Pruning, Grafting, DVMRP Tunnels
N/S
N/S
DVMRP timers supported N/S
N/S
N/S
N/S
N/S
Flash update interval, Graft retransmissions, Neighbor probe interval, Neighbor 
timeout, Prune lifetime, Prune retransmission, Route report interval, Route hold-
down, Route expiration timeout
N/S
N/S
Maximum number of 
interfaces
N/S
N/S
N/S
N/S
N/S
384 (Maximum 384 combined Multicast Interfaces between PIMv4, PIMv6 and 
DVMRP.)
N/S
N/S
Multicast protocols per 
interface
N/S
N/S
N/S
N/S
N/S
1 (PIM and DVMRP cannot be enabled on the same interface.)
N/S
N/S
Notes:
N/A

<<<PAGE 85>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-9
Advanced Routing Configuration Specifications 
         
PIM Specifications
PIM Specifications
The following Specifications table contains information for the OmniSwitch implementation of the Protocol-Independent Multicast (PIM) routing protocol. Note that any maximum limits provided in the table are 
subject to available system resources.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
N/S
N/S
2365—Administratively Scoped IP Multicast
4601—Protocol Independent Multicast-Sparse Mode (PIM-SM) Protocol Specification
4007—IPv6 Scoped IP Multicast
5060—Protocol Independent Multicast MIB
5132—IP Multicast MIB
3569—An Overview of Source-Specific Multicast (SSM)
3973—Protocol Independent Multicast-Dense Mode (PIM-DM)
5015 - Bidirectional Protocol Indpendent Multicast (BIDIR-PIM)
5059—Bootstrap Router (BSR) Mechanism for PIM
5240—Protocol Independent Multicast (PIM) Bootstrap Router MIB
2715—Interoperability Rules for Multicast Routing Protocols
PIM-SM version 
supported
N/S
N/S
PIM-SMv2
PIM attributes supported
N/S
N/S
Shared trees (also referred to as RP trees)
Designated Routers (DRs)
Designated Forwarders (DFs)
Bootstrap Routers (BSRs)
Candidate Bootstrap Routers (C-BSRs)
Rendezvous Points (RPs) (applicable only for PIM-SM) and BIDIR-PIM
Candidate Rendezvous Points (C-RPs)
PIM timers supported
N/S
N/S
C-RP expiry, C-RP holdtime, C-RP advertisement, Join/Prune, Probe, Register suppression, Hello, Expiry, Assert, Neighbor liveness, DF Election Timer
Maximum PIM interfaces
N/S
N/S
384 (Maximum 384 combined Multicast Interfaces between PIMv4, PIMv6 and DVMRP.) 
Maximum Rendezvous 
Point (RP)
N/S
N/S
100
Maximum Bootstrap 
Routers (BSRs)
N/S
N/S
1
Multicast Protocols per 
Interface
N/S
N/S
1 (PIM and DVMRP cannot be enabled on the same IP interface)
Reserved SSM IPv4 
Address Ranges
N/S
N/S
232.0.0.0 to 232.255.255.255
Reserved SSM IPv6 
Address Ranges
N/S
N/S
FF3x::/32

<<<PAGE 86>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                   
page 3-10
Advanced Routing Configuration Specifications 
         
MBR Specifications
MBR Specifications
The following Specifications table contains information for the OmniSwitch implementation of the multicast border router (MBR) functionality defined in the PIM-SM specification (RFC 4601). Note that any 
maximum limits provided in the table are subject to available system resources.
Maximum Anycast RP 
Routers
N/S
N/S
8
Notes:
- OS6560 and OS6570M require Advanced Routing license.
OS6360
OS6465
OS6560
OS6570M
OS6575
OS6860
OS6860N
OS6865
OS6870
OS6900-
V72/C32
OS6900-
X/T48C6,
X48C4E,
V48C8,
C32E,
X/T24C2
OS6920
OS9900
RFCs Supported
N/S
N/S
N/S
N/S
4601—Protocol Independent Multicast-Sparse Mode (PIM-SM) Protocol Specification
3973—Protocol Independent Multicast-Dense Mode (PIM-DM)
2715—Interoperability Rules for Multicast Routing Protocols
IETF Internet-Drafts 
Supported
N/S
N/S
N/S
N/S
draft-ietf-idmr-dvmrp-v3-09.txt - Distance Vector Multicast Routing Protocol, Version 3
MBR Interoperability
N/S
N/S
N/S
N/S
DVMRP interoperability with IPv4 PIM (PIM-SM and PIM-DM only).
Notes:
MBR is not supported on the OS6360, OS6465, OS6560 or OS6570M.

<<<PAGE 87>>>
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page 4-1
4   TCAM Profiles
The OmniSwitch allows for selecting a different number of TCAM rules for an application by allowing 
configuration of different TCAM profiles. The configuration offers different TCAM profiles based on the 
switch model. The user can configure the required TCAM profile and reload the switch to activate the 
configured TCAM profile.

<<<PAGE 88>>>
In This Chapter
TCAM Profiles
page 4-2
OmniSwitch AOS Release 8 Specifications Guide
December 2025
In This Chapter
This chapter contains the following specifications tables:
• “OmniSwitch 6870 TCAM Profile Specifications” on page 4-3.
• “OmniSwitch 6570 TCAM Profile Specifications” on page 4-4.
• “OmniSwitch 6575 TCAM Profile Specifications” on page 4-6.

<<<PAGE 89>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                                 page 4-3
TCAM Profiles 
 OmniSwitch 6870 TCAM Profile Specifications
OmniSwitch 6870 TCAM Profile Specifications
The following table contains information based on the 6870 TCAM Profile.
Feature 
Resource 
Name
Default
Metro 
services
QoS ACL
Source 
IPv6 ACL
Bidirectional  
IPv6 ACL
Description
QoS Policy Rules
QoS Policy 
Ingress
2048
2048
4096
2048
2048
QoS Egress Policy 
Rules
QoS Policy 
Egress
256
128
128
128
256
QoS Policy Rules - 
Bidirectional IPv6
QoS Policy 
Ingress
N/S
N/S
N/S
N/S
Supported
SAP Classification 
Rules
System TTI
2048
4096
1024
1024
2048
Map SVLAN/service to traffic coming on UNI/
SAP ports.
VSTK Egress VLAN 
Translation
VSTK SAP-
Profile Egress
256
1024
256
256
256
To replace SVLAN with CVLAN when packet 
goes out of UNI ports in translate mode.
Service Tunnels
Tunnel Services 
Ingress
2048
1024
1024
1024
2048
SPB, VxLAN or L2 GRE services creation.
DHCP Snooping ISF 
IPv4
UDP_RLY_ISF
256
256
256
256
256
DHCP Snooping ISF 
IPv6
DHCP6_RLY_IS
F
0
0
0
256
0
UNP Users
AG
2048
1024
1024
1024
2048
PVLAN Rules
PVLAN Ingress/ 
Egress
256
256
64
64
256
Ingress rules are for dropping the VLAN traffic 
and are different from the primary/secondary on 
the ports.
Egress rules for translating egress VLAN i.e. If 
the traffic comes from primary VLAN ports and 
then egresses out of secondary VLAN tagged 
ports, the VLAN tag needs to be translated to 
the secondary VLAN and vice-versa.
QoS Anti Spoofing
Qos-AntiSpoof
256
128
256
128
256

<<<PAGE 90>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                                 page 4-4
TCAM Profiles 
 OmniSwitch 6570 TCAM Profile Specifications
OmniSwitch 6570 TCAM Profile Specifications
The following table contains information based on the 6570 TCAM Profile.
Feature 
Resource Name
Default 
(All 6570M Models)
Fabric 
(OS6570M 12 Ports 
Models)
Fabric 
(OS6570M-U28)
QoS Policy Rules
QoS Policy Ingress
384
256
256
QoS Egress Policy Rules
QoS Policy Egress
128
64
64
QoS Policy Rules - 
Bidirectional IPv6
QoS Policy Ingress
N/S
N/S
N/S
SAP Classification Rules
System TTI
512
512
1536
Map SVLAN/service to 
traffic coming on UNI/
SAP ports.
VSTK Egress VLAN 
Translation
VSTK SAP-Profile 
Egress
128
0
0
To replace SVLAN with 
CVLAN when packet 
goes out of UNI ports in 
translate mode.
Service Tunnels
Tunnel Services Ingress
256
513
1536
SPB, VxLAN or L2 GRE 
services creation.
DHCP Snooping ISF IPv4 UDP_RLY_ISF
256
256
256
DHCP Snooping ISF IPv6 DHCP6_RLY_ISF
0
0
0
UNP Users
AG
256
350
750
PVLAN Rules
PVLAN Ingress/ Egress
64
0
0

<<<PAGE 91>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                                 page 4-5
TCAM Profiles 
 OmniSwitch 6570 TCAM Profile Specifications
QoS Anti Spoofing
Qos-AntiSpoof
128
64
64
Ingress rules are for 
dropping the VLAN 
traffic and are different 
from the primary/
secondary on the ports.
Egress rules for 
translating egress VLAN 
i.e. If the traffic comes 
from primary VLAN 
ports and then egresses 
out of secondary VLAN 
tagged ports, the VLAN 
tag needs to be translated 
to the secondary VLAN 
and vice-versa.
QoS Anti Spoofing v6
QoS Anti Spoofing v6
0
0
0

<<<PAGE 92>>>
OmniSwitch AOS Release 8 Specifications Guide 
December 2025                                                                                                                                                 page 4-6
TCAM Profiles 
 OmniSwitch 6575 TCAM Profile Specifications
OmniSwitch 6575 TCAM Profile Specifications
The following table contains information based on the 6575 TCAM Profile.
Feature 
Resource Name
Default
Fabric
Source IPv6 ACL
Description
QoS Policy Rules
QoS Policy Ingress
384
384
128
QoS Egress Policy Rules
QoS Policy Egress
64
128
32
QoS Policy Rules - 
Bidirectional IPv6
QoS Policy Ingress
N/S
N/S
N/S
SAP Classification Rules
System TTI
512
512
512
Map SVLAN/service to traffic 
coming on UNI/SAP ports.
VSTK Egress VLAN 
Translation
VSTK SAP-Profile Egress
128
0
0
To replace SVLAN with CVLAN 
when packet goes out of UNI 
ports in translate mode.
Service Tunnels
Tunnel Services Ingress
225
512
255
SPB, VxLAN or L2 GRE services 
creation.
DHCP Snooping ISF IPv4
UDP_RLY_ISF
256
256
256
DHCP Snooping ISF IPv6
DHCP6_RLY_ISF
0
0
81
UNP Users
AG
300
350
300
PVLAN Rules
PVLAN Ingress/ Egress
64
0
0
Ingress rules are for dropping the 
VLAN traffic and are different 
from the primary/secondary on 
the ports.
Egress rules for translating egress 
VLAN i.e. If the traffic comes 
from primary VLAN ports and 
then egresses out of secondary 
VLAN tagged ports, the VLAN 
tag needs to be translated to the 
secondary VLAN and vice-versa.
QoS Anti Spoofing
Qos-AntiSpoof
128
128
128
QoS Anti Spoofingv6
Qos-AntiSpoofv6
0
0
53

<<<PAGE 93>>>
Index
OmniSwitch AOS Release 8 Specifications Guide
December 2025
Index-1
Index
B
BGP
specifications
3-5
C
CMM
specifications
1-5
D
DVMRP
specifications
3-6
I
IS-IS
specifications
3-4
M
MBR
specifications
3-8
Multicast Address Boundary
specifications
3-6
O
OSPF
specifications
3-2
OSPFv3
specifications
3-3
P
PIM
specifications
3-7
S
SNMP
specifications
1-7
specifications
BGP
3-5
CMM
1-5
DVMRP
3-6
IS-IS
3-4
MBR
3-8
Multicast Address Boundary
3-6
OSPF
3-2
OSPFv3
3-3
PIM
3-7
SNMP
1-7
USB Flash Drive
1-5
U
USB Flash Drive
specifications
1-5

<<<PAGE 94>>>
Index
Index-2
OmniSwitch AOS Release 8 Specifications Guide
December 2025

<<<PAGE 95>>>
Software License and Copyright Statements
ALE USA, Inc. License Agreement
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page A-1
A  Software License and
Copyright Statements
This appendix contains ALE USA, Inc. and third-party software vendor license and copyright statements.
ALE USA, Inc. License Agreement
ALE USA, Inc. SOFTWARE LICENSE AGREEMENT
By opening this package, you accept and agree to the terms of this license agreement. If you are not 
willing to be bound by the terms of this license agreement, do not open this package. Please 
promptly return the product and any materials in unopened form to the place where you obtained it 
for a full refund. 
1. License Grant. This is a license, not a sales agreement, between you (the “Licensee”) and ALE USA, 
Inc.. ALE USA, Inc. hereby grants to Licensee, and Licensee accepts, a non-exclusive license to use 
program media and computer software contained therein (the “Licensed Files”) and the accompanying 
user documentation (collectively the “Licensed Materials”), only as authorized in this License Agreement. 
Licensee, subject to the terms of this License Agreement, may use one copy of the Licensed Files on the 
Licensee’s system. Licensee agrees not to assign, sublicense, transfer, pledge, lease, rent, or share their 
rights under this License Agreement. Licensee may retain the program media for backup purposes with 
retention of the copyright and other proprietary notices. Except as authorized under this paragraph, no 
copies of the Licensed Materials or any portions thereof may be made by Licensee and Licensee shall not 
modify, decompile, disassemble, reverse engineer, or otherwise attempt to derive the Source Code. 
Licensee is also advised that ALE USA, Inc. products contain embedded software known as firmware 
which resides in silicon. Licensee may not copy the firmware or transfer the firmware to another medium.
2. ALE USA, Inc.’s Rights. Licensee acknowledges and agrees that the Licensed Materials are the sole 
property of ALE USA, Inc. and its licensors (herein “its licensors”), protected by U.S. copyright law, 
trademark law, and are licensed on a right to use basis. Licensee further acknowledges and agrees that all 
rights, title, and interest in and to the Licensed Materials are and shall remain with ALE USA, Inc. and its 
licensors and that no such right, license, or interest shall be asserted with respect to such copyrights and 
trademarks. This License Agreement does not convey to Licensee an interest in or to the Licensed 
Materials, but only a limited right to use revocable in accordance with the terms of this License 
Agreement.
IMPORTANT. Please read the terms and conditions of this license agreement carefully before opening this 
package.

<<<PAGE 96>>>
ALE USA, Inc. License Agreement
Software License and Copyright Statements
page A-2
OmniSwitch AOS Release 8 Specifications Guide
December 2025
3. Confidentiality. ALE USA, Inc. considers the Licensed Files to contain valuable trade secrets of ALE 
USA, Inc., the unauthorized disclosure of which could cause irreparable harm to ALE USA, Inc.. Except 
as expressly set forth herein, Licensee agrees to use reasonable efforts not to disclose the Licensed Files to 
any third party and not to use the Licensed Files other than for the purpose authorized by this License 
Agreement. This confidentiality obligation shall continue after any termination of this License Agreement.
4. Indemnity. Licensee agrees to indemnify, defend and hold ALE USA, Inc. harmless from any claim, 
lawsuit, legal proceeding, settlement or judgment (including without limitation ALE USA, Inc.’s 
reasonable United States and local attorneys’ and expert witnesses’ fees and costs) arising out of or in 
connection with the unauthorized copying, marketing, performance or distribution of the Licensed Files.
5. Limited Warranty. ALE USA, Inc. warrants, for Licensee’s benefit alone, that the program media 
shall, for a period of ninety (90) days from the date of commencement of this License Agreement (referred 
to as the Warranty Period), be free from defects in material and workmanship. ALE USA, Inc. further 
warrants, for Licensee benefit alone, that during the Warranty Period the Licensed Files shall operate 
substantially in accordance with the functional specifications in the User Guide. If during the Warranty 
Period, a defect in the Licensed Files appears, Licensee may return the Licensed Files to ALE USA, Inc. 
for either replacement or, if so elected by ALE USA, Inc., refund of amounts paid by Licensee under this 
License Agreement. EXCEPT FOR THE WARRANTIES SET FORTH ABOVE, THE LICENSED 
MATERIALS ARE LICENSED “AS IS” AND ALE USA, Inc. AND ITS LICENSORS DISCLAIM ANY 
AND ALL OTHER WARRANTIES, WHETHER EXPRESS OR IMPLIED, INCLUDING (WITHOUT 
LIMITATION) ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A 
PARTICULAR PURPOSE. SOME STATES DO NOT ALLOW THE EXCLUSION OF IMPLIED 
WARRANTIES SO THE ABOVE EXCLUSIONS MAY NOT APPLY TO LICENSEE. THIS 
WARRANTY GIVES THE LICENSEE SPECIFIC LEGAL RIGHTS. LICENSEE MAY ALSO HAVE 
OTHER RIGHTS WHICH VARY FROM STATE TO STATE.
6. Limitation of Liability. ALE USA, Inc.’s cumulative liability to Licensee or any other party for any 
loss or damages resulting from any claims, demands, or actions arising out of or relating to this License 
Agreement shall not exceed the license fee paid to ALE USA, Inc. for the Licensed Materials. IN NO 
EVENT SHALL ALE USA, Inc. BE LIABLE FOR ANY INDIRECT, INCIDENTAL, 
CONSEQUENTIAL, SPECIAL, OR EXEMPLARY DAMAGES OR LOST PROFITS, EVEN IF ALE 
USA, Inc. HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. SOME STATES DO 
NOT ALLOW THE LIMITATION OR EXCLUSION OF LIABILITY FOR INCIDENTAL OR 
CONSEQUENTIAL DAMAGES, SO THE ABOVE LIMITATION OR EXCLUSION TO INCIDENTAL 
OR CONSEQUENTIAL DAMAGES MAY NOT APPLY TO LICENSEE. 
7. Export Control. This product is subject to the jurisdiction of the United States. Licensee may not 
export or reexport the Licensed Files, without complying with all United States export laws and 
regulations, including but not limited to (i) obtaining prior authorization from the U.S. Department of 
Commerce if a validated export license is required, and (ii) obtaining “written assurances” from licensees, 
if required.
8. Support and Maintenance. Except as may be provided in a separate agreement between ALE USA, 
Inc. and Licensee, if any, ALE USA, Inc. is under no obligation to maintain or support the copies of the 
Licensed Files made and  hereunder and ALE USA, Inc. has no obligation to furnish Licensee with any 
further assistance, documentation or information of any nature or kind.
9. Term. This License Agreement is effective upon Licensee opening this package and shall continue until 
terminated. Licensee may terminate this License Agreement at any time by returning the Licensed 
Materials and all copies thereof and extracts therefrom to ALE USA, Inc. and certifying to ALE USA, Inc. 
in writing that all Licensed Materials and all copies thereof and extracts therefrom have been returned or 
erased by the memory of Licensee’s computer or made non-readable. ALE USA, Inc. may terminate this 
License Agreement upon the breach by Licensee of any term hereof. Upon such termination by ALE USA,

<<<PAGE 97>>>
Software License and Copyright Statements
ALE USA, Inc. License Agreement
OmniSwitch AOS Release 8 Specifications Guide
December 2025
page A-3
Inc., Licensee agrees to return to ALE USA, Inc. or destroy the Licensed Materials and all copies and 
portions thereof.
10. Governing Law. This License Agreement shall be construed and governed in accordance with the 
laws of the State of California.
11. Severability. Should any term of this License Agreement be declared void or unenforceable by any 
court of competent jurisdiction, such declaration shall have no effect on the remaining terms herein.
12. No Waiver. The failure of either party to enforce any rights granted hereunder or to take action against 
the other party in the event of any breach hereunder shall not be deemed a waiver by that party as to 
subsequent enforcement of rights or subsequent actions in the event of future breaches.
13. Notes to United States Government Users. Software and documentation are provided with restricted 
rights. Use, duplication or disclosure by the government is subject to (i) restrictions set forth in GSA ADP 
Schedule Contract with ALE USA, Inc.’s reseller(s), or (ii) restrictions set forth in subparagraph (c) (1) 
and (2) of 48 CFR 52.227-19, as applicable.
14.Third Party Materials. Licensee is notified that the Licensed Files contain third party software and 
materials licensed to ALE USA, Inc. by certain third party licensors. Some third party licensors are third 
part beneficiaries to this License Agreement with full rights of enforcement. Please refer to the section 
entitled “Third Party Licenses and Notices” on page -4 for the third party license and notice terms.

<<<PAGE 98>>>
Third Party Licenses and Notices
Software License and Copyright Statements
page A-4
OmniSwitch AOS Release 8 Specifications Guide
December 2025
Third Party Licenses and Notices
Legal Notices applicable to any software  alone or in connection with the product to which this document 
pertains, are contained in files within the software itself located at: /flash/foss.
Also, if needed, we provide all FOSS (Free and Open Source Software) source code used in this release. 
Contact Service & Support for information.