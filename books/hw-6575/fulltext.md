<<<PAGE 1>>>
Part No. 060975-00, Rev. A
December 2025
OmniSwitch 6575
Hardware Users Guide
www.al-enterprise.com

<<<PAGE 2>>>
ii
December 2025
This user guide documents OmniSwitch 6575 hardware, including chassis and associated components. The 
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
OmniSwitch 6575 Hardware Users Guide
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
Documentation Roadmap ..................................................................................................ix
Related Documentation ...................................................................................................... x
Technical Support .............................................................................................................. x
Chapter 1
OmniSwitch 6575  ......................................................................................................1-1
OmniSwitch 6575 Availability Features .........................................................................1-2
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
Unpacking and Installing the Switch .......................................................................2-2
Items Included ...................................................................................................2-3
Weight Considerations ......................................................................................2-3
Connections and Cabling ................................................................................................2-3
Network Cable Installation Warning .................................................................2-3
Serial Connection to the Console Port ...............................................................2-3
Serial Connection Default Settings ...................................................................2-3
Booting the Switch ..........................................................................................................2-4
Component LEDs ..............................................................................................2-4
Your First Login Session ................................................................................................2-4
Logging In to the Switch ..........................................................................................2-4
Unlocking Session Types .........................................................................................2-5
Changing the Login Password ..................................................................................2-5
Setting the System Time Zone .................................................................................2-6

<<<PAGE 4>>>
Contents
iv
OmniSwitch 6575 Hardware Users Guide
December 2025
Setting the Date and Time ........................................................................................2-6
Setting Optional Parameters .....................................................................................2-6
Specifying an Administrative Contact ...............................................................2-6
Specifying a System Name ................................................................................2-6
Specifying the Switch’s Location ......................................................................2-7
Viewing Your Changes ............................................................................................2-7
Saving Your Changes ...............................................................................................2-7
Chapter 3
Chassis and Power Supplies ....................................................................................3-1
OmniSwitch 6575 Chassis Details ..................................................................................3-2
OS6575-P12 .............................................................................................................3-2
OS6575-P12 Front Panel ...................................................................................3-2
OS6575-P12 Rear Panel ....................................................................................3-3
OS6575-P12 Chassis Specifications ..................................................................3-4
OS6575-U28 .............................................................................................................3-5
OS6575-U28 Front Panel ..................................................................................3-5
OS6575-U28 Rear Panel ...................................................................................3-5
OS6575-U28 Chassis Specifications .................................................................3-6
OS6575-MP16 ..........................................................................................................3-7
OS6575-MP16 Front Panel ...............................................................................3-7
OS6575-MP16 Rear Panel ................................................................................3-8
OS6575-MP16 Chassis Specifications ..............................................................3-8
Chassis Status LEDs .................................................................................................3-9
Mounting the Switch .....................................................................................................3-11
General Mounting Recommendations ....................................................................3-11
Rack Mounting - OS6575-U28 ..............................................................................3-11
Rack Mounting Rear - OS6575-U28 ......................................................................3-13
DIN Rail Mounting - OS6575-P12 ........................................................................3-14
Wall Mounting - OS6575-P12 ...............................................................................3-16
Wall Mounting - OS6575-MP16 ............................................................................3-17
Power Supplies ..............................................................................................................3-18
OS6NN5-BPNS AC Power Supply ........................................................................3-19
LED States .......................................................................................................3-19
OS6NN5-BPNSX AC Power Supply .....................................................................3-20
LED States .......................................................................................................3-20
OS6575-BPR Power Supply ..................................................................................3-21
LED States .......................................................................................................3-21
OS6575-BPRD 180W DC Power Supply ..............................................................3-22
LED States .......................................................................................................3-22
 ................................................................................................................................3-22
Installing Power Supplies for Rear Mount Trays ...................................................3-23
Connecting the AC Power Supplies ..............................................................................3-24
Connecting the Removed Outer Jacket (ROJ) Power Cords ...........................3-24
Final Power Cord Connections ........................................................................3-26
Hot-Swapping / Removing a Power Supply ....................................................3-27
Grounding the Chassis ..................................................................................................3-28
Alarm Relay ..................................................................................................................3-29
Alarm Relay Configuration Examples ...................................................................3-30

<<<PAGE 5>>>
Contents
OmniSwitch 6575 Hardware Users Guide
December 2025
v
Monitoring Chassis Components ..................................................................................3-31
Viewing Chassis Slot Information .........................................................................3-31
Monitoring Chassis Temperature ..................................................................................3-31
Temperature Errors ..........................................................................................3-31
Dying Gasp ....................................................................................................................3-33
Scenarios ................................................................................................................3-33
SNMP Trap ............................................................................................................3-33
Syslog Message ......................................................................................................3-33
Chapter 4
 Managing Power over Ethernet (PoE) .................................................................4-1
In This Chapter ................................................................................................................4-2
Power over Ethernet Specifications ................................................................................4-3
Power over Ethernet Defaults .........................................................................................4-4
Power over Ethernet Budget ...........................................................................................4-5
Viewing Power Supply Status ..................................................................................4-6
Viewing PoE Status ..................................................................................................4-7
Understanding and Modifying the Default Settings .................................................4-7
PoE Class Detection .................................................................................................4-7
PoE Operational Status .............................................................................................4-8
Configuring the Total Power Available to a Port ..............................................4-8
Configuring the Total Power Available to a slot ...............................................4-9
Setting Port Priority Levels ...............................................................................4-9
Setting the Capacitor Detection Method .........................................................4-10
Understanding Guard Band ...........................................................................................4-11
Understanding Priority Disconnect ...............................................................................4-12
Setting Priority Disconnect Status ..........................................................................4-13
Disabling Priority Disconnect .........................................................................4-13
Enabling Priority Disconnect ..........................................................................4-13
Priority Disconnect is Enabled; Same Priority Level on All PD .....................4-13
Priority Disconnect is Enabled; 
Incoming PD Port has Highest Priority Level .................................................4-13
Priority Disconnect is Enabled; 
Incoming PD Port has Lowest Priority Level ..................................................4-14
Priority Disconnect is Disabled .......................................................................4-14
Monitoring Power over Ethernet via CLI .....................................................................4-15
Appendix A
Regulatory Compliance and Safety Information ..............................................A-1
Declaration of Conformity: CE Mark ............................................................................A-1
Waste Electrical and Electronic Equipment (WEEE) Statement ...................................A-1
China RoHS: Hazardous Substance Table .....................................................................A-2
Taiwan RoHS: Hazardous Substance Table ..................................................................A-3
California Proposition 65 Warning ................................................................................A-3
Standards Compliance ....................................................................................................A-4
FCC Class A, Part 15 ..............................................................................................A-7

<<<PAGE 6>>>
Contents
vi
OmniSwitch 6575 Hardware Users Guide
December 2025
Canada Class A Statement ......................................................................................A-8
JATE ........................................................................................................................A-8
CISPR22 Class A warning ......................................................................................A-8
Korea Emissions Statement .....................................................................................A-8
VCCI .......................................................................................................................A-8
Class A Warning for Taiwan (BSMI) and Other Chinese Markets ........................A-8
Class 1M Laser Warning .........................................................................................A-9
Network Cable Installation Warning .......................................................................A-9
NEBS-GR-1089-CORE Guidelines and Regulatory Compliance Statements ........A-9
Translated Safety Warnings .........................................................................................A-10
Blank Panels Warning ....................................................................................A-10
Electrical Storm Warning ...............................................................................A-10
Installation Warning .......................................................................................A-10
Invisible Laser Radiation Warning .................................................................A-10
Operating Voltage Warning ...........................................................................A-11
Power Disconnection Warning .......................................................................A-11
Proper Earthing Requirement Warning ..........................................................A-11
DC Power Supply Connection Warning ......................................................................A-12
Read Important Safety Information Warning .................................................A-12
Restricted Access Location Warning .............................................................A-12
Wrist Strap Warning .......................................................................................A-13
Instrucciones de seguridad en español .........................................................................A-13
Advertencia sobre el levantamiento del chasis ...............................................A-13
Advertencia de las tapaderas en blanco ..........................................................A-13
Advertencia en caso de tormenta eléctrica .....................................................A-13
Advertencia de instalación .............................................................................A-13
Advertencia de radiación láser invisible .........................................................A-13
Advertencia de la batería de litio ....................................................................A-14
Advertencia sobre la tensión de operación .....................................................A-14
Advertencia sobre la desconexión de la fuente ..............................................A-14
Advertencia sobre una apropiada conexión a tierra .......................................A-14
Leer “información importante de seguridad” .................................................A-14
Advertencia de acceso restringido ..................................................................A-14
Advertencia de pulsera antiestática ................................................................A-14
Clase de seguridad ..........................................................................................A-14
Advertencia de fuentes de poder ....................................................................A-15

