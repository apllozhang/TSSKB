<<<PAGE 1>>>
Part No. 060390-10, Rev. W
December 2025
OmniSwitch 6860/6860E/
6860N
Hardware Users Guide
www.al-enterprise.com

<<<PAGE 2>>>
ii
December 2025
This user guide documents OmniSwitch 6860/6860E/6860N hardware, including chassis and associated 
components. The specifications described in this guide are subject to change without notice.
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trade-
marks-copyright. All other trademarks are the property of their respective owners. The information 
presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any 
responsibility for inaccuracies contained herein. © Copyright 2023 ALE International, ALE USA Inc. All 
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
OmniSwitch 6860 Hardware Users Guide
December 2025
iii
Contents
About This Guide .......................................................................................................... ix
Supported Platforms .......................................................................................................... ix
Who Should Read this Manual? ........................................................................................ix
When Should I Read this Manual? ....................................................................................ix
What is in this Manual? ...................................................................................................... x
What is Not in this Manual? ............................................................................................... x
How is the Information Organized? ................................................................................... x
Documentation Roadmap ..................................................................................................xi
Related Documentation ...................................................................................................xiii
Technical Support ........................................................................................................... xiv
Chapter 1
OmniSwitch 6860  ......................................................................................................1-1
OmniSwitch 6860 Availability Features .........................................................................1-3
Power Supply Redundancy ......................................................................................1-3
Hot-Swapping ...........................................................................................................1-3
Hardware Monitoring ...............................................................................................1-4
Chapter 2
Getting Started ...........................................................................................................2-1
Installing the Hardware ...................................................................................................2-1
Items Required .........................................................................................................2-1
Site Preparation ........................................................................................................2-1
Environmental Requirements ............................................................................2-1
Electrical Requirements .....................................................................................2-1
Electrical Surge Warning ..................................................................................2-2
Unpacking and Installing the Switch .......................................................................2-3
Items Included ...................................................................................................2-3
Weight Considerations ......................................................................................2-3
Airflow Considerations .....................................................................................2-4
Mounting the Switch .......................................................................................................2-4
Connections and Cabling ................................................................................................2-5
Network Cable Installation Warning .................................................................2-5
Serial Connection to the Console Port ...............................................................2-5
Serial Connection Default Settings ...................................................................2-5
Ethernet Management Port (EMP) Cable Requirements .........................................2-5
Booting the Switch ..........................................................................................................2-6
Component LEDs ..............................................................................................2-6
Your First Login Session ................................................................................................2-7

<<<PAGE 4>>>
Contents
iv
OmniSwitch 6860 Hardware Users Guide
December 2025
Logging In to the Switch ..........................................................................................2-7
Setting IP Address Information for the EMP ...........................................................2-8
Unlocking Session Types .........................................................................................2-9
Changing the Login Password ..................................................................................2-9
Setting the System Time Zone ...............................................................................2-10
Setting the Date and Time ......................................................................................2-10
Setting Optional Parameters ...................................................................................2-10
Specifying an Administrative Contact .............................................................2-10
Specifying a System Name ..............................................................................2-10
Specifying the Switch’s Location ....................................................................2-10
Viewing Your Changes ..........................................................................................2-11
Saving Your Changes .............................................................................................2-11
Chapter 3
Chassis and Power Supplies ....................................................................................3-1
OmniSwitch 6860 Chassis Details ..................................................................................3-2
OmniSwitch 6860-24 ...............................................................................................3-2
OS6860-24 Front Panel .....................................................................................3-2
OS6860-24 Rear Panel ......................................................................................3-2
OS6860-24 Chassis Specifications ....................................................................3-3
OmniSwitch 6860-48 ...............................................................................................3-4
OS6860-48 Front Panel .....................................................................................3-4
OS6860-48 Rear Panel ......................................................................................3-4
OS6860-48 Chassis Specifications ....................................................................3-5
OmniSwitch 6860-P24 .............................................................................................3-6
OS6860-P24 Front Panel ...................................................................................3-6
OS6860-P24 Rear Panel ....................................................................................3-6
OS6860-P24 Chassis Specifications ..................................................................3-7
OmniSwitch 6860-P48 .............................................................................................3-8
OS6860-P48 Front Panel ...................................................................................3-8
OS6860-P48 Rear Panel ....................................................................................3-8
OS6860-P48 Chassis Specifications ..................................................................3-9
OmniSwitch 6860E-24 ...........................................................................................3-10
OS6860E-24 Front Panel .................................................................................3-10
OS6860E-24 Rear Panel ..................................................................................3-10
OS6860E-24 Chassis Specifications ...............................................................3-11
OmniSwitch 6860E-48 ...........................................................................................3-12
OS6860E-48 Front Panel .................................................................................3-12
OS6860E-48 Rear Panel ..................................................................................3-12
OS6860E-48 Chassis Specifications ...............................................................3-13
OmniSwitch 6860E-U28 ........................................................................................3-14
OS6860E-U28 Front Panel ..............................................................................3-14
OS6860E-U28 Rear Panel ...............................................................................3-14
OS6860E-U28 Chassis Specifications ............................................................3-15
OmniSwitch 6860E-P24 .........................................................................................3-16
OS6860E-P24 Front Panel ..............................................................................3-16
OS6860E-P24 Rear Panel ................................................................................3-16
OS6860E-P24 Chassis Specifications .............................................................3-17
OmniSwitch 6860E-P48 .........................................................................................3-18
OS6860E-P48 Front Panel ..............................................................................3-18
OS6860E-P48 Rear Panel ................................................................................3-18
OS6860E-P48 Chassis Specifications .............................................................3-19

<<<PAGE 5>>>
Contents
OmniSwitch 6860 Hardware Users Guide
December 2025
v
OmniSwitch 6860E-P24Z8 ....................................................................................3-20
OS6860E-P24Z8 Front Panel ..........................................................................3-20
OS6860E-P24Z8 Rear Panel ...........................................................................3-20
OS6860E-P24Z8 Chassis Specifications .........................................................3-21
OmniSwitch 6860N-U28 ........................................................................................3-22
 OS6860N-U28 Front Panel ............................................................................3-22
 OS6860N-U28 Rear Panel .............................................................................3-22
 OS6860N-U28 Chassis Specifications ...........................................................3-23
OmniSwitch 6860N-P48Z ......................................................................................3-24
OS6860N-P48Z Front Panel ............................................................................3-24
OS6860N-P48Z Rear Panel .............................................................................3-24
OS6860N-P48Z Chassis Specifications ..........................................................3-25
OmniSwitch 6860N-P48M .....................................................................................3-26
OS6860N-P48M Front Panel ..........................................................................3-26
OS6860N-P48M Rear Panel ............................................................................3-26
OS6860N-P48M Chassis Specifications .........................................................3-27
OmniSwitch 6860N-P24Z ......................................................................................3-28
OS6860N-P24Z Front Panel ............................................................................3-28
OS6860N-P24Z Rear Panel .............................................................................3-28
OS6860N-P24Z Chassis Specifications ..........................................................3-29
OmniSwitch 6860N-P24M .....................................................................................3-30
OS6860N-P24M Front Panel ..........................................................................3-30
OS6860N-P24M Rear Panel ............................................................................3-30
OS6860N-P24M Chassis Specifications .........................................................3-31
OmniSwitch 6860N Uplink Modules .....................................................................3-32
OS68-XNI-U4 Front Panel ..............................................................................3-32
OS68-QNI-U2 Front Panel ..............................................................................3-32
OS68-VNI-U4 Front Panel ..............................................................................3-33
OS68-CNI-U1 Front Panel ..............................................................................3-33
Chassis Status LEDs ...............................................................................................3-34
Mounting the Switch .....................................................................................................3-36
General Mounting Recommendations ....................................................................3-36
Airflow Recommendations ....................................................................................3-37
Blank Cover Panels ................................................................................................3-38
Installing Blank Cover Panels .........................................................................3-38
Rack-Mounting .............................................................................................................3-39
Installing Rack Mount Flanges ..............................................................................3-39
Installing the Chassis In the Rack ..........................................................................3-41
Standalone (Non-Rack Mounted) Installations ......................................................3-42
Power Supplies ..............................................................................................................3-43
Dying Gasp .............................................................................................................3-44
Scenarios ..........................................................................................................3-44
SNMP Trap ......................................................................................................3-44
Syslog Message ...............................................................................................3-44
Link OAM PDU ..............................................................................................3-44
OS6860-BP 150W Power Supply ..........................................................................3-46
OS6860-BP LED States ..................................................................................3-46
OS6860-BP-D 150W DC Power Supply ...............................................................3-47
OS6860-BP-D LED States ..............................................................................3-47
OS6860-BP-PH 600W Power Supply ....................................................................3-48

<<<PAGE 6>>>
Contents
vi
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-BP-PH LED States ............................................................................3-48
OS6860N-BPPH 600W Power Supply ..................................................................3-49
LED States .......................................................................................................3-49
OS6860-BP-PX 920W Power Supply ....................................................................3-50
OS6860-BP-PX LED States ............................................................................3-50
OS6860N-BPPX 920W Power Supply ..................................................................3-51
LED States .......................................................................................................3-51
OS6860N-BPXL 2000W Power Supply ................................................................3-52
LED States .......................................................................................................3-52
DC Power Supply Connections ..............................................................................3-53
Connecting a DC Cable Harness to the Chassis Power Supply ......................3-53
Connecting a DC Cable Harness to the DC Power Source .............................3-53
Installing Power Supplies .......................................................................................3-54
Removing Power Supplies .....................................................................................3-56
Grounding the Chassis ..................................................................................................3-58
Installing / Removing Uplink Modules .........................................................................3-59
OS6860 FANTRAY NONPOE Fan Tray .....................................................................3-60
OS6860 FANTRAY NONPOE LED States ..........................................................3-60
Monitoring Chassis Components ..................................................................................3-61
Viewing Chassis Slot Information .........................................................................3-61
Monitoring Chassis Temperature ..................................................................................3-61
Temperature Errors ..........................................................................................3-62
Chapter 4
 Managing Power over Ethernet (PoE) .................................................................4-1
In This Chapter ................................................................................................................4-2
Power over Ethernet Specifications ................................................................................4-3
Viewing Power Supply Status ..................................................................................4-3
Viewing PoE Status ..................................................................................................4-4
Power over Ethernet Budget ...........................................................................................4-4
Power over Ethernet Defaults .........................................................................................4-5
Understanding and Modifying the Default Settings .................................................4-5
PoE Class Detection .................................................................................................4-5
PoE Operational Status .............................................................................................4-6
Configuring the Total Power Available to a Port ..............................................4-7
Configuring the Total Power Available to a slot ...............................................4-7
Setting Port Priority Levels ...............................................................................4-8
Setting the Capacitor Detection Method ...........................................................4-8
Setting Timers and Other User-Defined PoE Power Rules ...............................4-9
Understanding Priority Disconnect ...............................................................................4-10
Setting Priority Disconnect Status ..........................................................................4-10
Disabling Priority Disconnect .........................................................................4-10
Enabling Priority Disconnect ..........................................................................4-10
Priority Disconnect is Enabled; Same Priority Level on All PD .....................4-11
Priority Disconnect is Enabled; 
Incoming PD Port has Highest Priority Level .................................................4-11
Priority Disconnect is Enabled; 
Incoming PD Port has Lowest Priority Level ..................................................4-11

<<<PAGE 7>>>
Contents
OmniSwitch 6860 Hardware Users Guide
December 2025
vii
Priority Disconnect is Disabled .......................................................................4-12
Understanding Guard Band ...........................................................................................4-12
Monitoring Power over Ethernet via CLI .....................................................................4-13
Appendix A
Regulatory Compliance and Safety Information ..............................................A-1
Declaration of Conformity: CE Mark ............................................................................A-1
Waste Electrical and Electronic Equipment (WEEE) Statement ............................A-1
China RoHS: Hazardous Substance Table .......................................................A-2
Taiwan RoHS: Hazardous Substance Table .....................................................A-3
California Proposition 65 Warning ..................................................................A-3
Standards Compliance ....................................................................................................A-4
FCC Class A, Part 15 ..............................................................................................A-6
Canada Class A Statement ......................................................................................A-6
JATE ........................................................................................................................A-6
CISPR22 Class A warning ......................................................................................A-6
Korea Emissions Statement .....................................................................................A-7
VCCI .......................................................................................................................A-7
Class A Warning for Taiwan and Other Chinese Markets ......................................A-7
Class 1M Laser Warning .........................................................................................A-7
Network Cable Installation Warning .......................................................................A-7
Translated Safety Warnings ...........................................................................................A-8
Blank Panels Warning ......................................................................................A-8
Electrical Storm Warning .................................................................................A-8
Installation Warning .........................................................................................A-8
Invisible Laser Radiation Warning ...................................................................A-9
Operating Voltage Warning .............................................................................A-9
Power Disconnection Warning .........................................................................A-9
Proper Earthing Requirement Warning ..........................................................A-10
DC Power Supply Connection Warning ......................................................................A-10
Read Important Safety Information Warning .................................................A-11
Restricted Access Location Warning .............................................................A-11
Wrist Strap Warning .......................................................................................A-11
Instrucciones de seguridad en español .........................................................................A-12
Advertencia sobre el levantamiento del chasis ...............................................A-12
Advertencia de las tapaderas en blanco ..........................................................A-12
Advertencia en caso de tormenta eléctrica .....................................................A-12
Advertencia de instalación .............................................................................A-12
Advertencia de radiación láser invisible .........................................................A-12
Advertencia de la batería de litio ....................................................................A-12
Advertencia sobre la tensión de operación .....................................................A-12
Advertencia sobre la desconexión de la fuente ..............................................A-12
Advertencia sobre una apropiada conexión a tierra .......................................A-13
Leer “información importante de seguridad” .................................................A-13
Advertencia de acceso restringido ..................................................................A-13
Advertencia de pulsera antiestática ................................................................A-13
Clase de seguridad ..........................................................................................A-13
Advertencia de fuentes de poder ....................................................................A-13

<<<PAGE 8>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
ix
About This Guide
This OmniSwitch 6860 Hardware Users Guide describes OmniSwitch 6860 switch components and basic 
switch hardware procedures. 
Supported Platforms
The information in this guide applies only to OmniSwitch 6860 switches.
Who Should Read this Manual?
The audience for this users guide is network administrators and IT support personnel who need to 
configure, maintain, and monitor switches and routers in a live network. However, anyone wishing to gain 
knowledge of OmniSwitch 6860 hardware will benefit from the material in this guide.
When Should I Read this Manual?
Read this guide as soon as you are ready to familiarize yourself with your switch hardware components. 
You should already be familiar with the very basics of the switch hardware, such as module LEDs and 
component installation procedures. This manual will help you understand your switch hardware in 
greater depth.

<<<PAGE 9>>>
x
OmniSwitch 6860 Hardware Users Guide
December 2025
What is in this Manual?
This users guide includes the following hardware-related information:
• Descriptions of “Availability” features.
• Technical specifications for the chassis, power supplies and modules.
• Power supply requirements.
• The dynamics of chassis airflow, including detailed illustrations of proper and improper airflow 
configurations.
• Hot-swapping power supplies and modules.
• Installation and removal procedures for power supplies and modules.
• Detailed illustrations and LED descriptions for chassis, network and power supply operability.
• Hardware-related Command Line Interface (CLI) commands.
What is Not in this Manual?
The descriptive and procedural information in this manual focuses on switch hardware. It includes 
information on some CLI commands that pertain directly to hardware configuration, but it is not intended 
as a software users guide. There are several OmniSwitch users guides that focus on switch software 
configuration. Consult those guides for detailed information and examples for configuring your switch 
software to operate in a live network environment. See “Documentation Roadmap” on page -xi and 
“Related Documentation” on page -xiii for further information on software configuration guides available 
for your switch.
How is the Information Organized?
Each chapter in this guide focuses on a specific hardware component or a set of hardware components. All 
descriptive, technical specification, and procedural information for a hardware component can be found in 
the chapter dedicated to that component.

