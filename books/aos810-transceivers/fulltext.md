<<<PAGE 1>>>
Part No. 060973-00 Rev. A
December 2025
OmniSwitch AOS Release 8
Transceivers Guide
8.10R4
Attention: Use of any transceivers other than the ALE-certified part numbers listed in 
the Compatibility Matrices is prohibited and unsupported. Failure to comply with these 
matrices may result in unpredictable system behavior, is not guaranteed for proper 
performance and may result in voiding the warranty for the affected platforms.
www.al-enterprise.com

<<<PAGE 2>>>
This user guide contains transceiver specifications and compatibility information for the 
OmniSwitch AOS Release 8 and supported platforms. The information described in this guide is 
subject to change without notice.
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trade-
marks-copyright. All other trademarks are the property of their respective owners. The information 
presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any 
responsibility for inaccuracies contained herein. © Copyright 2025 ALE International, ALE USA Inc. All 
rights reserved in all countries.
Service & Support Contact Information
North America: 800-995-2696
Latin America: 877-919-9526
EMEA: +800 00200100 (Toll Free) or +1(650)385-2193   
Asia Pacific: +65 6240 8484
Web: myportal.al-enterprise.com

<<<PAGE 3>>>
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
iii
Contents
About This Guide ........................................................................................................... v
Supported Platforms ........................................................................................................... v
Who Should Read this Manual? ........................................................................................vi
When Should I Read this Manual? ....................................................................................vi
What is Not in this Manual? .............................................................................................. vi
How is the Information Organized? ..................................................................................vi
Documentation Roadmap .................................................................................................vii
Related Documentation .....................................................................................................ix
Technical Support .............................................................................................................. x
Chapter 1
Small Form-Factor Pluggables ...............................................................................1-1
SFP/SFP+/SFP28/QSFP+/QSFP28/SFP56/QSFP56/QSFP-DD ....................................1-1
In This Chapter ................................................................................................................1-1
SFP MSA Specification ..................................................................................................1-3
Transceiver Installation and Removal .............................................................................1-4
40/100-Gigabit Fiber Optic Cables .................................................................................1-7
QSFP to QSFP MPO Fiber Optic Cable ..................................................................1-7
QSFP to SFP+ Splitter Fiber Optic Cable ................................................................1-7
Gigabit Ethernet Transceivers .........................................................................................1-8
Dual Speed Ethernet Transceivers ................................................................................1-15
100 FX Ethernet Transceivers .......................................................................................1-18
10-Gigabit SFP+ Transceivers ......................................................................................1-22
25-Gigabit SFP28 Transceivers ....................................................................................1-30
40-Gigabit QSFP+ Transceivers ...................................................................................1-34
50-Gigabit SFP56 Transceivers ....................................................................................1-41
100-Gigabit QSFP28 Transceivers ...............................................................................1-43
200-Gigabit QSFP56 Transceivers ...............................................................................1-48
400-Gigabit QSFP-DD Transceivers ............................................................................1-50
GPON Transceivers ......................................................................................................1-54
Industrial Transceivers ..................................................................................................1-55

<<<PAGE 4>>>
Contents
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
iv
Chapter 2
Transceiver Compatibility Matrix .........................................................................1-64
In This Chapter ..............................................................................................................1-64
OmniSwitch 6360 Compatibility ..................................................................................1-65
OmniSwitch 6465 Compatibility ..................................................................................1-67
OmniSwitch 6465T Compatibility ................................................................................1-68
OmniSwitch 6560(E) Compatibility .............................................................................1-70
OmniSwitch 6570M Compatibility ...............................................................................1-73
OmniSwitch 6575 Compatibility ..................................................................................1-76
OmniSwitch 6860 Compatibility ..................................................................................1-77
OmniSwitch 6860N Compatibility ...............................................................................1-80
OmniSwitch 6865 Compatibility ..................................................................................1-83
OmniSwitch 6870 Compatibility ..................................................................................1-84
OmniSwitch 6900-V72/C32/C32E Compatibility ........................................................1-87
OmniSwitch OS6900 Compatibility .............................................................................1-90
OmniSwitch 6920 Compatibility ..................................................................................1-93
OmniSwitch 9900 Compatibility ..................................................................................1-96

<<<PAGE 5>>>
OmniSwitch AOS Release 8 Tranceivers Guide
December 2025
page v
About This Guide
This OmniSwitch AOS Release 8 Transceivers Guide provides specifications and compatibility informa-
tion for the supported OmniSwitch transceivers for all OmniSwitch AOS Release 8 products.
Supported Platforms
This information in this guide applies to the following products:
• OmniSwitch 6360
• OmniSwitch 6465
• OmniSwitch 6560(E)
• OmniSwitch 6570M
• OmniSwitch 6575
• OmniSwitch 6860(E)
• OmniSwitch 6860N
• OmniSwitch 6865
• OmniSwitch 6870
• OmniSwitch 6900
• OmniSwitch 6920
• OmniSwitch 9900

<<<PAGE 6>>>
About This Guide
Who Should Read this Manual?
OmniSwitch AOS Release 8 Tranceivers Guide
December 2025
page vi
Who Should Read this Manual?
The audience for this user guide is network administrators and IT support personnel who need to provide 
network connectivity using SFP, SFP+, SFP28, QSFP+ and QSFP28 transceivers.
When Should I Read this Manual?
Read this guide as soon as you are ready to integrate your OmniSwitch into your network and you are 
ready to provide connectivity using the supported transceivers. You should have already stepped through 
the first login procedures and read the brief software overviews in the appropriate OmniSwitch Hardware 
Guide.
This guide includes information about the supported OmniSwitch transceivers.
• SFP/SFP+/SFP28/QSFP+/QSFP28 specifications and compatibility information
What is Not in this Manual?
Procedures for switch management methods, such as CLI, web-based (WebView or OmniVista) or SNMP, 
are outside the scope of this guide. 
For information on WebView and SNMP switch management methods consult the OmniSwitch Switch 
Management Guide. Information on using WebView and OmniVista can be found in the context-sensitive 
on-line help available with those network management applications.
This guide is designed to provide transceiver specification and compatibility information only and is not 
intended as a reference for any CLI commands or configuration information. Refer to the Documentation 
Roadmap for a list of available user guides.
How is the Information Organized?
Chapters in this guide are broken down by transceiver type. 
Specification Information. Each transceiver has an associated table providing individual specifications 
for all supported transceivers.
Compatibility Information. A compatibility chart is provided for each transceiver specifying which 
modules or switch the transceiver is supported on.

<<<PAGE 7>>>
About This Guide
Documentation Roadmap
OmniSwitch AOS Release 8 Tranceivers Guide
December 2025
page vii
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
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: OmniSwitch Hardware Users Guide
OmniSwitch AOS Release 8 Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the Hardware Guide. This guide 
provide specifications, illustrations, and descriptions of all hardware components, such as chassis, power 
supplies, Chassis Management Modules (CMMs), Network Interface (NI) modules, and cooling fans. It 
also includes steps for common procedures, such as removing and installing switch components.
This guide is the primary users guide for the basic software features on a single switch. This guide 
contains information on the switch directory structure, basic file and directory utilities, switch access 
security, SNMP, and web-based management. It is recommended that you read this guide before 
connecting your switch to the network.
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: OmniSwitch AOS Release 8 Network Configuration Guide
OmniSwitch AOS Release 8 Advanced Routing Configuration Guide
OmniSwitch AOS Release 8 Data Center Switching Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The Network Configuration Guide contains overview information, procedures, and examples on 
how standard networking technologies are configured on the OmniSwitch.
The Advanced Routing Guide includes configuration information for networks using advanced routing 
technologies (OSPF and BGP) and multicast routing protocols (DVMRP and PIM-SM).
The Data Center Switching Guide includes configuration information for data center networks using 
virtualization technologies (SPBM and UNP) and Data Center Bridging protocols (PFC, ETC, and 
DCBX).

<<<PAGE 8>>>
About This Guide
Documentation Roadmap
OmniSwitch AOS Release 8 Tranceivers Guide
December 2025
page viii
Anytime
The OmniSwitch AOS Release 8 CLI Reference Guide contains comprehensive information on all CLI 
commands supported by the switch. This guide includes syntax, default, usage, example, related CLI 
command, and CLI-to-MIB variable mapping information for all CLI commands supported by the switch. 
This guide can be consulted anytime during the configuration process to find detailed and specific 
information on each CLI command.

<<<PAGE 9>>>
About This Guide
Related Documentation
OmniSwitch AOS Release 8 Tranceivers Guide
December 2025
page ix
Related Documentation
The following are the titles and descriptions of all the OmniSwitch user manuals:
• OmniSwitch Hardware Users Guides
Describes the hardware and software procedures for getting an OmniSwitch up and running as well as 
complete technical specifications and procedures for all OmniSwitch chassis, power supplies, fans, and 
Network Interface (NI) modules.
• OmniSwitch AOS Release 8 CLI Reference Guide
Complete reference to all CLI commands supported on the OmniSwitch. Includes syntax definitions, 
default values, examples, usage guidelines and CLI-to-MIB variable mappings.
• OmniSwitch AOS Release 8 Switch Management Guide
Includes procedures for readying an individual switch for integration into a network. Topics include 
the software directory architecture, image rollback protections, authenticated switch access, managing 
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
• OmniSwitch AOS Release 8 Data Center Switching Guide
Includes and introduction to the OmniSwitch data center switching architecture as well as network 
configuration procedures and descriptive information on all the software features and protocols that 
support this architecture. Chapters cover Shortest Path Bridging MAC (SPBM), Data Center Bridging 
(DCB) protocols, Virtual Network Profile (vNP), and the Edge Virtual Bridging (EVB) protocol.
• OmniSwitch AOS Release 8 Transceivers Guide
Includes transceiver specifications and product compatibility information.
• OmniSwitch AOS Release 8 Specifications Guide
Includes Specifications table information for the features documented in the Switch Management 
Guide, Network Configuration Guide, Advanced Routing Guide, and Data Center Switching Guide.
• Technical Tips, Field Notices
Includes information published by Alcatel-Lucent Enterprise’s Customer Support group.
• Release Notes
Includes critical Open Problem Reports, feature exceptions, and other important information on the 
features supported in the current release and any limitations to their support.

<<<PAGE 10>>>
About This Guide
Technical Support
OmniSwitch AOS Release 8 Tranceivers Guide
December 2025
page x
Technical Support
An Alcatel-Lucent service agreement brings your company the assurance of 7x24 no-excuses technical 
support. You’ll also receive regular software updates to maintain and maximize your Alcatel-Lucent 
product’s features and functionality and on-site hardware replacement through our global network of 
highly qualified service delivery partners. 
With 24-hour access to Alcatel-Lucent Enterprise Service and Support web page, you’ll be able to view 
and update any case (open or closed) that you have reported to Alcatel-Lucent Enterprise technical 
support, open a new case or access helpful release notes, technical bulletins, and manuals. 
Access additional information on Alcatel-Lucent Enterprise Programs:
Web: myportal.al-enterprise.com
Phone: 1-800-995-2696

<<<PAGE 11>>>
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-1
1   Small Form-Factor
Pluggables
SFP/SFP+/SFP28/QSFP+/QSFP28/SFP56/
QSFP56/QSFP-DD
OmniSwitch Series switches use both copper-based and fiber-based optical Small Form Factor Pluggable 
transceivers. These transceivers are fully hot-swappable and are available for both short-reach and long-
reach applications. Copper-based and fiber-based optical transceivers can be mixed on the same module.
In This Chapter
This chapter describes the technical specifications for all the OmniSwitch supported transceivers. For 
additional details about OmniSwitch modules, see the appropriate OmniSwitch Hardware Guide.
Transceiver specifications in this chapter include:
• SFP MSA Specifications. See “SFP MSA Specification” on page 1-3.
• Transceiver Installation. See “Transceiver Installation and Removal” on page 1-4.
• 40-Gigabit Fiber Optic Cable Overview. See “40/100-Gigabit Fiber Optic Cables” on page 1-7.
• Gigabit Ethernet Transceivers. See “Gigabit Ethernet Transceivers” on page 1-8.
• Dual Speed Ethernet Transceivers. See “Dual Speed Ethernet Transceivers” on page 1-15.
• 100-FX Ethernet Transceivers. See “100 FX Ethernet Transceivers” on page 1-18.
• 10-Gigabit SFP+ Transceivers. See “10-Gigabit SFP+ Transceivers” on page 1-22.
• 25-Gigabit SFP28 Transceivers. See “25-Gigabit SFP28 Transceivers” on page 1-30.
• 40-Gigabit QSFP+ Transceivers. See “40-Gigabit QSFP+ Transceivers” on page 1-34.
• 50-Gigabit SFP56 Transceivers. See “50-Gigabit SFP56 Transceivers” on page 1-41.
• 100-Gigabit QSFP28 Transceivers. See “100-Gigabit QSFP28 Transceivers” on page 1-43.
• 200-Gigabit QSFP56 Transceivers. See “200-Gigabit QSFP56 Transceivers” on page 1-48.
• 400-Gigabit QSFP-DD Transceivers. See “400-Gigabit QSFP-DD Transceivers” on page 1-51.
• Industrial Transceivers. See “Industrial Transceivers” on page 1-55.
• GPON Transceivers. See “GPON Transceivers” on page 1-54.

<<<PAGE 12>>>
Small Form-Factor Pluggables
In This Chapter
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-2
• For a transceiver compatibility matrix, see “Transceiver Compatibility Matrix” on page 2-64.

<<<PAGE 13>>>
Small Form-Factor Pluggables
SFP MSA Specification
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-3
SFP MSA Specification
The Small Form-Factor Pluggable (SFP) MSA (Multi Source Agreement) is a specification for a common 
interface for optical modular transceivers. The SFP connector consists of a 20-pin receptacle and an SFP 
housing cage. The connector provides the interface for the hot pluggable SFP module. Each SFP module 
contains a serial interface to provide identification information that describes the SFP capabilities, stand 
interfaces, manufacturer and other information.
For information on installing SFPs, refer to the documentation included with the transceiver.
Small Form Factor Pluggable (SFP)
This diagram is a representation
only; the physical appearance of the
actual module may vary slightly.

<<<PAGE 14>>>
Small Form-Factor Pluggables
Transceiver Installation and Removal
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-4
Transceiver Installation and Removal
Follow the instructions below for the appropriate transceiver type. 
ESD Caution: Before handling the module, you must discharge all static electricity on your person to 
avoid Electrostatic Discharge (ESD) damage. If using a wrist strap, ensure that the wrist strap touches 
your skin. Attach the other end of the strap to the chassis. If your chassis provides a grounding lug, this 
can be used. Refer to your hardware user guide for details.
If using a wrist strap, ensure that the wrist strap touches your skin. Attach the other end of the strap to the 
chassis. If your chassis provides a grounding lug, this can be used. Refer to your hardware user guide for 
details.
Dust Exposure: To reduce the risk of dust exposure and physical damage, be sure to replace the protec-
tive rubber cover (provided) when the SFP is not in use. 
Eye Safety: SFP transceivers are international Class 1 laser products and are eye-safe devices when oper-
ated within the limits of manufacturers’ specifications. Operating SFP transceivers in a manner inconsis-
tent with intended usage and specification may result in hazardous radiation exposure.
Note: After removing a transceiver, wait for a minimum of 10 seconds before re-inserting any transceiver 
into the same port. This allows sufficient time for software to detect the removal of the transceiver. 
Note: Never force the transceiver in or out of the transceiver slot. 
Note: The design of the OS6865 chassis may result in a slight pressure on the transceiver cages. If the 
transceiver does not easily slide out of the slot, gently move the transceiver side-to-side while firmly pull-
ing out.

<<<PAGE 15>>>
Small Form-Factor Pluggables
Transceiver Installation and Removal
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-5
SFP - Hinged
SFP - Bail Wire
To remove, you must first open the SFP’s hinged face to approximately ninety
degrees. Then, grasp the hinged face and carefully pull the SFP straight out of
the slot.
When inserting a SFP, be sure that the hinged face is closed. Slide the SFP
straight into the slot until the module clicks firmly into place.
SFP Module
Interface Slot
To install, align the transceiver with the transceiver slot on the
NI module, as shown. Be sure that the bail wire delatch is in the
up, or closed position. Slide the transceiver straight into the slot
until the module clicks firmly into place.
SFP Transceiver
Network Interface (NI) 
Module
To remove, you must first pull down on the bail
wire delatch. Grip the wire delatch while it is in this
open position and carefully pull the transceiver
straight out of the slot.
Bail Wire Delatch
Transceiver Slot
(Shown in open “removal” posi-
tion; 
when 
inserting, 
bail
delatch must be closed.)

