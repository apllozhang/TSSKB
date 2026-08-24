

<<<PAGE 1>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
OMNISWITCH LAN - R8 
SPB CONCEPTS & IMPLEMENTATION - 
EDITION 12 
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
DT00XTE323EN
SPB Concepts & Implementation
OmniSwitch LAN - R8

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
‐ Agenda, Remote Lab Overview
• OmniFabric Overview
• Why SPB?
• Shortest Path Bridging Mac-in-MAC
‐ Lab - Deploying a Backbone network based on SPB-M technology
• Shortest Path Bridging Data Plane
‐ Lab - Deploying a network based on SPB-M technology-L2 services 
technology
• Shortest Path Bridging (PBB-SPB) Services 
‐ Lab - SPB protocol Analysis and protection
• Shortest Path Bridging BUM Traffic flows & 
Troubleshoot

<<<PAGE 7>>>
Day 2
• IP Routing over SPB
‐ Lab: Implementing IP Routing over SPB-M – Routing Redundancy
• IP Routing over SPB –IP-VPN Lite
‐ Lab: Implementing IP Routing VPN-Lite over SPB-M
• IP Routing over SPB – L3-VPN
‐ Lab: Implementing IP Routing L3 VPN over SPB-M
• SPB Advanced Configuration
• Lab - SPB network advanced features

<<<PAGE 8>>>
Day 3
• Dynamic Services
• Lab - Setting up UNP SPB Dynamic SAP
• OmniVista 2500 & SPB 
• Lab - SPB in OmniVista 2500
• Hybrid SAP and Bridge Port and SPB E-Tree Services
• Lab - Manage Hybrid Access Port & E-Tree Services
• Shortest Path Bridging - Success Stories

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
• Provides specifications and compatibility information SFP/XFP/QSFP/… transceivers supported on the OmniSwitch  
switches
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
Internet Resources
•
ALE Network Equipment
• www.al-enterprise.com/en/products/switches
•
Spacewalkers Community
• www.spacewalkers.com
•
Partners Website
• MyPortal

<<<PAGE 12>>>
• Evaluation links are available to you as of the last day of the session and can therefore be filled in 
at the end of the session before leaving the classroom or virtual class.
• Two main situations have to be considered to access to the course evaluation, and this depends 
on the Knowledge Hub session status (while still being in “In progress”, and as of it has switched to 
“Completed”).
• The status switches usually the next Monday after the session has ended.
Your opinion counts!

<<<PAGE 13>>>
• Directly from the Home page / My Recent Learning activity;
• if “Evaluate” option is viewable, please click on it.
• if “Evaluate” is not proposed, click on “Open Curriculum” and after, on “Evaluate”
Reach the session evaluation

<<<PAGE 14>>>
REMOTE LAB CONNECTION
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 15>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Remote-Labs (R-Labs) topology
• Connect to a Remote-Lab (R-Lab)

<<<PAGE 16>>>
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

<<<PAGE 17>>>
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

<<<PAGE 18>>>
REMOTE LABS > TOPOLOGY
1
2
3
4

<<<PAGE 19>>>
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

<<<PAGE 20>>>
DHCP SERVER
• A DHCP server is running with an IP address of 192.168.100.102 and has the following 
scopes (where x stands for the switch number):

<<<PAGE 21>>>
OMNIVISTA 2500 & INTERNET ACCESS
• An OmniVista 2500 server is configured with the IP address 192.168.100.107/24.
• The OmniVista 2500 is reachable
from RDP desktop through a WEB 
client at the URL:
https://10.4.pod#.208:8443
• DNS server on the client : 10.0.0.51
• If Internet access is required for VM clients,
a pre-configuration has to be done on the OS6900-A

<<<PAGE 22>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 23>>>
OMNIFABRIC OVERVIEW
OMNISWITCH LAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 24>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the OmniFabric key features
• Position the right protocol (SPB, VxLAN
EVPN, MPLS) depending on the context

<<<PAGE 25>>>
OMNIFABRIC

<<<PAGE 26>>>
OMNIFABRIC
OVERVIEW
A Network Fabric is designed to enable 
organizations to efficiently transmit and 
manage data across their network, 
supporting a wide range of applications 
and services.
ALE OmniFabric
The best security in any network 
architecture
• OmniFabric is a multi-technology network fabric 
ensuring end-to-end security in a Zero Trust 
Network architecture with automated 
segmentation for both IT and OT environments.
• Supporting SPB (Shortest Path Bridging), MPLS, 
and EVPN within a single AOS platform, 
OmniFabric network fabric provides unmatched 
flexibility and performance, integrating 
seamlessly into diverse vendor ecosystems to 
prevent lock-in.

<<<PAGE 27>>>
CUSTOMER 
BENEFITS (1/3)
A unique solution offering 
embedded, automated IoT 
device detection and 
segmentation.
• Multi-Technology Integration
Ensuring superior flexibility and performance.
• Enhanced Cybersecurity
Protects data integrity and prevents unauthorized 
access with support for Zero Trust networks and 
micro-segmentation.
• Built-in Automation
Advanced automation features streamline network 
operations, reduce manual intervention and minimize 
human errors.
• Secure IoT Connectivity
IoT devices are automatically detected, classified, 
and contained in virtual segments.

<<<PAGE 28>>>
CUSTOMER 
BENEFITS (2/3)
Multi-Technology 
Integration: Supports SPB, 
MPLS and EVPN within a 
single operating system 
(AOS) ensuring superior 
flexibility and performance.
• Easy monitoring
Single pane of glass, augmented with AI powered 
analytics. This is particularly beneficial for customers 
with limited resources.
• Customizable Solutions
Offers the choice of multiple technologies to be used 
depending on the area or architecture –SPB in campus 
networks, EVPN in data centers, and MPLS in 
metropolitan area networks (MAN).
• Enables operational technology teams to 
connect devices to the network without increasing 
exposure to cyberattacks. This capability is included 
at no extra charge.
• IT/OT Convergence
Available for both indoor and outdoor/and harsh 
environments.

<<<PAGE 29>>>
CUSTOMER 
BENEFITS (3/3)
OmniFabric adapts to various 
use cases, delivering reliable, 
end-to-end security that 
lowers Total Cost of
Ownership while enabling 
IT/OT convergence
• Flexibility and Interoperability
Compatible with environments where equipment from 
various vendors coexist, eliminating vendor lock-in 
and adapting to diverse underlying architectures, 
from edge to data center. It offers increased choices 
and freedom to customers.
• Simplified Operations
OmniFabric ensures an easy learning curve and 
management with all protocols integrated in one 
Operating system.
• Optimized Total Cost of Ownership (TCO)
With no hidden fees, simple procurement, ease of 
learning and unified management through Alcatel-
Lucent OmniVista.

<<<PAGE 30>>>
ALE OMNIFABRIC
Help future-proof the network and adapt to changing technology trends
MPLS
SPB
AOS
Universal Network Profile
Dynamic Services
Virtual Chassis
Automation
EVPN
All Technology fabric under the same Operating System - AOS
Simplified operations

<<<PAGE 31>>>
SPB
EVPN
MPLS
Main use case
Datacenter, Campus, IoT
Networks
Datacenter
Service Provider & Mission 
critical networks
Scalability
Large
Large/ Very large
Large/Very large
Resiliency
High
High
Very High
Ease of deployment
Simple to Moderate
Moderate to complex
Moderate to complex
Training needed
Low to Moderate
Moderate to High
High
Protocol Overhead
Low
IS-IS only
Moderate
BGP & VXLAN/ MPLS
High
LDP, RSVP, BGP
Troubleshooting
Simple & Fast
Intermediate time
Complex & Slow
EVPN, SPB & MPLS – POSITIONING SUMMARY

<<<PAGE 32>>>
SAMPLE ARCHITECTURES

<<<PAGE 33>>>
MPLS SPB FABRIC
High availability in every type of environment
MPLS
• Highly scalable
• Core, backbone
• Convergence: 50 ms
• Complex
• Cost: $$$
SPB
• Scalable
• Access, core, backbone
• Convergence: 100 ms
• Cost: $$
Mission critical support for harsh environments
MPLS
OS9900
OS6900
OS6860
OS6865
Main
campus
Primary DC
OS6900
OS6860
OS6560
OV
PBX 
OXE
NSP
VM/Storage
Secondary DC
OV
PBX 
OXE
NSP
OS9900
OS6900
OS6860
OS6865
Branch
location
SPB
SPB

<<<PAGE 34>>>
EVPN FABRIC
EVPN-VXLAN Fabric
PE-1
PE-2
PE-3
PE-4
LAG
CE-2
CE-3
ESI xxxx
nDF EVI 2
ESI xxxx
DF EVI 2
ESI 1
DF EVI 1
ESI yyyy
DF EVI 3
ESI yyyy
nDF EVI 3
VM-2 
VLAN 200
VM-3 
VLAN 300
CE-1
VM-1 
VLAN 100
EVI 3
EVI 2
EVI 1
1/1/1
1/1/1
1/1/1
EVI
Ethernet Virtual Instance. Ex: VNI (an individual subnet)
ESI
Ethernet Segment Identifier. Globally significant / Auto vs Manual. 
Single-homed segments have ESI=0 (as per RFC). MAC-based ESI.
SH/MH
Single-homing: CE attached to single PE
Multi-homing: CE attached to multiple PE
DF
Designated Forwarder. Election based on algorithm.
SA: Both unicast and BUM traffic forwarded by DF
AA: BUM traffic forwarded by DF to the CE
MH-SA
MH-AA
Forwarding of unicast traffic from remote PE to ES
AA: All-active: To all attached PE
SA: Single-active: to single PE (DF)
MAC-VRF
VRF table for MAC addresses for a single EVI. L2VNI is tied to MAC-VRF
IP-VRF
VRF table for IP routes. L3VNI is tied to IP-VRF
IRB
Integrated Routing and Bridging interface. Connected between Layer 2 
domain and IP-VRF.
EVI 1: VNI 100
EVI 2: VNI 200
EVI 3: VNI 300/400
VM-4 
VLAN 400
1/1/2
LAG

<<<PAGE 35>>>
USE CASE EXAMPLES
Market
Key Issues
Advantage
Video Surveillance
Scale < 1,000 Virtual-chassis
Staff with video expertise
Multicast
SPB – simplicity
Casino – video & operations
Scale < 1,000 Virtual-chassis
Staff with video expertise
Multicast
SPB – simplicity
Campus Network
Scale < 1,000 Virtual-chassis
Staff with broad responsibility (LAN, WLAN, 
FW) 
SPB - simplicity
ITS Network
Staff with broad responsibility
Outdoor deployments 
SPB – simplicity, ruggedized 
equipment
Large-data center
Scalability
EVPN
Rail, E&U
Very low convergence-times
IP-MPLS
MANs/Smart City
Scalability
Traffic Control
SPB/IP-MPLS*
* When IP-MPLS is mandatory in the tender

<<<PAGE 36>>>
OMNIFABRIC SUPPORT (PER OMNISWITCH)
SPB
VxLAN / VxLAN EVPN
MPLS
OmniSwitch 6860E



OmniSwitch 6570M
**


OmniSwitch 6860N

/

OmniSwitch 6870

/*
**
OmniSwitch 6900

/

OmniSwitch 9900

*/*
**
* Supported starting with 8.10 R3/R4
** HW ready

<<<PAGE 37>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 38>>>
WHY SPB?
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 39>>>
ALE OmniFabric
Adapting to your Architecture
ALE OmniFabric ensures end-to-end 
security through micro-segmentation in a 
Zero Trust Networking automated 
architecture.
✓Just define the roles and the policies for your IoTs and 
devices, ALE Multi-Technology Fabric will deploy it for you 
automatically.
✓Automated Security embedded, from the Edge to the Data 
Center
✓Scale, Interop and Control your network
MPLS
SPB
EVPN
Automation
All Technology fabric under the same Operating System - AOS
Build a Zero Trust autonomous network with enhanced 
micro/macro-segmentation
SPB IN OMNIFABRIC

<<<PAGE 40>>>
IT’S AN ALL-IN-ONE SWISS-KNIFE SOLUTION
◼Spanning Tree 
replacement
◼Multi-tenancy
◼Micro-segmentation
◼IoT
Campus
Data Centre
◼Intra and inter-DC fabric
◼Any to any
◼Fast convergence
WAN
◼MPLS-like L2/L3 VPN 
Services
◼Multi-site
◼Multi-tenancy
One Solution 
✓Reduce the 
complexity of 
managing 
multiple 
technologies.
OmniFabric SPB

<<<PAGE 41>>>
Hardened
◼Extended temperature
◼Environmentally hardened
◼Stringent EMC/EMI
◼HPOE
IT’S SUPPORTED ACROSS THE BOARD
One Solution 
◼Core, aggregation, access
◼High density
◼High capacity
◼HPOE
Modular
Compact
◼Top of Rack
◼Spine & leaf
◼Compact core
◼High capacity
Access
◼Advanced access
◼Small core
◼Multi-gig
◼HPOE

<<<PAGE 42>>>
IT’S NOT IP-BASED => IT’S MORE SECURE
x
Scanning
x
DOS
x
Man-in-the-middle
x
…
✓
Not vulnerable to 
IP-based attacks
OmniFabric SPB

<<<PAGE 43>>>
IT’S INTEROPERABLE AND BACKWARDS COMPATIBLE
◼802.1Q
◼Q-in-Q
◼LACP
◼Etc
L2
L3
◼OSPF
◼IS-IS
◼BGP
Multicast
◼PIM SM
◼PIM DM
◼PIM BIDIR
◼PIM SSM
✓
Investment protection
✓
Phased migration
✓
No forklift upgrade
OmniFabric SPB
Interoperability

<<<PAGE 44>>>
MACRO AND MICRO-SEGMENTATION
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓Security
✓Quality
✓
Authenticate
✓
Classify
✓
Provision
Users
✓
Authenticate
✓
Classify
✓
Provision
HVAC
✓
Authenticate
✓
Classify
✓
Provision
Access Security
✓
Zero-trust framework
✓
Software-defined segmentation
OmniFabric SPB
https://youtu.be/IttOgoATWpY

<<<PAGE 45>>>
SIMPLER NETWORK AUTOMATION
Simpler
◼Auto backbone
◼Auto services
◼Auto attachment
◼Self healing
Automatic
Edge Only
◼Edge-only provisioning
◼No-touch core
◼OmniVista NMS
Single Protocol
◼No protocol “stack”
◼One protocol
◼L2 + L3
◼IPv4 + IPv6
IS-IS
✓
Simpler to deploy
✓
Simpler to operate
OmniFabric SPB

<<<PAGE 46>>>
IT CAN RUN IN PARALLEL WITH YOUR CURRENT DESIGN
✓SPB Domain
HVAC
✓SPB Domain
Security
✓Legacy Domain
Desktop
Telephony
✓Phased migration
OmniFabric SPB

<<<PAGE 47>>>
IT CAN EXTEND OVER THIRD-PARTY NETWORKS
✓
WAN abstraction
✓
Self-managed services
✓
End 2 end services
✓
No service stitching
OmniFabric SPB
SPB
Network

<<<PAGE 48>>>
IT’S DYNAMIC AND ELASTIC => IT’S MORE SECURE
Stadium
Dormitory
Library
STEM Lab
Faculty
Student
Faculty
Student
Library
Faculty
STEM PROJECT

<<<PAGE 49>>>
IT’S DYNAMIC AND ELASTIC => IT’S MORE SECURE
Stadium
Dormitory
Library
STEM Lab
Faculty
Student
Faculty
Student
Library
Faculty
STEM PROJECT
Student

<<<PAGE 50>>>
IT’S DYNAMIC AND ELASTIC => IT’S MORE SECURE
Stadium
Dormitory
Library
STEM Lab
Faculty
Student
Faculty
Student
Library
Faculty
STEM PROJECT
Student
No Service
✓
Services stretch and contract as 
needed
✓
Policy and identity driven
✓
Reduced attack surface
OmniFabric SPB

<<<PAGE 51>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 52>>>
SHORTEST PATH BRIDGING MAC -IN-MAC (SPB)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 53>>>
LESSON SUMMARY
✓Introduction to Shortest Path Bridging
(IEEE 802.1aq)
✓SHORTEST PATH Bridging (SPB)
Control Plane (IS-IS SPB)

<<<PAGE 54>>>
SPB – AOS SPECIFICATIONS
Shortest Path Bridging - IEEE 802.1aq mac mode
• Multiple loop free shortest path routing 
• Supports P2P, P2MP & Mesh
• Supports up to 16 NNI paths
• Traffic Engineering
• Head end assignment of traffic to 16 shortest paths
• Deterministic traffic flows
• Scales to 1000’s of devices
• Uses IS-IS already proven well beyond 1000. 
• Significant improvement over the STP scales. 
• Convergence with fast recovery
• 100’s ms convergence times 
• Natively protect failures and reroute 
• IS-IS 
• SPB builds/reuses well known proven protocols 
• IEEE 802.1ad
Data Plane (Q-in-Q PB)
• IEEE 802.1ah 
Data Plane (M-in-M PBB)
• IEEE IS-IS SP
Control Plane
• Optimized multicast (head end or Tandem replication)
• Membership advertised in same protocol as topology
• Supports E-LINE/E-LAN/E-TREE
• Address learning restricted to edge
• FDB is computed and populated like a router
• Unicast and Multicast handled at the same time
•
ucast/mcast)
• Symmetry
• Congruence

<<<PAGE 55>>>
STP VS. SPB-M
Spanning Tree
•
•
•
SPB-M
• All Links utilized: 
•
MAC-in-MAC encapsulation, restricts mac 
learning to the edge of the network, increasing the network 
scalability and stability.
•
C
B
E
D
F
G
A
C
B
E
D
F
G
A

<<<PAGE 56>>>
SPB - CONTROL PLANE COMPONENTS
SPB Access Port
Where the customer 
traffic ingresses or 
egresses
BEB
BEB
BEB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
BEB = Backbone Edge Bridge
BCB = Backbone Core Bridge
C-VID = Customer VlanID
BVLAN=Backbone VLAN
I-SID = Service ID
SAP=Service Access Point
B-VID = Backbone VID
BMAC= Backbone switch MAC address
Backbone Core Bridge
BCB is unaware of services 
Performs forwarding only by 
looking at  BMAC header
Access
Node
Access
Node
SAP
SAP
Service Access Point (SAP)
Used to specify what type of CVLAN traffic is 
allowed to enter/exit from/to the SPB network
Associate a traffic to a SPB service based on 
Vlan-TAG
SAP
SAP
SAP
C-VID
802.1Q
Customer VLAN (CVLAN))
A traditional VLAN with MAC learning 
& flooding where users connect to
Backbone Edge Bridge
Edge nodes of the SPBM network
Service termination
Service Instance Identifier
Backbone services instance identifier 
Identifies a MAC-in-MAC service instance
Used to identify and transmit any virtualized 
traffic in an encapsulated SPB-M frame
Delivers service abstraction
ISID
1001
ISID
1002
ISID
1001
ISID
1002
ISID
1001
Service
A flooding domain for customer traffic
ISID
1002
ISID
1001
ISID
1002
ISID
1001
ISID
1002
Backbone Vlan (BVLAN)
Special VLAN provides the physical path and 
propagation of network control
Expansion of Layer 2 Ethernet domains
No source @mac learning of Customer data traffic 
Each B-VLAN calculates its own Shortest Path Tree
BVLAN
4002
BVLAN
4001
BEB
SAP
ISID
1001
BVLAN
4001
BVLAN
4002

<<<PAGE 57>>>
SPB - CONTROL PLANE COMPONENTS
B Component
Service Instance 
Identifier (I-SID)
Service Access 
Point (SAP)
SPB Access 
Interface
SPB-M
Core Network
SPB Network 
Interface
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002

<<<PAGE 58>>>
SPB - DATA PLANE
Ethernet
802.3
Provider
Bridges
802.1ad
Ethernet
802.1Q
Consistent
Forwarding 
I-SID = Service ID
B-VID = Backbone VID
B-DA = Backbone DA
B-SA = Backbone SA
SA = Source MAC address
DA = Dest MAC address
VID = VLAN ID
C-VID = Customer VID
S-VID = Service VID
Payload
Ethertype (IP)
C-SA
C-DA
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
C-SA
C-DA
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
C-SA
C-DA
I-SID
Ethertype 802.1ah
B-VID
Ethertype 802.1 ad
B-SA
B-DA
PBB-802.1ah
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
C-SA
C-DA
S-VID
Ethertype 802.1ad
S-VID
Ethertype 802.1ad
Provider
Backbone
Bridges
802.1ah

<<<PAGE 59>>>
BCB
BCB
BCB
BCB
BCB
BCB
BCB
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
C-SA (HostA)
C-DA (HostB)
Payload
Ethertype (IP)
C-SA (host A)
C-DA (host B)
SPB - DATA PATH
BEB - 2
BEB-1
Host A
Host B
Access
switch
Access
switch
Payload
Ethertype (IP)
C-SA (host A)
C-DA (host B)
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
C-SA (HostA)
C-DA (HostB)
Payload
Ethertype (IP)
C-VID
Ethertype 802.1q
C-SA (hostA)
C-DA (hostB)
I-SID
Ethertype 802.1ah
B-VID
Ethertype 802.1 ad
B-SA (BEB1)
B-DA (BEB2)
S-VID
Ethertype 802.1ad
SPB Network

<<<PAGE 60>>>
SHORTEST PATH BRIDGING
• Distributes traffic and makes better use of redundant links in a meshed network
• Multi-path loop-free shortest path bridging
• Up to 16 paths (Equal cost Tree Algorithms)
• Head-end assignment of traffic to any of those 16 shortest paths 
• Deterministic routing easily predicted by offline TE tools
• Excellent use of mesh connectivity
• Backbone provisioning simplicity
• Natively provides virtualized Layer 2 services
• Natively provides virtualized routing services
• Adapts to any physical layer / fibre plant
• Robust/Scalable link-state routing applied to MAC tables
• Separation between Services and Backbone

<<<PAGE 61>>>
SPB DESIGN TWO-TIER TOPOLOGY
SPB Core
Network
Data Center
BEB
BEB
BEB
BEB
BEB
Remote Site
BEB
Access
Access
LAG or DHL
Core Switch
• No need for BCB nodes
• Backbone edge bridge (BEB) role
• BEB nodes in partial or full mesh 
topology
• VLAN to I-SID
• IS-IS for MAC learning
• IS-IS for SPB paths
• PBB for data plane
• Redundancy achieved through BEB 
nodes made of two or more physical 
chassis in VC topology
Access Switch
• 802.1Q VLAN on LAG
• STP or DHL towards BEB
• Redundancy achieved through VC BEB 
and/or dual BEB nodes, LACP protocol
Remote
• Extension of SPB domain 
possible through MPLS or VXLAN 
domain to remote locations
MPLS
VXLAN
Access

<<<PAGE 62>>>
SPB DESIGN THREE-TIER TOPOLOGY
SPB Core
Network
Access
Access
Access
LAG or DHL
LAG
Data Center
BEB
BEB
BEB
BEB
BEB
BEB
BCB
BCB
BCB
BCB
Remote Site
BEB
BEB
Access Switch
• 802.1Q VLAN on LAG
• STP or DHL towards BEB
• Redundancy achieved through VC BEB 
and/or dual BEB nodes, LACP protocol
Core Switch
• Backbone Core Bridge (BCB) role
• Learns BEB addresses
• IS-IS SPB for paths
• PBB for data plane
Remote
• Extension of SPB domain possible through 
MPLS/VXLAN domain to remote locations
Aggregation Switch
• Backbone edge bridge (BEB) role
• VLAN to I-SID
• IS-IS for MAC learning
• IS-IS for SPB paths
• PBB for data plane
• Redundancy achieved through dual BCB nodes
MPLS
VXLAN
BCB

<<<PAGE 63>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 64>>>
SHORTEST PATH BRIDGING - CONTROL PLANE
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 65>>>
SPB CONFIGURATION STEPS
Interfaces IS-IS
Services
Control Plane (NNI ports)
SPB Core level
On BEB + BCB 
UNP Access Port (Dynamic)
UNP Profiles (Dynamic)
Access Port
SAP
Data Plane (UNI ports)
SPB Access level
Only on BEB 
Access Port (Static)
SAP (Static/Dynamic)
Multi Access
P2P
Pseudo-wire
Service
L2 Profiles (optional)
Loopback Detection (LBD) (optional)
BVLAN

<<<PAGE 66>>>
BVLAN
BVLANS (BACKBONE VLAN)    
• Shortest path bridge VLAN
• No spanning tree control 
• No source @mac learning of Customer data traffic 
• No flooding of unknown destination or multicast frames
• IP interface supported on Control BVLANs to provide In-Band 
Management
• Each B-VLAN calculates its own Shortest Path Tree
• Control BVLAN carries IS-IS control packets
• AOS support: 16 BVLANs
-> spb bvlan 4001 admin-state enable
Configure BVLANs
-> spb isis control-bvlan 4001
Setup the control B-VLAN
Control Plane

<<<PAGE 67>>>
SPB IN-LINE MANAGEMENT
• Support management IP access to the BEBs as well as BCBs 
• IP interface on the Control BVLAN
• ISIS-SPB protocol for 
•
Advertising IP routing in the IP BVLAN domain
•
Mapping MAC-to-IP addresses -> No ARP packet
BCB
BCB
BCB
BEB
BEB
BCB
NMS
CONTROL BVLAN 4001
-> spb isis control-bvlan 4001
-> ip interface "spb-mgmt" address 172.30.1.1/24 vlan 4001
Assign control BVLAN IP address
Configure BVLANs
Setup the control B-VLAN
BVLAN

<<<PAGE 68>>>
SPB IN-LINE MANAGEMENT
• In-band management subnet routing
• Static or Dynamic routing
• Interface “spb-management” used for route redistribution
• Redistribute SPB management routes into dynamic routing 
protocols
• Redistribute routes into ISIS-SPB
BCB
BCB
BCB
BEB1
BEB
BCB
CONTROL BVLAN 4001
NMS
IP Network
OSPF
-> ip static-route 0.0.0.0/0 gateway <BEB1_ip_address>
Setup Routing
-> ip redist <ospf> into spb-mgmt [all-routes | route-map] 
-> ip redist spb-mgmt into <ospf> [all-routes | route-map] 
Static
Dynamic
Assign control BVLAN IP address
Configure BVLANs
Setup the control B-VLAN
BVLAN

<<<PAGE 69>>>
IS-IS INTERFACES AND ADJACENCIES 
• Network topology discovery
• IS-IS Hello (IIH) packets
• Default Control MAC address: 01:80:c2:00:00:14
• Control BVLAN
• Active SPB interfaces
• Each bridge has one unique MAC address 
• Known as the B-MAC
• Advertised by IS-IS as the SYS-ID
• Keepalive messages to maintain the adjacencies 
• Build SPT from each system to the rest of the nodes
• Supported Adjacency types 
• Point-to-Point adjacencies
• Point-to-MultiPoint adjacencies
• MACsec supported on network ports
• Provides MACsec security on the tunnelled traffic
Control Plane

<<<PAGE 70>>>
SHORTEST PATH TREES CALCULATION
SPB Link Metric Cost 
Metric (Link cost) lower metric = higher priority
Lowest Hop Count = higher priority
When multiple links have an equal cost
(metric and hop count)
All bridges use predefined ECT algorithms to calculate 
layer 2 congruency and symmetry for switching
• Standard provides 16 predefined algorithms
• 16 ECT -> index 1-16
• Same algorithm is used both for unicast and multicast
• Sorted list of BridgeID’s* computed as ECTs
Bridge ID = System ID (6 bytes) + Priority (2 bytes)
System ID = System Base MAC Address
Priority (Default 32768)
Byte-by-byte XOR ECT-MASK (16 masks to provide 16 ECT) for all nodes 
excluding source and destination
• Each mask is assigned to a BVLAN
Shortest Hop Count
Shortest Metric
ECT-Algorithm
ECT-ID | MASKS | B-VID
1    
0x00
4001
2
0xFF
4002
3
0x88
4003
4
0x77
4004
5
0x44
6
0x33
7
0xCC
8
0xBB
9
0x22
10
0x11
11
0x66
12
0x55
13
0xAA
14
0x99
15
0xDD
16
0xEE
1  Low      4001     ECT-MASK(1) = 0x00 →default, will pick the lowest BridgeID
2  High      4002     ECT-MASK(2) = 0xFF →will invert, pick the largest BridgeID
3  High      4003     ECT-MASK(2) = 0x77→will pick lowest, then largest BridgeID
4  High      4004     ECT-MASK(2) = 0x88→will pick largest then lowest BridgeID
Control Plane
1st
2nd
3rd
SPB path calculations use the maximum 
value of the two nodes when the metric is 
different
The next available ECT ID is 
automatically assigned to a BVLAN 
when the BVLAN is created
When link metric is the same hop count is 
use

<<<PAGE 71>>>
POINT-TO-POINT ADJACENCIES
• SPB-ISIS operates over point-to-point (P2P) links 
• One adjacency on an SPB network interface
• BEBs form adjacencies with next-hop BCBs
• IS-IS SPB extended Hello TLV
• Local address “SPSourceID” advertisement
• Circuit type
• ECT Algorithms and BVLAN 
• Link cost (Link Metric)
• ISID et I-SIDs to B-VLAN mapping information
BCB
BCB
BCB
BEB
BEB
BCB
BEB
BEB
BEB
Control Plane

<<<PAGE 72>>>
CONFIGURING ISIS INTERFACES 
-> spb isis interface port 2/1 
-> spb isis interface linkagg 5
Create ISIS-SPB Interfaces
Interfaces IS-IS
-> spb isis admin-state enable
Enable IS-IS on each system
p2p: Point-to-Point adjacencies (default)
Configures the interface as an SPB point-to-point interface 
(P2P) on which one adjacency is allowed.
Control Plane
BVLAN
-> spb isis interface port 2/1 type p2p
-> spb isis interface linkagg 5 type p2p

<<<PAGE 73>>>
MONITORING SPB
• Displays the ISIS-SPB backbone VLAN (BVLAN) configuration for the switch
• Displays the shortest path first (SPF) information to all known SPB switches for a specific BVLAN.
-> show spb isis spf bvlan 4015
SPB ISIS Path Table:
Destination                              Outbound   Next Hop                                SPB     Num
(Name : BMAC)                            Interface  (Name : BMAC)                           Metric  Hops
----------------------------------------+----------+----------------------------------------+------+------
sw1             : e8:e7:32:81:3b:7d      1/1/5  
sw1          : e8:e7:32:81:3b:7d     10     1
sw8             : e8:e7:32:a4:77:7d      1/1/5  
sw1          : e8:e7:32:81:3b:7d     20     2
show spb isis spf bvlan bvlan_id
-> show spb isis spf bvlan 4015 bmac e8:e7:32:a4:77:7d
SPB ISIS Path Details:
Path Hop Name        Path Hop BMAC
--------------------+-------------------
sw8              e8:e7:32:a4:77:7d
sw1              e8:e7:32:81:3b:7d
show spb isis spf bvlan bvlan_id bmac mac_address
Sw1: Transit switch (next hop)
SPB ISIS BVLANS:
Services  Num    Tandem     Root Bridge
BVLAN   ECT-algorithm     In Use  mapped    ISIDS  Multicast  (Name : MAC Address)
-------+-----------------+-------+---------+------+----------+------------------------------
4015  00-80-c2-01       YES     YES
1  SGMODE
4016  00-80-c2-02       YES     YES
1  SGMODE
show spb isis bvlan
Control Plane

<<<PAGE 74>>>
-> show spb isis info
SPB ISIS Bridge Info:
System Id             = e8e7.32a4.777d,
System Hostname
= sw8,
SPSourceID
= 04-77-7d,
SPBM System Mode      = auto,
BridgePriority
= 32768 (0x8000),
……………  Omitted lines  …………………
MONITORING SPB
• Displays information about the ISIS-SPB adjacencies SPB ISIS
• Displays the discovered node-level parameter values for all of the ISIS-SPB switches participating in 
the topology 
SPB ISIS Nodes:
System Name        System Id    SourceID
BridgePriority
----------------+---------------+--------+---------------
sw1              e8e7.3281.3b7d  0x13b7d  32768 (0x8000)
sw8              e8e7.32a4.777d  0x4777d  32768 (0x8000)
sw7              e8e7.32c2.4e93  0x24e93  32768 (0x8000)
SPB ISIS Adjacency:
System
(Name : SystemId)                     Type   State   Hold  Interface
-------------------------------------+------+-------+------+----------
sw1             : e8e7.3281.3b7d  L1    UP        19       1/1/8
sw8             : e8e7.32a4.777d  L1    UP        25       1/1/8
show spb isis adjacency
show spb isis nodes
Control Plane

<<<PAGE 75>>>
MONITORING SPB
• Displays information about the ISIS-SPB interfaces
• Displays details of an IS-IS SPB interface, like interface type, oper state, priority, DIS etc.
Interface     : 1/1/8                      Type             : Multi-Access
Oper State    : UP                         Admin State      : UP
Circuit Id    : 1                          CSNP Int         : 10   sec
Desg IS       : e8e7.32c2.4e93             Adjacencies      : 2
Metric        : 10                         Hello Timer      : 9    sec
Hello Mult    : 3                          Priority         : 127
SPB ISIS Interfaces:
Oper
Admin   Link      Hello   Hello
Circ
Interface       Level   CircID
state  state
Metric    Intvl
Mult   Type
---------------+-------+----------+------+-------+---------+-------+------+------------
1/1/5           L1      1          UP     UP
10        9       3       Pt-to-Pt
1/1/6           L1      2          UP     UP      10        9       3       Multi-Access
show spb isis interfaces
show spb isis interfaces port 1/1/8
Indicates whether the interface 
was configured as a point-to-point 
(Pt-to-Pt) link or as a multiple 
access (Multi-Access) link.
Hello PDU transmissions timer
Number that is multiplied by the Hello 
Interval to determine the hold timer.
Control Plane

<<<PAGE 76>>>
MONITORING SPB
• Displays information about the multi-access DIS pseudo node
----------------------------------------------------------------------
Interface     : 1/1/8               Type             : Multi-Access
Oper State    : UP                  Admin State      : UP
Circuit Id    : 1                   CSNP Int         : 10   sec
Desg IS       : e8e7.32c2.4e93 
Adjacencies      : 2
Metric        : 10                  Hello Timer      : 9    sec
Hello Mult    : 3                   Priority         : 127
----------------------------------------------------------------------
show spb isis interfaces port 1/1/8
Elected DIS @MAC
SPB ISIS Bridge Info:
System Id        = e8e7.32c2.4e93,
System Hostname  = sw7,
SPSourceID
= 02-4e-93,
SPBM System Mode = auto,
BridgePriority
= 32768 (0x8000),
MT ID            = 0,
Control BVLAN    = 4001,
Area Address     = 0.0.0.0,
Level Capability = L1,
Admin State      = UP,
LSDB Overload    = Disabled,
Last Enabled     = Thu Oct  1 13:54:13 2020,
Last SPF         = Thu Oct  1 14:56:43 2020,
SPF Wait         = Max: 1000 ms
Initial: 100 ms
Second: 300 ms,
LSP Lifetime     = 1200,
LSP Wait         = Max: 1000 ms, Initial: 0 ms, Second: 300 ms,
Graceful Restart = Enabled,
GR helper-mode   = Enabled,
# of L1 LSPs     = 4
Control Address  = 01:80:c2:00:00:14 (AllL1)
show spb isis info
Control Plane

<<<PAGE 77>>>
MONITORING SPB
• Displays information about the multi-access DIS database
Legends : P    = The Partition repair bit is set
OV   = The overload bit is set
ATT  = The Attach bit is set
L1   = Specifies a Level 1 IS type
L2   = Specifies a Level 2 IS type
SPB ISIS LSP Database:
LSP ID                 Sequence    Checksum   Lifetime   Attributes
----------------------+-----------+----------+----------+-----------
e8e7.3281.3b7d.00-00        0x10      0x9f0        624   L1
e8e7.32a4.777d.00-00        0x16     0x4528       1152   L1
e8e7.32c2.4e93.00-00        0x0d     0x198c        605   L1
e8e7.32c2.4e93.01-00        0x07     0x10b3        660   L1
Level-1 LSP count : 4
show spb isis database
Control Plane

