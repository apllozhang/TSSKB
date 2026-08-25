<<<PAGE 1>>>
Part No. 060828-10, Rev. G
December 2025
OmniSwitch 6570M
Hardware Users Guide
www.al-enterprise.com

<<<PAGE 2>>>
ii
December 2025
This user guide documents OmniSwitch 6570M hardware, including chassis and associated components. 
The specifications described in this guide are subject to change without notice.
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trade-
marks-copyright. All other trademarks are the property of their respective owners. The information 
presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any 
responsibility for inaccuracies contained herein. © Copyright 2025 ALE International, ALE USA Inc. All 
rights reserved in all countries.
ALE USA Inc.
2000 Corporate Center Dr.
Thousand Oaks, CA 91320
(818) 880-3500
Service & Support Contact Information
North America: 800-995-2696
Latin America: 877-919-9526
EMEA: +800 00200100 (Toll Free) or +1(650)385-2193   
Asia Pacific: +65 6240 8484
Web: myportal.al-enterprise.com

<<<PAGE 3>>>
OmniSwitch 6570M Hardware Users Guide
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
OmniSwitch 6570M  ...................................................................................................1-1
OmniSwitch 6570M Availability Features .....................................................................1-2
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
Connections and Cabling ................................................................................................2-4
Network Cable Installation Warning .................................................................2-4
Serial Connection to the Console Port ...............................................................2-4
Serial Connection Default Settings ...................................................................2-4
Ethernet Management Port (EMP) Cable Requirements ...................................2-4
Booting the Switch ..........................................................................................................2-5
Component LEDs ..............................................................................................2-5
Your First Login Session ................................................................................................2-6
Logging In to the Switch ..........................................................................................2-6
Unlocking Session Types .........................................................................................2-7
Changing the Login Password ..................................................................................2-7

<<<PAGE 4>>>
Contents
iv
OmniSwitch 6570M Hardware Users Guide
December 2025
Setting the System Time Zone .................................................................................2-8
Setting the Date and Time ........................................................................................2-8
Setting Optional Parameters .....................................................................................2-8
Specifying an Administrative Contact ...............................................................2-8
Specifying a System Name ................................................................................2-8
Specifying the Switch’s Location ......................................................................2-8
Viewing Your Changes ............................................................................................2-9
Saving Your Changes ...............................................................................................2-9
Chapter 3
Chassis and Power Supplies ....................................................................................3-1
Chassis Details ................................................................................................................3-2
OS6570M-12 ............................................................................................................3-2
OS6570M-12 Front Panel ..................................................................................3-2
OS6570M-12 Rear Panel ...................................................................................3-3
OS6570M-12 Chassis Specifications ................................................................3-3
OS6570M-12D .........................................................................................................3-4
OS6570M-12D Front Panel ...............................................................................3-4
OS6570M-12D Rear Panel ................................................................................3-5
OS6570M-12D Chassis Specifications .............................................................3-5
OS6570M-U28 .........................................................................................................3-6
OS6570M-U28 Front Panel ...............................................................................3-6
OS6570M-U28 Rear Panel ................................................................................3-6
OS6570M-U28 Chassis Specifications .............................................................3-7
Chassis Status LEDs .................................................................................................3-8
Mounting the Switch .......................................................................................................3-9
General Mounting Recommendations ......................................................................3-9
Airflow / Clearance Recommendations ...................................................................3-9
Rack Mounting Steps (Full-width Chassis) ...........................................................3-10
Rack Mounting Steps (One Half-width Chassis - OS6570M-RM-19-L Kit) ........3-11
Rack Mounting Steps (Two Half-width Chassis - OS6570M-DUO-MNT Kit) ....3-13
Power Supplies ..............................................................................................................3-16
Internal Power Supplies .........................................................................................3-16
60W AC Power Supply ..........................................................................................3-17
30W DC Power Supply ..........................................................................................3-18
LED States .......................................................................................................3-18
150W AC Power Supply ........................................................................................3-19
LED States .......................................................................................................3-19
150W DC Power Supply ........................................................................................3-20
LED States .......................................................................................................3-20
DC Power Supply Connections ..............................................................................3-21
Connecting a DC Cable Harness to the Chassis Power Supply ......................3-21
Connecting a DC Cable Harness to the DC Power Source .............................3-21
Installing Power Supplies .......................................................................................3-22
Hot-Swapping / Removing Power Supplies ...........................................................3-23
Installing Power Supply Trays ...............................................................................3-25
Grounding the Chassis ..................................................................................................3-26
Monitoring Chassis Components ..................................................................................3-26
Viewing Chassis Slot Information .........................................................................3-26
Monitoring Chassis Temperature ...........................................................................3-26