<<<PAGE 16>>>
Small Form-Factor Pluggables
Transceiver Installation and Removal
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-6
SFP - Ejector Button
QSFP+ - Removal
To install, align the transceiver with the
transceiver slot on the NI module, as
shown. Carefully slide the transceiver
back until it clicks into place; this is an
indication that the connectors are firmly
seated.
SFP Transceiver
Network Interface (NI) Module
To remove, use the ejector tool (provided
with each switch chassis) to push the trans-
ceiver’s ejector button. The ejector button is
located just below the transceiver port; refer
to the diagram for more information. The
transceiver will disengage from the connec-
tors and eject slightly. Once disengaged, use
the clip end of the ejector tool to carefully
pull the transceiver straight out and away
from the NI module.
Dust Cover
Ejector
Transceiver Slot
To install, align the transceiver with the
transceiver slot on the NI module, as
shown. Carefully slide the transceiver
back until it clicks into place; this is an
indication that the connectors are firmly
seated.
QSFP+ Transceiver
Network Interface (NI) Module
To remove, use the rubber or metal ejector
handle and pull transceiver straight out and
away from the NI module.
Note: Never force the transceiver in or out of
the transceiver slot.
Transceiver Slot
Handle

<<<PAGE 17>>>
Small Form-Factor Pluggables
40/100-Gigabit Fiber Optic Cables
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-7
40/100-Gigabit Fiber Optic Cables
QSFP to QSFP MPO Fiber Optic Cable
To directly connect two Omniswitches with 40G/100G transceivers with an MPO-12 interface, an MPO 
trunk cable can be used. The cable can have 8 or 12 fibers, however only 8 fibers are used. The cable 
should be a Type-B crossover cable. 
Example Type B - MPO Cable Connection
QSFP to SFP+ Splitter Fiber Optic Cable
To connect a 40G transceiver with an MPO-12 interface to four 10G transceivers an MTP-LC splitter 
cable with a female connector can be used. The MPO-LC cable has eight fibers that connect the 40G MPO 
connector to four 10G LC connectors. The LC connectors can be manually rearranged to meet the neces-
sary transmit/receive requirements. 
Example MPO/LC Splitter Cable
Fiber
1
2
3
4
5-8
9
10
11
12
Type A
MPO1 Tx1
Tx2
Tx3
Tx4
N/A
Rx4
Rx3
Rx2
Rx1
MPO2 Rx1
Rx2
Rx3
Rx4
N/A
Tx4
Tx3
Tx2
Tx1
Fiber
1
2
3
4
5-8
9
10
11
12
Type B
Fiber
1
2
3
4
5-8
9
10
11
12
MPO1 Rx1
Rx2
Rx3
Rx4
N/A
Tx4
Tx3
Tx2
Tx1
MPO2 Tx1
Tx2
Tx3
Tx4
N/A
Rx4
Rx3
Rx2
Rx1
Fiber
12
11
10
9
5-8
4
3
2
1
QSFP
QSFP
MPO Connectors
LC/SFP4
LC/SFP2
LC/SFP3
LC/SFP1
MPO

<<<PAGE 18>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-8
Gigabit Ethernet Transceivers
SFP-GIG-SX
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-SX
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-9.0 to -2.5 dBm
Receiver Sensitivity
-17 dBm
Transmission Distance
~300 m on 62.5/125µm
~550 m on 50/125µm 
Operating Temperature
-20 ºC to 85ºC 
Digital Diagnostic Monitoring
Supported
SFP-GIG-LX
Gigabit SFP Optical Transceiver. 
Connector types
LC
Standards supported
802.3z, SFP MSA
Connections supported
1000BASE-LX
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-9.5 to -3 dBm
Receiver Sensitivity
-19 dBm
Transmission Distance
10 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported

<<<PAGE 19>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-9
SFP-GIG-LH40
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-LH40r
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
0 to +5 dBm
Maximum Input Power
0 dBm
Receiver Sensitivity
-22 dBm
Transmission Distance
~40 km
Operating Temperature
-10 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
SFP-GIG-LH70
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-LH70
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
0 to +5 dBm
Receiver Sensitivity
-22 dBm
Transmission Distance
~70 km
Operating Temperature
-10 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
SFP-GIG-EZX
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
0 to +5 dBm

<<<PAGE 20>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-10
Receiver Sensitivity
-35 dBm
Transmission Distance
~120 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes: 
No longer purchasable.
SFP-GIG-##CWD
Coarse Wavelength Division Multiplexing (CWDM) is an optical transceiver supporting single-mode fiber 
over various wavelengths. CWDMs are hot-pluggable and are available for long-reach applications.
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-LX
Fiber Type
SMF
Wavelength
1470, 1490, 1510, 1530, 1550, 1570, 1590, 1610
Optical Power Output
-2 to +3 dBm
Receiver Sensitivity
-24 dBm
Transmission Distances
~62 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Not Supported
Notes: 
No longer purchasable.
SFP-GIG-T 
Gigabit SFP Copper Transceiver. 
Connector Type
RJ-45
Standards Supported
802.3z, SFP MSA
Connections supported
10/100/1000BASE-T
Cable Type
CAT5, CAT5e, CAT6
Transmission Distance
100 m
Digital Diagnostic Monitoring
Not Supported
Notes: 
The existing SFP-GIG-T transceiver is being replaced with an updated 
transceiver. The existing part will continue to work with all AOS 
releases. The serial number format of the new part is “APxxxxxxxxxx” 
and requires a minimum of AOS release 8.9R3.
SFP-GIG-EZX
Gigabit SFP Optical Transceiver.

<<<PAGE 21>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-11
SFP-1G-T
Gigabit SFP Copper Transceiver. 
Connector Type
RJ-45
Standards Supported
802.3ab, SFP MSA
Connections supported
1000BASE-T
Cable Type
CAT5, CAT5e, CAT6
Transmission Distance
100 m
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Not Supported
SFP-GIG-EXTND
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3, SFP MSA
Connections Supported
-
Fiber Type
MMF
Wavelength
1310 nm
Saturation Power
0 dBm
Transmission Distance
~2 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes: 
No longer purchasable.
SFP-GIG-BX-D
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX10
Fiber Type
SMF
Wavelength
Transmit: 1490 nm
Receive: 1310 nm
Average Power Output
-9 to -3 dBm
Receiver Sensitivity
-19.5 dBm
Transmission Distance
~10 km

<<<PAGE 22>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-12
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-GIG-BX-U
SFP-GIG-BX-U
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX10
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1490 nm
Average Power Output
-9 to -3 dBm
Receiver Sensitivity
-19.5 dBm
Transmission Distance
~10 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-GIG-BX-D
SFP-GIG-BX-D20
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX20
Fiber Type
SMF
Wavelength
Transmit: 1490 nm
Receive: 1310 nm
Average Power Output
-8 to -3 dBm
Receiver Sensitivity
-23 dBm
Transmission Distance
~20 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-GIG-BX-U20
SFP-GIG-BX-D
Bi-Directional SFP Optical Transceiver.

<<<PAGE 23>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-13
SFP-GIG-BX-U20
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX20
Fiber Type
SMF
Wavelength
Transmit: 130 nm
Receive: 1490 nm
Average Power Output
-8 to -3 dBm
Receiver Sensitivity
-23 dBm
Transmission Distance
~20 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-GIG-BX-D20

<<<PAGE 24>>>
Small Form-Factor Pluggables
Gigabit Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-14
SFP-GIG-BX-D40
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX40
Fiber Type
SMF
Wavelength
Transmit: 1490 nm
Receive: 1310 nm
Average Power Output
-2 to +3 dBm
Receiver Sensitivity
-23 dBm
Transmission Distance
~40 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-GIG-BX-U40
SFP-GIG-BX-U40
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX20
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1490 nm
Average Power Output
-2 to +3 dBm
Receiver Sensitivity
-23 dBm
Transmission Distance
~40 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-GIG-BX-D40

<<<PAGE 25>>>
Small Form-Factor Pluggables
Dual Speed Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-15
Dual Speed Ethernet Transceivers
Note: For dual speed transceivers it's recommended to manually configure the speed on both ends to 
prevent speed mismatch. 
SFP-DUAL-MM
SFP-DUAL-MM-N
Dual speed Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
100BASE-FX, 1000BASE-LX
Fiber Type
MMF
Wavelength
1310 nm
Average Power Output
100BASE-FX: -20 to -14 dBm
1000BASE-LX: -11.5 to -3 dBm
Receiver Sensitivity
100BASE-FX: -28 dBm
1000BASE-LX: -22 dBm
Transmission Distance
550 m at 1.25 Gbps
2 km at 125 Mbps
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes: 
SFP-DUAL-MM is no longer purchasable. 
The existing SFP-DUAL-MM-N part SPG-DR-FX-CDFC-AL2 is being replaced with part SPG-DR-FX-
CDFD-AL2. The existing SPG-DR-FX-CDFC-AL2 will continue to work with all AOS releases. SPG-
DR-FX-CDFD-AL2 requires a minimum of AOS release 8.9R3.
SFP-DUAL-SM10
Dual speed Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, 802.3ah, SFP MSA
Connections Supported
100BASE-FX, 1000BASE-LX
Fiber Type
SMF
Wavelength
1310 nm

<<<PAGE 26>>>
Small Form-Factor Pluggables
Dual Speed Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-16
Average Power Output
100BASE-FX: -15 to -8 dBm
1000BASE-LX: -9.5 to -3 dBm
Receiver Sensitivity
100BASE-FX: -28 dBm
1000BASE-LX: -22 dBm
Transmission Distance
~10 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Not Supported
Notes: 
No longer purchasable.
SFP-DUAL-BX-D
Dual speed Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, 802.3ah, SFP MSA
Connections Supported
100/1000BASE-BX10-D
Fiber Type
SMF
Wavelength
Transmit: 1550 nm
Receive: 1310 nm
Average Power Output
-9 to -3 dBm
Receiver Sensitivity
-18.7 dBm
Transmission Distance
~10 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
SFP-DUAL-BX-U
Dual speed Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, 802.3ah, SFP MSA
Connections Supported
100/1000BASE-BX10-U
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1550 nm
Average Power Output
-9 to -3 dBm
SFP-DUAL-SM10
Dual speed Optical Transceiver.

<<<PAGE 27>>>
Small Form-Factor Pluggables
Dual Speed Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-17
Receiver Sensitivity
-18.7 dBm
Transmission Distance
~10 km
Operating Temperature
-5 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
SFP-DUAL-BX-U
Dual speed Optical Transceiver.

<<<PAGE 28>>>
Small Form-Factor Pluggables
100 FX Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-18
100 FX Ethernet Transceivers
SFP-100-BX20LT
Bi-Directional SFP Optical Transceiver. 
Connector Type
SC
Standards Supported
802.3ah, SFP MSA, ITU-T G.983
Connections Supported
100BASE-BX
Fiber Type
SMF
Wavelength
Transmit: 1550 nm
Receive: 1310 nm
Average Power Output
-14 to -8 dBm
Receiver Sensitivity
-32 dBm
Transmission Distance
~20 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-100-BX20NU.
No longer purchasable.
SFP-100-BX20NU
Bi-Directional SFP Optical Transceiver. 
Connector Type
SC
Standards Supported
802.3ah, SFP MSA, ITU-T G.983
Connections Supported
100BASE-BX
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1550 nm
Average Power Output
-14 to -8 dBm
Receiver Sensitivity
-32 dBm
Transmission Distance
~20 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-100-BX20LT.
No longer purchasable.

<<<PAGE 29>>>
Small Form-Factor Pluggables
100 FX Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-19
SFP-100-BXLC-D
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA, ITU-T G.983
Connections Supported
100BASE-BX
Fiber Type
SMF
Wavelength
Transmit: 1550 nm
Receive: 1310 nm
Average Power Output
-14 to -8 dBm
Receiver Sensitivity
-32 dBm
Transmission Distance
~20 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-100-BXLC-U
SFP-100-BXLC-U
Bi-Directional SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ah, SFP MSA, ITU-T G.983
Connections Supported
100BASE-BX
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1550 nm
Average Power Output
-14 to -8 dBm
Receiver Sensitivity
-32 dBm
Transmission Distance
~20 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-100-BXLC-D

<<<PAGE 30>>>
Small Form-Factor Pluggables
100 FX Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-20
SFP-100-LC-MM
SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3u, SFP MSA
Connections supported
100BASE-FX
Fiber Type
MMF
Wavelength
1310 nm
Optical Power Output
-19 to -14 dBm on 62.5/125µm
-22 to 14 dBm on 50/125µm 
Transmission Distance
~2 km on 62.5/125µm
~2 km on 50/125µm 
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Not Supported
SFP-100-LC-SM15
SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3u, SFP MSA
Connections Supported
100BASE-FX
Fiber Type
SMF
Wavelength (nm)
1310 nm
Optical Power Output
-15 to -8 dBm
Receiver Sensitivity
-34 dBm
Transmission Distance
~15 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Not Supported
SFP-100-LC-SM40
SFP Optical Transceiver. 
Connector Type
LC

<<<PAGE 31>>>
Small Form-Factor Pluggables
100 FX Ethernet Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-21
.
Standards Supported
802.3u, SFP MSA
Connections Supported
100BASE-FX
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-15 to -8 dBm
Receiver Sensitivity
-34 dBm
Transmission Distances
~40 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
No longer purchasable.
SFP-100-LC-SM40
SFP Optical Transceiver.

<<<PAGE 32>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-22
10-Gigabit SFP+ Transceivers
SFP-10G-SR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3 Clause 52
Connections supported
10GBASE-SR
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-7.3 to -3.0 dBm
Receiver Sensitivity
-11.1 dBm
Transmission Distance
~ 300 m
Operating Temperature
-5 ºC to 70ºC
Maximum Power Consumption
1 W
Digital Diagnostic Monitoring
Supported
SFP-10G-LR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3 Clause 52
Connections supported
10GBASE-LR
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-8.2 to 0.5 dBm
Receiver Sensitivity
-10.3 dBm
Transmission Distance
~ 10 km
Operating Temperature
-5 ºC to 70ºC
Maximum Power Consumption
1 W
Digital Diagnostic Monitoring
Supported

<<<PAGE 33>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-23
SFP-10G-ER
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ae
Connections supported
10GBASE-ER
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
-4.7 to 4.0 dBm
Receiver Damage Threshold
4.0 dBm
Receiver Sensitivity
-14.1 dBm
Transmission Distance
~ 40 km
Operating Temperature
-5 ºC to 70 ºC
Maximum Power Consumption
1.5 W
Digital Diagnostic Monitoring
Supported
SFP-10G-LRM
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3aq
Connections supported
10GBASE-LRM
Fiber Type
MMF
Wavelength
1310 nm
Optical Power Output
-4.5 to 1.5dBm
Receiver Sensitivity
-6.5 dBm
Transmission Distance
~ 220 m
Operating Temperature
-5 ºC to 70ºC
Maximum Power Consumption
1 Watt
Digital Diagnostic Monitoring
Supported
SFP-10G-ZR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ae
Connections supported
10GBASE-ZR

<<<PAGE 34>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-24
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
0 to +4 dBm
Receiver Overload
-7 dBm
Receiver Sensitivity
-24 dBm
Transmission Distance
~ 80 km
Operating Temperature
0 ºC to 70 ºC
Maximum Power Consumption
1.2 W
Digital Diagnostic Monitoring
Supported
SFP-10G-T
10-Gigabit SFP+ Copper Transceiver. 
Connector Type
RJ-45
Standards Supported
802.3an-2006
Connections supported
10GBASE-T
Cable Type
CAT6a/7
Transmission Distance
30 m
Operating Temperature
-5 ºC to 85ºC
Maximum Power Consumption
2.5W max @ 30m
Digital Diagnostic Monitoring
Not Supported
Notes:
The existing parts 903866-90 (HW Rev. -43 and -54) are being replaced 
with part 903866-90 (HW Rev. A53). The existing 903866-90 (HW Rev. -
43 and -54) will continue to work with all AOS releases. 
903866-90 (HW Rev. A53) requires a minimum AOS release of 8.9R3.
903866-90 (HW Rev. V1.0) requires a minimum AOS release of 8.10R2.
SFP-10G-C
10-Gigabit SFP+ Direct Attach Copper Cable. 
Connector Type
Direct Attached Copper
Standards Supported
802.3ae, SFF-8431
Cable Length
60cm, 1m, 3m, 7m
Wire Gauge
24AWG
Bend Radius
1.25 in.
SFP-10G-ZR
10-Gigabit SFP+ Optical Transceiver.