<<<PAGE 10>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
xi
Documentation Roadmap
The OmniSwitch user documentation suite was designed to supply you with information at several critical 
junctures of the configuration process.The following section outlines a roadmap of the manuals that will 
help you at each stage of the configuration process. Under each stage, we point you to the manual or 
manuals that will be most helpful to you.
Stage 1: Using the Switch for the First Time
Pertinent Documentation: OmniSwitch 6860 Getting Started Information
OmniSwitch AOS Release 8 Release Notes
A “Getting Started” chapter is included in the OmniSwitch 6860 Hardware Users Guide. This chapter 
provides all the information you need to get your switch up and running the first time. It also includes 
succinct overview information on fundamental aspects of the switch.
At this time you should also familiarize yourself with the Release Notes that accompanied your switch. 
This document includes important information on feature limitations that are not included in other 
user guides.
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: OmniSwitch 6860 Hardware Users Guide
OmniSwitch AOS Release 8 Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the OmniSwitch 6860 Hardware 
Guide. This guide provide specifications, illustrations, and descriptions of all hardware components. It also 
includes steps for common procedures, such as removing and installing switch components.
This guide is the primary users guide for the basic software features on a single switch. This guide 
contains information on the switch directory structure, basic file and directory utilities, switch access 
security, SNMP, and web-based management. It is recommended that you read this guide before 
connecting your switch to the network.
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: OmniSwitch AOS Release 8 Network Configuration Guide
OmniSwitch AOS Release 8 Advanced Routing Configuration Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The Network Configuration Guide guide contains overview information, procedures, and 
examples on how standard networking technologies are configured on the OmniSwitch.
The Advanced Routing Guide includes configuration information for networks using advanced routing 
technologies (OSPF and BGP) and multicast routing protocols (DVMRP and PIM-SM).

<<<PAGE 11>>>
xii
OmniSwitch 6860 Hardware Users Guide
December 2025
Anytime
The OmniSwitch CLI Reference Guide contains comprehensive information on all CLI commands 
supported by the switch. This guide includes syntax, default, usage, example, related CLI command, and 
CLI-to-MIB variable mapping information for all CLI commands supported by the switch. This guide can 
be consulted anytime during the configuration process to find detailed and specific information on each 
CLI command.

<<<PAGE 12>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
xiii
Related Documentation
The following are the titles and descriptions of all the OmniSwitch 6860 user manuals:
• OmniSwitch 6860 Hardware Users Guide
Complete technical specifications and procedures for all OmniSwitch 6860 chassis, power supplies, 
fans, and Network Interface (NI) modules.
• OmniSwitch CLI Reference Guide
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
security options (authenticated VLANs), Quality of Service (QoS), link aggregation, and server 
load balancing.
• OmniSwitch AOS Release 8 Advanced Routing Configuration Guide
Includes network configuration procedures and descriptive information on all the software features and 
protocols included in the advanced routing software package. Chapters cover multicast routing 
(DVMRP and PIM-SM), Open Shortest Path First (OSPF), and Border Gateway Protocol (BGP).
• OmniSwitch Transceivers Guide
Includes SFP and XFP transceiver specifications and product compatibility information.
• Technical Tips, Field Notices
Includes information published by Alcatel-Lucent’s Customer Support group.
• Release Notes
Includes critical Open Problem Reports, feature exceptions, and other important information on the 
features supported in the current release and any limitations to their support.

<<<PAGE 13>>>
xiv
OmniSwitch 6860 Hardware Users Guide
December 2025
Technical Support
An Alcatel-Lucent service agreement brings your company the assurance of 7x24 no-excuses technical 
support. You’ll also receive regular software updates to maintain and maximize your Alcatel-Lucent 
product’s features and functionality and on-site hardware replacement through our global network of 
highly qualified service delivery partners. 
With 24-hour access to Alcatel-Lucent’s Service and Support web page, you’ll be able to view and update 
any case (open or closed) that you have reported to Alcatel-Lucent’s technical support, open a new case or 
access helpful release notes, technical bulletins, and manuals. 
Access additional information on Alcatel-Lucent’s Service Programs:
Web: myportal.al-enterprise.com
Phone: 1-800-995-2696

<<<PAGE 14>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
page 1-1
1  OmniSwitch 6860
Refer to the information below for OmniSwitch 6860 (OS6860) models and components.
Model Number
Description
OS6860-24
Fixed-configuration chassis in a 1U form factor with 24 10/100/1000 Base-T 
ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis link ports.
OS6860-P24
Fixed-configuration chassis in a 1U form factor with 24 10/100/1000 Base-T 
PoE ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis 
link ports.
OS6860-48
Fixed-configuration chassis in a 1U form factor with 48 10/100/1000 Base-T 
ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis link ports.
OS6860-P48
Fixed-configuration chassis in a 1U form factor with 48 10/100/1000 Base-T 
PoE ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis 
link ports.
OS6860E-24
Fixed-configuration chassis in a 1U form factor with 24 10/100/1000 Base-T 
ports, four fixed SFP+ (1G/10G) ports and two 20G virtual Chassis link ports. 
Includes a built-in co-processor for Enhanced network services.
OS6860E-P24
Fixed-configuration chassis in a 1U form factor with 24 10/100/1000 Base-T 
PoE ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis link 
ports. Includes a built-in co-processor for Enhanced network services. 
OS6860E-48
Fixed-configuration chassis in a 1U form factor with 48 10/100/1000 Base-T 
ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis link ports. 
Includes a built-in co-processor for Enhanced network services.
OS6860E-P48
Fixed-configuration chassis in a 1U form factor with 48 10/100/1000 Base-T 
PoE ports, four fixed SFP+ (1G/10G) ports and two 20G Virtual Chassis link 
ports. Includes a built-in co-processor for Enhanced network services
OS6860E-U28
Fixed-configuration chassis in a 1U form factor with 28 ports supporting 
1000Base-X and 100Base-FX, four fixed SFP+ (1G/10G) ports and two 20G 
Virtual Chassis link ports. Includes a built-in co-processor for Enhanced 
network services.
OS6860E-P24Z8
Fixed-configuration chassis in a 1U form factor with 8 100/1000/2.5G BaseT 
HPoE ports and 16 10/100/1000 Base-T PoE ports, four fixed SFP+ (10G) ports 
and two 20G QSFP Virtual Chassis link ports. Includes a built-in co-processor 
for Enhanced network services. 
OS6860N-U28
Fixed-configuration chassis in a 1U form factor with 24 SFP ports, 4 SFP+ 
ports, 2 QSFP28 VFL ports, and 4 SFP28 ports. 
OS6860N-P48Z
Fixed-configuration chassis in a 1U form factor with 36 10/100/1000 Base-T 
PoE ports, 12 Multigig (2.5G) PoE ports, 2 QSFP28 VFL ports, and 4 SFP28 
ports.

<<<PAGE 15>>>
OmniSwitch 6860
page 1-2
OmniSwitch 6860 Hardware Users Guide
December 2025
Additional Chassis Components and Connectors
The OS6860 chassis provides two bays for 1+1 redundant hot-swappable power supplies. (Non-PoE 
models allow the installation of a single optional fan tray in place of one 150W power supply.)
All models include one console connector (for use with Micro USB-to-USB cable, included); one USB 
connector (for use with Alcatel-Lucent flash drive or Bluetooth dongle, not included); and one RS-232 
connector. 
Enhanced models provide one Ethernet Management Port (EMP) located on the rear panel for out-of-band 
management.
For detailed information on the chassis, including front and rear panel connectors and components, refer to 
Chapter 3, “Chassis and Power Supplies.”
For information on console, USB and Bluetooth connections and cable requirements, refer to the Switch 
Management Guide.
OS6860N-P48M
Modular chassis in a 1U form factor with 36 Multigig (2.5G) PoE ports, 12 Mul-
tigig (10G) PoE ports, 2 QSFP28 VFL, 1 slot for uplink modules.
OS6860N-P24Z
Fixed-configuration chassis in a 1U form factor with 12 10/100/1000 Base-T
PoE ports, 12 Multigig (2.5G) PoE ports, 2 QSFP28 VFL ports, and 4 SFP28
ports.
OS6860N-P24M
Modular chassis in a 1U form factor with 24 Multigig PoE ports, 2 QSFP28
VFL, 1 slot for uplink modules.
Model Number
Description

<<<PAGE 16>>>
OmniSwitch 6860
OmniSwitch 6860 Availability Features
OmniSwitch 6860 Hardware Users Guide
December 2025
page 1-3
OmniSwitch 6860 Availability Features
The switch provides a broad variety of availability features. Availability features are hardware and 
software-based safeguards that help prevent the loss of data flow in the unlikely event of a subsystem 
failure. In addition, some availability features allow users to maintain or replace hardware components 
without powering off the switch or interrupting switch operations. Combined, these features provide added 
resiliency and help ensure that the switch is consistently available for day-to-day network operations.
Hardware-related availability features include:
• Power Supply Redundancy
• Hot-Swapping
• Hardware Monitoring
Power Supply Redundancy
For information on power supply redundancy, refer to Chapter 3, “Chassis and Power Supplies.”
Hot-Swapping
Hot-swapping refers to the action of adding, removing, or replacing certain hardware components without 
powering off your switch and disrupting other components in the chassis. This feature greatly facilitates 
hardware upgrades and maintenance and also allows you to easily replace components in the unlikely 
event of hardware failure. The following hardware components can be hot-swapped:
• Power supplies
• Transceivers
• Plug-in modules
Note. For information on adding and removing power supplies and plug-in modules, refer to Chapter 3, 
“Chassis and Power Supplies.” Additionally, refer to the release notes for any known issues and addi-
tional guidelines regarding hot-swapping.
Hardware Monitoring
Automatic Monitoring
Automatic monitoring refers to the switch’s built-in sensors that automatically monitor operations. If an 
error is detected (e.g., over-threshold temperature), the switch immediately sends a trap to the user. The 
trap is displayed on the console in the form of a text error message.
LEDs
LEDs, which provide visual status information, are provided on the front and rear panels. LEDs are used 
to indicate conditions, such as hardware and software status, link integrity, data flow, etc. For detailed 
LED descriptions, refer to the corresponding hardware component section in the next chapter.

<<<PAGE 17>>>
OmniSwitch 6860 Availability Features
OmniSwitch 6860
page 1-4
OmniSwitch 6860 Hardware Users Guide
December 2025
User-Driven Monitoring
User-driven hardware monitoring refers to CLI commands that are entered by the user in order to access 
the current status of hardware components. The user enters “show” commands that output information to 
the console. The show commands for all the features are described in detail in the OmniSwitch CLI 
Reference Guide.

<<<PAGE 18>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
page 2-1
2  Getting Started
Installing the Hardware
Note. For information on configuring a Virtual Chassis (VC), refer to the OmniSwitch AOS Release 8 
Switch Management Guide.
Items Required
• Grounding wrist strap
• Phillips screwdriver
• Flat-blade screwdriver
Site Preparation
Environmental Requirements
OmniSwitch 6860 switches have the following environmental and airflow requirements:
• The installation site must maintain a temperature between 0° and 45° Celsius (32° and 113° Fahrenheit) 
and not exceed 95 percent maximum humidity (non-condensing) at any time.
• Be sure to allow adequate room for proper air ventilation at the front, back, and sides of the switch. 
Refer to “Airflow Considerations” on page 2-4 for minimum clearance requirements. No clearance is 
necessary at the top or bottom of the chassis.
Electrical Requirements
Note. Alcatel-Lucent switches must be installed by a professional installer. It is the responsibility of the 
installer to ensure that proper grounding is available and that the installation meets applicable local and 
national electrical codes.
OmniSwitch 6860 switches have the following general electrical requirements:
• Each switch requires one grounded electrical outlet for each power supply installed in the chassis. 
OmniSwitch 6860 switches offer both AC and DC power supply support. Refer to the OmniSwitch 
6860 Hardware Users Guide for more information.
• For switches using AC power connections, each supplied AC power cord is 2 meters (approx. 6.5 feet). 
Do not use extension cords.
•

<<<PAGE 19>>>
Installing the Hardware
Getting Started
page 2-2
OmniSwitch 6860 Hardware Users Guide
December 2025
• ALE provided power cords are UL recognized to IEC 62368-1 exceeding the maximum amperage 
requirement for the power source. If using a non-ALE provided power cord the installer shall confirm it 
meets the minimum electrical requirements of the power source.
Redundant AC Power. It is recommended that each AC outlet resides on a separate circuit. With 
redundant AC, if a single circuit fails, the switch’s remaining power supplies (on separate circuits) can 
remain operational.
• For switches using DC power, refer to the “DC Power Supply Connections” on page 3-52 for
more information.
Electrical Surge Warning
In order to help protect equipment against electrical surges please take note of the following 
recommendations and guidelines:
1 Earth grounding of all devices is fundamental to ensure long term reliability.
• All electrical equipment must be installed by a qualified, licensed electrician.
• Every power supply that is connected to building power should be earth grounded.
• Earth grounding for the power cable, should be verified to be 0.01 ohm or less.
• Each switch should be grounded to same earth ground as the power supply.
• Each powered device, such as an AP or camera, should be connected to earth ground.
• Each surge suppression device should be connected to earth ground.
2 Shielded cables (STP) offer some minimal level of additional protection over unshielded Ethernet 
cables (UTP) but the use of a surge protector is still recommended.
• It is suggested to use STP Cat5e or better for 1Gbps Ethernet switches for any outdoor application or 
applications where Ethernet cables come in close proximity to alternating current conductors.
• Always install cables according to manufacturer requirements.
3 For any connections where integrity of the cabling within a building ground is questionable (i.e outdoor 
connections), copper Ethernet ports must be connected with an appropriate surge protection device, inline, 
between the PSE and PD per the manufacturer’s recommendations for connection and grounding.
4 Caution should be taken for any cable connected to any outdoor device, not only on the device ground-
ing, but to ensure that any outdoor device cables that could carry surge currents, do not pass those surge 
currents to upstream Ethernet switches.
5 Caution - Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity 
due to the dielectric properties of their construction materials in addition, this build up of electricity could 
lead to a Cable Discharge Event (CDE). A CDE can occur due to the differential in charges on the cable 
and the equipment it’s being connected to. It is recommended that installers momentarily ground all 
copper Ethernet cables (especially in new cable runs) to a suitable and safe earth ground before connect-
ing them to the port.

<<<PAGE 20>>>
Getting Started
Installing the Hardware
OmniSwitch 6860 Hardware Users Guide
December 2025
page 2-3
Note. Failure to follow the above recommendations could result in voiding the warranty of the affected 
ALE product. 
Unpacking and Installing the Switch
To protect your switch components from damage, read all unpacking recommendations and instructions 
carefully before beginning.
Unpack your OmniSwitch 6860 chassis as close as possible to the location where it will be installed.
Items Included
Your OmniSwitch 6860 includes the following items:
• OmniSwitch chassis with power supplies, per order
• Transceivers, per order
• Blank cover panel
• Rack mount brackets
• Micro USB-to-USB cable
• Country-specific power cord(s)
• Rubber table-mounting feet
• Attachment screws
• Assorted instructional cards, anti-static bags and additional packaging
Weight Considerations
Depending on the model, when fully populated with power supplies and mounting brackets an OmniSwitch 
6860 can weigh up to approximately 8.16 kg (18 lb).

<<<PAGE 21>>>
Mounting the Switch
Getting Started
page 2-4
OmniSwitch 6860 Hardware Users Guide
December 2025
Airflow Considerations
To ensure proper airflow, be sure that the switch is placed in a clean, well-ventilated area free of dust and 
debris and provide minimum recommended clearance at the front, back and sides of the switch. Never obstruct 
chassis air vents.
Chassis Top View
Note. Clearance is not required at the top and bottom of the chassis.
Mounting the Switch
For information on mounting OmniSwitch 6860 switches, refer to the Chapter 3, “Chassis and Power 
Supplies.”
Connections and Cabling
Once your switch is properly installed, you should connect all network and management cables required for 
your network applications. Connections may include:
• Micro USB-to-USB cable to the console connector
• Ethernet cable to the Ethernet Management Port (EMP) (‘E’ and ‘N’ models only)
• Cables to NIs or transceivers
}
}
Rear. 6 inches minimum 
at rear of chassis.
Front. 6 inches minimum 
at front of chassis.
Sides. 2 inches minimum 
at left and right sides.

