<<<PAGE 1>>>
Part No. 060711-00, Rev. J
December 2025
OmniSwitch 6360
Hardware Users Guide
www.al-enterprise.com

<<<PAGE 2>>>
This user guide documents OmniSwitch 6360 hardware, including chassis and associated components. The 
specifications described in this guide are subject to change without notice.
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
OmniSwitch 6360 Hardware Users Guide
December 2025
iii
Contents
About This Guide .......................................................................................................... ix
Supported Platforms .......................................................................................................... ix
Who Should Read this Manual? ........................................................................................ix
When Should I Read this Manual? ....................................................................................ix
What is in this Manual? .....................................................................................................ix
What is Not in this Manual? ............................................................................................... x
How is the Information Organized? ................................................................................... x
Documentation Roadmap ..................................................................................................xi
Related Documentation ...................................................................................................xiii
Technical Support ...........................................................................................................xiii
Chapter 1
OmniSwitch 6360  ......................................................................................................1-1
OmniSwitch 6360 Availability Features .........................................................................1-3
Hot-Swapping ...........................................................................................................1-3
Hardware Monitoring ...............................................................................................1-3
Chapter 2
Getting Started ...........................................................................................................2-1
Installing the Hardware ...................................................................................................2-1
Items Required .........................................................................................................2-1
Site Preparation ........................................................................................................2-1
Environmental Requirements ............................................................................2-1
Electrical Requirements .....................................................................................2-1
Electrical Surge Warning ..................................................................................2-2
Unpacking and Installing the Switch .......................................................................2-2
Items Included ...................................................................................................2-3
Weight Considerations ......................................................................................2-3
Airflow Considerations .....................................................................................2-3
Mounting the Switch .......................................................................................................2-4
Connections and Cabling ................................................................................................2-4
Network Cable Installation Warning .................................................................2-4
Serial Connection to the Console Port ...............................................................2-4
Serial Connection Default Settings ...................................................................2-4
Booting the Switch ..........................................................................................................2-4
Component LEDs ..............................................................................................2-5
Your First Login Session ................................................................................................2-5
Logging In to the Switch ..........................................................................................2-5
Unlocking Session Types .........................................................................................2-6

<<<PAGE 4>>>
Contents
iv
OmniSwitch 6360 Hardware Users Guide
December 2025
Unlocking All Session Types ............................................................................2-6
Unlocking Specified Session Types ..................................................................2-6
Changing the Login Password ..................................................................................2-6
Setting the System Time Zone .................................................................................2-7
Setting the Date and Time ........................................................................................2-7
Setting Optional Parameters .....................................................................................2-7
Specifying an Administrative Contact ...............................................................2-7
Specifying a System Name ................................................................................2-7
Specifying the Switch’s Location ......................................................................2-7
Viewing Your Changes ............................................................................................2-8
Saving Your Changes ...............................................................................................2-8
Chapter 3
Chassis and Power Supplies ....................................................................................3-1
OmniSwitch 6360 Chassis Details ..................................................................................3-2
OS6360-10 ...............................................................................................................3-2
OS6360-10 Front Panel .....................................................................................3-2
OS6360-10 Rear Panel ......................................................................................3-2
OS6360-10 Chassis Specifications ....................................................................3-3
OS6360-P10 .............................................................................................................3-4
OS6360-P10 Front Panel ...................................................................................3-4
OS6360-P10 Rear Panel ....................................................................................3-4
OS6360-P10 Chassis Specifications ..................................................................3-5
OS6360-24 ...............................................................................................................3-6
OS6360-24 Front Panel .....................................................................................3-6
OS6360-24 Rear Panel ......................................................................................3-6
OS6360-24 Chassis Specifications ....................................................................3-7
OS6360-P24 .............................................................................................................3-8
OS6360-P24 Front Panel ...................................................................................3-8
OS6360-P24 Rear Panel ....................................................................................3-8
OS6360-P24 Chassis Specifications ..................................................................3-9
OS6360-P24X ........................................................................................................3-10
OS6360-P24X Front Panel ..............................................................................3-10
OS6360-P24X Rear Panel ...............................................................................3-10
OS6360-P24X Chassis Specifications .............................................................3-11
OS6360-PH24 ........................................................................................................3-12
OS6360-PH24 Front Panel ..............................................................................3-12
OS6360-PH24 Rear Panel ...............................................................................3-12
OS6360-PH24 Chassis Specifications .............................................................3-13
OS6360-48 .............................................................................................................3-14
OS6360-48 Front Panel ...................................................................................3-14
OS6360-48 Rear Panel ....................................................................................3-14
OS6360-48 Chassis Specifications ..................................................................3-15
OS6360-P48 ...........................................................................................................3-16
OS6360-P48 Front Panel .................................................................................3-16
OS6360-P48 Rear Panel ..................................................................................3-16
OS6360-P48 Chassis Specifications ................................................................3-17
OS6360-P48X ........................................................................................................3-18
OS6360-P48X Front Panel ..............................................................................3-18
OS6360-P48X Rear Panel ...............................................................................3-18
OS6360-P48X Chassis Specifications .............................................................3-19
OS6360-PH48 ........................................................................................................3-20

<<<PAGE 5>>>
Contents
OmniSwitch 6360 Hardware Users Guide
December 2025
v
OS6360-PH48 Front Panel ..............................................................................3-20
OS6360-PH48 Rear Panel ...............................................................................3-20
OS6360-PH48 Chassis Specifications .............................................................3-21
Chassis Status LEDs ...............................................................................................3-21
Mounting the Switch .....................................................................................................3-22
General Mounting Recommendations ....................................................................3-22
Airflow Recommendations ....................................................................................3-22
Blank Cover Panels ................................................................................................3-23
Installing Blank Cover Panels .........................................................................3-24
Rack-Mounting .............................................................................................................3-24
Installing Rack Mount Flanges ..............................................................................3-25
Installing the Chassis In the Rack ..........................................................................3-26
Standalone (Non-Rack Mounted) Installations ......................................................3-27
Rack-Mounting 1/2 Width Switches .............................................................................3-27
Available 1/2 Width Rack-Mounting Kits .............................................................3-28
General Rack-Mounting Guidelines .......................................................................3-28
Installing Available Rack Mounting Kits .....................................................................3-28
Installing the OS6360-RM-L Rack Mount Kit ......................................................3-28
Wall-Mounting ..............................................................................................................3-29
General Wall-Mounting Guidelines .......................................................................3-29
OS6360-WALL-MNT - Wall-Mounting Installation ............................................3-30
Grounding the Chassis ..................................................................................................3-31
Monitoring Chassis Components ..................................................................................3-31
Viewing Chassis Slot Information .........................................................................3-31
Monitoring Chassis Temperature ..................................................................................3-32
Temperature Errors ..........................................................................................3-32
Chapter 4
 Managing Power over Ethernet (PoE) .................................................................4-1
In This Chapter ................................................................................................................4-2
Power over Ethernet Specifications ................................................................................4-2
Power over Ethernet Defaults .........................................................................................4-3
Power over Ethernet Budget ...........................................................................................4-3
Viewing Power Supply Status ..................................................................................4-3
Viewing PoE Status ..................................................................................................4-4
Understanding and Modifying the Default Settings .................................................4-4
PoE Class Detection .................................................................................................4-4
Enabling 802.3bt ................................................................................................4-5
PoE Operational Status .............................................................................................4-5
Configuring the Total Power Available to a Port ..............................................4-6
Configuring the Total Power Available to a slot ...............................................4-7
Setting Port Priority Levels ...............................................................................4-7
Setting the Capacitor Detection Method ...........................................................4-8
Understanding Guard Band .............................................................................................4-8
Understanding Priority Disconnect .................................................................................4-9
Setting Priority Disconnect Status ............................................................................4-9