<<<PAGE 35>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-25
Digital Diagnostic Monitoring
Not Supported
Note: The iSFP-10G-C1M/C3M/C7M and the SFP-10G-C1M/C3M/C7M are the same part and can be 
used interchangeably on either the commercial or industrial switches. 
SFP-10G-24DWD80
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ae
Connections supported
10GBASE-ZR
Fiber Type
SMF
Wavelength
1558.17 nm
Optical Power Output
0 to 5dBm
Receiver Sensitivity
-23 dBm
Transmission Distance
~ 80 km
Operating Temperature
-5ºC to 70ºC
Maximum Power Consumption
1.2 Watt
Digital Diagnostic Monitoring
Supported
Notes:
No longer purchasable.
SFP-10G-C
10-Gigabit SFP+ Direct Attach Copper Cable.

<<<PAGE 36>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-26
SFP-10G-GIG-SR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3-2005
Connections supported
10GBASE-SR/SW, 1000BASE-SX
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-5 to -1 @ 10G
-9.5 to -1dBm @ 1G
Receiver Sensitivity
-11.1 dBm @ 10G
-17 dBm @ 1G
Transmission Distance
OM1: ~33m @ 10G, ~275m @ 1G
OM2: ~82m @ 10G, ~550m @ 1G
OM3: ~300m @ 10G, ~550m @ 1G
Operating Temperature
0ºC to 70ºC
Maximum Power Consumption
<1.0 Watt
Digital Diagnostic Monitoring
Supported
SFP-10G-GIG-LR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3-2005
Connections supported
10GBASE-LR/LW, 1000BASE-LX
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-8.2 to +5 dBm @ 10G
-11 to -3 dBm @ 1G
Receiver Sensitivity
-12.6 dBm @ 10G
-19 dBm @ 1G
Transmission Distance
~10 km
Operating Temperature
-5ºC to 70ºC
Maximum Power Consumption
<1.0 Watt
Digital Diagnostic Monitoring
Supported

<<<PAGE 37>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-27
SFP-10G-BX-D
Bi-Directional SFP+ Optical Transceiver.
Connector Type
LC
Standards Supported
SFP MSA
Connections Supported
10GBASE-LR
Fiber Type
SMF
Wavelength
Transmit: 1330 nm
Receive: 1270 nm
Average Power Output
-2 to +3 dBm
Receiver Sensitivity
-13 dBm
Transmission Distance
~10 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
- Designed for use with SFP-10G-BX-U. 
- Does not support VFL connections. 
SFP-10G-BX-U
Bi-Directional SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
SFP MSA
Connections Supported
10GBASE-LR
Fiber Type
SMF
Wavelength
Transmit: 1270 nm
Receive: 1330 nm
Average Power Output
-2 to +3 dBm
Receiver Sensitivity
-13 dBm
Transmission Distance
~10 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
- Designed for use with SFP-10G-BX-D.
- Does not support VFL connections.

<<<PAGE 38>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-28
SFP-10G-BX-D40
Bi-Directional SFP+ Optical Transceiver.
Connector Type
LC
Standards Supported
SFP MSA
Connections Supported
10GBASE-LR
Fiber Type
SMF
Wavelength
Transmit: 1330 nm
Receive: 1270 nm
Average Power Output
+1 to +5 dBm
Receiver Overload
0.5 dBm
Receiver Sensitivity
-15 dBm
Transmission Distance
~40 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
- Designed for use with SFP-10G-BX-U40. 
- Does not support VFL connections. 
SFP-10G-BX-U40
Bi-Directional SFP+ Optical Transceiver.
Connector Type
LC
Standards Supported
SFP MSA
Connections Supported
10GBASE-LR
Fiber Type
SMF
Wavelength
Transmit: 1270 nm
Receive: 1330 nm
Average Power Output
+1 to +5 dBm
Receiver Sensitivity
-15 dBm
Transmission Distance
~40 km
Operating Temperature
0 ºC to 70 ºC
Digital Diagnostic Monitoring
Supported
Notes:
- Designed for use with SFP-10G-BX-D40. 
- Does not support VFL connections.

<<<PAGE 39>>>
Small Form-Factor Pluggables
10-Gigabit SFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-29
SFP-10G-CWDM
10-Gigabit CWDM SFP+ transceiver.
Connector Type
LC
Standards Supported
SFP MSA, SFF-8472, SFF-8431, SFF-8432
Connections Supported
10GBASE-ER/EW
Fiber Type
SMF
Wavelength
1551 nm
Average Power Output
-1 to +4 dBm
Receiver Overload
-1 dBm
Receiver Sensitivity
-16 dBm
Transmission Distance
40 km
Operating Temperature
-40ºC to 85ºC
Maximum Power Consumption
<2.3 Watt
Digital Diagnostic Monitoring
Supported

<<<PAGE 40>>>
Small Form-Factor Pluggables
25-Gigabit SFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-30
25-Gigabit SFP28 Transceivers
CAUTION - CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH 
OPTICAL INSTRUMENTS.
SFP-25G-SR
25-Gigabit SFP28 Optical Transceiver. 
Connector Type
LC
Compliant/Compatible* 
Standards 
802.3by, SFP MSA, SFF-8472/8402/8432*/8431*
Applications
25GBASE-SR
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-8.4 to +2.4 dBm
Receiver Sensitivity
-10.3 dBm
Transmission Distance
OM2 - ~20 m
OM3 - ~70 m
OM4 - ~100 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
1.2 W
Digital Diagnostic Monitoring
Supported

<<<PAGE 41>>>
Small Form-Factor Pluggables
25-Gigabit SFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-31
SFP-25G-ESR
25-Gigabit SFP28 Optical Transceiver. 
Connector Type
LC
Compliant/Compatible 
Standards
SFP28 MSA, SFF-8431 and SFF-8432
Applications
25GBASE-SR
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-4.3 to +3 dBm
Receiver Sensitivity
-5.2 dBm
Transmission Distance
OM4 - 300 m
Operating Temperature
0 ºC to 70ºC
Digital Diagnostic Monitoring
Supported
SFP-25G-LR
25-Gigabit SFP28 Optical Transceiver. 
Connector Type
LC
Compliant/Compatible* 
Standards 
802.3cc-2017, SFP MSA, SFF-8472/8432*/8431*
Applications
25GBASE-LR
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-7 to +2 dBm
Receiver Sensitivity
-11.3 dBm
Transmission Distance
~10 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
1.5
Digital Diagnostic Monitoring
Supported

<<<PAGE 42>>>
Small Form-Factor Pluggables
25-Gigabit SFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-32
SFP-25G-CLR
25-Gigabit SFP28 Optical Transceiver. 
Connector Type
LC
Compliant/Compatible Stan-
dards
SFP28 MSA, SFF-8431 and SFF-8432
Applications
25GBASE-LR
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-5.0 to +3.0 dBm
Receiver Sensitivity
-10.3 dBm
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
1.5 W
Digital Diagnostic Monitoring
Supported
SFP-25G-A20M
25-Gigabit SFP28 Active Optical Cable. 
Connector Type
Direct Attached
Compliant / Compatible* Stan-
dards
SFF-8431, SFF-8432*
Transmission Distance
20 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
-
Digital Diagnostic Monitoring
Supported
SFP-25G-C
25-Gigabit SFP28 Direct Attach Copper Cable. 
Connector Type
Direct Attached Copper
Standards Supported
802.3by
Cable Length
1m, 3m, 5m
Wire Gauge
26-30 AWG
Bend Radius
35 mm
Digital Diagnostic Monitoring
Not Supported

<<<PAGE 43>>>
Small Form-Factor Pluggables
25-Gigabit SFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-33
SFP-25G-BX-D40
25-Gigabit Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
SFF-8402
Connections Supported
25GBASE-ER
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1270 nm
Average Power Output
-1 to 6 dBm
Receiver Overload
-4 dBm
Receiver Sensitivity
-19 dBm
Transmission Distance
~40 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-25G-BX-U40
SFP-25G-BX-U40
25-Gigabit Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
SFF-8402
Connections Supported
25GBASE-ER
Fiber Type
SMF
Wavelength
Transmit: 1270 nm
Receive: 1310 nm
Average Power Output
-1 to 6 dBm
Receiver Overload
-4 dBm
Receiver Sensitivity
-19 dBm
Transmission Distance
~40 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with SFP-25G-BX-D40

<<<PAGE 44>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-34
40-Gigabit QSFP+ Transceivers
CAUTION - CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH 
OPTICAL INSTRUMENTS.
QSFP-40G-SR
Four channel 40-Gigabit QSFP+ Optical Transceiver. 
Connector Type
MPO-12
Standards Supported
802.3ba, QSFP+ MSA
Connections supported
40GBASE-SR4
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-7.6 to +1.0 dBm
Receiver Sensitivity
-9.5 dBm
Transmission Distance
OM3 - ~ 100 m
OM4 - ~150 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
1.5 W
Digital Diagnostic Monitoring
Supported1
Notes:
Supports 4X10G splitter mode.
1. Supports the DDM parameters of Voltage (V), Temperature (T), Current (mA) and Input (dBm). If the 
threshold values of the transceiver are ‘0’ then NS will be displayed in the DDM output display. 
QSFP-40G-SR-BD
Dual channel 40-Gigabit QSFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ba-2010, QSFP+ MSA
Connections supported
40GBASE-SR4
Fiber Type
MMF
Wavelength
850 / 900 nm
Optical Power Output
-4.0 to +5.0 dBm
Receiver Sensitivity
-7.1 / -7.7 dBm
Transmission Distance
OM3 - ~ 100 m
OM4 - ~150 m
Operating Temperature
10 ºC to 70ºC
Maximum Power Consumption
3.5 W

<<<PAGE 45>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-35
Digital Diagnostic Monitoring
Not Supported
Notes:
Does not support VFL connections.
No longer purchasable.
QSFP-40G-LR
Four channel 40-Gigabit QSFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ba, QSFP+ MSA
Connections supported
40GBASE-LR4
Fiber Type
SMF
Wavelength(nm)
1264.5 – 1277.5
1284.5 – 1297.5
1304.5 – 1317.5
1324.5 – 1337.5
Optical Power Output
-7.0 to +2.3 dBm
Receiver Sensitivity
-11.5 dBm
Transmission Distance
10 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
< 3.5 W
Digital Diagnostic Monitoring
Supported
QSFP-40G-ER
Four channel 40-Gigabit QSFP+ Optical Transceiver.
Connector Type
LC
Standards Supported
802.3bm, QSFP+ MSA
Connections supported
40GBASE-ER4
Fiber Type
SMF
Wavelength (nm)
1264.5 – 1277.5
1284.5 – 1297.5
1304.5 – 1317.5
1324.5 – 1337.5
Optical Power Output
-2.7 to +4.5 dBm
Receiver Damage Threshold
3.8 dBm
Receiver Sensitivity
-19.0 dBm
Transmission Distance
40 km
Operating Temperature
0 ºC to 70ºC
QSFP-40G-SR-BD
Dual channel 40-Gigabit QSFP+ Optical Transceiver.

<<<PAGE 46>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-36
Maximum Power Consumption
< 3.5 W
Digital Diagnostic Monitoring
Supported1
QSFP-40G-LM4
Four channel 40-Gigabit QSFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ba, QSFP+ MSA
Connections supported
40GBASE-LM4
Fiber Type
MMF
Wavelength (nm)
1264.5 – 1277.5
1284.5 – 1297.5
1304.5 – 1317.5
1324.5 – 1337.5
Optical Power Output
-7.0 to +4.3 dBm
Receiver Sensitivity
-10.5 dBm
Transmission Distance
OM3 - ~ 140 m
OM4 - ~160 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
3.5 W
Digital Diagnostic Monitoring
Supported
Notes: 
No longer purchasable.
QSFP-40G-CLR
Four channel 40-Gigabit QSFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ba, QSFP+ MSA
Connections supported
40GBASE-LR4
Fiber Type
SMF
Wavelength (nm)
1264.5 – 1277.5
1284.5 – 1297.5
1304.5 – 1317.5
1324.5 – 1337.5
Optical Power Output
-9.0 to +2.3 dBm
Receiver Sensitivity
-11.0 dBm
QSFP-40G-ER
Four channel 40-Gigabit QSFP+ Optical Transceiver.

<<<PAGE 47>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-37
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
2.5 W
Digital Diagnostic Monitoring
Supported
QSFP-40G-PSM4
40-Gigabit QSFP+ PSM4 Optical Transceiver. 
Connector Type
MPO-12
Standards Supported
802.3bm, QSFP+ MSA
Fiber Type
SMF
Wavelength (nm)
1310 nm
Optical Power Output
-8.2 to +2 dBm
Damage Threshold
+3.3 dBm
Receiver Sensitivity
-12.6 dBm
Transmission Distance
10 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
< 3.5 W
Digital Diagnostic Monitoring
Supported
Notes:
Supports 4X10G splitter mode.
QSFP-40G-C
Four channel 40-Gigabit QSFP+ Direct Attach Copper Cable
Connector Type
Direct Attached Copper
Standards Supported
802.3ba, QSFP+ MSA
Cable Length
40cm, 1m, 3m, 7m1,2,3
Wire Gauge
26AWG
Bend Radius
1.69 in.
Digital Diagnostic Monitoring
Not Supported
QSFP-40G-CLR
Four channel 40-Gigabit QSFP+ Optical Transceiver.

<<<PAGE 48>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-38
1. Check for availability of lengths.
2. The QSFP-40G-C7M (7m) cable has been verified for proper operation when connected between 
OmniSwitch products. When connecting this cable between an OmniSwitch and other vendors’ equip-
ment, it’s recommended to verify proper operation prior to network deployment.
3. When connecting any QSFP-40G-C direct attached transceiver between the OS9900 and the OS6900, 
auto-negotiation must be disabled on the OS9900 port.
QSFP-4X10G-SR
Four channel 40-Gigabit QSFP+ Optical Transceiver. Connects a single 40G QSFP+ port to four 10G SFP+ 
ports
Connector Type
MPO-12
Standards Supported
802.3ba, 802.3ae, QSFP+ MSA
Connections supported
40GBASE-SR4, 10GBASE-SR
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-7.5 to +0.5 dBm
Receiver Sensitivity
-11.1 dBm
Transmission Distance
OM3 - ~ 300 m
OM4 - ~400 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
1.5 W
Digital Diagnostic Monitoring
Supported1
1. Supports the DDM parameters of Voltage (V), Temperature (T), Current (mA) and Input (dBm). If the 
threshold values of the transceiver are ‘0’ then NS will be displayed in the DDM output display. 
QSFP-4X10G-C
Four channel 40-Gigabit QSFP+ Direct Attached Copper Splitter Cable. Connects a single 40G QSFP+ port to 
four 10G SFP+ ports.
Connector Type
Direct Attached Copper Splitter Cable
Cable Length
1m, 3m, 5m
Digital Diagnostic Monitoring
Not Supported
QSFP-40G-C
Four channel 40-Gigabit QSFP+ Direct Attach Copper Cable

<<<PAGE 49>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-39
QSFP-40G-AOC20M
Four channel 40-Gigabit QSFP+ active optical cable.
Connector Type
Direct attached
Standards Supported
802.3ba, QSFP+ MSA
Connections supported
40GBASE-SR4
Cable Length
20 m
Bend Radius
45 mm
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
< 1.3 W
Digital Diagnostics Monitoring
Supported
OS6860-CBL-100
20-Gigabit QSFP+ direct attached copper transceiver.
Connector Type
Direct Attached Copper
Standards Supported
802.3ba, QSFP+ MSA
Cable Length
1m
Wire Gauge
26AWG
Bend Radius
1.69 in.
Digital Diagnostics Monitoring
Not Supported
OS6860-CBL-300
20-Gigabit QSFP+ direct attached copper transceiver.
Connector Type
Direct Attached Copper
Standards Supported
802.3ba, QSFP+ MSA
Cable Length
3m
Wire Gauge
26AWG
Bend Radius
1.69 in.
Digital Diagnostics Monitoring
Not Supported

<<<PAGE 50>>>
Small Form-Factor Pluggables
40-Gigabit QSFP+ Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-40
OS6860-CBL-40
20-Gigabit QSFP+ direct attached copper transceiver.
Connector Type
Direct Attached Copper
Standards Supported
802.3ba, QSFP+ MSA
Cable Length
40cm
Wire Gauge
26AWG
Bend Radius
1.69 in.
Digital Diagnostics Monitoring
Not Supported