<<<PAGE 22>>>
Getting Started
Booting the Switch
OmniSwitch 6860 Hardware Users Guide
December 2025
page 2-5
Note. For additional information on cabling for console, EMP, USB, Bluetooth and other connections, 
refer to the OmniSwitch AOS Release 8 Switch Management Guide. 
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
Serial Connection to the Console Port
The console port provides a serial connection to the switch using a USB connector and is required when 
logging into the switch for the first time. By default, this connector provides a DCE console connection.
Serial Connection Default Settings
For information on modifying these settings, refer to the OmniSwitch AOS Release 8 Switch 
Management Guide.
Ethernet Management Port (EMP) Cable Requirements
Enhanced OS6860 models (OS6860E) provide an Ethernet Management Port (EMP) on the rear panel of the 
chassis for out-of-band management. There are specific cable type requirements (i.e., straight-through or 
crossover) based on the device to which the EMP is connecting. Refer to the information below:
For information on manually configuring Ethernet ports, refer to the OmniSwitch AOS Release 8 Network 
Configuration Guide. 
Booting the Switch
Now that you have installed the switch components and connected network and management cables, you can 
boot the switch. To boot the switch, plug all power supply cords into easily-accessible, properly grounded 
power outlets. (Do not use extension cords.) The switch will power on and boot automatically.
Note. If you have more than one power supply installed, be sure to plug in each power supply in rapid 
succession, (i.e., within a few seconds of each other). This ensures that there will be adequate power for 
all components throughout the boot process.
baud rate
9600
115200 (6860N models)
parity
none
data bits (word size)
8
stop bits
1
EMP to a Switch
Straight-through
EMP to a Computer or 
Workstation 
Crossover

<<<PAGE 23>>>
Your First Login Session
Getting Started
page 2-6
OmniSwitch 6860 Hardware Users Guide
December 2025
Component LEDs
During the boot process, component LEDs will flash and change color, indicating different stages of the boot. 
Following a successful boot, chassis LEDs should display as follows:
If the LEDs do not display as indicated, make sure the boot process is complete. If the LEDs do not display as 
indicated following a complete boot sequence, contact Alcatel-Lucent Customer Support. For complete 
information on LED states, refer to “Chassis Status LEDs” on page 3-32.
Once the switch has completely booted and you have accessed your computer’s terminal emulation software 
via the console port, you are ready to log in to the switch’s Command Line Interface (CLI) and configure basic 
information. Continue to “Your First Login Session” on page 2-6.
Your First Login Session
In order to complete the setup process for the switch, you must complete the following steps during your first 
login session:
• Log in to the switch
• Set IP address information for the Ethernet Management Port (EMP) (Enhanced models only)
• Unlock session types
• Change the login password
• Set the date and time
• Set optional system information
• Save your changes
Important. You must be connected to the switch via the console port before initiating your first login 
session.
Logging In to the Switch
When you first log in to the switch, you will be prompted for a login name and password. Use the switch’s 
default settings:
• Login: admin
OK1
Solid Green
PRI
Solid Green (for switches running in 
master role)
Solid Amber (for switches running in 
slave role)
PS
Solid Green
BPS
Solid Green
GRN (Power Save)
Solid Green
OK2 (Enhanced models only)
Solid Green

<<<PAGE 24>>>
Getting Started
Your First Login Session
OmniSwitch 6860 Hardware Users Guide
December 2025
page 2-7
• Password: switch
The default welcome banner, which includes information such as the current software version and system date, 
is displayed followed by the CLI command prompt:
Welcome to the Alcatel-Lucent OS6860E-P48 8.1.1, April 15, 2014.
Copyright (c) 1994-2014 Alcatel-Lucent. All Rights Reserved.
OmniSwitch(tm) is a trademark of Alcatel-Lucent, registered in the United States 
Patent and Trademark Office.
->
Note. A user account includes a login name, password, and user privileges. Privileges determine whether 
the user has read or write access to the switch and which commands the user is authorized to execute. For 
detailed information on setting up and modifying user accounts, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.
Setting IP Address Information for the EMP
If installing an Enhanced OS6860 model (OS6860E), the IP address may be set via the Ethernet Management 
Port (EMP). To connect to the switch through the EMP Ethernet connection, use the default address below or 
change the port’s IP address.
Note. You should be connected to the switch via the console port before attempting to change IP 
address information. 
To change the default IP and mask, use the ip interface command. For example:
-> ip interface emp address 168.22.2.120 mask 255.255.255.0
Verify your settings using the show ip interface command. See the OmniSwitch AOS Release 8 Switch 
Management Guide for additional information regarding EMP port addressing. 
Note. Although you have configured the EMP with valid IP address information, you will not be able to 
access the switch through this port (i.e. TELNET, FTP, HTTP, SSH or SNMP) until you have unlocked 
these remote session types. See “Unlocking Session Types” on page 2-7 for more information.
Unlocking Session Types
Security is a key feature on OmniSwitch 6860 switches. As described on page 2-6, when you access the switch 
for the first time, you must use a direct console port connection. All other session types (Telnet, FTP, 
WebView, and SNMP) are locked out until they are manually unlocked by the user.
Default EMP IP Address
192.168.1.1
Default EMP Mask
255.255.255.0

<<<PAGE 25>>>
Your First Login Session
Getting Started
page 2-8
OmniSwitch 6860 Hardware Users Guide
December 2025
The CLI command used to unlock session types is aaa authentication. 
Note. When you unlock session types, you are granting switch access to non-local sessions (e.g., Telnet). 
As a result, users who know the correct user login and password will have remote access to the switch. For 
more information on switch security, refer to the OmniSwitch AOS Release 8 Switch Management Guide.
Unlocking All Session Types
To unlock all session types, enter the following command syntax at the CLI prompt:
-> aaa authentication default local
Unlocking Specified Session Types
You can also unlock session types on a one-by-one basis. For example, to unlock Telnet sessions only, enter 
the following command:
-> aaa authentication telnet local
To unlock WebView (HTTP) sessions only, enter the following command:
-> aaa authentication http local
You cannot specify more than one session type in a single command line. However, you can still unlock 
multiple session types by using the aaa authentication command in succession. For example:
-> aaa authentication http local
-> aaa authentication telnet local
-> aaa authentication ftp local
Refer to the OmniSwitch CLI Reference Guide for complete aaa authentication command syntax options.
Changing the Login Password
Change the login password for admin user sessions by following the steps below:
1 Be sure that you have logged into the switch as user type admin (see “Logging In to the Switch” on 
page 2-6). 
2 Enter the keyword password and press Enter.
3 Enter your new password at the prompt.
Note. Be sure to remember or securely record all new passwords; overriding configured passwords on an 
OmniSwitch is restricted.
4 You will be prompted to re-enter the password. Enter the password a second time.
New password settings are automatically saved in real time to the local user database; the user is not required 
to enter an additional command in order to save the password information. Also note that new password 
information is retained following a reboot. All subsequent login sessions, including those through the console 
port, will require the new password to access the switch.
For detailed information on managing login information, including user names and passwords, refer to the 
OmniSwitch AOS Release 8 Switch Management Guide.

<<<PAGE 26>>>
Getting Started
Your First Login Session
OmniSwitch 6860 Hardware Users Guide
December 2025
page 2-9
Setting the System Time Zone
The switch’s default time zone is UTC. If you require a time zone that is specific to your region, or if you need 
to enable Daylight Savings Time (DST) on the switch, you can configure these settings via the system 
timezone and system daylight-savings-time commands.
For detailed information on configuring a time zone for the switch, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.
Setting the Date and Time
Set the current time for the switch by entering system time, followed by the current time in hh:mm:ss. 
To set the current date for the switch, enter system date, followed by the current date in mm/dd/yyyy.
Setting Optional Parameters
Specifying an Administrative Contact
An administrative contact is the person or department in charge of the switch. If a contact is specified, users 
can easily find the appropriate network administrator if they have questions or comments about the switch.
To specify an administrative contact, use the system contact command.
Specifying a System Name
The system name is a simple, user-defined text description for the switch. To specify a system name, use the 
system name command.
Specifying the Switch’s Location
It is recommended that you use a physical labeling system for locating and identifying your switch(es). 
Examples include placing a sticker or placard with a unique identifier (e.g., the switch’s default IP address) on 
each chassis.
However, if no labeling system has been implemented or if you need to determine a switch’s location from a 
remote site, entering a system location can be very useful.
To specify a system location, use the system location command.
Viewing Your Changes
To view your current changes, enter show system at the CLI prompt.
Saving Your Changes
Once you have configured this basic switch information, save your changes by entering write memory at the 
CLI command prompt.

<<<PAGE 27>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-1
3  Chassis and Power Supplies
This chapter includes detailed information on the OmniSwitch 6860 switch. Topics include:
• Chassis details and technical specifications:
Basic Models - Non-PoE
OS6860-24, page 3-3.
OS6860-48, page 3-5.
Basic Models - PoE
OS6860-P24, page 3-7.
OS6860-P48, page 3-9.
Enhanced Models - Non-PoE
OS6860E-24, page 3-11.
OS6860E-48, page 3-13.
OS6860E-U28, page 3-15.
Enhanced Models - PoE
OS6860E-P24, page 3-17.
OS6860E-P48, page 3-19.
OS6860E-P24Z8, page 3-20.
Next-Generation (N) Models
 OS6860N-U28, page 3-22.
OS6860N-P48Z, page 3-24.
OS6860N-P48M, page 3-25.
OS6860N-P24Z, page 3-27.
OS6860N-P24M, page 3-29.
OS6860N Uplink Modules, page 3-27.
• Switch mounting information, page 3-35.
• Power supplies and power supply redundancy, page 3-45.
• Fan tray (non-PoE models only), page 3-59.

<<<PAGE 28>>>
Chassis and Power Supplies
page 3-2
OmniSwitch 6860 Hardware Users Guide
December 2025
• Temperature management, page 3-60.
• Monitoring the chassis components via the Command Line Interface (CLI), page 3-60

<<<PAGE 29>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-3
OmniSwitch 6860 Chassis Details
OmniSwitch 6860-24
OS6860-24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860-24 Rear Panel
 
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(24) 10/100/1000 Base-T ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
C
Power Supply/Fan Tray Bays 
OS6860-24
USB
VFL/30
VFL/29
USB
RS232
OK
PRI
PS
BPS GRN
OS6860-24
USB
VFL/30
VFL/29
USB
RS232
OK
PS
BPS GRN
VC
G
H
D
F
E
A B
C
PS 1
PS 2
BPS
A
B
C

<<<PAGE 30>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-4
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-24 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860-24 Chassis Weight
4.45 kg (9.8 lb)
OS6860-24 Chassis Weight (fully populated)1
5.17 kg (11.4 lb)
OS6860-24 Power Consumption (full system power)
46 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 31>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-5
OmniSwitch 6860-48
OS6860-48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860-48 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(48) 10/100/1000 Base-T ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
C
Power Supply/Fan Tray Bays 
OS6860-48
USB
VFL/54
VFL/53
USB
RS232
OK
PRI
PS
BPS GRN
OS6860-48
USB
VFL/54
VFL/53
USB
RS232
OK
VC
PS
BPS GRN
G
H
D
F
E
A B
C
PS 1
PS 2
BPS
A
B
C

<<<PAGE 32>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-6
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-48 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860-48 Chassis Weight
4.67 kg (10.3 lb)
OS6860-48 Chassis Weight (fully populated)1
5.40 kg (11.9 lb)
OS6860-48 Power Consumption (full system power)
57 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 33>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-7
OmniSwitch 6860-P24
OS6860-P24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860-P24 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(24) 10/100/1000 Base-T 802.3at PoE ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Fan Vent
C
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
D
PoE Power Supply Bays 
OS6860-P24
USB
VFL/30
VFL/29
USB
RS232
OK
PRI
PS
BPS GRN
OS6860-P24
USB
VFL/30
VFL/29
USB
RS232
OK
PS
BPS GRN
VC
G
H
D
F
E
A B
C
A
C
D
B

<<<PAGE 34>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-8
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-P24 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
2 Does not include attached PoE devices.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860-P24 Chassis Weight
4.58 kg (10.1 lb)
OS6860-P24 Chassis Weight (fully populated)1
6.03 kg (13.3 lb)
OS6860-P24 Power Consumption (full system power)2
75 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 35>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-9
OmniSwitch 6860-P48
OS6860-P48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860-P48 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(48) 10/100/1000 Base-T 802.3at PoE ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Fan Vent
C
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
D
PoE Power Supply Bays 
OS6860-P48
USB
VFL/54
VFL/53
USB
RS232
OK
PRI
PS
BPS GRN
OS6860-P48
USB
VFL/54
VFL/53
USB
RS232
OK
VC
PS
BPS GRN
G
H
D
F
E
A B
C
A
C
D
B

<<<PAGE 36>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-10
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-P48 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
2 Does not include attached PoE devices. 
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860-P48 Chassis Weight
4.90 kg (10.8 lb)
OS6860-P48 Chassis Weight (fully populated)1
6.35 kg (14.0 lb)
OS6860-P48 Power Consumption (full system power)2
89 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 37>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-11
OmniSwitch 6860E-24
OS6860E-24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860E-24 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(24) 10/100/1000 Base-T ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Ethernet Management Port (EMP) for Out-of-Band Management
C
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
D
Power Supply/Fan Tray Bays
OS6860E-24
USB
VFL/30
VFL/29
PRI
PS
BPS
OK2
GRN
OK1
USB
RS232
G
H
D
F
E
A B
C
EMP
PS 1
PS 2
BPS
A
B
C
D

<<<PAGE 38>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-12
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860E-24 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860E-24 Chassis Weight
4.58 kg (10.1 lb)
OS6860E-24 Chassis Weight (fully populated)1
5.26 kg (11.6 lb)
OS6860E-24 Power Consumption (full system power)
48 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 39>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-13
OmniSwitch 6860E-48
OS6860E-48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860E-48 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(48) 10/100/1000 Base-T ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Ethernet Management Port (EMP) for Out-of-Band Management
C
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
D
Power Supply/Fan Tray Bays
OS6860E-48
VFL/54
VFL/53
USB
RS232
PRI
PS
BPS
OK2
GRN
OK1
G
H
D
F
E
A B
C
EMP
PS 1
PS 2
BPS
A
B
C
D

<<<PAGE 40>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-14
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860E-48 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860E-48 Chassis Weight
4.81 kg (10.6 lb)
OS6860E-48 Chassis Weight (fully populated)1
5.49 kg (12.1 lb)
OS6860E-48 Power Consumption (full system power)
60 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 41>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-15
OmniSwitch 6860E-U28
OS6860E-U28 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860E-U28 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(28) 1000Base-X/100Base-FX ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Ethernet Management Port (EMP) for Out-of-Band Management
C
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
D
Power Supply/Fan Tray Bays
G
H
D
F
E
A B
C
EMP
PS 1
PS 2
BPS
A
B
C
D

<<<PAGE 42>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-16
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860E-U28 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860E-U28 Chassis Weight
4.58 kg (10.1 lb)
OS6860E-U28 Chassis Weight (fully populated)1
5.26 kg (11.6 lb)
OS6860E-U28 Power Consumption (full system power)
73 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 43>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-17
OmniSwitch 6860E-P24
OS6860E-P24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860E-P24 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(4) 10/100/1000 Base-T HPoE (60W - not 802.3bt compliant) ports
(20) 10/100/1000 Base-T 802.3at PoE ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Ethernet Management Port (EMP) for Out-of-Band Management
C
Fan Vent
D
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
E
Power Supply Bays
OS6860E-P24
USB
VFL/30
VFL/29
PRI
PS
BPS
OK2
GRN
OK1
USB
RS232
G
H
D
F
E
A B
C
A
B
D
E
C

<<<PAGE 44>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-18
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860E-P24 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
2 Does not include attached PoE devices.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860E-P24 Chassis Weight
4.81 kg (10.6 lb)
OS6860E-P24 Chassis Weight (fully populated)1
6.26 kg (13.8 lb)
OS6860E-P24 Power Consumption (full system power)2
76 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 45>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-19
OmniSwitch 6860E-P48
OS6860E-P48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860E-P48 Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(4) 10/100/1000 Base-T HPoE (60W - not 802.3bt compliant) ports
(44) 10/100/1000 Base-T 802.3at PoE ports
G
(4) fixed SFP+ (1G/10G) ports
H
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Ethernet Management Port (EMP) for Out-of-Band Management
C
Fan Vent
D
OmniSwitch Backup Power Supply (OS-BPS) (No longer supported.)
E
Power Supply Bays
OS6860E-P48
USB
VFL/54
VFL/53
USB
RS232
PRI
PS
BPS
OK2
GRN
OK1
G
H
D
F
E
A B
C
A
B
D
E
C

