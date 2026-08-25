<<<PAGE 1>>>
Part No. 060435-10, Rev. Y
December 2025
OmniSwitch 6865
Hardware Users Guide
www.al-enterprise.com

<<<PAGE 2>>>
This user guide documents OmniSwitch 6865 hardware, including chassis and associated components. The 
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
OmniSwitch 6865 Hardware Users Guide
December 2025
iii
Contents
About This Guide ........................................................................................................... v
Chapter 1
Getting Started and Installation ...........................................................................1-1
Getting Started ................................................................................................................1-1
Preparing for the Installation ....................................................................................1-1
Providing Air Flow and Minimum Recommended Clearances ...............................1-3
Items Included ..........................................................................................................1-4
Preparing the Chassis and Power Supply Tray Assembly ..............................................1-4
Side Mount Power Supply Tray ...............................................................................1-4
Rear Mount Power Supply Tray ...............................................................................1-5
Attaching Rack Mount Flanges ................................................................................1-7
Attaching Table Mount Feet ....................................................................................1-7
Installing Power Supplies ................................................................................................1-8
Installing Power Supplies for Side Mount Trays .....................................................1-9
Installing Power Supplies for Rear Mount Trays ...................................................1-10
Mounting the OmniSwitch 6865 ...................................................................................1-12
Rack Mounting .......................................................................................................1-12
Table Mounting ......................................................................................................1-15
DIN Rail Mounting - Power Supply ......................................................................1-16
DIN Rail Mounting - Chassis .................................................................................1-17
DNV Mounting Steps .............................................................................................1-19
Additional DIN / Wall Mounting Examples .................................................................1-25
Connections and Cabling ..............................................................................................1-28
System and Port LEDs ...........................................................................................1-29
The First Login Session ..........................................................................................1-30
Unlocking Session Types .......................................................................................1-31
Changing the Login Password ................................................................................1-31
Setting the System Time Zone ...............................................................................1-32
Setting the Date and Time ......................................................................................1-32
Setting Optional Parameters ...................................................................................1-32
Chapter 2
Chassis and Power .....................................................................................................2-1
OmniSwitch 6865-P16X .................................................................................................2-1
Chassis Front Panel ..................................................................................................2-3
Chassis Rear Panel ...................................................................................................2-4
OmniSwitch 6865-U12X ................................................................................................2-4
Chassis Front Panel ..................................................................................................2-5
Chassis Rear Panel ...................................................................................................2-6
OmniSwitch 6865-U28X ................................................................................................2-6
Chassis Front Panel ..................................................................................................2-7

<<<PAGE 4>>>
Contents
iv
OmniSwitch 6865 Hardware Users Guide
December 2025
Chassis Rear Panel ...................................................................................................2-8
Power Supplies ................................................................................................................2-8
OS6865-BP - 180W AC Power Supply ...................................................................2-8
OS6865-BP-D - 180W/140W DC Power Supply ....................................................2-9
DC Power Supply Connection ......................................................................................2-10
Connecting a DC Cable Harness to the Chassis Power Supply .............................2-10
Connecting a DC Cable Harness to the DC Power Source ....................................2-10
Connecting a DC Power Source .............................................................................2-11
Dying Gasp ....................................................................................................................2-12
Scenarios ................................................................................................................2-13
SNMP Trap ............................................................................................................2-13
Syslog Message ......................................................................................................2-13
Link OAM PDU .....................................................................................................2-13
Chapter 3
Power Over Ethernet (PoE) ......................................................................................3-1
Managing Power over Ethernet (PoE) ............................................................................3-1
Power over Ethernet Budget ....................................................................................3-1
Determining the Power Available for Powered Devices (PDs) ...............................3-2
PoE Operational Status .............................................................................................3-3
Understanding Priority Disconnect ..........................................................................3-7
Appendix A
Regulatory Compliance and Safety Information A-1
Declaration of Conformity: CE Mark ............................................................................A-1
Compliance and Certifications .......................................................................................A-1
Safety Standards ......................................................................................................A-1
EMI/EMC Standards ...............................................................................................A-2
Industrial Compliance Requirements ......................................................................A-3
China RoHS: Hazardous Substance Table ..............................................................A-5
Taiwan RoHS: Hazardous Substance Table ............................................................A-6
California Proposition 65 Warning .........................................................................A-6
Waste Electrical and Electronic Equipment (WEEE) Statement ............................A-7
FCC Class A, Part 15 ..............................................................................................A-7
JATE ........................................................................................................................A-8
CISPR22 Class A Warning .....................................................................................A-8
Korea Emissions Statement .....................................................................................A-8
VCCI .......................................................................................................................A-8
Class A Warning for Taiwan and Other Chinese Markets ......................................A-8
Translated Safety Warnings ....................................................................................A-9
Instrucciones de seguridad en español ..................................................................A-13

<<<PAGE 5>>>
OmniSwitch 6865 Hardware Users Guide
December 2025
v
About This Guide
This OmniSwitch 6865 Hardware Users Guide describes OmniSwitch 6560 switch components and basic 
switch hardware procedures. 
Supported Platforms
The information in this guide applies only to OmniSwitch 6865 switches.
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

<<<PAGE 6>>>
vi
OmniSwitch 6865 Hardware Users Guide
December 2025
• Hardware-related Command Line Interface (CLI) commands.
What is Not in this Manual?
The descriptive and procedural information in this manual focuses on switch hardware. It includes 
information on some CLI commands that pertain directly to hardware configuration, but it is not intended 
as a software users guide. There are several OmniSwitch users guides that focus on switch software 
configuration. Consult those guides for detailed information and examples for configuring your switch 
software to operate in a live network environment. See “Documentation Roadmap” on page -vi and 
“Related Documentation” on page -viii for further information on software configuration guides available 
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
OmniSwitch Release Notes
A “Getting Started” chapter is included in the OmniSwitch 6560 Hardware Users Guide. This chapter 
provides all the information you need to get your switch up and running the first time. It also includes 
succinct overview information on fundamental aspects of the switch.
At this time you should also familiarize yourself with the Release Notes that accompanied your switch. 
This document includes important information on feature limitations that are not included in other 
user guides.
Stage 2: Gaining Familiarity with Basic Switch Functions
Pertinent Documentation: Hardware Users Guide
OmniSwitch Switch Management Guide
Once you have your switch up and running, you will want to begin investigating basic aspects of its 
hardware and software. Information about switch hardware is provided in the OmniSwitch 6560 Hardware 
Guide. This guide provide specifications, illustrations, and descriptions of all hardware components. It also 
includes steps for common procedures, such as removing and installing switch components.
This guide is the primary users guide for the basic software features on a single switch. This guide 
contains information on the switch directory structure, basic file and directory utilities, switch access

<<<PAGE 7>>>
OmniSwitch 6865 Hardware Users Guide
December 2025
vii
security, SNMP, and web-based management. It is recommended that you read this guide before 
connecting your switch to the network.
Stage 3: Integrating the Switch Into a Network
Pertinent Documentation: OmniSwitch Network Configuration Guide
When you are ready to connect your switch to the network, you will need to learn how the OmniSwitch 
implements fundamental software features, such as 802.1Q, VLANs, Spanning Tree, and network routing 
protocols. The Network Configuration Guide guide contains overview information, procedures, and 
examples on how standard networking technologies are configured on the OmniSwitch.
Anytime
The OmniSwitch CLI Reference Guide contains comprehensive information on all CLI commands 
supported by the switch. This guide includes syntax, default, usage, example, related CLI command, and 
CLI-to-MIB variable mapping information for all CLI commands supported by the switch. This guide can 
be consulted anytime during the configuration process to find detailed and specific information on each 
CLI command.

<<<PAGE 8>>>
viii
OmniSwitch 6865 Hardware Users Guide
December 2025
Related Documentation
The following are the titles and descriptions of all the OmniSwitch user guides:
• Hardware Users Guide
Complete technical specifications and procedures for all OmniSwitch chassis, power supplies, fans, and 
Network Interface (NI) modules.
• OmniSwitch CLI Reference Guide
Complete reference to all CLI commands supported on the OmniSwitch. Includes syntax definitions, 
default values, examples, usage guidelines and CLI-to-MIB variable mappings.
• OmniSwitch Switch Management Guide
Includes procedures for readying an individual switch for integration into a network. Topics include the 
software directory architecture, image rollback protections, authenticated switch access, managing 
switch files, system configuration, using SNMP, and using web management software (WebView).
• OmniSwitch Network Configuration Guide
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

<<<PAGE 9>>>
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-1
1   Getting Started and Instal-
lation
Getting Started
Preparing for the Installation
Alcatel-Lucent Enterprise products must be installed by a professional installer. It is the responsibility of 
the installer to comply with product specifications and all applicable local and national codes.
When preparing for installation, unpack the product as close as possible to the location where it will be 
installed.
Elevated Operating Ambient Temperature
If installed in a closed or multi-rack assembly, the operating ambient temperature of the rack environment 
may be greater than the room’s ambient temperature. Therefore, consideration should be given to the 
maximum rated ambient temperature (Tmra). When operating at 74°C ambient temperature the switch 
must be installed in a suitable closed rack or cabinet enclosure.
Reduced Air Flow
Installation of the equipment should be such that the amount of air flow required for safe operation of the 
equipment is not compromised. Refer to “Providing Air Flow and Minimum Recommended Clearances” 
on page 1-3 for more information.
Mechanical Loading
Mounting of the equipment in the rack should be such that a hazardous condition is not achieved due to 
uneven loading.
Caution: An operating Omniswitch may be hot to the touch.

<<<PAGE 10>>>
Getting Started
Getting Started and Installation
page 1-2
OmniSwitch 6865 Hardware Users Guide
December 2025
Circuit Overloading
Consideration should be given to the connection of the equipment to the supply circuit and the effect that 
overloading of circuits could have on overcurrent protection and supply wiring. Appropriate consideration 
of equipment nameplate ratings should be used when addressing this concern.
Reliable Earthing
Reliable earthing of rack mounted equipment should be maintained. Particular attention should be given to 
supply connections other than direct connections to the branch (e.g., use of power strips).
Additional Electrical Requirements
The switches have the following general electrical requirements:
• AC and DC power supply support.
• Each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords.
• Each switch requires one grounded electrical outlet per power supply.
• ALE provided power cords are UL recognized to IEC 62368-1 exceeding the maximum amperage 
requirement for the power source. If using a non-ALE provided power cord the installer shall confirm it 
meets the minimum electrical requirements of the power source.
Redundant AC Power. It is recommended that each power supply resides on a separate circuit. With 
redundant power, if a single circuit fails, the switch’s remaining power supply (on separate circuits) can 
remain operational.
Electrical Surge Warning
In order to help protect equipment against electrical surges please take note of the following recommenda-
tions and guidelines:
1.
Earth grounding of all devices is fundamental to ensure long term reliability.
• All electrical equipment must be installed by a qualified, licensed electrician.
• Every power supply that is connected to building power should be earth grounded.
• Earth grounding for the power cable, should be verified to be 0.01 ohm or less.
• Each switch should be grounded to same earth ground as the power supply.
• Each powered device, such as an AP or camera, should be connected to earth ground.
• Each surge suppression device should be connected to earth ground.
2.
Shielded cables (STP) offer some minimal level of additional protection over unshielded Ethernet cables 
(UTP) but the use of a surge protector is still recommended.
• It is suggested to use STP Cat5e or better for 1Gbps Ethernet switches for any outdoor application or 
applications where Ethernet cables come in close proximity to alternating current conductors.
• Always install cables according to manufacturer requirements.