<<<PAGE 51>>>
Small Form-Factor Pluggables
50-Gigabit SFP56 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-41
50-Gigabit SFP56 Transceivers
CAUTION - CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH 
OPTICAL INSTRUMENTS.
SFP-50G-SR
50-Gigabit SFP56 Optical Transceiver.
Connector Type
LC
Standards Supported
SFP56, 50GBASE-SR, SFF-8431/8432/8472
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output 
-6.5 to +4.0 dBm
Receiver Sensitivity
-3.4 dBm
Transmission Distance
100m on OM4 MMF
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
3.3 W
Digital Diagnostic Monitoring
Supported
Notes:
SFP-50G-FR
50-Gigabit SFP56 Optical Transceiver.
Connector Type
LC
Standards Supported
SFP56, 50GBASE-FR, SFF-8432/8472
Fiber Type
SMF
Wavelength
1311 nm
Optical Power Output 
-4.1 to +3.0 dBm
Receiver Sensitivity
-6.9 dBm
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
2.0 W
Digital Diagnostic Monitoring
Supported
Notes:

<<<PAGE 52>>>
Small Form-Factor Pluggables
50-Gigabit SFP56 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-42
SFP-50G-LR
50-Gigabit SFP56 Optical Transceiver.
Connector Type
LC
Standards Supported
SFP56, 50GBASE-LR, SFF-8432/8472
Fiber Type
SMF
Wavelength
1311 nm
Optical Power Output 
-4.5 to +4.2 dBm
Receiver Sensitivity
-8.4 dBm
Transmission Distance
10 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
2.0 W
Digital Diagnostic Monitoring
Supported
Notes: 
SFP-50G-C
50-Gigabit SFP56 Direct Attach Copper Cable. 
Connector Type
Direct Attached Copper
Standards Supported
SFF-8432/8472
Cable Length
50cm, 1m, 3m
Wire Gauge
26-30 AWG
Operating Temperature
-20 ºC to 75ºC
Digital Diagnostic Monitoring
Not Supported
Notes:

<<<PAGE 53>>>
Small Form-Factor Pluggables
100-Gigabit QSFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-43
100-Gigabit QSFP28 Transceivers
QSFP-100G-SR4 
Four channel 100-Gigabit QSFP28 Optical Transceiver. 
Connector Type
MPO-12
Standards Supported
802.3bm, QSFP28 MSA
Connections supported
100GBASE-SR4
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-8.4 to +2.4 dBm
Receiver Sensitivity
-10.3 dBm
Transmission Distance
OM3 - ~ 70 m
OM4 - ~100 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
 3.5 W
Digital Diagnostic Monitoring
Supported
Notes:
Supports 4X25G splitter mode.
QSFP-100G-LR4
Four channel 100-Gigabit QSFP28 Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ba, QSFP28 MSA
Connections supported
100GBASE-LR4
Fiber Type
SMF
Wavelength (nm)
1294.53 – 1296.59
1299.02 – 1301.09
1303.54 – 1305.63
1308.09 – 1310.19
Optical Power Output
-4.3 to +4.5 dBm
Receiver Sensitivity
-8.6 dBm
Transmission Distance
10 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
3.5 W
Digital Diagnostic Monitoring
Supported

<<<PAGE 54>>>
Small Form-Factor Pluggables
100-Gigabit QSFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-44
QSFP-100G-CLR4
Four channel 100-Gigabit QSFP28 Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ba, QSFP28 MSA
Connections supported
100GBASE-LR4 Lite
Fiber Type
SMF
Wavelength (nm)
1294.53 – 1296.59
1299.02 – 1301.09
1303.54 – 1305.63
1308.09 – 1310.19
Optical Power Output
-6.0 to +4.5 dBm
Receiver Sensitivity
-8.4 dBm
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
3.5 W
Digital Diagnostic Monitoring
Supported
QSFP-100G-ER4
Four channel 100-Gigabit QSFP28 Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3-2018, QSFP28 MSA, SFF-8661, SFF-8636
Connections supported
100G 4WDM-40
Fiber Type
SMF
Wavelength (nm)
1294.53 – 1296.59
1299.02 – 1301.09
1303.54 – 1305.63
1308.09 – 1310.19
Optical Power Output
-2.5 to +6.5 dBm
Receiver Overload
-3.5 dBm
Receiver Sensitivity
-18.5 dBm
Transmission Distance
40 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
4.5 W
Digital Diagnostic Monitoring
Supported

<<<PAGE 55>>>
Small Form-Factor Pluggables
100-Gigabit QSFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-45
QSFP-100G-A20M
Four channel 100-Gigabit QSFP28 Active Optical Cable. 
Connector Type
Direct Attached
Fiber Type
MMF
Transmission Distance
20 m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
3.5 W
Digital Diagnostic Monitoring
Not Supported
Notes:
Auto-negotiation should be disabled and FEC configured to RS.
QSFP-100G-CWDM4
Four channel 100-Gigabit QSFP28 Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3bm, QSFP28 MSA
Connections supported
-
Fiber Type
SMF
Wavelength (nm)
1264.5 – 1277.5
1284.5 – 1297.5
1304.5 – 1317.5
1324.5 – 1337.5
Optical Power Output
-4.0 to +2.5 dBm
Receiver Sensitivity
-10 dBm
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
3.5 W
Digital Diagnostic Monitoring
Supported
QSFP-100G-C
Four channel 100-Gigabit QSFP28 Direct Attached Copper Cable. 
Connector Type
Direct Attached Copper Cable
Cable Length
1m, 3m, 5m, 40cm
Digital Diagnostic Monitoring
Not Supported

<<<PAGE 56>>>
Small Form-Factor Pluggables
100-Gigabit QSFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-46
QSFP-4X25G-C
Four channel 100-Gigabit QSFP+ Direct Attached Copper Splitter Cable. Connects a single 100G QSFP28 port 
to four 25G SFP28 ports.
Connector Type
Direct Attached Copper Cable
Cable Length
1m, 3m, 5m
Digital Diagnostic Monitoring
Not Supported
QSFP-100G-SR1.2
100G QSFP28 Optical Transceiver 
Connector Type
LC
Standards Supported
QSFP28 MSA
Connections supported
-
Fiber Type
SMF
Wavelength (nm)
850 nm/908 nm
Optical Power Output
-6.2 to +4.0 dBm
Receiver Sensitivity
-6.6 dBm
Transmission Distance
70m over OM3
100m over OM4
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
4 W
Digital Diagnostic Monitoring
-
Note: Connects to QSFPD-400G-SR4.2 breakout.
QSFP-100G-PSM4
100G QSFP28 PSM4 Transceiver
Connector Type
MPO
Standards Supported
QSFP28 MSA
Connections supported
-
Fiber Type
SMF
Wavelength (nm)
1310 nm
Optical Power Output
-6.5 to +2.5 dBm

<<<PAGE 57>>>
Small Form-Factor Pluggables
100-Gigabit QSFP28 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-47
Receiver Sensitivity
-10.5 dBm
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
< 3.5 W
Digital Diagnostic Monitoring
Supported
QSFP-100G-PSM4
100G QSFP28 PSM4 Transceiver

<<<PAGE 58>>>
Small Form-Factor Pluggables
200-Gigabit QSFP56 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-48
200-Gigabit QSFP56 Transceivers
CAUTION - CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH 
OPTICAL INSTRUMENTS.
QSFP-200G-SR4
200-Gigabit QSFP56 Optical Transceiver.
Connector Type
MPO-12
Standards Supported
QSFP56, 200GBASE-SR4
Fiber Type
MMF
Wavelength
840-860 nm
Optical Power Output 
-6.5 to +4.0 dBm
Receiver Sensitivity
-6.5 dBm
Transmission Distance
100m on OM4 MMF
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
< 4.5 W
Digital Diagnostic Monitoring
Supported
Notes:
QSFP-200G-FR4
200-Gigabit QSFP56 Optical Transceiver.
Connector Type
LC
Standards Supported
QSFP56, 200GBASE-FR4
Fiber Type
SMF
Wavelength
1264.5 - 1277.5 nm
1284.5 - 1297.5 nm
1304.5 - 1317.5 nm
1324.5 - 1337.5 nm
Optical Power Output 
-4.2 to +4.7 dBm
Receiver Sensitivity
-6.0 dBm
Transmission Distance
2 km
Operating Temperature
-0 ºC to 70ºC
Maximum Power Consumption
6 W
Digital Diagnostic Monitoring
Supported
Notes:

<<<PAGE 59>>>
Small Form-Factor Pluggables
200-Gigabit QSFP56 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-49
QSFP-200G-A20M
200-Gigabit QSFP56 Active Optical Cable.
Connector Type
Direct Attached
Fiber Type
SMF
Cable Length
20m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
5.0 W
Digital Diagnostic Monitoring
-
QSFP-200G-C
200-Gigabit QSFP56 Direct Attach Copper Cable. 
Connector Type
Direct Attached Copper
Standards Supported
QSFP56, SFF-8636
Cable Length
50cm, 1m, 3m
Wire Gauge
30, 30, 26 AWG
Operating Temperature
-20 ºC to 75ºC
Digital Diagnostic Monitoring
Supported
Notes:
QSFP-2XQ100-C
200G QSFP56 to 2x100G QSFP56 Passive Direct Attach Cable
Connector Type
Direct Attached Copper
Standards Supported
QSFP56
Cable Length
1m, 3m
Wire Gauge
30 AWG
Operating Temperature
0 ºC to 70ºC
Digital Diagnostic Monitoring
Not Supported
QSFP-2XQ200-C
400G QSFP-DD to 2x200G QSFP56 Passive Direct Attach Cable
Connector Type
Direct Attached Copper
Standards Supported
QSFP-DD MSA
Cable Length
1m, 3m

<<<PAGE 60>>>
Small Form-Factor Pluggables
200-Gigabit QSFP56 Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-50
Wire Gauge
30 AWG
Operating Temperature
0 ºC to 70ºC
Digital Diagnostic Monitoring
Not Supported
QSFP-2XQ100-C
200G QSFP56 to 2x100G QSFP56 Passive Direct Attach Cable
Connector Type
Direct Attached Copper
Standards Supported
QSFP56
Cable Length
1m, 3m
Wire Gauge
30 AWG
Operating Temperature
0 ºC to 70ºC
Digital Diagnostic Monitoring
Not Supported
QSFP-2XQ200-C
400G QSFP-DD to 2x200G QSFP56 Passive Direct Attach Cable

<<<PAGE 61>>>
Small Form-Factor Pluggables
400-Gigabit QSFP-DD Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-51
400-Gigabit QSFP-DD Transceivers
CAUTION - CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH 
OPTICAL INSTRUMENTS.
QSFPD-400G-C
400G QSFP-DD Passive Direct Attach Cable
Connector Type
Direct Attached Copper
Standards Supported
QSFP-DD MSA
Cable Length
50cm, 1m, 3m
Wire Gauge
30 AWG
Operating Temperature
0 ºC to 70ºC
Digital Diagnostic Monitoring
Not Supported
QSFPD-400G-DR4
400G QSFP-DD Transceiver
Connector Type
MPO-12
Standards Supported
QSFP-DD MSA
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output 
-2.9 to +4.0 dBm
Receiver Sensitivity
-4.4 dBm
Transmission Distance
500m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
10.0 W
Digital Diagnostic Monitoring
Supported
QSFPD-400G-FR4
400G QSFP-DD Transceiver
Connector Type
LC
Standards Supported
QSFP-DD MSA
Fiber Type
SMF
Wavelength
1271, 1291, 1311, 1331 nm

<<<PAGE 62>>>
Small Form-Factor Pluggables
400-Gigabit QSFP-DD Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-52
Optical Power Output 
-3.2 to +4.4 dBm
Receiver Sensitivity
-4.6 dBm
Transmission Distance
2 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
10.0 W
Digital Diagnostic Monitoring
Supported
QSFPD-400G-LR4
400G QSFP-DD Transceiver
Connector Type
LC
Standards Supported
QSFP-DD MSA
Fiber Type
SMF
Wavelength
1271, 1291, 1311, 1331 nm
Optical Power Output 
-2.7 to +5.1 dBm
Receiver Sensitivity
-6.8 dBm
Transmission Distance
10 km
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
10.0 W
Digital Diagnostic Monitoring
Supported
QSFPD-400G-A10M
400G QSFP-DD Active Optical Cable
Connector Type
Direct Attached
Standards Supported
QSFP DD MSA
Cable Length
10m
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
< 10.0 W
Digital Diagnostic Monitoring
Supported
QSFPD-400G-FR4
400G QSFP-DD Transceiver

<<<PAGE 63>>>
Small Form-Factor Pluggables
400-Gigabit QSFP-DD Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-53
QSFP-400G-SR4.2
400G QSFP-DD SR4.2 Transceiver
Connector Type
MPO-12
Standards Supported
QSFP-DD MSA
Fiber Type
MMF
Wavelength
850 nm/908 nm 
Optical Power Output 
-6.5 to +4.0 dBm
Receiver Sensitivity
-6.6 dBm
Transmission Distance
100m on OM4 multi-mode Fiber
Operating Temperature
0 ºC to 70ºC
Maximum Power Consumption
12.0 W
Digital Diagnostic Monitoring
-
Notes: Supports 4X breakout to QSFP-100G-SR1.2.
QSFPD-2Q100-C
200G QSFP-DD to 2x100G QSFP28 Passive Direct Attached Cable.
Connector Type
Direct Attached Copper
Standards Supported
QSFP-DD, QSFP-28 MSA 
Cable Length
1m, 3m
Wire Gauge
30 AWG
Operating Temperature
0 ºC to 70ºC
Digital Diagnostic Monitoring
Not Supported

<<<PAGE 64>>>
Small Form-Factor Pluggables
GPON Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-54
GPON Transceivers
3FE46541AA
Description
G-010S-A,GPON SFP ONT,1xGE UNI
3FE49327AA
Description
XS-010S-Q,XGS PON ONT,1x10GE

<<<PAGE 65>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-55
Industrial Transceivers
iSFP-GIG-SX
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-SX
Fiber Type
MMF
Wavelength
850 nm
Optical Power Output
-9.0 to -2.5 dBm
Receiver Sensitivity
-18 dBm
Transmission Distance
~300 m on 62.5/125µm
~500 m on 50/125µm 
Operating Temperature
-40ºC to 85ºC 
Digital Diagnostic Monitoring
Supported
iSFP-GIG-LX
Gigabit SFP Optical Transceiver. 
Connector types
LC
Standards supported
802.3z, SFP MSA
Connections supported
1000BASE-LX
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-9.5 to -3 dBm
Receiver Sensitivity
-19 dBm
Transmission Distance
10 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported

<<<PAGE 66>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-56
iSFP-GIG-LH40
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-LH40
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-2 to +3 dBm
Receiver Overload
-3 dBm
Receiver Sensitivity
-23 dBm
Transmission Distance
~40 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
iSFP-GIG-LH70
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA
Connections Supported
1000BASE-LH70
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
0 to +5 dBm
Receiver Overload
-3 dBm
Receiver Sensitivity
-22 dBm
Transmission Distance
~70 km
Operating Temperature
-40 ºC to 85ºC
Digital Diagnostic Monitoring
Supported

<<<PAGE 67>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-57
iSFP-GIG-T
Gigabit SFP Copper Transceiver. 
Connector Type
RJ-45
Standards Supported
802.3z, SFP MSA
Connections supported
10/100/1000BASE-T
Cable Type
CAT5, CAT5e, CAT6
Transmission Distance
100 m
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Not Supported
iSFP-GIG-BX-D
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX10
Fiber Type
SMF
Wavelength
Transmit: 1490 nm
Receive: 1310 nm
Average Power Output
-9 to -3 dBm
Receiver Sensitivity
-19.5 dBm
Transmission Distance
~10 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with iSFP-GIG-BX-U
iSFP-GIG-BX-U
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ah, SFP MSA
Connections Supported
1000BASE-BX10
Fiber Type
SMF
Wavelength
Transmit: 1310 nm
Receive: 1490 nm

<<<PAGE 68>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-58
Average Power Output
-9 to -3 dBm
Receiver Sensitivity
-19.5 dBm
Transmission Distance
~10 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with iSFP-GIG-BX-D
iSFP-10G-SR
10-Gigabit SFP+ Optical Transceiver.
Connector Type
LC
Standards Supported
802.3ae, SFP MSA
Connections Supported
10GBASE-SR
Fiber Type
MMF
Wavelength
850 nm
Average Power Output
-7.3 to -1 dBm
Receiver Sensitivity
-11.1 dBm
Transmission Distance
~300 m
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
iSFP-10G-LR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3 Clause 52
Connections supported
10GBASE-LR
Fiber Type
SMF
Wavelength
1310 nm
Optical Power Output
-8.2 to 0.5 dBm
Receiver Sensitivity
-10.3 dBm
Transmission Distance
~ 10 km
Operating Temperature
-40 ºC to 85 ºC
Maximum Power Consumption
1 W
Digital Diagnostic Monitoring
Supported
iSFP-GIG-BX-U
Bi-Directional SFP Optical Transceiver.

