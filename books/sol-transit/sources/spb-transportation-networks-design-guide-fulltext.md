<<<PAGE 1>>>
SPB-based Transportation Networks  
Design Guide

<<<PAGE 2>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
2 
 
Contents 
1. 
Introduction ...................................................................................................................................... 5 
1.1. 
Purpose .......................................................................................................................................... 5 
1.1. 
Audience ........................................................................................................................................ 5 
1.2. 
Scope .............................................................................................................................................. 5 
1.3. 
Acronyms ....................................................................................................................................... 5 
1.4. 
Related documents ...................................................................................................................... 6 
2. 
Transportation systems overview .................................................................................................. 8 
2.1. 
System description ....................................................................................................................... 8 
2.2. 
Network requirements ................................................................................................................. 9 
2.2.1. 
Virtualization .......................................................................................................................... 10 
2.2.2. 
Availability .............................................................................................................................. 10 
2.2.3. 
Scalability ................................................................................................................................ 10 
2.2.4. 
Performance and quality of service .................................................................................... 11 
2.2.5. 
Security .................................................................................................................................... 11 
2.2.6. 
Environmental ......................................................................................................................... 11 
3. 
SPB Intelligent Fabric in Transportation..................................................................................... 12 
4. 
Architectures .................................................................................................................................. 12 
4.1. 
Overview ...................................................................................................................................... 13 
4.2. 
Control architectures ................................................................................................................ 13 
4.3. 
Station architectures ................................................................................................................. 14 
4.3.1. 
L2 VPN ...................................................................................................................................... 14 
4.3.2. 
L3 VPN ...................................................................................................................................... 15 
4.4. 
Station attachment .................................................................................................................... 17 
5. 
Design Considerations and Guidelines ........................................................................................ 18 
5.1. 
Scalability .................................................................................................................................... 18 
5.1.1. 
SPB nodes ................................................................................................................................ 18 
5.1.2. 
SPB services ............................................................................................................................. 19 
5.1.3. 
FDB ........................................................................................................................................... 19 
5.1.4. 
L3 specifications ..................................................................................................................... 20 
5.2. 
Paths and BVLANs ....................................................................................................................... 21 
5.3. 
Link Aggregation ......................................................................................................................... 22 
5.4. 
Virtual chassis ............................................................................................................................. 22

<<<PAGE 3>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
3 
 
5.5. 
Link metric .................................................................................................................................. 23 
5.5.1. 
Link metric in a LAG .............................................................................................................. 24 
5.6. 
Quality of service ....................................................................................................................... 25 
5.7. 
Multicast ...................................................................................................................................... 26 
5.7.1. 
L2 multicast ............................................................................................................................ 26 
5.7.2. 
L3 multicast ............................................................................................................................ 27 
5.7.3. 
Multicast replication examples ............................................................................................ 28 
5.8. 
Link sizing and capacity planning ............................................................................................ 30 
5.8.1. 
Scenario: Light rail project overview .................................................................................. 30 
5.8.1.1. 
CCTV system ........................................................................................................................ 31 
5.8.1.2. 
Passenger announcement .................................................................................................. 32 
5.8.1.3. 
Passenger information system .......................................................................................... 32 
5.8.1.4. 
Other systems ..................................................................................................................... 33 
5.8.1.5. 
Traffic matrix ...................................................................................................................... 33 
5.9. 
Station network attachment .................................................................................................... 34 
5.9.1. 
Ethernet ring protection attachment .................................................................................. 34 
5.9.2. 
Spanning Tree attachment.................................................................................................... 36 
5.9.3. 
Loopback detection ............................................................................................................... 36 
5.10. 
Provisioning end devices and services – Network Profiles ............................................... 37 
5.11. 
Network management, monitoring and operations .......................................................... 38 
5.11.1. 
Element management ........................................................................................................ 38 
5.11.2. 
Operations and maintenance: 802.1ag ........................................................................... 39 
5.11.3. 
Network performance: Service assurance agent ........................................................... 40 
5.11.4. 
Network maintenance........................................................................................................ 41 
5.11.4.1. 
Overload state ................................................................................................................ 41 
5.11.4.2. 
Graceful restart .............................................................................................................. 41 
6. 
Conclusion ....................................................................................................................................... 41 
 
Figure 1 - Virtual Private Networks or Containers ............................................................................ 10 
Figure 2 - SPB iFab Benefits ................................................................................................................. 12 
Figure 3 - Ring Topology ....................................................................................................................... 13 
Figure 4 - Centralized Control ............................................................................................................. 14 
Figure 5 - Hierarchical Control ............................................................................................................ 14 
Figure 6 - L2 Design ............................................................................................................................... 15 
Figure 7 - L3 Design ............................................................................................................................... 16 
Figure 8 - L3 VPN Hairpin ...................................................................................................................... 16 
Figure 9 - Intra-Station Redundant Attachment................................................................................ 17 
Figure 10 - Inter-Station Redundant Attachment ............................................................................. 18

<<<PAGE 4>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
4 
 
Figure 11 - Shortest Paths on a Ring Topology .................................................................................. 22 
Figure 12 - VC and SPB .......................................................................................................................... 23 
Figure 13 - Influencing SPT with Link Metric ..................................................................................... 24 
Figure 14 - ERPv2 Sub-Ring Attachment Through SAP UNI............................................................... 35 
Figure 15 - ERP Ring Attachment Through ERP UNI .......................................................................... 35 
Figure 16 - Loopback Detection ........................................................................................................... 37 
Figure 17 – Authentication, Provisioning & Policies ......................................................................... 37 
Figure 18 - Network Profiles................................................................................................................. 38 
Figure 19 - OAM in BVLAN and VLAN Domains ................................................................................... 40 
Figure 20 - L2 Ping and L2 Trace ......................................................................................................... 40

<<<PAGE 5>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
5 
 
1. Introduction 
1.1. 
Purpose 
 
The purpose of this design guide is to present the requirements and considerations relevant to 
the transportation vertical along with design options, best practices and configuration 
guidelines. 
 
1.1. 
Audience 
 
 
This design guide is intended for network architects and network engineers involved in the 
design, implementation and maintenance of networks in the transportation vertical. 
 
To take advantage of this document, it is expected that the reader will be familiar with 
Shortest Path Bridging and will have a solid understanding of various networking technologies 
at the ACPS or similar level. 
 
Please refer to [1] for a short introduction to SPB and to [] for a more in-depth one. 
1.2. 
Scope 
 
Although several modes of transport exist, this document focuses on rail (metro, heavy, light) 
and road transport only. More specifically, this document focuses on the fixed network 
infrastructure underpinning the multiple systems that enable the safe and reliable operation 
of rail and intelligent transport systems.  
 
Rail transport involves critical signaling and control systems which usually require sub-50ms 
convergence time. Shortest Path Bridging convergence times are generally above 200ms and 
therefore cannot meet this requirement. Carriage of services requiring such convergence 
times is out of scope and must be handled by a separate network (for example, SDH or MPLS).  
 
On-board, in-vehicle, ground-to-train, ground-to-vehicle as well as vehicle-to-vehicle 
communications are out of scope. 
1.3. 
Acronyms 
 
   AC 
access control 
   ACPS 
Alcatel-Lucent Enterprise Certified Pre-Sales 
   AFC 
automatic fare collection 
   ATC 
automatic train control 
   ATO 
automatic train operation 
   ATP 
automatic train protection 
   ATS 
automatic train supervision

<<<PAGE 6>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
6 
 
   BCB 
backbone core bridge 
   BEB 
backbone edge bridge 
   B-DA 
backbone destination address in 802.1ah PBB header 
   B-MAC 
backbone MAC address  
   B-SA  
backbone source address in 802.1ah PBB header  
   B-VID  
backbone VLAN ID in 802.1ah PBB header  
   B-VLAN  
backbone virtual LAN  
   Bridge ID  
64 bit quantity = (Bridge Priority:16)<<48 | SYSID:48  
   Bridge Priority 
16 bit relative priority of a node for tie breaking   
   BUM 
broadcast, unknown unicast and multicast 
   C-MAC 
customer MAC. Inner MAC in 802.1ah PBB header  
   C-VID  
customer VLAN ID  
   C-VLAN 
customer virtual LAN   
   EC 