<<<PAGE 5>>>
Contents
OmniSwitch 6570M Hardware Users Guide
December 2025
v
Temperature Errors ..........................................................................................3-26
Dying Gasp ....................................................................................................................3-27
Scenarios ................................................................................................................3-27
SNMP Trap ............................................................................................................3-27
Syslog Message ......................................................................................................3-28
Link OAM PDU .....................................................................................................3-28
Link OAM PDU Priority .................................................................................3-28
Appendix A
Regulatory Compliance and Safety Information ..............................................A-1
Declaration of Conformity: CE Mark ............................................................................A-1
Waste Electrical and Electronic Equipment (WEEE) Statement ...................................A-1
China RoHS: Hazardous Substance Table .....................................................................A-2
Taiwan RoHS: Hazardous Substance Table ..................................................................A-3
California Proposition 65 Warning ................................................................................A-3
Standards Compliance ....................................................................................................A-4
FCC Class A, Part 15 ..............................................................................................A-7
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
Invisible Laser Radiation Warning .................................................................A-10
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
Advertencia sobre una apropiada conexión a tierra .......................................A-14
Leer “información importante de seguridad” .................................................A-14

<<<PAGE 6>>>
Contents
vi
OmniSwitch 6570M Hardware Users Guide
December 2025
Advertencia de acceso restringido ..................................................................A-14
Advertencia de pulsera antiestática ................................................................A-14
Clase de seguridad ..........................................................................................A-14
Advertencia de fuentes de poder ....................................................................A-14

<<<PAGE 7>>>
OmniSwitch 6570M Hardware Users Guide
December 2025
vii
About This Guide
This OmniSwitch 6570M Hardware Users Guide describes OmniSwitch 6570M switch components and 
basic switch hardware procedures. 
Supported Platforms
The information in this guide applies only to OmniSwitch 6570M switches.
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
OmniSwitch 6570M Hardware Users Guide
December 2025
• Hardware-related Command Line Interface (CLI) commands.
What is Not in this Manual?
The descriptive and procedural information in this manual focuses on switch hardware. It includes 
information on some CLI commands that pertain directly to hardware configuration, but it is not intended 
as a software users guide. There are several OmniSwitch users guides that focus on switch software 
configuration. Consult those guides for detailed information and examples for configuring your switch 
software to operate in a live network environment. See “Documentation Roadmap” on page -viii and 
“Related Documentation” on page -ix for further information on software configuration guides available 
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
Pertinent Documentation: Getting Started Information
Release Notes
A “Getting Started” chapter is included in the OmniSwitch 6570M Hardware Users Guide. This chapter 
provides all the information you need to get your switch up and running the first time. It also includes 
succinct overview information on fundamental aspects of the switch.
At this time you should also familiarize yourself with the Release Notes that accompanied your switch. 
This document includes important information on feature limitations that are not included in other 
user guides.
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: Hardware Users Guide
OmniSwitch AOS Release 8 Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the OmniSwitch 6570M 
Hardware Guide. This guide provide specifications, illustrations, and descriptions of all hardware 
components. It also includes steps for common procedures, such as removing and installing switch 
components.

<<<PAGE 9>>>
OmniSwitch 6570M Hardware Users Guide
December 2025
ix
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
Related Documentation
The following are the titles and descriptions of all the OmniSwitch 6570M user manuals:
• OmniSwitch 6570M Hardware Users Guide
Complete technical specifications and procedures for all OmniSwitch 6570M chassis, power supplies, 
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

<<<PAGE 10>>>
x
OmniSwitch 6570M Hardware Users Guide
December 2025
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
OmniSwitch 6570M Hardware Users Guide
December 2025
page 1-1
1   OmniSwitch 6570M
Refer to the information below for OmniSwitch 6570M models and components.
OmniSwitch 6570M Availability Features
The switch provides a broad variety of availability features. Availability features are hardware and 
software-based safeguards that help prevent the loss of data flow in the unlikely event of a subsystem 
failure. In addition, some availability features allow users to maintain or replace hardware components 
without powering off the switch or interrupting switch operations. Combined, these features provide added 
resiliency and help ensure that the switch is consistently available for day-to-day network operations.
Hardware-related availability features include:
• Power Supply Redundancy
• Hot-Swapping
• Hardware Monitoring
Model Number
Description
OS6570M-12
Fixed-configuration chassis with: 
• 8 - RJ45 10/100/1000Base-T ports
• 2 - 100/1000Base-X SFP ports
• 2 - Uplink/Stacking SFP+ Ports (1G/10G)
• 1 - Internal AC Power Supply
• 1 - External Power Connector
See “OS6570M-12” on page 3-2
OS6570M-12D
Fixed-configuration chassis with: 
• 8 - RJ45 10/100/1000Base-T ports
• 2 - 100/1000Base-X SFP ports
• 2 - Uplink/Stacking SFP+ Ports (1G/10G)
• 1 - Internal DC Power Supply
• 1 - External Power Connector
See “OS6570M-12D” on page 3-4
OS6570M-U28
Fixed-configuration chassis with: 
• 20 - 100/1000Base-X SFP ports
• 4 - 100/1000Base-X SFP or 10/100/1000Base-T RJ45 combo ports
• 6 - Uplink/Stacking SFP+ Ports (1G/10G)
• 2 - Power Supply Bays
See “OS6570M-U28” on page 3-6

