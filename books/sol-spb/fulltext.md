# sol-spb — 解决方案文档合并（页码全册连续）


<<<DOC 1: SPB/spb-architecture-tech-brief-en.pdf | 起始页 1 | 56p>>>

<<<PAGE 1>>>
Tech Brief
Shortest Path Bridging Architecture guide
Shortest Path Bridging  
Architecture guide

<<<PAGE 2>>>
2
Tech Brief
Shortest Path Bridging Architecture guide
Table of Contents
1.  About this architecture guide........................................................................................4
1.1  Purpose..........................................................................................................................4
1.2  Audience........................................................................................................................4
1.3  Glossary.........................................................................................................................4
1.4  References.....................................................................................................................5
2.  The network needs to evolve........................................................................................5
3.  Introducing SPB...................................................................................................................6
3.1  Scalable, fast-converging, multi-path fabric....................................................7
3.2  Multi-tenancy...............................................................................................................7
3.3  Dynamic service instantiation..............................................................................8
3.4  Edge-only service provisioning............................................................................8
3.5  Micro-segmentation..................................................................................................8
3.6  Non-IP core...................................................................................................................9
4.  The Data Plane: IEEE 802.1ah Provider backbone bridging..............................9
5.  The Control Plane: RFC 6329 IS-IS Equal-cost trees..........................................11
6.  The service framework..................................................................................................13
7. BUM traffic..........................................................................................................................15
8.  Creating an SPB backbone...........................................................................................16
9.  L2 services.........................................................................................................................20
10.  Routing concepts...........................................................................................................26
11.  L3 services.......................................................................................................................29
11.1  VPN Lite...................................................................................................................29
11.2  L3 VPN......................................................................................................................30
11.3  VPN Lite versus L3 VPN....................................................................................34
12.  Shared Services VPN and Route Leaking.............................................................34
13.  Automation......................................................................................................................36
13.1  Auto-Fabric.............................................................................................................36
13.2  Dynamic SAPs........................................................................................................38
13.3  Dynamic Services.................................................................................................42

<<<PAGE 3>>>
3
Tech Brief
Shortest Path Bridging Architecture guide
14.  Management...................................................................................................................43
15.  Operation and Maintenance......................................................................................45
15.1  Connectivity Fault Management: 802.1ag..................................................45
15.2  Network performance: Service Assurance Agent ...................................47
15.3  Network maintenance.........................................................................................48
16.  Service attachment redundancy.............................................................................48
17.  Loop avoidance and suppression...........................................................................51
18.  General design guidelines..........................................................................................52
18.1  BVLANs.....................................................................................................................52
18.2  VLAN-to-Service mapping.................................................................................52
18.3  Virtual Chassis.......................................................................................................53
18.4  Link Aggregation...................................................................................................53
18.5  Link Metric..............................................................................................................54
18.6  QoS.............................................................................................................................54
19.  Security guidelines.......................................................................................................54
19.1  Management VRF..................................................................................................55
19.2  MACSec.....................................................................................................................55
19.3  NAC............................................................................................................................55
19.4  Router authentication.........................................................................................55
20.  Conclusion........................................................................................................................56

<<<PAGE 4>>>
4
Tech Brief
Shortest Path Bridging Architecture guide
1.  About this architecture guide
1.1  Purpose
The purpose of this architecture guide is to present SPB (802.1aq) networking concepts along 
with design and deployment guidelines. It does not attempt to cover every aspect, nor every 
possible architecture option, only the most common, validated and recommended architectures. 
You are encouraged to refer to the Alcatel-Lucent Operating Software (AOS) documentation for 
additional details, options and guidelines.
1.2  Audience
The intended audience for this document includes customer and business partner networking 
professionals involved in the design and deployment of enterprise networks.
1.3  Glossary
AG	
Access Guardian
BCB	
Backbone Core Bridge
B-DA	
Backbone Destination Address
BEB	
Backbone Edge Bridge
BGP	
Border Gateway Protocol
BMAC	
Backbone MAC
B-SA	
Backbone Source Address
BSN	
Base Service Number
B-VID	
Backbone VLAN ID
BVLAN	
Backbone VLAN
CMAC	
Customer MAC
CP	
Control Plane
DoS	
Denial of Service
DP	
Data Plane
ECT	
Equal-Cost Tree
FDB	
Forwarding Data Base
IETF	
Internet Engineering Task Force
iFab	
Intelligent Fabric
IGP	
Interior Gateway Protocol
ISID	
Instance Service Identifier
IS-IS	
Intermediate System to Intermediate System
LDP	
Label Distribution Protocol
MAC	
Media Access Control
MACs	
Moves Adds and Changes
MP-BGP	 Multi-Protocol BGP

<<<PAGE 5>>>
5
Tech Brief
Shortest Path Bridging Architecture guide
MSTP	
IEEE 802.1s Multiple Spanning Tree Protocol
NAC	
Network Admission Control
OSPF	
Open Shortest Path First
PBB	
IEEE 802.1ah Provider Backbone Bridging
Q-in-Q	
IEEE 802.1ad Provider Bridging
RADIUS	
Remote Access Dial-In User Service
ROI	
Return on Investment
RSTP	
IEEE 802.1w Rapid Spanning Tree Protocol
SAP	
Service Access Point
SDP	
Service Distribution Point
SPB	
IEEE 802.1aq Shortest Path Bridging
SPB-M	
SPB MAC-in-MAC
SPB-V	
SPB Q-in-Q
SPF	
Shortest Path First
STP	
IEEE 802.1D Spanning Tree Protocol
TLV	
Type, Length, Value
UNP 	
User Network Profile
1.4  References
[1]	 IP/IPVPN services with IEEE 802.1aq SPB networks - draft-unbehagen-spb-ip-ipvpn-00.txt
[2]	 Alcatel-Lucent OmniSwitch® Template Based Provisioning with Alcatel-Lucent OmniVista®  
2500 Network Management System (NMS)
[3]	 Network infrastructure security best practices
2.  The network needs to evolve
Local Area Networks (LAN) have traditionally relied on Spanning Tree Protocol (STP), and its 
variants (RSTP, MSTP), collectively referred to as “STP” for simplicity, for loop prevention. STP 
achieves a loop-free topology by electing a “root bridge” and building a least-cost tree linking 
the root bridge with other non-root nodes. This least-cost tree is created by pruning (disabling) 
all branches (links) which are not in the least-cost path towards the root. STP’s design principle 
presents several drawbacks for modern Enterprise networks:
•	 Unused links: Creating a loop-free topology by disabling network links results in inefficient 
bandwidth use and low Return on Investment (ROI)
•	 Sub-optimal paths: While communication to-and-from the root bridge follows the least- 
cost path, communication between non-root bridges may need to traverse a sub-optimal  
route transiting the root-bridge instead of alternative better routes over links that have  
been disabled
•	 Slow convergence: STP is a decades-old protocol designed when network devices were far less 
powerful than they are today. Even with the “rapid” version of STP, typical convergence times 
are in the order of seconds. While STP re-converges to a new topology, transient loops may 
form, resulting in packet drops, link saturation, and session timeouts.

<<<PAGE 6>>>
6
Tech Brief
Shortest Path Bridging Architecture guide
Figure 1. The problems with STP
Destination 2
Inefﬁcient
routes
Cannot use
these links
All the nodes on
the route need to
learn MAC’s M1-M100
Destination 1
MACs
M1 ... M100
Source
Root bridge
 
In addition to STP’s weaknesses, Ethernet’s scalability beyond the LAN is limited by its lack of 
a coordinated control plane and use of a flat (as opposed to hierarchical) address space. Legacy 
Ethernet networks present the following challenges:
•	 Flooding: Ethernet’s “flood and learn” address learning floods unknown-unicast traffic until  
the destination address is learned from return traffic
•	 MAC Learning: All nodes in the LAN learn all end-device MAC addresses thus posing a 
scalability challenge
Lastly, IEEE 802.1ad (Provider Bridging, or Q-in-Q) is limited to a maximum of 4096  
service instances. 
3.  Introducing SPB
802.1aq Shortest Path Bridging (SPB) is an IEEE networking standard whose primary focus was 
addressing the challenges in STP. But SPB is much more than STP’s evolution: SPB provides 
MPLS-like VPN services but is significantly simpler to deploy and maintain. And unlike MPLS, 
which requires a “stack” of protocols (for example: LDP, OSPF, MP-BGP, among others), SPB relies 
on a single protocol to provide this functionality: IS-IS (Intermediate System to Intermediate 
System). IS-IS is the only control plane protocol required to build a multi-path topology, perform 
address learning, and carry VPN routes across the backbone. Alcatel-Lucent Enterprise’s 
Intelligent Fabric (iFab) brings further simplification by automating network node provisioning, 
client device attachment, and dynamic service instantiation. Because of this simplicity and 
automation, an ALE-powered SPB solution offers high-end services for a lower total cost of 
ownership (TCO). Let’s analyse SPB’s benefits in further detail.

<<<PAGE 7>>>
7
Tech Brief
Shortest Path Bridging Architecture guide
3.1  Scalable, fast-converging, multi-path fabric
Figure 2. Addressing STP’s challenges
Destination 2
Multiple
shortest
paths
All the links
are usable
MACs M1-M100
learning restricted
to the edges
Destination 1
MACs
M1 ... M100
PBB
encapsulation
at the edges
PBB
encapsulation
at the edges
PBB
encapsulation
at the edges
3
2
1
SPB’s loop-free topology is built by a link-state routing protocol running Dijkstra’s Shortest 
Path First (SPF) algorithm: IS-IS. With IS-IS, no network link is disabled, all paths are available 
and traffic between any pair of nodes follows the shortest path. In addition, with MAC-in-MAC 
encapsulation, backbone nodes do not learn any end-device MAC addresses, thus increasing  
the network scalability and stability. With IS-IS and MAC-in-MAC encapsulation, SPB creates an,  
any-to-any, scalable and fast-converging “fabric” supporting multiple active optimal paths for 
both bridged and routed traffic.
3.2  Multi-tenancy
SPB natively supports multi-tenancy: The physical network is partitioned into multiple virtual 
“slices” referred to as VPNs, “containers” or “communities”. Customers, or IoT device groups, 
segregated into different VPNs are isolated and do not interfere with one another. In fact, they 
can use overlapping address space without conflict. Inter-VPN communication, if needed, is 
tightly controlled by firewall policies. This multi-tenancy capability makes SPB suitable for use 
cases such as smart cities, transportation, higher education, video surveillance or data centres, 
to name a few. SPB’s scalability is not limited to 4096 tenants because its service identifier, the 
ISID, is a 24-bit field which can differentiate up to 16M services.
Figure 3. Multi-tenancy
 

<<<PAGE 8>>>
8
Tech Brief
Shortest Path Bridging Architecture guide
3.3  Dynamic service instantiation
SPB services do not need to be statically bound to a switch port. SPB is tightly integrated with 
Alcatel-Lucent Enterprise’s classification and Network Admission Control (NAC) framework 
known as Access Guardian (AG). Upon connection, end devices can be classified (for example; 
based on the MAC OUI or IoT “fingerprint” rules) or authenticated (for example; through 802.1x 
or MAC) against a RADIUS server. The appropriate service is dynamically instantiated according 
to the device or user classification, or role attribute returned by the RADIUS server. In the same 
manner, this user-to-service binding is removed when the user/device disconnects. This dynamic 
service instantiation has the following advantages:
•	 User/Device mobility: The network configuration dynamically adapts to mobile users and 
devices or Virtual Machines (VMs) migrations without need for Move, Add or Change requests
•	 Increased security: Services are instantiated on an as-needed basis only, and for authenticated 
devices/users only, if applicable. This association is maintained for as long as the user/device 
remains connected and/or authenticated, and is brought down on disconnection/log-off. These 
ephemeral services are inherently more secure: they cannot be scanned, DoSd, or otherwise 
hacked, while they’re not active.
•	 Device templates: This dynamic instantiation of network services easily lends itself into 
template-based configuration of network nodes. Edge nodes can all share the same base 
configuration template and dynamically adjust the service configurations on the fly.
3.4  Edge-only service provisioning
Whether statically or dynamically instantiated, SPB services need only be provisioned on edge 
nodes, not on core nodes. Core nodes are effectively isolated from service Moves, Adds and 
Changes and require no touch while these activities are performed. In fact, service MACs can  
be conducted during business hours and do not require a maintenance window to be scheduled, 
reducing time-to-service. 
3.5  Micro-segmentation
Firewalls filter and control communication between different VPN “tenants” or “containers”. 
But, how do you secure communication within the same VPN? For instance, if one device were 
compromised, how do you prevent lateral movement to other resources within the same VPN? 
When users/devices are dynamically bound to a service, they are also mapped to a User Network 
Profile (UNP). The UNP is a set of Access Control Lists (ACLs) and Quality of Service (QoS) policies 
which are applied to the device/user according to the device category or user role. Let’s take 
CCTV cameras as an example: ACLs contained in the UNP can allow communication between  
the camera and surveillance servers but at the same time block camera-to-camera communication, 
preventing the spread of malware, “pivoting” and other hacking techniques which rely on  
lateral movement.

<<<PAGE 9>>>
9
Tech Brief
Shortest Path Bridging Architecture guide
Figure 4. Micro-segmentation
Authenticate
Classify
Auto provision
Audio/visual proﬁle
✓ Container
✓ Quality
✓ Security
Authenticate
Classify
Auto provision
Campus operation proﬁle
✓ Container
✓ Quality
✓ Security
Authenticate
Classify
Auto provision
Security proﬁle
✓ Container
✓ Quality
✓ Security
 
3.6  Non-IP core
Even when providing L3 services to IP packets, SPB core nodes do not route traffic, they bridge 
it. In fact, SPB core nodes do not have IP addresses and the IS-IS control protocol, unlike OSPF 
and BGP, does not run on top of IP. This makes the network core inherently more secure and 
protects it from IP-based attacks such as scanning, spoofing, DoS and others. Of course, SPB 
nodes still need an IP address for management purposes, but the management IP interface is 
isolated in its own service and VRF, not in-line with user traffic.
4.  The Data Plane: IEEE 802.1ah Provider backbone bridging
The Data Plane’s (DP) mission is to forward user traffic between different ports. The DP makes 
no decisions as to what port a frame should be forwarded to. It simply performs lookups on 
the Forwarding Data Base (FDB). FDB entries indicate what port, or group of ports, each frame 
should be forwarded to and what encapsulation to use. Building, or populating entries in the 
FDB, is a function of the Control Plane (CP), which is discussed in the next section.
The SPB data plane utilizes IEEE 802.1ah Provider Backbone Bridging (PBB), aka MAC-in-MAC, 
encapsulation. The PBB header includes de following fields:
B-VID: Or Backbone VLAN (BVLAN) ID. A VLAN that serves as a transport VLAN for the SPB 
service instances and to connect SPB bridges together through SPT sets. Unlike the standard 
VLAN domain which uses “flood and learn” or source learning in the DP to populate the FDB,  
the BVLAN domain’s FDB is pre-populated by the CP. 
ISID: Service Instance Identifier. The ISID is a 24-bit number that designates the service instance, 
tenant, container or VPN. Different SPB services are assigned different ISIDs and isolated from 
one another. Each SPB service or ISID is bound to a BVLAN.
B-SA and B-DA: Or Backbone source and destination MAC addresses. The MAC addresses associated 
with SPB nodes (BMACs). Within the SPB backbone, traffic is forwarded based on the destination 
BMAC (B-DA). Inner customer MACs are not learnt or used for forwarding within the backbone.

<<<PAGE 10>>>
10
Tech Brief
Shortest Path Bridging Architecture guide
Ethertype: 0x88E7
Upon entering the SPB domain, the PBB header is wrapped around the incoming frame which 
can be un-tagged, single-tagged (IEEE 802.1q) or double-tagged (IEEE 802.1ad). Figure 5 
illustrates the case of a double-tagged (Q-in-Q) frame. Note that MAC and BMAC addresses  
are shortened to 2 bytes for simplicity in this diagram.
Figure 5. PBB Data Plane
MAC :00:01
Customer
network
Customer
network
Provider bridge
network
Provider bridge
network
Provider backbone
bridge network
MAC :00:02
MAC :00:0B
MAC :00:0A
Ethertype 802.1ad
00:01
Ethertype 802.1q
S-VID
C-VID
Ethertype (IP)
Payload
00:02
Ethertype 802.1ad
00:01
Ethertype 802.1q
S-VID
C-VID
Ethertype (IP)
Payload
00:02
Ethertype 802.1ad
00:0A
Ethertype 802.1ah
B-VID
Ethertype 802.1q
Ethertype (IP)
C-VID
I-SID
Payload
00:0B
Ethertype 802.1ad
00:01
S-VID
00:02
Ethertype 802.1q
00:01
Ethertype (IP)
C-VID
Payload
00:02
Ethertype 802.1q
00:01
Ethertype (IP)
C-VID
Payload
00:02
 
Let’s define a few key terms.
BEB: An SPB switch positioned at the edge of the PBB network that learns and encapsulates 
(adds an 802.1ah backbone header to) “customer” frames for transport across the backbone 
network. The BEB interconnects the customer network space with PBB network space.
BCB: An SPB node that resides inside the PBB network core. The BCB employs the same BVLAN 
on two or more network ports. This BVLAN does not terminate on the switch itself; traffic 
received on an SPB network port is switched to other SPB network ports. As a result, the BCB 
does not have to learn any of the customer MAC addresses. It mainly serves as a transit bridge 
for the PBB network.
Within the SPB domain, that is, between BEB and BCB nodes, frame forwarding depends entirely 
on the outer PBB 802.1ah header (BMAC and BVLAN) and not on the inner header or “customer” 
MAC addresses (CMAC). In fact, the SPB backbone nodes do not learn CMACs and this makes 
SPB networks more scalable and stable (CMACs are not learnt and therefore do not need to be 
flushed and re-learnt when they change or move). 
The DP implements an additional loop mitigation mechanism by which a node will not accept 
unexpected frames from their neighbours. This additional loop mitigation mechanism is faster 
during topology changes. In summary, SPB implements two loop avoidance mechanisms: loop 
prevention and loop mitigation.

<<<PAGE 11>>>
11
Tech Brief
Shortest Path Bridging Architecture guide
5.  The Control Plane: RFC 6329 IS-IS Equal-cost trees
As stated earlier, the role of the CP is to populate the FDB tables used by the DP. SPB uses IS-IS, 
or Intermediate System to Intermediate System (ISO/IEC 10589:2002); a well-known, proven 
and widely-deployed protocol, particularly in service-provider backbones. IS-IS is responsible 
for topology and service discovery. IS-IS is an extensible link-state protocol which implements 
Dijkstra’s Shortest Path algorithm for path computation. IS-IS extensions for SPB are described 
in RFC 6329 and include a new Network Layer Protocol Identifier (NLPID), as well as a set of 
Type-Length-Values (TLVs). In a nutshell, these extensions add support for multiple topologies, 
allowing load sharing over multiple equal-cost paths, and service-membership discovery, or in 
other words: Communicating what services are enabled on each SPB node.
Figure 6. RFC 6329 IS-IS extensions
SPB-ISIS
New!
Existing!
SPB extensions
Discovery and computation
NLPI, TLVs, PDUs
Discovery – Hello and LSP packets, Computation – SPF and SPT
 