<<<PAGE 69>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-59
iSFP-10G-ER
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ae
Connections supported
10GBASE-ER
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
-4.7 to 4.0 dBm
Receiver Damage Threshold
4 dBm
Receiver Sensitivity
-14.1 dBm
Transmission Distance
~ 40 km
Operating Temperature
-40 ºC to 85 ºC
Maximum Power Consumption
1.5 W
Digital Diagnostic Monitoring
Supported
iSFP-10G-ZR
10-Gigabit SFP+ Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3ae
Connections supported
10GBASE-ZR
Fiber Type
SMF
Wavelength
1550 nm
Optical Power Output
0 to +4 dBm
Receiver Overload
-7 dBm
Receiver Sensitivity
-24 dBm
Transmission Distance
~ 80 km
Operating Temperature
-40 ºC to 85ºC
Maximum Power Consumption
1.2 W
Digital Diagnostic Monitoring
Supported
iSFP-10G-C
10-Gigabit SFP+ Direct Attach Copper Cable. 
Connector Type
Direct Attached Copper
Standards Supported
802.3ae, SFF-8431

<<<PAGE 70>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-60
Cable Length
1m, 3m, 7m1
Wire Gauge
24AWG
Bend Radius
1.25 in.
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Not Supported
Note: The iSFP-10G-C1M/C3M/C7M and the SFP-10G-C1M/C3M/C7M are the same part and can be 
used interchangeably on either the commercial or industrial switches. 
OS6865-CBL-40/100/300
Four channel 40-Gigabit QSFP+ Direct Attach Copper Cable
Connector Type
Direct Attached Copper
Standards Supported
802.3ba, QSFP+ MSA
Cable Length
40cm, 1m, 3m
Wire Gauge
26AWG
Bend Radius
1.69 in.
Operating Temperature
-40ºC to 85ºC 
Digital Diagnostic Monitoring
Not Supported
iSFP-10G-C
10-Gigabit SFP+ Direct Attach Copper Cable.

<<<PAGE 71>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-61
iSFP-100-MM
SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
SFP MSA
Connections supported
100BASE-FX
Fiber Type
MMF
Wavelength
1310 nm
Optical Power Output
-20 to -14 dBm on 62.5/125µm
Receiver Sensitivity
-31 dBm
Transmission Distance
~2 km on 62.5/125µm
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Not Supported
iSFP-100-SM15
SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
SFP MSA
Connections Supported
100BASE-FX
Fiber Type
SMF
Wavelength (nm)
1310 nm
Optical Power Output
-15 to -8 dBm
Receiver Sensitivity
-28 dBm
Transmission Distance
~15 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Not Supported
iSFP-100-SM40
SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
SFP MSA
Connections Supported
100BASE-FX
Fiber Type
SMF

<<<PAGE 72>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-62
Wavelength (nm)
1310 nm
Optical Power Output
-5 to 0 dBm
Receiver Sensitivity
-34 dBm
Transmission Distance
~40 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes: 
No longer purchasable.
iSFP-100-BXLC-D
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
SFP MSA SFF-8074i
Connections Supported
100BASE-LX
Fiber Type
SMF
Wavelength
Transmit: 1550 nm
Receive: 1310 nm
Average Power Output
-15 to -8 dBm
Receiver Sensitivity
-28 dBm
Transmission Distance
~20 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with iSFP-100-BXLC-U
No longer purchasable.
iSFP-100-BXLC-U
Bi-Directional SFP Optical Transceiver.
Connector Type
LC
Standards Supported
SFP MSA SFF-8074i
Connections Supported
100BASE-LX
Fiber Type
SMF
iSFP-100-SM40
SFP Optical Transceiver.

<<<PAGE 73>>>
Small Form-Factor Pluggables
Industrial Transceivers
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 1-63
Wavelength
Transmit: 1310 nm
Receive: 1550 nm
Average Power Output
-15 to -8 dBm
Receiver Sensitivity
-28 dBm
Transmission Distance
~20 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes:
Designed for use with iSFP-100-BXLC-D
No longer purchasable.
iSFP-GIG-EZX
Gigabit SFP Optical Transceiver. 
Connector Type
LC
Standards Supported
802.3z, SFP MSA, SFF-8472
Connections Supported
-
Fiber Type
SMF
Wavelength
1550 nm
Average Power Output
0 to +5dBm
Receiver Overload
-8 dBm
Receiver Sensitivity
-35 dBm
Transmission Distance
~120 km
Operating Temperature
-40 ºC to 85 ºC
Digital Diagnostic Monitoring
Supported
Notes: 
No longer purchasable.
iSFP-100-BXLC-U
Bi-Directional SFP Optical Transceiver.

<<<PAGE 74>>>
Transceiver Compatibility Matrix
In This Chapter
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-64
2   Transceiver Compatibility
Matrix
In This Chapter
The following sections document the transceiver configurations and minimum release required for support 
on the OmniSwitch. 
Compatibility specifications in this chapter include:
• OmniSwitch 6360. See “OmniSwitch 6360 Compatibility” on page 2-65
• OmniSwitch 6465. See “OmniSwitch 6465 Compatibility” on page 2-67
• OmniSwitch 6465T. See “OmniSwitch 6465T Compatibility” on page 2-68
• OmniSwitch 6560(E). See “OmniSwitch 6560(E) Compatibility” on page 2-70
• OmniSwitch 6570M. See “OmniSwitch 6570M Compatibility” on page 2-73
• OmniSwitch 6575. See “OmniSwitch 6575 Compatibility” on page 2-76
• OmniSwitch 6860. See “OmniSwitch 6860 Compatibility” on page 2-77
• OmniSwitch 6860N. See “OmniSwitch 6860N Compatibility” on page 2-80
• OmniSwitch 6865. See “OmniSwitch 6865 Compatibility” on page 2-83
• OmniSwitch 6870. See “OmniSwitch 6870 Compatibility” on page 2-84
• OmniSwitch 6900-V72/C32/C32E. See “OmniSwitch 6900-V72/C32/C32E Compatibility” on 
page 2-87
• OmniSwitch 6900. See “OmniSwitch 6900 Compatibility” on page 2-90
• OmniSwitch 6920. See “OmniSwitch 6920 Compatibility” on page 2-93
• OmniSwitch 9900. See “OmniSwitch 9900 Compatibility” on page 2-95
Note: For transceivers supporting Digital Diagnostics Monitoring there may be a slight variance between 
actual and reported values for both the transmit and receive side depending on the transceiver.

<<<PAGE 75>>>
Transceiver Compatibility Matrix
OmniSwitch 6360 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-65
OmniSwitch 6360 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OmniSwitch 6360
SFP-GIG-SX
8.7R2
SFP-GIG-LX
8.7R2
SFP-GIG-LH40
8.7R2
SFP-GIG-LH70 
8.7R2
SFP-GIG-EZX
N/S
SFP-GIG-##CWD
(no longer purchasable)
N/S
SFP-GIG-T1
8.7R2 or 8.9R3
SFP-1G-T
8.7R2
SFP-GIG-EXTND
(no longer purchasable)
N/S
SFP-GIG-BX-D
8.7R2
SFP-GIG-BX-U
8.7R2
SFP-GIG-BX-D20
8.8R1
SFP-GIG-BX-U20
8.8R1
SFP-GIG-BX-D40
8.8R1
SFP-GIG-BX-U40
8.8R1
SFP-DUAL-MM
(no longer purchasable)
N/S
SFP-DUAL-MM-N
N/S
SFP-DUAL-SM10 
(no longer purchasable)
N/S
SFP-DUAL-BX-D 
N/S
SFP-DUAL-BX-U
N/S
SFP-100-BX20LT
(no longer purchasable)
N/S
SFP-100-BX20NU
(no longer purchasable)
N/S
SFP-100-BXLC-D 
N/S
SFP-100-BXLC-U 
N/S
SFP-100-LC-MM 
N/S
SFP-100-LC-SM15 
N/S
SFP-100-LC-SM40 
N/S
SFP-10G-SR
8.7R2
SFP-10G-LR
8.7R2

<<<PAGE 76>>>
Transceiver Compatibility Matrix
OmniSwitch 6360 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-66
1. Refer to the transceiver specifications table for minimum AOS requirements.
2. The following models and ports are supported: 
• OS6360-P10 (ports 11-12)
• OS6360-P24 (ports 25-28) 
• OS6360-PH24 (ports 25-28)
• OS6360-P48 (ports 49-52)
• OS6360-P24X (ports 25-28)
• OS6360-P48X (ports 49-52)
3. The following models and ports are supported: 
• OS6360-P24 (ports 27-28) 
• OS6360-PH24 (ports 27-28)
• OS6360-P48 (ports 51-52)
• OS6360-P24X (ports 25-28)
• OS6360-P48X (ports 49-52)
SFP-10G-ER
8.7R2
SFP-10G-LRM
N/S
SFP-10G-ZR
N/S
SFP-10G-T1
8.8R1 or 8.9R3
SFP-10G-C
- SFP-10G-C60CM (OS6360-CBL-60CM)
- SFP-10G-C1M (OS6360-CBL-1M)
- SFP-10G-C3M (OS6360-CBL-3M)
- SFP-10G-C7M
8.7R2
SFP-10G-24DWD80
(no longer purchasable)
N/S
SFP-10G-GIG-SR
8.8R1
SFP-10G-GIG-LR
8.8R1
SFP-10G-BX-D
8.7R2
SFP-10G-BX-U
8.7R2
SFP-10G-BX-D40
8.9R1
SFP-10G-BX-U40
8.9R1
SFP-10G-CWDM
N/S
3FE46541AA 2
8.8R1
3FE49327AA 3
8.8R2
Transceiver
OmniSwitch 6360

<<<PAGE 77>>>
Transceiver Compatibility Matrix
OmniSwitch 6465 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-67
OmniSwitch 6465 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6465
OS6465 (ENH-240)
iSFP-GIG-SX
8.5R1
8.8R1
iSFP-GIG-LX
8.5R1
8.8R1
iSFP-GIG-LH40
8.5R1
8.8R1
iSFP-GIG-LH70
8.5R1
8.8R1
iSFP-GIG-BX-D
8.5R1
8.8R1
iSFP-GIG-BX-U
8.5R1
8.8R1
iSFP-GIG-T
8.5R1
8.8R1
iSFP-GIG-EZX
(no longer purchasable)
8.8R1
8.8R1
iSFP-10G-SR
8.8R1
Not Supported
iSFP-10G-LR
8.5R2
Not Supported
iSFP-10G-ER 
8.5R2
Not Supported
iSFP-10G-ZR 
8.7R1
Not Supported
iSFP-10G-C 
(1M/3M/7M)
8.5R2
8.8R1
iSFP-100-MM
8.5R1
8.8R1
iSFP-100-SM15
8.5R1
8.8R1
iSFP-100-SM40 
(no longer purchasable)
8.5R1 
8.8R1
iSFP-100-BXLC-D 
(no longer purchasable)
Supported
8.8R1
iSFP-100-BXLC-U 
(no longer purchasable)
Supported
8.8R1
3FE46541AA
Not Supported
Not Supported
3FE49327AA
Not Supported
Not Supported

<<<PAGE 78>>>
Transceiver Compatibility Matrix
OmniSwitch 6465T Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-68
OmniSwitch 6465T Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OmniSwitch 6465T
SFP-GIG-SX
8.6R1
SFP-GIG-LX
8.6R1
SFP-GIG-LH40
8.6R1
SFP-GIG-LH70 
8.6R1
SFP-GIG-EZX
Not Supported
SFP-GIG-##CWD
(no longer purchasable)
Not Supported
SFP-GIG-T3
8.6R1 or 8.9R3
SFP-1G-T
8.6R2
SFP-GIG-EXTND
(no longer purchasable)
8.6R1
SFP-GIG-BX-D
8.6R1
SFP-GIG-BX-U
8.6R1
SFP-GIG-BX-D20
Not Supported
SFP-GIG-BX-U20
Not Supported
SFP-GIG-BX-D40
Not Supported
SFP-GIG-BX-U40
Not Supported
SFP-DUAL-MM
(no longer purchasable)
8.6R1
SFP-DUAL-MM-N3
8.6R1 or 8.9R3
SFP-DUAL-SM10
(no longer purchasable)
Not Supported
SFP-DUAL-BX-D
8.6R1
SFP-DUAL-BX-U
8.6R1
SFP-100-BX20LT
(no longer purchasable)
8.6R1
SFP-100-BX20NU
(no longer purchasable)
8.6R1
SFP-100-BXLC-D 
8.6R1
SFP-100-BXLC-U 
8.6R1
SFP-100-LC-MM 
8.6R1
SFP-100-LC-SM15 
8.6R1
SFP-100-LC-SM40 
(no longer purchasable)
8.6R1

<<<PAGE 79>>>
Transceiver Compatibility Matrix
OmniSwitch 6465T Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-69
1. Supported for VFL connections only. 
2. OS6465T-P12 (ports 9-12).
3. Refer to the transceiver specifications table for minimum AOS requirements.
SFP-10G-C1
- SFP-10G-C60CM (OS6465T-CBL-60)
- SFP-10G-C1M (OS6465T-CBL-1M)
- SFP-10G-C3M (OS6465T-CBL-3M)
- SFP-10G-C7M
8.5R2
3FE46541AA 2
8.7R1
3FE49327AA
Not Supported
Transceiver
OmniSwitch 6465T

<<<PAGE 80>>>
Transceiver Compatibility Matrix
OmniSwitch 6560(E) Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-70
OmniSwitch 6560(E) Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OmniSwitch 6560(E)
SFP-GIG-SX
8.4.1.R02
SFP-GIG-LX
8.4.1.R02
SFP-GIG-LH40
8.4.1.R02
SFP-GIG-LH70 
8.4.1.R02
SFP-GIG-EZX
(no longer purchasable)
8.9R1
SFP-GIG-##CWD
(no longer purchasable)
Not Supported
SFP-GIG-T1,9
8.4.1.R02 or 8.9R3
SFP-1G-T
8.6R2
SFP-GIG-EXTND 
(no longer purchasable)
8.4.1.R02
SFP-GIG-BX-D
8.4.1.R02
SFP-GIG-BX-U
8.4.1.R02
SFP-GIG-BX-D20
8.4.1.R02
SFP-GIG-BX-U20
8.4.1.R02
SFP-GIG-BX-D40
8.4.1.R02
SFP-GIG-BX-U40
8.4.1.R02
SFP-DUAL-MM 1
(no longer purchasable)
8.4.1.R02
SFP-DUAL-MM-N1,9
8.4.1.R02 or 8.9R3
SFP-DUAL-SM10 1
(no longer purchasable)
Not Supported
SFP-DUAL-BX-D 1
8.4.1.R02
SFP-DUAL-BX-U 1
8.4.1.R02
SFP-100-BX20LT
(no longer purchasable)
Not Supported
SFP-100-BX20NU
(no longer purchasable)
Not Supported
SFP-100-BXLC-D 
Not Supported
SFP-100-BXLC-U 
Not Supported
SFP-100-LC-MM 
Not Supported
SFP-100-LC-SM15 
Not Supported
SFP-100-LC-SM40 
Not Supported
SFP-10G-SR
8.4.1.R02

<<<PAGE 81>>>
Transceiver Compatibility Matrix
OmniSwitch 6560(E) Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-71
SFP-10G-LR
8.4.1.R02
SFP-10G-ER
8.4.1.R02
SFP-10G-LRM7
8.6R2
SFP-10G-ZR
8.4.1.R02 or 8.6R16
SFP-10G-T9
8.4.1.R02 or 8.9R3
SFP-10G-C3
- SFP-10G-C60CM
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
8.4.1.R02
SFP-10G-24DWD80
(no longer purchasable)
Not Supported
SFP-10G-GIG-SR4
8.4.1.R02
SFP-10G-GIG-LR4
8.4.1.R02
SFP-10G-BX-D5
8.6R1
SFP-10G-BX-U5
8.6R1
SFP-10G-BX-D40
8.9R1
SFP-10G-BX-U40
8.9R1
SFP-10G-CWDM
8.6R1
QSFP-40G-SR2
8.4.1.R02
QSFP-40G-SR-BD
Not Supported
QSFP-40G-LR
Not Supported
QSFP-40G-ER
Not Supported
QSFP-40G-LM4
(no longer purchasable)
Not Supported
QSFP-40G-CLR
Not Supported
QSFP-40G-PSM4
Not Supported
QSFP-40G-C2
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- QSFP-40G-C7M (Not supported)
- OS6560-CBL-100
- OS6560-CBL-300
- OS6560-CBL-40
8.4.1.R02
QSFP-4X10G-SR
Not Supported
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
Not Supported
QSFP-40G-AOC20M2
8.4.1.R02
3FE46541AA 8
8.7R1
3FE49327AA10
8.8R2
Transceiver
OmniSwitch 6560(E)