<<<PAGE 12>>>
OmniSwitch 6570M Availability Features
OmniSwitch 6570M
page 1-2
OmniSwitch 6570M Hardware Users Guide
December 2025
Power Supply Redundancy
Multiple power supplies can be used for power supply redundancy or load sharing on supported models. 
For information on power supplies, refer to Chapter 3, “Chassis and Power Supplies.” 
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

<<<PAGE 13>>>
OmniSwitch 6570M Hardware Users Guide
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
The switches have the following environmental and airflow requirements:
• The installation site must maintain a supported temperature and humidity range as given in the 
specifications table for the chassis. 
• Be sure to allow adequate room for proper air ventilation around the chassis. Refer to “Mounting the 
Switch” on page 3-9 for minimum clearance requirements. 
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

<<<PAGE 14>>>
Installing the Hardware
Getting Started
page 2-2
OmniSwitch 6570M Hardware Users Guide
December 2025
Redundant AC Power. It is recommended that each AC outlet resides on a separate circuit. With 
redundant AC, if a single circuit fails, the switch’s remaining power supplies (on separate circuits) can 
remain operational.
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

<<<PAGE 15>>>
Getting Started
Connections and Cabling
OmniSwitch 6570M Hardware Users Guide
December 2025
page 2-3
Unpacking and Installing the Switch
To protect your switch components from damage, read all unpacking recommendations and instructions 
carefully before beginning.
Unpack your chassis as close as possible to the location where it will be installed.
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

<<<PAGE 16>>>
Booting the Switch
Getting Started
page 2-4
OmniSwitch 6570M Hardware Users Guide
December 2025
Serial Connection Default Settings
For information on modifying these settings, refer to the Switch Management Guide.
Ethernet Management Port (EMP) Cable Requirements
There is an EMP port provided on the chassis for out-of-band management. There are specific cable type 
requirements (i.e., straight-through or crossover) based on the device to which the EMP is connecting. Refer to 
the information below:
For information on manually configuring Ethernet ports, refer to the OmniSwitch AOS Release 8 Network 
Configuration Guide. 
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
baud rate
9600
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

<<<PAGE 17>>>
Getting Started
Your First Login Session
OmniSwitch 6570M Hardware Users Guide
December 2025
page 2-5
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

<<<PAGE 18>>>
Your First Login Session
Getting Started
page 2-6
OmniSwitch 6570M Hardware Users Guide
December 2025
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

<<<PAGE 19>>>
Getting Started
Your First Login Session
OmniSwitch 6570M Hardware Users Guide
December 2025
page 2-7
For detailed information on configuring a time zone for the switch, refer to the Switch Management Guide.
Setting the Date and Time
Set the current time for the switch by entering system time, followed by the current time in hh:mm:ss. 
To set the current date for the switch, enter system date, followed by the current date in mm/dd/yyyy.
Setting Optional Parameters
Specifying an Administrative Contact
An administrative contact is the person or department in charge of the switch. If a contact is specified, users 
can easily find the appropriate network administrator if they have questions or comments about the switch. To 
specify an administrative contact, use the system contact command.
Specifying a System Name
The system name is a simple, user-defined text description for the switch. To specify a system name, use the 
system name command.
Specifying the Switch’s Location
It is recommended that you use a physical labeling system for locating and identifying your switch(es). 
Examples include placing a sticker or placard with a unique identifier (e.g., the switch’s default IP address) on 
each chassis. However, if no labeling system has been implemented or if you need to determine a switch’s 
location from a remote site, entering a system location can be very useful. To specify a system location, use 
the system location command.
Viewing Your Changes
To view your current changes, enter show system at the CLI prompt.
Saving Your Changes
Once you have configured this basic switch information, save your changes by entering write memory at the 
CLI command prompt.

<<<PAGE 20>>>
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-1
3   Chassis and Power
Supplies
This chapter includes detailed information on the chassis types. Topics include:
• Chassis details and technical specifications:
OS6570M-12, page 3-2.
OS6570M-12D, page 3-4.
OS6570M-U28, page 3-6.
• Mounting the Switch, page 3-9.
• Power supplies, page 3-16.
Internal Power Supplies, page 3-16.
OS6570M-12 AC Power Supply, page 3-17.
OS6570M-12D DC Power Supply, page 3-18.
OS6570M-U28 AC Power Supply, page 3-17.
OS6570M-U28 DC Power Supply, page 3-20.
• Temperature management, page 3-26.
• Monitoring the chassis components via the Command Line Interface (CLI), page 3-26