<<<PAGE 46>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-20
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860E-P48 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
2 Does not include attached PoE devices.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
OmniSwitch 6860E-P24Z8
OS6860E-P24Z8 Front Panel
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
OS6860E-P48 Chassis Weight
5.03 kg (11.1 lb)
OS6860E-P48 Chassis Weight (fully populated)1
6.49 kg (14.3 lb)
OS6860E-P48 Power Consumption (full system power)2
93 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
Console port
E
RS-232 port
F
(16) 10/100/1000 Base-T 802.3at PoE ports
G
(8) 100/1000/2.5G Base-T(75W HPoE Ports - not 802.3bt compliant)
A B
G
H
D
F
E
C
I

<<<PAGE 47>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-21
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860E-P24Z8 Rear Panel
OS6860E-P24Z8 Chassis Specifications
1 Fully populated weights include installed power supplies. These figures do not include transceivers.
2 Does not include attached PoE devices.
H
(4) fixed SFP+ (1G/10G) ports
I
(2) 20G Virtual Chassis link ports
Item
Description
A
Chassis Grounding Lug
B
Ethernet Management Port (EMP) for Out-of-Band Management
C
Fan Vent
D
Power Supply Bays
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
Chassis Weight
4.81 kg (10.6 lb)
Chassis Weight (fully populated)1
6.26 kg (13.8 lb)
Power Consumption (full system power)2
48W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Item
Description
A
B
D
C

<<<PAGE 48>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-22
OmniSwitch 6860 Hardware Users Guide
December 2025
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
OmniSwitch 6860N-U28
 OS6860N-U28 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
EMP port
E
Console port
F
(24) SFP (100M/1G) - Ports 1-24
G
(4) SFP+ (1G/10G) - Ports 25-28
H
(2) QSFP28 (VFL) - Ports 29-30
I
(4) SFP28 (1G/10G/25G) - Ports 31-34
Note: The OS6860N-U28 doesn’t support a mix of 1G/10G and 25G speeds on the 4-port group of 
ports 31-34. Ports within the port group must all run at either 1G/10G speed or 25G speed. Mix-
ing 1G and 10G speeds is supported. 
A
B
G
H
D
F
E
C
I

<<<PAGE 49>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-23
 OS6860N-U28 Rear Panel
 OS6860N-U28 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Item
Description
A
Chassis Grounding Lug
B
Fan Vent
C
Power Supply Bays
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.33 in)
Chassis Depth 
35 cm (13.78 in)
Chassis Weight
5.60 kg (12.36 lb)
Power Consumption (full system power)
143W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
A
B
C

<<<PAGE 50>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-24
OmniSwitch 6860 Hardware Users Guide
December 2025
OmniSwitch 6860N-P48Z
OS6860N-P48Z Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860N-P48Z Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
EMP port
E
Console port
F
(36) 10/100/1000 Base-T 802.3bt PoE (60W) - Ports 1-36
G
(12) 100M/1G/2.5G/5G Base-T 802.3bt PoE (95W) - Ports 37-48
H
(2) QSFP28 (VFL) - Ports 49-50
I
(4) SFP28 (1G/10G/25G) - Ports 51-54
Note: The OS6860N-P48Z doesn’t support a mix of 1G/10G and 25G speeds on the 4-port group of 
ports 51-54. Ports within the port group must all run at either 1G/10G speed or 25G speed. Mix-
ing 1G and 10G speeds is supported. 
Item
Description
A
Chassis Grounding Lug
B
Fan Vent
C
Power Supply Bays
A
B
G
H
D
F
E
C
I
A
B
C

<<<PAGE 51>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-25
OS6860N-P48Z Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
OmniSwitch 6860N-P48M
OS6860N-P48M Front Panel
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.32 in)
Chassis Depth 
44 cm (17.32 in)
Chassis Weight
7.80 kg (17.2 lb)
Power Consumption (full system power)
147W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Item
Description
A
Status LEDs
B
(36) 100M/1G/2.5G Base-T 802.3bt PoE (95W) - Ports 1-36
C
(12) 100M/1G/2.5G/5G/10G Base-T 802.3bt PoE (95W) - Ports 37-48
D
(2) QSFP28 (VFL) - Ports 49-50
E
Uplink Module (Slot 2)
A
B
D
C
E

<<<PAGE 52>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-26
OmniSwitch 6860 Hardware Users Guide
December 2025
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860N-P48M Rear Panel
OS6860N-P48M Chassis Specifications
Item
Description
A
Chassis Grounding Lug
B
EMP Port
C
USB Port
D
Console Port
E
Virtual Chassis ID LED
F
Fan Vent
G
Power Supply Bays
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.32 in)
Chassis Depth 
44 cm (17.32 in)
Chassis Weight
8.50 kg (18.76 lb)
Power Consumption (full system power)
260W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
A B
C
G
D
F
E

<<<PAGE 53>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-27
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
OmniSwitch 6860N-P24Z
OS6860N-P24Z Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
EMP port
E
Console port
F
(12) 10/100/1000 Base-T 802.3bt PoE (60W) ports
G
(12) 100M/1G/2.5G/5G Base-T 802.3bt PoE (95W) ports
H
(2) QSFP28 VFL ports
I
(4) SFP28 (1G/10G/25G) ports
Note: The OS6860N-P24Z doesn’t support a mix of 1G/10G and 25G speeds on the 4-port group of 
ports 27-30. Ports within the port group must all run at either 1G/10G speed or 25G speed. Mix-
ing 1G and 10G speeds is supported. 
A
B
G
H
D
F
E
C
I

<<<PAGE 54>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-28
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860N-P24Z Rear Panel
OS6860N-P24Z Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Item
Description
A
Chassis Grounding Lug
B
Fan Vent
C
Power Supply Bays
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.32 in)
Chassis Depth 
44 cm (17.32 in)
Chassis Weight
7.76 kg (17.11 lb)
Power Consumption (full system power)
142 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
A
B
C

<<<PAGE 55>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-29
OmniSwitch 6860N-P24M
OS6860N-P24M Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6860N-P24M Rear Panel
Item
Description
A
Virtual Chassis ID LED
B
Status LEDs
C
USB port 
D
EMP port
E
Console port
F
(24) 100M/1G/2.5G/5G/10G Base-T 802.3bt PoE (95W) ports
G
(2) QSFP28 VFL ports
H
Uplink Module (Slot 2)
Item
Description
A
Chassis Grounding Lug
B
Fan Vent
C
Power Supply Bays
A
B
D
C
E
G
H
F
A
B
C

<<<PAGE 56>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-30
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860N-P24M Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
OmniSwitch 6860N Uplink Modules
OS68-XNI-U4 Front Panel
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.32 in)
Chassis Depth 
44 cm (17.32 in)
Chassis Weight
8.38 kg (18.47 lb)
Power Consumption (full system power)
176 W
Altitude
13,000 ft
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Item
Description
A
Status LEDs
B
(4) SFP+ (1G/10G) ports
A
B

<<<PAGE 57>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-31
OS68-QNI-U2 Front Panel
OS68-VNI-U4 Front Panel
Item
Description
A
Status LEDs
B
(2) QSFP+ (40G) ports
Item
Description
A
Status LEDs
B
(4) SFP28 (1G/10G/25G) ports
Note: The OS68-VNI-U4 doesn’t support a mix of 1G/10G and 25G speeds. Ports must all run at 
either 1G/10G speed or 25G speed. Mixing 1G and 10G speeds is supported.
A
B
A
B

<<<PAGE 58>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-32
OmniSwitch 6860 Hardware Users Guide
December 2025
OS68-CNI-U1 Front Panel
Chassis Status LEDs
The chassis provides a series of status LEDs located on the front panel. These LEDs offer basic status 
information for hardware operation and port link and activity status.
Item
Description
A
Status LEDs
B
(1) QSFP28 (40G/100G) ports
LED
State
Description
OK1
Solid Green
Blinking Green
Solid Amber
System Diagnostics and AOS bootup OK
System Diagnostics and AOS in progress
(i.e., performing diagnostics or booting)
System Diagnostics and/or AOS bootup failed
VC
Solid Green
Solid Amber
Off
This unit is the master unit
This unit is a slave unit
This unit is in shutdown mode or is not part of 
a VC.
A
B

<<<PAGE 59>>>
Chassis and Power Supplies
OmniSwitch 6860 Chassis Details
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-33
PS
Solid Green
Solid Green
Solid Amber
Solid Amber
Off
Two power supplies are installed in the chassis 
and both supplies are functioning normally.
One power supplies is installed in the chassis 
and functioning normally (with the second 
power supply bay empty or occupied by a 
fan tray).
Two power supplies are installed in the chassis 
and one or both supplies has experienced 
a failure.
One power supply is installed in the chassis 
and has experienced a failure (with the second 
power supply bay empty or occupied by a 
fan tray).
No power supply is present. 
BPS
Solid Green
Solid Amber
Off
Backup power supply is operating normally
Backup power supply is operating, but a fault 
is present
No backup power supply is present
GRN
Solid Green
Off
Power save features are active
Power save features are off
OK2 (Enhanced
models only)
Solid Green
Blinking Green
Solid Amber
External CPU Diagnostics and AOS 
bootup OK
External CPU Diagnostics in progress
External CPU Diagnostic and/or AOS 
bootup failed
LED
State
Description

<<<PAGE 60>>>
OmniSwitch 6860 Chassis Details
Chassis and Power Supplies
page 3-34
OmniSwitch 6860 Hardware Users Guide
December 2025
Port LEDs
Port LEDs (6860N)
Solid Green
Blinking Green
Solid Amber
Blinking Amber
Solid Blue
Blinking Blue
Solid Blue+Yellow
Blinking Blue+Yellow
Solid Green (LED1)
Blinking Green (LED1)
Solid Blue (LED1)
Blinking Blue (LED1)
Solid Magenta (LED1)
Blinking Magenta (LED1)
Solid Amber (LED1)
Blinking Amber (LED1)
Solid Amber (LED2)
VFL/Uplink Ports Amber
VFL/Uplink Ports Green
Valid port link (non-PoE)
Valid port link with activity (non-PoE)
Valid port link (PoE)
Valid port link with activity (PoE)
2.5G valid port link (non-PoE)
2.5G valid port link with activity (non-PoE)
2.5G valid port link (PoE)
2.5G valid port link with activity (PoE)
Valid port link
Valid port link with activity
2.5G valid port link
2.5G valid port link with activity
5G valid port link
5G valid port link with activity
10G valid port link
10G valid port link with activity
PoE Active
VFL
Uplink
Note: The blue LED may flash at a reduced frequency for the 2.5G ports.
LED
State
Description

<<<PAGE 61>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-35
Mounting the Switch
General Mounting Recommendations
Elevated Operating Ambient Temperature. If installed in a closed or multi-rack assembly, the 
operating ambient temperature of the rack environment may be greater than the room’s ambient 
temperature. Therefore, consideration should be given to the maximum rated ambient temperature (Tmra) 
listed in the “OmniSwitch 6860 Chassis Details” section.
Reduced Air Flow. Installation of the equipment in a rack should be such that the amount of air flow 
required for safe operation of the equipment is not compromised. Refer to “Airflow Recommendations” 
on page 3-35 for more information.
Mechanical Loading. Mounting of the equipment in the rack should be such that a hazardous condition is 
not achieved due to uneven loading.
Circuit Overloading. Consideration should be give to the connection of the equipment to the supply 
circuit and the effect that overloading of circuits could have on overcurrent protection and supply wiring. 
Reliable Earthing. Reliable earthing of rack-mounted equipment should be maintained. Particular 
attention should be given to supply connections other than direct connections to the branch (e.g., use of 
power strips).
Airflow Recommendations
To ensure proper airflow, be sure that your switch is placed in a well-ventilated area and provide 
minimum recommended clearance at the front, back and sides of the switch, as shown below. Restricted 
airflow can cause your switch to overheat, which can lead to switch failure. Refer to the following 
important guidelines regarding airflow:

<<<PAGE 62>>>
Mounting the Switch
Chassis and Power Supplies
page 3-36
OmniSwitch 6860 Hardware Users Guide
December 2025
Follow the guidelines below regarding the minimum clearance requirements when mounting
the chassis.
Chassis Top View
Note. Clearance is not required at the top and bottom of the chassis.
Blank Cover Panels
Blank cover panels are provided with your switch and are used to cover empty slots. These cover panels 
play an important role in chassis airflow and temperature management. If your switch is not fully 
populated and blank cover panels are not installed over empty slot locations, airflow is adversely affected. 
When blank cover panels are missing, air does not take the direct route from the air intake vents. As a 
result, normal airflow is disrupted and an extra task is placed on the power supply fans to cool the chassis.
Cover panels also provide protection for module processor boards and other sensitive internal switch 
components by closing off a chassis that is not fully populated.
Note. Because they regulate airflow and help protect internal chassis components, blank cover panels 
should be installed over empty module slots and power supply bays at all times.
}
}
Rear. 6 inches minimum 
at rear of chassis.
Front. 6 inches minimum 
at front of chassis.
Sides. 2 inches minimum 
at left and right sides.

<<<PAGE 63>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-37
Installing Blank Cover Panels
1 When installing blank cover panels over power supply slots, orient the cover panels with the arrows
pointing up.
2 Insert the blank cover panel in the empty chassis slot and secure using attachment screws (provided).
Face arrow up
when installing.

<<<PAGE 64>>>
Rack-Mounting
Chassis and Power Supplies
page 3-38
OmniSwitch 6860 Hardware Users Guide
December 2025
Rack-Mounting
Refer to the following important guidelines before installing the chassis in a rack:
• Two people are required to rack mount the switch: One person to lift the chassis into position and one 
person to secure the chassis to the rack using the rack mount screws.
• The chassis has rack-mount flanges that support standard 19-inch rack mount installations.
• Alcatel-Lucent Enterprise does not provide rack-mount screws. Use the screws supplied by the 
rack vendor.
• To prevent a rack from becoming top heavy, it is recommended that you install the switch at the bottom 
of the rack whenever possible.
Note. If you are installing the switch in a relay rack, be sure to install and secure the rack per rack manu-
facturer’s specifications.
Installing Rack Mount Flanges
1 To install rack mount flanges, start by making sure the spring clip is in the out (disengaged) position.
2 Insert the tab into the chassis slot as shown.
Slot
Tab
Clip in “Out” 
(disengaged) 
position

<<<PAGE 65>>>
Chassis and Power Supplies
Rack-Mounting
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-39
3 Press the flange and spring clip until the flange clicks into place and the clip is in the in 
(engaged) position.
4 Secure the flange to the chassis using the attachment screw (provided).
5 Repeat steps 1 through 4 for the flange on the opposite side of the chassis.
6 Attach rear bracket guide and rear bracket (OS6860N-P48Z/P48M models).
Clip in “In” 
(engaged) 
position
“CLICK”
Rear bracket guide
Rear bracket
Rack Mounted Bracket Length
26.4 in.

<<<PAGE 66>>>
Rack-Mounting
Chassis and Power Supplies
page 3-40
OmniSwitch 6860 Hardware Users Guide
December 2025
Installing the Chassis In the Rack
1 Mark the holes on the rack where the chassis is to be installed.
2 One person should lift and position the chassis until the rack-mount flanges are flush with the
rack post.
3 Align the holes in the flanges with the rack holes marked in step 1.
4 Once the holes are aligned, the second person should insert a screw through the bottom hole on each 
flange. Tighten both screws until they are secure.
5 Install the remaining screws in the top hole of each flange. Be sure that all screws are 
securely tightened.

<<<PAGE 67>>>
Chassis and Power Supplies
Rack-Mounting
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-41
6 Slide rear bracket into rear bracket guide and secure rear bracket to rack.
OS6860N-P48Z/P48M Rear Mounting 
Attach Side Rails
Mount Front Brackets
Slide Rear Brackets into Side Rails and Mount

<<<PAGE 68>>>
Rack-Mounting
Chassis and Power Supplies
page 3-42
OmniSwitch 6860 Hardware Users Guide
December 2025
Standalone (Non-Rack Mounted) Installations
The chassis can also be placed unmounted on a stable, flat surface as a standalone unit. Be sure that the 
surface can accommodate the full, populated weight of all switches being installed. (Approximate chassis 
weights are provided in the technical specifications tables in the “OmniSwitch 6860 Chassis Details” 
section.) 
Be sure that adequate clearance has been provided for chassis airflow and that you have placed the chassis 
within reach of all required AC outlets. For recommended airflow allowances, refer to page 3-35.
To prepare the chassis for tabletop installations, follow the steps below:
1 Insert the four (4) rubber feet (provided separately in the switch packaging) into the holes in the bottom 
panel of the chassis. 
2 Place the switch on the tabletop “right side up.”
Note. Never attempt to operate a switch while it is placed on its top or side.
3 Connect network and management cables as needed.