Emergency call 
   ECT-ALGORITHM   32 bit unique id of an SPF tie breaking set of rules 
   FDB  
filtering database: {DA/VID}->{next hops}  
   I-SID  
logical grouping identifier for E-LAN/LINE/TREE UNIs 
   ITS 
intelligent transportation system 
   LAN  
local area network  
   LSDB  
link state database  
   LSP  
link state packet  
   MAC-IN-MAC 
Ethernet in Ethernet framing as per 802.1ah[PBB]  
   MDT  
multicast distribution tree  
   MT-ISIS  
multi topology IS-IS as used in [MT]  
   MT  
multi topology. As used in [MT]  
   NLPID   
Network Layer Protocol Identifier: IEEE 802.1aq= 0xC1  
   OAM 
operations and oaintenance (802.1ag) 
   OOBMN 
out-of-band oanagement network 
   Q-in-Q , QinQ 
additional S-VLAN after a C-VLAN (802.1ad)[PB]  
   PA 
public address 
   PBB  
provider backbone bridge - forwards using PBB  
   PIS 
passenger information system 
   (S,G)  
source & group - identity of a source specific tree  
   (*,G) 
any source & group - identity of a shared tree  
   SPB  
Shortest Path Bridging – 802.1aq 
   SPBM, SPB-M 
Shortest Path Bridging – Mac-in-Mac mode  
   SPOF 
single point of failure 
   SPT  
shortest path tree computed by one ECT-ALGORITHM  
   TC 
toll collection 
   TIS 
traveler information system 
   TMS 
traffic management system 
   VS 
video surveillance 
   VSL 
variable speed limit 
 
1.4. 
Related documents

<<<PAGE 7>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
7 
 
[1] “Evolving Enterprise Networks with SPB-M” application note, Alcatel-Lucent Enterprise 
[2] IEEE P802.1aq/D3.6, DRAFT Amendment to IEEE Std 802.1Q -2005 February 10, 2011 
[3] IS-IS Extensions Supporting IEEE 802.1aq Shortest Path Bridging draft-ietf-isis-ieee-aq-
05.txt 
[4] IEEE P802.1ah.D4.2, Supplement to Virtual Bridged Local Area Networks: Provider 
Backbone Bridges, March 26, 2008.

<<<PAGE 8>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
8 
 
2. Transportation systems overview 
 
Transportation services rely on multiple systems to keep traffic flowing or services running to 
schedule while ensuring drivers and passengers are safe and informed of any disruptions. All 
of these systems are enabled by a network and can be classified into four main categories: 
Control, safety, communications, and information. Please refer to Table 1 and Table 2 for 
examples of systems commonly found in ITS and rail/metro, respectively. 
 
Table 1 - Intelligent Transportation Systems 
Intelligent Transportation Systems 
Control 
Safety 
Communications 
Information 
Signaling 
Video Surveillance 
Telephony 
Traveler Information System 
Traffic Management System 
Emergency Call 
Wireless LAN 
 
Variable Speed Limit 
access Control 
Toll Collection 
 
 
Fire / Alarm Detection 
 
 
 
Table 2 – Rail and Metro Systems 
Rail and Metro Systems 
Control 
Safety 
Communications 
Information 
Signaling 
Video Surveillance 
Telephony 
Passenger Information System 
Automatic Train Control 
Emergency Call 
Wireless LAN 
Passenger Announcement 
 
access Control 
Ticketing 
Infotainment 
 
Fire / Alarm Detection 
Fare Collection 
Internet 
2.1. 
System description 
 
Many of these systems are found in both rail/metro and ITS while others are more specific to 
either rail/metro or ITS. We provide a brief description of these systems below. 
 
Signaling: The signaling system is responsible for directing road or railway traffic in order to avoid 
collisions. In the most basic form, use of the intersection or rail section is reserved for use in one 
direction at a time. More advanced forms of signaling improve use of the available capacity by 
detecting presence of vehicles or trains and adapting accordingly. Signaling is particularly critical in 
the case of trains: They require a long distance to stop due to the momentum associated with their 
large mass. 
 
Automatic Train Control (ATC): Automatic Train Control comprises three sub-systems: Automatic 
Train Protection (ATP), Automatic Train Operation (ATO) and Automatic Train Supervision (ATS). ATP is 
responsible for keeping trains a safe distance apart. ATO is responsible for stopping the train at the 
right place such that all coaches are accessible from the platform. ATS monitors the system status 
detecting deviation from normal operation and schedules and dynamically adjusting to them. 
 
Video surveillance (VS): CCTV is paramount to ensure personnel and passenger safety and to 
monitor critical assets as well as the state of the transportation network. High quality CCTV cameras 
can be installed at stations, intersections, tunnels, on-board the train, inside vehicles and along 
tunnels. Multiple parties can access video feeds in real time to improve response time in the event of 
an incident. 
 
access control (AC): These systems control access to restricted premises through badge or 
fingerprint scanners such that only authorized personnel is admitted.

<<<PAGE 9>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
9 
 
 
Emergency call: Push-to-talk buttons at stations, on-board the trains and along the road connects to 
assistance in the event of incidents, accidents or crime. 
 
Fire / alarm detection: Fire, smoke and other alarms are reported to security staff at the 
Operations Control Center and/or station. 
 
Telephony: The telephony system is used for staff communication and as the underlying 
infrastructure for emergency call and public address. The telephony system also links to emergency 
responders (police, fire, and ambulance). 
 
Passenger Information System (PIS): Provides real-time information about service status, 
departure/arrival times and any delays or disruptions. 
 
Traffic Management System (TMS): In a manner very similar to air traffic control, TMS systems 
regulate the flow of vehicles with the goal of lessening or eliminating congestion and, in this way, 
improving road safety and efficiency. Sensors are embedded in the surface of the road or mounted on 
equipment, for example, poles or signs. Cameras are mounted on overpasses and other vantage points. 
They feed data and video back to the Traffic Operations Center where it is processed and monitored 
and the resulting decisions are used to manage traffic. 
 
Variable speed limit (VSL): Speed limits are adjusted to respond to various traffic (for example, 
congestion or crashes), and weather conditions (for example, fog or ice) and displayed on electronic 
signs. 
 
Toll collection: This system includes manned stations as well as automatic smart tolling based on 
Dedicated Short Range Communications (DSRC), RFID tags or license plate recognition. 
 
Traveler Information System (TIS): Provides visual information about traffic and weather 
conditions, special events, incidents and disruptions. 
 
Ticketing and automatic fare collection (AFC): This system includes ticket vending machines, 
manned ticket booths, fare gates and tap on/off smart card scanners. 
 
Public address system (PAS): Provides audible information about service status, service departure 
times, schedule changes, etc. 
 
Infotainment: Provides information such as the weather forecast, news and advertising at stations or 
on board the train or vehicle and can be a source of non-fare revenue. 
 
Internet: Internet access at stations and on board the train or vehicle can improve passenger 
satisfaction. It can also generate ancillary revenues through access fees, advertising or other 
commercial arrangements. 
 
2.2. 
Network requirements 
 
This section will present and discuss the main requirements driving the network architecture 
and design choices.

<<<PAGE 10>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
10 
 
2.2.1. 
Virtualization 
 
One network will carry traffic for multiple systems over a common infrastructure. These 
systems will communicate various disparate, often proprietary, devices and applications that 
may be operated and maintained by different groups or vendors and may require 
communication with third parties. The network must be able to support multi-tenancy and 
virtual segregation such that systems and tenants do not interfere with one another. Virtual 
private networks (VPN) enable secure separation and bandwidth allocation for system and 
tenant traffic. As seen in Figure 1, all devices, systems and tenants connect to the same 
physical network. However, the network is logically partitioned into VPNs or “containers.” 
 
Figure 1 - Virtual Private Networks or Containers 
 
2.2.2. 
Availability 
 
High availability is a fundamental requirement for a network carrying mission-critical system 
traffic. Redundancy without single point of failure (SPOF) is required at the network and 
system level such that recovery upon a failure event is automatic and maintenance tasks can 
be performed in-service. When a network is redundant without SPOF, the duration of an 
outage is equal to the convergence time. This design guide considers transportation networks 
with sub-second convergence time requirements.  
2.2.3. 
Scalability 
 