<<<PAGE 6>>>
Contents
vi
OmniSwitch 6360 Hardware Users Guide
December 2025
Disabling Priority Disconnect ...........................................................................4-9
Enabling Priority Disconnect ..........................................................................4-10
Priority Disconnect is Enabled; Same Priority Level on All PD .....................4-10
Priority Disconnect is Enabled; 
Incoming PD Port has Highest Priority Level .................................................4-10
Priority Disconnect is Enabled; 
Incoming PD Port has Lowest Priority Level ..................................................4-10
Priority Disconnect is Disabled .......................................................................4-11
Monitoring Power over Ethernet via CLI .....................................................................4-11
Appendix A
Regulatory Compliance and Safety Information A-1
Declaration of Conformity: CE Mark ............................................................................A-1
Waste Electrical and Electronic Equipment (WEEE) Statement ...................................A-1
China RoHS: Hazardous Substance Table .....................................................................A-2
Taiwan RoHS: Hazardous Substance Table ..................................................................A-3
California Proposition 65 Warning ................................................................................A-4
Standards Compliance ....................................................................................................A-4
FCC Class A, Part 15 ..............................................................................................A-6
Canada Class A Statement ......................................................................................A-7
JATE ........................................................................................................................A-7
CISPR22 Class A warning ......................................................................................A-7
Korea Emissions Statement .....................................................................................A-8
VCCI .......................................................................................................................A-8
Class A Warning for Taiwan and Other Chinese Markets ......................................A-8
Class 1M Laser Warning .........................................................................................A-8
Network Cable Installation Warning .......................................................................A-8
Translated Safety Warnings ...........................................................................................A-9
Blank Panels Warning ......................................................................................A-9
Electrical Storm Warning .................................................................................A-9
Installation Warning .........................................................................................A-9
Invisible Laser Radiation Warning ...................................................................A-9
Operating Voltage Warning ...........................................................................A-10
Power Disconnection Warning .......................................................................A-10
Proper Earthing Requirement Warning ..........................................................A-11
DC Power Supply Connection Warning ......................................................................A-11
Read Important Safety Information Warning .................................................A-12
Restricted Access Location Warning .............................................................A-12
Wrist Strap Warning .......................................................................................A-12
Instrucciones de seguridad en español .........................................................................A-13
Advertencia sobre el levantamiento del chasis ...............................................A-13
Advertencia de las tapaderas en blanco ..........................................................A-13
Advertencia en caso de tormenta eléctrica .....................................................A-13
Advertencia de instalación .............................................................................A-13
Advertencia de radiación láser invisible .........................................................A-13
Advertencia de la batería de litio ....................................................................A-13
Advertencia sobre la tensión de operación .....................................................A-13
Advertencia sobre la desconexión de la fuente ..............................................A-13

<<<PAGE 7>>>
Contents
OmniSwitch 6360 Hardware Users Guide
December 2025
vii
Advertencia sobre una apropiada conexión a tierra .......................................A-14
Leer “información importante de seguridad” .................................................A-14
Advertencia de acceso restringido ..................................................................A-14
Advertencia de pulsera antiestática ................................................................A-14
Clase de seguridad ..........................................................................................A-14
Advertencia de fuentes de poder ....................................................................A-14

<<<PAGE 8>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
ix
About This Guide
This OmniSwitch 6360 Hardware Users Guide describes OmniSwitch 6360 switch components and basic 
switch hardware procedures. 
Supported Platforms
The information in this guide applies only to OmniSwitch 6360 switches.
Who Should Read this Manual?
The audience for this users guide is network administrators and IT support personnel who need to 
configure, maintain, and monitor switches and routers in a live network. However, anyone wishing to gain 
knowledge of the hardware will benefit from the material in this guide.
When Should I Read this Manual?
Read this guide as soon as you are ready to familiarize yourself with your switch hardware components. 
You should already be familiar with the very basics of the switch hardware, such as module LEDs and 
component installation procedures. This manual will help you understand your switch hardware in 
greater depth.
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

<<<PAGE 9>>>
x
OmniSwitch 6360 Hardware Users Guide
December 2025
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
OmniSwitch 6360 Hardware Users Guide
December 2025
xi
Documentation Roadmap
The OmniSwitch user documentation suite was designed to supply you with information at several critical 
junctures of the configuration process.The following section outlines a roadmap of the manuals that will 
help you at each stage of the configuration process. Under each stage, we point you to the manual or 
manuals that will be most helpful to you.
Stage 1: Using the Switch for the First Time
Pertinent Documentation: Getting Started Information
Release Notes
A “Getting Started” chapter is included in the Hardware Users Guide. This chapter provides all the 
information you need to get your switch up and running the first time. It also includes succinct overview 
information on fundamental aspects of the switch.
At this time you should also familiarize yourself with the Release Notes that accompanied your switch. 
This document includes important information on feature limitations that are not included in other 
user guides.
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: Hardware Users Guide
Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the Hardware Users Guide. This 
guide provide specifications, illustrations, and descriptions of all hardware components. It also includes 
steps for common procedures, such as removing and installing switch components.
This guide is the primary users guide for the basic software features on a single switch. This guide 
contains information on the switch directory structure, basic file and directory utilities, switch access 
security, SNMP, and web-based management. It is recommended that you read this guide before 
connecting your switch to the network.
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: Network Configuration Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The Network Configuration Guide guide contains overview information, procedures, and 
examples on how standard networking technologies are configured on the OmniSwitch.

<<<PAGE 11>>>
xii
OmniSwitch 6360 Hardware Users Guide
December 2025
Anytime
The OmniSwitch CLI Reference Guide contains comprehensive information on all CLI commands 
supported by the switch. This guide includes syntax, default, usage, example, related CLI command, and 
CLI-to-MIB variable mapping information for all CLI commands supported by the switch. This guide can 
be consulted anytime during the configuration process to find detailed and specific information on each 
CLI command.

<<<PAGE 12>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
xiii
Related Documentation
The following are the titles and descriptions of all the user manuals:
• OmniSwitch 6360 Hardware Users Guide
Complete technical specifications and procedures for all OmniSwitch 6360 chassis, power supplies, 
fans, and Network Interface (NI) modules.
• CLI Reference Guide
Complete reference to all CLI commands supported on the OmniSwitch. Includes syntax definitions, 
default values, examples, usage guidelines and CLI-to-MIB variable mappings.
• Switch Management Guide
Includes procedures for readying an individual switch for integration into a network. Topics include the 
software directory architecture, image rollback protections, authenticated switch access, managing 
switch files, system configuration, using SNMP, and using web management software (WebView).
• Network Configuration Guide
Includes network configuration procedures and descriptive information on all the major software 
features and protocols included in the base software package. Chapters cover Layer 2 information 
(Ethernet and VLAN configuration), Layer 3 information (routing protocols, such as RIP and IPX), 
security options (authenticated VLANs), Quality of Service (QoS), link aggregation, and server 
load balancing.
• Technical Tips, Field Notices
Includes information published by Alcatel-Lucent’s Customer Support group.
• Release Notes
Includes critical Open Problem Reports, feature exceptions, and other important information on the 
features supported in the current release and any limitations to their support.
Technical Support
A service agreement brings your company the assurance of 7x24 no-excuses technical support. You’ll also 
receive regular software updates to maintain and maximize your product’s features and functionality and 
on-site hardware replacement through our global network of highly qualified service delivery partners. 
With 24-hour access to the Service and Support web page, you’ll be able to view and update any case 
(open or closed) that you have reported to technical support, open a new case or access helpful release 
notes, technical bulletins, and manuals. 
Access additional information can be found below: 
Web: myportal.al-enterprise.com
Phone: 1-800-995-2696

<<<PAGE 13>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
page 1-1
1   OmniSwitch 6360
Refer to the information below for OmniSwitch 6360 models and components.
Model Number
Description
OS6360-10
Fixed-configuration chassis in a 1U form factor with: 
• 10 x RJ45 non-PoE ports
• 2 x SFP ports
• Internal power supply
• Fan less
See “OS6360-10” on page 3-2
OS6360-P10
Fixed-configuration chassis in a 1U form factor with: 
• 8 x RJ45 PoE (802.3at) ports
• 2 x RJ45 non-PoE ports
• 2 x SFP ports
• Internal power supply
• Fan less
See “OS6360-P10” on page 3-4.
OS6360-24
Fixed-configuration chassis in a 1U form factor with: 
• 24 x RJ45 non-PoE ports
• 2 x RJ45/SFP combo ports
• 2 x SFP+ software configurable ports: 
a) 2 x SFP uplinks
b) 2 x SFP+ uplink or VFL ports
• Internal power supply
• Fan less
See “OS6360-24” on page 3-6.
OS6360-P24
Fixed-configuration chassis in a 1U form factor with: 
• 24 x RJ45 PoE (802.3at) ports
• 2 x RJ45/SFP combo ports
• 2 x SFP+ software configurable ports: 
a) 2 x SFP uplinks
b) 2 x SFP+ uplink or VFL ports
• Internal power supply
• Fan less
See “OS6360-P24” on page 3-8