<<<PAGE 69>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-43
Power Supplies
OmniSwitch 6860 switches use the following power supply types:
OmniSwitch 6860 power supplies are located at the rear of the switch chassis. Refer to “OmniSwitch 6860 
Chassis Details” for more information on component locations. 
Note: The OS6860 does not provide an on/off switch. Connecting an installed power supply to a power 
source will boot the switch. Likewise, disconnecting all installed power supplies from a power source will 
power off the switch.
Note: The table above lists the power supply models and which chassis they are currently supported on. 
Inserting an unsupported power supply will result in the switching and PoE ports being disabled until the 
correct power supply is inserted. OS6860N power supplies are supported beginning with AOS release 
8.7R1.
Dying Gasp
If the switch loses all power it will maintain power long enough to send a Dying Gasp message before 
completely shutting down. An SNMP trap, Syslog message and Link OAM PDUs will be generated.
Scenarios
A Dying Gasp event will be generated in the following scenarios:
• Primary power supply failure (if only power supply present)
• Primary power supply failure and then backup power supply failure
• Backup power supply failure and then primary power supply failure
Note. Connect each power supply to a separate independent power source to avoid simultaneous 
power failures.
Model
Chassis Supported
OS6860-BP 150W AC 
Non-PoE PSU
OS6860-24, OS6860E-24, OS6860-48, OS6860E-48, OS6860E-
U28,  OS6860N-U28
OS6860-BP-D 150W DC 
Non-PoE PSU
OS6860-24, OS6860E-24, OS6860-48, OS6860E-48, OS6860E-
U28,  OS6860N-U28
OS6860-BP-PH 600W AC 
PoE PSU
OS6860-P24, OS6860E-P24, OS6860E-P24Z8
OS6860-BP-PX 920W AC 
PoE PSU
OS6860-P48, OS6860E-P48, OS6860E-P24Z8
OS6860N-BPPH 600W AC PoE 
PSU
OS6860N-P48Z, OS6860N-P48M, OS6860N-P24Z, 
OS6860N-P24M
OS6860N-BPPX 920W AC PoE 
PSU
OS6860N-P48Z, OS6860N-P48M, OS6860N-P24Z, 
OS6860N-P24M
OS6860N-BPXL 2000W AC 
PoE PSU
OS6860N-P48M, OS6860N-P24M

<<<PAGE 70>>>
Power Supplies
Chassis and Power Supplies
page 3-44
OmniSwitch 6860 Hardware Users Guide
December 2025
SNMP Trap
As soon as the power failure is detected, an SNMP trap is sent to the first three configured SNMP stations. 
The trap includes the following information:
• Slot number
• Power supply type (primary/backup)
• Time of the failure
Use the snmp station command and refer to the SNMP Configuration chapter for information on 
configuring an SNMP station.
Syslog Message
As soon as the power failure is detected, the following Syslog message is sent to the first three configured 
Syslog servers, along with the time of the failure:
Dying Gasp Power Failure Event Occurred
Use the swlog output socket command to add a Syslog station. Refer to the Using Switch Logging 
Configuration chapter in the Network Configuration Guide for information on configuring a Syslog server.
Link OAM PDU
As soon as the power failure is detected four 802.3ah OAM Information PDUs are sent to ports for which 
link OAM is enabled and the LinkOAM port status is operational. The PDU will have the Dying Gasp bit 
set.
Use the efm-oam and efm-oam port propagate-events commands to enable the generation of an 802.3ah 
OAM Information PDU upon a dying gasp event:
-> efm-oam admin-state enable
-> efm-oam port 1/1/23-34 admin-state enable
-> efm-oam port 1/1/23-24 propagate-events dying-gasp enable
Link OAM PDU Priority
It may not be possible to generate PDUs on all ports enabled for link OAM. Dying gasp packets will be 
sent in the following order based on port priority:
1. Uplink ports
2. All other ports
Note. The maximum number ports which can send out a dying gasp PDU simultaneously is limited to ten 
ports minus the number of Syslog/SNMP servers configured. For example, if two SNMP servers and one 
Syslog server are configured, the maximum number of ports which can send out a dying gasp PDU is 
seven.

<<<PAGE 71>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-45
OS6860-BP 150W Power Supply
OS6860-BP 150W AC Power Supply Front Panel
Model
OS6860-BP (PS-150W-AC)
Models Supported
OS6860-24, OS6860E-24, OS6860-48, OS6860E-48,  
OS6860N-U28
Input Voltage/Current
90V to 136VAC/3A
180V to 264VAC/1.5A
Input Frequency
47Hz to 63Hz
Max. Output Power/Current
150W/12.5A
Note
Mixing the OS6860-BP-D with the OS6860-BP in the same 
chassis is supported.
LED
Handle
Status LED
Air Vent
Lock Tab
AC Connector

<<<PAGE 72>>>
Power Supplies
Chassis and Power Supplies
page 3-46
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-BP LED States
OS6860-BP-D 150W DC Power Supply
OS6860-BP-D 150W DC Power Supply Front Panel
LED State
Description
Solid Green
The power supply is operating normally and providing power 
Flashing Green
The power supply is on standby and can provide power to the chassis if
power supply failover should occur
Flashing Red
No AC power is being provided to this power supply (but another power 
supply is installed and operating in the adjacent power supply bay)
Flashing Green/Red
Power supply warning
Solid Red
Power supply failure
Off
No AC power is being provided to any power supply installed in the 
chassis; all power supplies are effectively off
Model
OS6860-BP-D (PS-150W-DC)
Models Supported
OS6860-24, OS6860E-24, OS6860-48, OS6860E-48,  
OS6860N-U28
Input Voltage/Current
-36V to -72VDC/1.8A to 6A
Max. Output Power/Current
150W/12.5A
Note
Mixing the OS6860-BP-D with the OS6860-BP in the same 
chassis is supported.
LED
Handle
Status LED
Air Vent
Lock Tab
DC Connector

<<<PAGE 73>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-47
OS6860-BP-D LED States
OS6860-BP-PH 600W Power Supply
OS6860-BP-PH 600W AC Power Supply Front Panel
LED State
Description
Solid Green
The power supply is operating normally and providing power 
Flashing Green
The power supply is on standby and can provide power to the chassis if
power supply failover should occur
Flashing Red
No AC power is being provided to this power supply (but another power 
supply is installed and operating in the adjacent power supply bay)
Flashing Green/Red
Power supply warning
Solid Red
Power supply failure
Off
No power is being provided to any power supply installed in the chassis; 
all power supplies are effectively off
Model
OS6860-BP-PH (PS-600W-AC-P)
Models Supported
OS6860-P24, OS6860E-P24, OS6860E-P24Z8
Input Voltage/Current
90V to 136VAC/8.5A
180 to 264VAC/4.25A
Input Frequency
47Hz to 63Hz
Max. Output Power/Current
600W/11A
Note
Mixing different wattage power supplies in a chassis is not sup-
ported. 
Redundant power supplies, which must be the same model, pro-
vide electrical load sharing and increase the amount of PoE 
power available. Use the show lanpower command to deter-
mine PoE power available. 
AC Connector
Air Vent
Lock Tab
Status LEDs

<<<PAGE 74>>>
Power Supplies
Chassis and Power Supplies
page 3-48
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-BP-PH LED States
OS6860N-BPPH 600W Power Supply
OS6860N-BPPH 600W AC Power Supply Front Panel
LED State
Description
AC OK LED Solid Green
AC power is good
AC OK LED Solid Red
There is an AC power issue
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue
Model
OS6860N-BPPH (YPEB0600AM)
Models Supported
OS6860N-P48Z, OS6860N-P48M, OS6860N-P24M, 
OS6860N-P24Z 
Input Voltage/Current
90V to 132VAC/8.0A
180V to 264VAC/4.0A
Input Frequency
47Hz to 63Hz
Max. Output Power/Current
600W/11A
Note
Mixing different wattage power supplies in a chassis is not sup-
ported. 
Redundant power supplies, which must be the same model, pro-
vide electrical load sharing and increase the amount of PoE 
power available. Use the show lanpower command to deter-
mine PoE power available. 
AC Connector
Air Vent
Lock Tab
Status LEDs

<<<PAGE 75>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-49
LED States
OS6860-BP-PX 920W Power Supply
OS6860-BP-PX 920W AC Power Supply Front Panel
LED State
Description
AC OK LED Solid Green
AC power is good
AC OK LED Solid Red
There is an AC power issue
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue
Model
OS6860-BP-PX (PS-920W-AC-P)
Models Supported
OS6860-P48, OS6860E-P48, OS6860E-P24Z8
Input Voltage/Current
90V to 136VAC/13A
180V to 264VAC/6.5A
Input Frequency
47Hz to 63Hz
Max. Output Power/Current
920W/16.88A
Note
Mixing different wattage power supplies in a chassis is not sup-
ported. 
Redundant power supplies, which must be the same model, pro-
vide electrical load sharing and increase the amount of PoE 
power available. Use the show lanpower command to deter-
mine PoE power available. 
AC Connector
Air Vent
Lock Tab
Status LEDs

<<<PAGE 76>>>
Power Supplies
Chassis and Power Supplies
page 3-50
OmniSwitch 6860 Hardware Users Guide
December 2025
OS6860-BP-PX LED States
OS6860N-BPPX 920W Power Supply
OS6860N-BPPX 920W AC Power Supply Front Panel
LED State
Description
AC OK LED Solid Green
AC power is good
AC OK LED Solid Red
There is an AC power issue
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue
Model
OS6860N-BPPX (YPEB0920AM)
Models Supported
OS6860N-P48Z, OS6860N-P48M, OS6860N-P24M, 
OS6860N-P24Z
Input Voltage/Current
90V to 132VAC /12.0A
180V to 264VAC/6.0A
Input Frequency
47Hz to 63Hz
Max. Output Power/Current
920W/16.88A
Note
Mixing different wattage power supplies in a chassis is not sup-
ported. 
Redundant power supplies, which must be the same model, pro-
vide electrical load sharing and increase the amount of PoE 
power available. Use the show lanpower command to deter-
mine PoE power available. 
AC Connector
Air Vent
Lock Tab
Status LEDs

<<<PAGE 77>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-51
LED States
OS6860N-BPXL 2000W Power Supply
OS6860N-BPXL 2000W AC Power Supply Front Panel
LED State
Description
AC OK LED Solid Green
AC power is good
AC OK LED Solid Red
There is an AC power issue
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue
Model
OS6860N-BPXL (YPEE2000CM-1A01P10)
Models Supported
OS6860N-P48M, OS6860N-P24M
Input Voltage/Current
100V to 120VAC/13.0A
200V to 240VAC/13.0A
Input Frequency
47Hz to 63Hz
Max. Output Power/Current
1000W/18.35A (100-120VAC input)
2000W/36.7A (200-240VAC input)
Note
Mixing different wattage power supplies in a chassis is not sup-
ported. 
Redundant power supplies, which must be the same model, pro-
vide electrical load sharing and increase the amount of PoE 
power available. Use the show lanpower command to deter-
mine PoE power available. 
AC Connector
(C19 Power Cord)
Air Vent
Lock Tab
Status LEDs

<<<PAGE 78>>>
Power Supplies
Chassis and Power Supplies
page 3-52
OmniSwitch 6860 Hardware Users Guide
December 2025
LED States
DC Power Supply Connections
Connecting a DC Cable Harness to the Chassis Power Supply
When plugging in the cable, insert the connector end of the cable harness into the power supply connector 
until it clicks firmly into place. This is an indication that the connector is secure and properly seated.
Connecting a DC Cable Harness to the DC Power Source
Safety Guidelines
Before connecting the DC cable to a power source, be sure to follow these important guidelines:
• Connect to a reliably ground -48VDC Selv source.
• The branch circuit overcurrent protection must be rated 15A.
• Use 12AWG copper conductors.
• A readily accessible disconnect device that is suitably approved and rated shall be incorporated in the 
field wiring.
• It must be installed in a restricted access location.
Primary Ground Information
The product has been designed to be installed in a Common Bonding Network (CBN). The pin of the 
Green/Yellow ground lead in the three pin cable connector is connected to the ground connector on the DC 
power supply, which is identified by a Grounding symbol. The Green/Yellow lead wire at the other end of 
the cable must be connected to a proper earth ground point. 
The rear chassis has two ground holes. To properly ground the equipment, connect a Panduit Corporation 
UL listed Lug, (Part number LCD8-10A-L) to the two threaded holes located at the rear, insert two 10-32, 
3/8” threaded pan head screws into these ground holes, and connect them to a proper earth ground point, 
using protective earthing conductor wire and 8AWG copper conductors. Torque to between 30-60 inch 
pounds.
Connection Details
For DC power supply units, make the following power connections:
Connect the power supply using the supplied DC cable. The cable consists of three 12AWG wires (Green/
Yellow, Black, Red). 
LED State
Description
AC OK LED Solid Green
AC power is good
AC OK LED Solid Red
There is an AC power issue
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue

<<<PAGE 79>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-53
One end of the cable has a three pin connector in a plastic housing that is inserted into a three pin input 
connector on the power supply. The other end of the cable is connected to a fuse panel or other source of 
-48VDC power.
Observe proper polarity when connecting to a fuse panel. The cable wire leads must be connected as 
follows:
• Green/yellow - ground
• Black - return
• Red - -48VDC
Note. The battery return conductor is an Isolated DC Return (DC-1).
Installing Power Supplies
Note. The power supply shown in the following diagrams is a OS6860-BP-PH/OS6860-BP-PX unit. 
However, comparable installation and removal steps also apply to OS6860-BP and OS6860-BP-D power 
supply units, as well as the OS6860 FANTRAY NONPOE Fan Tray (see page 3-59).
1 Insert the power supply into a power supply bay at the rear of the chassis and slide it back until it is 
securely seated in the chassis backplane.

<<<PAGE 80>>>
Power Supplies
Chassis and Power Supplies
page 3-54
OmniSwitch 6860 Hardware Users Guide
December 2025
When the connector is fully seated, the lock tab will click and hold the power supply in place.
2 Plug the power cord (provided) into the power supply’s socket.
Note. The chassis does not provide an on/off switch. Connecting a the power supplies to a power source 
will boot the switch.
Lock Tab

<<<PAGE 81>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-55
Removing Power Supplies
1 When removing a power supply, first disconnect the power cord from the power source. Once the 
power cord is disconnected, pull the power cord out of the power supply housing. 
2 Pressing the lock tab toward the center of the power supply, as shown, will free the power supply from 
the chassis.
Lock Tab

<<<PAGE 82>>>
Power Supplies
Chassis and Power Supplies
page 3-56
OmniSwitch 6860 Hardware Users Guide
December 2025
3  While pressing the lock tab, pull the power supply straight back and out of the chassis slot.
Note. If you are not replacing the power supply, be sure to install a blank cover panel over the empty 
power supply bay.

<<<PAGE 83>>>
Chassis and Power Supplies
Grounding the Chassis
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-57
Grounding the Chassis
The switch has a grounding lug located on the rear of the chassis. This lug uses 10-32 screws and is 
surrounded by a small paint-free area, which provides metal-to-metal contact for a ground connection.
Use this connector to supplement the ground provided by the AC power cord. To do so, install a Panduit 
Grounding Lug (type LCD8-10A-L) using 8AWG copper conductors to the paint-free area. Torque to 
between 30-60 inch pounds
Refer to the rear chassis views on page 3-3 for location details.

<<<PAGE 84>>>
Installing / Removing Uplink Modules
Chassis and Power Supplies
page 3-58
OmniSwitch 6860 Hardware Users Guide
December 2025
Installing / Removing Uplink Modules
Installing
1 Insert the module into the slot and slide it back until it is securely seated in the chassis. 
2 Secure with the captive screws.
Removing
1 Loosen the captive screws.
2 Firmly grasp the module and pull straight out to remove. 
Installing an Uplink Module