The network must be capable of scaling to support the required: 
 
 
Systems and tenants (VPNs) 
 
Network nodes 
 
End devices 
 
Multicast flows 
 
Bandwidth

<<<PAGE 11>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
11 
 
Some of the largest transportation systems include dozens of systems, hundreds of nodes, 
thousands of end devices and multicast flows. 
 
2.2.4. 
Performance and quality of service 
 
Not all systems are critical to the same extent and different systems have different 
performance requirements. At one end of the spectrum, an emergency call is safety-critical 
with low bandwidth requirements and at the other end of the spectrum, internet and 
infotainment are not critical but have moderate bandwidth requirements. The ability to 
prioritize certain systems over others will be important when the network is congested or 
when traffic is re-routed around a failure. When these conditions occur, the network will 
need to manage the congestion by allocating bandwidth and prioritizing traffic on a per-
traffic-class basis. systems will be mapped to traffic classes based on their criticality and 
service level requirements. Every VPN service will carry traffic for a single system and will be 
mapped to a single traffic class. Therefore, single-level QoS is adequate and multi-level or 
hierarchical QoS will not be mandatory. 
2.2.5. 
Security 
 
In addition to segregation of system traffic into VPNs or containers, the following security 
requirements must be catered for: 
 
Network node security: Network nodes must be hardened and protected from attacks 
such as DDoS attacks. 
 
Network admission control and role-based access: access to network resources will 
only be granted upon successful user or device authentication and privileges will be 
set according to user or device role. 
 
Quarantine: The network must be capable of isolating a compromised device. 
2.2.6. 
Environmental 
 
 
Trackside and roadside equipment will be subject to harsh conditions such as extreme 
temperatures, vibrations and dust.  
 
Trackside equipment must be immune to electromagnetic emissions and keep its own 
emissions within certain limits so as to not adversely affect signaling and other systems. 
These limits are defined by European standard EN 50121.  
 
Roadside equipment must be compliant with NEMA TS-2 standard to be mounted in NEMA 
roadside cabinets.  
 
In short, trackside and roadside equipment must be fan-less, rugged and compliant with 
industrial-grade temperature, vibration, and shock and EMI/EMC specifications.

<<<PAGE 12>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
12 
 
3. SPB Intelligent Fabric in Transportation 
 
An Alcatel-Lucent Enterprise SPB-enabled Intelligent Fabric can cater for the requirements 
outlined in the preceding section as follows: 
 
 
L2 and L3 VPNs or IOT containers 
 
High availability through self-healing redundancy and sub-second convergence 
 
Scalability to thousands of nodes, services, devices and multicast flows 
 
High performance through shortest paths and QoS 
 
Security through network admission control, role-based access, quarantine, DDoS 
protection and OS hardening 
 
Hardened OmniSwitch 6855 and 6865 are suitable for roadside and trackside 
deployment 
 
In addition, an ALE SPB-enabled Intelligent Fabric greatly simplifies network operations with: 
 
 
Single control protocol (IS-IS) 
 
Plug & play end-point provisioning through profiles 
 
Service provisioning only at the edge, not at the core 
 
Single operating system 
 
Single network management system 
 
OAM (operations and maintenance) support for monitoring and troubleshooting 
 
Analytics 
 
 
Figure 2 - SPB iFab Benefits 
 
4. Architectures 
 
This section presents control, backbone, station and station attachment architectures.

<<<PAGE 13>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
13 
 
4.1. 
Overview 
 
Rings are the natural topology to redundantly interconnect network nodes along a road, 
highway, metro or railway line. A sample ring topology is show in Figure 3 for a simple light 
rail line with 17 stations, a control center and a backup control center.  
 
 
Figure 3 - Ring Topology 
 
 
 
The operations control center (OCC) is the primary location where all aspects of the 
transportation system are supervised and controlled and responses to incidents are 
coordinated. The OCC hosts multi-disciplinary teams as well as various systems, applications, 
databases and interfaces with third parties such as emergency responders. The backup 
control center (BCC) hosts redundant infrastructure and resources such that it can replace the 
OCC in the event of a disaster or during maintenance. OCC and BCC can operate in 
active/active or active/standby mode. 
 
4.2. 
Control architectures 
 
When multiple lines are operated by a single entity, control of the individual lines can be fully 
centralized as seen in Figure 4 or hierarchical as seen in Figure 5. For the rest of this 
document, we will focus on individual lines within a centralized or hierarchical control 
architecture.

<<<PAGE 14>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
14 
 
Figure 4 - Centralized Control 
 
 
 
Figure 5 - Hierarchical Control 
 
4.3. 
Station architectures 
 
Station architectures can be classified as L2 or L3. At the station access level, the topology 
may also be a ring, or a spine-and-leaf architecture. While SPB can also be used within the 
station, in this guide we will consider the more general case in which the station access 
network is based on standard Ethernet such as STP or ERP. Therefore, we will not discuss the 
architecture at the station access level but rather its point of attachment to the backbone. 
 
4.3.1. 
L2 VPN

<<<PAGE 15>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
15 
 
In an L2 VPN architecture, no routing is performed at the station level or at the station’s 
point of attachment to the backbone, the BEB. Station VLANs will be mapped to SPB Services 
(ISIDs) at the backbone BEBs through SAPs as seen in Figure 6.  
 
Station VLANs and ISIDs will normally be local to the station. In other words, each station will 
have its own set of VLANs and ISIDs which will not be shared across stations. Station VLANs 
will be mapped to ISIDs on a 1-to-1 basis through SAPs. All VLANs and ISIDs will be enabled at 
the OCC and BCC BEBs. As we will see in Section 5.1.2, this will limit the total number of 
VLANs that can be supported backbone-wide to the total number of ISIDs that can be 
supported at the OCC and BCC BEBs. 
 
Sharing of VLANs and ISIDs across multiple stations is possible, however, this is normally not 
recommended because of implications on Broadcast and multicast traffic. Please refer to 
Section 5.7.1 for a discussion of multicast replication modes and their impact on backbone 
bandwidth consumption.  
 
All routing will be performed at the OCC and BCC sites which are set up as a VRRP redundant 
pair. This includes intra-station as well as inter-station routed traffic. This must be taken into 
consideration when sizing backbone links as will be discussed in Section 5.8. 
 
Figure 6 - L2 Design 
 
 
4.3.2. 
L3 VPN 
 
Generally speaking, a L3 design is more scalable than a L2 design because the IP address 
space is hierarchical and allows for summarization while the MAC address space is flat and 
cannot be summarized. Transportation is no exception.

<<<PAGE 16>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
16 
 
In an L3 VPN architecture, routing is performed at the station BEBs. The station BEBs will be 
set up as a VRRP redundant pair and act as default gateway for station devices. Please refer 
to Figure 7. 
 
Figure 7 - L3 Design 
 
 
Every station will have its own set of station access VLANs which will not be shared among 
stations and are only local to the station. These station access VLANs can be the same or 
different across stations because they are only locally significant. The station access network 
will attach to the station BEBs through standard VLAN ports where these station access VLANs 
will be enabled. IP interfaces will reside in these station access VLANs and will be configured 
with VRRP to provide default gateway redundancy to station devices. For this reason, station 
access VLANs will need to be enabled on the link between both BEBs alongside BVLANs. 
 
A different set of VLANs will be mapped to SPB Services (ISIDs) through SAPs on a hairpin loop. 
We will refer to this second set of VLANs as station uplink VLANs. Station uplink VLANs will be 
shared among all stations. From a station access VLAN, routes outside of the station will point 
to an IP interface residing on a station uplink VLAN. No station devices will be mapped to 
station uplink VLANs. Station uplink VLANs will be used only for routing on the VLAN-side of 
the hairpin loop. Please refer to Figure 8. We will refer to this kind of hairpin as a VLAN UNI 
attachment hairpin. 
 
Please note that the speed of the hairpin ports must be the same or higher than the speed of 
the backbone NNI ports. 
Figure 8 - L3 VPN Hairpin

<<<PAGE 17>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
17 
 
 
At the BEBs, VRFs and ISIDs will be created for all systems requiring L3 isolation. These VRFs 
and ISIDs will be the same across all stations. By means of the L3 VPN feature, station access 
subnet and station uplink subnet routes within a particular VRF will be exported to and 
imported from the ISID. This means that these routes will be propagated throughout the 
backbone by IS-IS using special TLVs as defined in the IETF draft [3] and no additional routing 
protocol will be required. 
 