<<<PAGE 11>>>
Getting Started and Installation
Getting Started
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-3
3.
For any connections where integrity of the cabling within a building ground is questionable (i.e outdoor 
connections), copper Ethernet ports must be connected with an appropriate surge protection device, inline, 
between the PSE and PD per the manufacturer’s recommendations for connection and grounding.
4.
Caution should be taken for any cable connected to any outdoor device, not only on the device grounding, 
but to ensure that any outdoor device cables that could carry surge currents, do not pass those surge currents 
to upstream Ethernet switches.
Caution - Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity due 
to the dielectric properties of their construction materials in addition, this build up of electricity could lead 
to a Cable Discharge Event (CDE). A CDE can occur due to the differential in charges on the cable and the 
equipment it’s being connected to. It is recommended that installers momentarily ground all copper 
Ethernet cables (especially in new cable runs) to a suitable and safe earth ground before connecting them to 
the port.
Note: Failure to follow the above recommendations could result in voiding the warranty of the affected 
ALE product. 
Providing Air Flow and Minimum Recommended Clearances 
• Switches operating in an environment at or above 65°C require air flow.
• Switches operating in an environment below 65°C do not require airflow. 
• When mounting the chassis on a flat service (e.g., table) be sure that the top of the switch, 
with the larger heat sinks, is facing out and away from the mounting surface.
• Be sure to refer to minimum recommended clearances provided in the table below.
 
Minimum Recommended Clearances
Top (Rack mount)
0.875 inches (1/2 RU) for switches operating in an ambient 
temperature below 65°C; 
1.75 inches (1 RU) for switches operating in an ambient temperature 
at or above 65°C. (See important air flow requirements outlined 
above.)
Top (Table mount) 
0.875 inches; for table mounting, be sure to install the mounting 
brackets as described in the section, “Preparing the Chassis and 
Power Supply Tray Assembly.”
Bottom (Rack mount)
No minimum clearance required. However, be sure that the bottom of 
the chassis is not in direct contact with any equipment below. 
Bottom (Table mount)
0.875 inches; for table mounting, be sure to install the mounting 
brackets as described in the section, “Preparing the Chassis and 
Power Supply Tray Assembly.”.

<<<PAGE 12>>>
Getting Started
Getting Started and Installation
page 1-4
OmniSwitch 6865 Hardware Users Guide
December 2025
Items Included
Depending on your order the following items may be included:
• OmniSwitch chassis with power supplies and modules
• Country specific power cord(s)
• Cover Panels
• Rack Mount Brackets
• Product Documentation and Training Cards           
• DB9-RJ45 Connector
DNV Installations
0.875 inches (1/2 RU) for OS6865-U12X and OS6865-P16X that require 
a DNV power supply cover, operating between -40°C to 55°C (-40°F to
131°F).
1.75 inches (1 RU) for OS6865-U28X that requires a DNV power supply
cover, operating between -40°C to 55°C (-40°F to 131°F).
Sides
2 inches
Rear
6 inches
Front
6 inches
Minimum Recommended Clearances