Unlike STP which creates a single tree rooted at the root bridge, in SPB networks, every node 
builds a topology tree rooted on itself. This is the key reason why, in an SPB network, traffic 
between any pair of nodes always travels along the shortest path. When using STP, traffic 
between two nodes does not necessarily travel over the shortest path unless one of the two 
nodes involved is the root bridge. This is illustrated in figure 7 in which B1 is the root bridge. 
Traffic between nodes B5 and B2 for instance, none of which is the root bridge, cannot use the 
direct single-hop path because that link is disabled by STP. Traffic between these two nodes 
must take a 3-hop detour traversing the root bridge.
Figure 7. Multiple trees
B5
B2
B4
B1
Spanning Tree
SPB
B5
B2
Single root bridge
Every bridge is the root
Path B5 to B2 = B5 – B3 – B1 – B2
Path B5 to B2 = B5 – B2
B4
B1
B3
B3
 
In contrast, when using SPB, no link is disabled: each node is the root of its own tree. Nodes B2 
and B5 can simply communicate over the direct single-hop path while at the same time they can 
communicate with other nodes over different paths (for example; between B4 and B5). SPB’s 
support for multiple trees and multiple active paths unlocks utilization of bandwidth in optimal 
paths that would otherwise be wasted, increasing throughput and reducing latency.
An SPB network supports up to 16 BVLANs and each node builds a SPF tree for each BVLAN. 
Load balancing is accomplished by mapping different tenant services (ISIDs) to different BVLANs.  
Service traffic between any node pair uses a single path and this path only changes if the 
topology changes, for instance, on node or link failure and subsequent path re-computation. In 
other words: SPB networks do not balance loads on a packet-by-packet basis like IP networks 
do. Provided the physical topology supports multiple shortest paths (same cost and same hop 

<<<PAGE 12>>>
12
Tech Brief
Shortest Path Bridging Architecture guide
count) between two nodes, different BVLANs can build different trees and services mapped to 
those BVLANs can use different paths. And, those paths will remain the same for as long as the 
topology remains the same. An important property of SPB networks is that network paths are 
deterministic and frames are delivered in the order they were sent. This property is important 
for certain applications such as storage and real-time application traffic.
Figure 8. One tree per node and per BVLAN
B5
B2
B4
B1
B1’s tree on BVLAN A
B1’s tree on BVLAN B
B1’s tree on BVLAN C
B5
B2
B4
B1
B3
B5
B2
B4
B1
B3
B3
B5
B2
B4
B1
B5’s tree on BVLAN A
B5’s tree on BVLAN B
B5’s tree on BVLAN C
B5
B2
B4
B1
B3
B5
B2
B4
B1
B3
B3
 
The trees shown in figure 8 are SPB’s equal-cost trees (ECTs). Each node builds a tree per 
BVLAN and the cost to reach other nodes is the same across all BVLANs. The ECT-ID is a number 
assigned to each BVLAN at the time of BVLAN creation and is used for tie breaking during path 
computation. Assigning different ECT-IDs to different BVLANs helps those BVLANs build different 
trees, provided the underlying topology supports multiple equal-cost, or shortest paths.
Another important property of SPB networks is path symmetry. If you closely examine the 
picture above, you will notice that the path from node X to node Y is identical to the path from 
node Y to node X. Path symmetry is key to Operations and Maintenance (OAM). For instance, 
one-way delay calculations can be easily derived from roundtrip delay measurements. Note  
that this is not the case for other IP-based technologies such as MPLS in which the reverse  
path may differ.

<<<PAGE 13>>>
13
Tech Brief
Shortest Path Bridging Architecture guide
Figure 9. Symmetric paths, per-BVLAN load balancing
B5
B2
B4
B1
B5
B2
B4
B1
B3
B5
B2
B1 <–> B5 path BVLAN B
B1 <–> B5 path BVLAN A
B1 <–> B5 path BVLAN C
B4
B1
B3
B3
 
The result of IS-IS path computation for each BVLAN and node is the FDB which is used by the 
data plane for frame forwarding. Figure 10 shows BEB5’s unicast FDB. The multicast FDB will  
be discussed in Section 7.
Figure 10. B5’s Unicast FDB
B5
B2
B4
B1
B3
Outbound port
Node
BVID
Port 1
B1
BVID A
Port 2
B1
BVID B
Port 3
B1
BVID C
Port 1
B2
BVID A
Port 1
B2
BVID B
Port 1
B2
BVID C
Port 2
B3
BVID A
Port 2
B3
BVID B
Port 2
B3
BVID C
Port 3
B4
BVID A
Port 3
B4
BVID B
Port 3
B4
BVID C
 
6.  The service framework
An SPB service represents a VPN, or tenant, and is uniquely identified by its service identifier, 
the ISID. An SPB service needs only be created, or instantiated, on BEB nodes, not on BCB 
nodes, and only on those BEB nodes servicing locations associated to the service. SPB service 
membership information is shared across the SPB backbone by way of IS-IS TLVs such that all 
SPB nodes have a consistent view of the services which are active on each BEB. Each node  
then builds a service database.
Figure 11. The service database
B5
B2
B4
B1
B3
Node
BVID
ISID
B1
BVID A
66
B2
BVID A
66
B4
BVID A
66
B5
BVID A
66
B1
BVID B
77
B5
BVID B
77
ISID 66
ISID 77
ISID 66
ISID 66
ISID 66
ISID 77
 

<<<PAGE 14>>>
14
Tech Brief
Shortest Path Bridging Architecture guide
In each BEB node there are two kinds of virtual ports:
Service Access Point: The SAP is a UNI-side logical port which binds a physical port and specific 
customer traffic types (untagged, single-tagged, double-tagged or all) to an SPB service. Multiple 
SAPs can be associated to the same physical port thus multiplexing and mapping different 
customer traffic encapsulations to different SPB services.
Service Distribution Point: The SDP is an NNI-side logical port which binds an SPB service to  
a far-end BEB on which the service is instantiated. SDPs are dynamically created in the CP and 
only for those far-end BEBs with SAPs for the specific service. 
Let’s look at figure 12. In this diagram, B5 terminates 2 SPB services: One is associated to  
ISID 66 and the other to ISID 77. There are two SAP ports, one for each service. SAP 1:1 is 
defined on port 1, matches traffic tagged with VLAN 1, and binds it to service 66. SAP 2:2  
is defined on port 2, matches traffic tagged with VLAN 2, and binds it to ISID 77. 
ISID 66 is also enabled on nodes B1, B2 and B4 while ISID 77 is also enabled on node B1. 
Figure 12. The service framework
B5
B2
B4
B1
Node
BVID
Identiﬁer
—
—
SAP 1:1
—
—
SAP 2:2
B1
BVID A
SDP 32769: 66
B2
BVID A
SDP 32768: 66
B4
BVID A
SDP 32767: 66
B1
BVID B
SDP 32766: 77
ISID 66
ISID 77
SAP 1:1
SAP 2:2
ISID 66
ISID 66
ISID 66
ISID 77
SDP Y:66
SDP X:66
SDP X:77
SDP Z:66
 
It should be noted that while BMAC address learning is performed in the CP (for example; not 
through “flood and learn”) CMAC address learning is performed in the BEB’s DP through flood 
and learn. Near-end CMACs are bound to SAP ports and far-end CMACs are bound to SDP ports. 
BCB nodes have neither SAP nor SDP ports and therefore do not learn any CMACs.
Let’s expand this example by adding some end customer sites and CMACs associated to those 
customers. We will keep using 2-byte MAC addresses for simplicity. In figure 13, near-end CMAC 
addresses are bound to SAP ports while far-end CMAC addresses are bound to SDP ports. Within 
the service domain, a BEB performs CMAC source address learning like a standard Ethernet 
switch, except there is no “flooding” of BUM traffic. BUM traffic is discussed in the next section.
Figure 13. Customer MAC address learning
B5
B2
MAC B:B
MAC D:D
MAC E:E
MAC A:A
MAC C:C
MAC G:G
B4
B1
CMAC
ISID
Identiﬁer
A:A
66
SAP 1:1
E:E
77
SAP 2:2
C:C
66
SDP 32769: 66
B:B
66
SDP 32768: 66
D:D
66
SDP 32767: 66
G:G
77
SDP 32766: 77
ISID 66
ISID 77
ISID 66
ISID 66
ISID 66
ISID 77
SDP Y:66
SDP X:66
SDP X:77
SDP 1:1
SDP 2:2
SDP Z:66
 

<<<PAGE 15>>>
15
Tech Brief
Shortest Path Bridging Architecture guide
7. BUM traffic
SPB supports 3 BUM (broadcast, unknown unicast, and multicast) traffic replication and 
forwarding methods:
Head-end: In this mode, BUM traffic received on a SAP port is replicated at the ingress BEB and 
converted to multiple unicast frames: A replica is created for every other BEB in the same ISID 
and these replicas have the BEB BMACs as the B-DA and are forwarded using the unicast FDB. 
For this reason, Head-End replication can be inefficient in terms of bandwidth consumption but 
is efficient in terms of resource usage because it does not require a separate tree. However, 
Head-end replication can be optimal in some circumstances, particularly when combined with 
IGMP Snooping. Head-end replicated BUM traffic simply uses the unicast FDB and therefore 
travels along the same path. This property is known as congruency.
Figure 14. Head-end BUM replication
BEB4
BCB7
BEB3
BCB5
BEB1
Port
B-MAC
Type
Port 2
00:02
U
Port 7
00:03
U
Port 7
00:04
U
Port 7
00:05
U
Port 6
00:06
U
Port 7
BVID
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
00:07
U
ISID 77
ISID 77
ISID 77
ISID 77
BCB2
BCB6
 
Tandem (S,G): In this mode, a separate multicast SPT and FDB are created. The multicast SPT is also 
congruent with the unicast SPT however the B-DAs in the multicast FDB are multicast addresses 
constructed as a combination of ISID and source BEB BMAC. When a BUM frame is received on a 
BEB, it is MAC-in-MAC encapsulated with this special BMAC as the B-DA and forwarded according 
to the multicast FDB. A B node can use the unicast FDB to check if it is in the SPT between a source 
BEB and other BEBs in the same ISID. If the B node happens to be in the SPT, it will populate the 
multicast FDB such that the frame is replicated and forwarded as needed, to other BEBs connecting 
the same service (ISID). Tandem Replication is very efficient in terms of bandwidth use because it 
will only send a single replica on any given link; however, it is less efficient in terms of resource 
use because it requires an additional SPT and multicast FDB per ISID.
Figure 15. Tandem (S,G) BUM replication 
BEB4
BCB7
BEB3
BCB5
BEB1
Port
B-MAC
Type
Port 1
00:01
U
Port 2
00:02
U
Port 3
00:03
U
Port 4
00:04
U
Port 1
00:0W
M
Port 3
00:0X
M
Port 4
00:0Y
M
Port 5
00:0Z
M
Port 5
00:05
U
Port 6
BVID
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
BVID B
Out Intf
Port 3/4/5
Port 1/5
Port 1
Port 1/3
00:06
U
ISID 77
ISID 77
ISID 77
ISID 77
BCB2
BCB6

<<<PAGE 16>>>
16
Tech Brief
Shortest Path Bridging Architecture guide
Tandem (*,G): In this mode, a separate multicast tree is created. This tree is not a Shortest Path 
tree and is not congruent with the unicast SPT. A multicast (*,G) is created for every BVLAN using 
Tandem (*,G) multicast replication. This (*,G) tree is similar to a Spanning Tree and is rooted at one 
B node according to the bridge priority. In this mode, there is a single tree for the BVLAN and not 
one tree for every node. Therefore, traffic will not generally follow the shortest path. This mode 
is a compromise between bandwidth and resource usage, however, it can be a good option when 
all traffic is sourced or destined towards the root bridge.
Refer to Table 1 to compare these three modes.
Table 1. Multicast replication modes and suggested uses
Head-end 
Tandem (S,G) 
Tandem (*,G)
Operation 
BUM traffic replicated at 
ingress BEB and forwarded 
using the unicast FDB. 
BUM traffic forwarded per the 
multicast FDB and replicated 
as needed at the SPT’s fork-out 
points. 
BUM traffic forwarded using 
a shared, non-SP tree and 
replicated at fork-out points.
Bandwidth efficiency 
Low 
High 
High 
Resource efficiency 
High
Low
Medium 
Congruency 
Yes 
Yes 
No 
Suggested use 
•	 Low multicast bandwidth
•	 Many sources and few 
receivers*
•	 High multicast bandwidth
•	 Few sources and many receivers
•	 When root bridge is 
source or receiver of 
most multicast traffic 
and congruency is not 
required
•	 When required to inter-
operate with third-party 
equipment
* When combined with IGMP Snooping.
8.  Creating an SPB backbone
In this section, we provide a sample SPB Backbone configuration and refer to figure 16 as 
a sample topology. We will continue using this sample topology throughout the rest of this 
document. Nodes BEB-1 through BEB-4 are called “BEB” nodes because we will add services 
to these nodes later. Node BCB will remain a pure transit node and not terminate any service.
If you observe this topology, you will notice that it provides up to 3 shortest paths, for example, 
between nodes BEB-1 and BEB-3, or between nodes BEB-2 and BEB-4. To take advantage of 
those 3 diverse paths for traffic load balancing, we need to create a minimum of 3 BVLANs. In 
this example, we will however, dedicate one BVLAN purely for control traffic and therefore we 
will create a total of 4 BVLANs. However, it should be noted that this is not strictly necessary, 
the control BVLAN can also be used for services.
Backbone configuration entails the following tasks:
•	 Creating one or more BVLANs with their associated ECT-IDs. ECT-IDs need not be explicitly 
defined, default ECT-IDs are applied
•	 Defining the control BVLAN
•	 Defining one or more SPB IS-IS interfaces
•	 Enabling the SPB IS-IS protocol

<<<PAGE 17>>>
17
Tech Brief
Shortest Path Bridging Architecture guide
Figure 16. Sample backbone topology
BEB3
BCB
BEB1
BEB2
1/1/50A
1/1/50A
1/1/50A
1/1/49A
1/1/49A
1/1/49A
1/1/49A
1/1/49A
1/1/52A
1/1/50A
1/1/54A
1/1/53A
1/1/54A
1/1/49A
1/1/54A
1/1/54A
BEB4
 
Following are the configuration snippets for all nodes.
Snippet 1. BEB-1’s backbone configuration
 
Snippet 2. BEB-2’s backbone configuration
 
Snippet 3. BEB-3’s backbone configuration
 
Snippet 4. BEB-4’s backbone configuration
 

<<<PAGE 18>>>
18
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 5. BCB backbone configuration
 
Through this configuration, VLANs 4000 through 4003 are defined as SPB backbone VLANs and 
will therefore not use any form of spanning tree protocol. AOS automatically assigns a different 
ECT-ID to each BVLAN and this maximises the chance that different BVLANs will create different 
SPTs, up to the maximum number of shortest paths supported by the physical topology. Nodes 
will exchange IS-IS “Hello” messages over the control BVLAN (such as, 4000 in this example) and 
form point-to-point adjacencies. LSPs are exchanged, a topology database is created and one SPT 
is built for each BVLAN. 
Let’s review this configuration with some show commands.
Snippet 6. “show SPB isis interface”
 
In the “show spb isis interface” command output we can observe three interfaces are SPB-IS-
IS enabled for L1 adjacencies. All three interfaces are both administratively and operationally 
up. By default, the link metric is 10 regardless of link speed. “Hello” messages are sent at nine 
second intervals and adjacencies are declared lost if no “Hello” message is received for three 
consecutive intervals (for example; 27 seconds).
Snippet 7. “show SPB isis nodes”
 
In the “show spb isis nodes” command output we can observe all discovered SPB IS-IS nodes 
including the local node. For each node, we can see the system or host name, the system ID 
(the BMAC), as well as the source ID and the bridge priority. The source ID is a 20-bit identifier 
which designates the node as the origin of BUM traffic and is derived from the system ID’s least 
significant bytes. The source ID is relevant when using tandem BUM replication. The bridge 
priority is 16-bit identifier and is used as a tie breaker during path computation.

<<<PAGE 19>>>
19
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 8. “show SPB isis adjacency”
 
In the “show spb isis adjacency” command output we can observe all SPB IS-IS adjacencies 
established by the local node. For each adjacency, we can see the system or host name,  
the system ID (the BMAC), as well as type (always L1 for SPB IS-IS), the state, the hold timer  
(number of seconds until the adjacency is declared lost if no “Hello” messages are received)  
and the interface over which the adjacency is formed. 
Snippet 9. “show SPB isis bvlans”
 
In the “show spb isis bvlans” command output we can observe, for each configured BVLAN, the 
ECT algorithm in use and whether the BVLAN is in use and has services mapped to it. So far, we 
have not configured any service, therefore the only BVLAN in use is the control BVLAN, which is 
used for IS-IS CP messaging. We can also observe the number of ISIDs mapped to the BVLAN. For 
services using tandem BUM replication, we can observe whether this is (S,G), which is the default, 
or (*,G). Note that while the choice of head-end versus tandem replication is done on a per-service 
basis, the choice between (S,G) and (*,G) tandem replication is done on a per-BVLAN basis. Lastly, 
the root bridge BMAC is shown only for those BVLANs using (*,G) tandem replication.
Snippet 10. “show SPB isis unicast-table”
 

<<<PAGE 20>>>
20
Tech Brief
Shortest Path Bridging Architecture guide
In the “show spb isis unicast-table” command output we can observe, for each node, the 
outbound interface used when sending unicast traffic to that node. Note that the outbound 
interface can be different for different BVLANs because different BVLANs can build different 
SPTs. For example, the path to BEB-3 goes through interface 1/1/49A in the case of BVLAN 
4000, interface 1/1/54A in the case of BVLANs 40001 and 4002, and interface 1/1/50A in the 
case of BVLAN 4003.
Snippet 11. “show SPB isis spf bvlan”
 
In the “show spb isis spb bvlan” command output we can observe, for a given BVLAN, the 
outbound interface, the next hop node, as well as the SPB metric and total number of hops 
required to reach a destination node. We can observe in this output that traffic destined towards 
BEB-3 will transit BEB-2 in the case of BVLAN 4000, BCB in the case of BVLANs 4001 and 4002, 
and BEB-4 in the case of BVLAN 4003.
9.  L2 services
A L2 service refers to a type of VPN service connecting multiple sites in a single any-to-any 
bridging domain. In this section, we continue building upon the previous example and create a 
L2 service on top of the previously created backbone configuration.
Services need only be created on BEBs, not on BCBs, and only on those BEBs where the service 
needs to be delivered. Creating an SPB service entails the following tasks:
•	 Creating a service and associating the service to an IS-IS and BVLAN – the specified BVLAN’s 
SPF will be used for the service traffic
•	 Defining a Service Access Port (SAP)
•	 Defining SAPs matching specific customer traffic

<<<PAGE 21>>>
21
Tech Brief
Shortest Path Bridging Architecture guide
Figure 17. L2 service
BEB3
BEB1
Site 2
Site 1
Site 3
Site 4
1/1/48
1/1/48
1/1/48
1/1/48
1/1/54A
BEB4
BEB2
ISID 1001
BVLAN 4001
 