Compared to the L2 VPN design, a L3 VPN design is much more scalable in terms of total 
number of stations because station access VLANs are only locally significant and are not 
mapped to SPB services. Only station uplink VLANs are mapped to SPB services and these are 
shared among all stations. A L3 VPN design is also much more scalable in terms of total 
number of end devices because their MAC addresses will not be known outside of the station 
that they are in. 
4.4. 
Station attachment 
 
In order to avoid a single point of failure at the point of attachment to the backbone, the 
station access network will be redundantly attached to diverse BEBs. These BEBs can both 
reside within the same station as seen in Figure 9 or, alternatively, the station access 
network can be attached to a local BEB as well as a remote BEB as seen in Figure 10. The first 
alternative requires double the number of BEBs but no additional fiber cores and is simpler 
from an operational point of view while the second alternative requires no additional BEBs 
but requires additional fiber cores and is more complex from an operational perspective. 
 
Figure 9 - Intra-Station Redundant Attachment

<<<PAGE 18>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
18 
 
Figure 10 - Inter-Station Redundant Attachment 
 
 
When a station access network is attached to multiple BEBs, there is potential for loops to be 
created. Section 5.9 will discuss how loops can be avoided or mitigated. 
5. Design Considerations and Guidelines 
 
In this section we will look into various aspects that need to be considered when designing 
SPB-based networks for the transportation vertical. 
 
5.1. 
Scalability 
 
In this section we aim to provide some guidelines as to the size that the network can scale to 
and how this relates to switch specifications and design choices. 
5.1.1. 
SPB nodes 
 
 
As the number of SPB nodes on the network grows, so does the amount of state information in 
every SPB node (the Link State Database), SPT recalculations happen more frequently and the 
convergence time increases because SPB uses point-to-point adjacencies which means 
updates are relayed hop-by-hop. In a ring topology, the convergence time will grow with the 
number of nodes in the ring. 
 
It should be noted that not all nodes need to be SPB-enabled. In larger networks, SPB will be 
used only in the backbone while the station access network will be based on traditional 
Ethernet technologies such as Spanning Tree, Ethernet Ring Protection and Link Aggregation.

<<<PAGE 19>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
19 
 
 
5.1.2. 
SPB services 
 
The PBB header allows for 16M ISIDs, however, there are limits in the number of ISIDs that a 
single SPB node can support. This specification is most relevant in L2 designs. 
 
Since an ISID is a broadcast domain, station access VLANs need to be mapped to ISIDs on a 1-
to-1 basis in order to preserve L2 isolation in a L2 design. As a result, in a L2 design, station 
access VLANs are globally significant and the total number of station access VLANs network-
wide is limited by the total number of ISIDs supported on the OCC/BCC nodes as those nodes 
will have all VLANs and ISIDs enabled on them. Therefore, L2 designs are limited in total 
number of station access VLANs that can be supported across all stations. 
 
In a L3 design however, station access VLANs are only locally significant and it is only the 
station uplink VLANs which will be mapped to ISIDs on a 1-to-1 basis and, since these VLANs 
and ISIDs are shared among all stations, the number of supported ISIDs will not be a limiting 
factor. 
 
Table 3 specifies the number of ISIDs supported across the range of SPB-enabled OmniSwitch 
products. 
 
 
Table 3 - Service Specification 
 
OS10K 
OS9900 
OS6900 
OS6860 
OS6865 
ISIDs 
1K 
Future 
X20/X40/T20/T40: 1K 
X72/Q32: 8K 
2K 
2K 
 
5.1.3. 
FDB 
 
The FDB, or forwarding database, is the L2 (MAC) table. This specification is most relevant in 
L2 designs. 
The size of the FDB becomes relevant in L2 design because the BEBs at OCC/BCC will have all 
VLANs and ISIDs enabled on them. The size of the FDB is not so relevant in a L3 design 
because station access VLANs are only locally significant and end-device MAC addresses are 
only known within the station that they reside in. 
Table 4 specifies the FDB size across the range of SPB-enabled OmniSwitch products.

<<<PAGE 20>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
20 
 
Table 4 - FDB Specification 
 
OS10K 
OS9900 
OS6900 
OS6860 
OS6865 
FDB 
32K/slot 
128K/slot 
X20/X40/T20/T40: 128K 
X72/Q32: 228K 
48K 
48K 
 
5.1.4. 
L3 specifications 
 
L3 specifications are relevant both in L2 and L3 designs because routing is always performed, 
if not at the station BEB, at the OCC/BCC BEB. 
Both in L2 and L3 designs, a route is associated to each station access VLAN. The difference is 
that, while in L2 designs these routes will only exist at the OCC and BCC BEBs, in a L3 design 
these routes will normally exist on every BEB unless filtered out with route-maps.  
In a L3 design BEBs carry ARP entries for every end device within the station while in a L2 
design the OCC and BCC BEBs will carry entries for all end devices across all stations which 
again will limit the scalability of L2 designs. 
Systems requiring L3 isolation will be placed in separate VRFs. In a L2 design those VRFs exist 
in OCC and BCC BEBs only while in L3 designs those VRFs will exist in every BEB. 
Table 5 provides relevant L3 specifications across the range of SPB-enabled OmniSwitch 
products. 
 
Table 5 - L3 Specifications 
 
OS10K 
OS9900 
OS6900 
OS6860 
OS6865 
L3 
Table 
C48, U48, U32E: 16K 
U32S: 12K 
512K 
X20/X40/T20/T40: 
16K 
X72/Q32: 12K 
64K 
64K 
ARP 
Table 
C48, U48, U32E: 16K 
U32S: 8K 
(lowest across all modules) 
24K 
X20/X40: 8K 
T10/T40: 16K 
X72/Q32: 48K 
In a VC, lowest across 
16K 
16K

<<<PAGE 21>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
21 
 
all modules (central) 
or sum (distributed) 
VRFs 
64 
64 
64 
64 
64 
 
5.2. 
Paths and BVLANs 
 
In an SPB network, a Shortest Path Tree is built for every BVLAN. The ECT-ID influences the 
SPT tie-breaking logic in a way such that BVLANs assigned with different ECT-IDs will build 
different SPTs, provided multiple equal-cost paths exist. Load balancing is achieved by 
mapping different services (ISIDs) to different BVLANs. 
 
But as shown in Figure 11, there is a single shortest path between most node pairs in a ring 
topology. Only nodes located at the antipodes of the ring can communicate over two equal-
cost paths. 
 
For this reason, there is no gain in having more than 2 BVLANs in a ring topology. Furthermore, 
since every BVLAN builds its own SPT, resulting in additional consumption of resources and 
CPU cycles, this should be avoided. 
Moreover, in transportation, the ring topology is used for redundancy and not for the extra 
bandwidth associated to the alternative path: in the event of a failure, a single path must be 
able to carry the entire traffic load. It should also be noted that in the event of a failure, 
both SPTs will be recalculated (no fast re-route) and therefore having two paths will not 
improve re-convergence time. In fact, it will negatively impact the re-convergence time 
because double the number of CPU cycles are required to re-compute two SPTs. 
In addition, a second BVLAN will only improve link use marginally because there is a single 
path between most node pairs. 
In summary, a single BVLAN is recommended in a ring topology. Two BVLANs will provide a 
marginal improvement in link use during normal (no failure) conditions but this will come at 
the expense of increased resource and CPU utilization.

<<<PAGE 22>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
22 
 
Figure 11 - Shortest Paths on a Ring Topology 
 
5.3. 
Link Aggregation 
 
Combining multiple physical links into a logical link aggregate (LAG) improves resiliency and 
increases total available bandwidth on the logical link. 
 
In a LAG, traffic is load balanced across member ports in one of two ways: 
 
 
MAC hash (brief mode) 
 
IP + TCP/UDP port hash (extended mode) 
 
However, SPB backbone ports use MAC-in-MAC encapsulation which means MAC addresses are 
the BMACs of BEB and BCB nodes while IP addresses and port numbers are not visible to the 
hashing logic. In some situations, this will not provide enough randomness and the load will 
not be spread evenly across all different physical links. 
 