<<<PAGE 85>>>
Chassis and Power Supplies
OS6860 FANTRAY NONPOE Fan Tray
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-59
OS6860 FANTRAY NONPOE Fan Tray
The OS6860 FANTRAY NONPOE provides supplemental system cooling for non-PoE OS6860 switches 
connected to the OmniSwitch Backup Power Shelf/System (BPS).
Note. For information on installing or removing the OS6860 FANTRAY NONPOE unit, follow the steps 
outlined for power supplies beginning on page 3-53. 
OS6860 FANTRAY NONPOE Front Panel
OS6860 FANTRAY NONPOE LED States
Model
OS6860 FANTRAY NONPOE
Models Supported
OS6860-24, OS6860E-24, OS6860-48, OS6860E-48, 
OS6860E-U28
LED State
Description
Solid Green
Fan tray is receiving power and operating normally
Off
The fan tray is off or a failure has occurred
LED
Handle
Status LED
Air Vent
Lock Tab

<<<PAGE 86>>>
Monitoring Chassis Components
Chassis and Power Supplies
page 3-60
OmniSwitch 6860 Hardware Users Guide
December 2025
Monitoring Chassis Components
Viewing Chassis Slot Information
To view basic slot information, enter the show module command at the CLI prompt:
-> show module
To view more detailed information, use the show module long command:
-> show module long

<<<PAGE 87>>>
Chassis and Power Supplies
Monitoring Chassis Temperature
OmniSwitch 6860 Hardware Users Guide
December 2025
page 3-61
Monitoring Chassis Temperature
The operating temperature of your switch is a critical factor in its overall operability. In order to avoid a 
temperature-related system failure, your switch must always run at a temperature within the specified 
operating temperature range. 
To avoid chassis over-temperature conditions, follow the important chassis airflow recommendations on 
page 3-35.
To check the switch’s current temperature status, use the show temperature command. For example:
-> show temperature
Chassis/Device | Current |  Range  | Danger | Thresh |  Status
---------------+---------+---------+--------+--------+-----------------
 1/CMMA            54       15-93      93       96     UNDER THRESHOLD
 1/Slot1           54       15-93      93       101    UNDER THRESHOLD
 2/CMMA            39       15-85      85       88     UNDER THRESHOLD
 2/Slot1           39       15-85      85       101    UNDER THRESHOLD
For more information about this command, see the “Chassis Management and Monitoring Commands” 
chapter in the OmniSwitch CLI Reference Guide.
Temperature Errors
The switch monitors the chassis temperature at all times via an onboard sensor. If an over-temperature 
condition occurs, there are two different levels of error severity:
• Warning threshold has been exceeded
• Danger threshold has been exceeded
Warning Threshold
If the temperature exceeds the switch’s warning threshold, the switch sends out a trap. Traps are printed to 
the console in the form of text error messages.
When the warning threshold has been exceeded, switch operations remain active. However, it is 
recommended that immediate steps be taken to address the over-temperature condition.
Addressing warning threshold temperature conditions may include:
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature
Temperature Danger Threshold
If the chassis temperature rises above the danger threshold, the switch will power off until the temperature 
conditions have been addressed and the switch is manually booted. The danger threshold is factory-set and 
cannot be configured by the user.
Addressing danger threshold temperature conditions may include:

<<<PAGE 88>>>
Monitoring Chassis Temperature
Chassis and Power Supplies
page 3-62
OmniSwitch 6860 Hardware Users Guide
December 2025
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature

<<<PAGE 89>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-1
4   Managing Power over
Ethernet (PoE)
Power over Ethernet (PoE) provides inline power directly from the switch’s Ethernet ports. Powered 
Devices (PDs) such as IP phones, wireless LAN stations, Ethernet hubs, and other access points can be 
plugged directly into the Ethernet. From these RJ-45 the devices receive both electrical power and 
data flow.
As the feature reduces devices’ dependence on conventional power sources, PoE eliminates many restric-
tions that traditional electrical considerations have imposed on networks.
In a PoE configuration, Power Source Equipment (PSE) detects the presence of a PD and provides an elec-
trical current that is conducted along the data cable. The PD operates using the power received via the 
Ethernet data cable; no connection to an additional power source (e.g., an AC wall socket) is required.
Note on Terminology. There are several general terms used to describe the feature, PoE. The terms Power 
over Ethernet (PoE), Power over LAN (PoL), Power on LAN (PoL), and Inline Power are synonymous 
terms used to describe the powering of attached devices via Ethernet. For consistency, this chapter and the 
CLI Command Reference Guide refer to the feature as Power over Ethernet (PoE).
Additional terms, such as Powered Device (PD) and Power Source Equipment (PSE) are not synonymous 
with PoE, but are directly related to the feature:
• PD refers to any attached device that uses a PoE data cable as its only source of power. Examples 
include access points, IP telephones, Ethernet hubs, wireless LAN stations, etc. 
• PSE refers to power sourcing equipment, which provides power to a single link section. PSE main 
functions include searching the PD, optionally classifying the PD, supplying power to the link section 
only if the PD is detected, monitoring the power on the link section, and scaling power back to detect 
level when power is no longer requested or required.
As the switches fully support 10/100/1000 Ethernet connectivity, you may also attach non-PD equipment, 
such as computer workstations, printers, servers, etc. to the PoE ports. 
Important. Alcatel-Lucent recommends that PoE-enabled switches with attached IP telephones should 
have operational power supply redundancy at all times for 911 emergency requirements. In addition, both 
the switch and the power supply should be plugged into an Uninterruptible Power Source (UPS).

<<<PAGE 90>>>
In This Chapter
Managing Power over Ethernet (PoE)
page 4-2
OmniSwitch 6860 Hardware Users Guide
December 2025
In This Chapter
This chapter provides specifications and descriptions of hardware and software used to provide PoE for 
attached devices. 
The chapter also provides information on configuring PoE settings on the switch through the Command 
Line Interface (CLI). CLI commands are used in the configuration examples; for more details about the 
syntax of commands, see the OmniSwitch CLI Reference Guide. Topics and configuration procedures 
described in this chapter include:
• Power over Ethernet Specifications on page 4-3
• Viewing Power Status on page 4-3
• Configuring Power over Ethernet Parameters on page 4-3
• Understanding Priority Disconnect on page 4-11
• Monitoring Power over Ethernet via the CLI on page 4-15
Note. You can also monitor all chassis components and manage many chassis features, including Power 
over Ethernet, with WebView, Alcatel-Lucent’s embedded web-based device management application. 
WebView is an interactive and easy-to-use GUI that can be launched from the OmniVista or a web 
browser. Please refer to WebView’s Online Documentation for more information.

<<<PAGE 91>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Specifications
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-3
Power over Ethernet Specifications
The table below lists general specifications for Power over Ethernet support. For more detailed power 
supply and Power Source Equipment (PSE) specifications, refer to Chapter 3, “Chassis and Power 
Supplies.” 
Viewing Power Supply Status
To view the type and status for installed power supplies, use the show powersupply command:
-> show powersupply
             Total     PS
Chassis/PS   Power     Type     Status   Location
-----------+---------+--------+--------+-----------
 1/1         920       AC       UP       Internal
    Total   920
IEEE Standards supported
IEEE 802.3; 802.af; 802.3at, 802.3bt
PoE Class Detection
Supported
Platforms supporting PoE
OS6860-P24; OS6860-P48; OS6860E-P24; OS6860E-P48; 
OS6860E-P24Z8, OS6860N-P48Z,  OS6860N-P48M
Range of inline power per port
OS6860 models: 
- 3000-30000 milliwatts on all ports.
OS6860E (Enhanced) models: 
- 3000-60000 milliwatts on ports 1 through 4.
- 3000-30000 milliwatts on ports 5 and higher.
OS6860E-P248Z8: 
- 3000-30000 milliwatts on ports 1 through 16.
- 3000-75000 milliwatts on ports 17 through 24. 
OS6860N-P48Z: 
- 3000-60000 milliwatts on ports 1-36.
- 3000-95000 milliwatts on ports 37-48. 
OS6860N-P48M:
- 3000-95000 milliwatts on ports 1-48.
OS6860N-P24Z:
- 3000-60000 milliwatts on ports 1-12.
- 3000-95000 milliwatts on ports 13-24.
OS6860N-P24M:
- 3000-95000 milliwatts on ports 1-24.
Maximum PoE power per slot
Use the show lanpower command to determine PoE power avail-
able.

<<<PAGE 92>>>
Power over Ethernet Specifications
Managing Power over Ethernet (PoE)
page 4-4
OmniSwitch 6860 Hardware Users Guide
December 2025
Viewing PoE Status
To view current PoE status and settings, use the show lanpower slot command:
-> show lanpower slot 1/1
Port Maximum(mW) Actual Used(mW)   Status    Priority   On/Off   Class   Type
----+-----------+---------------+-----------+---------+--------+-------+----------
  1     60000            0       Powered Off    Low      OFF       .
  2     60000            0       Powered Off    Low      OFF       .
  3     60000            0       Powered Off    Low      OFF       .
  4     60000            0       Powered Off    Low      OFF       .
  5     30000            0       Powered Off    Low      OFF       .
  6     30000            0       Powered Off    Low      OFF       .
  7     30000            0       Powered Off    Low      OFF       .
  8     30000            0       Powered Off    Low      OFF       .
  9     30000            0       Powered Off    Low      OFF       .
 10     30000            0       Powered Off    Low      OFF       .
...
 45     30000            0       Powered Off    Low      OFF       .
 46     30000            0       Powered Off    Low      OFF       .
 47     30000            0       Powered Off    Low      OFF       .
 48     30000            0       Powered Off    Low      OFF       .
ChassisId 1 Slot 1 Max Watts 780
0 Watts Total Power Budget Used
780 Watts Total Power Budget Available
1 Power Supplies Available
BPS power: Not Available

<<<PAGE 93>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-5
Power over Ethernet Budget
The following table lists the Power over Ethernet wattages available based on the number and types of power 
supplies installed.
OmniSwitch
600W P/S
920W P/S
2000W P/S 
(115VAC)
2000W P/S 
(230VAC)
OS6860N-P48Z
(1) - 360W
(2) - 900W
(1) - 660W
(2) - 1500W
Not Supported
Not Supported
OS6860N-P48M
(1) - 300W
(2) - 845W
(1) - 590W
(2) - 1425W
(1) - 665W
(2) - 1570W
(1) - 1570W
(2) - 3390W
OS6860N-P24Z
(1) - 512W
(2) - 960W
(1) - 705W
(2) - 1545W
Not Supported
Not Supported
OS6860N-P24M
(1) - 385W
(2) - 935W
(1) - 680W
(2) - 1515W
(1) - 750W
(2) - 1600W
(1) - 1660W
(2) - 2280W

<<<PAGE 94>>>
Power over Ethernet Defaults
Managing Power over Ethernet (PoE)
page 4-6
OmniSwitch 6860 Hardware Users Guide
December 2025
Power over Ethernet Defaults
The following table lists the defaults for PoE configuration:
Understanding and Modifying the Default Settings
The sections below provide information on each of the key components within the Power over Ethernet 
software. They include information on PoE-related CLI commands. For detailed information on PoE-
related commands, refer to the OmniSwitch CLI Reference Guide. 
Note. PoE units support different wattage power supplies. If unlike power supplies are mixed or if an 
unsupported power supply is used, a console message and a trap are generated.
Parameter Description
Command(s)
Default Value/Comments
PoE operational status
lanpower slot service 
Disabled
Power available to a port
lanpower power
OS6860 models: 
- 30000 milliwatts on all ports.
OS6860E models: 
- 60000 milliwatts on ports 1 through 4.
- 30000 milliwatts on ports 5 and higher.
OS6860E-P248Z8: 
- 30000 milliwatts on ports 1 through 16. 
- 75000 milliwatts on ports 17 through 24. 
OS6860N-P48Z: 
- 60000 milliwatts on ports 1-36.
- 95000 milliwatts on ports 37-48.
OS6860N-P48M: 
- 95000 milliwatts on ports 1-48.
OS6860N-P24Z: 
- 60000 milliwatts on ports 1-12.
- 95000 milliwatts on ports 13-24.
OS6860N-P24M: 
- 95000 milliwatts on ports 1-24.
Power available to an entire 
slot
lanpower slot maxpower
Use the show lanpower command to deter-
mine PoE power available. 
Power priority level for a 
port
lanpower priority
low
Capacitor detection method
lanpower capacitor-detec-
tion
Disabled
Priority disconnect status
lanpower slot priority-dis-
connect
Enabled

<<<PAGE 95>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Defaults
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-7
PoE Class Detection 
Powered devices can be classified into different classes as shown in the table below. Class detection 
allows for automatic maximum power adjustment based on the power class detected. This will prevent the 
switch from delivering more than the maximum power allowed based on a device’s class. 
During class detection, the switch will allocate the maximum amount of power allowed based on the class 
detected. Once powered, if the device uses less than the maximum, the remaining power will be made 
available for other devices. 
Although class-detection is disabled by default, the OS6860 still provides power to incoming PDs (if 
available in the power budget). However, to strictly enforce class detection as specified in the 802.3at 
standard, class detection must be enabled using the lanpower slot class-detection command.
Enabling class detection will reset all PoE ports on the chassis.
PoE Operational Status
Enabling PoE
By default, Power over Ethernet is administratively enabled in the switch’s system software. However, in 
order to physically activate PoE, you must issue the lanpower slot service command on a slot-by-slot 
basis before any connected PDs will receive inline power.
To activate power to PoE-capable in a switch, enter the corresponding slot number only. For example:
-> lanpower slot 2/1 service start
If power to a particular port has been administratively disconnected, you can reactivate power to the port 
using the lanpower port admin-state command. For example:
-> lanpower port 2/1/1-24 admin-state enable
Note. You cannot use the lanpower port admin-state command to initially activate PoE on a port. This 
syntax is intended only to reactivate power to those that have been disconnected via the lanpower slot 
service command. To initially activate PoE, you must use the lanpower slot service command as 
described above.
Standard
Class
Type
Pairs
Power at Port 
(Watts)
IEEE 802.3af
0
1
2
15.4
1
1
2
4.0
2
1
2
7.0
3
1
2
15.4
802.3at
4
2
2
30
802.3bt
5
3
4
45
6
3
4
60
7
4
4
75
8
4
4
90-99

<<<PAGE 96>>>
Power over Ethernet Defaults
Managing Power over Ethernet (PoE)
page 4-8
OmniSwitch 6860 Hardware Users Guide
December 2025
Disabling PoE
To disable PoE on a particular port, use the lanpower port admin-state command. For example:
-> lanpower port 1/1/12 admin-state disable
To disable PoE for all PoE-capable ports in a slot, use the lanpower slot service command. For example:
-> lanpower slot 1/1 service stop
Fast PoE
Fast PoE can be used to provide PoE power within a few seconds after powering on the chassis. Prior to 
this feature PoE power was not provided until the chassis had completed boot-up. With Fast PoE the 
default state of the PoE subsystem is set to enabled in the FPGA image and the PoE configuration is stored 
in the controller EEPROM. This allows the chassis to immediately provide PoE power to any connected 
devices immediately after being powered on without waiting for the chassis to complete the boot-up 
process. 
• Fast PoE requires the proper FPGA/CPLD version, refer to the release notes for additional information. 
• Factory default switches that don't have any PoE configuration must have an initial PoE configuration 
completed. 
• The PoE configuration cannot be modified until the switch is up and the PoE software module is 
completely initialized.
• LLDP-based PoE devices will not function as expected until the switch has completed the boot-up 
process and the switch is in a state to respond to LLDP requests.
Perpetual PoE
Perpetual PoE allows the switch to provide uninterrupted power to connected power devices (PD) even 
when the switch is rebooting or reloading, such as on a soft reset. 
• Perpetual PoE requires the proper FPGA/CPLD version, refer to the release notes for additional infor-
mation.
• The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being 
upgraded.
Configuring the Total Power Available to a Port
By default, each port is authorized by the system software to use up to a maximum amount of milliwatts to 
power any attached device. 
You can either increase or decrease this value based on the allowed ranges.
Increasing the total power available to an individual port may provide a more demanding Powered Device 
(PD) with additional power required for operation. Decreasing the total power available to a port helps to 
preserve inline power and assists in the overall management of the switch’s power budget.
To increase or decrease the total power available to an individual port, use the lanpower power command. 
Since you are setting the power allowance for an individual port, you must specify chassis/slot/port values 
in the command line. For example, the syntax
-> lanpower port 1/1/24 power 3000