<<<PAGE 14>>>
OmniSwitch 6360
page 1-2
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-P24X
Fixed-configuration chassis in a 1U form factor with: 
• 24 x RJ45 PoE (802.3at) ports:
• 2 x RJ45/SFP+ combo ports
• 2 x SFP+ software configurable ports:
a) 2 x SFP uplinks
   b) 2 x SFP+ uplink or VFL ports
• Internal power supply
See “OS6360-P24X” on page 3-10
OS6360-PH24
Fixed-configuration chassis in a 1U form factor with: 
• 24 x RJ45 PoE (802.3at) ports:
• 2 x RJ45/SFP+ combo ports (Upgradeable to 10G)
• 2 x SFP+ software configurable ports: 
a) 2 x SFP uplinks
   b) 2 x SFP+ uplink or VFL ports
• Internal power supply
See “OS6360-PH24” on page 3-12
OS6360-48
Fixed-configuration chassis in a 1U form factor with: 
• 48 x RJ45 non-PoE ports
• 2 x RJ45/SFP combo ports
• 2 x SFP+ software configurable ports:
a) 2 x SFP uplinks
   b) 2 x SFP+ uplink or VFL ports
• Internal power supply
See “OS6360-48” on page 3-14
OS6360-P48
Fixed-configuration chassis in a 1U form factor with: 
• 48 x RJ45 PoE (802.3at) ports
• 2 x RJ45/SFP combo ports
• 2 x SFP+ software configurable ports: 
a) 2 x SFP uplinks
   b) 2 x SFP+ uplink or VFL ports
• Internal power supply
See “OS6360-P48” on page 3-16
OS6360-P48X
Fixed-configuration chassis in a 1U form factor with: 
• 48 x RJ45 PoE ports 
b) 46 x RJ45 PoE (802.3at) ports
a) 2 x Multigig PoE (802.3bt) ports
• 2 x RJ45/SFP+ combo ports
• 2 x SFP+ software configurable ports: 
a) 2 x SFP uplinks
   b) 2 x SFP+ uplink or VFL ports
• Internal power supply
See “OS6360-P48X” on page 3-18
Model Number
Description

<<<PAGE 15>>>
OmniSwitch 6360
OmniSwitch 6360 Availability Features
OmniSwitch 6360 Hardware Users Guide
December 2025
page 1-3
OmniSwitch 6360 Availability Features
The switch provides a broad variety of availability features. Availability features are hardware and 
software-based safeguards that help prevent the loss of data flow in the unlikely event of a subsystem 
failure. In addition, some availability features allow users to maintain or replace hardware components 
without powering off the switch or interrupting switch operations. Combined, these features provide added 
resiliency and help ensure that the switch is consistently available for day-to-day network operations.
Hardware-related availability features include:
• Hot-Swapping
• Hardware Monitoring
Hot-Swapping
Hot-swapping refers to the action of adding, removing, or replacing certain hardware components without 
powering off your switch and disrupting other components in the chassis. This feature greatly facilitates 
hardware upgrades and maintenance and also allows you to easily replace components in the unlikely 
event of hardware failure. 
Hardware Monitoring
Automatic Monitoring
Automatic monitoring refers to the switch’s built-in sensors that automatically monitor operations. If an 
error is detected (e.g., over-threshold temperature), the switch immediately sends a trap to the user. The 
trap is displayed on the console in the form of a text error message.
LEDs
LEDs, which provide visual status information, are provided on the front and rear panels. LEDs are used 
to indicate conditions, such as hardware and software status, link integrity, data flow, etc. For detailed 
LED descriptions, refer to the corresponding hardware component section in the next chapter.
OS6360-PH48
Fixed-configuration chassis in a 1U form factor with: 
• 48 x RJ45 PoE ports 
a) 46 x RJ45 PoE (802.3at) ports
b) 2 x Multigig PoE (802.3bt) ports
• 2 x RJ45/SFP+ combo ports (Upgradeable to 10G)
• 2 x SFP+ software configurable ports: 
a) 2 x SFP uplinks
   b) 2 x SFP+ uplink or VFL ports
• Internal power supply
See “OS6360-PH48” on page 3-20
Model Number
Description

<<<PAGE 16>>>
OmniSwitch 6360 Availability Features
OmniSwitch 6360
page 1-4
OmniSwitch 6360 Hardware Users Guide
December 2025
User-Driven Monitoring
User-driven hardware monitoring refers to CLI commands that are entered by the user in order to access 
the current status of hardware components. The user enters “show” commands that output information to 
the console. The show commands for all the features are described in detail in the CLI Reference Guide.

<<<PAGE 17>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
page 2-1
2   Getting Started
Installing the Hardware
Note. For information on configuring a Virtual Chassis (VC), refer to the Switch Management Guide.
Items Required
• Grounding wrist strap
• Phillips screwdriver
• Flat-blade screwdriver
Site Preparation
Environmental Requirements
The switches have the following environmental and airflow requirements:
• The installation site must maintain a supported temperature and humidity range as given in the 
specifications table for the chassis. See “OmniSwitch 6360 Chassis Details” on page 3-2.
• Be sure to allow adequate room for proper air ventilation at the front, back, and sides of the switch. 
Refer to “Airflow Considerations” on page 2-3 for minimum clearance requirements. No clearance is 
necessary at the top or bottom of the chassis.
Electrical Requirements
Note. Switches must be installed by a professional installer. It is the responsibility of the installer to ensure 
that proper grounding is available and that the installation meets applicable local and national electrical 
codes.
The switches have the following general electrical requirements:
• Each switch requires one grounded electrical outlet for each power supply installed in the chassis. 
• For switches using AC power connections, each supplied AC power cord is 2 meters (approx. 6.5 feet). 
Do not use extension cords.
• ALE provided power cords are UL recognized to IEC 62368-1 exceeding the maximum amperage 
requirement for the power source. If using a non-ALE provided power cord the installer shall confirm it 
meets the minimum electrical requirements of the power source.

<<<PAGE 18>>>
Installing the Hardware
Getting Started
page 2-2
OmniSwitch 6360 Hardware Users Guide
December 2025
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
Note. Failure to follow the above recommendations could result in voiding the warranty of the affected 
ALE product. 
Unpacking and Installing the Switch
To protect your switch components from damage, read all unpacking recommendations and instructions 
carefully before beginning.
Unpack your chassis as close as possible to the location where it will be installed.

<<<PAGE 19>>>
Getting Started
Installing the Hardware
OmniSwitch 6360 Hardware Users Guide
December 2025
page 2-3
Items Included
Your OmniSwitch may include the following items:
• OmniSwitch chassis with power supplies, per order
• Transceivers, per order
• Blank cover panel
• Rack mount brackets
• Country-specific power cord(s)
• Rubber table-mounting feet
• Attachment screws
• Assorted instructional cards, anti-static bags and additional packaging
Weight Considerations
Weights vary depending on model type. Please refer to the chassis specifications table.
Airflow Considerations
To ensure proper airflow, be sure that your switch is placed in a clean, well-ventilated area free of dust and 
debris and provide minimum recommended clearance at the front, back and sides of the switch.
Never obstruct chassis air vents.
Chassis Top View
}
}
Rear. 6 inches minimum 
at rear of chassis.
Front. 6 inches minimum 
at front of chassis.
Sides. 2 inches minimum 
at left and right sides.