Since AOS 8.3.1R01, a “tunnel-protocol” option can be selected such that the hashing can use 
CMACs or IP addresses + TCP/UDP ports. 
 
It is recommended that this option be enabled on all SPB backbone LAGs. The choice of MAC 
(brief) or IP+TCP/UDP ports (extended) is a global setting which will apply to all LAGs. Please 
refer to the AOS Command Line Interface Guide for further details. 
 
5.4. 
Virtual chassis 
 
Virtual chassis is a feature that combines multiple “stackable” switches into a single logical 
“virtual chassis” such that each physical switch is seen as a “slot” in the virtually modular 
chassis. A virtual chassis is a single logical entity managed as one device and with a single 
control plane.

<<<PAGE 23>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
23 
 
Virtual chassis provides many benefits such as network architecture and management 
simplification. The designs presented in this document do not make use of the VC feature 
because control plane independence is preferred such that nodes are failure-independent at 
the control plane and can run different software releases if needed for maintenance reasons. 
 
That being said, VC can be used within the SPB backbone as well as at the data centers and 
station aggregation or access networks if desired. 
 
When using virtual chassis in the SPB backbone, LAGs are recommended to interconnect the 
VC to all its SPB neighbors such that one member (physical) port connects to every slot in the 
VC as seen in Figure 12. This is not mandatory but is recommended and will improve the 
network convergence time in the event of VC unit failure because the need to update tables 
during the control plane takeover is greatly reduced. 
 
Figure 12 - VC and SPB 
 
5.5. 
Link metric 
 
 
SPB uses the link metric as a measure of a link’s cost to reach another node. By default, all 
link metrics are set to 10 regardless of link speed. The link metric is an integer in the 1-16M 
range. 
 
The link metric can be adjusted to influence the SPT calculations. For instance, the metric 
can be changed to reflect the link speed. The metric of the link between OCC and BCC sites 
can be increased in such a way that station-to-station traffic does not transit through this link 
as shown in Figure 13. 
 
It should be noted that the metric must be adjusted on both sides of a link. Nodes will 
become adjacent even when the metrics are different, but the highest metric will be used in 
the SPT calculations. 
 
Changing the link metric to reflect the link speed will help steer traffic to those links with 
higher capacity and away from lower capacity ones, thus making the best use of the total 
available bandwidth and improving performance. Table 6 below shows a way in which the 
metric can be set to be inversely proportional to the link speed.

<<<PAGE 24>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
24 
 
Table 6 - Suggested Link Metric 
Speed  Suggested Metric  
100G  
1000  
50G  
2000  
40G  
2500  
25G  
4000  
10G  
10000  
1G  
100000  
100M  
1000000  
  
 
Figure 13 - Influencing SPT with Link Metric 
 
 
5.5.1. 
Link metric in a LAG 
 
Another aspect to consider is that the link metric will not change when member ports in a 
LAG fail. If a LAG is used purely for resiliency but not for bandwidth, the LAG metric should 
reflect the speed of the member ports without adjustment for the extra bandwidth.  
 
If the LAG is used for the extra bandwidth and one of the member ports fail, the metric will 
not adjust automatically and traffic will continue using the LAG (if it is in the shortest path) 
which may lead to saturation even though an alternative path with higher bandwidth may 
exist. In this case, a simple Python script can be created to dynamically adjust the link metric 
when the member ports fail or recover.

<<<PAGE 25>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
25 
 
Alternatively, instead of using LAG, a single higher-capacity link can be used or multiple non-
aggregated links can be used and load can be spread across multiple paths on a per-BVLAN 
basis. 
 
5.6. 
Quality of service 
 
In an SPB network, traffic is classified at the SAP and the classification does not change as 
traffic traverses the backbone until it exits through another SAP at the destination BEB. 
Trusted SAPs copy CoS markings from the incoming CVLAN tag onto the BVLAN tag. If incoming 
traffic is not tagged, then the port’s default priority is used. Un-trusted SAPs set the CoS 
markings to a user-defined value. 
No further classification based on L2-L4 conditions is possible within the SPB backbone due to 
the MAC-in-MAC encapsulation. 
When using an external router or hairpin loop for routing, the standard VLAN port side of the 
hairpin must best set to trust and use CoS and not DSCP in order to preserve CoS markings 
end-to-end. 
Please refer to Table 7 for an example of how various transportation systems and applications 
can be mapped to traffic classes and per-hop behaviors. 
Table 7 - Traffic Classes and Per-Hop Behaviors 
Traffic Class  
PHB  CoS  Queuing  WRED  Example Systems / Applications  
Network Management  
AF  
7  
WFQ  
NO 
SSH, SNMP, HTTPS  
Network Control  
AF  
--  
WFQ  
NO  
IS-IS, OAM  
Real-Time  
EF  
5  
SP  
NO 
Telephony  
Business Critical  
AF  
4  
WFQ  
NO 
Ticketing, tolling, admission 
control, traffic management 
system, fire and alarm detection  
Broadcast  
AF  
3  
WFQ  
NO  
Passenger announcement, 
passenger information system

<<<PAGE 26>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
26 
 
Streaming  
AF  
2  
WFQ  
NO 
Video surveillance  
Bulk  
AF  
1  
WFQ  
YES 
Infotainment  
Best Effort  
BE  
0  
WFQ  
YES  
Internet  
 
Please refer to the AOS Network Configuration Guide for platform-specific QoS details. 
5.7. 
Multicast 
 
In transportation, systems such as video surveillance, passenger announcement and passenger 
information system can use multicast. Therefore, it is important to discuss how multicast 
traffic is handled in the SPB network. In this section we will cover the basics of multicast in 
an SPB network at L2 and L3. Please refer to Section 5.7.3 for a practical example. 
5.7.1. 
L2 multicast 
 
First, let’s review L2 multicast. There are three multicast replication modes in an SPB 
network. This is applicable not only to multicast traffic, but also Broadcast and Unknown 
unicast traffic. We will refer to this traffic as BUM traffic.  
 
Head-End: In this mode, BUM traffic received on a SAP port is replicated at the ingress BEB 
and converted to multiple unicast frames: A replica is created for every other BEB in the 
same ISID and these replicas have the BEB BMACs as the B-DA and are forwarded using the 
unicast FDB. For this reason, Head-End replication can be inefficient in terms of bandwidth 
consumption but is efficient in terms of resource usage because it does not require a separate 
tree. However, Head-End replication can be optimal in some circumstances, particularly when 
combined with Multicast Optimization Phase II *. 
 
Tandem (S,G): In this mode, a separate multicast SPT and FDB are created. The multicast SPT 
is congruent with the unicast SPT however the B-DAs in the multicast FDB are multicast 
addresses constructed as a combination of ISID and source BEB BMAC. When a BUM frame is 
received on a BEB, it is MAC-in-MAC encapsulated with this special BMAC as the B-DA and 
forwarded according to the multicast FDB. A B node can use the unicast FDB to check if it is in 
the SPT between a source BEB and other BEBs in the same ISID. If the B node happens to be in 
the SPT, it will populate the multicast FDB such that the frame is replicated and forwarded as 
needed to other BEBs connecting the same service (ISID). Tandem Replication is very efficient 
in terms of bandwidth use because it will only send a single replica on any given link, however, 
it is less efficient in terms of resource use because it requires an additional SPT and multicast 
FDB. 
 
Tandem (*,G): In this mode, a separate multicast tree is created. This tree is not a Shortest 
Path tree and is not congruent with the unicast SPT. A multicast (*,G) is created for every

<<<PAGE 27>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
27 
 
BVLAN using Tandem (*,G) multicast replication. This (*,G) tree is similar to a Spanning Tree 
and is rooted at one B node according to the bridge priority. In this mode, there is a single 
tree for the BVLAN and not one tree for every node. Therefore, traffic will not generally 
follow the shortest path. This mode is a compromise between bandwidth and resource usage, 
however, it can be a good option when all traffic is sourced or destined towards the root 
bridge, as can be the case in a transportation network (OCC can be the root bridge). 
 
We can now compare these three modes, please refer to Table 8. 
 
Table 8 - Multicast Replication Modes and Suggested Uses 
 