With regard to figure 17, we provide BEB configurations in the snippets that follow.  
As well, please note:
•	 The service number is only locally significant and can differ across different BEBs
•	 The ISID number is globally significant and must match across all BEBs connecting  
a given service
•	 The BVLAN that the service is mapped must also match across all BEBs connecting  
a given service
•	 Different services can be mapped to different BVLANs to achieve traffic load balancing
Snippet 12. BEB-1’s service configuration
 
Snippet 13. BEB-2’s service configuration
 
Snippet 14. BEB-3’s service configuration
 
Snippet 15. BEB-4’s service configuration
 

<<<PAGE 22>>>
22
Tech Brief
Shortest Path Bridging Architecture guide
In the four configuration snippets above we can observe the following:
•	 Service 1 is associated to ISID 1001 and mapped to BVLAN 4001’s SPF tree
•	 Port 1/1/48 is defined as a SAP
•	 A SAP is defined on port 1/1/48 mapping untagged traffic (:0) to service 1
Let’s now proceed to verify the service status.
Snippet 16. “show service spb” – BEB view
 
In the “show service spb” command output we can observe, for a given BEB, the locally defined 
SPB services, their administrative and operational status, the number of (local) SAPs and (remote) 
SDPs along with the ISID and BVLAN number that the service is mapped to. We can also observe 
the multicast replication mode, which is head-end by default. The multicast replication mode can 
be changed to tandem on a per-service basis.
Snippet 17. “show service spb” – BCB view
 
In the “show service spb” command output we can observe that, by definition, a BCB does not 
have locally defined services.
Snippet 18. “show spb isis services” – BEB view
 
In the “show spb isis services” command output we can observe SPB services known to the node 
along with their ISID and BVLAN number and the node name, and BMACs that the service is 
enabled on. We should note that these services are learnt thanks to the IS-IS CP. A “*” denotes 
that the service also matches a service locally created on the BEB.

<<<PAGE 23>>>
23
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 19. “show spb isis services” – BCB view
 
In the “show spb isis services” command output we can observe the same output now from the 
perspective of a BCB. We should note that a BCB is still aware of all existing services with the 
IS-IS CP.
Snippet 20. “show service spb”
 
The “show service spb” command output provides some additional details about a given SPB 
service. We can highlight the following:
•	 RemoveIngressTag: As explained in section 3, by default, a PBB frame includes all the frame’s 
original tags. However, we can choose to remove those tags with the “service service_id 
remove-ingress-tag enable” command.
•	 VLAN Translation: A given service may require different encapsulations on different SAPs. 
For instance, a server may tag traffic with a specific VLAN while client devices may require 
untagged SAPs. In such situation, VLAN translation can be enabled to allow both devices  
to communicate. We should note that VLAN translation must be enabled both at service  
level with the command “service service_id vlan-translation enable” and on the SAP with  
the command “service access port vlan-xlation enable”.
•	 Allocation Type: Services can be either statically or dynamically created. We will cover 
dynamic service creation in section 13.3.
Snippet 21. “show service access”
 

<<<PAGE 24>>>
24
Tech Brief
Shortest Path Bridging Architecture guide
In the “show service access” command output we can observe, for a given BEB, the list of SAPs 
along with their type (manual or dynamic), the number of defined SAPs and whether VLAN 
translation is enabled or not. We will cover dynamic SAP creation in section 12.2. We can also 
observe the L2Profile assigned to the SAP. The L2Profile defines how L2 control protocol frames 
received on a SAP will be handled. Traffic can be peered, dropped, or tunnelled. Default L2 
profile settings are shown in Table 2. Additional L2 profiles can be created with the command 
“service l2profile name stp action 802.1x action 802.3ad action mvrp action gvrp action amap 
action 802.1ab action” and assigned to the SAP with the command “service access l2profile 
name”. We will cover unp SAPs and profiles in section 12.2.
Table 2. Default L2 profiles
Protocol
def-access-profile
unp-def-access-profile
STP
tunnel
drop
802.1x
drop
peer
802.3ad
peer
peer
MVRP
tunnel
tunnel
GVRP
tunnel
tunnel
AMAP
drop
drop
802.1ab
drop
drop
Snippet 22. “show service spb ports”
 
In the “show service spb ports” command output, we can observe local (SAP) as well remote 
(SDP) ports for a given service. For each port, we can see administrative and operational status, 
the system ID (BMAC) and BVLAN, as well as the system name and associated local interface. SDP 
ports will always display a “*” next to them because SDP ports are always dynamically created 
by the IS-IS CP. The name of an SDP is a combination of a dynamically generated number, 
followed by a colon and the service number.

<<<PAGE 25>>>
25
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 23. “show service mesh-sdp spb”
In the “show service mesh-sdp spb” command output we can observe far-end SDPs for each 
service along with the ISID number and the far-end system ID (BMAC), BVLAN, system name  
and associated interface.
Snippet 24. “show mac-learning domain spb” – BEB view
 
In the “show mac-learning domain spb” command output we can observe the list of CMAC 
addresses learnt in the SPB domain along with the service number and ISID, as well as the 
interface (SAP or SDP) port that the CMAC address is bound to. 
Snippet 25. “show mac-learning domain spb” – BCB view
 
In the “show mac-learning domain spb” command output we can observe the same output now 
from the point of view of a BCB node. As expected, BCB nodes do not learn any CMACs.

<<<PAGE 26>>>
26
Tech Brief
Shortest Path Bridging Architecture guide
10.  Routing concepts
Before delving into L3 services, which are covered in the next section, we need to discuss certain 
routing concepts in relation to SPB. The Alcatel-Lucent OmniSwitch® product line has supported 
SPB since AOS 7.3.1, released in 2012. Since then, multiple SPB-enabled platforms have been 
launched and each new platform incorporated new advancements in ASICs. 
First generation ASICs were not capable of routing and performing MAC-in-MAC encapsulation in 
a single-pass operation. Consequently, routing between IP interfaces associated to two different 
SPB services, or to a VLAN and an SPB service, had to traverse the switch fabric twice. This 
required an external physical loopback connecting two different switch ports: one port in the 
VLAN domain and another SAP in the SPB domain. IP interfaces could only be associated to a 
VLAN, not directly to an SPB service. It should be noted that these physical loopbacks can be 
either physical ports or linkaggs. When using VC, linkagg member ports can span different units 
in the VC for redundancy. We refer to this as two-pass routing with external physical loopback.
Newer generation ASICs support a concept similar to an external physical loopback without 
requiring a cable connection. One or more physical ports’ bandwidth is dedicated to the 
loopback function without requiring a cable to be attached. Multiple ports can be dedicated to 
this function for additional bandwidth and redundancy. When using multiple ports, ports are 
configured as a linkagg and, when using VC, linkagg member ports can span different units in 
the VC. We refer to this as two-pass routing with internal front-panel loopback. One additional 
difference between the internal front-panel loopback and the external physical loopback 
described in the previous paragraph is that the internal front-panel loopback is a single logical 
port, not two ports (a VLAN port and a SAP) as in the case of the external physical loopback. 
However, even in the single logical port, there is a “VLAN” function and a “SAP” function. This  
will become clearer when looking at the configuration snippets later in this section.
Latest generation ASICs support integrated routing and bridging in the SPB domain in the exact 
same manner as in the VLAN domain. This means that IP interfaces can be associated to an  
SPB service directly and traffic can be routed between two SPB services or between a VLAN 
and an SPB service in a single-pass operation without loopbacks. We refer to this as single-pass 
inline routing.
Figure 18. Routing options – Physical view
Single-pass
or inline
Two-pass with external
physical loopback
ISID 1
VLAN 1
ISID 2
VLAN 11
VLAN 1
VLAN port
1/1/1
SAP port
1/1/2
VLAN + SAP
all in one
port or LAG
ISID 1
Two-pass with internal
physical loopback
VLAN 11
VLAN 1
ISID 1
 
Figure 18 provides a physical view of these routing options. The leftmost diagram represents a 
switch supporting single-pass inline routing. This example shows a bridge with 2 SPB services, 
designated by their ISIDs, and one VLAN. IP interfaces are represented by dots. As we can see, 
the IP interfaces are bound to either VLANs or services and the switch performs inter-VLAN, 
inter-Service or inter-VLAN-Service routing directly in a single operation. 

<<<PAGE 27>>>
27
Tech Brief
Shortest Path Bridging Architecture guide
The diagram in the middle illustrates the case of two-pass routing with a physical hairpin. In this 
diagram, you can observe that IP interfaces are bound to VLAN 1 and VLAN 11, but not directly 
to the service. The external physical loopback cable creates the link between the service and the 
“dummy” VLAN, VLAN 11 in this example, where the IP interface resides. This external physical 
loopback is configured with a SAP-side, where SAPs are defined for each service requiring 
routing, and a VLAN-side, where dummy VLANs mapping to those services are tagged. 
The right diagram illustrates the case of two-pass routing with internal front-panel loopback. 
In this diagram, the dotted line represents an imaginary physical external loopback, which is 
not required. In addition to not requiring an external physical loopback cable, the front-panel 
loopback requires a minimum of one port only. CLI configuration is different between physical 
external loopback and front-panel internal loopback. However, the concepts are very similar.  
You should still think about the front-panel internal loopback port or ports as having a SAP 
function and a VLAN function all in one port or linkagg.
Figure 19. Routing Options - Logical view
Single-pass
or inline
Two-pass with external
physical loopback
ISID 1
VLAN 1
ISID 2
VLAN 1
VLAN 1
VLAN 11
VLAN port
SAP port
VLAN + SAP
all in one port
ISID 1
Two-pass with internal
physical loopback
VLAN 1
ISID 1
VLAN 1
VLAN 11
 
Figure 19 provides a logical representation of these options. The left diagram represents the 
case of single-pass or inline routing. In these products, routing and bridging functions are fully 
integrated in the service domain in the exact same manner as they are integrated in the VLAN 
domain. For this reason, these products are represented with a router icon. 
The diagram in the middle represents the case of two-pass routing with an external physical 
loopback. In these products, routing and bridging functions are separate and represented by 
router and bridge icons. You can observe that the router function, where dots representing IP 
interfaces exist, connects to the bridge function using a VLAN port and a SAP. 
The right diagram illustrates the case of two-pass routing with internal front-panel loopback. 
As you can see, this case is almost the same to the case of two-pass routing with an external 
physical loopback from a logical standpoint. However, the routing function attaches to the 
bridging function using a single port or group of ports. This front-panel loopback port or group 
of ports still performs a SAP function and a VLAN function. In addition, this connection between 
routing and bridging functions is created internally in the switch ASIC and does not require an 
external cable.
Let’s review some configuration examples to commit these concepts.
Snippet 26. Single-pass or inline routing example
 

<<<PAGE 28>>>
28
Tech Brief
Shortest Path Bridging Architecture guide
The configuration snippet 26 shows that, in products supporting single-pass or inline routing, 
IP interfaces can be bound to services just like they can be bound to VLANs. The switch simply 
performs routing in the same domain (VLAN or Service) or between different domains (VLAN  
and Service). Note that the backbone and service configuration is not shown in this example.
Snippet 27. Two-pass routing with external physical loopback example
 
The configuration snippet 27 shows the equivalent configuration for products supporting two-
pass routing with external physical loopback. Since IP interfaces cannot be bound to a service 
directly, we create 2 additional “dummy” VLANs to bind these interfaces to. VLAN 11 will be 
associated to service 1 and VLAN 12 will be associated to service 2. The external physical 
loopback uses port 1/1/1 as VLAN port and port 1/1/2 as SAP. When creating the IP interfaces 
bound to those dummy VLANs, we use the rtr-port option. This prevents those VLANs from 
being bound to other ports and disables STP on those VLANs. Note that as explained previously, 
linkaggs can be used instead of single ports and linkagg member ports can span diverse units in 
a VC for redundancy.
Snippet 28. Two-pass routing with internal front-panel loopback example
 
The configuration snippet 28 shows the equivalent configuration for products supporting two-
pass routing with internal front-panel loopback. Firstly, port 1/1/51A is designated as the front-
panel loopback port. Dummy VLANs are created and SAPs linking those dummy VLANs to their 
associated services are defined on the loopback port. When creating the IP interfaces bound 
to the dummy VLANs, we use the rtr-port option and reference the loopback port. Once again, 
the example shows the case of single front-panel loopback port but linkaggs can be used for 
additional bandwidth and resiliency in the case of VC.

<<<PAGE 29>>>
29
Tech Brief
Shortest Path Bridging Architecture guide
11.  L3 services
A L3 service refers to a type of VPN service connecting multiple sites in a single any-to-any 
routing domain. Different sites utilize different subnets and require routing to communicate. 
For multi-tenancy, and to keep different customers isolated at L3, each customer service is 
associated to its own VRF instance.
Figure 20. Customer A’s L3 service
BEB1
BEB2
Site 1
10.0.1.0/24
.254
10.0.0.0/24
SPB Service A
VRF A
.254
.2
.1
Site 2
10.0.2.0/24
BEB3
BEB4
Site 3
10.0.3.0/24
.254
.254
.4
.3
Site 4
10.0.4.0/24
 
Figure 20 illustrates an example of a L3 Service connecting four of customer A’s sites: Sites 1 through 
4. You will notice that each site uses a different subnet and therefore, inter-site routing is required. 
BEB nodes connecting customer sites are represented with router icons for simplicity. These BEBs 
have a “LAN”-facing interface which acts as the local site default gateway, as well as a “WAN”-facing 
interface to reach remote sites. All “WAN” interfaces are bound to a single SPB service and are on the 
same “WAN” subnet. Lastly, all the LAN and WAN IP interfaces associated to customer A are bound  
to the same customer A VRF to provide L3 isolation between different customers.
SPB-based L3 VPN services rely on edge routing: Routing is only performed at ingress and egress 
BEBs and bridged between these. At L3, the WAN represents a single L3 hop regardless of the 
number of intermediate L2 hops (BCBs) in between. SPB simply bridges traffic from ingress BEB 
to egress BEB along the shortest path.
Up to this point, we have only described the DP. What about the CP? At the CP level, L3 VPN 
services come in two variants: VPN Lite and L3 VPN. Let’s elaborate on these two variants.
11.1  VPN Lite
A VPN Lite L3 Service is created by overlaying a L3 routing protocol on top of the L2 WAN SPB 
service. This routing protocol can be OSPF, BGP, or even static routing. The routing protocol runs 
inside the customer’s VRF and a separate instance and associated configuration is created for 
each customer. Figure 21 shows an example of how customer A’s L3 service can be created  
as a VPN Lite service by running OSPF on BEB nodes.
Figure 21. Customer A’s VPN Lite service
BEB1
BEB2
Site 1
10.0.1.0/24
.254
SPB Service A
VRF A
OSPF area 0
10.0.0.0/24
.254
.2
.1
Site 2
10.0.2.0/24
BEB3
BEB4
Site 3
10.0.3.0/24
.254
.254
.4
.3
Site 4
10.0.4.0/24

<<<PAGE 30>>>
30
Tech Brief
Shortest Path Bridging Architecture guide
We should highlight that, in a VPN Lite type of L3 service, the L2 SPB service simply provides 
L2 connectivity to the “WAN” IP interfaces. Continuing with OSPF as an example, this means that 
OSPF is configured as usual. Also, since all WAN IP interfaces are connected to a single L2 SPB 
service, in the case of OSPF, a DR/BDR election will take place as usual.
11.2  L3 VPN
SPB L3 VPN leverages the existing SPB IS-IS instance to carry customer VPN routes without 
requiring an additional routing protocol such as OSPF. This is accomplished with additional  
IS-IS TLVs extensions. We should note that each customer or tenant is still associated to its  
own VRF and IS-IS TLVs reference the customer’s ISID to preserve L3 isolation between different 
customers or tenants. This mechanism is described in an IETF draft [1]. Refer to figure 22.
For those familiar with MPLS or EVPN, those technologies rely on an IGP (for example; OSPF or 
IS-IS) for backbone node reachability, and MP-BGP (RFC 4760) for customer VPN route transport. 
In SPB L3 VPN, IS-IS can play both of those roles; backbone node reachability and customer VPN 
route transport. Using a single protocol instead of two, results in a network that is simpler to 
deploy and operate. 
In addition, when comparing SPB and MPLS, SPB BEB nodes play a role similar to MPLS PE nodes 
while SPB BCB nodes are similar to MPLS P nodes. In particular, SPB BCB nodes do not learn any 
customer VPN routes and require no VRFs to be created on them. VRFs need only be created on 
BEB nodes and customer VPN routes are only learnt on the BEBs that those customers connect to.
Figure 22. Customer A’s L3 VPN service
BEB1
BEB2
Site 1
10.0.1.0/24
.254
SPB Service A
VRF A
SPB IS-IS
10.0.0.0/24
.254
.2
.1
Site 2
10.0.2.0/24
BEB3
BEB4
Site 3
10.0.3.0/24
.254
.254
.4
.3
Site 4
10.0.4.0/24
 
Unlike the case of a VPN Lite, an SPB L3 VPN does not require the addition of any routing 
protocol. Customer’s VRF routes are exported to the SPB IS-IS instance, associated to the 
customer’s ISID, and bound to the WAN IP as a gateway address. Far-end BEBs will import those 
routes into their local VRF routing table. Therefore, those routes will point to the WAN IP address 
as next-hop. We should note that this mechanism is applicable and identical for both IPv4 and 
IPv6. This is illustrated in figure 23 from the perspective of BEB-1. We should note that route-
maps can be used for fine-grained route filtering.
Figure 23. Route Import/Export
BEB1
Site 1
10.0.1.0/24
.254
SPB Service A
VRF A
SPB IS-IS
10.0.0.0/24
Export local customer VRF routes to SPB IS-IS,
associate to customer’s ISID and bind to WAN address
Import far-end SPB IS-IS routes associated with the customer’s ISID
into the customer’s VRF and set the far-end WAN IP address as next hop
.1
 

<<<PAGE 31>>>
31
Tech Brief
Shortest Path Bridging Architecture guide
A L3 VPN service builds upon a L2 service and involves the following steps:
•	 Creating an L2 SPB service
•	 Creating a tenant VRF
•	 Creating LAN-side and WAN-side IP interfaces on the tenant VRF. LAN-side IP interfaces 
normally reside on a VLAN. WAN-side IP interfaces can reside directly on the SPB services 
itself on products supporting single-pass inline routing, or on a “dummy” VLAN on products 
requiring external physical or internal front-panel loopback.
•	 Binding the WAN IP interface to the L2 SPB service’s ISID
•	 Route import/export between local VRF routing table and SPB IS-IS ISID instance
Let’s go back to the sample topology used for L2 services in section 9 and configure a L3 VPN 
service so we can have a look at the configuration. We will look at devices supporting internal 
front-panel loopback.
Figure 24. L3 VPN service example
BEB3
BEB1
ISID 1002
VRF A
BVLAN 4002
192.168.30.0/24
.254
.254
1/1/48
1/1/48
1/1/48
.3
.1
Site 3
192.168.23.0/24
10.0.2.0/24
Site 1
192.168.21.0/24
BEB4
BEB2
.254
.4
.2
1/1/48
.254
Site 4
192.168.24.0/24
Site 2
192.168.22.0/24
 
