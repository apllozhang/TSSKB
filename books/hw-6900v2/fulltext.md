<<<PAGE 1>>>
Part No. 060925-00, Rev. C
December 2025
OmniSwitch 6900
Hardware Users Guide
www.al-enterprise.com

<<<PAGE 2>>>
This user guide documents OmniSwitch 6900 hardware, including chassis and associated components. 
The specifications described in this guide are subject to change without notice.
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/
trademarks-copyright. All other trademarks are the property of their respective owners. The information 
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
OmniSwitch 6900 Hardware Users Guide
December 2025
iii
Contents
About This Guide .........................................................................................................vii
Supported Platforms .........................................................................................................vii
Who Should Read this Manual? .......................................................................................vii
When Should I Read this Manual? ...................................................................................vii
What is in this Manual? ....................................................................................................vii
What is Not in this Manual? ............................................................................................viii
How is the Information Organized? ................................................................................viii
Documentation Roadmap ................................................................................................viii
Related Documentation ...................................................................................................... x
Technical Support ............................................................................................................. xi
Chapter 1
OmniSwitch 6900  ......................................................................................................1-1
OmniSwitch 6900 Availability Features .........................................................................1-2
Power Supply Redundancy ......................................................................................1-2
Hot-Swapping ...........................................................................................................1-2
Hardware Monitoring ...............................................................................................1-2
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
Mounting the Switch .......................................................................................................2-5
Connections and Cabling ................................................................................................2-5
Network Cable Installation Warning .................................................................2-5
Serial Connection to the Console Port ...............................................................2-5
Serial Connection Default Settings ...................................................................2-5
Ethernet Management Port (EMP) Cable Requirements .........................................2-5
Booting the Switch ..........................................................................................................2-7
Component LEDs ..............................................................................................2-7
Your First Login Session ................................................................................................2-8

<<<PAGE 4>>>
Contents
iv
OmniSwitch 6900 Hardware Users Guide
December 2025
Logging In to the Switch ..........................................................................................2-8
Setting IP Address Information for the EMP ...........................................................2-9
Unlocking Session Types .......................................................................................2-10
Changing the Login Password ................................................................................2-10
Setting the System Time Zone ...............................................................................2-11
Setting the Date and Time ......................................................................................2-11
Setting Optional Parameters ...................................................................................2-11
Specifying an Administrative Contact .............................................................2-11
Specifying a System Name ..............................................................................2-11
Specifying the Switch’s Location ....................................................................2-11
Viewing Your Changes ..........................................................................................2-12
Saving Your Changes .............................................................................................2-12
Chapter 3
Chassis and Power Supplies ....................................................................................3-1
OmniSwitch 6900 Chassis ..............................................................................................3-2
OS6900-V72 Front Panel .........................................................................................3-3
OS6900-V72 Rear Panel ..........................................................................................3-3
OS6900-V72 Chassis Specifications .................................................................3-4
OS6900-C32 Front Panel .........................................................................................3-5
OS6900-C32 Rear Panel ..........................................................................................3-5
OS6900-C32 Chassis Specifications .................................................................3-6
OS6900-C32E Front Panel .......................................................................................3-7
OS6900-C32E Rear Panel ........................................................................................3-7
OS6900-C32E Chassis Specifications ...............................................................3-8
OS6900-T48C6 Front Panel .....................................................................................3-9
OS6900-T48C6 Rear Panel ......................................................................................3-9
OS6900-T48C6 Chassis Specifications ...........................................................3-10
OS6900-X48C6 Front Panel ..................................................................................3-11
OS6900-X48C6 Rear Panel ...................................................................................3-11
OS6900-X48C6 Chassis Specifications ..........................................................3-12
OS6900-X48C4E Front Panel ................................................................................3-13
OS6900-X48C4E Rear Panel .................................................................................3-13
OS6900-X48C4E Chassis Specifications ........................................................3-14
OS6900-V48C8 Front Panel ..................................................................................3-15
OS6900-V48C8 Rear Panel ...................................................................................3-16
OS6900-V48C8 Chassis Specifications ..........................................................3-16
OS6900-T24C2 Front Panel ...................................................................................3-17
OS6900-T24C2 Rear Panel ....................................................................................3-18
OS6900-T24C2 Chassis Specifications ...........................................................3-18
OS6900-X24C2 Front Panel ..................................................................................3-19
OS6900-X24C2 Rear Panel ...................................................................................3-20
OS6900-X24C2 Chassis Specifications ..........................................................3-20
OS6920-D32 Front Panel .......................................................................................3-21
OS6920-D32 Rear Panel ........................................................................................3-22
OS6920-D32 Chassis Specifications ...............................................................3-22
Chassis Status LEDs ...............................................................................................3-23
Mounting the Switch .....................................................................................................3-24
General Mounting Recommendations ....................................................................3-24
Airflow Recommendations ....................................................................................3-25
Front-to-Rear Airflow .....................................................................................3-26
Rear-to-Front Airflow .....................................................................................3-26

<<<PAGE 5>>>
Contents
OmniSwitch 6900 Hardware Users Guide
December 2025
v
Airflow Mismatch ...........................................................................................3-27
Blank Cover Panels ................................................................................................3-28
Rack-Mounting .............................................................................................................3-29
Mid-Mounting the Chassis In the Rack ..................................................................3-31
Standalone (Non-Rack Mounted) Installations ......................................................3-33
Weight Considerations ....................................................................................3-33
Proper Clearance .............................................................................................3-33
Power Supplies ..............................................................................................................3-34
Airflow Direction ............................................................................................3-34
OS6900-V72/C32/C32E/X48C4E/V48C8 AC Power Supply ...............................3-35
AC Power Supply LED States .........................................................................3-35
OS6900-T48C6/X48C6/T24C2/X24C2 AC Power Supply ...................................3-36
AC Power Supply LED States .........................................................................3-36
OS6900-V72/C32/C32E/X48C4E/V48C8 DC Power Supply ...............................3-37
DC Power Supply LED States .........................................................................3-37
OS6900-T48C6/X48C6/T24C2/X24C2 DC Power Supply ...................................3-38
DC Power Supply LED States .........................................................................3-38
DC Power Supply Cord (IEC 60945) ..............................................................3-38
OS6920 AC Power Supply .....................................................................................3-39
AC Power Supply LED States .........................................................................3-39
OS6920-D32 DC Power Supply ............................................................................3-40
DC Power Supply LED States .........................................................................3-40
DC Power Supply Connections ..............................................................................3-41
Connecting a DC Cable Harness to the Chassis Power Supply ......................3-41
Connecting a DC Cable Harness to the DC Power Source .............................3-41
Installing Power Supplies .......................................................................................3-42
Removing Power Supplies .....................................................................................3-43
Chassis Fan Tray ...........................................................................................................3-44
Airflow Direction ............................................................................................3-44
Replacing the Fan Tray .................................................................................................3-46
Grounding the Chassis ..................................................................................................3-47
Monitoring Chassis Components ..................................................................................3-48
Viewing Chassis Slot Information .........................................................................3-48
Monitoring Chassis Temperature ..................................................................................3-48
Temperature Errors ..........................................................................................3-49
Monitoring Fan Tray Status .............................................................................3-49
Pinouts ...........................................................................................................................3-50
RJ45 Console Port Connector Pinout ..............................................................3-50
USB Console Port Connector (All Other Models) ..........................................3-50
RJ-45 Console Port – Connector Pinout ..........................................................3-51
10/100 Ethernet Port – RJ-45 Pinout ...............................................................3-51
Gigabit Ethernet Port – RJ-45 Pinout ..............................................................3-51
Appendix A
Regulatory Compliance and Safety Information ..............................................A-1
Declaration of Conformity: CE Mark ............................................................................A-1
Waste Electrical and Electronic Equipment (WEEE) Statement ............................A-1
China RoHS: Hazardous Substance Table .......................................................A-2

<<<PAGE 6>>>
Contents
vi
OmniSwitch 6900 Hardware Users Guide
December 2025
Taiwan RoHS: Hazardous Substance Table .....................................................A-3
California Proposition 65 Warning ..................................................................A-3
Standards Compliance ....................................................................................................A-4
FCC Class A, Part 15 ..............................................................................................A-5
Canada Class A Statement ......................................................................................A-5
JATE ........................................................................................................................A-5
CISPR22 Class A warning ......................................................................................A-6
Korea Emissions Statement .....................................................................................A-6
VCCI .......................................................................................................................A-6
Class A Warning for Taiwan (BSMI) and Other Chinese Markets ........................A-6
Class 1M Laser Warning .........................................................................................A-6
Network Cable Installation Warning .............................................................................A-7
Translated Safety Warnings ...........................................................................................A-7
Blank Panels Warning ......................................................................................A-7
Electrical Storm Warning .................................................................................A-7
Installation Warning .........................................................................................A-7
Invisible Laser Radiation Warning ...................................................................A-8
Operating Voltage Warning .............................................................................A-8
Power Disconnection Warning .........................................................................A-8
Proper Earthing Requirement Warning ............................................................A-9
DC Power Supply Connection Warning ........................................................................A-9
Read Important Safety Information Warning .................................................A-10
Restricted Access Location Warning .............................................................A-10
Wrist Strap Warning .......................................................................................A-10
Instrucciones de seguridad en español .........................................................................A-11
Advertencia sobre el levantamiento del chasis ...............................................A-11
Advertencia de las tapaderas en blanco ..........................................................A-11
Advertencia en caso de tormenta eléctrica .....................................................A-11
Advertencia de instalación .............................................................................A-11
Advertencia de radiación láser invisible .........................................................A-11
Advertencia de la batería de litio ....................................................................A-11
Advertencia sobre la tensión de operación .....................................................A-11
Advertencia sobre la desconexión de la fuente ..............................................A-11
Advertencia sobre una apropiada conexión a tierra .......................................A-12
Leer “información importante de seguridad” .................................................A-12
Advertencia de acceso restringido ..................................................................A-12
Advertencia de pulsera antiestática ................................................................A-12
Clase de seguridad ..........................................................................................A-12
Advertencia de fuentes de poder ....................................................................A-12

<<<PAGE 7>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
vii
About This Guide
This OmniSwitch 6900 Hardware Users Guide describes OmniSwitch 6900 switch components and basic 
switch hardware procedures. 
Supported Platforms
The information in this guide applies only to OmniSwitch 6900 switches.
Who Should Read this Manual?
The audience for this users guide is network administrators and IT support personnel who need to 
configure, maintain, and monitor switches and routers in a live network. However, anyone wishing to gain 
knowledge of OmniSwitch 6900 hardware will benefit from the material in this guide.
When Should I Read this Manual?
Read this guide as soon as you are ready to familiarize yourself with your switch hardware components. 
You should have already stepped through the first login procedures and already be familiar with the very 
basics of the switch hardware, such as module LEDs and component installation procedures. This manual 
will help you understand your switch hardware in greater depth.
What is in this Manual?
This users guide includes the following hardware-related information:
• Descriptions of “Availability” features.
• Technical specifications for the chassis, power supplies, modules and fan tray.
• Power supply requirements.
• The dynamics of chassis airflow, including detailed illustrations of proper and improper airflow 
configurations.
• Hot-swapping power supplies, fan trays and modules.
• Installation and removal procedures for power supplies, fan trays and modules.
• Detailed illustrations and LED descriptions for chassis, network and power supply operability.
• Hardware-related Command Line Interface (CLI) commands.