<<<PAGE 7>>>
OmniSwitch 6575 Hardware Users Guide
December 2025
vii
About This Guide
This OmniSwitch 6575 Hardware Users Guide describes OmniSwitch 6575 switch components and basic 
switch hardware procedures. 
Supported Platforms
The information in this guide applies only to OmniSwitch 6575 switches.
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
• Hot-swapping power supplies.
• Installation and removal procedures for power supplies and modules.
• Detailed illustrations and LED descriptions for chassis, network and power supply operability.

<<<PAGE 8>>>
viii
OmniSwitch 6575 Hardware Users Guide
December 2025
• Hardware-related Command Line Interface (CLI) commands.
What is Not in this Manual?
The descriptive and procedural information in this manual focuses on switch hardware. It includes 
information on some CLI commands that pertain directly to hardware configuration, but it is not intended 
as a software users guide. There are several OmniSwitch users guides that focus on switch software 
configuration. Consult those guides for detailed information and examples for configuring your switch 
software to operate in a live network environment. See “Documentation Roadmap” on page -ix and 
“Related Documentation” on page -x for further information on software configuration guides available 
for your switch.
How is the Information Organized?
Each chapter in this guide focuses on a specific hardware component or a set of hardware components. All 
descriptive, technical specification, and procedural information for a hardware component can be found in 
the chapter dedicated to that component.

<<<PAGE 9>>>
OmniSwitch 6575 Hardware Users Guide
December 2025
ix
Documentation Roadmap
The OmniSwitch user documentation suite was designed to supply you with information at several critical 
junctures of the configuration process.The following section outlines a roadmap of the manuals that will 
help you at each stage of the configuration process. Under each stage, we point you to the manual or 
manuals that will be most helpful to you.
Stage 1: Using the Switch for the First Time
Pertinent Documentation: Getting Started Information
Release Notes
A “Getting Started” chapter is included in the OmniSwitch 6575 Hardware Users Guide. This chapter 
provides all the information you need to get your switch up and running the first time. It also includes 
succinct overview information on fundamental aspects of the switch.
At this time you should also familiarize yourself with the Release Notes that accompanied your switch. 
This document includes important information on feature limitations that are not included in other 
user guides.
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: Hardware Users Guide
OmniSwitch AOS Release 8 Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the OmniSwitch 6575 Hardware 
Guide. This guide provide specifications, illustrations, and descriptions of all hardware components. It also 
includes steps for common procedures, such as removing and installing switch components.
This guide is the primary users guide for the basic software features on a single switch. This guide 
contains information on the switch directory structure, basic file and directory utilities, switch access 
security, SNMP, and web-based management. It is recommended that you read this guide before 
connecting your switch to the network.
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: OmniSwitch AOS Release 8 Network Configuration Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The Network Configuration Guide guide contains overview information, procedures, and 
examples on how standard networking technologies are configured on the OmniSwitch.
Anytime
The OmniSwitch AOS Release 8 CLI Reference Guide contains comprehensive information on all CLI 
commands supported by the switch. This guide includes syntax, default, usage, example, related CLI 
command, and CLI-to-MIB variable mapping information for all CLI commands supported by the switch. 
This guide can be consulted anytime during the configuration process to find detailed and specific 
information on each CLI command.

<<<PAGE 10>>>
x
OmniSwitch 6575 Hardware Users Guide
December 2025
Related Documentation
The following are the titles and descriptions of all the OmniSwitch 6575 user manuals:
• OmniSwitch 6575 Hardware Users Guide
Complete technical specifications and procedures for all OmniSwitch 6575 chassis, power supplies, 
and Network Interface (NI) modules.
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

<<<PAGE 11>>>
OmniSwitch 6575 Hardware Users Guide
December 2025
page 1-1
1   OmniSwitch 6575
Refer to the information below for OmniSwitch 6575 models and components.
Model Number
Description
OS6575-P12
Fixed-configuration, fanless, din-mountable chassis with:
• 1 - Console Port
• 1 - EMP Port
• 1 - USBport
• 1 - Alarm Relay
• 8 - 10/100/1000Base-T 802.3bt Ports
• 4 - SFP+ Uplink / VFL Ports
OS6575-U28
Fixed-configuration, fanless, rack-mountable chassis in a 1U form factor with: 
• 1 - Console Port
• 1 - EMP Port
• 1 - USBPort
• 1 - Alarm Relay
• 4 - 10/100/1000BaseT PoE+ or 100FX/1G SFP Combo Ports
• 20 - 100FX/1G SFP Ports
• 4 - SFP+ Uplink / VFL Ports
OS6575-MP16
Fixed-configuration, fanless, wall-mountable chassis with: 
• 1 - Console Port
• 1 - USB Port
• 1 - Alarm Relay
• 4 - 10/100BaseT Ports 
• 4 - 10/100BaseT 802.3at PoE Ports
• 4 - 10/100/1000BaseT 802.3bt Ports 
• 4 - 10/100/1000BaseT Ports

<<<PAGE 12>>>
OmniSwitch 6575 Availability Features
OmniSwitch 6575
page 1-2
OmniSwitch 6575 Hardware Users Guide
December 2025
OmniSwitch 6575 Availability Features
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
Multiple power supplies can be used for both system or PoE power supply redundancy dependent on the 
model. For information on power supplies, refer to Chapter 3, “Chassis and Power Supplies.” For informa-
tion on Power over Ethernet, refer to “Managing Power over Ethernet (PoE)”.
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
User-Driven Monitoring
User-driven hardware monitoring refers to CLI commands that are entered by the user in order to access 
the current status of hardware components. The user enters “show” commands that output information to 
the console. The show commands for all the features are described in detail in the OmniSwitch CLI 
Reference Guide.
Port Bypass
The OS6575-MP16 includes a port bypass feature that automatically connects two network ports if the 
device loses power or fails which allows traffic to continue uninterrupted. It prevents a single switch fail-
ure from breaking communications and improves availability for critical systems.

<<<PAGE 13>>>
OmniSwitch 6575 Hardware Users Guide
December 2025
page 2-1
2   Getting Started
Installing the Hardware
Items Required
• Grounding wrist strap
• Phillips screwdriver
• Flat-blade screwdriver
Site Preparation
Environmental Requirements
The switches have the following environmental and airflow requirements:
• The installation site must maintain a supported temperature and humidity range as given in the 
specifications table for the chassis. See “OmniSwitch 6575 Chassis Details” on page 3-2.
• Be sure to allow adequate room for proper air ventilation around the chassis. Refer to “Mounting the 
Switch” on page 3-10 for minimum clearance requirements. 
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
Redundant AC Power. It is recommended that each AC outlet resides on a separate circuit. With 
redundant AC, if a single circuit fails, the switch’s remaining power supplies (on separate circuits) can 
remain operational.

<<<PAGE 14>>>
Installing the Hardware
Getting Started
page 2-2
OmniSwitch 6575 Hardware Users Guide
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

<<<PAGE 15>>>
Getting Started
Connections and Cabling
OmniSwitch 6575 Hardware Users Guide
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
baud rate
9600
flow control
None
data bits
8
stop bits
1
cable type
rollover

<<<PAGE 16>>>
Booting the Switch
Getting Started
page 2-4
OmniSwitch 6575 Hardware Users Guide
December 2025
Booting the Switch
Now that you have installed the switch components and connected network and management cables, you can 
boot the switch. To boot the switch, plug all power supply cords into easily-accessible, properly grounded 
power outlets. (Do not use extension cords.) The switch will power on and boot automatically.
Note. If you have more than one power supply installed, be sure to plug in each power supply in rapid 
succession, (i.e., within a few seconds of each other). This ensures that there will be adequate power for all 
components throughout the boot process.
Component LEDs
During the boot process, component LEDs will flash and change color, indicating different stages of the boot 
For complete information on LED states, refer to “Chassis Status LEDs” on page 3-8.
Once the switch has completely booted and you have accessed your computer’s terminal emulation software 
via the console port, you are ready to log in to the switch’s Command Line Interface (CLI) and configure basic 
information. Continue to “Your First Login Session” on page 2-4.
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
Welcome to the Alcatel-Lucent Enterprise OmniSwitch 8.5.R01, February 15, 2018.

<<<PAGE 17>>>
Getting Started
Your First Login Session
OmniSwitch 6575 Hardware Users Guide
December 2025
page 2-5
Copyright (c) ALE-USA Inc., 2014-2021. All Rights Reserved.
OmniSwitch(tm) is a trademark of Alcatel-Lucent, registered in the United States 
Patent and Trademark Office.
->
Note. A user account includes a login name, password, and user privileges. Privileges determine whether 
the user has read or write access to the switch and which commands the user is authorized to execute. For 
detailed information on setting up and modifying user accounts, refer to the Switch Management Guide.
Unlocking Session Types
Security is a key feature on an OmniSwitch switch. As described on page 2-4, when you access the switch for 
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

<<<PAGE 18>>>
Your First Login Session
Getting Started
page 2-6
OmniSwitch 6575 Hardware Users Guide
December 2025
1 Be sure that you have logged into the switch as user type admin (see “Logging In to the Switch” on 
page 2-4). 
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
Switch Management Guide.
Setting the System Time Zone
The switch’s default time zone is UTC. If you require a time zone that is specific to your region, or if you need 
to enable Daylight Savings Time (DST) on the switch, you can configure these settings via the system 
timezone and system daylight-savings-time commands.
For detailed information on configuring a time zone for the switch, refer to the Switch Management Guide.
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