We will now provide configuration snippets for all BEBs. Like their L2 counterpart, L3 VPN 
services require no configuration on BCBs. Let’s provide some details about this example:
•	 Customer sites connect to their local BEB though interface 1/1/48
•	 LAN-side, or site default-gateway IP interfaces are bound to VLAN 3001, which is the default 
VLAN on port 1/1/48
•	 Port 1/1/54A is designated as a loopback port
•	 WAN-side IP interfaces are bound to dummy VLAN 3100

<<<PAGE 32>>>
32
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 29. L3 VPN example – BEB-1
 
Snippet 30. L3 VPN example – BEB-2
 
Snippet 31. L3 VPN example – BEB-3
 

<<<PAGE 33>>>
33
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 32. L3 VPN example – BEB-4
 
Having created the L3 VPN service on all nodes, we can now proceed to verify it with show 
commands. Let’s start by verifying correct route import and export. Snippet 33 shows routes in  
BEB-1’s VRF “Customer_A”. Both local LAN and WAN subnets are LOCAL routes while far-end LAN 
subnets are IMPORT routes whose next hop gateway address is the WAN address of the remote BEB.
Snippet 33. L3 VPN example – Verifying route import/export
 
Snippet 34 shows arp entries in BEB-1’s VRF “Customer_A”. Far-end WAN gateway addresses are 
dynamically learnt.
Snippet 34. L3 VPN example – Verifying gateway L2 reachability
 
In addition to these L3-related verification steps, all steps covered in section 9 can be used to 
verify the underlying L2 service. 

<<<PAGE 34>>>
34
Tech Brief
Shortest Path Bridging Architecture guide
11.3  VPN Lite versus L3 VPN
Having presented VPN Lite and L3 VPN, we can now discuss the pros and cons and provide 
guidelines to help you choose one versus the other.
Let’s start with the advantages of L3 VPN:
•	 Simplicity: L3 VPN does not require routing protocol configuration as it simply leverages the 
existing SPB IS-IS instance. VPN Lite on the other hand requires one routing protocol instance 
per tenant/VRF and BEB. For example, if using OSPF, 4 customer services spanning 8 BEB 
nodes require 4 x OSPF instances per node: A total of 32 x OSPF configurations across all 
nodes. In case dual stack IPv4 and IPv6 support is required, this translates to an OSPFv2 and 
an OSPFv3 instance per BEB and VRF: A total of 64 x OSPF configurations all nodes included. 
More routing protocol configurations result in longer service provisioning times and increased 
chances of making mistakes.
•	 Scalability: L3 VPN is significantly more efficient than VPN Lite from a CP point of view as it 
uses a single routing instance. This results in lighter CP load and allows for greater scalability 
than VPN Lite.
•	 Convergence: L3 VPN convergence can be faster than VPN Lite because it relies on a single 
protocol. VPN Lite convergence can be slower because the stacking of routing protocols has  
a compounding effect over convergence time: IS-IS must converge before OSPF can converge.
With such compelling arguments in favour of L3 VPN, you may wonder why anyone would 
choose to use VPN Lite instead. The reason is that, while L3 VPN is the recommended option 
within the SPB domain, L3 VPN relies on SPB IS-IS and cannot directly interoperate with external 
networks. This is where VPN Lite comes in. VPN Lite can be configured on border BEB nodes 
linking the SPB domain to external, non-SPB capable networks. These border BEB nodes use L3 
VPN to communicate with other BEB nodes and VPN Lite to interoperate with external non-SPB 
nodes through common routing protocols such as OSPF or BGPv4.
In short, L3 VPN is recommended within the SPB domain and VPN Lite is needed only on border 
nodes connecting to the outside world.
12.  Shared Services VPN and Route Leaking
In L3 VPN designs in which each VPN maps to its own VRF, it is common for certain services 
such as DHCP, DNS and Internet access to be shared across two or more of those VPNs. This  
can be implemented through VRF leaking.
Figure 25 shows the same familiar diagram that we have been using so far, but now with two 
customers, A and B. Each customer is associated to its own ISID (1002 for Customer A and  
1003 for Customer B) and VRF (Customer_A and Customer_B) on BEBs 1 through 4. Routes  
are propagated across the backbone as explained in section 11.2. 
Let’s now imagine that these customers need to also access some shared services and Internet 
access. An additional L3_VPN is created on BEB1 and BEB2, the “border” BEBs. These are 
the nodes that those shared services are accessed through. The “shared_services” L3VPN is 
associated to its own ISID (1004) and VRF (shared_services). Note that this L3VPN need not  
be stretched to BEBs 2 and 4. 
BEB1 and BEB2 can exchange routes with external entities, such as the firewalls, using a 
standard protocol, such as BGP4. Those routes can be leaked to customer A’s and B’s VRFs. In 
turn, customer A’s and B’s VRF routes can be leaked to the “shared_services” VRF. As a pre-
requisite, customer A’s and B’s address space must not overlap with each other nor with the 
shared services.

<<<PAGE 35>>>
35
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 35. Route leaking
 
Snippet 35 provides the commands required to accomplish this on the border BEBs, BEB1  
and BEB2.
We can summarize the process as below:
•	 Shared routes are exported from the shared_services VRF and into the global IP routing table. 
When doing so, a route-map filters routes such that only external routes are exported. This is 
to prevent re-export of routes imported from the other border BEB.
•	 Shared routes are imported from the global IP routing table and into the customer VRFs. Note 
that this step is only necessary if customer sites are connected to the border BEBs.
•	 Customer routes are imported from the global IP routing table and into the shared_services 
VRF. Note that this step is only necessary if customer sites are connected to the border BEBs.
•	 Remote customer routes are imported from the SPB IS-IS instance and ISID associated to those 
customers and into the shared_services VRF.
•	 Shared routes are redistributed from the shared_services VRF to the SPB IS-IS instance and 
ISIDs associated to customers. These routes will then be propagated across the backbone and 
imported into customer VRFs at remote BEBs.
Figure 25. Shared services
BEB3
SPB
IS-IS
BEB4
BEB1
Customer A
Site 3
Customer A
Site 4
Customer B
Site 3
Customer B
Site 4
Customer A
Site 2
Customer B
Site 2
Customer A
Site 1
Customer B
Site 1
BEB2
 

<<<PAGE 36>>>
36
Tech Brief
Shortest Path Bridging Architecture guide
13.  Automation
Up to this point, we have explained SPB concepts and configured the SPB backbone and 
services manually. However, AOS incorporates features that can build both the SPB backbone 
and services automatically. In this section, we will explain the various mechanisms that make a 
near zero-touch SPB network possible. A factory-default Alcatel-Lucent OmniSwitch has these 
mechanisms enabled by default and will automatically attempt to create an SPB backbone 
and services as explained in the subsequent subsections, unless these automation features are 
explicitly disabled. This set of features is sometimes referred to as “Intelligent Fabric” or “iFab” 
for short. In this section, we provide a simplified, high-level overview of these features. For a 
detailed description, please refer to the Alcatel-Lucent OmniSwitch Switch Management Guide.
13.1  Auto-Fabric
Figure 26 is a simplified view of a factory-default OmniSwitch bootup process. For a more 
detailed flow chart, please refer to the Alcatel-Lucent OmniSwitch Switch Management Guide.
This process involves the following stages:
•	 Auto Virtual Chassis (VC)
•	 Auto Remote Configuration Download (RCD)
•	 Auto LACP
•	 Auto SPB
•	 Auto MVRP
•	 Auto IP
Auto-Fabric features are enabled by default on a factory-default OmniSwitch. These features 
can however be disabled in their entirety, or, on a per-protocol or per-port basis. By default, 
automatically learnt and created configuration is not saved to the vcboot.cfg file but this option 
can be enabled.
Figure 26. Bootup state diagram
Fails or
succeeds with
AF enabled
As soon as IP
interface is up
if AF is enabled
Succeeds
with AF
disabled
Auto-RCD
Auto-IP
Auto-SPB
Auto-LACP
Auto-MVRP
Auto-VC
Link ﬂap
STOP
 
Let’s describe these stages one-by-one. 
13.1.2  Auto-VC
On bootup, and in absence of the vcsetup.cfg file, an OmniSwitch uses LLDP to detect other 
VC-compatible nodes connected to the default auto-VFL ports. Default auto-VFL ports depend 
on the product family. Some families such as the Alcatel-Lucent OmniSwitch® 6860 Stackable 
LAN Switch have 2 designated VFL ports which default to this role. In other families such as 
the Alcatel-Lucent OmniSwitch® 6900 Stackable LAN Switch, which support VC of up to 6 units, 
the last 5 VFL-eligible ports default to auto-VFL ports. If other products in the same family are 
detected at the other end, they will attempt to automatically create a VC. A Master node will 
be chosen through an election mechanism and non-Master nodes will reboot. Since this process 
creates a vcsetup.cfg file on all involved nodes, auto-VC will not kick-in in subsequent node 
reboot events.

<<<PAGE 37>>>
37
Tech Brief
Shortest Path Bridging Architecture guide
13.1.3  Auto-RCD
Next, and in absence of a vcboot.cfg file, an OmniSwitch attempts to obtain an IP address 
through DHCP on any of its operational non-VFL ports. It will try this using the untagged default 
VLAN and tagged VLAN 127 and it will retry three times. If the switch succeeds in obtaining 
an IP address, and depending on the DHCP options in the lease, the switch will subsequently 
attempt to fetch an instruction file from a TFTP server or it will contact the Alcatel-Lucent 
OmniVista® 2500 Network Management System. Next, the switch will attempt to download 
firmware and vcboot.cfg from either an FTP/SFTP server or OmniVista. If the switch succeeds  
at obtaining its firmware and configuration, it will reboot and load its configuration. Depending 
on the configured options, the switch may or may not continue with the subsequent stages. 
Please refer to the AOS Switch Management Guide and to [2] for further details.
13.1.4  Auto-LACP
All non-VFL ports are auto-LACP enabled by default. Auto-LACP kicks in on a factory-default 
switch or a non-factory-default switch, unless explicitly disabled. Auto-LACP can be disabled 
globally or only on specific ports.
During the auto-LACP stage, a switch uses LLDP to identify switches connected to auto-
LACP-enabled ports. Any LACP-compatible ports linking the same pair of switches will be 
automatically added to a linkagg. Even if there is only a single link connecting two nodes, it 
will still be configured as a linkagg because this allows additional links to be added later on 
without requiring configuration changes. For instance, by creating a linkagg of 1 member port 
and by referencing the (logical) linkagg as opposed to the (physical) port in other configuration 
commands, those configuration commands do not need to change when additional member  
ports are added to the linkagg. This is a best practice.
Note that, even if the remote switch is not an OmniSwitch, but is (manually) configured for LACP, 
the OmniSwitch detects LACP PDUs and automatically configures its side of the linkagg. This 
simplifies deployment even when 3rd party switches are used.
13.1.5  Auto-SPB
All non-VFL ports and linkaggs are auto-SPB enabled by default. Auto-SPB kicks in on a factory-
default switch or a non-factory-default switch, unless explicitly disabled. Auto-SPB can be 
disabled globally or only on specific ports or linkaggs.
Auto-SPB also uses LLDP to detect presence of SPB-capable switches. When an SPB-capable 
switch is detected, the switch will attempt to configure the port or linkagg as an SPB backbone 
interface. When doing so it will use certain defaults.
On switches running AOS release 8.7R1 and later these defaults are:
•	 BVLANs 4000 through 4003 are created and mapped to ECT IDs 1 through 4 respectively
•	 BVLAN 4000 is designated as the control BVLAN
If the switch succeeds in establishing at least one SPB adjacency, all remaining non-VFL and 
non-SPB backbone ports are automatically configured as auto UNP access ports, unless explicitly 
disabled. Please refer to section 13.3 for details on auto UNP access ports.
13.1.6  Auto-MVRP
Auto-MVRP is enabled on factory-default switches. On switches booting from a vcboot.cfg 
file however, this feature needs to be explicitly enabled. When auto-MVRP is enabled, and 
if the switch fails to establish any SPB adjacency, MVRP will be enabled on all remaining 
and operational non-VFL ports. This enables the dynamic instantiation of VLANs learnt from 
neighbouring switches.

<<<PAGE 38>>>
38
Tech Brief
Shortest Path Bridging Architecture guide
13.1.7  Auto-IP
The Auto-IP features runs in parallel with other features described in this section and, when 
enabled, it kicks-in as soon as an IP interface is created. Auto-IP listens for routing protocol 
(OSPFv2, OSPFv3 or IS-IS) “Hello” packets from neighbour devices and automatically creates local 
routing configuration matching parameters in the received “Hello” packets such that an adjacency 
can be formed. For example, reception of an OSPF “Hello” packet with area 1, Hello timer of  
5 and Dead timer of 20 will result in matching configuration on the local device such that the 
two devices become neighbours and an adjacency is established.
13.2  Dynamic SAPs
Up to this point, we have shown how to configure SAPs statically and manually. However, SAPs 
can be automatically and dynamically configured using the User Network Profile (UNP) feature  
in conjunction with authentication (802.1x, MAC) or classification rules (for example VLAN tag).
Dynamically-created SAPs can map traffic to a manually created service. Dynamically-created 
SAPs can also map traffic to a dynamically-created service for a fully dynamic configuration, 
which is covered in the next section.
Let’s analyse the sample configuration in snippet 36 . This example refers to the case of L2 
Services in which any required routing, such as default gateway, DHCP relay, is performed on a 
central node, which can be a switch or a Firewall. Either way, service and SAP configuration on 
the central L3 device is static. Dynamic configuration is useful at the edge nodes where client 
devices are added, moved, and changed on a regular basis.
Six UNP profiles named “EMPLOYEE”, “IoT”, “GUEST”, “WLAN”, “CCTV”, and “RESTRICTED” are 
created, each mapping to a different ISID. There are a total of four BVLANs, 4000 through 4003. 
BVLAN 4000 is reserved as control BVLAN and therefore services can be mapped to BVLANs 
4001 through 4003. As a result, each BVLAN carries traffic for two different services. These 
UNP profiles use head-end replication and have VLAN translation enabled; these are default 
behaviours which are explained elsewhere in this document.
So far, this describes the services but does not describe how ports or client devices will be 
mapped to those services. This mapping can be either static or dynamic. Let’s start by analysing 
the dynamic case. Ports 1/1/10 through 1/1/16 are defined as UNP “access” ports. This means 
that they map traffic to an SPB service, as opposed to a UNP “bridge” port which maps traffic to  
a VLAN. These ports utilise the “SAMPLE_FLOW” port template. This template is defined such that:
•	 802.1x supplicants are authenticated against the “UPAM” radius server. If successful, the 
radius server returns a “filter-id” attribute which matches one of the locally defined UNPs  
(for example; EMPLOYEE, IoT, among others). 
•	 As a fall-back mechanism for non-802.1x capable devices, such devices can use MAC 
authentication. If successful, the radius server also returns a “filter-id” attribute which  
matches one of the locally defined UNPs (for example; EMPLOYEE, IoT, among others).
•	 In both 802.1x or MAC authentication cases, it may happen that the radius server does not 
return a “filter-id” or that the returned “filter-id” value does not match any of the locally 
defined UNPs. In such case, those devices are bound to a “RESTRICTED” UNP. 
•	 The RESTRICTED UNP is also defined as the default UNP which is used in case of 
authentication failure. When bound to this RESTRICTED UNP, devices will receive an IP address 
through DHCP but will be very limited in their access to network resources. This is controlled 
at the central L3 node or firewall. This allows for these devices to have minimal network 
connectivity such that they can be onboarded (for example a digital certificate can be applied) 
and they can successfully authenticate next time they connect.
With this configuration in place, devices connected to ports 1/1/10 through 1/1/16 will be 
authenticated and dynamically bound to an SPB service according to their type or user identity. 
This means that the SPB service will automatically adapt and change as devices connect, 
disconnect, move, or otherwise change without manual intervention.

<<<PAGE 39>>>
39
Tech Brief
Shortest Path Bridging Architecture guide
In some cases, it may be necessary to statically bind these UNP services to a port. This is 
particularly useful if authentication is not used or when the device is a “silent” device. A “silent” 
device is a device that does not transmit traffic for extended periods of time because it goes into 
power-save mode for instance. These periods of inactivity can result in a loss of service binding, 
thus making the device effectively unreachable (for example for a WAKE-ON-LAN packet). This 
problem can be avoided by statically binding the UNP profile to the port. We have applied static 
UNP binding to ports 1/1/5 through 1/1/9 such that the service is statically bound to those ports 
even if the device disconnects or stops communicating for extended periods of time.
It should be noted that statically binding a SAP, as opposed to a UNP, also offers a solution to 
the silent device problem. However, by statically binding a UNP instead of a SAP, the exact 
same UNP constructs can be used for both silent and non-silent devices. This results in a more 
standardized configuration which is easier to create and maintain with fewer mistakes when 
configurations need to change. This is considered a best practice.
Snippet 36. Dynamic SAPs – L2 services
 

<<<PAGE 40>>>
40
Tech Brief
Shortest Path Bridging Architecture guide
Let’s analyse the L3 Service case for this example. What this means is that, rather than routing  
at a centralized switch or firewall, edge routing is performed. Furthermore, let’s consider the case 
of devices which attach to a standard VLAN port (for example not a SAP) and BEBs supporting 
front-end-panel loopback routing. Since VLAN-to-Service mapping happens at the loopback 
port, in this case we need to create bridge-type (VLAN) UNPs instead of access-type UNPs. 
The SPB configuration will be statically defined. Configuration snippets are split in three parts 
for convenience. Snippet 37 contains the VLAN-domain part of the configuration, snippet 38 
contains the IP-domain part of the configuration, and  snippet 39 contains the Service-domain 
part of the configuration. 
We should note that devices placed in the “RESTRICTED” role do not normally need to 
communicate with other such devices. However, the configuration snippet allows for all routes 
in the RESTRICTED VRF to be imported. This can be modified with the addition of a route-map 
permitting routes to a central BEB or firewall only. Furthermore, a policy list can be attached t 
o the RESTRICTED UNP definition such that those devices can only communicate with certain  
head-end resources and can only use certain ports or applications. We will leave this exercise  
for you to complete.
Snippet 37. Dynamic SAPs – L3 services – VLAN Domain
 

<<<PAGE 41>>>
41
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 38. Dynamic SAPs – L3 services – IP Domain
 
Snippet 39. Dynamic SAPs – L3 services – Service Domain
 