<<<PAGE 82>>>
Transceiver Compatibility Matrix
OmniSwitch 6560(E) Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-72
NOTE: Ports 25/26 (OS6560-24X4/P24X4) and ports 49/50 (OS6560-48X4/P48X4) require the OS6560-
SW-PERF license to operate at 10G. Ports support 1G by default.
1. Support 1Gbps only with this transceiver. 
2. Supported for VFL connections only. Cannot be used in 4X10G splitter mode.
3. SFP-10G-C7M not supported on (P)24Z24, (P)24Z8, (P)24X4 and ports 53/54 for OS6560-(P)48X4 
models.
4. Not supported on OS6560-X10.
5. Does not support VFL connections. 
6. Minimum supported AOS version is 8.6R1 if the transceiver was purchased after May 2019.
7. Only the following models and ports support the SFP-10G-LRM.
OS6560-48X4/P48X4 
• Ports 49-50 with OS6560-SW-PERF applied.
• Ports 51/52.
OS6560-P48Z16 (904044-90)
• Ports 49-52.
OS6560-X10 
• Ports 1-8.
8. The following models and ports are supported: 
• OS6560-P24X4 (ports 25-30) 
• OS6560(E)-P24Z8 (ports 25-26)
9. Refer to the transceiver specifications table for minimum AOS requirements.
10. The following models and ports are supported: 
• OS6560-X10 (ports 1-8) 
• OS6560(E)-P48Z16 (ports 49-52)
• OS6560-P48X4 (ports 51-54)
• OS6560-P24Z4 (ports 25-28)
• OS6560-P24X4 (ports 27-30)

<<<PAGE 83>>>
Transceiver Compatibility Matrix
OmniSwitch 6570M Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-73
OmniSwitch 6570M Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OmniSwitch 6570M
SFP-GIG-SX
8.9R2
SFP-GIG-LX
8.9R2
SFP-GIG-LH40
8.9R2
SFP-GIG-LH70 
8.9R2
SFP-GIG-EZX
(no longer purchasable)
8.9R2
SFP-GIG-##CWD
(no longer purchasable)
Not Supported
SFP-GIG-T1,5
8.9R2 or 8.9R3
SFP-1G-T
8.9R2
SFP-GIG-EXTND 
(no longer purchasable)
8.9R2
SFP-GIG-BX-D
8.9R2
SFP-GIG-BX-U
8.9R2
SFP-GIG-BX-D20
8.9R2
SFP-GIG-BX-U20
8.9R2
SFP-GIG-BX-D40
8.9R2
SFP-GIG-BX-U40
8.9R2
SFP-DUAL-MM 
(no longer purchasable)
Not Supported
SFP-DUAL-MM-N2,5
8.9R2 or 8.9R3
SFP-DUAL-SM10 
(no longer purchasable)
Not Supported
SFP-DUAL-BX-D 2
8.9R2
SFP-DUAL-BX-U 2
8.9R2
SFP-100-BX20LT
(no longer purchasable)
Not Supported
SFP-100-BX20NU
(no longer purchasable)
Not Supported
SFP-100-BXLC-D 
8.9R2
SFP-100-BXLC-U 
8.9R2
SFP-100-LC-MM 
8.9R2
SFP-100-LC-SM15 
8.9R2
SFP-100-LC-SM40 
(no longer purchasable)
8.9R2

<<<PAGE 84>>>
Transceiver Compatibility Matrix
OmniSwitch 6570M Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-74
1. Not supported on OS6570M-U28 combo ports. 
2. Supports 1G only with this transceiver. 
3. Supports 10G only with this transceiver. 
4. Does not support VFL connections. 
5. Refer to the transceiver specifications table for minimum AOS requirements.
SFP-10G-SR
8.9R2
SFP-10G-LR
8.9R2
SFP-10G-ER
8.9R2
SFP-10G-LRM
Not Supported
SFP-10G-ZR
8.9R2
SFP-10G-T3,5
8.9R2 or 8.9R3
SFP-10G-C
- SFP-10G-C60CM
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
8.9R2
SFP-10G-24DWD80
(no longer purchasable)
8.9R2
SFP-10G-GIG-SR
8.9R2
SFP-10G-GIG-LR
8.9R2
SFP-10G-BX-D4
8.9R2
SFP-10G-BX-U4
8.9R2
SFP-10G-BX-D40
Not Supported
SFP-10G-BX-U40
Not Supported
SFP-10G-CWDM
8.9R2
SFP-25G-SR
8.10R4
SFP-25G-ESR
8.10R4
SFP-25G-LR
8.10R4
SFP-25G-CLR
8.10R4
SFP-25G-A20M
8.10R4
SFP-25G-C
- SFP-25G-C1M
- SFP-25G-C3M
- SFP-25G-C5M
8.10R4
SFP-25G-BX-D40
Not Supported
SFP-25G-BX-U40
Not Supported
3FE46541AA
Not Supported
3FE49327AA6
8.9R2
Transceiver
OmniSwitch 6570M

<<<PAGE 85>>>
Transceiver Compatibility Matrix
OmniSwitch 6570M Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-75
6. The following models and ports are supported: 
• OS6570M-U28 (ports 25-30)

<<<PAGE 86>>>
Transceiver Compatibility Matrix
OmniSwitch 6575 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-76
OmniSwitch 6575 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6575
iSFP-GIG-SX
8.10R4
iSFP-GIG-LX
8.10R4
iSFP-GIG-LH40
8.10R4
iSFP-GIG-LH70
8.10R4
iSFP-GIG-BX-D
8.10R4
iSFP-GIG-BX-U
8.10R4
iSFP-GIG-T
8.10R4
iSFP-GIG-EZX
(no longer purchasable)
Not Supported
iSFP-10G-SR
8.10R4
iSFP-10G-LR
8.10R4
iSFP-10G-ER 
8.10R4
iSFP-10G-ZR 
8.10R4
iSFP-10G-C 
(1M/3M/7M)
8.10R4
iSFP-100-MM
8.10R4
iSFP-100-SM15
8.10R4
iSFP-100-SM40 
(no longer purchasable)
8.10R4
iSFP-100-BXLC-D 
(no longer purchasable)
Not Supported
iSFP-100-BXLC-U 
(no longer purchasable)
Not Supported

<<<PAGE 87>>>
Transceiver Compatibility Matrix
OmniSwitch 6860 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-77
OmniSwitch 6860 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6860/6860E
(Excluding U28)
OS6860E-U28
SFP-GIG-SX
8.1.1
8.1.1
SFP-GIG-LX
8.1.1
8.1.1
SFP-GIG-LH40
8.1.1
8.1.1
SFP-GIG-LH70 
8.1.1
8.1.1
SFP-GIG-EZX
(no longer purchasable)
8.9R1
8.9R1
SFP-GIG-##CWD
(no longer purchasable)
8.1.1
8.1.1
SFP-GIG-T1,7
8.1.1 or 8.9R3
8.1.1 or 8.9R3
SFP-1G-T
8.6R2
8.6R2
SFP-GIG-EXTND
(no longer purchasable)
8.1.1
8.1.1
SFP-GIG-BX-D
8.1.1
8.1.1
SFP-GIG-BX-U
8.1.1
8.1.1
SFP-GIG-BX-D20
8.1.1
8.1.1
SFP-GIG-BX-U20
8.1.1
8.1.1
SFP-GIG-BX-D40
8.1.1
8.1.1
SFP-GIG-BX-U40
8.1.1
8.1.1
SFP-DUAL-MM 2
(no longer purchasable)
Not Supported
8.4.1.R01
SFP-DUAL-MM-N2,7
8.4.1.R01 or 8.9R3
8.4.1.R01 or 8.9R3
SFP-DUAL-SM10 2
(no longer purchasable)
Not Supported
8.4.1.R01
SFP-DUAL-BX-D 2
Not Supported
8.4.1.R01
SFP-DUAL-BX-U 2
Not Supported
8.4.1.R01
SFP-100-BX20LT
(no longer purchasable)
Not Supported
Not Supported
SFP-100-BX20NU
(no longer purchasable)
Not Supported
Not Supported
SFP-100-BXLC-D
Not Supported
8.1.1
SFP-100-BXLC-U
Not Supported
8.1.1
SFP-100-LC-MM
Not Supported
8.1.1
SFP-100-LC-SM15
Not Supported
8.1.1
SFP-100-LC-SM40
(no longer purchasable)
Not Supported
8.1.1

<<<PAGE 88>>>
Transceiver Compatibility Matrix
OmniSwitch 6860 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-78
SFP-10G-SR
8.1.1
8.1.1
SFP-10G-LR
8.1.1
8.1.1
SFP-10G-ER
8.1.1
8.1.1
SFP-10G-LRM
8.1.1
8.1.1
SFP-10G-ZR
8.2.1 or 8.6R16
8.2.1 or 8.6R16
SFP-10G-T7
8.3.1.R02 or 8.9R3
8.3.1.R02 or 8.9R3
SFP-10G-C
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
8.1.1
8.1.1
SFP-10G-24DWD80
(no longer purchasable)
Not Supported
Not Supported
SFP-10G-GIG-SR3
8.1.1
8.1.1
SFP-10G-GIG-LR3
8.2.1
8.2.1
SFP-10G-BX-D5
8.6R1
8.6R1
SFP-10G-BX-U5
8.6R1
8.6R1
SFP-10G-BX-D40
8.9R1
8.9R1
SFP-10G-BX-U40
8.9R1
8.9R1
SFP-10G-CWDM
8.6R1
8.6R1
QSFP-40G-SR4
8.1.1
8.1.1
QSFP-40G-SR-BD
Not Supported
Not Supported
QSFP-40G-LR
Not Supported
Not Supported
QSFP-40G-ER
Not Supported
Not Supported
QSFP-40G-LM4
Not Supported
Not Supported
QSFP-40G-CLR
Not Supported
Not Supported
QSFP-40G-PSM4
Not Supported
Not Supported
QSFP-40G-C4
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- OS6860-CBL-100
- OS6860-CBL-300
- OS6860-CBL-40
8.1.1
8.1.1
QSFP-4X10G-SR4
8.4.1.R01
8.4.1.R01
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
Not Supported
Not Supported
QSFP-40G-AOC20M4
8.2.1
8.2.1
Transceiver
OS6860/6860E
(Excluding U28)
OS6860E-U28

<<<PAGE 89>>>
Transceiver Compatibility Matrix
OmniSwitch 6860 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-79
1. OS6860E-U28 user ports (1 - 28) support 10/100/1000. All 6860 uplink ports support 1Gbps only with 
this transceiver. If manually setting the user port speed to 10M the transceiver must first be inserted before 
setting the speed.
2. Supports 100/1000 on OS6860E-U28 SFP user ports (1 - 28) only. Uplink ports support 1G only. 
3. Not supported on OS6860E-U28 1G SFP user ports (1-28). 
4. Supported for 20-Gigabit VFL connections only.
5. Does not support VFL connections.
6. Minimum supported AOS version is 8.6R1 if the transceiver was purchased after May 2019.
7. Refer to the transceiver specifications table for minimum AOS requirements.
3FE46541AA
Not Supported
Not Supported
3FE49327AA
Not Supported
Not Supported
Transceiver
OS6860/6860E
(Excluding U28)
OS6860E-U28

<<<PAGE 90>>>
OmniSwitch 6860N Compatibility
Transceiver Compatibility Matrix
page 2-80
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
OmniSwitch 6860N Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6860N
-P24Z5
OS6860N
-P48Z5
OS6860N
-P24M
OS6860N
-P48M
OS6860N
-U285
OS68-
XNI-U4
OS68-
VNI-U4
OS68-
QNI-U2
OS68-
CNI-U1
SFP-GIG-SX
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-LX
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-LH40
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-LH70 
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-EZX
(no longer purchasable)
8.9R1
8.9R1
N/A
N/A
8.9R1
8.9R1
8.9R1
N/A
N/A
SFP-GIG-##CWD
(no longer purchasable)
N/S
N/S
N/A
N/A
N/S
N/S
N/S
N/A
N/A
SFP-GIG-T2,6
N/S
N/S
N/A
N/A
8.7R1 or 
8.9R3
8.7R2 or 
8.9R3
N/S
N/A
N/A
SFP-1G-T2
N/S
N/S
N/A
N/A
8.7R1
8.7R1
N/S
N/A
N/A
SFP-GIG-EXTND
(no longer purchasable)
8.8R1
8.7R2
N/A
N/A
8.7R2
8.7R2
8.7R2
N/A
N/A
SFP-GIG-BX-D
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-BX-U
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-BX-D20
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-BX-U20
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-BX-D40
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-GIG-BX-U40
8.8R1
8.7R2
N/A
N/A
8.7R1
8.7R1
8.7R2
N/A
N/A
SFP-DUAL-MM 
(no longer purchasable)
N/S
N/S
N/A
N/A
N/S
N/S
N/S
N/A
N/A
SFP-DUAL-MM-
N3,6
8.8R1 or 
8.9R3
8.8R1 or 
8.9R3
N/A
N/A
8.7R1 or 
8.9R3
8.7R2 or 
8.9R3
8.8R1 or 
8.9R3
N/A
N/A
SFP-DUAL-SM10 
(no longer purchasable)
N/S
N/S
N/A
N/A
N/S
N/S
N/S
N/A
N/A
SFP-DUAL-BX-D 3
8.8R1
8.8R1
N/A
N/A
8.7R1
8.7R1
8.8R1
N/A
N/A
SFP-DUAL-BX-U 3
8.8R1
8.8R1
N/A
N/A
8.7R1
8.7R1
8.8R1
N/A
N/A
SFP-100-BX20LT
(no longer purchasable)
N/S
N/S
N/A
N/A
N/S
N/S
N/S
N/A
N/A
SFP-100-BX20NU
(no longer purchasable)
N/S
N/S
N/A
N/A
N/S
N/S
N/S
N/A
N/A
SFP-100-BXLC-D
N/S
N/S
N/A
N/A
8.7R1
N/S
N/S
N/A
N/A
SFP-100-BXLC-U
N/S
N/S
N/A
N/A
8.7R1
N/S
N/S
N/A
N/A
SFP-100-LC-MM
N/S
N/S
N/A
N/A
8.7R1
N/S
N/S
N/A
N/A
SFP-100-LC-SM15
N/S
N/S
N/A
N/A
8.7R1
N/S
N/S
N/A
N/A
SFP-100-LC-SM40
(no longer purchasable)
N/S
N/S
N/A
N/A
8.7R1
N/S
N/S
N/A
N/A
SFP-10G-SR
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-LR
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-ER
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A