<<<PAGE 19>>>
Getting Started
Your First Login Session
OmniSwitch 6575 Hardware Users Guide
December 2025
page 2-7
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

<<<PAGE 20>>>
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-1
3  Chassis and Power Supplies
This chapter includes detailed information on the chassis types. Topics include:
• Chassis details and technical specifications:
OS6575-P12, page 3-2.
OS6575-U28, page 3-4.
OS6575-MP16, page 3-6.
• Mounting the Switch, page 3-10.
• Power supplies, page 3-17.
OS6NN5-BPNS, page 3-18.
OS6NN5-BPNSX, page 3-19.
OS6575-BPR, page 3-20.
OS6575-BPRD, page 3-21.
• Alarm Relays, page 3-29.
• Temperature management, page 3-31.
• Monitoring the chassis components via the Command Line Interface (CLI), page 3-31

<<<PAGE 21>>>
OmniSwitch 6575 Chassis Details
Chassis and Power Supplies
page 3-2
OmniSwitch 6575 Hardware Users Guide
December 2025
OmniSwitch 6575 Chassis Details
OS6575-P12
OS6575-P12 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
Item
Description
A
Console Port (RJ-45)
B
EMP Port (RJ-45)
C
USB Port (2.0)
D
Power Supply Connectors
E
Alarm Connectors
F
Grounding Lug
G
(1-8) 10/100/1000Base-T 802.3bt 60W
H
(9-12) 10G SFP+ Uplink / VFL Ports
LEDs
See “Chassis Status LEDs” on page 3-8
Note:
- Under 48VDC, PoE not supported. 
- When connecting in dual-redundant power supply configuration, both power supplies must have 
identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could 
result in unexpected behavior and is not supported.
G
H
B
C
F
A
D
E

<<<PAGE 22>>>
Chassis and Power Supplies
OmniSwitch 6575 Chassis Details
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-3
OS6575-P12 Rear Panel
 