<<<PAGE 42>>>
42
Tech Brief
Shortest Path Bridging Architecture guide
13.3  Dynamic Services
In the preceding section, we explained how SAPs can be dynamically configured to accommodate 
mobile users and devices, and highly dynamic environments. This same mechanism is applicable 
to VMs in a data centre. As VMs are created, turned-on or off, or migrated from one hypervisor 
to another, SAPs can be automatically and dynamically created to adapt to those events on the 
fly without network manager intervention. 
For instance, classification rules can match VM traffic based on the VLAN tag (configured in the 
hypervisor) and create the required SAPs dynamically and automatically. This is a best practice 
compared to statically enabling all possible SAPs on all access ports because it reduces the 
broadcast domain footprint to only the required ports, thus eliminating unnecessary broadcast 
traffic and MAC learning.
However, with the features that we have described so far, even if the SAPs can dynamically 
adapt, this would require that the service UNP be manually created. In certain scenarios, the 
network administrator does not know the required parameters beforehand. For instance, the 
server manager may create, change, and delete VLANs on the hypervisor’s vswitch on a regular 
basis. It may be tempting to pre-provision services for all 4096 VLANs. But this is a poor practice 
as it creates an unnecessary load on the control plane. 
The best practice for that type of environment is to use AOS’ Dynamic Services feature. With 
Dynamic Services, UNPs can be dynamically created, on the fly, based on the VLAN tag seen on 
UNP ports. This feature is enabled by default on factory-default switches.
Upon receiving a frame on a UNP access port, the OmniSwitch automatically creates a dynamic 
SAP and a dynamic UNP profile defining the SPB service that traffic will be mapped to. Snippet 
40 provides an example of such a dynamically created UNP profile. The profile in the snippet is 
created upon reception of traffic tagged with VLAN 101. How does the AOS select the ISID and 
BVLAN to be used in the newly created service? It uses the formulas below where ‘%’ denotes 
the “modulo” division: the reminder of the integer division.
•	 ISID Number = Base Service Number + Domain ID + (VLAN Number % Service Modulo)
•	 BVLAN Index = ISID Number % (Total number of BVLANs)
By default:
•	 Base Service Number = 10,000,000
•	 Domain ID = 0
•	 Service Modulo = 512
Let’s also assume that BVLANs 4000-4003 are created and calculate the ISID and BVLAN  
number manually.
ISID Number = 10,000,000 + 0 + (101 % 512) = 10,000,000 + 101 = 10,000,101
BVLAN Index = 10,000,101 % 4 = 1
The formula does not provide the BVLAN number directly but the BVLAN index: the position  
in a BVLAN array sorted in ascending order where the lowest numbered BVLAN is in position 0  
and the highest numbered BVLAN is in position N-1. Therefore, in our example, with BVLANs 
4000-4003, BVLAN index 1 maps to BVLAN 4001. 
Snippet 40. Dynamic services – Dynamic UNP
 

<<<PAGE 43>>>
43
Tech Brief
Shortest Path Bridging Architecture guide
It is important to understand that with 4096 possible VLAN tags, using the default Service 
Modulo of 512 can result in up to 8 different VLAN tags being mapped to the same service. This 
is not the desired outcome most of the time because it will result in different VLAN traffic being 
bridged in the same L2 domain. To ensure L2 isolation, we can change the Service Modulo to 
4096 as shown in Snippet 41.
Snippet 41. Dynamic services – Dynamic UNP – Service Modulo
 
Let’s now focus on another parameter used in the ISID calculation formula: Domain ID. The 
Domain ID is useful in a multi-tenanted environment. For example, let’s consider a network 
providing services to three different customers: A, B, and C. These customers can use multiple 
VLANs and some of those VLANs may overlap. How do you ensure customer traffic isolation 
in the SPB domain? Isolation is achieved by creating a Domain ID for each customer and by 
the mapping customer’s UNI ports to the Domain. The example in Snippet 42 illustrates this 
configuration. Domains 1 through 3 are created for customers A through C. Ports 1/1/1-10 
connecting customer A’s devices are mapped to domain 1, ports 1/1/11-21 connecting customer 
B’s devices are mapped to domain 2, and so on. This configuration preserves customer isolation 
even when services and SAPs are dynamically and automatically configured on the fly in 
response to VLAN tags in incoming traffic.
Snippet 42. Dynamic services – Dynamic UNP – Multi-tenancy
 
Lastly, the Base Service Number (BSN) enables manual and dynamic service coexistence without 
conflict. Dynamically created services map to ISIDs greater than or equal to the BSN. Manually 
created services should use ISID numbers lower than the BSN.
14.  Management
As explained in section 3.6, SPB IS-IS is not an IP protocol. BCB nodes do not require IP 
interfaces. BEB nodes supporting L2 services only do not require IP interfaces either. BEB nodes 
require IP interfaces only when supporting an L3 service (for example, L3 VPN or VPN Lite). 
However, all SPB nodes whether BCB or BEB, require IP interfaces for management purposes. 
There are different ways of managing SPB nodes:
•	 Out of Band Management (OOBM): OOBM is applicable to any network architecture and will 
not be discussed further 
•	 Dedicated Management Service: An SPB service and VRF are dedicated to management. This 
is a good option if all nodes support single-pass inline routing. However, nodes that do not 
support single-pass inline routing will require an external physical or internal front-panel 
loopback for this purpose even if they would not require it otherwise (for example, because 
they are BCBs). 
•	 In-band Management: In-band management is applicable to all SPB nodes regardless of their 
routing capabilities (such as, single-pass inline, external physical, or internal front-panel 
loopback). Management IP interfaces can be created directly on the control BVLAN, therefore, 

<<<PAGE 44>>>
44
Tech Brief
Shortest Path Bridging Architecture guide
no loopback of any kind is required. The management network or stations attach to one or 
more gateway nodes through VLAN-domain interfaces. We should note that IP interfaces 
created on the control BVLAN do not support configuration of any routing protocol or function 
(for example, OSPF or VRRP) and do not rely on ARP for IP-to-MAC resolution because there 
are no broadcasts on the SPB domain. IP-to-MAC mapping is resolved through IS-IS TLVs. IS-IS 
TLVs also carry management routes through the SPB backbone. VLAN-domain and SPB-domain 
management routes can be cross-redistributed at gateways nodes. The “spb-mgmt” protocol is 
associated to SPB-domain management routes.
Figure 27. In-band management
BEB3
1/1/1
1/1/1
BVLAN 4000
172.16.1.0/24
SPB IS-IS
Management VRF
172.16.0.0/24
OSPF area 0
BCB
BEB4
BEB1
BEB2
 
Let’s examine the in-band management example in figure 27. In this example, nodes BEB-1 and 
BEB-2 are gateways nodes linking the SPB-management domain and the VLAN-management 
domain. The VLAN-management subnet is 172.16.0.0/24 and the SPB-management subnet is 
172.16.1.0/24. OSPF is used in the Management network. Nodes BEB-1 and BEB-2 redistribute 
routes between OSPF and SPB-MGMT protocols. Route maps prevent circular route redistribution 
between these two protocols.
Snippet 43. In-band management – BEB-1
 
Snippet 44. In-band management – BEB-2
 

<<<PAGE 45>>>
45
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 45. In-band management – BEB-3
 
Snippet 46. In-band management – BEB-4
 
Snippet 47. In-band management – BCB
 
In-band management configuration examples are provided in snippets Snippet 43 through 
Snippet 47. OSPF and route-map configuration in BEBs 1 and 2 is excluded from these snippets.
15.  Operation and Maintenance
15.1  Connectivity Fault Management: 802.1ag
CFM in an SPB network is most useful to perform L2 trace and L2 ping for analysis and 
troubleshooting. Other aspects of CFM such as fault detection, which are important in PBB,  
are less important in SPB because SPB has an IS-IS control plane. These functions (CCM) are  
not currently supported in conjunction with SPB.
OAM is supported at the BVLAN level, refer to figure 28. Virtual MEPs must be configured for 
all BVLANs and BEBs and, optionally, also for BCBs (such that a L2 PING or L2 trace test can be 
initiated from any node to any other node). MIPs are automatically created and do not need to 
be explicitly configured.
Since there is no CCM function to map system names, link trace commands and output will 
reference the BMACs.
Figure 28. OAM in BVLAN and VLAN Domains
SPBM
BVLAN maintenance domain
V
MEP
V
MEP
(V)
MEP
(V)
MEP
MIP
MIP
MIP
VLAN maintenance domain
 

<<<PAGE 46>>>
46
Tech Brief
Shortest Path Bridging Architecture guide
OAM is also supported at the VLAN level or between L2 access switches connected to BEBs over 
SAP UNIs. This is useful in a L2 deployment for testing end-to-end service connectivity between 
sites. OAM at the VLAN level must be set at a higher maintenance domain level than BVLAN OAM.
Figure 29 shows a practical example of how OAM can be used to verify connectivity between 
BEBs by means of Loopback message (LBM) and loopback reply (LBR) and checking the route 
with link trace message (LTM) and link trace reply (LTR).
Figure 29. L2 ping and L2 trace
BEB
BCB
BCB
BEB
(V)
MEP
(V)
MEP
LBM
LBR
BEB
BCB
BCB
BEB
(V)
MEP
(V)
MEP
LTM
LTR
LTR
LTR
MIP
MIP
 
Configuration Snippet 48 provides a sample OAM configuration for service BVLANs 4001-4003. 
Snippet 48. OAM
 

<<<PAGE 47>>>
47
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 49 provides sample configuration and output for an L2 trace test. As shown in the 
snippet, the trace provides, among other elements, BMACs for all transit nodes as well as  
ingress and egress interfaces used. 
Snippet 49. L2 trace
 
15.2  Network performance: Service Assurance Agent 
Latency, jitter and packet loss SAA tests are automatically set-up between all BEBs and BCBs 
and across all BVLANs with the “saa auto-create” command. Refer to Snippet 50 showing the 
configuration and Snippet 51 showing sample statistics.
Snippet 50. Service Assurance Agent configuration
 

<<<PAGE 48>>>
48
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 51. Service Assurance Agent stats
 
15.3  Network maintenance
Two features in SPB can assist in network maintenance tasks: Overload state and graceful restart.
15.3.1  Overload state
SPB provides a graceful way to remove a node from service for maintenance and transition 
traffic to an alternate path (if there is one) with minimal disruption. This is the “overload state.”
Setting the overload state on the node will signal other nodes not to use it as a transit node and 
use alternate paths instead. This is similar to increasing the metric on all the links but is a much 
quicker way of achieving this outcome. Note, however, once the overload state is enabled on a 
node no traffic will transit through the node even if there are no alternative paths.
The overload state can be set indefinitely (until removed) or it can revert after a timer expires.
15.3.2  Graceful restart
SPB IS-IS supports graceful restart in a virtual chassis or physical chassis with redundant  
control modules. 
Without graceful restart, a VC master or CMM takeover event would require neighbour nodes 
to tear down and re-establish adjacencies with the restarting node and re-build the topology 
database, resulting in some disruption to traffic flows.
When graceful restart is enabled, and with the help of a neighbour node, the node undergoing 
a takeover will announce this condition to its neighbours by setting the RR (restart request) in 
a TLV message and continue using its existing FDB while restarting. The neighbour nodes will 
maintain their adjacencies with the restarting node during this process and send their complete 
LSP database information to the restarting node once the process is complete.
This makes the transition a much smoother process because disruption to traffic forwarding is 
minimized and the topology database is re-built in a much shorter time.
16.  Service attachment redundancy
When redundant links and nodes exist in the SPB domain, path computation in the event of a 
failure or restoration event is handled by the IS-IS protocol. But, access or Customer Edge (CE) 
devices connected to BEB nodes do not run SPB IS-IS and therefore other solutions are required 
when redundancy is needed. In this section we will present the different options for the different 
service types.
We start by highlighting that the simplest way of achieving redundant CE to BEB attachment 
is to use VC at the BEB and to attach the CE device to the BEB through a LAG. This redundancy 
option is applicable to any service type (L2 or L3). 

<<<PAGE 49>>>
49
Tech Brief
Shortest Path Bridging Architecture guide
We will now present alternate redundancy options other than VC+LAG. 
Let’s start with L2 Services in figure 30 below. We can consider the following options:
•	 Non-redundant: The CE is attached to a single BEB through a single link. Link, BEB or CE 
failure will result in loss of service to the site
•	 Redundant links: The CE is attached to a single BEB through a link aggregate (LAG). This adds 
protection from single-link failure. Note that fibre runs should use diverse physical paths to 
protect against fibre cuts which would typically interrupt both links otherwise.
•	 Redundant links and nodes: The CE is attached to two different BEBs through two different 
links. This adds protection from BEB failure. When possible, both links should use physically 
diverse paths such that link failure events are not correlated. Dual-Home Link (DHL) is a high 
availability feature that provides fast failover without implementing Spanning Tree or Link 
Aggregation. Please refer to the “AOS 8 Network Configuration Guide” for further details. 
•	 Fully redundant: This option adds CE device redundancy. MSTP (Multiple Spanning Tree 
Protocol) can be used to avoid loops in this redundant connection. By default, SPB floods STP 
BPDUs messaging over SPB services. When using MSTP, different sites must use different 
MSTP regions to avoid creating a large MSTP region spanning all sites.
Note that Virtual Chassis (VC) can be combined with all the options above to increase resiliency.
Figure 30. L2 Service attachment
1. Non-redundant
SPB
2. Redundant links
SPB
BEB
DHL
CE
3. Redundant links and nodes
SPB
MSTP
4. Fully redundant
SPB
 
Let’s now continue with L3 services. We can distinguish two sub-variants: L3 CE and L2 CE. A L3 
CE can exchange routes with the BEBs by using any supported routing protocol as well as static 
or default routes. A L2 CE on the other hand will completely delegate routing to the BEB, which 
will act as a default gateway for local devices. These two sub-variants are illustrated in figure 31 
and figure 32. Note that hairpins, when required, are not shown for simplicity. 
L3 Service attachment with L3 CE options:
•	 Non-redundant: The site is attached to a single BEB through a single link. Link, BEB or CE 
failure will result in loss of service to the site.
•	 Redundant links: The site is attached to a single BEB through a link aggregate (LAG). This adds 
protection from single-link failure. Note that fibre runs should use diverse physical paths to 
protect against fibre cuts which would typically interrupt both links otherwise.
•	 Redundant links and nodes: The site is attached to two different BEBs through two different 
links. This adds protection from BEB failure. When possible, both links should use physically 
diverse paths such that link failure events are not correlated. A dynamic routing protocol such 
as OSPF is used between BEBs and CEs to exchange routing information. Import/Export and 
re-distribution of routes must be carefully planned to avoid circular re-distribution of routes. 
This is accomplished with route maps.
•	 Fully redundant: This option adds CE device redundancy

<<<PAGE 50>>>
50
Tech Brief
Shortest Path Bridging Architecture guide
Figure 31. L3 Service attachment - L3 CE
1. Non-redundant
SPB
2. Redundant links
SPB
BEB
CE
Routing
protocol
3. Redundant links and nodes
SPB
Routing
protocol
4. Fully redundant
SPB
Routing
protocol
 
You may notice that the case of L3 Service attachment with a L2 CE is almost identical to the 
case of L2 Service attachment. However, since the routing function is delegated to the BEB, 
VRRP is required when CEs attach to redundant BEBs. This requires access VLANs to be extended 
across both BEBs. If BEBs are directly connected, the access VLANs can be simply tagged on the 
link interconnecting both BEBs. However, if there is no direct connection between the BEB pair,  
a dedicated SPB service can be created to this effect. 
In addition, note that when using a L2 CE in a L3 Service, there is no routing protocol between CE 
and BEB. In such a case, the associated VRF can be configured as a “low profile” VRF. Low profile 
VRFs have routing capabilities restricted to static and/or imported routes, which is sufficient for 
such a situation. Low profile VRFs take up less BEB resources than “max profile” VRFs allowing 
for creation of more VRFs on the BEB.
As in the case of L2 Service attachment, all options can be combined with VC and LAG.
Figure 32. L3 service attachment - L2 CE
1. Non-redundant
SPB
2. Redundant links
SPB
BEB
CE
3. Redundant links and nodes
SPB
MSTP
4. Fully redundant
SPB
DHL
VRRP
VRRP
 

<<<PAGE 51>>>
51
Tech Brief
Shortest Path Bridging Architecture guide
17.  Loop avoidance and suppression
In the CP, loops are avoided with IS-IS, a link-state routing protocol. In the DP, a node will not 
accept unexpected frames from its neighbours.
However, short-lived transient loops may form in the event of a topology change and until 
network convergence is attained. Loops pose a serious threat to the network stability. 
In the DP, SPB incorporates an additional loop mitigation technique to detect and break these 
transient loops:
•	 Reverse-path Forwarding Check (RPFC): RPFC exploits SPB’s symmetry and congruence 
properties. RPFC verifies that incoming traffic’s source BMAC is indeed reachable over the 
ingress interface according to the local FDB and discards non-conforming frames. 
In addition, the SPB backbone must be protected from loops that may be created due to failures 
and misconfiguration at the VLAN-domain access layer. By default, SAPs forward STP BPDUs 
allowing redundantly-attached VLAN-domain access layer to use STP for loop prevention. 
There is always a chance however that STP may be misconfigured, fail, or not be enabled at all. 
Configuration faults in customer networks can result in loops spanning both the SPB backbone 
and customer access network. This can result in broadcast storms. To protect the SPB backbone 
from broadcast storms, loops involving SAPs must be detected and broken. 
AOS supports an additional loop mitigation mechanism to detect and break access layer loops: 
Loopback Detection (LBD). LBD can detect and protect the backbone network from forwarding 
loops created at the VLAN-domain customer-access layer. LBD operates in addition to other 
mechanisms such as DHL or STP. When a loop is detected, the port is disabled and goes into a 
shutdown state. A trap is sent and the event is logged.
The switch periodically sends out LBD frames from LBD-enabled ports and concludes that the 
port is looped back if it receives the frame on any of the LBD-enabled ports.
LBD can be used on both VLAN UNI and SAP UNI ports. In the case of SAP UNI ports, LBD frames 
will be sent on all SAPs because different access VLANs may have different logical topologies. 
However, if a loop is detected on a SAP, the entire physical port will be shut down. 
LBD should be enabled on all UNI ports.
Figure 33 illustrates situations in which LBD can detect and break loops.
Figure 33. Loopback detection
SPB
Port in switch with highest
BridgeID is shut down
BEB-A
BEB-B
SPB
Port in switch with highest
BridgeID is shut down
BEB-A
BEB-B
SPB
Port in switch with highest
PortID is shut down
BEB-A
BEB-B
 
By default, LBD is disabled for the switch and on all service-access ports. Enable LBD globally  
on the switch and in specific service-access ports or linkaggs as shown in Snippet 52.

<<<PAGE 52>>>
52
Tech Brief
Shortest Path Bridging Architecture guide
Snippet 52. Loopback detection
 
AOS incorporates storm control through flood rate limiting of broadcast, multicast and unknown 
unicast traffic. A high threshold rate is configured in megabits-per-second (mbps), packets-per-
second (pps), or as a percentage of the port speed. When the threshold value is reached, packets 
are dropped or, the port is shutdown. Storm control is enabled by default with pre-defined rates. 
Please refer to the AOS Network Configuration Guide for further details.
18.  General design guidelines
Design guidelines have been provided throughout this document. In this section, we provide 
additional design guidelines to assist the network architect in designing SPB networks.
18.1  BVLANs
As described in section 5, SPB networks load balance traffic on a per-service basis. This load 
balancing is achieved by mapping different services to different BVLANs. An SPB network 
supports up to 16 BVLANs, however, most real-world physical topologies do not support 16 
equal-cost-paths. There is no advantage in creating more BVLANs than the number of equal-cost-
paths in the physical topology. Moreover, since a SPT must be computed for each BVLAN, having 
more BVLANs than equal-cost-paths in the physical topology creates an additional unnecessary 
load in the CP which results in increased resource utilization and convergence times. 
In short: Only create as many BVLANs as there are equal-cost-paths in the physical topology. As 
of AOS 8.7R1 and later releases, only four BVLANs are created by default when using auto-SPB.
18.2  VLAN-to-Service mapping
When creating a SAP, AOS allows mapping multiple or all VLAN tags to the same SPB service.  
We want to stress that, as a general guideline, to preserve L2 isolation between VLANs, different 
VLANs should be mapped to different services (for example, through different SAPs).
Mapping different VLANs to the same SPB service makes inter-VLAN bridging possible, thus 
defeating the purpose of having different VLANs in the first place.
In addition, there is a risk of having duplicate MAC addresses. In theory, there should be no 
duplicate MAC addresses; in reality, it can happen, particularly in virtualized environments. 
Duplicate MAC addresses in different VLANs do not collide, however, if these VLANs are mapped 
to the same SPB service and the client devices are connected to different SAPs, those MACs will 
be constantly learned, re-learned and flushed. This is known as a “mac-move” and should be 
avoided to maintain stability. To avoid mac-move, we strongly recommend mapping different 
VLANs to different SPB services (ISIDs). This will require one SAP and ISID per access VLAN.
There are some situations in which mapping different VLANs to the same SPB service (ISID) is 
acceptable, but we will not elaborate on those situations. 
In short: As a general guideline, map different VLANs to different SPB services by using specific 
SAPs for each VLAN.