<<<PAGE 20>>>
Mounting the Switch
Getting Started
page 2-4
OmniSwitch 6360 Hardware Users Guide
December 2025
Note. Clearance is not required at the top and bottom of the chassis.
Mounting the Switch
For information on mounting the switches, refer to the Chapter 3, “Chassis and Power Supplies.”
Connections and Cabling
Once your switch is properly installed, you should connect all network and management cables required for 
your network applications. Connections may include:
• Console connector
• Cables to NIs or transceivers
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
Serial Connection to the Console Port
The console port provides a serial connection to the switch is required when logging into the switch for the 
first time. By default, this connector provides a DCE console connection.
Serial Connection Default Settings
For information on modifying these settings, refer to the Switch Management Guide.
Booting the Switch
Now that you have installed the switch components and connected network and management cables, you can 
boot the switch. To boot the switch, plug all power supply cords into easily-accessible, properly grounded 
power outlets. (Do not use extension cords.) The switch will power on and boot automatically.
Note. If you have more than one power supply installed, be sure to plug in each power supply in rapid 
succession, (i.e., within a few seconds of each other). This ensures that there will be adequate power for all 
components throughout the boot process.
baud rate
9600
parity
none
data bits (word size)
8
stop bits
1

<<<PAGE 21>>>
Getting Started
Your First Login Session
OmniSwitch 6360 Hardware Users Guide
December 2025
page 2-5
Component LEDs
During the boot process, component LEDs will flash and change color, indicating different stages of the boot 
For complete information on LED states, refer to “Chassis Status LEDs” on page 3-21.
Once the switch has completely booted and you have accessed your computer’s terminal emulation software 
via the console port, you are ready to log in to the switch’s Command Line Interface (CLI) and configure basic 
information. Continue to “Your First Login Session” on page 2-5.
Your First Login Session
In order to complete the setup process for the switch, you must complete the following steps during your first 
login session:
• Log in to the switch
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
• Password: switch
The default welcome banner, which includes information such as the current software version and system date, 
is displayed followed by the CLI command prompt:
Welcome to the Alcatel-Lucent OmniSwitch 8.7.R01, July 15, 2020.
Copyright (c) 1994-2014 Alcatel-Lucent. All Rights Reserved.
OmniSwitch(tm) is a trademark of Alcatel-Lucent, registered in the United States 
Patent and Trademark Office.
->
Note. A user account includes a login name, password, and user privileges. Privileges determine whether 
the user has read or write access to the switch and which commands the user is authorized to execute. For 
detailed information on setting up and modifying user accounts, refer to the Switch Management Guide.

<<<PAGE 22>>>
Your First Login Session
Getting Started
page 2-6
OmniSwitch 6360 Hardware Users Guide
December 2025
Unlocking Session Types
Security is a key feature on an OmniSwitch switch. As described on page 2-5, when you access the switch for 
the first time, you must use a direct console port connection. All other session types (Telnet, FTP, WebView, 
and SNMP) are locked out until they are manually unlocked by the user.
The CLI command used to unlock session types is aaa authentication. 
Note. When you unlock session types, you are granting switch access to non-local sessions (e.g., Telnet). 
As a result, users who know the correct user login and password will have remote access to the switch. For 
more information on switch security, refer to the Switch Management Guide.
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
page 2-5). 
2 Enter the keyword password and press Enter.
3 Enter your new password at the prompt.
Note. Be sure to remember or securely record all new passwords; overriding configured passwords on an 
OmniSwitch is restricted.
4 You will be prompted to re-enter the password. Enter the password a second time.

<<<PAGE 23>>>
Getting Started
Your First Login Session
OmniSwitch 6360 Hardware Users Guide
December 2025
page 2-7
New password settings are automatically saved in real time to the local user database; the user is not required 
to enter an additional command in order to save the password information. Also note that new password 
information is retained following a reboot. All subsequent login sessions, including those through the console 
port, will require the new password to access the switch.
For detailed information on managing login information, including user names and passwords, refer to the 
Switch Management Guide.
Setting the System Time Zone
The switch’s default time zone is UTC. If you require a time zone that is specific to your region, or if you need 
to enable Daylight Savings Time (DST) on the switch, you can configure these settings via the system 
timezone and system daylight-savings-time commands.
For detailed information on configuring a time zone for the switch, refer to the Switch Management Guide.
Setting the Date and Time
Set the current time for the switch by entering system time, followed by the current time in hh:mm:ss. 
To set the current date for the switch, enter system date, followed by the current date in mm/dd/yyyy.
Note. The OS6360 does not contain a real-time clock. It is recommended to use NTP for time synchroni-
zation. Switch resets will boot up with an approximate time based on the last known system time. A 
powered off switch will boot up with the same time as when it was powered off.
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

<<<PAGE 24>>>
Your First Login Session
Getting Started
page 2-8
OmniSwitch 6360 Hardware Users Guide
December 2025
Viewing Your Changes
To view your current changes, enter show system at the CLI prompt.
Saving Your Changes
Once you have configured this basic switch information, save your changes by entering write memory at the 
CLI command prompt.

<<<PAGE 25>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-1
3   Chassis and Power
Supplies
This chapter includes detailed information on the chassis types. Topics include:
• Chassis details and technical specifications:
OS6360-10, page 3-2.
OS6360-P10, page 3-4.
OS6360-24, page 3-6.
OS6360-P24, page 3-8.
OS6360-P24X, page 3-10.
OS6360-PH24, page 3-12.
OS6360-48, page 3-14
OS6360-P48, page 3-16.
OS6360-P48X, page 3-18.
OS6360-PH48, page 3-20.
• Switch mounting information, page 3-22.
• Temperature management, page 3-31.
• Monitoring the chassis components via the Command Line Interface (CLI), page 3-31

<<<PAGE 26>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-2
OmniSwitch 6360 Hardware Users Guide
December 2025
OmniSwitch 6360 Chassis Details
OS6360-10
OS6360-10 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-10 Rear Panel
 
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-8) 10/100/1000 Base-T ports
D
(9-10) 10/100/1000 Base-T ports
E
(11-12) SFP ports (1G)
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (30W Internal AC Power Supply)
Console / USB
1
2
3
4
5
6
7
8
9
10
11
12
OK
VC
PWR
D
A
B
C
E
A
B

<<<PAGE 27>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-3
OS6360-10 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
21.7 cm (8.5 in)
Chassis Depth 
28.1 cm (11.1 in)
Chassis Weight
1.8 kg (4.0 lb)
Power Consumption (idle)
13 W
Nominal Voltage
100V-240V, 50-60Hz
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 28>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-4
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-P10
OS6360-P10 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-P10 Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-8) 10/100/1000 Base-T PoE(802.3at) ports
D
(9-10) 10/100/1000 Base-T ports
E
(11-12) SFP ports (1G)
Note: The OmniSwitch 6360-P10 model (904324-90), orderable part number OS6360-P10A-US, does not 
support Fast or Perpetual PoE. The overlay remains as OS6360-P10 but this model is differentiated from other 
OS6360-10 models by part number 904324-90. 
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (165W Internal AC Power Supply)
Console / USB
1
2
3
4
5
6
7
8
9
10
11
12
OK
VC
PWR
D
A
B
C
E
A
B

<<<PAGE 29>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-5
OS6360-P10 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
21.7 cm (8.5 in)
Chassis Depth 
28.1 cm (11.1 in)
Chassis Weight 
2.1 kg (4.6 lb)
Power Consumption (idle)
13 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
120W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 30>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-6
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-24
OS6360-24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-24 Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-24) 10/100/1000 Base-T ports
D
(25-26) RJ-45 (10/100/1000) / SFP (1G) combo ports
E
(27-28) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (65W Internal AC Power Supply)
D
E
A
B
C
A
B

<<<PAGE 31>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-7
OS6360-24 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
22 cm (8.7 in)
Chassis Weight
3.1 kg (6.8 lb) 
Power Consumption (idle)
21 W
Nominal Voltage
100V-240V, 50-60Hz
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 32>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-8
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-P24
OS6360-P24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-P24 Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-24) 10/100/1000 Base-T PoE (802.3at) ports
D
(25-26) RJ-45 (10/100/1000) / SFP (1G) combo ports
E
(27-28) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (260W Internal AC Power Supply)
D
E
E
A
B
C
A
B

<<<PAGE 33>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-9
OS6360-P24 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
22 cm (8.7 in)
Chassis Weight
3.2 kg (7.1 lb) 
Power Consumption (idle)
21 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
180W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 34>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-10
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-P24X
OS6360-P24X Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-P24X Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-24) 10/100/1000 Base-T PoE (802.3at) ports
D
(25-26) RJ-45 (10/100/1000/10G) / SFP+ (1G/10G) combo ports
E
(27-28) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (550W Internal AC Power Supply)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
25
26
27
28
OK
VC
PWR
Console / USB
D
E
A
B
C
A
B