<<<PAGE 8>>>
viii
OmniSwitch 6900 Hardware Users Guide
December 2025
What is Not in this Manual?
The descriptive and procedural information in this manual focuses on switch hardware. It includes 
information on some CLI commands that pertain directly to hardware configuration, but it is not intended 
as a software users guide. There are several OmniSwitch users guides that focus on switch software 
configuration. Consult those guides for detailed information and examples for configuring your switch 
software to operate in a live network environment. See “Documentation Roadmap” on page -viii and 
“Related Documentation” on page -x for further information on software configuration guides available 
for your switch.
How is the Information Organized?
Each chapter in this guide focuses on a specific hardware component or a set of hardware components. All 
descriptive, technical specification, and procedural information for a hardware component can be found in 
the chapter dedicated to that component.
Documentation Roadmap
The OmniSwitch user documentation suite was designed to supply you with information at several critical 
junctures of the configuration process.The following section outlines a roadmap of the manuals that will 
help you at each stage of the configuration process. Under each stage, we point you to the manual or 
manuals that will be most helpful to you.
Stage 1: Using the Switch for the First Time
Pertinent Documentation: OmniSwitch 6900 Hardware Users Guide “Getting Started” Chapter
A “Getting Started” chapter is included in this guide and provides all the information you need to get your 
switch up and running the first time. It provides information on unpacking the switch, rack mounting the 
switch, installing components, unlocking access control, setting the switch’s IP address, and setting up a 
password. It also includes succinct overview information on fundamental aspects of the switch, such as 
hardware LEDs, the software directory structure, CLI conventions, and web-based management.
At this time you should also familiarize yourself with the Release Notes that accompany this release. This 
document includes important information on feature limitations that are not included in other user guides.
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: OmniSwitch 6900 Hardware Users Guide
OmniSwitch AOS Release 8 Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the OmniSwitch 6900 Hardware 
Users Guide. This guide provide specifications, illustrations, and descriptions of all hardware components. 
It also includes steps for common procedures, such as removing and installing switch components.
This guide is the primary users guide for the basic software features on a single switch. This guide 
contains information on the switch directory structure, basic file and directory utilities, switch access 
security, SNMP, and web-based management. It is recommended that you read this guide before 
connecting your switch to the network.

<<<PAGE 9>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
ix
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: OmniSwitch AOS Release 8 Network Configuration Guide
OmniSwitch AOS Release 8 Advanced Routing Configuration Guide
OmniSwitch AOS Release 8 Data Center Switching Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The Network Configuration Guide guide contains overview information, procedures, and 
examples on how standard networking technologies are configured on the OmniSwitch.
The Advanced Routing Guide includes configuration information for networks using advanced routing 
technologies (OSPF and BGP) and multicast routing protocols (DVMRP and PIM-SM).
The Data Center Switching Guide includes configuration information for data center networks using 
virtualization technologies (SPBM and UNP) and Data Center Bridging protocols (PFC, ETC, and 
DCBX).
Anytime
The OmniSwitch AOS Release 8 CLI Reference Guide contains comprehensive information on all CLI 
commands supported by the switch. This guide includes syntax, default, usage, example, related CLI 
command, and CLI-to-MIB variable mapping information for all CLI commands supported by the switch. 
This guide can be consulted anytime during the configuration process to find detailed and specific 
information on each CLI command.

<<<PAGE 10>>>
x
OmniSwitch 6900 Hardware Users Guide
December 2025
Related Documentation
The following are the titles and descriptions of all the OmniSwitch 6900 user manuals:
• OmniSwitch 6900 Hardware Users Guide
Complete technical specifications and procedures for all OmniSwitch 6900 chassis, power supplies, 
fans, and Network Interface (NI) modules.
• OmniSwitch AOS Release 8 CLI Reference Guide
Complete reference to all CLI commands supported on the OmniSwitch. Includes syntax definitions, 
default values, examples, usage guidelines and CLI-to-MIB variable mappings.
• OmniSwitch AOS Switch Management Guide
Includes procedures for readying an individual switch for integration into a network. Topics include the 
software directory architecture, image rollback protections, authenticated switch access, managing 
switch files, system configuration, using SNMP, and using web management software (WebView).
• OmniSwitch AOS Network Configuration Guide
Includes network configuration procedures and descriptive information on all the major software 
features and protocols included in the base software package. Chapters cover Layer 2 information 
(Ethernet and VLAN configuration), Layer 3 information (routing protocols, such as RIP and IPX), 
security options (authenticated VLANs), Quality of Service (QoS), link aggregation, and server load 
balancing.
• OmniSwitch AOS Advanced Routing Configuration Guide
Includes network configuration procedures and descriptive information on all the software features and 
protocols included in the advanced routing software package. Chapters cover multicast routing 
(DVMRP and PIM-SM), Open Shortest Path First (OSPF), and Border Gateway Protocol (BGP).
• OmniSwitch AOS Data Center Switching Guide
Includes and introduction to the OmniSwitch data center switching architecture as well as network 
configuration procedures and descriptive information on all the software features and protocols that 
support this architecture. Chapters cover Shortest Path Bridging MAC (SPBM), Data Center Bridging 
(DCB) protocols, Virtual Network Profile (vNP), and the Edge Virtual Bridging (EVB) protocol.
• OmniSwitch Transceivers Guide
Includes SFP and XFP transceiver specifications and product compatibility information.
• Technical Tips, Field Notices
Includes information published by Alcatel-Lucent’s Customer Support group.
• Release Notes
Includes critical Open Problem Reports, feature exceptions, and other important information on the 
features supported in the current release and any limitations to their support.

<<<PAGE 11>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
xi
Technical Support
An Alcatel-Lucent Enterprise service agreement brings your company the assurance of 7x24 no-excuses 
technical support. You’ll also receive regular software updates to maintain and maximize your Alcatel-
Lucent Enterprise product’s features and functionality and on-site hardware replacement through our 
global network of highly qualified service delivery partners. 
With 24-hour access to Alcatel-Lucent Enterprise’s Service and Support web page, you’ll be able to view 
and update any case (open or closed) that you have reported to Alcatel-Lucent Enterprise’s technical 
support, open a new case or access helpful release notes, technical bulletins, and manuals. 
Access additional information on Alcatel-Lucent Enterprise’s Service Programs:
Web: myportal.al-enterprise.com
Phone: 1-800-995-2696

<<<PAGE 12>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
page 1-1
1   OmniSwitch 6900
The OmniSwitch 6900 (OS6900) is a family of aggregation switches that can also be installed as top-of-
rack boxes in data centers. Refer to the information below for model number and
component type.
OS6900 switches provide 1+1 redundant hot-swappable power supplies and a hot-swappable fan tray. 
All models include one RJ45 10/100/1000 EMP port, one console connector, one USB 2.0 high speed 
(480Mbits/sec) connector and support for front-to-rear or rear-to-front chassis airflow.
Model Number
Description
OS6900-V72
Chassis with 48XSFP28 ports and 6X100G QSFP28 ports
OS6900-C32
Chassis with 32X100G QSFP28 ports
OS6900-C32E
Chassis with 32X100G QSFP28 and 2X10G SFP+ ports
OS6900-T48C6
Chassis with 48X10GBaseT ports and 6X100G QSFP28 ports
OS6900-X48C6
Chassis with 48X10G SFP+ ports and 6X100G QSFP28 ports
OS6900-X48C4E
Chassis with 40X10G SFP+, 8X25G SFP28, and 6X100G QSFP28 ports
OS6900-V48C8
Chassis with 48X25G SFP28 ports, 6X100G QSFP28 ports, and 2X10G SFP+ 
ports
OS6900-T24C2
Chassis with 24X10GBaseT, 2XSFP+ and 2XQSFP28 ports.
OS6900-X24C2
Chassis with 26XSFP+ and 2XQSFP28 ports.
OS6920-D32
Chassis with 32X400G QSFP-DD and 1X10G SFP+ ports.

<<<PAGE 13>>>
OmniSwitch 6900 Availability Features
OmniSwitch 6900
page 1-2
OmniSwitch 6900 Hardware Users Guide
December 2025
OmniSwitch 6900 Availability Features
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
• Fan tray
For information on adding and removing power supplies refer to Chapter 3, “Chassis and Power Supplies.”
Hardware Monitoring
Automatic Monitoring
Automatic monitoring refers to the switch’s built-in sensors that automatically monitor operations. If an 
error is detected (e.g., over-threshold temperature), the switch immediately sends a trap to the user. The 
trap is displayed on the console in the form of a text error message.
LEDs
LEDs, which provide visual status information, are provided on the front and rear panels. LEDs are used 
to indicate conditions, such as hardware and software status, link integrity, data flow, etc. For detailed 
LED descriptions, refer to the corresponding hardware component section in the next chapter.
User-Driven Monitoring
User-driven hardware monitoring refers to CLI commands that are entered by the user in order to access 
the current status of hardware components. The user enters “show” commands that output information to 
the console. The Show commands for all the features are described in detail in the OmniSwitch CLI 
Reference Guide.

<<<PAGE 14>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
page 2-1
2   Getting Started
Installing the Hardware
Note. For information on configuring a Virtual Chassis (VC), refer to the OmniSwitch AOS Release 8 
Switch Management Guide.
Items Required
• Grounding wrist strap
• Phillips screwdriver
• Flat-blade screwdriver
Site Preparation
Environmental Requirements
OmniSwitch 6900 switches have the following environmental and airflow requirements:
• The installation site must maintain a temperature between 0° and 45° Celsius (32° and 113° Fahren-
heit) and not exceed 95 percent maximum humidity (non-condensing) at any time.
• The installation site must maintain a temperature between 0° and 35° Celsius (32° and 95° Fahrenheit) 
and not exceed 95 percent maximum humidity (non-condensing) at any time for the OmniSwitch 6920 
with back-to-front airflow.
• Be sure to allow adequate room for proper air ventilation at the front, back, and sides of the switch. 
Refer to “Airflow Considerations” on page 2-4 for minimum clearance requirements. No clearance is 
necessary at the top or bottom of the chassis.
Electrical Requirements
Note. Alcatel-Lucent switches must be installed by a professional installer. It is the responsibility of the 
installer to ensure that proper grounding is available and that the installation meets applicable local and 
national electrical codes.
OmniSwitch 6900 switches have the following general electrical requirements:
• Each switch requires one grounded electrical outlet for each power supply installed in the chassis. 
OmniSwitch 6900 switches offer both AC and DC power supply support.