<<<PAGE 91>>>
Transceiver Compatibility Matrix
OmniSwitch 6860N Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-81
SFP-10G-LRM
N/S
N/S
N/A
N/A
8.7R1
8.7R1
N/S
N/A
N/A
SFP-10G-ZR
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-T4,6
8.8R1 or 
8.9R3
8.7R1 or 
8.9R3
N/A
N/A
8.7R1 or 
8.9R3
8.7R1 or 
8.9R3
8.7R1 or 
8.9R3
N/A
N/A
SFP-10G-C
- SFP-10G-C60CM
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-
24DWD80
(no longer purchasable)
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-GIG-SR
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-GIG-LR
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-BX-D1
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-BX-U1
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-10G-BX-D40
8.9R1
8.9R1
N/A
N/A
8.9R1
8.9R1
8.9R1
N/A
N/A
SFP-10G-BX-U40
8.9R1
8.9R1
N/A
N/A
8.9R1
8.9R1
8.9R1
N/A
N/A
SFP-10G-CWDM
8.8R1
8.7R1
N/A
N/A
8.7R1
8.7R1
8.7R1
N/A
N/A
SFP-25G-SR
8.8R1
8.7R1
N/A
N/A
8.7R1
N/S
8.7R1
N/A
N/A
SFP-25G-ESR
8.9R2
8.9R2
N/A
N/A
8.9R2
N/S
8.9R2
N/A
N/A
SFP-25G-LR
8.8R1
8.7R1
N/A
N/A
8.7R1
N/S
8.7R1
N/A
N/A
SFP-25G-CLR
8.8R1
8.7R1
N/A
N/A
8.7R1
N/S
8.7R1
N/A
N/A
SFP-25G-A20M
8.8R1
8.7R1
N/A
N/A
8.7R1
N/S
8.7R1
N/A
N/A
SFP-25G-C
- SFP-25G-C1M
- SFP-25G-C3M
- SFP-25G-C5M
8.8R1
8.7R1
N/A
N/A
8.7R1
N/S
8.7R1
N/A
N/A
SFP-25G-BX-D40
8.9R1
8.9R1
N/A
N/A
8.9R1
N/S
8.9R1
N/A
N/A
SFP-25G-BX-U40
8.9R1
8.9R1
N/A
N/A
8.9R1
N/S
8.9R1
N/A
N/A
QSFP-40G-SR
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
8.7R1
8.7R2
QSFP-40G-SR-BD1
(no longer purchasable)
8.8R1
N/S
8.8R1
8.7R1
N/S
N/A
N/A
8.7R1
8.7R2
QSFP-40G-LR
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
8.7R1
8.7R2
QSFP-40G-ER
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
8.7R1
8.7R2
QSFP-40G-LM4
(no longer purchasable)
8.8R1
8.8R1
8.8R1
8.8R1
8.8R1
N/A
N/A
8.8R1
8.8R1
QSFP-40G-CLR
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
8.7R1
8.7R2
QSFP-40G-PSM4
8.9R1
8.9R1
8.9R1
8.9R1
8.9R1
N/A
N/A
8.9R1
8.9R1
QSFP-40G-C
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- QSFP-40G-C7M
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
8.7R1
8.7R2
QSFP-4X10G-SR
8.8R1
N/S
8.8R1
N/S
N/S
N/A
N/A
8.7R1
8.8R1
Transceiver
OS6860N
-P24Z5
OS6860N
-P48Z5
OS6860N
-P24M
OS6860N
-P48M
OS6860N
-U285
OS68-
XNI-U4
OS68-
VNI-U4
OS68-
QNI-U2
OS68-
CNI-U1

<<<PAGE 92>>>
OmniSwitch 6860N Compatibility
Transceiver Compatibility Matrix
page 2-82
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
1. Does not support VFL connections.
2. Not supported on SFP28 ports.
3. 1G only on SFP28 ports.
4. Supports 1G and 10G on SFP28 ports. 
5. SFP28 ports do not support auto-negotiation with 1G transceivers. Always disable auto-negotiation on 
the peer switch.
6. Refer to the transceiver specifications table for minimum AOS requirements.
7. The following models and ports are supported: 
• OS6860N-P24M or OS6860N-P48M with OS68-XNI-U4.
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
8.8R1
N/S
8.8R1
N/S
N/S
N/A
N/A
8.7R1
8.8R1
QSFP-40G-AOC-
20M
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
8.7R1
8.7R2
QSFP-4X25G-C
- QSFP-4X25G-C1M
- QSFP-4X25G-C3M
- QSFP-4X25G-C5M
8.8R1
N/S
8.8R1
N/S
N/S
N/A
N/A
N/S
8.8R1
QSFP-100G-SR4
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
N/S
8.7R2
QSFP-100G-LR4
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
N/S
8.7R2
QSFP-100G-CLR4
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
N/S
8.7R2
QSFP-100G-ER4
8.8R1
8.8R1
8.8R1
8.8R1
8.8R1
N/A
N/A
N/S
8.8R1
QSFP-100G-A20M
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
N/S
8.7R2
QSFP-100G-
CWDM4
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
N/S
8.7R2
QSFP-100G-C
- QSFP-100G-C40CM
- QSFP-100G-C1M
- QSFP-100G-C3M
- QSFP-100G-C5M
8.8R1
8.7R1
8.8R1
8.7R1
8.7R1
N/A
N/A
N/S
8.7R2
QSFP-100G-SR1.2
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
N/A
N/A
N/S
8.10R4
QSFP-100G-PSM4
N/S
N/S
N/S
N/S
N/S
N/A
N/A
N/S
N/S
3FE46541AA
N/S
N/S
N/A
N/A
N/S
N/S
N/S
N/A
N/A
3FE49327AA
N/S
N/S
N/A
N/A
N/S
8.9R47
N/S
N/A
N/A
Transceiver
OS6860N
-P24Z5
OS6860N
-P48Z5
OS6860N
-P24M
OS6860N
-P48M
OS6860N
-U285
OS68-
XNI-U4
OS68-
VNI-U4
OS68-
QNI-U2
OS68-
CNI-U1

<<<PAGE 93>>>
Transceiver Compatibility Matrix
OmniSwitch 6865 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-83
OmniSwitch 6865 Compatibility
The following table shows the available transceivers and minimum release required for support:
1. OS6865-U12X and OS6865-U28X only.
Transceiver
OS6865
iSFP-GIG-SX
8.3.1
iSFP-GIG-LX
8.3.1
iSFP-GIG-LH40
8.3.1
iSFP-GIG-LH70
8.3.1
iSFP-GIG-T
8.3.1
iSFP-GIG-BX-D
8.3.1
iSFP-GIG-BX-U
8.3.1
iSFP-GIG-EZX
(no longer purchasable)
8.8R1
iSFP-10G-SR
8.8R1
iSFP-10G-LR
8.3.1
iSFP-10G-ER
8.3.1
iSFP-10G-ZR 
8.7R1
iSFP-10G-C
8.3.1
OS6865-CBL-40/100/300
8.4.1.R01
iSFP-100-MM1
8.4.1.R01
iSFP-100-SM151
8.4.1.R01
iSFP-100-SM401
(no longer purchasable)
8.4.1.R01
iSFP-100-BXLC-D 1
(no longer purchasable)
Supported
iSFP-100-BXLC-U 1
(no longer purchasable)
Supported
3FE46541AA
Not Supported
3FE49327AA
Not Supported

<<<PAGE 94>>>
OmniSwitch 6870 Compatibility
Transceiver Compatibility Matrix
page 2-84
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
OmniSwitch 6870 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6870-
24
OS6870-
P24M
OS6870-
P24Z
OS6870-
48
OS6870-
P48M
OS6870-
P48Z
OS6870-
V12
OS6870-
CNI-U2
OS6870-
LNI-U6
SFP-GIG-SX
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-LX
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-LH40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-LH70 
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-EZX
(no longer purchasable)
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-##CWD
(no longer purchasable)
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-GIG-T1
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-1G-T
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-EXTND
(no longer purchasable)
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-BX-D
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-BX-U
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-BX-D20
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-BX-U20
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-BX-D40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-GIG-BX-U40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-DUAL-MM 
(no longer purchasable)
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-DUAL-MM-N
8.10R2
N/A
N/S
8.10R2
N/A
N/S
8.10R2
N/A
N/S
SFP-DUAL-SM10 
(no longer purchasable)
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-DUAL-BX-D
8.10R2
N/A
N/S
8.10R2
N/A
N/S
8.10R2
N/A
N/S
SFP-DUAL-BX-U
8.10R2
N/A
N/S
8.10R2
N/A
N/S
8.10R2
N/A
N/S
SFP-100-BX20LT
(no longer purchasable)
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-100-BX20NU
(no longer purchasable)
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-100-BXLC-D
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-100-BXLC-U
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-100-LC-MM
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-100-LC-SM15
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-100-LC-SM40
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
SFP-10G-SR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-LR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-ER
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-LRM
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S

<<<PAGE 95>>>
Transceiver Compatibility Matrix
OmniSwitch 6870 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-85
SFP-10G-ZR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-T
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-C
- SFP-10G-C60CM
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-
24DWD80
(no longer purchasable)
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-GIG-SR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-GIG-LR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-BX-D
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-BX-U
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-BX-D40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-BX-U40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-10G-CWDM
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-SR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-ESR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-LR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-CLR
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-A20M
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-C
- SFP-25G-C1M
- SFP-25G-C3M
- SFP-25G-C5M
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-BX-D40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
SFP-25G-BX-U40
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
8.10R2
N/A
8.10R2
QSFP-40G-SR2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-SR-BD
(no longer purchasable)
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-LR
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-ER
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-LM4
(no longer purchasable)
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-CLR
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-PSM4
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-40G-C
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- QSFP-40G-C7M
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-4X10G-SR
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
Transceiver
OS6870-
24
OS6870-
P24M
OS6870-
P24Z
OS6870-
48
OS6870-
P48M
OS6870-
P48Z
OS6870-
V12
OS6870-
CNI-U2
OS6870-
LNI-U6

<<<PAGE 96>>>
OmniSwitch 6870 Compatibility
Transceiver Compatibility Matrix
page 2-86
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
1. Supports 1G speed only.
2. Does not support Auto-VFL when in splitter mode.
QSFP-40G-AOC-
20M
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
SFP-50G-SR
N/S
N/S
N/A
N/S
N/S
N/A
N/S
N/A
8.10R2
SFP-50G-LR
N/S
N/S
N/A
N/S
N/S
N/A
N/S
N/A
8.10R2
SFP-50G-FR
N/S
N/S
N/A
N/S
N/S
N/A
N/S
N/A
8.10R2
SFP-50G-C
- SFP-50G-C50CM
- SFP-50G-C1M
- SFP-50G-C3M
N/S
N/S
N/A
N/S
N/S
N/A
N/S
N/A
8.10R2
QSFP-4X25G-C
- QSFP-4X25G-C1M
- QSFP-4X25G-C3M
- QSFP-4X25G-C5M
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-SR42
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-LR4
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-CLR4
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-ER4
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-A20M
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-
CWDM4
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-C
- QSFP-100G-C40CM
- QSFP-100G-C1M
- QSFP-100G-C3M
- QSFP-100G-C5M
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
8.10R2
N/A
QSFP-100G-SR1.2
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
N/A
QSFP-100G-PSM4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
N/A
QSFP-200G-SR4
N/S
8.10R2
N/S
N/S
8.10R2
N/S
8.10R2
N/S
N/A
QSFP-200G-FR4
N/S
8.10R2
N/S
N/S
8.10R2
N/S
8.10R2
N/S
N/A
QSFP-200G-A20M
N/S
8.10R2
N/S
N/S
8.10R2
N/S
8.10R2
N/S
N/A
QSFP-200G-C
- SFP-200G-C50CM
- SFP-200G-C1M
- SFP-200G-C3M
N//S
8.10R2
N//S
N//S
8.10R2
N//S
8.10R2
N/S
N/A
3FE46541AA
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
3FE49327AA
N/S
N/A
N/S
N/S
N/A
N/S
N/S
N/A
N/S
Transceiver
OS6870-
24
OS6870-
P24M
OS6870-
P24Z
OS6870-
48
OS6870-
P48M
OS6870-
P48Z
OS6870-
V12
OS6870-
CNI-U2
OS6870-
LNI-U6

<<<PAGE 97>>>
Transceiver Compatibility Matrix
OmniSwitch 6900-V72/C32/C32E Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-87
OmniSwitch 6900-V72/C32/C32E Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6900-V72
OS6900-C32
OS6900-C32E
SFP-GIG-SX
N/S
N/S
N/S
SFP-GIG-LX
N/S
N/S
N/S
SFP-GIG-LH40
N/S
N/S
N/S
SFP-GIG-LH70 
N/S
N/S
N/S
SFP-GIG-EZX
N/S
N/S
N/S
SFP-GIG-##CWD
(no longer purchasable)
N/S
N/S
N/S
SFP-GIG-T
N/S
N/S
N/S
SFP-1G-T
N/S
N/S
N/S
SFP-GIG-EXTND
(no longer purchasable)
N/S
N/S
N/S
SFP-GIG-BX-D
N/S
N/S
N/S
SFP-GIG-BX-U
N/S
N/S
N/S
SFP-GIG-BX-D20
N/S
N/S
N/S
SFP-GIG-BX-U20
N/S
N/S
N/S
SFP-GIG-BX-D40
N/S
N/S
N/S
SFP-GIG-BX-U40
N/S
N/S
N/S
SFP-DUAL-MM 
(no longer purchasable)
N/S
N/S
N/S
SFP-DUAL-MM-N
N/S
N/S
N/S
SFP-DUAL-SM10 
(no longer purchasable)
N/S
N/S
N/S
SFP-DUAL-BX-D 
N/S
N/S
N/S
SFP-DUAL-BX-U 
N/S
N/S
N/S
SFP-100-BX20LT
(no longer purchasable)
N/S
N/S
N/S
SFP-100-BX20NU
(no longer purchasable)
N/S
N/S
N/S
SFP-100-BXLC-D
N/S
N/S
N/S
SFP-100-BXLC-U
N/S
N/S
N/S
SFP-100-LC-MM
N/S
N/S
N/S
SFP-100-LC-SM15
N/S
N/S
N/S
SFP-100-LC-SM40
N/S
N/S
N/S
SFP-10G-SR
8.5R2
N/S
N/S
SFP-10G-LR
8.5R2
N/S
N/S
SFP-10G-ER
8.5R2
N/S
N/S
SFP-10G-LRM
N/S
N/S
N/S

<<<PAGE 98>>>
OmniSwitch 6900-V72/C32/C32E Compatibility
Transceiver Compatibility Matrix
page 2-88
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
SFP-10G-ZR
8.5R2 or 8.6R12
N/S
N/S
SFP-10G-T3
8.6R2 or 8.9R3
N/S
N/S
SFP-10G-C
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
8.5R2
N/S
N/S
SFP-10G-24DWD80
(no longer purchasable)
8.5R2
N/S
N/S
SFP-10G-GIG-SR
N/S
N/S
N/S
SFP-10G-GIG-LR
N/S
N/S
N/S
SFP-10G-BX-D1
8.6R1
N/S
N/S
SFP-10G-BX-U1
8.6R1
N/S
N/S
SFP-10G-BX-D40
8.9R1
N/S
N/S
SFP-10G-BX-U40
8.9R1
N/S
N/S
SFP-10G-CWDM
8.6R1
N/S
N/S
SFP-25G-SR
8.5R2
N/S
N/S
SFP-25G-ESR
8.9R2
N/S
N/S
SFP-25G-LR
8.5R2
N/S
N/S
SFP-25G-CLR
8.5R2
N/S
N/S
SFP-25G-A20M
8.5R2
N/S
N/S
SFP-25G-C
- SFP-25G-C1M
- SFP-25G-C3M
- SFP-25G-C5M
8.5R2
N/S
N/S
SFP-25G-BX-D40
8.9R1
N/S
N/S
SFP-25G-BX-U40
8.9R1
N/S
N/S
QSFP-40G-SR
8.5R2
8.5R2
8.8R1
QSFP-40G-SR-BD1
(no longer purchasable)
8.5R2
8.5R2
8.8R1
QSFP-40G-LR
8.5R2
8.5R2
8.8R1
QSFP-40G-ER
8.6R1
8.6R1
8.8R1
QSFP-40G-LM4
(no longer purchasable)
8.8R1
8.8R1
8.8R1
QSFP-40G-CLR
8.5R2
8.5R2
8.8R1
QSFP-40G-PSM4
8.9R1
8.9R1
8.9R1
QSFP-40G-C
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- QSFP-40G-C7M
8.5R2
8.5R2
8.8R1
QSFP-4X10G-SR
8.5R2
8.5R2
8.8R1
Transceiver
OS6900-V72
OS6900-C32
OS6900-C32E

<<<PAGE 99>>>
Transceiver Compatibility Matrix
OmniSwitch 6900-V72/C32/C32E Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-89
1. Does not support VFL connections.
2. Minimum supported AOS version is 8.6R1 if the transceiver was purchased after May 2019.
3. Refer to the transceiver specifications table for minimum AOS requirements.
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
8.5R2
8.5R2
8.8R1
QSFP-4X25G-C
- QSFP-4X25G-C1M
- QSFP-4X25G-C3M
- QSFP-4X25G-C5M
8.5R4
8.5R4
8.8R1
QSFP-40G-AOC20M
8.5R2
8.5R2
8.8R1
QSFP-100G-SR4
8.5R2
8.5R2
8.8R1
QSFP-100G-LR4
8.5R2
8.5R2
8.8R1
QSFP-100G-CLR4
8.5R2
8.5R2
8.8R1
QSFP-100G-ER4
8.8R1
8.8R1
8.8R1
QSFP-100G-A20M
8.5R2
8.5R2
8.8R1
QSFP-100G-CWDM4
8.5R2
8.5R2
8.8R1
QSFP-100G-C
- QSFP-100G-C40CM
- QSFP-100G-C1M
- QSFP-100G-C3M
- QSFP-100G-C5M
8.5R2
8.5R2
8.8R1
QSFP-100G-SR1.2
8.10R4
8.10R4
8.10R4
QSFP-100G-PSM4
8.10R4
8.10R4
8.10R4
3FE46541AA
N/S
N/S
N/S
3FE49327AA
N/S
N/S
N/S
Transceiver
OS6900-V72
OS6900-C32
OS6900-C32E