<<<PAGE 35>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-11
OS6360-P24X Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
30 cm (11.8 in)
Chassis Weight
3.9 kg (8.6 lb)
Power Consumption (idle)
34 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
380W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 36>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-12
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-PH24
OS6360-PH24 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-PH24 Rear Panel
 
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-24) 10/100/1000 Base-T PoE (802.3at) ports
D
(25-26) RJ-45 (10/100/1000/10G) / SFP+ (1G/10G) combo ports (Upgradeable to 10G)
E
(27-28) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (550W Internal AC Power Supply)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
25
26
27
28
OK
VC
PWR
Console / USB
D
E
A
B
C
A
B

<<<PAGE 37>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-13
OS6360-PH24 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
30 cm (11.8 in)
Chassis Weight
3.9 kg (8.6 lb) 
Power Consumption (idle)
34 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
380W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 38>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-14
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-48
OS6360-48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-48 Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-48) 10/100/1000 Base-T ports
D
(49-50) RJ-45 (10/100/1000) / SFP (1G) combo ports
E
(51-52) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Power Supply Connector (120W Internal AC Power Supply)
B
Chassis Grounding Lug
D
E
A
B
C
A
B

<<<PAGE 39>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-15
OS6360-48 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
33 cm (13.0 in)
Chassis Weight
4.6 kg (10.1 lb)
Power Consumption (idle)
46 W
Nominal Voltage
100V-240V, 50-60Hz
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 40>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-16
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-P48
OS6360-P48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-P48 Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-48) 10/100/1000 Base-T PoE (802.3at) ports
D
(49-50) RJ-45 (10/100/1000) / SFP (1G) combo ports
E
(51-52) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
 Power Supply Connector (550W Internal AC Power Supply)
B
Chassis Grounding Lug
D
E
A
B
C
A
B

<<<PAGE 41>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-17
OS6360-P48 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
33 cm (13.0 in)
Chassis Weight
4.6 kg (10.1 lb)
Power Consumption (idle)
47 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
350W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 42>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-18
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-P48X
OS6360-P48X Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-P48X Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-46) 10/100/1000 Base-T PoE (802.3at) ports
D
(47-48) 10/100/1000/2.5G PoE (802.3bt) ports
E
(49-50) RJ-45 (10/100/1000/10G) / SFP+ (1G/10G) combo ports 
F
(51-52) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (950W Internal AC Power Supply)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
49
50
OK
VC
PWR
Console / USB
D
E
A
B
C
F
A
B

<<<PAGE 43>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-19
OS6360-P48X Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
30 cm (11.8 in)
Chassis Weight
4.4 kg (9.7 lb) 
Power Consumption (idle)
60 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
760W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing

<<<PAGE 44>>>
OmniSwitch 6360 Chassis Details
Chassis and Power Supplies
page 3-20
OmniSwitch 6360 Hardware Users Guide
December 2025
OS6360-PH48
OS6360-PH48 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6360-PH48 Rear Panel
Item
Description
A
Status LEDs
B
Console and USB port
C
(1-46) 10/100/1000 Base-T PoE (802.3at) ports
D
(47-48) 10/100/1000/2.5G PoE (802.3bt) ports
E
(49-50) RJ-45 (10/100/1000/10G) / SFP+ (1G/10G) combo ports (Upgradeable to 10G)
F
(51-52) SFP+ (1G/10G) Uplink or VFL ports
Item
Description
A
Chassis Grounding Lug
B
Power Supply Connector (950W Internal AC Power Supply)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
49
50
OK
VC
PWR
Console / USB
	

D
E
A
B
C
F
A
B

