
<<<PAGE 283>>>
O M N I S W I T C H  P O S I T I O N I N G  A N D  D E P L O Y M E N T
CAMPUS LAN NETWORK 
SOLUTION
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.
<<<PAGE 284>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
•
Deployment Architecture and Scenarios
•
Hierarchical Layering design approach
•
OmniSwitch Model Selection
•
OmniSwitch model positioning
•
Features and Model Design Approach
<<<PAGE 285>>>
DEPLOYMENT ARCHITECTURE
AND SCENARIOS
<<<PAGE 286>>>
BUILDING A COMPLETE NETWORK SOLUTION
• Residential Ethernet
• Business Services
• Citynets
Metro
Ethernet
Enterprise
LAN Campus
SMB / Branch
Server access & DC Core
Transportation
Utilities, Energy
Defense
Verticals
Data Center
<<<PAGE 287>>>
NETWORK DESIGN
PROCESS GOALS AND CONSIDERATIONS 
• Scalability 
• Adaptability 
• Reliability
• Cost / ROI
• Predictability 
• Ease of Implementation  
• Manageability
• Business / Application Growth
• Troubleshooting
<<<PAGE 288>>>
LAN OMNISWITCH
HIERARCHICAL LAYERING DESIGN APPROACH
Shared
Ring
Star
Tree
Spine & Leaf
POD
Mesh
Access
Core
Aggregation
Access
Core
Network Topology
Network Architecture
2-tier
3-tier
<<<PAGE 289>>>
NETWORK ARCHITECTURE
THREE-TIER MODEL
• Scalable Segmentation 
• Flexible, low cost, Medium Density  
• Separate devices provide L2 & L3 Switching
• Reliability
• Redundancy
• Fault Tolerance
• Manageability
• Efficiency
• Adaptability
• Low-latency (>12µs)
Aggregation
Access
Core
100M->1G->2.5G->5G->10G
10G->25G->40G->100G
10G->25G->40G->100G
1G->10G->25G
<<<PAGE 290>>>
OS6860N
OS6870
Aggregation
Access
Core
OS2X60
LAN OMNISWITCH
THREE-TIER MODEL
OS9900
OS6900
OS9900
OS6900
OS6360
OS6465
• High Speeds traffic
• n x 10G/25G/40G/100G
• Redundancy
• High Reliability
• Virtual-Chassis 
• Shortest Path Bridging (SPB)
• MPLS, VXLAN EVPN
• ERP
• Very Fast Convergence 
• High Resiliency
• Scalability
• L2 support (SPT / LACP)
• IPv4 / IPv6 routing protocol  (UNI & MCAST)
• Extensive QoS / ACLs support
• Virtual-Chassis
• High Speeds traffic
• n x 10G/25G/40G
• Shortest Path Bridging (SPB)
• MPLS, VXLAN EVPN
• Dual-Home Link Aggregation Active/Active
• Policy-based connectivity 
• L3 and L2 Integration
• Fast Convergence
• Routing Protocols (OSPF, PIM....)
• Resiliency
• L2 support (STP / LACP)
• IPv4 / IPv6 routing protocol (unicast & mcast)
• Extensive QoS / ACLs support
• MACsec
• AppMon
• Connection points to end devices (100M to 10G)
• Workgroup / user  access to the network 
• Virtual Chassis
• Dual-Home Link Aggregation Active/Active
• Bandwidth control
• Basic QOS features
• User Mobility
• Alcatel Quarantine Manager 
• Access Guardian
• 802.1x/MAC
• Universal Network Profiles
• Captive Portal Auth
• Application Fingerprinting
• POE, POE+, POE++
• MACsec
OS6560
OS6570M
OS6860N
OS6870
OS6575
<<<PAGE 291>>>
Access
Core
NETWORK ARCHITECTURE
TWO-TIER MODEL
• High-throughput
• High Density
• Lowest-Latency
• High Performance
• Non-blocking design
• Dense deployment
• Lower oversubscription 
• Switch & link optimization
• Both layers provide L2 & L3 Switching
• Faultless with low and predictable latency
• 1.5 to 6µs
• Access and distribution layers merging 
• Data Center – Servers with built-in switches
• Enterprise – Fewer management points, less STP
100M->1G->2.5G->5G->10G
10G->25G->40G->100G
10G->25G->40G->50G->100G
<<<PAGE 292>>>
OS6860N
Access
Core
LAN OMNISWITCH
TWO-TIER MODEL
OS6870
OS6900
OS9900
• High Speeds traffic
• 10G/25G/40G/50G/100G
• Virtual-Chassis
• Shortest Path Bridging (SPB)
• MPLS + VXLAN EVPN 
• ERP
• Dual-Home Link Aggregation Active/Active
• High Redundancy
• High Reliability
• Very Fast Convergence 
• High Resiliency
• Scalability
• L2 support (SPT / LACP)
• IPv4 / IPv6 routing protocol (UNI & MCAST)
• Extensive QoS / ACLs support
• MACsec
• AppMon
• Connection points to end devices (10M to 10G)
• Workgroup / user  access to the network 
• Stacking / Virtual Chassis
• Dual-Home Link Aggregation Active/Active
• Bandwidth control
• Basic QOS features
• User Mobility
• Private VLAN
• Alcatel Quarantine Manager certified
• Access Guardian
• 802.1x/MAC
• Universal Network Profiles,
• Captive Portal Auth
• PostureCheck
• MACsec
• POE, POE+, POE++
OS2X60
OS6360
OS6465
OS6560
OS6570M
OS6860N
OS6575
OS6870
<<<PAGE 293>>>
HIERARCHICAL LAYERING
DESIGN APPROACH
<<<PAGE 294>>>
LAN OMNISWITCH
DESIGN APPROACH
Edge / Access Switching
Small Aggregation/Core Switching
1/10/40 GigE
uplinks
10M/100M/1G/2.5G/5G/10G
Switching
10M/100M/1G/2.5G/5G/10G
Switching
Core Layer
L2/L3
10M/100M/1G/2.5G/5G/10G
Switching
Access Layer 2/3
Switching
Core Layer
(L3 
Switching)
10/25/40/
100G
10/25/40/
100 GigE
uplinks
Access Layer
L2/L3
<<<PAGE 295>>>
LAN OMNISWITCH
DESIGN APPROACH
Core L2/L3 10/25/40/100 GigE
Ring links
Core L2/L3 10/25/40/100 GigE
Mesh links
10M/100M/1G/2.5G/5G/10G
Access Layer 2/3
Switching
10M/100M/1G/2.5G/5G/10G
Access Layer 2/3
Switching
10M/100M/1G/2.5G/5G/10G
Access Layer 2/3
Switching
Access Layer
L2/L3
Access Layer
L2/L3
Access Layer
L2/L3
10M/100M/1G/2.5G/5G/10G
Access Layer 2/3
Switching
10M/100M/1G/2.5G/5G/10G
Access Layer 2/3
Switching
10M/100M/1G/2.5G/5G/10G
Access Layer 2/3
Switching
Access Layer
L2/L3
Access Layer
L2/L3
Access Layer
L2/L3
<<<PAGE 296>>>
LAN OMNISWITCH
DESIGN APPROACH
• DHCP Option 82 configurable / DHCP Snooping
• IP Anti-Spoofing based on DHCP snooping 
• Dynamic ARP Inspection
• Multicast TV VLAN
• Ethernet services support
• IEEE 802.1ad Provider Bridges
• IEEE 802.1aq Shortest Path Bridging (SPB-M))
• Multipoint Ethernet VPN (EVPN) over I-SID service 
virtualization or Q-in-Q tunnels 
• Service Access Point (SAP) profile identification
• Service VLAN (SVLAN) and Customer VLAN (CVLAN) 
support
• VLAN translation and mapping including CVLAN to 
SVLAN
• C-tag to S-tag priority mapping 
• ETHOAM (802.1ag) Connectivity layer
• Service Assurance Agent (SAA)
• Port Mapping (Private VLANs) 
OmniSwitch 6860N
Ring of 
OmniSwitches
Ethernet Access
Business Managed Services
Aggregation
IP/MPLS
Core
IP/MPLS
10 Gig
Ring
1 Gig Fiber
OmniSwitch 6465-P28
Dual Homed
fiber
10 Gig
Ring
OmniSwitch 6465-P28
OmniSwitch 6560/E
Ethernet Access
Residential Triple-Play
Services
Service Router
OS6560
10  Gig Fiber
Metro Ethernet Network Switching
Customer A
Customer B
Customer C
Metro Access Ring
Service 
Provider 
Network
<<<PAGE 297>>>
LAN OMNISWITCH
DESIGN APPROACH
Data Center Network 
1/10 GigE
Layer 2
Switching
10/40/100 
GigE
uplinks
Mesh POD
10/40/100 GigE
Layer 2/3
Switching
OS6900
OS6900
OS6900
OS6900
OS6900
OS6900
POD
10/40
GigE
Server
Hosting
VMs
Server
Hosting
VMs
Server
Hosting
VMs
Server
Hosting
VMs
<<<PAGE 298>>>
OMNISWITCH MODEL DESIGN APPROACH
<<<PAGE 299>>>
OMNISWITCH MODEL SELECTION
<<<PAGE 300>>>
OMNISWITCH SELECTION
NETWORK LAYER BASED
Model
Layer
OS6360
OS6465
OS6560/E OS6570M
OS6575
OS6860N
OS6870
OS6900
OS9900
User Access
Yes
Yes
Yes
Yes
Yes
Yes
Yes
No
Yes
Distribution
No
No
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Core
No
No
No
No
No
Yes
Yes
Yes
Yes
Data Center
No
No
No
No
No
Yes
Yes
Yes
Yes
Switch model utilization per infrastructure layer
<<<PAGE 301>>>
OMNISWITCH SELECTION FOR CAMPUS DESIGN
Model
OS2260
OS2360-
24/48
OS6360-
10
OS6360-
24/48
OS6465
OS6560/E
OS6570M
OS6860N
OS6870
OS6900
OS9900
Availability
Virtual Chassis
No
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
ISSU 
No
No
Yes
Yes
No
No
Yes
Yes
Yes
Yes
Yes
Hot swap power supply
No
No
No
Yes
Yes
No
Yes
Yes
Yes
Yes
Yes
Layer 2 switching
Shortest Path Bridging (SPB)
No
No
No
No
No
Yes **
Yes **
Yes
Yes
Yes
Yes
DHL Active-Active
Yes
Yes
Yes
Yes
Yes
Yes
No
Yes
Yes
No
No
ERPv2
No
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Layer 3 switching
Basic Layer 3, IPv4/IPv6
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Advanced Layer 3 IPv4/IPv6
No
No
No
No
No
Yes **
Yes **
Yes
Yes
Yes
Yes
VRF IPv4/IPv6
No
No
No
No
No
No
Yes **
Yes
Yes
Yes
Yes
Multicast routing IPv4/IPv6
No
No
No
No
No
Yes **
Yes **
Yes
Yes
Yes
Yes
User network Profile
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Fanless
Yes
Yes
Yes
No
Yes (except 
P28)
No
No
No
No
No
No
Metro Ethernet
No
No
No
No
Yes
Yes **
Yes
Yes
Yes
Yes
Yes
MPLS
No
No
No
No
No
No
No
Yes **
Yes **
Yes **
No
Remote VC
No
No
Yes
Yes
No
Yes
Yes
Yes
Yes
Yes
Yes
*  Roadmap
** License based feature
<<<PAGE 302>>>
OMNISWITCH 6360, 6465, 6560/E, 6570M, 6860N, 6870 
COMPARISON
OS6360
OS6465
OS6560/E
OS6570M
OS6860N
OS6870
Software
AOS 8
AOS 8
AOS 8
AOS 8
AOS 8
AOS 8
Features
AOS L2 & Basic L3
Stackable
AOS L2 & Basic L3
Stackable
AOS L2 & Basic L3
Stackable
AOS L2 & Basic L3
Stackable
AOS L2 & Adv. L3
Virtual Chassis, SPB-M, 
MPLS, VXLAN
AOS L2 & Adv. L3
Virtual Chassis, SPB-M, 
MPLS, VXLAN
Routing
Basic static and 
RIP/RIPng
Basic static and 
RIP/RIPng
Full, advanced IP 
Routing with license
Full, advanced IP 
Routing with license
Full, advanced IP Routing
Full, advanced IP Routing
User ports
10M/100M/1G/10G
802.3at support 
10M/100M/1G
802.3at support 
10M/100M/1G/2.5G/
5G
802.3at/bt
95W POE (1 port)
10M/100M/1G
100M/1G/2.5G/5G/10G
802.3bt support 
100M/1G/2.5G/5G/10G
Full 802.3bt support
Uplinks
1/10 Gbps
1/10 Gbps
1/10 Gbps
1/10/25 Gbps
1/10/25/40/100 Gbps
1/10/25/40/50/100 Gbps
Stacking
5/10 Gbps links
5/10 Gbps links
10/20 Gbps links
10 Gbps links
100 Gbps links
100/200 Gbps links
Switching
208 Mpps
131 Mpps
241 Mpps
210 Mpps
758.9 Mpps
1,488 Mpps
Fabric 
Capacity
140 Gb/s
176 Gb/s
324 Gb/s
60 / 168 Gb/s
1,020 Gb/s
2,000 Gb/s
Traffic 
Analysis
Network Analytics
Network Analytics
Network Analytics
Network Analytics
Network Analytics,    
Application Monitoring
Network Analytics,    
Application Monitoring, 
Streaming Telemetry
Advanced 
Security
AG, UNP, CP, BYOD
AG, UNP, CP, BYOD
AG, UNP, CP, BYOD
AG, UNP, CP, BYOD
AG, UNP, CP, BYOD
MACsec
AG, UNP, CP, BYOD
MACsec
Management
OmniVista Cirrus/Terra
OmniVista Cirrus/Terra
OmniVista Cirrus/Terra
OmniVista Cirrus/Terra
OmniVista Cirrus/Terra
OmniVista Cirrus/Terra
Mac Table
16K
16K
16K
32K
64K
128K
Routing Table
64 routes
32 routes
2K routing table
16K routing table
144K
312K
Multicast
IGMP / Switching
IGMP / Switching
IGMP / Switching
IGMP / Switching
Full IP Multicast routing
Full IP Multicast routing
<<<PAGE 303>>>
VIRTUAL CHASSIS VS PHYSICAL CHASSIS
Virtual Chassis (6x6900)
Chassis (9907/9912)
Initial Investment
Lower – Pay as you grow
Higher for Chassis itself, high capacity power 
supply, and blade space
latency
Usually slightly higher (multiple hops)
Usually slightly lower (1 hop)
Reboot time (switch or blade)
Higher (control & data plane)
Lower (only data plane)
Rack space
Lower (6U)
Higher (11U/17U)
Management
Distributed
Centralized
POE
None with OS6900
75 & 30 W per port on P module
Cost
Lower
Significantly Higher
1G
432
288/480
10G
432
256/480
40G/100G
162 (with C32E, 27 ports x 6 switches)
108/208
Redundancy
Mgmt, PS
Mgmt Module, Fabric, PS, Fans
IP Routes IPv4/IPv6 
12K-32K (SM) / 144K-384K (varies on model)
128K
L2 MACs
16K / 32K / 64K / 228K (depends on model)
128K
ACLS
4K
1K
<<<PAGE 304>>>
OMNISWITCH MODELS POSITIONING
<<<PAGE 305>>>
OMNISWITCH 6360/6560
SMALL BUSINESS SOLUTION
• SMB solution
• Short installation and set-up time with zero-touch 
configuration saves time/cost
• Fully integrated and lab tested, single vendor, plug and play 
solution (IP Network + Wi-Fi + Voice + Mobility)
• Gigabit access for next generation Wi-Fi (WiFi 5/6/7)
• Up to 4 x 10 Gig uplinks for high-speed aggregation and 
Internet access
• Security with Basic Unified Access support
• MAC authentication
• 802.1x authentication
• AAA 
• User policies (uNP) such as VPNs and QoS
• UNP for NAC security and QoS
• Secure BYOD services (6560)
• PoE+ support for voice, data and video surveillance
OmniAccess
Instant Access 
Points (IAP)
Internet
OmniSwitch
6360-P10
6360-P24
6360-P48
MyIC & 8-Series phones
OpenTouch & OmniPCX
Office Clients
Wi-Fi Access
OmniPCX 
Office 
(RCE)
PTZ 
Camera
PSTN
OS6360/6560
<<<PAGE 306>>>
OMNISWITCH 6360
SMALL BUSINESS SOLUTION
• “Configure Voice, Data and Wi-Fi in under
20 minutes”
• OXO Purple boot-up process  and OMC access
• Once boot-up, starting automatically 
download the configuration files
from the OmniPCX 
• Network built
• IP Phones operational
• For the first AP to initialize once connected
to the OmniSwitch 6360
OS6360 positioning
• Support for 20-100 SMB users
• Up to 10Gbs uplink speeds
• Cost-effective, enterprise quality switch
• Zero-touch provisioning
OmniAccess
Stellar Access 
Points
Internet
ALE 300/400/500 phones
OXO Purple Clients
Wi-Fi Access
OmniPCX 
Office 
(OXO Purple)
PTZ Camera
PSTN
6360
<<<PAGE 307>>>
OMNISWITCH 6360/6465/6560/6570M/6860N/6870
LAN CAMPUS NETWORK
L3 Core/Aggregation
Small enterprise Access/Core “virtual chassis”
Core
Edge
OS6560/E
OS6860N
OS6360
OS6465
1 or 10 GigE
Uplinks
Edge
OS6560/E
OS6360
OS6900 / OS6870 / OS9900
OS6560/E
Aggregation
1 or 10
Gigabit
Uplinks
Core
OS6860N          OS6870
10/40 
GigE
Backbone
Virtual 
Chassis
DHL
10/100M
1G/2.5G
5G/10G
PoE
PoE+
HPoE
2-tier networks
3-tier networks
<<<PAGE 308>>>
OS6560/E
AT THE EDGE OF MGIG CONVERGED IP NETWORK
AP15xx
OS6560/E
2 x 2:2 
MU-MIMO
4 x 4:4 
MU-MIMO
CAT5e / CAT6 cable
10G Optical Uplink
WiFi 6/6E/7 AP’s
95W HPoE
AP132x
AP12xx
AP13xx
AP14xx
2 x 10G SFP+ 
OS6560E-P24Z8
OS6560-P24Z24/E-P48Z16
4 x 10G SFP+
<<<PAGE 309>>>
OS6860N
AT THE EDGE OF MGIG CONVERGED IP NETWORK 
• Key Elements
•
Virtual Chassis for simplified architecture
•
Fully redundant and resilient network
•
VC ports operate at 20/40/100GigE
•
Remote Stacking up to 100m
•
Up to 8 switches in a VC
•
95W of PoE
•
All user ports on OS6860N-P24M
•
12 m-gig user ports on OS6860N-P24Z
•
POE+ on others
•
100M/1G/2.5G/5G/10G GigE application
•
Modular uplinks supporting 
10G/25G/40G/100GigE uplinks
• WiFi 7 Access Point ready 
•
Multi gig support
•
95W PoE (802.3bt)
•
Fast re-convergence time on 
failure
•
UNP for NAC security and QoS
•
MACsec
•
SPB, VXLAN, MPLS
•
Secure BYOD services
•
Energy Efficient Ethernet (EEE)
•
Application Monitoring (AppMon)
CAT6 / CAT7 cable
10G Optical Uplink
WiFi 6 / 7 AP’s
8 x OS6860N
units
Up to 384 Gig ports
Up to 192 Multi Gig 
ports 
Core
OS6900
IEEE 802.11ax
WiFi 6 AP’s
IEEE 802.11be
WiFi 7 AP’s
4 x 25G SFP+
LACP
<<<PAGE 310>>>
OS6860N
AT THE EDGE OF MGIG CONVERGED IP NETWORK
4 x 10/25G SFP28
OS6860N-P24Z
OS6860N-P48Z
OS6860N-P24M
OS6860N-P48M
4 x 4:4 
MU-MIMO
4 x 4:4 
MU-MIMO
CAT5e / CAT6 cable
25G Optical Uplink
WiFi 6/7 AP’s
95W PoE
<<<PAGE 311>>>
OMNISWITCH 9900
TWO TIER/ THREE TIER DESIGN
In the Core of 
the Network
At the Access 
layer
OS9900
OS9900
OS6360
OS6560/E
OS6860N
OS6870
OS9900
Two Tier, single Building
10 GigE 
Link Aggregation
10 GigE
Dual Attachment L2/L3 
Dual Home link 
Active-Active
In the Core of 
the Network
At the 
Aggregation 
layer
At the Access 
layer
OS9900
OS9900
OS9900
OS6360
OS6560/E
OS6860N
OS6870
Three  Tier, Multi-Building
10/40 GigE Link Aggregation
10GigE  Link Aggregation or DHL
OS6860N
OS6870
OS6860N
OS6870
Dual core network for 
maximum redundancy
<<<PAGE 312>>>
In the Core of 
the Network
At the Access 
layer
Two Tier, single Building
In the Core of 
the Network
At the 
Aggregation 
layer
At the Access 
layer
Three  Tier, Multi-Building
OMNISWITCH 6900
TWO TIER/ THREE TIER DESIGN
OS6900
OS6900
OS6900
SPB-M 
Core
SPB-M
BEB
OS9900
OS6900
OS6900
Dual core network for 
maximum redundancy
OS6360
OS6465
OS6560/E
OS6860N
OS6870
10/25 GigE 
Link Aggregation
10 GigE
Dual Attachment L2/L3 
Dual Home link 
DHL Active-Active
OS6900
10/25/40/100 GigE 
10GigE 
1/10/25/40 GigE
10/25/40/100 GigE
OS6360
OS6465
OS6560/E
OS6860N
OS6870
<<<PAGE 313>>>
FEATURES AND MODELS
DESIGN APPROACH
<<<PAGE 314>>>
OMNISWITCH
COMPACT CORE NETWORK
• Key Elements
• Network virtualized using Virtual Chassis (VC) for 
simplified two-layer architecture 
• Fully redundant and resilient network 
• Fast re-convergence time on failure
• UNP for NAC security and QoS
• Deep Packet Inspection (DPI)
• Application Monitoring (AppMon)
• Server farm or data center dual home connected 
directly to network core with LAG
• High speed wireless access provided by APs 
connected to the access layer 
• Virtual Chassis with software upgrade
Virtual 
Chassis
OS6870
OS6870
OS6870
OS6870
OmniSwitch 6870 or 6860N 
for 10/25 GigE L2/L3 
Core switching
OmniSwitch 6560/E 
for 1 /2.5/ 5 GigE access with PoE+
and 10GigE uplinks
LAG
LAG
OS6560E
OS6560E
Data Center/Server Farm
LAG
<<<PAGE 315>>>
OMNISWITCH
COMPACT CORE NETWORK
• Key Elements
• Network virtualized using Virtual Chassis (VC)
• simplified two-layer architecture
• software upgrade 
• Fully redundant and resilient network 
• Fast re-convergence time on failure
• UNP for NAC security and QoS
• Server farm or data center dual home 
connected directly to network core with LAG
• High speed wireless access provided by APs 
connected to the access layer 
Data Center/Server Farm
LAG
OS6900
OS6900
OmniSwitch 6860N/OS6870
for 1/2.5/5/10 GigE access 
with PoE++ and 10/25/40/100 GigE uplinks
OmniSwitch 6900 
for 10/25/40/100 GigE L2/L3 
Core switching
Virtual 
Chassis
LAG
LAG
OS6860N
OS6870
<<<PAGE 316>>>
OMNISWITCH
10/40 GIGE DISTRIBUTED RING NETWORK
• Key Elements
• Network virtualized using ERPv2
•
Simplified two-layer architecture 
•
Fully redundant and resilient network 
•
Fast re-convergence time on failure
•
Dual Home Link (DHL) at the access
• User Network Profile mobility (UNP) at access 
layer
• 10 GigE links from the network core to Server 
farm or data center
• High speed WLAN access through APs connected 
to the access layer
Building 2
Building 3
Building 1
Building 4
ERP
OS6560/E
OS6360
OS6360
OS6560/E
OS6860N
OS6870
OS6900
Building 5
Data Center/Server Farm
OS6900
OS6900
OS6900
OS6900
OS6900
OS6900
OmniSwitch 6900
for 10/40/100 GigE 
Core switching
OmniSwitch 
6870/6860N/6560/E/6360 
for 1 GigE or MultiGigE access
10/25/40/100GigE uplinks
POE+
OS6360
<<<PAGE 317>>>
OMNISWITCH 
10/40/100 GIGE DENSE CORE NETWORK 
• Keys Elements
• Very large networks with high concentration of 
users on certain locations
• Network virtualized using Virtual Chassis (VC)
•
Widely scalable architecture 
•
Dual Home Link (DHL) at the access
•
Reduced management point with VC technology 
from access to core
• User Network Profile mobility (UNP) at access 
layer
• Fully redundant and resilient network 
• Fast re-convergence time on failure
• Triple speed to support various end devices
OmniSwitch 9900 
10/40/100 GigE core 
switching
OmniSwitch 6900
10/40 GigE
at aggregation layer
Data center dual home 
attached to network 
core with 10GigE links
(LAG)
OmniSwitch 6860N for
Multi GigE access with 
PoE+ & 10GigE uplinks
OS9900
OS6900
OS9900
OS6900
OS6900
OS6900
OS6360
OS6465 
OS6560
OS6860N
OS6870
OS6360
OS6465
OS6560
OS6860N
OS6870
OS6360
OS6465 
OS6560
OS6860N
OS6870
Data Center
Core
Aggregation
Access
Virtual 
Chassis
<<<PAGE 318>>>
OMNISWITCH 
10/40/100 GIGE DENSE CORE NETWORK 
• Keys Elements
• Very large networks with high concentration of 
users on certain locations
• Network virtualized using Virtual Chassis (VC)
•
Widely scalable architecture 
•
Dual Home Link (DHL) at the access
•
Reduced management point with VC technology 
from access to core
• User Network Profile mobility (UNP) at access 
layer
• Fully redundant and resilient network 
• Fast re-convergence time on failure
• Triple speed to support various end devices
OmniSwitch 6900
10/40/100 GigE core 
switching
OmniSwitch 6870
1/10/25 GigE
at aggregation layer
Data center dual home 
attached to network core 
with 10 GigE links (LAG)
OmniSwitch 
6360/6465/6560/E for
up to 5 GigE access with 
PoE+ & up to 10GigE 
uplinks
OS6360
OS6465
OS6560/E
OS6360
OS6465
OS6560/E
OS6360
OS6465
OS6560/E
OS6900
OS6900
OS6900
OS6900
OS6870
OS6870
OS6870
OS6870
Virtual 
Chassis
Data Center
Core
Aggregation
Access
<<<PAGE 319>>>
LAN
LAN
LAN
LAN
OMNISWITCH 6860N / 6865 / 6870 / 6900 / 9900 
ENTERPRISE SPB LAN CORE
OmniSwitch
6860N/6870/6900
OmniSwitch
6860N/6870/6900
OmniSwitch
6860N/6870/6900
OmniSwitch
6860N/6870/6900
OmniSwitch
6860/6865
6900
9900/10K
OmniSwitch
6360
6465
6560/E
OmniSwitch
6860N
OmniSwitch
6860N
OmniSwitch
6860N
OmniSwitch
6860N
SPB
Network
OmniSwitch
6360
6465
6560/E
OmniSwitch
6360
6465
6560/E
Admin
Admin
Staff
Agent
OmniSwitch
6360
6465
6560/E
Admin
Staff
Agent
Staff
Agent
MPLS styled service architecture
Development of service orientated architecture
VLAN extensibility across campus
No STP
Faster, easier to deploy
Service Virtualization (ISID) for departmental isolation
Enabling multi-tenancy on campus sites
L3 inter-departmental routed control with VPN-lite or 
L3-VPN
VXLAN support for DCI
Transparent VLAN extension and transport between campus segments across SPB-M network
<<<PAGE 320>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.
<<<PAGE 321>>>
O M N I S W I T C H L I C E N S I N G  M O D E L  A N D  Q U O TAT I O N
CAMPUS LAN NETWORK 
SOLUTION
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.
<<<PAGE 322>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
•
Pricing information
•
Ordering Guidelines
•
Licensing management
<<<PAGE 323>>>
PRICING INFORMATION
https://myportal.al-enterprise.com
<<<PAGE 324>>>
PRICING INFORMATION 
* The date noted on the front page of this price list.
The products and prices are subject to change without notice. 
No discount is offered on upgrades.
All prices in the Worldwide Price List version are in US Dollars and in the Worldwide Price List Euro are in Euros.
Month_EURO_WWPL_Final
Month_WWPL_Addendum
Price List Guidelines
Promotions
New products
Modified products
EoS Announced Products
Month_WWPL_EOS
MTBF Summary
Month_202x_WWPL_Excel_Version
Month_EURO_WWPL_Final
Month_WWPL_Addendum
Price List Guidelines
Promotions
New products
Modified products
EoS Announced Products
Month_WWPL_EOS
<<<PAGE 325>>>
LAN OMNISWITCH OFFER 
PRICE LIST
Family
Item
Sales Category
=> discount level
Availability
• Standard
• Extended
• Contact
Service Category
<<<PAGE 326>>>
PRICING
INFORMATION
Product Availability
Unless otherwise noted, availability of product is quoted as “Standard”, "Extended", or “Contact.” These 
are defined as follows:
• Standard: Indicates that availability of product ARO (After Receipt of Order) is within standard 
delivery times quoted by Alcatel-Lucent . Average delivery lead-time is two (2) weeks ARO.
• Extended: Indicates that availability of product ARO is greater than standard delivery time. 
Average delivery lead-time is Four (4) weeks ARO.
• Contact: Product is announced but not released; availability information can only be given by 
contacting your Alcatel-Lucent representative.
• "Contact" within the Service and Support section identifies items that must be scheduled 
before placing an order.
Section
Model No
Model Description
Sales Category
Service Category
Availability
List Price
Euro
Product Categories
Alcatel-Lucent Products have category designations to assist the sales force and business partners:
• Sales category designations are A, B, C, D, E, F, G, H, I, J, K, L, M, O, P, Q, S, U, W, Z and NA .
•
Consult your contract or channel partner for actual discount level.
• Service category designations are a combination of two digits.
•
Consult your contract or channel partner for further information.
Month_2xxx_WWPL_Excel_Version
<<<PAGE 327>>>
ORDERING GUIDELINES
<<<PAGE 328>>>
OMNISWITCH
ORDERING GUIDELINES
OmniSwitch model
Backup & POE Power-Supply
Stacking Interface, Cables, Transceivers and 
Accessories
Licenses
Switch model with  
“–ZZ” extension have 
no power cord included
e.g. 
OS6860N-P48M-ZZ
OS6560-P24X4-ZZ
For OS6860N models 
with “-00” extension 
PS must be ordered 
separately
e.g. OS6860N-P24M-00
<<<PAGE 329>>>
OMNISWITCH 2260
ORDERING GUIDELINES
OmniSwitch 2260 model
Transceivers
Switch model
●OS2260-10 / P10
●OS2260-24 / P24
●OS2260-48 / P48
AC PSUs / No Redundant PS 
Transceivers
-
SFP for Gigabit uplinks
(refer to the OmniSwitch Transceivers Guide)
<<<PAGE 330>>>
OMNISWITCH 2360
ORDERING GUIDELINES
OmniSwitch 2360 model
Transceivers
Switch model
●OS2360-24 / P24
●OS2360-48 / P48
●OS2360-P24X / P48X
●OS2360-U24X / U48X
AC PSUs / No Redundant PS 
Transceivers
-
SFP for Gigabit uplinks
-
SFP+ for 10 Gigabit uplinks
(refer to the OmniSwitch Transceivers Guide)
<<<PAGE 331>>>
OMNISWITCH 6360
ORDERING GUIDELINES
• Switch model
•
OS6360-10 / P10 / P10A
•
OS6360-24 / P24
•
OS6360-48 / P48
•
OS6360-PH24 / PH48
•
OS6360-P24X / P48X
• AC PSUs / No Redundant PS 
• Transceivers
•
SFP/SFP+ for Gigabit uplinks and stacking (refer to the OmniSwitch 
Transceivers Guide)
OmniSwitch 6360 model
Transceivers
- “A": Does not support PPoE and FPoE
License
• 10G license upgradeable
License
<<<PAGE 332>>>
OMNISWITCH 6465
ORDERING GUIDELINES
• Switch model
•
OS6465-P6 
•
OS6465H-P12
•
OS6465-P28 
•
OS6465T-12
•
OS6465T-P12
• With or Without PSUs / Redundant PS
•
OS6465-BRP – Modular 180W AC Power supply
•
OS6465-BPRD Modular 180W DC Power supply
•
OS6465-BPN-H DIN Rail mounted 180W AC power supply
•
OS6465H-BPNX DIN Rail mounted 240W AC power supply
• Transceivers
•
SFP/SFP+ for Gigabit uplinks and stacking (refer to the OmniSwitch 
Transceivers Guide)
• Licenses
•
MACsec license per unit (no cost)
OmniSwitch 6465 model
Backup & POE Power-Supply
Stacking Interface, Cables and Transceivers
<<<PAGE 333>>>
OMNISWITCH 6560
ORDERING GUIDELINES
• Switch model
•
OS6560-X10
•
OS6560-24X4 / P24X4 / 48X4 / P48X4
•
OS6560E-P24Z8 
•
OS6560-P24Z24
•
OS6560E-P48Z16
• AC or DC PSUs / Redundant PS 
•
OS6560-BP-P modular (300W) 
•
OS6560-BP-PH modular (600W)
•
OS6560-BP-PX modular (920W)
•
OS6560-BP-D modular (150W)
•
OS6560-BP modular (150W)
• Stacking cables
•
OS6560-CBL – 40xm/1m/3m non 1Gig Models only
• Transceivers
•
SFP/SFP+ for Gigabit uplinks and stacking
• Licenses
•
MACsec license per unit (no cost)
•
Metro Ethernet license from 8.9R1
•
Advanced Routing license from 8.9R4
OmniSwitch 6560 model
Backup Power-Supply
Stacking Interface, Cables and 
Transceivers
<<<PAGE 334>>>
OMNISWITCH 6570M
ORDERING GUIDELINES
• Switch model
•
OS6570M-12 / 12D
•
OS6570M-U28 / U28D
• AC or DC PSUs / Redundant PS 
•
OS6570-12-BP modular (30W) 
•
OS6570-12-BP-D modular (60W)
•
OS6570-BP modular (150W)
•
OS6570-BP-D modular (150W)
• Stacking cables
•
OS6560-CBL – 40cm/100cm/300cm/1m/3m/7m
• Transceivers
•
SFP/SFP+/SFP28 for uplinks and stacking
• Licenses
•
No license needed for Metro Ethernet, it is included
•
Advanced Routing (AR) license from 8.9R4
•
PRM12 license to enable both AR and SPB on 12/12D 
•
PERF license to enable additional 10G ports on U28
•
PRM28 to enable 25G speed on uplinks, Advanced Routing and SPB on U28
OmniSwitch 6570M model
Backup Power-Supply
Stacking Interface, Cables and 
Transceivers
<<<PAGE 335>>>
OMNISWITCH 6860N 
ORDERING GUIDELINES
• Switch model
•
OS6860N-P24M
•
OS6860N-P48M / PH48M
•
OS6860N-P24Z
•
OS6860N-P48Z / PH48Z
• AC or DC PSUs / Redundant PS 
•
OS6860-BP-P modular (300W) 
•
OS6860-BP-D modular (150W)
•
OS6860N-BPXL modular (2000W)
•
OS6860N-BPPX modular (920W)
•
OS6860N-BPPH modular (600W)
• Stacking cables (VC)
•
40 Gigabit direct attached stacking copper cable QSFP-40G [40cm, 1m, 3m, 7m] 
•
100 Gigabit direct attached cable QSFP-100G-[40cm, 1m, 3m, 5m]
• Transceivers
•
SFP/SFP+/SFP28/QSFP/QSFP28 for uplinks and stacking
• Uplink modules
•
OS68-CNI-U1 (1 x 40/100G QSFP28 port)
•
OS68-QNI-U2 (2 x 10/25/40G QSFP+ ports)
•
OS68-VNI-U4 (4 x 10/25G SFP28 ports)
•
OS68-XNI-U4 (4 x 10G SFP+ ports)
• Licenses
•
MACsec license per unit (no cost)
•
MPLS license per unit
OmniSwitch 6860N model with or 
without PS
Power supply (if needed) and
Backup Power-Supply
Uplink module (for M models)
- "P": it is a PoE capable model
- "D": the bundle comes with DC power supply
- “00” : bundle comes with no PS, needs to be 
ordered separately
Stacking Interface, Cables and 
Transceivers
<<<PAGE 336>>>
OMNISWITCH 6865 
ORDERING GUIDELINES
• Switch model
•
OS6865-P16X
•
OS6865-P16XD
•
OS6865-U12X
•
OS6865-U12XD
•
OS6865-U28X
•
OS6865-U28XD
• AC or DC PSUs / Redundant PS
•
OS6865-BP
•
OS6865-BP-D 
• Stacking cables (VC)
•
Direct attached copper cable
•
ISFP-10G-C1M
•
ISFP-10G-C7M
• Transceivers
•
SFP/SFP+ for Gigabit uplinks and stacking (refer to the 
OmniSwitch Transceivers Guide)
OmniSwitch 6865 model
Backup Power-Supply
Stacking Interface, Cables and Transceivers
- "P": it is a PoE capable model
- "D": the bundle comes with DC power supply
<<<PAGE 337>>>
OMNISWITCH 6870 
ORDERING GUIDELINES
• Switch model
•
OS6870-24/48 (D)
•
OS6870-PH(24)/(48)Z
•
OS6870-PX(24)/(48)Z
•
OS6870-PH(24)/(48)M
•
OS6870-PX(L)(24)/(48)M
•
OS6870-V12(D)
• AC or DC PSUs / Redundant PS 
•
OS6870-BP modular (250W)
•
OS6870-BP-D modular (250W)
•
OS6870-BPH modular (550W)
•
OS6870-BPPH modular (600W)
•
OS6870-BPPX modular (1200W)
•
OS6870-BPXL modular (2000W)
• Stacking cables (VC)
•
40 Gigabit direct attached stacking copper cable QSFP-40G [40cm, 1m, 3m, 7m]
•
100 Gigabit direct attached cable QSFP-100G-[40cm, 1m, 3m, 5m]
•
200 Gigabit direct attached cable SFP-200G-[50cm, 1m, 3m]
• Transceivers
•
SFP/SFP+/QSFP/SFP28/QSFP28/QSFP56 for uplinks and stacking
• Uplink modules
•
OS68-CNI-U2 (2 x 40/100G QSFP28 port)
•
OS68-LNI-U6 (6 x 10/25/40/50G SFP56 ports)
OmniSwitch 6870 model
Backup Power-Supply
Stacking Interface, Cables and 
Transceivers
Uplink module (for M/V models)
Licenses
•
MACsec license per unit (no cost)
•
PERF license per unit
•
PRM1 to enable VxLAN EVPN and 50G 
on Premium models (M and V)
•
PRM2 to enable VxLAN EVPN  on 
advanced models (24/48 and Z)
<<<PAGE 338>>>
OMNISWITCH 6860N
PRICING
<<<PAGE 339>>>
OMNISWITCH 6860N
PRICING (ACCESSORIES)
<<<PAGE 340>>>
OS6900 / 6920
ORDERING GUIDELINES
•
Model (Front to back cooling / Back to front cooling)
•
OS6900-T24C2
•
OS6900-X24C2 
•
OS6900-T48C6
•
OS6900-X48C6
•
OS6900-X48C4E
•
OS6900-V48C8
•
OS6900-C32E
•
OS6920-D32
•
Transceivers (refer to the OmniSwitch Transceivers Guide)
•
SFP for Gigabit
•
SFP+ for 10-Gigabit
•
QSFP+ for 40-Gigabit
•
QSFP28 for 100-Gigabit
•
QSFP-DD for 400-Gigabit
•
Splitter cable QSFP-4x10G, QSFP-4x25G …
•
All models come with built-in redundant PSUs
•
MACsec license OS-SW-MACSEC no cost, must be included
•
MPLS license
Chassis Model
Transceivers
Advanced Software 
Licenses
<<<PAGE 341>>>
OMNISWITCH 6900
PRICE LIST
<<<PAGE 342>>>
OS9900
ORDERING GUIDELINES
OS9907
Base bundle  [OS9907-CB2(-D)*)]
Chassis / Single CMM2 / Single CFM2
Three Fan tray / Single Power Supply (AC)
Fully featured AOS Software
Redundant bundle  [OS9907-RCB2(-D)*]
Chassis / Dual CMM2s /Dual CFM2
Three Fan tray / 2 Power Supplies (AC)
Fully featured AOS Software
Base bundle 
Redundant 
bundle
Network 
Interfaces
Transceivers
License
Transceivers
•
Based on desired connectivity (refer to the OmniSwitch Transceivers Guide)
*  D for DC power supply
** XX country specific power cord designator 
License
•
MACsec license
•
One license required per chassis. 
Network Interfaces
•
1G port connectivity
•
OS99-GNI-48
•
OS99-GNI-P48
•
OS99-GNI-U48
•
10G port connectivity
•
OS99-XNI-48
•
OS99-XNI-U24 
•
OS99-XNI-U48
OS9912
Base bundle  [OS9912-CB(-D*)]
Chassis / Single CMM2 / Single CFM
Three Fan tray / Single Power Supply (AC)
Fully featured AOS Software
Redundant bundle  [OS9912-RCB(-D)*]
Chassis / Dual CMM2s /Dual CFM
Three Fan tray / 2 Power Supplies (DC)
Fully featured AOS Software
•
Multi Gig port connectivity
•
OS99-XNI-P24Z8
•
OS99-XNI-UP24Q2
•
OS99-XNI-P48Z16       
•
100G port connectivity
•
OS99-CNI-U8
•
OS99-CNI-U20
<<<PAGE 343>>>
OMNISWITCH 9900
PRICING
<<<PAGE 344>>>
LICENSING MANAGEMENT
<<<PAGE 345>>>
OMNISWITCH
SOFTWARE LICENSE CREATION
5
6
7
1
2
3
4
<<<PAGE 346>>>
OMNISWITCH
DEMO VS PERMANENT LICENSES
• Demo License
• Available once for MPLS (can be used one time and not more)
• Valid for 30 days total
• Activated as soon as MPLS is run on a node
• Permanent License (for MPLS, Metro Ethernet, Advanced routing, 10G)
• Each one is unique (serialized)
• Valid for a specific set of feature and platform
• Shipped as a printed document or electronic copy
<<<PAGE 347>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.