HEAD-END  
TANDEM (S,G)  
TANDEM (*,G)  
Operation  
Frames replicated at 
the ingress BEB and 
forwarded as unicast 
using the SPT  
Frames forwarded as 
multicast and 
replicated at the 
SPT’s fork-out points  
Frames forwarded as 
multicast using a shared 
tree and replicated at fork-
out points  
Bandwidth 
Efficiency  
Low  
High  
High  
Resource 
Use  
Low  
High  
Low-Medium  
Congruency  
Yes  
Yes  
No  
Suggested 
use  
 
Low multicast 
bandwidth 
 
Many sources and 
few receivers * 
 
High multicast 
bandwidth. 
 
Few sources and 
many receivers. 
 
When root bridge is 
source or receiver of 
most multicast traffic 
and congruency is not 
required 
 
When required to 
interoperate with third 
party equipment.  
 
*: When combined with Multicast Optimization Phase II. Please contact ALE for availability. 
Tandem mode can be used as an alternative otherwise. 
5.7.2. 
L3 multicast 
 
Having discussed multicast at L2, we can now discuss multicast at L3.  
 
L3 multicast is based on Protocol Independent multicast (PIM). OmniSwitch products support 
PIM Sparse, Dense, BIDIR as well as Source Specific multicast. You can refer to the AOS 
Network Configuration Guide for a description of these multicast modes.

<<<PAGE 28>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
28 
 
In a L2 deployment, L3 multicast is used when sources and receivers do not reside in the same 
Subnet. Even if traffic is not routed at the station BEB, it will be routed at the OCC BEB. 
 
Frame forwarding and replication at L2 will depend on the type of multicast Forwarding used 
at L3. Please refer to Section 5.7.3 for practical examples. 
 
5.7.3. 
Multicast replication examples 
 
In this section we will look at multicast replication in various scenarios. This is important in 
order to plan for ring link capacity, which we will do in Section 5.8. 
 
In transportation, we normally find multicast used in two ways: 
 
 
Multicast source is located at the OCC and the multicast receivers are located at the 
stations. Passenger information, passenger announcement and infotainment systems 
may fit into this category. 
 
Multicast sources are located at the stations and multicast receivers are located at the 
OCC. Video surveillance fits into this category. 
 
There is also the possibility of sources and receivers both residing in the same station. An 
example of this may be a video surveillance console displaying local CCTV imagery. In a L3 
deployment, this traffic will be forwarded locally and not traverse the ring therefore we will 
not count it for link sizing purposes. In a L2 deployment, we will only consider the case in 
which source and receiver both reside in the same VLAN and therefore this traffic will also be 
forwarded locally and not impact ring link utilization. 
 
In L3 deployments, we will consider PIM Sparse Mode with the rendezvous point located at the 
OCC because either the sources or the receivers will be located at the OCC and therefore all 
multicast traffic will flow through the OCC. In addition, Source Specific multicast, when 
supported by the application, can be enabled such that subscribers receive traffic directly 
from the source without a RP. This helps when both sources and subscribers are co-located at 
the station. 
 
 In L2 deployments, we can consider two distinct cases:  
 
All VLAN/ISIDs are shared across all stations 
 
VLANs/ISIDs are specific to each station 
 
Now we can summarize all possibilities in Table 9 and Table 10. 
 
Table 9 - Multicast Replication for Source at OCC 
Multicast 
Source  
Design  
IP 
Replication  
SPB Replication  
Total Traffic  
One source at 
OCC  
L2 
with 
Different 
Once 
per 
VLAN/station 
Tandem: No  
N

<<<PAGE 29>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
29 
 
VLANs/ISIDs 
for 
every 
station  
(N)  
Head-End: Twice (once for the station and 
once for BCC)  
2N  
L2 with same 
VLANs/ISIDs 
for 
all 
stations  
No  
Tandem: No  
1  
Head-End: N+1 (once for every station plus 
the BCC)  
N+1  
L3 VPN with 
RP at OCC  
No  
Tandem: No  
1  
Head-End: Once per station plus once for 
BCC  
N+1  
 
 
Table 10 - Multicast Replication for Station Sources 
Multicast 
Source  
Design  
IP 
Replication  
SPB Replication  
Total Traffic  
One source at 
every station 
(N)  
L2 
with 
Different 
VLANs/ISIDs 
for 
every 
station  
No  
Tandem: No  
N  
Head-End: Twice (once for OCC and once for 
BCC)  
2N  
L2 with same 
VLANs/ISIDs 
for 
all 
stations  
No  
Tandem: No  
N  
Head-End: N+1 (once for every other station 
plus OCC and BCC)  
N x (N+1) !!!  
L3 VPN with 
RP at OCC  
No  
Tandem: No  
N  
Head-End: No  
N  
 
Referring to Table 9 and Table 10 above, it should be clear why Head-End replication is 
inefficient in terms of bandwidth consumption and tandem replication is recommended 
instead for multicast-intensive systems.  
 
In a L2 design with multicast sources at the stations and multicast receivers at the OCC, if 
VLANs and ISIDs are shared among all stations, traffic will blow out with the square of the 
number of stations if using head-end replication. Therefore, tandem replication mode is 
recommended in this case. This design is highly discouraged anyway because it has poor 
scalability in terms of end devices and even in the absence of multicast traffic, broadcast and 
Unknown unicast traffic still needs to be flooded throughout the network.

<<<PAGE 30>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
30 
 
 
5.8. 
Link sizing and capacity planning 
 
Link sizing must consider the worst case in which one of the nodes or ring links has failed and 
a single path remains. 
 
Depending on the specific system, traffic can flow: 
 
From OCC/BCC to stations (for example, passenger announcement, passenger 
information system) 
 
From stations to OCC/BCC (for example, video surveillance archiving ) 
 
Between stations (for example, telephony) 
 
Local to the station (for example, live video surveillance display) 
 
Link sizing must consider the type multicast replication: 
 
L2/L3 unicast is not replicated in the ring 
 
L2 multicast using head-end replication is replicated once per BEB in the same ISID 
 
L2 multicast using tandem replication sends a single copy on any one link 
 
L3 multicast is sent to RP as unicast and will not be replicated in the ring 
 
L3 multicast from RP will be sent as L2 multicast and will be replicated in the ring 
according to the multicast replication mode. 
5.8.1. 
Scenario: Light rail project overview 
 
In this section we will show how to do capacity planning by looking at a specific light rail 
scenario. We will show how bandwidth requirements can be estimated for the purpose of 
sizing the required link capacity. Note that this is for reference only. Requirements will 
depend on the specific solution being deployed (for example, the specific CCTV solution).  
 
This is a single-line light rail consisting of: 
 
 
OCC and BCC sites 
 
20 stations 
 
This is a L3 VPN design and as such, station access VLANs are local to the station while station 
uplink VLANs are shared across all stations. 
 
We will consider the systems below: 
 
 
CCTV 
 
Public address (PA) 
 
Passenger information system (PIS) 
 
Telephony (Tel) 
 
Automatic fare collection and ticketing system (AFC) 
 
Access control system (ACS) 
 
Time distribution System (TDS)

<<<PAGE 31>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
31 
 
In this L3 design, PIM Sparse Mode is used and the rendezvous point is located at the OCC. In 
addition, source specific multicast will be enabled such that CCTV subscribers receive traffic 
directly from the Source. This helps when both sources and subscribers are co-located at the 
station. Tandem (S,G) replication is used in ISIDs carrying multicast-intensive system traffic, 
and in this case, CCTV.  
 
Over the next few sections, we will evaluate some of these systems from a bandwidth point 
of view. 
5.8.1.1. CCTV system 
 
In many transportation networks, CCTV, or video surveillance, is the system generating the 
most traffic and placing the heaviest load on the network and hence we will discuss it in more 
detail. 
 
The CCTV system is comprised of: 
 
 
24 IP cameras per station (480 Total) 
 
4 x 6-way displays and 2 operator consoles per station 
 
12 x quad displays and 8 operator consoles at the OCC 
 
Each CCTV camera generates two streams: 
 
 
4Mbps stream for live viewing 
 
2Mbps compressed stream for archiving 
 
We consider a 20% network overhead on top of traffic requirements above. 
 