<<<PAGE 21>>>
Chassis Details
Chassis and Power Supplies
page 3-2
OmniSwitch 6570M Hardware Users Guide
December 2025
Chassis Details
OS6570M-12
OS6570M-12 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
Item
Description
A
USB port
B
Console port
C
EMP port (Out-of-band Management Port)
D
(1-8) 10/100/1000Base-T ports
E
(9-10) 100/1000Base-X SFP ports
F
(11-12) Uplink/Stacking SFP+ Ports (1G/10G)
LEDs
See “Chassis Status LEDs” on page 3-8
Note: The OS6570M-12 does not support half-duplex connections.
D
F
E
A
B
C

<<<PAGE 22>>>
Chassis and Power Supplies
Chassis Details
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-3
OS6570M-12 Rear Panel
OS6570M-12 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Internal temperature refers to the sensor reading of 
the internal switch temperature. Ambient temperature (Tmra) refers to the approximate room temperature. 
The ambient temperature will typically be lower than the internal temperature. 
Item
Description
A
AC Power Connector
B
Power Connector
C
Grounding Lug
Chassis Height
4.4 cm (1.73 in.)
Chassis Width 
21.72 cm (8.55 in.)
Chassis Depth 
28.07 cm (11.05 in.)
Chassis Weight
1.7 kg (3.7 lb)
Ambient Operating Temperature (Tmra)
0°C to 50°C (32°F to 122°F)
Warning Threshold (Thresh) 
(internal)
85°C (185°F)
Danger Threshold (internal)
88°C (190°F)
Storage Temperature
-20°C to 60°C (-4°F to 140°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Power Consumption (idle)
23 W
Refer to “Monitoring Chassis Temperature” on page 3-26 for an explanation of the Warning and Danger 
Thresholds.
A
B
C

<<<PAGE 23>>>
Chassis Details
Chassis and Power Supplies
page 3-4
OmniSwitch 6570M Hardware Users Guide
December 2025
OS6570M-12D
OS6570M-12D Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
Item
Description
A
USB port
B
Console port
C
EMP port (Out-of-band Management Port)
D
(1-8) 10/100/1000Base-T ports
E
(9-10) 100/1000Base-X SFP ports
F
(11-12) Uplink/Stacking SFP+ Ports (1G/10G)
LEDs
See “Chassis Status LEDs” on page 3-8
Note: The OS6570M-12D does not support half-duplex connections.
D
F
E
A
B
C

<<<PAGE 24>>>
Chassis and Power Supplies
Chassis Details
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-5
OS6570M-12D Rear Panel
OS6570M-12D Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Internal temperature refers to the sensor reading of 
the internal switch temperature. Ambient temperature (Tmra) refers to the approximate room temperature. 
The ambient temperature will typically be lower than the internal temperature. 
Item
Description
A
DC Power Connector
B
Power Connector
C
Grounding Lug
Chassis Height
4.4 cm (1.73 in.)
Chassis Width 
21.72 cm (8.55 in.)
Chassis Depth 
28.07 cm (11.05 in.)
Chassis Weight
1.7 kg (3.7 lb)
Ambient Operating Temperature (Tmra)
0°C to 50°C (32°F to 122°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Warning Threshold (Thresh) 
(internal)
85°C (185°F)
Danger Threshold (internal)
88°C (190°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Power Consumption (idle)
24 W
Refer to “Monitoring Chassis Temperature” on page 3-26 for an explanation of the Warning and Danger 
Thresholds.
When connecting in dual-redundant power supply configuration, both power supplies must have identical 
output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in 
unexpected behavior and is not supported. 
A
B
C

<<<PAGE 25>>>
Chassis Details
Chassis and Power Supplies
page 3-6
OmniSwitch 6570M Hardware Users Guide
December 2025
OS6570M-U28
OS6570M-U28 Front Panel
CLASS 1 M LASER CAUTION. CAUTION - CLASS 1 M LASER RADIATION WHEN OPEN.
DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS
OS6570M-U28 Rear Panel
Item
Description
A
USB port
B
Console port
C
Virtual Chassis ID LED
D
EMP port (Out-of-band Management Port)
E
(1-20) 100/1000Base-X SFP ports
F
(21-24) 100/1000Base-X SFP or 10/100/1000Base-T RJ45 combo ports
G
(25-30) Uplink/Stacking SFP+ Ports (1G/10G)
LEDs
See “Chassis Status LEDs” on page 3-8
Note: The OS6570M-U28 does not support half-duplex connections.
Item
Description
A
Grounding Lug
B
Power Supply Bays
E
G
F
A
B
D
C
A
B

<<<PAGE 26>>>
Chassis and Power Supplies
Chassis Details
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-7
OS6570M-U28 Chassis Specifications
*Note On Chassis Versus Ambient Temperatures. Internal temperature refers to the sensor reading of 
the internal switch temperature. Ambient temperature (Tmra) refers to the approximate room temperature. 
The ambient temperature will typically be lower than the internal temperature. 
 
Chassis Height
4.4 cm (1.73 in)
Chassis Width 
44 cm (17.32 in)
Chassis Depth 
35 cm (13.78)
Chassis Weight (without power supplies) 4.08 kg (8.99 lb)
Power Consumption (idle)
71 W
Ambient Operating Temperature (Tmra)
0°C to 50°C (32°F to 122°F)
Warning Threshold (Thresh) 
(internal)
69°C (156°F)
Danger Threshold (internal)
74°C (165°F)
Storage Temperature
-40°C to 85°C (-40°F to 185°F)
Operating Humidity
5% to 95% non-condensing
Storage Humidity
5% to 95% non-condensing
Refer to “Monitoring Chassis Temperature” on page 3-26 for an explanation of the Warning and Dan-
ger Thresholds.

<<<PAGE 27>>>
Chassis Details
Chassis and Power Supplies
page 3-8
OmniSwitch 6570M Hardware Users Guide
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
System Diagnostics and AOS bootup OK.
System Diagnostics and AOS in progress.
(i.e., performing diagnostics or booting)
System Diagnostics and/or AOS bootup failed.
VC
Solid Green
Solid Amber
Blinking Amber 
(12-port models only)
Off
This unit is the master unit.
This unit is a slave unit.
Identifies unit number by the number of blinks.
This unit is in shutdown mode or is not part of a VC.
PS1/PS2 (U28)
Solid Green
Solid Amber
Off
Power supply functioning normally.
Power supply not functioning normally. 
Power supply not present.
PS1/PS2 
(12-port models)
Solid Green
Off
Power supply functioning normally.
Power supply not present.
10/100/1000 Port LEDs Solid Green
Blinking Green
Valid port link.
Valid port link with activity.
SFP 100/1000Base-X 
Port LEDs
Solid Green
Blinking Green
Valid port link.
Valid port link with activity.
SFP+ Port LEDs
Solid Green
Blinking Green
Valid 1G/10G port link.
Valid 1G/10G port link with activity.

<<<PAGE 28>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-9
Mounting the Switch
General Mounting Recommendations
Elevated Operating Ambient Temperature. If installed in a closed or multi-rack assembly, the 
operating ambient temperature of the environment may be greater than the room’s ambient temperature. 
Therefore, consideration should be given to the maximum rated ambient temperature (Tmra) listed in the 
“Chassis Details” on page 3-2 section.
Reduced Air Flow. Installation of the equipment should be such that the amount of air flow required for 
safe operation of the equipment is not compromised. Refer to “Airflow / Clearance Recommendations” on 
page 3-9 for more information.
Mechanical Loading. Mounting of the equipment should be such that a hazardous condition is not 
achieved due to uneven loading.
Circuit Overloading. Consideration should be give to the connection of the equipment to the supply 
circuit and the effect that overloading of circuits could have on overcurrent protection and supply wiring. 
Reliable Earthing. Reliable earthing of equipment should be maintained. Particular attention should be 
given to supply connections other than direct connections to the branch (e.g., use of power strips).
Airflow / Clearance Recommendations
To ensure proper airflow, be sure that your switch is placed in a clean, well-ventilated area free of dust 
and debris and provide minimum recommended clearance as shown below. Restricted airflow can cause 
your switch to overheat, which can lead to switch failure. Refer to the following important guidelines: 
Minimum Recommended Clearances - 12-port Models
Top
N/A - (If no equipment is installed above chassis)
1 inch - (If equipment is installed above chassis).
Bottom
N/A - (If no equipment is installed below chassis)
1 inch - (If equipment is installed below chassis). 
Sides
2 inches
Front / Rear
N/A
Minimum Recommended Clearances - U28 Model
Top
1.75 inch (1RU)
Bottom
1.75 inch (1RU)
Sides
2 inches
Front / Rear
N/A

<<<PAGE 29>>>
Mounting the Switch
Chassis and Power Supplies
page 3-10
OmniSwitch 6570M Hardware Users Guide
December 2025
Rack Mounting Steps (Full-width Chassis)
1 Attach rack mount brackets to both sides of the chassis as shown. 
2 Mark the holes on the rack where the switch is to be installed.
3 Lift and position the switch until the rack-mount brackets are flush with the rack post, then align the 
holes in the brackets with the rack holes that were marked at step 1.
4 Once the holes are aligned, insert a rack mount screw (not provided) through the bottom hole of each 
bracket. Tighten both screws until they are secure.
Note. Be sure to install the screws in the bottom hole of each bracket, as shown, before proceeding.
Follow the recommended clearance requirements for the 
model being mounted.

<<<PAGE 30>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-11
5 Once the screws at the bottom of each bracket are secure, install the remaining two rack mount screws. 
Be sure that all screws are securely tightened.
Rack Mounting Steps (One Half-width Chassis - OS6570M-RM-
19-L Kit)
A single chassis can also be mounted into a standard 19-inch rack using L-brackets, as shown in the figure 
below.
1 Attach rack mount brackets to both sides of the front of the chassis.The long and short bracket can be 
mounted on either side of the chassis. 
Attach Rack Mount Brackets

<<<PAGE 31>>>
Mounting the Switch
Chassis and Power Supplies
page 3-12
OmniSwitch 6570M Hardware Users Guide
December 2025
2 Align the holes in the flanges with the rack holes and insert rack mount screws (not provided) through 
the bottom hole of each flange and then the top of each flange. Tighten both screws until they are secure
Follow the recommended clearance requirements for the 
model type being mounted.

<<<PAGE 32>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-13
Rack Mounting Steps (Two Half-width Chassis - OS6570M-DUO-MNT Kit)
Two chassis can be assembled side-by-side for mounting into a standard 19-inch rack as show in the 
figure below.
Fully Assembled Side-by-Side Chassis Assembly
1 Attach the slot-brackets and slide-brackets to the front and back of the chassis using the attachment 
screws (M3 flat head) provided for each bracket.
Attach Slot/Slide-Brackets
Slot -bracket
Plate and Screws
Slide -bracket
Power Supply Tray Rear Bracket
(Not Used)
Front center mounting brackets. 
Rear center brackets.

<<<PAGE 33>>>
Mounting the Switch
Chassis and Power Supplies
page 3-14
OmniSwitch 6570M Hardware Users Guide
December 2025
2 Align the chassis and slide both front and rear center brackets together.
Slide Chassis Together
3 Place bracket plate over front and rear brackets and secure with thumb screws.
Secure Front and Back with Bracket Plate
4 Attach rack mount brackets to both sides of the front of the chassis.
Attach Rack Mount Brackets
5 Using one additional person, lift and position the assembly on the rack until the rack-mount flanges are 
flush with the rack post.
Slide chassis together
Bracket Plate and Screws

<<<PAGE 34>>>
Chassis and Power Supplies
Mounting the Switch
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-15
6 Align the holes in the flanges with the rack holes and insert rack mount screws (not provided) through 
the bottom hole of each flange and then the top of each flange. Tighten both screws until they are secure.
Rack-mounting Two Chassis
Follow the recommended clearance requirements for the 
model being mounted.

<<<PAGE 35>>>
Power Supplies
Chassis and Power Supplies
page 3-16
OmniSwitch 6570M Hardware Users Guide
December 2025
Power Supplies
OmniSwitch 6570M switches can use the following power supplies:
Internal Power Supplies
Model
Chassis Supported
Internal Power Supply (See page 3-16)
OS6570M-12, OS6570M-12D
OS6570M-12 AC Power Supply (DA-60Z12)
(See page 3-17)
OS6570M-12
OS6570M-12D DC Power Supply (DDR-30L-12)
(See page 3-18)
OS6570M-12D
OS6570M-U28 AC Power Supply (PS-150W-AC)
(See page 3-19)
OS6570M-U28
OS6570M-U28 DC Power Supply (PS-150W-DC)
(See page 3-20)
OS6570M-U28
Model
Internal AC Power Supply
Description
Internal AC 65W power supply
Models Supported
OS6570M-12
Input
100-240V, 50-60Hz
Output
12V/5.42A (65W)
Model
Internal DC Power Supply
Description
Internal DC 30W power supply
Models Supported
OS6570M-12D
Input
36-72VDC
Output
12V/5.42A (30W)

<<<PAGE 36>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-17
60W AC Power Supply
60W AC Power Supply 
Model
OS6570-12-BP, PS-60W-AC (DA-60Z12)
Models Supported
OS6570M-12
Input
100-240VAC/50-60Hz
Output
12V/5A (60W)
AC Connector
Power Cord

<<<PAGE 37>>>
Power Supplies
Chassis and Power Supplies
page 3-18
OmniSwitch 6570M Hardware Users Guide
December 2025
30W DC Power Supply
30W DC Power Supply
LED States
Model
OS6570-12-BP-D, PS-30W-DC (DDR-30L-12)
Models Supported
OS6570M-12D
Input
18-75VDC (Tolerances Included)
Output
12V/2.5A (30W)
LED State
Description
Solid Green
DC power is good.
Solid Red
There is a DC power issue.
2
1
3
4
DC Output
Status LED
DC Input

<<<PAGE 38>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-19
150W AC Power Supply
150W AC Power Supply Front Panel
LED States
Model
OS6570-BP (PS-150W-AC)
Models Supported
OS6570M-U28
Input Voltage/Current
100-240VAC / 3-1.5A
Input Frequency
50-60Hz
Max. Output Power/Current
150 W/12.5 A
Weight
0.88 kg (1.94 lb) 
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
LED
Handle
Status LED
Air Vent
Lock Tab
AC Connector

<<<PAGE 39>>>
Power Supplies
Chassis and Power Supplies
page 3-20
OmniSwitch 6570M Hardware Users Guide
December 2025
150W DC Power Supply
150W DC Power Supply Front Panel
LED States
Model
OS6570-BP-D (PS-150W-DC)
Models Supported
OS6570M-U28
Input Voltage/Current
-36 V to-72 VDC/1.8 A to 6 A
Max. Output Power/Current
150 W/12.5 A
Weight
0.88 kg (1.94 lb) 
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
LED
Handle
Status LED
Air Vent
Lock Tab
DC Connector

<<<PAGE 40>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-21
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
Green/Yellow ground lead in the three pin cable connector is connected to the ground connector on the 
DC power supply, which is identified by a Grounding symbol. The Green/Yellow lead wire at the other 
end of the cable must be connected to a proper earth ground point. 
The rear chassis has two ground holes. To properly ground the equipment, connect a Panduit Corporation 
UL listed Lug, (Part number LCD8-10A-L) to the two threaded holes located at the rear, insert two 10-32, 
3/8” threaded pan head screws into these ground holes, and connect them to a proper earth ground point, 
using protective earthing conductor wire and 8AWG copper conductors.
Connection Details
For DC power supply units, make the following power connections:
Connect the power supply using the supplied DC cable. The cable consists of three 12AWG wires (Green/
Yellow, Black, Red). 
One end of the cable has a three pin connector in a plastic housing that is inserted into a three pin input 
connector on the power supply. The other end of the cable is connected to a fuse panel or other source of 
-48VDC power.
Observe proper polarity when connecting to a fuse panel. The cable wire leads must be connected as 
follows:
• Green/yellow - ground
• Black - return
• Red - -48VDC
Note. The battery return conductor is an Isolated DC Return (DC-1).

<<<PAGE 41>>>
Power Supplies
Chassis and Power Supplies
page 3-22
OmniSwitch 6570M Hardware Users Guide
December 2025
Installing Power Supplies
Note. The power supply shown in the following diagrams may differ from the actual unit. However, 
comparable installation and removal steps also apply to other power supply units.
1 Insert the power supply into a power supply bay at the rear of the chassis and slide it back until it is 
securely seated in the chassis backplane. 
When the connector is fully seated, the lock tab will click and hold the power supply in place.
2 Plug the power cord (provided) into the power supply’s socket.
Lock Tab

<<<PAGE 42>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-23
Note. The chassis does not provide an on/off switch. Connecting a the power supplies to a power source 
will boot the switch.
Hot-Swapping / Removing Power Supplies
1 When removing a power supply, first disconnect the power cord from the power source. Once the 
power cord is disconnected, pull the power cord out of the power supply housing. 
2 Pressing the lock tab toward the center of the power supply, as shown, will free the power supply from 
the chassis.
Lock Tab

<<<PAGE 43>>>
Power Supplies
Chassis and Power Supplies
page 3-24
OmniSwitch 6570M Hardware Users Guide
December 2025
3  While pressing the lock tab, pull the power supply straight back and out of the chassis slot.
Note. If you are not replacing the power supply, be sure to install a blank cover panel over the empty 
power supply bay.

<<<PAGE 44>>>
Chassis and Power Supplies
Power Supplies
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-25
Installing Power Supply Trays
Note. The same power supply tray is used for both AC and DC power supplies. Use the supplied cable ties 
to secure the power supply cables. 
1 Attach the power supply tray to the chassis using the provided screws (4). 
2 Mount the power supply to the tray and secure with the power supply bracket using the provided 
screws (2).
3 Attach power supply tray cover with screws (2).
4 Properly secure all cables using the supplied cable ties. 
Mounted Power Supplies and Trays
AC Power Supply
DC Power Supply
Power Supply With Cover

<<<PAGE 45>>>
Grounding the Chassis
Chassis and Power Supplies
page 3-26
OmniSwitch 6570M Hardware Users Guide
December 2025
Grounding the Chassis
The switch has a grounding lug located on the front or rear of the chassis. This lug uses 10-32 screws and 
is surrounded by a small paint-free area, which provides metal-to-metal contact for a ground connection.
Use this connector to supplement the ground provided by the AC power cord. To do so, install a Panduit 
Grounding Lug (type LCD8-10A-L) using 8AWG copper conductors to the paint-free area.
Refer to the chassis views on page 3-2 for location details. 
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
page 3-9.
To check the switch’s current temperature status, use the show temperature command. For example:
-> show temperature
Chassis/Device | Current |  Range     | Danger | Thresh |  Status
---------------+---------+------------+--------+--------+-----------------
 1/CMMA            58      15 to 85     88       85     UNDER THRESHOLD
For more information about this command, see the “Chassis Management and Monitoring Commands” 
chapter in the OmniSwitch CLI Reference Guide.
Temperature Errors
The switch monitors the chassis temperature at all times via an onboard sensor. The threshold values are 
factory-set and cannot be modified. If an over-temperature condition occurs, there are two different levels 
of error severity:
• Warning threshold (Thresh) temperature has been exceeded
• Danger threshold has been exceeded

<<<PAGE 46>>>
Chassis and Power Supplies
Dying Gasp
OmniSwitch 6570M Hardware Users Guide
December 2025
page 3-27
Warning Threshold Temperature
If the temperature exceeds the switch’s Warning threshold, the switch sends out a trap. Traps are also 
printed to the console in the form of text error messages.
When the Warning threshold has been exceeded, switch operations remain active. However, it is 
recommended that immediate steps be taken to address the over-temperature condition.
Addressing Warning threshold conditions may include:
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature
Danger Threshold
If the chassis temperature rises above the Danger threshold, the switch will power off until the temperature 
conditions have been addressed and the switch is manually booted.
Addressing the Danger threshold conditions may include:
• Checking for a chassis airflow obstruction
• Checking the ambient room temperature
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

<<<PAGE 47>>>
Dying Gasp
Chassis and Power Supplies
page 3-28
OmniSwitch 6570M Hardware Users Guide
December 2025
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

<<<PAGE 48>>>
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 49>>>
China RoHS: Hazardous Substance Table
Regulatory Compliance and Safety Information
page A-2
OmniSwitch 6570M Hardware Users Guide
December 2025
China RoHS: Hazardous Substance Table

<<<PAGE 50>>>
Regulatory Compliance and Safety Information
Taiwan RoHS: Hazardous Substance Table
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 51>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-4
OmniSwitch 6570M Hardware Users Guide
December 2025
Standards Compliance
The product bears the CE mark. In addition it is in compliance with the following other safety and 
EMC standards.
Note. All hardware switching modules used in an OmniSwitch switch comply with Class A 
standards. Modules with copper connectors meet Class A requirements using unshielded (UTP) cables.
Safety Standards
• US UL 62368-1
• IEC 62368-1 Health and Safety
• CAN/CSA-C22.2 No. 62368-1-03
• NOM-019 SCFI, Mexico
• AS/NZ TS-001 and 62368:2000, Australia
• UL-AR, Argentina
• UL-GS Mark, Germany
• CU, EAC, Russia
• EN 60825-1 Laser
• EN 60825-2 Laser
• CDRH Laser
• IEC 62368-1/EN 62368-1 with all country
• deviations
• IEC 62368-1:2005, Second Edition
• CQC, China
• ANATEL, Brazil
• BSMI, Taiwan
• KCC, Korea
• UAE RoHs

<<<PAGE 52>>>
Regulatory Compliance and Safety Information
Standards Compliance
OmniSwitch 6570M Hardware Users Guide
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
• EN 55035 (Immunity)
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
FCC Class A, Part 15
This equipment has been tested and found to comply with the limits for Class A digital device pursuant to 
Part 15 of the FCC Rules.These limits are designed to provide reasonable protection against harmful

<<<PAGE 53>>>
Standards Compliance
Regulatory Compliance and Safety Information
page A-6
OmniSwitch 6570M Hardware Users Guide
December 2025
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
CISPR22 Class A warning
This is a Class A product. In a domestic environment, this product may cause radio interference. Under 
such circumstances, the user may be requested to take appropriate countermeasures.

<<<PAGE 54>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 55>>>
Translated Safety Warnings
Regulatory Compliance and Safety Information
page A-8
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 56>>>
Regulatory Compliance and Safety Information
Translated Safety Warnings
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 57>>>
DC Power Supply Connection Warning
Regulatory Compliance and Safety Information
page A-10
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 58>>>
Regulatory Compliance and Safety Information
Instrucciones de seguridad en español
OmniSwitch 6570M Hardware Users Guide
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

<<<PAGE 59>>>
Instrucciones de seguridad en español
Regulatory Compliance and Safety Information
page A-12
OmniSwitch 6570M Hardware Users Guide
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
Las unidades OmniSwitch pueden estar equipadas con tres cordones para fuente de poder. Para reducir el 
riesgo de un choque electrico, desconecte todos los cordones de fuente de poder antes de dar servicio a la 
unidad.