<<<PAGE 15>>>
Installing the Hardware
Getting Started
page 2-2
OmniSwitch 6900 Hardware Users Guide
December 2025
• For switches using AC power connections, each supplied AC power cord is 2 meters (approx. 6.5 feet). 
Do not use extension cords.
• ALE provided power cords are UL recognized to IEC 62368-1 exceeding the maximum amperage 
requirement for the power source. If using a non-ALE provided power cord the installer shall confirm it 
meets the minimum electrical requirements of the power source.
Redundant AC Power. It is recommended that each AC outlet resides on a separate circuit. With 
redundant AC, if a single circuit fails, the switch’s remaining power supplies (on separate circuits) can 
remain operational.
• For switches using DC power, refer to the “DC Power Supply Connections” on page 3-34 for
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

<<<PAGE 16>>>
Getting Started
Installing the Hardware
OmniSwitch 6900 Hardware Users Guide
December 2025
page 2-3
copper Ethernet cables (especially in new cable runs) to a suitable and safe earth ground before connect-
ing them to the port.
Note. Failure to follow the above recommendations could result in voiding the warranty of the affected 
ALE product. 
Unpacking and Installing the Switch
To protect your switch components from damage, read all unpacking recommendations and instructions 
carefully before beginning.
Unpack your OmniSwitch 6900 chassis as close as possible to the location where it will be installed.
Items Included
Your OmniSwitch 6900 includes the following items:
• OmniSwitch chassis with power supplies, per order
• Blank cover panel
• Rack mount brackets
• Country-specific power cord(s)
• Rubber table-mounting feet
• Attachment screws
• Assorted instructional cards, anti-static bags and additional packaging
Weight Considerations
Depending on model type, an empty OmniSwitch 6900 chassis weighs up to 7.78 kg (17.15 lbs). 
When fully populated with fan tray, power supplies and plug-in modules, the OmniSwitch 6900 can weigh 
up to 10.86 kg (23.95 lbs). (Weights to not include transceivers or cabling.)

<<<PAGE 17>>>
Installing the Hardware
Getting Started
page 2-4
OmniSwitch 6900 Hardware Users Guide
December 2025
Airflow Considerations
To ensure proper airflow, be sure that the switch is placed in a clean, well-ventilated area free of dust and 
debris and provide minimum recommended clearance at the front, back and sides of the switch.
Note. Never obstruct chassis air vents.
Chassis Top View
Note. Clearance is not required at the top and bottom of the chassis.
}
}
Rear. 6 inches minimum 
at rear of chassis.
Front. 6 inches minimum 
at front of chassis.
Sides. 2 inches minimum 
at left and right sides.

<<<PAGE 18>>>
Getting Started
Mounting the Switch
OmniSwitch 6900 Hardware Users Guide
December 2025
page 2-5
Mounting the Switch
For information on mounting OmniSwitch 6900 switches, refer to the Chapter 3, “Chassis and Power 
Supplies.”
Connections and Cabling
Once your switch is properly installed, you should connect all network and management cables required 
for your network applications. Connections may include:
• Ethernet cable to the Ethernet Management Port (EMP)
• Cables to NIs or transceivers
Note. For additional information on cabling refer to the OmniSwitch AOS Release 8 Switch Management 
Guide. 
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
Serial Connection to the Console Port
The console port provides a serial connection to the switch using a USB or RJ45 connector (depending on 
OS6900 model) and is required when logging into the switch for the first time. By default, this connector 
provides a DTE/DCE console connection.
Serial Connection Default Settings
For information on modifying these settings, refer to the OmniSwitch AOS Switch Management Guide.
Ethernet Management Port (EMP) Cable Requirements
The OmniSwitch 6900 provides an Ethernet Management Port (EMP) on the front or rear panel of the 
chassis (depending on OS6900 model) for out-of-band management. There are specific cable type require-
ments (i.e., straight-through or crossover) based on the device to which the EMP is connecting. Refer to 
the information below:
baud rate
115200
parity
none
data bits (word size)
8
stop bits
1
cable type
rollover
EMP to a Switch
Straight-through
EMP to a Computer or 
Workstation 
Crossover

<<<PAGE 19>>>
Connections and Cabling
Getting Started
page 2-6
OmniSwitch 6900 Hardware Users Guide
December 2025
For more on configuring Ethernet ports, refer to the OmniSwitch AOS Network Configuration Guide.

<<<PAGE 20>>>
Getting Started
Booting the Switch
OmniSwitch 6900 Hardware Users Guide
December 2025
page 2-7
Booting the Switch
Now that you have installed the switch components and connected network and management cables, you 
can boot the switch. To boot the switch, plug all power supply cords into easily-accessible, properly 
grounded power outlets. (Do not use extension cords.) The switch will power on and boot automatically.
Note. If you have more than one power supply installed, be sure to plug in each power supply in rapid 
succession, (i.e., within a few seconds of each other). This ensures that there will be adequate power for 
all components throughout the boot process.
Component LEDs
During the boot process, component LEDs will flash and change color, indicating different stages of the 
boot. For detailed information, including correct post-boot LED states, refer to “Chassis Status LEDs” on 
page 3-19.
Once the switch has completely booted and you have accessed your computer’s terminal emulation soft-
ware via the console port, you are ready to log in to the switch’s Command Line Interface (CLI) and 
configure basic information. Continue to “Your First Login Session” on page 2-8.

<<<PAGE 21>>>
Your First Login Session
Getting Started
page 2-8
OmniSwitch 6900 Hardware Users Guide
December 2025
Your First Login Session
In order to complete the setup process for the switch, you must complete the following steps during your 
first login session:
• Log in to the switch
• Set IP address information for the Ethernet Management Port (EMP)
• Unlock session types
• Change the login password
• Set the date and time
• Set optional system information
• Save your changes
Important. You must be connected to the switch via the console port before initiating your first login 
session. For information on Remote Configuration Load (RCL) and connecting via SSH or HTTPS, see 
the OmniSwitch AOS Release 8 Switch Management Guide.
Logging In to the Switch
When you first log in to the switch, you will be prompted for a login name and password. Use the switch’s 
default settings:
• Login: admin
• Password: switch
The default welcome banner, which includes information such as the current software version and system 
date, is displayed followed by the CLI command prompt:
Welcome to the Alcatel-Lucent Enterprise OS6900-V72 8.9.R04, February 16, 2024.
Copyright (c) 1994-2014 Alcatel-Lucent. All Rights Reserved.
Copyright (c) ALE USA Inc., 2014-2024. All Rights Reserved.
OmniSwitch(tm) is a trademark of Alcatel-Lucent,
registered in the United States Patent and Trademark Office.
->
Note. A user account includes a login name, password, and user privileges. Privileges determine whether 
the user has read or write access to the switch and which commands the user is authorized to execute. For 
detailed information on setting up and modifying user accounts, refer to the OmniSwitch AOS Switch 
Management Guide.

<<<PAGE 22>>>
Getting Started
Your First Login Session
OmniSwitch 6900 Hardware Users Guide
December 2025
page 2-9
Setting IP Address Information for the EMP
IP address can be set via the Ethernet Management Port (EMP). To connect to the switch through the EMP 
Ethernet connection, use the default address below or change the port’s IP address.
Note. You should be connected to the switch via the console port before attempting to change IP 
address information. 
To change the default IP and mask, use the ip interface command. For example:
-> ip interface emp address 168.22.2.120 mask 255.255.255.0
Verify your settings using the show ip interface command. See the OmniSwitch AOS Switch Manage-
ment Guide for additional information regarding EMP port addressing. 
Note. Although you have configured the EMP with valid IP address information, you will not be able to 
access the switch through this port (i.e. TELNET, FTP, HTTP, SSH or SNMP) until you have unlocked 
these remote session types. See “Unlocking Session Types” on page 2-10 for more information.
Default EMP IP Address
192.168.1.1
Default EMP Mask
255.255.255.0

<<<PAGE 23>>>
Your First Login Session
Getting Started
page 2-10
OmniSwitch 6900 Hardware Users Guide
December 2025
Unlocking Session Types
Security is a key feature on OmniSwitch 6900 switches. As described on page 2-8, when you access the 
switch for the first time, you must use a direct console port connection. All other session types (Telnet, 
FTP, WebView, and SNMP) are locked out until they are manually unlocked by the user.
The CLI command used to unlock session types is aaa authentication. 
Note. When you unlock session types, you are granting switch access to non-local sessions (e.g., Telnet). 
As a result, users who know the correct user login and password will have remote access to the switch. For 
more information on switch security, refer to the OmniSwitch AOS Switch Management Guide.
Unlocking All Session Types
To unlock all session types, enter the following command syntax at the CLI prompt:
-> aaa authentication default local
Unlocking Specified Session Types
You can also unlock session types on a one-by-one basis. For example, to unlock Telnet sessions only, 
enter the following command:
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
page 2-8). 
2 Enter the keyword password and press Enter.
3 Enter your new password at the prompt.
Note. Be sure to remember or securely record all new passwords; overriding configured passwords on an 
OmniSwitch is restricted.

<<<PAGE 24>>>
Getting Started
Your First Login Session
OmniSwitch 6900 Hardware Users Guide
December 2025
page 2-11
4 You will be prompted to re-enter the password. Enter the password a second time.
New password settings are automatically saved in real time to the local user database; the user is not 
required to enter an additional command in order to save the password information. Also note that new 
password information is retained following a reboot. All subsequent login sessions, including those 
through the console port, will require the new password to access the switch.
For detailed information on managing login information, including user names and passwords, refer to the 
OmniSwitch AOS Switch Management Guide.
Setting the System Time Zone
The switch’s default time zone is UTC. If you require a time zone that is specific to your region, or if you 
need to enable Daylight Savings Time (DST) on the switch, you can configure these settings via the 
system timezone and system daylight-savings-time commands.
For detailed information on configuring a time zone for the switch, refer to the OmniSwitch AOS Switch 
Management Guide.
Setting the Date and Time
Set the current time for the switch by entering system time, followed by the current time in hh:mm:ss. 
To set the current date for the switch, enter system date, followed by the current date in mm/dd/yyyy.
Setting Optional Parameters
Specifying an Administrative Contact
An administrative contact is the person or department in charge of the switch. If a contact is specified, 
users can easily find the appropriate network administrator if they have questions or comments about the 
switch.
To specify an administrative contact, use the system contact command.
Specifying a System Name
The system name is a simple, user-defined text description for the switch. To specify a system name, use 
the system name command.
Specifying the Switch’s Location
It is recommended that you use a physical labeling system for locating and identifying your switch(es). 
Examples include placing a sticker or placard with a unique identifier (e.g., the switch’s default IP 
address) on each chassis.
However, if no labeling system has been implemented or if you need to determine a switch’s location from 
a remote site, entering a system location can be very useful.
To specify a system location, use the system location command.