<<<PAGE 45>>>
Chassis and Power Supplies
OmniSwitch 6360 Chassis Details
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-21
OS6360-PH48 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Chassis temperature refers to the sensor reading of 
the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room 
temperature. The ambient temperature will typically be lower than the chassis temperature. 
Chassis Status LEDs
The chassis provides a series of status LEDs located on the front panel. These LEDs offer basic status 
information for hardware operation and port link and activity status.
Chassis Height
4.4 cm (1.7 in)
Chassis Width 
44 cm (17.3 in)
Chassis Depth 
30 cm (11.8 in)
Chassis Weight
4.4 kg (9.7 lb) 
Power Consumption (idle)
60 W
Nominal Voltage
100V-240V, 50-60Hz
PoE Budget
760W
Operating Temperature (Tmra)
0°C to 45°C (32°F to 113°F)
Storage Temperature
-40°C to 70°C (-40°F to 158°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
LED
State
Description
OK
Solid Green
Blinking Green
Solid Amber
System Diagnostics and AOS bootup OK.
System Diagnostics and AOS in progress
(i.e., performing diagnostics or booting).
System Diagnostics and AOS/fan/temp fail
VC
Blinking Green
Blinking Amber
Off
Master (number of blinks identifies ID).
Salve (number of blinks identifies ID).
This unit is in shutdown mode or is not part of 
a VC.
PWR
Solid Green
Solid Amber
Blinking Amber
Off
Main power supply normal.
Main power supply fault (12V).
Main power supply fault (54V/PoE).
Main power supply not present.

<<<PAGE 46>>>
Mounting the Switch
Chassis and Power Supplies
page 3-22
OmniSwitch 6360 Hardware Users Guide
December 2025
Mounting the Switch
General Mounting Recommendations
Elevated Operating Ambient Temperature. If installed in a closed or multi-rack assembly, the operating 
ambient temperature of the rack environment may be greater than the room’s ambient temperature. 
Therefore, consideration should be given to the maximum rated ambient temperature (Tmra) listed in the 
“OmniSwitch 6360 Chassis Details” section.
Reduced Air Flow. Installation of the equipment in a rack should be such that the amount of air flow 
required for safe operation of the equipment is not compromised. Refer to “Airflow Recommendations” on 
page 3-22 for more information.
Mechanical Loading. Mounting of the equipment in the rack should be such that a hazardous condition is 
not achieved due to uneven loading.
Circuit Overloading. Consideration should be give to the connection of the equipment to the supply 
circuit and the effect that overloading of circuits could have on overcurrent protection and supply wiring. 
Reliable Earthing. Reliable earthing of rack-mounted equipment should be maintained. Particular 
attention should be given to supply connections other than direct connections to the branch (e.g., use of 
power strips).
Airflow Recommendations
To ensure proper airflow, be sure that your switch is placed in a clean, well-ventilated area free of dust and 
debris and provide minimum recommended clearance at the front, back and sides of the switch, as shown 
below. Restricted airflow can cause your switch to overheat, which can lead to switch failure. Refer to the 
following important guidelines regarding airflow: 
RJ45 Port LEDs
Solid Green
Blinking Green
Solid Amber
Blinking Amber
Valid port link (non-PoE).
Valid port link with activity (non-PoE).
Valid port link (PoE).
Valid port link with activity (PoE).
SFP Port LEDs
Solid / Blinking Green
Solid / Blinking Amber
Uplink port / with activity.
VFL port / with activity. 
LED
State
Description

<<<PAGE 47>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-23
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

<<<PAGE 48>>>
Rack-Mounting
Chassis and Power Supplies
page 3-24
OmniSwitch 6360 Hardware Users Guide
December 2025
Installing Blank Cover Panels
1 When installing blank cover panels over power supply slots, orient the cover panels with the arrows
pointing up.
2 Insert the blank cover panel in the empty chassis slot and secure using attachment screws (provided).
Rack-Mounting
Refer to the following important guidelines before installing the chassis in a rack:
• Two people are required to rack mount the switch: One person to lift the chassis into position and one 
person to secure the chassis to the rack using the rack mount screws.
• The chassis has rack-mount flanges that support standard 19-inch rack mount installations.
• Alcatel-Lucent Enterprise does not provide rack-mount screws. Use the screws supplied by the 
rack vendor.
• To prevent a rack from becoming top heavy, it is recommended that you install the switch at the bottom 
of the rack whenever possible.
Face arrow up
when installing.

<<<PAGE 49>>>
Chassis and Power Supplies
Rack-Mounting
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-25
Note. If you are installing the switch in a relay rack, be sure to install and secure the rack per rack manu-
facturer’s specifications.
Installing Rack Mount Flanges
1 To install rack mount flanges, start by making sure the spring clip is in the out (disengaged) position.
2 Insert the tab into the chassis slot as shown.
3 Press the flange and spring clip until the flange clicks into place and the clip is in the in 
(engaged) position.
Slot
Tab
Clip in “Out” 
(disengaged) 
position
Clip in “In” 
(engaged) 
position
“CLICK”

<<<PAGE 50>>>
Rack-Mounting
Chassis and Power Supplies
page 3-26
OmniSwitch 6360 Hardware Users Guide
December 2025
4 Secure the flange to the chassis using the attachment screw (provided).
5 Repeat steps 1 through 4 for the flange on the opposite side of the chassis.
Installing the Chassis In the Rack
1 Mark the holes on the rack where the chassis is to be installed.
2 One person should lift and position the chassis until the rack-mount flanges are flush with the
rack post.
3 Align the holes in the flanges with the rack holes marked in step 1.
4 Once the holes are aligned, the second person should insert a screw through the bottom hole on each 
flange. Tighten both screws until they are secure.

<<<PAGE 51>>>
Chassis and Power Supplies
Rack-Mounting 1/2 Width Switches
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-27
5 Install the remaining screws in the top hole of each flange. Be sure that all screws are 
securely tightened.
Standalone (Non-Rack Mounted) Installations
The chassis can also be placed unmounted on a stable, flat surface as a standalone unit. Be sure that the 
surface can accommodate the full, populated weight of all switches being installed. (Approximate chassis 
weights are provided in the technical specifications tables in the “OmniSwitch 6360 Chassis Details” 
section.) 
Be sure that adequate clearance has been provided for chassis airflow and that you have placed the chassis 
within reach of all required AC outlets. For recommended airflow allowances, refer to page 3-22.
To prepare the chassis for tabletop installations, follow the steps below:
1 Insert the four (4) rubber feet (provided separately in the switch packaging) into the holes in the bottom 
panel of the chassis. 
2 Place the switch on the tabletop “right side up.”
Note. Never attempt to operate a switch while it is placed on its top or side.
3 Connect network and management cables as needed.
Rack-Mounting 1/2 Width Switches
The following kits are available for rack mounting 1/2 width switches.

<<<PAGE 52>>>
Installing Available Rack Mounting Kits
Chassis and Power Supplies
page 3-28
OmniSwitch 6360 Hardware Users Guide
December 2025
Note. Some factory-installed screws may need to be removed prior to mounting, depending on the kit 
being used.
Available 1/2 Width Rack-Mounting Kits
Note. For information on rack mounting full width 24- and 48-port switches, refer to 
“Mounting the Switch” on page 3-22.
General Rack-Mounting Guidelines
If you will be rack-mounting your switch(es), refer to the important guidelines below before installing.
• It is recommended that two people install the switch assembly on the rack—one person to hold the 
chassis and position it on the rack, and a second person to secure the chassis to the rack using 
attachment screws. (Please note that Alcatel-Lucent Enterprise does not provide rack-mount screws. 
Use the screws supplied by the rack vendor.)
• To prevent a rack from becoming top heavy, it is recommended that you install heavier equipment at 
the bottom of the rack, whenever possible.
• Review page 4-1 for recommended chassis clearances before installing.
• If you are installing the switch on a relay rack, be sure to install and secure the rack per the rack 
manufacturer’s specifications.
Installing Available Rack Mounting Kits
Note. Some factory-installed screws may need to be removed prior to mounting, depending on the kit
being used.
Installing the OS6360-RM-L Rack Mount Kit
A single chassis can also be mounted into a standard 19-inch rack using L-brackets, as shown in the figure 
below.
Kit
Description
OS6360-RM-19-L
Simple L-bracket for mounting one 1/2 unit in a 19" rack. See page 3-28 for 
installation instructions.

<<<PAGE 53>>>
Chassis and Power Supplies
Wall-Mounting
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-29
1 Attach rack mount brackets to both sides of the front of the chassis.The long and short bracket can be 
mounted on either side of the chassis. 
Attach Rack Mount Brackets
2 Align the holes in the flanges with the rack holes and insert rack mount screws (not provided) through 
the bottom hole of each flange and then the top of each flange. Tighten both screws until they are secure
Rack-mounting Single Chassis
Wall-Mounting
The OmniSwitch 6360-10/P10 switches can also be installed as wall-mounted units using the OS6360-
WALL-MNT kit. 
General Wall-Mounting Guidelines
• When choosing a location for the switch, be sure that adequate clearance has been provided for chassis 
airflow and access to the front, back, and sides of the chassis. For recommended clearances, refer to 
“Airflow Considerations” on page 2-3.
• In order to ensure that damage to the power cord does not occur, steps must be taken to provide proper 
routing of the power cord, as well as proper access to the switch’s power source (i.e., grounded outlet). 
Refer to the guidelines listed below for additional details.
Follow the recommended clearance requirements for the 
model type being mounted.

<<<PAGE 54>>>
Wall-Mounting
Chassis and Power Supplies
page 3-30
OmniSwitch 6360 Hardware Users Guide
December 2025
• The power cord measures two (2) meters (approximately 6.5 feet) in length. When wall mounting the 
switch, be sure that the mounting location is within the reach of all the required power sources. In addi-
tion, the power cord must not be attached to the building surface 
(e.g., with U-brackets, cord retainer clips, or other fasteners), nor run through walls, ceiling, floors and 
similar openings in the building structure.
• Be sure that the wall section and wall attachment screws (not provided) have the required strength to 
easily support the chassis assembly.
• For each mounting hole the use of screws long enough to penetrate any soft surfaces, such as sheetrock 
or drywall, and securely attach to a hard surface such as a wall stud is recommended. 
• Two people will be required to wall mount the switch: one person to hold the chassis assembly in place 
and one person to mark the locations for the mounting screws.
• The wall mounting kit is needed for wall-mounting the chassis.
OS6360-WALL-MNT - Wall-Mounting Installation
1 Follow any assembly instructions based on the configuration of the chassis and power supply.
2  Orient the wall-mount brackets facing down. Attach the brackets to both the left and right side of the 
switch, as shown.
Attaching the wall-mount brackets.
3 Attach two additional mounting brackets to the rear portion of the chassis facing down. Attach the 
brackets to both the left and right side of the switch.
4 Use one person to securely hold the chassis assembly in position on the wall. Mark the location of the 
holes in the mounting brackets on the wall.

<<<PAGE 55>>>
Chassis and Power Supplies
Grounding the Chassis
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-31
5 Pre-drill the wall (if required).
Recommended Wall Mount Chassis Orientation (OS6360-WALL-MNT)
Note. Wall fasteners are not provided with your switch and will vary depending on the type of wall 
surface. Be sure to use fasteners that are approved for the full weight of the chassis assembly. Consult 
fastener specifications for full details.
6 Secure the unit to the wall using appropriate wall fasteners. 
Grounding the Chassis
The switch has a grounding lug located on the rear of the chassis. This lug uses 10-32 screws and is 
surrounded by a small paint-free area, which provides metal-to-metal contact for a ground connection.
Use this connector to supplement the ground provided by the AC power cord. To do so, install a Panduit 
Grounding Lug (type LCD8-10A-L) using 8AWG copper conductors to the paint-free area. Torque to 
between 30-60 inch pounds.
Refer to the rear chassis views on page 3-2 for location details. 
Monitoring Chassis Components
Viewing Chassis Slot Information
To view basic slot information, enter the show module command at the CLI prompt:
NOTE: For wall mounting, it is recommended that the 
chassis assembly is oriented sideways, with the chassis 
front panel facing to the side.
Wall surface
Chassis

<<<PAGE 56>>>
Monitoring Chassis Temperature
Chassis and Power Supplies
page 3-32
OmniSwitch 6360 Hardware Users Guide
December 2025
-> show module
To view more detailed information, use the show module long command:
-> show module long
Monitoring Chassis Temperature
The operating temperature of your switch is a critical factor in its overall operability. In order to avoid a 
temperature-related system failure, your switch must always run at a temperature within the specified 
operating temperature range. 
To avoid chassis over-temperature conditions, follow the important chassis airflow recommendations on 
page 3-22.
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
If the temperature exceeds the switch’s Warning threshold, the switch sends out a trap. Traps are also 
printed to the console in the form of text error messages.
When the Warning threshold has been exceeded, switch operations remain active. However, it is 
recommended that immediate steps be taken to address the over-temperature condition.
Addressing Warning threshold temperature conditions may include:
• Checking for a chassis airflow obstruction

<<<PAGE 57>>>
Chassis and Power Supplies
Monitoring Chassis Temperature
OmniSwitch 6360 Hardware Users Guide
December 2025
page 3-33
• Checking the ambient room temperature
Temperature Danger Threshold
If the chassis temperature rises above the Danger threshold, the switch will power off until the temperature 
conditions have been addressed and the switch is manually booted. The Danger threshold is factory-set 
and cannot be configured by the user.
Addressing danger threshold temperature conditions may include:
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature

<<<PAGE 58>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
page 4-1
4    Managing Power over
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
Important. It’s recommended that PoE-enabled switches with attached IP telephones should have opera-
tional power supply redundancy at all times for 911 emergency requirements. In addition, both the switch 
and the power supply should be plugged into an Uninterruptible Power Source (UPS).

<<<PAGE 59>>>
In This Chapter
Managing Power over Ethernet (PoE)
page 4-2
OmniSwitch 6360 Hardware Users Guide
December 2025
In This Chapter
This chapter provides specifications and descriptions of hardware and software used to provide PoE for 
attached devices. 
The chapter also provides information on configuring PoE settings on the switch through the Command 
Line Interface (CLI). CLI commands are used in the configuration examples; for more details about the 
syntax of commands, see the OmniSwitch CLI Reference Guide. Topics and configuration procedures 
described in this chapter include:
• Power over Ethernet Specifications on page 4-2
• Viewing Power Status on page 4-4
• Configuring Power over Ethernet Parameters on page 4-4
• Understanding Priority Disconnect on page 4-10
• Monitoring Power over Ethernet via the CLI on page 4-11
Power over Ethernet Specifications
The table below lists general specifications for Alcatel-Lucent’s Power over Ethernet support. For more 
detailed power supply and Power Source Equipment (PSE) specifications, refer to Chapter 3, “Chassis and 
Power Supplies.” .
IEEE Standards supported
IEEE 802.3; 802.af; 802.3at;802.3bt
PoE Class Detection
Supported
Range of inline power per port
802.3at ports - 3000-30000 milliwatts
802.3bt ports - 3000-95000 milliwatts
Maximum PoE power per chassis
See “Power over Ethernet Budget”.

<<<PAGE 60>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Defaults
OmniSwitch 6360 Hardware Users Guide
December 2025
page 4-3
Power over Ethernet Defaults
The following table lists the defaults for PoE configuration:
Power over Ethernet Budget
The following table lists the Power over Ethernet wattages available based on the number and types of power 
supplies installed.
Viewing Power Supply Status
To view the type and status for installed power supplies, use the show powersupply command:
-> show powersupply
             Total     PS
Chassis/PS   Power     Type     Status   Location
-----------+---------+--------+--------+-----------
Parameter 
Description
Command(s)
Default Value/Comments
PoE operational status
lanpower slot service 
Disabled
Power available to a 
port
lanpower power
802.3at ports - 30000 milliwatts
802.3bt ports - 95000 milliwatts
Power available to an 
entire slot
lanpower slot maxpower
See “Power over Ethernet Budget”.
Power priority level for 
a port
lanpower priority
low
Capacitor detection 
method
lanpower capacitor-detec-
tion
Disabled
Priority disconnect sta-
tus
lanpower slot priority-dis-
connect
Enabled
OmniSwitch
PoE Budget
OS6360-P10
120W
OS6360-P24
180W
OS6360-P24X
380W
OS6360-PH24
380W
OS6360-P48
350W
OS6360-P48X
760W
OS6360-PH48
760W

<<<PAGE 61>>>
Power over Ethernet Budget
Managing Power over Ethernet (PoE)
page 4-4
OmniSwitch 6360 Hardware Users Guide
December 2025
 1/1         165
 AC       UP       Internal
    Total   165
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
ChassisId 1 Slot 1 Max Watts 120
0 Watts Total Power Budget Used
120 Watts Total Power Budget Available
1 Power Supplies Available
‘*’ appending port maxpower indicates 4pair port operating in 2pair mode
Understanding and Modifying the Default Settings
The sections below provide information on each of the key components within the Power over Ethernet 
software. They include information on PoE-related CLI commands. For detailed information on PoE-
related commands, refer to the OmniSwitch CLI Reference Guide. 
PoE Class Detection 
Powered devices can be classified into different classes as shown in the table below. Class detection 
allows for automatic maximum power adjustment based on the power class detected. This will prevent the 
switch from delivering more than the maximum power allowed based on a device’s class. 
During class detection, the switch will allocate the maximum amount of power allowed based on the class 
detected. Once powered, if the device uses less than the maximum, the remaining power will be made 
available for other devices. 
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

<<<PAGE 62>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6360 Hardware Users Guide
December 2025
page 4-5
Although class-detection is disabled by default, the switch still provides power to incoming PDs (if avail-
able in the power budget). However, to strictly enforce class detection it must be enabled using the 
lanpower slot class-detection command.
Enabling class detection will reset all PoE ports on the chassis.
Enabling 802.3bt
The OmniSwitch supports IEEE 802.3af, IEEE 802.3at on 2-pairs, IEEE 802.3at on 4 pairs with support 
for classes 0, 1, 2, 3 and 4. Support for 60W, 75W and 95W per port is provided supporting IEEE 802.3at 
on 4-pairs and enabling PoH using the lanpower 4pair command.
The OmniSwitch also supports IEEE 802.3bt with an additional two types and 4 classes listed in the table 
above. IEEE 802.3bt can be enabled with the lanpower 8023bt command.
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
Disabling PoE
To disable PoE on a particular port, use the lanpower port admin-state command. For example:
-> lanpower port 1/1/12 admin-state disable
To disable PoE for all PoE-capable ports in a slot, use the lanpower slot service command. For example:
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
Standard
Class
Type
Pairs
Power at Port 
(Watts)

<<<PAGE 63>>>
Power over Ethernet Budget
Managing Power over Ethernet (PoE)
page 4-6
OmniSwitch 6360 Hardware Users Guide
December 2025
-> lanpower slot 1/1 service stop
Note. The OmniSwitch 6360-P10 (904324-90), orderable part number OS6360-P10A-US, does not 
support Fast or Perpetual PoE. The overlay remains as OS6360-P10 but this model is differentiated from 
other OS6360-10 models by part number 904324-90. 
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
reduces the power allowance on port 24 to 3000 milliwatts. This new value is now the maximum amount 
of power the port can use to power any attached device (until the value is modified by the user).

<<<PAGE 64>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6360 Hardware Users Guide
December 2025
page 4-7
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
changes the priority value of port 6 to the highest priority level of critical. Now that the default value has 
been reconfigured, this port should be reserved for those PDs that are mission critical for network opera-
tions.

<<<PAGE 65>>>
Understanding Guard Band
Managing Power over Ethernet (PoE)
page 4-8
OmniSwitch 6360 Hardware Users Guide
December 2025
Setting the Capacitor Detection Method
By default, the capacitor detection method is disabled. To enable it, use the lanpower capacitor-detec-
tion. For example:
-> lanpower slot 3/1 capacitor-detection enable
Note. The capacitive detection method should only be enabled to support legacy IP phones. This feature 
is not compatible with IEEE specifications. Please contact your Alcatel-Lucent sales engineer or Customer 
Support representative to find out which Alcatel-Lucent IP phones models need capacitive 
detection enabled.
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

<<<PAGE 66>>>
Managing Power over Ethernet (PoE)
Understanding Priority Disconnect
OmniSwitch 6360 Hardware Users Guide
December 2025
page 4-9
The Guard Band functionality does not apply to PDs that are already powered up. However, priority disconnect 
will apply if there's not enough power to power all PDs in the case of the power budget being reduced, such as 
the removal of a power supply.
Please refer to the “Understanding Priority Disconnect” on page 4-10 for additional details.
Understanding Priority Disconnect
The priority disconnect function differs from the port priority function described on page 4-7 in that it 
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
ing PDs, refer to the illustrated examples on pages 4-10 through 4-11.
Reminder. Priority disconnect applies only when there is inadequate power remaining in the power 
budget for an incoming device.
For information on setting the priority disconnect status, refer to the section below. For information on 
setting the port priority status (a separate function from priority disconnect), refer to “Setting Port Priority 
Levels” on page 4-7.
Setting Priority Disconnect Status
By default, priority disconnect is enabled in the switch’s system software. For information on changing 
the priority disconnect status, refer to the information below.
Disabling Priority Disconnect
When priority disconnect is disabled and there is inadequate power in the budget for an additional device, 
power will be denied to any incoming PD, regardless of its port priority status (i.e., low, high, and criti-
cal) or physical port number (i.e., 1–24).
To disable priority disconnect, use the lanpower slot priority-disconnect command. For example: 
-> lanpower slot 2/1 priority-disconnect disable

<<<PAGE 67>>>
Understanding Priority Disconnect
Managing Power over Ethernet (PoE)
page 4-10
OmniSwitch 6360 Hardware Users Guide
December 2025
Enabling Priority Disconnect
To enable priority disconnect, use the lanpower slot priority-disconnect command. For example: 
-> lanpower slot 2/1 priority-disconnect enable
Priority Disconnect is Enabled; Same Priority Level on All PD
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When a PD is being connected to a port with the same priority level as all other in the slot, the physical 
port number is used to determine whether the incoming PD will be granted or denied power. Due to the 
support of different PoE standards and PoE hardware on each platform the internal port priority is differ-
ent for each platform. The following should be used to determine PoE priority:
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
Port Number
1 (Highest) -> 48(Lowest)

<<<PAGE 68>>>
Managing Power over Ethernet (PoE)
Monitoring Power over Ethernet via CLI
OmniSwitch 6360 Hardware Users Guide
December 2025
page 4-11
Priority Disconnect is Disabled
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When priority disconnect is disabled, power will be denied to any incoming PD, regardless of its port 
priority status (i.e., low, high, and critical) or physical port number (i.e., 1–24).
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
-> show lanpower 1
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

<<<PAGE 69>>>
Monitoring Power over Ethernet via CLI
Managing Power over Ethernet (PoE)
page 4-12
OmniSwitch 6360 Hardware Users Guide
December 2025
Slot 3 Max Watts 150
1 Power Supplies Available
Note. For detailed information on show lanpower command output, refer to the OmniSwitch CLI Refer-
ence Guide.

<<<PAGE 70>>>
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-1
A  Regulatory Compliance
and Safety Information
This appendix provides information on regulatory agency compliance and safety for the OmniSwitch.
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
Waste Electrical and Electronic Equipment (WEEE) 
Statement
The product at end of life is subject to separate collection and treatment in the EU Member States, Norway 
and Switzerland and therefore marked with the following symbol:
Treatment applied at end of life of the product in these countries shall comply with the applicable national 
laws implementing directive 2002/96/EC on waste electrical and electronic equipment (WEEE).

<<<PAGE 71>>>
China RoHS: Hazardous Substance Table
Regulatory Compliance and Safety Information
page A-2
OmniSwitch 6360 Hardware Users Guide
December 2025
China RoHS: Hazardous Substance Table

<<<PAGE 72>>>
Regulatory Compliance and Safety Information
Taiwan RoHS: Hazardous Substance Table
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-3
Taiwan RoHS: Hazardous Substance Table

<<<PAGE 73>>>
California Proposition 65 Warning
Regulatory Compliance and Safety Information
page A-4
OmniSwitch 6360 Hardware Users Guide
December 2025
California Proposition 65 Warning
WARNING: This product can expose you to chemicals including Pb and Pb compounds, which is known 
to the State of California to cause cancer and birth defects or other reproductive harm. For more 
information go to www.P65Warnings.ca.gov.
Products are packaged using one or more of the following packaging materials:
Standards Compliance
The product bears the CE mark. In addition it is in compliance with the following other safety and 
EMC standards.
Note. All hardware switching modules used in an OmniSwitch switch comply with Class A 
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
Corrugated Cardboard                Corrugated Fiberboard              Low-Density Polyethylene
CB
FB

<<<PAGE 74>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-5
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

<<<PAGE 75>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-6
OmniSwitch 6360 Hardware Users Guide
December 2025
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

<<<PAGE 76>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-7
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
This equipment meets the requirements of the Japan Approvals Institute of Telecommunications Equip-
ment (JATE).
CISPR22 Class A warning
This is a Class A product. In a domestic environment, this product may cause radio interference. Under 
such circumstances, the user may be requested to take appropriate countermeasures.

<<<PAGE 77>>>
Translated Safety Warnings
Regulatory Compliance and Safety Information
page A-8
OmniSwitch 6360 Hardware Users Guide
December 2025
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
châssis. Il est vivement recommandé de vérifier que tous les caches, modules d'alimentation et plaques de 
protection sont en place avant d'utiliser le système.
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

<<<PAGE 78>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-9
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
angeschlossen sind. Blicken Sie nicht in die Öffnungen und installieren Sie unverzüglich die 
Abdeckungen über den Glasfaseranschlüssen.
Español: Debido a que la apertura del puerto puede emitir radiación invisible cuando no hay un cable de 
fibra conectado, procurar no mirar directamente a las aperturas para no exponerse a la radiación.
Operating Voltage Warning
To reduce the risk of electrical shock, keep your hands and fingers out of power supply bays and do not 
touch the backplane while the switch is operating.

<<<PAGE 79>>>
Translated Safety Warnings
Regulatory Compliance and Safety Information
page A-10
OmniSwitch 6360 Hardware Users Guide
December 2025
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

<<<PAGE 80>>>
Regulatory Compliance and Safety Information
DC Power Supply Connection Warning
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-11
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

<<<PAGE 81>>>
DC Power Supply Connection Warning
Regulatory Compliance and Safety Information
page A-12
OmniSwitch 6360 Hardware Users Guide
December 2025
Read Important Safety Information Warning
The Getting Started Guide that accompanied this equipment contains important safety information about 
which you should be aware when working with hardware components in this system. You should read this 
guide before installing, using, or servicing this equipment.
Français: Avant de brancher le système sur la source d'alimentation, consultez les directives d'installation 
disponibles dans le “Getting Started Guide”.
Deutsch: Der Getting Started Guide, welcher dieser Anlage beiliegt, enthält wichtige 
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
Français: Parce que les décharges électrostatiques (ESD) peuvent endommager les composants de 
commutation, vous devez suivre les procédures appropriées pour éliminer ESD de votre personne et la 
région environnante avant de manipuler les composants de commutation.
Deutsch: Da elektrostatische Entladung (ESD) Komponenten beschädigen können, müssen geeignete 
Verfahren getroffen werden, diese elektrostatische Entladung bedingt durch Ihre Person oder der 
Umgebung zu beseitigen.
Español: Debido a las descargas electrostáticas (ESD) puede dañar los componentes del interruptor, debe 
seguir los procedimientos adecuados para eliminar la EDS de su persona y sus alrededores antes de 
manipular los componentes del interruptor.

<<<PAGE 82>>>
Regulatory Compliance and Safety Information
Instrucciones de seguridad en español
OmniSwitch 6360 Hardware Users Guide
December 2025
page A-13
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
Advertencia sobre la desconexión de la fuente
Su interruptor esta equipado por fuentes de alimentación múltiples. Para reducir el riesgo de choque 
eléctrico, asegúrese desconectar todas las conexiones de alimentación antes de mantener o de mover la 
unidad.

<<<PAGE 83>>>
Instrucciones de seguridad en español
Regulatory Compliance and Safety Information
page A-14
OmniSwitch 6360 Hardware Users Guide
December 2025
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
Las unidades OmniSwitch pueden estar equipadas con tres cordones para fuente de poder. Para reducir el 
riesgo de un choque electrico, desconecte todos los cordones de fuente de poder antes de dar servicio a la 
unidad.