<<<PAGE 53>>>
53
Tech Brief
Shortest Path Bridging Architecture guide
18.3  Virtual Chassis
Virtual chassis (VC) is a feature that combines multiple “stackable” switches into a single logical 
“virtual chassis” such that each physical switch becomes a virtual “slot” in the virtually modular 
chassis. A virtual chassis is a single logical entity managed as one device and with single control 
and management planes.  
Virtual chassis provides many benefits such as network architecture and management 
simplification. VC greatly simplifies redundant service attachment. Customer CE access devices 
can be dual-homed to diverse slots in a BEB through a link aggregate. This eliminates the need  
to configure other L2 or L3 redundancy mechanisms such as DHL or VRRP.
When using virtual chassis in the SPB backbone, logical link aggregates (LAGs) are recommended 
to interconnect the VC to all its SPB neighbours such that one member (physical) port connects 
to every slot in the VC as seen in figure 34. This is not mandatory but is recommended and will 
improve the network convergence time in the event of slot failure because the need to update 
tables during the control plane takeover is greatly reduced. In addition, dual homing nodes to 
a VC reduces the need to forward traffic across the VFL because traffic forwarding in a LAG 
prioritizes the use of local linkagg member ports over remote (across the VFL) member ports.
Figure 34. VC and SPB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
BxB
 
18.4  Link Aggregation
Combining multiple physical links into a LAG improves resiliency and increases total available 
bandwidth on the logical link.
In a LAG, traffic is load balanced across member ports in one of two ways:
•	 MAC hash (brief mode)
•	 IP + TCP/UDP port hash (extended mode)
However, SPB backbone ports use MAC-in-MAC encapsulation which means MAC addresses are 
the BMACs of BEB and BCB nodes while IP addresses and port numbers are not visible to the 
hashing logic. In most cases this does not create enough entropy and the load will not be spread 
evenly across all different physical links.
Since AOS 8.3.1R01, a “tunnel-protocol” option can be selected such that the hashing can use 
CMACs or IP addresses + TCP/UDP ports.
It is recommended that this option be enabled on all SPB nodes using LAG. The choice of MAC 
(brief) or IP+TCP/UDP ports (extended) is a global setting which will apply to all LAGs. Please 
refer to the AOS Command Line Interface Guide for further details.

<<<PAGE 54>>>
54
Tech Brief
Shortest Path Bridging Architecture guide
18.5  Link Metric
SPB uses the link metric as a measure of a link’s cost to reach another node. By default, all link 
metrics are set to 10 regardless of link speed. The link metric is an integer in the 1-16M range.
The link metric can be adjusted to influence the SPT calculations. For instance, the metric can be 
changed to reflect the link speed. It should be noted that the metric must be adjusted on both 
sides of a link. Nodes will become adjacent even when the metrics are different, but the highest 
metric will be used in the SPT calculations.
Changing the link metric to reflect the link speed will help steer traffic towards links with 
higher capacity and away from lower capacity ones, making the best use of the total available 
bandwidth and improving performance. Table 3 shows a way in which the metric can be set to 
be inversely proportional to the link speed.
Table 3. Recommended Link Metric
Speed 
Suggested Metric 
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
18.6  QoS
In an SPB network, traffic is classified at the SAP and the classification does not change as traffic 
traverses the backbone and until it exits through another SAP at the destination BEB.
Trusted SAPs copy CoS markings from the incoming VLAN tag onto the BVLAN tag. If incoming 
traffic is not tagged, then the port’s default priority is used. Un-trusted SAPs set the CoS 
markings to a user-defined value.
No further classification based on inner L2-L4 conditions is possible within the SPB backbone 
due to the MAC-in-MAC encapsulation.
When using an external or two-pass routing (external physical or internal front-panel loopback), 
the standard VLAN port must best set to trust and use CoS and not DSCP to preserve CoS 
markings end-to-end.
19.  Security guidelines
In this section, we will provide some additional design guidelines specific to the security domain. 
This is not an exhaustive list of recommendations, rather, we will focus on certain guidelines 
specific to SPB deployments. We will go through different AOS features and how they can be 
used to improve security in an SPB network. Other more general security guidelines can be 
found in [3].

<<<PAGE 55>>>
55
Tech Brief
Shortest Path Bridging Architecture guide
19.1  Management VRF
As explained in section 3.6, SPB relies on a non-IP protocol for path computation. For this reason, 
BCB nodes and BEB nodes supporting L2 services only do not require an IP address. The only 
case in which an SPB node requires an IP address is the case of a BEB node supporting a L3 
service or feature such as L3 VPN, VPN Lite, or VRRP, among others.
We have covered different SBP management options in section 14. Management IP addresses 
can be bound to:
•	 The EMP port, in case of OOBM
•	 To a standard VLAN port, in the case of OOBM
•	 The control BVLAN, in the case of in-band management
•	 A Management SPB service, directly in the case of products supporting single-pass  
inline routing
•	 A Management SPB service, indirectly in the case of products supporting external physical  
or internal front-panel loopback
We want to point out that no matter what management option is chosen, management IP 
addresses should use a different VRF from the VRF used for service or customer traffic. This 
is already the case when using the EMP port for OOBM. One possibility is creating a dedicated 
management VRF and enabling the required management protocols on this VRF as shown in 
Snippet 43 through Snippet 47.
Another possibility is using the default VRF for management, under the condition of not using  
it for anything other than management.
19.2  MACSec
Data integrity and confidentiality must be protected while in transit through the network. 
MACSec is an IEEE standard (802.1AE) which provides point-to-point authentication and optional 
encryption between MACSec-capable devices such as switches. MACSec can prevent various 
threats such as man-in-the-middle, sniffing, spoofing, and playback attacks.
Because MACSec operates at the MAC layer, it transparently secures all upper layer traffic 
transiting through MACSec-enabled links. This includes both application-layer data, as well 
as control-plane and management-plane communication. In addition, unlike IPSec, MACSec is 
implemented in hardware at wire-speed and does not introduce additional latency or bandwidth 
limitations.
19.3  NAC
In section 13.2, we explained how users and devices can be dynamically mapped to their 
services based on their identity. Enabling authentication on every front-panel port ensures only 
authorized users and devices can access network services. One additional benefit of creating 
dynamic SAPs through NAC is that no service is instantiated on a BEB until an authorized user 
successfully authenticates and is mapped to the service: The service is instantiated on demand. 
This is an additional layer of security compared to static SAPs because no service is connected  
if no authorized user is connected. It is clearly more difficult to hack, attack, or otherwise disrupt 
a service when it is not even connected. 
19.4  Router authentication
As explained in section 11.1, an SPB network can exchange routes with external non-SPB entities 
by using the VPN Lite feature. This means that one or more SPB BEB nodes will run a routing 
protocol such as OSPF or BGP with external entities. Any learnt route may be imported into the 
SPB backbone and propagated to other BEB nodes by way of IS-IS TLVs. 

<<<PAGE 56>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license  
by ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.
com/en/legal/trademarks-copyright. All other trademarks are the property of their respective owners.  
The information presented is subject to change without notice. Neither ALE Holding nor any of 
its affiliates assumes any responsibility for inaccuracies contained herein. © Copyright 2021 ALE 
International, ALE USA Inc. All rights reserved in all countries. DID21040501EN (April 2021)
This creates an opportunity for a bad actor to inject malicious routes and poison the routing 
table to carry out DoS, MITM, or other attacks.
This risk can be mitigated by enabling routing protocol authentication (e.g. MD5 for OSPF or BGP).
20.  Conclusion
Shortest Path Bridging is a powerful technology yet simple when compared to others such as 
MPLS or EVPN. SPB is broadly supported across the Alcatel-Lucent OmniSwitch portfolio with 
products in multiple formats, from stackable to modular chassis and even industrial-grade 
ruggedized variants. This product breadth, coupled with SPB’s service-oriented framework, 
results in a network architecture that can deliver the required service to the right location  
with minimal network configuration changes, or even in a fully automated manner.
 


<<<DOC 2: SPB/spb-deployment-guide-en.pdf | 起始页 57 | 26p>>>

<<<PAGE 57>>>
SPB Deployment Guide 
Ed. 2025 
 
Shortest Path Bridging 
(SPB) Deployment Guide  
 
 

<<<PAGE 58>>>
 
2  
 
     
 
 
Table of Contents 
GLOSSARY ....................................................................................................................................................... 2 
ABOUT THIS DOCUMENT .................................................................................................................................. 3 
PURPOSE ....................................................................................................................................................................... 3 
SCOPE .......................................................................................................................................................................... 3 
AUDIENCE ..................................................................................................................................................................... 3 
INTRODUCTION ............................................................................................................................................... 4 
SHORTEST PATH BRIDGING (SPB) ...................................................................................................................................... 4 
IS-IS ............................................................................................................................................................................ 4 
PRE-DESIGN – REQUIREMENTS AND DATA COLLECTION..................................................................................... 5 
CONTEXT ....................................................................................................................................................................... 5 
TOPOLOGY .................................................................................................................................................................... 6 
MANAGEMENT ............................................................................................................................................................... 7 
DESIGN – SPECIFICATIONS ................................................................................................................................ 8 
HIGH LEVEL DIAGRAM ..................................................................................................................................................... 8 
ADDRESSING PLAN .......................................................................................................................................................... 9 
WAN INTERFACES .......................................................................................................................................................... 9 
MANAGEMENT ADDRESSES .............................................................................................................................................. 9 
DEPLOYMENT ................................................................................................................................................ 10 
VLANS ....................................................................................................................................................................... 10 
LOOPBACK DETECTION ................................................................................................................................................... 10 
BVLANS ..................................................................................................................................................................... 11 
SPB SERVICES .............................................................................................................................................................. 13 
SAP ........................................................................................................................................................................... 14 
SAP FOR DIRECTLY CONNECTED ACCESS POINTS ................................................................................................................. 16 
ROUTING ....................................................................................................................................................... 17 
VRF CREATION............................................................................................................................................................. 17 
VRF INTERFACES .......................................................................................................................................................... 17 
VRRP ......................................................................................................................................................................... 18 
CONFIGURING PBR FOR VRF INTERFACES ......................................................................................................................... 20 
VRRP TRACKING .......................................................................................................................................................... 21 
OSPF ......................................................................................................................................................................... 22 
POLICIES ........................................................................................................................................................ 23 
QOS ........................................................................................................................................................................... 23 
CONCLUSION ................................................................................................................................................. 23 
ALTERNATIVE CONFIGURATION ...................................................................................................................... 24 
S-HOOK CONFIGURATION ............................................................................................................................................... 24 
RELATED DOCUMENTS ................................................................................................................................... 25 

<<<PAGE 59>>>
SPB Deployment Guide 
Ed. 2025 
Deployment Guide 
Glossary 
ACRONYME 
DEFINITION 
BCB 
 Backbone Core Bridge 
BEB 
Backbone Edge Bridge 
ECT 
Equal-Cost Tree 
ISID 
Instance Service Identifier 
IS-IS 
Intermediate System to Intermediate System 
MAC 
Media Access Control 
OSPF 
Open Shortest Path First 
SAP 
Service Access Point 
SPB 
Shortest Path Bridging (IEEE 802.1aq) 
SPF 
Shortest Path First 
STP 
Spanning Tree Protocol 
VC 
Virtual Chassis 
LBD 
Loopback Detection 
 
 
 

<<<PAGE 60>>>
 
3  
 
     
 
 
About this document 
Purpose 
The purpose of this document is to provide a comprehensive guide on deploying a Shortest Path 
Bridging (SPB) Network. In this setup, all the SAPs within a service belong to the same VLAN and 
share the same IP subnet. The SPB nodes do not need to redistribute any routes. This guide offers 
a step-by-step walkthrough, highlighting our best practices and essential configurations for 
successful integration. By following the instructions outlined in this document, you will be able to 
understand and configure Alcatel Lucent Enterprise SPB solution within your networks.  
Ensure you have the most recent version of this document. 
Scope 
This document does not aim to cover every aspect or explore all possible architecture options, 
but instead focuses on a validated, recommended one.  
It offers an overview of the technology and configuration necessary to achieve the target 
architecture, specifically covering:  
• 
VLANs 
• 
Loopback Detection 
• 
BVLANs 
• 
SPB Services 
• 
SAPs  
• 
VRFs 
• 
VRRP & Tracking 
• 
Routing the network using OSPF 
Audience 
The intended audience for this document includes customer and business partner, networking 
professionals involved in the design and deployment of enterprise networks. 
 
 

<<<PAGE 61>>>
 
4  
 
     
 
 
Introduction 
Shortest Path Bridging (SPB) 
Shortest Path Bridging (SPB), also known as 802.1aq, is an IEEE networking standard designed to 
overcome the limitations of STP while offering advanced features. SPB not only addresses STP's 
challenges but also provides MPLS-like VPN services in a much simpler deployment model. We use 
SPB to build the core of our network, where we will create services for our multiple functions, and 
forward traffic related to those services efficiently, reliably and securely. 
IS-IS  
IS-IS is the protocol used by SPB to determine the forwarding paths within the participating 
nodes. It takes advantage of multiple equal-cost paths that utilize all the available links. As a link 
state protocol, it reacts swiftly to failures of nodes or links within the network to maintain 
connectivity.  
SPBM uses an extended version of the IS-IS protocol that supports SPB (ISIS-SPB) to calculate the 
SPBM network topology. In addition, the learning and propagation of source MAC addresses is 
handled through the ISIS-SPB control plane, instead of through the data plane.  
When SPB is used, each bridge is the Root for all traffic entering that bridge. As a result, each 
bridge can provide the shortest path to every other bridge in the network.  
 

<<<PAGE 62>>>
 
5  
 
     
 
 
Pre-design – Requirements and Data Collection 
Context 
Overview: 
This document provides a sample design for a mid-sized enterprise network. The design includes 
two Shortest Path Bridging (SPB) Backbone Core Bridges (BCBs) and four SPB Edge Bridges (BEBs), 
suitable for environments requiring dozens of BEBs and hundreds of access switches, supporting 
thousands of endpoints (users and devices). 
For larger organizations, this base design can be scaled by adding two or more BCBs, supporting 
an increased number of BEBs, access switches, and endpoints. 
Enterprises with multiple campuses or large distributed locations may require inter-segment 
routing across these sites. This approach will be detailed further in our "SPB Layer-3 Deployment 
Guide" document. 
Objectives: 
Our goal is to establish a robust, secure, and scalable network infrastructure that serves various 
departments, such as Corporate, R&D, Guest, Voice, and Utilities. 
Deployment Steps: 
0. Establish the physical topology and configure links/LAGs. 
1. Create the VLANs that will be used across all access switches. 
2. Configure the Loopback detection 
3. Configure the control BVLAN and other necessary BVLANs. 
4. Configure the SPB services. 
5. Configure the SAPs on the BEBs for the Access Devices. 
6. Set up the different VRFs to segment the network. 
7. Implement VRRP between the two main BEBs for high availability. 
8. Establish a point-to-point connectivity between all VRFs and the policy-based router. 
9. Enable VRRP Tracking 
10. Enable OSPF betweem the BEBs and the PBR for inter-service routing  
11. Finally, configure network policies to control traffic flow and ensure security and 
performance. 
 
 

<<<PAGE 63>>>
 
6  
 
     
 
 
Topology 
We reserve full mesh to the Core and ensure sufficient link redundancy as we add and connect 
the Edge nodes. In this topology every BEB is meshed with the two BCBs with LAGs, but not 
necessarily with the other BEBs. All the BEBs and BCBs are at least a Virtual Chassis (VC) of two 
switches. SPB finds the shortest path between every two nodes, maximizing the performance and 
low latency benefits of this design. At the access layer, we use BEB SAPs to provide access to 
computing devices, such as hypervisors or servers, and network devices, such as lower cost 
switches and wireless access points.  
 
BEB-3 and BEB-4 are running VRRP and function at the top of the network, hosting all VRFs and 
handling routing.  
 
Above, we have the Policy-Based Router (PBR). This switch has point-to-point connections with an 
interface in each VRF. It manages inter-service routing and applies restrictive policies, “like” a 
firewall would for the network. It also performs microsegmentation between VRF entities and 
uses OSPF to share routes across the VRFs and provide access outside the network. 

<<<PAGE 64>>>
 
7  
 
     
 
 
Management 
In terms of management, SPB IS-IS, is not an IP protocol, meaning BCB nodes don't need IP 
interfaces. BEB nodes only require IP interfaces when supporting L3 services like VPNs. However, 
all SPB nodes, BCB or BEB, need IP interfaces for management purposes. 
Management options include: 
• 
Out of Band Management (OOBM): Common across network architectures using EMP 
ports 
• 
Dedicated Management Service: An SPB service and VRF are assigned to management. For 
nodes without single-pass inline routing, an external loopback is needed. 
• 
In-band Management: In-band management is applicable to all SPB nodes regardless of 
their routing capabilities (such as, single-pass inline, external physical, or internal front-
panel loopback). Management IP interfaces can be created directly on the control BVLAN, 
therefore, no loopback of any kind is required. The management network or stations 
attach to one or more gateway nodes through VLAN-domain interfaces. 
It is up to you to choose the one that fits you best. 
Naming conventions 
The naming conventions that we use focus on easier management and intuitive understanding of the 
network.  
• 
BCB (Backbone Core Bridge) and BEB (Backbone Edge Bridge) are key elements of the network. 
• 
BEB-1 and BEB-2 names are not used because BCB-1 and BCB-2 occupy those numbers. Avoiding 
using the same numbers here will simplify understanding the network topology following our 
logic. 
 
Access Switch Naming 
All access switches connected to a BEB follow a clear naming pattern: 
• 
The first digit represents the BEB number. 
• 
The second digit represents the switch sequence. 
Examples: 
• 
The first access switch connected to BEB-3 is labeled ACC-31. 
• 
If there's another access switch, it would be ACC-32. 
 
Link Aggregation Naming 
Linkagg identifiers also follow an intuitive pattern: 
• 
The first digit corresponds to the BCB number. 
• 
The second digit corresponds to the BEB number. 
Examples: 
• 
Linkagg 13 connects BCB-1 to BEB-3. 
• 
Linkagg 24 connects BCB-2 to BEB-4. 
 