<<<PAGE 97>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Defaults
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-9
reduces the power allowance on port 24 to 3000 milliwatts. This new value is now the maximum amount 
of power the port can use to power any attached device (until the value is modified by the user).
Configuring the Total Power Available to a slot
Like the maximum port power allowance, the system software also provides a maximum slot-wide power 
allowance. By default, each slot is authorized by the system software to use a number of watts to power all 
devices connected to its ports depending on which power supply is used.
As with the maximum port power allowance, the user can either increase or decrease this value based on 
the allowed ranges.
Important. Decreasing the slot-wide power could cause lower priority ports to lose power if the new 
value is less than the total PoE power currently being consumed. 
To increase or decrease the total power available to a slot, use the lanpower slot maxpower command. 
Since you are setting the power allowance for an individual slot, you must specify a chassis/slot value in 
the command line. For example, the syntax
-> lanpower slot 3/1 maxpower 400
reduces the power allowance of chassis 3, slot 1 to 400 watts. This value is now the maximum amount of 
power the slot can use to power all attached devices (until the value is modified by the user).
Note. Changing the maximum power available to a slot or port does not reserve or immediately allocate 
that power. These settings are only used for configuring a maximum amount of power that may be used, 
any unused power is still available and remains a part of the overall PoE budget. 
Setting Port Priority Levels
As not all Powered Devices (PDs) connected to the switch have the same priority within a network setting, 
the OmniSwitch allows the administrator to specify priority levels on a port-by-port basis. Priority levels 
include low, high, and critical. The default priority level for a port is low.
• Low. This default value is used for port(s) that have low-priority devices attached. In the event of a 
power management issue, inline power to low-priority is interrupted first (i.e., before critical and high-
priority).
• High. This value is used for port(s) that have important, but not mission-critical, devices attached. If 
other ports in the chassis have been configured as critical, inline power to high-priority is given second 
priority.
• Critical. This value is used for port(s) that have mission-critical devices attached, and therefore require 
top (i.e., critical) priority. In the event of a power management issue, inline power to critical is main-
tained as long as possible.
To change the priority level for a particular port, use the lanpower priority command. Since the switch 
allows you to set priority levels on a port-by-port basis, be sure to specify chassis/slot/port information in 
the command line. For example, the syntax 
-> lanpower port 1/1/6 priority critical

<<<PAGE 98>>>
Power over Ethernet Defaults
Managing Power over Ethernet (PoE)
page 4-10
OmniSwitch 6860 Hardware Users Guide
December 2025
changes the priority value of port 6 to the highest priority level of critical. Now that the default value has 
been reconfigured, this port should be reserved for those PDs that are mission critical for network opera-
tions.
Setting the Capacitor Detection Method
By default, the capacitor detection method is disabled. To enable it, use the lanpower capacitor-detec-
tion. For example:
-> lanpower slot 3/1 capacitor-detection enable
Note. The capacitive detection method should only be enabled to support legacy IP phones. This feature 
is not compatible with IEEE specifications. Please contact your Alcatel-Lucent sales engineer or Customer 
Support representative to find out which Alcatel-Lucent IP phones models need capacitive 
detection enabled.
Setting Timers and Other User-Defined PoE Power Rules
The lanpower power-rule command allows user to set additional rules for PoE power (e.g., setting PoE to 
turn on or off on specific dates or at specific times). Refer to the OmniSwitch AOS CLI Guide for more 
information.

<<<PAGE 99>>>
Managing Power over Ethernet (PoE)
Understanding Priority Disconnect
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-11
Understanding Priority Disconnect
The priority disconnect function differs from the port priority function described on page 4-9 in that it 
applies only to the addition of powered devices (PDs) in tight power budget conditions. Priority discon-
nect is used by the system software in determining whether an incoming PD will be granted or denied 
power when there are too few watts remaining in the PoE power budget for an additional device. For 
example, if there are only 2 watts available in the current PoE power budget and a user plugs a 3.5W 
powered device into a PoE port, the system software must determine whether the device will be powered 
on. Based on priority disconnect rules, in some cases one or more existing devices may be powered down 
in order to accommodate the incoming device. In other cases, the incoming device will be denied power.
Priority disconnect rules involve the port priority status of an incoming device (i.e., low, high, and criti-
cal), as well as the port’s physical port number (i.e., 1–24). Understanding priority disconnect rules is 
especially helpful in avoiding power budget deficits and the unintentional shutdown of mission-critical 
devices when PDs are being added in tight power budget conditions. For detailed information on how 
priority disconnect uses port priority and port number criteria for determining the power status of incom-
ing PDs, refer to the illustrated examples on pages 4-12 through 4-13.
Reminder. Priority disconnect applies only when there is inadequate power remaining in the power 
budget for an incoming device.
Note. For OS6860 switches using 920W power supplies, priority disconnect supports up to a maximum of 
780W of PoE power (per power supply installed). For switches using 600W power supplies, priority 
disconnect supports up to a maximum of 450W of PoE power (per power supply installed). 
For information on setting the priority disconnect status, refer to the section below. For information on 
setting the port priority status (a separate function from priority disconnect), refer to “Setting Port Priority 
Levels” on page 4-9.
Setting Priority Disconnect Status
By default, priority disconnect is enabled in the switch’s system software. For information on changing 
the priority disconnect status, refer to the information below.
Disabling Priority Disconnect
When priority disconnect is disabled and there is inadequate power in the budget for an additional device, 
power will be denied to any incoming PD, regardless of its port priority status (i.e., low, high, and criti-
cal) or physical port number (i.e., 1–24).
To disable priority disconnect, use the lanpower slot priority-disconnect command. For example: 
-> lanpower slot 2/1 priority-disconnect disable
Enabling Priority Disconnect
To enable priority disconnect, use the lanpower slot priority-disconnect command. For example: 
-> lanpower slot 2/1 priority-disconnect enable

<<<PAGE 100>>>
Understanding Priority Disconnect
Managing Power over Ethernet (PoE)
page 4-12
OmniSwitch 6860 Hardware Users Guide
December 2025
Priority Disconnect is Enabled; Same Priority Level on All PD 
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When a PD is being connected to a port with the same priority level as all other in the slot, the physical 
port number is used to determine whether the incoming PD will be granted or denied power. Due to the 
support of different PoE standards and PoE hardware on each platform the internal port priority is differ-
ent for each platform. The following tables should be used to determine PoE priority:
PoE Physical Port Priority
Priority Disconnect is Enabled; Incoming PD Port has Highest Priority Level
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When a PD is being connected to a port with a higher priority level than all other in the slot, the incoming 
PD will automatically be granted power over the other devices, regardless of its physical port number. 
In order to avoid a power budget deficit, another port in the slot is disconnected. In determining which port 
to power off, the system software first selects the port with the lowest configured priority level. For exam-
ple, if a critical priority device is being added to a slot in which five existing devices are attached to high 
priority and one device is attached to a low priority port, the low priority port is automatically discon-
nected, regardless of its physical port number. 
If all existing devices are attached to with the same lower priority level, the system software disconnects 
the port with both the lowest priority level and the highest priority physical port number. For example, if a 
critical priority device is being added to a slot in which six existing devices are attached to high priority, 
the high priority port with the lowest physical port priority number is automatically disconnected.
Priority Disconnect is Enabled; Incoming PD Port has Lowest Priority Level
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When a PD is being connected to a port with a lower priority level than all other in the slot, the incoming 
PD will be denied power, regardless of its physical port number. Devices connected to other higher-prior-
ity will continue operating without interruption.
OS6860 Physical Port - 24 Port Models
24 (Highest) -> 1 (Lowest)
OS6860 Physical Port - 48 Port Models
48 (Highest) -> 1 (Lowest)

<<<PAGE 101>>>
Managing Power over Ethernet (PoE)
Understanding Priority Disconnect
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-13
Priority Disconnect is Disabled
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When priority disconnect is disabled, power will be denied to any incoming PD, regardless of its port 
priority status (i.e., low, high, and critical) or physical port number (i.e., 1–24).

<<<PAGE 102>>>
Understanding Guard Band
Managing Power over Ethernet (PoE)
page 4-14
OmniSwitch 6860 Hardware Users Guide
December 2025
Understanding Guard Band 
Guard Band functionality is implemented when the switch has to provide power to a newly connected PD. This 
functionality is more relevant on switches that have a lower amount of total PoE power available for the switch 
but a higher default maximum PoE power available to some ports. 
•
If the amount of power remaining is less than the port's configured maximum PoE power value or the PD's 
class maximum power then the switch will not power up the PD. 
•
This applies even if the newly connected PD actually requires less than the maximum power available for 
the port. 
For example, assume the following: 
•
There is 50W of PoE power remaining on the switch. 
•
A newly connected PD only requires 4W of power. 
•
The port's maximum PoE power value is 75W. 
In this example the newly connected PD will not be powered on since the port's maximum PoE power value is 
greater than the PoE power remaining on the switch. 
 
To allow the PD to be powered, the port's maximum PoE value can be configured to be less than the power 
remaining by issuing the following command to set the port's maximum PoE power to 10W:
-> lanpower power 1/1/1 power 10000
Using the previous example:
•
There is 50W of PoE power remaining on the switch. 
•
A newly connected PD only requires 4W of power. 
•
The port's maximum PoE power value is now 10W.
The newly connected PD will be powered on since the port's maximum PoE power value is now less than the 
PoE power remaining on the switch. The examples assume the new PD has the same or lower priority as the 
existing PDs, otherwise priority disconnect will override. 
The Guard Band functionality does not apply to PDs that are already powered up. However, priority disconnect 
will apply if there's not enough power to power all PDs in the case of the power budget being reduced, such as 
the removal of a power supply.
Please refer to the “Understanding Priority Disconnect” on page 4-11 for additional details.

<<<PAGE 103>>>
Managing Power over Ethernet (PoE)
Monitoring Power over Ethernet via CLI
OmniSwitch 6860 Hardware Users Guide
December 2025
page 4-15
Monitoring Power over Ethernet via CLI
To monitor current PoE statistics and settings, use the show lanpower slot command. The command 
output displays a list of all current PoE-capable, along with the following information for each port:
• Maximum power available to the port, in milliwatts
• Actual power used by the port
• Current port status
• Power priority status
• Power on/off status
Aggregate slot and chassis management information is also displayed. This information includes:
• Maximum watts available to the corresponding slot
• Amount of power budget remaining for PoE modules 
• Total amount of power remaining for additional switch functions
When entering the show lanpower command, you must include a valid slot number in the command line 
syntax. For example: 
-> show lanpower 2/1
Port Maximum(mW) Actual Used(mW)   Status    Priority   On/Off    Class
----+-----------+---------------+-----------+---------+--------+-------
  1     30000        12500       Powered On     Low      ON        0
2     30000         1800       Powered On     Low      ON        1
3     30000         3500       Powered On     Low      ON        2
4     30000         9800       Powered On     Low      ON        3
5     30000        25000       Powered On     Low      ON        4
6     30000            0       Undefined      Low      ON        -
7     30000            0       Undefined      Low      ON        -
8     30000            0       Undefined      Low      ON        -
9     30000            0       Undefined      Low      ON        -
(output truncated)
21     30000            0       Undefined      Low      ON        -
22     30000            0       Undefined      Low      ON        -
23     30000            0       Undefined      Low      ON        -
24     30000            0       Undefined      Low      ON        -
Slot 3 Max Watts 150
1 Power Supplies Available
Note. For detailed information on show lanpower command output, refer to the OmniSwitch CLI Refer-
ence Guide.

<<<PAGE 104>>>
OmniSwitch 6860 Hardware Users Guide
December 2025
page A-1
A  Regulatory Compliance
and Safety Information
This appendix provides information on regulatory agency compliance and safety for OmniSwitch 6860 
switches.
Declaration of Conformity: CE Mark
This equipment is in compliance with the essential requirements and other provisions of 
Directive 2014/30/EU (EMC), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/EEC (Telecom 
Terminal Equipment, if applicable), 2014/53/EU (R&TTE, if applicable). 
Français: Cet équipement est conforme aux exigences essentielles et aux autres provisions de la Directive 
2014/30/EU (EMC), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/CEE (équipements 
terminaux de télécommunications, le cas échéant), 2014/53/EU (R&TTE, le cas échéant). 
Deutsch: Diese Ausrüstung erfüllt die wesentlichen Anforderungen und sonstigen Bestimmungen der 
Richtlinien 2014/30/EU (EMV-Richtlinie), 2014/35/EU (Niederspannungsrichtlinie), 2011/65/EU (RoHS-
Directive), 91/263/EEC (Telekommunikationsendeinrichtungen, falls zutreffend), 2014/53/EU (Funkanla-
gen und Telekommunikationsendeinrichtungen, falls zutreffend). 
Español: Este equipo cumple los requisitos esenciales y otras disposiciones de las directivas 2014/30/EU 
(EMC), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/CEE (equipos terminales de teleco-
municación, si procede), 2014/53/EU (R&TTE, si procede). 
Waste Electrical and Electronic Equipment (WEEE) Statement
The product at end of life is subject to separate collection and treatment in the EU Member States, Norway 
and Switzerland and therefore marked with the following symbol:
Treatment applied at end of life of the product in these countries shall comply with the applicable national 
laws implementing directive 2002/96/EC on waste electrical and electronic equipment (WEEE).

<<<PAGE 105>>>
Declaration of Conformity: CE Mark
Regulatory Compliance and Safety Information
page A-2
OmniSwitch 6860 Hardware Users Guide
December 2025
China RoHS: Hazardous Substance Table

<<<PAGE 106>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6860 Hardware Users Guide
December 2025
page A-3
Taiwan RoHS: Hazardous Substance Table
California Proposition 65 Warning
WARNING: This product can expose you to chemicals including Pb and Pb compounds, which is known 
to the State of California to cause cancer and birth defects or other reproductive harm. For more 
information go to www.P65Warnings.ca.gov.
Products are packaged using one or more of the following packaging materials:
Standards Compliance
The product bears the CE mark. In addition it is in compliance with the following other safety and 
EMC standards.
Corrugated Cardboard                Corrugated Fiberboard              Low-Density Polyethylene
CB
FB

<<<PAGE 107>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-4
OmniSwitch 6860 Hardware Users Guide
December 2025
Note. All hardware switching modules used in an OmniSwitch 6860 switch comply with Class A 
standards. Modules with copper connectors meet Class A requirements using unshielded (UTP) cables.
Safety Standards
• US UL 60950-1
• US UL 62368-1
• IEC 60950-1 Health and Safety
• IEC 62368-1 Audio/Video, Information Technology: Safety requirement
• CAN/CSA-C22.2 No. 60950-1
• CAN/CSA-C22.2 No. 62638-1
• EN 62368-1
• NOM-019 SCFI, Mexico
• AS/NZ TS-001 and 60950:2000, Australia
• UL-AR, Argentina
• UL-GS Mark, Germany
• CU, EAC, Russia
• EN 60825-1 Laser
• EN 60825-2 Laser
• CDRH Laser
• IEC 60950-1/EN 60950 with all country deviations
• IEC 62368-1/EN 62368-1 with all country deviations
• CCC, China*
• ANATEL, Brazil (Contact for availability)
• BSMI, Taiwan
• KCC, Korea (Contact for availability)
• TEC, India (Contact for availability)
• Morocco (Contact for availability)

<<<PAGE 108>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6860 Hardware Users Guide
December 2025
page A-5
EMI/EMC Standards
• FCC Part 15:2012, Subpart B, Class A
• ICES–003:2012 Issue 5, Class A
• ANSI C63.4-2009
• FCC CRF Title 47 Subpart B (Class A)
• VCCI (Class A)
• AS/NZS 3548 (Class A)
• CE marking for European countries (Class A)
• EN 55032 (EMI & EMC)
• EN 61000-3-2
• EN 61000-3-3
• EN 55024 (Immunity)/EN 55035 (Immunity)
• EN 61000-4-2
• EN 61000-4-3
• EN 61000-4-4
• EN 61000-4-5
• EN 61000-4-6
• EN 61000-4-8
• EN 61000-4-11
• IEEE 802.3: Hi-Pot Test
(2250 V DC on all Ethernet ports)
Environmental Standards
• ETS 300 019 Storage Class 1.1
• ETS 300 019 Transportation Class 2.3
• ETS 300 019 Stationary Use Class 3.1
FCC Class A, Part 15
This equipment has been tested and found to comply with the limits for Class A digital device pursuant to 
Part 15 of the FCC Rules.These limits are designed to provide reasonable protection against harmful 
interference when the equipment is operated in a commercial environment.This equipment generates, uses, 
and can radiate radio frequency energy and, if not installed and used in accordance with the instructions in 
this guide, may cause interference to radio communications.Operation of this equipment in a residential 
area is likely to cause interference, in which case the user will be required to correct the interference at his 
own expense.