<<<PAGE 100>>>
OmniSwitch 6900 Compatibility
Transceiver Compatibility Matrix
page 2-90
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
OmniSwitch 6900 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6900-
T48C6
OS6900-
X48C67
OS6900-
X48C4E7
OS6900-
V48C87
OS6900-
T24C2
OS6900-
X24C2
SFP-GIG-SX
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-LX
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-LH40
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-LH70 
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-EZX
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
SFP-GIG-##CWD
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
SFP-GIG-T8
N/S
N/S
8.7R2 or 
8.9R34
N/S
8.9R1 or 
8.9R3
8.9R1 or 
8.9R3
SFP-1G-T
N/S
N/S
8.7R24
N/S
8.9R1
8.9R1
SFP-GIG-EXTND
(no longer purchasable)
N/S
8.7R2
8.7R2
N/S
8.9R1
8.9R1
SFP-GIG-BX-D
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-BX-U
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-BX-D20
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-BX-U20
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-BX-D40
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-GIG-BX-U40
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-DUAL-MM 
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-MM-N
N/S
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-SM10 
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-BX-D 
N/S
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-BX-U 
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-BX20LT
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-BX20NU
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-BXLC-D
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-BXLC-U
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-LC-MM
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-LC-SM15
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-LC-SM40
N/S
N/S
N/S
N/S
N/S
N/S
SFP-10G-SR
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-LR
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-ER
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1

<<<PAGE 101>>>
Transceiver Compatibility Matrix
OmniSwitch 6900 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-91
SFP-10G-LRM
N/S
N/S
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-ZR
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-T8
N/S
8.7R1 or 
8.9R31,5
8.7R2 or 
8.9R31,5
8.7R3 or 
8.9R31,5
8.9R1
8.9R1
SFP-10G-C
- SFP-10G-C60CM
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-24DWD80
(no longer purchasable)
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-GIG-SR
N/S
8.7R16
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-GIG-LR
N/S
8.7R16
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-BX-D3
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-BX-U3
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-10G-BX-D40
N/S
8.9R1
8.9R1
8.9R1
8.9R1
8.9R1
SFP-10G-BX-U40
N/S
8.9R1
8.9R1
8.9R1
8.9R1
8.9R1
SFP-10G-CWDM
N/S
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
SFP-25G-SR
N/S
N/S
8.7R2
8.7R3
N/S
N/S
SFP-25G-ESR
N/S
N/S
8.9R2
8.9R2
N/S
N/S
SFP-25G-LR
N/S
N/S
8.7R2
8.7R3
N/S
N/S
SFP-25G-CLR
N/S
N/S
8.7R2
8.7R3
N/S
N/S
SFP-25G-A20M
N/S
N/S
8.7R2
8.7R3
N/S
N/S
SFP-25G-C
- SFP-25G-C1M
- SFP-25G-C3M
- SFP-25G-C5M
N/S
N/S
8.7R2
8.7R3
N/S
N/S
SFP-25G-BX-D40
N/S
N/S
8.9R1
8.9R1
N/S
N/S
SFP-25G-BX-U40
N/S
N/S
8.9R1
8.9R1
N/S
N/S
QSFP-40G-SR
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-40G-SR-BD3
(no longer purchasable)
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-40G-LR
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-40G-ER
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-40G-LM4
(no longer purchasable)
8.8R1
8.8R1
8.8R1
8.8R1
8.9R1
8.9R1
QSFP-40G-CLR
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-40G-PSM4
8.9R1
8.9R1
8.9R1
8.9R1
8.9R1
8.9R1
QSFP-40G-C
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- QSFP-40G-C7M2
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
Transceiver
OS6900-
T48C6
OS6900-
X48C67
OS6900-
X48C4E7
OS6900-
V48C87
OS6900-
T24C2
OS6900-
X24C2

<<<PAGE 102>>>
OmniSwitch 6900 Compatibility
Transceiver Compatibility Matrix
page 2-92
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
1. Supports 1G and 10G speed.
2. The QSFP-40G-C7M is not supported.
3. Does not support VFL connections.
4. Not supported on SFP28 ports.
5. Supports a maximum of 38 SFP-10G-T transceivers per chassis.
6. Release 8.7R1 supports 10G only. 1G/10G support added in 8.7R2.
7. Does not support auto-negotiation with 1G transceivers. Always disable 
auto-negotiation on the peer switch.
8. Refer to the transceiver specifications table for minimum AOS requirements.
QSFP-4X10G-SR
8.7R3
8.7R3
8.8R1
8.8R1
8.9R1
8.9R1
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
8.7R3
8.7R3
8.8R1
8.8R1
8.9R1
8.9R1
QSFP-40G-AOC20M
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-100G-SR4
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-100G-LR4
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-100G-CLR4
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-100G-ER4
8.8R1
8.8R1
8.8R1
8.8R1
8.9R1
8.9R1
QSFP-100G-A20M
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-100G-CWDM4
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-100G-C
- QSFP-100G-C40CM
- QSFP-100G-C1M
- QSFP-100G-C3M
- QSFP-100G-C5M
8.7R1
8.7R1
8.7R2
8.7R3
8.9R1
8.9R1
QSFP-4X25G-C
- QSFP-4X25G-C1M
- QSFP-4X25G-C3M
- QSFP-4X25G-C5M
8.7R3
8.7R3
8.8R1
8.8R1
8.9R1
8.9R1
QSFP-100G-SR1.2
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
QSFP-100G-PSM4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
8.10R4
3FE46541AA
N/S
N/S
N/S
N/S
N/S
N/S
3FE49327AA
N/S
N/S
N/S
N/S
N/S
N/S
Transceiver
OS6900-
T48C6
OS6900-
X48C67
OS6900-
X48C4E7
OS6900-
V48C87
OS6900-
T24C2
OS6900-
X24C2

<<<PAGE 103>>>
Transceiver Compatibility Matrix
OmniSwitch 6920 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-93
OmniSwitch 6920 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS6900-D32
SFP-10G-SR
N/S
SFP-10G-LR
N/S
SFP-10G-ER
N/S
SFP-10G-LRM
N/S
SFP-10G-ZR
N/S
SFP-10G-T
N/S
SFP-10G-C
N/S
SFP-10G-24DWD80
(no longer purchasable)
N/S
SFP-10G-GIG-SR
N/S
SFP-10G-GIG-LR
N/S
SFP-10G-BX-D
N/S
SFP-10G-BX-U
N/S
SFP-10G-BX-D40
N/S
SFP-10G-BX-U40
N/S
SFP-10G-CWDM
N/S
SFP-25G-SR
N/S
SFP-25G-ESR
N/S
SFP-25G-LR
N/S
SFP-25G-CLR
N/S
SFP-25G-A20M
N/S
SFP-25G-C
N/S
SFP-25G-BX-D40
N/S
SFP-25G-BX-U40
N/S
QSFP-40G-SR
8.10R4
QSFP-40G-SR-BD
(no longer purchasable)
8.10R4
QSFP-40G-LR
8.10R4
QSFP-40G-ER
8.10R4
QSFP-40G-LM4
(no longer purchasable)
N/S
QSFP-40G-CLR
8.10R4
QSFP-40G-PSM4
8.10R4
QSFP-40G-C
8.10R4
QSFP-4X10G-SR
8.10R4

<<<PAGE 104>>>
OmniSwitch 6920 Compatibility
Transceiver Compatibility Matrix
page 2-94
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
QSFP-4X10G-C
8.10R4
QSFP-4X25G-C
8.10R4
QSFP-40G-AOC20M
8.10R4
SFP-50G-SR
N/S
SFP-50G-LR
N/S
SFP-50G-FR
N/S
SFP-50G-C
N//S
QSFP-100G-SR4
8.10R4
QSFP-100G-LR4
8.10R4
QSFP-100G-CLR4
8.10R4
QSFP-100G-ER4
8.10R4
QSFP-100G-A20M
8.10R4
QSFP-100G-CWDM4
8.10R4
QSFP-100G-C
8.10R4
QSFP-100G-SR1.2
8.10R4
QSFP-100G-PSM4
8.10R4
QSFP-200G-SR4
8.10R4
QSFP-200G-FR4
8.10R4
QSFP-200G-A20M
8.10R4
QSFP-200G-C
8.10R4
QSFP-2XQ100-C
8.10R4
QSFP-2XQ200-C
8.10R4
QSFPD-400G-C
8.10R4
QSFPD-400G-DR4
8.10R4
QSFPD-400G-FR4
8.10R4
QSFPD-400G-LR4
8.10R4
QSFPD-400G-A10M
8.10R4
QSFP-400G-SR4.2
8.10R4
QSFPD-2Q100-C
8.10R4
Transceiver
OS6900-D32

<<<PAGE 105>>>
Transceiver Compatibility Matrix
OmniSwitch 9900 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-95
OmniSwitch 9900 Compatibility
The following table shows the available transceivers and minimum release required for support:
Transceiver
OS99-
CMM
OS99-
CMM2
OS99-
XNI-U48
OS99-
GNI-U48
OS99-
CNI-U8
OS99-
CNI-U20
OS99-
XNI-
U24
OS99-
XNI-
U12Q
OS99-
XNI-
UP24Q2
SFP-GIG-SX
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-LX
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-LH40
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-LH70 
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-EZX
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
SFP-GIG-##CWD
(no longer purchasable)
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-GIG-T5
N/S
N/S
8.3.1 or 
8.9R31
8.4.1.R01 
or 8.9R3
N/S
N/S
8.5R4 or 
8.9R31
8.6R1 or 
8.9R3
8.6R1 or 
8.9R3
SFP-1G-T
N/S
N/S
8.6R2
8.6R2
N/S
N/S
8.6R2
8.6R2
8.6R2
SFP-GIG-EXTND
(no longer purchasable)
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-BX-D
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-BX-U
N/S
N/S
8.3.1
8.4.1.R01
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-GIG-BX-D20
N/S
N/S
8.3.1.R02
8.4.1.R01
N/S
N/S
8.5R4
N/S
N/S
SFP-GIG-BX-U20
N/S
N/S
8.3.1.R02
8.4.1.R01
N/S
N/S
8.5R4
N/S
N/S
SFP-GIG-BX-D40
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-GIG-BX-U40
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-MM 
(no longer purchasable)
N/S
N/S
8.3.1.R021
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-MM-
N1,5 
N/S
N/S
8.3.1.R02 
or 8.9R3
8.4.1.R01 
or 8.9R3
N/S
N/S
8.5R4 or 
8.9R3
N/S
N/S
SFP-DUAL-SM10 
(no longer purchasable)
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-BX-D 
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-DUAL-BX-U 
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-100-BX20LT
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-BX20NU
(no longer purchasable)
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
SFP-100-BXLC-D 
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-100-BXLC-U 
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-100-LC-MM 
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-100-LC-SM15 
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-100-LC-SM40 
(no longer purchasable)
N/S
N/S
N/S
8.4.1.R01
N/S
N/S
N/S
N/S
N/S
SFP-10G-SR
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-LR
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1

<<<PAGE 106>>>
OmniSwitch 9900 Compatibility
Transceiver Compatibility Matrix
page 2-96
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
SFP-10G-ER
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-LRM
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-ZR
N/S
N/S
8.3.13
N/S
N/S
N/S
8.5R43
8.6R1
8.6R1
SFP-10G-T5
N/S
N/S
8.3.1.R02 
or 8.9R3
N/S
N/S
N/S
8.5R4 or 
8.9R3
8.6R1 or 
8.9R3
8.6R1 or 
8.9R3
SFP-10G-C
- SFP-10G-C1M
- SFP-10G-C3M
- SFP-10G-C7M
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-
24DWD80
(no longer purchasable)
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-GIG-SR
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-GIG-LR
N/S
N/S
8.3.1
N/S
N/S
N/S
8.5R4
8.6R1
8.6R1
SFP-10G-BX-D2
N/S
N/S
8.6R1
N/S
N/S
N/S
8.6R1
8.6R1
8.6R1
SFP-10G-BX-U2
N/S
N/S
8.6R1
N/S
N/S
N/S
8.6R1
8.6R1
8.6R1
SFP-10G-BX-D402
N/S
N/S
8.9R1
N/S
N/S
N/S
8.9R1
8.9R1
8.9R1
SFP-10G-BX-U402
N/S
N/S
8.9R1
N/S
N/S
N/S
8.9R1
8.9R1
8.9R1
SFP-10G-CWDM
N/S
N/S
8.6R1
N/S
N/S
N/S
8.6R1
8.6R1
8.6R1
QSFP-40G-SR
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-40G-SR-BD2
(no longer purchasable)
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-40G-LR
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-40G-ER
8.6R1
8.9R3
N/S
N/S
8.6R1
8.9R3
N/S
8.6R1
8.6R1
QSFP-40G-LM4
(no longer purchasable)
8.8R1
8.9R3
N/S
N/S
8.8R1
8.9R3
N/S
8.8R1
8.8R1
QSFP-40G-CLR
8.5R1
8.9R3
N/S
N/S
8.5R1
8.9R3
N/S
8.6R1
8.6R1
QSFP-40G-PSM4
8.9R1
8.9R3
N/S
N/S
8.9R1
8.9R3
N/S
8.9R1
8.9R1
QSFP-40G-C
- QSFP-40G-C40CM
- QSFP-40G-C1M
- QSFP-40G-C3M
- QSFP-40G-C7M
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-4X10G-SR
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-4X10G-C
- QSFP-4X10G-C1M
- QSFP-4X10G-C3M
- QSFP-4X10G-C5M
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-40G-AOC-
20M
8.3.1.R02
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
8.6R1
8.6R1
QSFP-100G-SR4
N/S
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
N/S
N/S
QSFP-100G-LR4
N/S
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
N/S
N/S
QSFP-100G-CLR4
N/S
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
N/S
N/S
QSFP-100G-ER4
N/S
8.9R3
N/S
N/S
8.8R1
8.9R3
N/S
N/S
N/S
QSFP-100G-A20M
N/S
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
N/S
N/S
QSFP-100G-
CWDM4
N/S
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
N/S
N/S
Transceiver
OS99-
CMM
OS99-
CMM2
OS99-
XNI-U48
OS99-
GNI-U48
OS99-
CNI-U8
OS99-
CNI-U20
OS99-
XNI-
U24
OS99-
XNI-
U12Q
OS99-
XNI-
UP24Q2

<<<PAGE 107>>>
Transceiver Compatibility Matrix
OmniSwitch 9900 Compatibility
OmniSwitch AOS Release 8 Transceivers Guide
December 2025
page 2-97
1. Supports 1G only. Refer to the transceiver specifications table for minimum AOS requirements.
2. Does not support VFL connections.
3. Minimum supported AOS version is 8.6R1 if the transceiver was purchased after May 2019.
4. Beginning in AOS release 8.7R1 an error message will be displayed when this transceiver is inserted. 
5. Refer to the transceiver specifications table for minimum AOS requirements.
QSFP-100G-C
- QSFP-100G-C40CM
- QSFP-100G-C1M
- QSFP-100G-C3M
- QSFP-100G-C5M
N/S
8.9R3
N/S
N/S
8.4.1.R03
8.9R3
N/S
N/S
N/S
QSFP-4X25G-C
N/S
8.9R3
N/S
N/S
N/S4
8.9R3
N/S
N/S
N/S
QSFP-100G-SR1.2
N/S
8.10R4
N/S
N/S
8.10R4
8.10R4
N/S
N/S
N/S
QSFP-100G-PSM4
N/S
8.10R4
N/S
N/S
8.10R4
8.10R4
N/S
N/S
N/S
3FE46541AA
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
3FE49327AA
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
N/S
Transceiver
OS99-
CMM
OS99-
CMM2
OS99-
XNI-U48
OS99-
GNI-U48
OS99-
CNI-U8
OS99-
CNI-U20
OS99-
XNI-
U24
OS99-
XNI-
U12Q
OS99-
XNI-
UP24Q2