By adopting this approach, we can maintain a clear mental map of the network, ensuring easier 
troubleshooting and management. 
 

<<<PAGE 65>>>
 
8  
 
     
 
 
Design – Specifications 
High Level Diagram 
 
 

<<<PAGE 66>>>
 
9  
 
     
 
 
Addressing Plan 
 
CORP 
 
 
 
 
 
R&D 
 
 
 
 
 
Name 
Network 
VLAN 
SERVICE 
ISID 
BVLAN 
Name 
Network 
VLAN 
SERVICE 
ISID 
BVLAN 
corp-wired 
10.10.0.0/20 
1000 
1000 
1000 
4001 
rd-users 
10.11.0.0/20 
2000 
2000 
2000 
4001 
corp-wlan 
10.10.16.0/20 
1016 
1016 
1016 
4001 
rd-servers 
10.11.16.0/20 
1116 
1116 
1116 
4001 
corp-printers 
10.10.47.0/24 
1047 
1047 
1047 
4001 
rd-storage 
10.11.47.0/24 
1147 
1147 
1147 
4001 
 
 
 
 
 
 
 
 
 
 
 
 
GUEST 
 
 
 
 
 
VOICE 
 
 
 
 
 
Name 
Network 
VLAN 
SERVICE 
ISID 
BVLAN 
Name 
Network 
VLAN 
SERVICE 
ISID 
BVLAN 
guest-wired 
10.12.0.0/20 
1200 
1200 
1200 
4002 
voice-wired 
10.13.0.0/20 
1300 
1300 
1300 
4002 
guest-wlan 
10.12.16.0/20 
1216 
1216 
1216 
4002 
voice-wlan 
10.13.16.0/20 
1316 
1316 
1316 
4002 
guest-byod 
10.12.47.0/24 
1247 
1247 
1247 
4002 
 
 
 
 
 
 
 
 
 
UTILITIES 
 
 
Name 
IP Address 
VLAN 
SERVICE 
ISID 
BVLAN 
utilities-cameras 
10.14.0.0/20 
1400 
1400 
1400 
4002 
utilities-doorlocks 
10.14.16.0/20 
1416 
1416 
1416 
4002 
utilities-lights 
10.14.47.0/24 
1447 
1447 
1447 
4002 
utilities-temp-sensors 
10.14.48.0/24 
1448 
1448 
1448 
4002 
utilities-ac-servers 
10.14.49.0/24 
1449 
1449 
1449 
4002 
WAN Interfaces 
VRF-TO-PBR INTERFACES 
Name  
(source-destination) 
IP Interface 
VLAN ID 
VRF 
Device 
corp3-pbr 
10.90.250.1/30 
3913 
corp 
BEB-3 
corp4-pbr 
10.90.250.5/30 
3914 
corp 
BEB-4 
rd3-pbr 
10.90.250.9/30 
3923 
rd 
BEB-3 
rd4-pbr 
10.90.250.13/30 
3924 
rd 
BEB-4 
guest3-pbr 
10.90.250.17/30 
3933 
guest 
BEB-3 
guest4-pbr 
10.90.250.21/30 
3934 
guest 
BEB-4 
voice3-pbr 
10.90.250.25/30 
3943 
voice 
BEB3 
voice4-pbr 
10.90.250.29/30 
3944 
voice 
BEB-4 
utilities3-pbr 
10.90.250.33/30 
3953 
utilities 
BEB-3 
utilities4-pbr 
10.90.250.37/30 
3954 
utilities 
BEB-4 
Management Addresses 
 
 
 
 
 
SPB Nodes 
 
 
 
Name 
EMP-VC 
EMP-CHASSIS-1 
EMP-CHASSI-2 
BCB-1 
10.255.219.101 
10.255.218.101 
10.255.218.201 
BCB-2 
10.255.219.102 
10.255.218.102 
10.255.218.202 
BEB-3 
10.255.219.111 
10.255.218.111 
10.255.218.211 
BEB-4 
10.255.219.112 
10.255.218.112 
10.255.218.212 
BEB-5 
10.255.219.113 
10.255.218.113 
10.255.218.213 
BEB-6 
10.255.219.114 
10.255.218.114-CMMA 
10.255.218.214-CMMA 
Access Points  
 
 
Name 
Pool 10.20.0.0/22 
Attached device 
AP-31 
DHCP 
BEB-3 
AP-41 
DHCP 
ACC-41 
AP-51 
DHCP 
ACC-51 
AP-61 
DHCP 
BEB-6 
AP-62 
DHCP 
ACC-61 

<<<PAGE 67>>>
 
10  
 
     
 
 
Deployment 
VLANs 
First and foremost, the infrastructure includes multiple VLANs, each associated with specific 
numbers for specific services as shown in Network Plan: 
1000,1016,1047,1100,1116,1147,1200,1216,1247,1300,1316,1400,1416,1447,1448 
These VLANs must be configured on the Access Switches where needed. 
Create a new VLAN using the following command: 
->vlan 1000 
Repeat for the other VLANs. 
We can check that all VLANs have been successfully created using the following command: 
->show vlan 
The output should resemble the following:  
Snippet 1. 
 “show vlan on ACC-31” 
 
Repeat this process for all other relevant access switches. 
Loopback Detection 
Loopback Detection (LBD) is a feature designed to identify and mitigate network loops, which can 
cause broadcast storms, degraded performance, or complete network outages. Loopback-
Detection must first be enabled globally and then applied to specific LAGs. 
This configuration is implemented between BEBs and ACC switches SAPs. 
Enable Loopback Detection Globally: 
Example on BEB-3 and ACC-31 linkagg 31: 
->loopback-detection enable 
Enable Loopback Detection on the Specific LAG:: 
Example on BEB-3 and ACC-31 linkagg 31: 
->loopback-detection service-access linkagg 31 enable 

<<<PAGE 68>>>
 
11  
 
     
 
 
Repeat the above steps for all relevant devices and LAG interfaces in the network. 
BVLANs 
BVLANs are utilized within SPB to define the core or backbone VLANs that carry traffic across the 
SPB network. These VLANs serve as the foundation for forwarding frames and facilitating 
communication between different devices and network segments within an SPB network. 
The Control BVLAN, is a specific BVLAN designated to handle control plane traffic for SPB. It is 
responsible for the management and signaling functions required to maintain the SPB network's 
operation.  
 
Name 
BVLAN 
Default (Control BVLAN) 
4000 
Corp 
4001 
R&D 
4001 
Guest 
4002 
Voice 
4002 
Utilities 
4002 
During the design phase, we opted to allocate the SPB services across three BVLANs (4000-4002) 
for each upcoming VRF. These BVLANs operate within the SPB domain, encompassing both BEBs 
and BCBs, and must therefore be configured on each respective device. 
Enable the BVLANs on all the Omniswitch that belong in the SPB domain by entering the following 
command: 
->spb bvlan 4000-4002 admin-state enable 
With the BVLANs now active, we need to determine which one will serve as the control BVLAN.  
Configure the control BVLAN with this command: 
->spb isis admin-state disable 
->spb isis control-bvlan 4000 
->spb isis admin-state enable 
 
Notes 
SPB ISIS must be first disabled to configure the control BVLAN. 
We recommend not exceeding 4 BVLANs.  
VLANs 4000 through 4002 are used as SPB backbone VLANs and do not use spanning tree 
protocols. AOS assigns a unique ECT-ID to each BVLAN, which helps ensure that each BVLAN 
creates separate SPTs (Shortest Path Trees) based on the network's physical layout. IS-IS "Hello" 
messages are exchanged over the control BVLAN (VLAN 4000), establishing point-to-point 
connections. This allows for LSP (Link State Protocol) exchanges, creation of a topology database, 
and formation of an SPT for each BVLAN.  
 
 
Notes 
Use "spb isis bvlan ect-id" to make sure that the same ECT ID is assigned to the same BVLAN ID on each switch (edge and core 
switches) in the SPBM topology. 

<<<PAGE 69>>>
 
12  
 
     
 
 
 
The next step is to configure all the ports or LAGs that interconnect the backbone as SPB interfaces: 
Example between BCB-1 and BEB-6 linkagg: 
->spb isis interface linkagg 16 
This type of interface sends PDUs to detect neighboring SPB switches and form adjacencies. 
Repeat for the other interfaces that interconnect the SPB nodes. 
The interfaces can be displayed using the following command: 
Example on BCB-1: 
->spb isis interface 
Snippet 2. 
“show spb isis interface on BCB-1” 
 
We can verify that the connections are established by using the following command: 
->show spb isis adjacency 
We should see all the peers listed. 
Snippet 3. “show spb isis adjacency on CORE-1” 
 
We can also check that our BVLANs are created using the command: 
->show spb isis bvlans 
The output should look as followss: 
Snippet 4. 
 “show spb isis bvlans”  
 

<<<PAGE 70>>>
 
13  
 
     
 
 
We have at this point configured our SPB backbone. The next step will focus on creating the 
services. 
SPB Services 
An SPB service connects multiple sites within a single-to-any bridging domain. This section 
focuses on setting up the SPB services on the existing backbone configuration. Services are 
configured only on Backbone Edge Bridges (BEBs) where they are needed, and not on Backbone 
Core Bridges (BCBs). The process of creating an SPB service includes associating the service with 
an IS-IS instance and a BVLAN, which will handle the service traffic. 
• 
The service number is only locally relevant and can vary between different BEBs. 
• 
The ISID needs to be the same across all BEBs connected to the same service. 
• 
The BVLAN that the service is mapped should also be consistent across all BEBs 
connected to the service. 
• 
Different services can be mapped to different BVLANs to help balance traffic. 
We first choose a service number, associated with an ISID and a BVLAN: 
Example witch service 1000 
->service 1000 spb isid 1000 bvlan 4001 vlan-xlation enable 
 
Notes 
“vlan-xlation enable” is used to allow different VLANs on separate parts of the network to communicate without directly 
sharing the same VLAN ID. 
Although we use the same number for the service, ISID, and VLAN in this guide to maintain a good 
mentale map, it is important to understand that these identifiers serve different purposes and do 
not need to match.  
When all the services are configured, we can verify by using the following: 
->show spb isis services 
Snippet 5. 
 “show spb isis services on BEB-3” 

<<<PAGE 71>>>
 
14  
 
     
 
 
 
SAP 
Now that we have our SPB Backbone and configured our services we can focus on the access 
ports.  
The SAP is a UNI-side logical port which binds a physical port and specific customer traffic types 
(untagged, single-tagged, double-tagged or all) to an SPB service. Multiple SAPs can be associated 
with the same physical port thus multiplexing and mapping different customer traffic 
encapsulations to different SPB services. 
First, we need to set the port or the linkagg as access.  
Example with BEB-3 linkagg 31 
->service access linkagg 31 vlan-xlation enable 
 
Notes 
“vlan-xlation enable” needs to be set at both the service and port level when used, this why we add it here as well. 
Then to configure the port as SAP port the steps are as followss: 
1. Begin by selecting the appropriate service number followed by the SAP subsection. 
2. Specify if it’s a Linkagg or port along with its associated number. 
3. VLAN Selection: After the colon (:), indicate the VLAN(s) that will be accepted on this link 
for the selected service 
for instance, for the service 1000 on the BEB-3 which is attached to the Linkagg 31 we have: 
->service 1000 sap linkagg 31:1000  
 
Notes 
We can use the value “0” for untagged traffic 

<<<PAGE 72>>>
 
15  
 
     
 
 
This means that inbound traffic tagged vlan 1000 on linkagg 31 will be accepted and binded to 
service 1000 of the SPB domain. 
We can verify that our SAP port is created by using the following command: 
Example with service 1000 
->show service 1000 debug-info  
Which should output the following: 
Snippet 6. 
 “show service 1000 debug-info on BEB3” 
 
 
Repeat the procedure for all the services needed on all BEBs. 
 
At this stage we have a running SPB Backbone fully configured. We can test by configuring static IP 
addresses on both sides of the network, assigning a VLAN tag, and then performing a ping test to 
confirm that traffic is being properly bridged.  
Snippet 7. 
 “test IP interface creation and ping”  
 
This ping test shows that the test interface on ACC-31 can reach the test IP Interface on ACC-64. 
We can display the SPF path using the following: 
Example with bvlan 4001 on BEB-3 
->show spb isis spf bvlan 4001 
The service 1000 is carried by BVLAN 4001. 
Snippet 8. 
 “show spb isis spf bvlan 4001 on BEB-3” 
 

<<<PAGE 73>>>
 
16  
 
     
 
 
We acknowledge that the path used for BVLAN 4001 to reach BEB-6 is going through BCB-2. 
 
SAP for directly connected Access Points 
In some scenarios, we may need to connect Access Points directly to a BEB SAP. Since APs require 
an IP address and because the connection between the AP and SAP does not use VLAN tagging, 
the AP must obtain its IP address through the untagged traffic. To enable this, the BEB SAP should 
be configured to map the AP management service to untagged traffic. 
For instance, the service 2000 is the service we use to manage the APs. On the BEB-3 which is 
attached to the AP-31 we have the following configuration : 
First, we need to set the port as access:  
Example with BEB-3 port 1/1/31 with an AP connected 
->service access port 1/1/31 vlan-xlation enable 
 
Notes 
“vlan-xlation enable” needs to be set at both the service and port level when used, this why we add it here as well. 
 
->service 2000 sap port 1/1/31:0  
 
Notes 
We use the value “0” to map the untagged traffic to the AP management service on the port 1/1/31.  
Finally, we configure the SAPs to associate services with the tagged packets received from the 
APs' SSIDs. 
Example with Corp WLAN users service 1016, vlan 1016: 
->service 1016 sap port 1/1/31:1016 
The SAP is ready. 
The next step will focus on routing the network. 
 
 

<<<PAGE 74>>>
 
17  
 
     
 
 
Routing 
VRF Creation 
To ensure traffic isolation and provide secure and reliable access to resources for various 
departments, including corporate offices, R&D, guest access, VoIP, and network management 
services, Virtual Routing and Forwarding (VRF) instances are implemented on our Alcatel-Lucent 
Enterprise OmniSwitch. These VRF instances will be deployed on Backbone Edge Bridges (BEBs) 3 
and 4, which utilize VRRP for redundancy. 
The steps to create the VRFs are fairly simple. On the BEBs we simply use the following 
commands: 
->vrf create corp 
->vrf create rd 
->vrf create guest 
->vrf create voice 
->vrf create utilities 
We can verify that our VRFs are created using the following 
->show vrf 
Snippet 9. 
“show vrf” 
  
VRF Interfaces 
This section focuses on creating multiple logical interfaces under each VRF, with each interface 
serving distinct services. For instance, wired devices, wireless users, and printers for the 
corporate VRF. IP Addresses choice: 
• 
Each interface is assigned an IP address from the last addressable subnet, with the final 
digit representing the BEB number for simplicity and consistency. 
• 
This IP addressing scheme uses the last digit of the IP addresses to correspond with the 
BEB numbers, making them easy to remember. 
• 
BEB-3  uses .3 and BEB-4 .4 
• 
We reserve .1 for the VRRP interface. 
The VRRP IP (.1) of each interface is the main gateway for devices on the network, dynamically 
switching between BEB-3 and BEB-4 based on availability and redundancy requirements. We will 
see this later. 
 

<<<PAGE 75>>>
 
18  
 
     
 
 
Lets focus on BEB 3 first: 
We use the last digit corresponds to the BEB number .3 in this case. Similarly, BEB-4 will follow the same configuration, using .4 instead. 
->vrf corp 
->vrf corp ip interface "corp-wired" address 10.10.15.3 mask 255.255.255.0 service 1000 
->vrf corp ip interface "corp-wlan" address 10.10.31.3 mask 255.255.255.0 service 1016 
->vrf corp ip interface "corp-printers" address 10.10.47.3 mask 255.255.255.0 service 1047 
 
 
Notes 
Latest generation ASICs support integrated routing and bridging in the SPB domain in the exact same manner as in the VLAN 
domain. This means that IP interfaces can be associated with an SPB service directly and traffic can be routed between two 
SPB services or between a VLAN and an SPB service in a single-pass operation without loopbacks. We refer to this as single-
pass inline routing. At the configuration level we simply need to specify the service number when configuring the IP interface. 
See the alternative configuration at the end of the document. 
We can check that our interfaces are created using the following command: 
->vrf corp 
->show ip interfaces 
 
Which should output the following: 
Snippet 10. 
 “show ip interfaces in corp VRF on BEB 3” 
 
Repeate the step for the other interfaces on their corresponding VRFs on other BEBs. 
VRRP 
VRRP provides high availability by assigning one BEB as the primary (master) and the other as a 
backup (standby). If the primary BEB fails, the backup takes over, ensuring continuous service 
without interruption. It’s important to avoid having a single point of failure in the network. 
To configure VRRP its fairly simple and consist of doing 3 commands on both BEB 3 and BEB 4.  
Example on BEB 3 for the corp VRF: 
->vrf corp 
->ip vrrp 1 interface corp-wired 
->ip vrrp 1 interface corp-wired address 10.10.15.1 
->ip vrrp 1 interface corp-wired admin-state enable 
 
->ip vrrp 2 interface corp-wlan 
->ip vrrp 2 interface corp-wlan address 10.10.31.1 
->ip vrrp 2 interface corp-wlan admin-state enable  
->ip vrrp 3 interface corp-printers 

<<<PAGE 76>>>
 
19  
 
     
 
 
 
->ip vrrp 3 interface corp-printers address 10.10.47.1 
->ip vrrp 3 interface corp-printers admin-state enable  
->exit 
We can see our VRRP instance  and verify the status by doing the following command: 
Example on BEB 3 in corp VRF : 
->vrf corp 
->show ip vrrp 
Snippet 11. 
 “show ip vrrp on BEB 3 in the corp VRF”  
 
We can ping the interfaces with our test interfaces on ACC-31 to the VRRP Interface to check the 
connectivity. 
Snippet 12. 
 “ping from ACC-31 to VRRP IP corp wired”  
 
 
The VRRP configuration is done and working. 
 
Notes 
Each interface in each VRF has its own /24 or /20 subnet. The use of `.1` as the virtual gateway address for all VRRP interfaces 
does not imply shared use—it is unique per subnet. 
 
 
 
 
 
 

<<<PAGE 77>>>
 