CCTV archiving is centralized at the OCC and BCC. Archiving streams will be sent as unicast 
traffic to the RP at the OCC and from there onwards it will be distributed within the OCC and 
towards the BCC also. In this manner, a single stream will circulate on the ring. We can 
calculate this traffic as 20 x 24 x 2Mbps + 20% = 1152Mbps 
 
CCTV viewing is distributed. We can further distinguish between live viewing and archive 
viewing. 
 
In this example, live viewing is based on multicast. Local live viewing at the station is 
forwarded locally with SSM and does not impact ring bandwidth. Central live viewing at the 
OCC using tandem (S,G) replication will require one copy per stream to be sent over the ring. 
We can calculate this traffic as 20 x 24 x 4Mbps + 20% = 2304Mbps 
 
Archive viewing is based on unicast.  
 
Two consoles and one of the six-way displays at each station can subscribe to archived 
streams. We can calculate this traffic as 20 x (2 + 6) x 2Mbps + 20% = 384Mpbs. 
 
Eight consoles and 12 quad-way displays at the OCC can subscribe to archived streams. 
Normally, those archives would be local at the OCC, however, in the event of failure or

<<<PAGE 32>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
32 
 
maintenance, it may become necessary to access archives stored at the BCC. For this reason, 
we will calculate this traffic as (8 + 12 x 4) x 2Mbps + 20% = 134.4Mbps. 
 
This is summarized in Table 11. 
 
Table 11 - CCTV Bandwidth Requirements 
CCTV System  
Streams  
Rate  
BW  
Source  
Destination  
BW 
from 
OCC  
BW 
to 
OCC  
Archiving  
480  
2.Mbps  
1152Mbps  
Stations  
OCC & BCC  
 
1152Mbps  
Live Viewing @ OCC  
480  
4Mbps  
2304Mbps  
Stations  
OCC & BCC  
 
2304Mbps  
Archive Viewing @ 
Station  
160  
2Mbps  
384Mbps  
OCC/BCC  
Station  
384Mbps  
 
Archive Viewing @ 
OCC  
56  
2Mbps  
134.4Mbps  
BCC  
OCC  
 
134.4Mbps  
Sub-Total  
 
384Mbps  
3590Mbps  
 
5.8.1.2. Passenger announcement 
 
Passenger announcement uses both live and pre-recorded messages.  
 
Pre-recorded messages are sent from OCC to stations as a file and stored locally at the station. 
 
Live messages originate from the station or from the OCC. 
 
Live messages originating from the station do not consume ring bandwidth. 
 
Live messages originating from OCC consume 128Kbps each. 
 
100Mbps is reserved for this system such that a 50MB pre-recorded message can be 
transferred in five seconds (accounting for 25% overhead) when the network is congested. 
 
There are eight operators at OCC and therefore a maximum of 8 x 128Kbps = 1Mbps for live 
messages, this is negligible. 
5.8.1.3. Passenger information system 
 
Video files are transferred from the OCC and stored locally at the stations 100Mbps are 
reserved for PIS. 
 
A 1GB file can be transferred in 100 seconds, accounting for 25% overhead.

<<<PAGE 33>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
33 
 
5.8.1.4. Other systems 
 
Systems below require minimal bandwidth, 100Mbps bidirectional bandwidth is budgeted per 
system. 
 
 
Automatic fare collection and ticketing 
 
Access control system 
 
Time distribution system 
 
Telephony 
 
 
Two operator telephones and six emergency telephones per station 
 
128Kbps 
 
(2 + 6) x 20 x 128Kbps = 20Mbps 
 
Nevertheless, 100Mbps of bidirectional bandwidth is still budgeted for telephony. 
 
5.8.1.5. Traffic matrix 
 
Table 12 below summarizes the traffic requirements for all systems. A 30% buffer is added on 
top for future requirements. 
 
 
Table 12 - Traffic Matrix 
System  
BW from OCC  
BW to OCC  
CCTV  
384Mbps  
3590Mbps  
Passenger Announcement  
100Mbps  
~NIL  
Passenger Information  
100Mbps  
~NIL 
Telephony  
100Mbps  
100Mbps  
Automatic Fare Collection  
100Mbps  
100Mbps  
Access Control  
100Mbps  
100Mbps  
Time Distribution  
100Mbps  
100Mbps  
Total System Traffic  
984Mbps  
3990Mbps

<<<PAGE 34>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
34 
 
Buffer 30%  
295Mbps  
1197Mbps  
Grand Total  
1279Mbps  
5188Mbps  
 
As can be seen in Table 12 above, 10Gbps links will be sufficient in this case. However, a 
simple change in video codec can have tremendous impact on bandwidth consumption. 
5.9. 
Station network attachment 
 
The station access network is attached to diverse BEBs for redundancy. The station access 
network can be based on ERP or Spanning Tree Protocol. In this section we will consider both 
of these alternatives from a loop prevention point of view. 
5.9.1. 
Ethernet ring protection attachment 
 
There are two different ways in which this can be done. Please refer to the AOS Network 
Configuration Guide for an introduction to ERP and ERPv2. 
 
Let’s start by introducing the more general way. In this case, the station access network 
topology can be an ERPv2 sub-ring as shown in Figure 14. This sub-ring is attached to two 
BEBs through SAP Ports. The sub-ring should not be closed with additional ring or SAP ports 
and should only be closed through the SPB backbone instead. The sub-ring can use R-APS or 
non R-APS virtual channel. R-APS PDUs will be tunneled through the SPB backbone to other 
BEBs connecting the Service (ISID). Whether it is tagged or un-tagged, the sub-ring’s service 
VLAN must be matched by SAPs at the BEBs. 50ms should not be expected in every failure 
mode.

<<<PAGE 35>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
35 
 
Figure 14 - ERPv2 Sub-Ring Attachment Through SAP UNI 
 
 
Let’s now introduce the second alternative. In this case, we will take advantage of the fact 
that the SPB backbone topology is also a ring and there is a direct link between both BEBs as 
shown in Figure 15. ERP-protected VLANs as well as the ERP service VLAN will run alongside 
BVLANs on the link between both BEBs. In this manner, the ERP ring is closed with ring ports. 
But since SAP ports cannot be ring ports, a hairpin is used to map the ERP VLANs to SAPs. This 
method can be used in both L3 and L2 designs. The advantage of this method is that it can 
deliver 50ms convergence time in the event of sub-ring failure. 
 
Figure 15 - ERP Ring Attachment Through ERP UNI

<<<PAGE 36>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
36 
 
5.9.2. 
Spanning Tree attachment 
 
When the topology within the station is not a ring, or when the station access network is 
based on third-party equipment that does not support ERP, Spanning Tree Protocol can be 
used.  
 
On NNI ports, STP is automatically disabled for all BVLANs. If standard VLANs run alongside 
BVLANs on NNI interfaces, then STP can be used on those standard VLANs. 
 
The default L2 profile on SAP ports is to tunnel STP BPDUs. 
 
In a L2 design with SAP port attachment, this is appropriate when every station has its own 
set of VLANs and ISIDs. However, if all stations share VLANs and ISIDs, all station access 
networks will be in the same STP domain. This is not a preferred way. This situation can be 
avoided by placing each station in a different MSTP region and making use of the max-hop 
parameter. 
 
In a L3 design with VLAN UNI port attachment, station access VLANs are only local to the 
station and STP can be used to prevent loops within the station. Station uplink VLANs are 
shared across all stations and loops will be prevented with STP. 
 
5.9.3. 
Loopback detection 
 
An SPB backbone with a set of multiple interconnected switches can be logically viewed as a 
big switch. The big switch connects to the station access network through SAP or VLAN UNI 
ports. 
 
Mis-configurations and faults at the station access network can create loops spanning both the 
station access network and the SPB backbone. This can result in broadcast storms. In order to 
protect the SPB backbone from broadcast storms, these loops have to be detected and broken. 
 
Loopback detection (LBD) can detect and protect the backbone network from forwarding 
loops created at the station. LBD operates in addition to STP or ERP. When a loop is detected, 
the port is disabled and goes into a shutdown state. A trap is sent and the event is logged. 
 
The switch periodically sends out LBD frames from LBD-enabled ports and concludes that the 
port is looped back if it receives the frame on any of the loop-back-detection enabled ports. 
 