<<<PAGE 13>>>
Getting Started and Installation
Preparing the Chassis and Power Supply Tray Assembly
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-5
Preparing the Chassis and Power Supply Tray 
Assembly
The power supply tray may be mounted at the side or the rear of the chassis. Side mounted tray assem-
blies are typically used for rack mount applications; rear mounted tray assemblies are typically used for 
table mount applications.
Side Mount Power Supply Tray
1.
To mount the power supply tray to the side of the chassis, be sure that the attachment brackets are installed 
in the proper positions with the Front Chassis and Front Tray brackets aligned. 
Required Brackets for Side Mount Power Supply Tray (Brackets may be factory-installed.)
Front Chassis-to-Tray Bracket 
Front Chassis-to-Tray Bracket 
Front Tray-to-chassis Bracket 
(Aligns with Front Chassis-to-Tray Bracket (See Next Step)
Rear Chassis-to-Tray Bracket

<<<PAGE 14>>>
Preparing the Chassis and Power Supply Tray Assembly
Getting Started and Installation
page 1-6
OmniSwitch 6865 Hardware Users Guide
December 2025
2.
Align the holes in the power supply tray and fasten the two parts into a single assembly using the 
attachment screws.
Rear Mount Power Supply Tray
Note: For rear mount power supply assemblies, factory-installed power tray 
brackets (shown on page 5) should be removed.
2 (M4) Screws*
4 (M3X6) Screws
*Note: Four M4 screws are pre-installed on the rear of the chassis for mounting the power 
supply tray to the rear of the chassis. Use those screws for installing the power supply on the 
side of the chassis.

<<<PAGE 15>>>
Getting Started and Installation
Preparing the Chassis and Power Supply Tray Assembly
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-7
1.
To mount the power supply tray to the rear of the chassis, insert the tray tabs into the slots at the rear panel 
of the chassis. Once the tabs are inserted and the face of the tray is flush against the chassis rear panel, 
insert and tighten the attachment screws.
OS6865-U12X / P16X
OS6865-U28X

<<<PAGE 16>>>
Preparing the Chassis and Power Supply Tray Assembly
Getting Started and Installation
page 1-8
OmniSwitch 6865 Hardware Users Guide
December 2025
Attaching Rack Mount Flanges
Before rack mounting, rack mount flanges must be installed at the left and right sides of the chassis/tray 
assembly. To attach the flanges, align the holes in with the threaded holes in the side of the chassis and 
power supply tray. Insert and tighten the attachment screws. 
Attaching Rack Mount Flanges
Attaching Table Mount Feet
1.
Before table mounting, table mount feet must be installed at the left and right sides of the chassis/tray 
assembly. To install the feet, align the holes with the threaded holes in the sides of the chassis and power 
supply tray, as shown below. Insert and tighten the attachment screws.
Important. Table mount feet provide the 1/2 RU clearance required at the bottom of the chassis. Do not 
attempt to operate the OS6865-P16X on a tabletop surface without these feet properly installed. See 
“Providing Air Flow and Minimum Recommended Clearances” on page 1-3 for more clearance informa-
tion.
Use four (4) screws 
(M4X6mm).
Use four (4) screws (M4X6mm) 
and mounting holes ‘B’(4).

<<<PAGE 17>>>
Getting Started and Installation
Installing Power Supplies
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-9
 
Attaching Table Mount Feet
Table Mount Assembly with 1/2 RU Space Under Chassis
Installing Power Supplies
Once the chassis and tray are assembled and the mounting brackets are attached, install the power 
supplies.
Note. Whenever connecting or disconnecting a power supply to/from a chassis, 
the power supply must be disconnected from the power source.
Use five (5) screws (M4X6mm).
Mounting holes ‘D’ (4) and ‘E’ 
(1).
Use four (4) screws (M4X6mm).
Mounting holes ‘C’ (4).

<<<PAGE 18>>>
Installing Power Supplies
Getting Started and Installation
page 1-10
OmniSwitch 6865 Hardware Users Guide
December 2025
Installing Power Supplies for Side Mount Trays
1.
Slide the power supply into the tray and insert the tabs located at the bottom-rear of the power supply into 
the slots at the base of the power supply tray. 
2.
Align and tighten the thumb screw at the front of the power supply unit.

<<<PAGE 19>>>
Getting Started and Installation
Installing Power Supplies
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-11
3.
Plug the power supply-to-chassis connector cable (provided) into the DB-15 connectors located at the rear 
of the power supply and the chassis. 
4.
For redundant power supply configurations, repeat these steps for the additional power supply at the other 
side of the power supply tray.
Note. The switch does not provide an on/off switch. Instead, the switch powers 
on when a power cord is plugged into the power supply’s front panel and 
plugged into a power source. Do not connect to a power source until all power 
supplies and power supply-to-chassis cables are installed and the switch is ready 
to boot. 
Installing Power Supplies for Rear Mount Trays
1.
Orient the power supply as shown below. Insert the guide pins (located on either side of the DB-15 
connector) into the guide holes in the rear of the chassis. 
Power Supply-to-Chassis Cable (Pro-
vided)
Hole for Guide Pin

<<<PAGE 20>>>
Installing Power Supplies
Getting Started and Installation
page 1-12
OmniSwitch 6865 Hardware Users Guide
December 2025
For this example, table mount assembly shown.
2.
Push the power supply into place until the connector is fully seated and tighten the thumb screw at the front 
of the power supply unit.
3.
For redundant power supply configurations, repeat these steps using the power supply connector and thumb 
screw hole located at the other side of the chassis and power supply tray.
Note. The switch does not provide an on/off switch. Instead, the switch powers 
on when a power cord is plugged into the power supply’s front panel and 
plugged into a power source. Do not connect to a power source until all power 
supplies and power supply-to-chassis cables are installed and the switch is ready 
to boot.

<<<PAGE 21>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-13
Power Cord and Holder
Mounting the OmniSwitch 6865
Rack Mounting
General Rack Mounting Recommendations
• Install the switch in the rack using the rack manufacturer’s recommended attachment screws (not 
provided). Always follow rack manufacturer’s specifications when installing. 
• Be sure to accommodate spacing requirements when rack mounting the switch. See “Providing Air 
Flow and Minimum Recommended Clearances” on page 1-3 for more information. 
• Pre-marking the holes on the rack where the switch is to be installed can be helpful.
• Use an additional person to help lift and position the chassis/power supply assembly in the rack during 
installation.
• To keep the rack from becoming top heavy, install switches toward the bottom of the rack first.
• Use the OS6865-REAR-MNT mounting kit to help secure the rear of the OS6865-U28X.
• Use the OS6865-TRAY-1U mounting kit to rack-mount two power supply trays side-by-side.

<<<PAGE 22>>>
Mounting the OmniSwitch 6865
Getting Started and Installation
page 1-14
OmniSwitch 6865 Hardware Users Guide
December 2025
OS6865-REAR-MNT Mounting Kit for OS6865-U28X (Overview)
Attach Side Rails
Mount Front Brackets
Slide Rear Brackets into Side Rails and Mount

<<<PAGE 23>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-15
 OS6865-REAR-MNT (Mounting Hole Locations for Chassis and Rear Power Supply Tray)
 OS6865-REAR-MNT (Mounting Hole Locations for Chassis Only)
22.5”
Chassis Mounting Holes ‘A’ (3)
Tray Mounting Holes ‘A’ (4)
Chassis Mounting Holes ‘C’ (3)
Bracket Mounting holes ‘C’ (4)
 26 in. (with sliding rear bracket)
18.3”
Chassis Mounting Holes ‘B’ (2)
and Middle Hole (1)
Chassis Mounting Holes ‘D’ (2)
and Middle Hole (1)
(Use M4X6mm Screws)
 Note: 21.8 in. depth with sliding rear bracket.

<<<PAGE 24>>>
Mounting the OmniSwitch 6865
Getting Started and Installation
page 1-16
OmniSwitch 6865 Hardware Users Guide
December 2025
 OS6865-TRAY-1U (Mounting Hole Locations for Power Supply Tray)
Table Mounting
Important. Table mount feet provide the 1/2 RU clearance required at the 
bottom of the chassis. Do not attempt to operate the switch on a tabletop 
surface without these feet properly installed. For information on installing, 
refer to “Attaching Table Mount Feet” on page 1-8. See “Providing Air Flow and 
Minimum Recommended Clearances” on page 1-3 for more clearance information.
1.
Place the assembly on the tabletop surface. Refer to all requirements—including those outlined in the 
“Preparing for the Installation” and “Providing Air Flow and Minimum Recommended Clearances” on 
page 1-3—before placing the switch.
16”
Tray Mounting Holes ‘D’ (4)
Tray Mounting Holes ‘B’ (4)
(Use M4X6mm Screws)
 Note: 19.5 in. depth with sliding rear bracket.

<<<PAGE 25>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-17
2.
Fasten the assembly to the surface using attachment bolts or screws as appropriate for the 
surface material.
DIN Rail Mounting - Power Supply
The power supply can be mounted on a DIN rail. 
1.
Attach DIN rail clip to the power supply using the screws (M4X6mm) provided. 
2.
Hook the bottom of the DIN rail clip under the bottom of the DIN rail. 
3.
Push up, compressing the tension spring at the bottom of the DIN rail clip.
4.
Once the top of the DIN rail clip is over the top of the DIN rail release the tension on the tension spring and 
ensure the top and bottom of the DIN rail clip are securely attached. 
Warning. When mounted vertically, suitable for mounting on concrete or other 
non-combustible surfaces only (as shown).

<<<PAGE 26>>>
Mounting the OmniSwitch 6865
Getting Started and Installation
page 1-18
OmniSwitch 6865 Hardware Users Guide
December 2025
DIN Rail Mounting Power Supply
DIN Rail Unmounting - Power Supply
1.
Push up, compressing the tension spring at the bottom of the DIN rail clip.
2.
Once the top of the DIN rail clip is above the top of the DIN rail, lift the unit from the DIN rail. 
DIN Rail Mounting - Chassis
The chassis can be mounted on a DIN rail (OS6865-DIN-MNT). 
1.
Attach two (2) flat brackets to front and rear of chassis side mount brackets using four (4) screws 
(M5X10mm) provided for each flat bracket.
2.
Hook the top of the DIN rail clips over the top of the DIN rail. 
3.
Rotate assembly down and pull down on the DIN rail clip strap allowing bottom of DIN rail clip to hook on 
the bottom of the DIN rail. 
4.
Release the DIN rail clip strap, securing the assembly in place. 
Power Supply - Mounted
DIN Rail Clip - Attachment

<<<PAGE 27>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-19
Warning. When mounted vertically, suitable for mounting on concrete or other 
non-combustible surfaces only (as shown). 
Attaching Brackets To Chassis
DIN Rail Unmounting - Chassis
1.
Pull down on the DIN rail clip straps releasing the bottom of DIN rail clips.
2.
Rotate the bottom of the assembly away from the DIN rail and lift the assembly off the DIN rail.   
Flat Brackets to Chassis 
Flat Bracket Assembly

<<<PAGE 28>>>
Mounting the OmniSwitch 6865
Getting Started and Installation
page 1-20
OmniSwitch 6865 Hardware Users Guide
December 2025
 
DIN Rail Mounting Chassis Assembly
DNV Mounting Steps
The OmniSwitch chassis can be mounted according to DNV standards. The parts required are contained in 
the OS6865-DNV-FRCK and OS6865-DNV-HRCK kits.
• OS6865-DNV-FRCK (Full Rack) - (2) Side Rails, (2) Rear Brackets, (1) Support Bracket, (21) 
M4X8MM with DNV Power Supply Tray and Cover - (1) Power Supply Tray (182343-10), (1) 
Power Supply Cover, (1) Filler Bracket, (2) Slider Brackets, (6) M3X6MM (Flat), (4) M3X6MM 
(Round)
• OS6865-DNV-HRCK (Half Rack) - (2) Front Brackets, (2) Side Rails, (2) Rear Brackets, (1) Front 
Chassis-to-Tray Bracket, (1) Rear Chassis-to-Tray Bracket, (8) M4X8MM, (8) M3X6MM, (8) 
M4X6MM with DNV Power Supply Tray and Cover - (1) Power Supply Tray (182343-10), (1) 
Mounted (Chassis Not 
Completed Mounting Example

<<<PAGE 29>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-21
Power Supply Cover, (1) Filler Bracket, (2) Slider Brackets, (6) M3X6MM (Flat), (4) M3X6MM 
(Round)
Full-rack Mounting
1 Install the Side Rails, Rear Brackets, and Power Supply Tray.
Rails and Power Supply Tray
2 Install Power Supplies.
Side Rails, Rear Brackets, and Power Supply Tray with Power Supplies
Side Rail
(7) M4X8MM
Holes ‘A’
Rear Brackets
Power Supply Tray 
(4) M4X8MM
Support 
Bracket
Side Rail
(7) 
M4X8MM
Thumb

<<<PAGE 30>>>
Mounting the OmniSwitch 6865
Getting Started and Installation
page 1-22
OmniSwitch 6865 Hardware Users Guide
December 2025
3 Install Power Supply Cover.
Power Supply Tray Cover (Power Supplies Not Shown)
4 Final Assembly
Final Assembly
Filler Bracket
(2) M3X6MM
Slider Brackets
(2) M3X6MM
Cover
(4) M3X6MM
Bottom View
Top

<<<PAGE 31>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-23
Half-rack Mounting
1.
Install / align front and rear chassis-to-tray brackets. 
Required Brackets for Side Mount Power Supply Tray (Brackets may be factory-installed.)
Front Chassis-to-Tray Bracket 
Front Chassis-to-Tray Bracket 
Front Tray-to-chassis Bracket 
(Aligns with Front Chassis-to-Tray Bracket (See Next 
Rear Chassis-to-Tray Bracket

<<<PAGE 32>>>
Mounting the OmniSwitch 6865
Getting Started and Installation
page 1-24
OmniSwitch 6865 Hardware Users Guide
December 2025
2.
Align the holes in the power supply tray and fasten the two parts into a single assembly using the 
attachment screws.
Secure Power Supply Tray to Chassis
3.
Install Front Brackets and Side Rails. 
Attach Brackets and Rails
(2) M4X8MM
(4) M3X6
Side Rail
(3) M4X8MM
Holes ‘A’
Rear Brackets
Side Rail
(3) 
M4X8MM
Front Bracket
(4) M4X6MM
Holes ‘B’
Front Bracket
(4) M4X6MM
Holes (3) ‘B’

<<<PAGE 33>>>
Getting Started and Installation
Mounting the OmniSwitch 6865
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-25
4.
Install Power Supplies using thumb screws. 
Side Rails, Rear Brackets, and Power Supply Tray with Power Supplies
5.
Install Power Supply Cover. 
Side Power Supply Tray Cover (Power Supplies Not Shown)
Thumb Screws toward front (not 
Filler Bracket
(2) 
Slider Brackets
(2) M3X6MM
Cover
(4) M3X6MM
Bottom 
Top

<<<PAGE 34>>>
Additional DIN / Wall Mounting Examples
Getting Started and Installation
page 1-26
OmniSwitch 6865 Hardware Users Guide
December 2025
6.
Final Assembly
Final Assembly
Additional DIN / Wall Mounting Examples
This section provides images of additional mounting examples.
• Be sure that the wall section and wall attachment screws (not provided) have the required strength to 
easily support the chassis assembly, mounting brackets, and power supplies.
• For each mounting hole the use of screws long enough (i.e. 3.5mm X 25mm) to penetrate any soft 
surfaces, such as sheetrock or drywall, and securely attach to a hard surface such as a wall stud or 
plywood backing is recommended.

<<<PAGE 35>>>
Getting Started and Installation
Additional DIN / Wall Mounting Examples
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-27
OS6865-U12X/P16X DIN Rail Examples

<<<PAGE 36>>>
Additional DIN / Wall Mounting Examples
Getting Started and Installation
page 1-28
OmniSwitch 6865 Hardware Users Guide
December 2025
OS6865-U12X/P16X Wall Mount Examples
OS6865-U28X DIN Mount Examples

<<<PAGE 37>>>
Getting Started and Installation
Connections and Cabling
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-29
OS6865-U28X Wall Mount Examples
Connections and Cabling
Once the switch is properly installed, connect all network and management cables required for 
network applications. 
Network Cable Installation Warning
Never install exposed network cables outdoors. Install network cables per manufacturer requirements.
For additional information on cabling for console, USB, and other connections, refer to the OmniSwitch 
AOS Switch Management Guide.
Serial Connection to the Console Port
The console port provides a serial connection to the switch using an RJ45 connector and is required when 
logging into the switch for the first time.
Serial Connection Default Settings
baud rate 
9600
parity none
none
data bits (word size)
8
stop bits
1

<<<PAGE 38>>>
Connections and Cabling
Getting Started and Installation
page 1-30
OmniSwitch 6865 Hardware Users Guide
December 2025
For information on modifying these settings, refer to the OmniSwitch AOS Switch Management Guide.
Booting the Switch
The switch does not have a power on/power off switch. To boot a switch, plug a power cord into the 
power supply unit and then plug the cord into an easily-accessible, properly grounded power outlet. (Do 
not use an extension cord.) 
The switch will power on and boot automatically.
Connect any redundant power supply power cords and plug them into a power outlet as well.
System and Port LEDs
During the boot process, component LEDs will flash and change color, indicating different stages of the 
boot.
Note. Be sure the boot process is complete before checking LED status. If LEDs 
indicate persist errors, contact Alcatel-Lucent Customer Support. 
System LEDs
OK
Solid Green: Normal operation
Solid Amber: Software error detected
Blinking Green: Diagnostics in progress
VC
Off: The switch is booting
Blinking Green: VC Master. Unit number identified by the number of blinks. Pauses 
every 5 seconds.
Blinking Amber: VC Slave. Unit number identified by the number of blinks. Pauses 
every 5 seconds.
PS1
Off: Power supply not present
Solid Green: Normal operation
Solid Amber: Power supply error detected
PS2
Off: Power supply not present
Solid Green: Normal operation
Solid Amber: Power supply error detected
SFP/SFP+ Port LEDs
SFP and SFP+ 
Ports
Off: No link or link down
Solid Green: Link up
Blinking Green: Link up with activity
Solid Amber: Link up (100M)
Blinking Amber: Link up with activity (100M)
RJ45 (PoE) Ports
Off: No link or link down
Solid Green: Link up (no PoE)
Blinking Green: Link up (no PoE) with activity
Solid Amber: Link up (PoE devices connected)
Blinking Amber: Link up (PoE devices connected) with activity

<<<PAGE 39>>>
Getting Started and Installation
Connections and Cabling
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-31
Once the switch has completely booted, connect to the console port and log in to the switch’s Command 
Line Interface (CLI) and configure basic information. For more information, refer to “The First Login 
Session” on page 1-31.
The First Login Session
To complete the setup process, follow these steps during the first login session:
• Log in to the switch
• Unlock session types
• Change the login password
• Set the date and time
• Set optional system information
• Save changes
Important. Connect to the switch via the console port before initiating the first 
login session.
Logging In to the Switch
At the login and password prompts, use the switch’s default settings:
Note. A user account includes a login name, password, and user privileges. Privileges determine whether 
the user has read or write access to the switch and which commands the user is authorized to execute. For 
detailed information on setting up and modifying user accounts, refer to the OmniSwitch Switch Manage-
ment Guide.
The default welcome banner—which includes information such as the current software version and system 
date—displays, followed by the CLI command prompt:
Welcome to the Alcatel-Lucent Enterprise OS6865 8.3.1, June 03, 2016.
Copyright (c) 1994-2014 Alcatel-Lucent.  All Rights Reserved.
Copyright (c) 2014-2016 Alcatel-Lucent Enterprise.  All Rights Reserved.
OmniSwitch(tm) is a trademark of Alcatel-Lucent,
registered in the United States Patent and Trademark Office.
->
Unlocking Session Types
Remote session types (Telnet, FTP, WebView, SNMP) are restricted until they are manually unlocked by 
the user. The CLI command used to unlock session types is aaa authentication.
Login:
admin
Password:
switch

<<<PAGE 40>>>
Connections and Cabling
Getting Started and Installation
page 1-32
OmniSwitch 6865 Hardware Users Guide
December 2025
Note. Unlocking session types grants switch access to non-local sessions (e.g., 
Telnet). As a result, anyone with the correct user login and password will have 
remote access to the switch. 
For more information on switch security, refer to the OmniSwitch AOS Switch Management Guide.
Unlocking All Session Types
To unlock all session types, enter the following command syntax at the CLI prompt:
-> aaa authentication default local
Unlocking Specific Session Types
You can also unlock specific session types (console, telnet, ftp, http, snmp, ssh). For example, to unlock 
Telnet sessions, enter the following command:
-> aaa authentication telnet local
Refer to the OmniSwitch CLI Reference Guide for complete aaa authentication command syntax options.
Changing the Login Password
Change the login password for admin user sessions by following the steps below:
1.
Be sure that you have logged into the switch as user type admin (see “Logging In to the Switch” on 
page 1-31).
2.
Type password at the prompt and press Enter.
3.
Enter the new password at the prompt.
Note. Be sure to remember or securely record all new passwords; overriding 
configured passwords on an OmniSwitch is restricted.
4.
You will be prompted to re-enter the password. Enter the password a second time.
New password settings are automatically saved in real time to the local user database; the user is not 
required to enter an additional command in order to save the password information. Also note that new 
password information is retained following a reboot. All subsequent login sessions, including those 
through the console port, will require the new password to access the switch.
For detailed information on managing login information, including user names and passwords, refer to the 
OmniSwitch Switch Management Guide.
Setting the System Time Zone
The switch’s default time zone is UTC. If you require a time zone that is specific to your region, or if you 
need to enable Daylight Savings Time (DST) on the switch, you can configure these settings via the 
system timezone and system daylight-savings-time commands.

<<<PAGE 41>>>
Getting Started and Installation
Connections and Cabling
OmniSwitch 6865 Hardware Users Guide
December 2025
page 1-33
For detailed information on configuring a time zone for the switch, refer to the OmniSwitch AOS Switch 
Management Guide.
Setting the Date and Time
Set the current time for the switch by entering system time, followed by the current time in hh:mm:ss.
To set the current date for the switch, enter system date, followed by the current date in mm/dd/yyyy.
Setting Optional Parameters
Specifying an Administrative Contact
An administrative contact is the person or department in charge of the switch. If a contact is specified, 
users can easily find the appropriate network administrator if they have questions or comments about the 
switch. To specify an administrative contact, use the system contact command.
Specifying a System Name
The system name is a simple, user-defined text description for the switch. To specify a system name, use 
the system name command.

<<<PAGE 42>>>
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-1
2   Chassis and Power
OmniSwitch 6865-P16X
The Alcatel-Lucent Enterprise OmniSwitch® 6865 series are Gigabit Ethernet (GigE) and 10 Gb Ethernet 
(GigE) switches designed for demanding electrical and severe temperature environments.
OmniSwitch 6865-P16X (Side Mounted Power Supply Tray Shown)
OmniSwitch 6865-P16X Chassis Specifications
Fans
None
Power Supplies
2 total (1 primary PSU and 1 optional backup PSU)
Rack Unit Dimensions
2 RU (Additional clearance is required for airflow, 
see “Providing Air Flow and Minimum Recommended Clear-
ances” on page 2-17 for more information.)
Dimensions (WxHxD)
21.6 cm (8.5 in) x 8.81 cm (3.47 in) x 26 cm (10.24 in)
Weight
5.07 kg (11.18 lb)
Operating Temperature (TMRA)
With airflow: -40°C to 74°C (-40°F to 165°F)
Without airflow: -40°C to 65°C (-40°F to 149°F)
With DNV Power Supply Cover (with or without airflow):
-40°C to 55°C (-40°F to 131°F)

<<<PAGE 43>>>
OmniSwitch 6865-P16X
Chassis and Power
page 2-2
OmniSwitch 6865 Hardware Users Guide
December 2025
Storage Temperature 
-40°C to 85°C (-40°F to 185°F)
Operating and Storage Humidity
5% to 95% non-condensing
Altitude
4000m/13,000 feet
75W HPoE / 60W 802.3bt Ports
4
30W PoE+ Ports
8
SFP Ports
2
1G/10G SFP+ Ports
2
1588v2 Capability
Supported
PoE Power Budget
See “Power over Ethernet Budget” on page 3-48 for more 
information.
Power Consumption (idle)
30W
OmniSwitch 6865-P16X Chassis Specifications

<<<PAGE 44>>>
Chassis and Power
OmniSwitch 6865-P16X
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-3
Chassis Front Panel
Note: For LED descriptions, refer to “System and Port LEDs” on page 2-43.
Front Panel Descriptions (Left to Right)
Console (RJ45)
For console or modem
USB Type A
For storage devices that can download code or save configuration 
information, such as flash-based pen drives or external hard drives. 
For Maintenance Only.
Ports 1 and 2
Two (2) fixed SFP+ (1G/10G)
Ports 3 and 4
Two (2) 1000Base-X SFP
Ports 5 through 8
Four (4) 10/100/1000Base-T PoE+/802.3bt (supporting 75W HPoE / 
60W 802.3bt per port)
Ports 9 through 16
Eight (8) 10/100/1000Base-T PoE+ (supporting 30W PoE per port)
Note: Does not support half-duplex connections.

<<<PAGE 45>>>
OmniSwitch 6865-U12X
Chassis and Power
page 2-4
OmniSwitch 6865 Hardware Users Guide
December 2025
Chassis Rear Panel
OmniSwitch 6865-U12X
Rear Panel Descriptions (Left to Right)
PS2
Power Supply Connector
PS1
Power Supply Connector
Grounding Block
Chassis Ground
OmniSwitch 6865-U12X Chassis Specifications
Fans
None
Power Supplies
2 total (1 primary PSU and 1 optional backup PSU)
Rack Unit Dimensions
2 RU (Additional clearance is required for airflow, 
see “Providing Air Flow and Minimum Recommended Clear-
ances” on page 2-17 for more information.)
Dimensions (WxHxD)
21.6 cm (8.5 in) x 8.81 cm (3.47 in) x 26 cm (10.24 in)
Weight
5.17 kg (11.40 lb)
Operating Temperature (TMRA)
With airflow: -40°C to 74°C (-40°F to 165°F)
Without airflow: -40°C to 65°C (-40°F to 149°F)
With DNV Power Supply Cover (with or without airflow):
-40°C to 55°C (-40°F to 131°F)
Storage Temperature 
-40°C to 85°C (-40°F to 185°F)
Operating and Storage Humidity
5% to 95% non-condensing
Altitude
4000m/13,000 feet
75W HPoE / 60W 802.3bt Ports
4

<<<PAGE 46>>>
Chassis and Power
OmniSwitch 6865-U12X
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-5
Chassis Front Panel
Note: For LED descriptions, refer to “System and Port LEDs” on page 2-43.
30W PoE+ Ports
0
SFP Ports
6
1G/10G SFP+ Ports
2
1588v2 Capability
Supported
PoE Power Budget
See “Power over Ethernet Budget” on page 3-48 for more 
information.
Power Consumption (idle)
29W
Front Panel Descriptions (Left to Right)
Console (RJ45)
For console or modem
USB Type A
For storage devices that can download code or save configuration 
information, such as flash-based pen drives or external hard drives. 
For Maintenance Only.
Ports 1 and 2
Two (2) fixed SFP+ (1G/10G)
Ports 3 and 4
Two (2) 1000Base-X SFP
Ports 5 through 8
Four (4) 100Base-FX/1000Base-X SFP
Ports 9 through 12
Four (4) 10/100/1000Base-T PoE+/802.3bt (supporting 75W HPoE / 
60W 802.3bt per port)
Note: Does not support half-duplex connections.
OmniSwitch 6865-U12X Chassis Specifications

<<<PAGE 47>>>
OmniSwitch 6865-U28X
Chassis and Power
page 2-6
OmniSwitch 6865 Hardware Users Guide
December 2025
Chassis Rear Panel
OmniSwitch 6865-U28X
Rear Panel Descriptions (Left to Right)
PS2
Power Supply Connector
PS1
Power Supply Connector
Grounding Block
Chassis Ground
OmniSwitch 6865-U28X Chassis Specifications
Fans
None
Power Supplies
2 total (1 primary PSU and 1 optional backup PSU)
Rack Unit Dimensions
1 RU (Additional clearance is required for airflow, 
see “Providing Air Flow and Minimum Recommended Clear-
ances” on page 2-17 for more information.)
Dimensions (WxHxD)
43.75 cm (17.2 in) x 4.4 cm (1.73 in) x 26.88 cm (10.6 in)
Weight
6.28 kg (13.85 lb)
Operating Temperature (TMRA)
With airflow: -40°C to 74°C (-40°F to 165°F)
Without airflow: -40°C to 65°C (-40°F to 149°F)
With DNV Power Supply Cover (with or without airflow):
-40°C to 55°C (-40°F to 131°F)
Storage Temperature 
-40°C to 85°C (-40°F to 185°F)
Operating and Storage Humidity
5% to 95% non-condensing
Altitude
4000m/13,000 feet
75W HPoE / 60W 802.3bt Ports
4

<<<PAGE 48>>>
Chassis and Power
OmniSwitch 6865-U28X
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-7
Chassis Front Panel
Note: For LED descriptions, refer to “System and Port LEDs” on page 2-43.
30W PoE+ Ports
0
SFP Ports
20
1G/10G SFP+ Ports
4
1588v2 Capability
Supported
PoE Power Budget
See “Power over Ethernet Budget” on page 3-48 for more 
information.
Power Consumption (idle)
50W
Front Panel Descriptions (Left to Right)
Console (RJ45)
For console or modem
USB Type A
For storage devices that can download code or save configuration 
information, such as flash-based pen drives or external hard drives. 
For Maintenance Only.
Ports 1 through 4
Four (4) fixed SFP+ (1G/10G)
Ports 5 through 24
Twenty (20) 100Base-FX/1000Base-X SFP
Ports 25 through 28
Four (4) 10/100/1000Base-T PoE+/802.3bt (supporting 75W HPoE / 
60W 802.3bt per port)
Note: Does not support half-duplex connections.
OmniSwitch 6865-U28X Chassis Specifications

<<<PAGE 49>>>
Power Supplies
Chassis and Power
page 2-8
OmniSwitch 6865 Hardware Users Guide
December 2025
Chassis Rear Panel
Power Supplies
OS6865-BP - 180W AC Power Supply
Rear Panel Descriptions (Left to Right)
PS2
Power Supply Connector
PS1
Power Supply Connector
Grounding Block
Chassis Ground
Ports 29 and 30
QSFP+ VFL Ports
OS6865-BP - 180W Power Supply
Description
Modular AC power supply. Up to two (2) power supplies may 
be installed.
Dimensions (H x W x L) 
5.1 cm x 9.5 cm x 18.1 cm (2 in x 3.74 in x7.12 in)
Weight
1.36 kg (3.00 lbs)
Input Voltage / Current / Hz
100 VAC to 240 VAC / 3 A - 1.5 A / 50-60 Hz
Output Voltage / Current
+56 VDC / 3.22 A 
Fans
0
Front-of-Supply Component Descriptions (Left to Right)
Power Cord Connector
Power Supply Front
Power Supply Rear

<<<PAGE 50>>>
Chassis and Power
Power Supplies
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-9
OS6865-BP-D - 180W/140W DC Power Supply
Thumb Screw
Grounding Block
Power Supply Ground
Status LED
Solid Green indicates normal operation
Rear-of-Supply Component Descriptions
DB-15 Connector (with Guide Pins)
OS6865-BP-D 180W/140W DC Power Supply
Description
Modular DC power supply. Up to two (2) power supplies may 
be installed.
Dimensions (H x W x L)
5.1 cm x 9.5 cm x 18.1 cm (2 in x 3.74 in x7.12 in)
Weight
1.44 kg (3.17 lbs)
Input Voltage / Current
-20 VDC to -28 VDC / 12A
-36 VDC to -72 VDC/ 6A
Output Voltage / Current  
-56V/2.5A (140W)
-56V/3.22A (180W)
Fans
0
Front-of-Supply Component Descriptions (Left to Right)
DC Power Connector
See “DC Power Supply Connection” on page 2-10
Thumb Screw
Front-of-Supply Component Descriptions (Left to Right)
Power Supply Front
Power Supply Rear

<<<PAGE 51>>>
DC Power Supply Connection
Chassis and Power
page 2-10
OmniSwitch 6865 Hardware Users Guide
December 2025
DC Power Supply Connection
Connecting a DC Cable Harness to the Chassis Power Supply
When plugging in the cable, insert the connector end of the cable harness into the power supply connector 
until it clicks firmly into place. This is an indication that the connector is secure and properly seated. 
Secure the screws.
Connecting a DC Cable Harness to the DC Power Source
The other end of the cable harness is bare. Users must assemble and connect this end to the DC power 
source or to a cable coming from the power source. In addition to following the important guidelines listed 
below, be sure to consult manufacturer specifications for the DC power source before starting.
• Connect the power supply to a reliably grounded -24V or -48V DC SELV source.
• Use common DC return connections for the DC power supplies. The DC return terminal conductor 
should be connected to the equipment frame.
• The branch circuit overcurrent protection must be rated 15A.
• Use two 12 AWG copper conductors.
• A readily accessible disconnect device that is suitably approved and rated shall be incorporated in the 
field wiring.
CAUTION: Installation of a DC cable that is more than 3 meters in length is subject to LOCAL 
CODES and AUTHORITIES. Please contact your electrician and the Local AHJ (Authority Hav-
ing Jurisdiction) to follow the Electrical Codes before use of proper installation methods.
Twisted pair wire (red and black) for a DC power supply
Grounding Block
Power Supply Ground
Status LED
Solid Green indicates normal operation
Rear-of-Supply Component Descriptions
DB-15 Connector (with Guide Pins)
Front-of-Supply Component Descriptions (Left to Right)
MIN 1 TURN PER 1.5
HALF TURN PER .75
Black
Red

<<<PAGE 52>>>
Chassis and Power
DC Power Supply Connection
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-11
Connecting a DC Power Source
The DC power supply contains a power connector with three (3) square slots for connecting the positive, 
negative, and ground wires from a DC power source.
OmniSwitch DC Power Supply Connector 
A clamp inside each slot keeps the power wire tightly in place during operation. The DC power supply 
connector has side screws that can be used to remove the connector if required.
Installing DC Power Source Wire Leads
These instructions describe how to connect your 3-wire DC power source to the power connector on your 
DC power supply. A small flat-tip screwdriver and a wire stripper are required for this procedure.
1.
Prepare the three (3) wires—12 gauge—that will plug into the power supply. First make sure they are not 
plugged into the DC power source. Next, use a wire stripper to carefully strip between .24 and .30 inches 
(6-7.5 mm) off the end of each wire, removing the outer insulation to expose the copper core.
2.
Open the clamp for the ground wire slot by inserting a small flat-tip screwdriver into the top of the appro-
priate circular hole. Loosen the screw so that the clamp for the ground wire opens.
Opening Connector for Ground Wire
3.
Insert the ground wire lead into the slot. The lead you insert must match the lead attached to the DC power 
source. Push the wire in far enough such that it reaches the back wall of the connector, about a half inch 
inside.
Warning. You must plug DC wire leads into the correct holes in the DC power connector. Use the labels 
above the DC power connector as a guide to positive, negative, and ground connections. If the wire leads 
are plugged into the wrong holes, the power supply will not work properly and damage to the unit may 
result.
Side Screws for Connector Removal
+      -
Clamp inside square hole will open
when screw is loosened in top cir-
cular  hole.
Loosen Screw.
+      -

<<<PAGE 53>>>
Dying Gasp
Chassis and Power
page 2-12
OmniSwitch 6865 Hardware Users Guide
December 2025
Attaching the Ground Wire
4.
Tighten the clamp by tightening the screw above the slot into which you inserted the wire lead. The wire 
lead should be securely attached inside the connector. You should be able to pull on the wire and not dis-
lodge it.
Warning. For both -24V and -48V input voltages, the positive (+) wire of the sourcing equipment, such as 
a battery or rectifier, must be connected to the positive (+) terminal of the DC power supply and the nega-
tive (-) wire of the sourcing equipment must be connected to the negative (-) terminal of the DC power 
supply. This rule always applies to both -24V, and -48V input voltages, regardless of the polarity signs 
shown on the power supply specification labels such as: -48V, +24V, or -24V."
5.
Repeat Steps 2 through 4 for the remaining positive and negative wire leads. 
Correct Polarity Connections
Dying Gasp
If the switch loses all power it will maintain power long enough to send a Dying Gasp message before 
completely shutting down. An SNMP trap, Syslog message and Link OAM PDUs will be generated.
Scenarios
A Dying Gasp event will be generated in the following scenarios:
Ground Wire
+ -
DC Power Source
Switch Power Supply

<<<PAGE 54>>>
Chassis and Power
Dying Gasp
OmniSwitch 6865 Hardware Users Guide
December 2025
page 2-13
• Primary power supply failure (if only power supply present)
• Primary power supply failure and then backup power supply failure
• Backup power supply failure and then primary power supply failure
Connect each power supply to a separate independent power source to avoid simultaneous 
power failures.
SNMP Trap
As soon as the power failure is detected, an SNMP trap is sent to the first three configured SNMP stations. 
The trap includes the following information:
• Slot number
• Power supply type (primary/backup)
• Time of the failure
Use the snmp station command and refer to the SNMP Configuration chapter for information on config-
uring an SNMP station.
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

<<<PAGE 55>>>
Dying Gasp
Chassis and Power
page 2-14
OmniSwitch 6865 Hardware Users Guide
December 2025
1. Uplink ports
2. All other ports
Note: The maximum number of ports which can send out a dying gasp PDU 
simultaneously is limited to ten ports minus the number of syslog/snmp servers 
configured. For example, if two snmp servers and one syslog server are 
configured, the maximum number of ports which can send out a dying gasp PDU 
is seven.

<<<PAGE 56>>>
OmniSwitch 6865 Hardware Users Guide
December 2025
page 3-1
3   Power Over Ethernet (PoE)
Managing Power over Ethernet (PoE)
Important: It’s recommended that PoE-enabled switches with attached IP telephones have opera-
tional power supply redundancy at all times for 911 emergency requirements. In addition, both the 
switch and the power supply should be plugged into an Uninterruptible Power Source (UPS).
Power over Ethernet Budget
The following tables list the Power over Ethernet wattages available based on the number and types of 
power supplies installed and the ambient temperature. 
Power over Ethernet Specifications
IEEE Standards supported
IEEE 802.3; 802.af; 802.3at
Power over Ethernet Settings
Default
Related Command
PoE operational status
Disabled
lanpower slot service
Total power available to a port
75000 milliwatts (HPoE Ports)
60000 milliwatts (802.3bt)
30000 milliwatts (PoE Ports)
lanpower power
Total power available to an entire 
slot
lanpower slot maxpower
Power priority level for a port
low
lanpower priority
Capacitor detection method
Disabled
lanpower capacitor-detection
Priority disconnect status
Enabled
lanpower slot priority-disconnect
Operating Temperature (TMRA)/
Power Supply
60°C
(without airflow)
65°C
(without airflow)
74°C
(with airflow)
(1) OS6865-BP-D @ 48V
140W
140W
120W
(2) OS6865-BP-D @ 48V
300W
150W
150W
(1) OS6865-BP-D @ 24V 
100W
100W
80W
(2) OS6865-BP-D @ 24V
240W
150W
150W
(1) OS6865-BP
140W
140W
140W

<<<PAGE 57>>>
Managing Power over Ethernet (PoE)
Power Over Ethernet (PoE)
page 3-2
OmniSwitch 6865 Hardware Users Guide
December 2025
OmniSwitch 6865-P16X / U12X PoE Budget and Temperature Table
 
OmniSwitch 6865-U28X PoE Budget / Temperature Table
 
Determining the Power Available for Powered Devices (PDs)
Viewing Power Supply Status
To view the type and status for installed power supplies, use the show powersupply command.
Viewing PoE Status
To view current PoE status and settings, uncluding the amount of PoE power available for incoming 
powered devices, use the show lanpower slot command.
PoE Class Detection
Powered devices can be classified into different classes as shown in the table below. Class detection 
allows for automatic maximum power adjustment based on the power class detected. This will prevent the 
switch from delivering more than the maximum power allowed based on a device’s class.
(2) OS6865-BP
300W
150W
150W
(1) OS6865-BP and (1) OS6865-BP-D @ 
48V
300W
150W
150W
(1) OS6865-BP and (1) OS6865-BP-D @ 
24V
240W
150W
150W
Operating Temperature (TMRA)/
Power Supply
60°C
(without airflow)
65°C
(without airflow)
74°C
(with airflow)
(1) OS6865-BP-D @ 48V
100W
100W
100W
(2) OS6865-BP-D @ 48V
280W
150W
150W
(1) OS6865-BP-D @ 24V 
80W
80W
80W
(2) OS6865-BP-D @ 24V
200W
150W
150W
(1) OS6865-BP
100W
100W
100W
(2) OS6865-BP
280W
150W
150W
(1) OS6865-BP and (1) OS6865-BP-D @ 
48V
280W
150W
150W
(1) OS6865-BP and (1) OS6865-BP-D @ 
24V
200W
150W
150W

<<<PAGE 58>>>
Power Over Ethernet (PoE)
Managing Power over Ethernet (PoE)
OmniSwitch 6865 Hardware Users Guide
December 2025
page 3-3
During class detection, the switch will allocate the maximum amount of power allowed based on the class 
detected. Once powered, if the device uses less than the maximum, the remaining power will be made 
available for other devices.
Although class-detection is disabled by default, power is still provided to incoming PDs (if available in the 
power budget). However, to strictly enforce class detection as specified in the 802.3at standard, class 
detection must be enabled using the lanpower slot class-detection command.
Enabling class detection will reset all PoE ports.
PoE Operational Status
Enabling PoE
By default, PoE is administratively enabled in the switch’s system software. However, in order to physi-
cally activate PoE, you must issue the lanpower slot service command on a slot-by-slot basis before any 
connected devices will receive inline power.
To activate power to PoE-capable in a switch, enter the corresponding slot number only. For example:
-> lanpower slot 2/1 service start
If power to a particular port has been administratively disconnected, you can reactivate power to the port 
using the lanpower port admin-state command. For example:
-> lanpower port 1/1/1-16 admin-state enable
Note. You cannot use the lanpower port admin-state command to initially activate PoE on a port. This 
syntax is intended only to reactivate power to those that have been disconnected via the lanpower slot 
service command. To initially activate PoE, you must use the lanpower slot service command as 
described above.
Disabling PoE
To disable PoE on a particular port, use the lanpower port admin-state command. For example:
Class
Usage 
Classification
Current (mA)
Power Range
(Watts)
Class Description
0
Default
0-4
0.44-30.00
Unimplemented
1
Optional
9-12
0.44-3.84
Very Low Power
2
Optional
17-20
3.84-6.49
Low Power
3
Optional
26-30
6.49-12.95
Mid Power
4
Optional
36-44
12.95-30.00
High Power

<<<PAGE 59>>>
Managing Power over Ethernet (PoE)
Power Over Ethernet (PoE)
page 3-4
OmniSwitch 6865 Hardware Users Guide
December 2025
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
To enable Fast PoE, use the lanpower slot fpoe command. For example:
-> lanpower slot 1/1 fpoe enable
Perpetual PoE
Perpetual PoE allows the switch to provide uninterrupted power to connected power devices (PD) even 
when the switch is rebooting or reloading, such as on a soft reset. 
• Perpetual PoE requires the proper FPGA/CPLD version, refer to the release notes for additional infor-
mation.
• The power to the PD devices will be interrupted if the PoE controller (MCU) firmware itself is being 
upgraded.
To enable Perpetual PoE, use the lanpower slot ppoe command. For example:
-> lanpower slot 1/1 ppoe enable
Configuring the Total Power Available to a Port
By default, each port is authorized by the system software to use up to a maximum amount of milliwatts to 
power any attached device.
This value can be increased or decreased based on the allowed ranges.
Increasing the total power available to an individual port may provide a more demanding powered device 
with additional power required for operation. Decreasing the total power available to a port helps to 
preserve inline power and assists in the overall management of the switch’s power budget.

<<<PAGE 60>>>
Power Over Ethernet (PoE)
Managing Power over Ethernet (PoE)
OmniSwitch 6865 Hardware Users Guide
December 2025
page 3-5
To increase or decrease the total power available to an individual port, use the lanpower power 
command.
Note. Since the power allowance is being set for an individual port, chassis/
slot/port values must be specified.
Configuring the Total Power Available to a Slot
Like the maximum port power allowance, the system software also provides a maximum slot-wide power 
allowance. By default, each slot is authorized by the system software to use a number of watts to power all 
devices connected to its ports depending on which power supply is used.
As with the maximum port power allowance, the user can either increase or decrease this value based on 
the allowed ranges.
Note. Decreasing the slot-wide power could cause lower priority ports to lose 
power if the new value is less than the total PoE power currently being 
consumed.
To increase or decrease the total power available to a slot, use the lanpower slot maxpower command. 
Since you are setting the power allowance for an individual slot, you must specify a chassis/slot value in 
the command line. For example, the syntax
-> lanpower slot 1/1 maxpower 150
reduces the power allowance of chassis 1, slot 1 to 150 watts. This value is now the maximum amount of 
power the slot can use to power all attached devices (until the value is modified by the user).
Note. Changing the maximum power available to a slot or port does not reserve or immediately 
allocate that power. These settings are only used for configuring a maximum amount of power 
that may be used, any unused power is still available and remains a part of the overall PoE budget.
Setting Timers and Other User-Defined PoE Power Rules
The lanpower power-rule command allows user to set additional rules for PoE power (e.g., setting PoE 
to turn on or off on specific dates or at specific times). Refer to the OmniSwitch AOS CLI Command 
Reference Guide for more information. 
Setting Port Priority Levels
As not all Powered Devices (PDs) connected to the switch have the same priority within a network setting, 
the OmniSwitch allows the administrator to specify priority levels on a port-by-port basis. Priority levels 
include low, high, and critical. 
The default priority level for a port is low.
• Low. This default value is used for port(s) that have low-priority devices attached. In the event of a 
power management issue, inline power to low-priority is interrupted first (i.e., before critical and high 
priority).

<<<PAGE 61>>>
Managing Power over Ethernet (PoE)
Power Over Ethernet (PoE)
page 3-6
OmniSwitch 6865 Hardware Users Guide
December 2025
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
Setting the Capacitor Detection Method
By default, the capacitor detection method is disabled. To enable it, use the lanpower capacitor-detection 
command. For example:
-> lanpower slot 1/1 capacitor-detection enable
Note. The capacitive detection method should only be enabled to support legacy IP phones. This 
feature is not compatible with IEEE specifications. Please contact your Alcatel-Lucent sales engi-
neer or Customer Support representative to find out which Alcatel-Lucent IP phones models need 
capacitive detection enabled.
Understanding Priority Disconnect
Priority disconnect is used by the system software in determining whether an incoming PD will be granted 
or denied power when there are too few watts remaining in the PoE power budget for an additional device. 
For example, if there are only 2 watts available in the current PoE power budget and a user plugs a 3.5W 
powered device into a PoE port, the system software must determine whether the device will be powered 
on. 
Based on priority disconnect rules, in some cases one or more existing devices may be powered down in 
order to accommodate the incoming device. In other cases, the incoming device will be denied power.
Priority disconnect rules involve the port priority status of an incoming device (i.e., low, high, and criti-
cal), as well as the port’s physical port number. Understanding priority disconnect rules is especially help-
ful in avoiding power budget deficits and the unintentional shutdown of mission-critical devices when PDs 
are being added in tight power budget conditions. 
Reminder. Priority disconnect applies only when there is inadequate power 
remaining in the power budget for an incoming device.

<<<PAGE 62>>>
Power Over Ethernet (PoE)
Managing Power over Ethernet (PoE)
OmniSwitch 6865 Hardware Users Guide
December 2025
page 3-7
For information on setting the priority disconnect status, refer to the section below. For information on 
setting the port priority status (a separate function from priority disconnect), refer to “Setting Port Priority 
Levels” on page 3-5.
Setting Priority Disconnect Status
By default, priority disconnect is enabled in the switch’s system software. For information on changing 
the priority disconnect status, refer to the information below.
Disabling Priority Disconnect
When priority disconnect is disabled and there is inadequate power in the budget for an additional device, 
power will be denied to any incoming PD, regardless of its port priority status (i.e., low, high, and criti-
cal) or physical port number. To disable priority disconnect, use the lanpower slot priority-disconnect 
command. For example:
-> lanpower slot 1/1 priority-disconnect disable
Enabling Priority Disconnect
To enable priority disconnect, use the lanpower slot priority-disconnect command. For example:
-> lanpower slot 1/1 priority-disconnect enable
Priority Disconnect is Enabled; Same Priority Level on All Devices
Reminder. Priority disconnect examples are applicable only when there is 
inadequate power remaining to power an incoming device.
When a PD is being connected to a port with the same priority level as all other in the slot, the physical 
port number is used to determine whether the incoming PD will be granted or denied power. Due to the 
support of different PoE standards and PoE hardware on each platform the internal port priority is differ-
ent for each platform. The following tables should be used to determine PoE priority:
Priority Disconnect is Enabled; Incoming PD Port has Highest Priority Level
Reminder. Priority disconnect examples are applicable only when there is 
inadequate power remaining to power an incoming device.
When a PD is being connected to a port with a higher priority level than all other in the slot, the incoming 
PD will automatically be granted power over the other devices, regardless of its physical port number. 
In order to avoid a power budget deficit, another port in the slot is disconnected. In determining which
port to power off, the system software first selects the port with the lowest configured priority level. For 
example, if a critical priority device is being added to a slot in which five existing devices are attached to 
PoE Physical Port Priority
1 (Highest) -> 28 (Lowest)

<<<PAGE 63>>>
Managing Power over Ethernet (PoE)
Power Over Ethernet (PoE)
page 3-8
OmniSwitch 6865 Hardware Users Guide
December 2025
high priority and one device is attached to a low priority port, the low priority port is automatically discon-
nected, regardless of its physical port number.
If all existing devices are attached to with the same lower priority level, the system software disconnects 
the port with both the lowest priority level. For example, if a critical priority device is being added to a slot 
in which six existing devices are attached at high priority, the high priority port with the highest physical 
port number is automatically disconnected.
Priority Disconnect is Enabled; Incoming PD Port has Lowest Priority Level
Reminder. Priority disconnect examples are applicable only when there is 
inadequate power remaining to power an incoming device.
When a PD is being connected to a port with a lower priority level than all other in the slot, the incoming 
PD will be denied power, regardless of its physical port number. Devices connected to other higher-prior-
ity will continue operating without interruption.
Priority Disconnect is Disabled
Reminder. Priority disconnect examples are applicable only when there is 
inadequate power remaining to power an incoming device.
When priority disconnect is disabled, power will be denied to any incoming PD, regardless of its port 
priority status (i.e., low, high, and critical) or physical port number.
Understanding Guard Band 
Guard Band functionality is implemented when the switch has to provide power to a newly connected PD. 
This functionality is more relevant on switches that have a lower amount of total PoE power available for 
the switch but a higher default maximum PoE power available to some ports. 
• If the amount of power remaining is less than the port's configured maximum PoE power value or the 
PD's class maximum power then the switch will not power up the PD. 
• This applies even if the newly connected PD actually requires less than the maximum power available 
for the port. 
For example, assume the following: 
• There is 50W of PoE power remaining on the switch. 
• A newly connected PD only requires 4W of power. 
• The port's maximum PoE power value is 75W. 
In this example the newly connected PD will not be powered on since the port's maximum PoE power 
value is greater than the PoE power remaining on the switch. 
To allow the PD to be powered, the port's maximum PoE value can be configured to be less than the 
power remaining by issuing the following command to set the port's maximum PoE power to 10W:
-> lanpower power 1/1/1 power 10000
Using the previous example:

<<<PAGE 64>>>
Power Over Ethernet (PoE)
Managing Power over Ethernet (PoE)
OmniSwitch 6865 Hardware Users Guide
December 2025
page 3-9
• There is 50W of PoE power remaining on the switch. 
• A newly connected PD only requires 4W of power. 
• The port's maximum PoE power value is now 10W.
The newly connected PD will be powered on since the port's maximum PoE power value is now less than 
the PoE power remaining on the switch. 
The examples assume the new PD has the same or lower priority as the existing PDs, otherwise priority 
disconnect will override. 
The Guard Band functionality does not apply to PDs that are already powered up. However, priority 
disconnect will apply if there's not enough power to power all PDs in the case of the power budget being 
reduced, such as the removal of a power supply.
Please refer to the “Understanding Priority Disconnect” on page 3-6 for additional details.

<<<PAGE 65>>>
OmniSwitch 6865 Hardware Users Guide
December 2025
page -1
A Regulatory Compliance and
Safety Information
This appendix provides information on regulatory agency compliance and safety for the OmniSwitch.
Declaration of Conformity: CE Mark
This equipment is in compliance with the essential requirements and other provisions of 
Directive 2014/30/EU (EMC), 2014/35/EU (LVD), 2011/65/EU (RoHS-Directive), 91/263/EEC (Tele-
com Terminal Equipment, if applicable), 2014/53/EU (R&TTE, if applicable). 
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
Compliance and Certifications
Safety Standards
• US UL 60950-1
• US UL 62368-1
• IEC 60950-1 Health and Safety
• IEC 62368-1 Audio/Video, Information Technology: Safety requirement
• CAN/CSA-C22.2 No. 60950-1
• CAN/CSA-C22.2 No. 62638-1
• EN 62368-1
• NOM-019 SCFI, Mexico

<<<PAGE 66>>>
Compliance and Certifications
page -2
OmniSwitch 6865 Hardware Users Guide
December 2025
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

<<<PAGE 67>>>
Compliance and Certifications
OmniSwitch 6865 Hardware Users Guide
December 2025
page -3
• EN 61000-4-6
• EN 61000-4-8
• EN 61000-4-11
• IEEE 802.3: Hi-Pot Test
(2250 V DC on all Ethernet ports)
Environmental Standards
• ETS 300 019 Storage Class 1.1
• ETS 300 019 Transportation Class 2.3
ETS 300 019 Stationary Use Class 3.1
Industrial Compliance Requirements
Industrial Compliance Requirements
Safety
ISA 12.12.01 (UL 1604), CSA22.2/213, UL 508, EN50021
Operational 
Temperature
IEC 60870-2-2 (operational temperature)
IEC 60068-2-1 (temperature type test - cold)
IEC 60068-2-2 (temperature type test - hot)
Storage 
Temperature
IEC 60721-3-1: Class 1K5 (storage temperature)
Humidity
IEC 60068-2-30: 5% to 95% non-condensing humidity
Mechanical 
Shock
 IEC 60255-21-2 (mechanical shock)
Vibration
IEC 60255-21-1 (vibration)
Drop Test
IEC 60870-2-2 Free Fall 
Altitude Test
IEC 60870-2-2, GR-63-CORE, 4.1.3, 4.5
IPX
IPXX, IEC60529
EMI/EMC
IEC 61000-6-2 (Immunity) 
EN 61000-6-4 (Emmission) 
EN 55032,
EN 61000-3-3
EN 61000-3-2
EN 55024
IEC 61850-3
EN 61000-4-2 to EN 61000-4-6, 
EN 61000-4-8
EN 61131-2
IEEE 1613, Section 5.2, 5.3, 6.3.1, 6.3.2, 7, 8

<<<PAGE 68>>>
Compliance and Certifications
page -4
OmniSwitch 6865 Hardware Users Guide
December 2025
China RoHS: Hazardous Substance Table
DNV
DNV 2.4
Railway
EN 50121-4
IEC 62236-4
EN 61000-6-4
NEMA
NEMA TS-2

<<<PAGE 69>>>
Compliance and Certifications
OmniSwitch 6865 Hardware Users Guide
December 2025
page -5
Taiwan RoHS: Hazardous Substance Table
California Proposition 65 Warning
WARNING: This product can expose you to chemicals including Pb and Pb compounds, which is known 
to the State of California to cause cancer and birth defects or other reproductive harm. For more informa-
tion go to www.P65Warnings.ca.gov.
Products are packaged using one or more of the following packaging materials:
Corrugated Cardboard                Corrugated Fiberboard              Low-Density Polyethylene
CB
FB

<<<PAGE 70>>>
Compliance and Certifications
page -6
OmniSwitch 6865 Hardware Users Guide
December 2025
Waste Electrical and Electronic Equipment (WEEE) Statement
The product at end of life is subject to separate collection and treatment in the EU Member States, Norway 
and Switzerland, and is therefore marked with the symbol:
Treatment applied at end of life of the product in these countries shall comply with the applicable national 
laws implementing directive 2002/96EC on Waste Electrical and Electronic Equipment (WEEE).
FCC Class A, Part 15
This equipment has been tested and found to comply with the limits for Class A digital device pursuant to 
Part 15 of the FCC Rules.These limits are designed to provide reasonable protection against harmful inter-
ference when the equipment is operated in a commercial environment.This equipment generates, uses, and 
can radiate radio frequency energy and, if not installed and used in accordance with the instructions in this 
guide, may cause interference to radio communications. Operation of this equipment in a residential area is 
likely to cause interference, in which case the user will be required to correct the interference at his own 
expense.
The user is cautioned that changes and modifications made to the equipment without approval of the 
manufacturer could void the user’s authority to operate this equipment.It is suggested that the user use 
only shielded and grounded cables to ensure compliance with FCC Rules.
If this equipment does cause interference to radio or television reception, the user is encouraged to try to 
correct the interference by one or more of the following measures:
• Reorient the receiving antenna.
• Relocate the equipment with respect to the receiver.
• Move the equipment away from the receiver.
• Plug the equipment into a different outlet so that equipment and receiver are on different 
branch circuits.
If necessary, the user should consult the dealer or an experienced radio/television technician for additional 
suggestions.
Canada Class A Statement
This equipment does not exceed Class A limits per radio noise emissions for digital apparatus, set out in 
the Radio Interference Regulation of the Canadian Department of Communications.
Avis de conformitè aux normes du ministère des Communications du

<<<PAGE 71>>>
Compliance and Certifications
OmniSwitch 6865 Hardware Users Guide
December 2025
page -7
Canada
Cet èquipement ne dèpasse pas les limites de Classe A d íèmission de bruits radioèlectriques pour les 
appareils numèriques,telles que prescrites par le RÈglement sur le brouillage radioèlectrique ètabli par le 
ministère des Communications du Canada.
JATE
This equipment meets the requirements of the Japan Approvals Institute of Telecommunications Equip-
ment (JATE).
CISPR22 Class A Warning
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
Conformity Registration as business equipment (A), 
not home equipment. Sellers or users are required to 
take caution in this regard.

<<<PAGE 72>>>
Compliance and Certifications
page -8
OmniSwitch 6865 Hardware Users Guide
December 2025
Translated Safety Warnings
Chassis Lifting Warning
Two people are required when lifting the chassis. Due to its weight, lifting the chassis unassisted can cause 
personal injury. Also be sure to bend your knees and keep your back straight when assisting with the lift-
ing of the chassis.
Français: Le châssis doit être soulevé par deux personnes au minimum. Pour éviter tout risque d'accident, 
maintenez le dos droit et poussez sur vos jambes. Ne soulevez pas l'unité avec votre dos.
Deutsch: Sicherheitshinweise Hinweise zur Anhebung des Chassis Zum Anheben des Chassis werden 
zwei Personen benötigt. Aufgrund des Gewichts kann das Anheben ohne Unterstützung zu Personen-
schäden führen. Heben Sie das Chassis aus den Knien und halten Sie den Rücken gerade wenn Sie beim 
Anheben des Chassis assistieren.
Español: Se requieren dos personas para elevar el chasis. Para evitar lesiones, mantenga su espalda en 
posición recta y levante con sus piernas, no con su espalda.
Electrical Storm Warning
To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or 
reconfiguration of this product during an electrical storm.
Français: Ne pas travailler sur le système ni brancher ou débrancher les câbles pendant un orage.
Deutsch: Hinweise bei Unwetter Um elektrische Schläge zu vermeiden dürfen während eines Gewitters 
and diesem Gerät keine Kabel angeschlossen oder gelöst werden, sowie keinerlei Installationen, Wartun-
gen oder Konfigurationen vorgenommen werden.
Español: Para evitar peligro de descargas, no conecte o desconecte ningun cable, ni realice ninguna insta-
lación, maintenimiento o reconfiguración de este producto durante una tormenta eléctrica.
Installation Warning
Only personnel knowledgeable in basic electrical and mechanical procedures should install or maintain 
this equipment.
Français: Toute installation ou remplacement de l'appareil doit être réalisée par du personnel qualifié et 
compétent.
Deutsch: Installationshinweise Dieses Gerät soll nur von Personal installiert oder gewartet werden, 
welches in elektrischen und mechanischen Grundlagen ausgebildet ist.
Español: Estos equipos deben ser instalados y atendidos exclusivamente por personal adecuadamente 
formado y capacitado en técnicas eléctricas y mecánicas.
Invisible Laser Radiation Warning
Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When 
removing cables do not stare into the open apertures. In addition, install protective aperture covers to fiber 
with no cable connected.
Français: Des radiations invisibles à l'oeil nu pouvant traverser l'ouverture du port lorsque aucun câble en 
fibre optique n'y est connecté, il est recommandé de ne pas regarder fixement l'intérieur de ces ouvertures. 
Installez les caches connecteurs prévus à cet effet.

<<<PAGE 73>>>
Compliance and Certifications
OmniSwitch 6865 Hardware Users Guide
December 2025
page -9
Deutsch: Hinweise zur unsichtbaren Laserstrahlung Die Laser strahlen an der Blendenöffnung unsichtba-
res Licht ab, wenn keine Glasfaserkabel angeschlossen sind. Blicken Sie nicht in die Öffnungen und 
installieren Sie unverzüglich die Abdeckungen über den Glasfaseranschlüssen.
Español: Debido a que la apertura del puerto puede emitir radiación invisible cuando no hay un cable de 
fibra conectado, procurar no mirar directamente a las aperturas para no exponerse a la radiación.
Power Disconnection Warning
Your switch may be equipped with multiple power supplies (redundant power supply configurations). To 
reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving 
the unit.
Français: Il se peut que cette unité soit équipée de plusieurs raccordements d'alimentation. Pour supprimer 
tout courant électrique de l'unité, tous les cordons d'alimentation doivent être débranchés.
Deutsch: Hinweise zur Spannungsfreischaltung Ihr Gerät ist mit mehreren Netzteilen ausgerüstet. Um die 
Gefahr des elektrischen Schlages zu verringern, stellen sie sicher, daß alle Netzverbindungen getrennt sind 
bevor das Gerät gewartet oder bewegt wird.
Español: Antes de empezar a trabajar con un sistema, asegurese que el interruptor está cerrado y el cable 
eléctrico desconectado.
Proper Earthing Requirement Warning
To avoid shock hazard:
• The power cord must be connected to a properly wired and earth receptacle.
• Any equipment to which this product will attached must also be connected to properly 
wired receptacles.
• Use 22AWG solid copper conductor for ground leads connecting the frame to ground and DC return.
• Cleaning and dressing of grounding points during installation is strongly recommended. Also, do not 
forget the antioxidant.
• To ground the equipment properly, connect a Panduit Corporation UL listed Lug, P/N: LCD8-10AL to 
the two threaded holes located on the rear using 8AWG copper conductors. Use Panduit Corporation, 
P/N: CT-940CH for crimping. Torque to between 30-60 inch pounds.
Français: Pour éviter tout risque de choc électrique:
• Ne jamais rendre inopérant le conducteur de masse ni utiliser l'équipement sans un conducteur de 
masse adéquatement installé.
• En cas de doute sur la mise à la masse appropriée disponible, s'adresser à l'organisme responsable de la 
sécurité électrique ou à un électricien.
Deutsch: Hinweise zur geforderten Erdung des Gerätes Aus Sicherheitsgründen:
• Darf das Netzkabel nur an eine Schutzkontaktsteckdose angeschlossen werden.
• Dürfen für den Anschluß anderer Geräte, welche mit diesem Gerät verbunden sind, auch nur Schutz-
kontaktsteckdosen verwendet werden.

<<<PAGE 74>>>
Compliance and Certifications
page -10
OmniSwitch 6865 Hardware Users Guide
December 2025
Español: Para evitar peligro de descargas:
• Para evitar peligro de descargas asegurese de que el cable de alimentación está conectado a una toma 
de alimentación adecuadamente cableada y con toma de tierra.
• Cualquier otro equipo a cual se conecte este producto también debe estar conectado a tomas de 
alimentación adecuadamente cableadas.
DC Power Supply Connection Warning
• For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/
DC power supply to Earth Ground.
• Français: Pour EMC/EMI, pour chaque alimentation DC/DC, il est impératif que le fil de terre soit 
branché à la prise de terre.
• Deutsch: Zur Erfüllung der EMV-/EMI-Anforderungen muss das Erdungskabel jedes DC/DC-Netz-
teils an eine Erde angeschlossen werden.
• Español: Para EMC/EMI, cada fuente de alimentación de CC/CC requiere que el cable de tierra esté 
conectado desde cada fuente de alimentación de CC/CC a la conexión a tierra.
Read Important Safety Information Warning
This guide contains important safety information users must be aware of when working with hardware 
components in this system. Read this guide in its entirety before installing, using, or servicing this equip-
ment.
Français: Avant de brancher le système sur la source d'alimentation, consultez les directives d'installation 
disponibles dans ceci guide.
Deutsch: Bitte lesen - Sicherheitshinweise Dieses guide enthält wichtige Sicherheitsinformationen, über 
die sie sich beim Arbeiten mit den Hardwareeinheiten bewußt sein sollten. Sie sollten diese Hinweise 
lesen, bevor sie installieren, reparieren oder die Anlage verwenden.
Español: Esto guide contiene información importante de seguridad sobre la cual usted debe estar enterado 
al trabajar con los componentes de dotación física en este sistema. Usted debe leer esta guía antes de insta-
lar, usar o mantener este equipo.
Restricted Access Location Warning
This equipment should be installed in a location that restricts access. A restricted access location is one 
where access is secure and limited to service personnel who have a special key, or other means of security.
Français: Le matériel doit être installé dans un local avec accès limité ou seules les personnes habilitées 
peuvent entrer.
Deutsch: Hinweis zu Umgebungen mit beschränktem Zutritt Die Anlage sollte an einem Standort mit 
beschränktem Zutritt installiert sein. Ein Standort mit beschränktem Zutritt stellt sicher, daß dort nur 
Servicepersonal mit Hilfe eines Schlüssels oder eines anderen Sicherheitssystems Zugang hat.
Español: Este equipo se debe instalar en un sitio con acceso restrinjido. Un sitio con el acceso restrinjido 
es uno seguro y con acceso limitado al personal de servicio que tiene una clave especial u otros medios de 
seguridad.

<<<PAGE 75>>>
Compliance and Certifications
OmniSwitch 6865 Hardware Users Guide
December 2025
page -11
Wrist Strap Warning
Because electrostatic discharge (ESD) can damage switch components, you must ground yourself prop-
erly before continuing with the hardware installation. For this purpose, Alcatel-Lucent Enterprise provides 
a grounding wrist strap and a grounding lug located near the top-right of the chassis. For the grounding 
wrist strap to be effective in eliminating ESD, the power supplies must be installed in the chassis and 
plugged into grounded AC outlets.
Français: L'électricité statique (ESD) peut endommager les composants du commutateur. Pour cette raison 
Alcatel-Lucent Enterprise joint à l'envoi du châssis un bracelet antistatique à brancher sur la prise mise à 
la terre située en bas à droite du commutateur. Vous devrez mettre ce bracelet avant toute intervention 
hardware.
Deutsch: Hinweise zur ESD (Elektrostatischen Aufladung) Weil elektrostatische Aufladung (ESD) Teile 
der Anlage beschädigen könnten, müssen sie sich selbst erden, bevor sie mit der Hardware Installation 
beginnen. Zu diesem Zweck stellt Alcatel-Lucent Enterprise ein Erdungsarmband und eine Erdungsöse an 
der oberen rechten Seite des Chassis zur Verfügung. Um eine sichere Erdungsfunktion des Erdungsarm-
bandes sicherzustellen, müssen die Netzteile installiert und mit dem Schutzleiter des Versorgungsstrom-
kreises verbunden sein.
Español: La descarga electrostática (ESD) puede dañar componentes eletrónicos. Usted debe asegurarse 
que está en contacto con tierra antes de hacer la instalación del equipo. Con este fin, Alcatel-Lucent Enter-
prise proporciona una pulsera de muñeca para conectar al chasis en la toma de tierra situada en la parte 
superior derecha del chasis. Para que la correa de muñeca sea eficaz en la eliminación de ESD, las fuentes 
de alimentación deben estar instaladas en el chasis y conectadas a enchufes CA con tierra adecuada.
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

<<<PAGE 76>>>
Compliance and Certifications
page -12
OmniSwitch 6865 Hardware Users Guide
December 2025
Advertencia de la batería de litio
Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente. Substituya 
la batería solamente por el mismo o el equivalente de tipo de batería recomendado por el fabricante. 
Deseche las baterías usadas según las instrucciones del fabricante. Las instrucciones del fabricante son 
como sigue: Devuelva el módulo con la batería del litio a Alcatel-Lucent. La batería del litio será substitu-
ida en la fábrica de Alcatel-Lucent.
Advertencia sobre la tensión de operación
Para reducir el riesgo del choque eléctrico, matenga sus manos y dedos fuera de la fuente de alimentación 
y no toque la placa madre mientras que el interruptor está funcionando.
Advertencia sobre la desconexión de la fuente
Su interruptor esta equipado por fuentes de alimentación múltiples. Para reducir el riesgo de 
choque eléctrico, asegúrese desconectar todas las conexiones de alimentación antes de mantener o 
de mover la unidad.
Advertencia sobre una apropiada conexión a tierra
Para evitar peligro de descargas:
El cable de alimentación debe estar conectado a una toma de alimentación 
adecuadamente cableada y con toma de tierra.
Cualquier equipo al cual se conecte este producto debe estar también conectado a tomas de alimentación 
adecuadamente cableadas.
Leer “información importante de seguridad”
La Guía de “Comenzando a Usar” que acompaña este equipo contiene información importante de seguri-
dad sobre la cual usted debe saber al trabajar con los componentes de dotación física en este sistema. 
Usted debe leer esta guía antes de instalar, de usar, o de mantener este equipo.
Advertencia de acceso restringido
Este equipo se debe instalar en una ubicación que restrinja el acceso. Una ubicación con acceso restrin-
gido es una donde está seguro y limitado el acceso al personal de servicio que tiene un clave especial, u 
otros medios de la seguridad.
Advertencia de pulsera antiestática
Debido a que la descarga electrostática (ESD) puede dañar componentes del interruptor, usted debe conec-
tarse a tierra correctamente antes de continuar con la instalación del equipo. Para este propósito, Alcatel- 
Lucent proporciona una pulsera antiestática y un terminal que pone a tierra situados cerca de la parte supe-
rior derecha del chasis. Para que la pulsera antiestática sea eficaz en la eliminación de ESD, las fuentes de 
alimentación se deben instalar en el chasis y enchufar en las salidas de CA con descarga a tierra.
Clase de seguridad
Cumple con 21CFR 1040.10 y 1040.11 ó sus equivalentes.