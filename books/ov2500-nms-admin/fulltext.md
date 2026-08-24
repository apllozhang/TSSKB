<<<PAGE 1>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
OMNIVISTA 2500 NMS 
ADMINISTRATION R4 - EDITION 09 
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
DT00XTE311EN
OmniVista 2500 NMS Administration R4
OmniSwitch

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
• Welcome to the Alcatel-Lucent OmniVista
2500 training – Course DT00CTE/VTE311EN
• Through successful completion of this course, students will gain the required knowledge and 
experience to successfully implement and support a network comprised of OmniSwitch 6870, 6900, 
6560 and 6360 Series of switches managed with the Alcatel-Lucent’s OmniVista NMS platform
• The course is a combination of lecture and hands-on labs
• The hands-on labs will be used to reinforce the subjects covered during lecture
Course Description

<<<PAGE 7>>>
Day 1
• Lecture
- Agenda
- OmniVista Presentation
- OmniVista Installation and System Setup
- Using Network, Configuration & Administration Groups
- Unified Access
• Labs
- Basic Network Configuration
- AOS SNMP Setup
- OmniVista Install
- Discovery
- Topology
- VLANs
- Basic Routing
- Locator
- Notifications
- Resource Manager
- CLI Scripting
- Users and Groups
- Control Panel
- Preferences
- Audit
- Unified Access

<<<PAGE 8>>>
Day 2
• Lecture
- OmniVista PolicyView 
- Quarantine Manager
- Internet of Things
- Template Based Provisioning
- Analytics
- ProActive Lifecycle Management
- OmniVista Network Analyzer
- Spacewalkers
• Optional
- SIP Snooping
- Template Based Provisioning – Architecture and Configuration
• Labs
- PolicyView 
- Analytics

<<<PAGE 9>>>
Internet Resources
• Alcatel-Lucent Enterprise Web Site
https://www.al-enterprise.com/en
• Alcatel-Lucent Enterprise Web Site
for Business Partners
https://myportal.al-enterprise.com
• Training & Certification
https://www.al-enterprise.com/en/services/education-services
• RFC Technical documents
http://www.ietf.org

<<<PAGE 10>>>
Internet Resources
• Spacewalkers Community
• www.spacewalkers.com
• https://www.al-enterprise.com/en
• Partner Portal
• My Portal

<<<PAGE 11>>>
PRESENTATION
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 12>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the OmniVista 2500 NMS main 
features
• Define management interfaces
• Introduce New features

<<<PAGE 13>>>
OMNIVISTA 2500 NMS OVERVIEW
• Full Web-based Applications
• All are accessed directly through 
a single web GUI
• Provides applications for extended
NMS capabilities (QoS & Security)
• Provides access to network wide activities
• Provides access to individual or group of
network devices for setup
Provisioning
Management
Monitoring

<<<PAGE 14>>>
OMNIVISTA 2500 NMS R4
RESPONSIVE DESIGN & FLEXIBLE INTERFACES
• OmniVista 2500 R4 is web-based enabling the user to monitor and manage the network 
from a variety of platforms
Tablet Rendering
Traditional PC Rendering
SmartPhone

<<<PAGE 15>>>
OMNIVISTA 2500 NMS - 4.9R2 KEY FEATURES 
NODAL & RELEASE
SUPPORT
ESSENTIALS & 
FRAMEWORK
NODAL 
MANAGEMENT
•
Oracle 8.x upgrade for OV2500 (OS/Kernel for security fixes -> LTS)
•
Security fixes, specific #BlastRadius alert
•
Security Improvements (Higher Encryption , Password Reset options)
• AWOS 5.0.2 support
• AOS 8.10.R2 support
• PALM to Fleet Supervision – OV2500 Required changes to support PALM EOS & 
Fleet Solution
•
New OS6870 series ( NMS Monitoring, Provisioning & Premium Features like DPI)
SECURITY & 
RELIABILITY

<<<PAGE 16>>>
OMNIVISTA 2500 NMS SUPPORTED LAN DEVICES 
OmniSwitch 9900
OmniSwitch 6900
OmniSwitch 
2260/2360
OmniSwitch 6560/E
OmniSwitch 6465
OmniSwitch 6865
OmniSwitch 6860E/N
OmniSwitch 6360
OmniSwitch 6570M
OmniSwitch 6870

<<<PAGE 17>>>
OMNIVISTA 2500 NMS - HIGH AVAILABILITY
• Main/standby instances through
VM/VA instances
• Packaged as VA/VM 
• Main and standby supporting the 
complete set of features for L2
• All OV services -> topology, trap
• Extending for UPAM resiliency
• UPAM Authentication Service operating 
during OV HA upgrade
• Operates over L2 and L3 
• Single server deployment to
Primary/secondary operation controlled by optional software license

<<<PAGE 18>>>
OMNIVISTA 2500 NMS - HIGH AVAILABILITY
• Before introducing HA, if OmniVista became unavailable due to either loss of connectivity 
or a server failure then:
• The network administrator would no longer be able to monitor or make configuration changes
• If using UPAM, no new additional clients would be able to authenticate
• HA creates a redundant OmniVista that takes over if the primary (Main) OV becomes 
unavailable. Two instances of OV are constantly running:
• All functions are handled by the Main OV
• The Main OV keeps the standby OV in sync
• If the Main OV becomes unavailable, then the Standby OV takes over 
• When control is moved from Main to Standby, all services and operations are transferred
• UPAM with BYOD and Guest Access is taken over by Standby
• All network monitoring services are taken over by Standby

<<<PAGE 19>>>
OMNIVISTA 2500 NMS 
HIGH AVAILABILITY 
FEATURES
Use cases
Improvements
HA installation
• Simpler & reduced installation settings
• Settings entered only once for both instances
• Allows conversion from Standalone to HA 
• Disk synchronization is done in background
Performance
• Increased Performance for HA with higher number of devices
• Expanding OV2500 Scalability certification up to 4K AP w/1.5K 
Switches
Operation
Simplification
• Traps automatically configured for both instances, so always 
received on the active instance
• Traps recovery/Trap Replay automatic on failover.
• Alert banner displayed on failover.
• Link provided within the banner to switch to new active node.

<<<PAGE 20>>>
APPLICATION UPDATES / ENHANCEMENTS
• LAN/WLAN Menu 
• Displays application drop-down menus specific to WLAN devices (e.g., SSIDs, APs)
• Available by clicking on the LAN/WLAN Menu drop-down at the top of the screen
• By default, all application drop-down menus (for both LAN and WLAN Devices) are displayed ("LAN+WLAN")
• Select "WLAN Menu" to display application drop-down menus specific to WLAN devices
(e.g., SSIDs, APs). 
• Alarm Status Bar 
• A real-time display of unacknowledged alarms is displayed at the bottom of all screens in OmniVista. 
• The number of alarms in each category (e.g., Critical, Major, Minor, Warning) is displayed. 
• Click on a category to go to the Notifications application and view all alarms in the selected category

<<<PAGE 21>>>
NMS COMPONENTS
• Simple Network Management Protocol (SNMP)
• sFlow (Analytics)
• Management Information Base (MIB)
• Traps
• RMON
Agents
Managed Devices
Network Management
Systems
Agents

<<<PAGE 22>>>
ALCATEL-LUCENT - MANAGEMENT INTERFACE OPTIONS
• Preferences
• CLI vs. GUI
• CLI Pros
• Proficiency
• Scripting
• Familiarity
• GUI Pros
• Color-coding 
• Easier to spot problems
• Fewer “fat-fingered” mistakes
• Bulk operations
• Same features in CLI and in WebView
CLI
CLI-MIP
SNMP-MIP
EMWEB-MIP
SNMP
WebView

<<<PAGE 23>>>
ALCATEL-LUCENT CLI
PREFERRED TOOL FOR INITIAL CONFIGURATION
• Alcatel-Lucent CLI reduces initial configuration time:
• Designed for usability: new, clean, simple
• Able to gather a wide range of configuration
information into one set of commands
• ASCII based configuration files can be copied
and pasted from one switch to another
• Standardized, cross-platform commands 
for all AOS devices from chassis to stacks
• 100% Equivalent functionality to WebView

<<<PAGE 24>>>
ALCATEL-LUCENT WEBVIEW
• Native element manager for AOS devices
• Device centric view
• 100% CLI equivalent features
• Integrated with OmniVista
• Manages a single device at the time
• Common look and feel with OmniVista 2500 NMS

<<<PAGE 25>>>
OMNIVISTA 2500 NMS
• Administration
•
Web Interface
• Installation
• OmniVista 2500 = Virtual Appliance
• No standalone installers
Hypervisors
•
VMware ESXi
•
MS Hyper-V
•
KVM
OmniVista 2500 NMS

<<<PAGE 26>>>
OMNIVISTA 2500 NMS - HOME PAGE
• Applications
• Accessible via a 
drop down menu
• Dashboard
• OV 2500 Home Page
• Applications widgets 
• Quick overview
• Customizable
(add/remove…)

<<<PAGE 27>>>
OMNIVISTA 2500 NMS - APPLICATIONS
NETWORK
- DISCOVERY
- TOPOLOGY
- AP REGISTRATION
- SAA
- LOCATOR
- NOTIFICATIONS
- VM MANAGER
- ANALYTICS
- APPLICATION VISIBILITY
- PROVISIONING
- IOT
CONFIGURATION
- VLANS
- SERVICES
- VXLANS
- IP MULTICAST
- CLI SCRIPTING
- POLICYVIEW
- SIP
- CAPTIVE PORTAL
- GROUPS
- APP LAUNCH
- REPORT
- RESOURCE MANAGER
UNIFIED ACCESS
- UNIFIED PROFILE
- UNIFIED POLICY
- MULTIMEDIA SERVICES
- PAID ACCOUNT SERVICES
SECURITY
- USERS AND USER GROUPS
- AUTHENTICATION SERVERS
- EXTERNAL APPS
- QUARANTINE MANAGER
ADMINISTRATION
- CONTROL PANEL
- PREFERENCES
- AUDIT
- LICENSE
- OV SYSTEM HEALTH
UPAM
- SUMMARY
- AUTHENTICATION
- GUEST ACCESS
- BYOD ACCESS
- SETTINGS
- WEB CONTENT FILTERING
WLAN
- SSIDS
- WIRELESS INTRUSION
PROTECTION SYSTEM
(WIPS)
- RF MANAGEMENT
- HEAT MAP
- FLOOR PLAN
- CLIENT

<<<PAGE 28>>>
NETWORK

<<<PAGE 29>>>
OMNIVISTA - DISCOVERY & TOPOLOGY
• Discovery Management
• Alcatel-Lucent Enterprise devices in the network. 
• Links between devices in the network. Used to display links in graphical maps of network regions. 
• Additional link information required by OmniVista's Locator application. 
• Third-party devices that support has been added via the Third Party Device Support Preferences 
window. 
• Topology / Map
• Devices sorted by VLAN
• Link aggregation (all LACP information including MC-LAG)
• Spanning Tree View
• Subnet Mask Control
• Topology Map Export 
• Custom Map
• Discovery timestamp

<<<PAGE 30>>>
OMNIVISTA - LOCATOR & VM MANAGER 
• Locator
• Troubleshooting tool to identify devices & end-user location (switch, slot/port, MAC and IP 
addresses)
• Live or historical searches for immediate reaction or forensic use
• First line of defense against security hazards
• Available for Alcatel and third-party solutions (MIB-II compliant switches)
• Find and react with immediate Ban it, Change it with direct QM links
• Notifications
• Monitoring switch activity
• Trap Management tasks
• Automatic Trap Responders
• VM Manager
• Single vCenter interface
• Track VM and their associations to network equipment
• Manage UNP VLANs for virtual machines
• Notification of VMs not joining UNPs because of misconfiguration

<<<PAGE 31>>>
CONFIGURATION

<<<PAGE 32>>>
OMNIVISTA  - CONFIGURATION 
• VLAN manager 
• Create and manage VLANs across multiple switches
• Templates for rapid VLAN definition deployment
• Configuration support 
• DHCP generic rules, user defined rules & binding rules
• Link aggregation
• Integration with topology maps
• Resource Manager
• Backup and Restore current firmware configuration 
• Compare Configuration Backup Files on the same 
device or different devices
• Edit an existing backup and save the changes as a 
new backup file 
• Optimize Configuration Backup Files to save disk 
space 
• Import new or upgraded image and firmware files 
• Run Inventory Reports on network switches 
• Configure the Automatic Remote Configuration 
Feature
• Assign customized Banner and Captive Portal Web 
Interface files

<<<PAGE 33>>>
OMNIVISTA – CONFIGURATION 
• SIP
• Identifies and marks SIP and its corresponding media streams
• Provides user configured QoS treatment for SIP/RTP/RTCP traffic flows based on its marking
• Calculates QoS metric values of delay, jitter, round trip time, R Factor and MOS values of media 
streams from its corresponding RTCP streams.
• Groups
• Create LDAP service Groups
• Groups are used by policy conditions in
• PolicyView QoS 
• SecureView ACL 
• Groups enables you to create:
• MAC Groups 
• L2 VLAN Groups
• Network (IP) Groups 
• Multicast (IP) Groups
• Service Groups

<<<PAGE 34>>>
UNIFIED ACCESS

<<<PAGE 35>>>
UNIFIED ACCESS
• Unified Profile/Policy
• Create/Modify QoS Server Profiles and Access Roles, Authentication, Classification and Port Groups
• Multimedia Services
• Resolve host names to IP addresses within small networks without a Name Server.
• Paid Account Services
• Enables Bring Your Own Device (BYOD) access to the network
• Allows a wired or wireless guest, device or authenticated user to connect to the network through 
an AOS switch 
• Only supported for AOS devices running 8.1.1 and later

<<<PAGE 36>>>
SECURITY

<<<PAGE 37>>>
OMNIVISTA  - SECURITY 
• Users and User Groups
• Controls user access to OmniVista 
• Manages user access to network switches from OmniVista 
• Sets the login authentication server for OmniVista (Local, Radius and LDAP servers are currently
supported)
• Two-Factor Authentication
• Authentication Servers
• LDAP, RADIUS, ACE and TACACS+ servers are supported
• Quarantine Manager
• Protects the network from attacks
• Works with an external IPS or an AOS switch, which sends a Syslog message or SNMP trap containing 
the IP or MAC address of the offending device. 
• The attacker is immediately quarantined or placed in a Candidate List that can be reviewed for 
further action

<<<PAGE 38>>>
ADMINISTRATION

<<<PAGE 39>>>
OMNIVISTA - ADMINISTRATION
• Audit
• Monitors client and server activity
• when a user logged into OmniVista
• when an item was added to the discovery
database
• when a configuration file was saved 
• when a particular application was launched, etc.
• Administrator can
• Configure the maximum number of entries 
in the log files 
• Export and/or Archive a particular log file

<<<PAGE 40>>>
WLAN AND UPAM

<<<PAGE 41>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 42>>>
INSTALLATION & SYSTEM SETUP
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 43>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Install and configure the OmniVista
2500 
Server
- Server requirements and Licensing
- OVF Installation process
- Upgrading from a Previous Version of OmniVista
- OmniSwitch and Server parameters

<<<PAGE 44>>>
OMNIVISTA AS A VIRTUAL APPLIANCE
• Available as Virtual Machine / Virtual Appliance for 
all Hypervisors
• Includes both operating system (Linux) and OmniVista 
application
• Supported hypervisors
• VMware ESXi: 6.5, 6.7, 7.0.2 and 8.0
• MS Hyper-V: 2012 R2, 2016, 2019 and 2022
• MS Hyper-V on Windows 10 Pro 
• Linux KVM Ubuntu 22.04 
• Capacity Management
• Up to 10000 devices (includes AOS and Third-Party)
• Up to 4000 Stellar APs 
• Up to 5000 VMs from all Hypervisors

<<<PAGE 45>>>
OMNIVISTA 2500 NMS
PLATFORM AND SIZING REQUIREMENTS
• Specific configurations may vary depending on the network, number of wired/wireless 
clients, number of VLANs, open applications, etc.
*OmniVista allocates memory based on the 
network size selected during installation.
**If there are 4,000 Stellar AP in a “High” network 
size, up to 500 AOS switches can be supported. If 
there are 4,000 Stellar APs in a “Very High” 
network size, up to 1,000 AOS switches can be 
supported.

<<<PAGE 46>>>
OMNIVISTA 2500 NMS - LICENSING
• OmniVista 2500 NMS is based on licenses.
• A user is allowed to manage up to the maximum number of devices allowed for that 
license.
• There are two types of licenses:
• Device Licenses 
• Service Licenses.

<<<PAGE 47>>>
OMNIVISTA 2500 NMS - LICENSE TYPES
• Device Licenses - Manage a specific number of devices. 
• Alcatel-Lucent Enterprise Devices - Number of ALE devices (e.g. 6900, 6860) that can be managed. 
OmniVista has been certified to manage up to 10000 devices (includes AOS and Third-Party Devices). 
• Third Party Devices 
• Alcatel Lucent Enterprise OmniAccess Stellar APs - OmniAccess Stellar Wireless Devices. OmniVista 
has been certified to manage up to 4000 Stellar APs.

<<<PAGE 48>>>
OMNIVISTA 2500 NMS - LICENSE TYPES
• Service Licenses - Manage a specific number of devices for the following services: 
• VMs - Virtual Machines. VMs can be deployed on VMware vCenters and MS Hyper-V 
Servers; and OV 2500 NMS supports a mixture of Hypervisor types. The VM Manager 
application supports a maximum of 5,000 VMs from all Hypervisors.
• Alcatel Lucent Enterprise Guest Devices - Guest Devices authentication through 
UPAM. The following licenses are available: 10, 20, 50, 100, 500, or 1000 Guest Devices. 
• Alcatel-Lucent Enterprise On-Boarding Devices - BYOD Devices authentication 
through UPAM. The following licenses are available: 10, 20, 50, 100, 500, or 1000 Guest 
Devices. 
• High-Availability – Licenses the High-Availability Feature. 
• Web Content Filtering. (for Stellar APs) Control web content access and enforce web 
access policies, to keep users safe, productive, and improve network performance.

<<<PAGE 49>>>
OMNIVISTA 2500 NMS - LICENSE TYPES
• There are three types of Device Licenses: 
• Starter Pack - Free and enables you to use OmniVista on a limited basis without expiration. You can 
manage up to 30 devices (10 AOS, 10 Third Party, 10 Stellar APs). 
• Evaluation - Free and gives you full use of OmniVista, but for a limited time (90 days). You can manage 
up to 60 devices (20 AOS, 20 Third Party, 20 Stellar APs) 
• Production - Gives you full use of OmniVista without expiration. Number of devices is chosen at license 
generation (Up to 10000 devices)
• Service License Types:

<<<PAGE 50>>>
OMNIVISTA 2500 NMS - HIGH AVAILABILITY LICENSE
OmniVista 2500 HA
Please note that the HA option is available from OmniVista 4.3R1
New license makes OmniVista and its 
Unified Policy Authentication Manager 
(UPAM) component HA capable 
Once you add this license to the primary 
OmniVista 2500 installation, you don’t 
have to double the licenses on the 
redundant system

<<<PAGE 51>>>
OMNIVISTA 2500 NMS - NODE LICENSING MODEL
OS9907, OS9912
OS6900, OS6560, OS6250, 
OS6350, OS6360,OS6860, 
OS6865, OS6570M, OS6870
OmniAccess
Wireless  
Controller
3rd Party 
Devices
1 License Unit per 
Physical Unit
1 License Unit per 
Physical Unit
Licensable item as one 
unit per entity
1 license count per IP 
mgmt address
OS9907 in VC– All units need 
to be licensed 
A VC of 2 = 2 license units
OS6900 or OS6860 in VC 
All units need to be licensed 
i.e. VC of 4 = 4 license counts
OmniAccess
Stellar AP
Licensable item as one 
unit per AP

<<<PAGE 52>>>
OMNIVISTA 2500 - SUPPORTED OS & PLATFORMS FOR NMS
• Web Based User Interface 
• OmniVista 2500 NMS uses a web-based user interface.
• All applications are web-based.
• All are accessed directly through a single web GUI.
• The new web GUI is supported on the following HMTL5 capable browsers: 
• Firefox 62+ (on Windows and Redhat/SuSE Linux client PCs) 
• Chrome 68+ (on Windows and Redhat/SuSE Linux client PCs)
• Microsoft Edge

<<<PAGE 53>>>
VM APPLIANCE INSTALLATION PROCESS

<<<PAGE 54>>>
DEPLOYING THE VIRTUAL APPLIANCE
1. Log into vCenter and open the vSphere client. 
2. Select File > Deploy OVF Template. The Deploy OVF Template Wizard appears. 
3. Follow additional steps in the Virtual Appliance deployment wizard. The wizard may 
prompt the following steps: 
•
Review VM details. 
•
Review and accept end user license agreement. 
•
Specify a name and location for the deployed template. 
•
Select the host or cluster where the template is to be deployed 
•
Storage location of VM files. 
•
Disk formatting (Thin or Thick Provision). (Thick provision is recommended.) 
•
Network mapping. 
4. If the new Virtual Appliance was not powered on via the deployment wizard, power on 
the VM now.

<<<PAGE 55>>>
INSTALLATION STEPS
Prerequisite: Deploy the desired Hypervisor
Deploy the OmniVista 2500 NMS virtual appliance
Power on the OmniVista 2500 NMS virtual appliance 
•
Deployment on an Hypervisor
• Download the OmniVista 2500 Server virtual appliance from 
the Business Portal Website (BPWS)
• Deploy the virtual appliance on the chosen hypervisor
• Power on the virtual appliance

<<<PAGE 56>>>
INSTALLATION STEPS
OMNIVISTA 2500 VIRTUAL APPLIANCE > CONSOLE
• From the Hypervisor Console 
• Fill in the Initial Settings
• Keyboard layout
• Technical support code
• Password for the cliadmin user

<<<PAGE 57>>>
INSTALLATION STEPS
OMNIVISTA 2500 VIRTUAL APPLIANCE > CONSOLE
CAPTIVE PORTAL
OV WEB
ADDITIONAL OV WEB
• From the Hypervisor Console 
• Fill in the IP Settings
• OmniVista 2500 NMS IP address & Subnet Mask
•
HTTP & HTTPS Ports 
• Captive Portal IP address & Ports (if used)
• Additional OV Web IP address & Ports (optional)

<<<PAGE 58>>>
INSTALLATION STEPS
OMNIVISTA 2500 VIRTUAL APPLIANCE > CONSOLE
Network Size
Number of Devices
Low
Lower than 500
Medium
500 – 2000
High
2000 – 5000
Very High
5000 – 10000
• From the Hypervisor Console 
• Select the Network Size
• Number of devices that the OmniVista 2500 
NMS will manage

<<<PAGE 59>>>
INSTALLATION STEPS
OMNIVISTA 2500 VIRTUAL APPLIANCE > CONSOLE
• From the Hypervisor Console 
• Configure the OV2500 Additional Options
• Hostname
• DNS Server
•
NTP Server
• Timezone, Routes, ...

<<<PAGE 60>>>
INSTALLATION STEPS
OMNIVISTA 2500 VIRTUAL APPLIANCE > CONSOLE
• From the Hypervisor Console 
• Exit & Reboot
• Exit the Additional Options menu
• Virtual Appliance automatically reboots

<<<PAGE 61>>>
LAUNCHING OMNIVISTA 2500 NMS FOR THE FIRST TIME
URL
<IP@ OV WEB>
HOME PAGE
« LICENSE NOT FOUND » PAGE
• Web Interface & License
• OmniVista 2500 NMS access using a Web Browser
• 1st time connection to the Web Interface = 
License window to add the OV2500 license

<<<PAGE 62>>>
OMNIVISTA - DASHBOARD
• Home – Returns the user to the Dashboard
• Admin - Brings up the Local User Management 
Screen. 
• Help - Brings up the OmniVista 2500 NMS 
Getting Started Guide
• Videos – Launches the Alcatel-Lucent 
Enterprise YouTube Demo Playlist  
• About - Displays basic OmniVista 2500 NMS 
information
• Logout - Logs you out of OmniVista 2500 NMS.
• Dashboard Customization
• LAN / WLAN Widgets
• Adding Widgets
• Removing Widgets

<<<PAGE 63>>>
APPLICATION WIDGETS
• Provides a quick overview of key applications
• Provides direct access to the application for more detailed information/configuration

<<<PAGE 64>>>
OMNIVISTA - WEB PREFERENCES
• Administrator > Preferences
• User Settings
• Language
• Theme
• Inactivity Timeout
• Table/List View Mode
• Temperature Units
• Device Naming
• Colors 
• Sounds
• System Settings
• Branding
• Proxy
• ProActive Lifecycle 
Management
• Videos
• Email
• SMS
• CA Certificate Import
• Install Zulu CEK
• Collect Support Info
• Enforce Strong 
Password
• Google Map API

<<<PAGE 65>>>
OMNIVISTA - HELP

<<<PAGE 66>>>
LICENSES INFO
• Manage Licenses
• Enterprise, Third Party, Stellar APs, VMs, Guest, On-Boarding, High-Availability
• Add/Import

<<<PAGE 67>>>
OMNISWITCH INITIAL SETUP

<<<PAGE 68>>>
SWITCH – SNMPV1/V2 SET-UP
• Basic SNMP Set-up (V1 or V2)
• aaa authentication snmp local
• user test1234 password public99 read-write all read-only none no auth
• snmp community map public user test1234 enable 
• snmp security no security
• snmp station <ip> <v1|v2|v3>  test1234 enable
• Optional
• interfaces 1/1-24 link-trap enable 
• snmp trap to webview enable

<<<PAGE 69>>>
SWITCH – SNMPV3 SET-UP
• aaa authentication snmp local
• user test1234 password public99 read-write all read-only [md5+des, sha, md5, sha+des]
• snmp security options
• Trap management
->snmp authentication trap enable
->snmp station 192.168.3.100 162 test1234 v3 enable
Security Level
Security Level
Security Level
no security
All SNMP requests are accepted.
authentication set
SNMPv1, SNMPv2 Gets
Non-authenticated v3 Gets and Get-Nexts
Authenticated v3 Sets, Gets, and Get-Nexts
Encrypted v3 Sets, Gets, and Get-Nexts
authentication all
Authenticated v3 Sets, Gets, and Get-Nexts
Encrypted v3 Sets, Gets, and Get-Nexts
privacy set
Authenticated v3 Gets and Get-Nexts
Encrypted v3 Sets, Gets, and Get-Nexts
privacy all
Encrypted v3 Sets, Gets, and Get-Nexts
traps only
All SNMP requests are rejected.
SNMP requests 
accepted by the switch
Security Level

<<<PAGE 70>>>
LOOPBACK0 INTERFACE
SNMP SPECIFIED ADDRESS AS SOURCE ADDRESS
• By configuring the source field of SNMP packet that can either be loopback address or 
closest ip in the ip stack or any ip address
-> snmp source ip preferred {default | no-loopback | ip_address}
⚫Interface IP address: IP address to be used in the source IP field
⚫Non-Loopback: loopback0 address not used
IP field and the first available IP address from the IP stack will be used for this field
⚫Default: loopback0 address if configured, used for the source IP field
Else the first  available ip from the IP stack will be used
-> no aaa snmp agent preferred : set to default values

<<<PAGE 71>>>
WATCHDOG APPLICATION 
• Watchdog Application Manages Services
• GUI / CLI
• Watchdog can
• Start/Stop Services
• View Service info

<<<PAGE 72>>>
OMNIVISTA SYSTEM HEALTH
• Overview of the OmniVista Virtual Appliance (VA)
•
Including CPU usage, memory usage, and network traffic. 
• It also provides information if there is a problem with the VA configuration

<<<PAGE 73>>>
SESSION MANAGEMENT
• List of all OmniVista Client login sessions
•
Can be used to log out a session

<<<PAGE 74>>>
THIN CLIENT OMNISWITCH

<<<PAGE 75>>>
THIN CLIENT OMNISWITCH 
•
No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the 
config.
•
Thin Client is supported only on switches running AOS Release 8.8R1 (or higher). 
•
Thin Client mode is configured through the activation process. 
•
Switch boots up normally and registers to OV 2500 as part of the activation process. 
•
Thin-client mode must be configured as part of the activation response message.
•
In thin-client mode, no configuration is saved in the ‘running’ directory
•
But there will be vcboot.cfg with the minimal network reachability configuration.
•
All configuration changes should be done in OV 2500.
OmniVista 2500
Callhome
Sends Config

<<<PAGE 76>>>
THIN CLIENT OMNISWITCH
• To support Thin Client, the Rule menu in the Provisioning application has some additional 
attributes:
• Thin Switch: Yes / No
• Desired Switch Config: Switch Config Template and Incremental Template
Config Snapshot from latest backup
Config Snapshot from Golden Configuration

<<<PAGE 77>>>
THIN CLIENT OMNISWITCH
• A Provisioning Rule is created to match the serial number or MAC address of the switch 
that will use the Thin Client feature:
• If the Switch Config Template and Incremental Template option is used:
In the initial call home or after reboot, 
the switch will receive the configuration 
stored in the Switch Config Template
The commands in the Incremental 
Template will be applied once and only at 
the next periodic call-home (Default is 30 
minutes) of the switch.

<<<PAGE 78>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 79>>>
REMOTE LAB CONNECTION
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 80>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Remote-Labs (R-Labs) topology
• Connect to a Remote-Lab (R-Lab)

<<<PAGE 81>>>
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

<<<PAGE 82>>>
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

<<<PAGE 83>>>
REMOTE LABS > TOPOLOGY
1
2
3
4

<<<PAGE 84>>>
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

<<<PAGE 85>>>
DHCP SERVER
• A DHCP server is running with an IP address of 192.168.100.102 and has the following 
scopes (where x stands for the switch number):

<<<PAGE 86>>>
OMNIVISTA 2500 & INTERNET ACCESS
• An OmniVista 2500 server is configured with the IP address 192.168.100.107/24.
• The OmniVista 2500 is reachable
from RDP desktop through a WEB 
client at the URL:
https://10.4.pod#.208:8443
• DNS server on the client : 10.0.0.51
• If Internet access is required for VM clients,
a pre-configuration has to be done on the OS6900-A

<<<PAGE 87>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 88>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Basic Network Setup 
How to 
✓ 
Setup OmniVista in the Remote Lab 
Test connectivity between the switches and OmniVista 
Contents 
1 
Basic Network Diagram ....................................................................... 2 
2 
Network Configuration ....................................................................... 3 
3 
Commands ...................................................................................... 5

<<<PAGE 89>>>
2 
Basic Network Setup 
 
 1 
Basic Network Diagram 
In this network there are 6900A and 6870B (backbone), 6870A and 6860B (aggregation), and 6360A and 
6360B (access). The physical connections between them are shown in the diagram below. 
IP addresses and VLANs have been assigned and client VLANs have also been assigned. 
The OmniVista 2500 server is connected to one of the core switches and additional servers that will be 
needed to fully manage your network.

<<<PAGE 90>>>
3 
Basic Network Setup 
 
 2 
Network Configuration 
As you can see in the previous diagram OmniVista is connected to port 1/1/2 of the 6900A (Sw1) 
Switches need to be configured so they can be managed by Omnivista. Layer 3 connectivity is provided, and the 
routing protocol used is OSPF. 
All VLANs are assigned the following IP addresses:   
192.168.VLAN#.SW#  
Additionally, Loopback0 addresses will be configured. These are the IP addresses that will be used to discover 
the switches in Omnivista 
 
Switch 
VLAN 
IP address 
Port(type) 
6900A (sw1) 
100 
192.168.100.1/24 
1/1/2 untagged 
112 
192.168.112.1/24 
1/1/25-26 untagged 
117 
192.168.117.1/24 
1/1/5 untagged 
 
Loopback0: 192.168.200.1 
 
10 
192.168.10.1/24 
1/1/1 untagged 
6870B (sw2) 
112 
192.168.112.2/24 
1/1/29-30 untagged 
128 
192.168.128.2/24 
1/1/5 untagged 
 
Loopback0: 192.168.200.2 
 
6360A (sw5) 
157 
192.168.157.5/24 
1/3 untagged 
 
Loopback0: 192.168.200.5 
 
6360B (sw6) 
168 
192.168.168.6/24 
1/3 untagged 
 
Loopback0: 192.168.200.6 
 
6870A (sw7) 
117 
192.168.117.7/24 
1/1/5 untagged 
157 
192.168.157.7/24 
1/1/3 untagged 
178 
192.168.178.7/24 
1/1/24 untagged 
 
Loopback0: 192.168.200.7 
 
6860B (sw8) 
128 
192.168.128.8/24 
1/1/5 untagged 
168 
192.168.168.8/24 
1/1/3 untagged 
178 
192.168.178.8/24 
1/1/24 untagged 
 
Loopback0: 192.168.200.8 
 
 
- Confirm with your instructor that the initial training setup has been applied. 
 
 
Notes: 
The initial setup contains basic configuration of the switches: VLAN, IP addresses, OSPF and port assignment. 
 
- To verify that the configuration has been loaded correctly, connect to switch 6900-A (SW1) and ensure 
that the Loopback0 (192.168.200.x) addresses of the switches are in the routing table: 
 
 
Attention 
IF THE ROUTING TABLE DOES NOT CONTAIN LOOPBACK0 ADDRESSES, PLEASE CONTACT THE TRAINER!

<<<PAGE 91>>>
4 
Basic Network Setup 
 
 
sw1 (6900-A) -> show ip routes 
 
 + = Equal cost multipath routes 
 Total 28 routes 
 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  0.0.0.0/0            192.168.100.108   05:27:22   STATIC 
  10.4.103.0/24       +192.168.112.2     05:24:04   OSPF 
                      +192.168.117.7     05:24:03   OSPF 
  127.0.0.1/32         127.0.0.1         06:34:57   LOCAL 
  192.168.10.0/24      192.168.10.1      00:02:52   LOCAL 
  192.168.20.0/24      192.168.112.2     05:25:50   OSPF 
  192.168.50.0/24      192.168.117.7     05:15:06   OSPF 
  192.168.60.0/24     +192.168.112.2     05:17:07   OSPF 
                      +192.168.117.7     05:17:06   OSPF 
  192.168.70.0/24      192.168.117.7     03:45:51   OSPF 
  192.168.80.0/24     +192.168.112.2     05:23:59   OSPF 
                      +192.168.117.7     05:23:57   OSPF 
  192.168.100.0/24     192.168.100.1     06:26:48   LOCAL 
  192.168.112.0/24     192.168.112.1     06:05:11   LOCAL 
  192.168.117.0/24     192.168.117.1     05:48:54   LOCAL 
  192.168.128.0/24     192.168.112.2     05:25:55   OSPF 
  192.168.157.0/24     192.168.117.7     05:24:50   OSPF 
  192.168.168.0/24    +192.168.112.2     05:24:04   OSPF 
                      +192.168.117.7     05:24:03   OSPF 
  192.168.178.0/24     192.168.117.7     05:24:50   OSPF 
  192.168.200.1/32     192.168.200.1     05:27:22   LOCAL 
  192.168.200.2/32     192.168.112.2     05:25:55   OSPF 
  192.168.200.5/32     192.168.117.7     05:15:06   OSPF 
  192.168.200.6/32    +192.168.112.2     05:22:52   OSPF 
                      +192.168.117.7     05:22:51   OSPF 
  192.168.200.7/32     192.168.117.7     05:24:50   OSPF 
  192.168.200.8/32    +192.168.112.2     05:24:04   OSPF 
                      +192.168.117.7     05:24:03   OSPF 
 
 
Check connectivity between switches before continuing. 
- From OS6900-A, initiate pings to the loopback0 addresses of the other switches: 
ping 192.168.200.2 
ping 192.168.200.5 
ping 192.168.200.6 
ping 192.168.200.7 
ping 192.168.200.8 
 
- Proceed to the next lab.

<<<PAGE 92>>>
5 
Basic Network Setup 
 
 3 
 Commands 
If the initial setup was not applied correctly you can type the following commands to configure VLANs and IP 
addresses: 
 
 
Do this ONLY if the initial setup was not applied and with the approval of your instructor. 
 
(sw1) 6900A  
system location “Rlab LAN Pod#” 
system contact admin 
linkagg lacp agg 12 size 2 admin-state enable  
linkagg lacp agg 12 actor admin-key 12 
linkagg lacp port 1/1/25 actor admin-key 12 
linkagg lacp port 1/1/26 actor admin-key 12 
vlan 100 
vlan 112 
vlan 117 
ip interface vlan100 address 192.168.100.1/24 vlan 100 
ip interface vlan112 address 192.168.112.1/24 vlan 112 
ip interface vlan117 address 192.168.117.1/24 vlan 117 
vlan 100 members port 1/1/2 untagged 
vlan 112 members linkagg 12 untagged 
vlan 117 members port 1/1/5 untagged 
interfaces 1/1/1 admin-state enable 
interfaces 1/1/2 admin-state enable 
interfaces 1/1/5 admin-state enable 
interfaces 1/1/25 admin-state enable 
interfaces 1/1/26 admin-state enable 
ip load rip 
ip rip interface vlan100 
ip rip interface vlan100 admin-state enable 
ip rip admin-state enable 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "vlan117" 
ip ospf interface "vlan112" 
ip ospf interface "vlan117" area 0.0.0.0 
ip ospf interface "vlan112" area 0.0.0.0 
ip ospf interface "vlan117" admin-state enable 
ip ospf interface "vlan112" admin-state enable 
ip ospf admin-state enable 
ip route-map local sequence-number 10 action permit 
ip route-map local sequence-number 10 match ip-address 0.0.0.0/0 permit 
ip redist local into rip route-map local admin-state enable 
ip redist static into rip route-map local admin-state enable 
ip redist local into ospf route-map local admin-state enable 
ip redist static into ospf route-map local admin-state enable 
ip static-route 0.0.0.0/0 gateway 192.168.100.108 
ip interface Loopback0 address 192.168.200.1 
ip dhcp relay destination 192.168.100.102 
ip dhcp relay admin-state enable 
vlan 10 
vlan 10 members port 1/1/1 untagged 
ip interface vlan10 address 192.168.10.1/24 vlan 10 
write memory

<<<PAGE 93>>>
6 
Basic Network Setup 
 
(sw2) 6870B 
system location “Rlab LAN Pod#” 
system contact admin 
linkagg lacp agg 12 size 2 admin-state enable  
linkagg lacp agg 12 actor admin-key 12 
linkagg lacp port 1/1/29 actor admin-key 12 
linkagg lacp port 1/1/30 actor admin-key 12 
vlan 112 
vlan 128 
ip interface vlan112 address 192.168.112.2/24 vlan 112 
ip interface vlan128 address 192.168.128.2/24 vlan 128 
vlan 112 members linkagg 12 untagged 
vlan 128 members port 1/1/5 untagged 
interfaces 1/1/29 admin-state enable 
interfaces 1/1/30 admin-state enable 
interfaces 1/1/5 admin-state enable 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "vlan128" 
ip ospf interface "vlan112" 
ip ospf interface "vlan128" area 0.0.0.0 
ip ospf interface "vlan112" area 0.0.0.0 
ip ospf interface "vlan128" admin-state enable 
ip ospf interface "vlan112" admin-state enable 
ip ospf admin-state enable 
ip route-map local sequence-number 10 action permit 
ip route-map local sequence-number 10 match ip-address 0.0.0.0/0 permit 
ip redist local into ospf route-map local admin-state enable 
ip redist static into ospf route-map local admin-state enable 
ip static-route 0.0.0.0/0 follows 192.168.100.108 
ip interface Loopback0 address 192.168.200.2 
ip dhcp relay destination 192.168.100.102 
ip dhcp relay admin-state enable 
vlan 20 
vlan 20 members port 1/1/1 untagged 
ip interface vlan20 address 192.168.20.2/24 vlan 20 
interfaces 1/1/1 admin-state enable 
write memory 
 
(sw5) 6360A 
system location “Rlab LAN Pod#” 
system contact admin 
vlan 157 
ip interface vlan157 address 192.168.157.5/24 vlan 157 
vlan 157 members port 1/1/3 untagged  
interfaces 1/1/3 admin-state enable 
ip static-route 192.168.0.0/16 gateway 192.168.157.7 metric 1 
ip static-route 192.168.100.0/24 gateway 192.168.157.7 metric 1 
ip static-route 0.0.0.0/0 gateway 192.168.100.108 
ip interface Loopback0 address 192.168.200.5 
ip dhcp relay destination 192.168.100.102 
ip dhcp relay admin-state enable 
vlan 50 
vlan 50 members port 1/1/1 untagged 
ip interface vlan50 address 192.168.50.5/24 vlan 50 
interfaces 1/1/1 admin-state enable 
write memory

<<<PAGE 94>>>
7 
Basic Network Setup 
 
(sw6) 6360B 
system location “Rlab LAN Pod#” 
system contact admin 
vlan 168 
ip interface vlan168 address 192.168.168.6/24 vlan 168 
vlan 168 members port 1/1/3 untagged  
interfaces 1/1/3 admin-state enable 
ip static-route 192.168.0.0/16 gateway 192.168.168.8 metric 1 
ip static-route 192.168.100.0/24 gateway 192.168.168.8 metric 1 
ip static-route 0.0.0.0/0 gateway 192.168.168.8 
ip interface Loopback0 address 192.168.200.6 
ip dhcp relay destination 192.168.100.102 
ip dhcp relay admin-state enable 
vlan 60 
vlan 60 members port 1/1/1 untagged  
ip interface vlan60 address 192.168.60.6/24 vlan 60 
interfaces 1/1/1 admin-state enable  
write memory 
 
(sw7) 6870A 
system location “Rlab LAN Pod#” 
system contact admin 
vlan 117 
vlan 157 
vlan 178 
ip interface vlan117 address 192.168.117.7/24 vlan 117 
ip interface vlan157 address 192.168.157.7/24 vlan 157 
ip interface vlan178 address 192.168.178.7/24 vlan 178 
vlan 117 members port 1/1/5 untagged 
vlan 157 members port 1/1/3 untagged 
vlan 178 members port 1/1/27 untagged 
interfaces 1/1/5 admin-state enable 
interfaces 1/1/3 admin-state enable 
interfaces 1/1/24 admin-state enable 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "vlan117" 
ip ospf interface "vlan178" 
ip ospf interface "vlan117" area 0.0.0.0 
ip ospf interface "vlan178" area 0.0.0.0 
ip ospf interface "vlan117" admin-state enable 
ip ospf interface "vlan178" admin-state enable 
ip ospf admin-state enable 
ip route-map local sequence-number 10 action permit 
ip route-map local sequence-number 10 match ip-address 0.0.0.0/0 permit 
ip redist local into ospf route-map local admin-state enable 
ip redist static into ospf route-map local admin-state enable 
ip static-route 0.0.0.0/0 follows 192.168.100.108 
ip static-route 192.168.200.5/32 gateway 192.168.157.5 metric 1 
ip interface Loopback0 address 192.168.200.7 
ip dhcp relay destination 192.168.100.102 
ip dhcp relay admin-state enable 
vlan 70 
vlan 70 members port 1/1/1 untagged 
ip interface vlan70 address 192.168.70.7/24 vlan 70 
interfaces 1/1/1 admin-state enable 
write memory

<<<PAGE 95>>>
8 
Basic Network Setup 
 
 
(sw8) 6860B 
system location “Rlab LAN Pod#” 
system contact admin 
vlan 128 
vlan 168 
vlan 178 
ip interface vlan128 address 192.168.128.8/24 vlan 128 
ip interface vlan168 address 192.168.168.8/24 vlan 168 
ip interface vlan178 address 192.168.178.8/24 vlan 178 
vlan 128 members port 1/1/5 untagged 
vlan 168 members port 1/1/3 untagged 
vlan 178 members port 1/1/27 untagged 
interfaces 1/1/5 admin-state enable 
interfaces 1/1/3 admin-state enable 
interfaces 1/1/27 admin-state enable 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "vlan128" 
ip ospf interface "vlan178" 
ip ospf interface "vlan128" area 0.0.0.0 
ip ospf interface "vlan178" area 0.0.0.0 
ip ospf interface "vlan128" admin-state enable 
ip ospf interface "vlan178" admin-state enable 
ip ospf admin-state enable 
ip route-map local sequence-number 10 action permit 
ip route-map local sequence-number 10 match ip-address 0.0.0.0/0 permit 
ip redist local into ospf route-map local admin-state enable 
ip redist static into ospf route-map local admin-state enable 
ip static-route 0.0.0.0/0 follows 192.168.100.108 
ip static-route 192.168.200.6/32 gateway 192.168.168.6 metric 1 
ip interface Loopback0 address 192.168.200.8 
ip dhcp relay destination 192.168.100.102 
ip dhcp relay admin-state enable 
vlan 80 
vlan 80 members port 1/1/1 untagged 
ip interface vlan80 address 192.168.80.8/24 vlan 80 
interfaces 1/1/1 admin-state enable 
write memory

<<<PAGE 96>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
SNMP Setup for AOS Devices 
How to 
✓ Configure AOS Devices for SNMP Access to allow OmniVista to manage the 
devices. 
Contents 
1 
Configure SNMP Access ....................................................................... 2 
2 
Summary ........................................................................................ 2 
3 
Lab Check ...................................................................................... 2

<<<PAGE 97>>>
2 
SNMP Setup for AOS Devices 
 
 1 
Configure SNMP Access 
SNMP is a communication protocol used between the OmniSwitches and OmniVista 2500. In this lab, we will 
see how to configure this protocol on the OmniSwitches so they can reach OmniVista 2500. 
 
 
Attention 
THE COMMANDS THAT WILL FOLLOW MUST BE ENTERED ON EACH OF THE 6 OMNISWITCHES THAT WE WILL USE 
DURING THIS TRAINING : 
- 
SW1 (6900-A) 
- 
SW2 (6900-B) 
- 
SW5 (6360-A) 
- 
SW6 (6360-B) 
- 
SW7 (6860-A) 
- 
SW8 (6860-B) 
 
- Authorize access to the switch (ASA - Authenticated Switch Access) via all ports and all services (snmp, 
but also telnet, FTP, SSH, etc.), and specify the local user database as the authentication source: 
 
aaa authentication default local 
 
- Create a "snmpuserv3" user account in the local database. This user must have full read-write rights and 
use the SHA and DES encryption protocols: 
 
user snmpuserv3 read-write all password “Superuser=1” sha+des 
 
- Command for defining level of security 
 
snmp security privacy all 
 
- Enables or disables SNMP authentication failure trap forwarding. 
 
snmp authentication-trap enable 
 
- This command creates an SNMP station. The IP address of the OmniVista Server is 192.168.100.107 
 
snmp station 192.168.100.107 snmpuserv3 v3 enable 
 
- These commands activate typical settings for trap tables by enabling trap absorption and allowing traps to 
be seen in Webview. 
 
snmp-trap absorption enable  
snmp-trap to-webview enable 
 
In this section, you have configured the SNMP settings necessary for the switches to connect to OmniVista 
2500. In the next section, you will learn how to discover the OmniSwitches in OmniVista 2500. 
 2 
Summary 
By default, an OmniSwitch cannot be managed by Omnivista. The switch must be modified to allow SNMP 
access.  The commands above created a user to allow SNMPv3 and then associated to the SNMP station which 
is Omnivista. 
 3 
Lab Check 
By default, would OmniVista be able to discover a network of OmniSwitches?

<<<PAGE 98>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
OmniVista Installation 
Objective 
✓ How to install the OmniVista Server. 
Contents 
1 
OmniVista Server Verification ............................................................... 2 
2 
Generating & Installing an Evaluation License ............................................ 6 
2.1. Generating the Evaluation License ............................................................... 6 
2.2. Installing the Evaluation License ................................................................. 7 
2.2.1. Inserting the License File .................................................................................. 7 
2.2.2. Inserting the License Keys ................................................................................. 7 
2.3. Deleting the License File .......................................................................... 8

<<<PAGE 99>>>
2 
OmniVista Installation 
 
 1 
OmniVista Server Verification 
 
For this training, the server has been deployed (in the form of a virtual machine), and basic configuration 
(IP address, network size, ...) has been completed. During this section, you will verify that the OmniVista 
2500 server is functioning correctly, by connecting to its web administration interface. 
 
- Open the vSphere client and Log into vCenter. Make sure that Use Windows session credentials is 
checked 
 
- Click on Login button to login into Vcenter 
- Verify that the Use Windows session credentials box is checked, then click on Login: 
 
 
 
- Click on Inventory > VMs and Templates 
- Expand the tree view on the left, until you see the virtual machines. 
 
 
 
- According to your Pod number, select the Virtual Machine PodX_OV##, then right-click on it and select 
Snapshot -> Snapshot Manager 
 
 
The name of the VM may be different according to the OV version installed in the Pod.  
Make sure that you are selecting the latest OV VM.

<<<PAGE 100>>>
3 
OmniVista Installation 
 
 
- 
In the Snapshot Manager window Select OV-Init and click on Go to.  
 
 
The name of the Snapshot may be different according to the OV version installed in the Pod. 
There is typically only one snapshot so that is the one you have to choose. Confirm it with your instructor. 
IF NO SNAPSHOT IS AVAILABLE, PLEASE CONTACT YOUR TRAINER. 
 
 
 
Click Yes to confirm it  
 
 
- This snapshot contains Omnivista initial configuration parameters such as IP address, default gateway 
and network size. 
 
- 
Check the progress in the Status Bar. Once it is completed, check if the VM has been powered on. 
Otherwise, right-click on the VM PodX_OV## and select Power -> Power On 
 
 
 
 
- 
You should see a green triangle next to the VM icon to confirm that it has been powered on. 
 
- Also check that the VM PodX_pfsense is turned on. This VM provides the configuration necessary to 
access OmniVIsta. 
 
 
- Launch a Web Browser directly from the Remote Desktop client and enter the following URL according to 
the diagram: https://10.4.X.208:8443. (where X is your Pod number)

<<<PAGE 101>>>
4 
OmniVista Installation 
 
 
 
Additionally, there may be a desktop shortcut OV2500-PodX that launches OmniVista. 
Otherwise, simply type the IP address as mentioned above. 
 
 
 
 
 
The remote lab is configured so OmniVista can be reached through the remote desktop. It is 
done in this way for easier network management. 
 
Use the following credentials to log into OmniVista 
- Username: admin 
- Password: switch 
 
 
 
- A message indicating that the default password must be changed appears. Click on the Please change 
your password link 
 
 
 
- Set the new password to Training123# and confirm it. Click on Save

<<<PAGE 102>>>
5 
OmniVista Installation 
 
 
 
- Click on the Continue to Login Page link and login using the new password. 
 
 
 
 
 
- A message box appears to add the license(s)

<<<PAGE 103>>>
6 
OmniVista Installation 
 
 2 
Generating & Installing an Evaluation License 
 
An Evaluation License provides full OmniVista 2500 NMS feature functionality, but it is valid only 
for 90 Days (starting from the date the license is generated). There is one file that contains all of 
the Device (AOS, Third-Party, Stellar APs) and Service Licenses (VM, Guest, BYOD).  
In this section, you will learn how to generate and install an evaluation license 
 
 
Tips > Evaluation License 
This part is NOT ONLY dedicated for training. Don’t hesitate to use the same process if you need to generate an 
evaluation license for your own testing purpose (lab…).  
2.1. 
Generating the Evaluation License 
 
- From the Windows Desktop, open a new web browser tab/window: 
- Copy & Paste the following URL in your RDP session:  https://lds.al-enterprise.com/  
- Click on OmniVista 2500 NMS 
- Enter:  
o 
Customer ID: 99999 
o 
Order Number: evaluation 
o 
Leave the Customer Email field blank 
- Click on Submit 
 
 
- Select the License Type: EVAL-OV2500-ALL-TYPE_1 
- Enter the Passcode: omnivista 
- Click on Submit Entry 
 
 
- Enter Company Name: ALE (or something else) 
- Click on Generate License 
- Save the file locally

<<<PAGE 104>>>
7 
OmniVista Installation 
 
- By entering your mail you can receive the license information by mail. 
 
2.2. 
Installing the Evaluation License 
- There are 2 different ways to install the evaluation license:  
- By inserting directly the license file obtained in the previous step OR by typing the license keys 
Don’t do both! 
2.2.1. 
Inserting the License File  
- Go back to the OmniVista 2500 NMS webpage:  
> Go back to the OV 2500 Web Admin Interface 
  > Click on Add License 
    > License File: click on Browse 
      > Select the license file downloaded in the previous part 
      > Click on Open 
    > Click on Submit 
 
Software and/or documentation End-User License Agreement “EULA” 
> Check OK (don’t check Enable Fleet Supervision) 
2.2.2. 
Inserting the License Keys 
- Open the file with a text editor (notepad, notepad++…). The licence keys are in clear text.  
- Go back to the OmniVista 2500 NMS webpage:  
 
> Go back to the OV 2500 Web Admin Interface 
  > Click on Add License 
 
  > In the License Key field, enter all the licenses keys that are in the license file generated in the 
previous step (/!\ remove the license name before inserting them, look at the warning below /!\) 
  > Click on Submit 
 
 
Warning 
EXAMPLE. COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES! (THE INFO THAT YOU WOULD 
HAVE TO COPY AND PASTE IS HIGHLIGHTED): 
 
EVAL-NM-EX-20-N, KEQWEXRH-VXDJBEUM-4EX$299Z-BBXS7G#4-JC!GW81R-$C8YWB1K-DBE#$LDX-AXVRMLM# 
EVAL-VMM-100-N, WWITUJ#W-EWBU@BSM-@EX$299Z-BBXS7G#4-JC!GWL1R-$CFYWB1L-X5#PC4WT-5UDJU7B# 
EVAL-AP-NM-20-N, G1CUNONJ-YFZ%JX2W-JEX$299Z-BB@S7G#4-JC!GW81R-$CHYWB1L-WAPB3U7!-GDFXMHV& 
EVAL-GA-20-N, 
VTP@GOKN-E53P8#@E-NEX$299Z-BB@S7G#4-JC!GW81R-$C#YWB1L-CJD%PRTF-9GTXNX!1 
EVAL-BYOD-20-N, 
JSQRU%HH-GFFCJUGB-ZEX$299Z-BB@S7G#4-JC!GW81R-$CRYWB1L-EBX5WUFB-8X7HF@5G 
 
- Accept the End user Agreement and do not select the Enable Fleet Supervision option.

<<<PAGE 105>>>
8 
OmniVista Installation 
 
- The main Dashboard will be shown once the licenses are applied correctly 
 
2.3. 
Deleting the License File 
 
Once the license file correctly inserted, please delete the file (“EVAL…”) from the 
computer. 
 
 
 Please proceed to the next lab.

<<<PAGE 106>>>
NETWORK, CONFIGURATION 
& ADMINISTRATION GROUPS
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 107>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Learn how to use:
- Discovery Application
- Topology Application
- Locator Application
- Notification Application
- Audit Application
- Resource Manager Application
- CLI Scripting Application

<<<PAGE 108>>>
DISCOVERY

<<<PAGE 109>>>
DISCOVERY
• Discovery wizard enables you to discover:
• Alcatel-Lucent devices in the network. 
• Links between devices
• Additional link information
• VLAN information
• Third-party devices from Cisco, 3Com, and Extreme. 
• Any additional third-party devices for which support has been added via the Third-Party Device 
Support Preferences window in the Preferences application.
• Discovering Devices
• OmniVista performs a discovery based on a specified IP address range and a Discovery Profile
• You can "re-discover" previously-discovered devices to update information about a device(s).

<<<PAGE 110>>>
DISCOVERY PROFILE - GENERAL
• Contains the parameters that are used by OmniVista when performing a discovery
• General
• Name - Profile name.
• CLI/FTP User Name - Used to establish CLI and FTP sessions with the devices.
• CLI/FTP Password - Used to establish CLI and FTP sessions with the devices. Note that the 
username and password specified will be used to auto-login to the devices

<<<PAGE 111>>>
DISCOVERY PROFILE - SNMP 
• SNMP
•
SNMP Version that OmniVista will use to communicate with the 
device.
•
Timeout (msec) that OmniVista will wait for a switch to respond 
before assuming that the request has timed-out (Default = 5,000)
•
User Name (v3 only) - The SNMP version 3 username.
•
Auth and Priv Protocol (v3 only) - used for SNMP communications 
with the discovered switches (None, MD5, SHA, ...).
•
Auth Password (v3 only) - Used for MD5 or SHA authentication 
protocol (if applicable).
•
Priv Password (v3 only) - Used as secret key (if applicable).
•
Context Name (v3 only) - An SNMP context is a collection of 
management information accessible by an SNMP entity, in this case 
OmniVista.
•
Context ID (v3 only) - Each context must be identified by a unique 
context name and a unique context ID.

<<<PAGE 112>>>
DISCOVERY PROFILE - ADVANCED
• Advanced Services
• Trap Station Name - The device username that will be used when an AOS device is configured to 
send traps to OmniVista. 
• Discover Link - Specifies how OmniVista will discover the physical links associated with the 
discovered devices. 
• Shell Preference - Specifies the default CLI to be used for discovered devices: Telnet or SSH
• Use Get Bulk - Used for retrieving large amounts of data, particularly from large tables
• Max Repetitions - The number of rows of table data that the "Get Bulk" operation will request in 
each "Get Next" operation.

<<<PAGE 113>>>
DISCOVER NEW DEVICES – IP RANGES
• Defines address ranges to discover devices
• Associates Address Ranges to SNMP Setups

<<<PAGE 114>>>
DISCOVERY – START DISCOVERING
• After creating the IP Range, click on the Discover Now button

<<<PAGE 115>>>
DISCOVERY – MANAGED DEVICES
• Displays a list of all network devices that are currently being managed by OmniVista.
• There are two tabs. 
• "ALL“ displays all managed devices (LAN Devices and APs). 
• "OAW“ displays only managed APs.

<<<PAGE 116>>>
DISCOVERY – HARDWARE INVENTORY
• Displays inventory information (e.g., CMM, Chassis, Power Supplies) for any discovered 
device

<<<PAGE 117>>>
DISCOVERY - LINKS
• Displays existing links in the network
• Automatically discovered using AMAP or LLDP
• Links can also be added manually

<<<PAGE 118>>>
DISCOVERY – MANUAL LINK
• Manual links are persistent and displayed in RED when the link goes down.
• Recommended to configure critical links providing better monitoring capabilities.
• Useful to create links between ALE devices and external devices.

<<<PAGE 119>>>
DISCOVERY - PORTS
• Displays information about ports on network devices
• Enables/Disables device ports

<<<PAGE 120>>>
DISCOVERY – SPB PORTS
• Displays information about SPB Services Ports on network devices. 
•
SPB Services are configured on edge devices, so only edge devices are displayed.

<<<PAGE 121>>>
DISCOVERY – THIRD-PARTY DEVICES SUPPORT
• Discovery and support of third-party (non-AOS) devices.
• Once third-party devices have been discovered, OV supports the following:
• Web Browser, Telnet or SSH
• Custom MIBs
• Custom Icons
• Traps
• Locator

<<<PAGE 122>>>
DISCOVERY – ADDING THIRD-PARTY DEVICE SUPPORT
• Create Mibset
• OID: Device’s Object ID
• Display Name: Name to be used for the device
• Mib Directory Name: If you want to use MIB-2 level support for third-party devices, enter mib-2. 
This generic directory already exists in OV. If you are not using standard MIB-2, enter a directory 
name.

<<<PAGE 123>>>
DISCOVERY – IMPORT MIBS
• Imports new or updated MIB files to Omnivista
• All MIB files must have an file extension of .mib
• If you create a new MIB directory, you must import a complete set of MIBs into that 
directory.
• Select the Mibset to be updated from the drop-down box and click on the Import button

<<<PAGE 124>>>
DISCOVERY – SCHEDULED UPGRADES
• Allows to upgrade multiple switches at the same time
•
Upgrade can be done immediately or scheduled for a later time

<<<PAGE 125>>>
DISCOVERY – SCHEDULED UPGRADES
• User can set the same or different software version for each device
•
Directory in which the new version will be installed can be defined as well

<<<PAGE 126>>>
DISCOVERY – SCHEDULED UPGRADES
• At the end of the software update, the user can go to the Managed Devices window to 
review the result of the action
•
Verify that the directory where the installation was made is correct and that the status of the 
update is successful

<<<PAGE 127>>>
DISCOVERY – NAAS DEVICE LICENSES 
•
A device interacts with a designated License Activation Server to obtain a Device 
License:
•
NaaS. The switch is a licensed device that participates in the NaaS subscription-based model.
•
CAPEX. The switch does not participate in the NaaS subscription-based model. 
•
CAPEX Undecided. The switch has not yet obtained a license

<<<PAGE 128>>>
TOPOLOGY

<<<PAGE 129>>>
TOPOLOGY – GEO MAP VIEW
• Google Maps for Topology
• Display of Google Maps for geolocating sites
• Zoom-In / Zoom-Out on for displaying Countries / Cities / 
Sites
• Switch to Topology application for moving to floor plans
• Sites / Devices on Google Maps
• Declare sites using address or coordinates
• Add custom notes on maps
• Link between sites showing health status

<<<PAGE 130>>>
TOPOLOGY – PHYSICAL NETWORK VIEW
• Topology of 
discovered devices in 
the network
• All discovered devices 
(default)
• Highlight specific 
devices or links
• Re-arrange devices in a 
map
• Create custom maps

<<<PAGE 131>>>
TOPOLOGY - MAPS
• Create and Manage Maps
• Physical/Logical
• Location
• Background Images
• Custom Map
• Custom Color

<<<PAGE 132>>>
TOPOLOGY – DEVICE OPERATIONS AND INFORMATION
• When clicking on a device in the map, you can:
• View detailed information
• Perform certain operations                                                Left-click
Displays Detail panel on
the right of the screen
Pointing at the device
Right-click

<<<PAGE 133>>>
TOPOLOGY – SPB NETWORK MODE 
• Displays link information for devices by BVLAN or SPT links between devices. 
•
You can also navigate to the SPB Services Screen to view detailed information about all SPB 
Services.
•
To bring up an SPB Map, click on the Map Level Actions drop-down at the top of the screen and 
select SPB Network

<<<PAGE 134>>>
TOPOLOGY – SPB NETWORK MODE
• Viewing Options
• BVLAN. Enter a BVLAN ID in the Search Bar 
to bring up a list of linked devices on the 
BVLAN. Click on a link to highlight the link 
in the map.
• SPT Links - Click on the "Available" link to 
display a list of all available SPT links 
between the devices by BVLAN.

<<<PAGE 135>>>
LOCATOR

<<<PAGE 136>>>
LOCATOR APPLICATION
• Locates Switches and Devices
• IPv4 / v6 Address
• Mac Address
• Authorized User

<<<PAGE 137>>>
LOCATOR – BROWSE
• Displays
• Search Criterion
• Search Results
• Map Location

<<<PAGE 138>>>
LOCATOR – SEARCH RESULTS
• Locate on Map
• If the device you are searching for is a switch:
•
A notification will appear and you can click on the Locate on Map button to launch the Topology 
application and display a regional map in the Physical Network that contains the selected 
device. 
•
The device is automatically selected and centered in the map display.

<<<PAGE 139>>>
ETHERNET OAM

<<<PAGE 140>>>
SAA ETHERNET OAM
•
Displays information about all configured SAAs and is used to create, edit, 
and delete SAAs between switch pairs.

<<<PAGE 141>>>
VIEWING SAA STATISTICS
•
View statistics for configured SAA in terms of:
•
Jitter, RTT, Packet Loss
•
It can also be displayed from the Main Dashboard
Line Chart
Bar Chart

<<<PAGE 142>>>
NOTIFICATIONS

<<<PAGE 143>>>
NOTIFICATIONS
• Displays traps for switches. 
• View by table
• View by device tree
• Click on the trap to view detailed information.

<<<PAGE 144>>>
CONFIGURING ALARM SOUNDS
• Set audible alarm sounds for certain OmniVista actions:
•
UI Inactivity timeout
•
Notifications Traps

<<<PAGE 145>>>
AUDIT

<<<PAGE 146>>>
AUDIT
• Monitors client and server activity
• Date and time when a user logged into OmniVista
• Device added to the discovery database
• Configuration file was saved, etc.
• OmniVista organizes this information and stores it in the following categories

<<<PAGE 147>>>
USER ACTIVITY REPORT
• Contains detailed information about actions in OV
•
User /  Client IP
•
Action / Status ...

<<<PAGE 148>>>
RESOURCE MANAGER

<<<PAGE 149>>>
RESOURCE MANAGER

<<<PAGE 150>>>
RESOURCE MANAGER – BACKUP/RESTORE
• Backup and Restore 
to OmniVista
• Firmware
• Configuration Files
• Manage Files
• Compare config files
• Edit Backup files
• Save as new Backup
• Optimize Backup files

<<<PAGE 151>>>
RESOURCE MANAGER – COMPARE
• Text file comparison 
(boot.cfg)
• Select files from list 
• Same or different 
backup or switch
• Determine changes 
• GUI
• Color coded
• Edit/Save/Restore
• Save as new

<<<PAGE 152>>>
RESOURCE MANAGER - UPGRADE IMAGE
• Upgrade Image
• Import/Upgrade
• Image files
• Firmware files
• Scheduled

<<<PAGE 153>>>
RESOURCE MANAGER - INVENTORY
• Inventory from known Switches
• Software / Hardware
• Condensed / Detailed Content

<<<PAGE 154>>>
RESOURCE MANAGER – AUTO CONFIGURATION
• Auto Configuration
• Remote Configuration
• Remote Upgrade

<<<PAGE 155>>>
RESOURCE MANAGER – SWITCH FILE SET
• Switch File Set
• Background
• Banner
• Logo
• Captive Portal
• Welcome
• Welcome Fail
• Login Help
• Welcome Login
• Policy
• Welcome  Status

<<<PAGE 156>>>
TWO-FACTOR AUTHENTICATION

<<<PAGE 157>>>
TWO-FACTOR AUTHENTICATION
•
Displays Two-Factor Authentication Status by User Role
•
Used to enable/disable Two-Factor Authentication for user login based on User Role. 
•
It requires a user to enter an authentication code after entering their login/password to 
access OmniVista.

<<<PAGE 158>>>
TWO-FACTOR AUTHENTICATION INITIAL SETUP
•
Two-Factor Authentication uses the Google Authenticator App to generate a time-based, 
6-digit code that is used to log into OmniVista. 
•
User must first download the Google Authenticator App to their phone.
•
After entering your login/password on the OmniVista Login Screen, the following Two-Factor 
Authentication Screen will appear.

<<<PAGE 159>>>
TWO-FACTOR AUTHENTICATION INITIAL SETUP
•
Open the Google Authenticator App on your phone and use your phone to scan the QR Code on 
the login screen into the App. 
•
Enter the code for your user account into the TOTP Code Field on the OmniVista Login Screen 
and click Verify to log into OmniVista.

<<<PAGE 160>>>
CLI SCRIPTING

<<<PAGE 161>>>
CREATE TELNET SCRIPTS
• Create Exit & Apply Scripts
• Preconfigured files
• Create scripts in OV or text editor
• Import Scripts

<<<PAGE 162>>>
SEND SCRIPTS
• Select a Script
• Select Switches
• Schedule and send the script

<<<PAGE 163>>>
VIEW LOG
• View Script Log
• Success / Error
• Syntax errors

<<<PAGE 164>>>
SSH/TELNET
• SSH/Telnet to a New Device
• New from 4.3R2 and later
SNMP users and community strings need to be configured on devices before they can 
be managed by OmniVista. 
You can now SSH/Telnet to a newly added device that is not yet reachable by SNMP 
to configure the device for OmniVista management.

<<<PAGE 165>>>
SWITCH USER ACCOUNT

<<<PAGE 166>>>
SWITCH USER ACCOUNT
• Creates switch user accounts through UPAM
•
After creating a switch user, you create a AAA Profile for the user, setting UPAM as the server 
used for switch access, and assign the AAA Profile to network switches

<<<PAGE 167>>>
SWITCH ACCESS RECORD
• Displays information about user authentication access to network switches through UPAM.

<<<PAGE 168>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 169>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
OmniVista Getting Started with Discovery 
How to 
✓ Use the Discovery application to create a Discovery profile and discover 
devices in the network. 
Contents 
1 
Discover Devices on the Network ........................................................... 2 
2 
Summary ........................................................................................ 5 
3 
Lab Check ...................................................................................... 5

<<<PAGE 170>>>
2 
OmniVista Getting Started with Discovery 
 
Implementation 
 1 
Discover Devices on the Network 
- Open the GUI of OmniVista and Enter the user credentials (login: admin / password: Training123#) then 
click on Sign in : 
 
 
- Make sure LAN+WLAN menu is selected. 
- Go to Network -> Discovery -> Discovery Profiles to open the application.  
 
 
- Click on the “+” button to add a new Discovery profile.  
- In the Create Discovery Profile screen, Section General, enter the following parameters: 
- Name: Training 
- CLI/FTP User Name: admin 
- CLI/FTP Password: switch 
- Confirm CLI/FTP Password: switch 
 
- In the Create Discovery Profile screen, Section SNMP, enter the following parameters: 
- SNMP Version: SNMPv3 
- Timeout (msec): 5000 
- Retry count: 3

<<<PAGE 171>>>
3 
OmniVista Getting Started with Discovery 
 
- User Name: snmpuserv3 
- Auth & Priv Protocol: SHA+DES 
- Auth Password: Superuser=1 
- Confirm Auth Password: Superuser=1 
- Priv Password: Superuser=1 
- Confirm Priv Password: Superuser=1 
 
 
 
 
- In the Create Discovery Profile screen, Section Advanced Settings, enter the following parameters: 
- Trap Station User Name: admin 
- Discover Link: Normally 
- Shell Preference: SSH 
- Use BetBulk: on 
- Max Repetitions: 10 
 
 
 
- Select Create to finish the Discovery Profile creation. 
 
- Select Managed Devices on the left menu and then select Discover New Devices.

<<<PAGE 172>>>
4 
OmniVista Getting Started with Discovery 
 
 
 
- Select the “+” button and enter the following parameters: 
- Start IP: 192.168.200.0 
- End IP: 192.168.200.8 
- Subnet Mask: 255.255.255.0 
- Select the Training profile from Choose Discovery Profiles and click on “+” to move it to the right 
- Click Create 
 
 
- Select the ranges from the list and select Discover Now. 
 
- The discovery process will start and you should notice the progress.

<<<PAGE 173>>>
5 
OmniVista Getting Started with Discovery 
 
- Select Finish when the discovery is completed. 
 
 
- 
You should see the discovered devices in the Managed Devices window. You can also find additional 
information about the status of the switch, its IP address, the type of switch discovered, and the 
firmware version used. 
 
 
 2 
Summary 
When OmniVista is first run, it automatically starts the Dashboard application. From the dashboard 
Discover can be run to populate the database with network equipment.  Different SNMP settings can 
be configured for different equipment if necessary. Once devices are discovered, the Topology 
application can be used to browse the network. 
 3 
Lab Check 
1. 
How can 3rd party devices be discovered by OmniVista? 
 .......................................................................................................  
 .......................................................................................................  
2. 
Where and why are the switch Telnet and FTP usernames added? 
 .......................................................................................................  
 .......................................................................................................

<<<PAGE 174>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Topology Configuration 
How to 
✓ How to use OmniVista Topology application to create and modify maps and 
links. 
Contents 
1 
Setting up the Network Topology ........................................................... 2 
2 
Summary ........................................................................................ 4 
3 
Lab Check ...................................................................................... 4

<<<PAGE 175>>>
2 
Topology Configuration 
 
Implementation 
 1 
Setting up the Network Topology 
 
In this lab, we will see how to display an OmniSwitch on a map. This makes it easier to supervise the 
equipment; in fact, using this application, it is possible to display the connections (links) between the 
switches, as well as their status (in service / out of service). These connections (links) are updated at regular 
intervals. 
 
- Make sure LAN+WLAN menu is selected. 
- Go to Network -> Topology 
 
- The Geo Map View is shown. Switches currently do not have a specific location, so we will assign it to 
them. 
 
 
 
- Click Create Site and complete the following: 
Site Name: My Site 
Location: Select Street Address 
Enter the address of your company if available 
Select all switches using the + button, so they move to the right side of the screen. 
Click Create. 
 
 
 
 
 
- You should see the site is created in the location you entered. Drag the map if the location is not shown.

<<<PAGE 176>>>
3 
Topology Configuration 
 
- Select your site to show the details and click Go to Topology. 
 
 
 
 
- The Topology View is shown. A site Map is created with the switches in your network.  
- From the drop down box on the top left side of the screen, select your newly created map if it is not 
shown. You will see your network diagram. 
- Arrange the switches according to the diagram below: 
 
 
 
 
Any active link is automatically detected by Omnivista using LLDP. 
 
 
If a link is not being shown in the map, select the switch and look for the Operations window 
on the right. Select Poll Device or Poll Link and then wait for a moment to synchronize.

<<<PAGE 177>>>
4 
Topology Configuration 
 
- Clicking on your switch will display the menu on the right giving you the capability to manage your switch. 
Right click on a switch to see the various options. 
          
 
 
At the end of this lab, all of the OmniSwitches are declared, and can now be managed, from the OmniVista 
2500 web interface. 
 
 2 
Summary 
The Topology application allows an administrator to draw out the network and the actual links 
between devices. Additionally, by browsing the network using the Topology application all devices can 
be accessed for configuration. 
 3 
Lab Check 
1. 
What must be done for switches to show up in the Topology application? 
 ..............................................................................................................  
 ..............................................................................................................  
2. 
What are some mapping features that would be useful in creating a diagram of a network?  
 ..............................................................................................................  
 ..............................................................................................................  
3. 
3rd party devices cannot be seen under the Topology application. T/F 
 ..............................................................................................................  
 ..............................................................................................................

<<<PAGE 178>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
VLAN Manager 
How to 
✓ Use OmniVista to create and manage VLANs and interfaces across the 
network. 
Contents 
1 
Configuring VLANs ............................................................................. 2 
2 
Summary ........................................................................................ 8 
3 
Lab Check ...................................................................................... 8

<<<PAGE 179>>>
2 
VLAN Manager 
 
Implementation 
 1 
Configuring VLANs 
- Make sure the LAN+WLAN menu is selected 
- Go to Configuration -> VLANs 
 
- In this lab you are going to create VLAN Pod# +200 (e.g. VLAN 219 for Pod 19) on the switches you are 
working on and you will set this VLAN as a Q-tagged VLAN of the ports that are interconnecting the 
switches according to the lab diagram: 
 
 
 
 
 
 
If two users are working on the same Pod, then work together to complete this Lab.

<<<PAGE 180>>>
3 
VLAN Manager 
 
- From the VLAN Manager screen click on Create VLAN by Devices to launch the VLAN Wizard 
 
 
- In the Device Selection section, enter the VLAN ID and click the blue + button to add it. Do not modify 
the other options 
 
 
 
- Select Add/Remove Devices to add the switch(es) that you plan to configure. Select all the switches with 
“Add All>>” and click OK. Then click Next. 
 
 
 
 
 
- In the VLAN Configuration screen, confirm that the switches you have selected are in the list. Click Next.  
 
- Do not modify the Default Ports Assignment screen. Click Next.

<<<PAGE 181>>>
4 
VLAN Manager 
 
 
- In the Q Tagged Ports Assignment section, you are going to tag the VLAN on the required ports.  
 
- For each switch select the Add Port link and choose the ports according to the diagram. Once finished 
click Next 
 
 
 
 
 
 
- Review your VLAN configuration. You can come back to the previous sections if needed. Click on Create.

<<<PAGE 182>>>
5 
VLAN Manager 
 
 
 
- The VLAN configuration is pushed to the selected switches. You will then get the result when it is done. 
Click OK. 
 
 
 
- After the VLANs have been configured, you should be able to see them in the VLANs list. 
 
 
Click Add > Use Switch Picker to select the switches you want to display 
 
 
 
 
- Select any VLAN and click on Actions to see all the configuration options available.

<<<PAGE 183>>>
6 
VLAN Manager 
 
 
- Now let’s create an IP interface associated with the new VLAN.  
- Click on IP interface. 
- Click on “+” to add a new IP interface. 
 
 
 
 
- Configure the following: 
Name: VLAN_Pod# 
IP Address: 192.168.VLAN#.Switch# 
Subnet Mask: 255.255.255.0 
Device Type: VLAN 
VLAN ID: Pod# +200 (i.e. 219 for Pod 19) 
Device: Select the switch on which the IP interface will be created

<<<PAGE 184>>>
7 
VLAN Manager 
 
 
 
- Click on Create. 
 
 
 
- Click OK. 
Create an IP interface on all switches following the same procedure 
 
- Click on Select a Device and select the Switch on which the IP interface has been created. Verify that the 
IP interface is in the list. 
 
 
 
- From the Remote Desktop, open a console session to the switches and verify the configuration

<<<PAGE 185>>>
8 
VLAN Manager 
 
 2 
Summary 
The VLANs application allows for the creation of VLANs on multiple switches with just a few clicks. 
Without this capability it would be required to configure each switch individually. Additionally, 
mobility rules, spanning tree, 802.1, link aggregation and IP router interfaces can be configured. 
 3 
Lab Check 
1. 
In order to create a VLAN on multiple switches using OmniVista, each switch must be configured 
individually. T/F 
 .......................................................................................................  
 .......................................................................................................  
2. 
Can router IP interfaces be created directly from OmniVista? 
 .......................................................................................................  
 .......................................................................................................  
3. 
List some additional tasks that can be done with the VLANs application. 
 .......................................................................................................   
 .......................................................................................................

<<<PAGE 186>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Locator 
How to 
✓ Find devices on the network by IP address. 
Find devices on the network by MAC addresses. 
Find devices on the network by browsing the switch tables. 
Contents 
1 
Locator.......................................................................................... 2 
2 
Summary ........................................................................................ 4 
3 
Lab Check ...................................................................................... 4

<<<PAGE 187>>>
2 
Locator 
 
Implementation 
 1 
Locator 
 
- In this lab we are going to use the Locator application to find devices by IP or MAC address 
- Make sure LAN+WLAN menu is selected. 
- Go to Network -> Locator 
 
- Enter an IP Address of any of the interfaces that you have configured on the switches (192.168.X.Y). Click 
Locate to begin the search. 
 
 
 
 
You can try Live or Historical searches. 
 
 
 
- Once found, OmniVista will display it in the Initial Lookup and Search Results windows. If it’s a switch on 
the network OmniVista will display a message.  
 
- If you click on the Locate on Map icon, you’ll be brought to the Topology Map. The switch will be 
identified in the Map.

<<<PAGE 188>>>
3 
Locator 
 
 
 
- If you go back to the Locator application and select Browse on the left menu, you’ll see the MAC 
addresses learned for the selected switches. 
 
 
 
 
Click on ADD -> Use Picker to select a specific switch 
 
 
 
Select a switch and click on Add to move it to the right and then click OK.

<<<PAGE 189>>>
4 
Locator 
 
 
 
- Navigate between the different options: Location, Classification, Data Center and Layer 3 
 2 
Summary 
The Locator application can be extremely helpful in locating devices on the network. This can be done 
in either real-time using the Live Search option or from a historical database gathered during switch 
polling. 
 3 
Lab Check 
1. 
Locator can only find devices on the network if they have an IP address. T/F. 
 .......................................................................................................  
 .......................................................................................................  
2. 
What’s does checking the Live Search box do. 
 .......................................................................................................  
 .......................................................................................................  
3. 
What happens if a device is being bridged through several different OmniSwitches? 
 .......................................................................................................  
 .......................................................................................................

<<<PAGE 190>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Notifications 
How to 
✓ Manage faults in an enterprise network.  
Send traps to the OmniVista application. 
Contents 
1 
Prerequisite: Mail Server Configuration in OV ............................................ 2 
2 
Notifications ................................................................................... 3 
3 
Notification Sounds ........................................................................... 6 
4 
Summary ........................................................................................ 6 
5 
Lab Check ...................................................................................... 6

<<<PAGE 191>>>
2 
Notifications 
 
Implementation 
 1 
Prerequisite: Mail Server Configuration in OV  
- First, we have to specify the SMTP mail server that will be used to send e-mails generated by Omnivista. 
- Navigate to Administration > Preferences > System Settings > Email  
- Complete the following in the Email Settings screen: 
o 
SMTP Server: 10.130.5.6 
o 
‘From’Address: ovX@company.com  (where X is your pod number) 
o 
SMTP Authentication: OFF 
- Connection to the mail server can be tested using the following: 
o 
‘To’ Address to Test: adminX@company.com 
- Click on Send Test E-mail 
- Scroll up to see the successful message. 
- Open a web browser and open the mail server using the following address: http://10.130.5.6 
- Login using the following credentials: 
o 
Name: adminX@company.com   (where X is your pod number) 
o 
Password: password 
- Click Login 
 
- You should see the test email that was sent from OV. Look for the OmniVista Test Message email. 
 
- If you open it, you see that OV is configured correctly to send e-mails.

<<<PAGE 192>>>
3 
Notifications 
 
 2 
Notifications 
 
- The Notification application is a tool to help identify faults in an enterprise network. It allows the network 
administrator to receive traps and generate an email or launch an application when a fault occurs.  This 
allows the necessary action to be taken to rectify the situation. 
 
- Note: 
To receive a trap link message, make sure this is enabled: 
 
interfaces <slot>[/port] link-trap enable  
show interfaces status to check trap link messages are enabled 
 
- Make sure LAN+WLAN menu is selected 
- Select Network -> Notifications 
 
The Notifications Home screen will appear. 
 
 
 
 
- On the left menu select Trap Responders and click on the “+” button. 
 
 
 
 
- In the Agent section, configure the following: 
o 
Agent Type: Device 
o 
Agent Start IP: 192.168.200.1 
o 
Agent End IP: 192,168.200.8 
- Click Next 
 
 
 
- In the Trap Type section, disable the Normal trap so only the other severity levels are included in the 
mail.

<<<PAGE 193>>>
4 
Notifications 
 
- Do not modify the filter 
- Click Next 
 
 
 
- In the Response section, the response of all the traps will be done via the Action “Send an e-mail”. 
Provide the E-mail address adminX@company.com (where X is your Pod number) for OmniVista to send it 
(check with instructor for email server availability).  
- Click Create when done. 
 
 
 
- You may now test the configuration by disconnecting a link between 2 switches to generate a trap. 
-  Traps can be viewed from the Notifications Home screen

<<<PAGE 194>>>
5 
Notifications 
 
 
 
 
- Open a web browser and open the mail server using the following address: http://10.130.5.6 
- Login using the following credentials: 
o 
Name: adminX@company.com   (where X is your pod number) 
o 
Password: password 
- Click Login 
 
- Check that a new email was generated including the traps generated by OV 
 
 
 
 
 
- Try different events, i.e. logging in to the switch with an incorrect username or password and notice 
the trap being generated.

<<<PAGE 195>>>
6 
Notifications 
 
 3 
Notification Sounds 
 
- Notifications Alarms will sound when new traps are received.  
- Go to Administration – Preferences – User Settings – Sounds 
- In the Alarm Sounds box enable the Notifications option. 
- Select the For All Severities box and click Apply 
- You can enable the same alarm sound for all Trap Severity Levels or enable alarms for specific Severity 
Levels (e.g., Critical, Major). You can also set different alarm sounds for different Severity Levels. 
 
 
Due to the Remote lab Setup an audio device is not available to listen the notification sounds. 
 
 
 
 4 
Summary 
Network devices can be configured to generate traps and forward them to the OmniVista server. Using 
the Notifications application, an administrator can configure which traps to send and then respond 
using email or by launching an application when a trap is received. 
 5 
Lab Check 
1. 
Only OmniSwitches can be configured to send traps to the OmniVista Server. T/F 
 .......................................................................................................  
 .......................................................................................................  
2. 
A responder must be configured in order for OmniVista to receive traps. T/F 
 .......................................................................................................  
 .......................................................................................................

<<<PAGE 196>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Resource Manager 
How to 
✓ Perform Switch Backups and Image Code Upgrades 
Inventory Management 
Auto Configuration 
Switch File Set. 
Contents 
1 
Backup/Restore Switch ....................................................................... 2 
2 
Inventory Management ....................................................................... 7 
3 
Annex: Switch Image Upgrade ............................................................... 8 
4 
Summary ...................................................................................... 11 
5 
Lab Check .................................................................................... 11

<<<PAGE 197>>>
2 
Resource Manager 
 
Implementation 
 1 
Backup/Restore Switch 
This lab will provide the instructions to set up OmniVista to perform switch backups, image code upgrade and 
inventory management. 
- Make sure the LAN+WLAN menu is selected 
- Select Configuration -> Resource Manager 
- In the Resource Manager Home screen, click the Backup/Restore on the left panel. Then click 
Backup/Restore. 
 
- Click the Backup button. 
 
- Select Backup by Devices. Click Next.

<<<PAGE 198>>>
3 
Resource Manager 
 
- In the Device Selection screen, click on Add -> Use Switch Picker.  
 
- Select one of your switches and click Add. Then click Ok 
 
- Your switch may not have the FTP authentication credentials. Click on Add FTP Authentication if 
prompted.

<<<PAGE 199>>>
4 
Resource Manager 
 
- Enter the default user name and password (admin/switch) and click Apply. 
 
- Wait a moment until the database is synchronized. Click on Next. 
- In the Configuration screen set Backup Type to Configuration Only. Give the backup process a 
description and check Scheduled Setting to perform a scheduled backup if desired. Click on Backup. 
 
 
- Verify the result of the backup and click on OK.

<<<PAGE 200>>>
5 
Resource Manager 
 
- Choose Restore in the menu on the left to restore a backup configuration. 
 
- Click on Add/Remove Backup Files, select the files to restore and click OK. 
 
- You can then select manually the file(s) you want to restore. Click on Restore. Validate the restoration 
with Yes.

<<<PAGE 201>>>
6 
Resource Manager 
 
- Verify that all the files have been restored and click OK.

<<<PAGE 202>>>
7 
Resource Manager 
 
 2 
Inventory Management 
In the Resource Manager Home screen select Inventory on the left panel  
 
- In the Create Report screen select the switch from which you want to generate an inventory report with 
Select Devices 
- Select the type of report and click on Create. 
 
 
 
 
Select the link and OmniVista will launch a web-browser and the report will be created.

<<<PAGE 203>>>
8 
Resource Manager 
 
 3 
Annex: Switch Image Upgrade 
DO NOT perform this section unless directed by your instructor. 
- The first step for performing an image upgrade is to import the new images into OmniVista.  
- In the Resource Manager Home screen, click Upgrade Image on the left panel. 
- Click on the Import button.  
 
- The new image code should already be downloaded to the hard-drive from Alcatel’s support site. The 
file is located in C:/Remote Lab/ Omniswitches firmware/ and must be a *.zip file extension. Select 
the file and click on OK. 
 
- After importing the file into OmniVista, you’ll get the following display.

<<<PAGE 204>>>
9 
Resource Manager 
 
- You may select all or some of the images to upgrade. Click Install button to perform the upgrade. 
 
- Select the firmware files and click Next. 
 
- Select the switch on which the image will be pushed with Add/Remove Device and then click OK. Note 
that OmniVista will only present the switches that can run this firmware version. Click on Next then.

<<<PAGE 205>>>
10 
Resource Manager 
 
 
- Verify all the options in Software Installation and click on Install Software.

<<<PAGE 206>>>
11 
Resource Manager 
 
- When the upgrade is done, you’ll the following information in the summary. Read the message carefully 
and follow the instruction given. 
 
- Go to the Topology Application, select your switch and click on CLI Scripting – SSH. 
- Reload your switch from the working directory. 
 
- When the switch reboots, perform a Copy Working Certified. 
 4 
Summary 
The Resource Manager can be used to backup and restore configuration files as well as upgrade code 
on multiple OmniSwitches from a single screen. 
 5 
Lab Check 
1. 
Give some advantages to using Resource Manager to administer configuration files and code. 
 .......................................................................................................  
 .......................................................................................................  
2. 
What type of file is necessary to perform a code upgrade? 
 .......................................................................................................  
 .......................................................................................................

<<<PAGE 207>>>
12 
Resource Manager 
 
3. 
Where are the backup configuration files stored? 
 .......................................................................................................  
 .......................................................................................................

<<<PAGE 208>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
CLI Scripting 
How to 
✓ Open a Telnet or SSH connection to the switch.  
Use a script to execute CLI commands on a switch. 
Contents 
1 
CLI Scripting Application ..................................................................... 2 
2 
Summary ........................................................................................ 7 
3 
Lab Check ...................................................................................... 7

<<<PAGE 209>>>
2 
CLI Scripting 
 
Implementation 
 1 
CLI Scripting Application 
- Make sure the LAN+WLAN menu is selected 
- Select Configuration -> CLI Scripting 
 
- Select the Scripts menu on the left.  
- Click on each of the existing scripts to view the commands contained. 
 
 
 
-  
- Select one of the scripts and click on Send Script

<<<PAGE 210>>>
3 
CLI Scripting 
 
- The Send Script Wizard will show up 
 
 
Click Next, click on Add/Remove Devices button to choose the switch

<<<PAGE 211>>>
4 
CLI Scripting 
 
In the Device Selection window, select the switch to send the selected script 
 
 
 
You can send the script immediately by clicking the Send Script button or schedule it by clicking Next 
 
 
 
 
After clicking Next, the Scheduler screen will appear

<<<PAGE 212>>>
5 
CLI Scripting 
 
If you would like to send the script on periodically basis. Select the radio button Periodically, then select 
the start and end time for scripting the switch, also you can select Simple or Cron to define intervals 
 
 
 
Cron provides more granular in timing by Second, Minute, hour, Day, Month and Year. 
 
 
 
 
- 
Select now and click Next to define the user variables if the selected script contains these, once done 
click on Send Script

<<<PAGE 213>>>
6 
CLI Scripting 
 
 
 
 
 
Once all the settings are completed, click Next and Send Script. 
 
 
Select Terminal on the left menu. You can select the switch you want to access via the Browse button. A 
Telnet or SSH session will be opened to the device.

<<<PAGE 214>>>
7 
CLI Scripting 
 
- Select the Logs menu, select the script that has been sent to the switch and verify the outcome of the 
commands. The results can be exported or deleted if desired. 
 
 
- Return to the Create Scripts tab and experiment with creating your own scripts. 
 2 
Summary 
At time it may be necessary to gain access to the CLI remotely. The Telnet application can be used to bring 
up a Telnet or SSH session to the switch. Additionally, command can be entered into a text file and be run on 
the switch from a remote location without having to enter them each time.  
 3 
Lab Check 
1. 
What’s the advantage of SSH over Telnet? 
 .......................................................................................................  
 .......................................................................................................  
2. 
Where can the default shell for a switch be configured? 
 .......................................................................................................  
 .......................................................................................................  
3. 
What must be done on the OmniSwitch to allow Telnet and SSH? 
 .......................................................................................................  
 .......................................................................................................  
4. 
What do some of the default scripts do? 
 .......................................................................................................  
 .......................................................................................................

<<<PAGE 215>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Administrative Users and Groups 
How to 
✓ Create user accounts and manage the read-write capabilities for certain 
users. 
Contents 
1 
The Users and Groups Application .......................................................... 2 
2 
Summary ........................................................................................ 5 
3 
Lab Check ...................................................................................... 5

<<<PAGE 216>>>
2 
Administrative Users and Groups 
 
Implementation 
 1 
The Users and Groups Application 
 
This lab provides the instructions to set up security using OmniVista. You will create Users and Groups to 
determine access privileges within OmniVista. 
 
- Make sure the LAN+WLAN menu is selected. 
- Select Security -> Users & User Groups 
 
- In the Users & User Groups Home screen select Group 
 
 
 
- Click on the Create new Group icon 
 .

<<<PAGE 217>>>
3 
Administrative Users and Groups 
 
 
- Provide the new group with the name Training and give it a description.  
- Check on the Group Rights and choose Read to provide read-only access. 
- Users could be added at this point, but we’ll create a new user. 
- Click Create when done to save the new group. 
 
 
 
- The new group is now part of the Group List. 
 
- In the User & User Groups Home screen, select User  
 
- Click + to create a new user 
 
 
 
 
- Enter the new user training_user with a password of training_user1 and make it part of the Training 
group.  
 
- As you are typing the password you can check the password strength button going from Risky – Weak – 
Fair – OK. This provides an indication of the security of the password.

<<<PAGE 218>>>
4 
Administrative Users and Groups 
 
- Click Create when done. 
 
 
 
 
- The new user is now part of the Existing Users list. 
 
 
 
 
- Log out and log back in from Omnivista using the account you have just created and try to perform 
various tasks. Notice that you are limited to view information, but you are not allowed to modify the 
configuration. 
 
- Log back in as an administrator to continue with the following labs.

<<<PAGE 219>>>
5 
Administrative Users and Groups 
 
 2 
Summary 
OmniVista provides the capability to limit the rights of users logged into the OmniVista server. This 
feature can be used to provide read-only access or even to prevent certain users from seeing all of the 
devices discovered. 
 3 
Lab Check 
1. 
What are the default accounts and what privileges do each of them have? 
 ..............................................................................................................  
 ..............................................................................................................  
2. 
OmniVista can be configured to allow users to only make modifications on edge devices. T/F 
 ..............................................................................................................  
 ..............................................................................................................  
3. 
What was different about the OmniVista interface when you logged in with an account having 
read-only privileges? 
 ..............................................................................................................

<<<PAGE 220>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Control Panel 
How to 
✓ View services currently running on OmniVista 
View Asset Management History 
Shut Down server processes on OmniVista. 
Contents 
1 
Control Panel .................................................................................. 2 
1.1. Watchdog Service .................................................................................. 2 
2 
Summary ........................................................................................ 2

<<<PAGE 221>>>
2 
Control Panel 
 
Implementation 
 1 
Control Panel 
This lab will provide the steps required to view services and shutdown the OmniVista server. 
1.1. 
Watchdog Service 
- Make sure LAN+WLAN menu is selected. 
- Select Administrator -> Control Panel.  
- The Watchdog Screen displays the status of all of the services used by OmniVista. 
- Click on any service to view detailed information (e.g., description, status, dependencies). To Start/Stop 
a service, click on the slider control next to the service (Running/Stopped).  
 
 
 
- You can start/stop all services or shutdown OmniVista using the buttons at the top of the screen: 
(DO NOT modify or stop any process unless directed by your instructor!) 
- Start All icon 
 to start all stopped services.  
- Start All icon 
  to restart all services.  
 
- Select Scheduler -> Scheduler History on the left menu. 
- This screen displays a history of all Asset Management events. 
 
 2 
Summary 
The OmniVista Control Panel can be used to start and stop services and the OmniVista server.

<<<PAGE 222>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Preference 
How to 
✓ Manage the default settings of OmniVista Web GUI 
Contents 
1 
Preference ..................................................................................... 2 
1.1. User Settings ........................................................................................ 2 
1.2. System Settings ..................................................................................... 3 
2 
Summary ........................................................................................ 3 
3 
Lab Check ...................................................................................... 3

<<<PAGE 223>>>
2 
Preference 
 
Implementation 
 1 
Preference 
This lab will provide the instructions for making OmniVista Web GUI modifications using Preferences. 
- Make sure the LAN+WLAN menu is selected. 
- Select Administration -> Preferences. 
 
- Select User Settings 
 
 
1.1. 
User Settings 
Configure settings for each user

<<<PAGE 224>>>
3 
Preference 
 
1.2. 
System Settings 
Configure system wide settings. 
 
Continue exploring the various options that can be configured using Preferences. 
 2 
Summary 
Preferences allows an administrator to change the default behavior of the OmniVista Web GUI and 
change the look and feel of OmniVista. 
 3 
Lab Check 
1. 
What are the two different areas that can be modified using Preferences. 
 ..............................................................................................................  
 ..............................................................................................................  
 ..............................................................................................................

<<<PAGE 225>>>
UNIFIED ACCESS
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 226>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Configure Unified Profiles and Policies
• Configure Captive Portal

<<<PAGE 227>>>
AUTHENTICATION SERVERS

<<<PAGE 228>>>
OMNIVISTA SECURITY - CENTRALIZED FEATURES
• Authentication Servers application 
• Manages authentication servers in OmniVista
• LDAP, RADIUS, ACE, or TACACS+ Server 
• Default OmniVista LDAP Server
• Built-in UPAM RADIUS Server

<<<PAGE 229>>>
UNIFIED ACCESS

<<<PAGE 230>>>
UNIFIED ACCESS
•
Implementation of unified security rules on OmniSwitches and OmniAccess Stellar access 
points
•
Coherence & Unification of security rules on LAN & WLAN equipment
SAME CONNECTIVITY EXPERIENCE: WIRED 
OR WIFI
FROM ANY CUSTOMER, PROFESSIONAL OR 
PERSONAL
EASY ACCESS FOR GUESTS / VISITORS
OPTIMIZED SUPPORT FOR MULTIMEDIA 
APPLICATIONS
A common  
network policy 
to provide a 
single user 
experience

<<<PAGE 231>>>
USER ROLE ORIENTED ACCESS POLICY
Employee
Profile
Guest 
Profile
VLAN
30
Internet 
Only
Lower 
Bandwidth
Lower 
Priority
Guest
VLAN
20
Employee 
Resources
Higher 
Bandwidth
Higher 
Priority
Employee
“Employee” Access 
Profile (ARP/UNP)
“Guest” Access 
Profile (ARP/UNP)
OV 2500 / UPAM

<<<PAGE 232>>>
UNIFIED ACCESS - OVERVIEW
• Unified Access is now used to manage all types of devices (R8 and Stellar APs)
Unified Profile
• Unified security for Edge Ports for both wired 
and wireless devices
Unified Policy 
• Contains Unified Policy and Policy List 
applications
• Configure QoS policies for both wired and 
wireless devices
Multimedia Services 
• mDNS application
Paid Account Services 
• Tie-in with CP BYOD applications and locator

<<<PAGE 233>>>
UNIFIED PROFILE - HOME

<<<PAGE 234>>>
UNIFIED PROFILE - WORKFLOWS

<<<PAGE 235>>>
UNIFIED PROFILE - TEMPLATES
Access Auth Profile . Enables the assignment of a pre-defined UNP port configuration to an edge port 
WLAN Service. Assigns SSID, Security, QoS and Priority to Wireless Devices
Access Role Profiles. Contains the various UNP properties, (e.g., QoS Policy List attached to the UNP, Access Policies, Captive 
Portal Authentication) 
AAA Server Profile. Defines specific AAA parameters that can be used in an Access Auth Profile or a Captive Portal Profile
Access Classification. If authentication is not available or does not return a profile name, these rules are applied to 
determine the profile assignment
Customer Domain. Additional method for segregating device traffic. Once a UNP port is assigned to a specific customer 
domain ID, only classification rules associated with the same domain ID are applied.
SPB Profile. Dynamically assign devices to a specific SPB Service using a device's MAC Address
Far End IP - Edit/Delete Far End IP Lists. Far End IP Lists allow multiple far-end nodes to be associated with the service created 
for the VXLAN Network ID (VNID) specified in a VXLAN Profile.
Global Configuration. This can be assigned and automatically applied to all UNP ports which have not been assigned an Access 
Authentication Profile

<<<PAGE 236>>>
AAA SERVER PROFILE

<<<PAGE 237>>>
ACCESS ROLE PROFILE
• An Access Role Profile contains the various UNP properties (e.g., QoS Policy List attached 
to the UNP, Captive Portal Authentication) for users assigned to the profile

<<<PAGE 238>>>
ACCESS ROLE PROFILE (WIRELESS)
• Client Session Logging. 
• HTTP(S) / all sessions of wireless 
clients.
• Web Content Filtering. 
• Control web content access and 
enforce web access policies to 
improve network performance.
• Walled Garden. 
• Allows client authentication 
through social media. 
• Allows client to access sites 
without authentication.

<<<PAGE 239>>>
ASSIGNING AN ACCESS ROLE PROFILE
• After the profile is created, click on the Apply to Devices button to associate the VLAN 
and assign the profile to a switch/wireless device on the network

<<<PAGE 240>>>
ACCESS AUTH PROFILE 
• Enables a user to assign a pre-defined UNP port configuration to a UNP Edge Port or 
Linkagg
• Configures 802.1x and MAC authentication for both wired and wireless devices, Access 
Classification and the default AAA Server and/or UNP Profile to be used once a user is 
authenticated.

<<<PAGE 241>>>
ACCESS AUTH PROFILE - DEFAULT SETTINGS
• Port Bounce. Required to handle scenarios where a client is switched from one VLAN to 
other after COA. If it is enabled, the port will be administratively put down. This is to 
trigger DHCP renewal and re-authentication, if necessary.
• 802.1X Auth and MAC Auth only applies to wired devices.

<<<PAGE 242>>>
ACCESS AUTH PROFILE - NO AUTH/ FAILURE/ ALTERNATE
• 802.1X Authentication
• 802.1X Pass Alt - The user shall be assigned a Pass-Alternate UNP in case the 802.1X authentication does not result in a valid 
UNP for the pass branch. 
• Bypass Status - When it is enabled, the user's 802.1X authentication method is skipped. The user enters directly MAC-
authentication or Access Classification. 
• Failure Policy - The authentication method used if 802.1X authentication fails. 
• MAC Authentication
• MAC Pass Alt - The Access Role Profile the user is assigned to after passing authentication 
• MAC Allow EAP - Enables/Disables Extensible Authentication Protocol (EAP).

<<<PAGE 243>>>
ACCESS CLASSIFICATION
• Access Classification Rules are defined and associated with a UNP Access Role Profile to 
provide an additional method for classifying a device.
• If authentication is not available or does not return a profile name for whatever reason, Access 
Classification rules are applied to determine the profile assignment.

<<<PAGE 244>>>
ACCESS CLASSIFICATION - RULE TYPES
• For Wired devices:
• Port
• MAC 
• MAC OUI
• MAC + Port
• MAC + IP + Port
• LLDP
• Authentication Type
• IP Address; IP + Port
• For Wireless Devices:
• MAC
• BSSID
• ESSID
• DHCP Option
• DHCP Option 77
• Encryption Type
• Location

<<<PAGE 245>>>
UNIFIED POLICY

<<<PAGE 246>>>
UNIFIED POLICY
• QoS Policies that can be applied to both wireline and wireless devices.
• Unified policies are part of the Access Role Profile configuration.

<<<PAGE 247>>>
UNIFIED POLICIES
• Unified Access > Unified Policy
Click on the Create 
button to start the 
wizard

<<<PAGE 248>>>
UNIFIED POLICY LIST
• Set of Unified Policies that are grouped together and assigned to devices as a group.
• A List can be assigned to a network switch or a ClearPass server.

<<<PAGE 249>>>
ACCESS POLICIES
• Location. Specific location where a device can access the network. 
• Period. Specifies the days and times during which a device can access the network. 
•
Both policies are applied to devices classified into the Access Role Profile.

<<<PAGE 250>>>
CAPTIVE PORTAL

<<<PAGE 251>>>
CAPTIVE PORTAL - CONFIGURATION
• Creates Captive Portal global Configurations

<<<PAGE 252>>>
CAPTIVE PORTAL - PROFILE
• Provides flexible assignment of CP configuration parameters to devices classified into 
specific UNP Access Role Profiles. 
•
Only valid when assigned to Access Role Profiles on which Captive Portal authentication is 
enabled

<<<PAGE 253>>>
CAPTIVE PORTAL – PROFILE DOMAIN POLICY LIST
• Used to assign a Captive Portal Profile and QoS Policy List to users logging in from a 
specific domain

<<<PAGE 254>>>
CAPTIVE PORTAL – DOMAIN POLICY LIST
• Defines Policy Lists for different realms in which the endpoints are successfully 
authenticated.
•
Similar to creating a Profile Domain Policy List without the profile coming into play.

<<<PAGE 255>>>
CAPTIVE PORTAL - CUSTOMIZATION
• These files (e.g., html files, jpeg files) are used to create the web pages that are 
presented to the user during Captive Portal Login

<<<PAGE 256>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 257>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Unified Access 
How to 
✓ Configure Unified Access with integration of the RADIUS Server using 
OmniVista 2500NMS 
Contents 
1 
Setup RADIUS Server .......................................................................... 2 
2 
Configure Unified Access ..................................................................... 3 
2.1. Define RADIUS Server .............................................................................. 3 
2.2. User Network Profile and Unified Access ....................................................... 6 
3 
Test ........................................................................................... 10 
3.1. Unified Access ..................................................................................... 10

<<<PAGE 258>>>
2 
Unified Access 
 
 
 
Make sure that all the ports that will be part of this setup are enabled before continuing.  
 
 1 
Setup RADIUS Server 
At this step, we will setup the RADIUS Server VM. 
Open vSphere and select the AAA Training Server VM 
 
 
Right-click on it and select Power -> Power On

<<<PAGE 259>>>
3 
Unified Access 
 
 2 
Configure Unified Access  
We will now configure the 6860-B to demonstrate Unified Access: 
If the User is authenticated with the correct credentials, then the user is assigned to the UNP-employee profile, 
otherwise the user is blocked. 
 
User Type 
VLAN 
Authentication 
UNP 
Employee 
80 
802.1x 
UNP-employee 
 
- VLAN 80 was created on the 6860-B during the initial setup. Make sure this VLAN is created on the switch 
before proceeding. If not type the following: 
 
vlan 80 
vlan 80 members port 1/1/1 untagged 
ip interface vlan80 address 192.168.80.8/24 vlan 80 
interfaces 1/1/1 admin-state enable 
write memory 
2.1. 
Define RADIUS Server  
On 6860, we are going to define a RADIUS server as authentication and accounting server 
- Go to Security > Authentication Servers > RADIUS 
 
 
 
- Click on + to create a new server

<<<PAGE 260>>>
4 
Unified Access 
 
- In the Create RADIUS Server screen, type the following: 
- Server Name: RADIUS_VM 
- Host Name/ IP Address: 192.168.100.102 
- Shared Secret: alcatel-lucent 
- Confirm Secret: alcatel-lucent 
- Do not modify the other fields 
- Click on Create. 
 
 
 
- Go to Unified Access -> Unified Profile.  Select Templates

<<<PAGE 261>>>
5 
Unified Access 
 
- On the left menu select AAA Server Profile and click on the + to create a new profile 
 
 
 
- In the Create AAA Server Profile type the following: 
Profile Name: AAA_RADIUS 
- In the Authentication Servers section select the following: 
802.1X Primary: RADIUS_VM 
MAC Primary: RADIUS_VM 
Do not modify the other options 
Click on Create

<<<PAGE 262>>>
6 
Unified Access 
 
- Verify that the AAA Server Profile was created correctly and click Ok 
 
 
 
 
The AAA Server Profile is going to be applied in the following sections to the 6860. 
2.2. 
User Network Profile and Unified Access 
 
 
For OmniVista configuration, Access Role Profiles are created. 
An Access Role Profile is the same as the UNP profile for the 6860. 
 
- Go to Unified Access -> Unified Profile. Select Templates. 
 
 
 
- Select Access Role Profile from the menu that is on the left-hand side of the screen. 
- Click on the + button to create a new profile

<<<PAGE 263>>>
7 
Unified Access 
 
- In the Create Access Role Profile screen, type or select the following: 
Profile Name: UNP-employee 
- Do not modify the other options. 
- Click on Create. 
 
 
Notes: 
Type the UNP name as shown as it is the value returned from the RADIUS server 
 
 
 
- In the Access Role Profile screen, select the UNP-employee profile and click on Apply to Devices. 
 
 
 
- In the Access Role Profile Assignment screen, select the following: 
- In the Select Mapping Methods section: 
Mapping Method: Map to VLAN 
VLAN Number: 80

<<<PAGE 264>>>
8 
Unified Access 
 
- In the Select Devices section, click on the Add -> Use Picker button. 
- In the Device Selection screen, select the 6860B (192.168.200.8) and click Add, then click Ok. 
 
- No other parameters will be modified. Click Apply. 
- Make sure the profile has been assigned correctly, then click OK 
 
 
 
Next, we have to create an Access Authentication Profile. This Profile contains the type of authentication 
(802.1X and MAC-based) that will be applied on the switches. 
 
- Go to Unified Access -> Unified Profile. Select Template and then click on Access Auth Profile. 
- Click on the + button to start the configuration of a new Profile 
 
 
 
- In the Create Access Auth Profile screen, type or select the following: 
Template Name: UNP_template 
- In the Default Settings section: 
AAA Server Profile: AAA_RADIUS 
Port Bounce, MAC Auth, 802.1X Auth: Enabled. 
- Do not modify the other options. 
- Click on Create

<<<PAGE 265>>>
9 
Unified Access 
 
- In the Access Auth Profile screen, select the UNP_template profile and click on Apply to Devices 
 
 
 
- In the Access Auth Profile Assignments screen, click on the Add -> Use Switch Picker button. 
 
 
 
- In the Device Selection screen, select the 6860B (192.168.200.8) and click Add, then click Ok.  
 
- Back to the Access Auth Profile Assignments screen, select the 6860 and click on the Add Port link. 
 
- In the Port Selection screen, click on the + button that is next to the port 1/1/1 so it moves to the right-
side of the screen and then click OK 
 
 
- Make sure that the port is selected correctly and then click Apply 
- Make sure the objects were assigned correctly and click Finish.

<<<PAGE 266>>>
10 
Unified Access 
 
 3 
Test  
3.1. 
Unified Access 
- First, we will test if the RADIUS server is properly configured and reachable. From 6860B type: 
-> aaa test-radius-server RADIUS_VM type authentication user employee password password 
Testing Radius Server <192.168.100.102/RADIUS> 
Access-Challenge from 192.168.100.102 Port 1812 Time: 94 ms 
    Filter-ID = UNP-employee 
Access-Challenge from 192.168.100.102 Port 1812 Time: 213 ms 
    Filter-ID = UNP-employee 
Access-Accept from 192.168.100.102 Port 1812 Time: 272 ms 
Returned Attributes 
    Filter-ID = UNP-employee 
    User Name = employee 
- Open client 8 console to test the 6860-B. 
- Open Networks Connections and right-click on Local Area Connection 
 
 
 
- Select Properties then Authentication tab 
 
 
If Authentication tab is not available, click on the Start button, Run…, type services.msc and 
click Ok. Look for Wired AutoConfig service and start it. Now the Authentication should be 
available

<<<PAGE 267>>>
11 
Unified Access 
 
- Check the box Enable IEE 802.1X authentication and uncheck the box Cache user information for 
subsequent connections to this network  
 
 
- Click on Settings and uncheck Validate server certificate.

<<<PAGE 268>>>
12 
Unified Access 
 
 
- Keep the default authentication method (Secured password EAP-MSCHAP v2) and click on Configure. 
- Uncheck the box Automatically use my windows logon name and password. 
 
 
 
- Click on Ok three times to leave LAN connections properties. 
 
- To ensure a clean status of the user ports on the 6860, go to Configuration -> CLI Scripting,  open a SSH 
session to the switches and type the following: 
 
-> unp user flush port 1/1/1 
 
- Right-click on the network connection. Disable it and then re-enable it. 
- You should get a pop-up asking to connect to the network. 
 
 
 
- Type the following credentials: 
- User name = employee 
- Password = password 
- You should now be connected. 
- The user is assigned an IP address belonging to VLAN 80 (192.168.80.X) 
 
- On the 6860 type: 
 
-> show unp user 
                                               User 
Port    Username             Mac address       IP              Vlan Profile                          Type         
Status 
-------+--------------------+-----------------+---------------+----+--------------------------------+-----
-------+----------- 
1/1/1   employee             00:50:56:90:ae:a6 192.168.80.10   80   UNP-employee                     
Bridge       Active 
 
Total users : 1 
 
 
You may see a second entry with a different MAC address. This is the link to the physical NIC 
associated with the client VM. 
 
- Go to Network -> Locator and type or select the following: 
- Search by: Auth. User 
- employee 
- Live

<<<PAGE 269>>>
13 
Unified Access 
 
- Click on Locate 
 
 
- In the Netforward Results table select View as: Classification and check the MAC address of the VM   and 
that the user is assigned to the employee profile

<<<PAGE 270>>>
POLICYVIEW
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 271>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Administrate and deploy a global Quality of 
Service policy over a network

<<<PAGE 272>>>
OMNIVISTA POLICYVIEW
• PolicyView QoS
• “OneTouch” QoS
• Used to configure network-wide QoS policies
• Policies stored in LDAP server configured as 
part of OmniVista installation
• Switches notified to retrieve new policies from this 
server
OmniVista 2500
Infrastructure
OmniVista
PolicyView
Web Based ELMs
LDAP 
Directory
PolcyView

<<<PAGE 273>>>
OMNIVISTA POLICYVIEW
• OneTouch simplifies QoS configuration  
• Reduces the number of interfaces for configuring QoS for VoIP and time critical data operations
• Enables enhanced policy-based management across multiple devices
• Sets parameters once  
• Distributed to devices at the same time
• Operation modes
• OneTouch for Voice, Data & ACL
• QoS for one or more subnets of VoIP phones
• QoS priorities for selected data servers
• Accept/ Drop traffic for selected groups
• Expert Mode
• Advanced QoS controls for complex policies (including validation scheme)

<<<PAGE 274>>>
POLICYVIEW HOME

<<<PAGE 275>>>
QOS RULE CONFIGURATION STEPS
Create a Policy Condition
Create a Policy Action
Create a Policy Rule
Apply the Policy

<<<PAGE 276>>>
OMNIVISTA POLICYVIEW QOS - ONE TOUCH VOICE MODE
Set Voice Conditions for IP or MAC Policies

<<<PAGE 277>>>
OMNIVISTA POLICYVIEW QOS - ONE TOUCH DATA MODE
Set Data Server IP address and Priority
QoS Priority:
Platinum (7)
Gold (5)
Silver (3)
Bronze (1)

<<<PAGE 278>>>
OMNIVISTA POLICYVIEW QOS - ONE TOUCH ACL MODE
Set IP Network Group and traffic accessibility (Accept/ Drop)

<<<PAGE 279>>>
OMNIVISTA POLICYVIEW QOS - EXPERT MODE
Create Policy

<<<PAGE 280>>>
EXPERT MODE WIZARD
INITIAL CONFIGURATION
Set Policy Rule name, Precedence and Advanced 
options
Advanced options:
Default List. Adds the rule to the QoS Default 
Policy List 
Enabled. Enables the policy 
Save. Marks the policy rule so that it may be 
captured as part of the switch configuration. 
Log Matches. Log messages about specific 
flows coming into the switch that match this 
policy rule. 
Send Trap. Enables traps for the Policy 
Reflexive. Reflexive policies allow specific 
return connections that would normally be 
denied

<<<PAGE 281>>>
EXPERT MODE WIZARD - DEVICE SELECTION
Specify the devices to which the policy will be applied

<<<PAGE 282>>>
EXPERT MODE WIZARD - SET CONDITION 
Conditions:
L2 MACs. Source/ Destination MAC Address / 
MAC Group. Source MAC Range
L3 IPs. Fragment. Source / Destination IP 
Address / Network Group. Multicast IP Address
L3 DSCP / TOS
L4 Services. Protocol Only. Ports. Service. 
Service Group
L7 Application. App Group. App Name

<<<PAGE 283>>>
EXPERT MODE WIZARD - SET ACTION
Actions:
QoS. 
Disposition (Accept / Drop). 
QoS Parameters (Platinum / Gold / Silver / 
Bronze)
Max. Output Rate (kbits/sec)
Output Mapping
802.1p Priority Level
TCM. 
Committed information Rate.
Peak Information Rate

<<<PAGE 284>>>
EXPERT MODE WIZARD - VALIDITY PERIOD AND REVIEW

<<<PAGE 285>>>
POLICY AND POLICY MANAGER
Policy 
Administration
LDAP
Repository
LDAP
LDAP
LDAP

<<<PAGE 286>>>
POLICY FLOW
User creates a policy using 
OmniVista PolicyView
Policy
Directory 
Server
1
4
2
3
Policy Enabled
Switches

<<<PAGE 287>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 288>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
PolicyView 
Contents 
1 
PolicyView ...................................................................................... 2 
1.1. Configure PolicyView .............................................................................. 2 
2 
Summary ........................................................................................ 7 
3 
Lab Check ...................................................................................... 7

<<<PAGE 289>>>
2 
PolicyView 
 
Implementation 
 1 
PolicyView 
1.1. 
Configure PolicyView 
Make sure LAN+WLAN menu is selected 
Select Configuration -> PolicyView  
 
- In the Basic Network Setup Lab, VLAN 80 was configured in the 6860B. Also, port 1/1/1 was assigned to 
this VLAN. This lab uses client 8 VM which is connected to this switch. 
 
- Open a Console session to the 6860B and type the following to confirm:  
 
-> show ip interface 
Total 8 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
... 
vlan168                          192.168.168.8   255.255.255.0       UP     YES vlan 168 
vlan178                          192.168.178.8   255.255.255.0       UP     YES vlan 178 
vlan80                           192.168.80.8    255.255.255.0       UP     YES vlan 80 
 
-> show vlan 80 members 
   port      type        status 
----------+-----------+--------------- 
  1/1/1      default      forwarding 
 
- If VLAN 80 and its IP interface are not created, then type the following: 
 
vlan 80 
vlan 80 members port 1/1/1 untagged 
ip interface vlan80 address 192.168.80.8/24 vlan 80 
interfaces 1/1/1 admin-state enable 
write memory 
 
- Go to VMware vSphere Client and open client 8 VM console

<<<PAGE 290>>>
3 
PolicyView 
 
- Once in the client VM desktop, open Network Connections and select Pod connection and right-click 
Properties. Select Internet Protocol and click Properties. Make sure the Obtain an IP address 
automatically option is selected. 
 
 
An IP helper address of 192.168.100.102 was defined in the Basic Network Setup lab. If 
Client07 does not get an IP address, then make sure that the AAA Training Server PodX VM is 
powered on. 
If this does not solve the issue, then assign a static IP address in the 192.168.80.X subnet with 
the default gateway set to 192.168.80.8 
 
- 
As of now client 8 has full access to the network. From this client ping the Loopback0 IP addresses of all 
switches in the network. (192.168.200.#, where # is the switch number) 
 
 
 
An Access Control List that blocks this client to access the Loopback0 addresses in the network will be 
configured.  
 
Select Configuration > PolicyView.  
- 
In the Policy View Home, click Expert Mode.

<<<PAGE 291>>>
4 
PolicyView 
 
- 
Select the Create icon 
  
 
 
 
- 
In the Create Policy wizard, type/select the following: 
 
- 
In the Config section: 
- 
Name: Block_Loopback0_access 
- 
Precedence: 30001 
- 
Click Next 
 
 
 
- 
In the Device Selection section, select the switch8 (192.168.200.8) 
- 
Click Next 
 
- 
In the Set Condition section, open the L3 IPs section and type/select the following: 
- 
Check the Source IP Address Range option and select Subnet Mask 
- 
IP Address: 192.168.80.0 (subnet assigned to client 7) 
- 
Subnet Mask: 255.255.255.0 
 
- 
Check the Destination IP Address Range option and select Subnet Mask 
- 
IP Address: 192.168.200.0 (Loopback0 subnet configured on the switches) 
- 
Subnet Mask: 255.255.255.0 
- 
Click Next

<<<PAGE 292>>>
5 
PolicyView 
 
 
 
 
- 
In the Set Action section, select QOS. 
- 
Check the Disposition option and select Accessibility, DROP. 
- 
Click Next 
 
 
 
- 
Leave the Validity Period set to AllTheTime 
- 
Click Next 
 
 
 
 
- 
Finally review all parameters are correct and click on Create then OK. 
- 
In the Existing Policies list, select the policy that has been created and click on Select Device

<<<PAGE 293>>>
6 
PolicyView 
 
 
 
- 
Select the 6860B switch 8 (192.168.200.8) and click OK. 
 
- 
Click on Notify Selected and wait for the Notify Success! Message. 
- 
You may have to click on the Status button to get this message 
 
 
 
- 
Go back to Client 8 and try to ping the Loopback0 addresses of the switches 192.168.200.#; then ping 
the IP address of the RADIUS server 192.168.100.102 
- 
Now you see that ping to the Loopback0 IP addresses is not working because of the ACL that is blocking 
this traffic but access to other network resources is still available. 
 
 
 
Similar policies can be created to block or allow specific subnets and/or protocols.

<<<PAGE 294>>>
7 
PolicyView 
 
 2 
Summary 
At times it may be necessary to classify traffic on the network and apply QoS policies based on that 
traffic. PolicyView can be used to implement QoS throughout the entire network instead of having to 
configure each switch separately.  
 3 
Lab Check 
1. 
What is the main benefit of using PolicyView? 
 ..............................................................................................................  
 ..............................................................................................................  
2. 
Where are the policies stored? 
 ..............................................................................................................  
 ..............................................................................................................  
3. 
What has to be done to apply the Policy Rules to the switches? 
 ..............................................................................................................  
 ..............................................................................................................  
4. 
What’s the difference between the Expert and One Touch tabs? 
 ..............................................................................................................  
 ..............................................................................................................

<<<PAGE 295>>>
QUARANTINE MANAGER
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 296>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Protect an entire network by using
- Quarantine manager and remediation

<<<PAGE 297>>>
OMNIVISTA QUARANTINE MANAGER
• Quarantine Manager
• “OneTouch” device containment
• Global device containment
• "Quarantine Manager" is part of starter package
• Best when combined with an external IDS
OmniVista 2500
Infrastructure
OmniVista
Quarantine manager

<<<PAGE 298>>>
OMNIVISTA QUARANTINE MANAGER
• Detection & reporting
• Open notification scheme for security breach 
• Syslog, Trap from Alcatel-Lucent or Third party IPS/IDP solutions
• Intrusion notification from Alcatel-Lucent Security Solutions (Brick Firewall)
• OmniAccess WLAN rogue Alert
• Flexibility for containment & isolation actions
• Mac-based VLAN based on the MAC address
• ACLs for network access Resources
• Port Shut down for Third party switches 
• Wireless end user block Listing

<<<PAGE 299>>>
OMNIVISTA QUARANTINE MANAGER
Quarantine
Manager
Attack
Rogue AP
Malicious PC
Malicious PC

<<<PAGE 300>>>
OMNIVISTA QUARANTINE MANAGER
Quarantine
Manager
Attack
Rogue AP
Malicious PC
Malicious PC
Signal

<<<PAGE 301>>>
OMNIVISTA QUARANTINE MANAGER
Attack
Signal
Alert
Log
Push Webpage
Inform
Quarantine
Manager
Attack
Rogue AP
Malicious PC
Malicious PC
Quarantine

<<<PAGE 302>>>
QUARANTINE MANAGER HOME
• Quarantine Manager – Contain devices throughout entire network
• Detection of events and traps
• Syslog, WLAN Controller, ALA DoS Trap
• Removal of device from network

<<<PAGE 303>>>
QUARANTINE MANAGER
ATTACK DETECTION AND CONTAINMENT - DETECTION
• Detection of events and situations triggering  possible intrusion, attacks
• SNMP traps based rules sent by AOS Switches (AlaDoSTrap: AOS DoS traps) or by other devices 
• Syslog based rules events for WLAN controller, Third-party devices,…
SNMP AlaDosTrap 
(<IP address>)
Syslog Event
(<IP_Address>)
External Device
AOS Switch

<<<PAGE 304>>>
QUARANTINE MANAGER
ATTACK DETECTION AND CONTAINMENT - RULES
• Built-In Rules and Custom Rules 
• Alcatel DOS Trap Rule
• Triggers an action based on an AOS trap (AlaDosTrap)
• The rule triggers an action in response to a Teardrop, Ping of Death, or Port Scan attack
• Fortinet
• Anomaly - Triggers an action on a Fortinet Attack Anomaly Event. Ignores Anomaly attacks configured to 
"Pass" on Fortigate
• Signature - Triggers an action on a Fortinet Syslog Signature event. Ignores Signature attacks configured to 
"Pass" on Fortigate
• Virus - Triggers an action on a Fortinet Virus Detection event. Only triggers on sub-type "infected"
• OA WLAN
• Rogue AP Active - Triggers an action when the switch classifies an Access Point as a "Rogue AP" 
• Rogue AP Detected - Triggers an action when the Access Point detects an active "Rogue AP" 
• Station w/ Rogue AP - Triggers an action when the Access Point detects traffic from a client through a "Rogue 
AP" 
By Default all of the rules are disabled

<<<PAGE 305>>>
QUARANTINE MANAGER
ATTACK DETECTION AND CONTAINMENT - RULES
• User configurable elements to define custom QM rules and its operations
• Quarantine Rules
• A name 
• A description of the rule 
• A trigger expression that specifies the event or trap that will trigger an action 
• An extraction expression that is used to extract the source address from the event or trap 
• An action to be taken when the event or trap is received (device is placed in the Candidates list or Banned 
list)

<<<PAGE 306>>>
QUARANTINE MANAGER - ATTACK DETECTION AND 
CONTAINMENT – RULE ENFORCEMENT

<<<PAGE 307>>>
QUARANTINE MANAGER - ATTACK DETECTION AND 
CONTAINMENT – RULE ENFORCEMENT
• Quarantine actions following recognition of threats, intrusion
• Quarantine VLAN based on  VLAN MAC rule and mobility (vlan)
• Quarantine by black listing for WLAN Rogue device
• Quarantine by ACL 
• Disable port when allowed (port disabling)
• Candidate List
VLAN MAC Rule (vlan 999 <mac_address>)
VLAN DHCP MAC Rule 
ACL (condition IP source <>action <>)
IP <-> MAC
SNMP Set message

<<<PAGE 308>>>
CANDIDATES LIST 
• If a device is placed on the Candidates List, traffic to and from that device will continue 
until the Network Administrator decides what action should take place. 
• The Candidates list displays all of the devices that have been placed in by Quarantine 
Manager 
• The Network Administrator can: 
• Release the device from the Candidates List 
• Ban the device 
• Place the device on the list of devices to never be banned.

<<<PAGE 309>>>
BANNED LIST
• When a device is placed in the Banned List, it is quarantined from the rest of the network. 
• Devices can automatically be added to the Banned List based on a Quarantine Manager rule 
or manually placed in the list by the Network Administrator. 
• Once a device is placed in the Banned List, it remains quarantined until the Network 
Administrator manually releases it.

<<<PAGE 310>>>
NEVER BANNED LIST
• A device placed on the Never Banned list can never be banned, either manually or 
automatically, by Quarantine Manager. 
• Important network servers should be placed in the Never Ban list. 
• The OmniVista server and all switches discovered by OmniVista are implicitly placed in the 
Never Banned list. 
• Even though these devices do not appear in the list, they cannot be banned.

<<<PAGE 311>>>
QUARANTINE MANAGER - ATTACK DETECTION AND 
CONTAINMENT – RESPONDER
• AQM can send an e-mail to any address you specify
• Based on variables to specify the information to be included in the e-mail
• Variables exist for information, such as action, reason, Mac Address, etc. 
• AQM can execute an external program or script on the OmniVista server

<<<PAGE 312>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 313>>>
ANALYTICS
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 314>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the following:
- Analytics 
Reports
Profiles
Summary View
Applications Management
Anomalies
- Report 
Configuration
List
- Application Visibility
Configuration
Report
Enforcement

<<<PAGE 315>>>
ANALYTICS

<<<PAGE 316>>>
NETWORK ANALYTICS
• Real-time information to enable real-time business decisions 
• Historical and predictive views
• Insight of application usage and trends
• ‘Plain talking’ to drive improved business process decisions and IT cost control
• This application leverages sflow information
• Essentially L1-L4 information
• Simplified mode of operation and optimized dashboard for better visualization

<<<PAGE 317>>>
ANALYTICS - OVERVIEW
• Reports. 
Provides a comprehensive view of network resource utilization. 
Two types of reports: 
- "Visibility" Reports can be configured to show network utilization over different time periods.
- "Availability" Reports provide a "real-time" view of all discovered network switches.
• Profiles.
Used to create Analytics Profiles. To generate an Analytics Report for any of the "Visibility“ Reports, you 
must first create an Analytics Profile that defines the switches/ports that you want to view and the type 
of information that you want to view on those switches/ports.
• Statistics 
This screen is used to quickly view statistics on a device, create a View Profile, and view statistics 
from an existing View Profile

<<<PAGE 318>>>
ANALYTICS - OVERVIEW
• Summary View
Displays basic information on all supported network devices, including any Analytics Profiles defined 
for a device.
• Applications Management
When generating a Top N Applications Report, the Analytics application uses port numbers to identify 
application traffic. This screen is used to create port/application mappings to identify applications 
traffic.
• Anomalies
Displays any port utilization anomalies. An anomaly is a utilization data point that fall outside of 
expected norms based on past usage.

<<<PAGE 319>>>
REPORTS

<<<PAGE 320>>>
Application
Visibility
Network
Visibility
Network
Availability
Network Health
• Top Devices on the 
network in terms of 
CPU usage, memory 
usage and 
temperature
Top N Ports
• Top ports based on 
usage over time. Also 
provides predictive 
analytics to show 
expected future 
usage.
Network Availability 
• Current operational 
status of network 
devices (active / 
inactive)
Alarms
• Status of the 
network and traps 
by severity level.
NETWORK ANALYTICS >  REPORTS
Top N Applications 
• Top users using an 
application, and 
which switches have 
the most traffic for 
an application.
Top N POE Port
•POE port usage 
based on % of 
allocated power 
used by each POE 
port.
Top N POE Switches
•Top network 
devices based on 
the use of POE 
ports over time.
Top N Clients
•Top network users 
including the 
number of traffic 
flows for each of 
them.
Top N Applications 
- Advanced
• Top applications 
based on the 
signature profiles 
configured in 
Application Visibility

<<<PAGE 321>>>
REPORTS - MEASUREMENTS & OPERATIONS
KPI
Mechanisms
Outcome
Top N Apps 
Sflow sampling
Application name 
through TCP/UDP 
Ports
Top N Users
Sflow sampling
Source IP 
address/ Sflow
sampling
Top N Switches/ 
Resources 
Utilization
“Index” derived 
from CPU, Mem
use, Temp
Value /gravity 
scale
Top N Port 
Utilization
SNMP MIB Polling
Display top ports 
w/
high network 
traffic
KPI
Mechanisms
Outcome
Network 
Availability
SNMP- Device poll
Display device 
status
Alarms
SNMP –
Trap/Severity
Display total 
alarms in network
Network
Visibility
Network
Availability

<<<PAGE 322>>>
REPORTS - SFLOW SAMPLING OVERVIEW
Mongo DB
OV 
Analytics 
Service
AOS 
Switch
WebServer
Sflow
Packets
Store analytical 
data
Present 
analytics OV 
WebUI
• OV profiles used to create sampling on switch ports
• Reports can be pre-defined or customized
Sflow Collection & Sampling used for
•Top N app 
•Top N users

<<<PAGE 323>>>
REPORT CUSTOMIZATION
Report View
(Summary or Detail)
Report View
(List or Graph)
Selection of equipment to 
be analyzed
(Topology or Switch picker)
Adding to a scheduled report
Download PNG format 
Download PDF format
Print Report
Number of Devices
Time Interval
Interval duration

<<<PAGE 324>>>
TOP N REPORTS - CUSTOMIZATION
• Click on the Configuration icon in the upper right corner of the screen to configure how 
information is displayed in the report.
• Default Devices - By default, all top switches/ports are displayed. However, you can click on the 
Select Devices button to display only information from specific switches.
• Number of Top Applications/ Clients/ Switches/ Ports - Range = 1 – 20, Default = 10
• Interval Type - The time interval for the information: 
• Up Until Now - Displays all information in the selected time interval (e.g., last 24 Hours). 
• Custom - Sets the start and end time for the information you want to display. You can display up to 3 months 
of data. When data reaches the 3-month maximum, it is overwritten with new data.
• Time Interval - Last 24 Hours, 7 Days, or 4 Weeks
• Auto Refresh Timer - In minutes (Range = 15 - 60, Default = 15).

<<<PAGE 325>>>
TOP N APPLICATIONS - SUMMARY VIEW
• Displays information about the top applications being accessed on the network. 
• The Top N Applications are determined using sFlow. 
• OmniVista identifies the applications using the TCP/UDP port obtained from sFlow packets. 
• Well known ports (e.g., 161 for SNMP, 80 for HTTP) are automatically identified and labeled in the 
Top N Applications Report. 
• Other applications can be mapped using the Applications Management Screen.
Pie Chart
List View

<<<PAGE 326>>>
TOP N APPLICATIONS - CLIENT AND SWITCH INFORMATION
• When in the Pie Chart View of the Top N Applications Report you can identify:
• Clients accessing an application (by source IP address). 
• Switches passing the application traffic. 
• Right-click on a section of the Pie Chart and select the appropriate option.
A legend (not shown here) identifies 
the client or switch by color and 
text, or you can hover over a 
section to view the client/switch IP 
address (along with detailed flow 
information).
Clients
Switches

<<<PAGE 327>>>
TOP N APPLICATIONS - DETAIL VIEW
• Provides a detailed view of the specified time interval. 
• For example, if a report displays data for the last 24 hours, the Summary View will display a 
summary of the data for the last 24 hours; and the Detail View will then display data for each hour 
within those 24 hours.

<<<PAGE 328>>>
TOP N APPLICATIONS - TRENDING INFORMATION
• When in the Detail View, you can click on a bar in the chart to view usage trends for each 
application for the selected time interval by "drilling down" on a data set to see a subset of 
that data.
• The trend for an hour would be displayed in 15-minute increments.

<<<PAGE 329>>>
TOP N CLIENTS - SUMMARY VIEW
• Displays information for the top network clients including the number of traffic flows for 
each client. 
• OmniVista uses the source IP address in the sFlow packet to determine the client. 
• Each client is displayed as a percentage of the total for the configured time interval (e.g., last 24 
hours). 
Pie Chart
List View

<<<PAGE 330>>>
TOP N CLIENTS - DETAIL VIEW AND TRENDING INFORMATION
• Detail view provides a detailed view of the 
specified time interval 
• If a report displays data for the last 24 hours, 
the Detail View will display data for each hour 
within those 24 hours.
• Information is displayed in a bar chart view
• In the Detail View, you can click on a bar in 
the chart to view usage trends for each 
client for the selected time interval
• Displayed in 15-minute increments. 
• Click on a data point in the trending view 
for more detailed information.

<<<PAGE 331>>>
NETWORK HEALTH
• Displays information for the top switches on the network in terms of the switch's resource 
usage. 
• Based on switch's CPU usage, memory usage, and temperature.

<<<PAGE 332>>>
TOP N PORTS - SUMMARY VIEW
• Displays the top network ports based on 
utilization. 
• Displayed as a percentage of the total 
utilization for all monitored ports.
• In this view, switches/ports are 
displayed in a list view from highest to 
lowest utilization for the configured 
time period (e.g., day, week).

<<<PAGE 333>>>
TOP N PORTS - DETAIL VIEW
• Depending on the number of ports you 
configured for display (e.g., top 10 
ports, top 15 ports), any monitored 
ports that qualify during the configured 
time interval (e.g., last 24 hours) are 
displayed. 
• Ports are simply stacked numerically in 
each bar by IP address and port number 
(the order is not based on utilization).

<<<PAGE 334>>>
TOP N PORTS - TRENDING VIEW
• Used to view predicted future port utilization based on past utilization. 
• Predictions can provide valuable insight for capacity management. 
• OmniVista samples past port utilization for a period of time (Prediction: Training Timeout), 
and predicts future utilization within a configurable error rate (Prediction: Training Error) 
using a machine learning algorithm.
• The predicted utilization will appear in the display to the right of the current utilization. 
• The predicted usage will be slightly shaded to differentiate it from current usage.
• The amount of predicted data displayed depends on the interval time configured for the 
report
Configured Time Interval
Amount of Predicted Data
Last 24 Hours
12 Hours
Last 7 Days
3 Days
Last 4 Weeks
2 Weeks

<<<PAGE 335>>>
TOP N PORTS - TRENDING VIEW
Current
Predicted

<<<PAGE 336>>>
TOP N POE PORTS 
• Displays the top network PoE ports based on the amount of power being utilized by each 
PoE Port.
•
You can use the report to determine ports that may be drawing more power than anticipated

<<<PAGE 337>>>
TOP N POE SWITCHES
• Displays PoE utilization by switch
•
The "Usage Percentage" is the percentage of total PoE power available on the switch that is 
currently being used

<<<PAGE 338>>>
REPORTS - NETWORK AVAILABILITY
• Displays the current operational state of all discovered network devices 
(Up/Warning/Down)
• Each category is displayed as a percentage of all monitored switches
• Click on a category to display a list of switches in the category, with specific information about 
each switch.

<<<PAGE 339>>>
REPORTS - ALARMS
• Displays network status/traps for all discovered switches. 
• A graphical pie chart view or a list format can be displayed. 
• The reported alarms in each severity level are displayed as a percentage of the total 
alarms reported. 
• Click on a severity level in the pie chart to view the switch(es) from which the alarms originated, 
and the number of those alarms received.

<<<PAGE 340>>>
PROFILES
• Displays currently configured Analytics Profiles. 
• Used to create, edit, and delete profiles. 
• The first step in generating analytics information for any of the "Visibility" Reports (Top N 
Applications & Clients, and Top N Ports Utilization) is to create an Analytics Profile. 
• A profile consists of the type of information you want to view (Profile Type) and the 
switches/ports that you want to analyze.
Create Profile

<<<PAGE 341>>>
PROFILES - CONFIGURATION
• Configuration Screen
• Profile Name - User-configured name for the profile.
• Profile Type - Select a Profile Type from the drop-down menu:
• Top N Apps & Clients 
• Top N Ports Utilization  / Top N PoE Ports
• Sampling Rate (Top N Apps & Clients Only) - Ratio of packets observed at the data source to the 
samples generated. For example, a sampling rate of 100 specifies that 1 sample will be generated 
for every 100 packets observed.

<<<PAGE 342>>>
PROFILES - CONFIGURATION
• Device/Port Selection Screen
• Add/Remove Switches - From the list of switches, select those you want to analyze. 
• Add/Remove Ports - Select a switch and click on the Add/Remove Ports button. From the list of 
ports, select the port(s) that you want to analyze. 
• Note: A switch can only be in one profile of a particular Profile Type.

<<<PAGE 343>>>
STATISTICS
• Collect and view statistics for devices throughout the network.
•
All managed switches are automatically included in a Default Statistics Collection Profile
•
You can then view statistics by creating View Profiles containing the switches and statistics 
attributes you want to view

<<<PAGE 344>>>
STATISTICS – DEFAULT COLLECTION PROFILE
• The statistics attributes collected in the Default Profile can be configured as well as the 
polling interval and data retention period

<<<PAGE 345>>>
STATISTICS – VIEW PROFILE
• Go to Statistics – Chart View and create a View Profile containing the switches and 
attributes you want to display

<<<PAGE 346>>>
STATISTICS – DISPLAY DATA
• Select the Profile and click the View Statistics button to display the data

<<<PAGE 347>>>
DASHBOARD – PERFORMANCE MONITORING
• Statistics can be shown directly from the Dashboard by selecting the Performance 
Monitoring tab and adding a Chart View Profile

<<<PAGE 348>>>
SUMMARY VIEW
• Displays basic information for all discovered network switches,
• Including any Analytics Profiles to which a switch may belong.
Name - User-configured switch name.
Address - IP address of the switch.
Location - User-configured switch location (if no location was 
configured by the user, the field will display "Unknown").
MAC Address - MAC address of the switch
Version - Switch AOS version.
Type - Switch type (e.g., OS10K, OS6900-X20).

<<<PAGE 349>>>
APPLICATIONS MANAGEMENT
• When generating a Top N Applications Report, the Analytics application uses port numbers 
to identify application traffic. 
• Traffic on a specific port is identified as coming from a specific application.
• The Application Management Screen is used to create, edit, and delete application/port 
mapping.
• Well known ports (e.g., 161 for SNMP, 80 for HTTP) are automatically mapped.

<<<PAGE 350>>>
APPLICATIONS MANAGEMENT - MODES
• Mapping is done by choosing one of the two available modes:
• Range-Based - This mode is used to set a range of ports that are monitored by the Analytics 
application. 
• Traffic on these ports is monitored and can be displayed in the Top N Applications Report. 
• Information for all of these ports is available to be displayed
• Only those ports that have been mapped will be labeled with the application. 
• Other ports will be labeled as "Unknown". 
• Enumerated - This mode requires that you define specific ports to be monitored. 
• Only those ports you define when you create a mapping will be monitored.

<<<PAGE 351>>>
APPLICATIONS MANAGEMENT - CONFIGURATION
• Click on the Create icon and complete the fields as described below:
• Application Name - Enter the name of the application (e.g., SNMP) .
• Ports - Enter the port or port range to be associated with the application. If you are entering a 
range of ports, separate the port numbers with a "-" (e.g., 20-21).
• An existing application ports mapping file (.json file) can be imported into OmniVista 2500 
NMS.
• Note that this new mapping will override the existing mapping.

<<<PAGE 352>>>
REPORT

<<<PAGE 353>>>
REPORT - CONFIGURATION
• This Application creates and schedules Analytics 
Reports that can be viewed and stored as PDF 
documents.
• Includes:
• Information from specific Analytics Reports (e.g., 
Top N Users, Top N Apps) 
• Specific views of that report (e.g., Summary View, 
Detailed View). 
• A report is generated at specific times/intervals 
(e.g., Daily, Weekly). 
• When it is generated, it takes a current snapshot of 
the Analytics information you specified
Create Report

<<<PAGE 354>>>
REPORT - CONFIGURATION
• A report is created in two steps:
1) In the Report Configuration screen, click on the Create icon and complete the fields as 
described below:
• Report Title 
• Schedule Settings
• Purging Policy – The report will be removed from the server at the selected interval. Select "None" to never 
purge the report.
• Schedule – "Now” generates the report immediately. 
“Periodically” creates the report at specific times/intervals.
- "Simple” schedules the report generation every "x" number of days, hours,  
minutes, seconds (e.g., every 5 days, every 5 minutes). 
- "Cron” schedules the report generation as a cron job (e.g., every minute, 
every hour, every year).
• Other Settings - Optional report parameters (e.g., page size, orientation).

<<<PAGE 355>>>
REPORT
CONFIGURATION

<<<PAGE 356>>>
REPORT - CONFIGURATION
2) In the Analytics Application, go to the report that you want to include (e.g. Alarms). In 
the upper right corner of the screen, click on the Export icon and select Add to Report. 
▪
On the Add to Report Window, select the Report from the Report Configuration drop-down list 
and click OK. 
▪
You can open different views (e.g., Summary View, Detailed View) and repeat the 
procedure to include those views in the report.

<<<PAGE 357>>>
REPORT - LIST
• Displays all generated reports. 
• To download/view a report in PDF format, select the report and click on the Download 
button.
• To delete a report(s), select the report(s) and click on the Delete icon , then click OK at 
the confirmation prompt.

<<<PAGE 358>>>
APPLICATION VISIBILITY

<<<PAGE 359>>>
APPLICATION VISIBILITY - DEVICES MANAGEMENT
• Displays all network switches that support Application Visibility. 
• Name, IP address, and operational status of each switch, 
• Indicates whether an Application Visibility Profile has been assigned to the switch.

<<<PAGE 360>>>
APPLICATION VISIBILITY - SIGNATURE FILES
• A Signature File contains application signature information that is used to create Signature 
Profiles.

<<<PAGE 361>>>
APPLICATION VISIBILITY - SIGNATURE PROFILE CREATION

<<<PAGE 362>>>
APPLICATION VISIBILITY - SIGNATURE PROFILE CREATION
• Select one of the predefined groups or a custom application group can be configured
• Two different types of groups can be created:
• Monitor Flow Count: Used for the Analytics Reports
• Bandwidth Usage and Enforcement: used for the QoS and Access Role applications

<<<PAGE 363>>>
APPLICATION VISIBILITY - SIGNATURE PROFILE ASSIGNMENT
• After the profile is created, it has to be assigned to the switches and its ports.

<<<PAGE 364>>>
APPLICATION VISIBILITY
DISPLAYING APPLICATION REPORTS
• In the Analytics screen, select Top N Applications – Advanced to display the reports
• Click on any application to display
the switch that is identifying the flows

<<<PAGE 365>>>
APPLICATION VISIBILITY - POLICIES
• These policies are treated like regular policies, only the policy condition is set to the 
enforcement group that was configured during the Signature Profile creation

<<<PAGE 366>>>
APPLICATION VISIBILITY - QOS ENFORCEMENT
• The Policy has to be included in a Policy List.
• Then, the Policy List is included as part of the Access Role Profile configuration

<<<PAGE 367>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 368>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniVista 2500 NMS R4 
Network Analytics and Application Visibility 
Contents 
1 
Basic Network Diagram ....................................................................... 2 
2 
Configuring Application Visibility for OS6860N............................................ 3 
2.1. Procedure steps in Omnivista ..................................................................... 4 
2.2. Check the managed devices ...................................................................... 4 
2.3. Configure Signature files .......................................................................... 5 
2.4. Configure Signature profiles ...................................................................... 6 
2.4.1. Create a signature profile for OS6860-B................................................................. 6 
2.4.2. Verifying the Operations .................................................................................. 9 
2.4.3. Check signature profiles assignment ................................................................... 11 
2.4.4. Check OV2500 Logging files ............................................................................. 11 
3 
Using the Application Visibility reports .................................................. 12 
3.1. From Network Analytics application ............................................................ 12 
3.2. From OV2500 Dashboard Web page ............................................................. 13 
3.3. Traffic generation ................................................................................. 15 
4 
Setting up OmniVista 2500 Network Analytics .......................................... 17 
4.1. Analytics profile creation ........................................................................ 17 
4.1.1. Create an Analytics report profile for Top N Apps & Clients ....................................... 17 
4.1.2. Create an Analytics report profile for Top N Clients ................................................ 18 
4.2. Report visualization ............................................................................... 19 
4.2.1. From Network Analytics application ................................................................... 19 
4.2.2. From OV2500 Dashboard Web page .................................................................... 21 
5 
Statistics ...................................................................................... 23 
5.1. Edit the default collection profile .............................................................. 23 
5.2. Displaying the Statistics .......................................................................... 24 
5.2.1. Display of the view profile on the OV2500 home page .............................................. 26

<<<PAGE 369>>>
2 
Network Analytics and Application Visibility 
 
 1 
Basic Network Diagram 
In this topology, the VLAN 100 will be as management network that includes the servers OmniVista 2500 and 
AAA server (DHCP, Radius, NTP, ...) 
All clients will have to be set with dynamic IP address and will have access to internal network as well as 
Internet for accurate test.

<<<PAGE 370>>>
3 
Network Analytics and Application Visibility 
 
 2 
Configuring Application Visibility for OS6860N 
 
- 
User VLAN creation 
 
- Setup a vlan for users on following switches 
Switch 1 
vlan 10 
vlan 10 members port 1/1/1 untagged 
ip interface vlan10 address 192.168.10.1/24 vlan 10 
 
Switch 2 
vlan 20 
vlan 20 members port 1/1/1 untagged 
ip interface vlan20 address 192.168.20.2/24 vlan 20 
 
Switch 7 
vlan 70 
vlan 70 members port 1/1/1 untagged 
ip interface vlan70 address 192.168.70.7/24 vlan 70 
 
Switch 8 
vlan 80 
vlan 80 members port 1/1/1 untagged 
ip interface vlan80 address 192.168.80.8/24 vlan 80 
 
Application Visibility is responsible for monitoring the applications running the network and reporting it to a 
centralized OmniVista NMS system. 
Application Visibility identifies application/protocol flows based on Signatures Files  that identify an associated 
application or protocol. It supports monitoring and QoS/UNP configuration of Application traffic flows, and 
performs statistics profiling on the collected data. 
Application Visibility is supported on OS6860E/N (AOS 8.2.1.R01 and later) and OS6870 Switches as well as 
Virtual chassis of OS6860/OS6860E Switches where at least one OS6860E is present. 
Typical enterprise deployment topology of OS6860E/N and OS6870 
- Positioning at the Edge (AppMon Monitoring/Enforcement) 
- Positioning at Aggregation (AppMon Monitoring) 
 
In this exercise, we will configure the access switch OS6860-B to support Application Visibility for monitoring 
some applications and to enforce policies for specific traffic. 
 
 
Before proceeding, open a console session to client 8 VM and make sure it receives an IP address and also test 
internet access. 
 
In client 8 VM, open a web browser and navigate to facebook. We will use it to demonstrate application visibility  
 
 
Notes: DO NOT login to facebook and DO NOT add any personal information. Just 
make sure that the main page is displayed.

<<<PAGE 371>>>
4 
Network Analytics and Application Visibility 
 
 
 
You can close the browser for now, after making sure that the internet access is successful 
 
2.1. 
Procedure steps in Omnivista 
 
 
 
Notes: Refer to the Help documentation by clicking on icon 
 along with all the 
web pages. 
 
2.2. 
Check the managed devices 
 
Go to Top-level menu bar 
Network 
Application Visibility 
Devices Management 
 
Verify the network switches that support Application Visibility and that no Application Visibility Profile has 
been assigned to the device 
 
You should view the OS6860 with no profiles assigned.

<<<PAGE 372>>>
5 
Network Analytics and Application Visibility 
 
 
2.3. 
Configure Signature files 
 
A Signature File contains application signature information that is used to create Signature Profiles. 
A signature profile can be assigned to one or more switches. So, a Signature Profile essentially allows 
different configurations of app-groups and app-names from the same signature file to be downloaded on 
different switches. Second, it gives a snapshot of applications available on the switches to which it’s 
assigned.  
 
 
Notes: A switch can be assigned only to one Signature Profile 
 
OS6860E/N Switches support the Signature File Auto-Update Feature. If Signature File "Auto Update" is 
enabled on a switch when OmniVista imports a new Signature File that is included in a Signature Profile 
that has been applied to a switch, OmniVista automatically clone updates the profile, and assigns the 
updated profile to switches. 
 
Go to Top-level menu bar 
Network 
Application Visibility 
Signature Files 
 
You should see one or more signature files ready to use. The AppSig.upgrade_kit_3 is intended for the 
OS6860. 
 
 
 
 
 
Notes: OmniVista automatically checks the ALE Signature File Repository and updates and 
downloads Signature Files for OS6860(E)(N) Switches and Stellar APs. There should be no need to 
import these Signature Files into OmniVista. If necessary, you can perform a manual upload by 
going to the Application Visibility Settings Screen and clicking on the Update Now button. 
 
You can now use the Signature File to create a Signature Profile

<<<PAGE 373>>>
6 
Network Analytics and Application Visibility 
 
2.4. 
Configure Signature profiles 
 
The Signature Profiles Screen displays all configured Signature Profiles. Click on a profile to display 
detailed profile information. 
 
A profile contains the following information: 
Profile Name - The user-configured name for the profile.  
Description - A user-configured description for the profile.  
File Name - The name of the Signature File used in the profile.  
Applications - Lists the applications included in the profile. 
Application Groups - Lists the application groups included in the profile. 
Devices - Lists the switches to which the profile has been assigned.  
AP Groups - Lists the AP Groups to which the profile has been assigned. 
 
 The four steps to create a profile for monitoring and enforcement are as follow: 
 
 
 
 
Notes: For signature profile creation, user is offered to create Application Monitoring (AppMon) 
and Application Enforcement Groups and/or apps separately. 
For Security policies, AppMon Enforcement functionality can be enabled on any OS6860/E element 
of the network for enforcing policy actions such as dropping and rate limiting. 
 
 
 
Notes: The wizard guides you through creating a Signature Profile containing both monitoring 
groups and enforcement groups. You can create monitoring groups only, without creating 
enforcement groups.  
However, to configure enforcement, you must configure an enforcement group in the wizard. For 
enforcement, you then create an Application Visibility Policy List that you use to configure an 
Access Role Profile. 
 
2.4.1. 
Create a signature profile for OS6860-B 
 
Go to Top-level menu bar 
Network 
Application Visibility 
Signature Profiles 
+ (create)  
Name “OS6860_Profile” 
Next 
Select Signature File “AppSig.upgrade_kit” 
Next 
 
The next step is to associate an Application Group for Monitoring to the Signature Profile

<<<PAGE 374>>>
7 
Network Analytics and Application Visibility 
 
 
Under Select Groups/Apps – Monitor Flow Count  
Groups 
Create App Group (click on the three dots on the right) 
  
Enter the App Group Name “MyApps” and add a Description. 
Select Groups then search for applications to monitor and use the + or - buttons to select the 
applications you want to include in the group. 
In this example, we will choose some social media and gaming applications. Search for the following 
applications and add them with the “>>” button: 
 
 
Facebook 
Twitter 
youtube 
bet365 
 
 
 
 
Click on Create and then Next  
 
Now you will associate an Application Group for Enforcement to the Signature Profile. 
 
 
Creating an Enforcement Group allows the administrator to assign QoS/UNP Policies to 
the traffic. It is up to the administrator to choose which type of traffic (or application) 
can be assigned to a policy. 
Administrator can also associate QoS policies with UNP profile and provide user level 
policy treatment. 
 
In this example to demonstrate the Application Enforcement, you will set the following rule: 
- Traffic for the social media and gaming application selected in the previous step will be blocked. 
 
Limitations and constraints are stricter in a live environment, but we will limit to this rule for the 
purpose of demonstration.  
 
Under Groups/Apps – Bandwidth Usage and Enforcement  
Groups 
Choose App Group (click on the three dots on the right) 
 
Select the MyApps group from the Choose App Groups using the + button. 
Click Ok. 
Once selected, click on N/A link in the ACL/QoS field under MyApps group 
 
 
Enter ACL/QOS values as follow:

<<<PAGE 375>>>
8 
Network Analytics and Application Visibility 
 
Check the Disposition box  
Set Accesibility: DROP 
Do not modifiy the other parameters 
Click Ok 
 
 
 
 
Notes: An administrator can assign an Access Role for traffic enforcement by clicking on 
N/A after Access Role Profile. The Access role will give more advanced option to fine-
tune specific traffic.  
An Access role must be initially setup through Unified Access -> Unified Profile -> 
Access Role Profile 
 
Click on Create Profile 
 
 Your Signature Profile should appear in the Signature Profile main page. 
 
 
 
You can now assign the profile to switches to monitor/control application traffic on the network. 
 
 
For our exercise, we will apply the profile “OS6860_Profile” to the switch 6860-B (switch 8) and assign ports 1 
and 5. 
 
Go to Signature Profiles Menu 
Select “OS6860-Profile” 
Apply to Devices 
Devices Selection 
 Add (select switches) 
 Use Switch Picker 
 
Device Selection 
 
192.168.200.8 (6860-B) 
 
Add(+) 
 
OK 
 
192.168.200.8  
 
Add Port 
 
Select (1/1/1, 1/1/5)

<<<PAGE 376>>>
9 
Network Analytics and Application Visibility 
 
 
OK 
 
Apply 
 
 
Notes: Port 1/1/1 is the port connecting the client 8 VM to Switch 8 where the user 
traffic will be monitored as well as port 1/1/5 for aggregated traffic to the core. 
 
 
Notes: A Check Service Stats warning message may appear. Click Ok if prompted. 
 
 
The progress is displayed on the Action Results Screen. Verify that the Profile was applied correctly to the 
OmniSwitch and click OK to return to the Signature Profiles Screen.  
 
 
 
2.4.2. 
Verifying the Operations 
 
- At the switch level, a log is generated  
Open a console session to the 6860B 
 
 
Wed Dec 24 23:01:17 : vc_licManager licMgr info message: 
+++ [1419458477.297727] lic_install_afn called 
+++ [1419458477.297808]  <<Virtual-Chassis license installation>> 
+++ [1419458477.406654] build_afn_map AFN license info validation successful. 
+++ [1419458477.406944]  program local chassis license, vc_id 1 
 
Wed Dec 24 23:01:23 : APPMON_CMM main info message: 
+++ [1419458483.663440] Kit update complete 
 
 
- The next step is to check the QOS/ACL configured for enforcement during creation of Signature Profile 
 
- Go to Configuration > PolicyView > Users and Groups > Unified Policies 
 
 
Notes: A QoS Policy was automatically created by OV. It should include the MyApps name 
on it which is the name of the application group created previously. 
- Select this policy and review its parameters.

<<<PAGE 377>>>
10 
Network Analytics and Application Visibility 
 
 
 
- Check the switch configuration: 
 
CLI Useful commands 
show app-mon config 
show app-mon port <port_number> 
show app-mon app-list [monitor| enforcement] active 
show app-mon ipv4-flow-table [monitor| enforcement] 
show app-mon ipv6-flow-table [monitor| enforcement] 
show app-mon app-record current-hour 
show app-mon app-record twenty-four-hours 
show app-mon app-record hourly 
show configuration snapshot app-monitoring 
 
Display global AppMon configuration 
-> show app-mon config 
Admin State                            : Enable, 
Operational State                      : Enable, 
Separate Config File Status            : Yes, 
Enforcement Mode                       : IPV4-IPV6, 
Enforcement Flow-Sync Interval         : 60 seconds, 
Monitor Logging Threshold              : 7000, 
Enforcement Logging Threshold          : 7000, 
App-Pool Applications                  : 2849, 
Monitor Applied Applications           : 4, 
Enforcement Applied Applications       : 4, 
Upgraded Signature File Type           : Production, 
AOS Compatible Signature Kit Version   : 1, 
Signature Kit version                  : 3.9.6 
 
Display QOS policy created by OV2500 
-> show policy rule 
Rule name                        : G_DL_MyAppsDR 
  From                           = ldap, 
  Precedence                     = 30001, 
  Condition name                 = G_DL_MyAppsDRC, 
  Action name                    = G_DL_MyAppsDRA, 
  Log                            = Yes, 
  Validity period name           = AllTheTime 
 
 
Display a list of applications and application groups added for monitoring 
-> show app-mon app-list monitor 
 
Legend: Application-name: *= Not present in recently updated kit, 
 
App-Id      Application-List                                                    Application-List 
AppGrp-Id   Member Name                                                         MemberType 
-----------+-------------------------------------------------------------------+--------------------- 
1           MyApps                                                              APP-GRP

<<<PAGE 378>>>
11 
Network Analytics and Application Visibility 
 
 
 
Display a list of applications and application groups added forenforcement 
-> show app-mon app-list enforcement 
 
Legend: Application-name: *= Not present in recently updated kit, 
 
App-Id      Application-List                                                    Application-List 
AppGrp-Id   Member Name                                                         MemberType 
-----------+-------------------------------------------------------------------+--------------------- 
1           MyApps                                                              APP-GRP 
 
 
2.4.3. 
Check signature profiles assignment 
 
Go to Top-level menu bar 
Network 
Application Visibility 
Summary View 
 
 
 
Go to Top-level menu bar 
Network 
Application Visibility 
Devices Management 
 
Indicates whether an Application Visibility Profile has been assigned to the switch 8. 
 
 
 
 
2.4.4. 
Check OV2500 Logging files 
 
Go to Top-level menu bar 
Administration 
Audit  
Audit Log View Home 
    Network 
Check the different av logs

<<<PAGE 379>>>
12 
Network Analytics and Application Visibility 
 
 3 
Using the Application Visibility reports 
 
There are two ways to display the reports: From landing page or from Network Analytics application 
3.1. 
From Network Analytics application 
 
Verify data from Analytics Report 
Go to Top-level menu bar 
Network 
Analytics 
Reports 
Top N Applications - Advanced 
App Flow Count or App Bandwidth Usage (type of display) 
For All Managed Devices  
 
 
 
From here, you have the option to select the information you want to display for each switch type. 
App Flow Count: Displays information for all applications discovered on the network in the last week. 
App Bandwidth Usage: Displays packet/byte count information for specific applications discovered on the 
network over a configured period of time. 
 
- Click  
App Flow Count 
Manually Select devices

<<<PAGE 380>>>
13 
Network Analytics and Application Visibility 
 
- Click on the Select Device button. The Device Selection screen appears.  
- Select the switch 6860-B(192.168.200.8) from the list using the Add> button and click Ok. The switch has 
already been assigned to a signature profile as mentioned in the previous steps. 
 
 
 
At this point, you should see a “NO DATA AVAILABLE” warning. The main reason is that no traffic has been 
already generated from the client 8. In addition, the “App Discovery” will only display the traffic captured after 
the generation of the internet traffic (google, facebook,twitter, office365, …). 
 
You can come back later during the training to check the output from these widgets. 
 
3.2. 
From OV2500 Dashboard Web page 
 
In the OV Dashboard, select the appropriate widgets to give a quick view of the analytics data observed by the 
Application visibility application.  
 
 
 
Click on the       icon on the top right of the window -> Add Widget 
 
 
 
 
 
 
Then select all the Application Analytics - Layer 7 report types suggested:

<<<PAGE 381>>>
14 
Network Analytics and Application Visibility 
 
 
 
Application Flow Count OS6860/Aps 
Displays traffic flow information for Apps/App Groups discovered on the network, and the percentage of network 
resources being used by each application for the selected devices and configured time period. 
 
Application Bandwidth Usage Summary / Detail View 
Displays packet/byte count information for Apps/App Groups discovered on the network, and the percentage of 
network resources being used by each application for the selected devices and configured time period.  
 
Application Bandwidth Usage – UNPs Summary / Detail View 
Displays packet/byte count information for Apps/App Groups discovered on the network over the configured 
period of time, and the percentage of network resources being used by each application by UNP.  
 
You should get your new widgets placed on OV2500 dashboard page as follow: 
 
 
 
 
 
Notes: By clicking on Config, you can configure the amount and type of information 
displayed (e.g., the number of applications displayed, byte or packet information) as 
well as the time interval that you want to view. 
By clicking on More, you will be redirected to Network Analytics report view.

<<<PAGE 382>>>
15 
Network Analytics and Application Visibility 
 
3.3. 
Traffic generation 
 
- Scenario: Company wants to restrict users to access social media and gaming websites from the company 
devices 
 
 
 
Notes: Make sure the IP address of the network connection is assigned dynamically using 
DHCP in client 8 VM 
 
o 
In the previous section, Application Enforcement has been applied. You have checked that the 
associated QoS policy was generated in Omnivista and also that the app-mon group was added to 
the switch. 
o 
Open a console session to client 8 VM 
o 
Open a web browser and navigate to facebook.com 
o 
You should see that now your access is blocked 
o 
Navigate to another webpage and you should see that access is allowed normally. 
 
o 
In Omnivista, go to Network > Analytics > Reports > Top N Applications – Advanced. 
o 
You should that flows associated with facebook are registered by Omnivista.  
o 
However, as the Application Enforcement QoS policy was created to restrict this access, then 
the client is not allowed to access this webpage. 
o 
Wait for 15-20 minutes before the applications are displayed in the OV widgets. 
 
 
 
 
 
On the 6860-B CLI interface run the following commands: 
-> show app-mon ipv4-flow-table monitor 
-> show app-mon ipv4-flow-table enforcement verbose 
-> show app-mon app-record hourly 
 
Display the flow table for IPv4 flows entries for monitor flows 
-> show app-mon ipv4-flow-table monitor 
SrcIP               DestIP        SrcPort     DestPort    Proto     App Name          App Group 
---------------+---------------+-----------+-----------+---------+------------------+----------------- 
192.168.70.10    157.240.202.35   4654       443        TCP        facebook             MyApps 
192.168.70.10    157.240.202.1    4655       443        TCP        facebook             MyApps 
192.168.70.10    157.240.202.1    4656       443        TCP        facebook             MyApps 
192.168.70.10    157.240.202.35   4657       443        TCP        facebook             MyApps 
192.168.70.10    185.60.219.35    4658       443        TCP        facebook             MyApps 
192.168.70.10    157.240.202.35   4659       443        TCP        facebook             MyApps 
192.168.70.10    185.60.219.35    4665       443        TCP        facebook             MyApps 
192.168.70.10    157.240.202.35   4759       443        TCP        facebook             MyApps 
Number of Flows : 8 
 
 
Display the flow table for IPv4 flows entries for enforcement flows 
-> show app-mon ipv4-flow-table enforcement verbose

<<<PAGE 383>>>
16 
Network Analytics and Application Visibility 
 
Legend: start/date/time/zone  duration 
SrcIp           DestIP          SrcPort   DestPort  Protocol  Application-name 
App-group                       Policy rule                     Packet Count    Byte Count, 
---------------------------------------------------------------------------------------------------------- 
2024-09-16/22:28:16/UTC     0d 0h 7m 8s 
192.168.70.10    157.240.202.35   4759       443        TCP        facebook 
MyApps                           G_DL_MyAppsDR                    41               16061 
Number of Flows : 1 
 
Display current-hour application-record information as well the historic application-records on the hourly or 24-hours 
basis for monitored applications 
-> show app-mon app-record hourly 
Sampling Interval Every 5-minutes 
                           Application                                   Application group         Total Detected Flows 
----------------------------------------------------------------+--------------------------------+-------- 
2024-09-16 19:00:00 UTC 0d 01h 00m 00s 
facebook                                                         MyApps                           7                       
-------------------------------- 
-------------------------------- 
Number of Applications: 1

<<<PAGE 384>>>
17 
Network Analytics and Application Visibility 
 
 4 
Setting up OmniVista 2500 Network Analytics 
 
The Analytics Application provides: 
- A comprehensive view of network resource utilization, including views of users, devices, and applications.  
- Information on usage trends, including predictive analysis of future network resource utilization.  
- Real-time viewing of Analytics Reports 
 
It enables users to create different reports (e.g., Top N Applications, Top N Ports Utilization) that provide a 
comprehensive view of network and device utilization. 
In addition, it allows the administrator to configure how the information is displayed. 
 
Network Analytics reporting is supported on all AOS OmniSwitch models. 
 
The first step in generating analytics information for Top N Applications, Top N Clients, and Top N Ports 
Utilization Reports is to go to the Profiles Screen and create an Analytics Profile. 
In default, OmniVista shall not collect data of any switch. User need to specify which switch & which report they 
want to see. To do that, administrators need to create a profile in Profiles page. 
One switch can ONLY be in one profile of a particular profile type. 
  
Analytics information is gathered by creating an Analytics Profile that specifies the information to be viewed 
(e.g., Top N Applications, Top N Ports Utilization) and the network switches/ports that will be monitored. 
Reports will generate data only for those switches/ports included in a profile. 
 
4.1. 
Analytics profile creation 
 
 
4.1.1. 
Create an Analytics report profile for Top N Apps & Clients  
 
Go to Top-level menu bar 
Network 
Analytics 
Profiles 
+ 
Profile Name: TopN Apps&Clients POD# 
Profile Type: Top N Apps & Clients 
Next 
Device/Port selection 
Add/remove switches 
Use Picker 
Select all switches 
 
OS6900-A

<<<PAGE 385>>>
18 
Network Analytics and Application Visibility 
 
 
Add Ports (1/1/2) 
 
OS6870-B 
 
Add Ports (1/1/1, 1/1/5) 
 
OS6870-A 
 
Add Ports (1/1/1, 1/1/3) 
 
OS6860-B 
 
Add Ports (1/1/1, 1/1/3) 
 
OS6360-A 
 
Add Ports (1/1/1) 
 
OS6360-B 
 
Add Ports (1/1/1) 
Create 
OK 
 
 
 
4.1.2. 
Create an Analytics report profile for Top N Clients  
 
Go to Top-level menu bar 
Network 
Analytics 
Profiles 
+ 
Profile Name: TopN Ports POD# 
Profile Type: Top N Ports Utilization 
Next 
Device/Port selection 
Add/remove switches 
Use Picker 
Select all switches 
 
OS6900-A 
 
Add Ports (1/1/2) 
 
OS6870-B 
 
Add Ports (1/1/1, 1/1/5) 
 
OS6870-A 
 
Add Ports (1/1/1, 1/1/3) 
 
OS6860-B 
 
Add Ports (1/1/1, 1/1/3) 
 
OS6360-A 
 
Add Ports (1/1/1) 
 
OS6360-B 
 
Add Ports (1/1/1)

<<<PAGE 386>>>
19 
Network Analytics and Application Visibility 
 
 
Create 
 
OK 
 
 
 
 
From now, the Analytics service is only collecting the sFlow packets that match this configuration. 
You should start to see first information displayed. 
 
4.2. 
Report visualization 
 
As seen in precedent exercises, the Analytics reports can be displayed from landing page or from 
Network Analytics Application Reports page. 
4.2.1. 
From Network Analytics application 
 
Verify data from Analytics Report 
Go to Top-level menu bar 
Network 
Analytics 
Reports 
 
 
 
 
The Analytics Top N Clients Report Screen displays information for the top network clients including the number 
of traffic flows for each client.

<<<PAGE 387>>>
20 
Network Analytics and Application Visibility 
 
 
 
 
 
Notes: Report Views and configuration options are configured using the Options Bar located at the 
top of the report. This help page contains view and configuration information specific to Top N 
Applications Reports. For specific information on all of the options available. 
 
 
The information can also be displayed in different formats, and you can also configure the amount of information displayed. 
Go to Top-level menu bar 
Reports 
Top N Clients 
 
 
 
The Analytics Top N Ports Utilization Report Screen displays the top network ports based on utilization. 
 
 
 
 
 
Notes: By default, all top switches/ports are displayed. However, you can click on the Select 
Devices button to display only information from specific switches.  
 
 
The information can also be displayed in different formats, and you can also configure the amount of information displayed. 
Go to Top-level menu bar 
Reports 
Top N Ports

<<<PAGE 388>>>
21 
Network Analytics and Application Visibility 
 
 
 
 
 
The Analytics Top N Application Report Screen displays information about the top applications being accessed on 
the network. This report type is automatically generated since a Top N profile exist. 
 
 
 
 
4.2.2. 
From OV2500 Dashboard Web page 
 
In the OV Landing page, select the appropriate widgets to give a quick view of the analytics 
data observed by the Application visibility application.  
 
Click on the       icon on the top right of the window -> Add Widget 
 
 
 
 
 
Then select some or all the report types suggested: 
  
 
 
 
 
 
 
You should get your new widgets placed on OV2500 dashboard page as follow:

<<<PAGE 389>>>
22 
Network Analytics and Application Visibility 
 
 
 
 
Notes: By clicking on Config, you can configure the amount and type of information displayed 
(e.g., the number of applications displayed, byte or packet information) as well as the time 
interval that you want to view. 
By clicking on More, you will be redirected to Network Analytics report view.  
 
 
Generate Web traffic from user Clients 1 to 8 and wait for a moment.   
 
 
 
 
After a couple of hours ...

<<<PAGE 390>>>
23 
Network Analytics and Application Visibility 
 
 5 
Statistics 
 
The Statistics application is used to display statistics for one or more equipment (s). 
 
 
 
 
5.1. 
 Edit the default collection profile 
 
By default, OmniVista 2500 collects information from all discovered switches and this is used to generate 
statistics. 
A profile, available by default, collects all the available information. It is also possible to create one or 
more profiles to select only certain information to collect. 
 
- Go to NETWORK > ANALYTICS > Statistics 
- Click on Collection in the left menu 
- Select the Default Profile 
- Click on the Edit button at the top right 
 
 
 
- Verify that all the attributes that can be collected are selected:

<<<PAGE 391>>>
24 
Network Analytics and Application Visibility 
 
 
 
- Click on Cancel to exit this page 
 
 
Notes > Profile Creation  
Only one profile can be assigned to an OmniSwitch. 
By default, the "Default Profile" statistics profile is assigned to all OmniSwitches. 
If you create a new profile, you will first have to unassign the "Default Profile" from the desired switches. 
 
 
 
5.2. 
Displaying the Statistics 
 
- Click on Statistics in the left menu 
- Then click on Selectors: 
 
 
 
o 
Attributes : Select the following attributes 
▪ 
Switch Health > Memory Utilization 
▪ 
Switch Health > CPU Utilization 
▪ 
Switch Health > Temperature 
▪ 
Ethernet Port > Port Rx Bytes 
▪ 
Ethernet Port > Port Tx Bytes 
▪ 
Click OK 
o 
Devices :  
▪ 
Click ADD 
▪ 
Select OS6860-B (192.168.200.8): 
o 
Counters : click ADD 
▪ 
Go to AVAILABLE COUNTERS

<<<PAGE 392>>>
25 
Network Analytics and Application Visibility 
 
▪ 
Select the following :  
• 
Switch Memory Utilization 
• 
Switch CPU Utilization 
• 
Port Rx Bytes (port 1/1/1) 
• 
Port Tx Bytes (port 1/1/1) 
• 
Port Rx Bytes (port 1/1/5) 
• 
Port Tx Bytes (port 1/1/5) 
• 
Click Add Counters To Selection 
 
 
 
 
 
Notes > View Profile 
The Choose a View Profile option allows you to create a view profile allowing the upstream configuration of 
switches and counters deemed to be of interest. For more information, please refer to the dedicated part in 
the appendix of this exercise. 
 
- Click on the View button to display the statistics in the form of a graph 
 
 
 
- To display the information in the form of a table, click on the View Table button

<<<PAGE 393>>>
26 
Network Analytics and Application Visibility 
 
 
 
 
Notes > Additional configuration 
A larger share of CPU is used on equipment by protocols such as routing protocols as well as 
memory for the routing table. 
 
 
- Finally, click on the Save Selection As… button to save this view 
o 
Click on Save As New… 
o 
Profile Name: My_View_Profile 
o 
Refresh Interval: 2 minutes 
o 
 Click on the Create button 
 
 
Notes > Summary View 
Once configured, it is possible to view the name of the profile assigned to each switch from the 
Summary View menu> Chart Views column, available in the left menu of the ANALYTICS 
application. 
 
 
5.2.1. 
Display of the view profile on the OV2500 home page 
 
A preview of the graph obtained using the My_View_Profile profile (created in the previous step) can be 
displayed on the OmniVista 2500 home page, using the widgets dedicated to the Analytics application. 
 
- Go to the home page by clicking on the Alcatel-Lucent Enterprise logo at the top left of the page. 
- Click on the Performance Monitoring tab. 
 
 
 
- Click on the Add Widget button 
o 
Name : My_View_Widget 
o 
Chart View Profile : My_View_Profile 
o 
Click Create

<<<PAGE 394>>>
27 
Network Analytics and Application Visibility 
 
- The graph now appears in the Performance Monitoring tab:

<<<PAGE 395>>>
INTERNET OF THINGS
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 396>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe IoT Device Profiling
• Describe IoT implementation in OmniVista
• Understand IoT Inventory and Category in 
OmniVista
• Learn how to create a new custom category

<<<PAGE 397>>>
IOT DEVICE PROFILING

<<<PAGE 398>>>
End Point MAC / IP
Status (Active / Offline)
End Point Category
...
IOT DEVICE PROFILING
•
OmniVista monitors network packets to track these devices and presents detailed 
information on the devices connected to AOS Switches and Stellar APs. 
OmniSwitch®
IoT Inventory
OmniVista 2500/Cirrus

<<<PAGE 399>>>
IOT INVENTORY DETAILS
• Endpoint MAC / IP - The MAC / IP Address of the 
device
• Status - The operational status of the device on the 
network. 
• Active - The device is currently active on the network. 
• Offline - The device is not currently active on the network. 
• Error - There was an error in retrieving status information. 
Status is unknown. 
• Category - The device category (e.g., Datacenter 
Appliance, Phone/Table/Wearable)
• Manufacturer - The device manufacturer.
• Switch/AP Name - The IP address of the switch/AP 
through which the device is connected to the network. 
• Port/ESSID - The switch port or ESSID through which 
the device is connected to the network. 
• Start / End Time - The time the device first accessed 
/ disconnected from the network. 
• Last Updated - The time the device information was 
last updated by OmniVista.

<<<PAGE 400>>>
IOT IMPLEMENTATION IN OMNIVISTA
•
To Identify an IoT device, OmniVista uses the following:
•
MAC OUI: allows devices to be recognized by identifying their MAC addresses. 
•
DHCP FingerPrinting: allows to track the devices on the network
•
It also helps in analyzing the future growth by accessing the trending information. 
OmniSwitch
Stellar AP
Endpoints
Endpoint 
Inventory
Enforcement 
Policy
Device Category
DATA 
COLLECTION
UNP 
ENFORCEMENT
PROFILING 
API
Device Profile
Services
Local Cache
Local Cache
OmniVista 2500/Cirrus
IoT Phase 1 
IoT Phase 2 
DHCP client request
DHCP option 55 (the parameter 
request list) 
and option 60 (the vendor 
identifier)
Or 
[Mac Vendors]

<<<PAGE 401>>>
IOT IMPLEMENTATION IN OMNIVISTA 
Collect from End Points
Profile & Inventory
Analytics Summary
Enforcement
IoT devices
End Points
OmniVista 2500/
OmniVista Cirrus
• Global Parameters Setting
• Devices & Access Points data collection
• Device Profile Services Consumption (requests etc..)
• End Point inventory capture
• End Point (Mac & IP address) -> Who?
• Network Context (where the End point connected)-> Where?
• End Point Nature (Profiling results)-> What?
• End Point Profiling
• DP Services to OmniVista for Unknown device type
• Local cache Profile available
• Default Category from DP Services & Custom device category
• Analytics Summary from Inventory (Widgets summary)
• Historical & Cumulative View
• Uptime & Downtime
• Device Category Breakdown
• UNP Profile definition
• UNP assignment based on Device category/ Profiling
• Manual UNP assigment

<<<PAGE 402>>>
CONFIGURATION

<<<PAGE 403>>>
IOT DASHBOARD
•
Category
•
Endpoint Name
•
SSID
•
UNP
•
Status
•
AP/Switch that the device 
is connected to
New Apps that display IoT devices by:

<<<PAGE 404>>>
INITIAL CONFIGURATION
•
IoT is enabled for switches and APs in the Managed Devices List
•
Select the devices on which you want to enable IoT and click on the Enable IoT button at the 
top of the list. 
Note: IoT is supported 
on IPv4 devices only.

<<<PAGE 405>>>
IOT INVENTORY
•
Provides detailed information on all endpoint devices that connect to the network 
•
New endpoint association or disassociation (Status) is updated in real-time 
•
Any changes to the endpoint (e.g., profile change, IP address change) are updated every 5 
minutes for devices connected to Stellar APs and every 15 minutes for devices connected to AOS 
Switches 
User can export 
the IoT inventory 
contents to an .xls
file

<<<PAGE 406>>>
IOT INVENTORY
• IoT can be configured to integrate with Google G Suite to collect device information and 
provide network security for Chrome devices.
• IoT can also be used to enable/disable and monitor Zigbee devices. OmniVista interfaces 
with a Zigbee Server and Stellar APs to provide Zigbee device support.

<<<PAGE 407>>>
IOT CATEGORY
•
Displays information about device categories
•
OmniVista monitors network packets to determine the types of devices connected to the 
network and categorizes them based on the list of categories. 
•
Default categories cannot be modified, but custom categories can be added

<<<PAGE 408>>>
IOT ENFORCEMENT
• Configures category-based device authentication
•
By associating a Category with an Access Role Profile
•
You can also specify exceptions for specific devices by SSID, MAC address, AP Group, or IP 
address. When a device matching one of these exceptions is categorized, it will not be subject 
to IoT enforcement.

<<<PAGE 409>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 410>>>
TEMPLATE BASED PROVISIONING
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 411>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the Template Based Provisioning 
Application
• Understand the Deployment methods available

<<<PAGE 412>>>
PROVISIONING OVERVIEW

<<<PAGE 413>>>
TEMPLATE BASED PROVISIONING
•
Simple, secure and integrated solution to ease new branch or campus device rollouts.
•
It reduces the burden on enterprises by greatly simplifying the process of deploying new 
devices. 
•
A near zero-touch deployment experience.
•
Automated and centrally managed by OV
•
Predefined configuration templates can be pushed out as devices come online or when queried 
on behalf of devices
•
Configuration templates allow an administrator to define a template of CLI commands that can 
be used to consistently configure multiple network devices, reducing deployment time.
OmniVista 2500/
OmniVista Cirrus
Configuration
Templates
OmniSwitch®

<<<PAGE 414>>>
FACTORY-DEFAULT, BOOTSTRAPPED, PROVISIONED SWITCHES
Factory-default switch: Isolated and not operational.
Bootstrapped switch: Limited Connectivity, Ready 
for Provisioning. Not operational.
Mostly a temporary config and expected to be 
overwritten during the Provisioning phase. 
Provisioned switch: Ready for full 
function and management.
OV Provisioning Service
OV Server

<<<PAGE 415>>>
PROVISIONING WITHOUT CONNECTIVITY
•
OmniVista serves as the central Provisioning server. 
•
If there is NO connectivity to OV before bootstrap/provisioning of the switch, a Mobile App can 
be the middle-man (future release):
• To download a set of bootstrap configs from OV
• To push a bootstrap config to the switch to enable it to talk to OV for provisioning.
• Or to interact with OV on behalf of a switch, get the provisioning config and push it to the switch.
OmniVista 2500/Cirrus
OmniSwitch®
Mobile App®

<<<PAGE 416>>>
PROVISIONING WITHOUT CONNECTIVITY
• Recommended dongles for switch provisioning using mobile app
• SMK-Link Nano Dongle Bluetooth v4.0 LE+EDR
• Bluetooth Adapter for PC USB Bluetooth Dongle 4.0 EDR Receiver 
Wireless
• Warmstor Bluetooth Adapter, CSR 4.0 USB Dongle Bluetooth Receiver
• LSSEDA Bluetooth Adapter for PC, CSR 4.0 USB Bluetooth Dongle, 
Wireless Receiver

<<<PAGE 417>>>
PROVISIONING WITH CONNECTIVITY
•
If there is connectivity even before bootstrap, Switches can directly interact with OV
• In case of OVC, switches need connectivity to internet.
• In case of OVE, switches need connectivity to the OVE server in the Enterprise domain.
•
OV can also be used for configuration mgmt. of the switches even after Provisioning phase:
• To audit switch configurations periodically, 
• Allow operators to mark a configuration as “golden” configuration
• Alert operators when a switch deviates from its “golden” configuration 
• Enforce golden configurations (if required). 
OmniVista 2500/Cirrus
OmniSwitch®

<<<PAGE 418>>>
DEPLOYMENT SCENARIOS
• Basic DHCP Server. Only gives out IP Addresses. No DHCP options can be configured on the server, or no access is 
allowed to the server.
• Advanced DHCP Server: Gives out IP Addresses AND can be configured to send special DHCP options
• Mobile App: An app that can interface with one factory-default switch at a time, over a Serial interface to give it 
Bootstrap and/or Provisioning config. Available in future release
This App gets the configuration from OV, beforehand or online.
• RCD/RCL: The Remote Config Download framework includes the DHCP, TFTP, SFTP and OV Servers
Scenario#
OmniVista as the 
Provisioning Server
Basic DHCP 
server
Advanced 
DHCP server
Mobile
App
RCL
Use Case
1
Yes
Optional
Yes (Offline)
Remote installations with no 
3G/4G network
2
Yes
Optional
Yes (Online)
Remote installations with 
phone network
3
Yes
Yes
Yes
Enterprise/
Campus deployments
4
Yes
Yes
Enterprise/
Campus deployments
*Refer to the ‘If you want to know more’ section: 
Template Based Provisioning - Architecture and 
Configuration for additional information

<<<PAGE 419>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 420>>>
OMNIVISTA NETWORK ADVISOR
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 421>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe OmniVista Network Advisor (OVNA)
• Configure OVNA integration in OmniVista 2500 
NMS

<<<PAGE 422>>>
OMNIVISTA NETWORK ADVISOR - OVERVIEW
•
Detect anomalies and propose remediations
•
Real-time alerts with remediations
•
Rainbow bot or MS Team Chat
•
Serviceability
•
Manage anomalies
•
Manage remediations
•
Automatic logs collection
•
Easy set-up and configuration
•
Accountability : Reports and statistics
•
Alerts and decision reporting
OmniVista Network 
Advisor Edge Computing
OmniVista Network Advisor 
Cloud Processing & 
Orchestration
Customer premise
https
https
https
Server
Linux (Ubuntu)
Network Advisor 
Application
Network
devices
SSH
syslog
•
OS 6xxx and 9xxx models, AOS 8.7.R2 or Higher 
•
OS 6xxx and 2xxx models, AOS 5.2.R1 or Higher 
•
Stellar APs, AWOS 4.0.3 MR-3 or Higher

<<<PAGE 423>>>
OMNIVISTA NETWORK ADVISOR - OVERVIEW
• How does it work?
OmniVista
Network 
Advisor Edge 
Computing
(on premises)
OmniVista Network 
Advisor Cloud 
Processing & 
Orchestration
Network
devices
Customer
Send syslog
1
On pattern match, 
script is executed
SSH action scripted (if 
more infomation 
required)
2
2
HTTPs query
3
Rainbow notification
Customer Notification
4
5
5
Customer Interaction
5
Rainbow answer
6
https Response
Containing Interaction 
response
7
SSH action scripted
http Response Containing logs
Send syslog resulted of the action
8
9

<<<PAGE 424>>>
OMNIVISTA NETWORK ADVISOR ADD-ON CONFIGURATION
-
Obtain OVE API Key
-
Obtain OVNA UUID
-
Declare OVE instance in OVNA
-
Declare OVNA instance in OVE
-
Monitor devices in OVNA Rainbow bubble

<<<PAGE 425>>>
OBTAIN OMNIVISTA API KEY
•
In OmniVista, navigate to “Security > External Apps” to display available API Keys
•
Look for the API Key for OmniVista Network Advisor

<<<PAGE 426>>>
CONFIGURATIONS STEPS IN OV NETWORK ADVISOR
•
In OVNA, go to « Configuration > OmniVista Synchronization » and enable it.

<<<PAGE 427>>>
CONFIGURATIONS STEPS IN OVNA
•
Enter the different parameters required for the OV instance you want to monitor:
•
Server Type
•
OmniVista URL
•
API Key

<<<PAGE 428>>>
OBTAIN OVNA UUID
•
In OVNA, navigate to Dashboard and take note of the UUID

<<<PAGE 429>>>
CONFIGURATION STEPS IN OMNIVISTA
•
By default, OVNA support is disabled in the Managed Devices List

<<<PAGE 430>>>
CONFIGURATION STEPS IN OMNIVISTA
•
Select one or more devices in the catalog 
•
Navigate to the “Features” menu and select “Enable OmniVista Network Advisor”

<<<PAGE 431>>>
CONFIGURATION STEPS IN OMNIVISTA
•
Click on « Select » and « + Add New »
•
Enter a name for the OVNA instance, its IP address and UUID and click on « + »and then 
« OK »

<<<PAGE 432>>>
CONFIGURATION STEPS IN OMNIVISTA
•
You can then select the instance you just created and click on « OK »

<<<PAGE 433>>>
CONFIGURATION STEPS IN OMNIVISTA
•
Check the OmniVista Network Advisor status is « Enable » in the Device Catalog menu
•
Wait for the next synchronization period between OVNA and OmniVista (every hour)
•
Your devices should now appear in OVNA

<<<PAGE 434>>>
CHECK OVNA STATUS
•
Go to « Device Management », after a few minutes you should see your devices appearing
•
Reminder:
•
Switches / APs need to be configured including managment IP, syslog configuration and make 
sure that OVNA is reachable from these devices

<<<PAGE 435>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 436>>>
SIP SNOOPING
OMNIVISTA 2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 437>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe the following:
- SIP Application Overview
- Configuring Profiles
One Touch
SIP Profile
Global Parameters
SIP View
SIP Call Records

<<<PAGE 438>>>
OMNIVISTA SIP SNOOPING
• Detects SIP data packets 
• Configure SIP Profiles 
• Apply QoS parameters for SIP packets
• Monitor SIP traffic 
• Create traps to alert you to SIP events. 
• Identifies and marks SIP and its corresponding media 
streams. 
• Real Time Protocol (RTP)
• Real Time Control Protocol (RTCP) flows. 
• Marking is done using the DSCP field in the IP header. 
• Provides user configured QOS treatment for SIP/RTP/RTCP 
traffic flows based on its marking. 
• Calculates QOS metric values
• Delay, 
• Jitter, 
• Round trip time, 
• R factor and 
• MOS values of media streams 
SIP Server
SIP
WAN
External
RTP/RTCP flows
SIP signaling
SIP
SIP
SIP
SIP

<<<PAGE 439>>>
OMNIVISTA  SIP APPLICATION
• SIP Application 
• Creates SIP Snooping Profiles
• Loads Profiles on selected devices.   
• Receives device traps 
• Configure SIP Snooping Traps.
• Generates trap whenever Call Records file is renamed. 
• Gets renamed file from device, parse it and populate the data in its DB
• Other OmniVista Applications
• Discovery application locates SIP Ports and SIP snooping status during device discovery
• Statistics application displays SIP Snooping Statistics
• Update PolicyView application to support new SIP Snooping conditions and actions.

<<<PAGE 440>>>
SIP HOME

<<<PAGE 441>>>
SIP SNOOPING – ONE TOUCH
• Configures a global SIP Profile for all SIP enabled switches on the network. 
• OneTouch Media profiles
• Voice
• Video
• Other

<<<PAGE 442>>>
SIP SNOOPING – ONETOUCH MEDIA PROFILES
• Voice
•
Policy Condition - sip audio
•
Policy Action - dscp 46
•
Policy Rule - OneTouchSIPRule$Voice condition
•
OneTouchSIPCondition$Voice action
•
OneTouchSIPAction$Voice
• Video
•
Policy Condition - sip video
•
Policy Action - dscp 34
•
Policy Rule - OneTouchSIPRule$Video condition
•
OneTouchSIPCondition$Video action
•
OneTouchSIPAction$Video
• Other
•
Policy Condition - sip other
•
Policy Action - dscp 24
•
Policy Rule - OneTouchSIPRule$Other condition
•
OneTouchSIPCondition$Other action
•
OneTouchSIPAction$Other
•
One Touch SIP Voice Policy Precedence is fixed at 50000.
•
One Touch SIP Video Policy Precedence is fixed at 44000.
•
One Touch SIP Other Policy Precedence is fixed at 44001.

<<<PAGE 443>>>
SIP SNOOPING - SIP PROFILE
• A SIP Profile is a "Master" Profile  
• Global Params 
• Trusted Servers 
• Ports
• Threshold
• SOS

<<<PAGE 444>>>
GLOBAL PARAMETERS
• The Global Params Tab is used to configure global SIP Profile parameters and 
enable/disable SIP Snooping. 
• Global Parameter Profile can be included in a SIP Profile and assigned to switches/ports in 
the network.
• SIP Snooping Status 
• DSCP Number
• SOS Call DSCP No. 
• Threshold No. of Calls 
• Clear Stats

<<<PAGE 445>>>
OMNIVISTA - DEVICE VIEW
• The SIP View Tab is used to view SIP Profile configuration for any SIP-enabled switch in the 
network. 
• The View tab displays basic configuration information for each switch. 
• When you select a switch, SIP configuration information for that switch is displayed in the 
tabs at the bottom of the window (SIP Profile, Global Parameters, Trusted Servers , Ports, 
Threshold, SOS, SIP Statistics).

<<<PAGE 446>>>
OMNIVISTA SIP CALL RECORDS
• The Call Records Node in the SIP Application is used to view call record data for SIP-
enabled switches. 
• Display information for Active Calls or Ended Calls.

<<<PAGE 447>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 448>>>
TEMPLATE BASED PROVISIONING – ARCHITECTURES 
AND CONFIGURATION
OMNIVISTA
2500 NMS RELEASE 4
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 449>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the Deployment methods 
available
• Describe the Provisioning Rules screen
• Learn how to create a new Rule
• Understand the difference between static 
and dynamic templates
• Describe the Results screen

<<<PAGE 450>>>
DEPLOYMENT SCENARIOS

<<<PAGE 451>>>
DEPLOYMENT SCENARIOS
• Basic DHCP Server. Only gives out IP Addresses.
No DHCP options can be configured on the server or no access is allowed to the server.
• Advanced DHCP Server: Gives out IP Addresses AND can be configured to send special DHCP options
• Mobile App: An app that can interface with one factory-default switch at a time, over a Serial 
interface to give it Bootstrap and/or Provisioning config. Available in future release
• This App gets the configuration from OV, beforehand or online.
• RCD/RCL: The Remote Config Download framework includes the DHCP, TFTP, SFTP and OV Servers
Scenario#
OmniVista as the 
Provisioning Server
Basic
DHCP server
Advanced
DHCP server
Mobile App
RCL
Use Case
1
Yes
Optional
Yes (Offline)
Remote installations with no 3G/4G 
network
2
Yes
Optional
Yes (Online)
Remote installations with phone 
network
3
Yes
Yes
Yes
Enterprise/
Campus deployments
4
Yes
Yes
Enterprise/
Campus deployments

<<<PAGE 452>>>
SCENARIO 1: OV, MOBILE APP OFFLINE MODE,
OPTIONAL BASIC DHCP SERVER
Central OV Server
Mobile 
App
Network 
Administrator
Installer
Step #1
Set up config templates per 
SN#, Model Type, Location…
Step #2
Download config templates 
and Rules
Step #3
Connect with Mobile app to 
gather SN#, etc
Step#4
Operator input (optional)
Step #5
Push best matching config
to the Switch
Step#6
Switch is now managed by OV
Step #3
Step #4
Step #6
Local/Remote Switches
Optional Basic DHCP Server
Step #3
Public /Enterprise
Network

<<<PAGE 453>>>
SCENARIO#1: OV, MOBILE APP OFFLINE MODE, 
OPTIONAL BASIC DHCP SERVER
• Switches are in remote locations with no connectivity to OV
• Also no Mobile network connectivity for the Mobile App to OV 
• Hence Mobile App works in “Offline” mode.
• IP Address : Switch can get IP address using one of the following ways:
• A Basic DHCP server is reachable from ALL devices 
• Using the Mobile App, installer can give a Static IP Address to each switch
• OV is the Provisioning Server
• Operator has to set up the necessary config templates and rules on OV Template Based Provisioning 
• Mobile App could just push the Bootstrapping config to the switch and let OV do the 
provisioning or could push the Provisioning config to the switch.

<<<PAGE 454>>>
SCENARIO#2: OV, MOBILE APP ONLINE MODE,
OPTIONAL BASIC DHCP SERVER
Central OV Server
Mobile 
App
Network 
Administrator
Installer
Step #1
Set up config templates per 
SN#, Model Type, Location…
Step #2
Connect with Mobile app
to gather SN#, etc
Step #3
Operator input (optional)
Step#4
Query & get matching config 
template
Step #5
Operator input (optional),
Push configuration to the Switch
Step#6
Switch is now managed by OV
Step #2
Step #3, #5
Local/Remote Switches
Optional Basic DHCP Server
Step #2
Public /Enterprise
Network

<<<PAGE 455>>>
SCENARIO#2: OV, MOBILE APP ONLINE MODE, 
OPTIONAL BASIC DHCP SERVER
• Switches are in remote locations with no connectivity to OV 
• There is Mobile network connectivity for the Mobile App to OV
• Hence Mobile App can work in “Online” mode.
• IP Address : Switch can get IP address using one of the following ways:
• A Basic DHCP server is reachable from ALL devices 
• Using the Mobile App, installer can give a Static IP Address to each switch
• OV is the Provisioning Server
• Operator has set up the necessary config templates and rules on OV Template Based Provisioning 
• Mobile App would query OV live to get the best matching provisioning config and push it to 
the switch.

<<<PAGE 456>>>
MOBILE APP ENHANCEMENTS
• Mobile App is initially used to:
• Connect to the switch
• Provision / Display the configuration
• Latest version of the App can also be used to:
• Show switch health
• Show port information

<<<PAGE 457>>>
SCENARIO#3: OV, ADVANCED DHCP SERVER, RCL
• Customer has write access to DHCP server. 
• This DHCP server is reachable from ALL devices
• OV is reachable from ALL devices 
• RCL is the Bootstrap phase.
• OV could be the TFTP and/or SFTP
Server for the RCL phase.
• OV is also the Provisioning Server.
• Operator sets up config templates and rules on OV 
Template Based Provisioning
• Switches get managed by OV after the 
Provisioning phase
• No need for Mobile App.

<<<PAGE 458>>>
SCENARIO#4: OV, ADVANCED DHCP SERVER
• Customer has write access to DHCP server. 
• This DHCP server is reachable from ALL devices
• OV is the Provisioning Server. 
• Operator sets up config templates and rules on OV 
Template Based Provisioning
• No separate bootstrapping required
other than giving IP Address to 
the switches to enable them to talk
to the OV Provisioning server. 
• OV is reachable from ALL devices once they get their 
IP Address.
• Switches get managed by OV after the 
Provisioning phase
• No need for Mobile App.

<<<PAGE 459>>>
CONFIGURATION

<<<PAGE 460>>>
PREREQUISITES
• DCHP/DNS Configuration 
• Set up the DHCP Server to point to the local OmniVista Server as the Activation Server for 
provisioning - Option 43, Sub-Option 128 (recommended); 
• OR set up the DNS to resolve activation.myovcloud.com to point to the OmniVista Server. 
• Configure the Cloud Agent (Currently-Deployed Switches Only) 
• Modify the cloudagent.cfg File - Configure the "Activation Server URL" field in the cloudagent.cfg 
file to enter an FDQN in the following format: as-lite.*.ove.local. 
• Where * is the FDQN configured in the DNS Server for the OmniVista Server IP address. 
• Enable the Cloud Agent - Telnet to the switch and issue the following CLI command: 
• cloud-agent admin-state enable.

<<<PAGE 461>>>
RULES
• Rules can be created for specific switches (by serial number or MAC Address) or by switch 
model (e.g., OS6350-P10). 
• Once connected to the network, the switches will contact the OV server every 5 minutes
• If a switch matches a Rule, the Management and Configuration Templates in the Rule are pushed to 
the switch.

<<<PAGE 462>>>
CREATING A PROVISIONING RULE
• Serial Number/MAC - Enter either the switch serial number or MAC Address.
• Switch Model - Enter a specific switch model name 
• Switch Config Template - This Template will be pushed to any switch matching the Rule. 
• Configuration in this Template will be appended to the existing configuration file on the switch. 
• Value Mapping - If you create a dynamic Configuration Template, you must create Value 
Mappings for the variables in the template. 
• Mgmt Users Template -By default, the Default Management Users Template is pushed to the 
switch unless you select a different Management Template. 
• Save and Certify - Save the Configuration Template to the Certified Directory.

<<<PAGE 463>>>
CREATING A CONFIGURATION TEMPLATE
• A Configuration Template is created using CLI syntax. 
• Set of commands that are read by the switch on reloading. 
• Can be static or dynamic. 
• Static. Template without variables. It is useful for deployments where all switches can work with 
exactly same configurations. 
• Dynamic. Template with variables. It allows you to reuse the same Configuration Template even 
though different switches might need different values for some configurations 
Static
Dynamic
Template = 6860eTemplate
vlan 1 disable
vlan 100 members port 1/1-3 tagged
no ip interface dhcp-client
ip interface static-intf address 
192.168.1.10/24
vlan 100 
…
Template = 6860eTemplate
vlan 1 disable
vlan $VLAN members port $PORTS tagged
no ip interface dhcp-client
ip interface $INTERFACE_NAME address 
$STATIC_IP/24
vlan $VLAN
…

<<<PAGE 464>>>
INSTANTIATING A DYNAMIC CONFIGURATION TEMPLATE
6860eBranch1Vars
$VLAN
100
$PORTS
1/1-3
$INTERFACE_NAME
static-intf
$STATIC_IP
192.168.1.10
…
…
Configuration template
config derived from “6860eTemplate” and “6860eBranch1Vars”
vlan 1 disable
vlan 100 members port 1/1-3 tagged
no ip interface dhcp-client
ip interface static-intf address 192.168.1.10/24
vlan 100 
…
Value Mapping
Derived config that will 
be sent to the switch
Template = 6860eTemplate
vlan 1 disable
vlan $VLAN members port $PORTS tagged
no ip interface dhcp-client
ip interface $INTERFACE_NAME address $STATIC_IP/24
vlan $VLAN
…

<<<PAGE 465>>>
CONFIGURING THE DEFAULT MANAGEMENT TEMPLATE
• Applied to any switch that is successfully provisioned and enables OV management on the 
switch
• SNMP Settings. SNMP Version, Timeout, Retry Count 
• SNMP User Setup. Username, Password, SNMP Role
• Other Access Methods. CLI / FTP access

<<<PAGE 466>>>
RESULTS
• Displays information about all switches that have attempted provisioning
• Also used to configure a "Golden Configuration" for a switch 
• Also used to "Force Provision” a configuration to a device. 
• A switch may fail provisioning, or you may want to push a different configuration to a switch.
• The Force Provisioning Config button is used to push a Provisioning Rule configuration to a matching switch 
the next time the switch contacts the OmniVista server.

<<<PAGE 467>>>
GOLDEN CONFIGURATION
• Configuration selected from a list of the three most recent switch backups that can be 
applied to a switch in the event there is an unwanted configuration change. 
• Go to the "Golden Config" column for the switch in the Results Table and click Edit
• Select a Backup from the list and click Apply to set this backup as the Golden Configuration

<<<PAGE 468>>>
SETTINGS
• Configure onboarding process for switches that do not match a Provisioning Rule, and the 
Golden Template audit settings

<<<PAGE 469>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 470>>>
Datasheet 
Alcatel-Lucent OmniSwitch 2260
Alcatel-Lucent 
OmniSwitch 2260
WebSmart+ Gigabit Ethernet LAN Switch Family
The Alcatel-Lucent OmniSwitch® 
2260 Gigabit WebSmart family  
of switches provides a simple, 
secure, and smart business  
network at affordable prices.  
The Alcatel-Lucent OmniSwitch 
2260 operates on the field-proven Alcatel-Lucent Operating System (AOS) software 
supporting simple device management using the in-box web browser graphical user 
interface (GUI), as well as a subset of the most critical command-line interface (CLI) 
management commands. The OmniSwitch 2260 allows you to achieve reliable business-
class network performance, including security, without paying for advanced network 
management features. The switches are a lower price alternative compared to managed 
switches for wired connectivity, while maintaining performance, Quality of Service (QoS), 
and scalability, using a simplified web management interface.
The Alcatel-Lucent OmniSwitch 2260 family is embedded with the latest technology innovations,  
and offers maximum investment protection.
Deployments that benefit from the OmniSwitch 2260 family include:
• Small and medium-sized business network solutions
• High-speed desktop connectivity
• Secure wireless connectivity
• Unified communications connectivity (IP telephony, video, and converged solutions)	
Features
•	 8, 24, and 48 Gigabit Ethernet data or PoE+ ports with line-rate performance
•	 Gigabit Ethernet SFP uplink ports 
•	 Perpetual and fast PoE+ support across all PoE models
•	 Compact fan-less models for co-location work environments

<<<PAGE 471>>>
2
Datasheet
Alcatel-Lucent OmniSwitch 2260
Management
•	 AOS field-proven software with management through web interface (WebView 2.0), command-line 
interface (CLI), and Simple Network Management Protocol (SNMP)
•	 Ethernet operations, administration and management (OA&M) support for service configuration and 
monitoring
•	 Cloud enabled with Alcatel-Lucent OmniVista® Cirrus Network Management as a Service for a secure, 
resilient, and scalable cloud-based network management
•	 Support by Alcatel-Lucent OmniVista 2500 Network Management System (NMS) 
Security
•	 Comprehensive 802.1X features to control access to the network
•	 Flexible device and user authentication with Alcatel-Lucent Access Guardian (IEEE 802.1x/MAC)
•	 Advanced QoS and Access Control Lists (ACLs) for IPv4 and IPv6 traffic control, including an 
embedded denial of service (DoS) engine to filter out unwanted traffic attacks
•	 Extensive support of user-oriented features such as learned port security (LPS), port mapping, 
Dynamic Host Configuration Protocol (DHCP) binding tables, and User Network Profile (UNP) 
Performance and redundancy 
•	 Advanced layer-2+ features with static routing for both IPv4 and IPv6
•  Triple speed (10/100/1G) user interfaces and fiber interfaces (SFPs) supporting 1000Base-X 
•	 Wire-rate switching and routing performance
Convergence
•	 Auto VoIP VLAN for Alcatel-Lucent Enterprise VoIP Phones 
•	 Future-ready support for multimedia applications with wire-rate multicast
•	 IEEE 802.3af, IEEE 802.3at PoE support for IP phones, wireless LAN (WLAN) access points, PTZ video 
cameras, and IoT devices
Benefits
•	 Meets customer configuration needs and offers excellent investment protection and flexibility, as  
well as ease-of-deployment, operation, and maintenance
•	 Provides outstanding performance when supporting real-time voice, data, and video applications  
for converged scalable networks
•	 Ensures efficient power management, reduces operating expenses (OPEX), and lowers total cost of 
ownership (TCO) through low power consumption and dynamic PoE allocation, which delivers only 
the power needed by the attached device
•	 A field-upgradeable solution that makes the network highly available and reduces OPEX
•	 Fully secures the network at the edge, at no additional cost
•	 Enterprise-wide cost reduction through hardware consolidation, to achieve network segmentation  
and security without additional hardware installation
•	 Supports cost-effective installation and deployment with automated switch setup and configuration 
and end-to-end virtual LAN (VLAN) provisioning
•	 Alcatel-Lucent OmniVista Cirrus powers secure, resilient and scalable, cloud-based network 
management. It offers hassle-free network deployment and easy service rollout with advanced 
analytics for smarter decision-making. It provides IT-friendly Unified Access with secure 
authentication and policy enforcement for users and devices.

<<<PAGE 472>>>
3
Datasheet
Alcatel-Lucent OmniSwitch 2260
Table 1. Available OmniSwitch 2260 models
24/48 Port models 
User ports (1G RJ 45
1G SFP uplink
Power supply/PoE budget
Fan status
OS2260-10
8
4
Internal
Fan-less
OS2260-P10
8
4
Internal (75W)
Fan-less
OS2260-24
24
4
Internal
Fan-less
OS2260-P24
24
4
Internal (195W)
Variable-speed
OS2260-48
48
6
Internal
Variable-speed
OS2260-P48
48
6
Internal (370W)
Variable-speed
Technical specifications
Gigabit product 
matrix
OS2260-10
OS2260-P10
OS2260-24
OS2260-P24
OS2260-48
OS2260-P48
Gigabit RJ 45 ports
8
8
24
24 PoE+
48
48 PoE+
Fixed 1G SFP 
uplink
4
4
4
4
6
6
Console port
1
1
1
1
1
1
USB/OoB 
management port
1
1
1
1
1
1
Primary power
Internal
Internal
Internal
Internal
Internal
Internal
Backup power
N/A
N/A
N/A
N/A
N/A
N/A
Fans
0
0
0
1
1
1
CPU
800 MHz  
MIPS-34Kc
800 MHz  
MIPS-34Kc
1 GHz MIPS 
dual core
1 GHz MIPS 
dual core
1 GHz MIPS 
dual core
1 GHz MIPS 
dual core
File system flash
512 MB
512 MB
512 MB
512 MB
512 MB
512 MB
RAM
512 MB
512 MB
512 MB
512 MB
512 MB
512 MB
Packet Buffers
12 Mb/s
12 Mb/s
16 Mb/s
16 Mb/s
16 Mb/s
16 Mb/s
Performance aggregated
Max switching ASIC 
capacity
128 Gb/s
128 Gb/s
128 Gb/s
128 Gb/s
216 Gb/S
216 Gb/S
Switch capacity 
with all ports (full 
duplex)
24 Gb/s
24 Gb/s
56 Gb/s
56 Gb/s
108 Gb/s
108 Gb/s
Switch frame rate  
@ 64 byte packet
17.9 Mpps
17.9 Mpps
41.7 Mpps
41.7 Mpps
80.4 Mpps
80.4 Mpps
System power 
consumption:
• Idle
• 100% traffic all 
ports    (max)
 
 
5.3 W
15.3 W
 
 
7.6 W
17 W
 
 
13,1 W
29.5 W
 
 
24.5 W
40.7 W
 
 
30.8 W
61.9 W
 
 
35.2 W
63.2 W
System heat 
dissipation
N/A (BTU/h)
58 (BTU/h)
101 (BTU/h)
139 (BTU/h)
211 (BTU/h)
216 (BTU/h)
Power consumption  
w/PoE
N/A
101W
N/A
262.4 W
N/A
453.3W
Heat dissipation 
w/PoE
N/A (BTU/h)
345 (BTU/h)
N/A (BTU/h)
896 (BTU/h)
N/A (BTU/h)
1547 (BTU/h)
Power supply 
efficiency (max 
load)
81.66%
87.53%
83.50%
87.30%
83.90%
88.80%
Acoustics (dB) 
@25C*
0 db(A)
0 db(A)
0 db(A)
<40 db(A)
<40 db(A)
<40 db(A)
Number of fans
0
0
0
1
1
1

<<<PAGE 473>>>
4
Datasheet
Alcatel-Lucent OmniSwitch 2260
Gigabit product 
matrix
OS2260-10
OS2260-P10
OS2260-24
OS2260-P24
OS2260-48
OS2260-P48
MTBF (hours) 
@ 25C
2,174 k
1,042 k
1,632 k
693 k
1,181 k
625 k
Height
4.4 cm  
(1.73 in)
4.4 cm ( 
1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
Width
21.7 cm 
(8.55in)
21.7 cm 
(8.55in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
Depth
28 cm  
(11.05 in)
28 cm 
(11.05 in)
30 cm  
(11.81 in)
30 cm  
(11.81 in)
30 cm  
(11.81 in)
30 cm 
(11.81 in)
Weight
1.8 kg 
(3.9 lbs)
1.9 kg 
(4.2 lbs)
3.39 kg 
(7.47 lbs)
3.62 kg 
(7.98 lbs)
3.8 kg  
(8.3 lbs)
4.2 kg 
(9.3 lbs)
Operating 
temperature
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
Storage 
temperature
-20°C to 60°C
(-4°F to 140°F))
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
Humidity 
(operating)
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
Commercial references
OmniSwitch 2260 models
OS2260-10
Fixed 1RU ½ rack chassis 8 RJ 45 10/100/1G BaseT, 4 SFP (1G) uplink ports, Fan-less
OS2260-P10
Fixed 1RU ½ rack chassis 8 RJ 45 PoE 10/100/1G BaseT, 4 SFP (1G) uplink ports, 75W power budget, fan-less
OS2260-24
Fixed 1RU chassis 24 RJ 45 10/100/1G BaseT, 4 SFP (1G) uplink ports. Fan-less
OS2260-P24
Fixed 1RU chassis 24 RJ 45 PoE 10/100/1G BaseT, 4 SFP (1G) uplink ports, 195W power budget
OS2260-48
Fixed 1RU chassis 48 RJ 45 10/100/1G BaseT, 6 SFP (1G) uplink ports
OS2260-P48
Fixed 1RU chassis 48 RJ 45 PoE 10/100/1G BaseT, 6 SFP (1G) uplink ports. 370W power budget
OmniSwitch 2260 Gigabit transceivers and cables
SFP-GIG-T
1000Base T Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and full duplex mode
SFP-GIG-SX
1000Base SX Gigabit Ethernet optical transceiver (SFP MSA) 
SFP-GIG-LX
1000Base LX Gigabit Ethernet optical transceiver (SFP MSA) 
SFP-GIG-LH40
1000Base LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on 9/125 µm SMF. 
SFP-GIG-LH70
1000Base LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on 9/125 µm SMF. 
OS2x60-CBL-60CM
1/10G direct attached uplink copper cable (60 cm, SFP+)
OS2x60-CBL-1M
1/10G direct attached uplink copper cable (1 m, SFP+)
OS2x60-CBL-3M
1/10G direct attached uplink copper cable (3 m, SFP+)
OmniSwitch 2260 10 port mounting options
OS2260-RM-19-L
Simple L-bracket for mounting a single OS2260-10/-P10 switch in a 19 rack
OS2260-WALL-MNT
Wall mounting kit for OS2260 products, contains universal mounting brackets and screws for wall mounting 
a OS2260 switch

<<<PAGE 474>>>
5
Datasheet
Alcatel-Lucent OmniSwitch 2260
Detailed product features
Simplified management
•	 Intuitive CLI in a scriptable BASH 
environment via console, Telnet  
or Secure Shell (SSH) v2 over  
IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over 
IPv4/ IPv6+
•	 Fully-programmable RESTful web 
services interface with XML and 
JSON support. API enables access  
to CLI and individual mib objects
•	 Integrated with Alcatel-Lucent 
OmniVista products for network 
management
•	 Full configuration and reporting 
using SNMPv1/2 to facilitate third-
party network management over 
IPv4/IPv6
•	 File upload using USB, TFTP, FTP, 
SFTP, or SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line 
editing, bulk configuration, and  
out-of-the-box auto-provisioning
•	 Multiple microcode image support 
with fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
Monitoring and 
troubleshooting
•	 Local (on the flash memory) and 
remote server logging (Syslog):  
event and command logging
•	 IP tools: Ping and trace route
•	 Loopback IP address support for 
management per service
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD) 
and Digital Diagnostic Monitoring 
(DDM) 
Network configuration
•	 Zero-touch provisioning and 
provisioning based on templates 
using OV2500/OV Cirrus 
•	 Auto-negotiating 10/100/1000 ports 
automatically configure port speed 
and duplex setting
•	 Auto MDI/MDIX automatically 
configures transmit and receive 
signals to support straight-through 
and crossover cabling
•	 BOOTP/DHCP client allows 
auto-configuration of switch 
IP information for simplified 
deployment
•	 DHCP relay to forward client 
requests to a DHCP server
•	 IEEE 802.1AB Link Layer Discovery 
Protocol (LLDP) with MED extensions 
for automated device discovery
•	 Multiple VLAN Registration Protocol 
(MVRP) for IEEE 802.1Q-compliant 
VLAN pruning and dynamic VLAN 
creation
•	 Auto QoS for switch management 
traffic as well as traffic from  
Alcatel-Lucent IP phones
•	 Network Time Protocol (NTP) for 
network- wide time synchronisation
Resiliency and high-
availability
•	 Unified management and control 
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning 
Tree Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+)  
and 1x1 STP model
•	 IEEE 802.3ad/802.1AX Link 
Aggregation Control Protocol  
(LACP) and static LAG groups  
across modules
•	 Built-in CPU protection against 
malicious attacks
Advanced security
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive  
user-policy-based NAC
•	 Autosensing IEEE 802.1X multi-
client, multi-VLAN support
•	 MAC-based authentication for  
non-IEEE 802.1X hosts
• User Network Profile (UNP) simplifies 
NAC by dynamically providing 
pre-defined policy configuration to 
authenticated clients — VLAN, BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralised Remote Access Dial-
In User Service (RADIUS) and 
Lightweight Directory Access 
Protocol (LDAP) administrator 
authentication
•	 Centralised RADIUS for device 
authentication and network access 
control authorisation
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-
based field in hardware (Layer 1  
to Layer 4)
•	 ARP poisoning detection
•	 IP Source Filtering as a protective 
and effective mechanism against  
ARP attacks
Converged networks
Power over Ethernet (PoE)
•	 PoE models support Alcatel-Lucent 
IP phones and WLAN access points, 
as well as any IEEE 802.3af, IEEE 
802.3at compliant end device
•	 Configurable per-port PoE priority 
and max power for power allocation
•	 Dynamic PoE allocation: Delivers 
only the power needed by the 
powered devices (PD) up to the  
total power budget for most  
efficient power consumption
Quality of Service (QoS)
•	 Priority queues: Eight hardware-
based queues per port for flexible 
QoS management
•	 Traffic prioritisation: Flow-based 
QoS with internal and external (also 
known as, remarking) prioritisation 
•	 Bandwidth management: Flow-based 
bandwidth management
•	 Queue management: Configurable 
scheduling algorithms — Strict 
Priority Queuing (SPQ), Weighted 
Round Robin (WRR) 
•	 Auto QoS for switch management 
traffic as well as traffic from  
Alcatel-Lucent IP phones
Layer-2, Static Routing,  
and Multicast
Layer-2 switching
•	 Up to 16k MAC addresses
•	 Up to 62 VLANs
•	 Up to 1.5k total system policies
•	 Latency: < 4 µs
•	 Max Frame: 12KB (jumbo)

<<<PAGE 475>>>
6
Datasheet
Alcatel-Lucent OmniSwitch 2260
IPv4 and IPv6
•	 Static routing for IPv4 and IPv6
•	 Up to 2 IPv4 and 2 IPv6 static routes
•	 Up to 8 IPv4 and 2 IPv6 interfaces
Multicast
•	 IGMPv1/v2/v3 snooping to optimise 
multicast traffic
•	 Multicast Listener Discovery (MLD) 
v1/v2 snooping
•	 Up to 1000 multicast groups
Network protocols
•	 DHCP relay (including generic UDP 
relay)
•	 Address Resolution Protocol (ARP)
•	 Generic User Datagram Protocol 
(UDP) relay per VLAN
•	 DHCP Option 82 — configurable  
relay agent information
Indicators
System LEDs 
•	 System (OK) (chassis HW/SW status)
•	 PWR (primary power supply status)
•	 VC (virtual chassis primary)
Per-port LEDs
•	 10/100/1000: PoE, link/activity
•	 SFP: Link/activity
Compliance and certifications
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart B 
(Class A)
•	 VCCI (Class A limits. Note: Class A 
with UTP cables)
•	 ICES–003:2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) - C-Tick
•	 AS/NZS 3548 (Class A limits. Note: 
Class A with UTP cables)
•	 CE-Mark: Marking for European 
countries (Class A limits. Note: Class 
A with UTP cables)
•	 CE Emission consists of:
¬	EN 50581: Standard for technical 
documentation for RoHS recast
¬	EN 55022 (EMI and EMC 
requirement) 
¬	EN 55024: 2010 (ITE Immunity 
characteristics)
¬	EN 61000-3-2 (Limits for harmonic 
current emissions)
¬	EN 61000-3-3
¬	EN 61000-4-2
¬	EN 61000-4-3
¬	EN 61000-4-4
¬	EN 61000-4-5
¬	EN 61000-4-6
¬	EN 61000-4-8
¬	EN 61000-4-11
¬	IEEE802.3: Hi-Pot Test  
(2250 V DC on all Ethernet ports)
•	 IEC 62368-1
Safety agency certifications
•	 CDRH Laser
•	 Compliant with Restriction on 
Hazardous Substances (RoHS) and 
Waste Electrical and Electronic 
Equipment (WEEE) directives
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 IEC 62368-1
•	 UL 60950-1, 2nd Edition, 
Information Technology Equipment
•	 CAN/CSA C22.2 No. 60950-1-07, 
2nd Edition, Information Technology 
Equipment
•	 IEC 62368-1:2018, ICT and AV 
equipment safety, with all National 
Deviations
• IEC 60950-1, with all National 
Deviations 
¬	AS/NZ TS-001 and 60950, 
Australia
¬	ANATEL, Brazil
¬	CCC, China
¬	UL-GS Mark, Germany
¬	NOM-019 SCFI, Mexico
¬	RETIE, Colombia
¬	SNI, Indonesia
¬	ECAS, UAE
Supported standards
IEEE standards
•	 IEEE 802.1D (STP)
•	 IEEE 802.1p (CoS)
•	 IEEE 802.1Q (VLANs)
•	 IEEE 802.1s (MSTP)
•	 IEEE 802.1w (RSTP)
•	 IEEE 802.1X (Port-based Network 
Access Protocol)
•	 IEEE 802.3i (10Base-T)
•	 IEEE 802.3u (Fast Ethernet)
•	 IEEE 802.3x (Flow Control)
•	 IEEE 802.3z (Gigabit Ethernet)
•	 IEEE 802.3ab (1000Base-T)
•	 IEEE 802.3ac (VLAN Tagging)
•	 IEEE 802.3ad (Link Aggregation)
•	 IEEE 802.3af (Power over Ethernet)
•	 IEEE 802.3at (Power over Ethernet)
•	 IEEE 802.3ak (Multiple Registration 
Protocol)
•	 IEEE 802.3ax (Link Aggregation)
•	 IEEE 802.3az (Energy Efficient 
Ethernet)
IETF RFCs
IP Multicast
•	 RFC 1112 IGMP v1
•	 RFC 2236/2933 IGMP v2 and MIB
•	 RFC 2365 Multicast	
•	 RFC 3376 IGMPv3 for IPv6
IPv6
•	 RFC 1886 DNS for IPv6
•	 RFC 2292/2373/2374/2460/2462
•	 RFC 2461 NDP
•	 RFC 2463/2466 ICMP v6 and MIB
•	 RFC 2452/2454 IPv6 TCP/UDP MIB
•	 RFC 2464/2553/2893/3493/3513
•	 RFC 3056 IPv6 Tunneling
•	 RFC 3542/3587 IPv6
•	 RFC 4007 IPv6 Scoped Address 
Architecture
•	 RFC 4193 Unique Local IPv6 Unicast 
Addresses
Manageability 
•	 RFC 854/855 Telnet and Telnet 
options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1 and 
SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP 
Traps
•	 RFC 1573/2233/2863 Private 
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•	 RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from 
Forms: Multipart/form-data
•	 RFC 2396 Uniform Resource 
Identifiers (URI): Generic Syntax
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 4122 A Universally Unique 
IDentifier (UUID) URN Namespace
•	 RFC 4234 Augmented BNF for 
Syntax Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol

<<<PAGE 476>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by 
ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/
legal/trademarks-copyright. All other trademarks are the property of their respective owners. The information 
presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any 
responsibility for inaccuracies contained herein. © Copyright 2021 ALE International, ALE USA Inc. All rights 
reserved in all countries. DID21043002EN (November 2021)
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP Status 
Codes 
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and 
crypto algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618 
RADIUS Authentication and Client 
MIB
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS 
Extension
•	 RFC 4301 Security Architecture  
for IP
Quality of service
•	 RFC 896 Congestion control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 3635 Pause Control
Others
•	 RFC 791 /894/1024/1349 IP and  
IP/Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy 
ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 NTP v3 and Simple 
NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 
DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
 
Warranty
The OmniSwitch 2260 family comes with a Limited Lifetime Warranty.
Services and support
For more information about our Professional services, Support services, and Managed services, please 
go to https://www.al-enterprise.com/en/services/support-services

<<<PAGE 477>>>
Datasheet 
Alcatel-Lucent OmniSwitch 2360
Alcatel-Lucent  
OmniSwitch 2360
Stackable Gigabit Ethernet LAN Switch Family
The Alcatel-Lucent OmniSwitch® 
2360 Stackable Gigabit Ethernet 
LAN switch family offers value and 
is optimised for Small and Medium 
Businesses (SMB) and branch/
campus workgroup solutions.  
These are simple, flexible, and secure switches, ideal for out-of-the-wiring-closet 
converged solutions for workstation, access-point, IP telephony deployments. 
The Alcatel-Lucent OmniSwitch 2360 operates on the field-proven Alcatel-Lucent Operating System 
(AOS) software supporting simple device management through command-line interface (CLI), inbox 
web browser graphical user interface (GUI) WebView 2.0, Alcatel-Lucent OmniVista® 2500 Network 
Management System (NMS), and the cloud-enabled Alcatel-Lucent OmniVista Cirrus Network 
Management as a Service.
Powerful L2+ features such as static routing (IPv4/IPv6), flexible/advanced Quality of Service (QoS)  
and Access Control List (ACL) options, Denial-of-Service (DoS) features, and wire-rate performance, 
makes this family of switches optimal for delivering network security, network reliability, and 
operational efficiency for any SMB network.
The Alcatel-Lucent OmniSwitch 2360 family is embedded with the latest technology innovations,  
and offers maximum investment protection.
Deployments that benefit from the OmniSwitch 2360 family include:
•	 Brand and campus workgroups
•	 SMB networks	
Features
•	 24 and 48 Gigabit Ethernet data or PoE+ ports with line-rate performance
•	 Gigabit Ethernet SFP uplink ports or 10 Gigabit Ethernet SFP+ uplink ports (X models)
•	 10 GigE virtual chassis bandwidth up to 4 units (stacking) or 216 ports
•	 Perpetual and fast PoE+ support across all PoE models
•	 Compact fan-less models for co-location work environments

<<<PAGE 478>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 2360
Management
•	 AOS field-proven software with 
management through web interface 
(WebView 2.0), command-line 
interface (CLI), and Simple Network 
Management Protocol (SNMP)
•	 Ethernet operations, administration 
and management (OA&M) support for 
service configuration and monitoring
•	 Cloud enabled with OmniVista Cirrus 
for secure, resilient, and scalable 
cloud-based network management
•	 Support by OmniVista 2500 NMS
Security
•	 Comprehensive 802.1X features  
to control access to the network
•	 Flexible device and user 
authentication with Alcatel-Lucent 
Access Guardian (IEEE 802.1x/MAC) 
•	 Advanced QoS and Access Control 
Lists (ACLs) for IPv4 and IPv6 traffic 
control, including an embedded 
denial of service (DoS) engine to 
filter out unwanted traffic attacks
•	 Extensive support of user-oriented 
features such as learned port 
security (LPS), port mapping, 
Dynamic Host Configuration Protocol 
(DHCP) binding tables, and User 
Network Profile (UNP) 
Performance and redundancy 
•	 Advanced layer-2+ features with 
static routing for both IPv4 and IPv6
•	 Triple speed (10/100/1G) user 
interfaces and fibre interfaces (SFPs) 
supporting 1000Base-X 
•	 10G uplinks ports supporting SFP+  
(X models) 
•	 Wire-rate switching and routing 
performance
•	 High availability with virtual chassis 
concept, remote/redundant stacking 
links, primary/secondary unit 
failover and configuration rollback
Convergence
•   Auto VoIP VLAN for Alcatel-Lucent 
Enterprise VoIP Phones 
•	 Future-ready support for multimedia 
applications with wire-rate multicast
•	 IEEE 802.3af, IEEE 802.3at PoE 
support for IP phones, wireless LAN 
(WLAN) access points, PTZ video 
cameras, and IoT devices
Benefits
•	 Meets customer configuration needs 
and offers excellent investment 
protection and flexibility, as well as 
ease of deployment, operation, and 
maintenance
•	 Provides outstanding performance 
when supporting real-time voice, 
data, and video applications for 
converged scalable networks
•	 Ensures efficient power 
management, reduces operating 
expenses (OPEX), and lowers total 
cost of ownership (TCO) through low 
power consumption and dynamic 
PoE allocation, which delivers only 
the power needed by the attached 
device
•	 A field-upgradeable solution that 
makes the network highly available 
and reduces OPEX
•	 Fully secures the network at the 
edge, at no additional cost
•	 Enterprise-wide cost reduction 
through hardware consolidation, to 
achieve network segmentation and 
security without additional hardware 
installation
•	 Supports cost-effective installation 
and deployment with automated 
switch setup and configuration 
and end-to-end virtual LAN (VLAN) 
provisioning
•	 Alcatel-Lucent OmniVista Cirrus 
powers secure, resilient and scalable 
cloud-based network management. 
It offers hassle-free network 
deployment and easy service 
rollout with advanced analytics for 
smarter decision-making. It provides 
IT-friendly Unified Access with 
secure authentication and policy 
enforcement for users and devices.
Table 1. Available OmniSwitch 2360 models
24/48 port 
models 
User ports 1G 
RJ 45
1G SFP uplink
10G SFP uplink
1G SFP uplink 
10G SFP+ VFL
Power supply/
PoE budget
Fan status
OS2360-24
24
2
0
2
Internal
Fan-less
OS2360-P24
24
2
0
2
Internal (195W)
Variable-speed
OS2360-48
48
4
0
2
Internal
Variable-speed
OS2360-P48
48
4
0
2
Internal (370W)
Variable-speed
OS2360-P24X
24
0
2
2
Internal (370W)
Variable-speed
OS2360-P48X
48
2
2
2
Internal (740W)
Variable-speed

<<<PAGE 479>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 2360
Technical specification
Gigabit  
product matrix
OS2360-24
OS2360-P24
OS2360-48
OS2360-P48
OS2360-P24X
OS2360-P48X
Gigabit RJ 45 ports
24
24 PoE+
48
 48 PoE+
24 PoE+
48 PoE+
Fixed 1G SFP 
uplink
2
2
4
4
0
2
Fixed 1G/10G SFP+ 
uplink
0
0
0
0
2
2
Fixed 1G SFP 
uplink or 10G VFL 
ports
2 
2
2
2
2
2
Console port
1
1
1
1
1
1
USB/OoB 
management port 
1 
1 
1
1
1
1
Primary power 
Internal
Internal
Internal
Internal
Internal
Internal
Backup power 
N/A
N/A
N/A
N/A
N/A
N/A
Fans 
0
1
1
1
1
2
CPU
1 GHz MIPS  
dual core
1 GHz MIPS  
dual core
1 GHz MIPS  
dual core
1 GHz MIPS  
dual core
1 GHz MIPS  
dual core
1 GHz MIPS  
dual core
File system flash 
512 MB 
512 MB
512 MB
512 MB
512 MB
512 MB
RAM 
1 GB 
1 GB 
1 GB 
1 GB 
1 GB 
1 GB 
Packet buffers
16 Mb/s
16 Mb/s
16 Mb/s
16 Mb/s
16 Mb/s
16 Mb/s
Performance aggregated
Max switching ASIC 
capacity 
128 Gb/s
128 Gb/s
216 Gb/S
216 Gb/S
128 Gb/S
216 Gb/S
Switch capacity 
with all ports 
(full duplex + 
stacking)
92 Gb/s
92 Gb/s
144 Gb/s
144 Gb/s
128 Gb/s
180 Gb/s
Switch frame rate 
@ 64 byte packet 
68.4 Mpps
68.4 Mpps
107.1 Mpps
107.1 Mpps
95.2 Mpps
133.9 Mpps
2x10GE VFL 
capacity
40 Gb/s
40 Gb/s
40 Gb/s
40 Gb/s
40 Gb/s
40 Gb/s
System power 
consumption: 
• Idle
• 100% traffic all 
ports (max)
 
 
13.1 W 
29.5 W
 
 
24.5 W 
40.7 W
 
 
30.8 W 
61.9 W
 
 
35.2 W 
63.2 W
 
 
24.2 W 
40.2 W
 
 
37.1 W 
64.6 W
System heat 
dissipation 
101 (BTU/h)
139 (BTU/h)
211 (BTU/h)
216 (BTU/h)
137 (BTU/h)
220.5 (BTU/h)
Power 
consumption w/
PoE 
N/A
262.4 W
N/A
453.3W
427.2W 
891.2W
Heat Dissipation  
w/PoE 
N/A (BTU/h)
896 (BTU/h)
N/A (BTU/h)
1547 (BTU/h)
1458 (BTU/h)
3042 (BTU/h)
Power supply 
efficiency (max 
load)
83.5%
87.3%
83.9%
88.8%
89.1%
89.6%
Acoustics (dB) 
@25C
0 db(A)
<40 db(A)
<40 db(A)
<40 db(A)
<40 db(A)
<40 db(A)
Number of fans
0
1
1
1
1
2
MTBF (hours) @ 
25C
1,632 k
693 k
1,181 k
625 k
693 k
565 k
Height 
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm ( 
1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)

<<<PAGE 480>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 2360
Gigabit  
product matrix
OS2360-24
OS2360-P24
OS2360-48
OS2360-P48
OS2360-P24X
OS2360-P48X
Width 
44 cm  
(17.32 in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
44 cm  
(17.32 in)
Depth 
30 cm  
(11.81 in)
30 cm  
(11.81 in)
30 cm  
(11.81 in)
30 cm  
(11.81 in)
30 cm  
(11.81 in)
30 cm  
(11.81 in)
Weight 
3.39 kg  
(7.47 lbs)
3.62 kg  
(7.98 lbs)
3.8 kg  
(8.3 lbs)
4.2 kg  
(9.3 lbs)
3.8 kg  
(8.38 lbs)
4.5 kg  
(9.9 lbs)
Operating 
temperature 
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
0°C to 45°C
(32°F to 113°F)
Storage 
temperature 
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
-20°C to 60°C
(-4°F to 140°F)
Humidity 
(operating) 
5% to 95%
non-condensing 
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
5% to 95%
non-condensing
Commercial references
OmniSwitch 2360 models
OS2360-24
Fixed 1RU chassis 24 RJ 45 10/100/1G BaseT, 2 SFP (1G) uplink ports, 2 SFP(+) as 1G uplinks or 10G 
stacking ports, Fan-less
OS2360-P24
Fixed 1RU chassis 24 RJ 45 PoE 10/100/1G BaseT, 2 SFP (1G) uplink ports, 2 SFP(+) as 1G uplinks or 10G 
stacking ports. 195W power budget
OS2360-48
Fixed 1RU chassis 48 RJ 45 10/100/1G BaseT, 2 SFP (1G) uplink ports, 2 SFP(+) as 1G uplinks or 10G 
stacking ports
OS2360-P48
Fixed 1RU chassis 48 RJ 45 PoE 10/100/1G BaseT, 2 SFP (1G) uplink ports, 2 SFP(+) as 1G uplinks or 10G 
stacking ports, 370W power budget
OS2360-P24X
Fixed 1RU chassis 24 RJ 45 PoE 10/100/1G BaseT, 2 10G SFP+ uplink ports, 2 SFP(+) as 1G uplinks or 10G 
stacking ports, 370W power budget
OS2360-P48X
Fixed 1RU chassis 48 RJ 45 PoE 10/100/1G BaseT, 2 SFP (1G) uplink ports, 2 10G SFP+ uplink ports,  
2 SFP(+) as 1G uplinks or 10G stacking ports, 740W power budget
OmniSwitch 2360 10G transceivers and cables
OS2x60-CBL-60CM
1/10G direct attached uplink/stacking copper cable (60 cm, SFP+)
OS2x60-CBL-1M
1/10G direct attached uplink/stacking copper cable (1 m, SFP+)
OS2x60-CBL-3M
1/10G direct attached uplink/stacking copper cable (3 m, SFP+)
SFP-10G-SR
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 850 nm wavelength (nominal) with  
an LC connector. Typical reach of 300 m.
SFP-10G-LR
10 Gigabit optical transceiver (SFP+). Supports single mode fiber with an LC connector. Typical reach of 10 Km.
SFP-10G-ER
10 Gigabit optical transceiver (SFP+). Supports single mode fiber over 1550 nm wavelength (nominal) with 
an LC connector. Typical reach of 40 km.
OmniSwitch 2360 Gigabit transceivers
SFP-GIG-T
1000Base T Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and full duplex mode
SFP-GIG-SX
1000Base SX Gigabit Ethernet optical transceiver (SFP MSA) 
SFP-GIG-LX
1000Base LX Gigabit Ethernet optical transceiver (SFP MSA) 
SFP-GIG-LH40
1000Base LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on 9/125 µm SMF.
SFP-GIG-LH70
1000Base LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on 9/125 µm SMF.

<<<PAGE 481>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 2360
Detailed product features
Simplified management
•	 Intuitive CLI in a scriptable BASH 
environment via console, Telnet  
or Secure Shell (SSH) v2 over  
IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over 
IPv4/ IPv6+
•	 Fully-programmable RESTful web 
services interface with XML and 
JSON support. API enables access  
to CLI and individual mib objects
•	 Integrated with Alcatel-Lucent 
OmniVista products for network 
management
•	 Full configuration and reporting 
using SNMPv1/2 to facilitate  
third-party network management 
over IPv4/IPv6
•	 File upload using USB, TFTP, FTP, 
SFTP, or SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line 
editing, bulk configuration, and  
out-of-the-box auto-provisioning
•	 Multiple microcode image support 
with fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
Monitoring and 
troubleshooting
•	 Local (on the flash memory) and 
remote server logging (Syslog):  
event and command logging
•	 IP tools: Ping and trace route
• Loopback IP address support for 
management per service
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD) 
and Digital Diagnostic Monitoring 
(DDM)
Network configuration
•	 Zero-touch provisioning and 
provisioning based on templates 
using OV2500/OV Cirrus 
•	 Auto-negotiating 10/100/1000 ports 
automatically configure port speed 
and duplex setting
•	 Auto MDI/MDIX automatically 
configures transmit and receive 
signals to support straight-through 
and crossover cabling
•	 BOOTP/DHCP client allows 
auto-configuration of switch 
IP information for simplified 
deployment
•	 DHCP relay to forward client 
requests to a DHCP server
•	 IEEE 802.1AB Link Layer Discovery 
Protocol (LLDP) with MED extensions 
for automated device discovery
•	 Multiple VLAN Registration Protocol 
(MVRP) for IEEE 802.1Q-compliant 
VLAN pruning and dynamic VLAN 
creation
•	 Auto QoS for switch management 
traffic as well as traffic from  
Alcatel-Lucent IP phones
•	 Network Time Protocol (NTP) for 
network- wide time synchronisation
•	 Virtual chassis up to 4 units of  
24 and 48 port models
Resiliency and high-
availability
•	 Unified management, control,  
and virtual chassis technology
•	 Virtual Chassis 1+N redundant 
supervisor manager
•	 Smart continuous switching 
technology
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning 
Tree Protocol (RSTP)
•	 Per-VLAN spanning tree Flat and  
1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link 
Aggregation Control Protocol  
(LACP) and static LAG groups  
across modules
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection:  
Auto- detection and recovery of 
Virtual Chassis splitting due to one or 
more VFL or stack element failures
Advanced security
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive  
user-policy-based NAC
•	 Autosensing IEEE 802.1X  
multi-client, multi-VLAN support
•	 MAC-based authentication for  
non-IEEE 802.1X hosts
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing 
pre-defined policy configuration to 
authenticated clients — VLAN, BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralised Remote Access Dial-
In User Service (RADIUS) and 
Lightweight Directory Access 
Protocol (LDAP) administrator 
authentication
•	 Centralised RADIUS for device 
authentication and network access 
control authorisation
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-
based field in hardware (Layer 1  
to Layer 4)
•	 ARP poisoning detection
•	 IP Source Filtering as a protective 
and effective mechanism against  
ARP attacks
Converged networks
Power over Ethernet (PoE)
•	 PoE models support Alcatel-Lucent 
IP phones and WLAN access points, 
as well as any IEEE 802.3af, IEEE 
802.3at compliant end device
•	 Configurable per-port PoE priority 
and max power for power allocation
•	 Dynamic PoE allocation: Delivers 
only the power needed by the 
powered devices (PD) up to the  
total power budget for most efficient 
power consumption
Quality of Service (QoS)
•	 Priority queues: Eight hardware-
based queues per port for flexible 
QoS management
•	 Traffic prioritisation: Flow-based 
QoS with internal and external (also 
known as, remarking) prioritisation
•	 Bandwidth management: Flow-based 
bandwidth management 
•	 Queue management: Configurable 
scheduling algorithms — Strict 
Priority Queuing (SPQ), Weighted 
Round Robin (WRR)
•	 Auto QoS for switch management 
traffic* as well as traffic from  
Alcatel-Lucent IP phones

<<<PAGE 482>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 2360
Layer-2, Static Routing,  
and Multicast
Layer-2 switching
•	 Up to 16k MAC addresses
•	 Up to 1024 VLANs
•	 Up to 1.5k total system policies
•	 Latency: < 4 µs
•	 Max Frame: 12KB (jumbo)
IPv4 and IPv6
•	 Static routing for IPv4 and IPv6
•	 Up to 32 IPv4 and 16 IPv6 static 
routes
•	 Up to 24 IPv4 and 4 IPv6 interfaces
Multicast
•	 IGMPv1/v2/v3 snooping to optimise 
multicast traffic
•	 Multicast Listener Discovery (MLD) 
v1/v2 snooping
•	 Up to 1000 multicast groups
Network protocols
•	 DHCP relay (including generic UDP 
relay)
•	 Address Resolution Protocol (ARP) 
•	 Generic User Datagram Protocol 
(UDP) relay per VLAN
•	 DHCP Option 82 — configurable relay 
agent information
Indicators
System LEDs 
•	 System (OK) (chassis HW/SW status)
•	 PWR (primary power supply status)
•	 VC (virtual chassis primary)
Per-port LEDs
•	 10/100/1000: PoE, link/activity
•	 SFP: Link/activity
•	 Virtual Chassis (VFL): Link/activity
Compliance and certifications
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart B 
(Class A)
•	 VCCI (Class A limits. Note: Class A 
with UTP cables)
•	 ICES–003:2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) - C-Tick
•	 AS/NZS 3548 (Class A limits.  
Note: Class A with UTP cables)
•	 CE-Mark: Marking for European 
countries (Class A limits.  
Note: Class A with UTP cables)
•	 CE Emission consists of:
¬	EN 50581: Standard for technical 
documentation for RoHS recast
¬	EN 55022 (EMI and EMC 
requirement) 
¬	EN 55024: 2010 (ITE Immunity 
characteristics)
¬	EN 61000-3-2 (Limits for harmonic 
current emissions)
¬	EN 61000-3-3
¬	EN 61000-4-2
¬	EN 61000-4-3
¬	EN 61000-4-4
¬	EN 61000-4-5
¬	EN 61000-4-6
¬	EN 61000-4-8
¬	EN 61000-4-11
¬	IEEE802.3: Hi-Pot Test  
(2250 V DC on all Ethernet ports)
•	 IEC 62368-1
Safety agency certifications
•	 CDRH Laser
•	 Compliant with Restriction on 
Hazardous Substances (RoHS) and 
Waste Electrical and Electronic 
Equipment (WEEE) directives
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 IEC 62368-1
•	 UL 60950-1, 2nd Edition, 
Information Technology Equipment
•	 CAN/CSA C22.2 No. 60950-1-07, 
2nd Edition, Information Technology 
Equipment
•	 IEC 62368-1:2018, ICT and AV 
equipment safety, with all National 
Deviations 
•	 IEC 60950-1, with all National 
Deviations 
¬	AS/NZ TS-001 and 60950, 
Australia
¬	ANATEL, Brazil
¬	CCC, China
¬	UL-GS Mark, Germany
¬	NOM-019 SCFI, Mexico
¬	RETIE, Colombia
¬	SNI, Indonesia
¬	ECAS, UAE
Supported standards
IEEE standards
•	 IEEE 802.1D (STP)
•	 IEEE 802.1p (CoS)
•	 IEEE 802.1Q (VLANs)
•	 IEEE 802.1s (MSTP)
•	 IEEE 802.1w (RSTP)
•	 IEEE 802.1X (Port-based Network 
Access Protocol)
•	 IEEE 802.3i (10Base-T)
•	 IEEE 802.3u (Fast Ethernet)
•	 IEEE 802.3x (Flow Control)
•	 IEEE 802.3z (Gigabit Ethernet)
•	 IEEE 802.3ab (1000Base-T)
•	 IEEE 802.3ac (VLAN Tagging)
•	 IEEE 802.3ad (Link Aggregation)
•	 IEEE 802.3ae (10 Gigabit Ethernet)
•	 IEEE 802.3af (Power over Ethernet)
•	 IEEE 802.3at (Power over Ethernet)
•	 IEEE 802.3ak (Multiple Registration 
Protocol)
•	 IEEE 802.3ax (Link Aggregation)
•	 IEEE 802.3az (Energy Efficient 
Ethernet)
IETF RFCs
IP Multicast
•	 RFC 1112 IGMP v1
•	 RFC 2236/2933 IGMP v2 and MIB
•  RFC 2365 Multicast	
•	 RFC 3376 IGMPv3 for IPv6
IPv6
•	 RFC 1886 DNS for IPv6
•	 RFC 2292/2373/2374/2460/2462
•	 RFC 2461 NDP
•	 RFC 2463/2466 ICMP v6 and MIB
•	 RFC 2452/2454 IPv6 TCP/UDP MIB
•	 RFC 2464/2553/2893/3493/3513
•	 RFC 3056 IPv6 Tunneling
•	 RFC 3542/3587 IPv6
•	 RFC 4007 IPv6 Scoped Address 
Architecture
•	 RFC 4193 Unique Local IPv6 Unicast 
Addresses
Manageability 
•	 RFC 854/855 Telnet and Telnet 
options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1  
and SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP 
Traps
•	 RFC 1573/2233/2863 Private 
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML

<<<PAGE 483>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by 
ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/
legal/trademarks-copyright. All other trademarks are the property of their respective owners. The information 
presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any 
responsibility for inaccuracies contained herein. © Copyright 2021 ALE International, ALE USA Inc. All rights 
reserved in all countries. DID21043003EN (November 2021)
•	 RFC 1901-1908/3416-3418  
SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from 
Forms: Multipart/form-data
•	 RFC 2396 Uniform Resource 
Identifiers (URI): Generic Syntax
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 4122 A Universally Unique 
IDentifier (UUID) URN Namespace
•	 RFC 4234 Augmented BNF for 
Syntax Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP Status 
Codes 
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and 
crypto algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618 
RADIUS Authentication and Client 
MIB
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS 
Extension
•	 RFC 4301 Security Architecture  
for IP
Quality of service
•	 RFC 896 Congestion control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 3635 Pause Control
Others
•	 RFC 791 /894/1024/1349 IP and  
IP/Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/ 
Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 NTP v3 and Simple 
NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 
DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/BootP Relay 
•	 RFC 2132 DHCP Options
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
Warranty
The OmniSwitch 2360 family comes with a Limited Lifetime Warranty.
Services and support
For more information about our Professional services, Support services, and Managed services, please 
go to https://www.al-enterprise.com/en/services/support-services

<<<PAGE 484>>>
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Alcatel-Lucent
OmniSwitch 6360 
Stackable Gigabit Ethernet LAN Switch Family
The Alcatel-Lucent OmniSwitch® 6360 
Stackable Gigabit Ethernet LAN Switch 
Family is an industry leading, branch, campus 
workgroup, and enterprise, value access 
solution. These are simple, flexible, and secure 
switches ideal for out-of-the-wiring-closet 
workstation, access-point, IP telephony and 
critical Internet of Things (IoT) deployment.
OmniSwitch 6360 operates using the field proven Alcatel-Lucent Operating System (AOS) software supporting 
simple device management and network management with a Command-Line Interface (CLI) in addition to an in-
box web browser graphical user interface (GUI). These switches deliver enhanced network security, reliability, and 
operational efficiency for Small- and Medium-sized Businesses (SMB) or Enterprise edge networks.
The Alcatel-Lucent OmniSwitch 6360 family is embedded with the latest technology innovations, and offers 
maximum investment protection.
Deployments that benefit from the OmniSwitch 6360 family include:
• Classroom and campus workgroups
• Small enterprise or branch office enterprise
• Small-to-mid-sized and enterprise edge networks

<<<PAGE 485>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Features
•	 10, 24, and 48 Gigabit Ethernet data or PoE+ ports with line-rate performance
•	 Gigabit Ethernet SFP or SFP/RJ-45 combination uplink ports, or fixed 10 Gigabit Ethernet SFP+/RJ45 
combination uplink ports (X models)
•	 10 GigE virtual chassis bandwidth up to 4 units (stacking) or 208 ports
•	 Perpetual and fast PoE+ support across all PoE models
•	 Compact fanless models for co-location work environments
Management
•	 AOS field-proven software with management through web interface (WebView 2.0), command line interface 
(CLI), and Simple Network Management Protocol (SNMP)
•	 Ethernet operations, administration and management (OA&M) support for service configuration  
and monitoring
•	 Cloud-enabled with Alcatel-Lucent OmniVista® Cirrus for secure, resilient, and scalable cloud-based  
network management
•	 Support by Alcatel-Lucent OmniVista 2500 Network Management System (NMS) 
Security
•	 Comprehensive 802.1X features to control access to the network
•	 Flexible device and user authentication with Alcatel-Lucent Access Guardian (IEEE 802.1x/MAC/captive portal) 
•	 Enables deployment of comprehensive and secure Bring Your Own Device (BYOD) services in enterprise 
networks such as guest management, device on-boarding, device posturing, , IoT device profiling, application 
management and dynamic change of authentication (CoA)
•	 Advanced Quality of Service (QoS) and Access Control Lists (ACLs) for IPv4 and IPv6 traffic control, including an 
embedded denial-of-service (DoS) engine to filter out unwanted traffic attacks
•	 Extensive support of user-oriented features such as learned port security (LPS), port mapping, Dynamic Host 
Configuration Protocol (DHCP) binding tables and User Network Profile (UNP)
Performance and redundancy 
•	 Advanced layer-2+ features with static routing for both IPv4 and IPv6
•	 Triple speed (10/100/1G) user interfaces and fiber interfaces (SFPs) supporting 1000Base-X 
•	 Two Multi-Gigabit (10/100/1G/2.5) RJ-45 HPoE (95W IEEE802.3bt) user interfaces (-P48X)
•	 10G uplinks ports supporting SFP+ or 10GBase-T (X models) 
•	 Wire-rate switching and routing performance
•	 High availability with virtual chassis concept, remote/redundant stacking links, primary/secondary unit failover, 
in-service software upgrade and configuration rollback
Convergence
•	 Enhanced Voice over IP (VoIP) and video performance with policy-based QoS
•	 Future-ready support for multimedia applications with wire-rate multicast
•	 AirGroup™ Network Services for Bonjour® speaking devices provides consistent experience over wireless and 
wired networks
•	 IEEE 802.3af, IEEE 802.3at and IEEE802.3bt (-P48X) PoE support for IP phones, wireless LAN (WLAN) access 
points, PTZ video cameras and IoT devices

<<<PAGE 486>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Benefits
•	 Meets any customer configuration need and offers excellent investment protection and flexibility, as well as 
ease of deployment, operation, and maintenance
•	 Provides outstanding performance when supporting real-time voice, data, and video applications for converged 
scalable networks
•	 Ensures efficient power management, reduces operating expenses (OPEX), and lowers total cost of ownership 
(TCO) through low power consumption and dynamic PoE allocation, which delivers only the power needed by 
the attached device
•	 A field-upgradeable solution that makes the network highly available and reduces OPEX
•	 Fully secures the network at the edge at no additional cost
•	 Enterprise-wide cost reduction through hardware consolidation to achieve network segmentation and security 
without additional hardware installation
•	 Supports cost-effective installation and deployment with automated switch setup and configuration and end-to-
end virtual LAN (VLAN) provisioning
•	 OmniVista Cirrus powers a secure, resilient, and scalable cloud-based network management. It offers hassle 
free network deployment and easy service rollout with advanced analytics for smarter decision making. IT-
friendly unified access with secure authentication and policy enforcement for users and devices.
10 Port 
models
User ports
1G RJ-45
1G RJ45 uplinks
1G SFP uplink
Power Supply/
PoE budget
Fan status
OS6360-10
8
2
2 x SFP uplink
Internal
Fanless
OS6360-P10
8
2
2 x SFP uplink
Internal (120W)
Fanless
24/48 Port 
models 
User ports
1G RJ-45
1G RJ-45/SFP
combo
1G SFP uplink
10G SFP+ uplink/VFL
Power supply/
PoE budget
Fan status
OS6360-24
24
2
2
Internal
Fanless
OS6360-P24
24
2
2
Internal (180W)
Fanless
OS6360-48
48
2
2
Internal
Variable speed
OS6360-P48
48
2
2
Internal (350W)
Variable speed
24/48 Port 
X models 
User ports
RJ-45
1G RJ-45/SFP combo
10G RJ-45/SFP+ combo
1G SFP uplink
10G SFP+ uplink/VFL
Power supply
PoE budget
Fan status
OS6360-PH24
24
2*
2
Internal (380W)
Variable speed
OS6360-PH48
46 x 1G 
2 x 1G/2.5G
2*
2
Internal (760W)
Variable speed 
OS6360-P24X
24 x 1G
2
2
Internal (380W)
Variable speed
OS6360-P48X
46 x 1G 
2 x 1G/2.5G
2
2
Internal (760W)
Variable speed
Notes: 
•	
*OS6360-PH24/PH48 RJ45/SFP ports are license upgradable to 10G speeds with the OS6360-SW-PERF license
•	
OS6360-P48X/PH48 Multi-Gigabit PoE ports comply with IEEE 802.3bt (95 W) and IEEE 2.5GE 802.3bz standards

<<<PAGE 487>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Technical specifications
Gigabit product matrix
OS6360-10
OS6360-P10
OS6360-24
OS6360-P24
OS6360-48
OS6360-P48
Gigabit RJ-45 ports
8
8 PoE+
24
24 PoE+
48
48 PoE+
Combo Gigabit RJ-45/
SFP ports
0
0
2
2
2
2
Fixed SFP/SFP+ uplink 
or VFL ports
2 x SFP uplink
2 x SFP uplink
2 x SFP+
2 x SFP+
2 x SFP+
2 x SFP+
Console port
1
1
1
1
1
1
USB/OoB  
management port 
1 
1 
1
1
1
1
Primary power 
Internal
Internal
Internal
Internal
Internal
Internal
Backup power 
N/A
N/A
N/A
N/A
N/A
N/A
Fans 
0
0
0
0
1
1
CPU
800MHz ARM v7
800MHz ARM v7
800MHz ARM  
v7
800MHz ARM v7
800MHz ARM 
v7
800MHz ARM v7
File system flash 
1 GB 
1 GB 
1 GB 
1 GB 
1 GB 
1 GB 
RAM 
1 GB 
1 GB 
1 GB 
1 GB 
1 GB 
1 GB 
Packet buffers
1.5MB
1.5MB
1.5MB
1.5MB
1.5MB
1.5MB
Performance aggregated 
Max switching ASIC 
capacity 
40 Gb/s
40 Gb/s
92 Gb/S
92 Gb/S
140 Gb/S
140 Gb/S
Switching capacity
24 Gb/s
24 Gb/s
92 Gb/s
92 Gb/s
140 Gb/s
140 Gb/s
Throughput 
17.9 Mpps
17.9 Mpps
68.5 Mpps
68.5 Mpps
104.2 Mpps
104.2 Mpps
2x10GE VFL capacity
N/A
N/A
40 Gb/s
40 Gb/s
40 Gb/s
40 Gb/s
System power 
consumption: 
-	 Idle 
-	 100% traffic all 	
	
	
ports (max)
 
 
13 W 
15 W
 
 
13 W 
18 W
 
 
21 W 
24 W
 
 
21 W 
28 W
 
 
46 W 
49 W
 
 
47 W 
54 W
System heat 
dissipation 
51 (BTU/h)
61.5 (BTU/h)
82 (BTU/h)
95.5 (BTU/h)
167 (BTU/h)
184 (BTU/h)
Power consumption 
w/PoE 
N/A
145 W
N/A
222 W
N/A
484 W
Heat dissipation  
w/PoE 
N/A
495 (BTU/h)
N/A
758 (BTU/h)
N/A
1652 (BTU/h)
Power supply efficiency 
(max load)
89%
93.5%
87.3%
93.5%
89.4%
93.3%
Acoustics (dB) @27C*
0 db(A)
0 db(A)
0 db(A)
0 db(A)
<42 db(A)
<42 db(A)
# of fans
0
0
0
0
1
1
MTBF (hours) @ 25C
1,179 k
1,094 k
2,595 k
1,447 k
832 k
789 k
Height 
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
4.4 cm  
(1.73 in)
Width 
21.7 cm  
(8.5 in) 
21.7 cm  
(8.5 in)
44 cm  
(17.33 in)
4.4 cm  
(17.33 in)
44 cm  
(17.33 in)
44 cm  
(17.33 in)
Depth 
28 cm  
(11 in)
28 cm  
(11 in)
22 cm  
(8.66 in)
22 cm  
(8.66 in)
33 cm  
(13 in)
33 cm  
(13 in)
Weight 
1.8 kg  
(3.9 lbs)
2.1 kg  
(4.6 lbs)
3.1 kg  
(6.9 lbs)
3.2 kg  
(7 lbs)
4.6 kg  
(10.1 lbs)
4.6 kg  
(10.1 lbs)
Operating 
temperature 
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)  
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)

<<<PAGE 488>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Gigabit product matrix
OS6360-10
OS6360-P10
OS6360-24
OS6360-P24
OS6360-48
OS6360-P48
Performance aggregated 
Storage temperature 
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
Humidity (operating)
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing
Gigabit full PoE product matrix
OS6360-PH24
OS6360-P24X
OS6360-P48X
OS6360-PH48
Gigabit RJ-45 user ports
24 PoE+
24 PoE+
46 PoE+
46 PoE+
Multi-Gigabit (1G/2.5G) RJ-45 user ports
0
0
2 (HPoE+)
2 (HPoE+)
Combo Gigabit RJ-45/SFP ports
2
0
0
0
Combo 1G/10G RJ-45/SFP+ ports
2*
2
2
2*
SFP+ ports: 1G/10G uplink or VFL
2
2
2
2
Console port
1
1
1
1
USB/OoB management port 
1
1
1
1
Primary power 
Internal
Internal
Internal
Internal
Backup power 
N/A
N/A
N/A
N/A
Fans 
1
1
1
1
CPU
800MHz ARM v7
800MHz ARM v7
800MHz ARM v7
800MHz ARM v7
File system flash 
1 GB
1 GB
1 GB
1GB
RAM 
1 GB
1 GB
1 GB
1GB
Packet buffers
1.5MB
1.5MB
1.5MB
1.5MB
Performance aggregated 
Max switching 
ASIC capacity
128 Gb/S
128 Gb/S
182 Gb/S
182 Gb/S
Stacking capacity
92 Gb/s
128 Gb/s
182 Gb/s
146 Gb/S
Throughput 
68.5 Mpps
95.3 Mpps
135.4 Mpps
217 Mpps
2x10GE VFL capacity
40 Gb/s
40 Gb/s
40 Gb/s
40 Gb/s 
System power consumption:
•	 Idle
•	 100% traffic all ports (max)
 
34 W 
46 W
 
34 W 
46 W
 
60 W 
76 W
 
60 W 
76 W
System heat dissipation (max)
157 (BTU/h)
157 (BTU/h)
269 (BTU/h)
269 (BTU/h)
Power consumption w/PoE 
446 W
446 W
879 W
879 W
Heat dissipation w/PoE 
1521 (BTU/h)
1521 (BTU/h)
2999 (BTU/h)
2999 (BTU/h)
Power supply efficiency (max load)
95.7%
95.7%
95.6%
95.6%
Acoustics db(A) @25C
38 db(A)
38 db(A)
41-49 db(A)
41-49 db(A)
# of fans
1
1
1
1
MTBF (hours) @ 25C
1,447 k
1,447 k
789 k
789 k
Height 
4.4 cm (1.73 in)
4.4 cm (1.73 in)
4.4 cm (1.73 in)
4.4 cm (1.73 in)
Width 
4.4 cm (17.33 in)
4.4 cm (17.33 in)
44 cm (17.33 in)
44 cm (17.33 in)
Depth 
30 cm (11.8 in)
30 cm (11.8 in)
30 cm (11.8 in)
30 cm (11.8 in)
Weight 
3.9 kg (8.5 lbs)
3.9 kg (8.5 lbs)
4.4 kg (9.7 lbs)
4.4 kg (9.7 lbs)
Operating temperature 
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)
0°C to 45°C 
(32°F to 113°F)
Storage temperature 
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
-40°C to 85°C 
(-40°F to 185°F)
Humidity (operating)
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing

<<<PAGE 489>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Commercial references
OmniSwitch 6360 models
OS6360-10
Fixed 1RU ½ rack chassis 8 RJ-45 10/100/1G BaseT, 2 10/100/1G BaseT, 2 SFP ports. Fan-less, optional mounting.
OS6360-P10
Fixed 1RU ½ rack chassis 8 RJ-45 PoE 10/100/1G BaseT, 2 10/100/1G BaseT, 2 SFP ports. 120W power budget, fanless, 
optional mounting.
OS6360-24
Fixed 1RU chassis 24 RJ-45 10/100/1G BaseT, 2 fixed RJ45/SFP combo (1G), 2 SFP+ (1G/10G) uplink or VFL 
ports. Fanless.
OS6360-P24
Fixed 1RU chassis 24 RJ-45 PoE 10/100/1G BaseT, 2 RJ45/SFP combo (1G), 2 SFP+ (1G/10G) uplink or VFL ports. 180W 
power budget, fanless.
OS6360-48
Fixed 1RU chassis 48 RJ-45 10/100/1G BaseT, 2 RJ45/SFP combo (1G), 2 SFP+ (1G/10G) uplink or VFL ports.
OS6360-P48
Fixed 1RU chassis 48 RJ-45 PoE 10/100/1G BaseT, 2 RJ45/SFP combo (1G), 2 SFP+ (1G/10G) uplink or VFL ports. 350W 
power budget.
OS6360-PH24
Fixed 1RU chassis 24 RJ-45 PoE 10/100/1G BaseT, 2 1G* RJ45/SFP combo, 2 SFP+ (1G/10G) uplink or VFL ports. 380W 
power budget. *10G license upgradeable.  
OS6360-PH48
Fixed 1RU chassis 46 RJ-45 PoE 10/100/1G BaseT, 2 RJ-45 PoE 1G/2.5G BaseT, 2 1G* RJ45/SFP combo,
2 SFP+ (1G/10G) uplink or VFL ports. 760W power budget. *10G license upgradeable.
OS6360-P24X
Fixed 1RU chassis 24 RJ-45 PoE 10/100/1G BaseT, 2 1G/10G RJ45/SFP combo, 2 SFP+ (1G/10G)  uplink or VFL ports. 
380W power budget.  
OS6360-P48X
Fixed 1RU chassis 46 RJ-45 PoE 10/100/1G BaseT, 2 RJ-45 PoE 1G/2.5G BaseT, 2 1G/10G RJ45/SFP combo, 2 SFP+ 
(1G/10G) uplink or VFL ports. 760W power budget. 
OmniSwitch 6360 license options
OS6360-SW-PERF
Performance software license allowing the 2xRJ45/SFP combo ports of the OS6360-PH24/PH48 only to operate at 
10G speed.
OmniSwitch 6360 10G transceivers and cables
OS6360-CBL-60CM
10 Gigabit direct attached uplink/stacking copper cable (60 cm, SFP+).
OS6360-CBL-C1M
10 Gigabit direct attached uplink/stacking copper cable (1 m, SFP+).
OS6360-CBL-C3M
10 Gigabit direct attached uplink/stacking copper cable (3 m, SFP+).
SFP-10G-SR
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 850 nm wavelength (nominal) with an LC 
connector. Typical reach of 300 m. 
SFP-10G-LR
10 Gigabit optical transceiver (SFP+). Supports single mode fiber with an LC connector. Typical reach of 10 Km.
SFP-10G-ER
10 Gigabit optical transceiver (SFP+). Supports single-mode fiber over 1550 nm wavelength (nominal) with an LC 
connector. Typical reach of 40 km.
SFP-10G-BX-D
10 Gigabit optical transceiver (SFP+) with an LC type of interface. This bi-directional transceiver is designed
for use over single mode fiber optic on a single strand link up to 10 km. Transmits 1270 nm and receives
1330 nm optical signal.
SFP-10G-BX-U
10 Gigabit optical transceiver (SFP+) with an LC type of interface. This bi-directional transceiver is designed
for use over single mode fiber optic on a single strand link up to 10 km. Transmits 1330 nm and receives
1270 nm optical signal.
OmniSwitch 6360 Gigabit transceivers
SFP-GIG-T
1000Base-T Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and full-duplex mode.
SFP-GIG-SX
1000Base-SX Gigabit Ethernet optical transceiver (SFP MSA).
SFP-GIG-LX
1000Base-LX Gigabit Ethernet optical transceiver (SFP MSA).
SFP-GIG-LH40
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on 9/125 µm SMF. 
SFP-GIG-LH70
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on 9/125 µm SMF.
OmniSwitch 6360 10 port mounting options
OS6360-RM-19-L
Simple L-bracket for mounting a single OS6360-10/-P10 switch in a 19 rack.
OS6360-WALL-MNT
Wall mounting kit for OS6360 products. Contains universal mounting brackets and screws for wall mounting a 
OS6360 switch.

<<<PAGE 490>>>
7
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Warranty
The OmniSwitch 6360 family comes with a Limited Lifetime Warranty.
Detailed product features
Simplified management
•	 Intuitive CLI in a scriptable BASH 
environment via console, Telnet or 
Secure Shell (SSH) v2 over IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over IPv4/ 
IPv6+
•	 Fully programmable RESTful web 
services interface with XML and JSON 
support. API enables access to CLI and 
individual mib objects.
•	 Integrated with Alcatel-Lucent 
OmniVista products for network 
management
•	 Full configuration and reporting using 
SNMPv1/2/3 to facilitate third-party 
network management over IPv4/IPv6
•	 File upload using USB, TFTP, FTP, SFTP or 
SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line editing, 
bulk configuration and out-of-the-box 
auto-provisioning
•	 Multiple microcode image support with 
fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server managed 
by Alcatel-Lucent DNS/DHCP IP address 
management
Monitoring and troubleshooting
•	 Local (on the flash memory) and remote 
server logging (Syslog): event and 
command logging
•	 IP tools: ping and trace route
•	 Loopback IP address support for 
management per service
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD) 
and Digital Diagnostic Monitoring (DDM) 
•	 Loopback Detection (LBD)
Network configuration
•	 Zero-touch provisioning and 
provisioning based on templates using 
OV2500/OVCirrus
•	 Auto-negotiating 10/100/1000 ports 
automatically configure port speed and 
duplex setting
•	 Auto MDI/MDIX automatically configures 
transmit and receive signals to support 
straight-through and crossover cabling
•	 BOOTP/DHCP client allows auto-
configuration of switch IP information 
for simplified deployment
•	 DHCP relay to forward client requests to 
a DHCP server
•	 IEEE 802.1AB Link Layer Discovery 
Protocol (LLDP) with MED extensions for 
automated device discovery
•	 Multiple VLAN Registration Protocol 
(MVRP) for IEEE 802.1Q-compliant VLAN 
pruning and dynamic VLAN creation
•	 Auto QoS for switch management traffic 
as well as traffic from  
Alcatel-Lucent IP phones
•	 Network Time Protocol (NTP) for 
network- wide time synchronization
•	 Virtual chassis up to 4 units of 24 and 48 
port models
Resiliency and high availability
•	 Unified management, control, and 
virtual chassis technology
•	 Virtual Chassis 1+N redundant 
supervisor manager
•	 Virtual Chassis In-Service Software 
Upgrade (ISSU)
•	 Smart continuous switching technology
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning Tree 
Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+) and 
1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link Aggregation 
Control Protocol (LACP) and static LAG 
groups across modules
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection: Auto- 
detection and recovery of Virtual Chassis 
splitting due to one or more VFL or 
stack element failures
Advanced security
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive user-
policy-based NAC
•	 Autosensing IEEE 802.1X multi-client, 
multi-VLAN support
•	 MAC-based authentication for non-IEEE 
802.1X hosts
•	 Web-based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing pre-defined 
policy configuration to authenticated 
clients — VLAN, ACL, BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial-In 
User Service (RADIUS) and Lightweight 
Directory Access Protocol (LDAP) 
administrator authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-based 
filtering in hardware (Layer 1 to Layer 4)
•	 DHCP Snooping, DHCP IP and Address 
Resolution Protocol (ARP) spoof 
protection
•	 ARP poisoning detection
•	 IP source filtering as a protective and 
effective mechanism against ARP attacks
•	 BYOD provides on-boarding of guest, 
IT/non-IT issued and silent devices; 
restriction/remediation of traffic from 
non-compliant devices. RADIUS CoA 
dynamically enforces User Network 
Profiles based on authentication, 
profiling, posture check of devices using 
Unified Policy Access Manager (UPAM),  
or Aruba ClearPass Policy Access 
Manager (CPPM).

<<<PAGE 491>>>
8
Datasheet 
Alcatel-Lucent OmniSwitch 6360 
Converged networks
PoE
•	 PoE models support Alcatel-Lucent IP 
phones and WLAN access points, as well 
as any IEEE 802.3af, IEEE 802.3at, or 
802.3bt compliant end device
•	 Configurable per-port PoE priority and 
max power for power allocation
•	 Dynamic PoE allocation: Delivers only 
the power needed by the powered 
devices (PD) up to the total power 
budget for most efficient power 
consumption
QoS
•	 Priority queues: Eight hardware-based 
queues per port for flexible QoS 
management
•	 Traffic prioritization: Flow-based QoS 
with internal and external (also known 
as remarking) prioritization
•	 Bandwidth management: Flow-based 
bandwidth management; ingress rate 
limiting; egress rate shaping per port
•	 Queue management: Configurable 
scheduling algorithms — Strict Priority 
Queuing (SPQ), Weighted Round  
Robin (WRR)
•	 Congestion avoidance: Support for  
End- to-End Head-Of-Line (E2E-HOL) 
blocking protection
•	 Auto QoS for switch management traffic 
as well as traffic from Alcatel-Lucent IP 
phones
Layer-2, Layer-3 routing and 
multicast
Layer-2 switching
•	 Up to 16k MAC addresses
•	 Up to 4000 VLANs
•	 Up to 1.5k total system policies
•	 Latency: < 4 µs
•	 Max frame: 9216 bytes (jumbo)
IPv4 and IPv6
•	 Static routing for IPv4 and IPv6
•	 Up to 64 IPv4 and 4 IPv6 static routes
•	 Up to 32 IPv4 and 4 IPv6 interfaces
Multicast
•	 IGMPv1/v2/v3 snooping to optimize 
multicast traffic
•	 Multicast Listener Discovery (MLD) v1/
v2 snooping
•	 Up to 1000 multicast groups
Network protocols
•	 DHCP relay (including generic  
UDP relay)
•	 ARP
•	 Generic User Datagram Protocol (UDP) 
relay per VLAN
•	 DHCP Option 82 - configurable relay 
agent information
Indicators
System LEDs 
•	 System (OK) (chassis HW/SW status)
•	 PWR (primary power supply status)
•	 VC (virtual chassis primary)
Per-port LEDs
•	 10/100/1000: PoE, link/activity
•	 100/1000/2.5GE: link/activity/ 
PoE status
•	 SFP: Link/activity
•	 Virtual Chassis (VFL): Link/activity
Compliance and certifications
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart B 
(Class A)
•	 VCCI (Class A limits. Note: Class A with 
UTP cables)
•	 ICES–003: 2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) - C-Tick
•	 AS/NZS 3548 (Class A limits.  
Note: Class A with UTP cables)
•	 CE-Mark: Marking for European 
countries (Class A limits. Note: Class A 
with UTP cables)
•	 CE emission consists of:
	
¬ EN 50581: Standard for technical 
documentation for Restriction on 
Hazardous Substances (RoHS) recast
	
¬ EN 55022 (EMI and EMC requirement) 
	
¬ EN 55024: 2010 (ITE immunity 
characteristics)
	
¬ EN 61000-3-2 (Limits for harmonic 
current emissions)
	
¬ EN 61000-3-3
	
¬ EN 61000-4-2
	
¬ EN 61000-4-3
	
¬ EN 61000-4-4
	
¬ EN 61000-4-5
	
¬ EN 61000-4-6
	
¬ EN 61000-4-8
	
¬ EN 61000-4-11
	
¬ IEEE802.3: Hi-Pot Test (2250 V DC on 
all Ethernet ports)
Safety agency certifications
•	 CDRH laser
•	 Compliant with RoHS and Waste 
Electrical and Electronic Equipment 
(WEEE) directives
•	 EN 60825-1 laser
•	 EN 60825-2 laser
•	 IEC 62368-1
•	 UL 60950-1, 2nd edition, Information 
Technology Equipment
•	 CAN/CSA C22.2 No. 60950-1-07, 
2nd edition, Information Technology 
Equipment
•	 IEC 62368-1:2018, ICT and AV 
equipment safety, with all national 
deviations 
•	 IEC 60950-1, with all national deviations 
	
¬ UL-AR, Argentina
	
¬ AS/NZ TS-001 and 60950, Australia
	
¬ ANATEL, Brazil
	
¬ CCC, China
	
¬ UL-GS Mark, Germany
	
¬ KCC, Korea
	
¬ NOM-019 SCFI, Mexico
	
¬ CU, EAC, Russia
	
¬ BSMI, Taiwan
Supported standards
IEEE standards
•	 IEEE 802.1D (STP)
•	 IEEE 802.1p (CoS)
•	 IEEE 802.1Q (VLANs)
•	 IEEE 802.1s (MSTP)
•	 IEEE 802.1w (RSTP)
•	 IEEE 802.1X (Port Based Network Access 
Protocol)
•	 IEEE 802.3i (10Base-T)
•	 IEEE 802.3u (Fast Ethernet)
•	 IEEE 802.3x (Flow Control)
•	 IEEE 802.3z (Gigabit Ethernet)
•	 IEEE 802.3ab (1000Base-T)
•	 IEEE 802.3ac (VLAN Tagging)
•	 IEEE 802.3ad (Link Aggregation)
•	 IEEE 802.3ae (10 Gigabit Ethernet)
•	 IEEE 802.3af (Power-over-Ethernet)
•	 IEEE 802.3at (Power-over-Ethernet)
•	 IEEE 802.3bt (Power-over-Ethernet)
•	 IEEE 802.3az (Energy Efficient Ethernet)
•	 IEEE 802.3bz (2.5GE Multi-Gigabit 
Ethernet)
IETF RFCs
IP Multicast
•	 RFC 1112 IGMP v1
•	 RFC 2236/2933 IGMP v2 and MIB
•	 RFC 2365 Multicast
•	 RFC 3376 IGMPv3 for IPv6
IPv6
•	 RFC 1886 DNS for IPv6
•	 RFC 2292/2373/2374/2460/2462
•	 RFC 2461 NDP
•	 RFC 2463/2466 ICMP v6 and MIB
•	 RFC 2452/2454 IPv6 TCP/UDP MIB
•	 RFC 2464/2553/2893/3493/3513

<<<PAGE 492>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view 
other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trademarks-copyright. All 
other trademarks are the property of their respective owners. The information presented is subject to change without notice. 
Neither ALE Holding nor any of its affiliates assumes any responsibility for inaccuracies contained herein. © Copyright 2022  
ALE International, ALE USA Inc. All rights reserved in all countries. DID20121401EN (April 2022)
•	 RFC 3056 IPv6 Tunneling
•	 RFC 3542/3587 IPv6
•	 RFC 4007 IPv6 Scoped  
Address Architecture
•	 RFC 4193 Unique Local IPv6  
Unicast Addresses
Manageability 
•	 RFC 854/855 Telnet and Telnet options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP
•	 RFC 1155/2578-2580 SMI v1 and SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP Traps
•	 RFC 1573/2233/2863 Private  
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload 
 in HTML
•	 RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from Forms: 
multipart/form-data
•	 RFC 2396 Uniform Resource Identifiers 
(URI): Generic Syntax
•	 RFC 2570-2576/3410-3415/3584  
SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 3826 (AES) Cipher Algorithm in the 
SNMP User-based Security Model
•	 RFC 4122 A Universally Unique Identifier 
(UUID) URN Namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP Status Codes 
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and crypto 
algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618 
RADIUS Authentication and Client MIB
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 4301 Security Architecture for IP
Quality of service
•	 RFC 896 Congestion control
•	 RFC 1122 Internet hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 3635 Pause control
Others
•	 RFC 791/894/1024/1349 IP and IP/
Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 NTP v3 and Simple NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow 
Services and support
For more information about Alcatel-Lucent Enterprise professional services, support services, and managed 
services, please go to https://www.al-enterprise.com/en/services/support-services.

<<<PAGE 493>>>
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Alcatel-Lucent
OmniSwitch 6465 
Compact hardened ethernet switches
The Alcatel-Lucent OmniSwitch 6465 is a  
family of ruggedized, fully manageable and  
fan-less Gigabit Ethernet switches. Designed for 
Industrial Ethernet applications, these hardened 
ethernet family offers a range of DIN rail and 19” 
rack mountable switches that are ideal for a wide 
variety of Industrial applications such as Intelligent 
Transportation, Railway, smart cities and Utilities. 
OS6465-P6
OS6465-P12
OS6465 switches are a family of hardened, compact, fan-less gigabit Ethernet switches that have been designed 
specifically for industrial applications. The switches run on the widely deployed and field-proven Alcatel-Lucent 
Operating system that offers high security, reliability, performance and easy management. These switches are 
designed to operate in extended temperatures, offer higher EMI/EMC tolerance, a flexible range in power inputs 
options and high surge protection.              
The OS6465 series offers advanced PoE capabilities with 60W PoE per port and Fast / Perpetual PoE* support 
to power range of new age devices from PTZ IP cameras on toll booths, LED lights and building management 
gateways in smart buildings to industrial control systems. These switches are easy to deploy and offer out-of-the-
box plug-and-play, Zero-touch provisioning, network automation and disaster recovery options. These switches 
support IEEE 1588v2 PTP for the nanosecond-level precision timing requirements of industrial devices and 
applications. With support for MACSec on all ports, OS6465 enables end-to-end encrypted networks. The OS6465 
family offers advanced system and network level resiliency features and convergence through standardized 
protocols in a space efficient form factor. 
These versatile industrial switches are ideal for deployment in transportation and traffic control systems, utilities, 
IP surveillance systems and outdoor installations, to name a few.
OS6465-P28

<<<PAGE 494>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Features
Benefits
•	Designed for Industrial applications
•	Operates at a wider temperature range from -40°C to +75°C, withstands greater 
shock, vibrations, surge and EMI/EMC variance
•	Redundant power supply inputs with standard 1x 3 terminal block 
•	Alarm relays to connect external alarm systems
•	Compact DIN rail mountable design
•	Convection cooled fan-less models
•	Fan-less operations increases resiliency and maximizes uptime for converged 
mission-critical networks
•	Advanced Industrial PoE capabilities with support 
for IEEE 802.3bt PoE (60 W) on all models and 
Fast / Perpetual PoE * support
•	Enables converged deployments and is ideal for all type of PoE application 
requirements from outdoor wireless APs, to PTZ surveillance cameras and  video 
displays
•	Virtual Chassis to connect multiple switches for 
creating a single chassis-like entity
•	Increases system redundancy, resiliency and system scalability while simplifying 
deployment, operations and management of the network
•	Hot-swappable, fully redundant power supplies
•	Delivers redundant ring topologies using industry 
standard protocols
•	Field upgradable, highly redundant network solution maximizes network uptime
•	Switch Backup & Restore
•	Simplifying switch replacement in field and minimizing network downtime using USB 
drive. Encryption of USB ensures optimal security.
•	IEEE 1588v2 PTP support
•	Support for peer-to-peer and end-to-end transparent clock provides precise 
nanosecond time synchronization for devices on industrial networks
•	Simplified installation and service provisioning
•	Out-of-the-box Zero-touch provisioning and network automation with automatic 
protocol and topology discovery
•	MACSec Support
•	MACSec encryption support provides a secure network access ensuring data 
confidentiality & integrity 
* select models
Alcatel-Lucent OmniSwitch 6465 models
The OmniSwitch 6465 family offers customers an extensive selection of Gigabit fixed-configuration switches with 
up to 60 watts of PoE per port and power supply options that accommodate the most demanding requirements. 
The models can be mounted on DIN rail, 19” rack or a wall/panel.
All the models of OS6465 family support IEEE 802.3bt compliant 60W PoE, IEEE1588v2 PTP (peer-to-peer & end-
to-end transparent clock), MACSec and Alarm relays. All ports of OS6465-P6 and OS6465-P12 are capable of IEEE 
1588v2 and MACSec. All ports of OS6465-P28 are capable of IEEE 1588v2 & MACSec (except ports 27, 28). OS6465 
switches offer a surge protection of 6KV on all copper ports. OmniSwitch 6465 switches can form a Virtual Chassis 
between any models creating a single chassis-like entity using 1G SFP ports. OS6465-P28 switches can form a 
virtual chassis using 10G SFP+ ports. Up to 4 switches can be connected in a Virtual Chassis configuration with 
option to scale up to 8 in future.
Gigabit 
ports (RJ45)
SFP ports
1G/10G 
SFP+ ports
PoE Ports
60W, 30W
Description
OS6465-P6
4
2
0
2, 2
Fixed-configuration hardened fan-less compact DIN-mount 
chassis with four 10/100/1000 Base-T PoE+ ports, two of which 
can support 60W PoE, and two 100/1000 Base-X SFP ports.
OS6465-P12
8
4
0
4, 4
Fixed-configuration hardened fan-less compact DIN-mount 
chassis with eight 10/100/1000 Base-T PoE+ ports, four of which 
can support 60W PoE, and four 100/1000 Base-X SFP ports.
OS6465-P28
22
2
4
8, 14
Fixed-configuration hardened fan-less 19” rack width chassis 
with 22 10/100/1000 Base-T PoE+ ports, eight of which can 
support 60W HPoE, two 100/1000 Base-X SFP ports, and four 
1G/10G SFP+ ports.

<<<PAGE 495>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Technical specifications
OmniSwitch 6465 models
Product matrix
OS6465-P6
OS6465-P12
OS6465-P28
Operating temperature
-40°C to 75°C  
(-40°F to 167°F)
-40°C to 75°C  
(-40 °F to 167°F)
-40°C to 75°C  
(-40 °F to 167°F)
Fans
0
0
0
File system flash
1 GB
1 GB
1 GB
RAM
1 GB
1 GB
1 GB
Max switching capacity
12 Gb/s
24 Gb/s
128 Gb/s
Forwarding capacity
8.9 Mpps
17.9 Mpps
95.3 Mpps
Weight (no PS attached)
2.08 Kg (4.6 lbs)
2.13 Kg (4.7 lbs)
5.71 Kg (12.6 lbs)
Height
15 cm (5.9 in)
15 cm (5.9 in)
4.4 cm (1.73 in)
Width
8.0 cm (3.15 in)
8.0 cm (3.15 in)
44 cm (17.4 in)
Depth (no PS attached)
15 cm (5.9 in)
15 cm (5.9 in)
27 cm (10.62 in)
1588v2 capable ports
6
12
26
MACsec capable ports
6
12
26
USB port
1
1
1
Console port
1
1
1
Alarm relay contacts
1 in, 1 out
1 in, 1 out
1 in, 1 out
PSU connectors
2
2
2
Max PoE budget*
150 W
240 W
285 W
Altitude
13,000 ft
13,000 ft
13,000 ft
Storage temperature
-40°C to 85°C  
(-40°F to 185°F)
-40°C to 85°C  
(-40°F to 185°F)
-40°C to 85°C  
(-40°F to 185°F)
Humidity (operating & storage)
5% to 95% non-condensing
5% to 95% non-condensing
5% to 95% non-condensing
Power consumption (idle)**
9.72 W
11.79 W
29 W
Power consumption (full load)**
15.99 W
18.71 W
32.19 W
Heat dissipation (BTU/hr)**
33.16
40.22
98.95
Maximum surge protection ***
6 KV
6 KV
6 KV
MTBF (hours) (Switch only)  
1,452,904	
1,421,933
2,103,668
MTBF (hours) (switch+2 AC PSU)****
401,280
399,336
1,136,119
Mounting options	
DIN/Wall/Panel
DIN/Wall/Panel
19” rack
* At 60°C.  240W PoE budget is available only on new models of OS6465-P12 when ordered with references OS6465H-P12 or OS6465H-P12-xx. OS6465-P12 models ordered with 
references OS6465-P12 and OS6465-P12-xx have 150W PoE budget. Please refer to HW user’s guide for more information. 
**Consumption measured at 120 VAC input. Full load measurement does not include PoE power consumption. Heat dissipation measured at idle.
*** On RJ45 user ports
**** MTBF values for OS6465-P6, OS6465-P12 are calculated with two OS6465-BPN PSU and for OS6465-P28 with two OS6465-BPR PSU.
Switch dimensions
Unit: mm
OS6465-P6/OS6465-P12

<<<PAGE 496>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Switch power input specifications
OmniSwitch 6465-P6 and OS6465-P12 models support dual redundant, 1x3 terminal block inputs for power 
supplies in the front with three wire input cables : +VDC, -VDC and ground. 
These switches can be powered with a Power Supply whose output meets the input specifications of OS6465-P6 
and OS6465-P12 given below. When both input ports (PS1) and (PS2) are used, both inputs shall be powered by 
UL listed power supplies only. Please refer to the latest hardware user guide for more details.
OS6465-P6/OS6465-P12
Input voltage range
Maximum current
PoE type supported
54.5 V to  57 V 
3.5 A 
 IEEE 802.3 bt (60W)
50 V to 57 V
3.5 A
IEEE 802.3 at (30 W) 
44 V to 57 V
3.5 A
IEEE 802.3 af (15 W) 
24 V to 60 V
1.5 A
System power only
OS6465 power supplies
OmniSwitch 6465-P6 and OS6465-P12 models support a range of AC power supplies with 240W, 150W & 
45W PoE budget per switch. PoE budget of 240W is available only on OS6465-P12 switch (orderable through 
references OS6465H-P12 and OS6465H-P12-XX) when used with power supply model OS6465H-BPNX. Please 
refer to the power supply datasheet for more details. In addition, P6 and P12 switches have been functionally 
tested with third party DC power supplies for inter-operability. In a redundant configuration, power supplies can 
be installed in any manner AC+AC, AC+DC or DC+DC. 
PS models
OS6465-BPN
OS6465-BPN-H
Description
Modular AC power supply. Provides up to 75 W 
of system and PoE power to one OS6465-P6 or 
OS6465-P12 switch 
Modular AC DIN Mount Power supply. 
Provides up to 180 W of system and  
PoE power to one OS6465-P6 or  
OS6465-P12 switch
Dimensions (H x W x D)
12.52 cm x 3.2 cm x 10.2 cm
(4.93 in x 1.26 in x 4.01 in)
12.52 cm x 6.3 cm x 11.35 cm
(4.93 in x 2.48 in x 4.47 in)
Weight 
0.51 kg (1.12 lbs)
1.03 kg (2.27 lbs)
Input voltage
100 VAC to 240 VAC
100 VAC to 240 VAC       
Input current
1.55A
2.6A
Max output power
75 W
180 W
OS6465-P28

<<<PAGE 497>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 6465
PS models
OS6465-BPN
OS6465-BPN-H
Surge protection
Surge Level 4: 
4 KV Line to ground
2 KV Line to Line
Surge Level 4: 
4 KV Line to ground
2 KV Line to Line
Fans
0
0
Operating temp
-40°C to 70°C
-40°C to 70°C
Mounting
DIN
DIN
PoE type supported
IEEE 802.3 at (30 W)
IEEE 802.3 af (15 W)
IEEE 802.3bt (60W)
IEEE 802.3 at (30 W)
IEEE 802.3 af (15 W)
PS models
OS6465-BPR  
OS6465-BPRD
Description
Modular AC rack mount power supply. Provides 
up to 180 W of system and PoE power to one 
OS6465-P28 switch
Modular DC rack mount Power supply. 
Provides up to 180 W(@48V input)/140W 
(@24V Input) of system and PoE power to  
one OS6465-P28 switch
Dimensions (H x W x D)
5.1 cm x 9.5 cm x 18.1 cm
(2 in x 3.74 in x 7.12 in)
5.1 cm x 9.5 cm x 18.1 cm
(2 in x 3.74 in x 7.12 in)
Weight 
1.42 kg (3.14 lbs)   
1.42 kg (3.14 lbs)   
Input voltage
100 VAC to 240 VAC
-20 VDC to -72 VDC     
Input current
3A/100V to 127 VAC 
1.5A/200V to 240 VAC  
12A/-20V to -28 VDC
6A/-36V to -72 VDC
Max output power
180 W
180 W
Surge protection
Surge Level 4: 
4 KV Line to ground
2 KV Line to Line
Surge Level 4: 
2 KV Line to ground
1 KV Line to Line
Fans
0
0
Operating temp
-40°C to 75°C
-40°C to 75°C
Mounting
19” Rack
19” Rack
PoE type supported
IEEE 802.3bt (60 W) 
IEEE 802.3-at (30 W) 
IEEE 802.3-af (15 W)
IEEE 802.3bt (60 W)
IEEE 802.3-at (30 W)
IEEE 802.3-af (15 W)
Product specifications 
and measurements
Per-port LEDs
•	 Non-PoE ports - green: link/activity
•	 PoE ports - amber: link/activity
System LEDs
•	 OK: green/amber operational status of 
the switch
•	 VC: green/amber master or slave role 
in VC configuration. Number of blinks 
identify stacking unit number
•	 PS1: Green/Amber - status for  
the primary power supply
•	 PS2: Green/Amber - status for  
the backup power supply
•	 ALRM IN: Amber when alarm in
•	 ALRM OUT: Amber when alarm out
Scalability numbers and 
speeds
•	 Wire rate at layer 2 and layer 3  
on all ports
•	 Jumbo frame size: 9216 bytes  
(for 1 Gb/s)
•	 Total number of MAC addresses: 16 K 
•	 Total number of IPv4 routes: 128 
•	 Number of VLANs: 4,000
Virtual chassis
•	 Maximum number of units in  
a VC: 4
•	 Remote VC connection: using  
iSFP-GIG-SX, iSFP-GIG-LX
Compliance and 
certifications
Commercial safety
•	 IEC 62368-1
•	 UL 60950-1, 2nd Ed.
•	 IEC 60950-1; all national deviations
•	 EN 60950-1; all deviations
•	 CAN/CSA-C22.2 No. 60950-1-03
•	 NOM-019 SCFI, Mexico
•	 AS/NZ TS-001 and 60950:2000, Australia
•	 UL-AR, Argentina
•	 UL-GS Mark, Germany
•	 CU, EAC, Russia
•	 ANATEL, Brazil
•	 CCC, China
•	 KCC Korea
•	 BSMI, Taiwan
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 CDRH Laser
•	 RoHS and WEEE directives compliant
•	 REACH directive

<<<PAGE 498>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart B (Class 
A)VCCI (Class A, with UTP Cables)
•	 ICES–003:2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) – C-Tick
•	 CE marking for European countries 
(Class A)
•	 CE Emission
¬	 EN50581 (RoHS Recast)
¬	 EN 55032 (EMI & EMC requirement)
¬	 EN 55024 (Immunity Characteristics)
¬	 EN 61000-3-2(Harmonic Current 
emissions)
¬	 EN 61000-3-3
¬	 EN 61000-4-2
¬	 EN 61000-4-3
¬	 EN 61000-4-4
¬	 EN 61000-4-5  
(Surge Immunity, Class 4)
¬	 EN 61000-4-6
¬	 EN 61000-4-8
¬	 EN 61000-4-9
¬	 EN 61000-4-11
¬	 IEEE802.3: Hi-pot Test  
(2.25 KV DC on all Ethernet Ports)
Industrial
Industrial environmental
•	 IEC 60870-2-2 (operational temperature)
•	 IEC 60068-2-1 (temperature type  
test – cold)
•	 IEC 60068-2-2 (temperature type test – 
hot)
•	 IEC 60721-3-1: Class 1K5 (storage 
temperature)
•	 IEC 60068-2-30: 5% to 95%  
non-condensing humidity
•	 IEC 60255-21-2 (mechanical shock)
•	 IEC 60255-21-1 (vibration)
Industrial safety
•	 UL 508
•	 UL 61010
•	 EN 50021
•	 Hazardous location
¬	 ISA 12.12.01 (UL 1604)  
(Class l, Div 2, groups A-D) 
¬	 CSA22.2/213  
(Class l, Div 2, groups A-D)  
•	 IP30
Industrial emission
•	 EN 61805-3
•	 EN 55032 (Emission Standard)
•	 EN 61000-3-2
•	 EN 61000-3-3
•	 EN 55024/EN 55035 (Immunity 
Standard)
•	 EN 61000-4-2 to EN 61000-4-8
•	 EN 61000-4-11
•	 EN 61000-4-12
•	 EN 61000-4-16
•	 EN 61000-4-17
•	 EN 61000-4-29
•	 IEC 60255-5
•	 IEEE 1613
Industry specific
Electric power substation
•	 IEEE 1613, Section 4 to 8
•	 IEC 61850-3
Railway applications
•	 EN 50121-4
•   EN 50155:2017
•   EN 61373
•	 EN 62236-4
•	 EN61000-6-4
•	 EN61000-6-2
Intelligent transportation (road)
•	 NEMA TS-2
Marine certifications
•	 DNVGL-CG-0339†
•  IEC 60945:2002†
† Requires mandatory DNV kit for compliance
Federal certifications
•	  Trade Agreements Act (TAA)
Detailed product features
Simplified manageability  
and configuration
•	 Intuitive CLI in a scriptable Python & BASH 
environment via console, Telnet or Secure 
Shell (SSH) v2 over IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over  
IPv4/IPv6
•  Network Automation and 
Programmability Abstraction Layer with 
Multivendor (NAPALM) support
•	 Fully programmable RESTful web 
services interface with XML and JSON 
support. API enables access to CLI and 
individual mib objects
•	 Integrated with Alcatel-Lucent 
OmniVista® products for network 
management
•	 Integrated with Nokia Network 
Services Platform (NSP)© for network 
management  
•	 Full configuration and reporting using 
SNMPv1/2/3 to facilitate third-party 
network management over IPv4/IPv6
•	 File upload using USB, TFTP, FTP, SFTP or 
SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line editing, 
bulk configuration and  
out-of-the-box auto-provisioning
•	 Non-volatile memory for start-up 
configuration
•	 Multiple microcode image support with 
fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server managed 
by Nokia VitalQIP® DNS/DHCP IP 
Address Management
•	 Access to the AOS console via USB 
Adapter with Bluetooth technology 
provides wireless management access, 
eliminating the need of console cables
Cloud ready with OmniVista® 
Cirrus   
•	 OmniVista® Cirrus offers a secure, 
resilient and scalable cloud-based 
network management. It offers hassle 
free network deployment and easy 
service roll-out with advanced analytics 
for smarter decision making. It provides 
IT friendly Unified Access with secure 
authentication and policy enforcement 
for users and devices.
Monitoring and 
troubleshooting
•	 Local (on the flash) and remote server 
logging (Syslog): event and command 
logging
•	 IP tools: ping and trace route
•	 Dying Gasp support via SNMP and 
syslog messages
•	 Loopback IP address support for 
management per service
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD), 
Digital Diagnostic Monitoring (DDM)
Resiliency and high 
availability
•	 Unified management, control and virtual 
chassis technology
•	 Virtual Chassis 1+N redundant 
supervisor manager
•	 Smart continuous switching technology
•	 ITU-T G.8032/Y1344 2010: Ethernet  
Ring Protection

<<<PAGE 499>>>
7
Datasheet 
Alcatel-Lucent OmniSwitch 6465
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning Tree 
Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+) and 
1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link Aggregation 
Control Protocol (LACP) and static LAG 
groups across modules
•  Dual-home link support for sub-second 
link protection without STP
•	 Virtual Router Redundancy Protocol
•	 (VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Redundant and hot-swappable  
power supplies
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection: Auto-
detection and recovery of Virtual Chassis 
splitting due to one or more VFL or 
stack element failures*
Advanced security
Switch software security
•	 AOS secured diversified code solution 
is available on OmniSwitch® 6465, 
hardening it at both the software source 
code and binary executable levels to 
enhance overall network security.
•	 AOS secured diversified code protects 
networks from intrinsic vulnerabilities, 
code exploits, embedded malware, 
and potential back doors that could 
compromise mission critical operations.
•	 AOS secured diversified code is a 
proactive, defense  approach toward 
network security that continuously 
defines and implements value-add 
capabilities to address both current and 
future threats. 
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive user-
policy-based NAC
•	 Autosensing IEEE 802.1X multi-client, 
multi-VLAN support
•	 MAC-based authentication for non-IEEE 
802.1X hosts
•	 Web based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing pre-defined 
policy configuration to authenticated 
clients — VLAN, ACL, BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial-In 
User Service (RADIUS) and Lightweight 
Directory Access Protocol (LDAP) 
administrator authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•	 Learned Port Security (LPS)  
or MAC address lockdown
•	 Access Control Lists (ACLs);  
flow-based filtering in hardware  
(Layer 1 to Layer 4)
•	 DHCP Snooping, DHCP IP and Address 
Resolution Protocol (ARP) spoof 
protection
•	 ARP poisoning detection
•	 IP Source Filtering as a protective and 
effective mechanism against  
ARP attacks
•	 LLDP Security mechanism for rogue 
device detection and restriction
QoS
•	 Priority queues: Eight hardware-based 
queues per port for flexible QoS 
management
•	 Traffic prioritization: Flow-based 
QoS Flow-based traffic policing and 
bandwidth management
•	 32-bit IPv4/128-bit IPv6 non-contiguous 
mask classification
•	 Egress traffic shaping
•	 DiffServ architecture
•	 Congestion avoidance: Support for end- 
to-end head-of-line (E2E-HOL) blocking 
prevention, IEEE 802.1Qbb Priority-
based Flow Control (PFC) and IEEE 
802.3x Flow Control (FC)
•  Auto-QoS support for Generic  
Object Oriented Substation Events 
(GOOSE) messages
Layer-3 routing and 
multicast
IPv4 routing
•	 Static routing
•	 Routing Information Protocol (RIP)  
v1 and v2
•	 Virtual Router Redundancy Protocol 
(VRRPv2)
•	 DHCP relay (including generic  
UDP relay)
•	 Address Resolution Protocol (ARP)
•	 Policy-based routing and server load 
balancing
•	 DHCPv4 server
IPv6 routing
•	 Internet Control Message Protocol 
version 6 (ICMPv6)
•	 Static routing
•	 Virtual Router Redundancy Protocol 
version 3 (VRRPv3)
•	 Neighbor Discovery Protocol (NDP)*
•	 Policy-based routing and server load 
balancing
•	 DHCPv6 server
IPv4/IPv6 multicast
•	 Internet Group Management Protocol 
(IGMP) v1/v2/v3 snooping
•	 Multicast Listener Discovery (MLD) v1/v2 
snooping
Advanced Layer-2 services
•	 Ethernet services support using IEEE 
802.1ad Provider Bridges (also known as 
Q-in-Q or VLAN stacking
•	 Ethernet OAM (802.1ag, ITU-T Y.1731): 
Connectivity Fault Management (L2 ping 
& Link trace)
•	 Ethernet in First mile: Link OAM 
(802.3ah)
•	 Ethernet network-to-network interface 
(NNI) and user network interface (UNI)
•	 Service Access Point (SAP) profile 
identification
•	 Service VLAN (SVLAN) and Customer 
VLAN (CVLAN) support
•	 VLAN translation and mapping including 
CVLAN to SVLAN
•	 Port mapping
•	 DHCP Option 82: Configurable relay 
agent information
•	 Multiple VLAN Registration Protocol 
(MVRP)
•	 HA-VLAN for Layer 2 clusters such 
as MS-NLB and active-active Firewall 
clusters* 
•	 Customer Provider Edge (CPE) test head 
traffic generator and analyzer tool
•	 TR-101 Point-to-Point Protocol over 
Ethernet (PPPoE) Intermediate Agent 
allowing for the PPPoE network  
access method
•	 Service Assurance Agent (SAA) for 
proactively measuring network health, 
reliability and performance.
•	 Jumbo frame support
•	 Bridge Protocol Data Unit (BPDU) 
blocking
•	 STP Root Guard
*Future support

<<<PAGE 500>>>
8
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Supported standards
IEEE standards
•	 IEEE 802.1D STP
•	 IEEE 802.1p CoS
•	 IEEE 802.1Q VLANs
•	 IEEE 802.1ab (LLDP)
•	 IEEE 802.1ag (OA&M)
•	 IEEE 802.1ad Provider Bridges Q-in-Q/ 
VLAN stacking
•	 IEEE 802.1ak (Multiple VLAN Registration 
Protocol (MVRP)
•	 IEEE 802.1s MSTP
•	 IEEE 802.3i 10BASE-T
•	 IEEE 802.1w RSTP
•	 IEEE 802.3x Flow Control
•	 IEEE 802.3z Gigabit Ethernet
•	 IEEE 802.3ab 1000Base-T
•	 IEEE 802.3ac VLAN Tagging
•	 IEEE 802.3ad/802.1AX Link Aggregation
•	 IEEE 802.3ae 10 GigE
•	 IEEE 802.3af Power over Ethernet
•	 IEEE 802.3at PoE Plus
•	 IEEE 1588v2 Precision Time Protocol
ITU-T recommendations
•	 ITU-T G.8032/Y.1344 2010: Ethernet 
Ring Protection (ERPv2)
•	 ITU-T Y.1731 OA&M fault and 
performance management
IETF RFCs
IPv4
•	 RFC 2131 Dynamic Host Configuration 
Protocol (DHCPv4)
•	 RFC 4022/2452 MIB for IPv4 TCP
•	 RFC 4113/2454 MIB for IPv4 UDP
•	 RFC 4292/4293 IPv4 MIBs
RIP
•	 RFC 1058 RIP v1
•	 RFC 1722/1723/2453/1724 RIP v2  
and MIB
•	 RFC 1812/2644 IPv4 Router 
Requirements
•	 RFC 2080 RIPng for IPv6
IP Multicast
•	 RFC 2365 Multicast
•	 RFC 2710/3019/3810/MLD v2  
for IPv6
•	 RFC 2933 IGMP MIB
•	 RFC 3376 IGMPv3 (includes IGMP v2/v1)
•	 RFC 4541 Considerations for IGMP and 
MLD Snooping Switches
•	 RFC 5132 Multicast Routing MIB
IPv6
•	 RFC 1981 Path MTU Discovery
•	 RFC 2460 IPv6 Specification
•	 RFC 2464 IPv6 over Ethernet
•	 RFC 2465 MIB for IPv6: Textual 
Conventions (TC) and General Group
•	 RFC 2466 MIB for IPv6: ICMPv6 Group
•	 RFC 3484 Default Address Selection
•	 RFC 3493/2553 Basic Socket API
•	 RFC 3542/2292 Advanced Sockets API
•	 RFC 3587/2374 Global Unicast  
Address Format
•	 RFC 3595 TC for IPv6 Flow Label
•	 RFC 3596/1886 DNS for IPv6
•	 RFC 4007 Scoped Address
•	 RFC 4022/2452 MIB for IPv6 TCP
•	 RFC 4113/2454 MIB for IPv6 UDP
•	 RFC 4193 Unique Local Addresses
•	 RFC 4213/2893 Transition Mechanisms
•	 RFC 4291/3513/2373 Addressing 
Architecture (uni/any/multicast)
•	 RFC 4292/4293 IPv6 MIBs
•  RFC 4443/2463 ICMPv6
•	 RFC 4861/2461 Neighbor Discovery*
•	 RFC 4862/2462 Stateless Address 
Autoconfiguration
•	 RFC 5095 Deprecation of Type 0 Routing 
Headers in IPv6*
Manageability
•	 RFC 854/855 Telnet and Telnet options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•  RFC 1155/2578-2580 SMI v1  
and SMI v2
•  RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•  RFC 1213/2011-2013 SNMP  
v2 MIB
•	 RFC 1215 Convention for SNMP Traps
•	 RFC 1573/2233/2863 Private  
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•  RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from Forms: 
multipart/form-data
•	 RFC 2396 Uniform Resource Identifiers 
(URI): Generic Syntax
•  RFC 2570-2576/3410-3415/3584  
SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•  RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 3826 (AES) Cipher Algorithm in the 
SNMP User-based Security Model
•	 RFC 4122 A Universally Unique IDentifier 
(UUID) URN Namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 6585 Additional HTTP Status Codes
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and  
crypto algorithms
•	 RFC 2104 HMAC Message Authentication
•	 RFC 2138/2865/2868/3575/2618 RADIUS 
Authentication and Client MIB
•  RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 4301 Security Architecture for IP
QoS
•	 RFC 896 Congestion Control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 2697 srTCM
•	 RFC 2698 trTCM
•	 RFC 3635 Pause Control
Others
•  RFC 791/894/1024/1349 IP  
and IP/Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030/5905 NTP v4 and  
Simple NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
*Future support

<<<PAGE 501>>>
9
Datasheet 
Alcatel-Lucent OmniSwitch 6465
•	 RFC 1541/1542/2131/3396/3442 DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•  RFC 2338/3768/2787 VRRP and MIB
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
•  RFC 4562 MAC-Forced Forwarding
Ordering information
Part number
  Description
OmniSwitch 6465  models
OS6465-P6
OS6465-P6: Hardened Gigabit Ethernet fixed configuration fan-less compact din-mount chassis with 4 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 2 ports are 60W PoE capable, 2 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes user manuals access 
card and hardware for mounting on a TS-35/7.5 or 15 DIN rail. Power supply shall be ordered separately.
OS6465-P6-xx
OS6465-P6-xx: Hardened Gigabit Ethernet fixed configuration fan-less compact  din-mount chassis with 4 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 2 ports are 60W PoE capable, 2 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes one AC power supply, 
country-specific power cord, user manuals access card and hardware for mounting on a TS-35/7.5 or 15 DIN rail.
OS6465H-P12
OS6465-P12 (ENH-240) Hardened GigE fan-less switch capable of 240W PoE budget. 8x10/100/1000 BaseT RJ-45 
802.3bt type-3 PoE, 4x100/1000 BaseX SFP,RS-232 Console, alarm relay  & USB ports. Supports Fast PoE/Perpetual 
PoE. The bundle includes user manuals, access card and DIN rail mounting hardware. Power supply should be 
ordered separately.
OS6465H-P12-xx
OS6465-P12-xx (ENH-240) Hardened GigE fan-less switch capable of 240W PoE budget. 4x10/100/1000 BaseT 
802.3bt type 3 PoE, 4x10/100/1000 BaseT 802.3at type-2 PoE+,, 4x100/1000 BaseX SFP ,RS-232 Console, 1 alarm 
relay input, 1 alarm relay output  & 1 USB port. Supports fast PoE/Perpetual PoE.  
Shipping bundle includes one 75W AC power supply, country-specific power cord, user manuals & DIN rail  
mounting hardware.
OS6465-P12
OS6465-P12: Hardened Gigabit Ethernet fixed configuration fan-less compact din-mount chassis with 8 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 4 ports are 60W PoE capable, 4 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes user manuals, access 
card and hardware for mounting on a TS-35/7.5 or 15 DIN rail. Power supply shall be ordered separately.
OS6465-P12-xx
OS6465-P12-xx: Hardened Gigabit Ethernet fixed configuration fan-less compact   din-mount chassis with 8 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 4 ports are 60W PoE capable, 4 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes one AC power supply, 
country-specific power cord, user manuals, access card and hardware for mounting on a TS-35/7.5 or 15 DIN rail.
OS6465-P28
OS6465-P28: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with 22 
10/100/1000 Base-T PoE+ ports out of which 8 ports are 60W PoE capable, two 100/1000 Base-X SFP ports, four 
(1G/10G) SFP+ ports, RS-232 Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and one USB port. The bundle 
includes user manuals access card and hardware for mounting in a 19” rack. Power supply shall be  
ordered separately.
OS6465-P28-xx
OS6465-P28-xx: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with 22 
10/100/1000 Base-T PoE+ ports out of which 8 ports are 60W PoE capable, two 100/1000 Base-X SFP ports, four 
(1G/10G) SFP+ ports, RS-232 Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and one USB port. The bundle 
includes one AC power supplt, country-specific power cord, power supply tray, user manuals, access card and 
hardware for mounting in a 19” rack. 
OS6465-P28D
 OS6465-P28D: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with 22 
10/100/1000 Base-T PoE+ ports out of which 8 ports are 60W PoE capable, two 100/1000 Base-X SFP ports, four 
(1G/10G) SFP+ ports, RS-232 Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and one USB port. The bundle 
includes one DC power supply, power supply tray, user manuals, access card and hardware for mounting in a  
19” rack.
OmniSwitch 6465 TAA Certified Switches
TA6465-P6
TA6465-P6: Hardened Gigabit Ethernet fixed configuration fan-less compact din-mount chassis with 4 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 2 ports are 60W PoE capable, 2 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes user manuals access 
card and hardware for mounting on a TS-35/7.5 or 15 DIN rail. Power supply shall be ordered separately.

<<<PAGE 502>>>
10
Datasheet 
Alcatel-Lucent OmniSwitch 6465
Part number
  Description
TA6465-P12
TA6465-P12: Hardened Gigabit Ethernet fixed configuration fan-less compact din-mount chassis with 8 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 4 ports are 60W PoE capable, 4 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes user manuals access 
card and hardware for mounting on a TS-35/7.5 or 15 DIN rail. Power supply shall be ordered separately.
TA6465-P6-US
TA6465-P6-US: Hardened Gigabit Ethernet fixed configuration fan-less compact din-mount chassis with 4 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 2 ports are 60W PoE capable, 2 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes one AC power supply, US 
power cord, user manuals access card and hardware for mounting on a TS-35/7.5 or 15 DIN rail.
TA6465-P12-US
TA6465-P12-US: Hardened Gigabit Ethernet fixed configuration fan-less compact din-mount chassis with 8 RJ-45 
10/100/1000 Base-T PoE+ ports out of which 4 ports are 60W PoE capable, 4 100/1000 Base-X SFP ports, RS-232 
Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and USB port. The bundle includes one AC power supply, US 
power cord, user manuals access card and hardware for mounting on a TS-35/7.5 or 15 DIN rail.
TA6465-P28-US
TA6465-P28-US: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with 22 
10/100/1000 Base-T PoE+ ports out of which 8 ports are 60W PoE capable, two 100/1000 Base-X SFP ports, four 
(1G/10G) SFP+ ports, RS-232 Console (RJ45), 1 Alarm relay Input, 1 alarm relay output and one USB port. The bundle 
includes one AC power supply, US power cord, power supply tray, user manuals, access card and hardware for 
mounting in a 19” rack.
OmniSwitch 6465 power supplies
OS6465H-BPNX-xx   
DIN-mount AC power supply. Provides system & 240W PoE power to one OS6465-P12 switch (ENH-240) orderable 
through references OS6465H-P12 and OS6465H-P12-xx. NOT QUALIFIED WITH switches orderable through 
references OS6465-P12, OS6465-P12-xx, OS6465-P6 and OS6465-P6-xx. Ships with country specific power cord  
& DIN mounting hardware. Refer to Hardware User guide and power supply datasheet for certification  
compliance information
OS6465-BPN-H-xx
OS6465 modular DIN 180 W AC backup power supply. Provides system and PoE power to one OS6465-P6 or 
OS6465-P12 switch. Ships with country specific power cord 
OS6465-BPN-xx
OS6465 modular DIN 75 W AC backup power supply. Provides system and PoE power to one OS6465-P6 or 
OS6465-P12 switch. Ships with country specific power cord
OS6465-BPR-xx
OS6465 modular rack-mount AC backup power supply. Provides system and PoE power to one OS6465-P28 switch. 
Ships with country specific power cord.
OS6465-BPRD
OS6465 modular rack-mount DC backup power supply. Provides system and PoE power to one OS6465-P28 switch.
OmniSwitch 6465 DNV certified parts
OS6465-DNV-DIN
DNV power supply cover kit for OS6465-P6 & OS6465-P12. Mandatory kit for installations requiring DNV certified 
OS6465-P6 and OS6465-P12. Contains PS cover and all mounting hardware
OS6465-DNV-RACK
DNV power supply cover kit for OS6465-P28. Mandatory kit for installations requiring DNV certified OS6465-P28. 
Contains PS cover, rear side-support rail, rear support bracket, side mount bracket and all mounting hardware 
OmniSwitch 6465 software
OS-SW-MACSEC
Site license to enable MACSec on OS6465 models. One license per customer at no cost.
OmniSwitch 6465 transceivers
iSFP-100-MM
100Base-FX industrial transceiver with an LC type interface. This transceiver is designed for use over multimode fiber.
iSFP-100-SM15
100Base-FX industrial transceiver with an LC type interface. This transceiver is designed for use over single-mode 
fiber up to 15 km.
iSFP-100-SM40
100Base-FX Industrial SFP transceiver with an LC type interface. This transceiver is designed for use over single 
mode fiber optic cable up to 40 km.
iSFP-GIG-T
1000Base-T industrial Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed  
and full-duplex mode
iSFP-GIG-SX
1000Base-SX industrial Gigabit Ethernet industrial optical transceiver (SFP MSA)
iSFP-GIG-LX
1000Base-LX industrial Gigabit Ethernet optical transceiver (SFP MSA)
iSFP-GIG-LH40
1000Base-LH industrial Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km  
on 9/125 µm SMF
iSFP-GIG-LH70
1000Base-LH industrial Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km  
on 9/125 µm SMF

<<<PAGE 503>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license 
by ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.
com/en/legal/trademarks-copyright. All other trademarks are the property of their respective owners. The 
information presented is subject to change without notice. Neither ALE Holding nor any of its affiliates 
assumes any responsibility for inaccuracies contained herein. © Copyright 2022 ALE International, ALE USA 
Inc. All rights reserved in all countries. DID00321675EN (July 2022)
Part number
  Description
iSFP-GIG-BX-U
1000Base-BX SFP transceiver with an LC type of interface. This bi-directional transceiver is designed  
for use over single mode fiber optic on a single strand link up to 10 km. Transmits 1310 nm and receives  
1490 nm optical signal.
iSFP-GIG-BX-D
1000Base-BX SFP transceiver with an LC type of interface. This bi-directional transceiver is designed for use over 
single mode fiber optic on a single strand link up to 10 km. Transmits 1490 nm and receives  
1310 nm optical signal.
10G transceivers
iSFP-10G-LR
10 Gigabit industrial optical transceiver (SFP+). Supports monomode fiber over 1310 nm wavelength (nominal) with 
an LC connector. Typical reach of 10 km
iSFP-10G-ER
10 Gigabit industrial optical transceiver (SFP+). Supports monomode fiber over 1550 nm wavelength (nominal) with 
an LC connector. Typical reach of 40 km
iSFP-10G-ZR
10 Gigabit industrial optical transceiver HPoE (SFP+). Supports data transmission at 1550nm over up to 80km single 
mode fiber. LC connector type
SFP+ direct attached cables
iSFP-10G-C1M
10 Gigabit industrial direct attached copper cable (1 m, SFP+)
iSFP-10G-C3M
10 Gigabit industrial direct attached copper cable (3 m, SFP+)
iSFP-10G-C7M
10 Gigabit industrial direct attached copper cable (7 m, SFP+)
Please replace the “-xx” in the part number with the country-specific power cord (e.g. OS6465-12-US will come 
with a power cord for the USA, -UK for United Kingdom). ALE offers 11 different power cord options. Please 
consult the price list for the power cord options offered.
Warranty
The OmniSwitch 6465 family comes with a Limited Lifetime Hardware Warranty.
Services and support
For more information about our Professional services, Support services, and Managed services,  
please go to https://www.al-enterprise.com/en/services
Please visit our website to learn more: https://www.al-enterprise.com/en/products/switches/omniswitch-6465

<<<PAGE 504>>>
Datasheet 
Alcatel-Lucent OmniSwitch 6465T
Alcatel-Lucent
OmniSwitch 6465T 
Extended Temperature Ethernet Switches
The Alcatel-Lucent OmniSwitch® 6465T is a family of 
extended temperature, value, Layer 3 Gigabit Ethernet 
switches. These switches are versatile in nature and 
can be deployed in a variety of environments such as 
residential and business metro Ethernet access offered 
by service providers, in smart cities/buildings or for 
transportation deployments. 
OmniSwitch 6465T switches are a family of extended temperature, compact, gigabit Ethernet switches 
that are ideal for residential/metro Ethernet triple play applications. The PoE switches offer a value, 
power-efficient access for powering smart building subsystems such as lighting, CCTV and HVAC. The 
switches run on the widely deployed and field-proven Alcatel-Lucent Operating System (AOS) that offers 
high security, reliability, performance and easy management. These switches are designed to operate in 
an extended temperature range offering reliable operation in -10°C to 60°C ambient temperature range.  
The OmniSwitch 6465T 12-port models are designed with an optimized size, low-power consumption 
and a rich software feature set. This extended temperature PoE model can provide power to a range of 
new age devices from IP cameras on toll booths to LED lights and building management gateways in 
smart buildings. These switches are easy to deploy and offer out-of-the-box plug-and-play, zero-touch 
provisioning, network automation and disaster recovery options. These switches support IEEE 1588v2 
PTP for the nanosecond-level precision timing requirements of devices and applications. With support 
for MACsec on all ports, OmniSwitch 6465T enables end-to-end encrypted networks. The OmniSwitch 
6465T family offers advanced system and network level resiliency features and convergence through 
standardized protocols in a space efficient form factor. OmniSwitch 6465T models can operate with out 
fan up to 45°C ambient temperature. 
OmniSwitch 6465T-12
OmniSwitch 6465T-P12

<<<PAGE 505>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 6465T
Features
Benefits
Extended temperature range
Operates at an extended temperature range from -10°C to +60°C offering a 
reliable operation over a wider temperature range
Virtual chassis to connect multiple switches for 
creating a single chassis-like entity
Increases system redundancy, resiliency and system scalability while 
simplifying deployment, operations and management of the network
Delivers redundant ring topologies using 
industry standard protocols
Field upgradable, highly redundant network solution maximizes network uptime
Switch backup and restore
Simplifying switch replacement in field and minimizing network downtime 
using USB drive. Encryption of USB ensures optimal security.
IEEE 1588v2 PTP support
Support for peer-to-peer and end-to-end transparent clock provides precise 
nanosecond time synchronization for devices on industrial networks
Simplified installation and service provisioning
Out-of-the-box Zero-touch provisioning and network automation with automatic 
protocol and topology discovery
Layer 2 security with MACsec
MACsec encryption support provides a secure network access ensuring data 
confidentiality and integrity
Alcatel-Lucent OmniSwitch 6465T models
The Alcatel-Lucent OmniSwitch 6465T-12 and 6465T-P12 models are power and acoustically optimized, 
with a half-rack width, and have a fixed configuration chassis in a 1 RU form factor. All models can 
operate without fan up to 45°C ambient temperature and with fan can operate up to 60°C.  Both models  
have an internal power supply. PoE model is 802.3af/802.3at compliant and offers 115 W of power for 
PoE attached devices.
All ports of OmniSwitch 6465T-12 and OmniSwitch 6465T-P12 are capable of IEEE 1588v2 and MACsec. 
OmniSwitch 6465T switches can form a virtual chassis between any models creating a single chassis-
like entity using 1G SFP ports. Up to four switches can be connected in a virtual chassis configuration 
with option to scale up to eight in future. For forming virtual chassis connections, any SFP transceiver or 
SFP+ Direct attach cables can be used on 1G SFP ports.
Models
Gigabit ports 
(RJ45)
Gig combo 
ports
100/1000 SFP 
ports
Primary 
power
Backup 
power
Description
OS6465T-12
8
2
2
Internal AC
N/A
Fixed-configuration half-rack width 
chassis with eight 10/100/1000 
Base-T ports, two Gigabit combo ports 
and two 100/1000 Base-X SFP ports.
OS6465T-P12
8
2
2
Internal AC
N/A
Fixed-configuration half-rack width 
chassis with eight 10/100/1000 Base-T 
PoE+ ports, two Gigabit combo ports 
and two 100/1000 Base-X SFP ports.
Technical specifications
Product matrix
OS6465T-12
OS6465T-P12
File system flash
1 GB
1 GB
RAM
1 GB
1 GB
Fans*
2
2
USB Port
1 (type A, USB 2.0)
1 (type A, USB 2.0)
Console
1 (RS232 RJ45)
1 (RS232 RJ45)
IEEE 1588v2 capable ports
12
12
MACsec capable ports
12
12
Operating conditions
Operating temperature
-10°C to 60°C (14°F to 140°F)
-10°C to 60°C (14°F to 140°F)
Storage temperature
-40°C to 85°C (-40°F to 185°F)
-40°C to 85°C (-40°F to 185°F)
* Fans run only if switch is operated at an ambient temperature of +45°C to +60°C. Fans remain off when switch is operating at -10°C to 45°C

<<<PAGE 506>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 6465T
Product matrix
OS6465T-12
OS6465T-P12
Humidity (operating & storage) 
5% to 95% non-condensing
5% to 95% non-condensing
Altitude
13,000 ft
13,000 ft
MTBF (Hours)*
1,953,053
1,298,328
Power Supply efficiency
85%
85%
Acoustic (-10°C to 45°C) (dB)
Silent
Silent
Acoustic (45°C to 60°C) (dB)
56 dBA
56 dBA
System power consumption (idle)**
8.5 W
8.5 W
System power consumption (full load)**
16 W
19 W
Heat dissipation (BTU)**
54.6
64.8
PoE power budget
NA
115 W
Performance 
Switching capacity (aggregated)
24 Gb/s
24 Gb/s
Forwarding capacity 
17.9 Mb/s
17.9 Mb/s
Physical characteristics
Switch width
21.7 cm (8.55 in.)
21.7 cm (8.55 in.)
Switch height
4.4 cm (1.73 in.)
4.4 cm (1.73 in.)
Switch depth
28 cm (11.05 in.)
28 cm (11.05 in.)
Weight
1.7 Kg (3.8 lb)
2.0 Kg (4.46 lb)
*  MTBF calculations are done at ambient temperature of 25°C
** Power consumption measured at the 120 V AC outlet. Full load measurement does not include PoE power consumption. Heat dissipation: 1 watt ≈ 3.41214 BTU/h
Product specifications 
and measurements
Per-port LEDs
•	 Non-PoE ports - green: Link/activity
•	 PoE ports - amber: Link/activity
System LEDs
•	 OK: Green/amber operational status 
of the switch
•	 VC: Green/amber master or slave role 
in VC configuration. Number of blinks 
identify stacking unit number
•	 PWR: Green/amber - status for the 
primary power supply
Scalability numbers and 
speeds
•	 Wire rate at layer 2 and layer 3 on 
all ports
•	 Jumbo frame size: 9216 bytes  
(for 1 Gb/s)
•	 Total number of MAC addresses: 16 K
•	 Total number of IPv4 routes: 128
•	 Number of VLANs: 4000
Virtual chassis
•	 Maximum number of units in a VC: 4
•	 Remote VC connection: Using SFP-
GIG-SX, SFP-GIG-LX
Compliance and 
certifications
Commercial safety
•	 IEC 62368-1
•	 UL 60950-1, 2nd Ed.
•	 UL62368-1
•	 UL 2043 (plenum rated)
•	 IEC 60950-1; all national deviations
•	 IEC 62368-1; all national deviations
•	 EN 60950-1; all deviations
•	 CAN/CSA-C22.2 No. 60950-1-03
•	 CAN/CSA-C22.2 No. 62368-1
•	 NOM-019 SCFI, Mexico
•	 AS/NZ TS-001 and 60950:2000, 
Australia
•	 UL-AR, Argentina
•  AS/NZ 62368-1
•	 UL-GS Mark, Germany
•	 CU, EAC, Russia
•	 ANATEL, Brazil
•	 CCC, China
•	 KCC Korea
•	 BSMI, Taiwan
•	 EN 60825-1 Laser
•  C Mark, Morocco
•	 EN 60825-2 Laser
•	 CDRH Laser
•	 RoHS and WEEE directives compliant
•	 REACH directive
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart 
B (Class A)VCCI (Class A, with UTP 
Cables)
•	 ICES–003:2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) – C-Tick
•	 CE marking for European countries 
(Class A)
•	 CE Emission
	
¬ EN50581 (RoHS Recast)
	
¬ EN 55032 (EMI & EMC 
requirement)
	
¬ EN 55024/EN 55035 (Immunity 
Characteristics)
	
¬ EN 61000-3-2(Harmonic Current 
emissions)
	
¬ EN 61000-3-3
	
¬ EN 61000-4-2
	
¬ EN 61000-4-3
	
¬ EN 61000-4-4
	
¬ EN 61000-4-5 (Surge Immunity, 
Class 4)
	
¬ EN 61000-4-6
	
¬ EN 61000-4-8
	
¬ EN 61000-4-11
	
¬ IEEE802.3: Hi-pot Test (2.25 KV DC 
on all Ethernet Ports)

<<<PAGE 507>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 6465T
Detailed product features
Simplified manageability and 
configuration
•	 Intuitive CLI in a scriptable BASH 
environment via console, Telnet or 
Secure Shell (SSH) v2 over IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over 
IPv4/IPv6
•	 Fully programmable RESTful web 
services interface with XML and 
JSON support. API enables access to 
CLI and individual mib objects
•	 Integrated with Alcatel-Lucent 
OmniVista® products for network 
management
•	 Integrated with Nokia 5620 SAM™ 
for network management
•	 Full configuration and reporting 
using SNMPv1/2/3 to facilitate third- 
party network management over 
IPv4/IPv6
•	 File upload using USB, TFTP, FTP, 
SFTP or SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line 
editing, bulk configuration and out- 
of-the-box auto-provisioning
•	 Non-volatile memory for start-up 
configuration
•	 Multiple microcode image support 
with fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server 
managed by Nokia VitalQIP® DNS/ 
DHCP IP Address Management
•	 Access to the AOS console via USB 
Adapter with Bluetooth technology 
provides wireless management 
access, eliminating the need of 
console cables
Cloud ready with OmniVista 
Cirrus
•	 OmniVista Cirrus offers a secure, 
resilient and scalable cloud-based 
network management. It offers 
hassle free network deployment 
and easy service roll-out with 
advanced analytics for smarter 
decision making. It provides IT 
friendly Unified Access with 
secure authentication and policy 
enforcement for users and devices.
Monitoring and 
troubleshooting
•	 Local (on the flash) and remote 
server logging (Syslog): Event and 
command logging
•	 IP tools: Ping and trace route
•	 Dying Gasp support via SNMP and 
syslog messages
•	 Loopback IP address support for 
management per service
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD), 
Digital Diagnostic Monitoring (DDM)
Resiliency and high 
availability
•	 Unified management, control and 
virtual chassis technology
•	 Virtual chassis 1+N redundant 
supervisor manager
•	 Smart continuous switching 
technology
•	 ITU-T G.8032/Y1344 2010: Ethernet 
Ring Protection
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning 
Tree Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+)  
and 1x1 STP mode 
•	 IEEE 802.3ad/802.1AX Link 
Aggregation Control Protocol 
(LACP) and static LAG groups across 
modules
•	 Dual-home link support for sub-
second link protection without STP
•	 Virtual Router Redundancy Protocol 
(VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection: Auto- 
detection and recovery of Virtual 
Chassis splitting due to one or more 
VFL or stack element failures
Advanced security
Switch software security
•	 AOS secured diversified code 
solution is available on OmniSwitch 
6465T, hardening it at both the 
software source code and binary 
executable levels to enhance overall 
network security.
•	 AOS secured diversified code 
protects networks from intrinsic 
vulnerabilities, code exploits, 
embedded malware, and potential 
back doors that could compromise 
mission critical operations.
•	 AOS secured diversified code is a 
proactive, defense approach toward 
network security that continuously 
defines and implements value-add 
capabilities to address both current 
and future threats.
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive user- 
policy-based NAC
•	 Autosensing IEEE 802.1X multi- 
client, multi-VLAN support
•	 MAC-based authentication for non- 
IEEE 802.1X hosts
•	 Web based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (uNP) simplifies 
NAC by dynamically providing 
pre-defined policy configuration to 
authenticated clients — VLAN, ACL, 
BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial- 
In User Service (RADIUS) and 
Lightweight Directory Access 
Protocol (LDAP) administrator 
authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow- 
based filtering in hardware (Layer 1 
to Layer 4)
•	 DHCP Snooping, DHCP IP and 
Address Resolution Protocol (ARP) 
spoof protection
*Future support

<<<PAGE 508>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 6465T
•	 ARP poisoning detection
•	 IP Source Filtering as a protective 
and effective mechanism against  
ARP attacks
•	 LLDP Security mechanism for rogue 
device detection and restriction
QoS
•  Priority queues: Eight hardware- 
based queues per port for flexible 
QoS management
•	 Traffic prioritization: Flow-based 
QoS Flow-based traffic policing and 
bandwidth management
•	 32-bit IPv4/128-bit IPv6 non- 
contiguous mask classification
•	 Egress traffic shaping
•	 DiffServ architecture
•	 Congestion avoidance: Support for 
end- to-end head-of-line (E2E-HOL) 
blocking prevention, IEEE 802.1Qbb 
Priority-based Flow Control (PFC) 
and IEEE 802.3x Flow Control (FC)
•  Auto-QoS support for Generic Object 
Oriented Substation Events (GOOSE) 
messages
Layer-3 routing and multicast
IPv4 routing
•	 Static routing
•	 Virtual Router Redundancy Protocol 
(VRRPv2)
•	 DHCP relay (including generic UDP 
relay)
•	 Address Resolution Protocol (ARP)
•	 Policy-based routing and server load 
balancing
•	 DHCPv4 server
IPv6 routing
•	 Internet Control Message Protocol 
version 6 (ICMPv6)
•	 Static routing
•	 Virtual Router Redundancy Protocol 
version 3 (VRRPv3)
•	 Neighbor Discovery Protocol (NDP)*
•	 Policy-based routing and server load 
balancing
•	 DHCPv6 server
IPv4/IPv6 multicast
•	 Internet Group Management Protocol 
(IGMP) v1/v2/v3 snooping
•	 Multicast Listener Discovery (MLD) 
v1/v2 snooping
Advanced Layer-2 services
•	 Ethernet services support using 
IEEE 802.1ad Provider Bridges (also 
known as Q-in-Q or VLAN stacking
•	 Ethernet OAM (802.1ag , ITU-T 
Y.1731): Connectivity Fault 
Management (L2 ping & Link trace)
•	 Ethernet in first mile: Link OAM 
(802.3ah) 
•	 Ethernet network-to-network 
interface (NNI) and user network 
interface (UNI)
•	 Service Access Point (SAP) profile 
identification
•	 Service VLAN (SVLAN) and customer 
VLAN (CVLAN) support
•	 VLAN translation and mapping 
including CVLAN to SVLAN
•	 Port mapping
•	 DHCP Option 82: Configurable relay 
agent information
•	 Multiple VLAN Registration Protocol 
(MVRP)
•	 HA-VLAN for Layer 2 clusters such 
as MS-NLB and active-active firewall 
clusters*
•	 Customer Provider Edge (CPE) test 
head traffic generator and analyzer 
tool 
•	 TR-101 Point-to-Point Protocol over 
Ethernet (PPPoE) Intermediate Agent 
allowing for the PPPoE network 
access method
•	 Service Assurance Agent (SAA) for 
proactively measuring network 
health, reliability and performance.
•	 Jumbo frame support
•	 Bridge Protocol Data Unit (BPDU) 
blocking
•	 STP Root Guard
Supported standards
IEEE standards
•	 IEEE 802.1D STP
•	 IEEE 802.1p CoS
•	 IEEE 802.1Q VLANs
•	 IEEE 802.1ab (LLDP)
•	 IEEE 802.1ag (OAM)
•	 IEEE 802.3ah (OAM)
•	 IEEE 802.1ad Provider Bridges 
Q-in-Q/ VLAN stacking
•	 IEEE 802.1ak (Multiple VLAN 
Registration Protocol (MVRP)
•	 IEEE 802.1s MSTP
•	 IEEE 802.3i 10Base-T
•	 IEEE 802.1w RSTP
•	 IEEE 802.3x Flow Control
•	 IEEE 802.3z Gigabit Ethernet
•	 IEEE 802.3ab 1000Base-T
•	 IEEE 802.3ac VLAN Tagging
•	 IEEE 802.3ad/802.1AX Link 
Aggregation
•	 IEEE 802.3af Power over Ethernet
•	 IEEE 802.3at PoE Plus
•	 IEEE 802.1ae MAC Security
•	 IEEE 1588-2008 (PTP)
ITU-T recommendations
•	 ITU-T G.8032/Y.1344 2010: Ethernet 
Ring Protection (ERPv2)
IETF RFCs
IPv4
•	 RFC 2131 Dynamic 
HostConfiguration Protocol (DHCPv4)
•	 RFC 4022/2452 MIB for IPv4 TCP
•	 RFC 4113/2454 MIB for IPv4 UDP
•	 RFC 4292/4293 IPv4 MIBs
RIP
•	 RFC 1058 RIP v1
•	 RFC 1722/1723/2453/1724 RIP v2 
and MIB
•	 RFC 1812/2644 IPv4 Router 
Requirements
•	 RFC 2080 RIPng for IPv6
IP Multicast
•	 RFC 2365 Multicast
•	 RFC 2710/3019/3810/MLD v2 for 
IPv6
•	 RFC 2933 IGMP MIB
•	 RFC 3376 IGMPv3 (includes IGMP 
v2/v1)
•	 RFC 4541 Considerations for IGMP 
and MLD Snooping Switches
•	 RFC 5132 Multicast Routing MIB
IPv6
•	 RFC 1981 Path MTU Discovery
•	 RFC 2460 IPv6 Specification
•	 RFC 2464 IPv6 over Ethernet
•	 RFC 2465 MIB for IPv6: Textual 
Conventions (TC) and General Group
•	 RFC 2466 MIB for IPv6: ICMPv6 
Group
•	 RFC 3484 Default Address Selection
•	 RFC 3493/2553 Basic Socket API
•	 RFC 3542/2292 Advanced Sockets 
API
•	 RFC 3587/2374 Global Unicast 
Address Format
•	 RFC 3595 TC for IPv6 Flow Label
•	 RFC 3596/1886 DNS for IPv6
•	 RFC 4007 Scoped Address
•	 RFC 4022/2452 MIB for IPv6 TCP
*Future support

<<<PAGE 509>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 6465T
•	 RFC 4113/2454 MIB for IPv6 UDP
•	 RFC 4193 Unique Local Addresses
•	 RFC 4213/2893 Transition 
Mechanisms
•	 RFC 4291/3513/2373 Addressing 
Architecture (uni/any/multicast)
•	 RFC 4292/4293 IPv6 MIBs
•	 RFC 4443/2463 ICMPv6
•	 RFC 4861/2461 Neighbor Discovery
•	 RFC 4862/2462 Stateless Address 
Autoconfiguration*
•	 RFC 5095 Deprecation of Type 0 
Routing Headers in IPv6*
Manageability
•	 RFC 854/855 Telnet and Telnet 
options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1 and 
SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP 
Traps
•	 RFC 1573/2233/2863 Private 
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•	 RFC 1901-1908/3416-3418 SNMP 
v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from 
Forms: multipart/form-data
•	 RFC 2396 Uniform Resource 
Identifiers (URI): Generic Syntax
•	 RFC 2570-2576/3410-3415/3584 
SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2668/3636 IEEE 802.3 MAU 
MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 3826 (AES) Cipher Algorithm in 
the SNMP User-based Security Model
•	 RFC 4122 A Universally Unique 
IDentifier (UUID) URN Namespace
•	 RFC 4234 Augmented BNF for 
Syntax Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 6585 Additional HTTP Status 
Codes 
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and 
crypto algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618 
RADIUS Authentication and Client 
MIB
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS 
Extension
•	 RFC 4301 Security Architecture for IP
QoS
•	 RFC 896 Congestion Control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 2697 srTCM
•	 RFC 2698 trTCM
•	 RFC 3635 Pause Control
Others
•	 RFC 791/894/1024/1349 IP and IP/
Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy 
ARP
•	 RFC 2681 
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 NTP v3 and Simple 
NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 
DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 2338/3768/2787 VRRP and MIB 
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
•  RFC 4562 MAC-Forced Forwarding

<<<PAGE 510>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license 
by ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.
com/en/legal/trademarks-copyright. All other trademarks are the property of their respective owners. The 
information presented is subject to change without notice. Neither ALE Holding nor any of its affiliates 
assumes any responsibility for inaccuracies contained herein. © Copyright 2021 ALE International, ALE 
USA Inc. All rights reserved in all countries. MPR00390268EN (August 2021)
Ordering information
Part number                            
Description
OmniSwitch 6465T models
OS6465T-12
OS6465T-12: Gigabit Ethernet chassis. 8 RJ45 10/100/1000 BaseT, 2 SFP/RJ45 combo, 2 SFP ports. 1RU 
by 1/2 rack width, internal AC PSU. Operating temp -10° C to 60° C. Includes power cord, manuals/software 
access cards, RJ45 to DB9 adaptor
OS6465T-P12                    
OS6465T-P12: Gigabit Ethernet chassis. 8 RJ45 10/100/1000 BaseT PoE+, 2 SFP/RJ45 combo, 2 SFP ports. 
1RU by 1/2 rack width, internal AC PSU. Operating temp -10° C to 60° C. Includes power cord, manuals/
software access cards, RJ45 to DB9 adaptor.
OmniSwitch 6465T licenses
OS-SW-MACSEC
Site license to enable MACsec on applicable OS6465, OS6560, OS6860, OS6865, OS6900, OS9900 models. 
One license per customer at no cost
OmniSwitch 6465T Accessories 
OS6465T-CBL-60
60 centimeters long SFP+ direct stacking cable for OS6465T models
OS6465T-CBL-1M
1-meter long SFP+ direct stacking cable for OS6465T models
OS6465T-CBL-3M
3-meter long SFP+ direct stacking cable for OS6465T models
Gigabit transceivers
SFP-GIG-LH70
1000Base-LH transceiver with an LC interface for single mode fiber over 1550 nm wavelength. Typical 
reach of 70 km.
SFP-GIG-LH40
1000Base-LH transceiver with an LC interface for single mode fiber over 1310 nm wavelength. Typical 
reach of 40 km.
SFP-GIG-LX
1000Base-LX transceiver with an LC interface for single mode fiber over 1310 nm wavelength. Typical 
reach of 10 km.
SFP-GIG-SX
1000Base-SX transceiver with an LC interface for multimode fiber over 850 nm wavelength. Typical reach 
of 300 m.
SFP-GIG-EXTND
1000Base-SX transceiver with an LC interface for single mode fiber over 850 nm wavelength. Typical reach 
of 2 km.
SFP-GIG-T
1000Base-T Gigabit ethernet transceiver Supports category 5, 5E, and 6 copper cabling up to 100m. 
SFP-DUAL-MM-N
Dual Speed 100Base-FX or 1000Base-X Ethernet optical transceiver SFP MSA). Supports multimode fiber 
over 1310nm wavelength nominal) with an LC connector. Typical reach of 550 m at Gigabit speed and 2 km 
at 100 Mb/s speed.
SFP-DUAL-BX-D
Dual Speed 100Base-BXD or 1000Base-BXD SFP transceiver with an LC type connector. This bidirectional 
transceiver is designed for use over single mode fiber optic on a single strand link up to 10 km. Transmits 
1550 nm and receives 1310 nm optical signal.
SFP-DUAL-BX-U
Dual Speed 100Base-BXU or 1000Base-BXU SFP transceiver with an LC type connector. This bidirectional 
transceiver is designed for use over single mode fiber optic on a single strand link up to 10 km.Transmits 
1310 nm and receives 1550 nm optical signal.
100 Megabit transceivers
SFP-100-LC-MM
100Base-FX SFP transceiver with an LC type interface. This transceiver is designed for use over multimode 
fiber optic cable.
SFP-100-LC-SM15
100Base-FX SFP transceiver with an LC type interface. This transceiver is designed for use over single mode 
fiber optic cable up to 15 km.
SFP-100-LC-SM40
100Base-FX SFP transceiver with an LC type interface. This transceiver is designed for use over single mode 
fiber optic cable up to 40 km.
SFP-100-BXLC-D
100Base-BX SFP transceiver with an LC type interface. Designed for use over single mode fiber optic on  
a single strand link up to 20KM point-to point.This transceiver is normally used in the central office OLT)  
Tx-1550 nm and Rx-1310 nm optical signal
SFP-100-BXLC-U
100Base-BX SFP transceiver with an LC type interface. Designed for use over single mode fiber optic  
on a single strand link up to 20 km point-to point. This transceiver is normally used in the client ONU)  
Tx-1310 nm and Rx-1550 nm optical signal
Warranty
The OmniSwitch 6465T family comes with a Limited Lifetime Hardware Warranty.
Services and support
For more information about our Professional Services, Support Services, and Managed Services, please 
go to https://www.al-enterprise.com/en/services
Please visit our website to learn more: https://www.al-enterprise.com/en/products/switches/

<<<PAGE 511>>>
Datasheet  
Alcatel-Lucent OmniSwitch 6560
Alcatel-Lucent  
OmniSwitch 6560
Stackable Gigabit and Multi-Gigabit 
Ethernet LAN Switch Family 
The Alcatel-Lucent OmniSwitch™ 6560 Stackable Gigabit 
and Multi-Gigabit Ethernet LAN value switch family is an 
industry leading campus access solution for enterprise 
networks. With multi-gigabit ports for high-speed IEEE 
802.11ac devices, 10 GigE uplinks and 20 GigE stacking, 
the OmniSwitch 6560 is the right solution for your next 
generation network.
Offering a design optimized for flexibility and scalability as well as 
low power consumption, the OmniSwitch 6560 is an outstanding 
edge solution. It uses the field-proven Alcatel-Lucent Operating 
System (AOS) to deliver highly available, secure, self-protective, 
easily managed and eco-friendly networks.
The Alcatel-Lucent OmniSwitch 6560 family is embedded with  
the latest technology innovations, and offers maximum  
investment protection.
Deployments benefiting from the OmniSwitch 6560 family are:
•	 Edge of small-to-mid-sized networks
•	 Branch office enterprise and campus workgroups
•	 Residential and commercially managed services applications
OmniSwitch 6560-P24Z8
OmniSwitch 6560-24X4/-P24X4
OmniSwitch 6560-48X4/-P48X4
OmniSwitch 6560-P24Z24
OmniSwitch 6560-P48Z16
OmniSwitch 6560-X10

<<<PAGE 512>>>
2
Datasheet  
Alcatel-Lucent OmniSwitch 6560
Features
•	 24-port and 48-port, PoE and 
non-PoE with fixed small form 
factor pluggable (SFP+) with 
support for up to 6 x 10G 
interfaces.
•	 Support for 10 GigE stacking/
remote stacking or 20 GigE 
stacking
•	 Support for IEEE 802.1AE 
MACSec encryption
•	 Internal modular AC redundant 
power supplies 
Management
•	 AOS field-proven software with 
management through web 
interface (WebView), command 
line interface (CLI), and Simple 
Network Management Protocol 
(SNMP)
•	 Ethernet operations, 
administration and management 
(OA&M) support for service 
configuration and monitoring
•	 Cloud enabled with OmniVista® 
Cirrus for a secure, resilient and 
scalable cloud-based network 
management.
•	 Support by Alcatel-Lucent 
OmniVista™ 2500 Network 
Management System (NMS) 
Security
•	 MACSec encryption to secure the 
network edge: 1G/2.5G user and 
10G up-link ports
•	 Flexible device and user 
authentication with Alcatel-Lucent 
Access Guardian (IEEE 802.1x/
MAC/captive portal) with Host 
Integrity Check (HIC) enforcement
•	 Enables deployment of 
comprehensive and secure BYoD 
services in enterprise networks 
such as guest management, 
device on-boarding, device 
posturing, application 
management and dynamic 
change of authentication (CoA).
•	 Advanced Quality of Service (QoS) 
and Access Control Lists (ACLs) 
for traffic control, including an 
embedded denial of service (DoS) 
engine to filter out unwanted 
traffic attacks
•	 Extensive support of user-
oriented features such as learned 
port security (LPS), port mapping, 
Dynamic Host Configuration 
Protocol (DHCP) binding tables 
and User Network Profile (UNP)
Performance and redundancy 
•	 Advanced layer-2+ features with 
basic layer-3 routing for both 
IPv4 and IPv6+
•	 Triple speed (100/1G/2.5G) user 
interfaces and fiber interfaces 
(SFPs) supporting 1000Base-X or 
10GBase-X optical transceivers
•	 Up to 6 x 10G uplinks
•	 Precision Time Protocol (IEEE 
1588v2) on 48 port models
•	 Wire-rate switching and routing 
performance
•	 High availability with virtual 
chassis concept, redundant 
stacking links, primary/secondary 
unit failover, hot-swappable power 
options and configuration rollback
Convergence
•	 Enhanced Voice over IP (VoIP) 
and video performance with 
policy-based QoS
•	 Future-ready support for 
multimedia applications with 
wire-rate multicast
•	 Airgroup™ Network Services 
for Bonjour speaking devices 
provides consistent experience 
over wireless and wired networks
•	 IEEE 802.3af, IEEE 802.3at and 
IEEE802.3bt PoE support for IP 
phones, wireless LAN (WLAN) 
access points and video cameras
Benefits
•	 Meets any customer 
configuration need and offers 
excellent investment protection 
and flexibility, as well as ease of 
deployment, operation  
and maintenance
•	 Provides outstanding 
performance when supporting 
real-time voice, data and video 
applications for converged 
scalable networks
•	 Ensures efficient power 
management, reduces operating 
expenses (OPEX) and lowers total 
cost of ownership (TCO) through 
low power consumption and 
dynamic PoE allocation, which 
delivers only the power needed 
by the attached device
•	 A field-upgradeable solution 
that makes the network highly 
available and reduces OPEX
•	 Fully secures the network at the 
edge at no additional cost
•	 Enterprise-wide cost reduction 
through hardware consolidation 
to achieve network segmentation 
and security without additional 
hardware installation
•	 Supports cost-effective 
installation and deployment with 
automated switch setup and 
configuration and end-to-end 
virtual LAN (VLAN) provisioning
•	 OmniVista® Cirrus powers 
a secure, resilient and 
scalable cloud-based network 
management. It offers hassle 
free network deployment 
and easy service rollout with 
advanced analytics for smarter 
decision making. IT friendly 
Unified Access with secure 
authentication and policy 
enforcement for users  
and devices.

<<<PAGE 513>>>
3
Datasheet  
Alcatel-Lucent OmniSwitch 6560
Table 1. Available OmniSwitch 6560 models
Gigabit models
10/100/1000 
RJ-45 ports
1GE SFP+ 
ports
1GE/10GE 
SFP+ uplink/
stacking ports
20 GE 
stacking 
ports
Primary power
Backup power
OS6560-24X4
24
2*
4
0
Fixed internal AC
Modular internal AC/DC
OS6560-P24X4
24
2*
4
0
Modular internal AC
Modular internal AC
OS6560-48X4
48
2*
4
0
Fixed internal AC
Modular internal AC/DC
OS6560-P48X4
48
2*
4
0
Modular internal AC
Modular internal AC
OS6560-X10
0
0
8
2
Fixed internal AC
Modular internal AC/DC
Multi-Gigabit models
10/100/1000
RJ-45 ports
Multi-
Gigabit 
ports
1 GE/10 GE SFP+ 
uplink/stacking 
ports
20 GE stacking 
ports
Primary power 
(modular)
Backup power (modular)
OS6560-P24Z8
24
8
2
0
Internal AC
Internal AC
OS6560-P24Z24
24
24
4
2
Internal AC
Internal AC
OS6560-P48Z16
48
16
4
2
Internal AC
Internal AC
Note: All OmniSwitch Multi-Gigabit PoE ports comply with IEEE 802.3bt (95 W) and IEEE 2.5GE 802.3bz standards
Technical specification
Gigabit  
product matrix
OS6560-24X4
OS6560-P24X4
OS6560-48X4
OS6560-P48X4
OS6560-X10
Gigabit RJ-45  
port count 
24 
24 PoE+
48
48 PoE+
0
1G SFP+ port count
2*
2*
2*
2*
0
1G/10G SFP+ 
4
4 
4
4
8
20G QSFP+  
stacking ports
0
0
0
0
2
MACSec  
capable ports
All 1G RJ45
All 1G RJ45
All 1G RJ45
2 x 1G SFP
2 x 10 SFP+
All 1G RJ45
2 x 1G SFP
2 x 10 SFP+
8 x 10G SFP+
USB port 
1 
1 
1
1
1
IEEE 1588v2 PTP 
support
N/S 
N/S 
Yes
Yes
N/S
Console port 
1 
1 
1
1
1
Primary slide-in PSU 
slot 
Fixed
1 
Fixed
1
Fixed
Backup slide-in  
PSU slot 
1 
1 
1
1
1
Fans 
1 
2 
2
2
2
File system flash 
1 GB 
1 GB 
1GB
1 GB
1 GB
RAM 
1 GB 
1 GB 
2 GB
2 GB
2 GB
Max switching  
ASIC capacity 
168 Gb/s 
168 Gb/s 
216 Gb/S
216 Gb/S
240 Gb/S
Switching capacity
168 Gb/s
168 Gb/s
216 Gb/s
216 Gb/s
240 Gb/s
Throughput 
125 Mpps 
125 Mpps 
160.7 Mpps
160.7 Mpps
178.6 Mpps
Stacking Capacity 
(each)
40 Gb/s 
40 Gb/s 
40 Gb/s
40 Gb/s
80 Gb/s
Stacking Capacity 
(total)
320Gb/s
320Gb/s
320Gb/s
320Gb/s
640Gb/s

<<<PAGE 514>>>
4
Datasheet  
Alcatel-Lucent OmniSwitch 6560
Gigabit  
product matrix
OS6560-24X4
OS6560-P24X4
OS6560-48X4
OS6560-P48X4
OS6560-X10
System power 
consumption 
36 W 
42 W
87 W
104 W
49 W
System heat 
dissipation 
123 (BTU/h) 
143 (BTU/h) 
297 (BTU/h)
355 (BTU/h)
167 (BTU/h)
Power consumption 
w/PoE 
N/A 
600 W 
N/A
920 W
N/A
Heat Dissipation w/
PoE 
N/A 
2047 (BTU/h) 
N/A
3139 (BTU/h)
N/A
Acoustics (dB) @27C* 
43-54 (dBA) 
45-54 (dBA) 
43-54 (dBA)
45-54 (dBA)
45-54 (dBA)
MTBF (hours) 
372 k
352 k
665 k
339 k
885 k
Height 
4.4 cm (1.73 in) 
4.4 cm (1.73 in) 
4.4 cm (1.73 in)
4.4 cm (1.73 in)
4.4 cm (1.73 in)
Width 
44 cm (17.33 in) 
44 cm (17.33 in) 
44 cm (17.33 in)
44 cm (17.33 in)
44 cm (17.33 in)
Depth 
35 cm (13.78 in) 
35 cm (13.78 in) 
35 cm (13.78 in)
35 cm (13.78 in)
35 cm (13.78 in)
Weight 
4.7 kg (10.4 lb) 
4.88 kg (10.75 lb) 
4.54 kg (10.0 lb)
4.68 kg (10.3 lb)
4.04 kg (8.91 lb)
Operating 
temperature 
0° C to 45° C (32° F 
to 113° F) 
0° C to 45° C  
(32° F to 113° F) 
0° C to 45° C  
(32° F to 113° F) 
0° C to 45° C  
(32° F to 113° F) 
0° C to 45° C  
(32° F to 113° F) 
Storage temperature 
-40° C to 85° C 
(-40° F to 185° F) 
-40° C to 85° C (-40° 
F to 185° F) 
-40° C to 85° C 
(-40° F to 185° F)
-40° C to 85° C 
(-40° F to 185° F)
-40° C to 85° C (-40° F to 
185° F)
Humidity (operating) 
5% to 95%  
non-condensing 
5% to 95% 
non-condensing 
5% to 95% 
non-condensing
5% to 95% 
non-condensing
5% to 95% 
non-condensing
Multi-Gigabit product matrix
OS6560-P24Z24
OS6560-P48Z16
OS6560-P24Z8
Gigabit PoE port count
24
48
24
Multi-Gigabit port count
24
16
8
1G/10G SFP+
4
4
2
20G QSFP+ stacking ports
2
2
0
MACSec capable ports
0
All 1G/2.5G RJ45
2 x 1G SFP
2 x 10 SFP+ (*)
0
USB port
1
1
1
IEEE 1588v2 PTP support
N/S
1G & 10G ports
N/S
Console port
1
1
1
Primary slide-in PSU slot
1
1
1
Backup slide-in PSU slot
1
1
1
Fans
2
2
2
File system flash
2 GB
2 GB
2 GB
RAM
2 GB
2 GB
2 GB
Max switching ASIC capacity 
336 Gb/s
336 Gb/s
112 Gb/s
Switch Capacity with 4x10GE ports  
and 2x20GE stacking ports (all ports,  
full duplex)
280 Gb/s
304 Gb/s
112 Gb/s
Switch frame rate with 4x10GE ports 
and 2x20GE stacking ports @ 64-byte 
packet
208 Mpps
226 Mpps
83.33 Mpps
Stacking Capacity (each)
80 Gb/s
80 Gb/s
40 Gb/s
Stacking Capacity (total)
640Gb/s
640Gb/s
320Gb/s
System power consumption
42 W/92 W
89 W
28 W/66 W

<<<PAGE 515>>>
5
Datasheet  
Alcatel-Lucent OmniSwitch 6560
Multi-Gigabit product matrix
OS6560-P24Z24
OS6560-P48Z16
OS6560-P24Z8
System heat dissipation
143/314 (BTU/h)
303 (BTU/h)
95/225 (BTU/h)
Power consumption w/PoE
600 W
920 W
300 W
Heat dissipation w/PoE
2047 (BTU/h)
3140 (BTU/h)
1023 (BTU/h)
Acoustics (dB) @27C*
37-54 (dBA)
45-55 (dBA)
45-55 (dBA)
MTBF (hours)
372k/352k
296k
363k/337k
Height
4.4 cm (1.73 in)
4.4 cm (1.73 in)
4.4 cm (1.73 in)
Width
44 cm (17.33 in)
44 cm (17.33 in)
44 cm (17.33 in)
Depth
35 cm (13.78 in)
35 cm (13.78 in)
35 cm (13.78 in)
Weight
4.58 kg (10.1 lb)
4.67 kg (10.3 lb)
4.58 kg (10.1 lb)
Operating temperature
0° C to 45° C  
(32° F to 113° F)
0° C to 45° C  
(32° F to 113° F)
0° C to 45° C  
(32° F to 113° F)
Storage temperature
-40° C to 85° C  
(-40° F to 185° F)
-40° C to 85° C  
(-40° F to 185° F)
-40° C to 85° C  
(-40° F to 185° F)
Humidity (operating)
5% to 95%  
non-condensing 
5% to 95%  
non-condensing 
5% to 95%  
non-condensing
(*) Note: Only available on part number OS6560-P48Z16 (904044-90)
OmniSwitch 6560
6560 backup power supply and specifications 
All OmniSwitch 6560 models support 1+1 hot-swappable secondary\redundant power supplies in a 1RU 
configuration, allowing for easier maintenance and replacement. Non-PoE models have a fixed, internal, primary 
supply and a modular, internal secondary power supply. PoE models have modular, internal, primary and 
secondary power supplies. The OmniSwitch 6560 PoE models also supports power load-sharing for an increase 
PoE power budget.
PS models
OS6560-BP
OS6560-BP-P
OS6560-BP-PH
OS6560-BP-PX
Description
Modular 150W AC power 
supply.  Provides system 
power to one non-PoE 
switch
Modular 300-W AC power 
supply. Provides system 
and PoE power to one 24-
port PoE switch
Modular 600-W AC PoE 
power supply. Provides 
system and PoE power to 
one 24-port PoE switch
Modular 920-W AC PoE power 
supply. Provides system and PoE 
power to one 48-port PoE switch
Dimension
4.0 cm x 7.3 cm x 18.5 cm 
(1.57 in x 2.87 in x 7.28 in)
4.0 cm x 7.3 cm x  
18.5 cm (1.57 in x  
2.87 in x 7.28 in)
4.0 cm x 7.3 cm x  
18.5 cm (1.57 in x  
2.87 in x 7.28 in)
4.0 cm x 7.3 cm x  
18.5 cm (1.57 in x  
2.87 in x 7.28 in)
Weight
.5 kg (1.11 lb)
1.00 kg (2.2 lb)
1.02 kg (2.25 lb)
1.05 kg (2.32 lb)
PoE with 1 PSU**
N/A
Up to 245 W
Up to 532 W
Up to 815 W
PoE with 2 
PSU**	
N/A
Up to 532 W
Up to 1085 W
Up to 1645 W
Input voltage/
current
90 V to 136 V AC/3 A 
180 V to 264 VAC/1.5 A
90 V to 136 V AC/2.65 A
180 V to 264 VAC/1.5 A
90 V to 136 V AC/8.5 A
180 V to 264 V AC/ 
4.25 A
90 V to 136 V AC/13 A
180 V to 264 V AC/ 
6.5 A
Max output 
power/current 
150 W/12.5 A
300 W/5.5 A
600 W/11 A
920 W/16.88 A
Power supply 
efficiency
90%
92%
92%
89%
Fans
1
1
1
1
** PoE budget and load sharing PoE budget is dependent on the OS6560 PoE model.
See the OS6560 Hardware User Guide for detailed information related to switch model, power supply and available power budget combinations.

<<<PAGE 516>>>
6
Datasheet  
Alcatel-Lucent OmniSwitch 6560
Commercial references
OmniSwitch 6560 Gigabit models
OS6560-24X4 
Gigabit fixed chassis in 1RU size. Includes 24 RJ-45 10/100/1G BaseT, 2xSFP(1G) and 4xSFP+ (1G/10G) uplink/
stacking ports, internal AC supply, power cord, user guides, and 19” rack mount hardware.
OS6560-P24X4
Gigabit fixed chassis in 1RU size. Includes 24 RJ-45 10/100/1G BaseT PoE+, 2xSFP(1G) and 4xSFP+ (1G/10G) uplink/
stacking ports, 600W AC supply, power cord, user guides, and 19” rack mount hardware.
OS6560-48X4
Gigabit fixed chassis in 1RU size. Includes 48 RJ-45 10/100/1G BaseT, 2xSFP(1G) and 4xSFP+ (1G/10G) uplink/
stacking ports, internal AC supply, power cord, user guides, and 19” rack mount hardware.
OS6560-P48X4
Gigabit fixed chassis in 1RU size. Includes 48 RJ-45 10/100/1G BaseT PoE+, 2xSFP(1G) and 4xSFP+ (1G/10G) uplink/
stacking ports, 920W AC supply, power cord, user guides, and 19” rack mount hardware.
OS6560-X10
10GigE fixed chassis 8 SFP+ 10GigE, 2 QSFP+ (20G) stacking ports. 1RU size, internal AC power supply. Includes 
power cord, guides, and 19” rack mount hardware.
OS6560-P24Z8
Multi-GigE fixed chassis in 1RU size. Includes 8 RJ-45 100/1G/2.5G BaseT HPoE, 16 RJ-45 10/100/1G BaseT PoE and 
2xSFP+ (1G/10G) ports, 300W AC supply, power cord, user guides, and 19” rack mount hardware.
OS6560-P24Z24
Multi-GigE fixed chassis in 1RU size. Includes 24 RJ-45 100/1G/2.5G BaseT HPoE, 4xSFP+ (1G/10G) and 2x20G 
stacking ports, 600W AC supply, power cord, user guides, and 19” rack mount hardware.
OS6560-PXZ24
A bundle of OS6560-P24Z24 with a 920W power supply. Multi-GigE fixed chassis in 1RU size. Includes 24 RJ-45 
100/1G/2.5G BaseT HPoE, 4xSFP+ (1G/10G) and 2x20G stacking ports, 920W AC supply, power cord, user guides, 
and 19” rack mount hardware.
OS6560-P48Z16
Multi-GigE fixed chassis in 1RU size. Includes 16 RJ-45 100/1G/2.5G BaseT HPoE, 32 RJ-45 10/100/1G BaseT PoE, 
4xSFP+(1G/10G) and 2x20G stacking ports, 920W AC supply, power cord, user guides and 19” rack mount hardware.
OmniSwitch 6560 power supplies
OS6560-BP
OS6560-BP modular 150W AC non-PoE backup power supply. Provides system backup power  
to one OS6560 non-PoE switch. Ships with power cord.
OS6560-BP-P
OS6560-BP-P modular 300W AC PoE backup power supply. Provides system and PoE backup power to one OS6560 
PoE switch. Ships with power cord.
OS6560-BP-PH
OS6560-BP-PH modular 600W AC PoE backup power supply. Provides system and PoE backup power to one 
OS6560 PoE switch. Ships with power cord.
OS6560-BP-PX
OS6560-BP-PX modular 920W AC PoE backup power supply. Provides system and PoE backup power to one OS6560 
PoE switch. Ships with power cord.
OmniSwitch 6560 License Options
OS6560-SW-PERF
Performance software license allowing 2 additional fixed SFP+ ports to operate at 10G speed for a total of 6 x 10G 
SFP+ ports.
OmniSwitch 6560 transceivers and cables
OS6560-CBL-40
OS6560 20 Gigabit direct attached stacking copper cable (40 cm, QSFP+)
OS6560-CBL-100
OS6560 20 Gigabit direct attached stacking copper cable (100 cm, QSFP+)
OS6560-CBL-300
OS6560 20 Gigabit direct attached stacking copper cable (300 cm, QSFP+)
SFP-10G-C1M
10 Gigabit direct attached uplink/stacking copper cable (1 m, SFP+)
SFP-10G-C3M
10 Gigabit direct attached uplink/stacking copper cable (3 m, SFP+)
SFP-10G-C7M
10 Gigabit direct attached uplink/stacking copper cable (7 m, SFP+)
SFP-GIG-T
1000Base-T Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and full-duplex mode
SFP-GIG-SX
1000Base-SX Gigabit Ethernet optical transceiver (SFP MSA) 
SFP-GIG-LX
1000Base-LX Gigabit Ethernet optical transceiver (SFP MSA) 
SFP-GIG-LH40
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on 
9/125 µm SMF 
SFP-GIG-LH70
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on 
9/125 µm SMF 
SFP-10G-SR
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 850 nm wavelength (nominal) with an LC 
connector. Typical reach of 300 m

<<<PAGE 517>>>
7
Datasheet  
Alcatel-Lucent OmniSwitch 6560
OmniSwitch 6560 transceivers and cables (continued)
SFP-10G-LR
10 Gigabit optical transceiver (SFP+). Supports monomode fiber over 1310 nm wavelength (nominal) with an LC 
connector. Typical reach of 10 km 
SFP-10G-ZR
10 Gigabit optical transceiver (SFP+). Supports data transmission at 1550 nm over up to 80km single mode fiber. LC 
connector type.
SFP-10G-ER
10 Gigabit optical transceiver (SFP+). Supports monomode fiber over 1550 nm wavelength (nominal) with an LC 
connector. Typical reach of 40 km
Warranty
The OmniSwitch 6560 family comes with a Limited Lifetime Warranty.
Detailed product features
Simplified management
•	 Intuitive CLI in a scriptable BASH 
environment via console, Telnet or Secure 
Shell (SSH) v2 over IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over  
IPv4/ IPv6+
•	 Fully programmable RESTful web 
services interface with XML and JSON 
support. API enables access to CLI and 
individual mib objects
•	 Integrated with Alcatel-Lucent 
OmniVista® products for network 
management
•	 Full configuration and reporting using 
SNMPv1/2/3 to facilitate third-party 
network management over IPv4/IPv6
•	 File upload using USB, TFTP, FTP, SFTP or 
SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line editing, 
bulk configuration and out-of-the-box 
auto-provisioning
•	 Fully programmable OpenFlow 1.3.1 
and1.0 agent for control of native 
OpenFlow and hybrid ports
•	 Multiple microcode image support with 
fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server managed 
by Alcatel-Lucent DNS/DHCP IP  
Address Management
Monitoring and troubleshooting
•	 Local (on the flash memory) and remote 
server logging (Syslog): event and 
command logging
•	 IP tools: ping and trace route
•	 Dying Gasp support via SNMP  
and syslog messages
•	 Loopback IP address support  
for management per service
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD), 
Digital Diagnostic Monitoring (DDM)
Network configuration
•	 Remote auto-configuration download 
feature
•	 Auto-negotiating 10/100/1000 ports 
automatically configure port speed and 
duplex setting
•	 Auto MDI/MDIX automatically configures 
transmit and receive signals to support 
straight-through and crossover cabling
•	 BOOTP/DHCP client allows auto- 
configuration of switch IP information 
for simplified deployment
•	 DHCP relay to forward client requests to 
a DHCP server
•	 IEEE 802.1AB Link Layer Discovery 
Protocol (LLDP) with MED extensions for 
automated device discovery
•	 Multiple VLAN Registration Protocol 
(MVRP) for IEEE 802.1Q-compliant VLAN 
pruning and dynamic VLAN creation
•	 Auto QoS for switch management traffic 
as well as traffic from Alcatel-Lucent  
IP phones
•	 Network Time Protocol (NTP) for 
network- wide time synchronization
•	 Virtual chassis up to 8 units
Resiliency and high availability
•	 Unified management, control and virtual 
chassis technology
•	 Virtual Chassis 1+N redundant 
supervisor manager
•	 Virtual Chassis In-Service Software 
Upgrade (ISSU)
•	 Smart continuous switching technology
•	 ITU-T G.8032/Y1344 2010: Ethernet  
Ring Protection
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning Tree 
Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+) and 
1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link Aggregation 
Control Protocol (LACP) and static LAG 
groups across modules
•	 Virtual Router Redundancy Protocol 
(VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Bidirectional Forwarding Detection (BFD) 
for fast failure detection and reduced  
re-convergence times in a routed 
environment
•	 Redundant and hot-swappable  
power supplies
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection: Auto- 
detection and recovery of Virtual Chassis 
splitting due to one or more VFL or 
stack element failures
Advanced security
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive user-
policy-based NAC
•	 Autosensing IEEE 802.1X multi-client, 
multi-VLAN support
•	 MAC-based authentication for non-IEEE 
802.1X hosts
•	 Web based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing pre-
defined policy configuration to 
authenticated clients — VLAN, ACL, BW

<<<PAGE 518>>>
8
Datasheet  
Alcatel-Lucent OmniSwitch 6560
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial-In 
User Service (RADIUS) and Lightweight 
Directory Access Protocol (LDAP) 
administrator authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-based 
filtering in hardware (Layer 1 to Layer 4)
•	 DHCP Snooping, DHCP IP and Address 
Resolution Protocol (ARP) spoof 
protection
•	 ARP poisoning detection
•	 IP Source Filtering as a protective and 
effective mechanism against ARP attacks
•	 Bring Your Own Device (BYoD) provides 
on-boarding of Guest, IT/non-IT 
issued and silent devices. Restriction/
Remediation of traffic from non-
compliant devices. Uses RADIUS CoA 
to dynamically enforce User Network 
Profiles based on Authentication, 
Profiling, Posture check of devices with 
OmniVista UPAM or Aruba ClearPass 
management applications.
Converged networks
PoE
•	 PoE models support Alcatel-Lucent IP 
phones and WLAN access points, as well 
as any IEEE 802.3af, IEEE 802.3at or 
802.3bt compliant end device
•	 Configurable per-port PoE priority and 
max power for power allocation
•	 Dynamic PoE allocation: Delivers  
only the power needed by the  
powered devices (PD) up to the total 
power budget for most efficient  
power consumption
QoS
•	 Priority queues: Eight hardware-based 
queues per port for flexible QoS 
management
•	 Traffic prioritization: Flow-based QoS 
with internal and external (a.k.a., 
remarking) prioritization
•	 Bandwidth management: Flow-based 
bandwidth management, ingress rate 
limiting; egress rate shaping per port
•	 Queue management: Configurable 
scheduling algorithms — Strict Priority 
Queuing (SPQ), Weighted Round  
Robin (WRR)
•	 Congestion avoidance: Support for End- 
to-End Head-Of-Line (E2E-HOL) Blocking 
Protection
•	 Auto QoS for switch management traffic 
as well as traffic from Alcatel-Lucent  
IP phones
Software Defined 
Networking (SDN)
•	 Programmable AOS RESTful API
•	 Fully programmable OpenFlow 1.3.1 and 
1.0 agent for control  
of native OpenFlow and  
hybrid ports*
•	 OpenStack networking plug-in*
Layer-2, Layer-3 Routing and 
Multicast
Layer-2 switching
•	 Up to 16k MAC Addresses
•	 Up to 4000 VLANs
•	 Up to 1.5k total system policies
•	 Latency: < 4 µs
•	 Max Frame: 9216 bytes (jumbo)
IPv4 and IPv6
•	 Static routing for IPv4 and IPv6
•	 RIP v1 and v2 for IPv4; RIPng for IPv6
•	 Up to 256 IPv4 and 128 IPv6 static and 
RIP routes
•	 Up to 128 IPv4 and 16 IPv6 interfaces 
•	 OSPFv2 & OSPFv3 routing
•	 OSPFv2, OSPFv3 support
Multicast
•	 IGMPv1/v2/v3 snooping to optimize 
multicast traffic
•	 Multicast Listener Discovery (MLD) v1/v2 
snooping+
•	 Up to 1000 multicast groups
•	 IP Multicast VLAN (IPMVLAN) for 
optimized multicast replication at the 
edge, saving network core resources
Network protocols
•	 DHCP relay (including generic  
UDP relay)
•	 ARP
•	 Generic User Datagram Protocol (UDP) 
relay per VLAN
•	 DHCP Option 82 — configurable relay 
agent information
*Future software development
Indicators
System LEDs 
•	 System (OK) (chassis HW/SW status)
•	 PWR (primary power supply status)
•	 VC (virtual chassis primary)
•	 LED segment display indicates the 
Virtual Chassis ID of the unit in the 
stack: 1 to 2
Per-port LEDs
•	 10/100/1000: PoE, link/activity
•	 100/1000/2.5GE: link/activity
•	 100/1000/2.5GE: PoE status
•	 SFP: Link/activity
•	 Virtual Chassis (VFL): Link/activity
Compliance and certifications
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015  
Subpart B (Class A)
•	 VCCI (Class A limits. Note: Class A with 
UTP cables)
•	 ICES–003:2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) - C-Tick
•	 AS/NZS 3548 (Class A limits.  
Note: Class A with UTP cables)
•	 CE-Mark: Marking for European 
countries (Class A limits. Note: Class A 
with UTP cables)
•	 CE Emission consists of:
¬	 EN 50581: Standard for technical 
documentation  
for RoHS recast
¬	 EN 55022 (EMI and EMC requirement) 
¬	 EN 55024: 2010 (ITE Immunity 
characteristics)
¬	 EN 61000-3-2 (Limits for harmonic 
current emissions)
¬	 EN 61000-3-3
¬	 EN 61000-4-2
¬	 EN 61000-4-3
¬	 EN 61000-4-4
¬	 EN 61000-4-5
¬	 EN 61000-4-6
¬	 EN 61000-4-8
¬	 EN 61000-4-11
¬	 IEEE802.3: Hi-Pot Test (2250 V DC on 
all Ethernet ports)
Safety agency certifications
•	 CDRH Laser
•	 Compliant with Restriction on 
Hazardous Substances (RoHS) and 
Waste Electrical and Electronic 
Equipment (WEEE) directives.
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 IEC 62368-1
•	 UL 60950-1, 2nd Edition, Information 
Technology Equipment
•	 CAN/CSA C22.2 No. 60950-1-07, 
2nd Edition, Information Technology 
Equipment

<<<PAGE 519>>>
9
Datasheet  
Alcatel-Lucent OmniSwitch 6560
•	 IEC 60950-1, with all National Deviations 
¬	 UL-AR, Argentina
¬	 AS/NZ TS-001 and 60950, Australia
¬	 ANATEL, Brazil
¬	 CCC, China
¬	 UL-GS Mark, Germany
¬	 KCC, Korea
¬	 NOM-019 SCFI, Mexico
¬	 CU, EAC, Russia
¬	 BSMI, Taiwan
Supported standards
IEEE standards
•	 IEEE 802.1D (STP)
•	 IEEE 802.1p (CoS)
•	 IEEE 802.1Q (VLANs)
•	 IEEE 802.1ad (Provider Bridge) Q-in-Q 
(VLAN stacking)*
•	 IEEE 802.1s (MSTP)
•	 IEEE 802.1w (RSTP)
•	 IEEE 802.1AE MAC Security
•	 IEEE 802.1X (Port Based Network Access 
Protocol)
•	 IEEE 802.3i (10Base-T)
•	 IEEE 802.3u (Fast Ethernet)
•	 IEEE 802.3x (Flow Control)
•	 IEEE 802.3z (Gigabit Ethernet)
•	 IEEE 802.3ab (1000Base-T)
•	 IEEE 802.3ac (VLAN Tagging)
•	 IEEE 802.3ad (Link Aggregation)
•	 IEEE 802.3ae (10 Gigabit Ethernet)
•	 IEEE 802.3af (Power-over-Ethernet)
•	 IEEE 802.3at (Power-over-Ethernet)
•	 IEEE 802.3bt (Power-over-Ethernet)
•	 IEEE 802.3az (Energy Efficient Ethernet)
•	 IEEE 802.3bz (2.5GE Multi-Gigabit 
Ethernet)
• 	IEEE 1588v2 Precision Timing Protocol 
(PTP)
ITU-T recommendations
•	 G.8032/Y.1344 2010: Ethernet Ring 
Protection (ERPv2)
IETF RFCs
RIP
•	 RFC 1058 RIP v1
•	 RFC 1722/1723/1724/2453 RIP v2 and 
MIB
•	 RFC 1812/2644 IPv4 Router 
Requirement
•	 RFC 2080 RIPng for IPv6
OSPF
•	 RFC 1850/2328 OSPF v2 and MIB
•	 RFC 2154 OSPF MD5 Signature
•	 RFC 2370/3630 OSPF Opaque LSA
•	 RFC 3623 OSPF Graceful Restart
• 	RFC 1765 OSPF Database Overflow
• 	RFC 3101 OSPF NSSA
• 	RFC 5838 MIB for OSPFv3 
• 	RFC 4552 Authentication for OSPFv3
• 	RFC 5340/5838 OSPF v3 and MIB
IP Multicast
•	 RFC 1112 IGMP v1
•	 RFC 2236/2933 IGMP v2 and MIB
•	 RFC 2365 Multicast
•	 RFC 3376 IGMPv3 for IPv6
IPv6
•	 RFC 1886 DNS for IPv6
•	 RFC 2292/2373/2374/2460/2462
•	 RFC 2461 NDP
•	 RFC 2463/2466 ICMP v6 and MIB
•	 RFC 2452/2454 IPv6 TCP/ 
UDP MIB
•	 RFC 2464/2553/2893/3493/3513
•	 RFC 3056 IPv6 Tunneling
•	 RFC 3542/3587 IPv6
•	 RFC 4007 IPv6 Scoped Address 
Architecture
•	 RFC 4193 Unique Local IPv6 Unicast 
Addresses
Manageability 
•	 RFC 854/855 Telnet and Telnet options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1 and SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP Traps
•	 RFC 1573/2233/2863 Private  
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•	 RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from Forms: 
multipart/form-data
•	 RFC 2396 Uniform Resource Identifiers 
(URI): Generic Syntax
•	 RFC 2570-2576/3410-3415/3584  
SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 3826 (AES) Cipher Algorithm in the 
SNMP User-based Security Model
•	 RFC 4122 A Universally Unique IDentifier 
(UUID) URN Namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4627 JavaScript Object  
Notation (JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP  
Status Codes 
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP)  
and crypto algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618 
RADIUS Authentication and Client MIB
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 4301 Security Architecture for IP
Quality of service
•	 RFC 896 Congestion control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 3635 Pause Control
•	 RFC 2697 srTCM*
•	 RFC 2698 trTCM*
Others
•	 RFC 791/894/1024/1349 IP  
and IP/Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 NTP v3 and Simple NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 DHCP
•	 RFC 1757/2819 RMON and MIB

<<<PAGE 520>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trademarks-copyright. All 
other trademarks are the property of their respective owners. The information presented is subject to change without notice. 
Neither ALE Holding nor any of its affiliates assumes any responsibility for inaccuracies contained herein.  
© Copyright 2022 ALE International, ALE USA Inc. All rights reserved in all countries. MPR00364217EN (April 2022)
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 2338/3768/2787 VRRP and MIB
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
*Future AOS software feature 
Services and support
For more information about our Professional services, Support services, and Managed services, please go to 
https://www.al-enterprise.com/en/services.

<<<PAGE 521>>>
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Alcatel-Lucent  
OmniSwitch 6870
Premium stackable Gigabit and  
Multi-gigabit LAN switch family
The Alcatel-Lucent 
OmniSwitch® 6870, built on 
the innovative OmniFabric 
architecture, is designed to 
make networks more secure, 
flexible, and intelligent. With 
comprehensive protocol 
support, OmniFabric enables 
seamless interoperability across 
various network environments, 
ensuring readiness for Zero Trust network deployment. 
Key Features and Benefits
Multi-Technology Fabric
•	 Flexible Fabric Options: The first solution to support SPBM, VxLAN-EVPN, and MPLS within the Alcatel-
Lucent OS (AOS) unified service manager framework. This flexibility allows users to select the most 
suitable fabric for their needs, making deployment easy across diverse infrastructures.
•	 Simplified Network Management: OmniVista® Cirrus simplifies network management, allowing 
seamless functionality across different fabric technologies.
Robust Security
•	 Data Protection with MACsec Encryption: OmniFabric integrates MACsec to secure user data at Layer 2, 
maintaining data integrity without adding network complexity.
•	 Secure Boot for Trusted Operations: Secure Boot ensures that only trusted, manufacturer-approved 
software runs on devices, reducing the risk of malware or unauthorized code. This feature protects 
against a wide range of security threats, helping organizations meet compliance requirements for data 
integrity and privacy.
AI-Enabled Flow Telemetry
•	 Detailed Traffic Insights: The flow-based telemetry engine built into OmniSwitch 6870 provides 
comprehensive visibility into network traffic at the application level. This capability is essential for 
proactive management, delivering granular insights that empower network administrators to optimize 
and secure data flows.
OS6870-P48M
OS6870-P24M
OS6870-V12
OS6870-48

<<<PAGE 522>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 6870
•	 AI-Powered Optimization: Powered by the AI-driven OmniVista Network Advisor, OmniSwitch 6870 can 
automatically identify risks, resolve issues, and optimize performance, helping to prevent disruptions. 
This proactive management approach reduces downtime and troubleshooting time, ensuring a 
resilient network.
Why Choose OmniSwitch 6870?
The OmniSwitch 6870 combines versatile fabric support, strong security, and AI intelligence to create a 
flexible, secure, and low-maintenance platform tailored to meet a wide range of customer needs. This 
platform offers enhanced security, operational simplicity, and adaptable performance for the demands of 
modern network environments.
With Alcatel-Lucent OmniVista® Network Management System, you choose how you want to manage your 
network either on-premises or from the cloud to increase IT efficiency and business agility. 
Highlights
Premium models
•	 24 10GbE Multi-gigabit ports or 48 5GbE Multi-gigabit, up to 95W 802.3bt PoE with 600W, 1200W and 
2000W redundant PSU options
•	 	12 1/10/25G ports with AC/DC PSU options
•	 	All premium models have fixed 2 x 200G VFL stacking ports and an uplink module slot
•	 	Uplink module options of 2 100G ports or 6 25/50G ports. License required for 50G speed
•	 	All ports support 256bit MACsec
Advanced models
•	 	24/48 2.5GbE Multi-gigabit ports, up to 60W 802.3bt PoE with 600W and 1200W redundant PSU options
•	 	24/48 1GbE ports with AC/DC PSU options
•	 	All advanced models have fixed 2 100G VFL stacking ports and 4 or 6 1/10/25G uplink ports
•	 	All user and uplink ports support 256bit MACsec1
All models
•	 OmniFabric: SPB, VxLAN-EVPN2 and MPLS2
•	 	Secure boot2
•	 Streaming network telemetry2 and DPI2
•	 	1588v2 End-to-End Transparent Clock
•	 	Field replaceable redundant PSU both primary and backup
•	 	Mix and match any supported PoE PSU redundancy to meet the PoE budget requirement while providing 
continues system operation
•	 The lowest power consumption level in similar class in term of wattage per switching capacity.
•	 	Virtual chassis up to 8 with any model mix
•	 	VFL stacking port can be used for uplink port in non-VC operation
•	 	1RU compact size with EMP (out-of-band management), console and USB ports
•	 	Manage through Alcatel-Lucent OmniVista Cirrus Network Management System help visualize full wired-
wireless network to increase IT efficiency and business agility
1. MACsec not supported on OS6870-24 port 25/26 & OS6870-48 port 49/50
2. Will be supported in a later AOS release
Alcatel-Lucent OmniSwitch 6870 models
The OmniSwitch 6870 family offers customers an extensive selection of fixed-configuration switches with 
up to 95 watts of PoE per port and power supply options that can power a wide range of next-gen Ethernet 
edge PoE devices, be it pan-tilt-zoom cameras or Wi-Fi 6 /6E/7 devices. All models are in an 1RU form factor 
and are 19-inch rack-mountable. 
OmniSwitch 6870 family comprises of four advanced and three premium models. Premium models have 
modular uplink slot that can support 6 x 25G/50G or 2 x 100G uplink modules and have 2  x 200G fixed 
virtual chassis ports. Advanced models support fixed  2 x 100G virtual chassis ports and fixed 4 x 25G or  
6 x 25G SFP28 uplinks. All virtual chassis ports can also act as uplink ports. 
All OS6870 models can form virtual chassis with each other and support 256-bit MACsec on all ports. All PoE 
models support upto 60/95 watts of IEEE 802.3 bt compliant PoE. All OmniSwitch 6870 models have an USB 
2.0 port, a RJ45 console port and an RJ45 Ethernet management (EMP) port.

<<<PAGE 523>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Table 1. OmniSwitch 6870 Gigabit switch configurations
Gigabit models
Gigabit ports
Uplinks & VFL ports
Supported  
power supplies
PoE budget
With  
1 PS
With  
2 PS
The bundle 
offered
Advanced models
OS6870-24
24 RJ45
4 x 1/10/25G SFP28, 
2 x 40/100G QSFP28
OS6870-BP, 
OS6870-BP-D
N/A
N/A
OS6870-
24-##
OS6870-48
48 RJ45
4 x 1/10/25G SFP28,
2 x 40/100G QSFP28
OS6870-BP, 
OS6870-BP-D
N/A
N/A
OS6870-
24D
Table 2. OmniSwitch 6870 Multi-gigabit switch configurations
Models
Multi-gigagbit ports
Uplinks & VFL ports 
Supported  
power supplies
PoE budget
With  
1 PS
With  
2 PS
The bundle 
offered
Advanced models
OS6870-P24Z
24 x 10M/100M/1G/2.5G 
802.3bt PoE	
	
6 x 1/10/25G SFP28,
2 x 40/100G QSFP28
OS870-BPPH
375W
921W
OS6870-
PH24Z-##
OS6870-BPPX
739W
@ 
115VAC
1440W
@ 115VAC
OS6870-
PX24Z-##
921W
@ 
230VAC
1440W
@ 230VAC
OS6870-P48Z
48 x 10M/100M/1G/2.5G 
802.3bt PoE
6 x 1/10/25G SFP28,
2 x 40/100G QSFP28
OS6870-BPPH
339W
885W
OS6870-
PH48Z-##
OS6870-BPPX
703W
@ 
115VAC
1612W
@ 115VAC
OS6870-
PX48Z-##
885W
@ 
230VAC
1976W
@ 230VAC
Models
Multi-gigagbit and fiber 
ports
Uplinks and VFL ports
Supported  
power supplies
PoE 
budget
With  
1 PS
With  
2 PS
The bundle 
offered
Premium models
OS6870-P48M
48 x 10M/100M/1G/2.5G/5G 
 95W 802.3bt PoE
Modular,
2 x 40/100/200G 
QSFP56
OS6870-BPPH
216W
762W
OS6870-
PH48M-##
OS6870-BPPX
580W
@ 
115VAC
1490W
@ 115VAC
OS6870-
PX48M-##
762W
@ 
230VAC
1854W
@ 230VAC
OS6870-BPXL
580W  
@115 
VAC
1490W 
@115 
VAC
OS6870-
PXL48M-##
1490W 
@230 
VAC
3309W 
@230 
VAC

<<<PAGE 524>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 6870
OS6870-P24M
24 x 
10M/100M/1G/2.5G/5G/10G 
95W PoE, MACsec
Modular,
2 x 100/200G QSFP56
OS6870-BPPH
242W
788W
OS6870- 
PH24M-##
OS6870-BPPX
606W
@ 
115VAC
1516W
@ 115VAC
OS6870- 
PX24M-##
788W
@ 
230VAC
1880W
@ 230VAC
OS6870-BPXL
606W 
@115VAC
1516W 
@115VAC
OS6870- 
PXL24M-##
1516W 
@230VAC
2280W 
@230VAC
OS6870-V12
12 x 1/10/25G SFP28 ports
Modular, 
2 x 100/200G QSFP26
OS6870-BPH
NA
NA
OS6870- 
V12-##
OS6870-BP-D
NA
NA
OS6870- 
V12D
OS6870 supports unbalanced PoE load-sharing. Two different PoE PSUs can be combined in one device to provide the system and PoE redun-
dancy. Please refer to OmniSwitch 6870 Hardware Guide for the detail.
Table 3. OmniSwitch 6870 product specifications
Criteria
Advanced and premium models 
USB port (Type-A)
1
Out-of-band EMP port (RJ45)
1
Console port (RJ45)
1
Fans
Non-PoE models : 2 + 1 redundant, fixed
PoE and V12 models : 3 + 1 redundant, fixed
Altitude
13,000 ft
Operating temperature
0°C to 45°C  (32°F to 113°F)
Storage temperature
-40°C to 85°C (-40°F to 185°F)
Humidity  
(operating and storage)
5% to 95% non-condensing
Air flow
Front-to-back
Dimensions (H x W x D)
OS6870-P48Z, OS6870-P24Z, 
OS6870-P48M, OS6870-P24M
4.4 cm x 44 cm x 44.2 cm 
1.73 in x 17.32 in x 17.40 in
OS6870-24, OS6870-48, OS6870-V12
4.4 cm x 44 cm x 35 cm 
1.73 in x 17.32 in x 13.78 in 
Port LEDs
•	 RJ45 ports: two LEDs per port
	
¬ PoE LED: amber: link/activity.  
Off: No PoE 
	
¬ Speed LED: Solid: link, Blinking: activity
Amber: 10G speed
Magenta: 5G speed
Blue: 2.5G speed
Green: 100M/1G speed
Off: Link down
•	 Fiber ports: one LED per port
	
¬ Solid: link, Blinking: activity 
Amber: VC 
Green: Uplink
•	 EMP port:
	
¬  Solid green: link, Blinking green: activity

<<<PAGE 525>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Criteria
Advanced and premium models 
System LEDs
•	 OK1: green/yellow operational status of the switch 
•	 VC: green/yellow master or slave role in  
VC configuration 
•	 PS: green: normal operation, amber: fault
•	 VC ID 1-4: VC ID will be denoted by adding the numbers of the 
LEDs that are lit up. For example: if 1, 3, 4 are lit up, VC ID is 8. 
OmniSwitch 6870 uplink modules
The premium models on OS6870 support optional modules for uplinks. These modules are not included in 
the default shipping bundle and should be purchased separately.
Table 4. OmniSwitch 6870 uplink modules configuration 
Uplink module
Description
OS6870-LNI-U6
6 x 1/10/25/50G SFP56, 256-bit MACsec capable ports.
Purchase OS6870-SW-PERF license separately to enable 50G speed.
OS6870-CNI-U2
2 x 40/100G QSFP28, 256-bit MACsec capable ports
Table 5. OmniSwitch 6870 performance specifications
Criteria
Advanced and premium modes (OS6870)
Switching capacity (Aggregated)
OS6870-V12: 2,000 Gb/s
OS6870-P48M: 1,880 Gb/s
OS6870-P24M: 1,880 Gb/s
OS6870-P48Z: 940 Gb/s
OS6870-P24Z: 820 Gb/s
OS6870-48 : 696 Gb/s
OS6870-24 : 648 Gb/s
Throughput
OS6870-V12: 1,488 Mpps
OS6870-P48M: 1,398.8 Mpps
OS6870-P24M: 1,398.8 Mpps
OS6870-P48Z: 699.4 Mpps
OS6870-P24Z: 610.1 Mpps
OS6870-48 : 517.9 Mpps
OS6870-24 : 482.1 Mpps
Packet buffer
8MB
File system flash
32 GB
DRAM
8 GB
VLANs
4,000
MAC addresses
128 K
Max IPv4 routes
116 K
Max IPv6 routes
58 K
Max ARP
64K
Jumbo frames
9216 bytes
VFL ports capacity
Premium Models : 400 Gb/s or 800 Gb/s aggregate
Advanced Models: 200 Gb/s or 400 Gb/s aggregate
Maximum number of units in a virtual 
chassis
8
OS6870-LNI-U6
OS6870-CNI-U2

<<<PAGE 526>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Power supplies
All OmniSwitch 6870 models support 1+1 hot-swappable redundant. The primary and backup power 
supply units are internal and removable to allow for easier maintenance and replacement. The family also 
supports balanced and unbalanced load sharing for PoE. Any supported PoE PSU can be mixed to fulfill 
the PoE budget while providing the system redundancy.
The Advance models can provide up to 1976W of PoE per switch and the premium models can provide 
up to 2280W per switch. Please refer to Table 2 for the available PoE budget.
Table 6.1. OmniSwitch 6870 power supplies
PS models
OS6870-BP
OS6870-BP-D
OS6870-BPPH
OS6870-BPPX
Description
Modular AC power supply. 
Provides system power  
to one OS6870  
non-PoE switch
Modular DC power supply. 
Provides  
system power to  
one OS6870  
non-PoE switch
Modular 600-W AC PoE 
power supply. Provides 
system and PoE power to 
one OS6870 PoE switch
Modular 1200W AC PoE 
power supply. Provides 
system and PoE power to 
one OS6870 PoE switch
Dimensions  
(H x W x L)
3.9 cm x 7.35 cm x 18.5 cm
(1.54 in x 2.89 in x 7.28 in)
3.9 cm x 7.35 cm x 18.5 cm
(1.54 in x 2.89 in x 7.28 in)
3.98 cm x 7.3 cm x 18.5 cm
(1.57 in x 2.87 in x 7.28 in)
3.98 cm x 7.3 cm x 18.5 cm
(1.57 in x 2.87 in x 7.28 in)
Weight 
0.787 kg (1.74 lb)
0.787 kg (1.74 lb)
0.85 kg (1.87 lb)
0.85 kg (1.87 lb)
Max with 1 PSU
N/A
N/A
600W
1200W
Max with 2 
PSUs
N/A
N/A
1200W
2400W
Input voltage/
current
100V to 120 Vrms AC/4A
200V to 240Vrms AC/2A
-42 to -60 V DC/8A
100V to 120Vrms AC/8.5A
200V to 240Vrms AC/4.5A
100V to 120Vrms AC/12A
200V to 240Vrms AC/8.5A
Max output 
power/current
250W- 12V/20.8A
250W- 12V/20.8A
600W - 54.5V/11A
1000W - 54.5V/18.5A
1200W - 54.5V/22.02A
Fans
1
1
1
1
PS models
OS6870-BPXL
OS6870-BPH
Description
Modular 2000W AC PoE power supply. Provides 
system and PoE power to one OS6870-P48M or 
OS6870-P24M switch
Modular AC system power supply. Provides system 
power to one OS6870-V12 switch
Dimensions  
(H x W x L)
3.98 cm x 7.3 cm x 18.5 cm
(1.57 in x 2.87 in x 7.28 in)
3.9 cm x 7.35 cm x 18.5 cm
(1.54 in x 2.89 in x 7.28 in)
Weight 
0.9 kg (1.98 lb)
0.85 kg (1.87 lb)
Input voltage/current
100V to 120Vrms AC/12A
200V to 240Vrms AC/9.9A
100V to 120Vrms AC/7.6A
200V to 240Vrms AC/4A
Max output power/
current
1000W - 54.5V/18.4A
2000W - 54.5V/36.7A
550W - 12V/45.8A
Fans
1
1
Detailed product 
features
Simplified manageability  
and configuration
•	 Intuitive CLI in a scriptable BASH 
environment via console, Telnet or 
Secure Shell (SSH) v2 over IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over 
IPv4/IPv6
•	 Network Automation and 
Programmability Abstraction Layer 
with Multivendor (NAPALM) support
•	 Fully programmable RESTful web 
services interface with XML and JSON 
support. API enables access to CLI 
and individual mib objects
•	 Integrated with Alcatel-Lucent 
OmniVista® products for network 
management
•	 File upload using USB, TFTP, FTP, 
SFTP or SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line editing, 
bulk configuration and out-of-the-
box auto-provisioning
•	 Non-volatile memory for start-up 
configuration
•	 Multiple microcode image support 
with fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6

<<<PAGE 527>>>
7
Datasheet 
Alcatel-Lucent OmniSwitch 6870
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server 
managed by Alcatel-Lucent VitalQIP® 
DNS/DHCP IP Address Management
•	 Access to the AOS console via USB 
Adapter with Bluetooth technology 
provides wireless management 
access to the OmiSwitch 6870, 
eliminating the use of console cables
Cloud ready with  
Alcatel-Lucent  
OmniVista Cirrus
•	 OmniVista® Cirrus offers a secure, 
resilient and scalable cloud-based 
network management. It offers 
hassle free network deployment and 
easy service roll-out with advanced 
analytics for smarter decision 
making. It provides IT friendly Unified 
Access with secure authentication 
and policy enforcement for users  
and devices. 
Monitoring and 
troubleshooting
•	 Local (on the flash) and remote 
server logging (Syslog): event  
and command logging
•	 IP tools: ping and trace route
•	 Dying Gasp support via SNMP  
and syslog messages
•	 Loopback IP address support for 
management per service
•	 Management virtual routing and 
forwarding (VRF) support
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD), 
Digital Diagnostic Monitoring  
(DDM), and Time Domain 
Reflectometry (TDR)
Resiliency and high 
availability
•	 Unified management, control  
and virtual chassis technology
•	 Virtual Chassis 1+N redundant 
supervisor manager
•	 Virtual Chassis In-Service Software 
Upgrade (ISSU)
•	 Smart continuous switching 
technology
•	 ITU-T G.8032/Y1344 2010: Ethernet 
Ring Protection
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning 
Tree Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+) and 
1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link 
Aggregation Control Protocol 
(LACP) and static LAG groups across 
modules
•	 Virtual Router Redundancy Protocol 
(VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Bidirectional Forwarding Detection 
(BFD) for fast failure detection and 
reduced re-convergence times in a 
routed environment
•	 Redundant and hot-swappable 
power supplies
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection: Auto- 
detection and recovery of Virtual 
Chassis splitting due  
to one or more VFL or stack  
element failures
Advanced security
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive user-
policy-based NAC
•	 Autosensing IEEE 802.1X multi-client, 
multi-VLAN support for bridging and 
SPBM/VxLAN services
•	 MAC-based authentication for non-
IEEE 802.1X hosts
•	 Web based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing 
pre-defined policy configuration to 
authenticated clients — VLAN,  
ACL, BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial-
In User Service (RADIUS) and 
Lightweight Directory Access 
Protocol (LDAP) administrator 
authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-
based filtering in hardware (Layer 1 
to Layer 4)
•	 DHCP v4 and v6 Snooping, DHCP 
IP and Address Resolution Protocol 
(ARP) spoof protection
•  DHCPv6 guard and DHCPv6  
Client guard
•	 ARP poisoning detection
•	 IP v4 and v6 Source Filtering as a 
protective and effective mechanism 
against ARP attacks
•	 Bring Your Own Device (BYOD) 
provides on-boarding of Guest,  
IT/non-IT issued and silent devices. 
Restriction/Remediation of traffic 
from non-compliant devices. Uses 
RADIUS CoA to dynamically enforce 
User Network Profiles based on 
Authentication, Profiling, Posture 
check of devices.
•	 Role-based authentication for  
routed domains
Switch software security
•	 AOS secured diversified code 
solution is available on OmniSwitch 
6870, hardening it at both the 
software source code and binary 
executable levels to enhance overall 
network security.
•	 AOS secured diversified code 
protects networks from intrinsic 
vulnerabilities, code exploits, 
embedded malware, and potential 
back doors that could compromise 
mission critical operations.
•	 AOS secured diversified code is a 
proactive, defense approach toward 
network security that continuously 
defines and implements value-add 
capabilities to address both current 
and future threats.
QoS
•	 Priority queues: Eight hardware-
based queues per port for flexible 
QoS management
•	 Traffic prioritization: Flow-based QoS
•	 Flow-based traffic policing and 
bandwidth management
•	 32-bit IPv4/128-bit IPv6 non-
contiguous mask classification
•	 Egress traffic shaping
•	 DiffServ architecture
•	 Congestion avoidance: Support for 
end- to-end head-of-line (E2E-HOL) 
blocking prevention, and IEEE 802.3x 
Flow Control (FC)

<<<PAGE 528>>>
8
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Layer-3 routing  
and multicast 
IPv4 routing
•	 Multiple VRF
•	 Static routing
•	 Routing Information Protocol (RIP)  
v1 and v2
•	 Open Shortest Path First (OSPF) v2 
with Graceful Restart
•	 Intermediate System to Intermediate 
System (IS-IS) with Graceful Restart
•	 Border Gateway Protocol (BGP) v4 
with Graceful Restart
•	 Generic Routing Encapsulation (GRE) 
and IP/IP tunneling
•	 Virtual Router Redundancy Protocol 
(VRRPv2)
•	 DHCP relay (including generic  
UDP relay)
•	 Address Resolution Protocol (ARP)
•	 Policy-based routing and server  
load balancing
•	 DHCPv4 server
IPv6 routing
•	 Multiple VRF
•	 Internet Control Message Protocol  
version 6 (ICMPv6)
•	 Static routing
•	 Routing Information Protocol Next 
Generation (RIPng)
•	 Open Shortest Path First (OSPF) v3 
with Graceful Restart
•	 Intermediate System to Intermediate 
System (IS-IS) with Graceful Restart
•	 Multi-Topology IS-IS
•	 BGP v4 multiprotocol extensions for 
IPv6 routing (MP-BGP)
•	 Graceful Restart extensions for OSPF 
and BGP
•	 Virtual Router Redundancy Protocol 
version 3 (VRRPv3)
•	 Neighbor Discovery Protocol (NDP)
•	 Policy-based routing and server  
load balancing
•	 DHCPv6 server
•	 DHCPv6 relay & UDPv6 relay
IPv4/IPv6 multicast
•	 Internet Group Management 
Protocol (IGMP) v1/v2/v3 snooping
•	 Protocol Independent Multicast– 
Sparse-Mode (PIM-SM), Source 
Specific Multicast (PIM-SSM)
•	 Protocol Independent  
Multicast–Dense-Mode  
(PIM-DM), Bidirectional Protocol 
Independent Multicast (PIM-BiDir)
•	 Distance Vector Multicast Routing 
Protocol (DVMRP)
•	 Multicast Listener Discovery (MLD) 
v1/v2 snooping
•	 PIM to DVMRP gateway support
Fluent network for voice, 
video and data
•	 Session Initiation Protocol (SIP) 
detection, session monitoring  
and tracking
•	 Provides real-time conversation 
quality information contained in the 
SIP packets concerning packet loss, 
delay, jitter, MOS score, R-Factor in 
real time
•	 SIP profile for QOS, priority tuning 
for end-to-end processing
•	 Multicast DNS Relay: Bonjour protocol 
support for wired Airgroup 
Advanced Layer-2 services
•	 Ethernet services support using 
IEEE 802.1ad Provider Bridges (also 
known as Q-in-Q or VLAN stacking)
•	 Ethernet OAM (802.1ag): Connectivity 
Fault Management (L2 ping &  
Link trace)
•	 Ethernet in First mile: Link OAM 
(802.3ah)
•	 Fabric virtualization services IEEE 
802.1aq Shortest Path Bridging 
(SPB-M) and VxLAN
•	 In-band management for SPB-M
•	 Ethernet network-to-network 
interface (NNI) and user network 
interface (UNI)
•	 Service Access Point (SAP) profile 
identification
•	 Service VLAN (SVLAN) and Customer 
VLAN (CVLAN) support
•	 VLAN translation and mapping 
including CVLAN to SVLAN
•	 Port mapping
•	 DHCP Option 82: Configurable relay 
agent information
•	 Multiple VLAN Registration Protocol 
(MVRP)
•	 HA-VLAN for Layer 2 clusters  
such as MS-NLB and active-active 
Firewall clusters
•	 Jumbo frame support
•	 Bridge Protocol Data Unit (BPDU) 
blocking
•	 STP Root Guard
Data center networking
•	 IEEE 802.1aq Shortest Path bridging 
(SPB-M)
•	 RFC 7348 Virtual eXtensible Local 
Area Network (VxLAN)
Software Defined 
Networking (SDN)
•	 Programmable AOS RESTful API 
•	 Software-controlled VxLAN hardware 
VTEP gateway
Supported standards
IEEE standards
•	 IEEE 802.1D STP
•	 IEEE 802.1p CoS
•	 IEEE 802.1Q VLANs
•	 IEEE 802.1ab (LLDP)
•	 IEEE 802.1ag (OA&M)
•	 IEEE 802.1ad Provider Bridges 
Q-in-Q/VLAN stacking
•	 IEEE 802.1ak (Multiple VLAN 
Registration Protocol (MVRP)
•	 IEEE 802.1aq Shortest Path Bridging 
(SPB)
•	 IEEE 802.1s MSTP
•	 IEEE 802.3i 10BASE-T
•	 IEEE 802.1w RSTP
•	 IEEE 802.3x Flow Control
•	 IEEE 802.3z Gigabit Ethernet
•	 IEEE 802.3ab 1000Base-T
•	 IEEE 802.3ac VLAN Tagging
•	 IEEE 802.3ad/802.1AX Link 
Aggregation
•	 IEEE 802.3ae 10 GigE
•	 IEEE 802.3af Power over Ethernet
•	 IEEE 802.3at PoE Plus
•	 IEEE 802.3az Energy Efficient Ethernet 
(EEE)
•	 IEEE 802.3bz 2.5/5 GigE
•	 IEEE 802.3ba 40GBASE-X
•	 IEEE 802.1x-2004
•	 IEEE 802.1ae  MAC Security
•	 IEEE 1588-2008 (PTP)*
ITU-T recommendations
•	 ITU-T G.8032/Y.1344 2010: Ethernet 
Ring Protection (ERPv2)
•	 ITU-T Y.1731 OA&M fault and 
performance management
IETF RFCs
IPv4
•	 RFC 2003 IP/IP Tunneling
•	 RFC 2131 Dynamic Host 
Configuration Protocol (DHCPv4)
•	 RFC 2784 GRE Tunneling
•	 RFC 4022/2452 MIB for IPv4 TCP
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4113/2454 MIB for IPv4 UDP
•	 RFC 4292/4293 IPv4 MIBs

<<<PAGE 529>>>
9
Datasheet 
Alcatel-Lucent OmniSwitch 6870
OSPF
•	 RFC 1765 OSPF Database Overflow
•	 RFC 1850/2328 OSPF v2 and MIB
•	 RFC 2154 OSPF MD5 Signature
•	 RFC 2370/3630 OSPF Opaque LSA
•	 RFC 2740/5340 OSPFv3 for IPv6
•	 RFC 3101 OSPF NSSA Option
•	 RFC 3623/5187 OSPF Graceful 
Restart
•  RFC 5838 MIB for OSPFv3
•  RFC 4552 Authentication for OSPFv3
RIP	
•	 RFC 1058 RIP v1
•	 RFC 1722/1723/2453/1724 RIP v2 
and MIB
•	 RFC 1812/2644 IPv4 Router 
Requirements
•	 RFC 2080 RIPng for IPv6	
BGP
•	 RFC 1269/1657/4273 BGP v3 and v4 
MIB
•	 RFC 1403/1745 BGP/OSPF 
Interaction
•	 RFC 1771-1774/2842/2918/ 
3392/4271 BGP v4
•	 RFC 1965 BGP AS Confederations
•	 RFC 1966 BGP Route Reflection
•	 RFC 1997/1998/4360 BGP 
Communities Attribute
•	 RFC 2042/5396 BGP New Attribute
•	 RFC 2385 BGP MD5 Signature
•	 RFC 2439 BGP Route Flap Damping
•	 RFC 2545 BGP-4 Multiprotocol 
Extensions for IPv6 Routing
•	 RFC 2858/4760 Multiprotocol 
Extensions for BGP-4
•	 RFC 3065 BGP AS Confederations
•	 RFC 4456 BGP Route Reflection
•	 RFC 4486 Subcodes for BGP Cease 
Notification
•	 RFC 4724 Graceful Restart for BGP
•	 RFC 3392/5492/5668/6793 BGP 
4-Octet ASN
•	 RFC 5082 Generalized TTL Security 
Mechanism (GTSM)
IS-IS
•	 RFC 1142/1195/3719/3787/5308 IS-
IS v4
•	 RFC 2763/2966/3567/3373 
Adjacencies and route management
•	 RFC 5120 M-ISIS: Multi Topology IS-IS
•	 RFC 5306 Graceful Restart
•	 RFC 5309/draft-ietf-isis-igp-p2p-over-
lan Point to point over LAN
•	 RFC 6329 IS-IS Extensions 
Supporting IEEE 802.1aq SPB
•  RFC 5304 IS-IS Cryptographic 
Authentication
•  RFC 5310 IS-IS Generic Cryptographic 
Authentication	
IP Multicast
•	 RFC 1075/draft-ietf-idmr-
dvmrp-v3-11.txt DVMRP
•	 RFC 2362/4601/5059 PIM-SM
•	 RFC 2365 Multicast
•	 RFC 2710/3019/3810/MLD v2  
for IPv6
•	 RFC 2715 PIM and DVMRP 
interoperability
•	 RFC 2933 IGMP MIB
•	 RFC 3376 IGMPv3 (includes IGMP  
v2/v1)
•	 RFC 3569 Source-Specific Multicast 
(SSM)
•	 RFC 3973 Protocol Independent 
Multicast- Dense Mode (PIM-DM)
•	 RFC 4541 Considerations for IGMP 
and MLD Snooping Switches
•	 RFC 5015 BiDIR PIM
•	 RFC 5060 Protocol Independent 
Multicast MIB
•	 RFC 5132 Multicast Routing MIB
•	 RFC 5240 PIM Bootstrap Router MIB
IPv6
•	 RFC 1981 Path MTU Discovery
•	 RFC 2460 IPv6 Specification
•	 RFC 2461 NDP
•	 RFC 2464 IPv6 over Ethernet
•	 RFC 2465 MIB for IPv6: Textual 
Conventions (TC) and General Group
•	 RFC 2466 MIB for IPv6: ICMPv6 
Group
•	 RFC 2711 Router Alert Option
•	 RFC 3056 6to4 Tunnels
•	 RFC 3315 Dynamic Host 
Configuration Protocol for IPv6 
(DHCPv6)
•	 RFC 3484 Default Address Selection
•	 RFC 3493/2553 Basic Socket API
•	 RFC 3542/2292 Advanced  
Sockets API
•	 RFC 3587/2374 Global Unicast 
Address Format
•	 RFC 3595 TC for IPv6 Flow Label
•	 RFC 3596/1886 DNS for IPv6
•	 RFC 4007 Scoped Address
•	 RFC 4022/2452 MIB for IPv6 TCP
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4113/2454 MIB for IPv6 UDP
•	 RFC 4193 Unique Local Addresses
•	 RFC 4213/2893 Transition 
Mechanisms
•	 RFC 4291/3513/2373 Addressing 
Architecture (uni/any/multicast)
•	 RFC 4292/4293 IPv6 MIBs
•	 RFC 4301/2401 Security Architecture
•	 RFC 4302/2402 IP Authentication 
Header
•	 RFC 4303/2406 IP Encapsulating 
Security Payload (ESP)
•	 RFC 4308 Cryptographic Suites  
for IPSec
•	 RFC 4443/2463 ICMPv6
•	 RFC 4861/2461 Neighbor Discovery
•	 RFC 4862/2462 Stateless Address 
Auto-configuration
•	 RFC 5095 Deprecation of Type 0 
Routing Headers in IPv6
Manageability
•	 RFC 854/855 Telnet and Telnet 
options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1  
and SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP  
v2 MIB
•	 RFC 1215 Convention for  
SNMP Traps
•	 RFC 1573/2233/2863 Private  
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•	 RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from 
Forms: multipart/form-data
•	 RFC 2396 Uniform Resource 
Identifiers (URI): Generic Syntax
•	 RFC 2570-2576/3410-3415/3584 
SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3  
MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 3826 (AES) Cipher Algorithm 
in the SNMP User-based Security 
Model
* Supported on selected models

<<<PAGE 530>>>
10
Datasheet 
Alcatel-Lucent OmniSwitch 6870
•	 RFC 4122 A Universally Unique 
IDentifier (UUID) URN Namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4253  SSH Transport Layer 
Protocol
•	 RFC 4254  SSH Connection Protocol
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP  
Status Codes
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP)  
and crypto algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618  
RADIUS Authentication and  
Client MIB
•	 RFC 3576 Dynamic Authorization 
Extensions to RADIUS
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 3162 RADIUS and IPv6
•	 RFC 4301 Security Architecture for IP
•  RFC 5517 Private VLAN
QoS
•	 RFC 896 Congestion Control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246
•	 DiffServ
•	 RFC 2697 srTCM
•	 RFC 2698 trTCM
•	 RFC 3635 Pause Control
Others
•	 RFC 791/894/1024/1349 IP and IP/
Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•  RFC 2581 TCP Congestion Control
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy 
ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030/5905 NTP v4 and 
Simple NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 
DHCP
•	 RFC 1757/2819 RMON and MIB
•  RFC 4502 RMON MIB v2
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 2338/3768/2787 VRRP  
and MIB
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
•  IETF draft “IP/IPVPN services with 
IEEE 802.1aq SPB networks”
•  RFC 7348 Virtual extensible Local 
Area Network (VxLAN)
OmniSwitch 6870 specifications
Table 7. Power consumption, acoustics and weight
Switch module
Power  
consumption 
- idle (W)
Power  
consumption   
- full load (W)
Heat dissipation 
(BTU/h)
Acoustic 
(dB) 
MTBF
Weight (kg/lb)
Weight -  
fully populated 
(kg/lb)
OS6870-24
71
100.9
344
39.8
557,717 h
5.27 kg  
(11.61 lb)
6.84 kg  
(15.08 lb)
OS6870-48
73
105.2
359
39.8
533,368 h
5.49 kg  
(12.10 lb)
7.06 kg  
(15.57 lb)
OS6870-P24Z
90.2
173.6
592
41.6
414,986 h
6.94 kg  
(15.30 lb)
8.64 kg  
(19.05 lb)
OS6870-P48Z
92.4
215
734
40.1
374,799 h
7.26 kg  
(16.01 lb)
8.96 kg  
(19.75 lb)
OS6870-P24M
219.6
313.2
1069
48.2
386,437 h
7.43 kg  
(16.38 lb)
9.13 kg  
(20.13 lb)
OS6870-P48M
251.8
343.9
1173
46.9
349,827 h
7.44 kg  
(16.40 lb)
9.14 kg  
(20.15 lb)
OS6870-V12
73
157.8
538
41.1
507,909 h
5.37 kg  
(11.84 lb)
7.07 kg  
(15.59 lb)
 
The power consumption measured with redundant PSU on all models. OS6870-P24M, P48M and V12 models are equipped with OS6870-CNI-U2 module.
Heat dissipation is calculated for power consumption at full load. 1 watt ≈ 3.41214 BTU/h.
The acoustic level measured per ISO7779. The measurement is done with 1 PSU @ 50% PoE load.
MTBF is measured 25 °C ambient temperature with one AC power supply as per Telcordia SR-332 issue 4 standard.
Fully populated weight measured with redundant PSU on all models.

<<<PAGE 531>>>
11
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Table 8. OmniSwitch 6870 compliance and certifications
Compliance type
Certification
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart B (Class A)
•	 ICES–003:2012 Issue 5, Class A ANSI C63.4-2009
•	 VCCI (Class A, with UTP Cables)
•	 AS/NZS 3548 (Class A) – C-Tick CE marking for European countries (Class A, with UTP Cables)
•	 CE Emission
	
¬ EN 55032 (EMI & EMC)
	
¬ EN 55035
	
¬ EN 50581 (RoHS Recast)
	
¬ EN 61000-3-2
	
¬ EN 61000-3-3
	
¬ EN 61000-4-2
	
¬ EN 61000-4-3
	
¬ EN 61000-4-4
	
¬ EN 61000-4-5
	
¬ EN 61000-4-6
	
¬ EN 61000-4-8
	
¬ EN 61000-4-11
•	 IEEE 802.3: Hi-Pot Test (2250 V DC on all Ethernet ports)
Compliance type
Certification
Safety
•	 IEC 62368-1
•	 UL 60950-1, 2nd Edition
•	 IEC 60950-1/EN 60950-1, all national deviations
•	 UL 62368-1/IEC 62368-1
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 CDRH Laser
•	 CAN/CSA-22-2, 62368-1
•	 NOM-019 SCFI, Mexico
•	 CAN/CSA 62368-1
•	 AS/NZ TS-001 and 60950:2000, Australia
•	 UL-AR, Argentina
•	 AS/NZ 62368-1
•	 UL-GS Mark, Germany
•	 CCC, China
•	 ANATEL, Brazil
•	 BSMI, Taiwan
•	 KCC, Korea
•	 RoHS & WEEE directives compliant
•	 TEC, India
Ordering information
Part number
Description
OS6870-24-##
This is a bundle offer that includes one unit of OS6870-24 and one unit of OS6870-BP. Gigabit Ethernet 
L3 fixed configuration chassis in a 1U form factor with 24 RJ-45 10/100/1000 Base-T ports, two 40/100G 
QSFP28 VFL/stacking ports, four SFP28 (1G/10G/25G) ports, USB, RJ45 console and EMP. All RJ-45 and 
SFP28 ports support 256-bit MACsec.
The bundle includes one 250W AC power supply, country-specific power cord, user manuals access card, 
hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OS6870-24D
This is a bundle offer that includes one unit of OS6870-24 and one unit of OS6870-BP-D. Gigabit Ethernet 
L3 fixed configuration chassis in a 1U form factor with 24 RJ-45 10/100/1000 Base-T ports, two 40/100G 
QSFP28 VFL/stacking ports, four SFP28 (1G/10G/25G) ports, USB, RJ45 console and EMP. All RJ-45 and 
SFP28 ports support 256-bit MACsec.
The bundle includes one 250W DC power supply, user manuals access card, hardware for mounting in a 
19” rack and a RJ45 to DB9 console adapter.
OS6870-48-##
This is a bundle offer that includes one unit of OS6870-48 and one unit of OS6870-BP. Gigabit Ethernet 
L3 fixed configuration chassis in a 1U form factor with 48 RJ-45 10/100/1000 Base-T ports, two 40/100G 
QSFP28 VFL/stacking ports, four SFP28 (1G/10G/25G) ports, USB, RJ45 console and EMP. All RJ-45 and 
SFP28 ports support 256-bit MACsec.
The bundle includes one 250W AC power supply, country-specific power cord, user manuals access card, 
hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.

<<<PAGE 532>>>
12
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Part number
Description
OS6870-48D
This is a bundle offer that includes one unit of OS6870-48 and one unit of OS6870-BP-D. Gigabit Ethernet 
L3 fixed configuration chassis in a 1U form factor with 48 RJ-45 10/100/1000 Base-T ports, two 40/100G 
QSFP28 VFL/stacking ports, four SFP28 (1G/10G/25G) ports, USB, RJ45 console and EMP. All RJ-45 and 
SFP28 ports support 256-bit MACsec.
OS6870PH24Z-##
This is a bundle offer that includes one unit of OS6870-P24Z and one unit of OS6870-BPPH. Fixed-
configuration chassis in a 1U form factor with 24 10M/100M/1G/2.5G multi-gigabit 60W bt PoE ports, two 
40/100G QSFP28 VFL/stacking ports and six 1G/10G/25G SFP28 ports. All ports support 256-bit MACsec. 
Bundle includes one 600W AC power supply, country-specific power cord, user manuals access card, 
hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OS6870PX24Z-##
This is a bundle offer that includes one unit of OS6870-P24Z and one unit of OS6870-BPPX. Fixed-
configuration chassis in a 1U form factor with 24 10M/100M/1G/2.5G multi-gigabit 60W bt PoE ports, two 
40/100G QSFP28 VFL/stacking ports and six 1G/10G/25G SFP28 ports. All ports support 256-bit MACsec. 
Bundle includes one 1200W AC power supply, country-specific power cord, user manuals access card, 
hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter. 
OS6870PH48Z-##
This is a bundle offer that includes one unit of OS6870-P48Z and one unit of OS6870-BPPH. Fixed-
configuration chassis in a 1U form factor with 48 10M/100M/1G/2.5G multi-gigabit 60W bt PoE ports, two 
40/100G QSFP28 VFL/stacking ports and six 1G/10G/25G SFP28 ports. All ports support 256-bit MACsec. 
Bundle includes one 600W AC power supply, country-specific power cord, user manuals access card, 
hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.  
OS6870PX48Z-##
This is a bundle offer that includes one unit of OS6870-P48Z and one unit of OS6870-BPPX. Fixed-
configuration chassis in a 1U form factor with 48 10M/100M/1G/2.5G multi-gigabit 60W bt PoE ports, two 
40/100G QSFP28 VFL/stacking ports and six 1G/10G/25G SFP28 ports. All ports support 256-bit MACsec. 
Bundle includes one 1200W AC power supply, country-specific power cord, user manuals access card, 
hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter. 
OS6870-V12-##
This is a bundle offer that includes one unit of OS6870-V12 and one unit of OS6870-BPH. Fixed-
configuration chassis in a 1U form factor with 12 1G/10G/25G SFP28 ports, two 100/200G QSFP56 VFL/
stacking ports and one uplink module expansion slot. All ports support 256-bit MACsec.
The bundle includes one system 550W AC power supply, country-specific power cord, user manuals 
access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter. Uplink module 
needs to be ordered separately. 
OS6870-V12D
This is a bundle offer that includes one unit of OS6870-V12 and one unit of OS6870-BP-D. Fixed-
configuration chassis in a 1U form factor with 12 1G/10G/25G SFP28 ports, two 100/200G QSFP56 VFL/
stacking ports and one uplink module expansion slot. All ports support 256-bit MACsec.
The bundle includes one system 250W DC power supply, user manuals access card, hardware for 
mounting in a 19” rack and a RJ45 to DB9 console adapter. Uplink module needs to be ordered separately. 
OS6870PH24M-##
This is a bundle offer that includes one unit of OS6870-P24M and one unit of OS6870-BPPH Fixed-
configuration chassis in a 1U form factor with 24 10M/100M/1G/2.5G/5G/10G multigigabit 95W bt 
PoE ports, two 100G/200G QSFP56 VFL/stacking ports and one uplink module expansion slot. All ports 
support 256-bit MACsec. The bundle includes one 600W AC power supply, country-specific power cord, 
user manuals access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OS6870PX24M-##
This is a bundle offer that includes one unit of OS6870-P24M and one unit of OS6870-BPPX. Fixed-
configuration chassis in a 1U form factor with 24 10M/100M/1G/2.5G/5G/10G multigigabit 95W bt 
PoE ports, two 100G/200G QSFP56 VFL/stacking ports and one uplink module expansion slot. All ports 
support 256-bit MACsec. The bundle includes one 1200W AC power supply, country-specific power cord, 
user manuals access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OS6870PXL24M-##
This is a bundle offer that includes one unit of OS6870-P24M and one unit of OS6870-BPXL. Fixed-
configuration chassis in a 1U form factor with 24 10M/100M/1G/2.5G/5G/10G multigigabit 95W bt 
PoE ports, two 100G/200G QSFP56 VFL/stacking ports and one uplink module expansion slot. All ports 
support 256-bit MACsec. The bundle includes one 2000W AC power supply, country-specific power cord, 
user manuals access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OS6870PH48M-##
This is a bundle offer that includes one unit of OS6870-P24M and one unit of OS6870-BPPH Fixed-
configuration chassis in a 1U form factor with 48 10M/100M/1G/2.5G/5G multigigabit 95W bt PoE ports, 
two 100G/200G QSFP56 VFL/stacking ports and one uplink module expansion slot. All ports support 256-
bit MACsec. The bundle includes one 600W AC power supply, country-specific power cord, user manuals 
access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OS6870PX48M-##
This is a bundle offer that includes one unit of OS6870-P48M and one unit of OS6870-BPPX. Fixed-
configuration chassis in a 1U form factor with 48 10M/100M/1G/2.5G/5G multigigabit 95W bt PoE ports, 
two 100G/200G QSFP56 VFL/stacking ports and one uplink module expansion slot. All ports support 256-
bit MACsec. The bundle includes one 1200W AC power supply, country-specific power cord, user manuals 
access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.

<<<PAGE 533>>>
13
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Part number
Description
OS6870PXL48M-##
This is a bundle offer that includes one unit of OS6870-P48M and one unit of OS6870-BPXL. Fixed-
configuration chassis in a 1U form factor with 48 10M/100M/1G/2.5G/5G multigigabit 95W bt PoE ports, 
two 100G/200G QSFP56 VFL/stacking ports and one uplink module expansion slot. All ports support 256-
bit MACsec. The bundle includes one 2000W AC power supply, country-specific power cord, user manuals 
access card, hardware for mounting in a 19” rack and a RJ45 to DB9 console adapter.
OmniSwitch 6870N uplink modules 
OS6870-LNI-U6
OS6870-LNI-U6: One uplink module for OS6870-P24M / OS6870-P48M / OS6870-V12 switch with six 
10G/25G/50G SFP56 ports. All ports support 256-bit MACsec.
Purchase OS6870-SW-PERF license separately to enable 50G speed.
OS6870-CNI-U2
OS6870-CNI-U2: One uplink module for OS6870-P24M / OS6870-P48M / OS6870-V12 switch with 2 x 
40G/100G QSFP28 ports. All ports support 256-bit MACsec.
OmniSwitch 6870N power supplies 
OS6870-BPPH-##
OS6870-BPPH modular 600W AC PoE backup power supply. Provides system and PoE backup power to 
one OS6870 PoE switch
OS6870-BPPX-##
OS6870-BPPX modular 1200W AC PoE backup power supply. Provides system and PoE backup power to 
one OS6870 PoE switch 
OS6870-BPXL-##
OS6870-BPXL modular 2000W AC PoE power supply. Provides system and PoE power to one OS6870-
P48M or OS6870-P24M switch
OS6870-BPH-##
OS6870-BPH modular 550W AC system power supply. Provides system power to one OS6870-V12 switch.
OS6870-BP-D
OS6870-BPD modular 250W DC system power supply. Provides system power to one OS6870-24, 
OS6870-48 or OS6870-V12.
OS6870-BP-##
OS6870-BP modular 250W AC power supply. Provides system power to OS6870-24 or OS6870-48 
switches
OmniSwitch 6870 software
OS-SW-MACSEC
Site license to enable MACsec on OS6870 models. One license per customer at no cost.
OS6870-SW-PERF
Performance software license enables the OS6870-LNI-U6 ports to operate at 50G speed.
OmniSwitch 6870 accessories 
OS6-REAR-MNT2
Mounting brackets to stabilize the rear of OS6870 and OS6860N in a 19 rack.
1G transceivers
SFP-GIG-T
1000Base-T Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and full-duplex mode
SFP-GIG-SX
1000Base-SX Gigabit Ethernet optical transceiver (SFP MSA)
SFP-GIG-LX
1000Base-LX Gigabit Ethernet optical transceiver (SFP MSA)
SFP-GIG-LH40
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on  
9/125 µm SMF
SFP-GIG-LH70
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on  
9/125 µm SMF
SFP-DUAL-MM-N
Dual Speed 100Base-FX or 1000Base-X Ethernet optical transceiver (SFP MSA). Supports multimode fiber 
over 1310nm wavelength (nominal) with an LC connector. Typical reach of  
550m at Gigabit speed and 2km at 100 Mb/t speed
SFP-GIG-EXTND
Extended 1000Base-SX Gigabit Ethernet optical transceiver(SFP MSA). Multimode fiber over 850nm 
wavelength (nominal) LC connector. Reach of up to 2 km on 62.5/125 m MMF and  
50/125 m MMF.
SFP-GIG-BX-D
1000Base-BX SFP bi-directional transceiver with an LC interface. Works on single mode fiber optic on a 
single strand link up to 10 km. Transmits 1490 nm and receives 1310 nm optical signal.
SFP-GIG-BX-U
1000Base-BX SFP bi-directional transceiver with an LC interface. Works on single mode fiber optic on a 
single strand link up to 10 km. Transmits 1310 nm and receives 1490 nm optical signal.
SFP-GIG-BX-D%%
1000Base-BX SFP bi-directional transceiver with an LC interface. Works on single mode fiber optic on a 
single strand link. %% denotes length in KM. Available lengths are 20 & 40 Km. Transmits 1490 nm and 
receives 1310 nm optical signal.
SFP-GIG-BX-U%%
1000Base-BX SFP bi-directional transceiver with an LC interface. Works on single mode fiber optic on a 
single strand link. %% denotes length in KM. Available lengths 20 & 40 Km.. Transmits  
1310 nm and receives 1490 nm optical signal.

<<<PAGE 534>>>
14
Datasheet 
Alcatel-Lucent OmniSwitch 6870
Part number
Description
10G transceivers
SFP-10G-SR
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 850 nm wavelength (nominal) with 
an LC connector. Typical reach of 300 m
SFP-10G-LR
10 Gigabit optical transceiver (SFP+). Supports monomode fiber over 1310 nm wavelength (nominal) with 
an LC connector. Typical reach of 10 km
SFP-10G-ER
10 Gigabit optical transceiver (SFP+). Supports monomode fiber over 1550 nm wavelength (nominal) with 
an LC connector. Typical reach of 40 km
SFP-10G-ZR
10 Gigabit optical transceiver (SFP+). Supports data transmission at 1550 nm over up to 80km single 
mode fiber. LC connector type.
SFP-10G-LRM
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 1310 nm wavelength (nominal) with 
an LC connector. Typical reach of 220 m on FDDI-grade (62.5 µm)
SFP-10G-GIG-SR
Dual-speed SFP+ optical transceiver. Supports multimode fiber over 850 nm wavelength (nominal) with an 
LC connector. Supports 1000Base-SX and 10GBase-SR
SFP-10G-GIG-LR
Dual-speed SFP+ optical transceiver. Supports monomode fiber over 1310 nm wavelength (nominal) with 
an LC connector. Typical reach of 10 Km. Supports 1000BASE-LX and 10GBASE-LR
SFP-10G-T
10 Gigabit copper transceiver (SFP+). 10GBase-T 10 Gigabit ethernet Transceiver (SFP MSA) - Supports 
category 6a/7 cabling copper cabling up to 30m. This transceiver supports 10Gbs full-duplex mode only.
SFP+ Direct attached cables
SFP-10G-C1M
10 Gigabit direct attached copper cable (1 m, SFP+)
SFP-10G-C3M
10 Gigabit direct attached copper cable (3 m, SFP+)
SFP-10G-C7M
10 Gigabit direct attached copper cable (7 m, SFP+)
25G transceivers
SFP-25G-SR
25 Gigabit optical transceiver (SFP28). Supports link lengths of 70m on OM3 and 100m on 
OM4 multimode fiber cables. LC connector type.
SFP-25G-ESR
25 Gigabit optical transceiver (SFP28). Supports multimode fiber over 850nm wavelength nominal with an 
LC connector. Typical reach of 300m on OM4 MMF
SFP-25G-CLR
25 Gigabit optical transceiver (SFP28). Supports link lengths of 2Km over singlemode fiber cables.  
LC connector type.
SFP-25G-LR
25 Gigabit optical transceiver (SFP28). Supports link lengths of 10Km over singlemode fiber cables.  
LC connector type.
25G SFP28 direct attached cables
SFP-25G-A20M
25 Gigabit SFP28 direct attached active optical cable. 20 m.
SFP-25G-C1M
25 Gigabit direct attached copper cable 1m, SFP28)
SFP-25G-C3M
25 Gigabit direct attached copper cable 3m, SFP28)
SFP-25G-C5M
25 Gigabit direct attached copper cable 7m, SFP28)
40G transceivers
QSFP-40G-SR
Four channel 40 Gigabit optical transceiver QSFP+). Supports link lengths of 100m and 150m respectively 
on OM3 and OM4 multimode fiber cables. Single MPO receptacle
QSFP-40G-LR
Four channel 40 Gigabit optical transceiver QSFP+). Supports single mode fiber over 1310nm wavelength. 
Typical reach 10 km. Duplex LC receptacles
QSFP-40G-SR-BD
Dual channel 40 Gigabit optical transceiver QSFP+). Supports multimode fiber over 850nm wavelength 
nominal) with duplex LC connector. Supports link lengths up to 100 meters on  
OM3 MMF or 150 meters on OM4 MMF
QSFP-4X10G-SR
40 Gigabit to 4 x 10 Gigabit Multifiber Push-On (MPO) fiber splitter transceiver
40G QSFP+ direct attached cables
QSFP-40G-AOC20M
40 Gigabit QSFP+ direct attached active optical cable. 20 m.
QSFP-40G-C1M
40 Gigabit direct attached copper cable 1m, QSFP+
QSFP-40G-C3M
40 Gigabit direct attached copper cable 3m, QSFP+
QSFP-40G-C40CM
40 Gigabit direct attached copper cable 40 cm, QSFP+

<<<PAGE 535>>>
© 2025 ALE International, ALE USA Inc. All rights reserved in all countries. The Alcatel-Lucent name and logo are 
trademarks of Nokia used under license by ALE. To view a list of proprietary ALE trademarks, visit: www.al-enterprise.com/
en/legal/trademarks-copyright. MPR24040101EN (April 2025)
Part number
Description
QSFP-40G-C7M
40 Gigabit direct attached copper cable 7m, QSFP+
50G transceivers
SFP-50G-SR
50 Gigabit optical transceiver (SFP56). Supports link lengths of 100M on OM4 MMF. Duplex LC LC 
connector
SFP-50G-FR
50 Gigabit optical transceiver (SFP56). Supports link lengths of 2Km over singlemode cables. LC 
connector.
SFP-50G-LR
50 Gigabit optical transceiver (SFP56). Supports link lengths of 10Km over singlemode cables. Comply 
with SFF-8432 with duplex LC connector.
50G direct attached cables
SFP-50G-C50CM
50 Gigabit direct attached cable, (SFP56, 50cm)
SFP-50G-C1M
50 Gigabit direct attached cable, (SFP56, 1m)
SFP-50G-C3M
50 Gigabit direct attached cable, (SFP56, 3m)
100G transceivers
QSFP-100G-SR4
100 Gigabit optical transceiver QSFP28. Supports link lengths of 70m on OM3 and 100m  
on OM4 multimode fiber cables. LC connector type.  
QSFP-100G-CLR4
100 Gigabit optical transceiver QSFP28. Supports link lengths of 2Km over singlemode fiber cables. LC 
connector type.  
QSFP-100G-LR4
100 Gigabit optical transceiver QSFP28. Supports link lengths of 10Km over singlemode fiber cables. LC 
connector type.
QSFP-100G-CWDM4
100 Gigabit optical transceiver QSFP28. Supports link lengths of 2Km over singlemode fiber cables. LC 
connector type.. CWDM4
100G direct attach cables
QSFP-100G-A20M
100 Gigabit QSFP28 direct attached active optical cable. 20 m.
QSFP-100G-C1M
100 Gigabit direct attached copper cable 1m, QSFP28
QSFP-100G-C3M
100 Gigabit direct attached copper cable 3m, QSFP28
QSFP-100G-C5M
100 Gigabit direct attached copper cable 5m, QSFP28
200G transceivers
QSFP-200G-SR4
200 Gigabit optical transceiver (QSFP56). Supports link length of 70m on OM3 MMF, 100m on OM4 MMF. 
MPO-12 connector
QSFP-200G-FR4
200 Gigabit optical transceiver (QSFP56). Supports link length 1 for 2km FR4; 2 for 500m FR4 Lite. Duplex 
LC receptacles
200G direct attached cables
QSFP-200G-A20M
200 Gigabit direct attached active optical cable. (QSFP56, 20m)
QSFP-200G-C50CM
200 Gigabit direct attached cable, (QSFP56, 50cm)
QSFP-200G-C1M
200 Gigabit direct attached cable, (QSFP56, 1m)
QSFP-200G-C3M
200 Gigabit direct attached cable, (QSFP56, 3m)
Please replace the “##” in the part number with the country-specific power cord (for example, OS6870-P24M-US will come with a power cord for the USA). 11 different 
power cord options are available. Please consult the price list for all power cord options offered.
Warranty 
The OmniSwitch 6870 family comes with a Hardware Limited Lifetime Warranty.
Services and support
For more information about our Professional services, Support services, and Managed services, please go 
to https://www.al-enterprise.com/en/services.
Please visit our website to learn more.
https://www.al-enterprise.com/en/products/switches/omniswitch-6870

<<<PAGE 536>>>
Datasheet 
Alcatel-Lucent OmniSwitch 6865
Alcatel-Lucent  
OmniSwitch 6865 
Hardened Ethernet switches
The Alcatel-Lucent OmniSwitch 6865® is a family of 
ruggedized, advanced Layer 3, scalable Ethernet 
switches, designed to operate reliably in the harshest 
industrial environments and severe temperatures. 
OS6865 switches are rugged, high bandwidth switches that 
are ideal for industrial and mission-critical applications  
that require wider operating temperature ranges, stringent 
EMC/EMI requirements and an optimized feature set 
for high security, reliability, performance and easy 
management. These switches run on the widely deployed 
and field-proven Alcatel- Lucent Operating system 
offering SPB-M based VPNs and other advanced routing 
and switching capabilities.
The OS6865 series offers a unique mix of features to cater 
to the Hardened Ethernet applications such as IEEE 1588v2 
PTP capabilities for timing requirements of industrial IoT 
devices, 75W IEEE 802.3bt PoE for those power hungry 
devices on the access network, Fast PoE / Perpetual PoE 
for seamless connectivity of the IIoT PoE devices. SPB-M 
for fast, cost-efficient roll-out of VPN services on the edge 
and a comprehensive suite of security features to secure 
the network edge. These switches are easy to deploy with 
OS6865-P16X 
OS6865-U28X 
OS6865-U12X 
Alcatel Lucent’s award winning Intelligent-Fabric technology which offers out-of-the-box plug-and-play, Zero-
touch provisioning and network automation. The OS6865 family offers advanced system and network level 
resiliency features and convergence through standardized protocols.
These versatile industrial switches are ideal for deployment in transportation and traffic control systems, power 
utilities, video surveillance systems and outdoor installations.

<<<PAGE 537>>>
2
Datasheet  
Alcatel-Lucent OmniSwitch 6865
Features
Benefits 
•	 Resilient ruggedized hardware design
•	 Operates at a wider temperature range from -40° C to +74° C, withstands greater 
shock, vibrations, temperature and EMI/EMC variance 
•	 Convection cooled fan-less models
•	 Fan-less operations increases resiliency and maximizes uptime for converged 
mission-critical networks
•	 Advanced Industrial PoE capabilities with 
support for 75W IEEE 802.3bt PoE and Fast PoE / 
Perpetual PoE
•	 Enables converged deployments and is ideal for all type of PoE application 
requirements from outdoor wireless APs, to PTZ surveillance cameras and  
video displays
•	 Fast PoE allows the PoE power to be supplied to the connected devices within a 
matter of seconds, as soon as the switch is powered up. Perpetual PoE maintains 
the power to connected PoE devices when a switch is rebooted
•	 IEEE 1588v2 PTP support
•	 Provides precise sub-microsecond time synchronization for slave devices  
•	 SPB-M Support for Scalable network virtualization 
architecture over standard Ethernet fabric
•	 Optimizes/simplifies Layer 2 and Layer 3 network designs and reduces 
administration overhead
•	 Virtual Chassis technology, to connect multiple 
switches to create a single chassis-like entity
•	 Increases system redundancy, resiliency and high availability while simplifying 
deployment, operations and management of the network
•	 Auto-fabric technology to simplify installation and 
service provisioning
•	 Enables Zero-touch provisioning and network automation with automatic protocol 
and topology discovery
•	 Prevent human mistakes by automating standardized and replicable configurations
•	 Built in resiliency and redundancy
•	 Hot-swappable, fully redundant power supplies
•	 Delivers redundant ring topologies using industry 
standard protocols
•	 Field upgradable, highly redundant network solution maximizes network uptime
•	 SDN Ready
¬  OpenFlow and OpenStack support
¬  Supports RESTful APIs commands and MIBs
¬  Embedded scripting capabilities
•	 The support of SDN allows creation of specialized services which ensures that your 
investment is ready for the future and enables interoperability with third-party 
solutions
•	 REST APIs provides access to all AOS CLI and with advanced embedded  
scripting capabilities using Python and Bash, it enables fast deployment of  
new network services and be able to continuously adopt new applications to 
support the business
Alcatel-Lucent OmniSwitch 6865 models
The OmniSwitch 6865 offers customers Gigabit fixed-configuration switches with up to 75 watts of PoE per port 
and power supply options that accommodate the most demanding requirements. The switches can be mounted on 
wall/panel or a 19-inch rack. All the models have built-in 10 Gigabit SFP+ ports that support 10 Gigabits and 1000-X, 
a USB port and a console port. 
All the models of OS6865 family support 4 ports of 75W PoE. OS6865-U28X model also provides dedicated 20G 
Virtual chassis ports. OS6865 switches offer a surge protection of 6KV on all copper ports.
OmniSwitch 6865 switches can form a Virtual Chassis between any models creating a single chassis-like entity 
using 10G SFP+ ports. Up to 8 switches can be connected in a Virtual Chassis configuration OS6865-U28X also has 
dedicated QSFP+ Virtual Chassis ports in rear.
Gigabit ports 
(RJ45)
SFP 
ports
1G/10G 
SFP+ ports
75W /30W PoE 
ports
Description
OS6865-P16X
12
2
2
4/8
Fixed-configuration hardened fan-less half-rack width 2RU 
chassis with twelve 10/100/1000 Base-T PoE+ ports, four of 
which can support 75W PoE, two 1000 Base-X SFP ports and 
two fixed SFP+ (1G/10G) ports
OS6865-U12X
4
6
2
4/-
Fixed-configuration hardened fan-less half-rack width 2RU 
chassis with four 100/1000 Base-X SFP, two 1000 Base-X SFP, 
two fixed SFP+ (1G/10G)  ports and four 10/100/1000 Base-T 
75W PoE ports.
OS6865-U28X
4
20
4
4/-
Fixed-configuration hardened fan-less full-rack width 1RU 
chassis with twenty 100/1000 Base-X SFP, four  fixed SFP+ 
(1G/10G)  ports, four 10/100/1000 Base-T 75W PoE ports and 
two 20G VFL QSFP+ ports.

<<<PAGE 538>>>
3
Datasheet  
Alcatel-Lucent OmniSwitch 6865
Technical specifications
OmniSwitch 6865 models
Product matrix
OS6865-P16X
OS6865-U12X
OS6865-U28X
Operating temperature*
-40° C to 74° C 
(-40° F to 165° F)
-40° C to 74° C
(-40° F to 165° F)
-40° C to 74° C
(-40° F to 165° F)
Fans
0
0
0
File system flash
2 GB
2 GB
2 GB
RAM
2 GB
2 GB
2 GB
Altitude
13,000 ft
13,000 ft
13,000 ft
Storage temperature
-40° C to 85° C 
(-40° F to 185° F)
-40° C to 85° C 
(-40° F to 185° F)
-40° C to 85° C
(-40° F to 185° F)
Humidity (operating & storage)
5% to 95% non-condensing
5% to 95% non-condensing
5% to 95% non-condensing
USB port
1
1
1
Console port
1
1
1
Max raw fabric capacity
224 Gb/s
224 Gb/s
224 Gb/s
Switching capacity
68 Gb/s
60 Gb/s
208 Gb/s
Forwarding capacity
50.6 Mpps
44.6 Mpps
154.8 Mpps
Weight (no PS attached)
5.07 kg (11.18 lb)
5.17 Kg (11.40lb)
6.28 Kg (13.85 lbs)
Height
8.81 cm (3.47 in)
8.81 cm (3.47 in)
4.39cm (1.73 in)
Width
21.56 cm (8.49 in)
21.56 cm (8.49 in)
43.99 cm (17.32 in)
Depth (no PS attached)
26 cm (10.24 in)
26 cm (10.24 in)
27 cm (10.63 in)
1588v2 Capable Ports
16
12
28
20G QSFP+ VFL ports
0
0
2
Maximum PoE Budget**
300 W
300 W
280 W
Installation Options
DIN/wall/panel, 19” rack
DIN/wall/panel, 19” rack
19” rack
Power Consumption (idle)***
30 W
29 W
49.6 W
Power Consumption (full load)***
45 W
35.9 W
75.9 W
Heat Dissipation (BTU/hr)***
102.3
98.9 
170.6
Maximum surge protection on 
ports****
6 KV
6 KV
6 KV
MTBF (with 1 AC power supply)
767,181 h
827, 848 h
709,199 h 
MTBF (with 2 AC power supply)
1,044,414 h
1,141,692 h
952,763 h
* With airflow. In a sealed enclosure, without airflow, -40° C to +65 ° C
** With 2 x AC or 2 x DC (48 V input) power supplies operating at -40° C to 60° C. Please refer to HW user’s guide for more information on PoE budget. 
*** Power consumption measured at 120 VAC input. Full L2 traffic load measurement does not include PoE power consumption. Heat dissipation measured at idle:  
1 watt ≈ 3.41214 BTU/h
**** On copper ports 
Power supplies
OmniSwitch 6865 supports 1+1 redundant, hot-swappable fan-less power supplies. It also supports power 
load-sharing between the primary and backup power supplies to provide extended PoE budgets. There is no 
interruption of service when a new power supply is installed or an existing one replaced. The power supplies 
can be installed directly at the back of the switch or can be connected with a cable (included) and mounted 
independently using a Power tray. In a redundant configuration, power supplies can be installed in any manner

<<<PAGE 539>>>
4
Datasheet  
Alcatel-Lucent OmniSwitch 6865
AC+AC, AC+DC or DC+DC.
PS models
OS6865-BP
OS6865-BP-D
Description
Modular AC power supply. Provides up to 180 W of 
system & PoE power to one OS6865 switch
Modular DC power supply. Provides up to 180 W (48 
V input)/140 W (24 V input) of system and PoE power 
to one OS6865 switch
Dimensions (H x W x L)
5.1 cm x 9.5 cm x 18.1 cm 
(2 in x 3.74 in x 7.12 in)
5.1 cm x 9.5 cm x 18.1 cm 
(2 in x 3.74 in x 7.12 in)
Weight
1.42 Kg (3.14 lbs)
1.42 Kg (3.14 lbs)
Input voltage
100 VAC to 240 VAC
-20 VDC to -72 VDC
Input current
3A/100 V to 127 VAC 
1.5A/200 V to 240 VAC
12A/-20 V to -28 VDC 
6A/-36 V to -72 VDC
Max output power/current
180 W/3.22A
180 W/3.22A @ -36 to -72 VDC Input 
140 W/2.5 A @ -20 to -28 VDC Input
Surge protection
4 KV (Surge level 4)
4 KV (Surge level 4)
Fans
0
0
Product specifications 
and measurements
Per-port LEDs
•	 Non-PoE ports - green: link/activity
•	 PoE ports - amber: link/activity
System LEDs
•	 OK: green/amber operational status of 
the switch
•	 VC: green/amber master or slave role 
in VC configuration. Number of blinks 
between each solid color state indicates 
chassis-id
•	 PS1: Green/Amber - status for the 
primary power supply
•	 PS2: Green/Amber - status for the 
backup power supply
Scalability numbers and 
speeds
•	 Wire rate at layer 2 and layer 3 on all 
ports
•	 Virtual Fabric Link (VFL) ports raw 
capacity: 42 Gb/s or 84 Gb/s aggregate
•	 Jumbo frame size: 9 216 bytes (for 1/10 
Gb/s)
•	 Total number of MAC addresses: 48,000
•	 Total number of IPv4 routes: 64,000
•	 Number of VLANs: 4,000
Virtual chassis
•	 Number of units in a VC: 8 
•	 DAC cables for VC connection: 40 cm, 1 
m, 3 m
Compliance and 
certifications
Commercial safety
•	 IEC 62368-1
•	 UL 60950-1, 2nd Ed.
•	 IEC 60950-1; all national deviations and 
amendments
•	 EN 60950-1; all deviations
•  CAN/CSA-C22.2 No. 60950-1-03
•	 NOM-019 SCFI, Mexico
•	 AS/NZ TS-001 and 60950:2000, Australia
•	 UL-AR, Argentina
•	 UL-GS Mark, Germany
•	 CU, EAC, Russia
•	 ANATEL, Brazil
•	 CCC, China
•	 KCC Korea
•	 BSMI, Taiwan
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 CDRH Laser
•	 RoHS & WEEE directives compliant
Commercial EMI/EMC
•	 47 CRF FCC Part 15: 2015 Subpart B 
(Class A) VCCI (Class A, with UTP Cables)
•	 ICES–003:2012 Issue 5, Class A
•	 AS/NZS 3548 (Class A) – C-Tick
•	 CE marking for European countries 
(Class A)
•	 CE Emission
¬	 EN50581 (RoHS Recast)
¬	 EN 55022 (EMI & EMC requirement)
¬	 EN 55024/EN 55035 (Immunity 
Characteristics)
¬	 EN 61000-3-2 (Harmonic Current 
emissions)
¬	 EN 61000-3-3
¬	 EN 61000-4-2
¬	 EN 61000-4-3
¬	 EN 61000-4-4
¬	 EN 61000-4-5 (Surge Immunity, Class 4)
¬	 EN 61000-4-6
¬	 EN 61000-4-8
¬	 EN 61000-4-11
IEEE802.3: Hi-pot Test  
(2.25 KV DC on all Ethernet Ports)
Industrial
Industrial Environmental
•	 IEC 60870-2-2 (operational temperature)
•	 IEC 60068-2-1 (temperature type test – 
cold)
•	 IEC 60068-2-2 (temperature type test – 
hot)
•  IEC 60721-3-1: Class 1K5 (storage 
temperature)
•  IEC 60068-2-30: 5% to 95% non-
condensing humidity
•	 IEC 60255-21-2 (mechanical shock)
•	 IEC 60255-21-1 (vibration)
Industrial safety
•	 UL 508
•	 UL 61010
•	 EN 50021
•	 Hazardous Location 
¬	 ISA 12.12.01/UL 1604 
¬	 CSA22.2/213
•	 IP30
Industrial emission 
•	 EN 61805-3
•	 EN 55032 (Emission Standard)
•  EN 61000-3-2
•  EN 61000-3-3
•	 EN 55024 (Immunity Standard)
•	 EN 61000-4-2 to EN 61000-4-8
•	 EN 61000-4-11
•	 EN 61000-4-12
•	 EN 61000-4-16
•	 EN 61000-4-17
•	 EN 61000-4-29

<<<PAGE 540>>>
5
Datasheet  
Alcatel-Lucent OmniSwitch 6865
•	 IEC 60255-5
•	 IEEE 1613
Industry specific electric power 
substation 
•	 IEEE 1613, Section 4 to 8
•	 IEC 61850-3
Railway applications 
•	 EN 50121-4
•   EN 50155:2017
•   EN 61373
•	 EN 62236-4
•	 EN 61000-6-4
Intelligent Transportation (Road) 
•	 NEMA TS-2
Marine certifications 
•	 DNVGL-CG-0339†
• IEC 60945:2002†
† Requires mandatory DNV kit for compliance 
Federal certifications
•	 FIPS 140-2
•	 Common Criteria EAL2
•	 Common Criteria NDcPP
•	 JITC
•	 Trade Agreements Act (TAA)
Military
•	 MIL-STD-810F
•	 MIL-STD-461
Detailed product features
Simplified manageability and 
configuration
•	 Zero-touch provisioning and network 
automation. Out-of-the box plug-
and-play Auto-Fabric for automated 
discovery of configuration server, 
topology & protocols and automated 
switch configuration. Works with any 
non-Alcatel-Lucent device that supports 
Shortest Path Bridging-MAC, SPBM), 
802.1ak (MVRP), 802.3ad/802.1AX (Link 
Aggregation Control Protocol, LACP)
•	 Intuitive CLI in a scriptable Python & 
BASH environment via console, Telnet or 
Secure Shell (SSH) v2 over IPv4/IPv6
•	 Powerful WebView Graphical Web 
Interface via HTTP and HTTPS over IPv4/
IPv6
•	 Network Automation and 
Programmability Abstraction Layer with 
Multivendor (NAPALM) support
•	 Fully programmable RESTful web 
services interface with XML and JSON 
support. API enables access to CLI and 
individual mib objects
•	 Supported by ProActive Lifecycle 
Manager (PALM) which quickly and 
easily generates an inventory list of 
Alcatel-Lucent Enterprise Wi-Fi and 
LAN switching products on your 
network, provides status in terms of 
software lifecycle, hardware lifecycle, 
warranty, and support status. Current 
maintenance release, recommended 
replacement for EOL products, and 
latest release notes are available as well 
through an easy-to–use web interface
•	 Integrated with Alcatel-Lucent 
OmniVista® products for network 
management
•	 Full configuration and reporting using 
SNMPv1/2/3 to facilitate third-party 
network management over IPv4/IPv6
•	 Integrated with Nokia Network Services 
Platform (NSP)® application for network 
management.
•	 File upload using USB, TFTP, FTP, SFTP or 
SCP using IPv4/IPv6
•	 Human-readable ASCII-based 
configuration files for off-line editing, 
bulk configuration and out-of-the-box 
auto-provisioning
•	 Fully programmable OpenFlow 1.3.1 and 
1.0 agent for control of native OpenFlow 
and hybrid ports
•	 Non-volatile memory for start-up 
configuration
•	 Multiple microcode image support with 
fallback recovery
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discover 
Protocol (LLDP) with Media Endpoint 
Discover (MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server managed 
by Nokia VitalQIP® DNS/DHCP IP 
Address Management
•	 Dynamic PoE allocation delivers only 
the power needed up to the total 
power budget for most efficient power 
consumption
•	 Access to AOS console via USB Adapter 
with Bluetooth techology provides 
wireless managment access, eliminating 
the need of console cables
•	 Configurable per-port PoE priority, max 
power and time-of-day policy for PoE 
power allocation
Monitoring and 
troubleshooting
•	 Local (on the flash) and remote server 
logging (Syslog): event  
and command logging
•	 IP tools: ping and trace route
•	 Dying Gasp support via SNMP  
and syslog messages
•	 Loopback IP address support for 
management per service
•	 Management virtual routing and 
forwarding (VRF) support
•	 Policy- and port-based mirroring
•	 Remote port mirroring
•	 sFlow v5 and Remote Monitoring 
(RMON)
•	 Unidirectional Link Detection (UDLD), 
Digital Diagnostic Monitoring (DDM), and 
Time Domain Reflectometry (TDR)
Resiliency and high 
availability
•	 Unified management, control and virtual 
chassis technology
•	 Virtual Chassis 1+N redundant 
supervisor manager
•	 Virtual Chassis In-Service Software 
Upgrade (ISSU)
•	 Remote Virtual Chassis - Up to  
10-km fault-tolerant remote stacking 
supported
•	 Smart continuous switching technology
•  ITU-T G.8032/Y1344 2010: Ethernet Ring 
Protection
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP) encompasses IEEE 
802.1D Spanning Tree Protocol (STP) 
and IEEE 802.1w Rapid Spanning Tree 
Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+)  
and 1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link Aggregation 
Control Protocol (LACP) and static LAG 
groups across modules
•	 Dual-home link support for sub-second 
link protection without STP
•	 Virtual Router Redundancy Protocol 
(VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Bidirectional Forwarding Detection (BFD) 
for fast failure detection and reduced re-
convergence times in a IPv4/IPv6 routed 
environment
•	 Redundant and hot-swappable power 
supplies
•	 Built-in CPU protection against 
malicious attacks
•	 Split Virtual Chassis protection: Auto- 
detection and recovery of Virtual Chassis

<<<PAGE 541>>>
6
Datasheet  
Alcatel-Lucent OmniSwitch 6865
splitting due to one or more VFL or 
stack element failures
Advanced security
Access control
•	 Alcatel-Lucent Access Guardian 
framework for comprehensive user-
policy-based NAC
•	 Autosensing IEEE 802.1X multi-client, 
multi-VLAN support
•	 MAC-based authentication for non-IEEE 
802.1X hosts
•	 Web based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing pre-defined 
policy configuration to authenticated 
clients — VLAN, ACL, BW
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support
•	 Terminal Access Controller Access-
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial-In 
User Service (RADIUS) and Lightweight 
Directory Access Protocol (LDAP) 
administrator authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•  Kerberos snooping authentication for 
user authentication and network access 
control
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-based 
filtering in hardware (Layer 1 to Layer 4)
•	 DHCP v4 & v6 Snooping, DHCP IP and 
Address Resolution Protocol (ARP) spoof 
protection
• 	DHCPv6 guard and DHCPv6 Client guard
•	 ARP poisoning detection
•	 IP v4 & v6 Source Filtering as a 
protective and effective mechanism 
against ARP attacks
•	 Bring Your Own Device (BYoD) provides 
on-boarding of Guest,  
IT/non-IT issued and silent devices. 
Restriction/Remediation of traffic 
from non-compliant devices. Uses 
RADIUS CoA to dynamically enforce 
User Network Profiles based on 
Authentication, Profiling, Posture check 
of devices.
•	 Private VLAN
•	 LLDP Security mechanism for rogue 
device detection and restriction
Network control
•	 AOS secured diversified code solution 
is available  on OmniSwitch® 6865, 
hardening it at both the software source 
code and binary executable levels to 
enhance overall network security.
•	 AOS secured diversified code protects 
networks from intrinsic vulnerabilities, 
code exploits, embedded malware, 
and potential back doors that could 
compromise mission- critical operations.
QoS
•	 Priority queues: Eight hardware-based 
queues per port for flexible QoS 
management
•	 Traffic prioritization: Flow-based 
QoS Flow-based traffic policing and 
bandwidth management
•	 32-bit IPv4/128-bit IPv6 non-contiguous 
mask classification
•	 Egress traffic shaping
•	 DiffServ architecture
•	 Congestion avoidance: Support for end- 
to-end head-of-line (E2E-HOL) blocking 
prevention, IEEE 802.1Qbb Priority-
based Flow Control (PFC) and IEEE 
802.3x Flow Control (FC)
Layer-3 routing and multicast
IPv4 routing
•	 Multiple VRF & inter-VRF route leaking
•	 Static routing
•	 Routing Information Protocol (RIP) v1 
and v2
•	 Open Shortest Path First (OSPF) v2 with 
Graceful Restart
•	 Intermediate System to Intermediate 
System (IS-IS) with Graceful Restart
•	 Border Gateway Protocol (BGP) v4 with 
Graceful Restart
•	 Generic Routing Encapsulation (GRE) 
and IP/IP tunneling
•	 Virtual Router Redundancy Protocol 
(VRRPv2)
•	 DHCP relay (including generic UDP 
relay)
•	 Address Resolution Protocol (ARP)
•	 Policy-based routing and server  
load balancing
•	 DHCPv4 server
IPv6 routing
•	 Multiple VRF & Inter-vrf route leaking
•	 Internet Control Message Protocol 
version 6 (ICMPv6)
•	 Static routing
•	 Routing Information Protocol Next 
Generation (RIPng)
•	 Open Shortest Path First (OSPF) v3 with 
Graceful Restart
•	 Intermediate System to Intermediate 
System (IS-IS) with Graceful Restart
•	 Multi-Topology IS-IS (M-ISIS)
•	 BGP v4 multiprotocol extensions for 
IPv6 routing (MP-BGP)
•	 Graceful Restart extensions for OSPF 
and BGP
•	 Virtual Router Redundancy Protocol 
version 3 (VRRPv3)
•	 Neighbor Discovery Protocol (NDP)
•	 Policy-based routing and server  
load balancing
•	 DHCPv6 server
•	 DHCPv6 Relay and UDPv6 relay
IPv4/IPv6 multicast
•	 Internet Group Management Protocol 
(IGMP) v1/v2/v3 snooping
•	 Protocol Independent Multicast – 
Sparse- Mode (PIM-SM), Source Specific 
Multicast (PIM-SSM)
•	 Protocol Independent Multicast – 
Dense- Mode (PIM-DM), Bidirectional 
Protocol Independent Multicast  
(PIM-BiDir)
•	 Distance Vector Multicast Routing 
Protocol (DVMRP)
•	 Multicast Listener Discovery (MLD) v1/v2 
snooping
•	 PIM to DVMRP gateway support
Fluent network for voice, 
video and data
•	 SIP profile for QOS, priority tuning for 
end-to-end processing*
•	 Multicast DNS Relay: Bonjour protocol 
support for wired Airgroup
Advanced Layer-2 services
•	 Ethernet services support using IEEE 
802.1ad Provider Bridges (also known as 
Q-in-Q or VLAN stacking)
•	 Ethernet OAM (802.1ag , ITU-T Y.1731): 
Connectivity Fault Management  
(L2 ping & Link trace)
•	 Ethernet in First mile: Link OAM 
(802.3ah)
•	 Fabric virtualization services IEEE 
802.1aq Shortest Path Bridging (SPB-M)

<<<PAGE 542>>>
7
Datasheet  
Alcatel-Lucent OmniSwitch 6865
•	 In-band management for SPB-M
•	 Ethernet network-to-network interface 
(NNI) and user network interface (UNI)
•	 Service Access Point (SAP) profile 
identification
•	 Service VLAN (SVLAN) and Customer 
VLAN (CVLAN) support
•	 VLAN translation and mapping including 
CVLAN to SVLAN
•	 Port mapping
•	 DHCP Option 82: Configurable relay 
agent information
•	 Multiple VLAN Registration Protocol 
(MVRP)
•	 HA-VLAN for Layer 2 clusters such 
as MS-NLB and active-active Firewall 
clusters
•	 TR-101 Point-to-Point Protocol over 
Ethernet (PPPoE) Intermediate Agent 
allowing for the PPPoE network access 
method
•	 Service Assurance Agent (SAA) for 
proactively measuring network health, 
reliability and performance.
•	 Jumbo frame support
•	 Bridge Protocol Data Unit (BPDU) 
blocking
•	 STP Root Guard
•	 STP Loop-Guard
•	 Loopback Detection to auto-detect and 
prevent L2 loops
Supported standards
IEEE standards
•	 IEEE 802.1D STP
•	 IEEE 802.1p CoS
•	 IEEE 802.1Q VLANs
•	 IEEE 802.1ab (LLDP)
•	 IEEE 802.1ag (OA&M)
•	 IEEE 802.1ad Provider Bridges Q-in-Q/ 
VLAN stacking
•	 IEEE 802.1ak (Multiple VLAN Registration 
Protocol (MVRP)
•	 IEEE 802.1aq Shortest Path Bridging 
(SPB)
•	 IEEE 802.1s MSTP
•	 IEEE 802.3i 10BASE-T
•	 IEEE 802.1w RSTP
•	 IEEE 802.3x Flow Control
•	 IEEE 802.3z Gigabit Ethernet
•	 IEEE 802.3ab 1000Base-T
•	 IEEE 802.3ac VLAN Tagging
•	 IEEE 802.3ad/802.1AX Link Aggregation
•	 IEEE 802.3ae 10 GigE
•	 IEEE 802.3af Power over Ethernet
•	 IEEE 802.3at PoE Plus
•	 IEEE 802.3az Energy Efficient  
Ethernet (EEE)
•	 IEEE 802.1x-2004
•	 IEEE 1588-2008 (PTP)
ITU-T recommendations
•	 ITU-T G.8032/Y.1344 2010: Ethernet 
Ring Protection (ERPv2)
•	 ITU-T Y.1731 OA&M fault and 
performance management
IETF RFCs
IPv4
•	 RFC 2003 IP/IP Tunneling
•	 RFC 2131 Dynamic Host Configuration 
Protocol (DHCPv4)
•	 RFC 2784 GRE Tunneling
•	 RFC 4022/2452 MIB for IPv4 TCP
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4113/2454 MIB for IPv4 UDP
•	 RFC 4292/4293 IPv4 MIBs
OSPF
•	 RFC 1765 OSPF Database Overflow
•	 RFC 1850/2328/4570 OSPF v2  
and MIB
•	 RFC 2154 OSPF MD5 Signature
•	 RFC 2370/3630 OSPF Opaque LSA
•	 RFC 2740/5340 OSPFv3 for IPv6
•	 RFC 3101 OSPF NSSA Option
•	 RFC 3623/5187 OSPF Graceful Restart
•  RFC 5838 MIB for OSPFv3
•  RFC 4552 Authentication for OSPFv3
•  RFC 5709 OSPFv2 HMAC-SHA 
Cryptographic Authentication
RIP
•	 RFC 1058 RIP v1
•	 RFC 1722/1723/2453/1724 RIP v2 and 
MIB
•	 RFC 1812/2644 IPv4 Router 
Requirements
•	 RFC 2080 RIPng for IPv6
BGP
•	 RFC 1269/1657/4273 BGP v3  
and v4 MIB
•	 RFC 1403/1745 BGP/OSPF Interaction
•	 RFC 1771-1774/2842/2918/3392/4271  
BGP v4
•	 RFC 1965 BGP AS Confederations
•	 RFC 1966/2796 BGP Route Reflection
•  RFC 1997/1998/4360 BGP
Communities attribute
•	 RFC 2042/5396 BGP New Attribute
•	 RFC 2385 BGP MD5 Signature
•	 RFC 2439 BGP Route Flap Damping
•	 RFC 2545 BGP-4 Multiprotocol 
Extensions for IPv6 Routing
•	 RFC 2858/4760 Multiprotocol Extensions 
for BGP-4
•	 RFC 3065 BGP AS Confederations
•	 RFC 4456 BGP Route Reflection
•	 RFC 4486 Subcodes for BGP Cease 
Notification
•	 RFC 4724 Graceful Restart for BGP
•  RFC 3392/5492/5668/6793 BGP 4-Octet 
ASN
•	 RFC 5082 Generalized TTL Security 
Mechanism (GTSM)
IS-IS
•	 RFC 1142/1195/3719/3787/5308 IS-IS 
v4
•	 RFC 2763/2966/3567/3373 Adjacencies 
and route management
•	 RFC 5120 M-ISIS: Multi Topology  
IS-IS
•	 RFC 5306 Graceful Restart
•	 RFC 5309/draft-ietf-isis-igp-p2p-over-lan 
Point to point over LAN
•	 RFC 6329 IS-IS Extensions Supporting 
IEEE 802.1aq SPB
•	 RFC 5304 IS-IS Cryptographic 
Authentication
•	 RFC 5310 IS-IS Generic Cryptographic 
Authentication
IP multicast
•	 RFC 1075/draft-ietf-idmr-dvmrp-v3-11. 
txt DVMRP
•  RFC 2362/4601/5059 PIM-SM
•	 RFC 2365 Multicast
•  RFC 2710/3019/3810/MLD v2  
for IPv6
•	 RFC 2715 PIM and DVMRP 
interoperability
•	 RFC 2933 IGMP MIB
•	 RFC 3376 IGMPv3 (includes IGMP v2/v1)
•	 RFC 3569 Source-Specific Multicast 
(SSM)
•	 RFC 3973 Protocol Independent 
Multicast- Dense Mode (PIM-DM)
•	 RFC 4541 Considerations for IGMP and 
MLD Snooping Switches
•	 RFC 5015 BiDIR PIM
•	 RFC 5060 Protocol Independent 
Multicast MIB
•	 RFC 5132 Multicast Routing MIB
•	 RFC 5240 PIM Bootstrap Router MIB
IPv6
•	 RFC 1981 Path MTU Discovery
•	 RFC 2460 IPv6 Specification
•	 RFC 2461 NDP
•	 RFC 2464 IPv6 over Ethernet
•	 RFC 2465 MIB for IPv6: Textual 
Conventions (TC) and General Group
•	 RFC 2466 MIB for IPv6: ICMPv6 Group
•	 RFC 2711 Router Alert Option
•	 RFC 3056 6to4 Tunnels
•	 RFC 3315 Dynamic Host Configuration 
Protocol for IPv6 (DHCPv6)
•	 RFC 3484 Default Address Selection

<<<PAGE 543>>>
8
Datasheet  
Alcatel-Lucent OmniSwitch 6865
•	 RFC 3493/2553 Basic Socket API
•	 RFC 3542/2292 Advanced Sockets API
•	 RFC 3587/2374 Global Unicast  
Address Format
•	 RFC 3595 TC for IPv6 Flow Label
•	 RFC 3596/1886 DNS for IPv6
•	 RFC 4007 Scoped Address
•	 RFC 4022/2452 MIB for IPv6 TCP
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4113/2454 MIB for IPv6 UDP
•	 RFC 4193 Unique Local Addresses
•	 RFC 4213/2893 Transition Mechanisms
•	 RFC 4291/3513/2373 Addressing 
Architecture (uni/any/multicast)
•	 RFC 4292/4293 IPv6 MIBs
•	 RFC 4301/2401 Security Architecture
•	 RFC 4302/2402 IP Authentication 
Header
•	 RFC 4303/2406 IP Encapsulating 
Security Payload (ESP)
•	 RFC 4308 Cryptographic Suites for IPSec
•  RFC 4443/2463 ICMPv6
•	 RFC 4861/2461 Neighbor Discovery
•	 RFC 4862/2462 Stateless Address 
Autoconfiguration
•	 RFC 5095 Deprecation of Type 0 Routing 
Headers in IPv6
Manageability
•	 RFC 854/855 Telnet and Telnet options
•  RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•  RFC 1155/2578-2580 SMI v1 and SMI v2
•  RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•  RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP Traps
•	 RFC 1573/2233/2863 Private Interface 
MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•  RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from Forms: 
multipart/form-data
•	 RFC 2396 Uniform Resource Identifiers 
(URI): Generic Syntax
•	 RFC 2570-2576/3410-3415/3584 SNMP 
v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•  RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 3826 (AES) Cipher Algorithm in the 
SNMP User-based Security Model
•	 RFC 4122 A Universally Unique IDentifier 
(UUID) URN Namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251 Secure Shell Protocol 
Architecture
•	 RFC 4252 The Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4253  SSH Transport Layer Protocol
•	 RFC 4254  SSH Connection Protocol
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 6585 Additional HTTP Status Codes
Security
•	 RFC 1321 MD5
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and crypto 
algorithms
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575/2618 
RADIUS Authentication and Client MIB
•	 RFC 3576  Dynamic Authorization 
Extensions to RADIUS
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 3162 RADIUS and IPv6
•	 RFC 4301 Security Architecture for IP
•	 RFC 5517 Private VLAN
Security - With Common Criteria 
enabled  
•	 RFC 5280 - Internet X.509 PKI Certificate 
and CRL Profile  
•	 RFC 2560 - X.509 Internet PKI Online 
Certificate Status Protocol - OCSP  
•	 RFC 2986 - PKCS #10: Certification 
Request Syntax Specification v 1.7  
•	 RFC 5246 - TLS Protocol v 1.2  
•	 RFC 4346 - TLS Protocol v 1.1  
•	 RFC 3268 -  AES Cipher suites  
for TLS  
•	 RFC 6125 - Representation and 
Verification of Domain-Based 
Application Service Identity within 
Internet PKIX Certificates in the Context 
of TLS
•	 draft-ietf-radext-radsec-12 - TLS 
encryption for RADIUS
QoS
•	 RFC 896 Congestion Control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 2697 srTCM
•	 RFC 2698 trTCM
•	 RFC 3635 Pause Control
Others
•	 RFC 791/894/1024/1349 IP and IP 
Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•  RFC 2581 TCP Congestion Control
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/ 
Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router RADIUS 
Discovery
•	 RFC 1305/2030/5905 NTP v4 and Simple 
NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2581 TCP Congestion Control
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 2338/3768/2787 VRRP and MIB
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
•	 RFC 3621 Power Ethernet MIB
•  RFC 4562 MAC-Forced Forwarding
Software Defined Networking 
(SDN)
•	 OpenFlow Switch Specification v1.3.1
•	 OpenFlow Switch Specification v1.0.0

<<<PAGE 544>>>
9
Datasheet  
Alcatel-Lucent OmniSwitch 6865
Ordering information
Part number
Description
OmniSwitch 6865 models
OS6865-P16X
OS6865-P16X: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis with 12 RJ-45 10/100/1000 Base-T 
PoE+ ports out of which 4 are 75W IEEE 802.3bt ports, two 1000 Base-X SFP ports, two SFP+ (1G/10G) ports, RS-
232 Console (RJ45) and USB port. The bundle includes the chassis pre-installed with fully featured AOS software & 
advanced IP routing SW (IPv4/IPv6), one AC power supply, country-specific power cord, user manuals access card, 
power supply tray and hardware for mounting in a  
19” rack
OS6865-P16XD
OS6865-P16XD: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis with 12 RJ-45 10/100/1000 
Base-T PoE+ ports out of which 4 are 75W IEEE 802.3bt ports, 2 1000 Base-X SFP ports, 2 SFP+ (1G/10G) ports, RS-
232 Console (RJ45) and USB port. The bundle includes the chassis pre-installed with fully featured AOS software & 
advanced IP routing SW (IPv4/IPv6), one DC power supply, user manuals access card, power tray and hardware for 
mounting in a 19” rack
OS6865-U12X
OS6865-U12X: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis with four 100/1000 Base-X SFP 
ports, two 1000 Base-X SFP Ports, four 10/100/1000 Base-T 75W IEEE 802.3bt ports, two SFP+ (1G/10G) ports, RS-
232 Console (RJ45) and USB port. The bundle includes the chassis pre-installed with fully featured AOS software & 
advanced IP routing SW (IPv4/IPv6), one AC power supply, country-specific power cord, user manuals access card, 
power tray and hardware for mounting in a 19” rack. 
OS6865-U12XD
OS6865-U12XD: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis with four 100/1000 Base-X SFP 
ports, two 1000 Base-X SFP ports, four 10/100/1000 Base-T 75W IEEE 802.3bt ports, two SFP+ (1G/10G) ports, RS-
232 Console (RJ45) and USB port. The bundle includes the chassis pre-installed with fully featured AOS software & 
advanced IP routing SW (IPv4/IPv6), one DC power supply, user manuals access card, power tray and hardware for 
mounting in a 19” rack. 
OS6865-U28X
OS6865-U28X: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with 20 
100/1000 Base-X SFP ports, four SFP+ (1G/10G) ports, four 10/100/1000 Base-T 75W IEEE 802.3bt ports, RS-232 
Console (RJ45), USB, and two 20G VFL QSFP+ ports. The bundle includes the chassis pre-installed with fully featured 
AOS software & advanced IP routing SW (IPv4/IPv6), one AC power supply, country-specific power cord, user 
manuals access card, power tray and hardware for mounting in a 19” rack. 
OS6865-U28XD
OS6865-U28XD: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with 20 
100/1000 Base-X SFP ports, four SFP+ (1G/10G) ports, four 10/100/1000 Base-T 75W IEEE 802.3bt ports, RS-232 
Console (RJ45), USB, and two 20G VFL QSFP+ ports. The bundle includes the chassis pre-installed with fully featured 
AOS software & advanced IP routing SW (IPv4/IPv6), one DC power supply, user manuals access card, power tray 
and hardware for mounting in a 19” rack.
OmniSwitch 6865 TAA Certified Switches
TA6865-P16X-US
TA6865-P16X: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis with 12 RJ-45 10/100/1000 Base-T 
PoE+ ports out of which 4 are 75W IEEE 802.3bt ports, two 1000 Base-X SFP ports, two SFP+ (1G/10G) ports, RS-
232 Console (RJ45) and USB port. The bundle includes the chassis pre-installed with fully featured AOS software & 
advanced IP routing SW (IPv4/IPv6), one AC power supply, US power cord, user manuals access card, power supply 
tray and hardware for mounting in a 19” rack.
TA6865-U12X-US
TA6865-U12X: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis with four 100/1000 Base-X SFP 
ports, two 1000 Base-X SFP Ports, four 10/100/1000 Base-T 75W IEEE 802.3bt ports, two SFP+ (1G/10G) ports, 
RS-232 Console (RJ45) and USB port. The bundle includes the chassis pre-installed with fully featured AOS software 
& advanced IP routing SW (IPv4/IPv6), one AC power supply, US power cord, user manuals access card, power tray 
and hardware for mounting in a 19” rack.
TA6865-U28X-US
TA6865-U28X: Hardened Gigabit Ethernet L3 fixed configuration fan-less chassis in a 1U form factor with20 100/1000 
Base-X SFP ports, four SFP+ (1G/10G) ports, four 10/100/1000 Base-T 75W IEEE 802.3bt ports, RS-232 Console (RJ45), 
USB, and two 20G VFL QSFP+ ports. The bundle includes the chassis pre-installed with fully featured AOS software & 
advanced IP routing SW (IPv4/IPv6), one AC power supply, US power cord, user manuals access card, power tray and 
hardware for mounting in a 19” rack.

<<<PAGE 545>>>
10
Datasheet  
Alcatel-Lucent OmniSwitch 6865
OmniSwitch 6865 power supplies
OS6865-BP
OS6865-BP modular AC backup power supply. Provides system & PoE power to one OS6865 switch.  
Ships with country specific power cord
OS6865-BP-D
OS6865-BP modular DC backup power supply. Provides system & PoE power to one OS6865 switch
OmniSwitch 6865 accessories
OS6865-CBL-40
OS6865 20 Gigabit direct attached copper cable (40 cm, QSFP+) for Virtual Chassis connections, for OS6865-U28X
OS6865-CBL-100
OS6865 20 Gigabit direct attached copper cable (1m, QSFP+) for Virtual Chassis connections, for 
OS6865-U28X
OS6865-CBL-300
OS6865 20 Gigabit direct attached copper cable (3m, QSFP+) for Virtual Chassis connections, for  
OS6865-U28X
OS6865-TRAY-1U
Spare Power Supply tray kit with 1RU brackets for mounting two PS trays side-by-side in a 19” rack 
for OS6865-U28X
OS6865-DIN-MNT
DIN rail mounting kit for OS6865-P16X & OS6865-U12X switches. Includes universal mounting brackets and 2 
brackets with DIN clip attached.
OS6865-REAR-MNT
Mounting bracket & Side mounting rails kit to secure OS6865-U28x with the rear of a 19” rack
OmniSwitch 6865 DNV certified parts
OS6865-DNV-HRCK
DNV power supply cover kit for OS6865-P16x & OS6865-U12x. Mandatory kit for installations that require DNV 
certified  OS6865-P16x and OS6865-U12x. Contains PS cover, rear side-support rail, rear support bracket, side 
mount bracket and all mounting hardware.
OS6865-DNV-FRCK
DNV power supply cover kit for OS6865-U28x. Mandatory kit for installations requiring DNV certified OS6865-U28x. 
Contains PS cover, rear side-support rail, rear support bracket, side mount bracket and  
all mounting hardware.
OmniSwitch 6865 transceivers
iSFP-100-MM
100Base-FX industrial transceiver with an LC type interface. This transceiver is designed for use over multimode fiber.
iSFP-100-SM15
100Base-FX industrial transceiver with an LC type interface. This transceiver is designed for use over single-mode 
fiber up to 15 km
iSFP-100-LC-SM40
100Base-FX Industrial SFP transceiver with an LC type interface. This transceiver is designed for use  
over single mode fiber optic cable up to 40KM. 
iSFP-GIG-T
1000Base-T industrial Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and  
full-duplex mode
iSFP-GIG-SX
1000Base-SX industrial Gigabit Ethernet industrial optical transceiver (SFP MSA)
iSFP-GIG-LX
1000Base-LX industrial Gigabit Ethernet optical transceiver (SFP MSA)
iSFP-GIG-LH40
1000Base-LH industrial Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on  
9/125 µm SMF
iSFP-GIG-LH70
1000Base-LH industrial Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on  
9/125 µm SMF
iSFP-GIG-BX-U
1000Base-BX SFP bi-directional transceiver with an LC type of interface. Designed for use over single mode fiber 
optic on a single strand link up to 10 km. Transmits 1310 nm and receives 1490 nm optical signal.
iSFP-GIG-BX-D
1000Base-BX SFP bi-directional transceiver with an LC type of interface. Designed for use over single mode fiber 
optic on a single strand link up to 10 km. Transmits 1310 nm and receives 1490 nm optical signal. 
10G transceivers
iSFP-10G-LR
10 Gigabit industrial optical transceiver (SFP+). Supports monomode fiber over 1310 nm wavelength (nominal) with 
an LC connector. Typical reach of 10 km
iSFP-10G-ER
10 Gigabit industrial optical transceiver (SFP+). Supports monomode fiber over 1550 nm wavelength (nominal) with 
an LC connector. Typical reach of 40 km
iSFP-10G-ZR
10 Gigabit industrial optical transceiver (SFP+). Supports data transmission at 1550nm over up to 80km single 
mode fiber. LC connector type
SFP+ direct attached cables 
iSFP-10G-C1M
10 Gigabit industrial direct attached copper cable (1 m, SFP+)
iSFP-10G-C3M
10 Gigabit industrial direct attached copper cable (3 m, SFP+)
iSFP-10G-C7M
10 Gigabit industrial direct attached copper cable (7 m, SFP+)

<<<PAGE 546>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license  
by ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/
legal/trademarks-copyright. All other trademarks are the property of their respective owners.  
The information presented is subject to change without notice. Neither ALE Holding nor any of its affiliates 
assumes any responsibility for inaccuracies contained herein. © Copyright 2022 ALE International,  
ALE USA Inc. All rights reserved in all countries. MPR00302457EN (April 2022)
Warranty
The OmniSwitch 6865 family comes with a Limited Lifetime Warranty.
Services and support
For more information about our Professional services, Support services, and Managed services,  
please go to http://enterprise.alcatel-lucent.com/?services=EnterpriseServices&page=directory.

<<<PAGE 547>>>
Datasheet 
Alcatel-Lucent OmniSwitch 6900
Alcatel-Lucent OmniSwitch 6900
Core and Data Centre LAN Switches
The Alcatel-Lucent OmniSwitch® 6900 fixed Core 
LAN and Data Center (DC) switches are compact, 
high-density 10, 25, 40 and 100 Gigabit Ethernet 
(GigE) platforms. They offer high performance 
aand extremely low latency Layer-2 and Layer-3 
switching for campus and DC Fabric networks. 
They are designed for the most demanding 
software-defined operations in  
virtualized or physical networks.
OmniSwitch 6900s can be positioned as Top- of-
Rack (ToR) or spine switches in DC environments, 
or as core and aggregation devices in campus 
networks. They support a wide range of protocols 
and programable interface (API) for building 
ALE’s autonomous Service Defined Network or 
overlay networks based on Software Defined 
Network architectures.
OS6900C32E
OS6900V48
OS6900X48
OS6900T24
OS6900T48
OS6900X24
The OmniSwitch 6900 product family offers a very high port 
density, with up to 128 x 10 GigE, 80 x 25 GigE and up to  
32 x 40/100 GigE ports in a 1RU form factor. The Virtual 
Chassis feature extends the modularity and reliability 
of connectivity to address any size of virtualized, highly 
secured modern and autonomous networks. MACsec is also 
supported on specific OS6900 models for mission critical 
and encrypted communication networks. The OmniSwitch 
6900 product family leverages an energy-efficient model 
with leading low power consumption, making them the  
most efficient and versatile switches in their class.

<<<PAGE 548>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 6900
Features
Benefits
•	 Wire-rate non-blocking up to 6.4 Tb/s switching and routing capacity  
at 100 GigE, 40 GigE, 25 GigE, 10 GigE/1 GigE and 10BASE-T speeds.
•	 Resilient hardware system architecture.
•	 Internal, hot-swappable power supplies and fans.
•	 Front-to-back and back-to-front cooling options provide lowest power 
consumption per port in its class.
•	 Integral operating system advances functions: quality of service (QoS), 
access control lists (ACLs), Layer-2/ Layer-3 switching, Virtual LAN (VLAN) 
stacking and IPv6.
•	 High-availability hardware Virtual Extensible LAN (VXLAN) Virtual Tunnel 
End Point (VTEP) gateway for network virtualization.
•	 Integrated overlay (VXLAN) and underlay internetworking automated 
with OpenStack neutron plug-in and Open vSwitch Database (OVSDB) 
protocol for integration with SDN controllers such as VMware NSX and 
Nuage Networks.
•	 Hardware virtual routing and forwarding (VRF) support for VRF-lite and IP 
Virtual Private Network (IP VPN).
•	 Scalable network virtualization architecture with guaranteed SLA delivery 
over standard Ethernet fabric: auto-Fabric IP routing for routed backbone 
and access provisioning, SPB for bridging and routed services, Multiple 
VLAN Registration Protocol (MVRP) and dynamic Virtual Network  
Profiles (VNP).
•	 Zero-touch provisioning and network automation with out-of-the- box 
plug-and-play Auto-Fabric for automatic protocol and topology discovery. 
Protocol auto-discovery and self-provisioning works with any Ethernet 
device that supports standard IEEE protocols, such as 802.1aq (Shortest 
Path Bridging- MAC, SPBM), 802.1ak (MVRP), or 802.3ad/802.1AX (Link 
Aggregation Control Protocol, LACP). Auto-fabric operation extends to  
IP routing protocol provisioning and IP on-boarding.
•	 Virtualized management, control and programmability
•	 Unified virtual chassis with support for up to 6 switches.
•	 Flexible and programmable Layer 2, Layer 3, ACL, QoS network 
virtualization function abstracted into a single virtual routing and 
bridging instance
•	 Network management virtualization
•	 Comprehensive northbound RESTful API to the entire  
Alcatel- Lucent operating system (AOS) feature set.
•	 API offers access to all AOS CLI commands and all MIB structures
•	 AOS-embedded scripting capabilities supporting Python and Bash 
programming.
•	 VMware-certified Alcatel-Lucent OmniVista® 2500 Virtual Machine 
Manager (VMM), Virtual Network Profiles (VNP) integration, VM SLA 
monitoring and application fingerprinting for unmanned network 
operation and self-adjusting SLA for application delivery
•	 Interfaces with VMware vCenter® and Citrix™ XenServer® for discovery 
and inventory
•	 VMware vCenter integration
•	 Single pane-of-glass for end-to-end physical and virtual networks 
infrastructure operations VM to underlay network correlation and  
single pane visibility.
•	 Real time tracking between VM and its network location
•	 Dynamic VM performance for application performance analytics  
and visibility
•	 Dynamic application profiling with in-line application recognition  
based on signatures and auto-adjustment of the network security  
and QoS treatment.
•	 Outstanding performance when supporting real-time voice, data, 
storage, and video applications for converged scalable networks,  
with high port density in 1RU form factor
•	 Resiliency maximizes uptime for converged mission- critical networks.
•	 Ensures efficient power management, thereby reducing operating 
expenses and lowering total cost of ownership.
•	 The switch architecture simplifies the deployment of converged 
storage for Internet Small Computer System Interface (iSCSI) and 
Network-Attached Storage (NAS) systems.
•	 The switch supports RoCEv2 (RDMA over Converged Ethernet) a 
standard protocol that allows Remote Direct Memory Access (RDMA) 
over an Ethernet network to ensure a zero-packet-loss, low-latency, 
and high-throughput network for RoCEv2 distributed applications.
•	 Embedded Software-defined networking (SDN) integration to control 
virtual network profiles and policy management.
•	 VXLAN VTEP allows overlay to underlay bridging and data center 
interconnecting. 
•	 Built-in dynamic and automated policy enforcement
•	 Policy enforcement engine fully open for external control through 
RESTful northbound APIs for automation and integration of 
innovative applications
•	 Native and overlay Cloud Multi-tenancy support.
•	 Out-of-the-box flexible fabric architecture designed to automate  
and simplify the end-to-end deployment of campus, data center,  
and cloud-based services. 
•	 Prevent human mistakes by automating standardized and replicable 
configurations.
•	 Prevents host address explosion and flooding with built-in SLA 
service support at low capital and operating costs and based on 
interoperable proven standards.
•	 Optimizes/simplifies Layer 2 and Layer 3 network designs and 
reduces administration overhead while increasing network capacity 
with resilient multipath active-active dual homing multi-chassis 
support.
•	 Automated Cloud Multi-Tenancy support through vNP.
•	 The OmniSwitch 6900 virtual chassis increases system redundancy 
and resiliency, providing maximum uptime and high availability in  
the network.
•	 Provides interoperability, investment protection, and flexibility
•	 Supports Spine/Leaf and Pod/Mesh architectures for flexible 
deployment.
•	 Virtual chassis topology is flexible to accommodate any architecture 
that is needed to meet the desired latency and oversubscription 
requirements.
•	 The RESTful interface exposes the entire AOS feature set as a 
programmable data structure. The API allows external controllers 
and applications to control and manage the switch’s data plane and 
monitor its counters, statistics and events for the automation of the 
network
•	 Unifies physical and virtual infrastructures by providing network 
operators with a comprehensive end-to-end network view for VM 
inventory, VM performance, location tracking, event and log auditing
•	 Monitors applications and malware activity, adjusting the network 
to meet the application SLAs according to the business operational 
requirements.  and provisioning operations.

<<<PAGE 549>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 6900
Detailed product features 
Alcatel-Lucent OmniSwitch 
6900 models
The Alcatel-Lucent OmniSwitch 6900 
family offers high- performance and very 
low-latency Layer 2/Layer 3 10/40 GigE 
switches. All models are 1RU form factor 
with redundant power supplies and fan 
trays for front- to- back and back-to-front 
airflow. Available interfaces include 25 GigE, 
40/100 GigE, 1/10 GigE, 1/10 GBASE-T.
•	 OmniSwitch 6900V48 has 48 1/10/25G 
SFP28 ports and eight QSFP28 ports. 
The QSFP28 ports operate at 100G or 
4x25G or 40G or 4x10G. Maximum 25G 
port density is 80 ports.
•	 OmniSwitch 6900X48E has 40 1/10G 
SFP+ ports, 8 10/25G SFP28 ports and 
4 QSFP28 ports. The QSFP28 ports 
operate at 100G or 4x25G or 40G or 
4x10G. All ports support IEEE 802.1AE 
MAC Security standard with AES 128-bit 
and 256-bit encryption functionality.
•	 OmniSwitch 6900X24/T24 has  
24 1/10 GigE SFP+ or 1/10 GBASE-T  
and 2 100 GigE QSFP28 ports that 
operate at 100 GigE or 4x25 GigE  
or 40 GigE or 4x10 GigE
•	 OmniSwitch 6900C32E has 32 x QSFP28 
ports that can operate at 100 GigE or 
4x25 GigE or 40 GigE or 4x10 GigE. 
Maximum 25G port density is 128 ports.
•	 OmniSwitch 6900X48/T48 has 48 1-10 
GigE SFP+/1-10 GBASE-T and six 100 
GigE QSFP28 ports that operate at 100 
GigE or 40 GigE of which 2 ports can be 
splitted into 4x25 GigE or 4x10 GigE.
Simplified manageability
•	 Fully programmable RESTful web 
services interface with XML and JSON 
support. The API enables access to 
Command Line Interface (CLI) and 
individual management information 
BASE (MIB) objects.
•	 Intuitive Alcatel-Lucent Enterprise 
CLI in a scriptable Python and Bash 
environment through console, Telnet  
or Secure Shell (SSH) v2 over IPv4/IPv6
•	 Powerful Alcatel-Lucent Enterprise 
WebView Graphical Web Interface 
through HTTP and HTTPS over IPv4/IPv6
•	 Full configuration and reporting using 
Simple Network Management Protocol 
(SNMP) v1/2/3 to facilitate third-party 
network management over IPv4/ IPv6
•	 File upload using USB, Trivial File 
Transfer Protocol (TFTP), FTP, SFTP  
or secure copy (SCP) over IPv4/IPv6
•	 Multiple microcode image support  
with fallback recovery
•	 Local (on the flash) and remote server 
logging (Syslog) for events  
and commands
•	 Loopback IP address support for 
management-per-service
•	 Management VRF support
•	 Policy and port-based mirroring, 
Remote port mirroring sFlow v5 and 
Remote Network Monitoring (RMON)
•	 Digital Diagnostic Monitoring on all 
6900 fiber optic interfaces.
•	 Dynamic Host Configuration Protocol 
(DHCP) relay
•	 IEEE 802.1AB LLDP with MED extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server managed 
by Nokia VitalQIP® DNS/ DHCP IP 
Management Software
Resiliency and high availability
•	 Unified management, control and 
fabric-mesh virtual chassis technology
•	 Virtual chassis 1+N redundant 
supervisor manager
•	 Virtual chassis In-Service Software 
Upgrade (ISSU)
•	 Smart continuous switching technology
•	 ITU-T G.8032/Y1344 2010: Ethernet  
Ring Protection
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP), IEEE 802.1D Spanning 
Tree Protocol (STP) and IEEE 802.1w 
Rapid Spanning Tree Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+) and 
Alcatel-Lucent 1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link Aggregation 
Control Protocol (LACP) and static LAG 
groups across modules
•	 Virtual Router Redundancy Protocol 
(VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Bidirectional Forwarding Detection (BFD)
•	 Redundant and hot-swappable power 
supplies
•	 Redundant fans
•	 Hot-swappable fan tray
•	 Built-in CPU protection against 
malicious attacks
Data center networking
•	 Dynamic Virtual Network Profiles (vNP)
•	 IEEE 802.1aq Shortest Path Bridging 
(SPB-M)
•	 RFC 7348 Virtual extensible Local Area 
Network (VXLAN)
Software Defined Networking 
(SDN)
•	 Programmable AOS RESTful API
•	 OpenStack networking plug-in 
compatible with Grizzly or higher
•	 Software-controlled VXLAN hardware 
VTEP gateway
Advanced security Access control
•	 Autosensing IEEE 802.1X multi- client, 
multi-VLAN support for bridging and 
SPBM/VXLAN services
•	 MAC-based authentication for non-IEEE 
802.1X hosts
•	 Secure Shell (SSH) with public key 
infrastructure (PKI) support for bridging 
and SPBM/VXLAN services
•	 Terminal Access Controller Access- 
Control System Plus (TACACS+) client
•	 Centralized Remote Access Dial- In 
User Service (RADIUS) and Lightweight 
Directory Access Protocol (LDAP) 
administrator authentication
•	 Centralized RADIUS for device 
authentication and network access 
control authorization
•	 Learned Port Security (LPS) or MAC 
address lockdown
•	 Access Control Lists (ACLs); flow-based 
filtering in hardware (Layer 1 to Layer 4)
•	 DHCP snooping, DHCP IP and Address 
Resolution Protocol (ARP) spoof 
protection
•	 ARP poisoning detection
•	 IP source filtering as a protective and 
effective mechanism against ARP attacks
Quality of Service (QoS)
•	 Priority queues: Eight hardware-based 
queues per port
•	 Traffic prioritization: Flow-based QoS
•	 Flow-based traffic policing and 
bandwidth management
•	 32-bit IPv4/128-bit IPv6 non-contiguous 
mask classification
•	 Egress traffic shaping
•	 Lossless Virtual Output Queuing (VOQ) 
with configurable scheduling algorithms
•	 DiffServ architecture

<<<PAGE 550>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 6900
IPv4 routing
•	 Multiple VRF
•	 Static routing with route labeling
•	 Routing Information Protocol (RIP) v1 
and v2
•	 Open Shortest Path First (OSPF) v2 with 
graceful restart
•	 Intermediate System to Intermediate 
System (IS-IS) with graceful restart
•	 Border Gateway Protocol (BGP) v4 with 
graceful restart
•	 Generic Routing Encapsulation (GRE) 
and IP/IP tunneling Virtual Router 
Redundancy Protocol (VRRPv2)
•	 DHCP relay (including generic UDP relay)
ARP
•	 Policy-based routing and server load 
balancing
•	 DHCPv4 server
IPv6 routing
•	 Multiple VRF
•	 Internet Control Message Protocol 
version 6 (ICMPv6)
•	 Static routing
•	 Routing Information Protocol Next 
Generation (RIPng)
•	 OSPF v3 with graceful restart
•	 Intermediate System to Intermediate 
System (IS-IS) with graceful restart
•	 Multi-Topology IS-IS
•	 BGP v4 multiprotocol extensions for 
IPv6 routing (MP-BGP)
•	 Graceful restart extensions for OSPF 
and BGP
•	 Virtual Router Redundancy Protocol 
(VRRPv3)
•	 Neighbors Discovery Protocol (NDP)
•	 Policy-based routing and server load 
balancing
•	 DHCPv6 server
IPv4/IPv6 multicast
•	 Internet Group Management Protocol 
(IGMP) v1/v2/v3 snooping
•	 Protocol Independent Multicast  
– Sparse-mode (PIM-SM), Source 
Specific Multicast (PIM-SSM)
•	 Protocol Independent Multicast – 
Dense- mode (PIM- DM), Bidirectional 
Protocol Independent Multicast  
(PIM-BiDir)
•	 Distance Vector Multicast Routing 
Protocol (DVMRP) Multicast Listener 
Discovery (MLD) v1/v2 snooping
•	 PIM to DVMRP gateway support (S,G) 
and (*,G) forwarding
Advanced Layer 2 services
•	 Ethernet services support using IEEE 
802.1ad Provider Bridges (also known as 
Q-in-Q or VLAN stacking)
•	 Fabric virtualization services 
IEEE802.1aq Shortest Path Bridging 
(SPB-M) and VXLAN
¬ Ethernet network-to-network interface 
(NNI) and user network interface (UNI)
¬ Service Access Point (SAP)
¬ Service VLAN (SVLAN) and Customer 
VLAN (CVLAN) support
¬ VLAN translation and mapping 
including CVLAN to SVLAN
•	 Port mapping
•	 DHCP Option 82: Configurable relay 
agent information
•	 MVRP
•	 High availability VLAN (HA-VLAN) for L2 
clusters such as MS-NLB and active-
active Firewall clusters
•	 Jumbo frame support
•	 Bridge Protocol Data Unit (BPDU) 
blocking
•	 STP Root Guard
Technical specifications
Product specifications and 
measurements
•	 Per-port LEDs
•	 Ethernet/FC: link/activity
•	 EMP: link/activity
•	 System LEDs
•	 OK: green/yellow
•	 PS1: green/yellow 
•	 PS2: green/yellow
•	 PWR Save: green
Compliance and 
certifications
EMI/EMC - Commercial
•	 FCC 47 CFR Part 15 Class A 
•	  ICES-003 Class A
•	 CE marking for European countries 
(Class A)
•	 EMC Directive 89/336/EEC 
•	 EN55022:1998:2006 Class A
•	 EN55024 :1998:A1: 2001+A2:2003
•	 EN61000-3-2
•	 EN61000-3-3
•	 EN61000-4-2
•	 EN61000-4-3
•	 EN61000-4-4
•	 EN61000-4-5
•	 EN61000-4-6
•	 EN61000-4-8
•	 EN61000-4-11
•	 CISPR22:1997 Class A
•	 VCCI (Class A)
•	 AS/NZS 3548 (Class A)
•	 IEEE 802.3 Hipot requirement and 
1.5 kV surge on data port for copper 
interfaces
Safety agency certifications
•	 IEC 62368-1
•	 US UL 60950
•	 IEC 60950-1:2001: all national deviations
•	 EN 60950-1: 2001: all deviations
•	 CAN/CSA-C22.2 No. 60950-1-03
•	 AS/NZ TS-001 and 60950:2000: Australia
•	 UL-AR: Argentina
•	 UL-GS Mark: Germany
•	 GOST: Russian Federation
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 CDRH Laser
Federal certifications
•	 FIPS 140-2
•	 Common Criteria EAL2
•	 Common Criteria NDcPP
•	 JITC
•	 Trade Agreements Act (TAA)
Supported standards
IEEE standards
•	 IEEE 802.1D STP
•	 IEEE 802.1p CoS
•	 IEEE 802.1Q VLANs 
•	 IEEE 802.1ad Provider Bridges Q-in-Q/
VLAN stacking
•	 IEEE 802.1ak (MVRP)
•	 IEEE 802.1aq Shortest Path Bridging 
(SPB)
•	 IEEE 80.1ab LLDP
•	 IEEE 802.1ag OAM
•	 IEEE 802.1 CEE 1.01
•	 IEEE 802.1s MSTP
•	 IEEE 802.1w RSTP
•	 IEEE 802.1X Port-based Network Access 
Control (PNAC).
•	 IEEE 802.3x Flow Control
•	 IEEE 802.3u Fast Ethernet
•	 IEEE 802.3z 1 GigE
•	 IEEE 802.3ab 1 GBASE-T
•	 IEEE 802.3ac VLAN Tagging
•	 IEEE 802.3ad/802.1AX Link Aggregation
•	 IEEE 802.3ae 10 GigE
•	 IEEE 802.3an 10 GBASE-T

<<<PAGE 551>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 6900
•	 IEEE 802.3az Energy Efficient Ethernet 
(EEE)
•	 IEEE 802.3ba 40 GigE
•	 IEEE 802.3by 25 GigE
•	 IEEE 802.3bm 100 GigE
•	 IEEE 802.1x-2004
•	 IEEE 802.1AE MACsec
•	 ITU-T recommendations
•	 ITU-T G.8032/Y.1344 2010: Ethernet 
Ring Protection (ERPv2)
ANSI recommendations
•	 INCITS/Project 1647-D/Rev7.10 FC-PI-4
•	 INCITS/T11/Project 2159-D/Rev
•	 1.23 T11-BB-6 compliance
•	 INCITS/T11/Project 1871-D/Rev
•	 2.00 T11-BB-5 support
IETF RFCs
IPv4
•	 RFC 2003 IP/IP Tunneling
•	 RFC 2784 GRE Tunneling
•	 RFC 2131 DHCPv4
•	 RFC 4292 IP Forwarding Table MIB
OSPF
•	 RFC 1765 OSPF Database Overflow
•	 RFC  1850/2328/4750 OSPFv2 and MIB
•	 RFC 2154 OSPF MD5 Signature
•	 RFC 2370/5250 OSPF Opaque LSA
•	 RFC 3101 OSPF NSSA Option
•	 RFC 3623 OSPF Graceful Restart
•	 RFC 2740/5340 OSPFv3 for IPv6
•	 RFC 4552 Authentication/ Confidentiality 
for OSPFv3
•	 RFC 5187 OSPFv3 Graceful Restart
•	 RFC 5838 MIB for OSPFv3 RIP
•	 RFC 1058 RIPv1
•	 RFC  1722/1723/2453/1724 RIPv2  
and MIB
•	 RFC 1812/2644 IPv4 Router 
Requirements
•	 RFC 2080 RIPng for IPv6
BGP
•	 RFC 1269/1657/4273 BGP v3
•	 and v4 MIB
•	 RFC 1403/1745 BGP/OSPF
•	 Interaction
•	 RFC 1771- 1774/2842/2918/4271 BGP
•	 RFC 1965 BGP AS Confederations
•	 RFC 1966 BGP Route Reflection
•	 RFC 1997/1998/4360 BGP
•	 Communities Attribute
•	 RFC 2042 BGP New Attribute
•	 RFC 2385 BGP MD5 Signature
•	 RFC 2439 BGP Route Flap Damping
•	 RFC 2545 BGP-4 Multiprotocol 
Extensions for IPv6 Routing
•	 RFC 2796 BGP-4 Route Reflection
•	 RFC 2858/4760 Multiprotocol Extensions 
for BGP-4
•	 RFC 3065 BGP AS Confederations
•	 RFC 4456 BGP Route Reflection
•	 RFC 4486 Subcodes for BGP Cease 
Notification
•	 RFC 4724 Graceful Restart for BGP
•	 RFC 3392/5492 Capabilities 
Advertisement with BGP-4
•	 RFC 5396/5668/6793 BGP
•	 4-Octet ASN and Textual Representation 
of ASN
IS-IS
•	 RFC 1142/1195/3719/3787/5308 IS-IS 
v4
•	 RFC  2763/2966/3567/3373
•	 Adjacencies and route management
•	 RFC 5120 M-ISIS: Multi-topology IS-IS
•	 RFC 5306 Graceful Restart
•	 RFC 5309/draft-ietf-isis-igp-p2p- over-lan 
Point to point over LAN
•	 RFC 6329 IS-IS Extensions Supporting 
IEEE 802.1aq SPB
•	 RFC 5304 IS-IS Cryptographic 
Authentication
•	 RFC 5310 IS-IS Generic Cryptographic   
Authentication
IP Multicast
•	 RFC 1075/draft-ietf-idmr- dvmrp-v3-11. 
txt DVMRP
•	 RFC 2365 Multicast
•	 RFC 2710/3019/3810/MLD v2 for IPv6
•	 RFC 2715 PIM and DVMRP 
interoperability
•	 RFC 2933 IGMP MIB
•	 RFC 3376 IGMPv3 (includes IGMP v2/v1)
•	 RFC 3569 Source-specific Multicast 
(SSM)
•	 RFC 3973 PIM-DM
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4541 Considerations for IGMP and 
MLD snooping switches
•	 RFC 4601/5059 PIM-SM
•	 RFC 5015 BiDIR PIM
•	 RFC 5060 PIM MIB
•	 RFC 5240 PIM Bootstrap Router MIB
•	 RFC 5132 Multicast Routing MIB
IPv6
•	 RFC 1981 Path MTU Discovery
•	 RFC 2460 IPv6 Specification
•	 RFC 2464 IPv6 over Ethernet
•	 RFC 2465 MIB for IPv6: Textual 
Conventions (TC) and General Group
•	 RFC 2466 MIB for IPv6: ICMPv6 Group
•	 RFC 2711 Router Alert Option
•	 RFC 3056 6to4 Tunnels RFC 3315 
Dynamic Host Configuration Protocol for 
IPv6 (DHCPv6)
•	 RFC 3484 Default Address Selection
•	 RFC 3493/2553 Basic Socket API
•	 RFC 3542/2292 Advanced Sockets API
•	 RFC 3587/2374 Global Unicast Address 
Format
•	 RFC 3595 TC for IPv6 Flow Label
•	 RFC 3596/1886 DNS for IPv6
•	 RFC 4007 Scoped Address
•	 RFC 4022/2452 MIB for IPv6 TCP
•	 RFC 4113/2454 MIB for IPv6 UDP
•	 RFC 4193 Unique Local Addresses
•	 RFC 4213/2893 Transition Mechanisms
•	 RFC 4291/3513/2373 Addressing 
Architecture (uni/any/multicast)
•	 RFC 4293 Management Information 
BASE for the Internet Protocol (IP)
•	 RFC 4301/2401 Security Architecture
•	 RFC 4302/2402 IP Authentication 
Header
•	 RFC 4303/2406 IP Encapsulating 
Security Payload (ESP)
•	 RFC 4308 Cryptographic Suites for IP 
Security Architecture (IPsec)
•	 RFC 4443/2463 ICMPv6
•	 RFC 4861/2461 Neighbor Discovery
•	 RFC 4862/2462 Stateless Address 
Autoconfiguration
•	 RFC 5095 Deprecation of type 0 routing 
headers in IPv6
Manageability
•	 RFC 854/855 Telnet and Telnet options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1 and SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP v2 MIB
•	 RFC 1215 Convention for SNMP Traps
•	 RFC 1573/2233/2863 Private Interface 
MIB RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload in 
HTML
•	 RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from Forms: 
multipart/form-data
•	 RFC 2396 Uniform Resource Identifiers 
(URI): Generic Syntax

<<<PAGE 552>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 6900
•	 RFC 2570-2576/3411-3415 SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3 MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 4122 A Universally Unique Identifier 
(UUID) URN namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251/4418 Secure Shell Protocol 
Architecture with UMAC Message 
Authentication
•	 RFC 4252/4253 The Secure Shell (SSH) 
Authentication Protocol and Transport 
Layer Protocol
•	 RFC 4502 Remote Monitoring 
Management Information BASE Version 2
•	 RFC 4627 JavaScript Object Notation 
(JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP Status Codes
Security
•	 RFC 1321 MD5
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC  2138/2865/2868/3575/2618 
RADIUS Authentication and Client MIB
•	 RFC  2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 3162 RADIUS and IPv6
•	 RFC 4301 Security Architecture for IP
•	 RFC  1826/1827/4303/4305 
Encapsulating Payload (ESP) and crypto 
algorithms
•	 RFC 2560 X.509 Internet Public Key 
Infrastructure Online Certificate Status 
Protocol – OCSP
•	 RFC 2986 PKCS #10: Certification 
Request Syntax Specification Version 1.7
•	 RFC 3268 Advanced Encryption 
Standard (AES) Cipher suites for 
Transport Layer Security (TLS)
•	 RFC 4346 The Transport Layer Security 
(TLS) Protocol Version 1.1
•	 RFC 5246 The Transport Layer Security 
(TLS) Protocol Version 1.2
•	 RFC 5280 Internet X.509 Public Key 
Infrastructure Certificate and Certificate 
Revocation List (CRL) Profile
•	 RFC 6125 Representation and 
Verification of Domain-based Application 
Service Identity with PKI
•	 Draft-ietf-radext-radsec-12 TLS 
encryption for RADIUS
QoS
•	 RFC 896 Congestion Control
•	 RFC 1122 Internet Hosts
•	 RFC  2474/2475/2597/3168/3246 
DiffServ
•	 RFC 3635 Pause Control
•	 RFC 2697 Single Rate Three Color 
Marker (srTCM)
•	 RFC 2698 Two Rate Three Color Marker 
(trTCM)
Others
•	 RFC 791/894/1024/1349 IP and IP/
Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB RFC 826 
ARP
•	 RFC 919/922 Broadcasting Internet 
Datagram
•	 RFC 925/1027 Multi-LAN ARP/ Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 Bootstrap Protocol (BOOTP)
•	 RFC 1151 Remote Desktop Protocol 
(RDP)
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 Network Time Protocol 
(NTP) v3 and Simple NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 Classless Inter- Domain 
Routing (CIDR)
•	 RFC 1541/1542/2131/3396/ 3442 DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/ BOOTP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 2338/3768/2787 VRRP and MIB
•	 RFC 2581 TCP Congestion Control
•	 RFC 3021 Using 31-bit prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
•	 IETF draft “IP/IPVPN services with IEEE 
802.1aq SPB networks”
Software Defined Networking (SDN)
•	 RFC 7348 Virtual eXtensible Local Area 
Network (VXLAN)
Product matrix
Feature/Model
OS6900-V72
OS6900-C32
Port count
72 (48 SFP28 and 6 QSFP28)
32 (QSFP28)
Expansion slots
N/A
N/A
Out-of-band Ethernet port
1
1
USB port
1
1
Console port
1
1
Primary slide-in PSU slot
1
1
Backup slide-in PSU slot
1
1
Redundant fans
5+1
5+1
CPU Model
Intel Atom® C2538
Intel Atom® C2538
CPU Frequencies/Type
2.4GHz/quad-core
2.4GHz/quad-core
Flash Storage
16 GB
16 GB
RAM
16 GB
16 GB

<<<PAGE 553>>>
7
Datasheet 
Alcatel-Lucent OmniSwitch 6900
Feature/Model
OS6900-V72
OS6900-C32
Data buffer
16 MB
16 MB
Max switching
3.6 Tb/s
6.4 Tb/s
Capacity
Non-blocking
Non-blocking
Forwarding rate*
2678 Mpps
4761 Mpps
Latency
<600 ns
<600 ns
Power consumption*
330 W
360 W
Heat Dissipation
1125 Btu/h
1228 Btu/h
Mean time Between failures (MTBF) with AC 
power Supply
377,998 h
517,875 h
MTBF with DC power supply
377,998 h
517,875 h
Width
43.8 cm (17.26 in)
43.8 cm (17.26 in)
Depth
51.5 cm (20.27 in)
51.5 cm (20.27 in)
Height
4.4 cm (1.73 in.)
4.4 cm (1.73 in.)
Weight (chassis & fan)
6.7 kg (14.77 lb)
6.6 kg (14.55 lb)
Shipping Weight (fully populated***)
10 kg (22.04 lb)
10.5 kg (23.06 lb)
Operating emperature Front-to-rear Airflow
0°C to 45°C (32°F to 113°F) 55°C Shutdown
0°C to 45°C (32°F to 113°F) 55°C Shutdown
Operating temperature Rear-to-Front Airflow 
0°C to 45°C (32°F to 113°F) 55°C shutdown
0°C to 45°C (32°F to 113°F) 55°C shutdown
Storage Temperature
-10°C to 70°C (14°F to 158°F)
-10°C to 70°C (14°F to 158°F)
Humidity (operating)
5% to 95% non-condensing
5% to 95% non-condensing
Humidity (storage)
5% to 95% non-condensing
5% to 95% non-condensing
* Forwarding rate in table above are rounded values based on 64-byte packets.
** Maximum power consumption under full L2 traffic load includes a fan tray, two power supplies, transceivers; optional plug-in modules not included.
*** Shipping weight includes fully populated chassis with fan tray, two power supplies and all accessories; transceivers not included. 
Product matrix (Continued)
Feature/Model
OS6900X24
OS6900T24
OS6900X48
OS6900T48
OS6900X48E
OS6900V48
OS6900C32E
Port count
26 SFP+ and  
2 QSFP28
24 10GBASE-T, 
2 SFP+ and  
2 QSFP28
48 SFP+ and  
6 QSFP28
48 10GBASE-T 
and 6 QSFP28
40 SFP+, 
8 SFP28 and  
4 QSFP28
48 SFP28 and  
8 QSFP28
32 (QSFP28)
Out-of-band  
Ethernet port
1
1
1
1
1
1
1
USB port
1
1
1
1
1
1
1
Console port
1
1
1
1
1
1
1
Primary slide-in 
PSU 
1
1
1
1
1
1
1
Backup slide-in 
PSU
1
1
1
1
1
1
1
Redundant fans
4+1
4+1
4+1
4+1
5+1
5+1
5+1
CPU Model 
Intel Atom® 
C3558
Intel Atom® 
C3558
Intel Atom® 
C3558
Intel Atom® 
C3558
Intel Atom® 
C3558 
Intel Xeon®   
D-1518
Intel Xeon®   
D-1518 
CPU 
Frequencies/
Type
2.2GHz/ 
quad-core 
2.2GHz/ 
quad-core
2.2GHz/ 
quad-core
2.2GHz/ 
quad-core
2.2GHz/ 
quad-core
2.2GHz/ 
quad-core
2.2GHz/ 
quad-core
Flash Storage 
32GB
32GB
32GB
32GB
32GB
32GB
32GB
SDRAM
8 GB
8 GB
8 GB
8 GB
8 GB
16 GB
16 GB
Data buffer
32 MB
32 MB
32 MB
32 MB
32 MB
32 MB
32 MB

<<<PAGE 554>>>
8
Datasheet 
Alcatel-Lucent OmniSwitch 6900
Feature/Model
OS6900X24
OS6900T24
OS6900X48
OS6900T48
OS6900X48E
OS6900V48
OS6900C32E
Max switching
1.12 Tb/s
1.12 Tb/s
2.16 Tb/s
2.16 Tb/s
2.0 Tb/s
4.0 Tb/s
6.4 Tb/s
Capacity
Non-blocking
Non-blocking
Non-blocking
Non-blocking
Non-blocking
Non-blocking
Non-blocking
Forwarding 
rates*
833 Mpps
833 Mpps
1607 Mpps
1607 Mpps
1488 Mpps
2976 Mpps
4761 Mpps
Latency
<650 ns
<650 ns
<650ns
<650 ns
<650 ns
<600 ns
<600 ns
Power 
consumption**
219 W
222 W
356 W
323 W
460 W
550 W
360 W
Heat Dissipation
747 Btu/h
757 Btu/h
1214 Btu/h
1101 Btu/h
1568 Btu/h
1876 Btu/h
1228 Btu/h
Mean time 
Between failures 
(MTBF) with AC 
power Supply
384,636 h
384,636 h
384,636 h
372,562 h
319,364 h
203,816 h
371,983 h
MTBF with DC 
power supply
385,000 h
385,000 h
385,000 h
385,000 h
317,286 h
208,537 h
382,763 h
Width
44.3 cm   
(17.42 in)
44.3 cm   
(17.42 in)
44.3 cm   
(17.42 in)
44.3 cm    
(17.42 in)
43.8 cm      
(17.26 in)
43.8 cm   
(17.26 in)
43.8 cm      
(17.26 in)
Depth
47.33 cm 
(18.63 in.)
47.33 cm 
(18.63 in.)
47.33 cm 
(18.63 in.)
47.33 cm 
(18.63 in.)
51.5 cm      
(20.27 in)
53.6 cm    
(21.1 in)
51.5 cm   (20.27 
in)
Height
4.4 cm  
(1.73 in.)
4.4 cm 
(1.73 in.)
4.4 cm  
(1.73 in.)
4.4 cm  
(1.73 in.)
4.4 cm  
(1.73 in.)
4.4 cm 
(1.73 in.)
4.4 cm  
(1.73 in.)
Weight (chassis 
& fan)
6.663 kg 
(14.68 lb)
6.663 kg  
(14.68 lb)
6.663 kg 
(14.68 lb)
7.438 kg  
(16.39 lb)
7.150 kg    
(15.76 lb)
7.375 kg  
(16.25 lb)
6.663 kg  
(14.55 lb)
Shipping 
weight***
10.48 kg  
(23.10 lb)
10.7 kg    
(23.58 lb)
10.48 kg  
(23.10 lb)
10.7 kg    
(23.58 lb)
10.5 kg       
(23.14 lb)
11.35 kg 
(25.02 lb)
10.48       (23.10 
lb)
Operating 
Temperature
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
Front-to-rear 
Airflow
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
Operating 
Temperature
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C  
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
0°C to 45°C 
(32°F to113°F)
Rear-to-front 
Airflow
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
55°C shutdown
Storage 
Temperature
-10°C to 70°C 
(14°F to 158°F)
-10°C to 70°C 
(14°F to 158°F)
-10°C to 70°C 
(14°F to 158°F)
-10°C to 70°C 
(14°F to 158°F)
-10°C to 70°C 
(14°F to 158°F)
-10°C to 70°C 
(14°F to 158°F)
-10°C to 70°C 
(14°F to 158°F)
Humidity 
(operating)
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
Humidity 
(storage)
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
5% to 95%   
non-condensing
* Forwarding rate in table above are rounded values based on 64-byte packets.
** Maximum power consumption under full L2 traffic load includes a fan tray, two power supplies, transceivers; optional plug-in modules not included.
*** Shipping weight includes fully populated chassis with fan tray, two power supplies and all accessories; transceivers not included.

<<<PAGE 555>>>
9
Datasheet 
Alcatel-Lucent OmniSwitch 6900
Power supplies
All OmniSwitch 6900 models support 1+1 redundant, hot-swappable AC and DC power supplies. The primary and 
backup power supply units are internal, but removable to allow for easier maintenance and replacement. There is 
no service interruption when a new power supply is installed or an old one replaced. All OS6900 models ship with 
two redundant power supply units. 
Power Supply units OS6900C are used to power OS6900-V72, C32, C32E, X48E and V48. 
PS models
OS6900C-BP-F
OS6900C-BP-R
OS6900C-BPD-F
OS6900C-BPD-R
Description
Modular 650W AC backup 
power supply with front-to-
back cooling.
Modular 650W AC backup 
power supply with back-to-
front cooling. 
Modular 650W DC backup 
power supply with front-to-
back cooling.
Modular 650W DC backup 
power supply with back-to-
front cooling.
Dimensions
50.5 mm x 310.2 mm x 
40 mm (1.99 in x 12.2 in x 
1.58 in.)
50.5 mm x 310.2 mm x 
40mm (1.99 in x 12.2 in x 
1.58 in.)
50.5 mm x 310.2 mm x  
40 mm (1.99 in x 12.2 in x 
1.58 in.)
50.5 mm x 310.2 mm x 
40 mm (1.99 in x 12.2 in x 
1.58 in.)
Weight
0.983 kg (2.16 lb.)
0.983 kg (2.16 lb.)
0.983 kg (2.16 lb.)
0.983 kg (2.16 lb.)
Input current/ 
intensity
100–240VAC, 50-60Hz/10–
5A or 8.2-3.5A or 7.8- 3.8A
100–240VAC, 50-60Hz/10–5A 
or 8.2-3.5A or 7.8- 3.8A
36-72VDC/25-11A
36-72VDC/25-11A
Power Rating
650W
650W
48VDC, 650 Watts
48VDC, 650 Watts
Fans
1
1
1
1
Power Supply units OS6900X are used to power OS6900X48,T48 and OS6900X24, T24.
PS models
OS6900X-BP-F
OS6900X-BP-R
OS6900X-BPD-F
OS6900X-BPD-R
Description
Modular 400W AC backup 
power supply with front-to-
back cooling. 
Modular 400W AC backup 
power supply with back-to-
front cooling.
Modular 400W DC backup 
power supply with front-to-
back cooling.
Modular 400W DC backup 
power supply with back-to-
front cooling. 
Dimensions
50.5 mm x 310.2 mm x 
40 mm (1.99 in x 12.2 in x 
1.58 in.)
50.5 mm x 310.2 mm x 40 
mm (1.99 in x 12.2 in x 1.58 
in.)
50.5 mm x 310.2 mm x  
40 mm (1.99 in x 12.2 in x 
1.58 in.)
50.5 mm x 310.2 mm x  
40 mm (1.99 in x 12.2 in x 
1.58 in.)
Weight
0.983 kg (2.16 lb.)
0.983 kg (2.16 lb.)
0.983 kg (2.16 lb.)
0.983 kg (2.16 lb.)
Input current/ 
intensity
100–240VAC, 50-60Hz/6–3A
100–240VAC, 50-60Hz/6–3A
20 to 75 VDC/14-4A (200W 
Output) 36 to 75 VDC/ 14-7A, 
(400W Output)
-20 to -75 VDC/14-4A (200W 
Output) 36 to 75 VDC/ 14-7A, 
(400W Output)
Power Rating
400 Watts
400 Watts
12V/16A, 5V/3A (200W) 
12V/33.3A, 5V/3A (400W)
12V/16A, 5V/3A (200W) 
12V/33.3A, 5V/3A (400W)
Fans
1
1
1
1
Ordering information
OS6900 Switch Family
OS6900X24-F-xx
OS6900-X24C2: 10Gigabit/100Gigabit Ethernet L3 fixed,1RU chassis with 26 SFP+ ports and 2 QSFP28 ports. SFP+ 
ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Front to back cooling. The bundle ships with dual AC 
power supplies, country specific power cord, user manuals access card and rack mounts. (-xx to be replaced with the 
country-specific power cord code, e.g.: -EU for Europe)
OS6900X24-R-xx
OS6900-X24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 26 SFP+ ports and 2 QSFP28 ports. SFP+ 
ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Back to front cooling. The bundle ships with dual AC 
power supplies, country specific power cord, user manuals access card and rack mounts. (-xx to be replaced with the 
country-specific power cord code, e.g.: -EU for Europe)
OS6900X24D-F
OS6900-X24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 26 SFP+ ports and 2 QSFP28 ports. SFP+ 
ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Front to back cooling. The bundle ships with dual DC 
power supplies, user manuals access card and rack mounts. (-xx to be replaced with the country-specific power cord 
code, e.g.: -EU for Europe)

<<<PAGE 556>>>
10
Datasheet 
Alcatel-Lucent OmniSwitch 6900
OS6900 Switch Family
OS6900X24D-R
OS6900-X24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 26 SFP+ ports and 2 QSFP28 ports. SFP+ 
ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Back to front cooling. The bundle ships with dual DC 
power supplies, user manuals access card and rack mounts. (-xx to be replaced with the country-specific power cord 
code, e.g.: -EU for Europe)
OS6900T24-F-xx
OS6900-T24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 24 10GBaseT, 2 SFP+ ports and 2 QSFP28 
ports. SFP+ and 10GBaseT ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Front to back cooling. The 
bundle ships with dual AC power supplies, country specific power cord, user manuals access card and rack mounts.    
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900T24-R-xx
OS6900-T24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 24 10GBaseT, 2 SFP+ ports and 2 QSFP28 
ports. SFP+ and 10GBaseT ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Back to front cooling. The 
bundle ships with dual AC power supplies, country specific power cord, user manuals access card and rack mounts.    
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900T24D-F
OS6900-T24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 24 10GBaseT, 2 SFP+ ports and 2 QSFP28 
ports. SFP+ and 10GBaseT ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Front to back cooling. The 
bundle ships with dual DC power supplies, user manuals access card and rack mounts.
OS6900T24D-R
OS6900-T24C2: 10Gigabit/100Gigabit Ethernet L3 fixed, 1RU chassis with 24 10GBaseT, 2 SFP+ ports and 2 QSFP28 
ports. SFP+ and 10GBaseT ports operate as 1/10GE. QSFP28 ports operate as 100/40GE. Back to front cooling. The 
bundle ships with dual DC power supplies, user manuals access card and rack mounts.
OS6900X48-F-xx
0S6900-X48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
SFP+ ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports support 
splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Front to Rear cooling. The 
chassis includes two 400W AC power supplies. The bundle ships with user manuals access card and rack mounts.    
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900X48-R-xx
0S6900-X48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
SFP+ ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports support 
splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Rear to Front cooling. The 
chassis includes two 400W AC power supplies. The bundle ships with user manuals access card and rack mounts.    
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900X48D-F
0S6900-X48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
SFP+ ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports support 
splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Front to Rear cooling. The 
chassis includes two modular DC power supplies. The bundle ships with user manuals access card and rack mounts.
OS6900X48D-R
0S6900-X48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
SFP+ ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports support 
splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Rear to Front cooling. The 
chassis includes two modular DC power supplies. The bundle ships with user manuals access card and rack mounts.
OS6900T48-F-xx
0S6900-T48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
10GBASET ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports 
support splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Front to Rear 
cooling. The chassis includes two 400W AC power supplies. The bundle ships with user manuals access card and rack 
mounts.    (-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900T48-R-xx
0S6900-T48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
10GBASET ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports 
support splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Rear to Front 
cooling. The chassis includes two 400W AC power supplies. The bundle ships with user manuals access card and rack 
mounts.    (-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900T48D-F
0S6900-T48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
10GBASET ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports 
support splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Front to Rear 
cooling. The chassis includes two modular DC power supplies. The bundle ships with user manuals access card and 
rack mounts.
OS6900T48D-R
0S6900-T48C6: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10G 
10GBASET ports and 6 40/100G QSFP28 ports. All QSFP28 ports operate as single 40/100GE port and 2 ports 
support splitter mode to 4x10GE or 4x25GE. Console and Ethernet management ports are RJ45. Rear to Front 
cooling. The chassis includes two modular DC power supplies. The bundle ships with user manuals access card and 
rack mounts.

<<<PAGE 557>>>
11
Datasheet 
Alcatel-Lucent OmniSwitch 6900
OS6900 Switch Family
OS6900V48-F-xx
OS6900-V48C8: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10/25G 
SFP28 ports and 8 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. Console 
and Ethernet management ports are RJ45. Front to Rear cooling. The chassis includes two 650W AC power supplies. 
The bundle ships with user manuals access card and rack mounts.  (-xx to be replaced with the country-specific 
power cord code, e.g.: -EU for Europe)
OS6900V48-R-xx
OS6900-V48C8: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10/25G 
SFP28 ports and 8 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. Console 
and Ethernet management ports are RJ45. Rear to Front cooling. The chassis includes two 650W AC power supplies. 
The bundle ships with user manuals access card and rack mounts. (-xx to be replaced with the country-specific power 
cord code, e.g.: -EU for Europe)
OS6900V48D-F
OS6900-V48C8: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10/25G 
SFP28 ports and 8 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. Console 
and Ethernet management ports are RJ45. Front to Rear cooling. The chassis includes two modular DC power 
supplies. The bundle ships with user manuals access card and rack mounts.
OS6900V48D-R
OS6900-V48C8: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 1/10/25G 
SFP28 ports and 8 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. Console 
and Ethernet management ports are RJ45. Rear to Front cooling. The chassis includes two modular DC power 
supplies. The bundle ships with user manuals access card and rack mounts.
OS6900X48E-F-xx
OS6900-X48C4E: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 40 1/10G 
SFP+ ports, 8 10/25G SFP28 ports and 4 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port 
or Quad- 10/25GE. Provides MACsec on all ports. Front-to-back cooling. The chassis includes two 650W AC power 
supplies. The bundle ships with a country-specific power cord, user manuals access card, and rack mounts. (-xx to be 
replaced with the country- specific power cord code, e.g.: -EU for Europe)
OS6900X48E-R-xx
OS6900-X48C4E: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 40 1/10G 
SFP+ ports, 8 10/25G SFP28 ports and 4 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port 
or Quad- 10/25GE. Provides MACsec on all ports. Back-to-front cooling. The chassis includes two 650W AC power 
supplies. The bundle ships with a country-specific power cord, user manuals access card, and rack mounts. (-xx to be 
replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900X48E-D-F
OS6900-X48C4E: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 40 1/10G 
SFP+ ports, 8 10/25G SFP28 ports and 4 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or 
Quad- 10/25GE. Provides MACsec on all ports. Front-to-back cooling. The chassis includes two modular DC power 
supplies. The bundle ships with a user manuals access card, and rack mounts.
OS6900X48E-D-R
OS6900-X48C4E: 10Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 40 1/10G 
SFP+ ports, 8 10/25G SFP28 ports and 4 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or 
Quad- 10/25GE. Provides MACsec on all ports. Back-to-front cooling. The chassis includes two modular DC power 
supplies. The bundle ships with a user manuals access card, and rack mounts.
OS600C32E-F-xx
OS6900C32E: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Front-to-back cooling. The chassis includes two 650W AC 
power supplies. The bundle ships with a country-specific power cord, user manuals access card, and rack mounts. 
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900C32E-R-xx
OS6900C32E: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Back-to-front cooling. The chassis includes two 650W AC 
power supplies. The bundle ships with a country-specific power cord, user manuals access card, and rack mounts. 
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900C32E-D-F
OS6900C32E: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Front-to-back cooling. The chassis includes two modular DC 
power supplies. The bundle ships with a user manuals access card, and rack mounts.
OS6900C32E-D-R
OS6900C32E: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Back-to-front cooling. The chassis includes two modular DC 
power supplies. The bundle ships with a user manuals access card, and rack mounts.
OS6900-V72-F-xx
OS6900-V72: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 10/25G 
SFP28 ports and 6 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. Console 
and Ethernet management ports are RJ45. Front to Rear cooling. The chassis includes two 650W AC power supplies. 
The bundle ships with user manuals access card and rack mounts. (-xx to be replaced with the country-specific power 
cord code, e.g.: -EU for Europe)

<<<PAGE 558>>>
12
Datasheet 
Alcatel-Lucent OmniSwitch 6900
OS6900 Switch Family
OS6900-V72-R-xx
OS6900-V72: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 10/25G 
SFP28 ports and 6 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. Console 
and Ethernet management ports are RJ45. Rear to Front cooling. The chassis includes two 650W AC power supplies. 
The bundle ships with user manuals access card and rack mounts. (-xx to be replaced with the country-specific power 
cord code, e.g.: -EU for Europe)
OS6900-V72D-F
OS6900-V72: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 10/25G 
SFP28 ports and 6 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE. 
Console and Ethernet management ports are RJ45. Front to Rear cooling. The chassis includes two modular DC 
power supplies. The bundle ships with user manuals access card and rack mounts.
OS6900-V72D-R
OS6900-V72: 25Gigabit/100Gigabit Ethernet L3 fixed configuration chassis in a 1RU form factor with 48 10/25G 
SFP28 ports and 6 40/100G QSFP28 ports. QSFP28 ports operate as single 40/100GE port or Quad-10/25GE.  
Console and Ethernet management ports are RJ45. Rear to Front cooling. The chassis includes two modular DC 
power supplies. The bundle ships with user manuals access card and rack mounts.
OS600-C32-F-xx
OS6900-C32: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Front-to-back cooling. The chassis includes two 650W AC 
power supplies. The bundle ships with a country-specific power cord, user manuals access card, and rack mounts. 
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900-C32-R-xx
OS6900-C32: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Back-to-front cooling. The chassis includes two 650W AC 
power supplies. The bundle ships with a country-specific power cord, user manuals access card, and rack mounts. 
(-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900-C32D-F
OS6900-C32: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Front-to-back cooling. The chassis includes two modular  
DC power supplies. The bundle ships with a user manuals access card, and rack mounts.
OS6900-C32D-R
OS6900-C32: 100 Gb Ethernet L3 fixed configuration chassis in a 1RU form factor with 32 QSFP28 ports. Ports 
operate as single 40/100GigE port or Quad-10/25GigE. Back-to-front cooling. The chassis includes two modular  
DC power supplies. The bundle ships with a user manuals access card, and rack mounts.
OS6900 Backup power supplies 
OS6900C-BP-F-xx
Modular 650W AC backup power supply. Front-to-back cooling. Provides system power to one OS6900-V72, C32, 
X48C4E or V48C8 switch; (-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900C-BP-R-xx
Modular 650W AC backup power supply. Back-to-front cooling. Provides system power to one OS6900-V72, C32, 
X48C4E or V48C8 switch; (-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900C-BPD-F
Modular 650W DC backup power supply. Front-to-back cooling. Provides backup system power to one OS6900-V72, 
C32, X48C4E or V48C8 switch.
OS6900C-BPD-R
Modular 650W DC backup power supply. Back-to-front cooling. Provides backup system power to one OS6900-V72, 
C32, X48C4E or V48C8 switch.
OS6900X-BP-F-xx
Modular 650W AC backup power supply. Front-to-back cooling. Provides system power to one OS6900-V72, C32, 
X48C4E or V48C8 switch; (-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900X-BP-R-xx
Modular 400W AC backup power supply. Back-to-front cooling. Provides system power to one OS6900-X48C6 or 
T48C6 switch. (-xx to be replaced with the country-specific power cord code, e.g.: -EU for Europe)
OS6900X-BPD-F
Modular 400W DC backup power supply. Front-to-back cooling. Provides system power to one OS6900-X48C6 or 
T48C6 switch.
OS6900X-BPD-R
Modular 400W DC backup power supply. Back-to-front cooling. Provides system power to one OS6900-X48C6 or 
T48C6 switch.
OS6900 Fan trays
OS6900C-FTKIT-F
Replacement fan tray kit for OS6900-V72, OS6900-C32 and OS6900-X48E. Front-to-back cooling, the kit contains  
6 fan tray units.
OS6900C-FTKIT-R
Replacement fan tray kit for OS6900-V72, OS6900-C32 and OS6900-X48E. Back-to-front cooling, the kit contains  
6 fan tray units.
OS6900X-FTKIT-F
Replacement fan tray kit for OS6900X48/T48 and OS6900X24/T24. Front-to-back cooling, the kit contains 5 fan  
tray units.
OS6900X-FTKIT-R
Replacement fan tray kit for OS6900X48/T48 and OS6900X24/T24. Back-to-front cooling, the kit contains 5 fan  
tray units.

<<<PAGE 559>>>
13
Datasheet 
Alcatel-Lucent OmniSwitch 6900
OS6900 Switch Family
OS6900V-FTKIT-F
Replacement fan tray kit for OS6900V48. Front-to-back cooling, the kit contains 5 fan tray units.
OS6900V-FTKIT-R
Replacement fan tray kit for OS6900V48. Back-to-front cooling, the kit contains 5 fan tray units.
Transceivers
GigE 
SFP MSA (Multiple Source Agreement) Transceivers
SFP-GIG-SX
1000BASE-SX Gb Ethernet optical transceiver. Typical reach of 300m on 62.5/125µm to 500m on 50/125µm MMF, 
 LC connector.
SFP-GIG-LX
1000BASE-LX Gb Ethernet optical transceiver. Typical reach of 10 km on 9/125µm SMF, LC connector.
SFP-GIG-LH40
1000BASE-LH Gb Ethernet optical transceiver. Typical reach of 40 km on 9/125µm SMF, LC connector.
SFP-GIG-LH70
1000BASE-LH Gb Ethernet optical transceiver. Typical reach of 70 km on 9/125µm SMF, LC connector.
SFP-GIG-EXTND
1000BASE-EXTND Gb Ethernet optical transceiver. Typical reach of 2 km on 50/125µm MMF, LC connector.
GigE 
Bi-Directional SFP MSA (Multiple Source Agreement) Transceivers
SFP-GIG-BX-U
1000BASE-BX 10 Gb Ethernet optical transceiver. Bi-Directional typical reach of 10 km SMF, LC connector, designed to 
be used with SFP-GIG-BX-D
SFP-GIG-BX-U20
1000BASE-BX 10 Gb Ethernet optical transceiver. Bi-Directional typical reach of 20 km SMF, LC connector, designed to 
be used with SFP-GIG-BX-D20
SFP-GIG-BX-U40
1000BASE-BX 10 Gb Ethernet optical transceiver. Bi-Directional typical reach of 40 km SMF, LC connector, designed to 
be used with SFP-GIG-BX-D40
SFP-GIG-BX-D
1000BASE-BX 10 Gb Ethernet optical transceiver. Bi-Directional typical reach of 10 km SMF, LC connector, designed to 
be used with SFP-GIG-BX-U
SFP-GIG-BX-D20
1000BASE-BX 10 Gb Ethernet optical transceiver. Bi-Directional typical reach of 10 km SMF, LC connector, designed to 
be used with SFP-GIG-BX-U20
SFP-GIG-BX-D40
1000BASE-BX 10 Gb Ethernet optical transceiver. Bi-Directional typical reach of 10 km SMF, LC connector, designed to 
be used with SFP-GIG-BX-U40
10 GigE 
SFP+ Transceivers
SFP-10G-T
10GBASE-T Ethernet transceiver, RJ45 connector.
SFP-10G-C60CM
10 Gb direct attached copper cable, 60 cm, SFP+.
SFP-10G-C1M
10 Gb direct attached copper cable, 1 m, SFP+.
SFP-10G-C3M
10 Gb direct attached copper cable, 3 m, SFP+.
SFP-10G-C7M
10 Gb direct attached copper cable, 7 m, SFP+.
SFP-10G-SR
10GBASE-SR optical transceiver (SFP+). Typical reach of 300 m on 850 nm wavelength (nominal) MMF, LC connector. 
SFP-10G-LR
10BASE-LR optical transceiver. Typical reach of 10 km on SMF 1310 nm, LC connector.
SFP-10G-ER
10BASE-ER optical transceiver. Typical reach of 40 km on SMF 1550 nm, LC connector.
SFP-10G-ZR
10BASE-ZR optical transceiver. Typical reach of 80 km on SMF 1550 nm, LC connector.
SFP-10G-LRM
10BASE-LRM optical transceiver. Typical reach of ~220 m on MMF 1310 nm, LC connector. 
SFP-10G-GIG-SR
Dual speed 10BASE-SR/SW, 1000BASE-SX optical transceiver. Typical reach @ 1G on OM3 ~300 m; @ 10G on OM3 
~550 m on 850 nm MMF, LC connector.
SFP-10G-GIG-LR
Dual speed 10BASE-LR/LW, 1000BASE-LX optical transceiver. Typical reach @ 1G/10G of 10 km on 1310 nm SMF,  
LC connector.
10 GigE 
Bi-Directional SFP MSA (Multiple Source Agreement) Transceivers
SFP-10G-BX-D
10GBASE-LR optical transceiver. Bi-Directional typical reach of 10 km SMF, LC connector, designed to be used with 
SFP-10G-BX-U
SFP-10G-BX-U
10GBASE-LR optical transceiver. Bi-Directional typical reach of 10 km SMF, LC connector, designed to be used with 
SFP-GIG-BX-D
10 GigE 
CWDM - DWDM SFP+ Transceivers
SFP-10G-CWDM
10GBASE-ER/EW optical CWDM transceiver SFP MSA, SFF-8472/8431/8432. Typical reach of 40 km on SMF 1551 nm, 
LC connector.
SFP-10G-24DWD80
10GBASE-ZR optical DWDM transceiver 802.3ae. Typical reach of 80 km on SMF 1558.17 nm, LC connector.

<<<PAGE 560>>>
14
Datasheet 
Alcatel-Lucent OmniSwitch 6900
OS6900 Switch Family
25 GigE 
SFP28 Transceivers
SFP-25G-SR
25GBASE-SR, CPRI 25G, OTU4 optical transceiver. Typical reach of 70 m on OM3 and 100 m on OM4, MMF 850 nm, 
LC connector.
SFP-25G-CLR
25GBASE-LR, CPRI 25G, OTU4 optical transceiver. Typical reach of 2 km on SMF 1310 nm, LC connector.
SFP-25G-LR
25GBASE-LR, optical transceiver. Typical reach of 10 km on SMF 1310 nm, LC connector.
SFP-25G-A20M
25 GigE Direct Attached, Active Optical Cable length of 20 m. 
SFP-25G-C1M
25 GigE Direct Attached, Copper Cable length of 1 m. 
SFP-25G-C3M
25 GigE Direct Attached, Copper Cable length of 3 m. 
SFP-25G-C5M
25 GigE Direct Attached, Copper Cable length of 5 m. 
40 GigE 
QSFP+ Transceivers
QSFP-40G-SR
40GBASE-SR4, Four Channel optical transceiver. Typical reach of 100 m on OM3 and 150 m on OM4, MMF 850 nm, 
MPO connector.
QSPF-40G-SR-BD
40GBASE-SR4, Dual Channel optical transceiver. Typical reach of 100 m on OM3 and 150 m on OM4, MMF 850/900 
nm, LC connector. Does not support VFL connections.
QSFP-40G-LR
40GBASE-LR4, Four Channel optical transceiver. Typical reach of 10 km on SMF 1264.5-1277.5, 1284.5-1297.5, 
1304.5-1317.5 and 1324.5-1337.5 nm, LC connector. 
QSFP-40G-ER
40GBASE-LR4, Four Channel optical transceiver. Typical reach of 40 km on SMF 1264.5-1277.5, 1284.5-1297.5, 
1304.5-1317.5 and 1324.5-1337.5 nm, LC connector.
QSFP-40G-LM4
40GBASE-LR4, Four Channel optical transceiver. Typical reach of 140 m on OM3 MMF and 160 m on OM4 MMF, 
1264.5-1277.5, 1284.5-1297.5, 1304.5-1317.5 and 1324.5-1337.5 nm, LC connector.
QSFP-40G-CLR
40GBASE-LR4, Four Channel optical transceiver. Typical reach of 2 km on SMF 1264.5-1277.5, 1284.5-1297.5, 1304.5-
1317.5 and 1324.5-1337.5 nm, LC connector.
QSF-4x10G-SR
40GBASE-SR4, Four Channel Splitter optical transceiver, connects a single 40G QSFP+ port to four 10G SFP+ ports. 
Typical reach of 300 m on OM3 and 400 m on OM4, MMF 850 nm, MPO connector.
40 GigE 
QSFP+ Direct Attached Cables 
QSFP-40G-C40CM
40GigE 802.3ab, QSFP+ MSA, direct attached cable length of 40 cm.
QSFP-40G-C1M
40GigE 802.3ab, QSFP+ MSA, direct attached cable length of 1 m.
QSFP-40G-C3M
40GigE 802.3ab, QSFP+ MSA, direct attached cable length of 3 m.
QSFP-40G-C5M
40GigE 802.3ab, QSFP+ MSA, direct attached cable length of 5 m.
QSFP-4x10G-C1M
40GigE Four Channel Direct Attached Splitter Cable, connects a single QSFP+ port to four 10G SFP+ port, cable 
length 1 m.
QSFP-4x10G-C3M
40GigE Four Channel Direct Attached Splitter Cable, connects a single QSFP+ port to four 10G SFP+ port, cable 
length 3 m.
QSFP-4x10G-C5M
40GigE Four Channel Direct Attached Splitter Cable, connects a single QSFP+ port to four 10G SFP+ port, cable 
length 5 m.
QSFP-40G-PSM4
40GigE Four independent channels optical transceiver, connects a single QSFP+ port to four 10G SFP+ port. Typical 
reach of 2 km on SMF, MPO/MTP connector.
100 GigE 
QSFP28 Transceivers
QSFP-100G-SR4
100GBASE-SR4, Four Channel optical transceiver. Typical reach of 70 m on OM3 and 100 m on OM4, MMF 850 nm, 
MPO12 connector.
QSFP-100G-CLR4
100GBASE-LR4 Lite, Four Channel optical transceiver. Typical reach of 2 Km on SMF 1294.53-1296.59, 1299.02-
1301.09, 1303.54-1305.63, 1308.09-1310.19 nm, LC connector.
QSFP-100G-LR4
100GBASE-LR4, Four Channel optical transceiver. Typical reach of 10 Km on SMF 1294.53-1296.59, 1299.02-1301.09, 
1303.54-1305.63, 1308.09-1310.19 nm, LC connector.
QSFP-100G-ER4
100GBASE-ER4, 4WDM-40, Four Channel optical transceiver. Typical reach of 40 Km on SMF 1294.53-1296.59, 
1299.02-1301.09, 1303.54-1305.63, 1308.09-1310.19 nm, LC connector.
QSFP-100G-CWDM4
100GigE 802.3bm, QSFP28 MSA, Four Channel optical transceiver. Typical reach of 2 km on SMF 1264.5-1277.5, 
1284.5-1297.5, 1304.5-1317.5, 1324.5-1337.5 nm, MPO12 connector.

<<<PAGE 561>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view 
other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trademarks-copyright. All 
other trademarks are the property of their respective owners. The information presented is subject to change without notice. 
Neither ALE Holding nor any of its affiliates assumes any responsibility for inaccuracies contained herein. © Copyright 2022  
ALE International, ALE USA Inc. All rights reserved in all countries. DID20220704EN (October 2022)
OS6900 Switch Family
QSFP-100G-PSM4
100GigE Four independent channels optical transceiver, connects a single QSFP+ port to four 25G SFP28 ports. 
Typical reach of 2 km on SMF, MPO/MTP connector.
100 GigE 
QSFP28 Direct Attached Cables 
QSFP-100G-C1M
100 GigE Four Channel Direct Attached Cable length of 1 m.
QSFP-100G-C3M
100 GigE Four Channel Direct Attached Cable length of 3 m.
QSFP-100G-C5M
100 GigE Four Channel Direct Attached Cable length of 5 m.
QSFP-100G-A20M
100 GigE Direct Attached, Active Optical Cable MMF 20 m.
QSFP-4x25G-C1M
100 GigE Four Channel Direct Attached Splitter Cable, connects a single QSFP28 port to four 25G SFP28 ports,  
length 1 m.
QSFP-4x25G-C3M
100 GigE Four Channel Direct Attached Splitter Cable, connects a single QSFP28 port to four 25G SFP28 ports,  
length 3 m.
QSFP-4x25G-C5M
100 GigE Four Channel Direct Attached Splitter Cable, connects a single QSFP28 port to four 25G SFP28 ports,  
length 5 m.

<<<PAGE 562>>>
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Alcatel-Lucent  
OmniSwitch 9900 Series  
Modular LAN Chassis 
The Alcatel-Lucent OmniSwitch® 9900 series 
Modular LAN chassis platform is a high-capacity, 
high-performance modular Ethernet LAN switch 
that is field-proven in enterprise and data center 
environments. As the OmniSwitch 9900 series 
runs on the Alcatel-Lucent Operating System 
(AOS), a state-of-the-art programmable operating 
system designed for Software-Defined Networking 
(SDN), it delivers uninterrupted network uptime 
with non-stop Layer-2 and Layer-3 forwarding.
The OmniSwitch 9900 is a high density, multi Terabit modular platform. The platform can linearly scale switching 
capacity with virtual chassis technology providing tens of Terabit of aggregate switching capacity. In particular its 
modular design provides investment protection allowing for scaling out with future inline upgrades offering high 
density 1G/2.5G/5G/10G/25G/40G/50G/100G interfaces.
The OmniSwitch 9900 series is ideally suited for enterprise core, aggregation and edge environments. Its 
resilient platform architecture providing control plane and data plane redundancy together with unparalleled 
scalability helps meet demanding resiliency and throughput requirements for evolving enterprises of all sizes.The 
OmniSwitch 9900 series offers a broad range of modules supporting 1 GigE, 10 GigE and 40/100 GigE ports in an  
11-RU chassis form factor, and it offers highest 1 GigE/10GigE port density in its class. 
The OmniSwitch 9900 offers the highest density of Power over Ethernet (PoE) in its class, scaling up to 10800 W 
of inline PoE power. The gigabit and multi-gigabit PoE line card supports 8 ports of HPoE (75 W) and 40 ports of 
802.3at PoE (30 W). All PoE-enabled ports are IEEE 802.3af/at compliant.
The OmniSwitch 9900 leverages an energy-efficient model with leading low power consumption, making it an 
efficient and versatile switch.
The Alcatel-Lucent Enterprise Intelligent Fabric technology is also enabled on the OmniSwitch 9900 Modular LAN 
chassis. The technology brings true network flexibility ensuring business agility. It not only delivers a resilient, high-
capacity infrastructure, but it also delivers automated deployment and self-healing network capabilities to reduce 
overhead in IT operations. The technology platform is built upon standard IEEE protocols and key innovations such 
as Shortest Path Bridging (802.1aq/SPB-M) for bridged and routed services, Multiple VLAN Registration Protocol 
(MVRP), dynamic Virtual Network Profiles (vNP), 802.3ad/802.1AX (LACP) and Auto- Fabric for automatic protocol 
and topology discovery.

<<<PAGE 563>>>
2
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Benefits
•	 Modules provide very low latency for high-performance server clusters and core connectivity over QSFP28, 
QSFP+, SFP+, DAC or CAT 5/6.
•	 Outstanding performance when supporting real-time voice, data, storage and video applications for converged 
scalable networks
•	 Modular slots offer versatility in terms of 100GigE QSFP28, 40 GigE QSFP+, 10 GigE SFP+, 10 G Base-T and 
10/100/1000Base-T ports.
•	 Each QSFP port is capable of operating as 40 GigE or 4x10 GigE.
•	 Each QSFP28 port is capable of operating as 40/100 GigE or 4x10/25 GigE.
•	 Hardware resiliency maximizes uptime for converged mission-critical networks.
•	 Software virtualization, the Chassis Management Module (CMM) control plane and data plane management are 
virtualized and execute as virtual machines, enabling high availability during upgrades and/or during unexpected 
network failures.
•	 The OmniSwitch 9900 virtual chassis further increases system redundancy, resiliency and  
high availability while simplifying deployment, operations and management of the network.
•	 Embedded SDN integration to control virtual network profiles and policy management
•	 Built-in dynamic and automated policy enforcement
•	 Policy enforcement engine fully open for external control through RESTful northbound APIs for automation and 
integration of innovative applications
•	 Out-of-the-box flexible fabric architecture designed to automate and simplify the end-to-end deployment of 
campus, data center, and cloud-based services
•	 Prevents human mistakes by automating standardized and replicable configurations
•	 Prevents host address explosion and flooding with built-in SLA service support at low capital and operating 
costs, and based on interoperable proven standards
•	 Optimizes/simplifies Layer-2 and Layer-3 network designs and reduces administration overhead while 
increasing network capacity with resilient multipath active-active dual homing multi-chassis support
•	 Out-of-the-box Auto-Provisioning to simplify installation and service provisioning
•	 With its advanced PoE capabilities and high density of PoE ports, the OmniSwitch 9900 is ideal for converged 
campus deployments, as it offers deployment flexibility, simplifies the wiring and reduces the time to deploy 
edge devices such as VoIP phones, surveillance cameras, 802.11ac access points, and emerging devices that 
require more than 30 W, such as video displays, a small network switch or a thin virtual desktop infrastructure 
(VDI) client.
•	 Unified Access and application-fluent networks provide simplified network architecture with automated controls 
and enhanced security for both wired and wireless users. Offers enhanced management and security for 
reduced operational complexity costs.
•	 User network profiles add intelligence to the network to automatically adapt as users move around the 
corporation without compromising the security
•	 With its advanced capabilities, the OmniSwitch 9900 brings enhanced performance when supporting real-time 
voice, data and video applications.
•	 Provides consistent and secure user experience when applications and services are accessed from wired or 
wireless end devices
•	 Offers flexible deployment options and enables the network for BYOD deployments and  
zero-touch guest management
•	 Supports dynamic change of authentication (CoA) and enforces traffic remediation  
or restriction for non- compliant devices
•	 Provides control and increased security over corporate data/applications for the mixed personal and corporate 
environment for improved visibility and control for IT
•	 Opens the door for fast deployment of new network services that meet employees’ needs to continuously adopt  
new applications that support the business

<<<PAGE 564>>>
3
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
•	 The support of SDN reassures customers that their investment helps them prepare for the future and enables 
interoperability with third-party solutions. 
Features
•	 Wire-rate non-blocking switching and routing performance for Ethernet at 40/100 GigE, 10/25 GigE and 
10/100/1000 Base-T speeds
•	 High port density in 11-RU.
¬	 Up to 288 10/100/1000Base-T triple speed ports
¬	 Up to 288 1000Base-X ports
¬	 Up to 288 SFP+ ports. Capable of 1 GigE/10 GigE
¬  Up to 288 10 G Base-T ports. Capable of 1 GigE/10 GigE
¬	 Up to 88 1/2.5/5/10 G Base-T ports
¬	 Up to 4 QSFP+ ports. Capable of 40 GigE or 4x10GigE
¬	 Up to 40 QSFP28 ports. Capable of 40/100 GigE or 4x10/25 GigE
•	 Resilient hardware system and highly available virtualized software architecture
•	 Up to two switches can be connected using virtual chassis technology to create a single chassis-like entity with 
up to 480 10 GigE or 576 GigE ports
•	 Integral operating system advanced functions: Quality of Service (QoS), access control lists (ACLs), Layer-2/
Layer-3 switching, virtual LAN (VLAN) stacking and IPv6
•	 Intelligent policy control through OpenFlow 1.3.1/1.0
•	 Hardware virtual routing and forwarding (VRF) support for VRF-lite and IPVPN
•	 Scalable network virtualization architecture with guaranteed Service Level Agreement (SLA) delivery over standard 
Ethernet fabric: Auto-Fabric IP routing for routed backbone and access provisioning, Shortest Path Bridging (SPB) 
for bridging and routed services, Edge Virtual Bridging (EVB), Multiple VLAN Registration Protocol (MVRP)  
and dynamic Virtual Network Profiles (vNP)
•	 Zero-touch provisioning and network automation with out-of-the-box plug- and-play Auto-Fabric for automatic 
protocol and topology discovery. Protocol auto-discovery and self-provisioning works with any Ethernet device 
that supports standard IEEE protocols such as 802.1aq (Shortest Path Bridging Media Access Control, SPBM), 
802.1ak (MVRP), 802.3ad/802.1AX (Link Aggregation Control Protocol, LACP). Auto-Fabric operation extends to 
IP routing protocol provisioning and  IP onboarding.
•	 On PoE-enabled network interface modules:
¬	 IEEE 802.3af and 802.3at compliant PoE of 30 W per port on all ports
¬	 Up to 75 W of PoE (High Power-over- Ethernet, HPoE) per port on first eight ports
¬	 Capacity to deliver 1800 W of PoE power
•	 Advanced Unified Access features providing application fluency in converged campus networks:
¬	 Integrated policy with dynamic User Network Profiles (UNP)
¬	 Extensive security features for network access control (NAC), policy enforcement and attack containment
¬	 Session Initiation Protocol (SIP) fluency to provision and monitor QoS treatment of SIP flows
¬	 AirGroup™ Network Services for Bonjour® speaking devices
•	 Enables deployment of comprehensive and secure bring-your-own-device (BYOD) services in enterprise networks:
¬	 Advanced guest management capabilities
¬	 Device onboarding and automated IEEE 802.1x provisioning
¬	 Device posture/health check and fingerprinting
¬	 Application management
•	 The OmniSwitch 9900 is SDN-ready:
¬	 Comprehensive northbound RESTful API to the entire AOS feature set.
¬	 API offers access to all AOS command line interface (CLI) commands and management information base 
(MIB) structures
¬	 AOS-embedded scripting capabilities supporting Python® and Bash programming
¬	 OpenFlow™ 1.0/1.3
¬	 OpenStack® neutron plugin

<<<PAGE 565>>>
4
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
OmniSwitch 9900 chassis and interface modules
The OmniSwitch 9900 family offers high-performance and very low latency Layer-2/Layer-3 switching. The 
chassis has a 11-RU form factor with four power supply bays and fan trays for front-to- back airflow. Available 
interfaces vary from 100 GigE, 40 GigE, 25 GigE, 1/10 GigE, 1/10G Base-T and 10/100/1000Base-T. The chassis 
management module has built-in 2x 40 GbE ports; each port can also be used as 4x 1/10 GbE with splitter cables. 
The OmniSwitch 9900 supports 1+1 redundant and hot-swappable power supplies. The power supply units are 
internal but removable to allow for easier maintenance and replacement. The OmniSwitch 9900 power supplies 
provide both system power and PoE power. The platform supports power load-sharing for PoE between the power 
supplies providing up to 10800 W of PoE per switch. There is no interruption of service when a new power supply 
is installed or an existing one replaced. The OmniSwitch 9900 allows for maximum flexibility and investment 
protection as customers migrate from 1 GigE and 10 GigE to 40 GigE and 100GigE.
Detailed product features
Simplified manageability
•	 Fully programmable RESTful web 
services interface with XML and 
JavaScript Object Notation (JSON) 
support. API enables access to CLI and 
individual MIB objects
•	 Intuitive CLI in a scriptable Bash 
environment through console, Telnet or 
Secure Shell (SSH) v2 over IPv4/IPv6
•	 Built-in Python engine enables 
automation, providing programmatic 
access of network events with scripted 
controlled actions
•	 Powerful WebView Graphical Web 
Interface through HTTP and HTTPS over 
IPv4/IPv6
•	 Integrated with Alcatel-Lucent 
Enterprise OmniVista® products for 
network management.
•	 Integrated with Alcatel-Lucent 
Enterprise Omnivista® cloud platform 
for cloud based network management.
•	 Full configuration and reporting using 
Simple Network Management Protocol 
(SNMP) v1/2/3  
to facilitate third-party network 
management over IPv4/IPv6
•	 File upload using USB, TFTP, FTP, SFTP or 
SCP using IPv4/IPv6
•	 Multiple microcode image support with 
fallback recovery
•	 Local (on the flash) and remote server 
logging (Syslog): event  
and command logging
•	 Loopback IP address support  
for management per service
•	 Management Virtual Routing  
and Forwarding (VRF) support
•	 Dynamic Host Configuration Protocol 
(DHCP) relay for IPv4/IPv6
•	 IEEE 802.1AB Link Layer Discovery 
Protocol (LLDP)  
with Media Endpoint Discovery  
(MED) extensions
•	 Network Time Protocol (NTP)
•	 DHCPv4 and DHCPv6 server 
Monitoring and troubleshooting
•	 Policy and port-based mirroring (many 
to many)
•	 Remote port mirroring
•	 sFlow v5 and Remote Network 
Monitoring (RMON)
•	 Dying gasp support through  
SNMP and syslog messages
•	 IP tools: ping and trace route 
Unidirectional Link Detection (UDLD)
•	 Digital Diagnostic Monitoring (DDM)
Resiliency and high availability
•	 Unified management, control and 
fabric- mesh virtual chassis technology
•	 1+1 redundant supervisor manager
•	 Virtual chassis In-Service Software 
Upgrade (ISSU)
•	 Smart continuous switching technology
•	 ITU-T G.8032/Y1344 2010: Ethernet  
Ring Protection
•	 IEEE 802.1s Multiple Spanning Tree 
Protocol (MSTP), IEEE 802.1D Spanning 
Tree Protocol  
(STP) and IEEE 802.1w Rapid Spanning 
Tree Protocol (RSTP)
•	 Per-VLAN spanning tree (PVST+) and 
1x1 STP mode
•	 IEEE 802.3ad/802.1AX Link Aggregation 
Control Protocol (LACP) and static link 
aggregation (LAG) groups  
across modules
•	 Virtual Router Redundancy Protocol 
(VRRP) with tracking capabilities
•	 IEEE protocol auto-discovery
•	 Bidirectional Forwarding Detection (BFD)
•	 Redundant and hot-swappable  
power supplies
•	 Hot-swappable fan trays
•	 Built-in CPU protection against 
malicious attacks
•	 Split virtual chassis protection: Auto- 
detection and recovery of virtual chassis 
splitting due  
to Virtual Fabric Link (VFL) failures
•	 Broadcast and multicast storm control 
to avoid degradation in overall  
system performance
Software Defined Networking 
(SDN)
•	 Programmable AOS RESTful API
•	 Fully programmable OpenFlow 1.3.1 and 
1.0 agent for control of native OpenFlow 
and hybrid ports
•	 OpenStack networking plug-in
Advanced security
Network control
•	 AOS secured diversified code solution 
is available on OmniSwitch® 9900, 
hardening it at both the software source 
code and binary executable levels to 
enhance overall network security.
•	 AOS secured diversified code protects 
networks from intrinsic vulnerabilities, 
code exploits, embedded malware, 
and potential back doors that could 
compromise mission- critical operations.
•	 AOS secured diversified code is a 
proactive, defense-in- depth approach 
toward network security that 
continuously defines and implements 
value-add capabilities to address both 
current and future threats.
Access control
•	 AOS Access Guardian framework for 
comprehensive user-policy-based NAC
•	 Autosensing IEEE 802.1X multi-client, 
multi-VLAN support
•	 Media Access Control (MAC)- 
based authentication for  
non-IEEE 802.1X hosts

<<<PAGE 566>>>
5
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
•	 Web-based authentication (captive 
portal): a customizable web portal 
residing on the switch
•	 User Network Profile (UNP) simplifies 
NAC by dynamically providing pre-
defined policy configuration to 
authenticated clients: VLAN,  
ACL, bandwidth
•	 Secure Shell (SSH) with public  
key infrastructure (PKI) support
•	 Terminal Access Controller  
Access-Control System Plus  
(TACACS+) client
•	 Centralized Remote Access Dial-In 
User Service (RADIUS) and Lightweight 
Directory Access Protocol (LDAP) 
administrator authentication
•	 Centralized RADIUS for device 
authentication and network  
access control authorization
•	 Learned Port Security (LPS)  
or MAC address lockdown
•	 ACLs; flow-based filtering in hardware 
(Layer 1 to Layer 4)
•	 DHCP Snooping, DHCP IP and Address 
Resolution Protocol  
(ARP) spoof protection
•	 ARP poisoning detection
•	 IP source filtering as a protective and 
effective mechanism against ARP attacks
•	 LLDP Security mechanism for rogue 
device detection and restriction
•	 BYOD provides on-boarding of guest, 
IT/non-IT issued and silent devices. 
Restriction or remediation of traffic 
from non-compliant devices. Uses 
RADIUS CoA to dynamically enforce 
User Network Profiles based on 
authentication, profiling, posture check 
of devices.
MACSec
•	 Provides secure communication for 
traffic on all ethernet links, using 
MACSec technology
Quality of Service (QoS)
•	 Priority queues: Eight hardware-based 
queues per port
•	 Traffic prioritization: Flow-based QoS
•	 Flow-based traffic policing and 
bandwidth management
•	 32-bit IPv4/128-bit IPv6 non-contiguous 
mask classification
•	 Egress traffic shaping
•	 DiffServ architecture
•	 Congestion avoidance: IEEE 802.3x Flow 
Control (FC)
•	 SIP detection, session monitoring  
and tracking
•	 Provides real-time conversation quality 
information contained in the SIP packets 
concerning packet loss, delay, jitter, 
mean opinion score (MOS), R-Factor in 
real time
•	 SIP profile for QoS, priority tuning for 
end-to-end processing
•	 Multicast DNS Relay: Bonjour protocol 
support for wired AirGroup
•	 LLDP network polices for dynamic 
designation of VLAN-ID and Layer-2/ 
Layer-3 priority for IP phones
•	 Auto-QoS for switch management traffic 
as well as traffic from IP phones 
IPv4 routing
•	 Multiple Virtual Routing and  
Forwarding (VRF)
•	 Static routing with route labeling
•	 Routing Information Protocol (RIP) v1 
and v2
•	 Open Shortest Path First (OSPF) v2 with 
graceful restart
•	 Intermediate System to Intermediate 
System (IS-IS) with graceful restart
•	 Border Gateway Protocol (BGP)  
v4 with graceful restart
•	 Generic Routing Encapsulation (GRE) 
and IP/IP tunneling
•	 Virtual Router Redundancy Protocol 
(VRRPv2)
•	 DHCP relay, including generic User 
Datagram Protocol (UDP) relay
•	 Address Resolution Protocol (ARP)
•	 Policy-based routing and server  
load balancing
•	 DHCPv4 server
•	 IP router port
•	 Export/Import IPv4 routes  
across VRFs
IPv6 routing
•	 Multiple Virtual Routing and Forwarding 
(VRF)
•	 Internet Control Message Protocol 
version 6 (ICMPv6)
•	 Static routing
•	 Routing Information Protocol  
Next Generation (RIPng)
•	 Open Shortest Path First (OSPF) v3 with 
graceful restart
•	 Intermediate System to Intermediate 
System (IS-IS)  
with graceful restart
•	 Multi-Topology IS-IS
•	 BGP v4 multiprotocol extensions for 
IPv6 routing (multiprotocol Border 
Gateway Protocol, MP-BGP)
•	 Graceful restart extensions for OSPF 
and BGP
•	 Virtual Router Redundancy Protocol 
(VRRPv3)
•	 Neighbor Discovery Protocol (NDP)
•	 Policy-based routing and  
server load balancing
•	 DHCPv6 server
•	 Export/Import IPv6 routes  
across VRFs
IPv4/IPv6 multicast
•	 Internet Group Management Protocol 
(IGMP) v1/v2/v3 snooping
•	 Protocol Independent Multicast – 
Sparse- Mode (PIM-SM), Source Specific 
Multicast (PIM-SSM),
•	 Protocol Independent Multicast – 
Dense- Mode (PIM-DM), Bidirectional 
Protocol Independent Multicast  
(PIM-BiDir)
•	 Distance Vector Multicast Routing 
Protocol (DVMRP)
•	 Multicast Listener Discovery (MLD)  
v1/v2 snooping
•	 PIM to DVMRP gateway support
•	 (S,G) and (*,G) forwarding 
Advanced Layer-2 services
•	 Up to 4094 IEEE 802.1Q VLANs
•	 Ethernet services support using IEEE 
802.1ad Provider Bridges (also known as 
Q-in-Q or VLAN stacking)
•	 Fabric virtualization services IEEE 
802.1aq Shortest Path Bridging (SPB-M)
¬	 Ethernet Virtual Connection (EVC) 
support for transparent LAN services 
such as E-LAN, E-Line and E-Tree
¬	 Multipoint Ethernet VPN (EVPN) over 
I-SID service virtualization or  
Q-in-Q tunnels
¬	 Ethernet network-to-network interface 
(NNI) and user network interface (UNI)
¬	 Service Access Point (SAP) profile 
identification
¬	 Service VLAN (SVLAN) and Customer 
VLAN (CVLAN) support
¬	 VLAN translation and mapping 
including CVLAN to SVLAN
¬	 C-tag to S-tag priority mapping
•	 DHCP Option 82: Configurable relay 
agent information
•	 Multicast VLAN Registration  
Protocol (MVRP)
•	 High-availability VLAN (HA-VLAN) for 
Layer-2 clusters such as Microsoft® 
Network Load Balancing (MS-NLB) and 
active-active firewall clusters
•	 Jumbo frame support up to  
9216 bytes
•	 Bridge Protocol Data Unit  
(BPDU) blocking

<<<PAGE 567>>>
6
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
•	 Spanning Tree Protocol (STP) Root 
Guard prevents edge devices from 
becoming STP root nodes
•	 MAC-Forced Forwarding support 
according to RFC 4562
•	 Private VLAN feature for user  
traffic segregation
•	 TR-101 Point-to-Point Protocol over 
Ethernet (PPPoE) Intermediate Agent 
allowing for the PPPoE network  
access method
•	 TACACS+ client allows for authentication 
authorization and accounting (AAA) with 
a remote TACACS+ server
PoE
•	 Dynamic PoE allocation delivers only the 
power needed by the attached device 
up to the total power budget for most 
efficient power consumption
•	 PoE models support Alcatel-Lucent IP 
phones and WLAN access points, as well 
as any IEEE 802.3af-compliant  
end device
•	 Configurable per-port PoE  
priority and max power for  
power allocation
•	 Negotiation for Additional PoE Power 
using LLDP Power-via- 
MDI TLV
Technical specifications
Product specifications and 
measurements
System LEDs
•	 Chassis Backlight (OS9900):  
active Blue
•	 CMM Backlight (OS99-CMM): active Blue
•	 40G: active Green
•	 PRI: Primary active Green/ Secondary 
active Yellow
•	 VC: active Blue
•	 FAB: active Green
•	 PS: active Green
•	 TEMP: active Green
•	 CMM USB Type A: active Green  
link/activity
•	 CMM EMP: active Green link/activity
•	 PWR Save: active Green (reserved for 
future use)
Per-port LEDs
•	 CMM 40G Uplink Mode: First LED active 
Green link/activity
•	 CMM 40G VFL Mode: First LED active 
Blue link/activity
•	 CMM 10G Uplink Mode: All LEDs active 
Yellow link/activity
•	 CMM 10G VFL Mode: All LEDs active 
Blue link/activity
•	 1G: active Green link/activity
•	 1G PoE enabled: active Yellow  
link/activity
•	 10G: active Green link/activity 
Compliance and certifications
EMI/EMC - Commercial
•	 FCC 47 CFR Part 15 Class A
•	 ICES-003 Class A
•	 CE marking for European countries 
(Class A)
•	 EMC Directive 89/336/EEC
•	 EN55022:1998:2006 Class A
•	 EN55024:1998:A1: 2001+A2:2003
•	 EN61000-3-2
•	 EN61000-3-3
•	 EN61000-4-2
•	 EN61000-4-3
•	 EN61000-4-4
•	 EN61000-4-5
•	 EN61000-4-6
•	 EN61000-4-8
•	 EN61000-4-11
•	 CISPR22:1997 (Class A)
•	 VCCI (Class A)
•	 AS/NZS 3548 (Class A)
•	 IEEE 802.3 Hi-Pot requirement and 1.5 
kV surge on data port  
for copper interfaces
Safety agency certifications
•	 IEC 62368-1
•	 US UL 60950
•	 IEC 60950-1:2001; all national deviations
•	 EN 60950-1: 2001; all deviations
•	 CAN/CSA-C22.2 No. 60950-1-03
•	 AS/NZ TS-001 and 60950:2000, Australia
•	 UL-AR, Argentina
•	 UL-GS Mark, Germany
•	 GOST, Russian Federation
•	 EN 60825-1 Laser
•	 EN 60825-2 Laser
•	 CDRH Laser
Federal certifications
•	 FIPS 140-2
•	 Common Criteria EAL2
•	 Common Criteria NDcPP
•	 JITC
•	 Trade Agreements Act
Supported standards
IEEE standards
•	 IEEE 802.1D STP
•	 IEEE 802.1p CoS
•	 IEEE 802.1Q VLANs
•	 IEEE 802.1ab (LLDP)
•	 IEEE 802.1ag (OA&M)
•	 IEEE 802.1ad Provider Bridges Q-in-Q/ 
VLAN stacking
•	 IEEE 802.1ak Multiple VLAN Registration 
Protocol (MVRP)
•	 IEEE 802.1aq Shortest Path  
Bridging (SPB)
•	 IEEE 802.1s MSTP
•	 IEEE 802.1w RSTP
•	 IEEE 802.1X Port-based Network Access 
Control (PNAC).
•	 IEEE 802.3x Flow Control
•	 IEEE 802.3i 10Base-T
•	 IEEE 802.3u Fast Ethernet
•	 IEEE 802.3z 1 GigE
•	 IEEE 802.3ab 1 GBase-T
•	 IEEE 802.3af Power over Ethernet
•	 IEEE 802.3at PoE Plus
•	 IEEE 802.3ac VLAN Tagging
•	 IEEE 802.3ad/802.1AX Link Aggregation
•	 IEEE 802.3ae 10 GigE
•	 IEEE 802.3an 10 GBase-T
•	 IEEE 802.3az Energy Efficient  
Ethernet (EEE)
•	 IEEE 802.3ba 40 GigE
•	 IEEE 802.3bm 40/100 GigE
•	 IEEE 802.3bz 2.5/5 GigE
•	 IEEE 802.1x-2004 
•	 IEEE 802.1ae MAC Security 
•	 IEEE 802.3bm (CAUI-4, 100GBASE-SR4 
clause 95)
•	 IEEE 802.3bj (100Base-KR4  
clause 93, 100GBase-CR4)
•	 IEEE 802.3ba (100GBASE-LR4, 
ER4 clause 88)
•	 IEEE 802.3by 25 Gig Ethernet 
ITU-T recommendations
•	 ITU-T G.8032/Y.1344 2010: Ethernet 
Ring Protection (ERPv2) 
ANSI recommendations
•	 ANSI TIA-1057 LLDP-MED Support
IETF RFCs
IPv4
•	 RFC 2003 IP/IP Tunneling
•	 RFC 2784 GRE Tunneling
•	 RFC 2131 Dynamic Host Configuration 
Protocol (DHCPv4)
•	 RFC 4022/2452 MIB for IPv4 TCP
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4113/2454 MIB for IPv4 UDP
•	 RFC 4292/4293 IPv4 MIBs
OSPF
•	 RFC 1765 OSPF Database Overflow
•	 RFC 1850/2328/4750 OSPF v2 and MIB
•	 RFC 2154 OSPF MD5 Signature
•	 RFC 2370/3630 OSPF Opaque LSA
•	 RFC 3101 OSPF NSSA Option

<<<PAGE 568>>>
7
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
•	 RFC 3623 OSPF Graceful Restart
•	 RFC 2740 OSPFv3 for IPv6
•	 RFC 2740/5340 OSPFv3 for IPv6
•	 RFC 4552 Authentication/Confidentiality 
for OSPFv3
•	 RFC 5187 OSPFv3 Graceful Restart
•	 RFC 5838 MIB for OSPFv3 
RIP
•	 RFC 1058 RIP v1
•	 RFC 1722/1723/2453/1724 RIP v2  
and MIB
•	 RFC 1812/2644 IPv4 Router 
Requirements
•	 RFC 2080 RIPng for IPv6
BGP
•	 RFC 1269/1657/4273 BGP v3  
and v4 MIB
•	 RFC 1403/1745 BGP/OSPF Interaction
•	 RFC 1771-1774/2842/2918/ 
3392/4271 BGP v4
•	 RFC 1965 BGP AS Confederations
•	 RFC 1966 BGP Route Reflection
•	 RFC 1997/1998/4360 BGP  
Communities Attribute
•	 RFC 2042/5396 BGP New Attribute
•	 RFC 2385 BGP MD5 Signature
•	 RFC 2439 BGP Route Flap Damping
•	 RFC 2545 BGP-4 Multiprotocol 
Extensions for IPv6 Routing
•	 RFC 2796 BGP-4 Route Reflection
•	 RFC 2858/4760 Multiprotocol Extensions 
for BGP-4
•	 RFC 3065 BGP AS Confederations
•	 RFC 4456 BGP Route Reflection
•	 RFC 4486 Subcodes for BGP  
Cease Notification
•	 RFC 4724 Graceful Restart  
for BGP
•	 RFC 5082 Generalized TTL Security 
Mechanism (GTSM)
•	 RFC 3392/5492/5668/6793 BGP 4-Octet 
ASN and Capabilities Advertisement with 
BGP-4
•	 RFC 5396/5668/6793 BGP 4-Octet ASN 
and Textual Representation of ASN
IS-IS
•	 RFC 1142/1195/3719/3787/5308 
IS-IS v4
•	 RFC 2763/2966/3567/3373 Adjacencies 
and route management
•	 RFC 5120 M-ISIS: Multi Topology IS-IS
•	 RFC 5306 Graceful Restart
•	 RFC 5309/draft-ietf-isis-igp-p2p-over-lan 
Point to point over LAN
•	 RFC 6329 IS-IS Extensions Supporting 
IEEE 802.1aq SPB
•	 RFC 5304 IS-IS Cryptographic 
Authentication 
•	 RFC 5310 IS-IS Generic Cryptographic 
Authentication 
IP Multicast
•	 RFC 1075 DVMRP
•	 RFC 2365 Multicast
•	 RFC 2710/3019/3810/MLD v2  
for IPv6
•	 RFC 2715 PIM and DVMRP 
interoperability
•	 RFC 2933 IGMP MIB
•	 RFC 3376 IGMPv3 (includes IGMP v2/v1)
•	 RFC 3569 Source-Specific Multicast 
(SSM)
•	 RFC 3973 Protocol Independent 
Multicast- Dense Mode (PIM-DM)
•	 RFC 4541 Considerations for IGMP and 
MLD Snooping Switches
•	 RFC 2362/4601/5059 PIM-SM
•	 RFC 5015 BiDIR PIM
•	 RFC 5060 Protocol Independent 
Multicast MIB
•	 RFC 5240 PIM Bootstrap Router MIB
•	 RFC 5132 Multicast Routing MIB
IPv6
•	 RFC 1981 Path MTU Discovery
•	 RFC 2460 IPv6 Specification
•	 RFC 2464 IPv6 over Ethernet
•	 RFC 2465 MIB for IPv6: Textual 
Conventions (TC) and General Group
•	 RFC 2466 MIB for IPv6: ICMPv6 Group
•	 RFC 2711 Router Alert Option
•	 RFC 3056 6to4 Tunnels
•	 RFC 3315 Dynamic Host Configuration 
Protocol for IPv6 (DHCPv6)
•	 RFC 3484 Default Address Selection
•	 RFC 3493/2553 Basic Socket API
•	 RFC 3542/2292 Advanced Sockets API
•	 RFC 3587/2374 Global Unicast  
Address Format
•	 RFC 3595 TC for IPv6 Flow Label
•	 RFC 3596/1886 DNS for IPv6
•	 RFC 4007 Scoped Address
•	 RFC 4022/2452 MIB for IPv6 TCP
•	 RFC 4087 IP Tunnel MIB
•	 RFC 4113/2454 MIB for IPv6 UDP
•	 RFC 4193 Unique Local Addresses
•	 RFC 4213/2893 Transition Mechanisms
•	 RFC 4291/3513/2373 Addressing 
Architecture (uni/any/multicast)
•	 RFC 4292/4293 IPv6 MIBs
•	 RFC 4301/2401 Security Architecture
•	 RFC 4302/2402 IP Authentication 
Header
•	 RFC 4303/2406 IP Encapsulating 
Security Payload (ESP)
•	 RFC 4308 Cryptographic Suites for IPsec
•	 RFC 4443/2463 ICMPv6
•	 RFC 4861/2461 Neighbor Discovery
•	 RFC 4862/2462 Stateless Address  
Auto-configuration
•	 RFC 5095 Deprecation of Type 0 Routing 
Headers in IPv6
Manageability
•	 RFC 854/855 Telnet and Telnet options
•	 RFC 959/2640 FTP
•	 RFC 1350 TFTP Protocol
•	 RFC 1155/2578-2580 SMI v1  
and SMI v2
•	 RFC 1157/2271 SNMP
•	 RFC 1212/2737 MIB and MIB-II
•	 RFC 1213/2011-2013 SNMP  
v2 MIB
•	 RFC 1215 Convention for SNMP Traps
•	 RFC 1573/2233/2863 Private  
Interface MIB
•	 RFC 1643/2665 Ethernet MIB
•	 RFC 1867 Form-based File Upload  
in HTML
•	 RFC 1901-1908/3416-3418 SNMP v2c
•	 RFC 2096 IP MIB
•	 RFC 2131 DHCP Server/Client
•	 RFC 2388 Returning Values from Forms: 
multipart/form-data
•	 RFC 2396 Uniform Resource Identifiers 
(URI): Generic Syntax
•	 RFC 2570-2576/3410-3415/3584  
SNMP v3
•	 RFC 2616 /2854 HTTP and HTML
•	 RFC 2667 IP Tunneling MIB
•	 RFC 2668/3636 IEEE 802.3  
MAU MIB
•	 RFC 2674 VLAN MIB
•	 RFC 3023 XML Media Types
•	 RFC 3414 User-based Security Model
•	 RFC 4122 A Universally Unique IDentifier 
(UUID) URN Namespace
•	 RFC 4234 Augmented BNF for Syntax 
Specifications: ABNF
•	 RFC 4251 Secure Shell  
Protocol Architecture
•	 RFC 4252 Secure Shell (SSH) 
Authentication Protocol
•	 RFC 4502 Remote Monitoring 
Management Information Base  
Version 2
•	 RFC 4627 JavaScript Object  
Notation (JSON)
•	 RFC 5424 The Syslog protocol
•	 RFC 6585 Additional HTTP Status Codes
•	 RFC 4253 The Secure Shell (SSH) 
Transport Layer Protocol 
•	 RFC 4254 The Secure Shell (SSH) 
Connection Protocol 
•	 RFC 3576 Dynamic Authorization 
Extensions to RADIUS

<<<PAGE 569>>>
8
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Security
•	 RFC 1321 MD5
•	 RFC 2104 HMAC Message 
Authentication
•	 RFC 2138/2865/2868/3575 /2618 
RADIUS Authentication and Client MIB
•	 RFC 2139/2866/2867/2620 RADIUS 
Accounting and Client MIB
•	 RFC 2228 FTP Security Extensions
•	 RFC 2284 PPP EAP
•	 RFC 2869/2869bis RADIUS Extension
•	 RFC 3162 RADIUS and IPv6
•	 RFC 4301 Security Architecture for IP
•	 RFC 1826/1827/4303/4305 
Encapsulating Payload (ESP) and  
crypto algorithms
•	 RFC 2560 X.509 Internet Public Key 
Infrastructure Online Certificate Status 
Protocol – OCSP
•	 RFC 2986 PKCS #10: Certification 
Request Syntax Specification Version 1.7
•	 RFC 3268 Advanced Encryption 
Standard (AES) Ciphersuites for 
Transport Layer Security (TLS )
•	 RFC 4346 The Transport Layer Security 
(TLS) Protocol Version 1.1
•	 RFC 5246 The Transport Layer Security 
(TLS) Protocol Version 1.2
•	 RFC 5280 Internet X.509 Public Key 
Infrastructure Certificate and Certificate 
Revocation List (CRL) Profile
•	 RFC 6125 Representation and 
Verification of Domain-Based 
Application Service Identity with PKI
•	 Draft-ietf-radext-radsec-12 TLS 
encryption for RADIUS
QoS
•	 RFC 896 Congestion Control
•	 RFC 1122 Internet Hosts
•	 RFC 2474/2475/2597/3168/3246 
DiffServ
•	 RFC 3635 Pause Control
•	 RFC 2697 srTCM
•	 RFC 2698 trTCM
Others
• RFC 791/894/1024/1349 IP  
and IP/Ethernet
•	 RFC 792 ICMP
•	 RFC 768 UDP
•	 RFC 793/1156 TCP/IP and MIB
•	 RFC 826 ARP
•	 RFC 919/922 Broadcasting  
Internet Datagram
•	 RFC 925/1027 Multi-LAN ARP/Proxy ARP
•	 RFC 950 Subnetting
•	 RFC 951 BOOTP
•	 RFC 1151 RDP
•	 RFC 1191 Path MTU Discovery
•	 RFC 1256 ICMP Router Discovery
•	 RFC 1305/2030 NTP v3 and Simple NTP
•	 RFC 1493 Bridge MIB
•	 RFC 1518/1519 CIDR
•	 RFC 1541/1542/2131/3396/3442 DHCP
•	 RFC 1757/2819 RMON and MIB
•	 RFC 2131/3046 DHCP/BootP Relay
•	 RFC 2132 DHCP Options
•	 RFC 2251 LDAP v3
•	 RFC 2338/3768/2787 VRRP and MIB
•	 RFC 2581 TCP Congestion Control
•	 RFC 3021 Using 31-bit Prefixes
•	 RFC 3060 Policy Core
•	 RFC 3176 sFlow
•	 IETF draft “IP/IPVPN services with IEEE 
802.1aq SPB networks”
•	 RFC 4562 MAC-Forced Forwarding 
Software Defined Networking (SDN)
•	 OpenFlow Switch Specification,  
Version 1.3.1
•	 OpenFlow Switch Specification,  
Version 1.0.0
*Please refer to current Release Notes for details on 
supported features.
Chassis model
OmniSwitch 9907
Number of modular slots
11 (Front accessible 7 slots + Rear accessible 4 slots)
Management and network interface slots (NI)
7 (Slot 1 CMM with integrated 2 x 40G NI. Slot 2 is universal; accommodates CMM or 
NI. CMM/NI is limited to 160 Gb/s switching capacity)
Fabric module slots (CFM)
4 (Bays marked CFM 3 and CFM 4 inactive; reserved for future use)
Fan tray slots
3
Current switching capacity per CMM (b/s /pps)
160 Gb/s Aggregate/119 Mpps
Current switching capacity per 1 G NI (b/s /pps)	
96 Gb/s Aggregate/71.4 Mpps
OmniSwitch 9907
Current switching capacity per 10 G NI (b/s /pps)
960 Gb/s Aggregate/714 Mpps
Current switching capacity per 100G NI
(b/s /pps)
1.6Tb/s Aggregate/1190 Mpps (using OS9907-CFM2)
Current switching capacity per fabric module 	
12.8 Tb/s Aggregate (using OS9907-CFM2)
2.56 Tb/s Aggregate (using OS9907-CFM)
Max Chassis switching capacity
25.6 Tb/s Aggregate (with two OS9907-CFM2 modules)
51.2 Tb/s Aggregate (with four OS9907-CFM2 modules *)
5.12 Tb/s Aggregate (with two OS9907-CFM modules)
Power supply (AC/DC) slots
4
Height (19-in. and 23-in. rack mount)
11U
OmniSwitch 9907
Dimensions (HxWxD)
49.02 x 44.2 x 58.42 cm (19.3 x 17.4 x 23 in)
Weight (RCB)
32.83 kg (72.24 lb)

<<<PAGE 570>>>
9
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Environment
Operating temperature
0°C to 45°C (32°F to 113°F)
Storage temperature
-20°C to 70°C (-4°F to 158°F)
Operating humidity
10% to 90% (non-condensing)
Storage humidity
10% to 95% (non-condensing)
Max operating altitude
4000m/13,000 feet
* Supported in future
 
Network interface characteristics
Model numbers
CPU
Memory
Port count
Interface type
OS99-CMM
Intel® Rangeley Quad core,  
1.7 GHz, 64-bit
16 GB SDRAM, 2 GB eUSB Flash*, 
32 Mb packet buffer
6
USB Type-A, EMP** RJ-45, Console RJ-
45/ micro-USB, 2x 40 GigE QSFP+
OS99-GNI-48
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 32 Mb packet buffer
48
10/100/1000Base-T
OS99-GNI-P48
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 32 Mb packet buffer
48
10/100/1000Base-T PoE
OS99-XNI-48
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 192 Mb packet buffer
48
1/10 GigE Base-T
OS99-XNI-U48
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 192 Mb packet buffer
48
1/10 GigE SFP+
OS99-GNI-U48
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 32 Mb packet buffer
48
10/100/1000Base-X
OS99-XNI-U24
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 96 Mb packet buffer
24
1/10 GigE SFP+
OS99-XNI-U12Q
Intel Rangeley Dual core,  
1.7 Ghz, 64-bit
8 GB SDRAM, 48 Mb packet buffer
13
12x 1/10 GigE SFP+, 1x 40 GigE 
QSFP+
OS99-XNI-P48Z16
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 192 Mb packet buffer
48
1/2.5/5/10 GigE Base-T PoE
OS99-XNI-P24Z8
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 192 Mb packet buffer
24
1/2.5/5/10 GigE Base-T PoE
OS99-XNI-UP24Q2
Intel Rangeley Dual core,  
1.7 Ghz, 64-bit
8 GB SDRAM, 64 Mb packet buffer
26
12x 1/10 GigE SFP+, 12x 1/10 GigE 
Base-T, 2x 40 GigE QSFP+
OS99-CNI-U8
Intel Rangeley Dual core,  
1.7 GHz, 64-bit
8 GB SDRAM, 192 Mb packet buffer
8
40/100 GigE Base-X 
4x10/25 GigE Base-X
 
*eUSB Flash for storing switch configuration, monitoring logs and AOS images etc.
**EMP (Ethernet Management Port) for out-of-band management
 
Power supplies
Model numbers
Max with 1 PSU
Input voltage/ current
Max output power/
current
Dimension (hxwxd)
Weight
OS99-PS-A
3K Watts
100 V AC (13.8A) to  
240 V AC (16.5 A)
1200 W/21.4 A
3000 W/53.5 A
1.63 in x 4 in x 17.2 in
4.8 lb (2.18 kg)
OS99-PS-D
2.5K Watts
-40 V DC to
-72 V DC
2500 W/44.6 A
1.63 in x 4 in x 17.2 in
4.6 lb (2.1 kg)

<<<PAGE 571>>>
10
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Ordering information
Chassis and power supply
Model numbers
Description
OS9907-CHAS
OS9900 11-slot chassis with 7 front accessible CMM/NI slots and 4 rear accessible fabric slots. Includes 3 x fan trays 
- 5 dedicated slots for any OS9900 network interfaces modules, 1 dedicated slot for CMM (management module), 1 
hybrid slot for either CMM OR network interface module, 4 dedicated slots for CFMs (switch fabric module), 4 power 
supply bays.
OS9907-CB1-XX
OS9907 base bundle with AC power. Base bundle includes 1 x OS9907 Chassis with 3 x Fan Trays, 1 x OS99-CMM 
management module, 1 x OS9907-CFM2 fabric module, 1 x OS99-PS-A power supply, and fully featured AOS 
software w/ advanced IP routing SW IPv4/IPv6).
OS9907-CB1-D
OS9907 base bundle with DC power. Base bundle includes 1 x OS9900 Chassis with 3 x Fan Trays, 1 x OS99-CMM 
management module, 1 x OS9907-CFM2 fabric module, 1 x OS99-PS-D power supply, and fully featured AOS 
software w/ advanced IP routing SW IPv4/IPv6).
OS9907-RCB1-XX
OS9907 redundant bundle with AC power. Redundant base bundle includes 1 x OS9900 Chassis, 2 x OS99-CMM 
management module, 2 x OS9907-CFM2 fabric module, 2 x OS99-PS-A power supplies, and fully featured AOS 
software w/ advanced IP routing SW IPv4/IPv6).
OS9907-RCB1-D
OS9907 redundant bundle with DC power. Redundant base bundle includes 1 x OS9900 Chassis, 2 x OS99-CMM 
management module, 2 x OS9907-CFM2 fabric module, 2 x OS99-PS-D power supplies, and fully featured AOS 
software w/ advanced IP routing SW IPv4/IPv6).
Model numbers
Description
OS9907-Fan tray
OS9907 Fan Tray. Spare.
OS99-PS-A
OS9900 series AC power supply. Provides up to 3KW of power, auto-ranging 110VAC-240VAC. XX country specific 
power cord designator.
OS99-PS-D
OS9900 series DC power supply. Provides up to 2.5KW of power.
Management and switching fabric  modules
Model numbers
Description
OS99-CMM
OS9900 Chassis Management Module w/SSL (DES, 3DES, RC2, RC4). The OS99-CMM includes a processor module, 
2x 40G QSFP ports and AOS software w/ advanced IP routing SW (IPv4/IPv6).
OS9907-CFM2
OS9907 Chassis Fabric Module. The OS9907-CFM2 is the second generation fabric card for the OS9907 chassis. 
This fabric card provides a  high performance fabric plane for the OS9907 chassis and provides inter-module 
connectivity for the data traffic.
Network interface cards
Model numbers
Description
Gigabit modules
OS99-GNI-48
OS9900 Gigabit network interface card offers 48 wirerate RJ-45 10/100/1000M Base-T ports. This Enhanced network 
interface card is MPLS ready, supports MACSEC, and provides large table support for L2, L3, and ACL policies.
OS99-GNI-U48
OS9900 Gigabit network interface card offers 48 unpopulated wire rate SFP 1000Base-X ports. This Enhanced 
network interface card is MPLS ready, supports MACSEC, and provides large table support for L2, L3, and  
ACL policies.
OS99-GNI-P48
OS9900 Gigabit network interface card offers 48 wirerate RJ-45 10/100/1000M Base-T ports with PoE. This  
Enhanced network interface card is MPLS ready, supports MACSEC, and provides large table support for L2, L3,  
and ACL policies.
10 Gigabit modules
OS99-XNI-48
OS9900 10 Gigabit network interface card offers 48 wirerate RJ-45 10GBase-T ports. This Enhanced network 
interface card is MPLS ready, supports MACSEC, and provides large table support for L2, L3, and ACL policies.
OS99-XNI-U48
OS9900 10 Gigabit network interface card offers 48 wirerate unpopulated SFP+ 1/10 GbE ports. This Enhanced 
network interface card is MPLS ready, supports MACSEC, and provides large table support for L2, L3, and  
ACL policies.
OS99-XNI-U24
OS9900 10 Gigabit network interface card offers 24 wirerate unpopulated SFP+ 1/10 GbE ports. This Enhanced 
network interface card is MPLS ready, supports MACSEC, and provides large table support for L2, L3, and  
ACL policies.

<<<PAGE 572>>>
11
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Model numbers
Description
OS99-XNI-U12Q
OS9900 10 Gigabit network interface card offers 12 wirerate unpopulated SFP+ 1/10 GbE ports and 1 wirerate 
unpopulated QSFP+ 40 GbE port. This Enhanced network interface card is MPLS ready, supports MACSEC, and 
provides large table support for L2, L3, and ACL policies.
OS99-XNI-P48Z16
OS9900 Multi-Gigabit network interface card offers 32 RJ-45 10G Base-T and 16 RJ-45 1/2.5/5/10G Base-T wire rate 
PoE ports. This Enhanced network interface card is MPLS ready, supports MACSEC, and provides large table support 
for L2, L3, and ACL policies.
OS99-XNI-P24Z8
OS9900 Multi-Gigabit network interface card offers 16 RJ-45 10G Base-T and 8 RJ-45 1/2.5/5/10G Base-T wire rate 
PoE ports. This Enhanced network interface card is MPLS ready, supports MACSEC, and provides large table support 
for L2, L3, and ACL policies.
OS99-XNI-UP24Q2
OS9900 10 Gigabit network interface card offers 12 wirerate unpopulated SFP+ 1/10 GbE ports, 12 wirerate RJ-45 
10GBase-T ports and 2 wirerate unpopulated QSFP+ 40 GbE ports. This Enhanced network interface card is MPLS 
ready, supports MACSEC, and provides large table support for L2, L3, and ACL policies.
100 Gigabit modules
OS99-CNI-U8
OS9900 100 Gigabit network interface card offers 8 unpopulated QSFP28 40/100GE ports. This Enhanced network 
interface card is MPLS ready, and provides large table support for L2, L3, and ACL policies..
TAA certified model numbers
TA9907-CHAS
TA9900 11-slot chassis with 7 front accessible CMM/NI slots and 4 rear accessible fabric slots. There are 4 power 
supply slots and includes 3 x fan trays. TAA
TA99-CMM
TA9900 Chassis Management Module w/SSL DES,3DES,RC2,RC4). The OS99-CMM includes a processor module, 2x 
40G QSFP ports and its AOS software w/ advanced IP routing SW IPv4/IPv6) TAA
TA99-GNI-48
TA9900 Gigabit network interface card offers 48 wire rate RJ-45 10/100/1000M Base-T ports ports. This Enhanced 
network interface card is MPLS, MACSEC ready, and provides large table support for L2, L3, and ACL policies.  TAA
TA99-GNI-P48
TA9900 Gigabit network interface card offers 48 wire rate RJ-45 10/100/1000M Base-T ports with PoE. This Enhanced 
network interface card is MPLS, MACSEC HW ready, and provides large table support for L2, L3, and ACL policies.  TAA
TA99-GNI-U48
TA9900 Gigabit network interface card offers 48 unpopulated wire rate SFP 1000Base-X ports. This Enhanced 
network interface card is MPLS, MACSEC ready, and provides large table support for L2, L3, and ACL policies.  TAA
TA99-XNI-48
TA9900 10 Gigabit network interface card offers 48 1/10G wire rate 10GBase-T ports. This Enhanced network 
interface card is MPLS, MACSEC HW ready, and provides large table support for L2, L3, and ACL policies.  TAA
TA99-XNI-P48Z16
TA9900 Multi-Gigabit network interface card offers 32 RJ-45 10G Base-T and 16 RJ-45 1/2.5/5/10G Base-T wire rate 
PoE ports. This Enhanced network interface card is MPLS, MACSEC ready, and provides large table support for L2, L3, 
and ACL policies.  TAA
TA99-XNI-U48
TA9900 10 Gigabit network interface card offers 48 1/10G wire rate unpopulated SFP+ ports. This Enhanced network 
interface card is MPLS, MACSEC HW ready, and provides large table support for L2, L3, and ACL policies.  TAA
TA99-XNI-U12Q
TA9900 10-Gigabit network interface card offers 12 unpopulated wire rate SFP+ 1/10 GbE ports. This Enhanced card 
is MPLS ready, has MACSEC, and provides large table support for L2, L3, and ACL policies. Provides one 40G QSFP+ 
port for flexibility. TAA
TA99-XNI-UP24Q2
TA9900 10-Gigabit network interface card offers 12 unpopulated SFP+ 1/10 GbE ports and 12 10G-Base-T ports. 
This card is MPLS ready, has MACSEC, and provides large table support for L2, L3,and ACL policies. Provides two 40G 
QSFP+ ports for flexibility. TAA
Software License 
OS-SW-MACSEC
Site license to enable MACSec on applicable OS6465, OS6560, OS6860, OS6865, OS6900, OS9900 models. One 
license per customer at no cost.
GE transceivers
SFP-GIG-T 
1000Base-T Gigabit Ethernet Transceiver (SFP MSA). SFP works at 1000 Mb/s speed and full-duplex mode.
SFP-GIG-SX
1000Base-SX Gigabit Ethernet optical transceiver (SFP MSA).
SFP-GIG-LX 
1000Base-LX Gigabit Ethernet optical transceiver (SFP MSA).
SFP-GIG-LH40
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 40 km on  
9/125 µm SMF.
SFP-GIG-LH70
1000Base-LH Gigabit Ethernet optical transceiver (SFP MSA). Typical reach of 70 km on  
9/125 µm SMF.
10 GE SFP+ transceivers
SFP-10G-SR
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 850 nm wavelength (nominal) with an LC 
connector. Typical reach of 300 m

<<<PAGE 573>>>
12
Datasheet 
Alcatel-Lucent OmniSwitch 9900 Series 
Model numbers
Description
SFP-10G-LR 
10 Gigabit optical transceiver (SFP+). Supports monomode fiber over 1310 nm wavelength (nominal) with an LC 
connector. Typical reach of 10 km
SFP-10G-ER
10 Gigabit optical transceiver (SFP+). Supports monomode fiber over 1550 nm wavelength (nominal) with an LC 
connector. Typical reach of 40 km
SFP-10G-ZR
10 Gigabit optical transceiver (SFP+). Supports data transmission at 1550nm over up to 80km single mode fiber. LC 
connector type.
SFP-10G-LRM
10 Gigabit optical transceiver (SFP+). Supports multimode fiber over 1310 nm wavelength (nominal) with an LC 
connector. Typical reach of 220 m on FDDI-grade (62.5µm)
SFP-10G-GIG-SR 
Dual-speed SFP+ optical transceiver. Supports multimode fiber over 850nm wavelength (nominal) with an LC 
connector. Supports 1000BaseSX and 10GBASE-SR
SFP-10G-24DWD80
10 Gigabit DWDM optical transceiver (SFP+ MSA), 1558.17 nm/Channel 24 (100GHz ITU Grid),  
80 km, LC Connector.
10 GE SFP+ direct attached cables 
SFP-10G-C1M
10 Gigabit direct attached copper cable (1 m, SFP+).
SFP-10G-C3M
10 Gigabit direct attached copper cable (3 m, SFP+).
SFP-10G-C7M
10 Gigabit direct attached copper cable (7 m, SFP+).
40 GE QSFP+ transceivers
QSFP-40G-SR
Four channel 40 Gigabit optical transceiver (QSFP+). Supports link lengths of 100 m and 150 m, respectively, on OM3 
and OM4 multimode fiber cables.
QSFP-40G-LR
Four channel 40 Gigabit optical transceiver (QSFP+). Supports single mode fiber over 1310 nm wavelength. Typical 
reach 10 km
QSFP-40G-CLR
Four channel 40 Gigabit optical transceiver (QSFP+). Supports maximum link length of 2 km on Single Mode Fiber 
using 1310 nm wavelength.
QSFP-40G-ER
Four channel 40 Gigabit optical transceiver (QSFP+). Supports single mode fiber over 1310 nm wavelength. Typical 
reach 40 km.
QSFP-4x10G-SR
40 Gigabit to 4 x 10 Gigabit Multifiber Push-On (MPO) fiber splitter transceiver
40 GE QSFP+ direct attached cables 
QSFP-40G-C1M
40 Gigabit direct attached copper cable (1 m, QSFP+).
QSFP-40G-C3M 
40 Gigabit direct attached copper cable (3 m, QSFP+).
QSFP-40G-C7M
40 Gigabit direct attached copper cable (7 m, QSFP+).
QSFP-4X10G-C1M 
40 Gigabit to 4 x 10 Gigabit direct attached copper splitter cable (1m, QSFP+)
QSFP-4X10G-C3M
40 Gigabit to 4 x 10 Gigabit direct attached copper splitter cable (3m, QSFP+)
QSFP-4X10G-C5M
40 Gigabit to 4 x 10 Gigabit direct attached copper splitter cable (5m, QSFP+)
QSFP-40G-AOC20M
Four channel active optical cable with connected QSFP+ transceivers. Supports 40G data rates over link lengths of 20 m.
100 GE QSFP28 transceivers
QSFP-100G-SR4
100 Gigabit optical transceiver (QSFP28). Supports maximum link length of 100 m on OM4 Multi Mode Fiber using 
850 nm wavelength.
QSFP-100G-CLR4 
100 Gigabit optical transceiver (QSFP28). Supports maximum link length of 2 km “on Single Mode Fiber using 1310 
nm wavelength”. The transceiver supports both FEC and non-FEC applications.
QSFP-100G-LR4
100 Gigabit optical transceiver (QSFP28). Supports maximum link length of 10 km on Single Mode Fiber using  
1310 nm wavelength.
QSFP-100G-CWDM4 
100 Gigabit optical transceiver (QSFP28). Supports maximum link length of 2 km on Single Mode Fiber using  
1310 nm wavelength. The transceiver supports FEC applications.

<<<PAGE 574>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view 
other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trademarks-copyright. All 
other trademarks are the property of their respective owners. The information presented is subject to change without notice. 
Neither ALE Holding nor any of its affiliates assumes any responsibility for inaccuracies contained herein. © Copyright 2022  
ALE International, ALE USA Inc. All rights reserved in all countries. DID00358015EN (September 2022)
Model numbers
Description
100 GE QSFP28 direct attached cables
QSFP-100G-C1M
100 Gigabit direct attached copper cable (1m, QSFP28) 
QSFP-100G-C3M 
100 Gigabit direct attached copper cable (3m, QSFP28)
QSFP-100G-C5M
100 Gigabit direct attached copper cable (5m, QSFP28)
QSFP-100G-AOC20M 
Four channel active optical cable with connected QSFP28 transceivers. Supports 100G data rates over link lengths 
of 20 m.
Please replace the “-xx” in the part number with the country-specific power cord (for example, OS9907-RCB-A-US comes with a power cord for the US, -UK for the 
United Kingdom). We offer 11 different power cord options. See the price list for the official power cord options offered.
Warranty
Hardware Lifetime Limited Warranty to the original owner from time of the purchase up to 5 years after the end-
of-sales (EoS) announcement.
Service and support
For more information about our Professional services, Support services, and Managed services, please go to 
https://www.al-enterprise.com/en/services
Please visit our website to learn more https://www.al-enterprise.com/en/products/switches/omniswitch-9900

<<<PAGE 575>>>
CL A SSRO O M SESSIO N  O R VIRTUA L C L A SS SESSIO N
END OF TRAINING EVALUATIONS

<<<PAGE 576>>>
YOUR FEEDBACKS ARE 
IMPORTANT!
Thank you to complete the training 
evaluation online survey before leaving 
your session. This will take you 2 minutes! 
You must complete the end of training 
evaluation to be able to download your 
training certificate of attendance.

<<<PAGE 577>>>
LOGIN TO ALE KNOWLEDGE HUB
• Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual 
credentials

<<<PAGE 578>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (1/2)
• Click on My Training on the home page
• Search for the training course by the reference provided by your instructor

<<<PAGE 579>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (2/2)
• From the session, select Evaluate in the dropdown menu and follow the instructions
OR
• From the curriculum, select Open Curriculum
• Then select Evaluate in the dropdown menu associated to the session and follow the 
instructions

<<<PAGE 580>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 581>>>
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