OS6575-P12 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Internal temperature refers to the sensor reading of 
the internal switch temperature. Ambient temperature (Tmra) refers to the approximate room temperature. 
The ambient temperature will typically be lower than the internal temperature. 
Item
Description
A
DIN / Wall Mounting Bracket Options Available
Chassis Height
17 cm (6.70 in.)
Chassis Width 
9.1 cm (3.58 in.)
Chassis Depth 
16.1 cm (6.34 in.)
Chassis Weight
2.5 kg (5.51 lb)
Ambient Operating Temperature (Tmra)
-40°C to 75°C (-40°F to 167°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
System Power Consumption
50W
Input Power & Current
24-57VDC, max. 8A
A

<<<PAGE 23>>>
OmniSwitch 6575 Chassis Details
Chassis and Power Supplies
page 3-4
OmniSwitch 6575 Hardware Users Guide
December 2025
OS6575-U28
OS6575-U28 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
Item
Description
A
Console Port (RJ-45)
B
EMP Port (RJ-45)
C
USB Port
D
Alarm Connector
E
(1-4) - 10/100/1000BaseT PoE+ (90W) or 100FX/1G SFP Combo Ports
F
(5-28) - 100FX/1G SFP Ports
G
(29-32) 1G/10G SFP+ Uplink / VFL
LEDs
See “Chassis Status LEDs” on page 3-8
Note:
- Under 48VDC, PoE not supported. 
- When connecting in dual-redundant power supply configuration, both power supplies must have 
identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could 
result in unexpected behavior and is not supported.
F
E
G
D
A
B
C

<<<PAGE 24>>>
Chassis and Power Supplies
OmniSwitch 6575 Chassis Details
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-5
OS6575-U28 Rear Panel
OS6575-U28 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Internal temperature refers to the sensor reading of 
the internal switch temperature. Ambient temperature (Tmra) refers to the approximate room temperature. 
The ambient temperature will typically be lower than the internal temperature. 
Item
Description
A
PS2 - Power Supply Connector
B
PS1 - Power Supply Connector
C
Grounding Block
Chassis Height
4.34 cm (1.70 in.)   
Chassis Width 
44 cm (17.32 in.)
Chassis Depth 
29.5 cm (11.61 in.)
Chassis Weight
5.6 kg (12.35 lb)
Ambient Operating Temperature (Tmra)
-40°C to 75°C (-40°F to 167°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Power Consumption (idle)
60W
Input Power & Current
24-60Vdc, max. 3.5A
Input Range
50 - 57V: (3.5A), 150W max, PoE 802.3AT
44 - 57V: (3.5A), 120W max, PoE 802.3 AF
24 - 60V: (1.5A), Non-PoE, system only 
B
A
C

<<<PAGE 25>>>
OmniSwitch 6575 Chassis Details
Chassis and Power Supplies
page 3-6
OmniSwitch 6575 Hardware Users Guide
December 2025
OS6575-MP16
OS6575-MP16 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
Item
Description
A
Console - M12 A-code Connector (M)
B
USB 2.0 - M12 A-code Connector (M)
C
Alarm IN/OUT- M12 A-code Connector (M)
D
Power - M23 5-pin Connector (M)
E
(1-4) - 10/100 BaseT M12 D-code Ports (F) 
F
(5-8) - 10/100 BaseT IEEE 802.3at (30W) PoE M12 D-code Ports (F)
G
(9-12) - 10/100/1000 BaseT IEEE 802.3bt (60W) M12 X-code Ports (F) 
H
(13-16) - 10/100/1000 BaseT M12 X-code Ports (With Bypass function) (F)
LEDs
See “Chassis Status LEDs” on page 3-8
See “Pinouts and Cables” on page 3-34
Note:
- Under 48VDC, PoE not supported. 
- When connecting in dual-redundant power supply configuration, both power supplies must have 
identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could 
result in unexpected behavior and is not supported.
D
F
E
A
B
C
G
H

<<<PAGE 26>>>
Chassis and Power Supplies
OmniSwitch 6575 Chassis Details
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-7
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6575-MP16 Rear Panel
OS6575-MP16 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Internal temperature refers to the sensor reading of 
the internal switch temperature. Ambient temperature (Tmra) refers to the approximate room temperature. 
The ambient temperature will typically be lower than the internal temperature. 
Item
Description
A
Mounting Holes
Chassis Height
17.5 cm (6.89 in.)
Chassis Width 
27 cm (10.63 in.)
Chassis Depth 
8 cm (3.15 in.)
Chassis Weight
3.4 kg (7.50 lb)
Ambient Operating Temperature (Tmra)
-40°C to 75°C (-40°F to 167°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
System Power Consumption
50W
Input Power & Current
20V-110VDC

<<<PAGE 27>>>
OmniSwitch 6575 Chassis Details
Chassis and Power Supplies
page 3-8
OmniSwitch 6575 Hardware Users Guide
December 2025
Chassis Status LEDs
The chassis provides a series of status LEDs located on the front panel. These LEDs offer basic status 
information for hardware operation and port link and activity status.
LED
State
Description
OK
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
Blinking Amber
Off
This unit is the master unit
This unit is a slave unit
Identifies unit number by the number of 
blinks.
This unit is in shutdown mode or is not part of 
a VC.
PS
Solid Green
Solid Amber
Off
Main power supply and secondary power 
supply functioning normally.
Main power supply or secondary power 
supply functioning normally.
Power supply not present.
Alarm In
Alarm Out
Solid Red
Solid Red
Alarm input detected.
Alarm output detected.
See “Alarm Relay” on page 3-29.
EMP
Solid Green
Blinking Green
Valid port link
Valid port link with activity
GRN (Leaf)
Solid Green
Off
Power Saving Mode
Normal Operating Mode
M12 / RJ45
Solid Green
Blinking Green
Solid Amber
Blinking Amber
Valid port link (non-PoE)
Valid port link with activity (non-PoE)
Valid port link (PoE)
Valid port link with activity (PoE)

<<<PAGE 28>>>
Chassis and Power Supplies
OmniSwitch 6575 Chassis Details
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-9
Uplink / VFL
Solid Green
Blinking Green
Solid Amber
Blinking Amber
Valid uplink
Valid uplink with activity
Valid VFL link
Valid VFL link with activity
LED
State
Description

<<<PAGE 29>>>
Mounting the Switch
Chassis and Power Supplies
page 3-10
OmniSwitch 6575 Hardware Users Guide
December 2025
Mounting the Switch
General Mounting Recommendations
Elevated Operating Ambient Temperature. If installed in a closed or multi-rack assembly, the operating 
ambient temperature of the environment may be greater than the room’s ambient temperature. Therefore, 
consideration should be given to the maximum rated ambient temperature (Tmra) listed in the 
“OmniSwitch 6575 Chassis Details” section.
Reduced Air Flow. Installation of the equipment should be such that the amount of air flow required for 
safe operation of the equipment is not compromised. Refer to “Airflow / Clearance Recommendations” on 
page 3-11 for more information.
Mechanical Loading. Mounting of the equipment should be such that a hazardous condition is not 
achieved due to uneven loading.
Circuit Overloading. Consideration should be give to the connection of the equipment to the supply 
circuit and the effect that overloading of circuits could have on overcurrent protection and supply wiring. 
Reliable Earthing. Reliable earthing of equipment should be maintained. Particular attention should be 
given to supply connections other than direct connections to the branch (e.g., use of power strips).
Rack Mounting - OS6575-U28
1 Attach rack mount brackets to both sides of the chassis as shown. 
2 Mark the holes on the rack where the switch is to be installed.
3 Lift and position the switch until the rack-mount brackets are flush with the rack post, then align the 
holes in the brackets with the rack holes that were marked at step 1.

<<<PAGE 30>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-11
4 Once the holes are aligned, insert a rack mount screw (not provided) through the bottom hole of each 
bracket. Tighten both screws until they are secure.
Note. Be sure to install the screws in the bottom hole of each bracket, as shown, before proceeding.
5 Once the screws at the bottom of each bracket are secure, install the remaining two rack mount screws. 
Be sure that all screws are securely tightened.
Follow the recommended clearance requirements for the 
model being mounted.

<<<PAGE 31>>>
Mounting the Switch
Chassis and Power Supplies
page 3-12
OmniSwitch 6575 Hardware Users Guide
December 2025
Rack Mounting Rear - OS6575-U28
The OS6575-U28 chassis can be mounted from rear of the chassis. The parts required are contained in the 
kits below.
• OS6575-REAR-MNT - (2) Side Rails, (2) Rear Brackets, (1) Support Bracket, (18) M4X8MM (Flat)
• OS6575-TRAY-1U - (1) Power Supply Tray
1 Install the Side Rails, Rear Brackets, and Power Supply Tray.
Rails and Power Supply Tray (OS6575-REAR-MNT)
2 Install Power Supplies.
Side Rail
(7) M4X8MM
Holes ‘A’
Rear Brackets
Power Supply Tray 
(4) M4X8MM
Support Bracket
(3) M4X8MM
Side Rail
(7) M4X8MM
Holes ‘C’

<<<PAGE 32>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-13
Side Rails, Rear Brackets, and Power Supply Tray with Power Supplies
Thumb Screws

<<<PAGE 33>>>
Mounting the Switch
Chassis and Power Supplies
page 3-14
OmniSwitch 6575 Hardware Users Guide
December 2025
DIN Rail Mounting - OS6575-P12
The OmniSwitch-P12 is DIN rail mountable. 
DIN Rail Bracket Options
DIN Mounted Chassis

<<<PAGE 34>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-15
Wall Mounting - OS6575-P12
The OmniSwitch-P12 is wall mountable.
Wall Bracket Options

<<<PAGE 35>>>
Mounting the Switch
Chassis and Power Supplies
page 3-16
OmniSwitch 6575 Hardware Users Guide
December 2025
Wall Mounting - OS6575-MP16
The OmniSwitch-MP16 is wall mountable.

<<<PAGE 36>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-17
Power Supplies
OmniSwitch 6575 switches can use the following power supplies:
Please note that the chassis does not provide an on/off switch. Connecting a power supply to a power 
source will boot the switch. Likewise, disconnecting all installed power supplies from a power source will 
power off the switch.
Model
Chassis Supported
OS6NN5-BPNS (See page 3-18)
OS6575-P12
OS6NN5-BPNSX (See page 3-19)
OS6575-P12, OS6575-U28
OS6575-BPR (See page 3-20)
OS6575-U28
OS6575-BPRD (See page 3-21)
OS6575-U28

<<<PAGE 37>>>
Power Supplies
Chassis and Power Supplies
page 3-18
OmniSwitch 6575 Hardware Users Guide
December 2025
OS6NN5-BPNS AC Power Supply
150W AC Power Supply
LED States
Model
OS6NN5-BPNS (XDR-150E-48)
Models Supported
OS6575-P12
Input Voltage Range
85 - 260VAC
Input Frequency
47 - 63Hz
Input Current
2.6A/115VAC 
1.6A/230VAC
Output Voltage
54.5VDC
Output Current
2.25A/115VAC
2.8A/230VAC
Output Power
115VAC/122.6W
230VAC 152.6W
Max. Output for PoE Power
See “Power over Ethernet Budget”.
LED State
Description
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue

<<<PAGE 38>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-19
OS6NN5-BPNSX AC Power Supply
480W AC Power Supply
LED States
Model
OS6NN5-BPNSX (XDR-480E-48)
Models Supported
OS6575-P12, OS6570-U28
Input Voltage Range
85 - 264VAC 
Input Frequency
47-63Hz
Input Current
6A/115VAC 
3A/230VAC
Output Voltage
54.5VDC
Output Current
8.8A
Output Power
480W
Max. Output for PoE Power
See “Power over Ethernet Budget”.
LED State
Description
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue

<<<PAGE 39>>>
Power Supplies
Chassis and Power Supplies
page 3-20
OmniSwitch 6575 Hardware Users Guide
December 2025
OS6575-BPR Power Supply
LED States
Model
OS6575-BPR (PS-I180AC-P)
Description
Modular AC power supply. Up to two (2) power supplies 
may be installed.
Dimensions (H x W x L)
5.1 cm x 9.5 cm x 18.1 cm (2 in x 3.74 in x7.12 in)
Weight
1.36 kg (3.00 lbs)
Models Supported
OS6575-U28
Input Voltage / Current / Hz
100 VAC to 240 VAC / 3 A - 1.5 A / 50-60 Hz
Output Voltage / Current
+56 VDC / 3.22 A 
Status LEDs
Solid Green indicates normal operation
Max. Output for PoE Power
See “Power over Ethernet Budget”.
LED State
Description
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue
Power Supply Front
Power Supply Rear

<<<PAGE 40>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-21
OS6575-BPRD 180W DC Power Supply
LED States
Model
OS6575-BPRD (PS-I180DC-P)
Description
Modular DC power supply. Up to two (2) power supplies 
may be installed.
Dimensions (H x W x L)
5.1 cm x 9.5 cm x 18.1 cm (2 in x 3.74 in x7.12 in)
Weight
1.44 kg (3.17 lbs)
Models Supported
OS6575-U28
Input Voltage / Current 
-20 VDC to -28 VDC / 12A
-36 VDC to -72 VDC/ 6A
Output Voltage / Current
-56V/2.5A (140W)
-56V/3.22A (180W)
Status LEDs
Solid Green indicates normal operation
Max. Output for PoE Power
See “Power over Ethernet Budget”.
LED State
Description
DC OK LED Solid Green
DC power is good
DC OK LED Solid Red
There is a DC power issue
Power Supply Front
Power Supply Rear

<<<PAGE 41>>>
Power Supplies
Chassis and Power Supplies
page 3-22
OmniSwitch 6575 Hardware Users Guide
December 2025
Installing Power Supplies for Rear Mount Trays
1.
Orient the power supply as shown below. Insert the guide pins (located on either side of the DB-15 
connector) into the guide holes in the rear of the chassis. 
Align power supply guide pins and slide into postion
2.
Push the power supply into place until the connector is fully seated and tighten the thumb screw at 
the front of the power supply unit.
Secure power supply with thumb screw
3.
For redundant power supply configurations, repeat these steps using the power supply connector 
and thumb screw hole located at the other side of the chassis and power supply tray.
Hole for Guide Pin

<<<PAGE 42>>>
Chassis and Power Supplies
Connecting the AC Power Supplies
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-23
Connecting the AC Power Supplies
Connecting the Removed Outer Jacket (ROJ) Power Cords
AC Input Wire Color and Cord Type
DC Output Wire Color
Parts Required
Only parts provided by Alcatel-Lucent Enterprise should be used when installing the power supplies. 
The PoE power supply uses both an input and output power cord with Removed Outer Jackets (ROJ): 
• An AC power cord that provides input power from an AC power source to the power supply.
• An output power cord that provides output power from the power supply to the chassis.
AC ROJ Input Power Cord
DC ROJ Output Power Cord
Power Supply Label
North America Wire 
Color
International Wire Color
L (Line)
Black (30mm ROJ)
Brown (30mm ROJ)
N (Neutral)
White (30mm ROJ)
Blue (30mm ROJ)
Protective Ground (PG) 
Green (33mm ROJ)
Green/Yellow Stripe (33mm ROJ)
Power Supply Label
North America and International (Use same 
power cord)
V-
Red (ROJ)
V+
Black (ROJ)
Protective Ground (PG)
Green (ROJ with grounding lug)
Red (V-)
Green with ring (Ground)
Black (V+)
Red (V-)
Green (Ground)
Black (V+)

<<<PAGE 43>>>
Connecting the AC Power Supplies
Chassis and Power Supplies
page 3-24
OmniSwitch 6575 Hardware Users Guide
December 2025
DB15 to 3-Wire Power Cord for OS6575-U28
Warning. Do not insert the NEMA 5-15 plug or power connector into the power supply or any live power 
source until prompted to do so. Failure to follow these instructions may result in bodily injury and/or 
equipment damage.
Be sure to properly install the power cords by following the steps below.
1 To install the output power cord, begin by inserting the RED wire into either of the V- terminals 
located at the top-front of the power supply and the negative terminal (-) on the switch power supply 
connector.
2 Next, insert the BLACK wire into either of the V+ terminals on the power supply and the positive (+) 
terminal on the switch power supply connector.
3 Using a screwdriver torque each terminal to approximately 3.5 inch-pounds. 
Red (V-)
Black (V+)
Green with ring (Ground)
DB15 Connector

<<<PAGE 44>>>
Chassis and Power Supplies
Connecting the AC Power Supplies
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-25
4 Secure the remaining ground wire to the power supply using the supplied attachment screw. Insert the 
screw through the ground wire connector and tighten firmly. Connect other end to ground terminal on 
switch power connector. 
Output Power Terminal Locations
OS6NN5-BPNSX
OS6NN5-BPNS
Connection Examples
Top-Front of Power Supply - Example only. Terminal 
and ground locations will differ based on power supply. 
V-
V+
+ -
Clamp inside square hole will open
when screw is loosened.
Loosen Screw.
Switch Connections
Power Supply Connections
Black
Red
Green

<<<PAGE 45>>>
Connecting the AC Power Supplies
Chassis and Power Supplies
page 3-26
OmniSwitch 6575 Hardware Users Guide
December 2025
5 To connect the AC power cord, begin by inserting the BLACK (North America) or BROWN (Interna-
tional) wire into the Line (L) terminal located at the bottom-front of the power supply.
6 Next, insert the WHITE (North America) or BLUE (International) wire into the Neutral (N) terminal.
7 Insert the GREEN (North America) or GREEN/YELLOW stripe (International) ground wire into the 
terminal marked with the protective ground symbol.
Input Power Terminal Locations (North America wire color shown)
8 Using a screwdriver torque each terminal to the inch-pounds labeled on the power supply. 
Final Power Cord Connections
1 Insert the output power cord into the power connector (PS1 or PS2) located on the front of chassis (if 
required). 
2 Plug the AC power cord’s NEMA 5-15 into an easily accessible AC power source.
Caution. The product uses a Pluggable Type A power cord; therefore, please make sure that the power 
socket is located near the equipment and is easily accessible. 
Bottom-Front of Power Supply
N
L

<<<PAGE 46>>>
Chassis and Power Supplies
Connecting the AC Power Supplies
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-27
Configuring a Power Supply
The OmniSwitch 6575 cannot auto-detect the type of power supply connected. The type of power supply 
connected must be configured so that the system and PoE power information is correctly displayed and 
utilized. Use the powersupply type command to configure the power supply, for example:
-> powersupply 1 name ALE-75W-ps1 type ale lo-ac
-> powersupply 2 name ALE-75W-ps2 type ale lo-ac
Hot-Swapping / Removing a Power Supply
Follow the steps below to remove a power supply. Please note that if the chassis is running with redun-
dant power supplies, either one of the power supplies can be replaced without affecting chassis operation 
(hot-swap). 
1 Unplug the power supply from the power source. 
2 Disconnect the AC input power cord from the power supply by loosening all terminal connectors and 
disconnecting the wires from the power supply. 
3 Disconnect the output power cord from the power supply by loosening all terminal connectors and 
disconnecting the wires from the power supply. 
4 Reconnect the new power supply by following the steps provided in “Connecting the AC Power 
Supplies”

<<<PAGE 47>>>
Grounding the Chassis
Chassis and Power Supplies
page 3-28
OmniSwitch 6575 Hardware Users Guide
December 2025
Grounding the Chassis
The switch has a grounding lug located on the front or rear of the chassis. This lug uses 10-32 screws and 
is surrounded by a small paint-free area, which provides metal-to-metal contact for a ground connection.
Use this connector to supplement the ground provided by the AC power cord. To do so, install a Panduit 
Grounding Lug (type LCD8-10A-L) using 8AWG copper conductors to the paint-free area. Torque to 
between 30-60 inch pounds.
Refer to the chassis views on page 3-2 for location details.

<<<PAGE 48>>>
Chassis and Power Supplies
Alarm Relay
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-29
Alarm Relay
The alarm relay feature is used for notification whenever there is a system event on the switch or an alarm 
input. Notification is either by an alarm output, trap or by logging a SWLog message. 
There is a single line alarm input to the switch which can be connected to an external source. External 
sources can be temperature, proximity, door open sensors as examples. The alarm input status is also indi-
cated to the user by the alarm input LED. 
There is a single line alarm output from the switch. The alarm output is user configurable for associating 
any system event or an alarm input. Alarm output status is also indicated to the user by the alarm output 
LED. 
Alarm relay is supported on both standalone and virtual chassis (VC).
On standalone system: The alarm input, traps, and system events are mapped to the local chassis alarm 
output. 
On VC: The alarm input, traps, and system events are synced across all the chassis of the VC. The alarm 
output on any of the chassis can be set by the alarm input, trap, or system events of any other chassis. 
• User can connect different external devices (sensors) to alarm inputs of different chassis.
• User can map the single alarm input or event to multiple chassis alarm outputs for redundancy.
• User can map multiple inputs or events to single alarm output on any chassis.
The alarm status is indicated to the user by the alarm LEDs as noted below:
Use the alarm command to configure the alarm relay feature.
Events
Input LED
Output LED
Alarm input with action alarm output
On
On
Alarm input with action trap
On
Off
Alarm input with action SWLog
On
Off
Alarm output due to system events
Off
On
Alarm
 Specifications
Connector
Alarm Relay Input
Input range: 5VDC 5- 12VDC
1 - Positive
2 - Ground
Alarm Relay Output
- Max Switching Voltage - 220VDC, 250VAC
- Max Switching / Carrying Current - 2 A
- Max Power - 60W
1 - Normally Open (NO)
2 - Common (C)
3 - Normally Closed (NC)

<<<PAGE 49>>>
Alarm Relay
Chassis and Power Supplies
page 3-30
OmniSwitch 6575 Hardware Users Guide
December 2025
Alarm Relay Configuration Examples
The following shows an example of configuring an alarm-out action based on the alarm relay input being 
activated. The alarm-out action will trigger the alarm relay output.
-> alarm in temperature-alarm-in action alarm-out admin-state enable
-> alarm out alarm-out-1 admin-state enable
-> alarm map temperature-alarm-in out alarm-out-1
The following shows an example of how to map an ‘authentication-failure’ event to trigger the alarm 
output relay. 
-> alarm event auth-fail-event event authentication-failure admin-state enable
-> alarm out set-alarm-out-chassis-1
-> alarm map auth-fail-event out set-alarm-out-chassis-1
-> show alarm event config
Alarm Duration 24 hrs 0 Mins
Alarm-Name     Chassis-in  Network-Port  Trap-Id  Event-Name   Admin-State Alarm-Output-Name   Chassis-out
--------------+-----------+-------------+--------+-----------+--------------+--------------------+-------
auth-fail-event  1          -          -      authentication-failure  enable set-alarm-out-chassis-1  1
If there is an authentication failure detected on Chassis 1, the alarm output relay will be triggered, the LED 
for the alarm output relay will be turned on and the alarm will be logged as seen below. 
-> show alarm status
Alarm-Name    Chassis-in   Time-Stamp  Network-Port Trap-Id Event-Name Alarm-Output-Name       Chassis-out
--------------+------+------------+-------------+-----------+-----+-----------------------+-----------
auth-fail-event 1      03/01/14 : 01:18:51    -   -    authentication-failure set-alarm-out-chassis-1  1
To clear the alarm the alarm clear status command can be used. 
-> alarm clear status 
Alarm Relay Output Wiring Diagram Example
When the alarm relay output is triggered, the
normally open (NO) contact will close and
the normally closed (NC) contact will open.

<<<PAGE 50>>>
Chassis and Power Supplies
Monitoring Chassis Components
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-31
Monitoring Chassis Components
Viewing Chassis Slot Information
To view basic slot information, enter the show module command at the CLI prompt:
-> show module
To view more detailed information, use the show module long command:
-> show module long
Monitoring Chassis Temperature
The operating temperature of your switch is a critical factor in its overall operability. In order to avoid a 
temperature-related system failure, your switch must always run at a temperature within the specified 
operating temperature range. 
To avoid chassis over-temperature conditions, follow the important chassis airflow recommendations on 
page 3-11.
To check the switch’s current temperature status, use the show temperature command. For example:
-> show temperature
Chassis/Device | Current |  Range     | Danger | Thresh |  Status
---------------+---------+------------+--------+--------+-----------------
 1/CMMA            33      -45 to 93     98       93     UNDER THRESHOLD
For more information about this command, see the “Chassis Management and Monitoring Commands” 
chapter in the OmniSwitch CLI Reference Guide.
Temperature Errors
The switch monitors the chassis temperature at all times via an onboard sensor. If an over-temperature 
condition occurs, there are two different levels of error severity:
• Warning threshold (Thresh) temperature has been exceeded
• Danger threshold has been exceeded
Warning Threshold Temperature
If the temperature exceeds the switch’s Warning threshold, the switch sends out a trap. Traps are also 
printed to the console in the form of text error messages.
When the Warning threshold has been exceeded, switch operations remain active. However, it is 
recommended that immediate steps be taken to address the over-temperature condition.
Addressing Warning threshold conditions may include:
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature

<<<PAGE 51>>>
Monitoring Chassis Temperature
Chassis and Power Supplies
page 3-32
OmniSwitch 6575 Hardware Users Guide
December 2025
Danger Threshold
If the chassis temperature rises above the Danger threshold, the switch will power off until the temperature 
conditions have been addressed and the switch is manually booted. The Danger threshold is factory-set 
and cannot be configured by the user.
Addressing the Danger threshold conditions may include:
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature

<<<PAGE 52>>>
Chassis and Power Supplies
Dying Gasp
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-33
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

<<<PAGE 53>>>
Pinouts and Cables
Chassis and Power Supplies
page 3-34
OmniSwitch 6575 Hardware Users Guide
December 2025
Pinouts and Cables
M23 (Power) Pinout
M12 A-Code (USB) Pinout
M12 A-Code (Console) Pinout
M12 A-Code (Alarm) Pinout
Pin Number
Signal
No. 1
PWR-1+
No. 2
PWR-1-
No. 3
FGND
No. 4
PWR-2+
No. 5
PWR-2-
Pin Number
Signal
No. 1
D+
No. 2
D-
No. 3
VCC 5V
No. 4
GND
No. 5
N/A
Pin Number
Signal
No. 1
TX
No. 2
RX
No. 3
N/A
No. 4
GND
No. 5
N/A
Pin Number
Signal
No. 1
D+
No. 2
D-
No. 3
DO-NO
No. 4
DO-NC
No. 5
DO Comm

<<<PAGE 54>>>
Chassis and Power Supplies
Pinouts and Cables
OmniSwitch 6575 Hardware Users Guide
December 2025
page 3-35
M12 D-Code (Without PoE) Pinout
M12 X-Code (With PoE) Pinout
M12 D-Code (With PoE) Pinout
Pin Number
Signal
No. 1
TX+
No. 2
RX+
No. 3
TX-
No. 4
RX-
Housing
Shield
Pin Number
Signal
PoE
No. 1
TXD1+
PoE- (G1)
No. 2
TXD1-
PoE- (G1)
No. 3
RXD2+
PoE+ (G1)
No. 4
RXD2-
PoE+ (G1)
No. 5
BID4+
PoE- (G2)
No. 6
BID4-
PoE- (G2)
No. 7
BID3-
PoE+ (G2)
No. 8
BID3+
PoE+ (G2)
Housing
Shield
Pin Number
Signal
PoE
No. 1
TX+
PoE+
No. 2
RX+
PoE-
No. 3
TX-
PoE+
No. 4
RX-
PoE-
Housing
Shield

<<<PAGE 55>>>
Pinouts and Cables
Chassis and Power Supplies
page 3-36
OmniSwitch 6575 Hardware Users Guide
December 2025
M12 X-Code (Without PoE) Pinout
Accessory Cables
Pin Number
Signal
No. 1
TXD1+
No. 2
TXD1-
No. 3
RXD2+
No. 4
RXD2-
No. 5
BID4+
No. 6
BID4-
No. 7
BID3-
No. 8
BID3+
Housing
Shield
Part Number
Description
M23-PWRCONN-5P 
M23 6-PIN (F) POWER CONN (W/O CABLE) 5PK
M12-USB-2P
M12 5-PIN A-CODE (F) To USB PLUG, 0.5M 2PK
M12-CONSOLE-5P
M12 5-PIN A-CODE (F) To RS232 (F), 1M 5PK 
M12-ALARM-6P
M12 5-PIN A-CODE (F) To BARE CABLE, 1M 6PK
M12-DC-M-8P
M12 4-PIN D-CODE (M) To M12 4-PIN D-CODE (M), 0.5M 8PK 
M12-DC-RJ45F-8P
M12 4-PIN D-CODE (M) To RJ45 (F), 0.5M 8PK 
M12-DC-RJ45M-8P
M12 4-PIN D-CODE (M) To RJ45 (M), 0.5M 8PK 
M12-XC-M-8P
M12 8-PIN X-CODE (M) To M12 8-PIN X-CODE (M) , 0.5M 8PK 
M12-XC-RJ45F-8P
M12 8-PIN X-CODE (M) To RJ45 (F), 0.5M 8PK 
M12-XC-RJ45M-8P
M12 8-PIN X-CODE (M) To RJ45 (M), 0.5M 8PK

<<<PAGE 56>>>
OmniSwitch 6575 Hardware Users Guide
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
As the switches fully support Ethernet connectivity, you may also attach non-PD equipment, such as 
computer workstations, printers, servers, etc. to the PoE ports. 
Important. It’s recommended that PoE-enabled switches with attached IP telephones should have opera-
tional power supply redundancy at all times for 911 emergency requirements. In addition, both the switch 
and the power supply should be plugged into an Uninterruptible Power Source (UPS).

<<<PAGE 57>>>
In This Chapter
Managing Power over Ethernet (PoE)
page 4-2
OmniSwitch 6575 Hardware Users Guide
December 2025
In This Chapter
This chapter provides specifications and descriptions of hardware and software used to provide PoE for 
attached devices. 
The chapter also provides information on configuring PoE settings on the switch through the Command 
Line Interface (CLI). CLI commands are used in the configuration examples; for more details about the 
syntax of commands, see the OmniSwitch CLI Reference Guide. Topics and configuration procedures 
described in this chapter include:
• Power over Ethernet Specifications on page 4-3
• Viewing Power Status on page 4-6
• Configuring Power over Ethernet Parameters on page 4-4
• Understanding Priority Disconnect on page 4-13
• Monitoring Power over Ethernet via the CLI on page 4-16
Note. Before PoE functionality can be configured the type of power supply connected must be config-
ured. See “Configuring a Power Supply” for additional information.

<<<PAGE 58>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Specifications
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-3
Power over Ethernet Specifications
The table below lists general specifications for Alcatel-Lucent’s Power over Ethernet support. For more 
detailed power supply and Power Source Equipment (PSE) specifications, refer to Chapter 3, “Chassis and 
Power Supplies.” .
IEEE Standards supported
IEEE 802.3at, 802.3bt
PoE Class Detection
Supported
Platforms supporting PoE
OS6575-P12, OS6575-U28, OS6575-MP16
Range of inline power per port
802.3at ports - 3000-30000 milliwatts
802.3ab ports - 3000-90000 milliwatts
Maximum PoE power per slot
See “Power over Ethernet Budget”.

<<<PAGE 59>>>
Power over Ethernet Defaults
Managing Power over Ethernet (PoE)
page 4-4
OmniSwitch 6575 Hardware Users Guide
December 2025
Power over Ethernet Defaults
The following table lists the defaults for PoE configuration:
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
802.3at ports (HPoE) - 60000 milliwatts
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

<<<PAGE 60>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-5
Power over Ethernet Budget
The following table lists the Power over Ethernet wattages available based on the number and types of power 
supplies installed and the ambient temperature.
OmniSwitch 6575-P12 PoE Budget
OmniSwitch 6575-U28 PoE Budget
OmniSwitch 6575-P12
(1) OS6NN5-BPNS 
150W AC
(2) OS6NN5-BPNS 
150W AC
< = 50°C
52W
52W
> 50°C and < 60°C
33W
33W
> 60°C and < 70°C
24W
24W
> 70°C and < 75°C
15W
15W
(1) OS6NN5-BPNSX 
480W AC
(2) OS6NN5-BPNSX 
480W AC
< = 50°C
330W
360W
> 50°C and < 60°C
280W
360W
> 60°C and < 70°C
238W
360W
> 70°C and < 75°C
140W
180W
OmniSwitch 6575-U28
(1) OS6575-BPR(D)
180W AC/DC
(2) OS6575-BPR(D)
180W AC/DC
< = 50°C
75W
210W
> 50°C and < 60°C
45W
150W
> 60°C and < 70°C
30W
110W
> 70°C and < 75°C
15W
75W
(1) OS6NN5-BPNSX 
480W AC
(2) OS6NN5-BPNSX 
480W AC
< = 50°C
120W
120W
> 50°C and < 60°C
120W
120W
> 60°C and < 70°C
120W
120W
> 70°C and < 75°C
120W
120W

<<<PAGE 61>>>
Power over Ethernet Budget
Managing Power over Ethernet (PoE)
page 4-6
OmniSwitch 6575 Hardware Users Guide
December 2025
OmniSwitch 6575-MP16 PoE Budget
OmniSwitch 6575-MP16
(1) 150W Power Supply
(2) 150W Power Supply
< = 50°C
52W
52W
> 50°C and < 60°C
33W
33W
> 60°C and < 70°C
24W
24W
> 70°C and < 75°C
15W
15W
(1) 480W Power Supply
(2) 480W Power Supply
< = 50°C
120W
120W
> 50°C and < 60°C
120W
120W
> 60°C and < 70°C
120W
120W
> 70°C and < 75°C
120W
120W
PoE budget for 3rd party power supplies is dependent upon input wattage and voltage. 
- For PoE support 48V or higher is required.
- Examples provided based on 150W and 480W input.

<<<PAGE 62>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-7
Viewing Power Supply Status
To view the type and status for installed power supplies, use the show powersupply command:
-> show powersupply
Total     PS
Chassis/PS   Power     Type     Status   Location
-----------+---------+--------+--------+-----------
 1/1         75        AC       UNPLUG   Internal
    Total   75

<<<PAGE 63>>>
Power over Ethernet Budget
Managing Power over Ethernet (PoE)
page 4-8
OmniSwitch 6575 Hardware Users Guide
December 2025
Viewing PoE Status
To view current PoE status and settings, use the show lanpower slot command:
Port Maximum(mW) Actual Used(mW)   Status    Priority   On/Off   Class   Type
----+-----------+---------------+-----------+---------+--------+-------+----------
  1     60000            0       Powered Off    Low      OFF       .
  2     30000            0       Powered Off    Low      OFF       .
  3     60000            0       Powered Off    Low      OFF       .
  4     30000            0       Powered Off    Low      OFF       .
ChassisId 1 Slot 1 Max Watts 45
0 Watts Actual Power Consumed
0 Watts Total Power Budget Used
45 Watts Total Power Budget Available
1 Power Supply Available
'*' appending port maxpower indicates 4pair port operating in 2pair mode
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
Although class-detection is disabled by default, the switch still provides power to incoming PDs (if avail-
able in the power budget). However, to strictly enforce class detection as specified in the 802.3at standard, 
class detection must be enabled using the lanpower slot class-detection command.
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

<<<PAGE 64>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-9
Enabling class detection will reset all PoE ports on the chassis.
PoE Operational Status
Enabling PoE
By default, Power over Ethernet is administratively enabled in the switch’s system software. However, in 
order to physically activate PoE, you must issue the lanpower slot service command on a slot-by-slot 
basis before any connected PDs will receive inline power.
To activate power to PoE-capable in a switch, enter the corresponding slot number only. For example:
-> lanpower slot 1/1 service start
If power to a particular port has been administratively disconnected, you can reactivate power to the port 
using the lanpower port admin-state command. For example:
-> lanpower port 1/1/1-4 admin-state enable
Note. You cannot use the lanpower port admin-state command to initially activate PoE on a port. This 
syntax is intended only to reactivate power to those that have been disconnected via the lanpower slot 
service command. To initially activate PoE, you must use the lanpower slot service command as 
described above.
Disabling PoE
To disable PoE on a particular port, use the lanpower port admin-state command. For example:
-> lanpower port 1/1/4 admin-state disable
To disable PoE for all PoE-capable ports in a slot, use the lanpower slot service command. For example:
-> lanpower slot 1/1 service stop
Configuring the Total Power Available to a Port
By default, each port is authorized by the system software to use up to a maximum amount of milliwatts to 
power any attached device. 
You can either increase or decrease this value based on the allowed ranges.
Increasing the total power available to an individual port may provide a more demanding Powered Device 
(PD) with additional power required for operation. Decreasing the total power available to a port helps to 
preserve inline power and assists in the overall management of the switch’s power budget.
To increase or decrease the total power available to an individual port, use the lanpower power 
command. Since you are setting the power allowance for an individual port, you must specify chassis/slot/
port values in the command line. For example, the syntax
-> lanpower port 1/1/4 power 3000
reduces the power allowance on the port to 3000 milliwatts. This new value is now the maximum amount 
of power the port can use to power any attached device (until the value is modified by the user).

<<<PAGE 65>>>
Power over Ethernet Budget
Managing Power over Ethernet (PoE)
page 4-10
OmniSwitch 6575 Hardware Users Guide
December 2025
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
-> lanpower slot 1/1 maxpower 400
reduces the power allowance of the slot to 400 watts. This value is now the maximum amount of power 
the slot can use to power all attached devices (until the value is modified by the user).
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
-> lanpower port 1/1/4 priority critical
changes the priority value of the port to the highest priority level of critical. Now that the default value has 
been reconfigured, this port should be reserved for those PDs that are mission critical for network opera-
tions.

<<<PAGE 66>>>
Managing Power over Ethernet (PoE)
Power over Ethernet Budget
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-11
Setting the Capacitor Detection Method
By default, the capacitor detection method is disabled. To enable it, use the lanpower capacitor-detec-
tion. For example:
-> lanpower slot 3/1 capacitor-detection enable
Note. The capacitive detection method should only be enabled to support legacy IP phones. This feature 
is not compatible with IEEE specifications. Please contact your Alcatel-Lucent sales engineer or Customer 
Support representative to find out which Alcatel-Lucent IP phones models need capacitive 
detection enabled.

<<<PAGE 67>>>
Understanding Guard Band
Managing Power over Ethernet (PoE)
page 4-12
OmniSwitch 6575 Hardware Users Guide
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
Please refer to the “Understanding Priority Disconnect” on page 4-13 for additional details.

<<<PAGE 68>>>
Managing Power over Ethernet (PoE)
Understanding Priority Disconnect
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-13
Understanding Priority Disconnect
The priority disconnect function differs from the port priority function described on page 4-10 in that it 
applies only to the addition of powered devices (PDs) in tight power budget conditions. Priority discon-
nect is used by the system software in determining whether an incoming PD will be granted or denied 
power when there are too few watts remaining in the PoE power budget for an additional device. For 
example, if there are only 2 watts available in the current PoE power budget and a user plugs a 3.5W 
powered device into a PoE port, the system software must determine whether the device will be powered 
on. Based on priority disconnect rules, in some cases one or more existing devices may be powered down 
in order to accommodate the incoming device. In other cases, the incoming device will be denied power.
Priority disconnect rules involve the port priority status of an incoming device (i.e., low, high, and criti-
cal), as well as the port’s physical port number (i.e., 1–8). Understanding priority disconnect rules is espe-
cially helpful in avoiding power budget deficits and the unintentional shutdown of mission-critical devices 
when PDs are being added in tight power budget conditions. For detailed information on how priority 
disconnect uses port priority and port number criteria for determining the power status of incoming PDs, 
refer to the illustrated examples on pages 4-14 through 4-15.
Reminder. Priority disconnect applies only when there is inadequate power remaining in the power 
budget for an incoming device.
For information on setting the priority disconnect status, refer to the section below. For information on 
setting the port priority status (a separate function from priority disconnect), refer to “Setting Port Priority 
Levels” on page 4-10.

<<<PAGE 69>>>
Understanding Priority Disconnect
Managing Power over Ethernet (PoE)
page 4-14
OmniSwitch 6575 Hardware Users Guide
December 2025
Setting Priority Disconnect Status
By default, priority disconnect is enabled in the switch’s system software. For information on changing the 
priority disconnect status, refer to the information below.
Disabling Priority Disconnect
When priority disconnect is disabled and there is inadequate power in the budget for an additional device, 
power will be denied to any incoming PD, regardless of its port priority status (i.e., low, high, and critical) 
or physical port number (i.e., 1–8).
To disable priority disconnect, use the lanpower slot priority-disconnect command. For example: 
-> lanpower slot 2/1 priority-disconnect disable
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
Port Number
1 (Highest) -> 8 (Lowest)

<<<PAGE 70>>>
Managing Power over Ethernet (PoE)
Understanding Priority Disconnect
OmniSwitch 6575 Hardware Users Guide
December 2025
page 4-15
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
Priority Disconnect is Disabled
Reminder. Priority disconnect examples are applicable only when there is inadequate power remaining to 
power an incoming device.
When priority disconnect is disabled, power will be denied to any incoming PD, regardless of its port 
priority status (i.e., low, high, and critical) or physical port number (i.e., 1–8).

<<<PAGE 71>>>
Monitoring Power over Ethernet via CLI
Managing Power over Ethernet (PoE)
page 4-16
OmniSwitch 6575 Hardware Users Guide
December 2025
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
-> show lanpower 1/1
Port Maximum(mW) Actual Used(mW)   Status    Priority   On/Off    Class
----+-----------+---------------+-----------+---------+--------+-------
  1     60000        12500       Powered On     Low      ON        0
2     30000         1800       Powered On     Low      ON        1
3     60000         3500       Powered On     Low      ON        2
4     30000         9800       Powered On     Low      ON        3
5     60000        25000       Powered On     Low      ON        4
6     30000            0       Undefined      Low      ON        -
7     60000            0       Undefined      Low      ON        -
8     30000            0       Undefined      Low      ON        -
Slot 3 Max Watts 150
1 Power Supplies Available
Note. For detailed information on show lanpower command output, refer to the OmniSwitch CLI Refer-
ence Guide.

<<<PAGE 72>>>
OmniSwitch 6465 Hardware Users Guide
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
2014/30/EU (EMC), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/EEC (équipements 
terminaux de télécommunications, le cas échéant), 2014/53/EU (R&TTE, le cas échéant). 
Deutsch: Diese Ausrüstung erfüllt die wesentlichen Anforderungen und sonstigen Bestimmungen der 
Richtlinien 2014/30/EU (EMV-Richtlinie), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/
EEC (Telekommunikationsendeinrichtungen, falls zutreffend), 2014/53/EU (Funkanlagen und Telekom-
munikationsendeinrichtungen, falls zutreffend). 
Español: Este equipo cumple los requisitos esenciales y otras disposiciones de las directivas 2014/30/EU 
(EMC), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/EEC (equipos terminales de teleco-
municación, si procede), 2014/53/EU (R&TTE, si procede). 
Waste Electrical and Electronic Equipment (WEEE) 
Statement
The product at end of life is subject to separate collection and treatment in the EU Member States, Norway 
and Switzerland and therefore marked with the following symbol:
Treatment applied at end of life of the product in these countries shall comply with the applicable national 
laws implementing directive 2002/96/EC on waste electrical and electronic equipment (WEEE).

<<<PAGE 73>>>
China RoHS: Hazardous Substance Table
Regulatory Compliance and Safety Information
page A-2
OmniSwitch 6465 Hardware Users Guide
December 2025
China RoHS: Hazardous Substance Table

<<<PAGE 74>>>
Regulatory Compliance and Safety Information
Taiwan RoHS: Hazardous Substance Table
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-3
Taiwan RoHS: Hazardous Substance Table
California Proposition 65 Warning
WARNING: This product can expose you to chemicals including Pb and Pb compounds, which is known 
to the State of California to cause cancer and birth defects or other reproductive harm. For more 
information go to www.P65Warnings.ca.gov.
Products are packaged using one or more of the following packaging materials:
Corrugated Cardboard                Corrugated Fiberboard              Low-Density Polyethylene
CB
FB

<<<PAGE 75>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-4
OmniSwitch 6465 Hardware Users Guide
December 2025
Standards Compliance
The product bears the CE mark. In addition it is in compliance with the following other safety and 
EMC standards.
Note. All hardware switching modules used in an OmniSwitch switch comply with Class A 
standards. Modules with copper connectors meet Class A requirements using unshielded (UTP) cables.
Safety Standards
• US UL 60950-1
• IEC 60950-1 Health and Safety
• CAN/CSA-C22.2 No. 60950-1-03
• NOM-019 SCFI, Mexico
• AS/NZ TS-001 and 60950:2000, Australia
• UL-AR, Argentina
• UL-GS Mark, Germany
• CU, EAC, Russia
• EN 60825-1 Laser
• EN 60825-2 Laser
• CDRH Laser
• IEC 60950-1/EN 60950 with all country
• deviations
• IEC 60950-1:2005, Second Edition
• CCC, China
• ANATEL, Brazil (Contact for availability)
• BSMI, Taiwan
• KCC, Korea (Contact for availability)
EMI/EMC Standards
• FCC Part 15:2012, Subpart B, Class A
• ICES–003:2012 Issue 5, Class A
• ANSI C63.4-2009
• FCC CRF Title 47 Subpart B (Class A)
• VCCI (Class A)
• AS/NZS 3548 (Class A)

<<<PAGE 76>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-5
• CE marking for European countries (Class A)
• EN 55032 (EMI & EMC)
• EN 61000-3-2
• EN 61000-3-3
• EN 55024 (Immunity)
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
• IEC 60068-2-1
• IEC 60068-2-2
• IEC 60068-2-30
• IEC 60068-2-13
• IEC 60068-2-40
• IEC 60068-2-41
• IEC 6068-2-6
• IEC 60068-2-64
• IEC 60068-2-27
• GR-63-CORE
• MIL-STD-810F Method 516.5 IV
• MIL-STD-810F Method 516.5 C

<<<PAGE 77>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-6
OmniSwitch 6465 Hardware Users Guide
December 2025
Industrial Compliance Requirements
Safety
• ISA 12.12.01 (UL 1604), CSA22.2/213, UL 508, EN50021
Operational Temperature
• IEC 60870-2-2 (operational temperature)
• IEC 60068-2-1 (temperature type test - cold)
• IEC 60068-2-2 (temperature type test - hot)
Storage Temperature
• IEC 60721-3-1: Class 1K5 (storage temperature)
Humidity
• IEC 60068-2-30: 5% to 95% non-condensing humidity
Mechanical Shock
• IEC 60255-21-2 (mechanical shock)
Vibration
• IEC 60255-21-1 (vibration)
Drop Test
• IEC 60870-2-2 Free Fall
Altitude Test 
• IEC 60870-2-2, GR-63-CORE, 4.1.3, 4.5
IPX
• IPXX, IEC60529
EMI/EMC
• IEC 61000-6-2 (Immunity), EN 61000-6-4 (Emission), EN 55032, EN 61000-3-3, EN 61000-3-2, EN 
55024, IEC 61850-3, EN 61000-4-2 to EN 61000-4-6,EN 61000-4-8, EN 61131-2 IEEE 1613, Section 
5.2, 5.3, 6.3.1, 6.3.2, 7, 8
DNV 
• DNV 2.4
Railway
• EN 50121-4, IEC 62236-4, EN 61000-6-4
NEMA 
• NEMA TS-2

<<<PAGE 78>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-7
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

<<<PAGE 79>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-8
OmniSwitch 6465 Hardware Users Guide
December 2025
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
Korea Emissions Statement
VCCI
This is a Class A product based on the standard of the Voluntary Control Council for Interference by 
Information Technology Equipment (VCCI). If this equipment is used in a domestic environment, radio 
disturbance may arise. When such trouble occurs, the user may be required to take corrective actions.
Class A Warning for Taiwan (BSMI) and Other Chinese Markets
Warning: To avoid electromagnetic interference, this product should not be installed or used in residential 
environments.
警告：為避免電磁干擾，本產品不應安裝或使用於住宅環境
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

<<<PAGE 80>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-9
Class 1M Laser Warning
CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL 
INSTRUMENTS.
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
NEBS-GR-1089-CORE Guidelines and Regulatory Compliance 
Statements
WARNING: The intra-building port(s) of the equipment or subassembly is suitable for connection to 
intra-building or unexposed wiring or cabling only. The intra-building port(s) of the equipment or subas-
sembly MUST NOT be metallically connected to interfaces that connect to the OSP or its wiring. These 
interfaces are designed for use as intra-building interfaces only (Type 2 or Type 4 ports as described in 
GR-1089-CORE, Issue 4) and require isolation from the exposed OSP cabling. The addition of Primary 
Protectors is not sufficient protection in order to connect these interfaces metallically to OSP wiring.
• The AC power supply must be connected to a surge protection device (SPD). 
• The equipment should be installed in a location that restricts access. A restricted access location is one 
where access is secure and limited to service personnel who have a special key, or other means of secu-
rity.
• The switch has a grounding lug located on the chassis. This lug uses 10-32 screws and is surrounded 
by a small paint-free area, which provides metal-to-metal contact for a ground connection. Install a 
Panduit Grounding Lug (type LCD8-10A-L) using 8AWG copper conductors to the paint-free area. 
Torque to between 30-60 inch pounds. Only use copper conductors for grounding purposes. 
• Star washers must be used to prevent any connections from loosening. 
• The switch must be installed utilizing a Common Bonding Network (CBN).
• Bare conductors must be cleaned and coated with antioxidant before crimping and bonding connec-
tions are made.
• The switch is suitable for installation in Network Telecommunications Facilities.

<<<PAGE 81>>>
Translated Safety Warnings
Regulatory Compliance and Safety Information
page A-10
OmniSwitch 6465 Hardware Users Guide
December 2025
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

<<<PAGE 82>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-11
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

<<<PAGE 83>>>
DC Power Supply Connection Warning
Regulatory Compliance and Safety Information
page A-12
OmniSwitch 6465 Hardware Users Guide
December 2025
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

<<<PAGE 84>>>
Regulatory Compliance and Safety Information
Instrucciones de seguridad en español
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-13
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

<<<PAGE 85>>>
Instrucciones de seguridad en español
Regulatory Compliance and Safety Information
page A-14
OmniSwitch 6465 Hardware Users Guide
December 2025
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

<<<PAGE 86>>>
Regulatory Compliance and Safety Information
Instrucciones de seguridad en español
OmniSwitch 6465 Hardware Users Guide
December 2025
page A-15
Advertencia de fuentes de poder
Las unidades OmniSwitch pueden estar equipadas con tres cordones para fuente de poder. Para reducir el 
riesgo de un choque electrico, desconecte todos los cordones de fuente de poder antes de dar servicio a la 
unidad.