<<<PAGE 109>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-6
OmniSwitch 6860 Hardware Users Guide
December 2025
The user is cautioned that changes and modifications made to the equipment without approval of the 
manufacturer could void the user’s authority to operate this equipment.It is suggested that the user use 
only shielded and grounded cables to ensure compliance with FCC Rules.
If this equipment does cause interference to radio or television reception, the user is encouraged to try to 
correct the interference by one or more of the following measures:
• Reorient the receiving antenna.
• Relocate the equipment with respect to the receiver.
• Move the equipment away from the receiver.
• Plug the equipment into a different outlet so that equipment and receiver are on different branch 
circuits.
If necessary, the user should consult the dealer or an experienced radio/television technician for additional 
suggestions.
Canada Class A Statement
This equipment does not exceed Class A limits per radio noise emissions for digital apparatus, set out in 
the Radio Interference Regulation of the Canadian Department of Communications.
Avis de conformitè aux normes du ministère des Communications du Canada 
Cet èquipement ne dèpasse pas les limites de Classe A d íèmission de bruits radioèlectriques pour les 
appareils numèriques,telles que prescrites par le RÈglement sur le brouillage radioèlectrique ètabli par le 
ministère des Communications du Canada.
JATE
This equipment meets the requirements of the Japan Approvals Institute of Telecommunications 
Equipment (JATE).
CISPR22 Class A warning
This is a Class A product. In a domestic environment, this product may cause radio interference. Under 
such circumstances, the user may be requested to take appropriate countermeasures.

<<<PAGE 110>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6860 Hardware Users Guide
December 2025
page A-7
Korea Emissions Statement
VCCI
This is a Class A product based on the standard of the Voluntary Control Council for Interference by 
Information Technology Equipment (VCCI). If this equipment is used in a domestic environment, radio 
disturbance may arise. When such trouble occurs, the user may be required to take corrective actions.
Class A Warning for Taiwan (BSMI) and Other Chinese Markets
Warning: To avoid electromagnetic interference, this product should not be installed or used in residential 
environments.
警告：為避免電磁干擾，本產品不應安裝或使用於住宅環境
Class 1M Laser Warning
CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL 
INSTRUMENTS.
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
Translated Safety Warnings
Blank Panels Warning
Because they regulate airflow and help protect internal chassis components, blank cover plates should 
remain installed at empty module slots and power supply bays at all times.
Français: Les caches blancs remplissent trois fonctions importantes: ils évitent tout risque de choc 
électrique à l'intérieur du châssis, ils font barrage aux interférences électromagnétiques susceptibles 
d'altérer le fonctionnement des autres équipements et ils dirigent le flux d'air de refroidissement dans le 
A 급 기기 ( 업무용 방송통신 기자재)
이 기기는 업무용(A 급) 전자파적합기기로서 판
매자 또는 사용자는 이 점을 주의하시기 바라
며, 가정외의 지역에서 사용하는 것을 목적으
로 합니다.
Class A Equipment (Business equipment)
This equipment is registered for Electromagnetic 
Conformity Registration as business equipment 
(A), not home equipment. Sellers or users are 
required to take caution in this regard.

<<<PAGE 111>>>
Translated Safety Warnings
Regulatory Compliance and Safety Information
page A-8
OmniSwitch 6860 Hardware Users Guide
December 2025
châssis. Il est vivement recommandé de vérifier que tous les caches, modules d'alimentation et plaques de 
protection sont en place avant d'utiliser le système.
Deutsch: Die leeren Modulblenden schützen interne Komponenten und leiten den Luftstrom. Deshalb 
müssen in allen unbelegten Slots die Modulblenden immer installiert bleiben. 
Español: Las tapaderas blancas regulan la circulación de aire y ayudan a proteger componentes internos 
del chasis y siempre deben estar instaladas en las ranuras vacías del chasis y fuentes de alimentación.
Electrical Storm Warning
To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or 
reconfiguration of this product during an electrical storm.
Français: Ne pas travailler sur le système ni brancher ou débrancher les câbles pendant un orage.
Deutsch: Um elektrische Schläge zu vermeiden dürfen während eines Gewitters an diesem Gerät keine 
Kabel angeschlossen oder gelöst werden, sowie keinerlei Installationen, Wartungen oder Konfigurationen 
vorgenommen werden.
Español: Para evitar peligro de descargas, no conecte o desconecte ningun cable, ni realice ninguna 
instalación, maintenimiento o reconfiguración de este producto durante una tormenta eléctrica.
Installation Warning
Only personnel knowledgeable in basic electrical and mechanical procedures should install or maintain 
this equipment.
Français: Toute installation ou remplacement de l'appareil doit être réalisée par du personnel qualifié et 
compétent.
Deutsch: Dieses Gerät soll nur von Personal installiert oder gewartet werden, welches in elektrischen und 
mechanischen Grundlagen ausgebildet ist.
Español: Estos equipos deben ser instalados y atendidos exclusivamente por personal adecuadamente 
formado y capacitado en técnicas eléctricas y mecánicas.
Invisible Laser Radiation Warning
Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When 
removing cables do not stare into the open apertures. In addition, install protective aperture covers to fiber 
ports with no cable connected.
Français: Des radiations invisibles à l'œil nu pouvant traverser l'ouverture du port lorsque aucun câble en 
fibre optique n'y est connecté, il est recommandé de ne pas regarder fixement l'intérieur de ces ouvertures. 
Installez les caches connecteurs prévus à cet effet. 
Deutsch: Die Laser strahlen an der Blendenöffnung unsichtbares Licht ab, wenn keine Glasfaserkabel 
angeschlossen sind. Blicken Sie nicht in die Öffnungen und installieren Sie unverzüglich die Abdeckungen 
über den Glasfaseranschlüssen.
Español: Debido a que la apertura del puerto puede emitir radiación invisible cuando no hay un cable de 
fibra conectado, procurar no mirar directamente a las aperturas para no exponerse a la radiación.

<<<PAGE 112>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6860 Hardware Users Guide
December 2025
page A-9
Operating Voltage Warning
To reduce the risk of electrical shock, keep your hands and fingers out of power supply bays and do not 
touch the backplane while the switch is operating.
Français: Pour réduire tout risque électrique, gardez vos mains et doigts hors des alimentations et ne 
touchez pas au fond de panier pendant que le commutateur fonctionne.
Deutsch: Um die Gefahr des elektrischen Schlages zu verringern, greifen sie bitte nicht in die 
Spannungsversorgung und berühren sie nicht die Rückwandplatine während das Gerät arbeitet.
Español: Para reducir el riesgo de descargas eléctricas, no meta sus manos y dedos dentro del chasis de la 
fuente de alimentación y no toque componentes internos mientras que el interruptor está conectado.
Power Disconnection Warning
Your switch is equipped with multiple power supplies. To reduce the risk of electrical shock, be sure to 
disconnect all power connections before servicing or moving the unit.
Français: Il se peut que cette unité soit équipée de plusieurs raccordements d'alimentation. Pour 
supprimer tout courant électrique de l'unité, tous les cordons d'alimentation doivent être débranchés.
Deutsch: Ihr Gerät ist mit mehreren Netzteilen ausgerüstet. Um die Gefahr des elektrischen Schlages zu 
verringern, stellen sie sicher, daß alle Netzverbindungen getrennt sind bevor das Gerät gewartet oder 
bewegt wird.
Español: Antes de empezar a trabajar con un sistema, asegurese que el interruptor está cerrado y el cable 
eléctrico desconectado.
Proper Earthing Requirement Warning
To avoid shock hazard:
• The power cord must be connected to a properly wired and earth receptacle.
• Any equipment to which this product will attached must also be connected to properly wired 
receptacles.
Français:
Pour éviter tout risque de choc électrique:
• Ne jamais rendre inopérant le conducteur de masse ni utiliser l'équipement sans un conducteur de 
masse adéquatement installé.
• En cas de doute sur la mise à la masse appropriée disponible, s'adresser à l'organisme responsable de 
la sécurité électrique ou à un électricien.
Deutsch: 
Aus Sicherheitsgründen:
• darf das Netzkabel nur an eine Schutzkontaktsteckdose angeschlossen werden.
• dürfen für den Anschluß anderer Geräte, welche mit diesem Gerät verbunden sind, auch nur 
Schutzkontaktsteckdosen verwendet werden.
Español: 
Para evitar peligro de descargas:
• Para evitar peligro de descargas asegurese de que el cable de alimentación está conectado a una 
toma de alimentación adecuadamente cableada y con toma de tierra.

<<<PAGE 113>>>
DC Power Supply Connection Warning
Regulatory Compliance and Safety Information
page A-10
OmniSwitch 6860 Hardware Users Guide
December 2025
• Cualquier otro equipo a cual se conecte este producto también debe estar conectado a tomas de 
alimentación adecuadamente cableadas.
DC Power Supply Connection Warning
For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/DC 
power supply to Earth Ground.
Français: Pour EMC/EMI, pour chaque alimentation DC/DC, il est impératif que le fil de terre soit 
branché à la prise de terre.
Deutsch: Zur Erfüllung der EMV-/EMI-Anforderungen muss das Erdungskabel jedes DC/DC-Netzteils an 
eine Erde angeschlossen werden.
Español: Para EMC/EMI, cada fuente de alimentación de CC/CC requiere que el cable de tierra esté 
conectado desde cada fuente de alimentación de CC/CC a la conexión a tierra.
Read Important Safety Information Warning
The Getting Started Guide that accompanied this equipment contains important safety information about 
which you should be aware when working with hardware components in this system. You should read this 
guide before installing, using, or servicing this equipment.
Français: Avant de brancher le système sur la source d'alimentation, consultez les directives d'installation 
disponibles dans le “Getting Started Guide”.
Deutsch: Der Getting Started Guide, welcher diese Anlage beiliegt, enthält wichtige 
Sicherheitsinformationen, über die sie sich beim Arbeiten mit den Hardwareeinheiten bewußt sein sollten. 
Sie sollten diese Hinweise lesen, bevor sie installieren, reparieren oder die Anlage verwenden.
Español: La 'Getting Started Guide' que acompañó este equipo contiene información importante de 
seguridad sobre la cual usted debe estar enterado al trabajar con los componentes de dotación física en este 
sistema. Usted debe leer esta guía antes de instalar, usar o mantener este equipo.
Restricted Access Location Warning
This equipment should be installed in a location that restricts access. A restricted access location is one 
where access is secure and limited to service personnel who have a special key, or other means of security.
Français: Le matériel doit être installé dans un local avec accès limité ou seules les personnes habilitées 
peuvent entrer.
Deutsch: Die Anlage sollte an einem Standort mit beschränktem Zutritt installiert sein. Ein Standort mit 
beschränktem Zutritt stellt sicher, daß dort nur Servicepersonal mit Hilfe eines Schlüssels oder eines 
anderen Sicherheitssystems Zugang hat.
Español: Este equipo se debe instalar en un sitio con acceso restrinjido. Un sitio con el acceso restrinjido 
es uno seguro y con acceso limitado al personal de servicio que tiene una clave especial u otros medios de 
seguridad.
Wrist Strap Warning
Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures 
to eliminate ESD from your person and the surrounding area before handling switch components.

<<<PAGE 114>>>
Regulatory Compliance and Safety Information
Instrucciones de seguridad en español
OmniSwitch 6860 Hardware Users Guide
December 2025
page A-11
Français: Parce que les décharges électrostatiques (ESD) peuvent endommager les composants de 
commutation, vous devez suivre les procédures appropriées pour éliminer ESD de votre personne et la 
région environnante avant de manipuler les composants de commutation.
Deutsch: Da elektrostatische Entladung (ESD) Komponenten beschädigen können, müssen geeignete 
Verfahren getroffen werden, diese elektrostatische Entladung bedingt durch Ihre Person oder der 
Umgebung zu beseitigen.
Español: Debido a las descargas electrostáticas (ESD) puede dañar los componentes del interruptor, debe 
seguir los procedimientos adecuados para eliminar la EDS de su persona y sus alrededores antes de 
manipular los componentes del interruptor.
Instrucciones de seguridad en español
Advertencia sobre el levantamiento del chasis
Se requieren dos personas para levantar el chasis. Debido a su peso, la elevación del chasis sin ayuda 
puede causar daños corporales. También es seguro doblar sus rodillas y guardar su espalda derecho al 
ayudar a levantar el chasis.
Advertencia de las tapaderas en blanco
Porque regulan la circulación de aire y ayudan a proteger componentes internos del chasis, las tapaderas 
en blanco deben seguir instaladas en las ranuras vacías del módulo y la fuente de alimentación siempre.
Advertencia en caso de tormenta eléctrica
Para evitar peligro de descargas, no conecte o desconecte ningun cable, ni realice ninguna instalación, 
maintenimiento o reconfiguratión de este producto durante una tormenta eléctrica.
Advertencia de instalación
Solamente el personal bien informado en procedimientos eléctricos y mecánicos básicos debe instalar o 
mantener este equipo.
Advertencia de radiación láser invisible
Los lasers emiten radiación invisible de la apertura abierta cuando no se conecta ningún cable de fibra 
óptica. Al quitar los cables no mire fijamente en las aberturas abiertas. Además, instale las cubiertas 
protectoras de la abertura a las salidas de la fibra sin el cable conectado.
Advertencia de la batería de litio
Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente. Substituya 
la batería solamente por el mismo o el equivalente de tipo de batería recomendado por el fabricante. 
Deseche las baterías usadas según las instrucciones del fabricante. Las instrucciones del fabricante son 
como sigue: Devuelva el módulo con la batería del litio a Alcatel-Lucent. La batería del litio será 
substituida en la fábrica de Alcatel-Lucent.
Advertencia sobre la tensión de operación
Para reducir el riesgo del choque eléctrico, matenga sus manos y dedos fuera de la fuente de alimentación 
y no toque la placa madre mientras que el interruptor está funcionando.

<<<PAGE 115>>>
Instrucciones de seguridad en español
Regulatory Compliance and Safety Information
page A-12
OmniSwitch 6860 Hardware Users Guide
December 2025
Advertencia sobre la desconexión de la fuente
Su interruptor esta equipado por fuentes de alimentación múltiples. Para reducir el riesgo de choque 
eléctrico, asegúrese desconectar todas las conexiones de alimentación antes de mantener o de mover la 
unidad.
Advertencia sobre una apropiada conexión a tierra
Para evitar peligro de descargas:
• El cable de alimentación debe estar conectado a una toma de alimentación adecuadamente cableada 
y con toma de tierra.
Cualquier equipo al cual se conecte este producto debe estar también conectado a tomas de alimentación 
adecuadamente cableadas.
Leer “información importante de seguridad”
La Guía de “Comenzando a Usar” que acompaña este equipo contiene información importante de 
seguridad sobre la cual usted debe saber al trabajar con los componentes de dotación física en este sistema. 
Usted debe leer esta guía antes de instalar, de usar, o de mantener este equipo.
Advertencia de acceso restringido
Este equipo se debe instalar en una ubicación que restrinja el acceso. Una ubicación con acceso restringido 
es una donde está seguro y limitado el acceso al personal de servicio que tiene un clave especial, u otros 
medios de la seguridad.
Advertencia de pulsera antiestática
Debido a que la descarga electrostática (ESD) puede dañar componentes del interruptor, usted debe 
conectarse a tierra correctamente antes de continuar con la instalación del equipo. Para este propósito, 
Alcatel-Lucent proporciona una pulsera antiestática y un terminal que pone a tierra situados cerca de la 
parte superior derecha del chasis. Para que la pulsera antiestática sea eficaz en la eliminación de ESD, las 
fuentes de alimentación se deben instalar en el chasis y enchufar en las salidas de CA con descarga a 
tierra.
Clase de seguridad
Cumple con 21CFR 1040.10 y 1040.11 ó sus equivalentes.
Advertencia de fuentes de poder
Las unidades OmniSwitch 6860 pueden estar equipadas con tres cordones para fuente de poder. Para 
reducir el riesgo de un choque electrico, desconecte todos los cordones de fuente de poder antes de dar 
servicio a la unidad.