<<<PAGE 25>>>
Your First Login Session
Getting Started
page 2-12
OmniSwitch 6900 Hardware Users Guide
December 2025
Viewing Your Changes
To view your current changes, enter show system at the CLI prompt.
Saving Your Changes
Once you have configured this basic switch information, save your changes by entering write memory at 
the CLI command prompt.

<<<PAGE 26>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-1
3   Chassis and Power
Supplies
This chapter includes detailed information on the OmniSwitch 6900 chassis, as well as fan tray and power 
supply components. Topics include:
• Technical specifications, page 3-2.
• Switch mounting information, page 3-24.
• Power supplies and power supply redundancy, page 3-34.
• Temperature management, page 3-49.
• Chassis fan tray on page 3-50.
• Monitoring the chassis components via the Command Line Interface (CLI), page 3-49

<<<PAGE 27>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-2
OmniSwitch 6900 Hardware Users Guide
December 2025
OmniSwitch 6900 Chassis

<<<PAGE 28>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-3
OS6900-V72 Front Panel
*Refer to page 3-23 for detailed information on port LED behavior.
OS6900-V72 Rear Panel
Item
Description
A
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
B
Port Status LEDs*
C
System Status LEDs*
D
SFP28 ports 1 through 48 (10G/25G)
E
QSFP28 ports 49 through 54: (4X10G/40G/4X25G/100G)
F
RJ45 10/100/1000 Ethernet Management Port (EMP)
G
Console Port 
H
Reset Button (Used to reboot system)
Note: The OS6900-V72 doesn’t support a mix of 10G and 25G speeds on the 4-port groups of ports 1-48. Ports 
within a port group must all run at either 10G speed or 25G speed. 
- Port Groups (1-4, 5-8, 9-12, 13-16, 17-20, 21-24, 25-28, 29-32, 33-36, 37-40, 41-44, 45-48)
Item
Description
A
Power Supply Bays
B
Fan Trays (6 individual trays)
F
E
C
A
D
B
G
H
B
A
A