LBD can be used on both VLAN UNI and SAP UNI ports. In the case of SAP UNI ports, LBD 
frames will be sent on all SAPs because different station access VLANs may have different 
logical topologies. However, if a loop is detected on a SAP, the entire physical port will be 
shut down.  
 
LBD should be enabled on all UNI ports. 
 
Figure 16 illustrates situations in which LBD can detect and break loops.

<<<PAGE 37>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
37 
 
Figure 16 - Loopback Detection 
 
 
5.10. 
Provisioning end devices and services – Network Profiles 
 
A transportation network will comprise dozens of systems and thousands of end devices. Each 
device needs to be mapped to the right service, or “container”, and the service needs to be 
enabled on the access switch that the device is connecting to. In addition, differentiated 
security (ACL) and QoS policies are often required for the various systems and devices.  
 
 
Figure 17 – Authentication, Provisioning & Policies 
 
 
 
A Network Profile (NP) is a set of rules that specifies how a device will be bound to a VLAN or 
SPB service. This binding can be based on MAC address or range, IP address, VLAN tag or 
authentication (802.1x or MAC) with a RADIUS server. If the VLAN or SPB service that the NP 
refers to does not exist on the access switch, it can be dynamically created as well. The NP

<<<PAGE 38>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
38 
 
can also contain ACL and QoS policies such that different security and SLAs can be applied to 
different systems and device types. 
 
Figure 18 - Network Profiles 
 
 
At the station access switch, end devices are mapped to VLANs based on their MAC address or 
range, IP address or authentication (802.1x or MAC) against a RADIUS server. If the VLAN does 
not exist on the access switch, it can be dynamically created and added to the uplink through 
MVRP, provided the VLAN exists on another switch. 
 
At the BEB switch, there are two possibilities depending on the type of attachment (VLAN or 
SAP UNI). When attaching on a SAP UNI port, an SPB NP profile will bind the traffic to an SPB 
service based on the incoming traffic VLAN tag. If the SPB service does not already exist on 
the BEB, it can be dynamically created. When attaching on a VLAN UNI port, the port will be 
simply configured as a trunk and all required VLANs will be enabled on the port. When using a 
hairpin loop, both sides of the hairpin will be statically configured. 
 
Network Profiles reduce deployment and operations cost because manual configuration tasks 
are greatly reduced and moves, adds and changes are automated. In addition, Network 
Profiles improve security and service levels because only authenticated devices are allowed 
and differentiated policies are dynamically applied without the burden of manual 
configuration. 
 
5.11. 
Network management, monitoring and operations 
 
This section will discuss several aspects related to the management, monitoring, operations 
and maintenance of an SPB network. 
5.11.1. 
Element management

<<<PAGE 39>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
39 
 
OmniSwitch products can be managed through a Console port as well as Telnet, SSH and Web 
(HTTP/HTTPS) interface (Webview). 
 
Remote management through Telnet, SSH or Web requires IP connectivity. IP connectivity is 
also required to communicate with a RADIUS server, both for AAA and end-device 
authentication (NAC) through 802.1x or MAC. 
 
There are various ways in which this can be accomplished: 
 
 
Out-of-band management: An out-of-band management network (OOBMN) is a 
dedicated, physically separate network that is used for management purposes only and 
not for user traffic. Depending on the specific device, this OOBMN can connect to: 
o Ethernet management port: The EMP is a dedicated physical port which is 
present on certain OmniSwitch products such as 10K, 9900 and 6860E. The EMP 
can only be used for management and not for user traffic. 
o Standard port: This is a standard VLAN port. A VLAN is dedicated for 
management purposes and a Loopback IP address will reside in that 
management VLAN. The standard VLAN port can be locked-down with ACLs to 
ensure that it can only be used for management. Routing protocols must be 
configured not to exchange routing updates or route user traffic through the 
management port. 
 
In-band management: A special management VLAN is also required in this case and this 
is where the loopback IP address will reside. The difference is that management 
traffic will not run on a physically separate network. Again, there are three different 
ways in which this can be accomplished: 
o A special management ISID is created and the management VLAN is mapped to 
this ISID with a hairpin loop and SAP. 
o The management VLAN runs alongside BVLANs on backbone interfaces. The 
management VLAN uses STP or ERP. 
o A special management ISID is created and the loopback management IP resides 
in this ISID but there is no need to use a hairpin loop. This is called “in-line 
routing” and is a roadmap feature on OmniSwitch 9900. Please contact ALE for 
availability of this feature. 
5.11.2. 
Operations and maintenance: 802.1ag 
 
OAM in an SPB network is most useful to perform L2 trace and L2 ping for analysis and 
troubleshooting. Other aspects of OAM such as fault detection, which are important in PBB, 
are not so important in SPB because SPB has an IS-IS control plane. These functions (CCM) are 
not currently supported in conjunction with SPB. 
 
OAM is supported at the BVLAN level, please refer to Figure 19. Virtual MEPs must be 
configured for all BVLANs and BEBs and, optionally, also for BCBs (such that a L2 PING or L2 
trace test can be initiated from any node to any other node). MIPs are automatically created 
and do not need to be explicitly configured. 
 
Since there is no CCM function to map system names, link trace commands and output will 
reference the BMACs.

<<<PAGE 40>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
40 
 
Figure 19 - OAM in BVLAN and VLAN Domains 
 
 
OAM is also supported at the CVLAN level or between station access switches. This is useful in 
a L2 deployment for testing end-to-end service connectivity between stations or between 
stations and OCC/BCC. OAM at the CVLAN level must be set at a higher maintenance domain 
level than BVLAN OAM. 
 
Figure 20 shows a practical example of how OAM can be used to verify connectivity between 
BEBs by means of Loopback message (LBM) and loopback reply (LBR) and also checking the 
route with link trace message (LTM) and link trace reply (LTR). 
 
Figure 20 - L2 Ping and L2 Trace 
 
5.11.3. 
Network performance: Service assurance agent  
 
Latency, jitter and packet loss SAA tests are automatically set-up between all BEBs and BCBs 
and over all BVLANs with the saa auto-create command.

<<<PAGE 41>>>
Design Guide: SPB-based Transportation Network                                              Alcatel-Lucent Enterprise          
41 
 
5.11.4. 
Network maintenance 
 
Two features in SPB can assist in network maintenance tasks: Overload state and graceful 
restart. 
 
5.11.4.1. 
Overload state 
 
SPB provides a graceful way to remove a node from service for maintenance and transition 
traffic to an alternate path (if there is one) with minimal disruption. This is the “overload 
state.” 
 
Setting the overload state on the node will signal other nodes not to use it as a transit node 
and use alternate paths instead. This is equivalent to increasing the metric on all the links but 
is a much quicker way of achieving this outcome. 
 
The overload state can be set indefinitely (until removed) or it can revert after a timer 
expires. 
 
5.11.4.2. 
Graceful restart 
 
SPB IS-IS supports graceful restart in a virtual chassis or physical chassis with redundant 
control modules.  
 
Without graceful restart, a VC master or CMM takeover event would require neighbor nodes to 
tear down and re-establish adjacencies with the restarting node and re-build the topology 
database, resulting in some disruption to traffic flows. 
 
When graceful restart is enabled, and with the help of a neighbor node, the node undergoing 
a takeover will announce this condition to its neighbors by setting the RR (restart request) in 
a TLV message and continue using its existing FDB while restarting. The neighbor nodes will 
maintain their adjacencies with the restarting node during this process and send their 
complete LSP database information to the restarting node once the process is complete. 
 
This makes the transition a much smoother process because disruption to traffic forwarding is 
minimized and the topology database re-built in a much shorter time. 
6. Conclusion 
 
 
Transportation networks are under pressure to improve safety, service operation and to keep 
drivers and passengers informed and connected. Trends in mobility and internet of (IoT)things 
not only increase demands for bandwidth and power but also introduce new security and 
operational challenges.

<<<PAGE 42>>>
enterprise.alcatel-lucent.com 
 
 
Alcatel-Lucent Enterprise SPB-based Intelligent Fabric technology creates a single converged 
network that meets the present and future needs of Transportation operators with simplified 
operations and reduced TCO. 
 
This design guide has provided practical guidelines that will assist the network architect and 
network engineer in designing and managing ALE iFab-based transportation networks.