20  
 
     
 
 
Configuring PBR for VRF Interfaces 
In our setup, we use an OmniSwitch as a “Policy-Based Router” (PBR). This switch have point-to-
point connections with an interface in each VRF and serve as a routing point, applying QoS to 
manage traffic between services and external networks. 
For these interfaces we use a /30 subnet. 
VRFs WAN INTERFACES 
Name (source-destination) 
Subnet 
VLAN ID 
VRF 
Device 
IP Interface 
(source-destination) 
corp3-pbr 
10.90.250.0/30 
3913 
corp 
BEB-3 
.1 - .2 
corp4-pbr 
10.90.250.4/30 
3914 
corp 
BEB-4 
.5 - .6 
rd3-pbr 
10.90.250.8/30 
3923 
rd 
BEB-3 
.9 - .10 
rd4-pbr 
10.90.250.12/30 
3924 
rd 
BEB-4 
.13 - .14 
guest3-pbr 
10.90.250.16/30 
3933 
guest 
BEB-3 
.17 - .18 
guest4-pbr 
10.90.250.20/30 
3934 
guest 
BEB-4 
.21 - .22 
voice3-pbr 
10.90.250.24/30 
3943 
voice 
BEB-3 
.25 - .26 
voice4-pbr 
10.90.250.28/30 
3944 
voice 
BEB-4 
.29 - .30 
utilities3-pbr 
10.90.250.32/30 
3953 
utilities 
BEB-3 
.33 - .34 
utilities4-pbr 
10.90.250.36/30 
3954 
utilities 
BEB-4 
.37 - .38 
The interface names should be easy to understand, which is why we use the format "source-
destination." For example, on BEB-3 within the VRF "corp," the interface will be named "corp3-
pbr." On the PBR, the interfaces will be named "pbr-corp3" and "pbr-corp4," indicating the corp 
interfaces for BEB-3 and BEB-4, respectively. 
We first need to create the different VLANs for these interfaces. 
On the PBR : 
->vlan 3913 name "vrf-corp-beb3" 
->vlan 3914 name "vrf-corp-beb4" 
->vlan 3923 name "vrf-rd-beb3" 
->vlan 3924 name "vrf-rd-beb4" 
->vlan 3933 name "vrf-guest-beb3" 
->vlan 3934 name "vrf-guest-beb4" 
->vlan 3943 name "vrf-voice-beb3" 
->vlan 3944 name "vrf-voice-beb4" 
->vlan 3953 name "vrf-utilities-beb3" 
->vlan 3954 name "vrf-utilities-beb4" 
Verify using show vlan : 
Snippet 13. 
 “show vlan on PBR” 
 
 

<<<PAGE 78>>>
 
21  
 
     
 
 
Then create the diffrerrente interfaces and assign the corresponding VLAN on the PBR:: 
->ip interface pbr-corp4 address 10.90.250.6/30 vlan 3914 
->ip interface pbr-rd4 address 10.90.250.14/30 vlan 3924 
->ip interface pbr-guest4 address 10.90.250.22/30 vlan 3934 
->ip interface pbr-voice4 address 10.90.250.30/30 vlan 3944 
->ip interface pbr-utilities4 address 10.90.250.38/30 vlan 3954 
->ip interface pbr-corp3 address 10.90.250.2/30 vlan 3913 
->ip interface pbr-rd3 address 10.90.250.10/30 vlan 3923  
->ip interface pbr-guest3 address 10.90.250.18/30 vlan 3933  
->ip interface pbr-voice3 address 10.90.250.26/30 vlan 3943  
->ip interface pbr-utilities3 address 10.90.250.34/30 vlan 3953 
In the corp VRF BEB-3: 
->vrf corp 
->ip interface corp3-pbr address 10.90.250.2/30 vlan 3913 
In the corp VRF BEB-4: 
->vrf corp 
->ip interface corp4-pbr address 10.90.250.1/30 vlan 3913 
Repeat the steps for the other interface in each VRFs. 
VRRP Tracking 
In our setup, we monitor the point-to-point interface between each VRF and the PBR. All VRRP 
interfaces initially have a priority of 100, we configured the master to be 120. If the link goes 
down, the VRRP interfaces within the VRF will reduce their priorities by 25, reducing the priority 
to 95. By decreasing the priority when the link fails, the second VRRP router takes over as the 
master. 
 
The configuration steps are as follows: 
Example BEB-3 with Corp VRF : 
->vrf corp vrf corp  
->vrf corp ip vrrp track 1 admin-state enable priority 25 address 10.90.250.2 
->vrf corp ip vrrp 1 interface "corp-wired" track-association 1 
->vrf corp ip vrrp 2 interface "corp-wlan" track-association 1 
->vrf corp ip vrrp 3 interface "corp-printers" track-association 1 
Repeat the step for the other VRFs and BEB-4. 
 
 

<<<PAGE 79>>>
 
22  
 
     
 
 
OSPF 
To learn the routes between each VRF and the PBR, we use OSPF.  
 
OSPF must be enabled on BEB-3, BEB-4, and the PBR. Each VRF is assigned to a unique OSPF area, 
while the default VRF is configured to operate in Area 0. 
Example with Corp VRF on BEB-3 and BEB-4: 
->vrf corp ip load ospf 
->vrf corp ip ospf area 0.0.0.1 
->vrf corp ip ospf interface "corp-pbr" 
->vrf corp ip ospf interface "corp-pbr" area 0.0.0.1 
->vrf corp ip ospf interface "corp-pbr" admin-state enable  
->vrf corp ip ospf admin-state enable 
Next, a local access list is created in each VRF. The subnets are grouped under a larger mask, and 
redistributed into OSPF using a route map. 
CORP 
 
Name 
Network 
corp-wired 
10.10.0.0/20 
corp-wlan 
10.10.16.0/20 
corp-printers 
10.10.47.0/24 
In our case, for Example, Corp subnets can be easily grouped into a 16 mask: 
->vrf corp ip access-list "local" 
->vrf corp ip access-list "local" address 10.10.0.0/16 action permit redist-control all-subnets 
->vrf corp ip route-map "local-to-ospf" sequence-number 50 action permit 
->vrf corp ip route-map "local-to-ospf" sequence-number 50 match ip-address "local" 
->vrf corp ip redist local into ospf route-map "local-to-ospf" admin-state enable 
 
 
 

<<<PAGE 80>>>
 
23  
 
     
 
 
Then proceed with the PBR configuration.  
Example with Corp VRF on PBR: 
->ip load ospf 
->ip ospf area 0.0.0.1 
->ip ospf interface "pbr-corp" 
->ip ospf interface "pbr-corp" area 0.0.0.1 
->ip ospf interface "pbr-corp" admin-state enable  
->ip ospf admin-state enable 
Repeat the same steps using a different area number for the other VRFs. 
Policies 
QoS 
Each service can communicate internally, but routing to another service requires passing through 
the PBR, which enforces the policies. For example, in our setup, a policy restricts the Guest VRF 
from communicating with other services.  
On PBR: 
->qos enable 
->policy network group corp 10.10.0.0 mask 255.255.0.0 
->policy network group guest 10.30.0.0 mask 255.255.0.0 
->policy network group rd 10.20.0.0 mask 255.255.0.0 
->policy network group utilities 10.50.0.0 mask 255.255.0.0 
->policy network group voice 10.40.0.0 mask 255.255.0.0 
->policy condition guest-voice-deny source network group guest destination network group voice  
->policy condition guest-corp-deny source network group guest destination network group corp  
->policy condition guest-rd-deny source network group guest destination network group rd  
->policy condition guest-utilities-deny source network group guest destination network group utilities  
->policy action ALLOW  
->policy action DENY disposition deny  
->policy rule guest-voice-deny precedence 30000 condition guest-voice-deny action DENY  
->policy rule guest-corp-deny condition guest-corp-deny action DENY  
->policy rule guest-rd-deny condition guest-rd-deny action DENY  
->policy rule guest-utilities-deny condition guest-utilities-deny action DENY  
->qos apply 
Notes 
While inter-VRF isolation is enforced by the PBR, for additional intra-VRF security (e.g. guest-to-guest isolation), it is advised 
to implement DHCP snooping, dynamic ARP inspection. 
 
Conclusion 
Shortest Path Bridging (SPB) stands out as a powerful yet straightforward technology, offering a 
simpler alternative to complex protocols like MPLS or EVPN. Widely supported across the Alcatel-

<<<PAGE 81>>>
 
24  
 
     
 
 
Lucent OmniSwitch portfolio—including stackable, modular chassis, and ruggedized industrial 
variants—SPB provides a versatile solution for diverse network environments. Its service-oriented 
architecture ensures seamless delivery of services to the desired locations, minimizing 
configuration efforts and enabling fully automated network deployments. 
This design provides a robust and flexible foundation for supporting the networking requirements 
of mid-sized enterprises. With scalability and efficient interconnectivity at its core, it can be easily 
expanded to meet the growing demands of larger organizations. Future considerations for multi-
campus routing and further integration details will ensure seamless network performance as the 
infrastructure evolves. 
Alternative Configuration 
Latest generation ASICs support integrated routing and bridging in the SPB domain in the exact same manner 
as in the VLAN domain. This means that IP interfaces can be associated with an SPB service directly and traffic 
can be routed between two SPB services or between a VLAN and an SPB service in a single-pass operation 
without loopbacks. We refer to this as single-pass inline routing. At the configuration level we simply need to 
specify the service number when configuring the IP interface. This section focus on alternate configuration. 
S-hook configuration 
Example on BEB-4: 
VLAN DOMAINE : 
->interfaces port 1/1/25 alias "SHook LAG-125 VLAN" 
->interfaces port 2/1/25 alias "SHook LAG-125 VLAN" 
->linkagg static agg 125 size 2 admin-state enable  
->linkagg static agg 125 name "SHook VLAN" 
->linkagg static port 1/1/25 agg 125 
->linkagg static port 2/1/25 agg 125 
->vlan 100 members linkagg 125 tagged 
->vlan 1000 members linkagg 125 tagged 
->vlan 1016 members linkagg 125 tagged 
->vlan 1047 members linkagg 125 tagged 
->vlan 1100 members linkagg 125 tagged 
->vlan 1116 members linkagg 125 tagged 
->vlan 1147 members linkagg 125 tagged 
->vlan 1200 members linkagg 125 tagged 
->vlan 1216 members linkagg 125 tagged 
->vlan 1247 members linkagg 125 tagged 
->vlan 1300 members linkagg 125 tagged 
->vlan 1316 members linkagg 125 tagged 
->vlan 1347 members linkagg 125 tagged 
->vlan 1400 members linkagg 125 tagged 
->vlan 1416 members linkagg 125 tagged 
->vlan 1447 members linkagg 125 tagged 
->vlan 1448 members linkagg 125 tagged 

<<<PAGE 82>>>
 
25  
 
     
 
 
->vlan 1449 members linkagg 125 tagged 
 
 
SERVICE DOMAINE : 
->interfaces port 1/1/26 alias "SHook LAG-127 SPB" 
->interfaces port 2/1/26 alias "SHook LAG-127 SPB" 
->linkagg static agg 127 size 2 admin-state enable  
->linkagg static agg 127 name "SHook SPB" 
->linkagg static port 1/1/26 agg 127 
->linkagg static port 2/1/26 agg 127 
->service access linkagg 127 vlan-xlation enable  
->service 100 sap linkagg 127:100 
->service 1000 sap linkagg 127:1000 
->service 1016 sap linkagg 127:1016 
->service 1047 sap linkagg 127:1047 
->service 1100 sap linkagg 127:1100 
->service 1116 sap linkagg 127:1116 
->service 1147 sap linkagg 127:1147 
->service 1200 sap linkagg 127:1200 
->service 1216 sap linkagg 127:1216 
->service 1247 sap linkagg 127:1247 
->service 1300 sap linkagg 127:1300 
->service 1316 sap linkagg 127:1316 
->service 1347 sap linkagg 127:1347 
->service 1400 sap linkagg 127:1400 
->service 1416 sap linkagg 127:1416 
->service 1447 sap linkagg 127:1447 
->service 1448 sap linkagg 127:1448 
->service 1449 sap linkagg 127:1449 
Related documents 
[1] 
ALE SPB Tech Brief – SPB Inline routing – Based Single Pass 
 
 
For more technical content, visit spacewalkers.com.  
 


<<<DOC 3: SPB/spb-solution-brief-en.pdf | 起始页 83 | 4p>>>

<<<PAGE 83>>>
Solution brief
Unlike STP, by enabling multiple active paths, SPB delivers more 
rapid convergence (from Rapid STP’s 2-3 seconds to SPB’s 100ms), 
fault tolerance, redundancy and shortest path determination. 
Furthermore, SPB is more than just an STP evolution. SPB 
addresses a multitude of network problems. It has been 
compared to Multiprotocol Label Switching (MPLS) in the 
Campus/Metro Area Network (MAN), but SPB is simpler to 
deploy and manage than MPLS, which requires a “stack” of 
protocols. SPB relies on a single protocol to move information 
efficiently within the network. 
Shortest Path Bridging:  
Versatile, simple and reliable 
  
802.1aq Shortest Path Bridging (SPB) is an IEEE networking standard 
focused primarily on addressing the shortcomings of the aging  
Spanning Tree Protocol (STP). 
SPB follows industry standards, ensuring compatibility with  
other technologies, and it combines physical hardware with 
virtual services, giving organizations the best of both worlds in 
terms of performance and flexibility. Overall, SPB streamlines 
networking, making it efficient, secure and adaptable to any 
organization’s needs.
SPB is a foundational technology at Alcatel-Lucent Enterprise, 
refined through years of investment and adaptation to market 
needs. Its proven reliability across diverse customers and 
industries sets it apart.
 

<<<PAGE 84>>>
Solution brief
Shortest Path Bridging: Versatile, simple and reliable
Benefits 
Shortest Path Bridging (SPB) is a networking technology that 
brings several benefits to businesses and organizations. 
Scalability
SPB is highly scalable, meaning it can easily handle growing 
amounts of data and devices without slowing down. This is 
perfect for organizations that want to expand their operations 
without worrying about their network performance. 
Security
Security lies within the network. Implementing SPB is the most 
effective method for establishing secure micro and macro network 
segmentation, a crucial element in constructing your Zero Trust 
Network Architecture (ZTNA). SPB ensures security by using a 
containerized approach, with separate compartments for different 
types of information, to prevent unauthorized access. This gives 
SPB the ability to support multi-tenancy securely and cost-effectively. 
It is also perfect for IoT integration, utilizing role-based access 
within the SPB network to onboard IoT devices securely and 
manage their network behavior.
Simplicity
SPB’s simplicity is a standout feature. It takes the complexity out 
of networking by automating the setup and configuration of 
connections between devices. This significantly reduces errors, 
minimizes downtime and optimizes time spent on repetitive 
tasks. It also enables hassle-free reconfiguration as changes in 
the SPB network need only be applied where services are added, 
modified or deleted. This adaptability allows organizations to 
maintain a dynamic and responsive network that can rearrange 
itself to fit organizations’ requirements. This means less time 
spent on technical setup and modifications and more time 
focusing on value-added work.
Reliability
SPB’s self-healing capabilities enhance network availability.  
Its fast convergence time ensures that if there’s a problem in  
the network, it recovers quickly. This reliability is crucial for 
organizations that can’t afford any downtime. 
Where to implement SPB 
Instead of implementing different solutions for the following 
applications, organizations can simplify operations by using  
SPB for all three. 
Campus LAN
In the Campus LAN, SPB is a perfect replacement for STP as it 
offers multiple load-balancing paths with optimal throughput, 
latency and built-in network redundancy. It can also solve the 
multi-tenancy problem, when multiple internal or external entities 
connected to the same network require isolation from one another. 
This same multi-tenancy capability enables efficient and secure 
micro and macro segmentation, making it ideal for IoT deployments 
and bringing organizations closer to achieving a ZTNA.
Data center
In the data center, SPB is a great solution both within the data 
center as well as to interconnect to other data centers. SPB 
provides any-to-any fabric connectivity over lower latency paths. 
It is also ideal for transforming data centers into private cloud 
environments quickly and easily.
Metro Area Networks 
In Metro Area Networks (MANs), SPB enables Layer 2 and 3 
services similar to MPLS but is much simpler and cheaper to 
operate. It provides multi-tenancy in multiple sites connected 
across the MAN. 

<<<PAGE 85>>>
Solution brief
Shortest Path Bridging: Versatile, simple and reliable
SPB in action
SPB is a versatile solution for various settings, including large campuses and verticals (military, universities, transportation, 
airports, energy, utilities, healthcare and smart cities) and mid-size to large data centers.
Sample vertical use cases
Education
•	Large campus / multi-site VPN,  
multi-tenancy
•	STP replacement
•	IoT containment
Transportation
•	VPN/syste, isolation (Rail/ITS)
•	Multi-tenancy (airport)
•	IoT containment
Energy & Utilities
•	STP replacement 
•	IoT containment 
•	VPNs, system isolation 
Service Providers
•	Large government facilities, MANs 
•	Multi-site VPNs 
•	Smart cities
Healthcare
•	Large hospital/Multi-site VPN
•	STP replacement
•	IoT containment 
(biomed devices
Hospitality
•	Large resort / casino
•	Multi-tenancy 
(gaming, CCTV, etc.)
•	IoT containment (door lock etc)
Government
•	Large government facilties,  
STP replacement
•	Multi-site VPNs for schools, hospitals 
andgovernment agencies
•	Smart cities

<<<PAGE 86>>>
© 2024 ALE International, ALE USA Inc. All rights reserved in all countries. The Alcatel-Lucent name and 
logo are trademarks of Nokia used under license by ALE. To view a list of proprietary ALE trademarks,  
visit: www.al-enterprise.com/en/legal/trademarks-copyright. DID24061101EN (June 2024)
To learn more, visit our Shortest Path Bridging web page.
Nevada Department of Transport
The Nevada Department of Transportation 
(NDOT) is responsible for the planning, 
construction, operation and maintenance 
of the 5400 miles of highway and over 
1000 bridges that make up Nevada’s 
state highway system. SPB allowed the  
IT team to create a scalable network 
while cutting the time it takes to roll out 
new devices, services and applications.
“The new solution makes it simpler to 
provide the best services throughout 
the 25 billion miles travelled by our 
road users annually, providing the 
right information for safe travel and 
ultimately reducing the time spent on 
the road. ALE went above and beyond 
throughout the entire process.” 
Gary Molnar, 
ITS Network Manager 
IDC Frontier
IDC Frontier, a 100%-owned subsidiary of 
Yahoo Japan Corporation, has nine data 
centers located throughout Japan with 
headquarters in Tokyo and a sales office 
in Osaka. IDC Frontier provides their 
customers with data center and cloud 
computing services. SPB provided them 
with the scalability required to serve their 
growing customer base and the level of 
resiliency that ensures their SLAs.
“At first we felt unsure if the  
Alcatel-Lucent Enterprise products  
we chose were right because it was 
new technology for us, and it also had 
to cover a geographically wide area  
of over 1000km between Kitakyushu 
City and Shirakawa City.; however, 
that concern evaporated when we 
realized the competitive edge of SPB 
technology and the stability of the 
OmniSwitch 6900 after performing  
a field test in our actual network.”
Mr. Tokuda, Network Group,  
Platform Engineering Department,  
Customer Service Division of IDC Frontier
University of Technology Sydney 
The University of Technology Sydney 
(UTS), renowned for its technical course 
offering, was founded in 1988. With 
more than 35,000 students and 3,500 
employees, as well as academics, the 
campus consists of 10 buildings on 
its main site with additional facilities 
across Sydney. SPB ensures that if 
there is a problem in one building, it 
does not affect another building. ALE 
infrastructure enables a move towards 
more virtual networking. It provides a 
scalable architecture to support more 
than 90% of the day-to-day activities  
UTS needs to run.
“Alcatel-Lucent Enterprise have 
helped us modernize our network 
infrastructure over the years, they 
have been a reliable partner on our 
growth journey. The guest experience 
for on-campus users was very critical 
for us, and operationally, we have 
reduced the time taken for providing 
guest access from hours to minutes, 
and the best part is, we don’t have to 
go out and test it every time because 
we know that it works!” 
Graham Redwood, Network Manager,  
University of Technology Sydney
Select customer case studies