<<<PAGE 29>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-4
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-V72 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Chassis Width
43.8 cm (17.26 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
51.5 cm (20.28 inches)
Chassis Weight (fully populated)1
9.7 kg (21.38 lb)
Power Supply Bays
2
Power Consumption
188 W (Idle)
400 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 30>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-5
OS6900-C32 Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
OS6900-C32 Rear Panel
Item
Description
A
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
B
Port Status LEDs*
C
System Status LEDs*
D
QSFP28 ports (Ports 1-32 - 4X10G/40G/4X25G/100G)
E
Console Port 
F
RJ45 10/100/1000 Ethernet Management Port (EMP)
G
Reset Button (Used to reboot system)
Item
Description
A
Power Supply Bays
B
Fan Trays (6 individual trays)
F
E
C
A
D
B
B
G
B
A
A

<<<PAGE 31>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-6
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-C32 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Chassis Width
43.8 cm (17.26 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
51.5 cm (20.28 inches)
Chassis Weight (fully populated)1
9.7 kg (21.38 lb)
Power Supply Bays
2
Power Consumption
145 W (Idle)
543 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 32>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-7
OS6900-C32E Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
OS6900-C32E Rear Panel
Item
Description
A
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
B
Port Status LEDs*
C
System Status LEDs*
D
QSFP28 ports (Ports 1-32 - 4X10G/40G/4X25G/100G)
E
SFP+ ports (Ports 33-34 - 1G/10G) - Not currently functional
F
RJ45 10/100/1000 Ethernet Management Port (EMP)
G
Console Port 
H
Reset Button (Used to reboot system)
Item
Description
A
Power Supply Bays
B
Fan Trays (6 individual trays)
LOC
Diag
Fan
PS1
PS2
Reset
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
Mgmt
Console
SFP+
OS6900-C32E
CLASS 1
LASER
PRODUCT
F E
C
A
D
B
B
G
H
B
A
A

<<<PAGE 33>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-8
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-C32E Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Chassis Width
43.8 cm (17.26 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
51.5 cm (20.28 inches)
Chassis Weight (fully populated)1
9.8 kg (21.60 lb)
Power Supply Bays
6
Power Consumption
175 W (Idle)
510 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 34>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-9
OS6900-T48C6 Front Panel
*Refer to page 3-35 for detailed 
information on port LED behavior.
OS6900-T48C6 Rear Panel
Item
Description
A
10/100/1000 RJ45 Ethernet Management Ports (EMP) 
Note: Only top port is functional.
B
System Status LEDs*
C
Port Status LEDs*
D
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
E
Console Port 
F
1G/10GBaseT ports (Ports 1-48)
G
QSFP28 ports (Ports 49-54 - 40G/100G)
Note: Ports 51 and 54 support splitter functionality.
Note: Mixing Direct-attached cables (DAC) and QSFPs is not supported on ports 52 and 53. If 
both ports are populated they must be of the same type.
Item
Description
A
Power Supply Bays
B
Fan Trays (5 individual trays)
F
E
C
A
D
B
G
B
A
A

<<<PAGE 35>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-10
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-T48C6 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Chassis Width
44.3 cm (17.44 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
47.3 cm (18.62 inches)
Chassis Weight (fully populated)1
10.5 kg (23.15 lb)
Power Supply Bays
2
Power Consumption
139 W (Idle)
315 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 36>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-11
OS6900-X48C6 Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
OS6900-X48C6 Rear Panel
Item
Description
A
10/100/1000 RJ45 Ethernet Management Port (EMP)
Note: Only top port is functional.
B
System Status LEDs*
C
Port Status LEDs*
D
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
E
Console Port
F
1G/10G SFP+ ports (Ports 1- 48)
G
QSFP28 ports (Ports 49-54 - 40G/100G)
Note: Ports 51 and 54 support splitter functionality.
Note: Mixing Direct-attached cables (DAC) and QSFPs is not supported on ports 52 and 53. If 
both ports are populated they must be of the same type.
Item
Description
A
Power Supply Bays
B
Fan Trays (5 individual trays)
F
E
C
A
D
B
G
B
A
A

<<<PAGE 37>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-12
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-X48C6 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Chassis Width
44.3 cm (17.44 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
47.3 cm (18.62 inches) 
Chassis Weight1
9.7 kg (21.38 lb)
Power Supply Bays
2
Power Consumption
114 W (Idle)
392 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 38>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-13
OS6900-X48C4E Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
OS6900-X48C4E Rear Panel
Item
Description
A
10/100/1000 RJ45 Ethernet Management Port (EMP)
B
System Status LEDs*
C
Port Status LEDs*
D
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
E
Console Port
F
SFP+ ports (Ports 1- 40 - 1G/10G)
G
SFP28 ports (Ports 41-48 - 1G/10G/25G)
H
QSFP28 ports (Ports 49-52 - 4X10G/40G/4X25G/100G)
Note: The OS6900-X48C4E doesn’t support a mix of 1G/10G and 25G speeds on the 4-port groups of ports 41-
48. Ports within a port group must all run at either 1G/10G speed or 25G speed. Mixing 1G and 10G speeds 
is supported. 
- Port Group 1 (41,42,43,44)
- Port Group 2 (45,46,47,48)
Item
Description
A
Power Supply Bays
B
Fan Trays (6 individual trays)
F
E
C
A
D
B
G
H
B
A
A

<<<PAGE 39>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-14
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-X48C4E Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Chassis Width
43.8 cm (17.24 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
51.5 cm (20.28 inches)
Chassis Weight1
10.5 kg (23.15 lb)
Power Supply Bays
2
Power Consumption
152 W (Idle)
395 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 40>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-15
OS6900-V48C8 Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
Note: The OS6900-V48C8 doesn’t support a mix of 1G/10G and 25G speeds on the 4-port groups of ports 1-48 
listed below. Ports within a port group must all run at either 1G/10G speed or 25G speed. Mixing 1G and 
10G speeds is supported.
Port Group Numbering Table
Front Panel Ports 1-48 Representation
Item
Description
A
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
B
Port Status LEDs*
C
System Status LEDs*
D
SFP28 (Ports 1-48 - 1G/10G/25G)
E
QSFP28 (Ports 49-56 - 4X10G/40G/4X25G/100G)
F
SFP+ (Ports 57-58 - 1G/10G) - Not currently functional
G
RJ45 10/100/1000 Ethernet Management Port (EMP)
H
Console Port 
Group
1
2
3
4
5
6
Ports
1,2,3,6
4,5,7,9
8,10,11,12
13,14,15,18
16,17,19,21
20,22,23,24
Group
7
8
9
10
11
12
Ports
25,26,27,30
28,29,31,33
32,34,35,36
37,38,39,42
40,41,43,45
44,46,47,48
F
E
C
A
D
B
G
H

<<<PAGE 41>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-16
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-V48C8 Rear Panel
OS6900-V48C8 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Item
Description
A
Power Supply Bays
B
Fan Trays (6 individual trays)
Chassis Width
43.84 cm (17.26 inches)
Chassis Height 
4.34 cm (1.70 inches or 1RU)
Chassis Depth 
53.6 cm (21.10 inches)
Chassis Weight (fully populated)1
10.5 kg (23.15 lb)
Power Supply Bays
2
Power Consumption
226 W (Idle)
532 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
B
A
A

<<<PAGE 42>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-17
OS6900-T24C2 Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
Item
Description
A
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
B
Console Port 
C
RJ45 10/100/1000 Ethernet Management Port (EMP)
D
System Status LEDs* 
E
10GBASE-T (Ports 1-24 - 100M/1G/10G) 
F
SFP+ (Ports 25-26 - 1G/10G)
G
QSFP28 (Ports 27-28 - 4X10G/40G/4X25G/100G)
F
E
C
A
D
B
G

<<<PAGE 43>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-18
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-T24C2 Rear Panel
OS6900-T24C2 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Item
Description
A
Power Supply Bays
B
Fan Trays (5 individual trays)
Chassis Width
43.84 cm (17.42 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
47.3 cm (18.62 inches)
Chassis Weight (fully populated)1
8.3 kg (18.3 lb)
Power Supply Bays
2
Power Consumption
91 W (Idle)
209 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
B
A
A

<<<PAGE 44>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-19
OS6900-X24C2 Front Panel
*Refer to page 3-35 for detailed information on port LED behavior.
Item
Description
A
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
B
Console Port 
C
RJ45 10/100/1000 Ethernet Management Port (EMP)
D
System Status LEDs* 
E
SFP+ (Ports 1-24 - 1G/10G)
F
SFP+ (Ports 25-26 - 1G/10G)
G
QSFP28 (Ports 27-28 - 4X10G/40G/4X25G/100G)
F
E
C
A
D
B
G

<<<PAGE 45>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-20
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-X24C2 Rear Panel
OS6900-X24C2 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Item
Description
A
Power Supply Bays
B
Fan Trays (5 individual trays)
Chassis Width
44.25 cm (17.42 inches)
Chassis Height 
4.4 cm (1.73 inches or 1RU)
Chassis Depth 
47.3 cm (18.62 inches)
Chassis Weight (fully populated)1
8.14 kg (17.95 lb)
Power Supply Bays
2
Power Consumption
75 W (Idle)
197 W (Max)
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
B
A
A

<<<PAGE 46>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-21
OS6920-D32 Front Panel
*Refer to page 3-23 for detailed information on port LED behavior.
Item
Description
A
RJ45 10/100/1000 Ethernet Management Port (EMP)
B
USB Port (For information on using a USB flash drive, refer to the OmniSwitch AOS Release 8 
Switch Management Guide.)
C
Console Port 
D
System Status LEDs* 
E
Reset Button
F
QSFP-DD (Ports 1-32)
- QSFP-DD - 400G, 2X200G, 4X100G
- QSFP56 - 200G, 2X100G
- QSFP28 - 100G, 4X25G
- QSFP+ - 40G, 4X10G
G
SFP+ (Port 33 - 1G/10G) - Not currently functional
F
E
C
A
D
B
G

<<<PAGE 47>>>
OmniSwitch 6900 Chassis
Chassis and Power Supplies
page 3-22
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6920-D32 Rear Panel
OS6920-D32 Chassis Specifications
1 Fully populated weights include fan tray, all installable power supplies and expansion modules. These 
figures do not include transceivers.
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. Due to 
different airflow characteristics, chassis temperatures will vary by model.
Item
Description
A
Power Supply Bays
B
Fan Trays (6 individual trays)
Chassis Width
43.84 cm (17.26 inches)
Chassis Height 
4.31 cm (1.67 inches or 1RU)
Chassis Depth 
59.01 cm (23.23 inches)
Chassis Weight (fully populated)1
8.96 kg (19.75 lb)
Power Supply Bays
2
Power Consumption
1400 W (Max)
Operating Temperature (Tmra) - Front-to-Back Airflow
Operating Temperature (Tmra) - Back-to-Front Airflow
0°C to 45°C (32°F to 113°F)
0°C to 35°C (32°F to 95°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
B
A
A

<<<PAGE 48>>>
Chassis and Power Supplies
OmniSwitch 6900 Chassis
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-23
Chassis Status LEDs
The chassis provides a series of status LEDs offering basic status information for hardware operation and 
port link and activity status.
LED
State
Description
PS1 / PS2
Green
Amber
Off
Operating normally.
Error condition.
Not present.
Diag
Green
Amber
Operating normally.
Self-diagnostic test fault.
Fan
Green
Amber
Operating normally.
Error condition.
LOC
Amber (flashing)
Remote management activated for 
identification purposes.
RJ45/SFP+
Amber 
Green
1G link
10G link
SFP28 Ports
Green
Amber
25G link
10G link
1G link
QSFP28 Ports 
(V72/C32/C32E)
LED 1 - Blue
LED 1 - Amber
LEDs 1 - 4 White
LEDs 1 - 4 Green
100G
40G
4X25G
4X10G
QSFP28 Ports
LED 1 - Green
LED 1 - Blue
LEDs 1 - 4 Amber
LEDs 1 - 4 Purple
100G
40G
4X25G
4X10G
QSFP-DD
LED1 - Cyan
LED1 - Purple
LED1 - Blue
LED1 - Orange
LED1 - Purple/LED3 - Green 
LED1 - Blue/LED3 - Green 
LED1 - Yellow/LED3 - Green 
LED1 - Blue/LED2-4 - Green 
LED1 - Yellow/LED2-4 - Green 
LED1 - White/LED2-4 - Green 
LED1-4 - Green
LED1 - Red/LED2-4 - Off
1 X 400G
1 X 200G
1 X 100G
1 X 40G
2 X 200G
2 X 100G
2 X 50G
4 X 100G
4 X 50G
4 X 25G
4 X 10G
Port failure

<<<PAGE 49>>>
Mounting the Switch
Chassis and Power Supplies
page 3-24
OmniSwitch 6900 Hardware Users Guide
December 2025
Mounting the Switch
General Mounting Recommendations
Elevated Operating Ambient Temperature. If installed in a closed or multi-rack assembly, the operating 
ambient temperature of the rack environment may be greater than the room’s ambient temperature. 
Therefore, consideration should be given to the maximum rated ambient temperature (Tmra) given for the 
individual chassis specifications. 
Reduced Air Flow. Installation of the equipment in a rack should be such that the amount of air flow 
required for safe operation of the equipment is not compromised. Refer to “Airflow Recommendations” on 
page 3-25 for more information.
Mechanical Loading. Mounting of the equipment in the rack should be such that a hazardous condition is 
not achieved due to uneven loading.
Circuit Overloading. Consideration should be give to the connection of the equipment to the supply 
circuit and the effect that overloading of circuits could have on overcurrent protection and supply wiring. 
Reliable Earthing. Reliable earthing of rack-mounted equipment should be maintained. Particular 
attention should be given to supply connections other than direct connections to the branch (e.g., use of 
power strips).

<<<PAGE 50>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-25
Airflow Recommendations
To ensure proper airflow, be sure that your switch is placed in a well-ventilated area and provide 
minimum recommended clearance at the front, back and sides of the switch, as shown below. Restricted 
airflow can cause your switch to overheat, which can lead to switch failure. Refer to the following 
important guidelines regarding airflow: 
• The switch supports both Front-to-Rear and Rear-to-Front airflow depending on the fan tray and power 
supplies installed. The airflow direction of the power supplies and fan tray must be the same. 
• Running a mismatched fan tray or power supply will cause an error and trap to be displayed. 
Eventually the mismatched configuration will cause the chassis to reboot to avoid overheating.
• Follow the guidelines below regarding the minimum clearance requirements when mounting
the chassis.
Chassis Top View
Note. Clearance is not required at the top and bottom of the chassis.
}
}
Rear. 6 inches minimum 
at rear of chassis.
Front. 6 inches minimum 
at front of chassis.
Sides. 2 inches minimum 
at left and right sides.

<<<PAGE 51>>>
Mounting the Switch
Chassis and Power Supplies
page 3-26
OmniSwitch 6900 Hardware Users Guide
December 2025
Front-to-Rear Airflow
The OmniSwitch 6900 fan tray and power supplies are located at the rear of the switch and draw air 
through the intake vents located at the top-front of the chassis. The air is directed straight through the 
chassis’ module compartment and past the switch’s circuit boards. Airflow is then exhausted through
their vents.
Chassis Airflow - Front to Rear
Rear-to-Front Airflow
The OmniSwitch 6900 fan tray and power supplies are located at the rear of the switch and draw air 
through their vents located at the rear of the chassis. The air is directed straight through the chassis’ 
module compartment and past the switch’s circuit boards. Airflow is then exhausted through the air vents 
on the top-front of the chassis.
Chassis Airflow - Rear-to-Front

<<<PAGE 52>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-27
Airflow Mismatch
If an airflow mismatch is detected at bootup, OK and PS LEDs blink green/amber and the GRN LED 
blinks green (see “Chassis Status LEDs” on page 3-23), warnings display, and the switch continuously 
reboots until the issue is corrected. 
If an airflow mismatch is detected after the switch has fully booted (e.g., when a fan tray or power supply 
is hot-inserted) OK and PS LEDs blink amber and the GRN LED blinks green (see “Chassis Status LEDs” 
on page 3-23, warnings displayed, switch will reboot when it reaches temperature danger threshold. 
Color Coding
To help users avoid mismatched fan trays and power supplies, rear-to-front components are marked with 
purple color coding. (Front-to-rear components use standard product colors.)

<<<PAGE 53>>>
Mounting the Switch
Chassis and Power Supplies
page 3-28
OmniSwitch 6900 Hardware Users Guide
December 2025
Blank Cover Panels
Blank cover panels are provided with your switch and are used to cover empty slots. These cover panels 
play an important role in chassis airflow and temperature management. If your switch is not fully 
populated and blank cover panels are not installed over empty slot locations, airflow is affected. 
When blank cover panels are missing, air does not take the direct route from the air intake vents, through 
the chassis module compartment, and out through the fan’s exhaust vent as intended. Instead, a portion of 
the airflow is allowed to escape through other openings in the chassis. As a result, normal airflow is 
disrupted and an extra task is placed on the fan tray to cool the chassis.
Cover panels also provide protection for module processor boards and other sensitive internal switch 
components by closing off a chassis that is not fully populated.
Note. Because they regulate airflow and help protect internal chassis components, blank cover panels 
should be installed over empty module slots and power supply bays at all times.
Blank Panels and Chassis Airflow

<<<PAGE 54>>>
Chassis and Power Supplies
Rack-Mounting
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-29
Rack-Mounting
Refer to the following important guidelines before installing the chassis in a rack:
• Two people are required to rack mount the switch: One person to lift the chassis into position and one 
person to secure the chassis to the rack using the rack mount screws.
• The chassis has rack-mount flanges that support standard 19-inch rack mount installations.
• Alcatel-Lucent does not provide rack-mount screws. Use the screws supplied by the rack vendor.
• To prevent a rack from becoming top heavy, it is recommended that you install the switch at the 
bottom of the rack whenever possible.
• If you are installing the switch in a relay rack, be sure to install and secure the rack per rack 
manufacturer’s specifications.
To rack mount the switch, follow the steps below.
Note. Because of the overall chassis depth, additional support braces are used to support the rear of the 
chassis and prevent sagging in the rack. These braces are required for all rack-mount installations.
1 Mark the holes on the rack where the chassis is to be installed.
2 Attach two slot rails to the left and right side of the chassis.
OS6900
OS6920

<<<PAGE 55>>>
Rack-Mounting
Chassis and Power Supplies
page 3-30
OmniSwitch 6900 Hardware Users Guide
December 2025
3 One person should lift and position the chassis until the rack-mount flanges are flush with the 
rack post.
4 Align the holes in the flanges with the rack holes marked in step 1.
5 Once the holes are aligned, the second person should insert a screw through the bottom hole on each 
flange. Tighten both screws until they are secure.
6 From the back of the chassis and with the flanges facing out, insert the slide-in braces into the slot rails 
until they meet the rack posts.
7 The chassis installation should be level. Be sure that the holes and flanges of the slide-in brace are 
aligned with the corresponding holes at the front of the rack.
8 Once the flanges are aligned, install the remaining screws in all four flanges. Be sure that all screws are 
securely tightened.
Note. Never rack mount OS6900 switches using only the front-installed rack mount flanges. Due to the 
chassis overall depth, OS6900 switches must be mounted using additional support braces (available from 
Chassis Front
Chassis Rear

<<<PAGE 56>>>
Chassis and Power Supplies
Rack-Mounting
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-31
Alcatel-Lucent) or by attaching flanges to the mid portion of the chassis (using the threaded holes 
provided). Failure to properly mount the switch may result in the chassis sagging in the rack or damage to 
the switch and its components. Refer to the following sections for more information.
Mid-Mounting the Chassis In the Rack
The switch may also be installed in the rack using mid-mount flanges. To mid-mount the switch in a rack, 
follow the steps below.
1 If needed, remove the mounting flanges from the front of the chassis and the slot rails from the side of 
the chassis by unscrewing the attachment screws.
2 Reinstall the mounting flanges at the mid point of the chassis using the threaded holes, as shown in the 
diagram below.
3 Mark the holes on the rack where the chassis is to be installed.
4 One person should lift and position the chassis until the mid-mount flanges are flush with the rack post.
5 Align the holes in the flanges with the rack holes marked in step 3.

<<<PAGE 57>>>
Rack-Mounting
Chassis and Power Supplies
page 3-32
OmniSwitch 6900 Hardware Users Guide
December 2025
6 Once the holes are aligned, the second person should insert a screw through the bottom hole on each 
flange. Tighten both screws until they are secure.
7 Once the flanges are aligned, install the remaining screws. Be sure that all screws are securely 
tightened.

<<<PAGE 58>>>
Chassis and Power Supplies
Rack-Mounting
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-33
Rack Mounting
Rack Mounting
Standalone (Non-Rack Mounted) Installations
The chassis can also be placed unmounted on a stable, flat surface as a standalone unit. Be sure that the 
surface can accommodate the full, populated weight of all switches being installed. 
Weight Considerations
Depending on model type, an empty OmniSwitch 6900 chassis weighs up to 7.78 kg (17.15 lbs). 
When fully populated with fan tray, power supplies and plug-in modules, the OmniSwitch 6900 can weigh 
up to 10.86 kg (23.95 lbs). (Weights do not include transceivers or cabling.)
Proper Clearance
For a standalone unit, be sure that adequate clearance has been provided for chassis airflow and that you 
have placed the chassis within reach of all required AC outlets. For recommended airflow allowances, 
refer to page 3-25.
Note. Chassis must be placed “right side up.” Never attempt to operate a switch while it is placed on its 
top or side.
Rear Bracket (6 screws)
Rear Bracket Ear and Lock 
Screw
Front Bracket (4 screws)
Rack Mounted Chassis Depth
29.71 in.

<<<PAGE 59>>>
Power Supplies
Chassis and Power Supplies
page 3-34
OmniSwitch 6900 Hardware Users Guide
December 2025
Power Supplies
OmniSwitch 6900 power supplies are located at the rear of the switch chassis. Two slots are provided. If a 
second power supply is installed, it will assume a standby role. 
Please note that the OS6900 does not provide an on/off switch. Connecting an installed power supply to a 
power source will boot the switch. Likewise, disconnecting all installed power supplies from a power 
source will power off the switch.
Airflow Direction
Power supplies are available in front-to-rear airflow or rear-to-front airflow models. Fan trays are also 
direction-specific (front-to-rear or rear-to-front). When installing power supplies, they must match the 
airflow direction of the fan tray. (See “Airflow Mismatch” on page 3-27 for more information.)

<<<PAGE 60>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-35
OS6900-V72/C32/C32E/X48C4E/V48C8 AC Power Supply
AC Power Supply Front Panel
AC Power Supply LED States
Model
OS6900C-BP-F (OS6900V-PS-A-F), Front-to-Rear
OS6900C-BP-R (OS6900V-PS-A-R), Rear-to-Front
Product Compatibility
OS6900-V72, OS6900-C32, OS6900-C32E, OS6900-X48C4E, 
OS6900-V48C8
Total DC Output
650 Watts
AC Input
100–240VAC, 50-60Hz, 10–5A or 8.2-3.5A or 7.8-
3.8A
DC Output
5VSB @ 4A, 12VDC @ 52.9A 
Airflow
This power supply is available in either a front-to-rear or 
rear-to-front model. 
Notes:
Do not mix OS6900-V72/C32/C32E/X48C4E/V48C8 power 
supplies with OS6900-T48C6/X48C6/T24C2/X24C2 power 
supplies. Mixing an AC and DC power supply in the same 
chassis is supported.
LED State
Description
Solid Green
The power supply is operating normally and providing power to the 
chassis
Solid Red
Power supply failure
Off
No AC power.
Status LED
AC Connector
Handle
Air Vent
Lock Tab
AC Power Cord

<<<PAGE 61>>>
Power Supplies
Chassis and Power Supplies
page 3-36
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-T48C6/X48C6/T24C2/X24C2 AC Power Supply
AC Power Supply
AC Power Supply LED States
Model
OS6900X-BP-F (OS6900-T48C6/OS6900-X48C6-PS-A-F), 
Front-to-Rear
OS6900X-BP-R (OS6900-T48C6/OS6900-X48C6-PS-A-R), 
Rear-to-Front
Product Compatibility
OS6900-T48C6, OS6900-X48C6, OS6900-T24C2, OS6900-
X24C2
Total DC Output
400 Watts
AC Input
100–240VAC, 50-60Hz, 6–3A
DC Output
12VDC @ 33.34A
Airflow
This power supply is available in either a front-to-rear or 
rear-to-front model. 
Notes:
Do not mix OS6900-T48C6/X48C6/T24C2/X24C2 power sup-
plies with OS6900-V72/C32/C32E/X48C4E/V48C8 power 
supplies. Mixing an AC and DC power supply in the same 
chassis is supported.
LED State
Description
Solid Green
The power supply is operating normally and providing power to the 
chassis
Solid Red
Power supply failure
Off
No AC power.
Status LED
AC Connector
Handle
Air Vent
Lock Tab
AC Power Cord

<<<PAGE 62>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-37
OS6900-V72/C32/C32E/X48C4E/V48C8 DC Power Supply
DC Power Supply Front Panel
DC Power Supply LED States
Model
OS6900C-BPD-F (OS6900V-PS-D-F), Front-to-Rear
OS6900C-BPD-R (OS6900V-PS-D-R), Rear-to-Front
Product Compatibility
OS6900-V72, OS6900-C32, OS6900-C32E, OS6900-X48C4E, 
OS6900-V48C8
Power Rating
48 VDC, 650 Watts
DC Input
36-72 VDC, 25-11A
DC Output
5 VDC @ 4 A, 12 VDC @ 52.9 A
Airflow
This power supply is available in either a front-to-rear or 
rear-to-front model. 
Note
Do not mix OS6900-V72/C32/X48C4E/V48C8 power supplies 
with OS6900-T48C6/X48C6/T24C2/X24C2 power supplies. 
Mixing an AC and DC power supply in the same chassis is sup-
ported.
LED State
Description
Solid Green
The power supply is operating normally and providing power to the 
chassis
Solid Red
Power supply failure
Off
No DC power.
Status LED
DC Connector
Handle
Air Vent
Lock Tab
DC Power Cord

<<<PAGE 63>>>
Power Supplies
Chassis and Power Supplies
page 3-38
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6900-T48C6/X48C6/T24C2/X24C2 DC Power Supply
DC Power Supply Front Panel
DC Power Supply LED States
DC Power Supply Cord (IEC 60945)
This cable is required for the OS6900-X48C6 when used with the OS6900X-BPD-F power supply in 
installations that require IEC 60945 certification. 
OS-DNV-DC-PWR - IEC 60945 Certified Cable (Two Ferrite Cores)
Model
OS6900X-BPD-F (OS6900-T48C6/OS6900-X48C6-PS-D-F), Front-
to-Rear
OS6900X-BPD-R (OS6900-T48C6/OS6900-X48C6-PS-D-R), Rear-
to-Front
Product Compatibility
OS6900-T48C6, OS6900-X48C6, OS6900-T24C2, OS6900-X24C2
Total DC Output
200/400 Watts
DC Input
-20 - -75 VDC, 14-4A (200W Output)
-36 - -75 VDC, 14-7A, (400W Output)
DC Output
12V/16A, 5V/3A (200W)
12V/33.3A, 5V/3A (400W)
Airflow
This power supply is available in either a front-to-rear or 
rear-to-front model. 
Note
Do not mix OS6900-T48C6/X48C6/T24C2/X24C2 power supplies 
with OS6900-V72/C32/X48C4E/V48C8 power supplies. Mixing an 
AC and DC power supply in the same chassis is supported.
LED State
Description
Solid Green
The power supply is operating normally and providing power to the chassis
Solid Red
Power supply failure
Off
No DC power.
Status LED
DC Connector
Handle
Air Vent
Lock Tab
DC Power Cord

<<<PAGE 64>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-39
OS6920 AC Power Supply
AC Power Supply Front Panel
AC Power Supply LED States
Model
OS6920-BP-F, Front-to-Rear
OS6920-BP-R, Rear-to-Front
Product Compatibility
OS6920-D32
Total DC Output
1500 Watts
AC Input
100–127V, 50-60Hz, 12A
220-240V, 50-60Hz, 8A
DC Output
+12V, 83.33A (Input 100-127V)
+12V, 125A (Input 220-240V) 
+5VSB, 5A 
Airflow
This power supply is available in either a front-to-rear or 
rear-to-front model. 
Notes:
Mixing an AC and DC power supply in the same chassis is sup-
ported. The system hold time for this power supply at 100% 
load is less than 20ms.
LED State
Description
Solid Green
The power supply is operating normally and providing power to the 
chassis
Solid Red
Power supply failure
Off
No AC power.
Status LED
AC Connector
Handle
Air Vent
Lock Tab
AC Power Cord

<<<PAGE 65>>>
Power Supplies
Chassis and Power Supplies
page 3-40
OmniSwitch 6900 Hardware Users Guide
December 2025
OS6920 DC Power Supply
DC Power Supply Front Panel
DC Power Supply LED States
Model
OS6920-BPD-F, Front-to-Rear
OS6920-BPD-R, Rear-to-Front
Product Compatibility
OS6920-D32
Total DC Output
1600 Watts
DC Input
-40V - -75 V, 50A
DC Output
+12V, 133.33A
+5VSB, 5A
Airflow
This power supply is available in either a front-to-rear or 
rear-to-front model. 
Note
Mixing an AC and DC power supply in the same chassis is sup-
ported.
LED State
Description
Solid Green
The power supply is operating normally and providing power to the 
chassis
Solid Red
Power supply failure
Off
No DC power.
Status LED
DC Terminals
Handle
Air Vent
Lock Tab
Ground 
Terminal

<<<PAGE 66>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-41
DC Power Supply Connections
Connecting a DC Cable Harness to the Chassis Power Supply
When plugging in the cable, insert the connector end of the cable harness into the power supply connector 
until it clicks firmly into place. This is an indication that the connector is secure and properly seated.
Connecting a DC Cable Harness to the DC Power Source
Safety Guidelines
Before connecting the DC cable to a power source, be sure to follow these important guidelines:
• Review all manufacturer specifications and requirements for DC power supplies and cables 
before connecting. 
• Connect to a reliably ground -40 to -75 VDC Selv source.
• The branch circuit overcurrent protection must be rated 50A.
• Use 6AWG copper conductors.
• A readily accessible disconnect device that is suitably approved and rated shall be incorporated in the 
field wiring.
• The power source must be installed in a restricted access location.
Primary Ground Information
The product has been designed to be installed in a Common Bonding Network (CBN). The pin of the 
Green/Yellow ground lead in the three pin cable connector is connected to the ground connector on the 
DC power supply, which is identified by a Grounding symbol. The Green/Yellow lead wire at the other 
end of the cable must be connected to a proper earth ground point. 
The rear chassis has two ground holes. To properly ground the equipment, connect a Panduit Corporation 
UL listed Lug, (Part number LCD8-10A-L) to the two threaded holes located at the rear, insert two 10-32, 
3/8” threaded pan head screws into these ground holes, and connect them to a proper earth ground point, 
using protective earthing conductor wire and 8AWG copper conductors. Torque to between 30-60 inch 
pounds.
Connection Details
Connect the power supply using the supplied DC cable. The cable consists of three 12AWG wires 
(Green/Yellow, Black, Red). 
One end of the cable has a three pin connector in a plastic housing that is inserted into a three pin input 
connector on the power supply. The other end of the cable is connected to a fuse panel or other source of 
-48VDC power.
Observe proper polarity when connecting to a fuse panel. The cable wire leads must be connected as 
follows:
• Green/yellow - ground
• Black - return
• Red - -48VDC

<<<PAGE 67>>>
Power Supplies
Chassis and Power Supplies
page 3-42
OmniSwitch 6900 Hardware Users Guide
December 2025
Note. The battery return conductor is an Isolated DC Return (DC-1).
Connecting Ring Terminals to OmniSwitch 6920 DC Power Supply
The OS6920-PS-D-F/R power supplies do not ship with a power cable. Use the specifications below for 
connecting the ring terminals to the power supply power and ground terminals.
Installing Power Supplies
1 Orient the power supply so that the power cord socket is situated at the right of the power supply. Also, 
for the power supply to seat properly, make sure that the handle is in the vertical position as show. (Note: 
The location and size of the lock tab may differ depending on the power supply model.)
2 Slide the power supply back until it is securely seated in the chassis backplane.When the connector is 
fully seated, the lock tab will click and hold the power supply in place.
3 Plug the power cord (provided) into the power supply’s socket.
AWG
Dimensions
d2
W
F
L
E
D
d1
T
Power 
Ring 
Terminals
8
4.3mm 
(0.169 in)
8mm 
(0.315 in)
9.3mm 
(0.366 in)
30mm 
(1.181 in)
16.7mm 
(0.657 in)
8.5mm 
(0.335 in)
4.5mm 
(0.177 in)
1.2mm 
(0.047 in)
Ground 
Ring 
Terminal
6
6.4mm 
(0.252 in)
12mm 
(0.472 in)
13.3mm 
(0.524 in)
41.8mm 
(1.646 in)
22.5mm 
(0.886 in)
10.5mm 
(0.413 in)
5.8mm 
(0.228 in)
1.5mm 
(0.059 in)
Power Ring Terminal
Ground Ring Terminal

<<<PAGE 68>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-43
OS6900 Power Supply Install (X48C6/T48C6 shown)
Note. The chassis does not provide an on/off switch. Connecting a the power supplies to a power source 
will boot the switch.
1. Insert power supply.
2. Properly seat power supply, locking tab will click.
3. Plug the power cord into power supply socket.

<<<PAGE 69>>>
Power Supplies
Chassis and Power Supplies
page 3-44
OmniSwitch 6900 Hardware Users Guide
December 2025
Removing Power Supplies
1 When removing a power supply, first disconnect the power cord from the power source. Once the 
power cord is disconnected, pull the power cord out of the power supply housing. 
2 Pressing the lock tab will free the power supply from the chassis. While pressing the lock tab, pull the 
power supply straight back and out of the chassis slot.
OS6900 Power Supply Removal (X48C6/T48C6 shown)
Note. If you are not replacing the power supply, be sure to install a blank cover panel over the empty 
power supply bay.
1. Remove power cord.
2. Press the lock tab and remove power supply.
3. Install replacement power supply.

<<<PAGE 70>>>
Chassis and Power Supplies
Chassis Fan Tray
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-45
Chassis Fan Tray
The OmniSwitch 6900 chassis houses multiple fan trays. The fans are the main temperature control 
components for the switch, providing cooling airflow for all chassis components. This airflow is a crucial 
factor in the switch’s overall operability. Refer to “Airflow Recommendations” on page 3-25 for more 
information.
Important. The fan tray is a required component. Never attempt to operate the switch without a fan 
tray installed
Airflow Direction
The fan tray is available in front-to-rear airflow or rear-to-front airflow models. Power supplies are also 
direction-specific (front-to-rear or rear-to-front). When installing a fan tray in the chassis, it must match 
the airflow direction of the power supplies. (See “Airflow Mismatch” on page 3-27 for more information.) 
 
OmniSwitch 6900 Fan (OS6900V-FT-F/R shown)
Model
OS6900V-FT-F, Front-to-Rear
OS6900V-FT-R, Rear-to-Front
Product Compatibility
OmniSwitch 6900-V72/C32/C32E/X48C4E
Model
OS6900-T48C6/OS6900-X48C6-FT-F, Front-to-Rear
OS6900-T48C6/OS6900-X48C6-FT-R, Rear-to-Front
(Thumb screw in upper right, image not shown)
Product Compatibility
OmniSwitch 6900-T48C6/X48C6/T24C2/X24C2
Model
 OS6900-V48C8-FT-F, Front-to-Rear
 OS6900-V48C8-FT-R, Rear-to-Front
Product Compatibility
OmniSwitch 6900-V48C8
Model
OS6920-FT-F, Front-to-Rear
OS6920-FT-R, Rear-to-Front

<<<PAGE 71>>>
Chassis Fan Tray
Chassis and Power Supplies
page 3-46
OmniSwitch 6900 Hardware Users Guide
December 2025
Product Compatibility
OmniSwitch 6920-D32
Airflow
Fans are available in either a front-to-rear or 
rear-to-front model. 
Note:
Do not attempt to install incompatible fan models in a chassis.

<<<PAGE 72>>>
Chassis and Power Supplies
Replacing the Fan Tray
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-47
Replacing the Fan Tray
1 Begin by loosening the captive screw. 
2 Pull the fan tray straight out of the chassis.
3 Insert the tray into the chassis slot and slide it straight back until it meets the chassis backplane connec-
tors.
4 When the fan tray is firmly seated in the chassis, tighten the two captive screws at the left and right 
sides of the fan tray’s front panel.
OS6900 Fan Tray Replacement- (V72/C32/C32E/X48C4E/V48C8 shown)
Important. The switch should not run without a fan tray more than 60 seconds to prevent over heating
1. Loosen the captive screw. 
2. Remove fan tray.
3. Install new fan tray and tighten captive screw.

<<<PAGE 73>>>
Grounding the Chassis
Chassis and Power Supplies
page 3-48
OmniSwitch 6900 Hardware Users Guide
December 2025
Grounding the Chassis
The switch has a grounding lug located on the rear of the chassis. This lug uses 10-32 screws and is 
surrounded by a small paint-free area, which provides metal-to-metal contact for a ground connection.
Use this connector to supplement the ground provided by the AC power cord. To do so, install a Panduit 
Grounding Lug (type LCD8-10A-L) using 8AWG copper conductors to the paint-free area. Torque to 
between 30-60 inch pounds
Refer to the rear chassis views on page 3-2 for location details.

<<<PAGE 74>>>
Chassis and Power Supplies
Monitoring Chassis Components
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-49
Monitoring Chassis Components
Viewing Chassis Slot Information
To view basic slot information, enter the show module command at the CLI prompt:
-> show module
To view more detailed information, use the show module long command:
-> show module long
Monitoring Chassis Temperature
The operating temperature of your switch is a critical factor in its overall operability. In order to avoid a 
temperature-related system failure, your switch must always run at a temperature within the specified 
operating temperature range. Refer to the chassis specifications section for additional information.
To avoid chassis over-temperature conditions, follow the important chassis airflow recommendations
on page 3-25.
To check the switch’s current temperature status, use the show temperature command:
-> show temperature
For more information about this command, see the “Chassis Management and Monitoring Commands” 
chapter in the OmniSwitch AOS Release 8 CLI Reference Guide

<<<PAGE 75>>>
Monitoring Chassis Temperature
Chassis and Power Supplies
page 3-50
OmniSwitch 6900 Hardware Users Guide
December 2025
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
• Checking the fan tray status using the show fan command. See page page 3-50 for more information. 
Note. For the OS6900’s default warning threshold value, refer to the specifications on page 3-2. The 
warning threshold may be viewed using the show temperature command.
Temperature Danger Threshold
If the chassis temperature rises above the danger threshold (see specifications on page 3-2) the switch will 
power off until the temperature conditions have been addressed and the switch is manually booted. The 
danger threshold is factory-set and cannot be configured by the user.
Addressing danger threshold temperature conditions may include:
• Checking for a chassis airflow obstruction or direction mismatch.
• Checking the ambient room temperature
• Checking the fan tray status using the show fan command. See page page 3-50 for more information.
Monitoring Fan Tray Status
The switch constantly monitors fan operation. If any of the switch’s fans unexpectedly shuts down, the 
switch sends out a trap and the FAN LED on the chassis front panel displays amber.
To check the switch’s current fan tray status, use the show fan command. For example:
-> show fan
For more information about this command, see the “Chassis Management and Monitoring Commands” 
chapter in the OmniSwitch CLI Reference Guide.

<<<PAGE 76>>>
Chassis and Power Supplies
Pinouts
OmniSwitch 6900 Hardware Users Guide
December 2025
page 3-51
Pinouts
OmniSwitch 6900 RS-232 console ports use either an RJ-45 connector or a USB connector. (Refer to 
diagrams below.) Three signals are used: Transmit Data (TXD), Receive Data (RXD) and Signal 
Ground (GND).
Note. No hardware handshaking (RTS, CTS) is used. Instead, software flow control (XON, XOFF) is 
required, where XON is equal to ready and XOFF is equal to not ready.
RJ45 Console Port Connector Pinout
USB Console Port Connector (All Other Models)
TXD
The data sent out from the console port to the receiving device.
RXD
The data received by the console port from the sending device.
GND
The common return for all signals on the interface.
OS6900 Console
Pin
RTS
1
Not Connected
2
TXD
3
GND
4
GND
5
RXD
6
Not Connected
7
CTS
8
RS-232 Signal
USB Type A Pin
Not Connected
1
RXD
2
TXD
3
GND
4

<<<PAGE 77>>>
Pinouts
Chassis and Power Supplies
page 3-52
OmniSwitch 6900 Hardware Users Guide
December 2025
RJ-45 Console Port – Connector Pinout
10/100 Ethernet Port – RJ-45 Pinout
Gigabit Ethernet Port – RJ-45 Pinout
Pin Number
Signals as DTE Console Port
1
NC
2
NC
3
RXD
4
Ground
5
Ground
6
TXD
7
NC
8
NC
Pin Number
Description
1
TX+
2
TX-
3
RX+
4
not used
5
not used
6
RX-
7
not used
8
not used
Pin Number
Description
1
BI_DA+
2
BI_DA-
3
BI_DB+
4
BI_DC+
5
BI_DC-
6
BI_DB-
7
BI_DD+
8
BI_DD-

<<<PAGE 78>>>
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-1
A  Regulatory Compliance
and Safety Information
This appendix provides information on regulatory agency compliance and safety for OmniSwitch 6900 
switches.
Declaration of Conformity: CE Mark
This equipment is in compliance with the essential requirements and other provisions of 
Directive 2004/108/EC (EMC), 2006/95/EC (LVD), 91/263/EEC (Telecom Terminal Equipment, 
if applicable), 1999/5/EC (R&TTE, if applicable). 
Français: Cet équipement est conforme aux exigences essentielles et aux autres provisions de la Directive 
2004/108/EC (EMC), 2006/95/CE (LVD), 91/263/CEE (équipements terminaux de télécommunications, le 
cas échéant), 1999/5/EC (R&TTE, le cas échéant). 
Deutsch: Diese Ausrüstung erfüllt die wesentlichen Anforderungen und sonstigen Bestimmungen der 
Richtlinien 2004/108/EG (EMV-Richtlinie), 2006/95/EG (Niederspannungsrichtlinie), 91/263/EWG 
(Telekommunikationsendeinrichtungen, falls zutreffend), 1999/5/EG (Funkanlagen und Telekommunika-
tionsendeinrichtungen, falls zutreffend). 
Español: Este equipo cumple los requisitos esenciales y otras disposiciones de las directivas 2004/108/CE 
(EMC), 2006/95/CE (LVD), 91/263/CEE (equipos terminales de telecomunicación, si procede), 1999/5/
CE (R&TTE, si procede). 
Waste Electrical and Electronic Equipment (WEEE) Statement
The product at end of life is subject to separate collection and treatment in the EU Member States, Norway 
and Switzerland and therefore marked with the following symbol:
Treatment applied at end of life of the product in these countries shall comply with the applicable national 
laws implementing directive 2002/96/EC on waste electrical and electronic equipment (WEEE).

<<<PAGE 79>>>
Declaration of Conformity: CE Mark
Regulatory Compliance and Safety Information
page A-2
OmniSwitch 6900 Hardware Users Guide
December 2025
China RoHS: Hazardous Substance Table

<<<PAGE 80>>>
Regulatory Compliance and Safety Information
Declaration of Conformity: CE Mark
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-3
Taiwan RoHS: Hazardous Substance Table
California Proposition 65 Warning
WARNING: This product can expose you to chemicals including Pb and Pb compounds, which is known 
to the State of California to cause cancer and birth defects or other reproductive harm. For more 
information go to www.P65Warnings.ca.gov.
Products are packaged using one or more of the following packaging materials:
UN3091 - Lithium Metal Batteries Contained In Equipment. 
Do not discard in household trash or standard recycling bins. Consult with local or national hazardous 
waste agencies or authorities for specific regulations and guidance on UN3091 disposal in your area. 
There is danger of explosion if the Lithium battery in your chassis is incorrectly replaced. Replace the 
Corrugated Cardboard                Corrugated Fiberboard              Low-Density Polyethylene
CB
FB

<<<PAGE 81>>>
Declaration of Conformity: CE Mark
Regulatory Compliance and Safety Information
page A-4
OmniSwitch 6900 Hardware Users Guide
December 2025
battery only with the same or equivalent type of battery (CR1220) recommended by the manufacturer. 
(Applicable to the OS6900-X48C6/T48C6/X48C4E/V48C8).

<<<PAGE 82>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-5
Standards Compliance
The product bears the CE mark. In addition it is in compliance with the following other safety and 
EMC standards:
All hardware switching modules used in an OmniSwitch 6900 switch comply with Class A standards. 
Modules with copper connectors meet Class A requirements using unshielded (UTP) cables.
Safety Standards
• UL 60950-1, 2nd Edition
• CAN/CSA-C22.2 No. 60950-1-07, 2nd Edition
• EN 60950-1 with Amendment II
• IEC 60950-1 2nd Edition
• AS/NZS TS-001 and 60950: Australia
• UL-AR, Argentina
• TUV,UL-GS Mark, Germany
• NOM-019 SCFI, Mexico
• EN 60825-1 Laser
• EN 60825-2 Laser
• CDRH Laser
• CB Certification per IEC 60950-1, Second Edition)
EMC Standards
• FCC Part 15 (CFR 47) Class A
• ICES-003 Class A
• EN 55022: Class A
• CISPR 22 Class A
• AS/NZS 3548 Class A
• VCCI Class A; A1 and A2
• EN 55024: (Immunity)
• EN 61000-3-2
• EN 61000-3-3
• EN 61000-4-2
• EN 61000-4-3
• EN 61000-4-4
• EN 61000-4-5
• EN 61000-4-6
• EN 61000-4-8
• EN 61000-4-11

<<<PAGE 83>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-6
OmniSwitch 6900 Hardware Users Guide
December 2025
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

<<<PAGE 84>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-7
CISPR22 Class A warning
This is a Class A product. In a domestic environment, this product may cause radio interference. Under 
such circumstances, the user may be requested to take appropriate countermeasures.
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
A 급 기기 ( 업무용 방송통신 기자재)
이 기기는 업무용(A 급) 전자파적합기기로서 판
매자 또는 사용자는 이 점을 주의하시기 바라
며, 가정외의 지역에서 사용하는 것을 목적으
로 합니다.
Class A Equipment (Business equipment)
This equipment is registered for Electromagnetic Conformity 
Registration as business equipment (A), not home equipment. 
Sellers or users are required to take caution in this regard.

<<<PAGE 85>>>
Network Cable Installation Warning
Regulatory Compliance and Safety Information
page A-8
OmniSwitch 6900 Hardware Users Guide
December 2025
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
Translated Safety Warnings
Blank Panels Warning
Because they regulate airflow and help protect internal chassis components, blank cover plates should 
remain installed at empty module slots and power supply bays at all times.
Français: Les caches blancs remplissent trois fonctions importantes: ils évitent tout risque de choc 
électrique à l'intérieur du châssis, ils font barrage aux interférences électromagnétiques susceptibles 
d'altérer le fonctionnement des autres équipements et ils dirigent le flux d'air de refroidissement dans le 
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
Deutsch: Um elektrische Schläge zu vermeiden dürfen während eines Gewitters and diesem Gerät keine 
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

<<<PAGE 86>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-9
Invisible Laser Radiation Warning
Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When 
removing cables do not stare into the open apertures. In addition, install protective aperture covers to fiber 
ports with no cable connected.
Français: Des radiations invisibles à l'œil nu pouvant traverser l'ouverture du port lorsque aucun câble en 
fibre optique n'y est connecté, il est recommandé de ne pas regarder fixement l'intérieur de ces ouvertures. 
Installez les caches connecteurs prévus à cet effet. 
Deutsch: Die Laser strahlen an der Blendenöffnung unsichtbares Licht ab, wenn keine Glasfaserkabel 
angeschlossen sind. Blicken Sie nicht in die Öffnungen und installieren Sie unverzüglich die 
Abdeckungen über den Glasfaseranschlüssen.
Español: Debido a que la apertura del puerto puede emitir radiación invisible cuando no hay un cable de 
fibra conectado, procurar no mirar directamente a las aperturas para no exponerse a la radiación.
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

<<<PAGE 87>>>
DC Power Supply Connection Warning
Regulatory Compliance and Safety Information
page A-10
OmniSwitch 6900 Hardware Users Guide
December 2025
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

<<<PAGE 88>>>
Regulatory Compliance and Safety Information
DC Power Supply Connection Warning
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-11
Read Important Safety Information Warning
The Getting Started information that accompanied this equipment contains important safety information 
about which you should be aware when working with hardware components in this system. You should 
read this information before installing, using, or servicing this equipment.
Français: Avant de brancher le système sur la source d'alimentation, consultez les directives d'installation 
disponibles dans le “Getting Started.”
Deutsch: Der “Getting Started,” welcher diese Anlage beiliegt, enthält wichtige Sicherheitsinformationen, 
über die sie sich beim Arbeiten mit den Hardwareeinheiten bewußt sein sollten. Sie sollten diese Hinweise 
lesen, bevor sie installieren, reparieren oder die Anlage verwenden.
Español: La “Getting Started” que acompañó este equipo contiene información importante de seguridad 
sobre la cual usted debe estar enterado al trabajar con los componentes de dotación física en este sistema. 
Usted debe leer esta información antes de instalar, usar o mantener este equipo.
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
Because electrostatic discharge (ESD) can damage switch components, you must follow proper 
procedures to eliminate ESD from your person and the surrounding area before handling switch 
components. 
Français: Parce que les décharges électrostatiques (ESD) peuvent endommager les composants de 
commutation, vous devez suivre les procédures appropriées pour éliminer ESD de votre personne et la 
région environnante avant de manipuler les composants de commutation.
Deutsch: Da elektrostatische Entladung (ESD) Switch-Komponenten beschädigen können, müssen Sie 
geeignete Verfahren zur Beseitigung von Ihrer Person und der Umgebung vor dem Umgang mit 
ESDSchalter-Komponenten folgen.
Español: Debido a las descargas electrostáticas (ESD) puede dañar los componentes del interruptor, debe 
seguir los procedimientos adecuados para eliminar la EDS de su persona y sus alrededores antes de 
manipular los componentes del interruptor.

<<<PAGE 89>>>
Instrucciones de seguridad en español
Regulatory Compliance and Safety Information
page A-12
OmniSwitch 6900 Hardware Users Guide
December 2025
Instrucciones de seguridad en español
Advertencia sobre el levantamiento del chasis
Se requieren dos personas para levantar el chasis. Debido a su peso, la elevación del chasis sin ayuda 
puede causar daños corporales. También es seguro doblar sus rodillas y guardar su espalda derecho al 
ayudar a levantar el chasis.
Advertencia de las tapaderas en blanco
Porque regulan la circulación de aire y ayudan a proteger componentes internos del chasis, las tapaderas en 
blanco deben seguir instaladas en las ranuras vacías del módulo y la fuente de alimentación siempre.
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
Advertencia sobre la desconexión de la fuente
Su interruptor esta equipado por fuentes de alimentación múltiples. Para reducir el riesgo de choque 
eléctrico, asegúrese desconectar todas las conexiones de alimentación antes de mantener o de mover la 
unidad.

<<<PAGE 90>>>
Regulatory Compliance and Safety Information
Instrucciones de seguridad en español
OmniSwitch 6900 Hardware Users Guide
December 2025
page A-13
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
Las unidades OmniSwitch 6900 pueden estar equipadas con tres cordones para fuente de poder. Para 
reducir el riesgo de un choque electrico, desconecte todos los cordones de fuente de poder antes de dar 
servicio a la unidad.