<<<PAGE 78>>>
MONITORING SPB
• Displays content of a particular multi-access pseudo node LSP 
SPB ISIS LSP Database:
-------------------------------------------------------------------------------
LSP ID        : e8e7.3281.3b7d.00-00                   Level     : L1
Sequence      : 0x11             Checksum  : 0x7f1     Lifetime  : 1076
Version       : 1                Pkt Type  : 18        Pkt Ver   : 1
Attributes    : L1               Max Area  : 3
SysID Len     : 6                Used Len  : 159       Alloc Len : 178
TLVs :
Area Addresses      :
Area Address     : (01) 00
Area Address     : (03) 00.00.00
Supp Protocols      :
Protocols        : SPB
IS-Hostname         :
Hostname         : sw1
TE IS Neighbors     :
Neighbor         : e8e7.32c2.4e93  SPB Metric 10 Num of Ports 1 Port-Id 0x4
MT Capability       :
MT-ID : 0x0
SPB INSTANCE     :
CIST Root-ID: 0x0 0x0
CIST Ext Root Path Cost: 0x00000000  Bridge Priority: 0x8000
SPSourceID: 0x00113b7d (Auto)        Number of Trees: 6
[#1 ] ECT-algo:0x0080c201 baseVid: 4001 spVid:   0 usedByISID: 1(I-SID) mode: 1(SPBM)
[#2 ] ECT-algo:0x0080c202 baseVid: 4002 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#3 ] ECT-algo:0x0080c203 baseVid: 4003 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#4 ] ECT-algo:0x0080c204 baseVid: 4004 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#5 ] ECT-algo:0x0080c205 baseVid: 4007 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#6 ] ECT-algo:0x0080c206 baseVid: 4222 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
MT Capability       :
MT-ID : 0x0
SPB SVCID-UCAST-ADDR :
B-MAC e8.e7.32.81.3b.7d Base-VID 4001
[ISID# 1] 16776961 (T=1/R=1)
show spb isis database lsp-id  e8e7.3281.3b7d.00-00
Control Plane

<<<PAGE 79>>>
MONITORING SPB
• Displays the unicast forwarding information for a specified BVLANs 
• Bridge :01's Unicast forwarding table routes toward B-MACs :07, :03 
and :05 via interface 1/2 while its single hop paths are all direct
as can be seen from its FDB
B-MAC
44:55:66:77:00:0X
:04
:01
:05
:03
:07
:02
:06
1/1
1/2
1/3
1/1
1/2
1/3
1/4
1/5
1/6
1/1
1/2
1/3
1/1
1/2
1/3
1/1
1/2
1/3
1/1
1/2
1/3
1/1
1/2
1/3
ISID
1001
ISID
1001
ISID
1001
ISID
1001
Host A
Host B
Host C
Host D
SPB ISIS Unicast MAC Table:
Destination                       Outbound
BVLAN  (Name : MAC Address)                Interface
------+-----------------------------------+-----------
4001    BRIDGE-2 : 44:55:66:77:00:02
1/1/2
4001    BRIDGE-3 : 44:55:66:77:00:03 
1/1/2
4001    BRIDGE-4 : 44:55:66:77:00:04 
1/1/1
4001    BRIDGE-5 : 44:55:66:77:00:05 
1/1/2
4001    BRIDGE-6 : 44:55:66:77:00:06 
1/1/3
4001    BRIDGE-7 : 44:55:66:77:00:07 
1/1/2
MAC Addresses: 6
show spb isis unicast-table bvlan bvlan_id
Egress port to next hop
Control Plane

<<<PAGE 80>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 81>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Deploying a network based on SPB-M technology 
Contents 
1 
Objectives ...................................................................................... 2 
2 
Physical diagram .............................................................................. 2 
3 
Configure a SPB network for extending L2 connectivity. ................................ 3 
3.1. Creating the Backbone VLANs .................................................................... 3 
3.2. Defining the Control BVLAN ....................................................................... 3 
3.3. Configuring ISIS on network ports ................................................................ 4 
3.4. Activating ISIS protocol ............................................................................ 5 
3.5. Understanding SPB-M protocol operations ...................................................... 5

<<<PAGE 82>>>
2 
Lab: Deploying a network based on SPB-M technology 
 
 1 
Objectives 
This lab is designed to familiarize you with SPBM deployment and have a good understanding of SPBM 
configuration with the Alcatel-Lucent OmniSwitch family. 
First, you'll configure an example SPB backbone, using the figure below as a topology example. 
We will continue using this sample topology throughout the rest of this eBook. 
Nodes BEB-7 and BEB-8 are called “BEB” nodes because we will add services to these nodes later.  
Node BCB-1 and BCB-2 will remain a pure transit node and not terminate any service on first labs. 
A scenario for extending Layer 2 connections across a SPB-M service backbone network for Customer VLAN 2 
and VLAN 3 will be done on next lab. 
The SPB network is setup as a partial mesh, mainly to demonstrate the different flows that are possible. 
 
 2 
Physical diagram

<<<PAGE 83>>>
3 
Lab: Deploying a network based on SPB-M technology 
 
 3 
Configure a SPB network for extending L2 connectivity. 
If you observe this topology, you will notice that it provides up to 2 shortest paths, for example, 
between nodes BEB-7 and BEB-8, To take advantage of those 2 diverse paths for traffic load balancing, we 
need to create a minimum of 2 BVLANs. In this example, we will however, dedicate one BVLAN purely for 
control traffic and therefore we will create a total of 3 BVLANs. However, it should be noted that this is not 
strictly necessary, the control BVLAN can also be used for services. 
Backbone configuration entails the following tasks: 
- Creating one or more BVLANs with their associated ECT-IDs. ECT-IDs need not be explicitly defined, 
default ECT-IDs are applied 
- Defining the control BVLAN 
- Defining one or more SPB IS-IS interfaces 
- Enabling the SPB IS-IS protocol 
3.1. 
Creating the Backbone VLANs 
- On each node, create three backbone VLANs (BVLAN) 
-> spb bvlan 2000 
-> spb isis bvlan 2000 ect-id 1 
-> spb bvlan 2001 
 
-> spb isis bvlan 2001 ect-id 2 
-> spb bvlan 2002 
-> spb isis bvlan 2002 ect-id 3 
 
 
Notes 
BVLAN configuration and ECT algorithm assignment must match on each SPB bridge to ensure proper ISIS-SPB 
neighbour discovery and shortest path calculations throughout the backbone SPB network. 
When creating multiple BVLANs for each node, it is best practice to use different ECT algorithm for each BVLAN 
to maximize the traffic distribution.  
3.2. 
Defining the Control BVLAN 
- On each switch, configure the control BVLAN for management.  
-> spb isis admin-state disable  
-> spb isis control-bvlan 2000 
 
 
Notes 
Control BVLAN carries the ISIS PDUs which are single tagged with the chosen BVLAN ID. 
Control BVLAN can only be changed when protocol is disabled.  
There is no Spanning Tree on BVLANs

<<<PAGE 84>>>
4 
Lab: Deploying a network based on SPB-M technology 
 
3.3. 
Configuring ISIS on network ports 
Setup the ISIS protocol on appropriate network ports on every switch participating in SPB core network, 
accordingly to the physical connection between each node: 
 
 
Notes 
On system startup, ISIS is automatically loaded on the system without the need to enable the protocol like we 
do with OSPF and other protocols. 
-> spb isis interface port 1/1/5-6 
-> spb isis interface port 1/1/25 
-> interface port 1/1/5-6 admin-state enable 
-> interface port 1/1/25 admin-state enable 
-> spb isis interface port 1/1/5-6 
-> spb isis interface port 1/1/29 
-> interface port 1/1/5-6 admin-state enable 
-> interface port 1/1/29 admin-state enable 
-> spb isis interface port 1/1/5-6 
-> interface port 1/1/5-6 admin-state enable 
-> spb isis interface port 1/1/5-6 
-> interface port 1/1/5-6 admin-state enable 
 
 
Notes 
The ISIS interface can be a fixed port or a logical port (linkagg). When you configure the port as an ISIS SPB 
interface, it becomes the SPB network port, and the system will automatically add all BVLANs configured to the 
port. 
 
 
Question 
These interfaces are called « Network port » in SPB context. Before you enable ISIS in the next step, what is 
happening to these 4 nodes now in terms of L2 connectivity and Spanning Tree?  Is there a loop?  Should there 
be a blocking somewhere?

<<<PAGE 85>>>
5 
Lab: Deploying a network based on SPB-M technology 
 
3.4. 
Activating ISIS protocol  
On every SPB nodes, enable globally IS-IS SPB protocol: 
-> spb isis admin-state enable 
 
 
Notes 
Enabling ISIS-SPB on a switch starts the process of ISIS-SPB discovery, adjacency building, and shortest path 
tree calculations. Make sure that the SPBM configuration is set up first, then enable ISIS-SPB on each switch 
that will participate in the SPBM network. 
3.5. 
Understanding SPB-M protocol operations 
Let’s review this configuration with some show commands. 
 
 
Notes 
Refer to the CLI reference and Network Configuration Guides for detailed information about 
outputs. 
 
- Check the BVLANs and the associated ECT algorithm on each of the system.  
-> show spb isis bvlans 
-> show vlan id 
 
- Display the list of all the SPB interfaces configured for the system and their states.  
-> show spb isis interface 
 
- Displays the information about the SPB adjacencies on the system. 
Determine if ISIS SPB is in “UP” state then check the ISIS SPB neighbors on each of the equipment. 
-> show spb isis adjacency 
-> show spb isis adjacency detail 
 
- Display the global ISIS-SPB status and configuration information for the SPB bridge. 
-> show spb isis info 
 
- Verify the unicast addresses learned on each SPB switch in the ISIS-SPB backbone topology as well the 
outbound interface used when sending unicast traffic to other nodes. 
-> show spb isis unicast-table bvlan 2000 
-> show spb isis unicast-table bvlan 2001 
-> show spb isis unicast-table bvlan 2002 
 
- Checks the shortest path first (SPF) information to all known SPB bridges for a specific BVLAN (the 
outbound interface, the next hop node as well as the SPB metric and total number of hops 
required to reach a destination node) 
-> show spb isis spf bvlan 2000 
-> show spb isis spf bvlan 2000 bmac <BMAC> 
-> show spb isis spf bvlan 2001 
-> show spb isis spf bvlan 2001 bmac <BMAC> 
-> show spb isis spf bvlan 2002 
-> show spb isis spf bvlan 2002 bmac <BMAC> 
 
- Display information about the ISIS SPB topology database 
-> show spb isis database [lsp-id <lspid>] 
 
- Display the discovered node for all SPBM bridges participating in the topology. 
-> show spb isis nodes

<<<PAGE 86>>>
6 
Lab: Deploying a network based on SPB-M technology 
 
 
What commands would be used to determine the following? 
- 
System ID                                           -> _______________________________ 
- 
Destination @MAC/Name                    -> _______________________________ 
- 
Outbound interface                            -> _______________________________ 
- 
Next Hop switch                                 -> _______________________________ 
- 
SPB metric                                          > _______________________________ 
- 
Number of hops                                  -> _______________________________ 
- 
Neighbors list                                     -> _______________________________ 
 
Do the path are identical for each BVLAN? Explain the result.

<<<PAGE 87>>>
SHORTEST PATH BRIDGING MAC -IN-MAC (DATA PLANE)
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 88>>>
LESSON SUMMARY
✓SPB Data Plane (PBB-SPB) Services 
Data Plane (PBB-SPB) Configuration Steps

<<<PAGE 89>>>
SPB CONFIGURATION STEPS
Interfaces IS-IS
Services
Control Plane (NNI ports)
SPB Core level
On BEB + BCB 
UNP Access Port (Dynamic)
UNP Profiles (Dynamic)
Access Port
SAP
Data Plane (UNI ports)
SPB Access level
Only on BEB 
Access Port (Static)
SAP (Static/Dynamic)
Multi Access
P2P
Pseudo-wire
Service
BVLAN
Loopback Detection (LBD) (optional)
L2 Profiles (optional)

<<<PAGE 90>>>
SERVICES
UPDATE
• Layer 2 domain
• Traffic Isolation
• High performance
• Secure
• Not vulnerable to IP-based attacks
BEB
BEB
BEB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
Access
Node
Access
Node
BEB
ISID
1001
ISID
1001
SAP
ISID
1001
BVLAN
4001
SAP
SAP
BVLAN
1001
ISID
1002
SAP
ISID
1002
ISID
1002
SAP
BVLAN
4002
SAP
A Virtual Private Network for 
every department, 
company…
A Virtual Private Network for 
every department, Device 
type, company…
Data Plane

<<<PAGE 91>>>
SAP AND SERVICES
• Globally unique entity that bind sap port to a I-SID to B-VLAN
• Provides E-LAN connectivity for customer traffic and is identified by an I-SID 
SPB Network
SAP
SDP ID
Service 
I-SID 
1001
SAP
Service 
I-SID 
1002
SDP ID
Service 
I-SID 
1001
Service 
I-SID 
1002
SAP
SAP
DEMUX
DEMUX
BEB
BEB
Service Access Point
• UNI Sub-Interface
• Maps customer traffic to SPB Service (ISID)
• A logical term used for customer access point to the service 
• Mapped Traffic:
• All traffic
• All un-tagged traffic
• Specific VLAN tag or range
• Combination of inner & outer VLAN tags
• Near-end Customer MACs are bound to the SAP at the BEB’s 
MAC table
Service Distribution Point (SDP)
• NNI Sub-interface
• Logical transport 802.1ah tunnel between SPB nodes to 
transport service data
• Automatically & dynamically configured
• Logical forwarding links mapping remote BEBs
• Combination of BMAC & BVLAN
• Far-end Customer MACs are bound to dynamic SDPs that 
are created automatically to the far-end BEB nodes 
Service
Data Plane

<<<PAGE 92>>>
SERVICES
•
Maps I-SIDs to BVLANs
•
Create the services (ISID’s)
•
IS-IS distributes the information to all the nodes
•
All SPBM nodes (BEB/BCB) are aware of all the services and end-points
-> service service_id spb isid instance_id bvlan bvlan_id
[description desc_info] 
[multicast-mode {head-end*|tandem|hybrid}] 
[stats {enable|disable*}] 
[vlan-xlation {enable|disable*}] 
[admin-state {enable*|disable}] 
-> service spb 10 isid 1001 bvlan 4001
Create a Service
Services ISID to BVLAN Mapping
AOS support
• 1024 ISIDs/BVLAN
• 4094 VLANs per ISID
BVLAN
Interfaces IS-IS
Services
BEB
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
* Default values
Data Plane

<<<PAGE 93>>>
-> service service_id[-service_id2] spb isid instance_id[-instance_id2] bvlan bvlan_id[:x]
-> service spb 11-13 isid 1001-1003 bvlan 4001:3 
SERVICES
BEB
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
• Configure a range of three SPB service IDs (11, 12, 13)
• Configure a range of three SPB I-SIDs (1001, 1002, 1003) 
• Assign a range of three SPB BVLANs in sequence (bvlan_id [:x] )
•
Ex: where “x” is the number of BVLANs to assign in sequence (for example, 4001:3 
would assign BVLANs 4001, 4002, and 4003). 
Data Plane
Create a range of Services
BVLAN
Interfaces IS-IS
Services

<<<PAGE 94>>>
PSEUDO-WIRE SERVICES
UPDATE
• E-LINE connection between two local SAPs or between two SAPs across the SPB network.
• Also known as SPB Point-to-Point Transparent Circuit
• Transparent packets forwarding
• Each port or site is connected to an attachment point (SAP) of the two ends of the virtual wire
• No source @mac learning on the SAP
• Head-end multicast mode
• No Flooding and replication
SPB 
Network
BEB
BEB
SAP
I-SID 1000
I-SID 1000
SAP
CE-1
CE-2
BEB
CE-1
CE-2
I-SID 1000
SAP
SAP
Data Plane

<<<PAGE 95>>>
SPB Network
PSEUDO-WIRE SERVICES
➔service service_id spb isid instance_id[-instance_id2] bvlan bvlan_id[:x] [pseudo-wire {enable | disable} 
[e-tree {enable | disable} [description desc_info] 
Example :
➔service 100 spb isid 1000 bvlan 4000 pseudo-wire enable description "Pseudo-wire for ISID 1000" 
The SPB service will operate as a 
point-to-point (E-LINE) service. 
MAC address learning for the 
service is automatically turned off.
The SPB service will operate as a multipoint-to-
multipoint (E-LAN) service (default). 
MAC addresses for the service are learned. 
BEB
BEB
SAP
I-SID 1000
I-SID 1000
SAP
Data Plane
Create a Pseudo-wire Service
BVLAN
Interfaces IS-IS
Services

<<<PAGE 96>>>
ACCESS PORTS
• Allows VM traffic to enter and egress on this port
• Fixed port or Logical ports
• Enables Service Access Points (SAPs) to be configured on the ports 
• Static  Service or Dynamic UNP 
-> service access linkagg 5
-> service access port 1/1/3
Access Ports
Static or 
Dynamic (UNP)
BEB
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
Data Plane
Create Static Access Ports
BVLAN
Interfaces IS-IS
Services
Access ports

<<<PAGE 97>>>
SERVICE ACCESS POINT (SAP)
• Define what type of traffic is allowed to enter and exit from/to the SPB network
• A SAP is uniquely identified by the following:
• Physical Ethernet port
• Configured as an access port
• Encapsulation identifier (ID), such as VLAN ID, Q-tag.
• SAPs can only be created on access interfaces.
• Static or Dynamic SAPs
Service Access Point 
(SAP)
Access
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
Data Plane

<<<PAGE 98>>>
STATIC SAP
• A user can configure SAPs with different encapsulation types on the same access port
• Untagged, Tagged, QinQ
• Depending on the encapsulation used, a port can have more than one SAP associated with 
it.
• A switch can support either multiple services for one CVLAN, or one service for multiple 
CVLANs.
VLAN
10
VLAN
20
VLAN
30
Service Access Point (SAP)
Access
Customer Vlan
(CVLAN)
Q-tag
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
Data Plane

<<<PAGE 99>>>
-> service spb 1001 sap port 1/1/3:20
-> service spb 1002 sap port 1/1/2:all
-> service spb 1003 sap linkagg 5:500
Create SAPs
STATIC SAP
-> service spb 1001 sap port 1/1/3:20
-> service spb 1002 sap port 1/1/3:0
-> service spb 1002 sap port 1/1/3:10
-> service spb 1003 sap port 1/1/3:30.32
Create multiple SAPs on same port
SAPs
SPB
Network port
BEB
Service
1001 
Service
1003 
Service
1002 
Access Port
VLAN
10
VLAN
20
VLAN
30
VLAN
20
VLAN
30VLAN
31
VLAN
32
VLAN
10
Service Access Point (SAP)
BVLAN
4001
BVLAN
4002
BVLAN
4003
Access
Data Plane
BVLAN
Interfaces IS-IS
Services
Access ports

<<<PAGE 100>>>
SPB VLAN TRANSLATION
• Vlan-xlation feature changes the Vlan tag on edge switches UNI 
ports
SPB 
Network
BEB-1
BEB-2
SAP
I-SID 1001
I-SID 1001
SAP
VLAN 10
VLAN 20
-> service service_id vlan-xlation {enable | disable}
Configuring the status of egress VLAN translation for all SAPs 
associated with the specified service.
default: disable
-> service access {port chassis/slot/port[-port2] | linkagg agg_id[-agg_id2]}  vlan-xlation {enable | disable}
default: disable
service 1 spb isid 1001 bvlan 4001 vlan-xlation enable
service 1 vlan-xlation enable
service access port 1/1/1 vlan-xlation enable
service 1 sap port 1/1/1:10
1/1/1
1/1/1
service 1 spb isid 1001 bvlan 4001 vlan-xlation enable
service 1 vlan-xlation enable
service access port 1/1/1 vlan-xlation enable
service 1 sap port 1/1/1:20
Data Plane
SAPs
BVLAN
Interfaces IS-IS
Services
Access ports

<<<PAGE 101>>>
MONITORING SPB
• Displays the service instance identifier (I-SID) mapping for bridges participating in SPB 
topology
• Displays the Service Distribution Point (SDP) configuration for SPB services 
Legend: (*) dyn unicast object (+) remote mcast object (#) local mcast object
SPB SDP Info
FarEnd
Bind  FarEnd
SdpId
SysId:BVlan / GroupMac SourceId Oper Intf/Isid
Count SystemName / PortList
-------+-----------------------+--------+----+----------+-----+---------------------
32786*   e8e7.32a4.777d:4000    0x4777d   Up   1/1/8      0     sw8
32787*   e8e7.32a4.777d:4001    0x4777d   Up   1/1/8      1     sw8
32788*   e8e7.32a4.777d:4002    0x4777d   Up   1/1/8      1     sw8
Legend: * indicates locally configured ISID
SPB ISIS Services Info:
System
ISID      BVLAN   (Name : BMAC)                         MCAST(T/R)
------------+-------+--------------------------------------+-----------
*     1001     4001   sw8             : e8:e7:32:a4:77:7d
*     1001     4001   sw7             : e8:e7:32:c2:4e:93
*     1002     4002   sw1             : e8:e7:32:81:3b:7d
*     1002     4002   sw8             : e8:e7:32:a4:77:7d
*     1002     4002   sw7             : e8:e7:32:c2:4e:93
show spb isis services
show service sdp spb
SDP Detailed 32786 Info
SDP-Id         : 32786,               Description      : ,
Service Type   : SPB,                 SysId:BVlan
: e8e7.32a4.777d:2000,
Admin Status   : Up,                  Oper Status      : Up,
SDP Bind Count : 0,                   Allocation Type  : Dynamic,
Mgmt Change    : 10/01/2020 14:18:14, Status Change    : 10/01/2020 14:18:14
show service sdp 32786
Data Plane

<<<PAGE 102>>>
MONITORING SPB
• Checking status of SAP ports
• Monitoring the traffic forwarding on SAP ports
-> show service spb 1003 sap port 1/1/1:0
SAP Detailed Info
SAP Id           : 1/1/1:0,              Description      :
Admin Status     : Up,                   Oper Status      : Up,
Stats Status     : No,                   Vlan Translation : No,
Service Type     : SPB,                  Allocation Type  : Static,
Trusted          : Yes,                  Priority         : 0,
Ingress Pkts     : 0,                    Ingress Bytes    : 0,
Egress Pkts      : 0,                    Egress Bytes     : 0,
Mgmt Change      : 10/02/2020 15:10:42,  Status Change    : 10/02/2020 15:10:51
-> show service spb 2003
SPB Service Detailed Info
Service Id       : 1003,                 Description      :                    ,
ISID             : 1003,                 BVlan
: 4003,
Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0,
Admin Status     : Up,                   Oper Status      : Up,
Stats Status     : No,                   Vlan Translation : No,
Service Type     : SPB,                  Allocation Type  : Static,
MTU              : 9194,                 VPN IP-MTU       : 1500,
SAP Count        : 1,                    SDP Bind Count   : 2,
RemoveIngressTag : No,                   Option           : None,
Ingress Pkts     : 0,                    Ingress Bytes    : 0,
Egress Pkts      : 0,                    Egress Bytes     : 0,
Mgmt Change      : 10/02/2020 14:47:11,  Status Change    : 10/02/2020 14:47:11
show service spb service_id ports
show service spb service_id sap {slot/port | linkagg agg_num} [:0 | :all | :qtag1 :outer_qtag.inner_qtag]
Data Plane

<<<PAGE 103>>>
MONITORING SPB
Domain   Vlan/SrvcId[ISId/vnId]  Mac Address          Type      Operation    Interface
--------+----------------------+-------------------+----------+------------+---------------
SPB                   2003:2003  00:50:56:90:eb:3a
dynamic   servicing         sap:1/1/1
SPB                   2003:2003  00:50:56:90:45:05
dynamic   servicing    sdp:32789:2003
SPB                   2003:2003  e8:e7:32:81:3b:7d    dynamic   servicing    sdp:32801:2003
SPB                   2003:2003  e8:e7:32:81:3b:92    dynamic   servicing    sdp:32801:2003
SPB                   2004:2004  e8:e7:32:81:3b:92    dynamic   servicing    sdp:32801:2004
show mac-learning domain spb
Domain   Vlan/SrvcId[ISId/vnId]  Mac Address          Type      Operation    Interface
--------+----------------------+-------------------+----------+------------+---------------
SPB                   2003:2003 00:50:56:90:45:05
dynamic   servicing 
sap:1/1/1
SPB                   2003:2003 00:50:56:90:eb:3a
dynamic   servicing    sdp:32789:2003
SPB                   2003:2003 e8:e7:32:81:3b:7d
dynamic   servicing    sdp:32795:2003
SPB                   2003:2003 e8:e7:32:81:3b:92     dynamic   servicing    sdp:32795:2003
SPB                   2004:2004 e8:e7:32:81:3b:92     Dynamic   servicing    sdp:32795:2004
show mac-learning domain spb
@mac endpoints
SPB service_id: associated ISID number
Service Access Point (SAP) or the 
Service Distribution Point (SDP) 
associated with the MAC address
Local BEB
Remote BEB
DEMUX
32789
I-SID 2003
I-SID 1000
DEMUX
32789
BEB
BEB
SAP
1/1/1
SAP
1/1/1
SDP ID
32795
DEMUX
32795
00:50:56:90:45:05
00:50:56:90:eb:3a 
Data Plane

<<<PAGE 104>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 105>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Deploying a network based on SPB-M technology-L2 services 
Contents 
1 
Objectives ...................................................................................... 2 
2 
Physical diagram .............................................................................. 2 
3 
Logical diagram ................................................................................ 3 
4 
Configure a SPB network for extending L2 connectivity ................................. 4 
4.1. Creating VLANs on access switches .............................................................. 4 
4.2. Creating two SPB services ......................................................................... 5 
4.3. Configuring SPB access ports...................................................................... 5 
4.4. Setting up the SAP services ....................................................................... 6 
5 
Analysis and understanding the concept of SPB services ................................ 7 
5.1. Checking the configuration ....................................................................... 7 
5.2. Testing end device connectivity .................................................................. 7

<<<PAGE 106>>>
2 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 1 
Objectives 
In this lab, you will configure a scenario for extending Layer 2 connections across a SPB-M service backbone 
network for Customer VLAN 2 and VLAN 3. 
 
 2 
Physical diagram

<<<PAGE 107>>>
3 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 3 
Logical diagram 
Here is a simple SPB network to provide a good foundation to understand how SPBM works on the 
OmniSwitches. The SPB network is setup as a partial mesh, mainly to demonstrate the different flows that 
are possible.

<<<PAGE 108>>>
4 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 4 
Configure a SPB network for extending L2 connectivity 
A L2 service refers to a type of VPN service connecting multiple sites in a single any-to-any bridging domain. 
In this lab, we continue building upon the previous example and create a L2 service on top of the previously 
created backbone configuration. 
Services need only be created on BEBs, not on BCBs, and only on those BEBs where the service needs to be 
delivered.  
Creating an SPB service entails the following tasks: 
- Creating a service and associating the service to an IS-IS and BVLAN – the specified BVLAN’s SPF will be 
used for the service traffic. 
- Defining a Service Access Port (SAP) 
- Defining SAPs matching specific customer traffic 
 
- So, Configuration steps will be: 
1. 
Creating VLANs on access switches 
2. 
Create the Service Access Port 
3. 
Create the Service Access Profile (Optional) 
4. 
Create the Service I-SID 
5. 
Create the Service SAP 
4.1. 
Creating VLANs on access switches 
We will create two VLAN (2 and 3) on access switches OS6360 and on OS6560-A VLAN (2) distributed over SPB 
backbone network. 
These VLANs will be tagged over uplinks towards the backbone. So, proceed as follow: 
Switch 5 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> ip interface vlan2 address 192.168.2.5/24 vlan 2 
-> vlan 3  
-> vlan 3 members port 1/1/2 untagged 
-> ip interface vlan3 address 192.168.3.5/24 vlan 3 
-> vlan 2 members port 1/1/3 tagged  
-> vlan 3 members port 1/1/3 tagged 
-> interfaces 1/1/1-3 admin-state enable 
Switch 6 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> ip interface vlan2 address 192.168.2.6/24 vlan 2 
-> vlan 3  
-> vlan 3 members port 1/1/2 untagged 
-> ip interface vlan3 address 192.168.3.6/24 vlan 3 
-> vlan 2 members port 1/1/3 tagged  
-> vlan 3 members port 1/1/3 tagged 
-> interfaces 1/1/1-3 admin-state enable 
Switch 3 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> vlan 2 members port 1/1/7 tagged 
-> ip interface vlan2 address 192.168.2.3/24 vlan 2 
-> interfaces 1/1/1 admin-state enable 
-> interfaces 1/1/7 admin-state enable

<<<PAGE 109>>>
5 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
4.2. 
Creating two SPB services 
This step consists in configuring a Shortest Path Bridging (SPB) service and associates that service with a 
backbone service instance identifier (I-SID) and BVLAN. 
 
 
Notes 
- 
The service number is only locally significant and can differ across different BEBs. 
- 
The ISID number is globally significant and must match across all BEBs connecting a given service. 
- 
The BVLAN that the service is mapped must also match across all BEBs connecting a given service. 
- 
Different services can be mapped to different BVLANs to achieve traffic load balancing 
 
- On each of the BEB nodes, create two instances ISID 2001 and 2002 that will be associate respectively with 
the BVLANs 2001 and 2002.   
Switch 7 & 8 
-> service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable 
-> service spb 2002 isid 2002 bvlan 2002 description vlan3 admin-state enable 
 
 
Notes 
- 
ISID and BVLAN must be defined on all SPB network for network consistency. 
- 
Each SPB service is capable of learning customer MAC addresses from the access side (SAPs) and from the 
network side (Mesh SDP) and then switching the traffic based on this information. 
- 
Each ISID can be attached to one BVLAN only. 
4.3. 
Configuring SPB access ports 
 
- On each BEB nodes (OS6860-A and OS6860-B), configure the service access port(s) accordingly to the lab 
diagram.  The service access port(s) is the entry point of the LAN Access switch. (OS6360-A et OS6360-B 
vlan 2 and 3) 
 
 
Notes 
- 
Access ports are required to configure a SAP.  
The access port can be either a fixed port or logical port (linkagg). 
- 
A SAP is the point at which customer traffic enters and exits the service. SAPs are not configurable on other 
port types. 
Switch 7  
-> service access port 1/1/3 
-> interfaces 1/1/3 admin-state enable 
-> service access port 1/1/7 
-> interfaces 1/1/7 admin-state enable 
Switch 8 
-> service access port 1/1/3 
-> interfaces 1/1/3 admin-state enable

<<<PAGE 110>>>
6 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
4.4. 
Setting up the SAP services 
This will define the type of customer traffic that can enter the SPBM network.  
 
 
 
 
 
In this exercise, we will associate the Vlan2 traffic to the service 2001 and Vlan3 to the service 2002 on the 
BEB nodes. 
Classify the Vlan2 and Vlan3 traffic with the identifier 2 and 3 on the uplink port 
 
Switch 7  
-> service spb 2001 sap port 1/1/3:2 admin-state enable stats enable 
-> service spb 2002 sap port 1/1/3:3 admin-state enable stats enable 
-> service spb 2001 sap port 1/1/7:2 admin-state enable stats enable 
 
Switch 8 
-> service spb 2001 sap port 1/1/3:2 admin-state enable stats enable 
-> service spb 2002 sap port 1/1/3:3 admin-state enable stats enable 
 
 
Notes 
- 
A SAP ID is comprised of a customer-facing port (referred to as an access port) and an encapsulation value 
that is used to identify the type of customer traffic to map to the associated service. 
- 
Configuring SAPs with different encapsulation types for the same access port is allowed.

<<<PAGE 111>>>
7 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 5 
Analysis and understanding the concept of SPB services 
5.1. 
Checking the configuration 
- Display the information of the services configured  
Switch 7 & 8 
-> show spb isis services 
-> show service 
-> show service access 
-> show service spb 
-> show service sdp spb 
-> show service spb ServiceId ports  
-> show service mesh-sdp 
-> show service spb ServiceId debug-info 
-> show mac-learning 
 
 
Notes 
Refer to the CLI reference and Network Configuration Guides for detailed information about outputs. 
5.2. 
Testing end device connectivity 
From Virtual machines connected on the access switch, run some connectivity test between machines sharing 
the same SPB service (members of same Vlan). 
In addition to the ping requests and use of tracert application, use the following commands on BEB systems to 
verify the @MAC classified as well as the associated SAP. 
Test scenario 
- Open the clients (shortcut 
 on access POD desktop) 
- Use following VMs 
- PodXClient5 on OS6360-A port 1/1/1 
- PodXClient6 on OS6360-B port 1/1/1 
- PodXClient9 on OS6360-A port 1/1/2 
- PodXClient10 on OS6360-B port 1/1/2 
- PodXClient3 on OS6560-A port 1/1/1 
- Right-click on it then select Open console 
- For each of the VM client 
- Note the @MAC  
- Assign an IP address  
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.5 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.6 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.5 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.6 
PodXClient3 
Switch 3 
1/1/1 
2 
192.168.2.103 
192.168.2.3 
 
- In addition to the ping requests and use of tracert application, use the following commands on BEB 
systems to verify the @MAC classified as well as the associated SAP. 
 
-> show mac-learning domain spb 
-> show service spb 2001 sap port 1/1/3:2 
-> show service spb 2002 sap port 1/1/3:3 
...

<<<PAGE 112>>>
8 
Lab: Deploying a network based on SPB-M technology-L2 services 
 
 
- Example: 
 
sw7 (6860-A) -> show mac-learning domain spb 
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
        ID = ISID/Vnid/vplsid 
 
   Domain    Vlan/SrvcId[:ID]           Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
       SPB                2001:2001   00:0c:29:1a:13:68            dynamic    servicing               sap:1/1/3:2 
       SPB                2001:2001   94:24:e1:f0:f6:39            dynamic    servicing               sap:1/1/3:2 
       SPB                2001:2001   00:0c:29:44:aa:3b            dynamic    servicing               sap:1/1/7:2 
       SPB                2001:2001   2c:fa:a2:95:8f:9f            dynamic    servicing               sap:1/1/7:2 
       SPB                2001:2001   2c:fa:a2:95:8f:ac            dynamic    servicing               sap:1/1/7:2 
       SPB                2001:2001   00:0c:29:83:6f:85            dynamic    servicing            sdp:32775:2001 
       SPB                2001:2001   94:24:e1:f6:65:95            dynamic    servicing            sdp:32775:2001 
       SPB                2001:2001   94:24:e1:f6:65:9e            dynamic    servicing            sdp:32775:2001 
       SPB                2002:2002   00:0c:29:31:0f:97            dynamic    servicing               sap:1/1/3:3 
       SPB                2002:2002   94:24:e1:f0:f6:39            dynamic    servicing               sap:1/1/3:3 
       SPB                2002:2002   94:24:e1:f0:f6:42            dynamic    servicing               sap:1/1/3:3 
       SPB                2002:2002   00:0c:29:ed:d0:4a            dynamic    servicing            sdp:32776:2002 
       SPB                2002:2002   94:24:e1:f6:65:95            dynamic    servicing            sdp:32776:2002 
       SPB                2002:2002   94:24:e1:f6:65:9e            dynamic    servicing            sdp:32776:2002 
 
 Total number of Valid MAC addresses above = 14 
 
You have now completed this lab.

<<<PAGE 113>>>
SHORTEST PATH BRIDGING (PBB -SPB) SERVICES 
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 114>>>
LESSON SUMMARY
✓SPB Data Plane (PBB-SPB) Services 
Layer 2 Control Frame Profiles
Loop Detection (LBD)

<<<PAGE 115>>>
LAYER 2 PROFILES
• Specify treatment of control packets on SAP ports 
• Associated with each SAP port
• Applied to incoming traffic on an access port
• Default profile: def-access-profile
• Peer:  Interact with the peer switch according to the protocol
• Drop: discards unconditionally the specified PDU
• Tunnel: Control packet encapsulated across the provider network
CVLAN
Tagged
CVLAN
Untagged
Access
Port
Control Frames
B
P
D
U
Tunnel
SPB
network
Peer
BEB
Drop
L2 Protocol
Default Treatment
STP
Tunnel
802.1X
Drop
802.1AB
Drop
802.3AD
Peer
GVRP 
Tunnel
AMAP
Drop
MVRP
Tunnel
Data Plane

<<<PAGE 116>>>
LAYER 2 PROFILES
L2 Protocol
PEER
DROP
TUNNEL
Default Treatment
STP
NO
YES
YES
Tunnel
802.1X
NO
YES
YES
Drop
802.1AB
YES
YES
YES
Drop
802.3AD
YES
NO
NO
Peer
GVRP 
NO
YES
YES
Tunnel
AMAP
YES
YES
YES
Drop
MVRP
NO
YES
YES
Tunnel
Data Plane
Access ports
BVLAN
Interfaces IS-IS
Services
SAPs
L2 Profiles
Service l2profile l2profile_name [inbound {tagged|untagged| both}] [stp|802.1x|802.3ad|802.1ab|gvrp|amap|mvrp] [tunnel|peer|drop]
1. Configuring a Layer2 profile
service access {port chassis/slot/port[-port2] | linkagg agg_id[-agg_id2]} l2profile {default | profile-name}
2. Assign a Layer2 profile to a service access port

<<<PAGE 117>>>
IEEE 802.1AB TRAFFIC
A service manager L2 profile provides an “inbound” option 
to specify a separate action for 802.1AB tagged and 
untagged traffic.
L2 Protocol
PEER
DROP
TUNNEL
Default Treatment
802.1AB
YES
YES
YES
Drop
service l2profile l2profile_name inbound {tagged | untagged| both} 802.1ab  {tunnel|peer|drop}
Configuring Layer2 profile for 802.1ab traffic
Data Plane
Access ports
BVLAN
Interfaces IS-IS
Services
SAPs
L2 Profiles

<<<PAGE 118>>>
SAP AND QOS
• SPB uses Class of Service (CoS) mechanism 
• Traffic is classified at the SAP level
• Highest priority assigned to untagged tunnelled L2 
Control BPDUs 
• No further classification within the SPB backbone due 
to MAC-in-MAC encapsulation
Default classification 802.1p
Tagged traffic: CoS marking from incoming VLAN tag 
onto BVLAN tag
Untagged traffic: the port’s default priority is used
Trusted SAPs
Set the CoS marking to a user-defined value
Untrusted SAPs
Data Plane

<<<PAGE 119>>>
LOOPBACK DETECTION (LBD)

<<<PAGE 120>>>
LOOPBACK DETECTION (LBD)
• Automatically Loop detection
• Prevents loops on ports having forwarded network traffic which has looped back to the originating 
switch
• No need of STP/RSTP/MSTP
• Periodically sends out frames from all loopback detection enabled ports
• Based on specific multicast frames
•
D-MAC: ALU proprietary MAC 0x01-20-DA-02-01-71
•
S-MAC: Individual Port MAC
• Available on bridge or service access ports (port/linkagg)
• Actions
• Port shutdown
• Trap
• Event log
• Port recovery
• Automatically after a configurable timer or manually
L2 switch
SPB Backbone
SAP
SAP
BEB-B
BEB-A

<<<PAGE 121>>>
-> loopback-detection enable
LBD SERVICE ACCESS PORT CONFIGURATION
Enable Loopback Detection globally on the switch
Enable LBD protocol on an access port
View the LBD statistics on a port
Loopback Detection (LBD)
Access Port
BVLAN
Interfaces IS-IS
Services
SAP
L2 Profiles
-> loopback-detection service access port 1/1/7 enable
-> show loopback-detection statistics port 1/1/7

<<<PAGE 122>>>
LBD SERVICE ACCESS PORT
• Switch A and B are AOS switches running enhanced loopback-detection
• Switch C is a legacy switch or a non-AOS switch
-> show loopback-detection
Global LBD Status                : enabled,
Global Remote-origin LBD Status  : enabled,
Global LBD Transmission Timer    : 10 sec,
Global LBD Auto-recovery Timer   : 300 sec,
Display LBD Status
Port in switch with highest BridgeID is shut down
SPB 
Backbone
BEB-A
BEB-B
Port with highest PortID is shut down
SPB 
Backbone
BEB-A
BEB-B
SPB 
Backbone
Port in switch with highest BridgeID is shut down
BEB-A
BEB-B

<<<PAGE 123>>>
LBD SERVICE ACCESS PORT
• Switch A has higher bridge identifier
• Configuration ports 1/1/7 and 1/1/8
• SAP ports with same ISID and path cost
• Loopback-detection enabled with option “service-access”
-> show loopback-detection port 1/1/7
Global LBD Status                 : enabled,
Global Remote-origin LBD Status   : enabled,
Global LBD Transmission Timer     : 10 sec,
Global LBD Auto-recovery Timer    : 300 sec,
Port LBD Status                   : enabled,
Port Remote-origin LBD Status     : disabled,
Port LBD State                    : ShutDown,
Port LBD Type                     : service-edge,
Checking LBD status on port 1/1/7  (BEB1)
In case the 2 SAP ports are on the same switch, port 1/1/8 is shutdown as this interface has higher port identifier
2020 May 31 01:44:55 sw7 swlogd: intfNi Drv info(5) eniPhyPortEnable(2020):IND:gport:6 1/0/7 portEnable:Disable autoNeg:Disable portAdv:0x0
2020 May 31 01:44:55 sw7 swlogd: portMgrCmm main info(5) pvr trap: Violation set, chass 1, slot 1, port 7: source LBD, reason lbd shutdown
2020 May 31 01:44:57 sw7 swlogd: portMgrNi main info(5) : [pmnHALLinkStatusCallback:216] LINKSTS 1/1/7 DOWN (gport 0x6) Speed 0 Duplex HALF
2020 May 31 01:44:57 sw7 swlogd: vfcn main info(5) [vfccQsHandleLinkEvents:487] 1/1/7 LINK DOWN
2020 May 31 01:44:57 sw7 swlogd: stpNi _SOKt info(5) stpnimsg_processMsgFromPM: PM_LINK_STATUS_MSGID gPort=x6 linkStatus=0
2020 May 31 01:44:57 sw7 swlogd: intfNi Drv info(5) niEsmHandleEvent: current NI state:RUNNING event:8
2020 May 31 01:44:57 sw7 swlogd: intfNi Drv info(5) niEsmSendLinkStatusChgMsg(796): linkstatus DOWN sent on peerId=1
2020 May 31 01:44:57 sw7 swlogd: intfCmm Mgr info(5) cmmEsmHandleNiMsg: Rx CMM_ESM_LINK_STATUS_CHG from chassis 1 NI 1
X
System Id 
e8e7.32cd.63d3
System Id
e8e7.32d4.850d
A
B
1/1/7
1/1/8
C
SPB Backbone
BEB-B
BEB-A
L2 switch
SAP
SAP

<<<PAGE 124>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 125>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: SPB protocol Analysis 
Contents 
1 
Objectives ...................................................................................... 2 
2 
Physical diagram .............................................................................. 2 
3 
Logical diagram ................................................................................ 3 
4 
Analysis and understanding the concept of SPB services ................................ 3 
4.1. Testing Network Resiliency ....................................................................... 3 
4.2. Modifying SPB Path Cost ........................................................................... 5 
4.3. Overload state mechanism ........................................................................ 6 
5 
Loopback Detection ........................................................................... 7 
6 
Control Frames behavior ................................................................... 10

<<<PAGE 126>>>
2 
Lab: SPB protocol Analysis 
 
 1 
Objectives 
This lab is based on the previous exercise “Deploying a network based on SPB-M technology”. 
You will setup optional SPB parameters to customize the network behaviour, deploy a multipoint SPB 
topology feature then, learn how to protect a SPB based network. 
 
 
 2 
Physical diagram

<<<PAGE 127>>>
3 
Lab: SPB protocol Analysis 
 
 3 
Logical diagram 
 
 4 
Analysis and understanding the concept of SPB services 
4.1. 
Testing Network Resiliency 
- Perform some basic tests of failover in the SPBM network. 
- Monitor the rerouting of sessions between the clients. 
1. Identify the interface selected by SPB IS-IS on node 7 to join the node 8 for all BVLANs. 
2. Determine the outbound port used by Client 5 or Client 9. 
3. Run a permanent ping between Clients 5 and 6 (and/or Clients 9 and 10) 
 
Example (connectivity test between client 5 and 6) 
 
 
-> show spb isis unicast-table 
 
SPB ISIS Unicast MAC Table: 
        Destination                              Outbound 
 BVLAN  (Name : MAC Address)                     Interface 
------+----------------------------------------+----------- 
  2000  Pod21sw1            : 78:24:59:2b:32:ab      1/1/5 
  2000  Pod21sw8            : 94:24:e1:e8:b4:13      1/1/5 
  2000  Pod21sw2            : e8:e7:32:77:f6:b9      1/1/6 
  2001  Pod21sw1            : 78:24:59:2b:32:ab      1/1/5 
  2001  Pod21sw8            : 94:24:e1:e8:b4:13      1/1/6 
  2001  Pod21sw2            : e8:e7:32:77:f6:b9      1/1/6 
  2002  Pod21sw1            : 78:24:59:2b:32:ab      1/1/5 
  2002  Pod21sw8            : 94:24:e1:e8:b4:13      1/1/6 
  2002  Pod21sw2            : e8:e7:32:77:f6:b9      1/1/6 
 
MAC Addresses: 9

<<<PAGE 128>>>
4 
Lab: SPB protocol Analysis 
 
For instance, here for Vlan 2 traffic attached to SPB service 2001 
 
-> show spb isis unicast-table 
SPB ISIS Unicast MAC Table: 
        Destination                              Outbound 
 BVLAN  (Name : MAC Address)                     Interface 
------+----------------------------------------+----------- 
---omitted lines--- 
  2001  Pod11sw1            : e8:e7:32:81:39:d9      1/1/5 
  2001  Pod11sw2            : e8:e7:32:94:54:4d      1/1/6 
  2001  Pod11sw8            : e8:e7:32:cd:57:f3      1/1/6 
---omitted lines--- 
 
-> show spb isis spf bvlan 2001 
SPB ISIS Path Table: 
 Destination                              Outbound   Next Hop                                SPB     Num 
 (Name : BMAC)                            Interface  (Name : BMAC)                           Metric  Hops 
----------------------------------------+----------+----------------------------------------+------+------ 
 Pod21sw1            : e8:e7:32:81:39:d9      1/1/5  Pod21sw1            : 78:24:59:2b:32:ab     10    1 
 Pod21sw8            : e8:e7:32:cd:57:f3      1/1/6  Pod21sw2            : e8:e7:32:77:f6:b9     20    2 
 Pod21sw2            : e8:e7:32:94:54:4d      1/1/6  Pod21sw2            : e8:e7:32:77:f6:b9     10    1 
 
4. Disable the appropriate interface on switch 7 into the direction of switch 8. 
5. Check the ping test. 
6. Identify the interface selected and the path to switch 8 
 
-> show spb isis unicast-table 
SPB ISIS Unicast MAC Table: 
        Destination                              Outbound 
 BVLAN  (Name : MAC Address)                     Interface 
------+----------------------------------------+----------- 
  2000  Pod21sw1            : 78:24:59:2b:32:ab      1/1/5 
  2000  Pod21sw8            : 94:24:e1:e8:b4:13      1/1/5 
  2000  Pod21sw2            : e8:e7:32:77:f6:b9      1/1/5 
  2001  Pod21sw1            : 78:24:59:2b:32:ab      1/1/5 
  2001  Pod21sw8            : 94:24:e1:e8:b4:13      1/1/5 
  2001  Pod21sw2            : e8:e7:32:77:f6:b9      1/1/5 
  2002  Pod21sw1            : 78:24:59:2b:32:ab      1/1/5 
  2002  Pod21sw8            : 94:24:e1:e8:b4:13      1/1/5 
  2002  Pod21sw2            : e8:e7:32:77:f6:b9      1/1/5 
 
7. Enable the port on switch 7 before to go ahead.

<<<PAGE 129>>>
5 
Lab: SPB protocol Analysis 
 
4.2. 
Modifying SPB Path Cost 
Let now see how the path cost related to SPB network ports may affect the shortest path tree (SPT) 
calculations. 
1. Identify SPB Path between Client 5 and 6 
Use the following commands to determine the path in use between clients 5 and 6. 
 
 
Notes  
The following displays are shown here as an example and may not reflect your network. 
Switch 7 & 8 
-> show mac-learning 
---omitted lines--- 
       SPB                2001:2001   00:50:56:90:c5:3a     dynamic    servicing        sap:1/1/3:2 
       SPB                2001:2001   00:50:56:90:8b:c3     dynamic    servicing        sdp:32770:2001 
---omitted lines--- 
 
-> show spb isis unicast-table bvlan 2001 
SPB ISIS Unicast MAC Table: 
        Destination                              Outbound 
 BVLAN  (Name : MAC Address)                     Interface 
------+----------------------------------------+----------- 
  2001  Pod11sw1            : e8:e7:32:81:39:d9      1/1/5 
  2001  Pod11sw2            : e8:e7:32:94:54:4d      1/1/6 
  2001  Pod11sw8            : e8:e7:32:cd:57:f3      1/1/6 
 
-> show spb isis spf bvlan 2001 
 
SPB ISIS Path Table: 
 Destination                              Outbound   Next Hop                                SPB     Num 
 (Name : BMAC)                            Interface  (Name : BMAC)                           Metric  Hops 
----------------------------------------+----------+----------------------------------------+------+------ 
 Pod11sw1            : e8:e7:32:81:39:d9      1/1/5  Pod11sw1            : e8:e7:32:81:39:d9     10    1 
 Pod11sw2            : e8:e7:32:94:54:4d      1/1/6  Pod11sw2            : e8:e7:32:94:54:4d     10    1 
 Pod11sw8            : e8:e7:32:cd:57:f3      1/1/6  Pod11sw2            : e8:e7:32:94:54:4d     20    2 
 
2. Change the Path Cost of the corresponding link, to force the traffic to go a shorter/cheaper path. 
Switch 7 
-> spb isis interface port 1/1/6 metric 40 
Switch 8 
-> spb isis interface port 1/1/6 metric 40 
 
 
Notes  
If the SPB interface metric value is set to a different value for each side of a link, the highest 
metric value is applied to the entire link. 
 
3. Identify and comment SPB Path between Client 5 and 6 then explain the changes. 
Switch 7 
-> show spb isis spf bvlan 2001 
SPB ISIS Path Table: 
 Destination                              Outbound   Next Hop                                SPB     Num 
 (Name : BMAC)                            Interface  (Name : BMAC)                           Metric  Hops 
----------------------------------------+----------+----------------------------------------+------+------ 
 Pod11sw1            : e8:e7:32:81:39:d9      1/1/5  Pod11sw1            : e8:e7:32:81:39:d9     10    1 
 Pod11sw2            : e8:e7:32:94:54:4d      1/1/5  Pod11sw1            : e8:e7:32:81:39:d9     20    2 
 Pod11sw8            : e8:e7:32:cd:57:f3      1/1/5  Pod11sw1            : e8:e7:32:81:39:d9     30    3

<<<PAGE 130>>>
6 
Lab: SPB protocol Analysis 
 
Switch 8 
-> show spb isis spf bvlan 2001 
SPB ISIS Path Table: 
 Destination                              Outbound   Next Hop                                SPB     Num 
 (Name : BMAC)                            Interface  (Name : BMAC)                           Metric  Hops 
----------------------------------------+----------+----------------------------------------+------+------ 
Pod11sw1            : e8:e7:32:81:39:d9      1/1/5  Pod11sw2            : e8:e7:32:94:54:4d     20    2 
Pod11sw2            : e8:e7:32:94:54:4d      1/1/5  Pod11sw2            : e8:e7:32:94:54:4d     10    1 
Pod11sw7            : e8:e7:32:d4:88:95      1/1/5  Pod11sw2            : e8:e7:32:94:54:4d     30    3 
 
4. Before to continue, change Cost back to get Equal Costs. 
Switch 7 & 8 
-> spb isis interface port 1/1/6 metric 10 
 
5. You can do the same test for clients 4 and 9 after having identified the SPB Path. 
4.3. 
Overload state mechanism 
- The Overload state mechanism allows ISIS-SPB to inform its neighbors that the ISIS instance is nearing or 
exceeding its capabilities. When peers see that a switch is advertising in this state, they will select an 
alternate path around the overloaded switch. 
- During normal operation, the router may be forced to enter an overload state due to a lack of resources. 
When in the overload state, the router is used only if the destination route is directly reachable by the 
router (for example, it will not be used for other transit traffic). 
- However, it is possible to manually trigger the overload state condition using the “spb isis overload” 
command.  
 
1. Run a permanent ping between Clients 5 and 6. 
2. Identify SPB Path between Client 5 and 6.  
3. Enable “Overload State” on the OS6900 that is inside the Path.  
 
-> spb isis overload timeout 120 
 
 
Notes  
The router remains in the overload state during a period defined by the timeout interval. 
This command can be used when the router is overloaded or before executing a shutdown command to divert 
traffic around the router. 
 
4. Check again the SPB Path between the two clients. 
5. Observe the Ping between Client 5 and 6. What happens? 
 
 
Notes  
ISIS-SPB switch can also operate in the overload state after a system bootup for a specified 
amount of time. 
-> spb isis overload-on-boot [timeout seconds]

<<<PAGE 131>>>
7 
Lab: SPB protocol Analysis 
 
 5 
Loopback Detection 
Loopback Detection (LBD) automatically detects and prevents L2 forwarding loops on an access port. 
When a loopback is detected, the port is disabled and goes into a shutdown state. A trap is sent, and the 
event is logged. 
Configure Loopback Detection on BEB switch 7 and 8: 
1. Enable Loopback Detection globally 
2. Enable Loopback Detection on access port. 
 
 
Notes  
When loopback is detected on any one of the Linkagg port, all the ports of the Linkagg 
will be shut down due to loopback detection. 
 
 
 
1. Create a SAP on Switch 8 port 1/1/4 for Service 2001  
Switch 8 
-> service access port 1/1/4 
-> service spb 2001 sap port 1/1/4:2 admin-state enable stats enable 
 
2. Tag the User VLANs on Switch 5 port 1/4 
Switch 5 
-> vlan 2 members port 1/1/4 tagged 
 
3. Disable Spanning Tree on Switch 5 Vlan 2  
Switch 5 
-> spantree vlan 2 admin-state disable

<<<PAGE 132>>>
8 
Lab: SPB protocol Analysis 
 
4. Activate Port 4 between Switch 8 and 5.  
Switch 8 
-> interfaces 1/1/4 admin-state enable 
Switch 5 
-> interfaces 1/1/4 admin-state enable 
 
5. Check that a loop has been created 
Client 5 is learned on both switches 7 and 8 on access port 
Switch 7 
-> show mac-learning port 1/1/3 
 
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
       SPB                2001:2001   00:50:56:90:8b:c3            dynamic    servicing               sap:1/1/3:2 
       SPB                2001:2001   00:50:56:90:e9:df            dynamic    servicing               sap:1/1/3:2 
       SPB                2001:2001   2c:fa:a2:05:cd:71            dynamic    servicing               sap:1/1/3:2 
       SPB                2002:2002   00:50:56:90:2a:18            dynamic    servicing               sap:1/1/3:3 
Switch 8 
-> show mac-learning port 1/1/4 
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
       SPB                2001:2001   00:50:56:90:e9:df            dynamic    servicing               sap:1/1/4:2 
 
Ping between Client 5 & 6 is not operational anymore 
 
 
 
 
 
6. Enable Loopback Detection Protocol (LBD) on Switch 7 and 8 and on access ports 
Switch 7 
-> loopback-detection enable 
-> loopback-detection service-access port 1/1/3 enable

<<<PAGE 133>>>
9 
Lab: SPB protocol Analysis 
 
Switch 8 
-> loopback-detection enable 
-> loopback-detection service-access port 1/1/4 enable 
 
7. Verify the LBD configuration on the access ports 
Switch 7 
 
-> show loopback-detection port 1/1/3 
Global LBD Status                  : enabled, 
Global Remote-origin LBD Status    : disabled, 
Global LBD Transmission Timer      : 30 sec, 
Global LBD Auto-recovery Timer     : 300 sec, 
Port LBD Status                    : enabled, 
Port Remote-origin LBD Status      : -, 
Port LBD State                     : Normal, 
Port LBD Type                      : service-edge, 
 
-> show loopback-detection statistics port 1/1/3 
LBD Port Statistics 
LBD Packet Send               : 148, 
Invalid LBD Packet Received   : 0, 
Member of Link Aggregation    : -, 
 
8. Check for the Loop has been resolved? 
 
You should get this output (here is an example and may not match your network behaviour) 
Switch 8 
 
-> show loopback-detection port 1/1/4 
Global LBD Status                  : enabled, 
Global Remote-origin LBD Status    : enabled, 
Global LBD Transmission Timer      : 30 sec, 
Global LBD Auto-recovery Timer     : 300 sec, 
Port LBD Status                    : enabled, 
Port Remote-origin LBD Status      : -, 
Port LBD State                     : ShutDown, 
Port LBD Type                      : service-edge, 
 
• 
Check for connectivity between clients 5 and 6. 
• 
Discover and explain which access port has been blocked? 
 
9. Before to continue, remove Vlan 2 configuration on Switch 5 and Switch 8. 
Switch 5 
-> spantree vlan 2 admin-state enable 
-> no vlan 2 members port 1/1/4  
-> interfaces 1/1/4 admin-state disable 
-> write memory 
Switch 8 
-> service spb 2001 no sap port 1/1/4:2 
-> no service access port 1/1/4 
-> interfaces 1/1/4 admin-state disable 
-> write memory

<<<PAGE 134>>>
10 
Lab: SPB protocol Analysis 
 
 6 
Control Frames behavior 
A Layer 2 profile determines how control frames entering on an access port are processed. 
When a port is configured as an access port, a default Layer 2 profile (L2profile) is applied to the port with 
default values for processing different type of control frames. 
 
 
Notes 
For a static access port, L2Profile is def-access-profile 
For a dynamic access port, L2profile is unp-def-access-profile 
 
1. Display the default L2profile 
Switch 7 
-> show service l2profile 
Legend: (*)In-use by UNP 
 
                                                                                                       802.1AB    802.1AB     802.1AB 
   Profile Name             STP        802.1X       802.3AD      MVRP         GVRP          AMAP        Both       Tagged     Untagged 
-----------------------+------------+------------+------------+------------+------------+------------+----------+----------+----------- 
def-access-profile      tunnel        drop         peer         tunnel       tunnel       drop         drop            -            - 
unp-def-access-profile*  drop          peer        peer         tunnel       tunnel       drop         drop         -         - 
 
2. In our case, the def-access-profile tunnels GVRP frames. We will create a new profile “Drop-GVRP” that 
will discard the GVRP traffic ingressing the access port. 
 
- Create the profile 
 Switch 7 & 8 
-> service l2profile Drop-GVRP GVRP drop 
 
-> show service l2profile 
Legend: (*)In-use by UNP 
 
                                                                                                       802.1AB    802.1AB     802.1AB 
   Profile Name             STP        802.1X       802.3AD      MVRP         GVRP          AMAP        Both       Tagged     Untagged 
-----------------------+------------+------------+------------+------------+------------+------------+----------+----------+----------- 
Drop-GVRP               tunnel        drop         peer         tunnel       drop         drop         drop           -            - 
def-access-profile      tunnel        drop         peer         tunnel       tunnel       drop         drop           -            - 
unp-def-access-profile*  drop          peer         peer         tunnel       tunnel       drop         drop           -            - 
 
- Apply the new profile to the access ports 
Switch 7 & 8 
-> service access port 1/1/3 l2profile Drop-GVRP 
 
- Check the configuration has been applied 
Switch 7 & 8 
-> show service access port 1/1/3 
Port       Link  SAP     SAP     Vlan 
Id        Status Type    Count   Xlation L2Profile                        Description 
---------+------+-------+-------+-------+--------------------------------+--------------------------------- 
1/1/3       Up    Manual    2       N       Drop-GVRP 
 
Total Access Ports: 1 
You have now completed this lab.

<<<PAGE 135>>>
SHORTEST PATH BRIDGING BUM TRAFFIC FLOWS & 
TROUBLESHOOT
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 136>>>
LESSON SUMMARY
✓SPB Data Plane (PBB-SPB) Services 
BUM Traffic Flows
SPB Troubleshooting

<<<PAGE 137>>>
BUM TRAFFIC FLOWS

<<<PAGE 138>>>
MULTICAST FORWARDING
• BUM = Broadcast Unknown Multicast
• ARPs packets, Boot-p/DHCP requests, etc.
• SPBM supports two BUM traffic distribution methods for replicating and forwarding 
multicast frames
• Head-End (native mode)
• Tandem (optimized)

<<<PAGE 139>>>
HEAD-END REPLICATION MODE 
• Sparse community of interest 
• Low Multicast bandwidth
• Multicast frames are replicated at the ingress BEB
• One copy of each packet is sent to each BEB where the ISID 
exists
• The replicas are encapsulated with the destination BEB’s 
BMAC
• Multicast traffic follows Unicast tree and uses the same FDB
Layer 2 Service 
BMAC :01
BCB
BEB
BMAC :13
BEB
BMAC :11
BMAC :03
BEB
BCB
BMAC :02
BEB
BMAC :04
BCB
BMAC :05
ISID 
1001
ISID 
1001
ISID 
1001
ISID 
1001
Host A
Host B
Host C
Host D
B-VID 4001
Ethertype 802.1 ad
SA BMAC :11
DA BMAC :03
B-VID 4001
Ethertype 802.1 ad
SA BMAC :11
DA BMAC :04
B-VID 4001
Ethertype 802.1 ad
SA BMAC :11
DA BMAC :13
BEB 3
CORE 1
BEB 1
BEB 2
BEB 4
CORE 2
• Node :11's sends 3 frames to each Node
• 1 frame for node :03,
• 1 frame for node :04
• 1 frame for node :13
• Node :05 is the primary path and 
will provide replication services
Core 5
-> show service 20
SPB Service Detailed Info
Service Id       : 20,             Description       : Training
ISID             : 1001,            BVlan
: 4001,
Multicast-Mode   : Headend,         Tx/Rx Bits       : 1/1,
Admin Status     : Up,              Oper Status      : Up,
--- omitted lines ---

<<<PAGE 140>>>
TANDEM (S,G) REPLICATION MODE 
• For every ISID, each bridge builds a source specific multicast trees (S,G)
• Using special destination Multicast Group B-MAC
• Replicate and forward the BUM traffic
• Every node is the root of the tree and computes Multicast Tree per service
• More bandwidth-efficient
• BUM traffic uses Multicast Group (S,G) per source per ISID
• Node :11's sends 1 frame to Node :01 with a B-DA of its SPSourceID
Intermediate nodes on the shortest path 
only install group B-MAC 
Layer 2 Service 
BMAC :05
BCB
BEB
BMAC :13
BEB
BMAC :11
BMAC :03
BEB
BCB
BMAC :02
BEB
BMAC :04
BCB
BMAC :01
ISID 
1001
ISID 
1001
ISID 
1001
ISID 
1001
Host A
Host B
Host C
Host D
BEB 3
CORE 5
BEB 1
BEB 2
BEB 4
CORE 2
CORE 1
B-VID 4001
Ethertype 802.1 ad
SA BMAC :11
DA BMAC 03:00:11:00:01:90
-> show spb isis multicast-table
Legend: MCAST Source * indicates any source in GMODE bvlans
SPB ISIS Multicast MAC Table:
MCAST Source                      Inbound     Outbound
ISID   BVLAN  MCAST Group Address (Name : BMAC)                     Interface   Interfaces
------+-------+-------------------+---------------------------------+----------+-----------
1001   4001   63:15:81:00:07:d1  BEB1          : e8:e7:32:f6:15:11             1/1/10
1001   4001   c3:23:b3:00:07:d1  BEB3          : e8:e7:32:fc:23:03  1/1/10
1001   4001   c3:23:b3:00:07:d1  BEB4          : e8:e7:32:fc:23:04  1/1/10
1001   4001   c3:23:b3:00:07:d1  BEB2          : e8:e7:32:fc:23:13  1/1/10
MAC Addresses: 4
-> show service 20
SPB Service Detailed Info
Service Id       : 20,                 Description        : Training
ISID             : 1001,                 BVlan
: 4001,
Multicast-Mode   : Tandem,               Tx/Rx Bits       : 1/1,
Admin Status
: Up,                   Oper Status
: Up,
--- omitted lines ---

<<<PAGE 141>>>
TANDEM (*,G) REPLICATION MODE 
• For every BVLAN, each bridge builds a source specific multicast tree
• Create a shared multicast distribution tree per BVLAN
• Node with lowest bridge ID used as Root Bridge of the tree for all BVLANs
• BUM traffic forwarded along the shared tree
• Less resource usage 
-> show spb isis bvlans
SPB ISIS BVLANS:
Services  Num
Tandem     Root Bridge
BVLAN   ECT-algorithm
In Use  mapped
ISIDS  Multicast  (Name : MAC Address)
-------+-----------------+-------+---------+------+----------+-------------------------------
--
4001  00-80-c2-01       YES     NO            1    SGMODE
4002  00-80-c2-02       YES     YES
1    GMODE      Core5     : 2c:fa:a2:05:cd:05
4003  00-80-c2-03       YES     YES
1    GMODE      Core5     : 2c:fa:a2:05:cd:05
BVLANs:     3
Intermediate nodes on the shortest path 
only install group B-MAC 
Layer 2 Service 
BMAC :05
BCB
BEB
BMAC :13
BEB
BMAC :11
BMAC :03
BEB
BCB
BMAC :02
BEB
BMAC :04
BCB
BMAC :01
ISID 
1001
ISID 
1001
ISID 
1001
ISID 
1001
Host A
Host B
Host C
Host D
BEB 3
CORE 1
BEB 1
BEB 2
BEB 4
CORE 2
Core 5
B-VID 4001
Ethertype 802.1 ad
SA BMAC :11
DA BMAC 03:00:11:00:01:90
->  show spb isis multicast-table
Legend: MCAST Source * indicates any source in GMODE bvlans
SPB ISIS Multicast MAC Table:
MCAST Source                      Inbound     Outbound
ISID   BVLAN  MCAST Group Address
(Name : BMAC)                     Interface   Interfaces
------+-------+-------------------+----------------------------------+-----------+-----------
1001   4001   01:1e:83:00:07:d1     *                                           1/1/10
1002   4002   01:1e:83:00:07:d2     *                                           1/1/10
MAC Addresses: 2

<<<PAGE 142>>>
MULTICAST GROUP B-MAC
• SPBM Group MAC addresses are derived
from of B-DA unicast address and 
I-SID information
• Identifies the source BEB and the ISID
The least significant and the next to least significant bits of 
the first octet of the address, the Individual/Group and 
Universally/Locally administered bits, are both set denoting 
a locally administered group address
• I/G (multicast bit) = 1
• U/L (local bit) = 1
• SPBM type = 00
• SPSourceID == 20-bit ‘short-form’ node ID
• I-SID == 24-bit I-component identifier.
SPB ISIS Bridge Info:
System Id             = 
e8e7.32f6.1581,
System Hostname       = BEB-A,
SPSourceID            = 06-15-81,
……………  Omitted lines  …………………
Legend: MCAST Source * indicates any source in GMODE bvlans
SPB ISIS Multicast MAC Table:
MCAST Source             Inbound    Outbound
ISID   BVLAN   MCAST Group Address    (Name  :  BMAC)                 Interface   Interfaces
------+------+-------------------+------------------------------------+-----------+-----------
1001   4001   53:cd:71:00:07:09  BEB-C         : 2c:fa:a2:05:cd:71      1/1/6
1001   4001   53:cd:a9:00:07:09  BEB-B         : 2c:fa:a2:05:cd:a9      1/1/5
1001   4001   63:15:81:00:07:09  BEB-A         : e8:e7:32:f6:15:81      1/1/5 
1/1/6
1001   4001   c3:23:b3:00:07:09  BEB-D         : e8:e7:32:fc:23:b3      1/1/5
I-SID encoded 
as last 3 octets
Last 3 Octets of B-DA 
encoded as 1st 3 octets
B-DA Unicast
B-DA Multicast
I-SID
BVID
2c:fa:a2:05:cd:71 
53:cd:71:00:07:09 
1001
4001
05:cd:71:00:07:09
0011
SPBM Group MAC address
B-DA –Unicast
I-SID
2c:fa:a2:05:cd:71
1001 
-> show spb isis multicast-table
-> show spb isis info

<<<PAGE 143>>>
IP MULTICAST SWITCHING OVER SPBM (IPMS)
• All multicast control/data traffic will be flooded to all SAP and SDP tunnel ports whether 
they want it or not
• Prevent IP multicast flooding at the service using multicast snooping
• Supports IPv4 and IPv6 multicast
• Similar fashion to Vlan domain
• Eliminates unsolicited multicast flooding in the SAP egress
• Optimizes use of core bandwidth
• IPMS supported options (incl. IPv4/IPv6(MLD)
• IGMP/MLD snooping and proxy per service
• Spoofing, zapping, robustness controls
• Querier forwarding
• Zero based queries
• Flood unknown controls

<<<PAGE 144>>>
SDP 10007
ip multicast service 4000 admin-state enable
IP MULTICAST OPTIMIZATION
SAP 1/1/1:20
SAP 1/1/2:40
SAP 1/1/3:30
SDP 10005
SDP 10006
Dynamic 
Querier
Q
SAP
SAP
SAP
Head-End with Optimization
Head End without Optimization
Without IP Multicast snooping, floods IP multicast over the service
Flooding of ALL SAPs and SDP (tunnels to remote nodes)
IP multicast snooping at service level
Prevents flooding SAPs and SDPs
Multicast Data replicates only to IGMP client
ISID 4000
SDP 
10005
SDP 
10006
SDP 
10007

<<<PAGE 145>>>
Multicast mode can be specified on a per I-SID basis or globally
Same multicast mode is used across all nodes for a given SPB 
BVLAN 
Configure SPB Multicast Mode
MULTICAST FORWARDING CONFIGURATION
-> service spb [service_id|all] multicast-mode [head-end | tandem]
-> spb isis bvlan bvlan_id tandem-multicast-mode {sgmode | gmode}
Configure the tandem multicast mode 
Tandem Multicast mode is specified on a per BVLAN basis 
All ISIDs on the bvlan will use the same tandem mode 
configured for the bvlan.
-> ip multicast service service_id admin-state enable
Enable SPB IP Multicast at service level to all BEBs
IPMS must be explicitly enabled or disabled for each SPB service.

<<<PAGE 146>>>
SPB TROUBLESHOOTING

<<<PAGE 147>>>
MONITORING SPB
• Mac-ping: Proprietary ping 
• The timeout for each ping request packet is 1 sec. (not configurable)
• Destination MAC cannot be a broadcast, multicast, or NULL address
sw1-> show spb isis info
SPB ISIS Bridge Info:
System Id             = e8e7.32a4.777d,
System Hostname
= sw8,
SPSourceID
= 04-77-7d,
SPBM System Mode      = auto,
BridgePriority
= 32768 (0x8000),
……………  Omitted lines  …………………
BMAC address identification (switch @BMAC)
sw2-> mac-ping dst-mac e8:e7:32:a4:77:7d vlan 4015
Reply from E8:E7:32:A4:77:7D - 1/1/5  : bytes=64 seq=1 time=109us
Reply from E8:E7:32:A4:77:7D - 1/1/5  : bytes=64 seq=2 time=96us
Reply from E8:E7:32:A4:77:7D - 1/1/5  : bytes=64 seq=3 time=106us
Reply from E8:E7:32:A4:77:7D - 1/1/5  : bytes=64 seq=4 time=114us
Reply from E8:E7:32:A4:77:7D - 1/1/5  : bytes=64 seq=5 time=111us
----E8:E7:32:A4:77:7D MAC-PING Statistics----
5 packets transmitted, 5 packets received, 0% packet loss
round-trip (us)  min/avg/max = 96/107/114
Based on destination BMAC via  BVLAN
-> mac-ping dst-mac mac vlan vlan-id [priority vlan-priority] [drop-eligible {true|false}] [count count] [interval delay] [size size] [isid-check isid]

<<<PAGE 148>>>
SERVICE ASSURANCE AGENT (SAA)
Create a SAA SPB test
Start SAA test
Stop SAA test
Service Assurance Agent (SAA)
[auto-create] 
[auto-start] 
Reset
flush
[interval interval] 
[vlan-priority vlan_priority] 
[drop-eligible {true | false}] 
[data data] [num-pkts count] 
[inter-pkt-delay delay] [payload-size size] 
[jitter-threshold jitter_thresh] 
[rtt-thresh rtt_thresh] 
[keep]
• SAA – Test over SPB
• Automatically creates an SPB SAA session for each discovered 
BVLAN-BMAC pair.
• SPB dynamically discovers remote switches.
• SPB sends the SPB VLANs and MACs that it discovers.
• SAA sessions are created for each VLAN/MAC pairing.
• If the destination MAC is determined to be on a link 
aggregation group, SAA traverse all paths of the Linkaggs
-> saa spb auto-start
-> saa spb stop [never | at yyyy-mm-dd,hh:mm:ss]
-> saa spb

<<<PAGE 149>>>
• SAA – Statistics
• History of the past iterations of sessions
• Logs saved in XML statistics file
• Located in /flash/network directory
• Ability to manage filename (default: saa.xml)
• File periodically created (configurable)
SERVICE ASSURANCE AGENT STATISTICS
SAA name and ID
•Iteration number
• For each iteration
−
last run time
−
reason 
−
packet sent
−
packet received
−
RTT min/avg/max
−
Jitter min/av/max
XML File
Configure SAA historical file
Service Assurance Agent (SAA)
[file-name xml_filename] 
[interval interval] 
[admin-state {enable | disable}]
-> saa spb

<<<PAGE 150>>>
-> show saa spb
SPB creation parameters:
Auto-create           : Enabled,
Auto-start            : Enabled,
Interval(minutes)     : 1,
Jitter Threshold (us) : 100,
RTT Threshold (us)    : 500,
Payload-Size (bytes)  : 32,
Num-pkts              : 5,
Inter-pkt-delay       : 1000,
Keep                  : Disabled,
Data                  : ""
-> show saa statistics aggregate
Aggregate Record:
SAA              Owner   Type    Time of Last-Run        RTT    RTT
RTT
RTT
Jitter Jitter
Jitter  Jitter
Packets   Description
Min    Avg     Max    Thr
Min    Avg     Max     Thr
Sent Rcvd
-----------------------------+------+---------+-----------------------+-----+-------+------+------+------+------+-------+-------+----+----+------------
SPB-2000-2c-fa-a2-05-d0-2d     SPB    mac-ping  2020-01-14,11:31:21.0    92   108     159    500     0      5       45     100  
80   80   DEFAULT
SPB-2000-2c-fa-a2-05-d1-e9     SPB    mac-ping  2020-01-14,11:31:26.0    91   114     406    500     0     13      306     100  
80   80   DEFAULT
SPB-2000-e8-e7-32-fc-22-f5     SPB    mac-ping  2020-01-14,11:31:31.0   114   240    4684    500     0    159     4541     100  
80   80   DEFAULT
SPB-2001-2c-fa-a2-05-d0-2d     SPB    mac-ping  2020-01-14,11:31:06.0    89   139    2436    500     0     64     2339     100  
80   80   DEFAULT
SPB-2001-2c-fa-a2-05-d1-e9     SPB    mac-ping  2020-01-14,11:31:11.0    87   135    1571    500     0     36     1459     100  
80   80   DEFAULT
SPB-2001-e8-e7-32-fc-22-f5     SPB    mac-ping  2020-01-14,11:31:16.0   103   244    4828    500     1     65     3482     100  
80   80   DEFAULT
SPB-2002-2c-fa-a2-05-d0-2d     SPB    mac-ping  2020-01-14,11:30:51.0    90   129    1275    500     0     35     1158     100  
80   80   DEFAULT
SPB-2002-2c-fa-a2-05-d1-e9     SPB    mac-ping  2020-01-14,11:30:56.0    87   179    3359    500     0     50     2128     100  
80   80   DEFAULT
SPB-2002-e8-e7-32-fc-22-f5     SPB    mac-ping  2020-01-14,11:31:01.0   107   145     248    500     1      8       89     100  
80   80   DEFAULT
MONITORING SAA SPB
Display the SAA configuration 
Display SAA statistics

<<<PAGE 151>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 152>>>
IP ROUTING OVER SPB
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 153>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Define the IP Routing over SPB – L3 services 
• Describe Routing Concept
Single-pass or inline

<<<PAGE 154>>>
DEFINE THE IP ROUTING OVER SPB
L3 SERVICES

<<<PAGE 155>>>
OBJECTIVES
• Allowing the mapping of Layer 3 traffic onto the underlying SPB infrastructure
• Single system acting as both Bridge and Router for the same traffic
• No devices required specifically for routing between SPB services 
• Reducing the need for an additional tier
• No IGPs needed on Core devices
• IPv4/IPv6 support

<<<PAGE 156>>>
L3 SERVICES
•
A L3 service refers to a type of VPN service connecting multiple sites in a single any-to-any routing 
domain. 
•
Different sites utilize different subnets and require routing to communicate.
•
For multi-tenancy, and to keep different customers isolated at L3, each customer service is 
associated to its own VRF instance.
•
VPN Lite :   A VPN Lite L3 Service is created by overlaying a L3 routing protocol on top of the L2 WAN SPB 
service. This routing protocol can be OSPF, BGP, or even static routing.
•
L3 VPN :    SPB L3 VPN leverages the existing SPB IS-IS instance to carry customer VPN routes without 
requiring an additional routing protocol such as OSPF. This is accomplished with additional IS-IS    
TLVs extensions

<<<PAGE 157>>>
CONCEPTS
•
Bridges will do layer 3 forwarding in a VRF and SPB bridging on a service, thus fulfilling L3 
connectivity across SPB network
•
VRFs on different BEBs are tied together by ISIDs across SPB backbone
Customer
Network 1
VRF
ISID
ISID
VRF
Customer
Network 2
SPB Core 
Network
BEB
BEB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
Customer
Network 1
ISID
ISID
Customer
Network 2
SPB Core 
Network
BEB
BEB
BCB
BCB
BCB
BCB
BCB
BCB
BCB
SAP
SAP
Can operate on Backbone Edge Bridges (BEB)
Can operate on Backbone Core Bridges (BCB)

<<<PAGE 158>>>
ROUTING CONCEPT

<<<PAGE 159>>>
AOS SUPPORT
•
• Inline Routing using native single-pass processing
OS6860N
OS6900-X48C6
OS6900-X48C4E
OS6900-T48C6 
OS6900-C32E 
OS9900
No physical loopback cable required.
No dedicated front-panel ports
L3 VPN interface defined through the configuration 
of an IP interface bound to an SPB service
VRF
Service 1

<<<PAGE 160>>>
NATIVE SINGLE-PASS PROCESSING
•
L3 VPN interface defined through the configuration of an IP interface bound to an SPB service.
•
IP service-based interface configured through software for single-pass in-line routing.
•
IP address assigned to the service interface used as a gateway address to bind a VRF instance 
to an SPB service instance.
SPB
OS9900

<<<PAGE 161>>>
CONFIGURATION STEPS
-> service service_id spb isid instance_id bvlan bvlan_id vlan-xlation
-> ip interface if_name address ip_address/mask vlan vlan_id service service_id
A service-based interface is used to provide in-line routing.
Specify the service parameter to create an L3 VPN interface that is required for IP Routing over SPB.
The IP address assigned to the service interface is used as a gateway address to bind a VRF instance to an SPB service instance.
Create a Service SPB instance
Configure an IP interface for the L3VPN VLAN
Configure IP-VPN LITE or L3-VPN
L3VPN Interface

<<<PAGE 162>>>
CONFIGURATION EXAMPLE
-> service 10 spb isid 1000 bvlan 4001 vlan-xlation
-> ip interface L3VPN1 address 10.10.10.1/24 service 10
L3VPN Interface
Create a Service SPB instance
Configure an IP interface for the L3VPN VLAN
Configure IP-VPN LITE or L3-VPN

<<<PAGE 163>>>
CONFIGURATION GUIDELINES - SPB INLINE ROUTING
•
When creating an IP interface for an SPB service:
•
An SPB service with the specified ID must exist in the switch configuration
•
VLAN translation is implicitly enabled when a service is assigned to an IP interface regardless of 
whether or not VLAN translation is enabled for the service
•
The VLAN translation status is no longer configurable as long as the service is bound to an IP interface
•
Both an IPv4 and IPv6 interface can be assigned to the same SPB service as long as both interface types 
are in the same VRF instance.

<<<PAGE 164>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 165>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Implementing IP Routing over SPB-M – Network Routing 
Redundancy 
Content 
1 
Objectives ...................................................................................... 2 
2 
Topological diagram .......................................................................... 2 
3 
IP Routing over SPB configuration .......................................................... 3 
3.1. Configuring routing for access VLAN 2 & 3 ...................................................... 3 
3.2. Setup new services on Core switches ............................................................ 3 
3.3. Network Routing Redundancy..................................................................... 4

<<<PAGE 166>>>
2 
Lab: Implementing IP Routing over SPB-M – Network Routing Redundancy 
 
 1 
Objectives 
- In addition to L2 VPN, the OmniSwitch also provides an IP over SPB-M capability that consolidates the 
routing functionality of Customer Edge (CE) devices into the BEB devices. 
The Virtual Routing and Forwarding (VRF) instances on different BEBs are tied together via backbone I-SIDs 
across the same SPB-M backbone that is used to support L2 VPNs. 
 
In this exercise, we will implement the L3-VPN solution by allowing IP routing across SPB backbone 
between: 
Clients 5 and 9 connected to OS6360-A 
Clients 6 and 10 connected to OS6360-B 
 
 
 
Be sure your partner group has completed the previous lab (Deploying a network based 
on SPB-M technology) before going on with the following exercises. 
 2 
Topological diagram

<<<PAGE 167>>>
3 
Lab: Implementing IP Routing over SPB-M – Network Routing Redundancy 
 
 3 
IP Routing over SPB configuration 
3.1. 
Configuring routing for access VLAN 2 & 3  
 
- 
We will attach, on both switch 1 & 2, the VLANs 2 & 3 traffic respectively to the SPB services 
2001 and 2002 to participate in routing L3 traffic through the SPB network. 
3.2. 
Setup new services on Core switches 
Switch 1 & 2 (6900-A & 6870-B) 
-> service spb 2001 isid 2001 bvlan 2001 description vlan2 admin-state enable 
-> service spb 2002 isid 2002 bvlan 2002 description vlan3 admin-state enable 
- 
Configure VLAN 2 and SAP  
Switch 1 
-> ip interface L3vpnvlan2 address 192.168.2.1/24 service 2001 
 
-> show service 2001 
SPB Service Detailed Info 
  Service Id       : 2001,                 Description      : vlan2              , 
  ISID             : 2001,                 BVlan            : 2001, 
  Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0, 
  Admin Status     : Up,                   Oper Status      : Up, 
  Stats Status     : No,                   Vlan Translation : Y (Auto), 
  Service Type     : SPB,                  Allocation Type  : Static, 
  MTU              : 9194,                 VPN IP-MTU       : 1500, 
  SAP Count        : 0,                    SDP Bind Count   : 3, 
  RemoveIngressTag : No,                   Option           : None, 
  IPv4 VRF Instance: Default,              IPv4 Interface   : L3vpnvlan2, 
  Mgmt Change      : 03/15/2020 23:49:40,  Status Change    : 03/15/2020 23:49:40 
- 
Configure VLAN 3 and SAP  
Switch 1 
-> ip interface L3vpnvlan3 address 192.168.3.1/24 service 2002 
 
-> show service 2002 
SPB Service Detailed Info 
  Service Id       : 2002,                 Description      : vlan3              , 
  ISID             : 2002,                 BVlan            : 2002, 
  Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0, 
  Admin Status     : Up,                   Oper Status      : Up, 
  Stats Status     : No,                   Vlan Translation : Y (Auto), 
  Service Type     : SPB,                  Allocation Type  : Static, 
  MTU              : 9194,                 VPN IP-MTU       : 1500, 
  SAP Count        : 0,                    SDP Bind Count   : 3, 
  RemoveIngressTag : No,                   Option           : None, 
  IPv4 VRF Instance: Default,              IPv4 Interface   : L3vpnvlan3, 
  Mgmt Change      : 03/15/2020 23:50:04,  Status Change    : 03/15/2020 23:47:47 
Switch 2  
-> ip interface L3vpnvlan2 address 192.168.2.2/24 service 2001 
-> ip interface L3vpnvlan3 address 192.168.3.2/24 service 2002 
Switch 7 
-> service access port 1/1/3 vlan-xlation enable 
-> service access port 1/1/7 vlan-xlation enable 
-> service 2001 vlan-xlation enable 
-> service 2002 vlan-xlation enable

<<<PAGE 168>>>
4 
Lab: Implementing IP Routing over SPB-M – Network Routing Redundancy 
 
Switch 8 
-> service access port 1/1/3 vlan-xlation enable 
-> service 2001 vlan-xlation enable 
-> service 2002 vlan-xlation enable 
 
- 
L3 path between nodes 1 and 2 should be now established.  
- 
Check L3 connectivity by running a ping between the two OS6900 L3VPN interfaces through CLI 
interface. 
- 
Open the clients (shortcut 
 on access POD desktop) 
 
- 
Right-click on appropriate VM Client then select Open console. 
 
- 
Setup clients 5, 6, 9 and 10 with the following IP addresses. 
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.1 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.1 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.2 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.2 
 
- 
Test the resiliency by disabling the uplinks on Switch1 or Switch2 while running continuous ping 
test between clients 5, 6, 9 and 10. 
 
- 
Check the path used by the network to route IP packets. 
3.3. 
Network Routing Redundancy 
 
- 
In order to ensure routing redundancy for Vlan 2 and Vlan 3 on switch 7 and 8, we need to 
create two VRP instances for these VLANs on core switches. 
 
- 
Create two VRP instances with Switch 1 as the master for Clients 5 & 6 (VLAN 2) and Switch 2 
as the Master for Clients 9 & 10 (Vlan 3).

<<<PAGE 169>>>
5 
Lab: Implementing IP Routing over SPB-M – Network Routing Redundancy 
 
Switch 1 
-> ip vrrp 2 interface L3vpnvlan2 priority 200 
-> ip vrrp 2 interface L3vpnvlan2 address 192.168.2.254 
-> ip vrrp 2 interface L3vpnvlan2 admin-state enable 
-> ip vrrp 3 interface L3vpnvlan3 priority 100 
-> ip vrrp 3 interface L3vpnvlan3 address 192.168.3.254 
-> ip vrrp 3 interface L3vpnvlan3 admin-state enable 
Switch 2 
-> ip vrrp 2 interface L3vpnvlan2 priority 100 
-> ip vrrp 2 interface L3vpnvlan2 address 192.168.2.254 
-> ip vrrp 2 interface L3vpnvlan2 admin-state enable 
-> ip vrrp 3 interface L3vpnvlan3 priority 200 
-> ip vrrp 3 interface L3vpnvlan3 address 192.168.3.254 
-> ip vrrp 3 interface L3vpnvlan3 admin-state enable 
- 
Check your configuration and VRRP instances status on each of the switch. 
Switch 1 
-> show ip vrrp  
-> show ip vrrp statistics 
Checksum Errors :          0, 
Version Errors  :          0, 
VRID Errors     :          0 
                Interface 
VRID              Name                  State      UpTime   Become Master Adv. Rcvd 
----+--------------------------------+----------+----------+-------------+---------- 
   2 L3vpnvlan2                       Master         963083            1           4 
   3 L3vpnvlan3                       Backup         963083            0        9631 
- 
Open the clients (shortcut 
 on access POD desktop) 
- 
Right-click on appropriate VM Client then select Open console 
- 
Change the default gateway on clients 5, 6, 9 and 10 with the VRRP instances IP addresses 
(.254). 
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.254 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.254 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.254 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.254 
 
- 
Test the resiliency by disabling the uplinks on Switch 1 or Switch 2 while running continuous 
ping test between clients 5, 6, 9 and 10. 
- 
Check the path used by the network to route IP packets.

<<<PAGE 170>>>
IP ROUTING OVER SPB –IP-VPN LITE 
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 171>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe and configure VPN Lite routing

<<<PAGE 172>>>
IP-VPN LITE

<<<PAGE 173>>>
IP-VPN LITE
• Routing L3 traffic over a L2 SPBM backbone network
• Run routing protocols on L3VPN IP interfaces
SPB
BACKBONE
VRF
VRF
RIB
(Routing
Information 
Base)
RIB
(Routing
Information 
Base)
L3 protocols
OSPF, Static Routes, …
IP-VPN Lite

<<<PAGE 174>>>
IP-VPN LITE
• Example
SPB
BACKBONE
ISID 1001
ISID 1002
VRF1
VRF2
VRFs interconnections across a SPB cloud 
SPB acts more like a physical media 
SPB tunnel endpoint is presented as just 
another VLAN port for L2/L3 traffic 
Routing or bridging based on S/D @MAC
▪Static routing
▪Point To Point routing
▪Multi-point routing
Routing to IP interfaces in a VRF attached to an end 
of the SPB tunnel 
VRF 2
VRF 2
VRF 1
VRF 1
IP-VPN Lite

<<<PAGE 175>>>
CONFIGURATION GUIDELINES
• Each VRF must have a single IP interface on the routing side of the loop back tied to a 
specific VLAN not used on other ports.
• In the VPN Lite version there can actually be multiple IP interfaces tied to different I-SID 
per VRF (but two VRF cannot share the same ISID).
• There is a corresponding SAP on the other side of the loopback tied to the correct I-SID 
using the same VLAN as its identifier.
• Administrator can use the routed side of the loop back for both routing protocol 
communication or as the router port for a set of hosts.
• VRRP can also be configured per interface on the loopback to allow two or more BEB to act 
as redundant routers for the host connected across SPB.
• VRRP hellos are sent across the PBB network
• The administrator can also choose to forgot dynamic routing and use static routes where the 
gateway is a router connected via SPB (and can be the IP interface tied to the routing loopback of 
another BEB)
IP-VPN Lite

<<<PAGE 176>>>
IP-VPN LITE- SPB INLINE IP ROUTING 
• Static & Dynamic routing – inline Routing
IP-VPN Lite
spb bvlan 4001
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf 1 ip interface L3vpn2 address 10.5.1.2/24 service 10 
vrf 1 ip static-route 192.168.1.0/24 gateway 10.5.1.2
vrf 1 ip static-route 192.168.2.0/24 gateway 10.5.1.2
vrf 1 ip load ospf
vrf 1 ip ospf interface L3vpn2
vrf 1 ip ospf interface L3vpn2 admin-state enable
vrf 1 ip ospf area 0.0.0.0
vrf 1 ip ospf interface L3vpn2 area 0.0.0.0
vrf 1 ip ospf admin-state enable
Static routing
Dynamic routing
spb bvlan 4001
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10 
vrf 1 ip static-route 192.168.3.0/24 gateway 10.5.1.2
vrf 1 ip static-route 192.168.4.0/24 gateway 10.5.1.2
vrf 1 ip load ospf
vrf 1 ip ospf interface L3vpn1
vrf 1 ip ospf interface L3vpn1 admin-state enable
vrf 1 ip ospf area 0.0.0.0
vrf 1 ip ospf interface L3vpn1 area 0.0.0.0
vrf 1 ip ospf admin-state enable
Static routing
Dynamic routing
SPB
Backbone
ISID-1000
ISID-1000
VRF 1
192.168.3.0/24
192.168.4.0/24
VRF 1
192.168.1.0/24
192.168.2.0/24
L3vpn2
L3vpn1
OS9900
OS9900

<<<PAGE 177>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 178>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Implementing IP Routing VPN-Lite over SPB-M 
Content 
1 
Objectives ...................................................................................... 2 
2 
Topological diagram .......................................................................... 2 
3 
VPN-Lite Configuration ....................................................................... 3 
3.1. Configuring VLAN for clients 7 and 8 ............................................................ 4 
3.2. Configuring VLAN for clients 1 and 2 ............................................................ 4 
3.3. Setting up OSPF protocol .......................................................................... 4 
3.4. Test scenario. ....................................................................................... 4

<<<PAGE 179>>>
2 
Lab: Implementing IP Routing VPN-Lite over SPB-M 
 
 1 
Objectives 
In this lab you will configure a scenario for routing L3 traffic over a L2 SPB-M backbone network. 
 
 
 
 
Be sure your partner group has completed the previous lab (Deploying a network based 
on SPB-M technology) before going on with the following exercises. 
 2 
Topological diagram

<<<PAGE 180>>>
3 
Lab: Implementing IP Routing VPN-Lite over SPB-M 
 
 3 
VPN-Lite Configuration 
The VPN-Lite method provides a gateway between a regular SPBM service and a router within the same  
OmniSwitch chassis.  
This solution provides a specific advantage in that it allows a single box to represent two tiers in a typical 
fat-tree network. 
A VPN-Lite configuration can act purely as an L3 VPN when configured correctly. In this mode, existing 
routing protocols can form adjacencies across the SPBM PBB network. 
- In this exercise, we will implement the VPN-Lite solution by allowing IP routing across SPB backbone 
between: 
Clients 5 and 9 connected to OS6360-A 
Clients 6 and 10 connected to OS6360-B 
Clients 1 connected to OS6900-A 
Clients 2 connected to OS6870-B 
Clients 7 connected to OS6870-A 
Clients 8 connected to OS6860-B 
 
 
 
Switch 1 
-> service spb 2009 isid 2009 bvlan 2000 description vlan999 admin-state enable 
-> ip interface L3vpn999 address 10.132.2.1/24 service 2009 
Switch 2 
-> service spb 2009 isid 2009 bvlan 2000 description vlan999 admin-state enable 
-> ip interface L3vpn999 address 10.132.2.2/24 service 2009 
Switch 7 
 
-> service spb 2009 isid 2009 bvlan 2000 description vlan999 admin-state enable 
-> ip interface L3vpn999 address 10.132.2.7/24 service 2009 
Switch 8 
-> service spb 2009 isid 2009 bvlan 2000 description vlan999 admin-state enable 
-> ip interface L3vpn999 address 10.132.2.8/24 service 2009

<<<PAGE 181>>>
4 
Lab: Implementing IP Routing VPN-Lite over SPB-M 
 
L3 path between nodes 1 and 2 should be now established. Check L3 connectivity by running a ping between 
the two OS6900 L3VPN interfaces through CLI interface. 
3.1. 
Configuring VLAN for clients 7 and 8 
Switch 7 
-> vlan 7 
-> ip interface vlan7 address 192.168.7.7/24 vlan 7 
-> vlan 7 members port 1/1/1 untagged 
-> interfaces 1/1/1 admin-state enable 
Switch 8 
-> vlan 8 
-> ip interface vlan8 address 192.168.8.8/24 vlan 8 
-> vlan 8 members port 1/1/1 untagged 
-> interfaces 1/1/1 admin-state enable 
3.2. 
Configuring VLAN for clients 1 and 2 
Switch 1 
-> vlan 10 
-> ip interface vlan10 address 192.168.10.1/24 vlan 10 
-> vlan 10 members port 1/1/1 untagged 
-> interfaces 1/1/1 admin-state enable 
Switch 2 
-> vlan 20 
-> ip interface vlan20 address 192.168.20.2/24 vlan 20 
-> vlan 20 members port 1/1/1 untagged 
-> interfaces 1/1/1 admin-state enable 
3.3. 
Setting up OSPF protocol 
Define the backbone area and interfaces associated with the backbone area, then redistribute local routes to 
OSPF protocol. 
Switch 1, 2, 7 & 8 
-> ip load ospf 
-> ip ospf area 0.0.0.0 
-> ip ospf interface L3vpn999 
-> ip ospf interface L3vpn999 admin-state enable 
-> ip ospf interface L3vpn999 area 0.0.0.0 
-> ip ospf admin-state enable 
-> ip route-map local sequence-number 10 action permit 
-> ip route-map local sequence-number 10 match ip-address 0.0.0.0/0 
-> ip redist local into ospf route-map local 
 
OSPF parameters verification 
 
-> show ip ospf 
-> show ip ospf area 0.0.0.0 
-> show ip ospf interface 
-> show ip routes 
-> show ip ospf routes 
3.4. 
Test scenario. 
Check connectivity between Clients 1, 2, 5, 6, 7, 8, 9,10. 
From Virtual machines connected on the network, run some connectivity test between clients.

<<<PAGE 182>>>
5 
Lab: Implementing IP Routing VPN-Lite over SPB-M 
 
- Open the clients (shortcut 
 on access POD desktop) 
- Right-click on appropriate VM Client then select Open console 
- Configure and use VMs as shown here: 
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient1 
Switch 1 
1/1/1 
10 
192.168.10.101 
192.168.10.1 
PodXClient2 
Switch 2 
1/1/1 
20 
192.168.20.102 
192.168.20.2 
PodXClient7 
Switch 7 
1/1/1 
7 
192.168.7.107 
192.168.7.7 
PodXClient8 
Switch 8 
1/1/1 
8 
192.168.8.108 
192.168.8.8 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.254 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.254 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.254 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.254 
 
- Run continuous ping requests between the selected VM clients.  
 
- Monitor and comment the SPB network behavior: 
1. 
Display the path used between each of the clients 
2. 
Analyze the routing tables and the data path. 
3. 
Display the mac address table and check for sap port and client @mac mapping 
4. 
Disable the appropriate interconnection port to verify the network resiliency.

<<<PAGE 183>>>
IP ROUTING OVER SPB – L3-VPN
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 184>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe and configure L3 VPN routing

<<<PAGE 185>>>
L3 VPN

<<<PAGE 186>>>
SPB
BACKBONE
L3 VPN - OVERVIEW
• Routing L3 traffic over a L2 SPBM backbone network
• VRF L3 routes exchanged via dedicated ISIS/SPB TLV
GRM
VRF
ISIS
IGP
L3-VPN
SPB-ISIS protocol

<<<PAGE 187>>>
L3 VPN - OVERVIEW
• Notion
SPB
BACKBONE
L3-VPNs concept similar to BGP-L3VPNs 
over MPLS
Layer 3 routes between VRFs 
exchanges via IPVPN TLV
VRFs interconnections using 
one ISID-per-VRF mapping
No needs to run routing 
protocols on L3 VPN IP 
interfaces
AOS Switch acts as an access or 
edge router to connect VRFs 
across the SPB backbone PBB 
network
BEB
BEB
L3-VPN

<<<PAGE 188>>>
L3 VPN - OVERVIEW
• Notion
GRT: Global Routing Manager
IPRM: IP Route Manager
ISID 
1001
ISID 
1002
VRF1
VRF2
ISIS-SPB protocol acts as an IGP protocol
ISID represents the VRF/L3VPN  
Segregates the routing information
1 VRF to 1 ISID mapping 
Routes can be selectively imported into ISIS- SPB 
and advertised across the SPB domain
VRF routes are imported and exported from its 
IPRM Database into the GRM
SPB
BACKBONE
IS-IS
IS-IS
IS-IS
GRT
GRT
IP routes are exported into a global routing 
table (GRM) to generate IP route entries
VRFs interconnections using one ISID-
per-VRF mapping
L3-VPN

<<<PAGE 189>>>
L3 VPN - CONCEPT
• ISIS-SPB inter-ISID route leaking
• Leaking between VRFs is allowed via additional configurations
• Each represents import/export or redistribution process
VRF to VRF route import/export
ISID to VRF route import
ISID to ISID route redistribution
VRF to ISID route redistribution
VRF 1
VRF 2
ISID
4001
ISID
4002
L3-VPN

<<<PAGE 190>>>
L3 VPN - COMPONENTS
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “Default”
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “1”
RIB - Routing Information Base
FIB – Forwarding Information Base
GRT – Global Route Table
GRT
Global 
Routing
Table
ISIS
(SPB IPVPN 
Route table)
Route 
Map
Route 
Map
L3-VPN

<<<PAGE 191>>>
L3 VPN – ROUTING PROCESS
SPB
Backbone
Réseau A
GRT
(Global 
Routing
Table)
RIB
(Routing
Information 
Base)
ISIS
(SPB IPVPN 
Route table)
VRF Network A
Réseau B
GRT
(Global 
Routing
Table)
RIB
(Routing
Information 
Base)
ISIS
(SPB IPVPN 
Route table)
VRF Network B
VRF to VRF route import/export
ISID to VRF route import
ISID to ISID route redistribution
VRF to ISID route redistribution
ISID – VRF binding
VRF to VRF route import/export
ISID to VRF route import
ISID to ISID route redistribution
VRF to ISID route redistribution
ISID – VRF binding
ISIS-SPB TLV 
Advertissemnt
ISIS acts as an IGP and import/export routes from VRFs then mutualise in SPB 
backbone through a table named Global Routing Table (GRT).
L3-VPN

<<<PAGE 192>>>
L3 VPN – ROUTING PROCESS
GRT
ISIS
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “Default”
Route 
Map
ISID 1
VRF default
Route 
Map
Route 
Map
ISID – VRF binding
ISID to ISID route redistribution
VRF to VRF route import/export
ISID to VRF route import
VRF to ISID route redistribution
ISID 1
ISID 2
ISID 2
ISID 1
ISID 2
VRF “other”
RIB
(Routing
Information 
Base)
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
IPRM 
Route 
Map
L3-VPN

<<<PAGE 193>>>
L3 VPN CONFIGURATION
• Routes exchanged by importing and exporting between VRF and SPB-ISIS via GRT table
• Create a “bind” entry between <vrf, gateway IP> and VRFs
-> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 route-map net
-> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 all-routes
GRT
ISIS
ISID 4000
ISID 4001
ISID 4001
1
ISID 4001
route-map: imported routes filtering
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “Default”
Route 
Map
Route 
Map
IPv4
spb ipvpn bind vrf {vrf_name} isid instance_id gateway ip_address {all-routes | import-route map route_map_name}
IPv6
spb ipvpn6 bind vrf {<name> | DEFAULT} isid <isid-num> gateway <gateway-IPv6> {all-routes | import-route-map <route-map-name>}
L3-VPN

<<<PAGE 194>>>
L3 VPN CONFIGURATION
• Export routes from a VRF to GRT table or to other VRF instances
IPv4
spb ipvpn bind vrf {vrf_name} isid instance_id gateway ip_address {all-routes | import-route map route_map_name}
IPv6
spb ipvpn6 bind vrf {<name> | DEFAULT} isid <isid-num> gateway <gateway-IPv6> {all-routes | import-route-map <route-map-name>}
L3-VPN

<<<PAGE 195>>>
GRT
ISIS
L3 VPN CONFIGURATION
• Import VRF or SPB service instance (ISID) routes from the GRT to the destination VRF
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
ISID 4000
ISID 4001
ISID 4001
VRF “Default”
ISID 4001
VRF default
Routes “import”
-> vrf default ip import isid 4001 route-map net3
3
-> vrf default ip redist import into ospf route-map net5
4
Option: Routes « import » 
redistribution inside VRF
⚫All routes can be
exported or filtered
through a route-map
Route 
Map
Route 
Map
IPv4
spb ipvpn bind vrf {vrf_name} isid instance_id gateway ip_address {all-routes | import-route map route_map_name}
IPv6
spb ipvpn6 bind vrf {<name> | DEFAULT} isid <isid-num> gateway <gateway-IPv6> {all-routes | import-route-map <route-map-name>}
L3-VPN

<<<PAGE 196>>>
GRT
INTER-ISID ROUTE LEAKING
• Route redistribution from a VRF to an ISID
ISIS
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
ISID 4000
ISID 4001
ISID 4002
ISID 4001
VRF “Default”
ISID 4001
VRF default
-> vrf default ip export route-map net1
2
1
-> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 all-routes
ISID 4002
-> spb ipvpn redist source-vrf default destination-isid 4002 route-map net9
3
⚫All routes can be exported or 
filtered through a route-map
Route 
Map
Route 
Map
IPv4
spb ipvpn redist {source-vrf {vrf_name | default} destination-isid instance_id {all-routes | route-map route_map_name}
IPv6
spb ipvpn6 redist source-vrf {<name>| DEFAULT} destination-isid <isid-num> {all-routes | route-map <route-map-name>}
L3-VPN

<<<PAGE 197>>>
ISIS
GRT
INTER-ISID ROUTE LEAKING
• Routes exportation from 2 VRF to 1 ISID instance
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “1”
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “Default”
ISID 4000
ISID 4001
VRF default
-> vrf 1 ip export route-map net2
-> vrf default ip export route-map net1
2
ISID 4001
1
-> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 all-routes
ISID 
4001
-> spb ipvpn redist source-vrf 1 destination-isid 4001 all-routes
3
VRF 1
Route 
Map
Route 
Map
Route 
Map
Route 
Map
L3-VPN

<<<PAGE 198>>>
GRT
INTER-ISID ROUTE LEAKING
• Route redistribution from an ISID to another ISID
ISIS
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
ISID 4000
ISID 4001
ISID 4002
ISID 4001
VRF “Default”
ISID 4001
VRF default
-> vrf default ip export route-map net1
2
1
-> spb ipvpn bind vrf default isid 4001 gateway 10.1.2.1 all-routes
ISID 4002
-> spb ipvpn redist source-isid 4001 destination-isid 4002 all-routes
3
⚫All routes can be exported or 
filtered through a route-map
One ISID cannot be attached
(binding) and be redistributed
to a same VRF instance
Route 
Map
Route 
Map
IPv4
spb ipvpn redist source-isid instance_num destination-isid instance_id {all-routes | route-map route_map_name}
IPv6
spb ipvpn6 redist source-isid <isid_num> destination-isid <isid_num> {all-routes | route-map <route-map-name>}
L3-VPN

<<<PAGE 199>>>
VPN LITE VERSUS L3 VPN
•
Let’s start with the advantages of L3 VPN:
•
Simplicity: 
•
L3 VPN does not require routing protocol configuration as it simply leverages the existing SPB IS-IS instance. VPN Lite on the other hand 
requires one routing protocol instance per tenant/VRF and BEB.
•
Scalability:
•
L3 VPN is significantly more efficient than VPN Lite from a CP point of view as it uses a single routing instance. This results in lighter CP load 
and allows for greater scalability than VPN Lite.
•
Convergence:
•
L3 VPN convergence can be faster than VPN Lite because it relies on a single protocol. VPN Lite convergence can be slower because the 
stacking of routing protocols has a compounding effect over convergence time: IS-IS must converge before OSPF can converge

<<<PAGE 200>>>
CONFIGURATION GUIDELINES
• Between the two ports, the mapping of VRF to I-SID is coordinated by VLAN IDs
• The router side loop back port is not open for use of routing protocols
• IP interfaces must be created for each VRF on the loop back port
• These basically allow IS-IS to exchange routes between BEBs on a per I-SID bases
• The VRF, SPB BVLAN and the SPB service (ISID) are set up as usual
• A loopback-port pair is then configured
• A SAP is created for L3VPN, assigned to the SPB service and associated with a VRF, the IP 
VLAN to be created and the corresponding IP interface address to be used
L3-VPN

<<<PAGE 201>>>
CONFIGURATION GUIDELINES
• When creating an IP interface for an SPB service:
• An SPB service with the specified ID must exist in the switch configuration
• VLAN translation is implicitly enabled when a service is assigned to an IP interface regardless of 
whether or not VLAN translation is enabled for the service
• The VLAN translation status is no longer configurable as long as the service is bound to an IP interface
• Both an IPv4 and IPv6 interface can be assigned to the same SPB service as long as both interface 
types are in the same VRF instance.

<<<PAGE 202>>>
SPB INLINE IP ROUTING – L3-VPN
spb bvlan 4001
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf 1 ip interface L3vpn2 address 10.5.1.2/24 service 10 
spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.2 all-routes
vrf 1 ip export all-routes
vrf 1 ip import isid 1000 all-routes
spb bvlan 4001
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf 1 ip interface L3vpn1 address 10.5.1.1/24 service 10 
spb ipvpn bind vrf 1 isid 1000 gateway 10.5.1.1 all-routes
vrf 1 ip export all-routes
vrf 1 ip import isid 1000 all-routes
SPB
Backbone
ISID-1000
ISID-1000
VRF 1
192.168.3.0/24
192.168.4.0/24
VRF 1
192.168.1.0/24
192.168.2.0/24
L3vpn2
L3vpn1
L3-VPN

<<<PAGE 203>>>
L3 VPN MONITORING
Local
Static
RIP
OSPF
BGP
IS-IS
Local
Static
RIP
OSPF
BGP
IS-IS
FIB
(Forwarding 
Information 
Base)
RIB
(Routing
Information 
Base)
IPRM 
VRF “Default”
GRT
(Global 
Routing
Table)
ISIS
(SPB IPVPN 
Route table)
-> show spb ipvpn route-table
-> show spb ipvpn6 route-table
-> show ip global-route-table
-> show ipv6 global-route-table
-> vrf default show ip router database
or
-> show ip router database
-> show ip router database
-> vrf default show ip routes
or
-> show ip routes
-> show ipv6 routes
RIB - Routing Information Base
FIB – Forwarding Information Base
GRT – Global Route Table
Route 
Map
L3-VPN

<<<PAGE 204>>>
MONITORING L3 VPN
• Display the contents of the Global Routing Table (GRT) for all the routes that are exported 
from VRF instances or from SPB instance service identifiers (ISIDs)
-> show ip global-route-table
Type  Source               Destination        Gateway         Metric     Tag
-----+--------------------+------------------+---------------+----------+----------
isid
2000                 10.132.2.0/24      10.132.2.8               1          0
isid
2000                 192.168.2.0/24     10.132.2.8               1          0
isid
2000                 192.168.3.0/24     10.132.2.8               1          0
isid
2000                 192.168.8.0/24     10.132.2.8               1          0
vrf
default              10.132.2.0/24      10.132.2.7               1          0
vrf
default              192.168.2.0/24     192.168.2.7              1          0
vrf
default              192.168.3.0/24     192.168.3.7              1          0
vrf
default              192.168.7.0/24     192.168.7.7              1          0
GRT
(Global 
Routing
Table)
Route imported from ISID 2000
L3-VPN

<<<PAGE 205>>>
MONITORING L3 VPN
• Display the contents of the SPB IPVPN route table
Legend: * indicates IPVPN route has matching locally configured ISID
SPB IPVPN Route Table:
Source Bridge
ISID   Destination          Gateway           (Name : BMAC)                             Metric
----------+--------------------+-----------------+-----------------------------------------+--------
*    2000   10.132.2.0/24        10.132.2.7        Pod10sw7            : e8:e7:32:d4:85:0d        1
*    2000   10.132.2.0/24        10.132.2.8        Pod10sw8            : e8:e7:32:cd:63:d3        1
*    2000   192.168.2.0/24       10.132.2.7        Pod10sw7            : e8:e7:32:d4:85:0d        1
*    2000   192.168.2.0/24       10.132.2.8        Pod10sw8            : e8:e7:32:cd:63:d3        1
*    2000   192.168.3.0/24       10.132.2.7        Pod10sw7            : e8:e7:32:d4:85:0d        1
*    2000   192.168.3.0/24       10.132.2.8        Pod10sw8            : e8:e7:32:cd:63:d3        1
*    2000   192.168.7.0/24       10.132.2.7        Pod10sw7            : e8:e7:32:d4:85:0d        1
*    2000   192.168.8.0/24       10.132.2.8        Pod10sw8            : e8:e7:32:cd:63:d3        1
Routes: 8
ISIS
(SPB IPVPN 
Route table)
Route learned from ISID 2000
-> show spb ipvpn route-table
L3-VPN

<<<PAGE 206>>>
MONITORING L3 VPN
• Display the contents of the routing table (per VRF)
-> show ip routes
-> vrf default show ip routes
+ = Equal cost multipath routes
Total 6 routes
Dest Address       Gateway Addr
Age        Protocol
------------------+-------------------+----------+-----------
10.132.2.0/24        10.132.2.7        00:00:12   LOCAL
127.0.0.1/32         127.0.0.1         00:01:36   LOCAL
192.168.2.0/24       192.168.2.7       00:00:12   LOCAL
192.168.3.0/24       192.168.3.7       00:00:12   LOCAL
192.168.7.0/24       192.168.7.7       00:00:12   LOCAL
192.168.8.0/24       10.132.2.8        00:00:05   IMPORT
RIB
(Routing
Information 
Base)
Route imported from GRT
L3-VPN

<<<PAGE 207>>>
MONITORING L3 VPN
• Displays the SPB IPVPN redistribution configuration 
• Routes redistribution from ISID to ISID or from VRF to ISID 
spb ipvpn redist source-isid 1001 destination-isid 1501 route-map Dept1toDept2 
spb ipvpn redist source-isid 1501 destination-isid 1001 route-map Dept2toDept1
Legend: * indicates redist entry is active
SPB IPVPN Redist ISID Table:
Source-ISID           Destination-ISID     Route-Map
----------------------+--------------------+--------------------
* 1001                  1501                 Dept1toDept2
* 1501                  1001                 Dept2toDept1
Total Redist ISID Entries: 2
Legend: * indicates redist entry is active
SPB IPVPN Redist VRF Table:
Source-VRF            Destination-ISID     Route-Map
----------------------+--------------------+--------------------
default               1001
Total Redist Vrf Entries: 1
-> show spb ipvpn redist
-> show spb ipvpn6 redist
L3-VPN
spb ipvpn redist source-vrf default destination-isid 1001 all-routes

<<<PAGE 208>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 209>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Implementing IP Routing over SPB-M 
Content 
1 
Objectives ...................................................................................... 2 
2 
Topological diagram .......................................................................... 2 
3 
Configuring L3-VPN routing .................................................................. 3 
3.1. Creating the mapping between the VRF and SPB services .................................... 3 
3.2. Exporting the local routes into GRT table ...................................................... 4 
3.3. Importing SPB routes into VRF default .......................................................... 4 
3.4. Analysis and understanding the concept of IP Routing over SPB ............................. 5 
3.4.1. Routing tables............................................................................................... 5 
3.4.2. Test scenario ................................................................................................ 5 
4 
Test ............................................................................................. 6

<<<PAGE 210>>>
2 
Lab: Implementing IP Routing over SPB-M 
 
 1 
Objectives 
✓ 
In this lab you will configure a scenario for routing L3 traffic over a L2 SPB-M backbone network. 
 
 
 
Be sure your partner group has completed the previous lab (Deploying a network based 
on SPB-M technology) before going on with the following exercises. 
 2 
Topological diagram

<<<PAGE 211>>>
3 
Lab: Implementing IP Routing over SPB-M 
 
 3 
Configuring L3-VPN routing 
- L3-VPN solution consists in exchanging layer 3 routes between VRFs.  
- Instead of running routing protocols on L3 VPN IP interfaces as for VPN-Lite solution, IP routes are 
imported into ISIS from VRFs and ISIS carries the routes in IPVPN TLVs over SPB network to the other SPB 
BEBs. ISIS also receives IPVPN TLVs from SPB-M network and exports them to VRFs. 
 
- In this exercise, we will implement the L3-VPN solution by allowing IP routing across SPB backbone 
between: 
o 
Clients 5 and 9 connected to OS6360-A 
o 
Clients 6 and 10 connected to OS6360-B 
o 
Clients 1 connected to OS6900-A 
o 
Clients 2 connected to OS6870-B 
o 
Clients 7 connected to OS6870-A 
o 
Clients 8 connected to OS6860-B 
 
 
3.1. 
Creating the mapping between the VRF and SPB services 
 
- Configure VRF/ISID bindings to exchange routes between Switch 1 and 2. 
- Here, we will map the VRF « default » with the SPB services 2009. 
 
 
 
 
- Disable OSPF routing 
Switch 1,2, 7 & 8 
-> ip ospf admin-state disable

<<<PAGE 212>>>
4 
Lab: Implementing IP Routing over SPB-M 
 
Switch 1 
-> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.1 all-routes 
Switch 2 
-> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.2 all-routes 
Switch 7 
-> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.7 all-routes 
Switch 8 
-> spb ipvpn bind vrf default isid 2009 gateway 10.132.2.8 all-routes 
 
 
Notes 
The VRF “default” is bound to SPB I-SID 2009 and gateway 10.132.2.x identifies the IPv4 L3VPN interfaces. 
Enables the bidirectional exchange of routes between the VRF “default” and SPB ISID 2009 via the Global Route 
Manager (GRM). 
VRF import and export commands are used to exchange routes between the VRF and I-SID specified in the 
binding configuration. 
 
3.2. 
Exporting the local routes into GRT table 
 
- Create a route-map to identify the local routes 
Switch 1,2, 7 & 8 
-> ip route-map local-to-spb sequence-number 50 action permit 
-> ip route-map local-to-spb sequence-number 50 match protocol local 
 
- Export filtered routes into GRT table 
 
 
Switch 1,2, 7 & 8 
-> ip export route-map local-to-spb 
 
 
 
Notes :  
All routes in VRF “Default” are exported to the Global Route Manager (GRM), which then exports the routes to 
I-SID 2009. 
A route map can be specified to filter exported routes. 
 
3.3. 
Importing SPB routes into VRF default 
 
 
 
Switch 1,2, 7 & 8 
-> ip import isid 2009 all-routes 
 
 
 
Notes:  
This command imports SPB service instance identifier (ISID) 2009 routes from the GRT to the default VRF. A 
route map could be specified to filter exported routes.

<<<PAGE 213>>>
5 
Lab: Implementing IP Routing over SPB-M 
 
3.4. 
Analysis and understanding the concept of IP Routing over SPB 
3.4.1. 
Routing tables 
Monitor, validate and comment the routing tables as well as associated configuration parameters by using 
following commands: 
-> show spb ipvpn bind 
-> show ip global-route-table 
-> show spb ipvpn route-table 
-> show ip routes 
-> show ip export 
-> show ip import 
-> show spb ipvpn redist 
… 
 
 
Notes: Refer to the CLI reference and Network Configuration Guides for information about outputs. 
 
 
3.4.2. 
Test scenario 
 
From Virtual machines connected on the network, run some connectivity test between clients. 
- Open the clients (shortcut 
 on access POD desktop) 
- Right-click on appropriate VM Client then select Open console 
- Configure and use VMs as shown here: 
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient1 
Switch 1 
1/1/1 
10 
192.168.10.101 
192.168.10.1 
PodXClient2 
Switch 2 
1/1/1 
20 
192.168.20.102 
192.168.20.2 
PodXClient7 
Switch 7 
1/1/1 
7 
192.168.7.107 
192.168.7.7 
PodXClient8 
Switch 8 
1/1/1 
8 
192.168.8.108 
192.168.8.8 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.254 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.254 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.254 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.254 
 
- Run continuous ping requests between the selected VM clients.  
  
- Monitor and comment the SPB network behavior: 
 
1. Display the path used between each of the clients 
 
2. Analyze the routing tables and the data path. 
 
3. Display the mac address table and check for sap port and client @mac mapping 
 
4. Disable the appropriate interconnection port to verify the network resiliency. 
 
 
You have now completed this lab.

<<<PAGE 214>>>
6 
Lab: Implementing IP Routing over SPB-M 
 
 4 
Test  
 
 
1. What is the role of the L3 VPN loopback ports? 
2. Was it necessary to export the routes from default VRF to the ISIDs ? Why? 
3. Indicate in what case the use of « route-map » is required to filter the IP 
address to be advertised or to be imported?

<<<PAGE 215>>>
IP ROUTING OVER SPB – EXAMPLES
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 216>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Analyse configuration examples
- Inline/Outline Configuration
- Inline/Outline ECMP
- Inline/Outline Routing Redundancy

<<<PAGE 217>>>
INLINE/OUTLINE CONFIGURATION EXAMPLE
spb bvlan 4001
spb bvlan 4000
spb isis control-bvlan 4000
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf default ip interface L3vpn2 address 10.5.1.3/24 service 10 
spb ipvpn bind vrf default isid 1000 gateway 10.5.1.3 all-routes
vrf default ip export all-routes
vrf default ip import isid 1000 all-routes
spb bvlan 4001
spb bvlan 4000
spb isis control-bvlan 4000
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf default ip interface L3vpn2 address 10.5.1.2/24 service 10 
spb ipvpn bind vrf default isid 1000 gateway 10.5.1.2 all-routes
vrf default ip export all-routes
vrf default ip import isid 1000 all-routes
spb bvlan 4001
spb bvlan 4000
spb isis control-bvlan 4000
spb isis admin-state enable
service spb 10 isid 1000 bvlan 4001 admin-state enable
vrf default ip interface L3vpn2 address 10.5.1.1/24 service 10 
spb ipvpn bind vrf default isid 1000 gateway 10.5.1.1 all-routes
vrf default ip export all-routes
vrf default ip import isid 1000 all-routes
VRF 
default
192.168.1.0/24
192.168.2.0/24
ISID-1000
ISID-1000
ISID-1000
L3vpn1
VRF 
default
192.168.3.0/24
192.168.4.0/24
L3vpn2
L3vpn3
VRF 
default
192.168.5.0/24
192.168.6.0/24
SPB
Backbone

<<<PAGE 218>>>
INLINE/OUTLINE CONFIGURATION EXAMPLE
VRF 
default
192.168.1.0/24
192.168.2.0/24
ISID-1000
ISID-1000
ISID-1000
L3vpn1
VRF 
default
192.168.3.0/24
192.168.4.0/24
L3vpn2
L3vpn3
VRF 
default
192.168.5.0/24
192.168.6.0/24
SPB
Backbone
sw1 -> show spb ipvpn route-table
Source Bridge
ISID   Destination          Gateway           (Name : BMAC)                             Metric
----------+--------------------+-----------------+-----------------------------------------+--------
*    1000   1.1.1.1/32           10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   2.2.2.2/32           10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   10.5.1.0/24          10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   10.5.1.0/24          10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.1.0/24       10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   192.168.3.0/24       10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.4.0/24       10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.2.0/24       10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
sw1 -> show ip global-route-table
Type  Source               Destination        Gateway         Metric
Tag
-----+--------------------+------------------+---------------+----------+----------
isid
1000                 2.2.2.2/32         10.5.1.2                 1          0
isid
1000                 10.5.1.0/24        10.5.1.2                 1          0
isid
1000                 192.168.3.0/24     10.5.1.2                 1          0
isid
1000                 192.168.4.0/24     10.5.1.2                 1          0
vrf
default              1.1.1.1/32         1.1.1.1                  1          0
vrf
default              10.5.1.0/24        10.5.1.1                 1          0
vrf
default              192.168.1.0/24     192.168.1.1              1          0
vrf
default              192.168.2.0/24     192.168.2.1              1          0
sw1 -> show ip routes
Dest Address
Gateway Addr
Age        Protocol
------------------+-------------------+----------+-----------
1.1.1.1/32           1.1.1.1           00:07:32   LOCAL
2.2.2.2/32           10.5.1.2          00:07:19   IMPORT
10.5.1.0/24          10.5.1.1          02:14:28   LOCAL
127.0.0.1/32         127.0.0.1         02:49:51   LOCAL
192.168.1.0/24       192.168.1.1       02:23:40   LOCAL
192.168.3.0/24       10.5.1.2          02:07:28   IMPORT
192.168.4.0/24       10.5.1.2          02:07:28   IMPORT
192.168.2.0/24       192.168.2.1     02:23:40   LOCAL
sw2 -> show spb ipvpn route-table
Source Bridge
ISID   Destination          Gateway           (Name : BMAC)                             
Metric
----------+--------------------+-----------------+-----------------------------------------+----
----
*    1000   1.1.1.1/32           10.5.1.1           sw1           : e8:e7:32:42:f6:11        1
*    1000   2.2.2.2/32           10.5.1.2           sw2           : 2c:fa:a2:13:e3:fa        1
*    1000   10.5.1.0/24          10.5.1.1           sw1           : e8:e7:32:42:f6:11        1
*    1000   10.5.1.0/24          10.5.1.2           sw2           : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.1.0/24       10.5.1.1           sw1           : e8:e7:32:42:f6:11        1
*    1000   192.168.3.0/24       10.5.1.2           sw2           : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.4.0/24       10.5.1.2           sw2           : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.2.0/24       10.5.1.1           sw1           : e8:e7:32:42:f6:11        1
sw2 -> show ip global-route-table
Type  Source               Destination        Gateway         Metric     Tag
-----+--------------------+------------------+---------------+----------+----------
isid
1000                 1.1.1.1/32         10.5.1.1            1          0
isid
1000                 10.5.1.0/24        10.5.1.1            1          0
isid
1000                 192.168.1.0/24     10.5.1.1            1          0
isid
1000                 192.168.2.0/24     10.5.1.1            1          0
vrf
default              2.2.2.2/32         2.2.2.2             1          0
vrf
default              10.5.1.0/24        10.5.1.2            1          0
vrf
default              192.168.3.0/24     192.168.3.2         1          0
vrf
default              192.168.4.0/24     192.168.4.2         1          0
sw2 -> show ip routes
Dest Address       Gateway Addr
Age        Protocol
------------------+-------------------+----------+-----------
1.1.1.1/32           10.5.1.1          00:08:39   IMPORT
2.2.2.2/32           2.2.2.2           00:08:26   LOCAL
10.5.1.0/24          10.5.1.2          02:08:39   LOCAL
127.0.0.1/32         127.0.0.1         03:05:29   LOCAL
192.168.10.0/24      10.5.1.1          02:08:39   IMPORT
192.168.20.0/24      192.168.20.2      02:26:23   LOCAL
192.168.3.0/24       10.5.1.1          02:08:39   IMPORT
192.168.4.0/24       10.5.1.1          02:08:39   IMPORT

<<<PAGE 219>>>
INLINE/OUTLINE ECMP CONFIGURATION EXAMPLE
L3 ECMP VPN on multiple ISIDs
spb bvlan 4001
spb bvlan 4002
service spb 10 isid 1000 bvlan 4001 admin-state enable
service spb 20 isid 1001 bvlan 4002 admin-state enable 
vrf default ip interface L3vpn21 address 10.5.1.3/24 service 10
vrf default ip interface L3vpn31 address 10.5.2.3/24 service 20
spb ipvpn bind vrf default isid 1000 gateway 10.5.1.3 all-routes
spb ipvpn bind vrf default isid 1001 gateway 10.5.2.3 all-routes
(vrf default) ip export all-routes
(vrf default) ip import isid 1000 all-routes
(vrf default) ip import isid 1001 all-routes
spb bvlan 4001
spb bvlan 4002
service spb 10 isid 1000 bvlan 4001 admin-state enable
service spb 20 isid 1001 bvlan 4002 admin-state enable
vrf default ip interface L3vpn2 address 10.5.1.2/24 service 10
vrf default ip interface L3vpn21 address 10.5.2.2/24 service 20
spb ipvpn bind vrf default isid 1000 gateway 10.5.1.2 all-routes
spb ipvpn bind vrf default isid 1001 gateway 10.5.2.2 all-routes
(vrf default)t ip export all-routes
(vrf default) ip import isid 1000 all-routes
(vrf default) ip import isid 1001 all-routes
ip interface L3vpn1 address 10.5.1.1/24 service 10
ip interface L3vpn11 address 10.5.2.1/24 service 20
spb bvlan 4001
spb bvlan 4002
vrf default ip interface L3vpn1 address 10.5.1.1/24 service 10
vrf default ip interface L3vpn11 address 10.5.2.1/24 service 20
service spb 10 isid 1000 bvlan 4001 admin-state enable
service spb 20 isid 1001 bvlan 4002 admin-state enable
spb ipvpn bind vrf default isid 1000 gateway 10.5.1.1 all-routes
spb ipvpn bind vrf default isid 1001 gateway 10.5.2.1 all-routes
(vrf default) ip export all-routes
(vrf default) ip import isid 1000 all-routes
(vrf default) ip import isid 1001 all-routes
VRF 
default
192.168.1.0/24
192.168.2.0/24
ISID-1000
OS9900
L3vpn1
L3vpn11
VRF 
default
192.168.3.0/24
192.168.4.0/24
L3vpn2
L3vpn21
L3vpn3
L3vpn31
ISID-1001
VRF 
default
192.168.5.0/24
192.168.6.0/24
SPB
Backbone
ISID-1000
ISID-1001
ISID-1000
ISID-1001

<<<PAGE 220>>>
INLINE/OUTLINE ECMP CONFIGURATION EXAMPLE
L3 ECMP VPN on multiple ISIDs
sw1 -> show ip global-route-table
Type  Source               Destination        Gateway         Metric
Tag
-----+--------------------+------------------+---------------+----------+----------
isid
1000                 2.2.2.2/32         10.5.1.2             1          0
isid
1000                 10.5.1.0/24        10.5.1.2             1          0
isid
1000                 10.5.2.0/24        10.5.1.2             1          0
isid
1000                 192.168.2.0/24     10.5.1.2             1          0
isid
1001                 2.2.2.2/32         10.5.2.2             1          0
isid
1001                 10.5.1.0/24        10.5.2.2             1          0
isid
1001                 10.5.2.0/24        10.5.2.2             1          0
isid
1001                 192.168.2.0/24     10.5.2.2             1          0
vrf
default              1.1.1.1/32         1.1.1.1              1          0
vrf
default              10.5.1.0/24        10.5.1.1             1          0
vrf
default              10.5.2.0/24        10.5.2.1             1          0
vrf
default              192.168.1.0/24     192.168.1.1          1          0
vrf
default              192.168.2.0/24     192.168.2.1          1          0
sw1 -> show spb ipvpn route-table
Source Bridge
ISID   Destination          Gateway           (Name : BMAC)                             Metric
----------+--------------------+-----------------+-----------------------------------------+--------
*    1000   1.1.1.1/32           10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   2.2.2.2/32           10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   10.5.1.0/24          10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   10.5.1.0/24          10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   10.5.2.0/24          10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   10.5.2.0/24          10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.1.0/24       10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1000   192.168.3.0/24       10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.4.0/24       10.5.1.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1000   192.168.2.0/24       10.5.1.1          sw1          : e8:e7:32:42:f6:11        1
*    1001   1.1.1.1/32           10.5.2.1          sw1          : e8:e7:32:42:f6:11        1
*    1001   2.2.2.2/32           10.5.2.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1001   10.5.1.0/24          10.5.2.1          sw1          : e8:e7:32:42:f6:11        1
*    1001   10.5.1.0/24          10.5.2.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1001   10.5.2.0/24          10.5.2.1          sw1          : e8:e7:32:42:f6:11        1
*    1001   10.5.2.0/24          10.5.2.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1001   192.168.1.0/24       10.5.2.1          sw1          : e8:e7:32:42:f6:11        1
*    1001   192.168.3.0/24       10.5.2.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1001   192.168.4.0/24       10.5.2.2          sw2          : 2c:fa:a2:13:e3:fa        1
*    1001   192.168.2.0/24       10.5.2.1          sw1          : e8:e7:32:42:f6:11        1
sw1 -> show ip routes
Dest Address
Gateway Addr
Age        Protocol
------------------+-------------------+----------+-----------
1.1.1.1/32           1.1.1.1           00:44:23   LOCAL
2.2.2.2/32          +10.5.1.2          00:00:40   IMPORT
+10.5.2.2          00:00:40   IMPORT
10.5.1.0/24          10.5.1.1          02:51:19   LOCAL
10.5.2.0/24          10.5.2.1          00:07:42   LOCAL
127.0.0.1/32         127.0.0.1         03:26:42   LOCAL
192.168.10.0/24      192.168.10.1      03:00:31   LOCAL
192.168.20.0/24     +10.5.1.2          00:00:40   IMPORT
+10.5.2.2          00:00:40   IMPORT
192.168.100.0/24     192.168.100.1     03:00:31   LOCAL
VRF 
default
192.168.1.0/24
192.168.2.0/24
ISID-1000
L3vpn1
L3vpn11
VRF 
default
192.168.3.0/24
192.168.4.0/24
L3vpn2
L3vpn21
L3vpn3
L3vpn31
ISID-1001
VRF 
default
192.168.5.0/24
192.168.6.0/24
SPB
Backbone
ISID-1000
ISID-1001
ISID-1000
ISID-1001

<<<PAGE 221>>>
sw1 -> show ip vrrp
Interface                 IPv4                 Admin                             Adv.
VRID              Name                 Address(es)    Version  Status  Priority Preempt Accept Interval
----+--------------------------------+---------------+-------+--------+--------+-------+------+--------
30      L3vpnvlan30                   192.168.30.254   V3   Enabled      200     Yes     NA      100
sw1 -> show ip vrrp statistics
Interface
VRID              Name                  State      UpTime
Become Master Adv. Rcvd
----+--------------------------------+----------+----------+-------------+----------
30       L3vpnvlan30                   Master 
73356          1           4
INLINE/OUTLINE ROUTING REDUNDANCY
ISID-1000
VRF 
192.168.1.0/24
192.168.2.0/24
SPB
Backbone
L3vpnvlan30
L3vpnvlan30
VRRP
VLAN 30
192.168.30.254
OS9900
OS6900-Q32
OS6900-X
OS6900-T
BCB
MASTER
SLAVE
Access 
SAP
ISID-1000
ISID-1000
sw2 -> show ip vrrp
Interface                 IPv4                 Admin                             Adv.
VRID              Name                 Address(es)    Version  Status  Priority Preempt Accept Interval
----+--------------------------------+---------------+-------+--------+--------+-------+------+--------
30 L3vpnvlan30                      192.168.30.254     V3   Enabled       100     Yes     NA      100
sw2 -> show ip vrrp statistics
Interface
VRID              Name                  State      UpTime
Become Master Adv. Rcvd
----+--------------------------------+----------+----------+-------------+----------
30      L3vpnvlan30                    Backup         146123            2        1208
BEB
ip vrrp 30 interface "L3vpnvlan30" priority 100 preempt interval 100 version v3
ip vrrp 30 interface "L3vpnvlan30" address 192.168.30.254
ip vrrp 30 interface "L3vpnvlan30" admin-state enable
ip vrrp 30 interface "L3vpnvlan30" priority 200 preempt interval 100 version v3
ip vrrp 30 interface "L3vpnvlan30" address 192.168.30.254
ip vrrp 30 interface "L3vpnvlan30" admin-state enable
VLAN 30
192.168.30.0/24

<<<PAGE 222>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 223>>>
SPB ADVANCED TOPOLOGIES
OMNISWITCH AOS R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 224>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Implementing SPB advanced features
- SPB over a Shared Network
- Pseudo-wire Services
- ERP/SPB interworking

<<<PAGE 225>>>
LESSON SUMMARY
✓SPB over a Shared Network
✓Pseudo-wire Services
✓ERP/SPB interworking

<<<PAGE 226>>>
SPB OVER A SHARED NETWORK

<<<PAGE 227>>>
POINT-TO-MULTI-POINT ADJACENCIES
• Objective
• Extend a SPB backbone network over a multi-access domain
• Shared
• Service provider network 
• Or connect to another SPB-ISIS domain
• Neighbours' discovery: IS-IS Hello packets
• Multiple adjacencies on an SPB network interface
• BEBs form adjacencies with each of the other BEBs 
over a shared network.
• Same IS-IS SPB extended Hello TLV as p2p
• + priority 
• + LAN id
Control Plane
Link-State 
database 
synchronization
+
LSPs 
BEB
BEB
BEB
Layer 2 
Shared Network
MPLS/802.1Q/SPB/QinQ
Microwave PMP
BEB
BEB

<<<PAGE 228>>>
POINT-TO-MULTI-POINT ADJACENCIES
• Designated intermediate system (DIS) 
• Pseudo node for a multi-access link
• Logical representation of the LAN 
• Responsible for synchronizing the LSP database
• LSPs Flooding 
• SPT calculation
• All shortest paths calculated travel through the DIS
• DIS sends LSP listing all the SPB nodes connected to
the multi-access network
• No DIS backup
• New DIS election without significant disruption (3s)
Control Plane
BEB
BEB
(DIS)
BEB
BEB
Layer 2 Shared Network
MPLS/VPLS/802.1Q/SPB/QinQ
Microwave PMP
Link-State 
database 
synchronization
+
LSPs 
• Adjacency up
• LSP packets
• DIS: Highest interface priority
• Tiebreaker: highest @BMAC
DIS Election

<<<PAGE 229>>>
CONFIGURING ISIS INTERFACES 
-> spb isis interface port 2/1 type multi-access
-> spb isis interface linkagg 5 type multi-access
Create ISIS-SPB Interfaces
BVLAN
Interfaces IS-IS
-> spb isis admin-state enable
Enable IS-IS on each system
-> spb isis interface port 2/1 priority 90
-> spb isis interface linkagg 5 priority 90
Setup ISIS-SPB Interface priority
Default: 64
Control Plane
Multi-access: Point-to-MultiPoint adjacencies (default)
Configuring a P2P and a multi-access network interfaces on the same switch is supported.
Configures the interface as an SPB multiple access LAN 
interface on which multiple adjacencies are allowed.

<<<PAGE 230>>>
MONITORING SPB
• Displays information about the ISIS-SPB interfaces
• Displays details of a IS-IS SPB interface, like interface type, oper state, priority, DIS etc.
Interface     : 1/1/8                      Type             : Multi-Access
Oper State    : UP                         Admin State      : UP
Circuit Id    : 1                          CSNP Int         : 10   sec
Desg IS       : e8e7.32c2.4e93             Adjacencies      : 2
Metric        : 10                         Hello Timer      : 9    sec
Hello Mult
: 3                          Priority         : 127
SPB ISIS Interfaces:
Oper
Admin   Link      Hello   Hello
Circ
Interface       Level   CircID
state  state
Metric    Intvl
Mult
Type
---------------+-------+----------+------+-------+---------+-------+------+------------
1/1/5           L1      1          UP     UP
10        9       3       Pt-to-Pt
1/1/6           L1      2          UP     UP      10        9       3       Multi-Access
show spb isis interfaces
show spb isis interfaces port 1/1/8
Indicates whether the interface 
was configured as a point-to-point 
(Pt-to-Pt) link or as a multiple 
access (Multi-Access) link.
Hello PDU transmissions timer
Number that is multiplied by the Hello 
Interval to determine the hold timer.
Control Plane

<<<PAGE 231>>>
MONITORING SPB
• Displays information about the multi-access DIS pseudo node
-----------------------------------------------------------------------------
Interface     : 1/1/8                      Type             : Multi-Access
Oper State    : UP                         Admin State      : UP
Circuit Id    : 1                          CSNP Int         : 10   sec
Desg IS       : e8e7.32c2.4e93
Adjacencies      : 2
Metric        : 10                         Hello Timer      : 9    sec
Hello Mult
: 3                          Priority         : 127
-----------------------------------------------------------------------------
show spb isis interfaces port 1/1/8
Elected DIS @MAC
SPB ISIS Bridge Info:
System Id             = e8e7.32c2.4e93,
System Hostname       = sw7,
SPSourceID
= 02-4e-93,
SPBM System Mode      = auto,
BridgePriority
= 32768 (0x8000),
MT ID                 = 0,
Control BVLAN         = 2000,
Area Address          = 0.0.0.0,
Level Capability      = L1,
Admin State           = UP,
LSDB Overload         = Disabled,
Last Enabled          = Thu Oct  1 13:54:13 2020,
Last SPF              = Thu Oct  1 14:56:43 2020,
SPF Wait              = Max: 1000 ms
Initial: 100 ms
Second: 300 ms,
LSP Lifetime          = 1200,
LSP Wait              = Max: 1000 ms, Initial: 0 ms, Second: 300 ms,
Graceful Restart      = Enabled,
GR helper-mode        = Enabled,
# of L1 LSPs          = 4
Control Address       = 01:80:c2:00:00:14 (AllL1)
show spb isis info
Control Plane

<<<PAGE 232>>>
MONITORING SPB
• Displays information about the multi-access DIS database
Legends : P    = The Partition repair bit is set
OV   = The overload bit is set
ATT  = The Attach bit is set
L1   = Specifies a Level 1 IS type
L2   = Specifies a Level 2 IS type
SPB ISIS LSP Database:
LSP ID                 Sequence    Checksum   Lifetime   Attributes
----------------------+-----------+----------+----------+-----------
e8e7.3281.3b7d.00-00        0x10      0x9f0        624   L1
e8e7.32a4.777d.00-00        0x16     0x4528       1152   L1
e8e7.32c2.4e93.00-00        0x0d     0x198c        605   L1
e8e7.32c2.4e93.01-00        0x07     0x10b3        660   L1
Level-1 LSP count : 4
show spb isis database
Control Plane

<<<PAGE 233>>>
MONITORING SPB
• Displays content of a particular multi-access pseudo node LSP 
SPB ISIS LSP Database:
-------------------------------------------------------------------------------
LSP ID        : e8e7.3281.3b7d.00-00                   Level     : L1
Sequence      : 0x11             Checksum  : 0x7f1     Lifetime  : 1076
Version       : 1                Pkt Type  : 18        Pkt Ver   : 1
Attributes    : L1               Max Area  : 3
SysID Len     : 6                Used Len  : 159       Alloc Len : 178
TLVs :
Area Addresses      :
Area Address     : (01) 00
Area Address     : (03) 00.00.00
Supp Protocols      :
Protocols        : SPB
IS-Hostname         :
Hostname         : sw1
TE IS Neighbors     :
Neighbor         : e8e7.32c2.4e93  SPB Metric 10 Num of Ports 1 Port-Id 0x4
MT Capability       :
MT-ID : 0x0
SPB INSTANCE     :
CIST Root-ID: 0x0 0x0
CIST Ext Root Path Cost: 0x00000000  Bridge Priority: 0x8000
SPSourceID: 0x00113b7d (Auto)        Number of Trees: 6
[#1 ] ECT-algo:0x0080c201 baseVid: 2000 spVid:   0 usedByISID: 1(I-SID) mode: 1(SPBM)
[#2 ] ECT-algo:0x0080c202 baseVid: 2001 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#3 ] ECT-algo:0x0080c203 baseVid: 2002 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#4 ] ECT-algo:0x0080c204 baseVid: 2003 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#5 ] ECT-algo:0x0080c205 baseVid: 2007 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
[#6 ] ECT-algo:0x0080c206 baseVid: 2222 spVid:   0 usedByISID: 0()      mode: 1(SPBM)
MT Capability       :
MT-ID : 0x0
SPB SVCID-UCAST-ADDR :
B-MAC e8.e7.32.81.3b.7d Base-VID 2000
[ISID# 1] 16776961 (T=1/R=1)
show spb isis database lsp-id  e8e7.3281.3b7d.00-00
Control Plane

<<<PAGE 234>>>
PSEUDO-WIRE SERVICES

<<<PAGE 235>>>
PSEUDO-WIRE SERVICES
• E-LINE connection between two local SAPs or between two SAPs across the SPB network.
• Also known as SPB Point-to-Point Transparent Circuit
• Transparent packets forwarding
• Each port or site is connected to an attachment point (SAP) of the two ends of the virtual wire
• No source @mac learning on the SAP
• Head-end multicast mode
• No Flooding and replication
Data Plane
BEB
CE-1
CE-2
I-SID 1000
SAP
SAP
SPB Network
BEB
BEB
SAP
I-SID 1000
I-SID 1000
SAP
CE-1
CE-2

<<<PAGE 236>>>
PSEUDO-WIRE SERVICES
Data Plane
-> service service_id pseudo-wire {enable | disable} [remote-node mac_address]
The SPB service will operate as a point-to-point (E-LINE) service. 
MAC address learning for the service is automatically turned off. 
The SPB service will operate as a multipoint-to-multipoint (E-LAN) service. (default) 
MAC addresses for the service are learned. 
Remote SPB node 
System ID (bridge @mac)
Create a Pseudo-wire Service
BVLAN
Interfaces IS-IS
Services
SPB Network
BEB
BEB
SAP
I-SID 1000
I-SID 1000
SAP

<<<PAGE 237>>>
MONITORING SPB
• Checking status of SAP ports
• Monitoring the traffic forwarding on SAP ports
-> show service spb 2003 sap port 1/1/1:0
SAP Detailed Info
SAP Id           : 1/1/1:0,              Description      :
Admin Status     : Up,                   Oper Status      : Up,
Stats Status     : No,                   Vlan Translation : No,
Service Type     : SPB,                  Allocation Type  : Static,
Trusted          : Yes,                  Priority         : 0,
Ingress Pkts     : 0,                    Ingress Bytes    : 0,
Egress Pkts      : 0,                    Egress Bytes     : 0,
Mgmt Change      : 10/02/2020 15:10:42,  Status Change    : 10/02/2020 15:10:51
-> show service spb 2003
SPB Service Detailed Info
Service Id       : 2003,                 Description      :                    ,
ISID             : 2003,                 BVlan
: 2003,
Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0,
Admin Status     : Up,                   Oper Status      : Up,
Stats Status     : No,                   Vlan Translation : No,
Service Type     : SPB,                  Allocation Type  : Static,
MTU              : 9194,                 VPN IP-MTU       : 1500,
SAP Count        : 1,                    SDP Bind Count   : 2,
RemoveIngressTag : No,                   Option           : None,
Ingress Pkts     : 0,                    Ingress Bytes    : 0,
Egress Pkts      : 0,                    Egress Bytes     : 0,
Mgmt Change      : 10/02/2020 14:47:11,  Status Change    : 10/02/2020 14:47:11
show service spb service_id ports
show service spb service_id sap {slot/port | linkagg agg_num} [:0 | :all | :qtag1 :outer_qtag.inner_qtag]
Data Plane

<<<PAGE 238>>>
ERP/SPB INTERWORKING

<<<PAGE 239>>>
ERP-SPB INTERWORKING
•
Objective
• Providing seamless connectivity between ERP ring and SPB network
• Forwarding ERP control frames to other ERP nodes via the SPB network
• No flooding of ERP control frames to non-ERP BEBs
• Available on OS6860E/N, OS6865, OS6900 and OS9900 models
BEB-1
BEB-2
Backbone
SPB
SAP ERP port
SDP ERP port
SAP ERP port
SDP ERP port
OmniSwitch
OmniSwitch
OmniSwitch
RPL port
ERP port
ERP port
ERP Ring
Extended ERP Ring

<<<PAGE 240>>>
ERP/SPB INTERNETWORKING
•
Topologies supported
• ERP ring connects to the SPB network through a single BEB
• ERP rings connects to separate BEBs
Backbone
SPB
ERP ring connected to 
single SPB BEB
ERP ring connected to separate 
SPB BEBs
ERP ring
ERP ring
RPL
RPL
OmniSwitch
OmniSwitch
OmniSwitch
OmniSwitch
OmniSwitch
OmniSwitch
OmniSwitch
OmniSwitch
BCB
BEB
BEB
BEB

<<<PAGE 241>>>
ERP-SPB INTERWORKING
• ERP control frames
• Contained within the control ISID
• Configured only on two ERP BEBs for a given ring
• User doesn't need to know which SDPs are used as ERP port on the BEB.
• ERP port specific configuration commands not possible in ERP BEB
• RPL port, ETHOAM config, sub-rings
• ERP protected vlans are mapped to a SPB service
• ERP link failure: Fast convergence
•
SPB BEBs participate in both SPB and ERP protocol exchanges
•
Trigger RPL port-down or port-up when a link failure is detected

<<<PAGE 242>>>
ERP-SPB GUIDELINES
• Only two ERP type NNI associations are allowed per SVLAN
• Configuring an ERP ring on 802.1q tagged port associations with SVLANs is not allowed
• Configuring an ERP ring on an STP type NNI association with an SVLAN is not allowed
• BEB cannot be a RPL node
• RPL port shall not be configured on SPB network
• RPL port cannot be configured as a SAP neighbour
• SPB Service associated with the ERP Service VLAN has to be configured in the Control BVLAN
• Ensure reachability to all nodes of the SPB network
• In case where the underlay network needs to support more than one ERP ring
• Ensure there is no overlap in the VLAN range supported within the ERP rings
• That is, each ERP ring must have an exclusive range of VLANs including the service VLAN relative to the other 
ERP rings
• In the underlay network, the services association with the ERP VLANS is exclusive to each ring
• The service IDs cannot extend across/into the other ERP rings

<<<PAGE 243>>>
ERP-SPB CONFIGURATION
-> erp-ring ring_id port1 {chassis/slot/port | linkagg agg_id port2 {chassis/slot/port | linkagg agg_id} service-vlan vlan_id level level_num
-> erp-ring ring_id rpl-node {port chassis/slot/port | linkagg agg_id}  
-> erp-ring ring_id enable
Configure the RPL on one node
Create ERP ring, ERP Service VLAN and MEG Level and associate two ports to the ring
Create Protected VLANs
Enable ERP Ring and ports
default: disable
ERP –SPB interworking
Configure ERP ring SAP neighbor on nodes connected to the BEB's SAP ports
-> erp-ring ring_id sap-neighbor {port chassis/slot/port | linkagg agg_id}
SPB BEB nodes
Create Service
Configure SAP for ERP Vlans
Setup ERP ring SAP neighbor
MAC address of the remote system of 
the BEB where the other end of the ERP 
ring is connected as the access port.
-> erp-ring ring_id port1 {chassis/slot/port | linkagg agg_id access-[tagged | untagged] spb-remote-system switch_mac_address service-vlan vlan_id level level_num
-> erp-ring ring_id enable
Tagged: ERP cpntrol vlan mapped to tagged SAP
Untagged: ERP cpntrol vlan mapped to untagged SAP
Backbone
SPB
ERP ring
RPL
OmniSwitch
OmniSwitch
OmniSwitch
OmniSwitch
BCB
BEB
BEB
ERP nodes

<<<PAGE 244>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 245>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Setting up advanced SPB topologies 
Contents 
1 
Configuring a Point to Multipoint SPB topology ........................................... 2 
1.1. Configure switch to simulate as a LAN shared network ....................................... 3 
1.2. Disable existing backbone network ports ....................................................... 3 
1.3. Configure network ports as multi-access network interface. ................................ 4 
1.4. Checking the configuration ....................................................................... 4 
1.5. Analysing the shortest path calculation ......................................................... 4 
2 
Configuring Redundant access port - case 1............................................... 6 
2.1. Logical diagram ..................................................................................... 6 
2.2. Access switch ....................................................................................... 6 
2.2.1. Create User Vlans .......................................................................................... 7 
2.3. SPB Service Configuration ......................................................................... 7 
2.3.1. Setup the SPB ingress ports as access port ............................................................. 7 
2.3.2. Configure two new services for Finance and Marketing department ................................ 8 
2.3.3. Create SAP for Finance VLAN ............................................................................. 8 
2.3.4. Initialize the classification process. ..................................................................... 8 
2.3.5. Configure vlan-xlation ..................................................................................... 8 
2.3.6. Monitoring DHL configuration ............................................................................. 9 
2.3.7. Configure Routing for Vlans Finance & Marketing ..................................................... 9 
2.4. Configuration monitoring .......................................................................... 9 
2.5. Testing connectivity .............................................................................. 10 
3 
Configuring Redundant access port - case 2............................................. 11 
3.1. Logical diagram .................................................................................... 11 
3.2. Physical diagram ................................................................................... 11 
3.3. Setup access switch parameters ................................................................ 12 
3.3.1. Prequisites ................................................................................................. 12 
3.3.2. Setup access switch parameters ....................................................................... 12 
3.4. Setup SPB edge switch parameters ............................................................. 13 
3.5. Checking the ERP Ring 1 configuration ......................................................... 14 
3.6. ERP Protection switching mechanism test ..................................................... 14

<<<PAGE 246>>>
2 
Lab: Setting up advanced SPB topologies 
 
 1 
Configuring a Point to Multipoint SPB topology 
In case where BEBs are connected to other BEBs over a multi-access domain, each SPB network interface port 
must be configured as a multi-access interface to allow multiple adjacencies to form across the broadcast 
network domain. 
 
 
Notes 
By default, the SPB network interface type is set to Point-to-Point.  
 
 
 
In this exercise, we will use the switch 3 (OS6560-A) to emulate the shared network as follow: 
 
 
 
 
 
Notes 
A Designated Intermediate System (DIS) election process determines which multiple 
access LAN interface will serve as the DIS for the network. 
All BEB interfaces report their adjacencies to the DIS.

<<<PAGE 247>>>
3 
Lab: Setting up advanced SPB topologies 
 
1.1. 
Configure switch to simulate as a LAN shared network 
Switch 3 
! First remove Vlan 2 used in previous lab 
-> no vlan 2  
-> no ip interface vlan2 
-> interfaces 1/1/1 admin-state disable 
-> interfaces 1/1/7 admin-state disable 
 
! Enter following instructions 
-> vlan 2000-2002 members port 1/1/3-4 tagged 
-> vlan 2000-2002 members port 1/1/7-8 tagged 
-> interfaces 1/1/3-4 admin-state enable 
-> interfaces 1/1/7-8 admin-state enable 
1.2. 
Disable existing backbone network ports 
Switch 1 
-> spb isis interface port 1/1/25 admin-state disable 
-> spb isis interface port 1/1/5 admin-state disable 
-> spb isis interface port 1/1/6 admin-state disable 
-> interfaces 1/1/5-6 admin-state disable  
-> interfaces 1/1/25 admin-state disable  
Switch 2 
-> spb isis interface port 1/2/1 admin-state disable 
-> spb isis interface port 1/1/5 admin-state disable 
-> spb isis interface port 1/1/6 admin-state disable 
-> interfaces 1/1/5-6 admin-state disable  
-> interfaces 1/2/1 admin-state disable  
Switch 7 
-> spb isis interface port 1/1/5 admin-state disable 
-> spb isis interface port 1/1/6 admin-state disable 
-> interfaces 1/1/5-6 admin-state disable  
 
! In addition, remove access port used in previous lab 
-> service spb 2001 no sap port 1/1/7:2  
-> no service access port 1/1/7 
-> interfaces 1/1/7 admin-state disable 
Switch 8 
-> spb isis interface port 1/1/5 admin-state disable 
-> spb isis interface port 1/1/6 admin-state disable 
-> interfaces 1/1/5-6 admin-state disable

<<<PAGE 248>>>
4 
Lab: Setting up advanced SPB topologies 
 
1.3. 
Configure network ports as multi-access network interface. 
Switch 1 
-> spb isis interface port 1/1/3 type multi-access 
-> interfaces 1/1/3 admin-state enable 
Switch 2 
-> spb isis interface port 1/1/4 type multi-access 
-> interfaces 1/1/4 admin-state enable  
Switch 7 
-> spb isis interface port 1/1/7 type multi-access priority 127 
-> interfaces 1/1/7 admin-state enable  
Switch 8 
-> spb isis interface port 1/1/8 type multi-access 
-> interfaces 1/1/8 admin-state enable  
1.4. 
Checking the configuration 
 
-> show spb isis adjacency 
-> show spb isis interface 
-> show spb isis services 
-> show spb isis unicast-table 
-> show spb isis nodes 
-> show spb isis database 
-> show spb isis bvlans 
-> show spb isis info 
-> show vlan 2000 (Backbone Control Vlan) 
-> show service 
-> show service access 
-> show service spb 
-> show service sdp spb 
-> show service spb id ports  
-> show service mesh-sdp 
-> show service spb id debug-info 
-> show mac-learning 
1.5. 
Analysing the shortest path calculation 
 
- Which command can be used to display the p2p or multi-access interfaces? 
- Identify and comment the SPB Path between Client 5 and 6. 
Switch 7 
-> show spb isis spf bvlan 2001 
Switch 8 
-> show spb isis spf bvlan 2001 
 
- Compare to the p2p configuration, explain the changes. 
- Which command allows you to 
- Display the DIS (designated IS)? 
- Do the switch 6900-A to be the DIS?

<<<PAGE 249>>>
5 
Lab: Setting up advanced SPB topologies 
 
 Before continuing, enter the following to return to previous SPB P2P backbone topology 
Switch 1 
-> no spb isis interface port 1/1/3 
-> interfaces 1/1/3 admin-state disable 
-> spb isis interface port 1/1/25 admin-state enable 
-> spb isis interface port 1/1/5 admin-state enable 
-> spb isis interface port 1/1/6 admin-state enable 
-> interfaces 1/1/5-6 admin-state enable  
-> interfaces 1/1/25 admin-state enable 
Switch 2 
-> no spb isis interface port 1/1/4 
-> interfaces 1/1/4 admin-state disable 
-> spb isis interface port 1/2/1 admin-state enable 
-> spb isis interface port 1/1/5 admin-state enable 
-> spb isis interface port 1/1/6 admin-state enable 
-> interfaces 1/1/5-6 admin-state enable 
-> interfaces 1/2/1 admin-state enable 
Switch 7 
-> no spb isis interface port 1/1/7 
-> interfaces 1/1/7 admin-state disable 
-> spb isis interface port 1/1/5 admin-state enable 
-> spb isis interface port 1/1/6 admin-state enable  
-> interfaces 1/1/5-6 admin-state enable 
Switch 8 
-> no spb isis interface port 1/1/8 
-> interfaces 1/1/8 admin-state disable 
-> spb isis interface port 1/1/5 admin-state enable 
-> spb isis interface port 1/1/6 admin-state enable 
-> interfaces 1/1/5-6 admin-state enable  
Switch 3 
-> no vlan 2000-2002 
-> interfaces 1/1/3-4 admin-state disable 
-> interfaces 1/1/7-8 admin-state disable

<<<PAGE 250>>>
6 
Lab: Setting up advanced SPB topologies 
 
 2 
Configuring Redundant access port - case 1 
2.1. 
Logical diagram 
 
You will configure SPB SAP ports to assign dynamically client 3 moving to Marketing or to Finance departments, 
respectively to the service 4003 and 4004. 
 
2.2. 
Access switch 
 
To setup a dual attachment of the access switch to the BEB nodes, we will use an AOS feature called DHL 
(Dual Home Link). 
 
 
 
Reminders 
The Dual-Home Link (DHL) is an AOS feature on access switches. 
DHL provides fast failover between core and edge switches without implementing 
Spanning Tree. 
A DHL Active-Active configuration consists of the following components: 
- 
A DHL session. Only one session per switch is allowed. 
- 
Two DHL links associated with the session (link A and link B).  
- 
A physical switch port or a logical link aggregate (linkagg) ID are configurable as a DHL link. 
- 
A group of VLANs (or pool of common VLANs) in which each VLAN is associated (802.1q tagged) with 
both link A & link B. 
- 
A VLAN-to-link mapping that specifies which of the VLANs each DHL link will service.

<<<PAGE 251>>>
7 
Lab: Setting up advanced SPB topologies 
 
2.2.1. 
Create User Vlans 
Switch 3 
-> vlan 30 name Finance 
-> ip interface Finance address 192.168.30.3/24 vlan 30 
-> vlan 30 members port 1/1/7 tagged 
-> vlan 30 members port 1/1/8 tagged 
-> vlan 30 members port 1/1/1 untagged 
-> vlan 40 name Marketing 
-> ip interface Marketing address 192.168.40.3/24 vlan 40 
-> vlan 40 members port 1/1/7 tagged 
-> vlan 40 members port 1/1/8 tagged 
 
- Setup switch 3 dual attachment to the core with AOS DHL feature 
Switch 3 
-> dhl 1 
-> dhl 1 linka port 1/1/7 linkb port 1/1/8 
-> dhl 1 vlan-map linkb 40 
-> dhl 1 mac-flushing raw 
-> dhl 1 admin-state enable 
-> interfaces 1/1/7-8 admin-state enable 
-> interfaces 1/1/1 admin-state enable 
 
2.3. 
SPB Service Configuration 
 
 
2.3.1. 
Setup the SPB ingress ports as access port 
Switch 7 
-> service access port 1/1/7 
Switch 8 
-> service access port 1/1/8 
 
 
Notes 
Access ports are required to configure a SAP.  
The access port can be either a fixed port or logical port (linkagg).

<<<PAGE 252>>>
8 
Lab: Setting up advanced SPB topologies 
 
A SAP is the point at which customer traffic enters and exits the service. SAPs are not configurable on other 
port types. 
2.3.2. 
Configure two new services for Finance and Marketing department 
Switch 1, 2, 7 & 8 
-> service spb 4003 isid 4003 bvlan 2002 description Finance admin-state enable 
-> service spb 4004 isid 4004 bvlan 2002 description Marketing admin-state enable 
 
2.3.3. 
Create SAP for Finance VLAN 
 
- On Switch 7 and 8, classify the Vlan30 and Vlan40 traffic on the uplink port 
Switch 7 
 
-> service spb 4003 sap port 1/1/7:30 admin-state enable stats enable 
-> service spb 4004 sap port 1/1/7:40 admin-state enable stats enable 
Switch 8 
 
-> service spb 4003 sap port 1/1/8:30 admin-state enable stats enable 
-> service spb 4004 sap port 1/1/8:40 admin-state enable stats enable 
2.3.4. 
Initialize the classification process. 
Switch 7 
 
-> interfaces 1/1/7 admin-state disable 
-> interfaces 1/1/7 admin-state enable 
Switch 8 
 
-> interfaces 1/1/8 admin-state disable 
-> interfaces 1/1/8 admin-state enable 
2.3.5. 
Configure vlan-xlation 
Switch 7 
 
-> service access port 1/1/7 vlan-xlation enable 
-> service 4003 vlan-xlation enable 
-> service 4004 vlan-xlation enable 
Switch 8 
 
-> service access port 1/1/8 vlan-xlation enable 
-> service 4003 vlan-xlation enable 
-> service 4004 vlan-xlation enable 
Switch 1&2 
 
-> service 4003 vlan-xlation enable 
-> service 4004 vlan-xlation enable

<<<PAGE 253>>>
9 
Lab: Setting up advanced SPB topologies 
 
2.3.6. 
Monitoring DHL configuration 
- Display the DHL configuration. The output must be as follow: 
Switch 3 
-> show dhl 1 
DHL session name           : DHL-1 
  Admin state              : up, 
  Operational state        : up, 
  Pre-emption time(sec)    : 30, 
  Mac Flushing             : raw, 
  Active MAC flushing      : raw, 
  LinkB Vlan Map           : 40, 
  Protected Vlans          : 1 30 40 
    LinkA: 
      Port                 : 1/1/7, 
      Operational State    : up, 
      Unprotected Vlans    : none, 
      Active  Vlans        : 1 30 
    LinkB: 
      Port                 : 1/1/8, 
      Operational State    : up, 
      Unprotected Vlans    : none, 
      Active  Vlans        : 40 
2.3.7. 
Configure Routing for Vlans Finance & Marketing 
Switch 1 
-> ip interface L3vpnvlan30 address 192.168.30.1/24 service 4003 
-> ip vrrp 30 interface L3vpnvlan30 priority 200 
-> ip vrrp 30 interface L3vpnvlan30 address 192.168.30.254 
-> ip vrrp 30 interface L3vpnvlan30 admin-state enable 
 
-> ip interface L3vpnvlan40 address 192.168.40.1/24 service 4004 
-> ip vrrp 40 interface L3vpnvlan40 priority 100 
-> ip vrrp 40 interface L3vpnvlan40 address 192.168.40.254 
-> ip vrrp 40 interface L3vpnvlan40 admin-state enable 
Switch 2 
-> ip interface L3vpnvlan30 address 192.168.30.2/24 service 4003 
-> ip vrrp 30 interface L3vpnvlan30 priority 100 
-> ip vrrp 30 interface L3vpnvlan30 address 192.168.30.254 
-> ip vrrp 30 interface L3vpnvlan30 admin-state enable 
 
-> ip interface L3vpnvlan40 address 192.168.40.2/24 service 4004 
-> ip vrrp 40 interface L3vpnvlan40 priority 200 
-> ip vrrp 40 interface L3vpnvlan40 address 192.168.40.254 
-> ip vrrp 40 interface L3vpnvlan40 admin-state enable 
2.4. 
Configuration monitoring 
Switch 1 & 2 
-> show ip vrrp 
-> show ip vrrp 30 
-> show ip vrrp 40 
-> show ip vrrp statistics 
Switch 7 & 8 
-> show service 
-> show service access 
-> show mac-learning domain spb 
-> show service 
-> show service id port

<<<PAGE 254>>>
10 
Lab: Setting up advanced SPB topologies 
 
2.5. 
Testing connectivity 
- Connect to the Client 3 console, change the IP address to match vlan 30: 
 
Client 3 
192.168.30.103/24    
GW: 192.168.30.254 
 
- Reinitialize port. 
Switch 7 
-> interfaces 1/1/7 admin-state disable 
-> interfaces 1/1/7 admin-state enable 
Switch 8 
-> interfaces 1/1/8 admin-state disable 
-> interfaces 1/1/8 admin-state enable 
 
- Check for MAC addresses learned on an access port 
Switch 7 & 8 
-> show mac-learning domain spb 
-> show service 4003 ports 
 
- Resiliency 
Check for resiliency at the access by running continuous ping from client 3 to its gateway, then on the 
switch 3, disable the port 1/1/7 when client in Vlan 30 or 1/1/8 when in vlan 40. 
Monitor the location on client 3 @MAC on switch 7 and/or 8 as well as the ping traffic behavior. 
 
 
Notes 
To move client 3 from Vlan 30 to vlan 40, just run the command: 
-> vlan 40 members port 1/1/1 untagged 
Change client 3 @IP 
Client 3 
192.168.40.104/24    
GW: 192.168.40.254

<<<PAGE 255>>>
11 
Lab: Setting up advanced SPB topologies 
 
 3 
Configuring Redundant access port - case 2 
In this exercise, the Finance and Marketing users are assigned to services 4003 and 4004 respectively and are 
connected on access switches 5 and 6 members of a ring network. 
3.1. 
Logical diagram 
 
 
3.2. 
Physical diagram

<<<PAGE 256>>>
12 
Lab: Setting up advanced SPB topologies 
 
3.3. 
Setup access switch parameters 
To setup a dual attachment of the access layer to the BEB nodes, we will use the ERP feature. 
This feature allows ERP protected VLANs to be mapped dynamically and manually to a service on the SPBM 
network on the same SAP.  
This functionality is configured on a gateway switch that supports both ERP and SPB.  
3.3.1. 
Prequisites 
Switch 5 and 6 
-> cp labinit/vcboot.cfg working 
-> cp labinit/vcboot.cfg certified 
-> cp labinit/vcsetup.cfg working 
-> cp labinit/vcsetup.cfg certified 
-> cp labinit/pre_banner.txt switch 
-> reload from working no rollback-timeout 
3.3.2. 
Setup access switch parameters 
Switch 5 
- Create protected vlans 
-> vlan 30 name Finance 
-> vlan 40 name Marketing 
-> vlan 30 members port 1/1/1 untagged 
-> vlan 30 members port 1/1/3 tagged 
-> vlan 30 members port 1/1/27 tagged 
-> vlan 40 members port 1/1/27 tagged 
-> vlan 40 members port 1/1/3 tagged  
-> ip interface Finance address 192.168.30.5 mask 255.255.255.0 vlan 30 
- Create Service Vlan 
-> vlan 1000 name erp-service 
-> vlan 1000 members port 1/1/3 tagged 
-> vlan 1000 members port 1/1/27 tagged 
- Create ERP ring ID 1 on two ports with service vlan 1000 and MEG level 1 
-> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1000 level 1 
- Setup Switch 5 as RPL owner node 
-> erp-ring 1 rpl-node port 1/1/27 
-> erp-ring 1 wait-to-restore-timer 1 
- Configure ERP ring SAP neighbor 
-> erp-ring 1 sap-neighbor port 1/1/3 
- Activate the ERP ring  
-> erp-ring 1 enable 
-> interfaces 1/1/3 admin-state enable 
-> interfaces 1/1/27 admin-state enable 
Switch 6 
- Create protected vlans 
-> vlan 30 name Finance 
-> vlan 40 name Marketing 
-> vlan 40 members port 1/1/1 untagged 
-> vlan 40 members port 1/1/3 tagged 
-> vlan 40 members port 1/1/27 tagged 
-> vlan 30 members port 1/1/27 tagged 
-> vlan 30 members port 1/1/3 tagged 
-> ip interface Marketing address 192.168.40.6 mask 255.255.255.0 vlan 40 
- Create Service Vlan 
-> vlan 1000 name erp-service 
-> vlan 1000 members port 1/1/3 tagged 
-> vlan 1000 members port 1/1/27 tagged

<<<PAGE 257>>>
13 
Lab: Setting up advanced SPB topologies 
 
- Create ERP ring ID 1 on two ports with service vlan 1000 and MEG level 1. 
-> erp-ring 1 port1 1/1/3 port2 1/1/27 service-vlan 1000 level 1 
- Configure ERP ring SAP neighbor 
-> erp-ring 1 sap-neighbor port 1/1/3 
 
 
Notes 
The SAP neighbor port is on the ERP ring node, which has the connection to the BEB's SAP port 
 
- Activate the ERP ring  
-> erp-ring 1 enable 
-> interfaces 1/1/3 admin-state enable 
-> interfaces 1/1/27 admin-state enable 
3.4. 
Setup SPB edge switch parameters 
Switch 7 
-> interfaces 1/1/3 admin-state disable 
-> service 4003 spb isid 4003 bvlan 2002 description Finance 
-> service 4004 spb isid 4004 bvlan 2002 description Marketing 
- Create SAP for user VLANs 
-> service access port 1/1/3 
-> service 2009 sap port 1/1/3:1000 
-> service 4003 sap port 1/1/3:30 
-> service 4004 sap port 1/1/3:40 
- Create ERP ring ID 1 on two ports with service vlan 1000 and MEG level 1. 
-> erp-ring 1 port1 access-tagged 1/1/3 spb-remote-system switch_mac_address service-vlan 1000 level 1 
 
 
Notes 
The MAC address of the remote system of the BEB where the other end of the ERP ring is connected as the 
access port. 
 
- Activate the ERP ring  
-> erp-ring 1 enable 
-> interfaces 1/1/3 admin-state enable 
Switch 8 
-> interfaces 1/1/3 admin-state disable 
-> service 4003 spb isid 4003 bvlan 2002 description "Finance" 
-> service 4004 spb isid 4004 bvlan 2002 description "Marketing" 
- Create SAP for user VLANs 
-> service access port 1/1/3 
-> service 2009 sap port 1/1/3:1000 
-> service 4003 sap port 1/1/3:30 
-> service 4004 sap port 1/1/3:40 
- Create ERP ring ID 1 on two ports with service vlan 1000 and MEG level 1. 
-> erp-ring 1 port1 access-tagged 1/1/3 spb-remote-system switch_mac_address service-vlan 1000 level 1 
- Activate the ERP ring  
-> erp-ring 1 enable 
-> interfaces 1/1/3 admin-state enable

<<<PAGE 258>>>
14 
Lab: Setting up advanced SPB topologies 
 
3.5. 
Checking the ERP Ring 1 configuration 
- On all nodes, check the ERP setup 
 
-> show erp 
-> show erp ring 1 
-> show erp { port <slot/port> |linkagg <Id>}  
 
-> show erp statistics ring <ringId>  
-> show erp statistics ring <ringId> { port <slot/port> | linkagg <Id>}  
-> clear erp statistics  
-> clear erp statistics ring <ringId>  
-> clear erp statistics ring <ringId> { port <slot/port> |linkagg <Id>}  
3.6. 
ERP Protection switching mechanism test 
- Run a continuous ping test from client 5 and 6 to their default gateways presuming the port 1/1/27 switch 
5 is blocked. Then unplug port 1/1/3 switch 6 and analyse the test behaviour and switches status by 
working around following commands and its options. 
-> show erp 
-> show erp port <chassis/slot/port> 
-> show erp ring 1 
-> show erp statistics 
- Check the time RPL switch waits before returning the RPL port 1/1/27 on switch 5 to a blocked state after 
the ERP ring has recovered from a link failure. 
You have now completed this lab.

<<<PAGE 259>>>
SPB DYNAMIC SERVICES
OMNISWITCH AOS R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 260>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe and Manage in SPB context
- UNP port
- UNP Authentication
- UNP SPB Classification
- UNP SPB Service configuration
- Dynamic UNP/Service creation

<<<PAGE 261>>>
UNP SPB CLASSIFICATION
SPB Service Profile
UNP port
MAC / 802.1x
CP / Kerberos
authentication
or
Classification
Rules?
UNP SPB profile
VLAN Tag
I-SID
BVLAN ID
Multicast-mode
VLAN translation
Policy List
ACL
QoS
SPB Service Classification

<<<PAGE 262>>>
SERVICE ACCESS POINT (DYNAMIC)
-> unp port 3/1/20 port-type access
-> unp linkagg 10 port-type access
UNP Port 
Service Access ports
VLAN
10
VLAN
20
VLAN
30
Access
SPB-M
Core 
Network
BEB
B Comp
I Comp
BVLAN
4001
BVLAN
4003
ID
1001
ISID
1002
ISID
1003
BVLAN
4002
Create a Service access port
* Redirecting quarantined users learned on UNP access ports for remediation is not supported 
Dynamic SAPs supported from UNP service 
profiles
Device assignment to an SPB service profile
Automatic SAP creation
Quarantine Manager support *
LPS support

<<<PAGE 263>>>
SPB SERVICES
SPB NNI
BEB
UNP Port
Static, Dynamic or 
persistent SAP
SPB UNI
Service
4005 
Backbone SPB
SPB UNP profile
VLAN Tag: 3
I-SID: 1000
BVLAN ID: 4015
Multicast-mode: Headend
VLAN translation: Disable
Policy List
ACL
QoS
Dynamic Service
SPB UNP profile
VLAN Tag: 3
I-SID: 1000
BVLAN ID: 4015
Multicast-mode: Headend
VLAN translation: Disable
Policy List
ACL
QoS
Persistent SAP
SPB UNP profile
VLAN Tag: 3
I-SID: 1000
BVLAN ID: 4015
Multicast-mode: Headend
VLAN translation: Disable
Policy List
ACL
QoS
Authentication
SPB UNP profile
VLAN Tag: 3
I-SID: 1000
BVLAN ID: 4015
Multicast-mode: Headend
VLAN translation: Disable
Policy List
ACL
QoS
Dynamic SAP
SPB UNP profile
VLAN Tag: 3
I-SID: 1000
BVLAN ID: 4015
Multicast-mode: Headend
VLAN translation: Disable
Policy List
ACL
QoS
Static SAP
BVLAN 4001
BVLAN 4002
BVLAN 4003
BVLAN 4004
BVLAN 4005
Service
32770
Service
4004 
Service
4001 
Service
4003 
•
MAC-based (non-supplicant)
•
802.1x-based (supplicant)

<<<PAGE 264>>>
-> unp profile profile_name
-> unp profile profile_name map service-type spb tag-value {0 | ALL | outer_qtag:all | qtag | 
outer_qtag:inner_qtag} isid instance_id
bvlan bvlan_id [multicast-mode {headend | tandem}] [vlan-xlation] 
Other options: captive-portal-authentication, kerberos-authentication, location-policy <lp-name>, period-policy <pp-name>
-> unp {port chassis/slot/port1 | linkagg agg_id1} port-type access
-> unp {port chassis/slot/port1 | linkagg agg_id1} 802.1x authentication
-> unp {port chassis/slot/port1 | linkagg agg_id1} mac authentication
-> aaa radius-server server_name host {hostname | ip_address | ipv6_address} [hostname2 | ip_address2 | 
ipv6_address2] {key secret | hash-key hash_secret | prompt-key} [retransmit retries] [timeout seconds] 
[auth-port auth_port] [acct-port acct_port] [vrf-name name] [ssl | no ssl] 
CONFIGURATION STEPS
Configuring UNP SPB Profile
Configuring UNP Port type
Configuring UNP Authentication Server
Authentication

<<<PAGE 265>>>
-> unp profile my_profile1
-> unp profile my_profile1 map service-type spb tag-value 10 isid 1000 bvlan 4015
-> unp port 1/1/1-5 port-type access
-> unp port 1/1/1-5 802.1x authentication
-> unp port 1/1/1-5 mac authentication
-> aaa radius-server AAA host 192.168.100.102/24 key mysharedkey
-> aaa device-authentication mac AAA
-> aaa device-authentication 802.1x AAA
CONFIGURATION EXAMPLE
1.
What Profile to assign?
2. Which Access Ports?
3. How to classify?
4. Which Authentication server?
Configuring UNP Port type
Configuring UNP Authentication Server
UNP Access ports
BEB
VLAN 10
1/1/1-5
Configuring UNP SPB Profile
Authentication

<<<PAGE 266>>>
-> unp profile profile_name
-> unp profile profile_name map service-type spb tag-value {0 | ALL | outer_qtag:all | qtag | 
outer_qtag:inner_qtag} 
isid instance_id bvlan bvlan_id [multicast-mode {headend | tandem}] [vlan-xlation]
-> unp {port chassis/slot/port1 | linkagg agg_id1} port-type access
-> unp {port chassis/slot/port1 | linkagg agg_id1} classification
-> unp classification rule_type {rule options} {profile1 profile_name [profile2 profile_name] [profile3
profile_name]}
CONFIGURATION STEPS
Configuring UNP Port type
Configuring UNP Classification Rules
1.
What Profile to assign?
2. Which Access Ports?
3. How to classify?
Configuring UNP SPB Profile
Classification

<<<PAGE 267>>>
Configuring UNP SPB Profile
-> unp classification mac-range low_mac_add high_mac_add vlan-tag {vlan_id} {profile1 profile_name[profile2 profile_name] 
[profile3 profile_name]}
CONFIGURING UNP CLASSIFICATION RULES 
Authentication
UNP Port classification rule 
precedence
1.
– MAC address + VLAN tag
2.
– MAC address
3.
– MAC address range + VLAN tag
4.
– MAC address range
5.
– IP address + VLAN tag
6.
– IP address
7.
– VLAN tag
-> unp classification mac-address mac_address vlan-tag {vlan_id} {profile1 profile_name [profile2 profile_name] [profile3
profile_name]}
-> unp classification mac-address mac_address {profile1 profile_name [profile2 profile_name] [profile3 profile_name]}
-> unp classification ip-address ip_address mask subnet_mask vlan-tag {vlan_id} {profile1 profile_name [profile2 profile_name] 
[profile3 profile_name]}
-> unp classification mac-range low_mac_address high_mac_address {profile1 profile_name[profile2 profile_name] [profile3
profile_name]}
-> unp classification ip-address ip_address mask subnet_mask {profile1 profile_name [profile2 profile_name] [profile3
profile_name]}
-> unp classification vlan-tag {vlan_id} {profile1 profile_name [profile2 profile_name] [profile3 profile_name]}
UNP Classification Rules

<<<PAGE 268>>>
-> unp profile my_profile1
-> unp profile my_profile1 map service-type spb tag-value 10 isid 1000 bvlan 4015
-> unp port 1/1/1-5 port-type access
-> unp port 1/1/1-5 classification
-> unp classification vlan-tag 10 profile1 myprofile
CONFIGURATION STEPS
Configuring UNP SPB Profile
Configuring UNP Port type
Classification
Configuring UNP Classification Rules
UNP Access ports
BEB
VLAN 10
1/1/1-5
1.
What Profile to assign?
2. Which Access Ports?
3. How to classify?

<<<PAGE 269>>>
-> unp {port chassis/slot/port1[-port2] | linkagg agg_id[-agg_id2]}  
default-profile profile_name
-> unp {port chassis/slot/port1[-port2] | linkagg agg_id[-agg_id2]}
802.1x-authentication } pass-alternate profile_name
CONFIGURING UNP CLASSIFICATION 
OPTIONS
Name of an existing SPB service-based UNP to serve as the 
default for the specified UNP access port or LAG
Existing SPB service-based UNP to use as an alternate UNP 
when successful MAC or 1x auth does not return a UNP name
WebView
WebView
Configuring UNP SPB Profile
Default UNP/SPB Profile
Pass-Alternate UNP/SPB Profile

<<<PAGE 270>>>
-> unp port-template template_name options
-> unp {port chassis/slot/port1[-port2] | linkagg agg_id[-agg_id2]} port-template template_name
-> unp {port chassis/slot/port1 | linkagg agg_id} port-template template_name
CONFIGURING UNP PORT TEMPLATES
Configuring UNP Port template
UNP Port Template
Apply Port Template to a UNP port
[802.1x-authentication]
[802.1x-authentication pass-alternate profile_name]
[mac-authentication]
[mac-authentication pass-alternate profile_name]
[classification]
[trust-tag]
[default-profile profile_name]
[domain domain_id]
[aaa-profile profile_name]
[redirect port-bounce]
[direction {in | both}]
[802.1x-authentication tx-period seconds]
[802.1x-authentication supp-timeout seconds]
[802.1x-authentication max-req max_req]
[802.1x-authentication bypass]
[802.1x-authentication failure-policy {mac}]
[mac-authentication allow-eap {pass | fail | noauth}]
[force-l3-learning [port-bounce]]
[admin-state {enable | disable}
[dynamic-service {spb | vxlan}
[vlan vlan_id [-vlan_id2] [tagged]
[l2-profile l2profile_name]
[profile profile_name]
[ap-mode]
Display Port Template parameters

<<<PAGE 271>>>
MULTIPLE UNTAGGED TRAFFIC ON UNP 
-> unp multi-untag-sap
-> show unp global configuration 
Configuring multiple untagged MAC 
Enable multiple untagged users
Classification of different untagged users to the same UNP dynamic untagged SAP
Users can be associated to different services SPB
Supported only for UNP dynamic SAPs
Available on:
•
6860N
•
6900-V72 
•
6900-X48C6/T48C6/X48C4E
•
6900-V48C8
•
6900-C32/32E
•
6900-T24C2/ X24C2
Dynamic Vlan Configuration
= Disabled,
Dynamic Profile Configuration
= Disabled,
Auth Server Down Profile1
= -,
Auth Server Down Profile2
= -,
Auth Server Down Profile3
= -,
Auth Server Down Voice Profile1
= -,
Auth Server Down Voice Profile2
= -,
Auth Server Down Voice Profile3
= -,
Auth Server Down Port Bounce
= Disabled
Auth Server Down Timeout
= 60,
Redirect Port Bounce
= Enabled,
Redirect Pause Timer
= -,
Redirect http proxy-port
= 8080,
Redirect Server FQDN
= -,
Redirect Server IP
= -,
Allowed IP
= -,
Force L3-Learning
= Disabled,
Force L3-Learning Port Bounce
= Enabled,
802.1x Pass Through Mode
= Disabled,
AP Mode
= Enabled,
Secure AP Mode
= Disabled,
System-default service-mod
= 512,
System-default service-base
= 10000000,
System-default MulticastMode
= Headend,
System-default Vlan-Xlation
= Enabled,
System-default MulticastGroup
= 239.0.0.0,
System-default far-end-ip-list
= -,
IPv6 Drop Packets
= Disabled,
Delayed Learning Interval
= 0,
Global Mac-Mobility
= Disabled,
802.1x EAP Version
= v1,
Multiple Untag SAP
= Enabled
Multiple untagged devices behind a hub or L2-bridge.
Multiple untagged Traffic ingressing on same UNP  access port.
Need to be classified to different services.
UNP Port
BEB
Service
Data1 
Service
Voice1
mac1
mac2
L2 Access Switch
UNP Port
BEB
Service
Data1 
Service
Data2 
mac1
mac2
IP-Phone and PC behind the IP-Phone.
Both traffic (untagged) ingressing on same UNP Access Port.
Need to be classified to different services.

<<<PAGE 272>>>
Assign a static profile for a specified UNP port 
CONFIGURING PERSISTENT UNP SAP PROFILE
Use Case: Silent device
-> unp profile silent map service-type spb tag-value 100 isid 1004 bvlan 4002
-> unp port 5/1/1 profile silent
-> unp profile silent mac-mobility
UNP SPB profile
VLAN Tag: 3
I-SID: 1000
BVLAN ID: 4015
Multicast-mode: Headend
VLAN translation: Disable
No Policy List
ACL
QoS
Silent 
Device
UNP Port 
5/1/1
Persistent UNP SPB Profile
UNP SPB Static Profile Assignment
Create a persistent SAP
Device MAC address ages out
Up to eight SPB service profiles per UNP port

<<<PAGE 273>>>
Required for the VRRP master/slave election process 
Configures the global status of MAC address mobility.
Applied to any new UNP service profiles at creation time.
Only on profiles mapped to SPB services.
-> unp mac-mobility
A persistent SAP does not age out
Ensures an uninterrupted flow of VRRP advertisements between the VRRP master and slave routers.
Applied on loopback port (SAP)
-> unp profile silent map service-type spb tag-value 100 isid 1004 bvlan 4002
-> unp port 1/1/18 profile silent
-> unp profile silent mac-mobility
PERSISTENT UNP SAP PROFILE
Enable MAC address mobility for the SPB service-mapped UNP profile
Use Case: VRRP router communication over a SPB service domain
ISID-1000
VRF 
SPB
Backbone
L3VPN
VRF 
L3VPN
VRRP
OS9900
OS6900
MASTER
SLAVE
ISID-1000
Enable MAC address globally

<<<PAGE 274>>>
CONFIGURING UNP SPB DYNAMIC PROFILE
Calculated SPB BVLAN
Calculated default I-SID number
Incremental reserved service ID number
“System 
Default”
SPB service 
profile
SAP
Classifcation
SAP
already 
exists?
Yes
No
Device
UNP
port
SPB
Dynamic SAP
creation
I-SID exists?
I-SID &
Service id
creation
BVLAN exists?
yes
No
Dynamic
Service?
-> unp {port [chassis_id/]slot/port1[-port2] | linkagg agg_id[-agg_id2]} dynamic-service spb
Enabling Dynamic Profile 
SAP configuration Automation
Dynamic SPB SAP creation
Based on traffic received on UNP port

<<<PAGE 275>>>
UNP SPB DYNAMIC PROFILE CREATION
-> show mac-learning port 2/1/1
Legend: Mac Address: * = address not valid,
Mac Address: & = duplicate static address,
Domain    Vlan/SrvcId[ISId/vnId]     Mac Address
Type          Operation
Interface
------------+----------------------+-------------------+------------------+-------------+-------------------------
SPB           32770:10000412    00:50:56:b8:6b:2d            dynamic
servicing
sap:2/1/1:412
-> show service
32770*      SPB   Up   Up
N    1       0       Dynamic Service isid=10000412 for UNP
-----
-> show spb isis services
Legend: * indicates locally configured ISID
SPB ISIS Services Info:
System
ISID      BVLAN   (Name : BMAC)                           MCAST(T/R)
------------+-------+----------------------------------------+-----------
•
10000412     4015     switch13       : e8:e7:32:40:14:68
Default SPB Service ID number Calculation
Service ID number: 32768 incremented by 1 for each 
additional dynamic service (SPB or VXLAN) 
Multicast Mode: head-end
VLAN translation: enabled
Default I-SID number Calculation
10,000,000 + (Domain ID * 10,000) + (Vlan Tag % 512)
10,000,000 + (0 * 10,000) + (412 % 512) = 10,000,412
Default BVLAN number to use
BVLAN index (Calculated I-SID number %8)
Total number of BVLANs [BVLAN index]
Here 2 BVLANs created -> 4015 and 4016-> 4015
SPB service profile
“System DefaultISID”

<<<PAGE 276>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 277>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: Advanced UNP Service Configuration 
Contents 
1 
Objectives ...................................................................................... 2 
2 
Logical diagram ................................................................................ 2 
3 
Configure Dynamic Services ................................................................. 3 
3.1. Setup UNP ports .................................................................................... 3 
3.2. Display created dynamic services ................................................................ 4 
4 
Configure 802.1x Authentication on UNP ports ........................................... 5 
4.1. Client 7 802.1x authentication configuration .................................................. 5 
4.1.1. Create service 4005 and UNP port ....................................................................... 5 
4.1.2. Create UNP a profile UNP-employee ..................................................................... 5 
4.1.3. Create the RADIUS server VLAN .......................................................................... 6 
4.1.4. Define the Radius Server for device authentication ................................................... 6 
4.2. Setup routing for service 4005 traffic ........................................................... 6 
4.2.1. Checking configuration .................................................................................... 7 
4.2.2. Radius server connectivity ................................................................................ 7 
4.2.3. Test Client7 802.1x authentication ...................................................................... 8 
5 
Configure UNP port and SPB profile for Silent Devices .................................. 9 
5.1. Configure Silent devices ........................................................................... 9 
5.2. Create a new BVLAN and service for Silent Devices .......................................... 10 
5.3. Create a UNP Profile for Silent devices ........................................................ 10 
5.4. Configure routing parameters for silent devices .............................................. 11 
5.5. Configure a UNP service profile as a static profile for the specified UNP port ........... 11 
5.6. Setup Classification rule .......................................................................... 11 
5.7. Checking configuration ........................................................................... 12 
5.8. Monitor UNP user activity ........................................................................ 12

<<<PAGE 278>>>
2 
Lab: Advanced UNP Service Configuration 
 
 1 
Objectives 
This lab is designed to focus on three cases on UNP Service Access Ports:  
- Dynamic Services 
- 802.1x authentication 
- Silent devices  
 2 
Logical diagram

<<<PAGE 279>>>
3 
Lab: Advanced UNP Service Configuration 
 
 3 
Configure Dynamic Services 
To further automate SAP configuration, UNP also supports dynamically creating a “System Default” service 
profile for traffic received on UNP access ports that is not classified into a UNP service profile.  
A System Default profile specifies the attributes used to dynamically create an SPB SAP for the traffic. 
 
Traffic received on UNP access ports that is not assigned to a configured service profile is assigned to the 
System Default service profile.  
A System Default profile is defined to carry traffic for an SPB service or for a VXLAN service based 
on the dynamic service setting for the UNP access port on which the traffic is received. 
The System Default profile attributes used to dynamically create a SAP for such traffic are derived based on 
the setting for this UNP port parameter. 
If the dynamic service port parameter is set to SPB, a SAP is dynamically created for SPB service traffic 
received on the UNP access port, by using the following attributes: 
- A calculated SPB BVLAN,  
- A calculated default I-SID number,  
- An incremental reserved service ID number 
3.1. 
Setup UNP ports 
 
Notes: 
1. By default, base service number 10,000,000 is used for the System Default profile calculation. 
Administrators can modify it. 
-> unp system-default service-base {base_number | default} 
2. By default, modulo number 512 is used for the System Default profile to calculate an SPB 
Service Instance Identifier (I-SID). Administrators can modify.  
-> unp system-default service-mod {mod_number | default} 
3. Administrators can setup the port to not create dynamically a System Default service profile 
based on the traffic received on the UNP access port. 
-> unp {port [chassis_id/]slot/port1[-port2] | dynamic-service none  
Remove previous port configuration 
-> no vlan 7 
-> unp port 1/1/1 port-type access 
-> unp system-default service-base 1000 
-> interfaces 1/1/1 admin-state disable 
-> interfaces 1/1/1 admin-state enable

<<<PAGE 280>>>
4 
Lab: Advanced UNP Service Configuration 
 
Remove previous port configuration 
-> no vlan 8 
-> unp port 1/1/1 port-type access 
-> unp system-default service-base 1000 
-> interfaces 1/1/1 admin-state disable 
-> interfaces 1/1/1 admin-state enable 
3.2. 
Display created dynamic services 
-> show unp user 
                                               User 
Port    Username             Mac address       IP              Vlan Profile                          Type         Status 
-------+--------------------+-----------------+---------------+----+----------------------------+------------+----------- 
1/1/1   00:50:56:90:a4:e0    00:50:56:90:a4:e0 192.168.7.107   4095    systemDefault1000             Access       Active 
 
---Omitted Lines--- 
 
-> show mac-learning port 1/1/1 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
   SPB               32768:1000       00:50:56:90:a4:e0        dynamic       servicing          sap:1/1/1 
 
-> show spb isis services 
                      System 
    ISID      BVLAN   (Name : BMAC)                           MCAST(T/R) 
------------+-------+----------------------------------------+----------- 
*     1000     2000   Pod11sw8            : e8:e7:32:cd:57:f3 
*     1000     2000   Pod11sw7            : e8:e7:32:d4:88:95  
 
---Omitted Lines--- 
 
-> show service spb 
Legend: * denotes a dynamic object 
SPB Service Info 
  SystemId : e8e7.32d4.8895,   SrcId : 0x48895,    SystemName : Pod11sw7 
 
                            SAP     Bind                    MCast 
ServiceId   Adm  Oper Stats Count   Count   Isid      BVlan Mode     (T/R) 
-----------+----+----+-----+-------+-------+---------+-----+-------------- 
---Omitted Lines--- 
 
32768*      Up   Up    N    1       1       1000      2000  Headend  (0/0) 
 
-> show service spb “service_id” 
SPB Service Detailed Info 
  Service Id       : 32768,                Description      : Dynamic Service isid=1000 for UNP, 
  ISID             : 1000,                 BVlan            : 2000, 
  Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0, 
  Admin Status     : Up,                   Oper Status      : Up, 
  Stats Status     : No,                   Vlan Translation : Y, 
  Service Type     : SPB,                  Allocation Type  : Dynamic, 
  MTU              : 9194,                 VPN IP-MTU       : 1500, 
  SAP Count        : 1,                    SDP Bind Count   : 1, 
  RemoveIngressTag : No, 
  Ingress Pkts     : 0,                    Ingress Bytes    : 0, 
  Egress Pkts      : 0,                    Egress Bytes     : 0, 
  Mgmt Change      : 10/03/2021 09:56:55,  Status Change    : 10/03/2021 09:56:55 
 
-> show service spb “service_id” ports 
SPB Service 32768 (Dynamic Service isid=1000 for UNP) 
  Admin : Up,        Oper  : Up,     Stats      : N,         Mtu     : 9194,   VlanXlation : Y, 
  ISID  : 1000,      BVlan : 2000,   MCast-Mode : Headend,   Tx/Rx   : 0/0,    RemoveIngTag: N 
 
                                       Sap Trusted:Priority/         Sap Description / 
Identifier             Adm  Oper Stats Sdp SystemId:BVlan   Intf     Sdp SystemName 
----------------------+----+----+-----+--------------------+--------+-------------------------------- 
sap:1/1/1:0*           Up   Up    N           Y:x           1/1/1    Dynamic SAP for UNP 
sdp:32776:32768*       Up   Up    Y    e8e7.32cd.57f3:2000  1/1/5    Pod11sw8  
 
- Test connectivity between clients 7 and 8 after having set up the IP addresses. 
Client 7: 192.168.7.107 
Client 8: 192.168.7.108 
 
- How is the dynamic Service created/calculated?  
(Tip: Check AOS Network Guide – Section Configuring Access Guardian)

<<<PAGE 281>>>
5 
Lab: Advanced UNP Service Configuration 
 
 4 
Configure 802.1x Authentication on UNP ports 
The following scenario will demonstrate how to enable authentication on UNP access port. 
 
4.1. 
Client 7 802.1x authentication configuration 
- 
For this lab, a RADIUS and DHCP server VM (IP address 192.168.100.102) is running on the virtual 
machine called “AAA Training Server”.  
- 
Client 7 must be authenticated on Switch 7 port 1/1/1 to be associated with a new service 4005 
4.1.1. 
Create service 4005 and UNP port  
First, remove unp port managed in previous section. 
-> no unp port 1/1/1 
-> service 4005 spb isid 4005 bvlan 2002 description Training stats enable vlan-xlation enable 
-> unp port 1/1/1 port-type access 
-> unp port 1/1/1 802.1x-authentication 
-> no unp port 1/1/1 mac-authentication 
-> unp port 1/1/1 ap-mode dynamic-service none  
 
-> service 4005 spb isid 4005 bvlan 2002 description Training stats enable vlan-xlation enable 
4.1.2. 
Create UNP a profile UNP-employee 
-> unp profile UNP-employee 
-> unp profile UNP-employee map service-type static tag-value 0 service-id 4005 
 
An 802.1x supplicant user is authenticated by the Radius Server which send back the UNP as Filter-Id attributes 
(UNP-employee).

<<<PAGE 282>>>
6 
Lab: Advanced UNP Service Configuration 
 
4.1.3. 
Create the RADIUS server VLAN 
-> vlan 100 
-> ip interface AAA address 192.168.100.1/24 vlan 100 
-> vlan 100 members port 1/1/2 untagged 
-> interfaces 1/1/2 admin-state enable 
4.1.4. 
Define the Radius Server for device authentication 
- 
Define radius server as authentication server. 
-> aaa radius-server AAA host 192.168.100.102 key alcatel-lucent 
-> aaa device-authentication 802.1x AAA 
-> aaa accounting 802.1x AAA 
4.2. 
Setup routing for service 4005 traffic 
- Setup new service 4005 on Core switches 
-> service spb 4005 isid 4005 bvlan 2002 description Training vlan-xlation enable admin-state enable 
 
- Configure Vlan and SAP on loopback access port  
-> ip interface L3vpnvlan7 address 192.168.7.1/24 service 4005 
-> service spb 4005 isid 4005 bvlan 2002 description vlan7 admin-state enable 
-> vlan 7  
-> ip interface L3vpnvlan7 address 192.168.7.2/24 vlan 7 
-> vlan 7 members port 1/1/15 tagged 
-> service 4005 sap port 1/1/16:7 stats enable 
-> service 4005 vlan-xlation enable 
-> ip interface L3vpnvlan7 address 192.168.7.8/24 service 4005 
-> service spb 4005 isid 4005 bvlan 2002 description vlan7 admin-state enable 
-> service 4005 vlan-xlation enable 
 
- Define a DHCP Relay for the switch 1 
-> ip dhcp relay admin-state enable 
-> ip dhcp relay destination 192.168.100.102 
- 
When enabled, DHCP packets can be relayed between clients in vlan 7 and the DHCP server in Vlan 100. 
 
- Create a VRRP instance setting up the Switch 1 as the master for VLAN 7. 
-> ip vrrp 7 interface L3vpnvlan7 priority 200 
-> ip vrrp 7 interface L3vpnvlan7 address 192.168.7.254 
-> ip vrrp 7 interface L3vpnvlan7 admin-state enable 
-> ip vrrp 7 interface L3vpnvlan7 priority 100 
-> ip vrrp 7 interface L3vpnvlan7 address 192.168.7.254 
-> ip vrrp 7 interface L3vpnvlan7 admin-state enable

<<<PAGE 283>>>
7 
Lab: Advanced UNP Service Configuration 
 
4.2.1. 
Checking configuration 
-> show service 4005 
-> show service 4005 ports 
-> show unp port 1/1/1 config 
-> show service access port 1/1/1 
 
-> show service 4005 
SPB Service Detailed Info 
  Service Id       : 4005,                 Description      : Training           , 
  ISID             : 4005,                 BVlan            : 4005, 
  Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0, 
  Admin Status     : Up,                   Oper Status      : Up, 
  Stats Status     : Yes,                  Vlan Translation : Y, 
  Service Type     : SPB,                  Allocation Type  : Static, 
  MTU              : 9194,                 VPN IP-MTU       : 1500, 
  SAP Count        : 1,                    SDP Bind Count   : 3, 
  RemoveIngressTag : No,                   Option           : None, 
  Mgmt Change      : 03/31/2021 12:08:02,  Status Change    : 03/31/2021 12:08:02 
 
-> show service 4005 ports 
SPB Service 4005 (UNP-Auth) 
  Admin : Up,        Oper  : Up,     Stats      : Y,         Mtu     : 9194,   VlanXlation : Y, 
  ISID  : 4005,      BVlan : 4005,   MCast-Mode : Headend,   Tx/Rx   : 0/0,    RemoveIngTag: N 
 
                                       Sap Trusted:Priority/         Sap Description / 
Identifier             Adm  Oper Stats Sdp SystemId:BVlan   Intf     Sdp SystemName 
----------------------+----+----+-----+--------------------+--------+-------------------------------- 
sap:1/1/1:0*           Up   Up    N           Y:x           1/1/1    Dynamic SAP for UNP 
sdp:32795:4005*        Up   Up    N    2cfa.a205.cd71:4005  1/1/6    Pod12sw2 
sdp:32796:4005*        Up   Up    N    2cfa.a205.cda9:4005  1/1/5    Pod12sw1 
sdp:32797:4005*        Up   Up    N    e8e7.32fc.23b3:4005  1/1/6    Pod12sw8 
 
-> show service access port 1/1/1 
Port       Link  SAP     SAP     Vlan 
Id        Status Type    Count   Xlation      L2Profile                        Description 
---------+------+-------+-------+-------+---------------------------+------------------------------- 
1/1/1     Up     Dynamic 1         Y     unp-def-access-profile      UNP Dynamic Access Port(1X-Auth) 
4.2.2. 
Radius server connectivity 
- Use the RADIUS test tool to test the RADIUS server reachability from the switch 7. 
-> aaa test-radius-server AAA type authentication user employee password password 
 
Testing Radius Server <192.168.100.102/AAA> 
Access-Challenge from 192.168.100.102 Port 1812 Time: 40 ms 
    Filter-ID = UNP-employee 
Access-Challenge from 192.168.100.102 Port 1812 Time: 79 ms 
    Filter-ID = UNP-employee 
Access-Accept from 192.168.100.102 Port 1812 Time: 106 ms 
Returned Attributes 
    Filter-ID = UNP-employee 
    User Name = employee 
-> show ip dhcp relay interface 
  IP DHCP Relay : 
    DHCP Relay Admin Status         
= Enable, 
    Forward Delay(seconds)          
= 0, 
    Max number of hops              
= 16, 
    Relay Agent Information         
= Disabled, 
    Relay Agent Information Policy  
= Drop, 
    DHCP Relay Opt82 Format 
 
= Base MAC, 
    DHCP Relay Opt82 String   
= 2c:fa:a2:05:cd:a9, 
    PXE support                     
= Disabled, 
    Relay Mode                      
= Global, 
    Bootup Option                   
= Disable, 
    Relay Destination list (Global Mode): 
  ip dhcp relay admin-state enable 
      From Interface Any to Server 192.168.100.102

<<<PAGE 284>>>
8 
Lab: Advanced UNP Service Configuration 
 
-> show ip vrrp 7 
  Virtual Router VRID = 7 on INTERFACE = L3vpnvlan7 
    Version       = V2 
    Admin. Status = Enabled 
    Priority      = 200 
    Preempt       = Yes 
    Adv. Interval = 100 
    Virtual MAC   = 00-00-5E-00-01-07 
    IP Address(es) 
      192.168.7.254 
 
-> show ip vrrp statistics 
4.2.3. 
Test Client7 802.1x authentication 
- Open VM console for client 7 
- Enable IEEE 802.1X authentication in “Local Area Network Properties” 
- Configure IP parameters as DHCP Client 
- Connect with credentials 
o 
Login: employee 
o 
Password: password 
- Note the Client MAC/IP addresses 
 
- At any moment, you can flush the port on the OS6860 to force authentication 
-> unp user flush port 1/1/1 
 
- Check employee user status 
 
-> show unp user 
                                      User 
Port      Username      Mac address            IP (V4/V6)              Vlan          Profile                   Type         Status 
-------+-----------+-----------------+--------------------------------+----+--------------------------------+----------+----------- 
1/1/1    employee    00:50:56:90:ae:a6   192.168.7.20                  4095       UNP-employee                 SPB          Active 
 
-> show unp user “mac_address” 
-> show unp user details 
-> show mac-learning port 1/1/1 
-> show mac-learning domain spb

<<<PAGE 285>>>
9 
Lab: Advanced UNP Service Configuration 
 
 5 
Configure UNP port and SPB profile for Silent Devices 
 
The following scenario will consist in demonstrating how AOS supports Silent Devices on UNP Service Access Port. 
 
It consists in configuring a static SAP on the port that does not age out and receives these broadcast/multicast 
packets coming in on the service even if there are no MACs learned on the service. 
Such Service/SAP associated with the profile will remain persistent on the UNP port until it is explicitly removed 
from the port. 
 
In our case, switch 5 and 6 will be used to simulate the two silent devices (Silent-A and Silent-B) associated with 
service 2007. 
 
 
 
5.1. 
Configure Silent devices 
 
- We will here simulate a silent device by configuring the switch 5 and 6 as follow: 
-> interfaces 1/1/1-12 admin-state disable 
-> vlan 90 
-> vlan 90 members port 1/1/4 tagged 
-> spantree vlan 1 admin-state disable 
-> spantree vlan 90 admin-state disable 
-> ip interface Silent-A address 192.168.90.6/24 vlan 90 
-> interfaces 1/1/4 admin-state enable 
-> interfaces 1/1/1-12 admin-state disable 
-> vlan 90 
-> vlan 90 members port 1/1/4 tagged 
-> spantree vlan 1 admin-state disable 
-> spantree vlan 90 admin-state disable 
-> ip interface Silent-B address 192.168.90.5/24 vlan 90 
-> interfaces 1/1/4 admin-state enable

<<<PAGE 286>>>
10 
Lab: Advanced UNP Service Configuration 
 
5.2. 
Create a new BVLAN and service for Silent Devices 
-> spb bvlan 2007 
-> spb isis bvlan 2007 ect-id 5 
-> service spb 2007 isid 1111 bvlan 2007 description Silent admin-state enable 
-> spb bvlan 2007 
-> spb isis bvlan 2007 ect-id 5 
-> service spb 2007 isid 1111 bvlan 2007 description Silent admin-state enable 
-> spb bvlan 2007 
-> spb isis bvlan 2007 ect-id 5 
-> service spb 2007 isid 1111 bvlan 2007 description Silent admin-state enable 
 
5.3. 
Create a UNP Profile for Silent devices 
 
Static UNP profile  
- This type of profile assignment is particularly useful for silent devices that are connected to a UNP port 
- The profile SAP won’t age out when the device goes idle. 
 
 
 
 
Configure a classification profile that is used to provide role-based access to the switch 
-> unp profile unp-profile-silent 
-> unp profile unp-profile-silent map service-type spb tag-value 90 isid 1111 bvlan 2007 vlan-xlation 
 
 
 
Notes 
This type of profile assignment is particularly useful for silent devices that are connected to a UNP 
port. 
The profile SAP won’t age out when the device goes idle.

<<<PAGE 287>>>
11 
Lab: Advanced UNP Service Configuration 
 
5.4. 
Configure routing parameters for silent devices 
-> ip interface L3vpnvlan90 address 192.168.90.1/24 service 2007 
-> ip vrrp 90 interface L3vpnvlan90 priority 200 
-> ip vrrp 90 interface L3vpnvlan90 address 192.168.90.254 
-> ip vrrp 90 interface L3vpnvlan90 admin-state enable 
-> vlan 90 
-> ip interface L3vpnvlan90 address 192.168.90.2/24 vlan 90 
-> vlan 90 members port 1/1/15 tagged 
-> service 2007 sap port 1/1/16:90 stats enable 
-> ip vrrp 90 interface L3vpnvlan90 priority 100 
-> ip vrrp 90 interface L3vpnvlan90 address 192.168.90.254 
-> ip vrrp 90 interface L3vpnvlan90 admin-state enable 
-> service 2007 vlan-xlation enable 
-> service 2007 vlan-xlation enable 
-> ip static-route 192.168.0.0/16 gateway 192.168.90.254 
 
5.5. 
Configure a UNP service profile as a static profile for the specified UNP port 
 
- 
Create UNP ports and associate the profile to unp ports 
 
-> unp port 1/1/4 port-type access 
-> no unp port 1/1/4 802.1x-authentication 
-> no unp port 1/1/4 mac-authentication 
-> unp port 1/1/4 profile unp-profile-silent 
5.6. 
Setup Classification rule 
 
- Configure a classification profile that is used to provide role-based access to the switch for silent 
devices. 
-> unp classification mac-address “@mac Silent-A” profile1 unp-profile-silent   
-> unp classification mac-address “@mac Silent-B” profile1 unp-profile-silent   
 
 
 
Notes 
Use the “show chassis” command on switch 5 and 6 to get the proper @MAC. 
 
- Reactivate the user ports 
-> interfaces 1/1/4 admin-state disable 
-> interfaces 1/1/4 admin-state enable

<<<PAGE 288>>>
12 
Lab: Advanced UNP Service Configuration 
 
5.7. 
Checking configuration 
 
 
-> show service 2007 
SPB Service Detailed Info 
  Service Id       : 2007,                 Description      : , 
  ISID             : 1111,                 BVlan            : 2007, 
  Multicast-Mode   : Headend,              Tx/Rx Bits       : 0/0, 
  Admin Status     : Up,                   Oper Status      : Up, 
  Stats Status     : No,                   Vlan Translation : yes, 
  Service Type     : SPB,                  Allocation Type  : Static, 
  MTU              : 9194,                 VPN IP-MTU       : 1500, 
  SAP Count        : 1,                    SDP Bind Count   : 1, 
  RemoveIngressTag : No, 
  Ingress Pkts     : 0,                    Ingress Bytes    : 0, 
  Egress Pkts      : 0,                    Egress Bytes     : 0, 
  Mgmt Change      : 10/03/2021 10:16:53,  Status Change    : 10/03/2021 10:16:53 
 
-> show service spb 2007 ports 
Legend: (*) dyn unicast object (+) remote mcast object (#) local mcast object 
SPB Service 2007 Info 
  Admin : Up,        Oper  : Up,     Stats      : N,         Mtu     : 9194,   VlanXlation : N, 
  ISID  : 1111,      BVlan : 2007,   MCast-Mode : Headend,   Tx/Rx   : 0/0,    RemoveIngTag: N 
 
                                       Sap Trusted:Priority/         Sap Description / 
Identifier             Adm  Oper Stats Sdp SystemId:BVlan   Intf     Sdp SystemName 
----------------------+----+----+-----+--------------------+--------+-------------------------------- 
sap:1/1/4:90*          Up   Up    N           Y:x           1/1/4    Dynamic SAP for UNP 
sdp:32797:2007*        Up   Up    Y    e8e7.32cd.57f3:2007  1/1/5    Pod11sw8 
 
Total Ports: 2 
 
-> show unp port 1/1/4 profile 
Port    Profile 
-------+---------------- 
1/1/4   unp-profile-silent 
5.8. 
Monitor UNP user activity 
-> show unp user 
                                               User 
Port    Username             Mac address       IP              Vlan Profile                          Type         
Status 
-------+--------------------+-----------------+---------------+----+-----------------------+------------+----------- 
1/1/1   00:50:56:90:a4:e0    00:50:56:90:a4:e0 192.168.7.107   1    systemDefault1000          Access       Active 
1/1/7   00:50:56:90:f7:ad    00:50:56:90:f7:ad 192.168.30.103  30   Finance                    Access       Active 
1/1/7   2c:fa:a2:aa:35:27    2c:fa:a2:aa:35:27 192.168.30.3    30   Finance                    Access       Active 
 
 
 
 
You should see that no user has been learned on port 1/1/4. 
 
- Initiate a ping test from Silent-A to Silent-B device. 
 
-> show unp user 
1/1/1   00:50:56:90:a4:e0    00:50:56:90:a4:e0 192.168.7.107   1    systemDefault1000            Access       Active 
1/1/4   e8:e7:32:40:d2:e0    e8:e7:32:40:d2:e0 192.168.90.6    90   unp-profile-silent           Access       Active 
1/1/7   00:50:56:90:f7:ad    00:50:56:90:f7:ad 192.168.30.103  30   Finance                      Access       Active 
1/1/7   2c:fa:a2:aa:35:27    2c:fa:a2:aa:35:27 192.168.30.3    30   Finance                      Access       Active 
 
-> show unp user “mac_address” 
Vlan 90: 
  Port                        : 1/1/4, 
  Mac-address                 : e8:e7:32:40:d2:e0, 
  IP                          : 192.168.90.6, 
  UNP-Profile                 : unp-profile-silent, 
  Login Timestamp             : 10/03/2021 10:30:41, 
  Authentication Type         : - , 
  Authentication Status       : - , 
  Classification Source       : Tag MAC Rule UNP, 
  Role Applied                : - ,

<<<PAGE 289>>>
13 
Lab: Advanced UNP Service Configuration 
 
-> show mac-learning port 1/1/4 
Legend: Mac Address: * = address not valid, 
 
        Mac Address: & = duplicate static address, 
 
   Domain    Vlan/SrvcId[ISId/vnId]     Mac Address           Type          Operation          Interface 
------------+----------------------+-------------------+------------------+-------------+------------------------- 
       SPB                2007:1111   e8:e7:32:40:d2:e0            dynamic    servicing              sap:1/1/4:90 
 
- Flush the mac table 
 
-> mac-learning flush dynamic 
 
-> show unp user 
                                               User 
Port    Username             Mac address       IP              Vlan Profile                          Type         
Status 
-------+--------------------+-----------------+---------------+----+-----------------------+------------+----------- 
 
Total users : 0 
 
- Restart a ping between Silent devices. 
 
-> show unp user details port 1/1/4 
Port: 1/1/4 
    MAC-Address: e8:e7:32:40:d2:e0 
      SAP                             = :90, 
      Service ID                      = 2007, 
      VNID                            = 1111 ( 0. 4.87), 
      VPNID                           = 1111 ( 0. 4.87), 
      ISID                            = 1111, 
      Access Timestamp                = 10/03/2021 10:30:41, 
      User Name                       = e8:e7:32:40:d2:e0, 
      IP-Address                      = 192.168.90.6, 
      Vlan                            = 90, 
      Authentication Type             = -, 
      Authentication Status           = -, 
      Authentication Failure Reason   = -, 
      Authentication Retry Count      = 0, 
      Authentication Server IP Used   = -, 
      Authentication Server Used      = -, 
      Server Reply-Message            = -, 
      Profile                         = unp-profile-silent, 
      Profile Source                  = Tag MAC Rule UNP, 
      Profile From Auth Server        = -, 
      Session Timeout                 = -, 
      Classification Profile Rule     = -, 
---Omitted Lines---

<<<PAGE 290>>>
OMNIVISTA 2500 SPB SERVICE PROVISIONING
OMNISWITCH AOS R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 291>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe SPB Service Provisioning through
OmniVista 2500 NMS Software

<<<PAGE 292>>>
SPB – L2 Profile Creation
L2 Profile Configuration
• Set the behavior for processing control 
frame types ingressing on an access port
Service L2 Profiles
• L2 Profiles applied on devices

<<<PAGE 293>>>
SPB – Service configuration
Friendly Name - The IP address of the device on which the Service is configured. 
Service Type - The Service type (SPB).
Tunnel ID - The Tunnel ID used by the Service.
Service ID - unique numerical value that identifies the Service
Name - A user-configured name for the Service. It can also be auto-generated by a dynamically created 
service.
Admin State - administrative state of the Service (Up/Down).
Oper State - operational state of the Service (Up/Down).
BVLAN - The BVLAN associated with the Service.
Mcast Mode - multicast replication mode for the Service (Headend, Tandem). 
VLAN Translation - Whether VLAN Translation is enabled for the Service. (Yes/No). 
Remove Ingress - Whether " Remove Ingress Tag" is enabled for the Service (Yes/No).
Stats - Whether statistics collection is enabled for the device (Yes/No).
Router Interface - The SBP interface.
VPN MTU - Set the VPN MTU. the largest frame size, in octets, that the Service can handle. (Default = 1,500)
NB SAPs - The number of SAPs configured on the device.
NB SDPs - The number of SDPs configured on the device.
Device Information

<<<PAGE 294>>>
SPB - Service Monitoring
Friendly Name - The IP address of the device on which the SAP is configured. 
Service Type - The Service type (SPB).
Tunnel ID - The Tunnel ID used by the Service.
Outer/Inner VLAN - The Inner/Outer VLAN configured for the SAP.
Service ID - Unique numerical value that identifies the Service
Name - user-configured name for the Service. It can also be auto-generated by a dynamically created 
service.
Admin State - Administrative state of the Service (Up/Down).
Oper State - Operational state of the Service (Up/Down).
Description - An optional user description.
SAP Type - The SAP Priority setting (Trusted/Fixed)
Priority - The Priority Value if the SAP Priority Type is "Fixed". 
Stats - Whether ingress and egress statistics collection for packets flowing through the SAP is enabled 
(Yes/No).
SAP Information

<<<PAGE 295>>>
SPB - Service Monitoring
Friendly Name -The IP address of the device on which the SAP is configured. 
Service Type -The Service type (SPB).
Tunnel ID - The Tunnel ID used by the Service.
Interface - Interface on which the SDP is configured.
SDP Type - The SDP type (Dynamic).
Service ID - Unique numerical value  identifying the Service.
SDP ID - Unique numerical value that identifies the Service. Dynamically generated by OmniVista. 
Admin State - The administrative state of the SDP (Up/Down).
Oper State -Operational state of the SDP (Up/Down).
Description - The SDP description, if applicable. 
SDP Name - The SDP name.
SDP Info - Additional SDP information, if applicable.
Stats - Statistics collection for the SDP if enabled (Yes/No). 
TTL - TTL value for the SDP. 
SDP Information

<<<PAGE 296>>>
SPB – Profile Creation
• Home -> Unified Access -> Unified Profile -> Template -> SPB Profile 
SPB Profile Name - The SPB Profile name.
Tag Value - The VLAN tag information from classified traffic used to create the Service Access Point (SAP) for the traffic. If 
the traffic is untagged, the SAP is created with 0 as the encapsulation value (for example, 1/12:0).
ISID - A service instance identifier (ISID) that is used to identify an SPB service in a provider backbone bridge (PBB) 
network. The valid range is 256 - 16777214. 
BVLAN - The VLAN ID number of an existing SPB backbone VLAN (BVLAN). 
VLAN Translation - Enables/Disables egress VLAN translation for the service. 
Multicast Mode - Select the multicast mode from the drop-down menu: 
Headend - Specifies the head-end replication mode for the service. 
Tandem - Specifies the tandem replication mode for the service.

<<<PAGE 297>>>
SPB Service Ports Information

<<<PAGE 298>>>
SPB Services Information
Service Port Information
Service ID - The Service Port ID.
System Name - The system name assigned to the SPB bridge.
IP Address - The IP address of the device on which the port resides.
Service Identifier - The SPB Instance Service Identifier (ISID).
Type - Service Access Point (SAP) or Service Distribution Point (SDP).
Admin Status - The administrative status of the SBP interface (Up/Down). 
Operational Status - The operational status of the SPB interface (Up/Down).
Statistics - Indicates if ingress and egress statistics collection for packets flowing through the service is Enabled or Disabled. 
Trusted - The trust mode for the SAP (Trusted/Untrusted). (Default = Trusted).
Priority - The priority value to set for tagged and untagged packets received on an untrusted SAP. 
0 (lowest priority) to 7 (highest priority).
System ID - The system ID of the SPB bridge. The system ID is the base chassis MAC address of the SPB bridge.
BVLAN - The SPB base VLAN assigned to exchange ISIS-SPB control traffic with other SPB bridges. 
Port - The slot/port or link aggregate ID of the SPB interface. 
SAP Description - An optional description configured for the SAP. By default, the description is blank.

<<<PAGE 299>>>
SPB – SERVICE PROFILE
• Service profile parameters can be mapped to an Access Role Profile. 
• An SPB SAP is automatically created using the specified profile parameters
• A device is dynamically assigned to the profile through authentication or classification 
• Traffic from the device is then forwarded on the SAP.

<<<PAGE 300>>>
SPB PROFILE - ACCESS ROLE MAPPING

<<<PAGE 301>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 302>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch R8 
Lab: SPB with OV2500 
Contents 
1 
Objectives ...................................................................................... 2 
2 
SPB In-band Management over Services .................................................... 3 
2.1. Setup IP Interfaces on Control BVLAN ........................................................... 3 
2.2. Test In-Band management interface ............................................................. 3 
3 
Discovering devices with OmniVista 2500.................................................. 4 
3.1. OmniVista 2500 Preparation ...................................................................... 4 
3.1.1. OmniVista 2500 Virtual Machine initialization .......................................................... 4 
3.1.2. Enable OV2500 Access from desktop. .................................................................... 5 
3.1.3. Generating & Installing an Evaluation License ......................................................... 7 
3.1.4. Generating the Evaluation License ....................................................................... 7 
3.1.5. Installing the Evaluation License ......................................................................... 8 
3.2. Setting up SNMP parameters on AOS switches.................................................. 8 
3.3. OmniVista 2500 Network Discovery .............................................................. 9

<<<PAGE 303>>>
2 
Lab: SPB with OV2500 
 
 1 
Objectives 
This lab is designed to Discover devices with OmniVista 2500

<<<PAGE 304>>>
3 
Lab: SPB with OV2500 
 
 2 
SPB In-band Management over Services 
 
OmniSwitch support management IP access to the BEBs as well as BCBs. 
To support, an IP interface will be configured on (only) the Control BVLAN. 
IP routing information in this IP BVLAN domain is advertised by the ISIS-SPB protocol.  
 
 
Dynamic Routing protocol (including VRRP) are supported on control BVLAN. 
Static or dynamic routing is required to route packets to destinations outside of the IP 
BVLAN subnet when necessary. 
 
- We will now allow the management of the SPB switches from the OmniVista 2500 NMS through the BVLAN 
2000. 
 
2.1. 
Setup IP Interfaces on Control BVLAN 
 
- Configure IP interfaces on BVLAN 2000 for all the switch supporting SPB. (Switch 1, 2, 7, 8) 
-> ip interface "spb-mgmt" address 172.30.1.x/24 vlan 2000   
(where x is the switch id) 
2.2. 
Test In-Band management interface 
o 
Check the connectivity OmniVista and Switch 1, 2, 7 and 8 
-> ping 172.30.1.X source-interface AAA 
-> ping 192.168.100.107 (OV) 
 
 
Notes: OmniVista 2500 can now discover and manage all the switches.  
OV 2500 is located at @IP 192.168.100.107 and connected to Switch 1 port 1/1/2.

<<<PAGE 305>>>
4 
Lab: SPB with OV2500 
 
 3 
Discovering devices with OmniVista 2500 
3.1. 
OmniVista 2500 Preparation 
3.1.1. 
OmniVista 2500 Virtual Machine initialization 
 
Open the vSphere client and Log into vCenter. Make sure that Use Windows session credentials is 
checked. 
- Click on Login button to login into Vcenter 
 
 
 
 
 
 
 
 
 
Turn on the Virtual Machine called “Pod#-OV2500.4xx” 
- Right-click on it and select Snapshot -> Snapshot Manager 
 
 
 
 
In the Snapshot Manager Window Select “OV-init” and click on Go to. 
- Click Yes to confirm it  
 
 
 
Check the progress in the Status Bar.  
- Once completed, right-click on the VM “Pod#-OV2500.4xx” and select Power -> Power On 
 
 
Notes:  
OV2500 is preconfigured (network configuration, default SNMPv2 parameters but without OV 
licenses.

<<<PAGE 306>>>
5 
Lab: SPB with OV2500 
 
3.1.2. 
Enable OV2500 Access from desktop. 
 
OmniVista 2500 runs on the LAN network of the POD with the IP 192.168.100.107.  
The web interface can be reached from a Web browser within the remote desktop. 
 
 
 
 
On Switch 1, we need to setup a static route to give access to OV from RDP desktop. 
-> ip static-route 0.0.0.0/0 gateway 192.168.100.108 metric 2 
 
 
Open a web browser and enter the following URL 
o 
https://10.4.pod#.208:8443 
 
Use the following credentials to log into OmniVista: 
o 
Username: admin 
o 
Password: switch  
 
 
Warning:  
Depending on the type of web browser being used, a warning regarding the website’s security certificate will 
be shown. Skip this warning and continue to the OmniVista login page. 
 
 
 
- 
A message indicating that the default password must be changed appears. Click on the Please change 
your password link

<<<PAGE 307>>>
6 
Lab: SPB with OV2500 
 
- 
Set the new password to Training123=! and confirm it. Click on Save 
 
 
 
- 
Click on the Continue to Login Page link and login using the new password. 
 
 
 
 
 
- 
A message box appears to add the license(s) 
 
 
Go to the next section to generate and apply an evaluation license

<<<PAGE 308>>>
7 
Lab: SPB with OV2500 
 
3.1.3. 
Generating & Installing an Evaluation License 
 
An Evaluation License provides full OmniVista 2500 NMS feature functionality, but is valid only 
for 90 Days (starting from the date the license is generated). There is one file that contains all of 
the Device (AOS, Third-Party, Stellar APs) and Service Licenses (VM, Guest, BYOD).  
 
In this section, you will generate and install an evaluation license. 
 
 
 
Warning 
Before this step, ensure that no license generated in a previous training is available to avoid any possible 
confusion. On this Windows desktop, delete any files with the name “-EVAL-OV2500…” 
 
3.1.4. 
Generating the Evaluation License 
 
From the Windows Desktop, open a new web browser tab/window: 
 
> Copy & Paste the following URL in your RDP session: https://lds.al-enterprise.com/  
 > Select OmniVista 2500 NMS 
  > Enter:  
   > Customer ID: 99999 
    > Order Number: evaluation 
     > Leave the Customer Email field blank 
      > Click on Submit 
 
 
       > Select the License Type: EVAL-OV2500-ALL-TYPE_1 
        > Enter the Passcode: omnivista 
         > Click on Submit Entry 
 
 
 
          > Enter Company Name: ALE (or something else) 
           > Click on Generate License 
            > Save the file locally 
 
 
         “The sole purpose of entering your mail is to receive the license information by mail.” 
 
 
Tips > Evaluation License 
This license is NOT dedicated for training. Don’t hesitate to use the same process if you need to generate an 
evaluation license for testing purpose (lab…).

<<<PAGE 309>>>
8 
Lab: SPB with OV2500 
 
3.1.5. 
Installing the Evaluation License 
 
- Inserting directly the license file obtained in the previous part  
 
> Go back to the OV 2500 Web Admin Interface 
  > Click on Add License 
 
     
 
   > License File: click on Browse 
    > Select the license file downloaded in the previous part 
 
 
     > Click on Open 
      > Click on Submit 
 
       Software and/or documentation End-User License Agreement “EULA” 
 
       > Check OK (don’t check Enable ProActive Lifecycle Management) 
 
 
 
Tips > Inserting the License Keys 
Another alternative consists in the following 2 steps:  
1. 
Go to ADMINISTRATION > LICENSE > Add or Import License 
2. 
Open the file with a text editor, then copy & paste the license keys in the License Key field. 
 
3.2. 
Setting up SNMP parameters on AOS switches 
 
Enter the following CLI commands to set up SNMP Access.  
 
 
Notes: The username string cannot be “admin”, “diag”, or “user”. A unique username must be used.  
In this case we are creating a user named snmpuser to access SNMP. This will be set up through a CLI Session 
on AOS Devices. 
 
 
Set up SNMP access to authenticate with the local database on the switch. 
-> aaa authentication snmp local 
 
Create a user with read-write privileges for SNMPv2 queries. 
-> user snmpuser password "Superuser=1" read-write all no auth 
 
 
Define the security level to accept SNMPv1, v2 and v3 requests. 
-> snmp security no-security 
 
Configure a community string public and maps it to the user account name snmpuser. 
-> snmp community-map public user snmpuser enable 
 
Enable a community string to be mapped to a user account in the local database. 
-> snmp community-map mode enable 
 
Define a SNMP station to which the switch will transmit traps (specify IPv4 or IPv6 address). 
-> snmp station 192.168.100.107 snmpuser v2 enable 
 
Optionally, activate trap absorption. 
-> snmp-trap absorption enable

<<<PAGE 310>>>
9 
Lab: SPB with OV2500 
 
3.3. 
OmniVista 2500 Network Discovery 
 
 -> Go to Top-level menu bar 
 -> Network -> Managed Devices -> Discover New Devices 
 
 
 
-> Create a new Range List  ->  + button  
Note: We will use IP range list “172.30.1.1 to 172.30.1.8 (Control BVLAN IP address range) 
 
o 
 Enter the following parameters: 
Start IP: 172.30.1.1 
End IP:   172.30.1.8 
Subnet Mask: 255.255.255.0 
 
-> Select the Default profile from Choose Discovery Profiles and click on “+” to move it to the right 
-> Click Create 
-> Select the ranges from the list and select Discover Now. 
The discovery process starts, and you should notice the progress.  
-> Select Finish when the discovery is completed. 
 
 
You should see the discovered devices in the Managed Devices window.  
 
 
 
You can also find additional information about the status of the switch, its IP address, the type of switch 
and the firmware version in used.

<<<PAGE 311>>>
10 
Lab: SPB with OV2500 
 
-> Go to Top-level menu bar 
 -> Network -> Topology -> Map Level Action -> SPB Network  
-> And then -> Poll Latest Data  
 
 
-> Then click on “Multiple Selection” icon on the top right corner 
 
 
> 
Select 172.30.1.7 and select a Bvlan 2001 and then Bvlan 2002

<<<PAGE 312>>>
IMPLEMENTING SPB ADVANCED FEATURES
OMNISWITCH AOS R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 313>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Implement SPB advanced features
-
Hybrid SAP and Bridge Port
-  SPB E-Tree Services

<<<PAGE 314>>>
SPB - HYBRID ACCESS PORTS

<<<PAGE 315>>>
SHORTEST PATH BRIDGING - HYBRID ACCESS PORTS
•
Hybrid SAP and Bridge Port Hybrid access port feature allows a single port to function 
both as an access port and a bridging port
• Hybrid configured port 
•
a bridge port with a default VLAN and tagged VLAN for bridging 
•
a SAPs for services with mapped tagged VLANs.

<<<PAGE 316>>>
HYBRID SAP AND BRIDGE PORT - CONFIGURING
•
The following CLI commands are associated with this feature: 
•
Example :
•
To enable hybrid mode on the access port, use the service access command with the hybrid option with 
enable keyword. 
•
To disable hybrid mode on the access port, use the service access command with the hybrid option with 
disable keyword. 
-> service access {port chassis/slot/port[-port2] | linkagg agg_id[-agg_id2]} hybrid {enable | disable}] [description port_description] 
-> service access port 1/1/3-10 hybrid enable
-> service access port 1/1/6 hybrid disable

<<<PAGE 317>>>
SPB E-TREE SERVICES

<<<PAGE 318>>>
SPB E-TREE SERVICES - OVERVIEW
•
L2 Customer to Customer Isolation Over SPB (PVLAN on SAP)
•
Provide rooted multipoint connectivity (P2MP) between UNIs (SAPs) of an SPBm service
•
SAPs are designated as either leaf SAP or Root SAP
•
A leaf SAP cannot communicate with another Leaf SAP in the service spanning multiple BEBs 
whereas Leaf SAP to Root SAP traffic is allowed. Root SAPs can communicate to all Leaf SAPs and 
Root SAPs.
•
This is in contrast with the E-LAN services which provide any to any connectivity (MP2MP).
Note : Conventional SAPs are called Root SAPs
Note : As of 8.9.R03, all SAPs created for E-Tree 
service are only of type Leaf

<<<PAGE 319>>>
SPB E-TREE SERVICES - OVERVIEW
•
SPB E-Tree Services E-TREE services provide rooted multipoint connectivity (P2MP) 
between UNIs (SAPs) of an SPBm service. 
•
With this implementation, the traffic ingressing on the SAPs of a BEB (say BEB-1) of a service created with ETREE option is 
sent out with MAC-in-MAC (MIM) encapsulation on network port to the remote BEB. 
•
On BEB-3, a service with same ISID value is created 
as an E-LAN service (without E-TREE option)
Note : By default, an SPB service is an E-LAN service

<<<PAGE 320>>>
SPB E-TREE SERVICES - CONFIGURING
• E-Tree feature on an SPB service can be configured by enabling ‘e-tree’ option while 
creating the service. 
• Configuring E-Tree enables point-to-multipoint services, that is, allows traffic to flow only 
between Leaf to Root SAPs.
• For example:
• service service_id[-service_id2] spb isid instance_id[-instance_id2] bvlan bvlan_id[:x] [e-tree {enable | disable}
-> service 100 spb isid 1000 bvlan 4001 e-tree enable

<<<PAGE 321>>>
SPB E-TREE SERVICES - CONFIGURING
•
E-Tree feature on UNP created services can be configured by enabling ‘e-tree’ option on 
the UNP profile while creating the profile
• Configuring E-Tree enables point-to-multipoint services, that is, allow flow between Leaf 
to Root SAPs.
• For example:
unp profile profile_name map service-type spb tag-value {0 | ALL | outer_qtag:all | qtag | outer_qtag:inner_qtag} isid instance_id bvlan bvlan_id [e-tree]
-> unp profile vNP1 map service-type spb tag-value 10 isid 1500 bvlan 500 e-tree

<<<PAGE 322>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 323>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniSwitch AOS R8 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
Contents 
1 
Hybrid Access Ports ........................................................................... 2 
2 
Prequisites ..................................................................................... 3 
3 
Bridge ports from 6360-A to 6360-B with a default VLAN ............................... 3 
3.1. Manage the switches as following. ............................................................... 3 
3.2. Checking the configuration ....................................................................... 3 
3.3. Testing end device connectivity .................................................................. 4 
4 
Configure a SPB network for extending L2 connectivity ................................. 4 
4.1. Creating the Backbone VLANs .................................................................... 4 
4.2. Defining the Control BVLAN ....................................................................... 4 
4.3. Configuring ISIS on network ports ................................................................ 4 
4.4. Activating ISIS protocol ............................................................................ 5 
4.5. Understanding SPB-M protocol operations ...................................................... 5 
4.6. Creating VLANs on access switches .............................................................. 6 
4.7. Creating SPB service ............................................................................... 6 
4.8. Configuring SPB access port ....................................................................... 6 
4.9. Setting up the SAP services ....................................................................... 7 
4.10. Analysis and understanding the concept of SPB services ..................................... 7 
4.10.1. 
Checking the configuration ........................................................................... 7 
4.10.2. 
Testing end device connectivity ...................................................................... 7 
5 
L2 Customer to Customer Isolation Over SPB ............................................. 8 
5.1. Topology for the test .............................................................................. 8 
5.2. Initialize switches. ................................................................................. 9 
5.3. Configuration ........................................................................................ 9 
5.4. Analysis and understanding the concept of SPB services .................................... 10 
5.4.1. Checking the configuration ............................................................................. 10 
5.4.2. Testing end device connectivity ........................................................................ 10

<<<PAGE 324>>>
2 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
 1 
Hybrid Access Ports 
 
This lab is designed to familiarize you with configuration Hybrid Access Ports. 
Hybrid access port feature allows a single port to function both as an access port and a bridging port. 
 
From AOS 8.9.R03 release, a single port can function both as an access port and a bridging port by enabling 
Hybrid mode on an access port. 
 
Hybrid configured port can be understood as a bridge port with a default VLAN and tagged VLAN for bridging 
and the user can configure SAPs for services with mapped tagged VLANs. 
 
Below is an example topology depicting traffic treatment on a hybrid configured port. When different 
domains (SAP/VLAN/Default-VLAN) traffic from customer network is received on the hybrid configured port at 
BEB from aggregator switch, the traffic gets classified to their respective domain. SAP VLAN tagged traffic is 
processed in service domain and regular VLAN tagged/untagged (default) packet gets processed in VLAN 
domain. 
 
You will configure a scenario for extending Layer 2 connections across a SPB-M service backbone network for 
Customer VLAN 2 (SAP VLAN tagged traffic is processed in service domain ) and VLAN 3 regular VLAN 
tagged/untagged (default) packet gets processed in VLAN domain.

<<<PAGE 325>>>
3 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
 2 
Prequisites 
Initialize the switches for the test 
-> cp labinit/vcboot.cfg working 
-> cp labinit/vcboot.cfg certified 
-> cp labinit/vcsetup.cfg working 
-> cp labinit/vcsetup.cfg certified 
-> cp labinit/pre_banner.txt switch 
-> reload from working no rollback-timeout 
-> Y 
 3 
Bridge ports from 6360-A to 6360-B with a default VLAN  
3.1. 
Manage the switches as following. 
-> vlan 3 
-> vlan 3 members port 1/1/23 untagged 
-> vlan 3 members port 1/1/3 untagged 
-> interfaces 1/1/3 admin-state enable 
-> interfaces 1/1/23 admin-state enable 
-> vlan 3 
-> vlan 3 members port 1/1/23 untagged 
-> vlan 3 members port 1/1/3 untagged 
-> interfaces 1/1/3 admin-state enable 
-> interfaces 1/1/23 admin-state enable 
-> vlan 3 
-> vlan 3 members port 1/1/3 untagged 
-> vlan 3 members port 1/1/2 untagged 
-> ip interface int_3 address 192.168.3.5/24 vlan 3 
-> interfaces 1/1/2-3 admin-state enable 
-> vlan 3 
-> vlan 3 members port 1/1/3 untagged 
-> vlan 3 members port 1/1/2 untagged 
-> ip interface int_3 address 192.168.3.6/24 vlan 3 
-> interfaces 1/1/2-3 admin-state enable 
 
3.2. 
Checking the configuration 
 
- Test scenario 
o 
Open the clients 9 and 10 (shortcut 
 on access POD desktop) 
o 
Use following VMs 
▪ 
PodXClient9 on OS6360-A port 1/1/2 
▪ 
PodXClient10 on OS6360-B port 1/1/2 
o 
Right-click on it then select Open console. 
o 
For each of the VM client 
▪ 
Note the @MAC  
▪ 
Assign an IP address

<<<PAGE 326>>>
4 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient9 
Switch 5 
1/1/2 
3 
192.168.3.105 
192.168.3.5 
PodXClient10 
Switch 6 
1/1/2 
3 
192.168.3.106 
192.168.3.6 
 
3.3. 
Testing end device connectivity 
 
- From Virtual machines connected on the access switch, run some connectivity (ping) test between client 9 
and Client 10. 
 4 
Configure a SPB network for extending L2 connectivity 
4.1. 
Creating the Backbone VLANs 
 
- On both node, create two backbone VLANs (BVLAN) 
-> spb bvlan 2001 
-> spb isis bvlan 2001 ect-id 1 
-> spb bvlan 2002 
 
-> spb isis bvlan 2002 ect-id 2 
 
 
Notes 
BVLAN configuration and ECT algorithm must be the same on each SPB bridge to ensure proper ISIS-SPB 
neighbor discovery and shortest path calculations throughout the backbone SPB network.  
When creating multiple BVLANs for each node, it is best practice to use different ECT algorithm for each BVLAN 
to maximize the traffic distribution.  
4.2. 
Defining the Control BVLAN 
 
- On each switch, configure the control BVLAN for management  
-> spb isis admin-state disable  
-> spb isis control-bvlan 2001 
 
 
Notes 
Control BVLAN carries the ISIS PDUs which are single tagged with the chosen BVLAN ID. 
Control BVLAN can only be changed when protocol is disabled.  
Spanning Tree is automatically disabled for any BVLAN created. 
 
4.3. 
Configuring ISIS on network ports 
 
Setup the ISIS protocol on appropriate network ports on every switch participating in SPB core network, 
accordingly to the physical connection between each node: 
 
 
Notes 
On system startup, ISIS is automatically loaded on the system without the need to enable the 
protocol like we do with OSPF and other protocols.

<<<PAGE 327>>>
5 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
-> spb isis interface port 1/1/23 
-> spb isis interface port 1/1/23 
 
 
 
 
 
Notes 
The ISIS interface can be a fixed port or a logical port (linkagg). When you configure the port as an ISIS SPB 
interface, it becomes the SPB network port, and the system will automatically add all BVLANs configured to the 
port. 
 
4.4. 
Activating ISIS protocol  
 
On every SPB nodes, enable globally IS-IS SPB protocol: 
-> spb isis admin-state enable 
 
 
Notes 
Enabling ISIS-SPB on a switch starts the process of ISIS-SPB discovery, adjacency building, and shortest path 
tree calculations. Make sure that the SPBM configuration is set up first, then enable ISIS-SPB on each switch 
that will participate in the SPBM network. 
 
4.5. 
Understanding SPB-M protocol operations 
 
 
Notes 
Refer to the CLI reference and Network Configuration Guides for detailed information about 
outputs. 
 
- Check the BVLANs and the associated ECT algorithm on each of the system.  
-> show spb isis bvlans 
-> show vlan id 
 
- Display the list of all the SPB interfaces configured for the system and their states.  
-> show spb isis interface

<<<PAGE 328>>>
6 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
- Displays the information about the SPB adjacencies on the system. 
Determine if ISIS SPB is in “UP” state then check the ISIS SPB neighbors on each of the equipment. 
-> show spb isis adjacency 
-> show spb isis adjacency detail 
 
- Verify the unicast addresses learned on each SPB switch in the ISIS-SPB backbone topology as well the 
outbound interface used when sending unicast traffic to other nodes. 
-> show spb isis unicast-table bvlan 2001 
-> show spb isis unicast-table bvlan 2002 
4.6. 
Creating VLANs on access switches 
- We will create VLAN 2 on access switches OS6360 distributed over SPB backbone network. 
- These VLAN will be tagged over uplinks towards the backbone. 
- Proceed as follow: 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> ip interface vlan2 address 192.168.2.5/24 vlan 2 
-> vlan 2 members port 1/1/3 tagged  
-> interfaces 1/1/1 admin-state enable 
-> vlan 2 
-> vlan 2 members port 1/1/1 untagged 
-> ip interface vlan2 address 192.168.2.6/24 vlan 2 
-> vlan 2 members port 1/1/3 tagged  
-> interfaces 1/1/1 admin-state enable 
 
4.7. 
Creating SPB service 
 
-> service spb 2002 isid 2002 bvlan 2002 description vlan2 admin-state enable 
 
 
 
Notes 
• 
ISID and BVLAN must be defined on all SPB network for network consistency. 
• 
Each SPB service is capable of learning customer MAC addresses from the access side (SAPs) 
and from the network side (Mesh SDP) and then switching the traffic based on this 
information. 
• 
Each ISID can be attached to one BVLAN only. 
4.8. 
Configuring SPB access port 
 
- On each BEB nodes (OS6870-A and OS6860-B), configure the service access port(s) accordingly to the lab 
diagram.  The service access port(s) is the entry point of the LAN Access switch. (OS6360-A et OS6360-B 
vlan 2) 
-> service access port 1/1/3 hybrid enable  
-> service access port 1/1/3 hybrid enable

<<<PAGE 329>>>
7 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
4.9. 
Setting up the SAP services 
-> service spb 2002 sap port 1/1/3:2 admin-state enable stats enable 
 
-> service spb 2002 sap port 1/1/3:2 admin-state enable stats enable 
4.10. Analysis and understanding the concept of SPB services 
4.10.1. Checking the configuration 
 
- Display the information of the services configured  
 
-> show spb isis services 
-> show service 
-> show service access 
-> show service spb 
-> show service sdp spb 
-> show service spb id ports  
-> show service mesh-sdp 
-> show service spb id counters 
-> show service spb id debug-info 
-> show mac-learning 
 
 
Notes 
Refer to the CLI reference and Network Configuration Guides for detailed information about outputs. 
4.10.2. Testing end device connectivity 
 
- From Virtual machines connected on the access switch, run some connectivity test between machines 
sharing the same SPB service (members of same Vlan). 
- In addition to the ping requests and use of tracert application, use the following commands on BEB 
systems to verify the @MAC classified as well as the associated SAP. 
- Test scenario 
o 
Open the clients (shortcut 
 on access POD desktop) 
o 
Use following VMs 
▪ 
PodXClient5 on OS6360-A port 1/1/1 
▪ 
PodXClient6 on OS6360-B port 1/1/1 
 
o 
Right-click on it then select Open console 
o 
For each of the VM client 
▪ 
Note the @MAC  
▪ 
Assign an IP address  
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient5 
Switch 5 
1/1/1 
2 
192.168.2.105 
192.168.2.5 
PodXClient6 
Switch 6 
1/1/1 
2 
192.168.2.106 
192.168.2.6

<<<PAGE 330>>>
8 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
 5 
L2 Customer to Customer Isolation Over SPB  
 
E-TREE services will provide rooted multipoint connectivity (P2MP) between UNIs (SAPs) of an SPBm service. 
  
In an E-TREE service, SAPs are designated as either Leaf SAP or Root SAP. Conventional SAPs are called Root 
SAPs. 
 
A leaf SAP cannot communicate with another Leaf SAP in the service spanning multiple BEBs whereas Leaf SAP to 
Root SAP traffic is allowed. Root SAPs can communicate to all Leaf SAPs and Root SAPs.  
 
 
 
This is in contrast with the E-LAN services which provide any to any connectivity (MP2MP). 
5.1. 
Topology for the test 
Following is the sample configuration for the topology shown below, with Service Manager configuration.

<<<PAGE 331>>>
9 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
5.2. 
Initialize switches. 
-> cp labinit/vcboot.cfg working 
-> cp labinit/vcboot.cfg certified 
-> cp labinit/vcsetup.cfg working 
-> cp labinit/vcsetup.cfg certified 
-> cp labinit/pre_banner.txt switch 
-> reload from working no rollback-timeout 
-> Y 
5.3. 
Configuration 
BEB1 -> sw1 (6900-A)  
-> spb bvlan 2001 admin-state enable  
-> spb bvlan 2004 admin-state enable 
-> spb isis bvlan 2001 ect-id 1 
-> spb isis bvlan 2004 ect-id 4 
-> spb isis control-bvlan 2001 
-> spb isis interface port 1/1/5-6 
-> spb isis admin-state enable 
-> interface port 1/1/5-6 admin-state enable 
-> service access port 1/1/3 
-> service 2004 spb isid 2004 bvlan 2004 description vlan4 e-tree enable 
-> service 2004 sap port 1/1/3:4 stats enable 
-> interface port 1/1/3 admin-state enable                          
 
BEB2 -> sw8 (6860-B)  
-> spb bvlan 2001 admin-state enable  
-> spb bvlan 2004 admin-state enable 
-> spb isis bvlan 2001 ect-id 1 
-> spb isis bvlan 2004 ect-id 4 
-> spb isis control-bvlan 2001 
-> spb isis interface port 1/1/6 
-> interface port 1/1/6 admin-state enable 
-> spb isis admin-state enable 
-> service access port 1/1/3 
-> service 2004 spb isid 2004 bvlan 2004 description vlan4 e-tree enable 
-> service 2004 sap port 1/1/3:4 stats enable 
-> interface port 1/1/3 admin-state enable 
 
BEB3 -> sw7 (6870-A)  
-> spb bvlan 2001 admin-state enable  
-> spb bvlan 2004 admin-state enable 
-> spb isis bvlan 2001 ect-id 1 
-> spb isis bvlan 2004 ect-id 4 
-> spb isis control-bvlan 2001 
-> spb isis interface port 1/1/5 
-> interface port 1/1/5 admin-state enable 
-> spb isis admin-state enable 
-> service access port 1/1/3 
-> service 2004 spb isid 2004 bvlan 2004 description vlan4 admin-state enable 
-> service 2004 sap port 1/1/3:4 stats enable 
-> interface port 1/1/3 admin-state enable 
 
sw5 (6360-A) 
-> vlan 4 admin-state enable 
-> vlan 4 members port 1/1/1 untagged 
-> vlan 4 members port 1/1/3 tagged 
-> ip interface "vlan4" address 192.168.4.5 mask 255.255.255.0 vlan 4 
-> interfaces 1/1/1 admin-state enable 
-> interfaces 1/1/3 admin-state enable 
 
sw6 (6360-B) 
-> vlan 4 admin-state enable 
-> vlan 4 members port 1/1/1 untagged 
-> vlan 4 members port 1/1/3 tagged 
-> ip interface "vlan4" address 192.168.4.6 mask 255.255.255.0 vlan 4

<<<PAGE 332>>>
10 
Lab: Deploying a Hybrid Access Ports and L2 Customer to Customer Isolation Over SPB 
 
-> interfaces 1/1/1 admin-state enable 
-> interfaces 1/1/3 admin-state enable 
 
sw3 (6560-A)  
-> vlan 4 admin-state enable 
-> vlan 4 members port 1/1/1 untagged 
-> vlan 4 members port 1/1/3 tagged 
-> ip interface "vlan4" address 192.168.4.3 mask 255.255.255.0 vlan 4 
-> interfaces 1/1/1 admin-state enable 
-> interfaces 1/1/3 admin-state enable 
5.4. 
Analysis and understanding the concept of SPB services 
5.4.1. 
Checking the configuration 
 
- Display the information of the services configured  
 
-> show spb isis services 
-> show service 
-> show service access 
-> show service spb 
-> show service sdp spb 
-> show service spb id ports  
-> show mac-learning 
 
5.4.2. 
Testing end device connectivity 
 
- From Virtual machines connected on the access switch, run some connectivity test between machines 
sharing the same SPB service (members of same Vlan). 
- In addition to the ping requests and use of tracert application, use the following commands on BEB 
systems to verify the @MAC classified as well as the associated SAP. 
- Test scenario 
o 
Open the clients (shortcut 
 on access POD desktop) 
o 
Use following VMs 
▪ 
PodXClient5 on OS6360-A port 1/1/1 
▪ 
PodXClient6 on OS6360-B port 1/1/1 
▪ 
PodXClient3 on OS6560-A port 1/1/1 
 
o 
Right-click on it then select Open console 
o 
For each of the VM client 
▪ 
Note the @MAC  
▪ 
Assign an IP address  
 
Client 
Switch 
Port 
VLAN 
IP Address 
Default GW 
PodXClient5 
Switch 5 
1/1/1 
4 
192.168.4.105 
192.168.4.5 
PodXClient6 
Switch 6 
1/1/1 
4 
192.168.4.106 
192.168.4.6 
PodXClient3 
Switch 3 
1/1/1 
4 
192.168.4.103 
192.168.4.3

<<<PAGE 333>>>
SUCCESS STORIES
SHORTEST PATH BRIDGING
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 334>>>
LINKÖPING UNIVERSITY

<<<PAGE 335>>>
LINKÖPING 
UNIVERSITY
Spine & leaf topology after 
successful SPB 
implementation
“Our new campus network is incredibly simple to 
configure and manage. We can now fully meet 
user expectations and provide them with 
additional services. With ALE, we have a partner 
who helps us succeed.”
David Byers, Head of IT office, Linköping 
University
Read the full success story here :
https://www.al-enterprise.com/en/company/customers/linkoping-
university?utm_medium=social&utm_campaign=dysi&utm_source=None

<<<PAGE 336>>>
NEVADA DEPARTMENT OF TRANSPORTATION
(NDOT)

<<<PAGE 337>>>
ROADSIDE NETWORKS NEED TO EVOLVE AND BECOME 
“ENTERPRISE-CLASS”
• Better management tools to facilitate 
troubleshooting, decrease MTTR
• Analytics to better understand usage trends
• Open, standards-based protocols like shortest-
path bridging…
• … allows for the elimination of spanning tree, 
increasing reliability

<<<PAGE 338>>>
NDOT “ENTERPRISE CLASS” 
NETWORK ARCHITECTURE
Network Operations Center
OmniVista 2500 
Network Management
Distribution/Fiber Hut
Fiber ring
OS6900
OS6860E
OS6865
OS6865
OS6865
OS6865
NEMA-TS2 Enclosures
SPB to the edge
Fully Managed from NOC
Temperature Controlled
•
Aggregation of rings
•
Redundant ring connections
•
Support for PoE
Managed switches provide high degree of visibility
Spanning tree eliminated in favor of SPB
High flexibility: stacking switches, ample PoE budgets
OS6900
OS6900
OS6900
OS6900
Temperature Controlled
•
Server Connections
•
Fiber Hut Aggregation
•
Core Mesh Topology
Core/Data Center
Edge/Hardened Switches
OS6900

<<<PAGE 339>>>
METZ EUROMETROPOLIS

<<<PAGE 340>>>
CONTEXT
• Large French city
• Shared IT service between the metropolis and 
the town hall.
• Network :
• Serves nearly 80 public administrative buildings.
• The network is made up of 100km of fibre optic 
cable belonging to the metropolitan authority.
• Thousands of items of equipment pass through the 
network: PCs and mobiles on the WLAN network, 
servers, boiler room automats, swimming pool 
turnstiles, intruder alarms, etc.
• 200 switches, 100 APs, ALE supervision and 
analytics.

<<<PAGE 341>>>
INITIAL NETWORK
• Large broadcast domain
• 10 000 connected devices spanning on layer 2
• Routing needs to be moved to datacenter
A pair of centralized routers configured in 
VRRP handles all network routing
A vlan strategy per site is used, a 
local vlan has an ip interface and is 
configured on the access ports
1
2
3
1
1
1
3
1
All vlans are present on the uplinks between 
the site and the routers (transit vlan)
Spanning Tree is used to 
control level 2 loops induced 
by redundant topology.
VRRP

<<<PAGE 342>>>
NETWORK AFTER SPB IMPLEMENTATION
• Replace STP, no loop, all links used
• Low latency and fast convergence
• Multi-site, multi-tenant
1
2
3
1
1
1
3
1
SPB
No more transit VLANs: SPB 
will map on the basis of the 
service deployed
Loops without SPBs are controlled by unique and 
independent STP instances
BEBs adjoining two loops are 
configured with two STP 
instances in Root Bridge and 
Next Best Root.
A point-to-point SPB service 
is dedicated to transporting 
STP control.
All the switches on the core network are SPB-
compatible; there are no longer any Layer 2 loops 
on this part of the network
SPB uses an SPF algorithm to find the best path between two nodes. 
Several BVLANs will be included to allow several active paths to be 
maintained.

<<<PAGE 343>>>
KEY HIGHLIGHTS
• No service disruption during the transition
• Extended Level 2 transparent for existing L2 
services
• All links are used
• Replacement of Spanning Tree protocols
• Use of the shortest paths
• IS-IS: automatic traffic protection and 
redirection
• Configuration of SPB access services at the edge 
only.
• Integration of existing standards
OPTIMISING BANDWIDTH AND STABILITY
LATENCY AND RESILIENCE
SIMPLIFIED CONFIGURATION
AND MONITORING
SIMPLE, LOW-IMPACT TRANSITION

<<<PAGE 344>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 345>>>
ROUTING CONCEPTS IN RELATION TO SPB WITH 
PREVIOUS SWITCHES HARDWARE
OMNISWITCH R8
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 346>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Describe Routing Concept
-
-

<<<PAGE 347>>>
ROUTING CONCEPT

<<<PAGE 348>>>
AOS SUPPORT
•
•
Outline Routing using external loopback cable
•
Inline Routing using bandwidth from front-panel ports
OS6900-X20
OS6900-X72
OS6900-T20
OS6900-Q32
OS6860/E
OS6860N
OS6900-X48C6
OS6900-X48C4E
OS6900-T48C6 
OS6900-C32E 
OS9900
OS6900-V72
OS6900-C32
Service 1
VRF
L3 VPN Access Port (SPB SAP side)
L3 VPN Router Port (VRF side)
Use of two physical loopback ports.
One side of as an access port for SPB.
Other side is a bridged port 
configured for routing only
linkagg port or a physical port .
Multiple ports can be shared among 
different VRFs.
Dedicated Front panel 
port interface
Dedicated Static Link Aggregate
No physical loopback cable required.
Single port or link aggregate in use.
Multiple front-panel loopback ports can 
be combined into a LAG for redundancy 
and to increase bandwidth.
VPN interface defined through specific 
front panel port(s).
Bandwidth processing is taken from the 
front panel port.
No physical loopback cable required.
No dedicated front-panel ports
L3 VPN interface defined through the configuration 
of an IP interface bound to an SPB service
VRF
Service 1
VRF

<<<PAGE 349>>>
SPBM
SPB OUTLINE ROUTING
OS6900-X20/40
OS6900-T20/40
OS6900-Q32
OS6900-X72

<<<PAGE 350>>>
LOOPBACK PORTS
•
AOS supported mechanisms
•
L3/IP-VPN routing over SPB
•
IP-VPN Lite over SPB
•
In both mechanisms, use of loopback
•
One side of as an access port for SPB
•
Other side is a bridged port configured for routing only
•
linkagg port or a physical port 
•
Multiple ports can be shared among different VRFs
Loopback ports

<<<PAGE 351>>>
ISID 1
SPB
Backbone
L3 VPN Access Port (SPB SAP side)
L3 VPN Router Port (VRF side)
LOOPBACK PORTS
•
Between the two loopback ports, the 
mapping of VRF to I-SID are coordinated by 
VLAN IDs
•
Each router side use different VLANs
Customer
Network A
Loopback ports

<<<PAGE 352>>>
-> vlan vlan_id
-> vlan vlan_id members port chassis/slot/port tagged
-> vlan vlan_id members linkagg linkagg_id tagged
-> vrf vrf_name ip interface if_name address ip_address vlan vlan_id
-> vrf vrf_name ipv6 interface if_name vlan vlan_id
-> service service_id spb isid instance_id bvlan bvlan_id
-> service access port chassis/slot/port
-> service access linkagg agg_id
-> service spb service_id sap port chassis/slot/port:vlan_id
-> service spb service_id sap linkagg agg_id:vlan_id
CONFIGURATION STEPS
Create a Service SPB instance
Create a SAP on the loopback port 
Configure the L3VPN VRF interface on Router port side 
Configure an IP interface for the L3VPN VLAN
Configure IP-VPN LITE or L3-VPN
Define the SPB access port side
ISID 1000
BVLAN 4001
Loopback 
ports
SPB
Backbone
Customer
Network A
VLAN 500
10.5.1.1/24
VRF
Loopback ports

<<<PAGE 353>>>
-> vlan 500
-> vlan 500 members port 1/1/11 tagged
-> vrf default ip interface l3vpn1 address 10.5.1.1/24 vlan 500
-> spb bvlan 4001
-> service spb 10 spb isid 1000 bvlan 4001 admin-state enable
-> service access port 1/1/12
-> service spb 10 sap port 1/1/12:500
Create a Service SPB instance
Create a SAP on the loopback port 
Configure the L3VPN VRF interface on Router port side 
Configure an IP interface for the L3VPN VLAN
Configure IP-VPN LITE or L3-VPN
Define the SPB access port side
CONFIGURATION EXAMPLE
ISID 1000
BVLAN 4001
Loopback 
ports
SPB
Backbone
1/1/11
1/1/12
Customer
Network A
VLAN 500
10.5.1.1/24
VRF default
Loopback ports

<<<PAGE 354>>>
LOOPBACK PORTS CONFIGURATION
SPB
Backbone
ISID-1000
ISID-1000
VRF 1
192.168.3.0/24
192.168.4.0/24
VRF 1
192.168.1.0/24
192.168.2.0/24
L3vpn2
L3vpn1
L3 VPN Access Port 1/1/24
L3 VPN Router Port 1/1/23
L3 VPN Access Port 1/1/12
L3 VPN Router Port 1/1/11
vlan 500
vlan 500 members 1/1/23 tagged
spb bvlan 4001
service access port 1/1/24
service spb 10 isid 1000 bvlan 4001 admin-state enable
service spb 10 sap port 1/1/24:500
vrf create 1
vrf 1 ip interface L3vpn1 vlan 500 address 10.5.1.2/24
vlan 500
vlan 500 members 1/1/11 tagged
spb bvlan 4001
service access port 1/1/12
service spb 10 isid 1000 bvlan 4001 admin-state enable
service spb 10 sap port 1/1/12:500
vrf create 1
vrf 1 ip interface L3vpn1 vlan 500 address 10.5.1.1/24
•
Configure the L3 VPN loopback ports for VPN-Lite or L3 VPN mechanisms
“The loopback configuration consists of one port tagged with an IP interface VLAN that belongs to a single VRF instance connected to another port that 
is assigned to an SPB SAP, to which the VLAN ID associated with the other loopback port is assigned.”
Loopback Ports
Loopback ports

<<<PAGE 355>>>
SPB INLINE ROUTING FROM FRONT-PANEL PORTS
OS6900-V72
OS6900-C32
SPB

<<<PAGE 356>>>
INLINE ROUTING FROM FRONT-PANEL PORTS
•
No physical loopback cable required.
•
Single ports or link aggregates in use
•
L3 VPN interface defined through the configuration of specific front panel port(s)
•
Bandwidth processing is taken from the front panel port.
•
Multiple front-panel loopback ports can be combined into a static loopback link aggregate
•
Redundancy
•
Increased bandwidth
•
Prerequisites
•
Reserved VLAN
•
Front panel or link aggregate configured to run in loopback mode. 
A single port provides the loopback function, which conserves the number of ports needed.
Same port is assigned to the L3 VPN VLAN and is also configured as a service access port.
Front panel port interface

<<<PAGE 357>>>
CONFIGURATION STEPS
-> interfaces port chassis/slot/port[-port2] loopback 
-> linkagg static agg agg_id size size
-> linkagg static agg agg_id loopback
-> linkagg static port {chassis/slot/port[-port2] agg agg_id}
-> service access port {chassis/slot/port | linkagg agg_id} vlan-xlation enable
-> service service_id spb isid instance_id bvlan bvlan_id vlan-xlation enable
-> service service_id sap {port chassis/slot/port| linkagg agg_id}:vlan_id
-> ip interface if_name address ip_address/mask vlan vlan_id rtr-port {port chassis/slot/port | linkagg agg_id} tagged
Configure a port to operate in the loopback mode
OR
Loopback Mode
Create a Service SPB instance
Configure the Loopback port/linkagg as Service Access Port/linkagg
Create a SAP on loopback port 
Configure a link aggregate to operate in the loopback mode
Configure an IP interface for the L3VPN VLAN
Configure IP-VPN LITE or L3-VPN (Next Module)

<<<PAGE 358>>>
CONFIGURATION EXAMPLE
-> interfaces port 1/1/18 loopback
-> service access port 1/1/18 vlan-xlation enable
-> service 10 spb isid 1000 bvlan 500 vlan-xlation enable
-> service 10 sap port 1/1/18:200
-> ip interface L3VPN address 10.10.10.1/24 rtr-port port 1/1/18 tagged vlan 200
-> ipv6 interface L3VPN rtr-port port 1/1/18 tagged vlan 200
-> ipv6 address 2001:db8:10::1/64 L3VPN
Create the Service SPB 10
Configure the Loopback port as Service Access Port
Create a SAP on loopback port 
Configure port 1/1/18 to operate in the loopback mode
Configure an IP interface for the L3VPN VLAN 200
Front panel port interface 1/1/18
Loopback Mode

<<<PAGE 359>>>
CONFIGURATION GUIDELINES -INLINE ROUTING FROM FRONT-
PANEL PORTS
•
The same port is assigned to the L3 VPN VLAN and is also configured as a service access port.
•
A dedicated VLAN and a port or link aggregate configured to operate in the loopback mode are 
required.
•
Once a port or link aggregate is configured to run in the loopback mode, no other functionality is 
supported on the port or link aggregate.
•
The dedicated VLAN is reserved for the L3 VPN and can only be associated with the loopback port or 
link aggregate
•
To ensure this, configure the L3 VPN IP interface using the router port and VLAN options, where the router port is 
the loopback port and the VLAN is the dedicated VLAN.
•
Multiple front panel loopback ports can be combined into a static loopback link aggregate for 
redundancy and to increase bandwidth.
•
When configuring the loopback port or link aggregate as an access port and creating an SPB service, 
enable VLAN translation.
•
Once the loopback mode is enabled for a link aggregate, the link aggregate is dedicated to providing 
loopback functionality for an SPB L3 VPN inline routing configuration. The loopback mode is disabled 
only when the link aggregate is deleted.

<<<PAGE 360>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 361>>>
CLASSROOM SESSION 
OR VIRTUAL CLASS SESSION
END OF TRAINING EVALUATIONS
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 362>>>
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

<<<PAGE 363>>>
LOGIN TO ALE KNOWLEDGE HUB
• Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual 
credentials

<<<PAGE 364>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (1/2)
• Click on My Training on the home page
• Search for the training course by the reference provided by your instructor

<<<PAGE 365>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (2/2)
• From the session, select Evaluate in the dropdown menu and follow the instructions
• OR
• From the curriculum, select Open Curriculum
• Then select Evaluate in the dropdown menu associated to the session and follow 
the instructions

<<<PAGE 366>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 367>>>
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