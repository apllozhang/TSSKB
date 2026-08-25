# sol-evpn-architecture — 解决方案文档合并（页码全册连续）


<<<DOC 1: evpn-architecture-guide-en.pdf | 起始页 1 | 73p>>>

<<<PAGE 1>>>
Architeture Guide 
EVPN 
 
 
 
 
 
EVPN Architecture Guide  

<<<PAGE 2>>>
Architeture Guide 
EVPN 
 
2 
Table of Contents 
About This Document ............................................................................. 4 
Purpose ............................................................................................................................ 4 
Audience ........................................................................................................................... 4 
Scope ................................................................................................................................ 4 
Introduction ............................................................................................ 5 
VXLAN Overview .............................................................................................................. 6 
Proactive vs Reactive Learning Model .......................................................................... 7 
EVPN Use Cases ....................................................................................... 8 
Data Centre Fabric .......................................................................................................... 8 
Enterprise Campus Fabric .............................................................................................. 8 
EVPN Fundamentals ............................................................................... 9 
EVPN Terminology .......................................................................................................... 9 
Control Plane ................................................................................................................. 10 
EVPN Route-Types ................................................................................................................. 11 
Route Distinguisher and Route Target ............................................................................... 19 
EVPN Service Interface Models ........................................................................................... 19 
ARP Suppression and Proxy ARP ......................................................................................... 20 
EVPN Extended Communities .............................................................................................. 21 
Integrated Routing and Bridging ....................................................................................... 23 
Distributed Anycast Gateway .............................................................................................. 28 
Data Plane ...................................................................................................................... 29 
BUM Traffic Handling ........................................................................................................... 29 
Intra-subnet Communication - Bridging ............................................................................ 30 
Inter-subnet Communication - Routing ............................................................................. 31 
Multi-homing ................................................................................................................. 32 
Multicast Optimizations ............................................................................................... 36 
Multicast Switching .............................................................................................................. 36 
Multicast Routing ................................................................................................................. 37 
MAC and IP Mobility Service ........................................................................................ 39 
Silent Hosts .................................................................................................................... 40 
AOS EVPN Model and Differentiators ................................................. 40 

<<<PAGE 3>>>
Architeture Guide 
EVPN 
 
3 
AOS EVPN ESI Model ............................................................................................................. 40 
AOS Service Interface Model ............................................................................................... 41 
Auto-generated RD/RT for Various Route Types ............................................................... 42 
AOS Multicast Optimizations ............................................................................................... 43 
EVPN Architecture Design ................................................................... 44 
Network Topology Recommendations ....................................................................... 44 
Underlay/Overlay Design Options .............................................................................. 45 
External Connectivity .................................................................................................... 46 
Border Leaf Connectivity Considerations .......................................................................... 48 
EVPN Configuration Example .............................................................. 48 
OSPF Underlay Configuration ..................................................................................... 49 
BGP Overlay Configuration .......................................................................................... 57 
Verification Commands ........................................................................................................ 60 
Link Aggregation Configuration ................................................................................. 60 
Verification Commands ........................................................................................................ 61 
VRF/Fabric-VPN Configuration .................................................................................... 61 
Verification Commands ........................................................................................................ 63 
EVPN-VXLAN Service Access Port and Multi-Homing Configuration ...................... 64 
Verification Commands ........................................................................................................ 64 
EVPN-VXLAN Services Provisioning ............................................................................. 65 
Verification Commands ........................................................................................................ 66 
Symmetric IRB Configuration ...................................................................................... 67 
Verification Commands ........................................................................................................ 68 
DAG Configuration ........................................................................................................ 68 
Verification Commands ........................................................................................................ 68 
External Route Advertisement .................................................................................... 70 
Verification Commands ........................................................................................................ 70 
Proxy ARP Configuration .............................................................................................. 71 
Verification Commands ........................................................................................................ 71 
Conclusion ............................................................................................. 72 
Related Documents .............................................................................. 73 
 
 

<<<PAGE 4>>>
Architeture Guide 
EVPN 
About This Document 
Purpose 
The purpose of this design guide is to present general EVPN fundamentals, reference design 
concepts, and deployment guidelines for the Alcatel-Lucent Operating Software (AOS) 
implementation of MP-BGP EVPN for VXLAN. 
 
Audience 
The intended audience for this document includes customer and business partner networking 
professionals involved in the design and deployment of enterprise and data center networks. 
 
Scope 
This document does not attempt to cover every aspect, nor every possible architecture 
option; but only the most common, validated and recommended architectures.  
This document will provide an overview of the technology and some features which will be 
presented but might not be supported in the first release of MP-BGP EVPN in AOS. An 
updated version of this document may be published once such features are available. 
Supported features will be presented in the Implementation section of this document. 
The MP-BGP EVPN for VXLAN first supported release is 8.10R1 and supported on the 
OmniSwitch 6900 platform. This document has been updated for the 8.10R3 release. 
You are encouraged to refer to the AOS documentation for additional details, options and 
guidelines, as referenced in the Related Documents section. 
 
 
 
 
 
 
 
 
 
 

<<<PAGE 5>>>
Architeture Guide 
EVPN 
Introduction 
Before we dive in to how Ethernet Virtual Private Network (EVPN) works, we should first 
understand the drivers that led to creating this technology. Data center technologies evolved 
to support scalability, resiliency, multi-tenancy, and flexibility for host mobility and multi-
homing, driven by recent shifts towards virtualization, cloud deployment, distributed 
microservices architectures, and increased east-west traffic (server-to-server communication). 
Modern data centers required an evolution from the traditional flood-and-learn and VLAN 
segmentation networking due to the limitations placed on such model, including: 
• 
Inefficient use of resources: The use of Spanning Tree Protocol (STP) led to inefficient 
use of resources due to blocked redundant links as shown below. It was also complex, 
slow to converge, and had inter-operating issues between different versions. 
 
• 
Stability issues: Broadcast storms and endless Layer 2 loops (due to lack of TTL in Layer 2 
frames) can cause instability of the entire infrastructure.  
• 
Scalability issues since VLAN segmentation allows for a 12-bit VLAN ID, which has an 
upper limit of 4096 VLANs. This is very restrictive specifically in data center environments 
due to the development of virtualization and containerization technologies.  
• 
Operational complexity and administrative tax: VLANs are also required to be 
configured at every switch in the network for host mobility and should be tagged on every 
link. 
• 
Traffic tromboning issues: Inter-VLAN traffic flows could suffer a “trombone” effect and 
follow a sub-optimal path for east-west traffic. This is due to having a static first-hop 
router. 
These and many more reasons drove the creation of VXLAN technology. We will cover an 
overview of VXLAN technology and understand its weaknesses and how this eventually led to 
the development of EVPN technology.

<<<PAGE 6>>>
Architeture Guide 
EVPN 
VXLAN Overview 
Virtual eXtensible Local Area Network (VXLAN) is a standards-based Layer 2 overlay 
technology, as defined in RFC 7348, that is used to encapsulate and tunnel traffic through a 
Layer 3 IP network. It is primarily used in data center or cloud network infrastructures.  
VXLAN technology is similar to other tunneling and network virtualization solutions, such as 
Shortest Path Bridging (SPB), in that an encapsulation technique is used to tunnel device 
traffic through the network. The technique implemented with the VXLAN technology 
encapsulates an Ethernet MAC frame received from a host (usually a VM) into an IP packet 
with a UDP header, then forwards the packet on a Layer 3 network. 
The following terms and definitions describe the VXLAN components: 
• 
VXLAN segment: A VXLAN Layer 2 overlay network used to tunnel traffic between hosts. 
Each segment is identified with a VXLAN network identifier (VNI), which is similar to a 
VLAN I
• 
D (used to segment network traffic into virtual bridging domains). Only hosts associated 
with the same VXLAN segment can communicate with each other. 
• 
VXLAN Network Identifier (VNI): A 24-bit number that identifies a VXLAN segment (also 
referred to as a VXLAN segment ID). A VNI is used to associate a host MAC frame with a 
VXLAN segment when the frame is encapsulated with a VXLAN header. 
• 
VXLAN Tunnel Interface (VTI): A UDP tunnel that forwards encapsulated VXLAN packets 
between VXLAN Tunnel End Points (VTEPs). A VTI is treated as just another Layer 2 
interface within a bridging domain. 
• 
VXLAN Tunnel End Point (VTEP): The device configured with one or more VTIs. The VTEP 
provides an initiation and termination point for each VXLAN segment bound to the VTI. 
This is the point at which Layer 2 host frames are encapsulated and sent through the 
tunnel or the encapsulation header is removed from a VXLAN packet and the Layer 2 host 
frames are forwarded on a traditional VLAN domain. 
• 
VXLAN gateway: A device that serves as a VTEP to transparently bridge traffic between 
VXLAN and traditional VLAN domains. A VXLAN gateway switch represents a single VTEP 
on which multiple VTIs may exist. 

<<<PAGE 7>>>
Architecture Guide 
 
 
The VTEP can be a host or network device (gateway switch). This allows for many different 
VTEP options or models: Host-to-host, host-to-gateway, or gateway-to-gateway. 
VXLAN brings many benefits into the network. It: 
• 
Provides Layer 2 connectivity between devices in the same VLAN over an IP transport 
network. For example, a VM can communicate across a Layer 3 network with a remote 
VM as long as both VMs reside in the same VLAN domain on either side of the Layer 3 
network. 
• 
Increases the scalability of the network beyond the limit of 4096 VLANs. A VNI is used 
to isolate VLAN traffic into logical network segments. Up to approximately 16 million 
logical networks (VNIs) are possible when VXLAN is implemented. 
• 
Transparently extends the Layer 2 network by connecting VLANs from multiple hosts 
through VXLAN (UDP) tunnels. 
• 
Provides entropy through the VXLAN UDP header for load-balancing traffic across the 
fabric.  
• 
Provides Layer 2 migration of a host (VM) across a Layer 3 infrastructure to a remote 
server host; without VXLAN, Layer 2 migration is restricted to other servers within the 
local Layer 2 broadcast domain. 
Even with all those benefits of using VXLAN in your network, you will still need a 
mechanism to learn the MAC Addresses of connected hosts. This can be done using the 
reactive flood-and-learn method or using an intelligent control plane protocol such as MP-
BGP EVPN which uses a proactive learning model. 
Proactive vs Reactive Learning Model 
In the traditional flood-and-learn reactive learning model, in case the destination MAC 
address is unknown, when a switch recieves traffic from a connected host, it will flood this 
traffic along the path where the broadcast domain is extended. Switches in turn learn the 
MAC address based on this flood-and-learn behaviour through the data plane. In a VXLAN 
enabled network, this model requires a multicast-enabled underlay to discover remote 

<<<PAGE 8>>>
Architecture Guide 
EVPN 
8 
VTEPs and to learn endpoint MAC addresses. This adds complexity to the architecture. 
Furthermore, to route between different bridging domains, you will be required to route 
to a centralized gateway. 
In the proactive learning model, which is used by MP-BGP EVPN, endpoint reachability 
information is advertised intelligently through the control plane within MP-BGP Network 
Layer Reachability Information (NLRI) updates. 
 
EVPN Use Cases 
There are many use cases for MP-BGP EVPN; whether in the DC, Data Center Interconnect 
(DCI), the enterprise campus, or in a service provider network. EVPN allows for a single 
control plane protocol to provide Layer 2 and Layer 3 services. 
Data Centre Fabric 
EVPN-VXLAN provides a scalable and efficient multitenant solution in modern data 
centers. A common topology used is spine-and-leaf or Clos architecture. It can be 2-tier (3-
stage) or 3-tier (5-stage) depending on the scale. A fully-routed underlay architecture is 
used with OSPF/IS-IS or only eBGP, and enabling EVPN-VXLAN as your overlay protocol 
using e/iBGP. We will discuss different considerations in the Underlay/Overlay Design 
Options and Best Practices section. 
Using spine-and-leaf topology allows for optimum performance in the DC when using 
EVPN. Benefits include: 
• 
Simple and non-blocking network 
• 
The routed architecture eliminates STP issues. 
• 
Guaranteed qual cost paths between peer PE switches (leaf switches) which 
provides better load-balancing.  
• 
Modularity and horizontal scalability of the fabric. If required to add more capacity, 
leaves and/or spines can be added as needed. 
• 
Predictable, consistent bandwidth and latency. The number of hops between two 
hosts is always the same. 
Spine nodes can also be used as border gateway nodes in a multi-site EVPN-VXLAN 
network. This can be considered for future scalability requirements. 
A 3-tier (5-stage) spine-leaf topology can be used for requirements with hyper scalability 
for DCI. Here, the topology will consist of a Super-Spine layer that provides the inter-site 
gateway functionality. This is especially beneficial when the core network (Inter-site) is 
operating in a different overlay protocol (for example, MPLS) or when it is required to 
have a decoupled intra-site and inter-site operation to sustain the complexity of a multi-
site EVPN network. 
Enterprise Campus Fabric 
EVPN-VXLAN campus fabric can be built using the standard two or three-tier heirarchichal 
design or using spine-and-leaf architecture similar to modern DC designs. 

<<<PAGE 9>>>
Architecture Guide 
EVPN 
9 
Using EVPN-VXLAN in your enterprise campus network brings many benefits including: 
• 
Simplicity: unified control plane allows for simple add/remove operations.  
• 
Micro-segmentation and multi-tenancy through the use of VRFs/RDs/RTs. This is 
useful in IoT environments. We will define these terminologies in an upcoming 
section. 
• 
Security: use of RT provides better control of route import/export. This allows for 
a common security policy across the enterprise campus fabric. 
• 
Scalability: EVPN allows extension of Layer 2 fabric over large architectures 
 
EVPN Fundamentals 
MP-BGP EVPN is a control plane protocol for VXLAN based on RFC 7342 and RFC 8365. 
Prior to EVPN, VXLAN overlay networks operated using the flood-and-learn learning model 
where the end-host reachability information and VTEP discovery are both data-plane 
based. The VTEPs can also be setup manually on the leaf switches. There was no control 
protocol to distribute end-host reachability information among VTEPs. The overlay 
Broadcast, Unknown unicast, and Multicast (BUM) traffic is encapsulated into multicast 
VXLAN packets and transported to remote VTEP switches through the underlay multicast 
forwarding. Constant flooding over the fabric in such a deployment in order to maintain 
accurate end-host reachability information can present a challenge for scalability. 
MP-BGP EVPN changes this model and uses a proactive approach for end-host reachability 
information learning. It provides a separate control plane for VXLAN tunnels.  
Key benefits of choosing MP-BGP EVPN as your network fabric technology: 
• 
Unified Control Plane: a single control plane protocol that supports Layer 2 and Layer 
3 VPN services and allows for seamless integration. It has many use cases in the DC, 
Data Center Interconnect (DCI), enterprise campus, and more.  
• 
Scalability/Efficiency: EVPN features such as multi-homing, aliasing, ARP 
suppression, mass withdrawal, Distributed Anycast Gateway (DAG), MAC mobility, and 
EVPN multicast optimizations provide an efficient network fabric that easily scales. 
• 
Flexibility: MP-BGP EVPN can run on multiple transport technologies such as VXLAN, 
Multiprotocol Label Switching (MPLS), Provider Backbone Bridging (PBB), and more. 
This provides flexibility. It is also a standards-based technology supported by many 
vendors which allows for inter-operability. 
• 
Better Security and Control: MP-BGP EVPN allows the delivery of multi-tenant 
services across a shared infrastructure using Virtual routing and forwarding (VRF) 
instances, VNIs, Route Distinguishers (RDs), and Route Targets (RTs) for segmentation 
and control. 
EVPN Terminology  
Let’s go through a few key terminologies for EVPN: 
• 
Ethernet VPN Instance (EVI): It is a EVPN forwarding and routing instance which 
spans across all the PE devices in the EVPN network. It is configured per-customer 

<<<PAGE 10>>>
Architecture Guide 
EVPN 
10 
basis and consists of Route Distinguisher (RD) and Route Target (RT). We will cover 
RD/RT in an upcoming section. 
• 
Broadcast Domain (BD): a BD may correspond to an EVI or an EVI may contain 
multiple BDs depending on the service model used. This is explained in the EVPN 
Service Interface Models section. 
• 
Ethernet Segment (ES): It is a set of Ethernet link connecting a group of PEs. 
• 
Ethernet Segment Identifier/Index (ESI): It is a unique non-zero identifier (Example: 
11:22:33:44:55:66:77:88:99) used to identify an ES. The ESI is required by the multi-
homing CEs. 
• 
Ethernet Tag (ETag): It idenitifes a particular broadcast domain, such as a VLAN. Its 
value is the VLAN ID associated with the SAP. 
• 
MAC-VRF: A Virtual Routing and Forwarding (VRF) table for MAC addresses for a single 
EVI. 
• 
IP-VRF: A VRF table for IP routes on a PE. 
Other terminologies: 
• 
Service Access Point (SAP): A SAP is a logical service entity (also referred to as a 
virtual port) that is configured on a PE to bind an access port to a service and specify 
the type of customer traffic (untagged, single-tagged, double-tagged, or all) to 
encapsulate and tunnel through the overlay network. 
• 
Provider Edge (PE): It is the device is where the services originate and terminate, and 
where all the necessary tunnels are setup to connect to all the other PE. It is owned 
and managed by the service provider. It is connected directly to the CE. 
• 
Customer Edge (CE): The host, switch, or router that is located at the customer 
premises which can be owned and managed by the customer or the service provider.  
A few other remaining terminologies will be covered in the relevant sections. 
Control Plane 
EVPN introduces a new address family, EVPN, to the MP-BGP protocol family. The EVPN 
NLRI is carried in BGP using BGP Multiprotocol Extensions with an Address Family (AFI) of 
25 (L2VPN) and a Subsequent Address Family Identifier (SAFI) of 70 (EVPN). In order for 
two BGP speakers to exchange labeled EVPN NLRI, they must use the BGP Capabilities 
Advertisement to ensure that they both are capable of properly processing such NLRI. 
The MP-BGP EVPN control plane provides protocol-based VTEP peer discovery as well as 
end-host reachability information distribution that allows more scalable VXLAN overlay 
network designs. The MP-BGP EVPN control plane introduces a set of features that 
reduces or eliminates traffic flooding in the overlay network and enables optimal 
forwarding of traffic. It reduces network flooding through protocol-based MAC/IP route 
distribution and ARP suppression on the local PE switches.  
 
PE and VTEP are used interchangebly in this document. 

<<<PAGE 11>>>
Architecture Guide 
EVPN 
11 
EVPN Route-Types 
The below table lists the primary EVPN Route-Types (R-Ts) which are used in EVPN NLRI: 
 
 
Route 
Type 
Description 
RFC 
Purpose 
Type 1 
Ethernet 
Auto-
Discovery (A-
D) Route 
RFC 
7432 
Used in multi-homing scenarios to announce the 
reachability of a multi-homed ES. It is also used for 
aliasing (load-balancing) and backup path features, 
loop avoidance with split-horizon filtering, and mass 
withdraw (fast-convergence). 
Type 2 
MAC/IP 
Advertisemen
t Route 
RFC 
7432 
Used to advertise end-host MAC reachability 
information between PEs and optionally IP prefix 
routes. It also allows the PE to perform ARP 
suppression/proxy ARP. 
Type 3 
Inclusive 
Multicast 
Ethernet Tag 
(IMET) Route  
RFC 
7432 
Used to to exchange information about the location 
of the VTEPs on a per-VNI basis, thereby enabling 
automatic discovery. It is mostly used for ingress 
replication of BUM traffic. 
Type 4 
ES Route 
RFC 
7432 
Used for multi-homing scenarios to discover which 
PEs are attached to the same shared ES as well as 
performing the DF Election process. 
Type 5 
IP Prefix 
Route 
RFC 
9136 
Used for the advertisement of IP prefix and next-hop 
information. It can be used for L3VPN services and in 
case external connextivity is required. 
Type 6 
Selective 
Multicast 
Ethernet Tag 
(SMET) Route 
RFC 
9251 
Used for support of Internet Group Management 
Protocol (IGMP)/Multicast Listener Discovery (MLD) 
proxy functionality and to distribute multicast traffic 
interest by hosts for (*,G) or (S,G) 
Type 7 
Multicast 
Membership 
Report Synch 
Route 
RFC 
9251 
It is used to synchronize IGMP Join state information 
between multi-homed nodes which are attached to 
the same ES 
Type 8 
Multicast 
Leave Synch 
Route 
RFC 
9251 
It is used to synchronize IGMP Leave state 
information between multi-homed nodes which are 
attached to the same ES 
The shaded R-Ts in the table above are the primary used R-Ts for basic EVPN host route 
and VNI advertisements. 
Let’s discuss these route types further.  
We will use RT to abbreviate Route Target and R-T to abbreviate Route Types 
throughout this document.  

<<<PAGE 12>>>
Architecture Guide 
EVPN 
12 
 
 
Route Type 1 – Ethernet Auto-Discovery Route 
R-T1 is used for three purposes: aliasing, split horizon (loop prevention), and mass 
withdrawal features. These will be covered further in the Multi-homing section. 
R-T1 BGP NLRI encoding, as per RFC 7432, consists of the following fields: 
 
Route Distinguisher (8 octets) 
Ethernet Segment Identifier (ESI) (10 octets) 
Ethernet Tag ID (4 octets) 
MPLS Label/L2VNI (3 octets) 
 
The ESI field specifies the ES where the MAC address was learnt.  
The Ethernet Tag ID (Etag) is a 32-bit field containing either a 12-bit or 24-bit identifier 
that identifies a particular broadcast domain (e.g., a VLAN) in an EVPN instance. The usage 
of Ethernet Tag ID is discussed below in the subtypes of A-D Routes.  
The MPLS label field specifies the service tunnel identifier. For VXLAN, it is the VNI of the 
EVPN service. 
In addition to the EVPN BGP NLRI, this R-T may include other path attributes in the BGP 
update message, depending on the route subtype: 
• 
BGP Path Attributes: Origin (IGP), AS_PATH, Local_Pref (100)… 
• 
“MP_REACH_NLRI” path attribute 
• 
RT Extended Community 
• 
BGP Tunnel Encapsulation Extended Community 
• 
ESI Label Extended Community 
Extended communities are further discussed in EVPN Extended Communities section.  
There are two subtypes of A-D Routes: 
1. Ethernet A-D Route per ESI (R-T1A): This route is used for fast convergence 
scenarios and allows PE devices to change the next-hop adjacencies for all MAC 
addresses associated with a particular ESI (mass withdrawal). It is also used as a 
split horizon filter for all-active multi-homing and to signal the multi-homing status 
of the ES (and the disposition of the ES: single-active or all-active) to the EVPN 
network. This information is carried in the ESI Label Extended Community which 
we will discuss in the EVPN Extended Communities section. It is received by all the 
Please note that when a PE is sending a BGP update message, other path 
attributes and extended communities maybe added to the EVPN NLRI, depending 
on the route type, to the BGP update message. 

<<<PAGE 13>>>
Architecture Guide 
EVPN 
13 
participating EVPN nodes but only imported into the control-plane if there is a local 
service (EVI) which matches a service in the RT set in the advertised route. ETag will 
be set to 0xFFFFFFFF (or 4294967295).  
2. Ethernet A-D Route per EVI (R-T1B): This route is used for aliasing (load-
balancing), backup path, and service carving features which allow traffic to be 
balanced across multiple egress points. It contains the ESI to EVI association of a 
PE (SAP to Service attachments). In this route, the ETag is a non-zero value. 
This route type and the features provided will be covered in more detail in the Multi-
homing section. 
Route Type 2 – MAC/IP Advertisement Route 
The main purpose of R-T2 MAC/IP route is to advertise locally learnt host MAC addresses 
on SAP ports and advertise them to the remote peer PE. It is also used for other features 
such as ARP suppression (proxy ARP). We will cover the Proxy ARP functionality in the ARP 
Suppression and Proxy ARP section.  
R-T2 can include MAC address or MAC+IP address. The MAC and MAC+IP will be advertised 
as separate messages for both updates and withdraw. If switch learns MAC address when 
the host is connected, then only the MAC address is sent. If switch learns through 
gratuitous ARP (for duplicate IP address detection) sent from the host which includes both 
the MAC and IP address, then both are sent in different updates. The MAC-VRF will 
maintain separate DBs for MAC entry and the MAC+IP.  
MAC address table aging will be disabled for all MAC address learnt from the EVPN control 
plane. Even in case of addresses advertised from peer nodes of a local ESI, the addresses 
are learnt on the SAPs with a static disposition to disable aging until the peer PE will 
withdraw the route address. 
As defined in RFC 7432, the MAC/IP Route BGP NLRI encoding consists of the following 
fields: 
 
Route Distinguisher (8 octets) 
Ethernet Segment Identifier (ESI) (10 octets) 
Ethernet Tag ID (4 octets) 
MAC Address Length (1 octet) 
MAC Address (6 octets) 
IP Address Length (1 octet) 
IP Address (0, 4, or 16 octets) 
MPLS Label 1 – L2VNI (3 octets) 
MPLS Label 2 – L3VNI (0 or 3 octets) 

<<<PAGE 14>>>
Architecture Guide 
EVPN 
14 
 
The MAC address and MAC address length are used to advertise and receive the local and 
remote MAC addresses in the MAC-VRF tables. The IP address and IP address length fields 
are optional. The IP address would be 4 octets for IPv4 and 16 octets for IPv6. 
The L2VNI and L3VNI fields replace the MPLS Label 1 and Label 2 fields specified in RFC 
7432 to support VXLAN. The L3VNI is optional. 
In addition to the EVPN BGP NLRI, this R-T may include other path attributes in the BGP 
update message, depending on the route subtype: 
• 
BGP Path Attributes: Origin (IGP), AS_PATH, Local_Pref (100)… 
• 
“MP_REACH_NLRI” path attribute 
• 
RT Extended Community 
Extended communities are further discussed in EVPN Extended Communities section.  
Route Type 3 - Inclusive Multicast Ethernet Tag (IMET) Route 
This R-T is used for the auto-discovery of remote peers that are part of the same EVI to set 
up the BUM tunnels (flooding lists) over VXLAN. Multicast traffic such as control plane 
frames (ex: BPDUs) can be forwarded on these tunnels. Broadcast frames can also be 
forwarded using the EVI distribution tunnels but is generally not recommended since the 
FDB learning and ARP suppression mechanism is relied upon to reduce the flood traffic in 
the network. 
This route is advertised to all nodes but only imported into the control plane by only those 
nodes that have an EVI which matches the advertised RT EVI of the R-T3 frame. 
As specified in RFC 7432, the IMET route type BGP NLRI encoding consists of the following 
fields:  
 
Route Distinguisher (8 octets) 
Ethernet Tag ID (4 octets) 
IP Address Length (1 octet) 
Originating Router’s IP Address (4, or 16 octets) 
 
The IP address and IP address length fields are for the originating PE. The IP address 
would be 4 octets for IPv4 and 16 octets for IPv6. 
In addition to the EVPN BGP NLRI, this R-T may include other path attributes in the BGP 
update message, depending on the route subtype: 
• 
BGP Path Attributes: Origin (IGP), AS_PATH, Local_Pref (100)… 
• 
“MP_REACH_NLRI” path attribute 
• 
BGP Tunnel Encapsulation Extended Community 
• 
RT Extended Community 

<<<PAGE 15>>>
Architecture Guide 
EVPN 
15 
• 
Provider Multicast Service Interface (PMSI) path attribute 
Extended communities are further discussed in EVPN Extended Communities section.  
When sending R-T3 IMET routes, PMSI tunnel attributes will be included to identify the 
provider tunnel (P-Tunnel) used for sending BUM traffic. These attributes include the 
tunnel type (ingress replication), the MPLS label (L2VNI in case of VXLAN), the tunnel 
identifier (destination IP address), and other flags. The tunnel type is set to ingress 
replication if this method is used for BUM traffic replication. 
We will cover this route type further in the BUM Traffic Handling section. 
Route Type 4 – Ethernet Segment Route 
This R-T is used exclusively for EVPN multi-homing scenarios. It is used to discover PEs 
which are attached to the same ES and for DF election. This R-T is only generated by multi-
homed PEs for each ESI configured on the PE node. 
As specified in RFC 7432, the ES Route BGP NLRI encoding consists of the following fields:  
 
Route Distinguisher (8 octets) 
Ethernet Segment Identifier (10 octets) 
IP Address Length (1 octet) 
Originating Router’s IP Address (4, or 16 octets) 
 
The IP address would be 4 octets for IPv4 and 16 octets for IPv6. 
In addition to the EVPN BGP NLRI, this R-T may include other path attributes in the BGP 
update message, depending on the route subtype: 
• 
BGP Path Attributes: Origin (IGP), AS_PATH, Local_Pref (100)… 
• 
“MP_REACH_NLRI” path attribute 
• 
ESI Label Extended Community 
• 
ES-Import Route Target Extended Community 
• 
DF Election Extended Community 
Extended communities are further discussed in EVPN Extended Communities section.  
We will discuss this R-T further in the Multi-homing Features section. 
Route Type 5 – IP Prefix Route 
R-T5 is used to advertise IP prefixes rather than host MAC or MAC/IP as advertised in R-T2. 
It can be used for external communication and to summarize routes (such as default 
route). It also provides the ability to provide L3VPN services. IP prefixes of any length can 
be advertised using R-T5. Host routes (/32) are usually advertised using R-T2, while prefix 
routes are advertised using R-T5. 
R-T5 can also be advertised with an overlay index for recursive route lookup to determine 
the egress PE. This overlay index can be a gateway IP address, MAC address, or ESI, which 

<<<PAGE 16>>>
Architecture Guide 
EVPN 
16 
will be encoded accordingly in the R-T5 message or set ot all zeros. In case MAC address 
overlay index is used, then router MAC extended community. This is further discussed in 
the EVPN Extended Communities section. It can also be advertised without an overlay 
index, but will use the BGP next-hop as the egress PE. In this case, the L3VNI field in the R-
T5 NLRI will be encoded. Otherwise it will be set to zero. 
As per RFC 9136, the IP Prefix Route BGP NLRI encoding consists of the following fields: 
 
Route Distinguisher (8 octets) 
Ethernet Segment Identifier (10 octets) 
Ethernet Tag ID (4 octets) 
IP Address Length (1 octet) 
IP Address (4 octets for IPv4, 16 octets for IPv6) 
Gateway IP Address (4 octets for IPv4, 16 octets for IPv6) 
MPLS Label – L3VNI (3 octets) 
 
The primary fields for the R-T is RD, IP Prefix and IP Prefix Length. Rest of the fields are 
optional.  
 
Route Type 6 – Selective Multicast Ethernet Tag (SMET) Route 
This route type is used to support the IGMP/MLD proxy functionality and to distribute 
multicast traffic interest by hosts for (*,G) or (S,G). The SMET Route BGP NLRI encoding 
consists of the following fields: 
 
Route Distinguisher (8 octets) 
Ethernet Tag ID (4 octets) 
Multicast Source Length (1 octet) 
Multicast Source Address (Variable) 
Multicast Group Length (1 octet) 
R-T5 is supported starting release 8.10R2 

<<<PAGE 17>>>
Architecture Guide 
EVPN 
17 
Multicast Group Address (Variable) 
Originator Router IP Address Length (1 octet) 
Originator Router IP Address (variable) 
Flags (1 octet) 
 
For the purpose of BGP route key processing, all the fields are considered to be part of 
the prefix in the NLRI, except for the Flags field. 
For (S,G): 
• 
The Multicast Source Address is the source IP address from the IGMP Membership 
Report . 
• 
The Multicast Source Length is usually 32 for IPv4 and 128 for IPv6. 
For (*,G): 
• 
The Multicast Source Address field is not used. 
• 
The Multicast Source Length is 0. 
The Multicast Group Length and Address is the group address and length from the IGMP 
Membership Report. 
The Originator Router IP Address and IP Address Length is the IP address and length of 
the router originating this route. 
This R-T is further explained in the Multicast Optimizations section. 
Route Type 7 – IGMP/MLD Join Synch 
This route type is used to synchronize IGMP Join state information between multi-homed 
nodes which are attached to the same ES.  
The BGP NLRI encoding consists of the following fields: 
 
Route Distinguisher (8 octets) 
Ethernet Segment Identifier (10 octets) 
Ethernet Tag ID (4 octets) 
Multicast Source Length (1 octet) 
Multicast Source Address (Variable) 
Multicast Group Length (1 octet) 
Multicast Group Address (Variable) 

<<<PAGE 18>>>
Architecture Guide 
EVPN 
18 
Originator Router IP Address Length (1 octet) 
Originator Router IP Address (variable) 
Flags (1 octet) 
 
This route type carries exactly one ES-Import Route Target extended community which 
corresponds to the ES on which the IGMP Membership Report was received. Extended 
communities are further discussed in the EVPN Extended Communities section. 
The fields are similar to R-T6 and are self-explanatory. 
This R-T is further explained in the Multicast Optimizations section. 
Route Type 8 – IGMP/MLD Leave Synch 
This route type is used to synchronize IGMP Leave state information between multi-
homed nodes which are attached to the same ES.  
The BGP NLRI encoding consists of the following fields: 
 
Route Distinguisher (8 octets) 
Ethernet Segment Identifier (10 octets) 
Ethernet Tag ID (4 octets) 
Multicast Source Length (1 octet) 
Multicast Source Address (Variable) 
Multicast Group Length (1 octet) 
Multicast Group Address (Variable) 
Originator Router IP Address Length (1 octet) 
Originator Router IP Address (variable) 
Reserved (4 octets) 
Maximum Response Time (1 octet) 
Flags (1 octet) 
 

<<<PAGE 19>>>
Architecture Guide 
EVPN 
19 
Similar to R-T7, this route type must carry exactly one ES-Import Route Target extended 
community which corresponds to the ES on which the IGMP Leave was received. Extended 
communities are further discussed in the EVPN Extended Communities section. 
The Maximum Response Time field is the value used while sending the query. The 
remaining fields are similar to R-T7 and are self-explanatory.  
This R-T is further explained in the Multicast Optimizations section. 
 
Route Distinguisher and Route Target 
Similar to MPLS L3VPNs, the new EVPN address family also provides multi-tenant 
separation and allows for overlapping addresses between tenants. To maintain the 
separation, it uses: Route Distinguishers (RDs) and Route Targets (RTs). In the AOS 
EVPN Model, the RD and RT are auto-generated as explained in the Auto-generated RD/RT 
for Various Route Types section. 
The RD makes overlapping routes from different tenants (VRFs) unique. In EVPN, it is used 
to distinguish routes between EVIs in case of overlaps. The 8-octet RD is prepended to 
each advertised route before the route is sent to its MP-BGP EVPN peer. EVPN uses Type-1 
RD, as defined in RFC 4364, which is derived from the Router ID (Loopback0) if it is auto-
generated. It can be also manually configured. 
EVPN also makes use of the RT extended community for route filtering and separating 
tenants. The RT, which is 6-bytes, is advertised in the MP-BGP update message along with 
the EVPN routes, and is not part of the MP-BGP NLRI itself. It is usually auto-derived from 
the Etag (VLAN) and the ASN, but can also be manually configured. An EVPN route can 
have multiple RTs. The RT extended community distinguishes which routes should be 
exported from and imported into a specific MAC-VRF table on a PE. If the export RT in the 
received update matches the import RT of an EVI on the PE receiving the update, the 
corresponding routes will be imported into that EVI’s MAC-VRF table. If the RTs do not 
match, the route will not be imported. 
EVPN Service Interface Models 
There are different EVPN Etag service interfaces as mentioned in RFC 7432:  
 
• 
VLAN-based Service Model: This model follows a one-to-one mapping where each 
VLAN is mapped to a dedicated MAC-VRF, which is mapped to a dedicated VNI, which is 
mapped to a dedicated EVI. This will allow for overlapping MAC addresses across 
VLANs. VLAN translation can be performed where the incoming VLAN tag is stripped 
on the ingress PE and another is added on the egress PE. There is a single broadcast 

<<<PAGE 20>>>
Architecture Guide 
EVPN 
20 
domain per EVI. In case this service model is used, The ETag in all EVPN routes MUST 
be set to 0. 
 
 
 
• 
VLAN Bundle Service Model: This model follows a many-to-one mapping where 
multiple VLANs are mapped to a dedicated MAC-VRF, which is mapped to a dedicated 
VNI, which is mapped to a dedicated EVI. This means a single broadcast domain and 
MAC addresses must be unique. SAPs are configured with untagged or wildcard value 
(*/all)  and the incoming VLAN tag is carried end-to-end. In this model, VLAN 
translation is not allowed and the ETag in all EVPN routes MUST be set to 0. 
 
 
 
• 
VLAN-aware Service Model: This model follows a many-to-one mapping where 
multiple VLANs are mapped to a dedicated MAC-VRF that has multiple switching 
tables, which is mapped to separate VNIs, which is mapped to a dedicated EVI. This 
allows for separate broadcast domain per EVI. VLAN translation can be performed and 
MAC addresses can overlap. Local and peer PE’s in multi-homed segment should still 
have identical VLAN IDs. Each individual CE-VLAN ID will be assigned to a different 
broadcast domain, which will be represented by an ETag in the control plane. In this 
model, ETag will be set according to the VLAN ID(s) configured in the SAP. 
 
ARP Suppression and Proxy ARP 
One of the benefits and optimization features of MP-BGP EVPN is the ability to allow PEs 
to act as a proxy and respond to a local ARP request messages (proxy ARP) to 
reduce/suppress the ARP flooding into the fabric (ARP suppression). This reduces BUM 
AOS supports two models: VLAN-based service interface model and Enhanced 
VLAN-bundle Service Interface (ALE Defined) model, which is explained in the AOS 
Service Interface Model. 

<<<PAGE 21>>>
Architecture Guide 
EVPN 
21 
traffic flooding in the fabric. In the R-T2 MAC/IP advertisement route, you can optionally 
carry IPv4/IPv6 addresses associated with a MAC address. 
ARP entries on the local PE maybe learnt through snooping DHCP packets, IPv6 ND, or 
gratuitous ARP (GARP) messages sent by the end host. They may also be configured 
statically. Once the IP addresses are learnt, it can be sent along with the MAC address in 
R-T2 route updates and added to the local and remote proxy ARP cache. 
Proxy ARP should always be kept enabled for performance, but some use cases might 
require to disable it. Some example are hosts that are using Gratuitous ARPs or ARP 
probes for detection and when you’re debugging L2/L3 connectivity issues and require full 
visibility of ARP packets in the EVPN fabric. 
EVPN Extended Communities 
There are additional extended communities that can be carried with EVPN R-Ts such as: 
• 
Route Target Extended Community 
• 
ES-Import Route Target Extended Community 
• 
ESI Label Extended Community 
• 
BGP Tunnel Encapsulation Extended Community 
• 
MAC mobility Extended Community 
• 
Default Gateway Extended Community 
• 
Designated Forwarder (DF) Election Extended Community 
• 
Router MAC Extended Community 
Route Target Extended Community 
This is a standard transitive BGP extended community attribute as defined in RFC 4360, 
which is used for route filtering and separating tenants. This is discussed in the Route 
Distinguisher and Route Target section. 
ES-Import Route Target Extended Community 
This is a new optional transitive extended community carried with the Ethernet Segment 
(R-T4) route used in multi-homing scenarios. It is used to ensure that only the PEs which 
are connected to the same ES to import the R-T4 route. The ES route is imported only by 
the PEs that are multi-homed to the same ES. It is a 6-octet value which is automatically 
encoded from the ESI value. Use of this extended community will be further discussed in 
the Multi-homing Features section.  
ESI Label Extended Community 
R-T1 can optionally carry the ESI Label Extended Community having a Type value of 0x06 
and a Sub-Type 0x01 as well as the ESI Label which represents an ES by the advertising PE. 
It is primarily used for loop prevention by applying split-horizon features for multi-homed 
sites. This will be further discussed in the Multi-homing Features section.  
Proxy ARP is enabled by default in AOS. Disabling of proxy ARP default settings is 
not supported in the current release 

<<<PAGE 22>>>
Architecture Guide 
EVPN 
22 
BGP Tunnel Encapsulation Extended Community 
A BGP tunnel encapsulation attribute may also be included in all EVPN R-Ts to indicate the 
data plane encapsulation type. For EVPN-VXLAN, 8 is used. This allows each PE in a given 
EVPN instance to know each of the encapsulations supported by each of the other PEs in 
that EVI. As specified in RFC 8365, if the BGP Encapsulation extended community is not 
present in an EVPN route, then the default MPLS encapsulation or a locally configured 
encapsulation is assumed. 
MAC Mobility Extended Community 
EVPN supports host mobility across Ethernet segments. If a MAC/IP address becomes 
reachable in multiple segments, EVPN tags the R-T2 MAC/IP advertisement routes with the 
MAC mobility extended community, which is an optional transitive community, and 
includes information necessary to decide which of the MAC advertisements to use. The 
MAC Mobility extended community includes a sequence number to keep track of the latest 
location of the host and enables quick sub-second convergence during host or VM moves 
within the data center.  
When the MAC address is first advertised, it includes the MAC mobility extended 
community with a sequence number of 0. When the host moves to a different location, the 
new PE where the host is connected learns about this MAC address locally and through 
the EVPN fabric. Once it realizes this, it sends a new R-T2 with the MAC mobility extended 
community with an incremented sequence number of 1. Eventually, the old PE ages out 
the R-T2 with the lower sequence number, and the PEs retain the R-T2 with the highest 
sequence number. 
Protection mechanisms are required to be in place, which are covered in more details in 
the MAC and IP Mobility Service section. 
Default Gateway Extended Community 
This extended community is optional and transitive and is used when the PE is acting as a 
default gateway for inter-subnet routing. Each PE that acts as a default gateway for a 
given EVI may advertise in the EVPN control plane its default gateway MAC address using 
the MAC/IP Advertisement route (R-T2). Each such PE indicates that such a route is 
associated with the default gateway by carrying the Default Gateway Extended community 
as defined in RFC 7432.  
The ESI field is set to zero when advertising the MAC route with the Default Gateway 
extended community. The IP Address field of the MAC/IP Advertisement route is set to the 
default gateway IP address for the EVPN instance. For a given EVPN instance, the default 
gateway IP address is the same across all the participant PEs. 
This functionality brings efficiency since it allows the default gateway to be fully 
distributed across all PEs in the EVPN fabric. Inter-subnet traffic for VMs connected in the 
same PE does not need to cross the fabric. 
This functionality is further covered in the Distributed Anycast Gateway section. 
DF Election Extended Community 
The DF Election Extended Community is a new BGP transitive Extended Community 
attribute as defined in RFC 8584, that is used to identify the DF election procedure to be 
used for the ES. 

<<<PAGE 23>>>
Architecture Guide 
EVPN 
23 
 
Router MAC Extended Community 
The router MAC extended community is an optional extended community that includes 
the MAC address of the originating router that is associated with an advertised prefix. 
This extended community is only used when the MAC address is used as an overlay index 
in one of the symmetric IRB routing use cases. 
Integrated Routing and Bridging 
Integrated Routing and Bridging (IRB) is a solution based on EVPN which allows for 
dynamic and efficient inter-subnet connectivity among VRFs and end devices while 
maintaining the multi-homing capabilities of EVPN. Instead of sending all the traffic to a 
centralized L3 gateway in a data center use-case, even if two hosts that belong to the 
different subnets are connected to the same PE, they are instead routed in the local PE 
using integrated routing and bridging capabilities. 
 
An IP-VRF table is instantiated when a tenant requires IRB services. This IP-VRF table will 
contain one or more MAC-VRF tables. When an EVI is created, a MAC-VRF is instantiated as 
well. A MAC-VRF table can contain one or more BDs (VLANs), but this will depend on the 
service interface model used as explain in the EVPN Service Interface Models section. Each 
BD is connected to the IP-VRF via an L3 IRB interface, which is usually the gateway for this 
BD. 
Each IP-VRF and MAC-VRF is identified by its corresponding RT and RD, with each having 
different encodings for the RD as will be explained in the Auto-generated RD/RT for 
Various Route Types section. To identify where to forward the traffic, then the receiving PE 
needs both the MAC-VRF RT and the ETag (VLAN) in order to identify the correct BD, but 
this again depends on the service interface model used. 
AOS EVPN adapts the Service Carving-based DF election which provides a more 
granular mechanism for load distribution based on per-service DF election 

<<<PAGE 24>>>
Architecture Guide 
EVPN 
24 
There are two types of IRB solutions: Asymmetric IRB and Symmetric IRB.   
Asymmetric IRB 
The asymmetric IRB deployment is based on a stretched EVI design. It is more simplistic 
model for deployment but is also resource intensive.  
Inter-EVI forwarding in this model requires the EVIs to be stretched across the forwarding 
PEs. i.e. the source and destination EVIs have to be configured in both the PEs involved in 
the forwarding. This makes the model more resource and configuration intensive 
particularly when there are many EVIs participating in the forwarding topology.  
Since the model relies of bridging to the destination host at the ingress point, the host 
address should be available in the ingress PE. 
 
In the asymmetrical routing model, the ingress PE performs three lookups, while the 
egress PE performs one lookup. The ingress PE performs a MAC lookup and does Layer 2 
switching to the gateway IRB interface. Then, it also performs an IP lookup and does Layer 
3 routing to the destination IRB interface. After the Layer 3 routing, the ingress PE again 
performs a MAC lookup and does Layer 2 switching to the destination VNI. The egress PE 
only performs a MAC lookup and does Layer 2 switching to the destination host. 
Therefore, the ingress PE does routing and bridging, while the egress PE does only 
bridging (hence the name asymmetric). This implies that the source and destination EVIs 
have to be configured in all the PEs involved in the forwarding, and all PEs need to 
maintain each host’s (local and remote) IP and MAC address in its ARP table and maintain 
MAC-VRFs and IRB interfaces for all subnets in an IP-VRF (local and remote). This makes 
the model more resource and configuration intensive particularly when there are many 
EVIs participating in the forwarding topology.  
 
Symmetric IRB 
The Symmetric IRB model is simpler for configuration and deployment and offers better 
scalability than the Asymmetric IRB model and therefore is the prevalent and 
recommended configuration for the inter-service routing of EVPN hosts. 

<<<PAGE 25>>>
Architecture Guide 
EVPN 
25 
In the symmetric model, as the name implies, both the ingress and egress PEs perform 
Layer 2 bridging and Layer 3 routing. The ingress PE performs a MAC lookup followed by 
an IP lookup, and the egress PE performs an IP lookup followed by a MAC lookup. This will 
not require service configuration in all PEs, but only where the hosts are attached. 
 
For the symmetric IRB model, each PE participating in symmetric IRB only maintains ARP 
entries for locally connected hosts and MAC-VRFs for only locally configured subnets. This 
offers better scalability and therefore, is the prevalent and recommended configuration 
for the inter-service routing of EVPN hosts.  
In the symmetric IRB model, a network unique EVI is created on all the PEs for each 
tenant/VRF of the PE. This EVI is configured as the L3EVI (called Supplmentary Broadcast 
Domain [SBD]) and only one L3EVI is required per VRF which will provide the inter-EVI 
reachability for all the IRB services in the VRF. Additionally, the L3EVI is also used as the 
gateway for prefix route advertisement for both EVPN and non-EVPN routes. 
 
Each customer/tenant of the VXLAN network is assigned a unique VRF. The VLAN-tag 
based traffic from the hosts are assigned to an IRB-EVI on the access side. A L3EVI is 
provisioned in each tenancy for the inter-subnet routing among the subnets (IRB 
interfaces) and prefix rotues of this tenant network. 
All the IRB-EVI services within the VRF will be aware of the L3EVI associated with the VRF. 
The forwarding path in the MAC-VRF entries can use either bridge (using the L2EVI) or 
route (using the L3EVI) based forwarding. 
When an L3EVI is configured for a VRF for symmetric IRB, the RT-2 MAC-VRF message to 
advertise the host entries are modified such that the remote hosts can either bridge or 
route to the host. 
Supplementary Broadcast Domain (SBD) is denoted in AOS as Fabric-VPN 

<<<PAGE 26>>>
Architecture Guide 
EVPN 
26 
The symmetric IRB model is used for establishing L3 connectivity for both host-based and 
prefix-based routes. 
There are two routing models defined in RFC 9135/9136 for inter-subnet connectivity:  
• 
Host-based routing: In this model, only host addresses (/32) are advertised using 
R-T2 messages. This can use the asymmetric or the symmetric IRB model. 
• 
Prefix-based routing: In this model, prefix addresses of any length can be 
advertised using R-T5 messages. This will only use the symmetric IRB model. 
 
Host-based Routing 
For host-based routing, MAC and IPs are encoded in R-T2 are used to populate MAC-VRFs, 
ARP tables, and IP-VRF tables. 
The R-T2 message for the host MAC-IP advertisement will also include the L3EVI IRB 
information as below: 
• 
Both the IRB-EVI and the L3EVI associated with the VRF are included in the 
message using the Label1 and Label2 fields of the RT-2 message.  
• 
The Route-Tag for both the EVIs are added to the message. 
• 
An additional router MAC extended community is included in the RT-2 message. 
This TLV will contain the Route-MAC (Chassis-MAC) associated with the sending PE. 
This address will be used as the destination PE when the hosts route entry is 
inserted in the remote PE. Extended communities are further discussed in the 
EVPN Extended Communities section. 
 
Prefix-based Routing 
There are multiple prefix-based routing models that were defined in RFC 9136: 
• 
Interface-less IP-VRF-to-IP-VRF Model: No SBD nor overlay indexes required 
• 
Interface-ful IP-VRF-to-IP-VRF with SBD IRB Model: Requires SBD as well as 
gateway IP addresses as overlay indexes. 
• 
Interface-ful IP-VRF-to-IP-VRF with unnumbered SBD IRB Model: Requires SBD 
as well as MAC addresses as overlay indexes. 
Interface-less IP-VRF-to-IP-VRF Model 
In this model, R-T5 is used to advertised local prefixes with the next-hop set to the PE’s 
loopback IP address and VNI label, and no overlay index is used. 

<<<PAGE 27>>>
Architecture Guide 
EVPN 
27 
 
Interface-ful IP-VRF-to-IP-VRF with SBD IRB Model 
 
In this model, IP-VRFs are connected using the L3EVI. R-T5 routes are used to advertise 
local subnets with the next-hop set as the L3EVI gateway IP address (overlay index). In 
addition, R-T2 is used to advertise the MAC address and IP address of the L3EVI IRB 
interface to recursively resolve the overlay index. 

<<<PAGE 28>>>
Architecture Guide 
EVPN 
28 
Interface-ful IP-VRF-to-IP-VRF with unnumbered SBD IRB Model 
 
This model is similar to the previous one, but in this case the IRB interface for the L3EVI 
are unnumbered, i.e. no IP address is configured. The MAC address will be used instead as 
the overlay index. In this model, both R-T2 and R-T5 are used. R-T5 advertises local 
subnets with the next-hop set as the L3EVI IRB interface MAC address (Chassis-MAC) 
associated with the sending PE as the overlay index. R-T2 is used to advertise the MAC 
address of the L3EVI IRB interface to recursively resolve the overlay index. In addtion, the 
router MAC extended community will also be added. 
 
 
Distributed Anycast Gateway 
In a large network, for example, Data Center network, there will be host mobility among 
the PE nodes of the connected service. To support large scalable networks, such mobility 
should be managed with efficiency. Distributed Anycast Gateway (DAG) supports this host 
mobility without the need for any added redundancy protocols for the EVI service. 
Previously, a redundancy protocol (such as VRRP) would be required on the VTEPs such 
that only the master VTEP router can act as the gateway. But this solution is not efficient 
since it can lead to traffic tromboning and the overhead of the control plane of the 
redundancy protocol. 
A distributed anycast address called the anycast IP address is configured on all the PEs 
that share the EVI. Along with the anycast IP, an anycast MAC address (virtual MAC) is 
configured on all the common PEs. This anycast MAC must be setup per VRF and the same 
anycast MAC address is used for all subnet anycast IP interfaces of VRFs. 
Only symmetric IRB based on the Interface-ful IP-VRF-to-IP-VRF with SBD IRB 
Model is supported starting release 8.10R2 

<<<PAGE 29>>>
Architecture Guide 
EVPN 
29 
 
DAG is also supported in multi-homing scenarios, as we will discuss in the Multi-homing 
Features section. 
The Anycast MAC can be auto derived or configured manually. When enabled for auto 
configuration, the MAC will use the standards-based reserved 00:00:5e:00:01:<VRF-ID> as 
the derived VMAC for each VRF. Auto-derivation of the anycast MAC can only be used if 
there is a certainty that the auto-derived MAC does not collide with any MAC address that 
is already being used in the network. An anycast MAC-address is configured on all the 
common VTEPs, This anycast MAC address must be configured per VRF and the same 
anycast MAC address is used for all subnet anycast IP interfaces of a VRF. 
Another alternative for auto-generation of VMAC address is to use the the site-based 
VMAC which will be encoded as follows in the 6-byte VMAC address: 
• 
3-byte Alcatel OUI 
• 
2-byte site-id (required to configure on all VTEPs) 
• 
1-byte VRF-ID 
Data Plane 
BUM Traffic Handling 
Layer 2 BUM traffic can be flooded in two ways in a VXLAN fabric: 
1. Tandem replication using a multicast-enabled underlay network.  
2. Head-end or ingress replication using EVPN R-T3 
Each of these methods have their pros and cons. While tandem replication adds 
complexity by using a multicast-enabled underlay, it provides efficiency in the core. Head-
end replication, also called ingress replication, on the other hand, is a unicast approach to 

<<<PAGE 30>>>
Architecture Guide 
EVPN 
30 
handle multi-destination traffic which involves an ingress device replicating every BUM 
packet and sending them as a separate unicast to the remote egress devices, which is less 
efficient than tandem replication. Ingress replication, however, is much simpler to 
configure. 
 
Ingress replication is performed using R-T3 IMET routes. This R-T is used for the for the 
auto-discovery of remote peers to set up the ingress replication lists or BUM tunnels over 
VXLAN for a VNI. These BUM tunnels are created after receiving the R-T3 IMET routes from 
a remote PE. This tunnel will be shared if more than one VNI exists in the same PE. PEs 
then create and maintain an ingress replication list which will store all the remote 
destination PEs which exist in the same EVI which were created using R-T3 IMET routes. 
Flooded frames across the fabric are not flooded back due to split horizon rules. 
In multi-homing scenarios, a Designated Forwarder (DF) will be elected to flood BUM 
traffic in the ES. This will be further discussed in the Multi-homing Features section. 
Intra-subnet Communication - Bridging 
When MP-BGP EVPN service is enabled, PEs exchange R-T3 IMET routes to auto-discover 
remote peers and set up the BUM tunnels (ingress replication list) over VXLAN. 
Locally connected MAC addresses of hosts are learned by data-plane learning or through 
control-plane protocols such as ARP, 802.1x, LLDP, etc. These MAC addresses are recorded 
in the local MAC addresses table (MAC-VRF) and advertised to remote PEs through R-T2 
MAC/IP routes. The RD is included in the advertisement to make the prefix unique, and 
the RT is sent as an extended community and is used for the import/export of routes. 
 
Intra-subnet data plane communication between two hosts (Client-1 and Client-6) is 
explained using the above topology and detailed steps below: 
Only ingress (head-end) replication is supported  

<<<PAGE 31>>>
Architecture Guide 
EVPN 
31 
1. The source host (Client-1) sends an ARP request for the destination host (Client-6) 
MAC address.  
2. When the ingress PE, assuming it was hashed to LEAF-1 in this case, first receives 
the ARP request from Client-1, which is a broadcast, it will trigger a route lookup 
for the Client-6 IP. If LEAF-6 EVPN control plane has gleaned the Client-6 MAC or 
MAC+IP address from frames it received from Client-6, then LEAF-1 would have 
received the R-T2 route notification from LEAF-6 for this Client-6. In this case, it 
would have been populated in the proxy ARP and MAC-VRF table in LEAF-1.  
3. Since proxy ARP is enabled, LEAF-1 will send an ARP response to Client-1 with the 
MAC+IP address information for Client-6. 
4. When Client-1 starts the unicast communication and LEAF-1 recieves the frame, it 
will consult its MAC-VRF, encapsulate the frame with the VXLAN headers, and 
routes the packet over the fabric. 
5. When the packet reaches LEAF-6, it will decapsulate the packet and bridge the 
frame to Client-6 
Inter-subnet Communication - Routing 
Assuming the symmetric IRB forwarding model (interface-ful IP-VRF to IP-VRF with SBD 
Tunnel), Client-1 is configured with the Anycast Gateway as the IRB interface on LEAF 
switches 1-3, and Fabric-VPN (EVI 50) is configured on all PEs, inter-subnet data plane 
communication between two Client-1 and Client-4 is explained using the above topology 
and detailed steps below.  
In this model, R-T5 routes will be used to advertise the local IP prefixes, whereas EVPN R-
T2 routes will advertise the MAC/IP addresses of each SBD IRB interface. The gateway IP 
address in R-T5 will be the IRB interface IP of the SBD, which will be the overlay index that 
will be used as a next-hop required for the recursive route resolution. : 
1. Client-1 sends an ARP request for the DGW configured on the local PE IRB interface 
since the destination is in a different subnet. We will assume it was hashed to 
LEAF-1. 
2. When the LEAF-1 receives the frame, it checks the MAC-VRF table and responds 
back with its IRB MAC address. 
3. Client-1 then sends a packet with the final destination IP of Client-4 and the 
destination MAC address of LEAF-1 DGW IRB interface. 
4. When LEAF-1 recieves the packet, a destination IP lookup is performed on LEAF-1 
IP-VRF table and will determine that next-hop IRB interface is the SBD IRB interface 
IP address (overlay index) in LEAF-4, which was derived from R-T2 received 
previously. 
5. LEAF-1 consults the ARP table to identify the destination (LEAF-4) MAC address and 
consults the SBD MAC-VRF table to determine the VNI. Then it encpasulates the 
packet with the VXLAN header and forwards the packet. 
6. When the packet reaches the LEAF-4 it decapsulates the VXLAN packet and 
forwards the packet to the SBD IP-VRF table based on the VNI. LEAF-4 then 
perfoms an IP lookup in the IP-VRF table for and determines the destination IP 
address corresponds to a locally-attached subnet. Finally, LEAF-4 will consult the 

<<<PAGE 32>>>
Architecture Guide 
EVPN 
32 
MAC-VRF table using the inner destination MAC address and forwards the packet 
to the Client-4. 
Multi-homing  
Multi-homing generally refers to a host or CE device that is connected to multiple PE 
devices through a Link Aggregation (LAG) for redundant connectivity. It is one of the key 
benefits that EVPN offers. Mutli-homing can also be achieved through other technologies 
such as Virtual Chassis (VC). We will cover the differences in the EVPN Multi-homing vs VC 
Host Attachment section. There are two redundancy modes supported as defined in RFC 
7432: 
 
1. Single-active: This redundancy mode allows active/standby connectivity with one 
path active at any time. Failover occurs in case of active link failure to the 
secondary link. 
2. All-active: This redundancy mode allows active/active connectivity of multi-homed 
devices. This allows for efficient bandwidth utilization and per-flow load-balancing. 
LAG is required to be configured between the PE switches and the multi-homed CE 
device. This is to avoid receiving duplicate packets and for loop prevention. 
 
Multi-homing primarily uses R-T1 Auto-Discovery and R-T4 ES routes. The following 
procedures take place when a service is first enabled on a multi-homed ES: 
• 
The multi-homed peer PEs which belong to the same ES will advertise R-T4 to discover 
each other. The BGP advertisement that advertises R-T4 also carries an extended 
community called ES-Import RT. Extended communities are further discussed in the 
EVPN Extended Communities section 
• 
Then, they proceed to elect a Designated Forwarder (DF) for the ES. This is required for 
loop prevention and to prevent duplicate traffic. This election process is further 
discussed in the DF Election section. 
• 
If the ES is single-active multi-homed: 
All-active multi-homing is supported starting release 8.10R2 

<<<PAGE 33>>>
Architecture Guide 
EVPN 
33 
o 
R-T1A (A-D per ES) route is advertised with ESI Label extended community. This 
extended community has a flags field set to 1 to indicate single-active 
redundancy. ESI Label is also carried in this extended community and is used 
for split horizon filtering as covered in Split Horizon section. It is received by all 
the participating EVPN nodes but only imported into the control plane if there 
is a local service (EVI) which matches a service in the RT set in the advertised 
route. This route is also used for fast convergence as covered in the Mass 
Widthraw section. 
o 
R-T1B (A-D per EVI) route for the EVI is advertised which is used by the remote 
PEs to create primary/backup lists which is used for backup path in 
combination with the R-T1A (A-D per ES) route to determine the redundancy 
mode in use. This is covered in more details in the Backup Path section. 
• 
If the ES is all-active multi-homed: 
o 
R-T1A (A-D per ES) route is advertised with ESI Label extended community. This 
extended community has a flags field set to 0 to indicate all-active redundancy 
mode. ESI Label is also carried in this extended community and is used for split 
horizon filtering as covered in Split Horizon section. It is received by all the 
participating EVPN nodes but only imported into the control plane if there is a 
local service (EVI) which matches a service in the RT set in the advertised route. 
This route is also used for fast convergence as covered in the Mass Widthraw 
section. 
o 
R-T1B (A-D per EVI) route for the EVI is advertised to the remote PEs for the 
aliasing (load-balancing) functionality. This will allow the remote PEs to create a 
list of participating PEs in the ES and to perform load-balancing. This is used in 
combination with the R-T1A (A-D per ES) route to determine the redundancy 
mode in use. This is covered in more details in the Aliasing section. 
The ESI value is typically derived from the port MAC for physical access ports, CE MAC for 
all-active multi-homed ES using LACP, or statically defined for static LAG. This is covered in 
more details in the AOS EVPN ESI Model section. 
DF Election and Service Carving 
A DF is elected after ESI members discover each other using R-T4. This is performed to 
avoid duplicate BUM flooding in multi-homing scenarios. In single-active multi-homing, 
one DF is elected per ESI using a pre-defined algorithm and will be responsible to flood 
BUM traffic and forward unicast traffic to the CE. In all-active multi-homing, the DF is only 
responsible to forward BUM traffic from the EVPN fabric to the CE while the other peer 
PEs in the same ES will not allow it. Unicast traffic can be forwarded based on LACP 
hashing. 
The default procedure for DF election is referred to as “service carving”. It is also possible 
to elect multiple DFs per ES (one per VLAN) in order to perform load balancing of BUM 
traffic destined to a given segment.  
Each PE in multi-homed ES builds an ordered RT list if R-T1 is received from the peer PEs. 
The default algorithm used is a modulo-based algorithm, which is (DF = EVI mod N), where 
N is the number of PEs in the RT list. 
By default, the DF election is pre-emptive, so it is recalculated when a PE is added to the 
candidate list. 

<<<PAGE 34>>>
Architecture Guide 
EVPN 
34 
Split Horizon  
EVPN uses split-horizon rules for loop prevention in all-active multi-homing scenarios. The 
split horizon basic principle is simple: Information about the routing for a particular 
packet is never sent back in the direction from which it was received.  
In the case of PEs designated as non-DF, the SAP attachments on the access ports will 
need to treat the BUM traffic forwarding to CE differently from unicast forwarding to the 
CE. All BUM traffic needs to be filtered and dropped. The filtering of this egress BUM 
traffic is achieved by associating these non-DF SAPs with a different Split Horizon Group 
(SPG) for BUM traffic while the unicast traffic will be associated with the default access 
SPG. The non-DF SPG will be set to drop BUM traffic from all network tunnels.  
As defined in RFC 7432, which is MPLS-based EVPN, the ESI Label extended community is 
used for split horizon filtering. When sending BUM traffic, the non-DF ingress PE adds the 
ESI Label extended community that identifies the ES. This label is distributed between PEs 
using R-T1A (A-D per ES) route. However, EVPN-VXLAN does not include the ESI label as 
mentioned in RFC 8365 (section 8.3.1). The procedure used for split horizon is for each PE 
to track and maintain a list of peer PE IP address which are part of the same ES for split 
horizon filtering. If the BUM frame originated on the PE (source IP Address in the VXLAN 
header) that is not in the PE list of an ES, then traffic is forwarded only by the DF PE of the 
ES. Otherwise, the frame is dropped. 
Local Bias and ES Pruning 
As specified in RFC 8365, for an ES that is multi-homed in all-active mode, the forwarding 
to this ES from other access ports of the PE should always use the local access 
attachment. This would mean that even non-DF attachment will forward both unicast and 
BUM traffic originated on any local access port of the PE. The other PE nodes of the ES 
including the DF should avoid duplicating the BUM traffic which is received on their 
network port from other peer nodes. Each PE should be aware of the originating PE of the 
BUM traffic and drop the forwarding to its ES allowing only local forwarding on the 
originating node. This procedure is called Local Bias and is accomplished by ES Pruning. 
In case of BUM traffic, the BUM bit is set in the VXLAN Header at the originating PE. The 
traffic is then sent to all forwarding distribution set of PEs of that EVI.  
Each PE maintains the list of peer PE nodes associated for all the locally configured ES. If 
the BUM frame originated on the PE (source IP Address in the VXLAN header) that is not in 
the PE list of an ES, then traffic is forwarded only by the DF PE of the ES. Otherwise, the 
frame is dropped using an ACL rule. 
When there is a match the egress filtering rule will drop the frame egressing out the 
destination access port of the ESI. If there is no match (BUM frame originates on a remote 
PE), then only the DF will forward the frame to ES utilizing the above-mentioned allocation 
of the split-horizon filtering. 
Aliasing  
The aliasing feature allows the remote PEs to perform per-flow load balancing of traffic to 
an all-active multi-homed ES. To achieve this, each peer PE in the all-active multi-homed 
segment advertises R-T1A and RT-1B routes. R-T1A is used to indicate the the redundancy 
mode (0 in this case) and the ESI, while RT-1B is used to advertise the VNI to be used to 
send traffic from remote PEs. R-T1 is advertised by all the peer PEs which are part of the 
same ES, which allows the remote PE to build a list of VTEPs which are part of the same ES. 
When the remote PE recieves the R-T2 MAC/IP route from any of the peer PEs in the multi-

<<<PAGE 35>>>
Architecture Guide 
EVPN 
35 
homed ES, it will learn the next-hop ES for each host MAC address. When sending traffic to 
an all-active multi-homed ES, it will perform load-balancing using the list of VTEPs learnt 
through R-T1. 
 
In case of failure of one of the PE-CE links in an all-active multi-homed segment, an RT-1B 
route update is sent with a withdraw from the affected PE and advertised to remote PEs. 
Backup Path 
 
Another feature is “backup path” feature is similar but for single-active multi-homing 
scenarios. The R-T1A (A-D per ES) route is sent with the redundancy mode set as single-

<<<PAGE 36>>>
Architecture Guide 
EVPN 
36 
active. Peer PEs of an ES will elect a Primary and Backup PE among the peer nodes. This 
status will be sent to the rest of the nodes in the network. All forwarding to the ES from 
remote nodes is only sent to the Primary PE. In case of ES withdrawal by Primary PE, the 
remote PEs seamlessly switched over to backup PE with minimal loss of connectivity when 
forwarding to the multi-homed ES. 
Mass Withdraw 
In multi-homing scenarios, EVPN defines a mechanism to rapidly signal to remote PEs to 
update their MAC address table when a failure occurs in an ES. R-T1A (A-D per ES) route is 
used for this purpose. The ESI is advertised to be no longer reachable from the local PE. 
The mass withdrawal is signaled by encoding the EVI value of 0xFFFFFFFF in the RT-1A 
message. All the peer and remote PEs will update the ESI as no longer reachable from this 
advertising PE. Remote PEs will update the path-list for the MAC addresses associated 
with this ESI. If there are no other PE in the path-list, the MAC addresses are flushed and 
removed. This is in essence a mass withdraw of the MAC addresses based on a single ESI 
update message. 
Multicast Optimizations 
Multicast Switching 
RFC 9251 introduces multicast optimization features to EVPN such as IGMP/MLD proxy. 
These features reduce flooding of IGMP messages in the EVPN fabric and uses control 
plane messages to synchronize the IGMP state information and multicast interest. R-T6, 7, 
and 8 are introduced to support this functionality. 
Multicast generally uses R-Ts 3, 6, 7, and 8. RT-3 is used in general for BUM replication, 
while RT-6 is used for support of IGMP/MLD proxy functionality and to distribute multicast 
traffic interest by hosts for (*,G) or (S,G). In case multi-homing is configured and without 
the use of R-T6, 7, or 8: 
• 
All-active: There is no guarantee that IGMP Join and Leave packets will be sent to the 
DF for that ES 
• 
Single-active: A failover in the DF will cause a loss of IGMP state information. 
R-T7 and R-T8 are used to synchronize IGMP state information between multi-homed 
hosts. 
When IGMP/MLD proxy functionality is enabled on the PE, this allows the PE to generate 
R-T6 SMET routes, which allows a host to receive multicast traffic on request. This 
provides multicast optimization and minimizes IGMP traffic in the core. 
When multi-homing, by default only the DF will originate SMET routes (R-T6) for the 
groups learnt on the multi-homed ES. So, the multicast traffic from remote PEs will be 
sent to the DF PE and then gets forwarded over the respective SAPs. In the event of a DF 
change, there will be traffic drop to clients, as the remote PEs will continue to forward the 
traffic to older PE until they receive the SMET routes form the new PE. 
An enhancement to this feature is implemented in AOS, which is covered in the AOS 
Multicast Optimizations section. 
 

<<<PAGE 37>>>
Architecture Guide 
EVPN 
37 
Multicast Routing  
Optimized Inter-Subnet Multicast (OISM) 
RFC 9625 specifies a solution for multicast routing across different subnets of a tenant 
using IRB routing interface. This does not involve any native multicast routing protocols, 
like PIM. This solution is called Optimized Inter-Subnet Multicast (OISM). 
 
This solution relies on the Fabric-VPN (SBD) and R-T6 for the multicast routing. When an 
IGMP join is received from a multicast reciever host/CE to a PE, the PE generates a R-T6. If 
OISM routing is enabled, then R-T6 will be advertised with the Fabric-VPN RT instead of 
the local RT.  
 
The PE where the multicast source is connected, assuming it is in a different EVI, will 
import the R-T6 and informs the IP Multicast Switching (IPMS) service.  
 
The IPMS creates a multicast group entry in the Fabric-VPN service and its associated SDP. 
When a multicast packet is first received by the the source into the ingress PE, it will 
create a route forward entry from the local service to the Fabric-VPN service and forward 
the traffic to the egress PE where the reciever is located. Once the egress PE recieves the 
OISM is available as an Early Availability (EA) feature starting 8.10R3 
The OmniSwitch implementation of IGMP Snooping is called IP Multicast Switching 
(IPMS) and MLD snooping is called IP Multicast Switching version 6 (IPMSv6). 
IPMS/IPMSv6 allows switches to efficiently deliver multicast traffic in hardware at 
wire speed. 

<<<PAGE 38>>>
Architecture Guide 
EVPN 
38 
first multicast packet on the Fabric-VPN service, it will create a route forward entry to the 
client interfaces. 
PIM EVPN Gateway (PEG) 
Another feature which is supported in EVPN is the interworking between the EVPN fabric 
and an external PIM router. This feature is called PIM EVPN Gateway (PEG). 
 
In this case, PIM will be enabled on the Fabric-VPN (SBD) and the VLAN interface towards 
the external domain on the PEG router(s). It is also possible to have two PEGs acting as 
redundant pairs for a given VRF and supports load balancing across different VRFs. One of 
the PEGs will be elected as a designated router (DR) and that PEG node is responsible to 
interwork with external PIM router. In case you are using two PEGs for redundancy, then a 
dedicated L3 link should be used between PEGs for RP reachability. 
 
To discover internal sources in EVPN, RFC 9625 proposes the concept default SBD-SMET 
route (*,*). By sending this default route, PEG indicates all other PEs in the Fabric-VPN 
service to forward all the multicast traffic they receive from their local services. This way 
the PEG discovers all the multicast sources in the EVPN network and register all those 
sources to the RP. However, this approach makes the inefficient use of EVPN network 
bandwidth. The other approach is to inherit MVPN source discovery mechanism using R-
T10 (S-PMSI AD Route).  
PEG is available as an Early Availability (EA) feature starting 8.10R3 

<<<PAGE 39>>>
Architecture Guide 
EVPN 
39 
In this case, when the ingress PE first recieves multicast traffic, R-T10 is generated (if 
OISM is enabled) with the (S,G) information in the Fabric-VPN. The DR PEG will process this 
R-T10 and registers this source with the external PIM RP. Now the PIM RP will know that 
the source is behind the DR PEG. If there is a reciever for this (*,G)/(S,G) in the PIM 
network, the PIM RP will trigger a PIM join of the (S,G) to the DR PEG. When the DR PEG 
recieves the PIM join, it will generate R-T6 for the given (S,G) to pull traffic from the 
source. When the ingress PE where the multicast source is located recieves this R-T6, it 
creates a path towards the DR PEG and starts forwarding multicast traffic towards the 
source. 
When compared to the source discovery using (*/*), R-T10 based source discovery adds a 
little latency (additional delta time taken by PEG to generate RT-6 route plus traffic 
forwarding from source PE to PEG) when establishing data path. 
MAC and IP Mobility Service  
If a CE MAC address is constantly moving between two different Ethernet segments, it will 
cause the address to be learned on a different PE each time. This is called MAC 
duplications and can be a result of a loop in the ES network or if the same address is 
present in two hosts of the service. Such a behavior leads to a continuous exchange of the 
MAC being advertised and withdrawn in the control plane among all the PEs in the EVPN 
network and leads to degradation of the EVPN network performance. This can be avoided 
by enabling MAC mobility feature for the EVPN enabled service. 
When MAC mobility loop protection is enabled, and if a PE detects a MAC mobility event 
through local learning, it starts the timeout value, and if it detects MAC moves count 
reaching the threshold count before the timer expires, it concludes that a duplicate MAC 
situation has occurred. The PE then alerts to stop sending, updating, or processing any 
BGP MAC advertisement routes for that MAC address until a corrective action is taken, and 
that MAC address is considered for hold-down. After completion of the retry-time interval, 
the MAC is moved out of hold-down and is flushed to restart the process of duplicate 
detection. 
In case two hosts are assigned the same IP address, then DAD (Duplicate Address 
Detection) feature is used in this situation. DAD is considered as movement of IP to MAC 
association. This could be either because of human error or a spoofing attack on an EVPN 
network. 
Duplicate IP detection monitors N "IP-moves" within M-second timer. If there are N moves 
within M time interval, then the host is moved to "filtering state" (F state) for a hold-down 
time of (3 * M). This is the default. 
Consider a scenario, where the ARP was learned on PE1 from host1 (macA). Now, a new 
ARP with the same IP from host 2 (MAC B) entering to the EVPN network is considered as 
IP Mobility. When an existing host is modified with a different MAC, a PE starts a M-second 
timer (duplicate detection interval), and if it detects N IP moves (threshold count) before 
the timer expires, it concludes that a duplicate IP situation has occurred. 
To detect the duplicate IP faster, the PE will send a Confirm message to the former owner 
of the IP. A Confirm message is a unicast ARP request message sent by the PE to the MAC 
addresses that previously owned the IP. If the PE does not receive an answer within a 
given time (CE confirm timeout), the new host will be confirmed and activated. If there are 
N moves within M-second time interval, then the host is moved to "filtering state" (F state) 

<<<PAGE 40>>>
Architecture Guide 
EVPN 
40 
for a hold-down time interval. After the hold-down timer expires, the host that was in 
filtering state will be removed. 
While a PE sends CONFIRM message to CE to probe for its local presence, the PE shall 
activate the remote host (during this confirm time). This is because the route is owned 
and activated by the new PE and other PEs in the network have updated the host route to 
this new PE. The new PE route has a higher sequence number and thats the reason its 
activated. 
In case of VM mobility where the Host (IP+MAC) is moved from one ESI to another ESI, this 
is not considered as DAD as both the IP and MAC is not changing during the move. So 
none of the DAD procedures (N moves in M timeout) will follow for such scenario. 
Silent Hosts 
In some cases, it may be necessary to statically bind MAC address to a SAP port. This is 
particularly useful if when the device is a “silent” device. A “silent” device is a device that 
does not transmit traffic for extended periods of time because it goes into power-save 
mode for instance. These periods of inactivity can result in a loss of service binding, thus 
making the device effectively unreachable (for example for a WAKE-ON-LAN packet). This 
problem can be avoided by statically binding the MAC address to the SAP port. 
The configured silent host MAC address will be advertised by BGP-EVPN with a sticky bit to 
mark the address with a static disposition on all the PE nodes of the EVPN network. This 
will ensure that no MAC move can be triggered by any remote node if this address is 
being learnt on the SAP of a remote node. 
 
AOS EVPN Model and Differentiators 
The AOS EVPN service model provides enhanced stability, better scalability, and improved 
convergence of BGP based EVPN network by: 
• 
Ease of configuration: Supports the auto-generation of the RD and RT for various EVPN 
R-T messages. It also uses the same service manager configuration for other fabric 
technologies such as SPB and MPLS. 
• 
Instantiating an ESI for any access port that is enabled for EVPN. This allows the access 
port types (physical, single-homed or LAG/multi-homed ports) to work efficiently by 
using the EVPN control-plane based Forwarding Database (FDB) management. 
• 
Providing hierarchy in route generation. 
• 
Providing high granularity, by generating the ESI + ETag aware routes. 
 
AOS EVPN ESI Model 
The AOS EVPN model allows to generate the ESI value automatically and manually. The 
AOS EVPN model automates the ESI generation wherever possible to simplify the ES 
configuration. All the ESI generated by AOS nodes will be based on Type 0x3 (MAC 
address-based) ESI as specified in the RFC 7432. The fields of the 9-Byte ESI will depend on 
the type of access port. 

<<<PAGE 41>>>
Architecture Guide 
EVPN 
41 
 
Type Field (1 
Octet) 
MAC Address (6 Octets) 
Local Discriminator (3 Octets) 
The scope of the configuration of a unique 9-byte ESI is as per the table below: 
 
Access Port Type 
Auto ESI Configuration 
Manual ESI Configuration 
Physical Port 
Yes. Derived from access port MAC 
address 
(0x3 + Port_MAC + 0xFFFFFF) 
No 
LACP LAG 
Yes. Derived from CE MAC obtained 
from the LACP frames of the trunk 
port 
(0x3 + CE_MAC + 0xFF + AggID) 
No 
Static LAG 
No 
Yes. User will input manual 5-
byte ESI 
(0x3 + 0xA1 + 5-byte_Manual_ESI 
+ 0xFF + AggID) 
For the manual configuration of ESI, AOS EVPN will provide a 5-octet user input in the 
format specified in the table above. The remaining 4-octet is reserved/internal to AOS to 
interpret the trunk information associated with the ESI. 
The AOS manual ESI will use a 1-byte signature in the upper octet to ensure the global 
uniqueness of the configured ESI. 
The AOS EVPN ESI model provides the ability to associate an ESI for both SH and MH 
based access ports and the generation of Etag-based Routes. Its goal is to provide 
stability, better scalability, and improved convergence of the BGP-based EVPN network. 
AOS Service Interface Model 
The AOS service interface model provides an additional level of granularity in the 
management of FDB entries (L2 and L3) of the EVPN-based control plane by generation of 
ETag-based routes. All SAP attachments configured on the EVPN-enabled access ports will 
generate an ETag-based route update. Route updates and withdrawals associated with the 
SAP attachments can be summarized at the ETag level rather than the withdrawal of 
routes associated with each MAC and host addresses associated with the ESI+ETag tuple. 
The ETag value is the VLAN ID associated with the SAP. This service model is called 
Enhanced VLAN-bundle service interface, which is an ALE defined service-based interface 
model. It is similar to VLAN-aware-bundle (please refer to the the EVPN Service Interface 
Models section) where ETags are carried in the R-T1 (EAD per EVI) and R-T2. However, 
VLAN-aware bundle mandates that R-T3 is generatd per ETag for the same EVI to achieve 
a different broadcast domain. In case of ALE model, only one R-T3 is generated for an EVI, 
which is applicable to all ETags (hence ETAG = 0). This reduces the number of R-T3 routes 
in the network. The data plane mimics VLAN-bundle service interface model. This means 
that MAC addresses across different ETags belonging to same EVI will not be allowed and 
considered as move. In this model, VLAN-translation is enabled on the egress PE. 

<<<PAGE 42>>>
Architecture Guide 
EVPN 
42 
 
It is recommended to always use the enhanced VLAN-bundle service model for optimal 
performance, and to fall back to VLAN-based service model when required for inter-
operability purposes. 
When using the VLAN-based service model, the following changes will happen: 
• 
R-T1B (A-D per EVI), R-T2, R-T7, R-T8 would have ETag as zero. 
• 
Audit for R-T1B is based on EVI instead of ETag+EVI. 
• 
In data plane, the passenger packet is stripped of all tags and sent in the tunnel as 
untagged. Egress VLAN translation on PE’s take care of adding the right VLAN.  
 
Auto-generated RD/RT for Various Route Types 
The RD value of an EVPN message is used as the identifier of the PE object that generates 
an EVPN R-T message. As specified in RFC 7432, all EVPN Route Types will use the Type-1 
RD. The RD types are defined in RFC 4364. It is mostly based on the Loopback0 (Router ID) 
of the originating router. 
The RD value associated with an EVPN R-T message is 8-octet in size comprising of a 2-
byte Type field and a 6-byte value field. For EVPN routes, the 2-byte Type Field is set to 0x1 
(per RFC 7432) and the value field is interpreted as shown in the below figure. There are 
three AOS object types supported for the RD: The service object type, the ESI object type, 
and the prefix route object type.: 
 
The object type field value and ID fields are generated based on the type of object. For the 
Service and Prefix Object Type, this will correspond to the MAC-VRF and IP-VRF tables 
respectively. 
 
Object Type 
Value 
Description 
AOS will support two models: VLAN-based service interface model and Enhanced 
VLAN-bundle Service Interface (ALE Defined) model. 

<<<PAGE 43>>>
Architecture Guide 
EVPN 
43 
Service Object Type 
0x0 (000) 
Indicates that the RD is associated with an 
EVI object (for R-T1B, R-T2 and R-T3). The 
Virtual Forwarding Instance (VFI) allocated 
for the EVI will identify the 13-bit Object ID 
(Range 1 - 8191) 
ESI Object Type 
0x1 (001) 
Indicates that the RD is associated with an 
ESI object (for R-T1A and R-T4) 
The 13-bit Object-ID is derived as: 8-bit Local 
Segment ID + 5-bit Fragment ID 
The local segment ID is a switch local 
numeric value associated with a locally 
configured ES. 
The 8-bit value will limit the number of locally 
configurable ES to a maximum of 256 
Segments. 
Prefix Object Type 
0x2 (010) 
Indicates that the RD is associated with a VRF 
object (for R-T5) 
The VRF-ID associated with the prefix-route 
object will identify the 13-bit Object ID (range 
1 to 8191) 
The service domain is identified by a VNI which is translated into a Service Manger service 
ID to represent a virtual forwarding instance (VFI). In the service domain, each VFI is 
accessed through a virtual port, referred to as a Service Access Point (SAP).  
For example, assuming Loopback ID of 1.1.1.1, for R-T2, the value of RD that will be 
generated will be the concatenation of: 
• 
Loopback ID = 1.1.1.1 
• 
Object Type = Service Object Type = 0x0 (000) 
• 
Object ID = VFI = 1 (0000000000001) 
So, the auto-generated RD is 1.1.1.1:1. 
The RT is also auto-generated using the ASN + Etag (VNI). 
AOS Multicast Optimizations 
As previously explained in the Multicast Optimizations section, by default on a multi-
homed ES, only the DF will originate R-T6 for the groups learnt on the multi-homed ES. 
This causes an issue in the event of a DF change where traffic from remote PEs will 
continue to forward the traffic to older PE until they receive the SMET routes form the new 
PE. 
‘SMET by all PEs’ is a feature designed to address to minimize the traffic loss in DF change 
events. By enabling this feature (SMETs by all PEs), all the PEs will originate R-T6 routes. 
So, the remote PEs receive SMETs form all the PEs of the multi-homed ES and so forward 
the traffic to all PEs. But, the traffic will be forwarded only by the DF to the SAPs. In the 
case of DF change event, the new elected DF will start forwarding the traffic as it is 
already receiving traffic from remote PEs. This way the traffic loss is minimized. The 

<<<PAGE 44>>>
Architecture Guide 
EVPN 
44 
disadvantage with this approach is that there will be traffic duplication in the core, 
wasting the bandwidth. So, this feature is recommended for customer scenarios in which 
the traffic loss is a concern. 
 
EVPN Architecture Design  
We will discuss certain design considerations based upon a Data Centre use case, but they 
can be similarly applied to an enterprise campus architecture. 
Network Topology Recommendations 
Typically, EVPN-VXLAN will require a spine and leaf-based topology. While support is 
available for EVPN in networks with a full or partial mesh topology, spine and leaf 
architecture is the most relevant deployment of EVPN.  
 
As shown in the architecture above, this tiered topology provides multi-path redundancy 
for both the CE multi-homing and for inter-leaf connectivity.  
The EVPN network depends on a Spine and Leaf topology for optimum performance. Here 
each ES is guaranteed to have equal cost paths to the peer leaf nodes of the ES from any 
other leaf in the VXLAN network. Thus, EVPN can advertises the ES from different peer 
VTEP/leaf Nodes to other/remote leaf nodes in the network without having to account for 
the path costs from remote nodes to the Peer VTEPs. 
While a 2-tier network is depicted above, a 3-tier spine and leaf topology can also be 
considered for deployments that require hyper scalability. This is typically the case for 
Data Center Interconnectivity (DCI). Here the topology will consist of a Super-Spine layer 
that provides the inter-site gateway functionality. This is especially beneficial when the 
core network (inter-site) is operating in a different overlay protocol (ex: MPLS) or when it 
is required to have a decoupled intra-site and inter-site operation in order to sustain the 
complexity of a multi-site EVPN network. 

<<<PAGE 45>>>
Architecture Guide 
EVPN 
45 
 
Underlay/Overlay Design Options 
There are multiple options to consider for your underlay network which we have covered 
in the Data Center Reference Design Solution Guide referenced in the Related 
Documents section. Typically, the options which are configured in Data Center topologies 
include OSPF/IS-IS underlay with an iBGP overlay, or eBGP for both underlay and overlay. 
The recommended topology to be used is an OSPF underlay with iBGP overlay. 
 
For an optimum BGP EVPN session convergence, the best practice recommendations and 
considerations below can be configured in your underlay and overlay network, assuming a 
typical spine-and-leaf architecture: 
- 
Use a single-area OSPF configuration to limit the SPF flooding domain. 

<<<PAGE 46>>>
Architecture Guide 
EVPN 
46 
- 
Using point-to-point OSPF network type between the switches with routed VLAN-
based IP interfaces. This eliminates DR election wait times. 
- 
Using BFD for millisecond fast-convergence and failure detection on the OSPF-
enabled interfaces. 
- 
ECMP for efficient multi-pathing. This is usually enabled by default. 
- 
Fine-tuning OSPF SPF timers to optimize convergence. 
- 
MTU should be considered in your underlay to allow for overhead of the VXLAN 
header. This is automtically adjusted in AOS. 
- 
For larger topologies, configure the spines as redundant Route Reflectors (RRs) to 
avoid full-mesh BGP configuration. Use the same cluster ID in the spines as it will 
save on memory usage and resources. This is because routes received with the 
same cluster ID are not considered. 
- 
In case using Redundant RRs, it is recommended to enable TTL Security feature 
and set the max-hops to 0. This will provide optimal reachability between leaf 
switches and the Redundant RR. This is because if the direct connection between 
the leaf and spine is down, the BGP neighbor will take the alternate path which is 
not direct connection. This feature will bring the BGP neighbor down when direct 
connection goes down. 
The EVPN-VXLAN is operational in only one underlay VRF which is usually the default VRF, 
with the overlay configured in a non-default VRF. 
Please refer to the Data Center Reference Design Solution Guide referenced in the 
Related Documents section for more details about different spine-and-leaf architectures 
and considerations. 
External Connectivity  
The most basic requirement for prefix-based routing is to provide access to external 
network for the host devices of an EVPN network. This model will only be supported with 
symmetric IRB-based routing. i.e. it is mandatory to configure a Fabric-VPN for the PE(s) 
that needs reachability to the prefix-route. Typically, one PE node in the EVPN network will 
act as a border leaf to the external network. This PE will act as the gateway node for all 
other PEs of the EVPN network in order for their hosts to route to external networks. 
 

<<<PAGE 47>>>
Architecture Guide 
EVPN 
47 
 
In the example shown above, border leaf (LEAF-1) has reachability to external network 
192.168.0.X/24 in VRF-2 and hosts are spread across different EVPN nose of the network 
and operational in VRF-1. For the hosts attached to ESIs to be able to reach the external 
network, a Fabric-VPN (EVI-50) and a gateway interface IP, for example 50.50.50.X(LEAF-
X)/24 must be configured across all the PEs which host these ESIs. In this case, LEAF-1 
should export the routes from VRF-2 to the Global Route Manager (GRM) and the Fabric-
VPN (EVI-50) should register with the GRM to receive these routes from VRF-2. The GRM 
can then redistribute the routes from VRF-2 to EVI-50. LEAF-1 then advertises R-T5 as per 
the below: 
  
Route Distinguisher  
LEAF-1 Loopback0:VRF-1 
ESI 
0 
ETag 
0 
IP Address Length  
24 
IP Address  
192.168.0.0 
Gateway IP Address 
50.50.50.1 
L3VNI  
50 
The remote PEs will import the R-T5 into the RIB if there is a matching RT configured on 
that PE. The VRF-1 on the remote PEs will import the routes from GRM and insert the route 
in the RIB. Any hosts on this VRF can now establish reachability to the external route. 

<<<PAGE 48>>>
Architecture Guide 
EVPN 
48 
In the case of reachability for local hosts on the border leaf, the route must be 
redistributed between the VRFs (in this case from VRF-2 to VRF-1).  
Border Leaf Connectivity Considerations 
In case you are using a border leaf to an external network, there is a need to summarize 
the host routes under the subnet of their IRB interface. This will avoid an issue if there is a 
large number of host routes that are advertised through the EVPN BGP R-T2 messages. 
The border leaf will advertise all the host routes to the external network leading to 
excessive load in both the control-plane and the data-plane of the external router. 
A route-map policy needs to be defined with a specific ACL. This ACLwill contain only the 
aggregate route for each IRB subnets of the EVPN network.  
Assuming you are using OSPF for external route advertisement, the route redistribution 
from EVPN to OSPF should only include routes that match this route-map policy. All other 
routes such as the host-routes will be omitted from the redistribution. 
Another consideration is in case you decide to use redundant border leaf nodes which are 
connected to an external router, it is possible for the external router to echo a route from 
one border leaf back to the other border leaf. 
To prevent this behavior, and assuming you are using OSPF for external route 
advertisement, the import routes should have to be configured to have a higher route-
preference than the OSPF routes (lower value than OSPF). This will ensure that the host 
has only one direct tunnel path from the border-node to a local PE.  
The default setting is for import routes have a lower precedence than OSPF. 
 
EVPN Configuration Example 
The topology below is an example of the leaf-and-spine topology that will be configured 
with EVPN-VXLAN with the recommended configuration. The simplicity of enabling and 
deploying AOS EVPN based services is highlighted in the configuration example.  
The goal is to provide connectivity between all clients and between clients and the 
external network. Different types of configurations have been added to accommodate 
most of the features. 
The CE devices have been pre-configured for LAG and the required VLAN tagging. The 
below subnets will be configured for L3VPN services in the EVPN fabric: 
 
VRF 
VLAN 
Service 
VNI 
VM 
Name 
IP Address 
Default 
Gateway 
VRF-1 
940 
100 
1000 
Client-1 
10.10.94.50/24 
10.10.94.254 
VRF-1 
950 
200 
2000 
Client-2 
10.10.95.50/24 
10.10.95.254 
VRF-1 
960 
300 
3000 
Client-3 
10.10.96.50/24 
10.10.96.254 
VRF-1 
970 
400 
4000 
Client-4 
10.10.97.50/24 
10.10.97.254 
VRF-1 
980 
500 
5000 
Client-5 
10.10.98.50/24 
10.10.98.254 

<<<PAGE 49>>>
Architecture Guide 
EVPN 
49 
VRF-1 
990 
600 
6000 
Client-6 
10.10.99.50/24 
10.10.99.254 
 
The below Fabric-VPN configuration will be configured on all the Leaf switches in the EVPN 
Fabric: 
VRF 
LEAF 
Service 
VNI 
IP Address 
VRF-1 
LEAF-1 
50 
50 
50.50.50.1/24 
VRF-1 
LEAF-2 
50 
50 
50.50.50.2/24 
VRF-1 
LEAF-3 
50 
50 
50.50.50.3/24 
VRF-1 
LEAF-4 
50 
50 
50.50.50.4/24 
VRF-1 
LEAF-5 
50 
50 
50.50.50.5/24 
VRF-1 
LEAF-6 
50 
50 
50.50.50.6/24 
 
OSPF Underlay Configuration 
The first step to build our topology is to configure the routed underlay. The following 
steps will be taken to configure it: 
1. Configure the Loopback0 address for each switch.  
2. Configure the router ID for both OSPF and BGP overlay. This will be the same as 
the Loopback0 address. 
3. Configure the inter-switch links as router VLAN-based ports. Below is the address 
details: 
 
VLAN 
Inter-Switch Link 
Subnet 
11 
SPINE-1 and LEAF-1 
11.11.11.0/24 
12 
SPINE-1 and LEAF-2 
12.12.12.0/24 

<<<PAGE 50>>>
Architecture Guide 
EVPN 
50 
13 
SPINE-1 and LEAF-3 
13.13.13.0/24 
14 
SPINE-1 and LEAF-4 
14.14.14.0/24 
15 
SPINE-1 and LEAF-5 
15.15.15.0/24 
16 
SPINE-1 and LEAF-6 
16.16.16.0/24 
21 
SPINE-2 and LEAF-1 
21.21.21.0/24 
22 
SPINE-2 and LEAF-2 
22.22.22.0/24 
23 
SPINE-2 and LEAF-3 
23.23.23.0/24 
24 
SPINE-2 and LEAF-4 
24.24.24.0/24 
25 
SPINE-2 and LEAF-5 
25.25.25.0/24 
26 
SPINE-2 and LEAF-6 
26.26.26.0/24 
 
4. Configure and enable BFD sessions on the inter-switch links and set the required 
timers. 
5. Load and enable OSPF. Then create a backbone area to connect the routers. 
6. Create the OSPF interfaces for each of the inter-switch links. 
7. Choose network type point-to-point for each of the OSPF interfaces 
8. Register OSPF with the BFD protocol and enable the BFD sessions on the specific 
OSPF interfaces 
9. Enable BFD subsecond option to allow OSPF to act on interface down events from 
BFD immediately. This is not required on the spines, but recommended on the 
leaves. 
10. Set OSPF SPF delay and hold timers to 0 to trigger SPF calculation immediately 
after receiving LSA from the network. 
 
SPINE-1 
! IP: 
ip interface "Loopback0" address 1.1.1.1 
ip interface "v11" address 11.11.11.1/24 vlan 11 rtr-port port 1/1/49A tagged 
ip interface "v12" address 12.12.12.1/24 vlan 12 rtr-port port 1/1/50A tagged 
ip interface "v13" address 13.13.13.1/24 vlan 13 rtr-port port 1/1/51A tagged 
ip interface "v14" address 14.14.14.1/24 vlan 14 rtr-port port 1/1/52A tagged 
ip interface "v15" address 15.15.15.1/24 vlan 15 rtr-port port 1/1/53A tagged 
ip interface "v16" address 16.16.16.1/24 vlan 16 rtr-port port 1/1/54A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v11" 
ip bfd interface "v11" admin-state enable 
ip bfd interface "v12" 

<<<PAGE 51>>>
Architecture Guide 
EVPN 
51 
ip bfd interface "v12" admin-state enable 
ip bfd interface "v13" 
ip bfd interface "v13" admin-state enable 
ip bfd interface "v14" 
ip bfd interface "v14" admin-state enable 
ip bfd interface "v15" 
ip bfd interface "v15" admin-state enable 
ip bfd interface "v16" 
ip bfd interface "v16" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 1.1.1.1 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v11" 
ip ospf interface "v11" area 0.0.0.0 
ip ospf interface "v11" type point-to-point 
ip ospf interface "v11" bfd-state enable 
ip ospf interface "v11" admin-state enable 
ip ospf interface "v12" 
ip ospf interface "v12" area 0.0.0.0 
ip ospf interface "v12" type point-to-point 
ip ospf interface "v12" bfd-state enable 
ip ospf interface "v12" admin-state enable 
ip ospf interface "v13" 
ip ospf interface "v13" area 0.0.0.0 
ip ospf interface "v13" type point-to-point 
ip ospf interface "v13" bfd-state enable 
ip ospf interface "v13" admin-state enable 
ip ospf interface "v14" 
ip ospf interface "v14" area 0.0.0.0 
ip ospf interface "v14" type point-to-point 
ip ospf interface "v14" bfd-state enable 
ip ospf interface "v14" admin-state enable 
ip ospf interface "v15" 
ip ospf interface "v15" area 0.0.0.0 
ip ospf interface "v15" type point-to-point 
ip ospf interface "v15" bfd-state enable 
ip ospf interface "v15" admin-state enable 
ip ospf interface "v16" 
ip ospf interface "v16" area 0.0.0.0 
ip ospf interface "v16" type point-to-point 
ip ospf interface "v16" bfd-state enable 
ip ospf interface "v16" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
SPINE-2 

<<<PAGE 52>>>
Architecture Guide 
EVPN 
52 
! IP: 
ip interface "Loopback0" address 2.2.2.2 
ip interface "v21" address 21.21.21.1/24 vlan 21 rtr-port port 1/1/2A tagged 
ip interface "v22" address 22.22.22.1/24 vlan 22 rtr-port port 1/1/1A tagged 
ip interface "v23" address 23.23.23.1/24 vlan 23 rtr-port port 1/1/3A tagged 
ip interface "v24" address 24.24.24.1/24 vlan 24 rtr-port port 1/1/4A tagged 
ip interface "v25" address 25.25.25.1/24 vlan 25 rtr-port port 1/1/5A tagged 
ip interface "v26" address 26.26.26.1/24 vlan 26 rtr-port port 1/1/6A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v21" 
ip bfd interface "v21" admin-state enable 
ip bfd interface "v22" 
ip bfd interface "v22" admin-state enable 
ip bfd interface "v23" 
ip bfd interface "v23" admin-state enable 
ip bfd interface "v24" 
ip bfd interface "v24" admin-state enable 
ip bfd interface "v25" 
ip bfd interface "v25" admin-state enable 
ip bfd interface "v26" 
ip bfd interface "v26" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 2.2.2.2 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v21" 
ip ospf interface "v21" area 0.0.0.0 
ip ospf interface "v21" type point-to-point 
ip ospf interface "v21" bfd-state enable 
ip ospf interface "v21" admin-state enable 
ip ospf interface "v22" 
ip ospf interface "v22" area 0.0.0.0 
ip ospf interface "v22" type point-to-point 
ip ospf interface "v22" bfd-state enable 
ip ospf interface "v22" admin-state enable 
ip ospf interface "v23" 
ip ospf interface "v23" area 0.0.0.0 
ip ospf interface "v23" type point-to-point 
ip ospf interface "v23" bfd-state enable 
ip ospf interface "v23" admin-state enable 
ip ospf interface "v24" 
ip ospf interface "v24" area 0.0.0.0 
ip ospf interface "v24" type point-to-point 
ip ospf interface "v24" bfd-state enable 
ip ospf interface "v24" admin-state enable 
ip ospf interface "v25" 
ip ospf interface "v25" area 0.0.0.0 
ip ospf interface "v25" type point-to-point 
ip ospf interface "v25" bfd-state enable 
ip ospf interface "v25" admin-state enable 

<<<PAGE 53>>>
Architecture Guide 
EVPN 
53 
ip ospf interface "v26" 
ip ospf interface "v26" area 0.0.0.0 
ip ospf interface "v26" type point-to-point 
ip ospf interface "v26" bfd-state enable 
ip ospf interface "v26" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
LEAF-1 
! IP: 
ip interface "Loopback0" address 10.10.10.10 
ip interface "v11" address 11.11.11.2/24 vlan 11 rtr-port port 1/1/27A tagged 
ip interface "v21" address 21.21.21.2/24 vlan 21 rtr-port port 1/1/28A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v11" 
ip bfd interface "v11" admin-state enable 
ip bfd interface "v21" 
ip bfd interface "v21" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 10.10.10.10 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v11" 
ip ospf interface "v11" area 0.0.0.0 
ip ospf interface "v11" type point-to-point 
ip ospf interface "v11" bfd-state enable 
ip ospf interface "v11" admin-state enable 
ip ospf interface "v21" 
ip ospf interface "v21" area 0.0.0.0 
ip ospf interface "v21" type point-to-point 
ip ospf interface "v21" bfd-state enable 
ip ospf interface "v21" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
LEAF-2 
! IP: 
ip interface "Loopback0" address 20.20.20.20 
ip interface "v12" address 12.12.12.2/24 vlan 12 rtr-port port 1/1/28A tagged 

<<<PAGE 54>>>
Architecture Guide 
EVPN 
54 
ip interface "v22" address 22.22.22.2/24 vlan 22 rtr-port port 1/1/27A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v12" 
ip bfd interface "v12" admin-state enable 
ip bfd interface "v22" 
ip bfd interface "v22" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 20.20.20.20 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v12" 
ip ospf interface "v12" area 0.0.0.0 
ip ospf interface "v12" type point-to-point 
ip ospf interface "v12" bfd-state enable 
ip ospf interface "v12" admin-state enable 
ip ospf interface "v22" 
ip ospf interface "v22" area 0.0.0.0 
ip ospf interface "v22" type point-to-point 
ip ospf interface "v22" bfd-state enable 
ip ospf interface "v22" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
LEAF-3 
! IP: 
ip interface "Loopback0" address 30.30.30.30 
ip interface "v13" address 13.13.13.2/24 vlan 13 rtr-port port 1/1/49A tagged 
ip interface "v23" address 23.23.23.2/24 vlan 23 rtr-port port 1/1/50A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v13" 
ip bfd interface "v13" admin-state enable 
ip bfd interface "v23" 
ip bfd interface "v23" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 30.30.30.30 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v13" 
ip ospf interface "v13" area 0.0.0.0 

<<<PAGE 55>>>
Architecture Guide 
EVPN 
55 
ip ospf interface "v13" type point-to-point 
ip ospf interface "v13" bfd-state enable 
ip ospf interface "v13" admin-state enable 
ip ospf interface "v23" 
ip ospf interface "v23" area 0.0.0.0 
ip ospf interface "v23" type point-to-point 
ip ospf interface "v23" bfd-state enable 
ip ospf interface "v23" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
LEAF-4 
! IP: 
ip interface "Loopback0" address 40.40.40.40 
ip interface "v14" address 14.14.14.2/24 vlan 14 rtr-port port 1/1/49A tagged 
ip interface "v24" address 24.24.24.2/24 vlan 24 rtr-port port 1/1/50A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v14" 
ip bfd interface "v14" admin-state enable 
ip bfd interface "v24" 
ip bfd interface "v24" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 40.40.40.40 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v14" 
ip ospf interface "v14" area 0.0.0.0 
ip ospf interface "v14" type point-to-point 
ip ospf interface "v14" bfd-state enable 
ip ospf interface "v14" admin-state enable 
ip ospf interface "v24" 
ip ospf interface "v24" area 0.0.0.0 
ip ospf interface "v24" type point-to-point 
ip ospf interface "v24" bfd-state enable 
ip ospf interface "v24" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
LEAF-5 

<<<PAGE 56>>>
Architecture Guide 
EVPN 
56 
! IP: 
ip interface "Loopback0" address 50.50.50.50 
ip interface "v15" address 15.15.15.2/24 vlan 15 rtr-port port 1/1/49A tagged 
ip interface "v25" address 25.25.25.2/24 vlan 25 rtr-port port 1/1/50A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v15" 
ip bfd interface "v15" admin-state enable 
ip bfd interface "v25" 
ip bfd interface "v25" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 50.50.50.50 
! OSPF: 
ip load ospf 
ip ospf area 0.0.0.0 
ip ospf interface "v15" 
ip ospf interface "v15" area 0.0.0.0 
ip ospf interface "v15" type point-to-point 
ip ospf interface "v15" bfd-state enable 
ip ospf interface "v15" admin-state enable 
ip ospf interface "v25" 
ip ospf interface "v25" area 0.0.0.0 
ip ospf interface "v25" type point-to-point 
ip ospf interface "v25" bfd-state enable 
ip ospf interface "v25" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
 
LEAF-6 
! IP: 
ip interface "Loopback0" address 60.60.60.60 
ip interface "v15" address 16.16.16.2/24 vlan 16 rtr-port port 1/1/49A tagged 
ip interface "v25" address 26.26.26.2/24 vlan 26 rtr-port port 1/1/50A tagged 
! BFD: 
ip bfd transmit 200 
ip bfd receive 200 
ip bfd echo-interval 200 
ip bfd interface "v16" 
ip bfd interface "v16" admin-state enable 
ip bfd interface "v26" 
ip bfd interface "v26" admin-state enable 
ip bfd admin-state enable 
! IP Route Manager: 
ip router router-id 60.60.60.60 
! OSPF: 
ip load ospf 

<<<PAGE 57>>>
Architecture Guide 
EVPN 
57 
ip ospf area 0.0.0.0 
ip ospf interface "v16" 
ip ospf interface "v16" area 0.0.0.0 
ip ospf interface "v16" type point-to-point 
ip ospf interface "v16" bfd-state enable 
ip ospf interface "v16" admin-state enable 
ip ospf interface "v26" 
ip ospf interface "v26" area 0.0.0.0 
ip ospf interface "v26" type point-to-point 
ip ospf interface "v26" bfd-state enable 
ip ospf interface "v26" admin-state enable 
ip ospf spf-timer delay 0 
ip ospf spf-timer hold 0 
ip ospf bfd-state enable 
ip ospf admin-state enable 
BGP Overlay Configuration 
The next step is to configure the iBGP overlay network with with both the IPv4 unicast 
AFI/SAFI and the L2VPN-EVPN AFI/SAFI. In this configuration example, we are using single 
cluster with redundant Route Reflector (RR) topology, which provides both control and 
data plane redundancy. 
The following steps will be taken to configure it: 
1. Load and enable BGP. Set the ASN to be the same for all the switches. 
2. Enable the EVPN advertisements for the BGP routing process. 
3. Configure the iBGP peering sessions with the loopback interfaces. Set the “update-
source” as the loopback interface 
4. Activate EVPN capability for each peer in BGP. 
5. Configure TTL Security Max-Hop feature and set to 0.  
 
SPINE-1 
! BGP: 
ip load bgp 
ip bgp autonomous-system 65000 
ip bgp client-to-client reflection 
ip bgp cluster-id 1.1.1.1 
ip bgp address-family evpn 
ip bgp neighbor 10.10.10.10 
ip bgp neighbor 10.10.10.10 remote-as 65000 
ip bgp neighbor 10.10.10.10 route-reflector-client 
ip bgp neighbor 10.10.10.10 update-source "Loopback0" 
ip bgp neighbor 10.10.10.10 activate-evpn 
ip bgp neighbor 10.10.10.10 admin-state enable 
ip bgp neighbor 10.10.10.10 ttl-security 0 
ip bgp neighbor 20.20.20.20 
ip bgp neighbor 20.20.20.20 remote-as 65000 
ip bgp neighbor 20.20.20.20 route-reflector-client 

<<<PAGE 58>>>
Architecture Guide 
EVPN 
58 
ip bgp neighbor 20.20.20.20 update-source "Loopback0" 
ip bgp neighbor 20.20.20.20 activate-evpn 
ip bgp neighbor 20.20.20.20 admin-state enable 
ip bgp neighbor 20.20.20.20 ttl-security 0 
ip bgp neighbor 30.30.30.30 
ip bgp neighbor 30.30.30.30 remote-as 65000 
ip bgp neighbor 30.30.30.30 route-reflector-client 
ip bgp neighbor 30.30.30.30 update-source "Loopback0" 
ip bgp neighbor 30.30.30.30 activate-evpn 
ip bgp neighbor 30.30.30.30 admin-state enable 
ip bgp neighbor 30.30.30.30 ttl-security 0 
ip bgp neighbor 40.40.40.40 
ip bgp neighbor 40.40.40.40 remote-as 65000 
ip bgp neighbor 40.40.40.40 route-reflector-client 
ip bgp neighbor 40.40.40.40 update-source "Loopback0" 
ip bgp neighbor 40.40.40.40 activate-evpn 
ip bgp neighbor 40.40.40.40 admin-state enable 
ip bgp neighbor 40.40.40.40 ttl-security 0 
ip bgp neighbor 50.50.50.50 
ip bgp neighbor 50.50.50.50 remote-as 65000 
ip bgp neighbor 50.50.50.50 route-reflector-client 
ip bgp neighbor 50.50.50.50 update-source "Loopback0" 
ip bgp neighbor 50.50.50.50 activate-evpn 
ip bgp neighbor 50.50.50.50 admin-state enable 
ip bgp neighbor 50.50.50.50 ttl-security 0 
ip bgp neighbor 60.60.60.60 
ip bgp neighbor 60.60.60.60 remote-as 65000 
ip bgp neighbor 60.60.60.60 route-reflector-client 
ip bgp neighbor 60.60.60.60 update-source "Loopback0" 
ip bgp neighbor 60.60.60.60 activate-evpn 
ip bgp neighbor 60.60.60.60 admin-state enable 
ip bgp neighbor 60.60.60.60 ttl-security 0 
ip bgp admin-state enable 
 
SPINE-2 
! BGP: 
ip load bgp 
ip bgp autonomous-system 65000 
ip bgp client-to-client reflection 
ip bgp cluster-id 1.1.1.1 
ip bgp address-family evpn 
ip bgp neighbor 10.10.10.10 
ip bgp neighbor 10.10.10.10 remote-as 65000 
ip bgp neighbor 10.10.10.10 route-reflector-client 
ip bgp neighbor 10.10.10.10 update-source "Loopback0" 
ip bgp neighbor 10.10.10.10 activate-evpn 
ip bgp neighbor 10.10.10.10 admin-state enable 
ip bgp neighbor 10.10.10.10 ttl-security 0 
ip bgp neighbor 20.20.20.20 
ip bgp neighbor 20.20.20.20 remote-as 65000 
ip bgp neighbor 20.20.20.20 route-reflector-client 

<<<PAGE 59>>>
Architecture Guide 
EVPN 
59 
ip bgp neighbor 20.20.20.20 update-source "Loopback0" 
ip bgp neighbor 20.20.20.20 activate-evpn 
ip bgp neighbor 20.20.20.20 admin-state enable 
ip bgp neighbor 20.20.20.20 ttl-security 0 
ip bgp neighbor 30.30.30.30 
ip bgp neighbor 30.30.30.30 remote-as 65000 
ip bgp neighbor 30.30.30.30 route-reflector-client 
ip bgp neighbor 30.30.30.30 update-source "Loopback0" 
ip bgp neighbor 30.30.30.30 activate-evpn 
ip bgp neighbor 30.30.30.30 admin-state enable 
ip bgp neighbor 30.30.30.30 ttl-security 0 
ip bgp neighbor 40.40.40.40 
ip bgp neighbor 40.40.40.40 remote-as 65000 
ip bgp neighbor 40.40.40.40 route-reflector-client 
ip bgp neighbor 40.40.40.40 update-source "Loopback0" 
ip bgp neighbor 40.40.40.40 activate-evpn 
ip bgp neighbor 40.40.40.40 admin-state enable 
ip bgp neighbor 40.40.40.40 ttl-security 0 
ip bgp neighbor 50.50.50.50 
ip bgp neighbor 50.50.50.50 remote-as 65000 
ip bgp neighbor 50.50.50.50 route-reflector-client 
ip bgp neighbor 50.50.50.50 update-source "Loopback0" 
ip bgp neighbor 50.50.50.50 activate-evpn 
ip bgp neighbor 50.50.50.50 admin-state enable 
ip bgp neighbor 50.50.50.50 ttl-security 0 
ip bgp neighbor 60.60.60.60 
ip bgp neighbor 60.60.60.60 remote-as 65000 
ip bgp neighbor 60.60.60.60 route-reflector-client 
ip bgp neighbor 60.60.60.60 update-source "Loopback0" 
ip bgp neighbor 60.60.60.60 activate-evpn 
ip bgp neighbor 60.60.60.60 admin-state enable 
ip bgp neighbor 60.60.60.60 ttl-security 0 
ip bgp admin-state enable 
 
LEAF-1/2/3/4/5/6 
! BGP: 
ip load bgp 
ip bgp autonomous-system 65000 
ip bgp address-family evpn 
ip bgp neighbor 1.1.1.1 
ip bgp neighbor 1.1.1.1 remote-as 65000 
ip bgp neighbor 1.1.1.1 update-source "Loopback0" 
ip bgp neighbor 1.1.1.1 activate-evpn 
ip bgp neighbor 1.1.1.1 admin-state enable 
ip bgp neighbor 1.1.1.1 ttl-security 0 
ip bgp neighbor 2.2.2.2 
ip bgp neighbor 2.2.2.2 remote-as 65000 
ip bgp neighbor 2.2.2.2 update-source "Loopback0" 
ip bgp neighbor 2.2.2.2 activate-evpn 
ip bgp neighbor 2.2.2.2 admin-state enable 
ip bgp neighbor 2.2.2.2 ttl-security 0 

<<<PAGE 60>>>
Architecture Guide 
EVPN 
60 
ip bgp admin-state enable 
 
Verification Commands 
We can verify that the BGP neighborship has been established and the EVPN address 
family is activated and advertised for each neighbor: 
LEAF-1 
LEAF-3> show ip bgp neighbors 
Legends: Nbr = Neighbor 
         As  = Autonomous System 
Nbr address     As          Admin state Oper state   BGP Id          Up/Down     BFD Status 
---------------+-----------+-----------+------------+---------------+-----------+---------- 
1.1.1.1         65000       enabled     idle         0.0.0.0         00h:00m:00s enabled 
2.2.2.2         65000       enabled     idle         0.0.0.0         00h:00m:00s enabled 
 
LEAF-3> show ip bgp neighbors 1.1.1.1 
Neighbor address                  = 1.1.1.1, 
Neighbor autonomous system        = 65000, 
Neighbor Admin state              = enabled, 
Neighbor Oper state               = established, 
Neighbor passive status           = disabled, 
Neighbor name                     = peer(1.1.1.1), 
Neighbor local address            = Loopback0, 
Neighbor EBGP multiHop            = disabled, 
Neighbor next hop self            = disabled, 
Neighbor TTL security             = 0, 
Neighbor Route Refresh            = enabled, 
Neighbor Ipv4 unicast             = enabled, 
… <OUTPUT OMMITTED> …  
BFD Status                        = enabled, 
Activate IPv4 unicast             = enabled, 
Activate evpn                     = enabled, 
Neighbor evpn                     = advertised, 
Activate evpn fabric nbr          = disabled, 
Activate check-first-AS           = enabled, 
Activate L2VPN vpls               = disabled, 
Neighbor L2VPN vpls               = not-advertised 
Neighbor Template                 = none 
 
Link Aggregation Configuration 
In this part of the configuration, we will configure the LACP link aggregation on the Leaf 
switches as per the configuration performed in the CE. In our topology, LEAF-1 to LEAF-3 
have LACP link aggregation configuration since they are performing all-active multi-
homing, while LEAF-6 is performing static link aggregation: 
 
LEAF-1/2/3 

<<<PAGE 61>>>
Architecture Guide 
EVPN 
61 
! Link Aggregate: 
linkagg lacp agg 10 size 3 admin-state enable 
linkagg lacp agg 10 actor system-id 78:24:59:64:69:9a 
linkagg lacp agg 10 actor admin-key 10 
linkagg lacp port 1/1/3 actor admin-key 10 
 
LEAF-6 
! Link Aggregate: 
linkagg static agg 20 size 2 admin-state enable 
linkagg static port 1/1/3 agg 20 
linkagg static port 1/1/4 agg 20 
 
Verification Commands 
We can verify the link aggregation configuration using the commands below: 
LEAF-1/2/3 
LEAF-1> show linkagg 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  10     Dynamic      40000010   3   ENABLED      UP              1   1 
 
LEAF-1> show linkagg agg 10 port 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
          1/1/3     Dynamic      1003   ATTACHED     10  UP   UP    YES 
 
LEAF-6 
LEAF-6> show linkagg 
Number  Aggregate     SNMP Id   Size Admin State  Oper State     Att/Sel Ports 
-------+-------------+---------+----+------------+--------------+------------- 
  20     Static       40000020   2   ENABLED      UP              2   2 
 
LEAF-6> show linkagg agg 20 port 
Chassis/Slot/Port  Aggregate   SNMP Id   Status    Agg  Oper   Link Prim 
-------------------+----------+--------+----------+----+-----+-----+---- 
          1/1/3     Static       1003   ATTACHED     20  UP   UP    YES 
          1/1/4     Static       1004   ATTACHED     20  UP   UP    NO 
VRF/Fabric-VPN Configuration 
As per our topology, we will configure a Fabric-VPN (SBD) in VRF-1 established among the 
Leaf switches in L3EVI 50. This will be used for symmetric IRB and inter-subnet routing. 
We will also configure the import/export of all routes from the VRF routing table into the 

<<<PAGE 62>>>
Architecture Guide 
EVPN 
62 
Fabric-VPN EVI 50. This will allow the external prefixes to be imported, which will be 
automatically advertised once we learn the external prefixes. This will be configured in the 
External Route Advertisement section. 
 
 
LEAF-1 
vrf create vrf1 
<vrf vrf1> ip interface "Fabric-VPN" address 50.50.50.1 mask 255.255.255.0 service 50 
<vrf vrf1> service 50 vxlan vnid 50 bgp-evpn enable vlan-xlation enable vpn-type fabric-vpn 
<vrf vrf1> ip export all-routes 
<vrf vrf1> ip import evi 50 all-routes 
 
LEAF-2 
vrf create vrf1 
<vrf vrf1> ip interface "Fabric-VPN" address 50.50.50.2 mask 255.255.255.0 service 50 
<vrf vrf1> service 50 vxlan vnid 50 bgp-evpn enable vlan-xlation enable vpn-type fabric-vpn 
<vrf vrf1> ip export all-routes 
<vrf vrf1> ip import evi 50 all-routes 
 
LEAF-3 
vrf create vrf1 
<vrf vrf1> ip interface "Fabric-VPN" address 50.50.50.3 mask 255.255.255.0 service 50 
<vrf vrf1> service 50 vxlan vnid 50 bgp-evpn enable vlan-xlation enable vpn-type fabric-vpn 
<vrf vrf1> ip export all-routes 
<vrf vrf1> ip import evi 50 all-routes 
 
LEAF-4 
vrf create vrf1 
<vrf vrf1> ip interface "Fabric-VPN" address 50.50.50.4 mask 255.255.255.0 service 50 
<vrf vrf1> service 50 vxlan vnid 50 bgp-evpn enable vlan-xlation enable vpn-type fabric-vpn 
<vrf vrf1> ip export all-routes 
<vrf vrf1> ip import evi 50 all-routes 

<<<PAGE 63>>>
Architecture Guide 
EVPN 
63 
 
LEAF-5 
vrf create vrf1 
<vrf vrf1> ip interface "Fabric-VPN" address 50.50.50.5 mask 255.255.255.0 service 50 
<vrf vrf1> service 50 vxlan vnid 50 bgp-evpn enable vlan-xlation enable vpn-type fabric-vpn 
<vrf vrf1> ip export all-routes 
<vrf vrf1> ip import evi 50 all-routes 
 
LEAF-6 
vrf create vrf1 
<vrf vrf1> ip interface "Fabric-VPN" address 50.50.50.6 mask 255.255.255.0 service 50 
<vrf vrf1> service 50 vxlan vnid 50 bgp-evpn enable vlan-xlation enable vpn-type fabric-vpn 
<vrf vrf1> ip export all-routes 
<vrf vrf1> ip import evi 50 all-routes 
 
Verification Commands 
We can verify the Fabric-VPN configuration using the commands below: 
ALL LEAF SWITCHES 
vrf1::LEAF-1> show ip interface 
Total 1 interfaces 
 Flags (D=Directly-bound) 
       (A=Anycast IP) 
            Name                 IP Address      Subnet Mask     Status Forward  Device              Flags 
--------------------------------+---------------+---------------+------+-------+--------------------+------ 
Fabric-VPN                       50.50.50.1      255.255.255.0   UP     YES     service 50 
 
vrf1::LEAF-1> show service evpn 
Legend: * denotes a dynamic object 
EVPN Service Info 
                        Svc         Adm    Oper         SAP   Bind 
ServiceId   EVI         Type        Status Status Stats Count Count Description 
-----------+-----------+-----------+------+------+-----+-----+-----+------------- 
50          50          EVPN-VxLAN  Up     Up      N    0     5 
Total Services: 1 
 
vrf1::LEAF-1> show ip evpn proxy-arp 
*= Local Saps 
#= Static Arps 
@= Inactive Arps 
!= Peer Arps 
(M) Monitored Arps 
(F) Filtered Arps 
EVI        IP Address           Mac-Address        ESI                            ETAG             Adv-PE          Service Id   Interface            SeqNum 
----------+--------------------+------------------+------------------------------+----------------+---------------+------------+--------------------+-------- 
50         50.50.50.2 #         78:24:59:64:69:91  00:00:00:00:00:00:00:00:00:00  0                20.20.20.20     50           32768:50             0 
50         50.50.50.3 #         78:24:59:7e:35:4d  00:00:00:00:00:00:00:00:00:00  0                30.30.30.30     50           32769:50             0 
50         50.50.50.4 #         78:24:59:7d:85:4b  00:00:00:00:00:00:00:00:00:00  0                40.40.40.40     50           32770:50             0 
50         50.50.50.5 #         78:24:59:75:55:c9  00:00:00:00:00:00:00:00:00:00  0                50.50.50.50     50           32771:50             0 
50         50.50.50.6 #         78:24:59:75:55:39  00:00:00:00:00:00:00:00:00:00  0                60.60.60.60     50           32772:50             0 
Total count: 5 
 

<<<PAGE 64>>>
Architecture Guide 
EVPN 
64 
EVPN-VXLAN Service Access Port and Multi-Homing 
Configuration 
Next, we will configure the Service Access Ports and the ES with the required type of multi-
homing configuration: 
LEAF-1/2/3 
service access linkagg 10 vlan-xlation enable evpn-ethernet-segment enable multi-homing all-active 
 
LEAF-4 
service access port 1/1/3 vlan-xlation enable evpn-ethernet-segment enable 
Since we are using static link aggregation on LEAF-6, the first 5-octets of the ESI has to be 
provided for an ES. On a dynamic lingkagg, and physical port, ESI is auto generated: 
LEAF-6 
service access linkagg 20 vlan-xlation enable evpn-ethernet-segment enable esi 01:01:01:02:04 
 
Verification Commands 
We can verify our configuration using the commands below: 
LEAF-1 
LEAF-1> show service evpn ethernet-segment 
All Ethernet Segment[ES] Info 
PE: 
Legend: L-Local, R-Remote, A-Auto, M-Manual, SH-Single-Homing, MH-Multi-Homing, 
        SA-Single-Active, AA-All-Active I-InterSite 
                              ES-CLASS   RT/EVI ETag  Adm    Oper   Interface       Description 
ESID                          [TYPE]     Count  Count Status Status 
-----------------------------+----------+------+-----+------+------+---------------+----------- 
03:2c:fa:a2:c0:d4:d3:00:0a:00 MH-AA[L-A] -      -     Up     Up     0/10            0/10 
Total ES: 1 
 
 
LEAF-4 
LEAF-4> show service evpn ethernet-segment 
All Ethernet Segment[ES] Info 
PE: 

<<<PAGE 65>>>
Architecture Guide 
EVPN 
65 
Legend: L-Local, R-Remote, A-Auto, M-Manual, SH-Single-Homing, MH-Multi-Homing, 
        SA-Single-Active, AA-All-Active I-InterSite 
                              ES-CLASS   RT/EVI ETag  Adm    Oper   Interface       Description 
ESID                          [TYPE]     Count  Count Status Status 
-----------------------------+----------+------+-----+------+------+---------------+----------- 
03:78:24:59:7d:85:54:ff:ff:ff SH[L-A]    -      -     Up     Up     1/1/3           1/1/3 
Total ES: 1 
 
LEAF-6 
LEAF-6> show service evpn ethernet-segment 
All Ethernet Segment[ES] Info 
PE: 
Legend: L-Local, R-Remote, A-Auto, M-Manual, SH-Single-Homing, MH-Multi-Homing, 
        SA-Single-Active, AA-All-Active I-InterSite 
                              ES-CLASS   RT/EVI ETag  Adm    Oper   Interface       Description 
ESID                          [TYPE]     Count  Count Status Status 
-----------------------------+----------+------+-----+------+------+---------------+----------- 
03:a1:01:01:01:02:04:ff:ff:01 MH-SA[L-M] -      -     Up     Up     0/20            0/20 
Total ES: 1 
 
EVPN-VXLAN Services Provisioning 
Since we will be using symmetric IRB in this configuration example, it is not required to 
have all the services instantiated in all leaf switches, but only where the hosts are 
attached. 
LEAF-1/2/3 
vrf vrf1 
<vrf vrf1> service 100 vxlan vnid 1000 bgp-evpn enable vlan-xlation enable 
<vrf vrf1> service 200 vxlan vnid 2000 bgp-evpn enable vlan-xlation enable 
<vrf vrf1> service 300 vxlan vnid 3000 bgp-evpn enable vlan-xlation enable 
<vrf vrf1> service 100 sap linkagg 10:940 
<vrf vrf1> service 200 sap linkagg 10:950 
<vrf vrf1> service 300 sap linkagg 10:960 
 
LEAF-4 
vrf vrf1 
<vrf vrf1> service 400 vxlan vnid 4000 bgp-evpn enable vlan-xlation enable 
<vrf vrf1> service 500 vxlan vnid 5000 bgp-evpn enable vlan-xlation enable 
<vrf vrf1> service 400 sap port 1/1/3:970 
<vrf vrf1> service 500 sap port 1/1/3:980 
 

<<<PAGE 66>>>
Architecture Guide 
EVPN 
66 
LEAF-6 
vrf vrf1 
<vrf vrf1> service 600 vxlan vnid 6000 bgp-evpn enable vlan-xlation enable 
<vrf vrf1> service 600 sap linkagg 20:990 
 
 
 
Verification Commands 
We can verify the EVPN service configuration and status: 
LEAF-1 
vrf1::LEAF-1> show service evpn 
Legend: * denotes a dynamic object 
EVPN Service Info 
                        Svc         Adm    Oper         SAP   Bind 
ServiceId   EVI         Type        Status Status Stats Count Count Description 
-----------+-----------+-----------+------+------+-----+-----+-----+------------- 
50          50          EVPN-VxLAN  Up     Up      N    0     5 
100         1000        EVPN-VxLAN  Up     Up      N    1     2 
200         2000        EVPN-VxLAN  Up     Up      N    1     2 
300         3000        EVPN-VxLAN  Up     Up      N    1     2 
 
Total Services: 4 
We can also verify the tunnel SDP port details per EVI: 
LEAF-1 
vrf1::LEAF-1> show service evpn evi 1000 tunnel-ports 
EVPN Service Detailed Info 
  Service Id      : 100,                   Description     : - 
  EVI             : 1000, 
  Multicast-Mode  : Hybrid, 
  Admin Status    : Up,                    Oper Status     : Up 
  Stats Status    : No,                    Vlan Translation: Yes 
  Service Type    : VxLAN,                 Allocation Type : Static 
  MTU             : 9194,                  VPN IP-MTU      : 1500 
  SAP Count       : 1,                     SDP Bind Count  : 2 
  RemoveIngressTag: No,                    Option          : None 
  BGP-EVPN        : Ena, 
    Mac-Advertisement: Ena,                  Proxy-Arp        : Ena 
    Unknown-Mac-Route: Ena,                  Mac-Vrf-Hw-Lrng  : Dis 
    OISM: Dis,                               PEG: Dis, 
    Igmp-Proxy: Disable,                     Mld-Proxy:  Disable 
    Smet-Capability:  Disable,               Smet-on-Multihome:  DF 
Please ensure that the SAP is configured consistently on all peer nodes of a MH-
ES, otherwise the remote nodes will only forward traffic to the subset of PE nodes 
that have this ES+ETag attachment configured. This ensures that reachability 
from remote PE to local ES is available even if there is the inconsistency in the 
configuration. However, the CE side traffic towards the PE will be black-holed! (if 
the flow were to hash to the attached PE that has the missing config).   

<<<PAGE 67>>>
Architecture Guide 
EVPN 
67 
  Mgmt Change     : 06/17/2025 18:13:38,  Status Change   : 06/17/2025 18:13:38 
Sdp-Id              Far-End-Info    RD                   IgmpProxy   MLDProxy    OISM      PEG       Gateway 
-------------------+---------------+--------------------+-----------+-----------+---------+-------+------------- 
32768:100           20.20.20.20     20.20.20.20:2        Dis         Dis         Dis         Dis        11.11.11.1 
                                                                                                        21.21.21.1 
32769:100           30.30.30.30     30.30.30.30:2        Dis         Dis         Dis         Dis        11.11.11.1 
                                                                                                        21.21.21.1 
 
Symmetric IRB Configuration 
The next step is to configure the IRB interfaces on our Leaf switches. EVPN IRB feature 
enables a Layer 2 VPN and an Layer 3 VPN overlay that allows end hosts across the overlay 
to communicate with each other within the same subnet and across different subnets 
within the VPN. We will configure symmetric IRB: 
 
LEAF-1 
<vrf vrf1> ip interface l1svc100 service 100 address 10.10.94.1/24 
<vrf vrf1> ip interface l1svc200 service 200 address 10.10.95.1/24 
<vrf vrf1> ip interface l1svc300 service 300 address 10.10.96.1/24 
 
LEAF-2 
<vrf vrf1> ip interface l2svc100 service 100 address 10.10.94.2/24 
<vrf vrf1> ip interface l2svc200 service 200 address 10.10.95.2/24 
<vrf vrf1> ip interface l2svc300 service 300 address 10.10.96.2/24 
 
LEAF-3 
<vrf vrf1> ip interface l3svc100 service 100 address 10.10.94.3/24 
<vrf vrf1> ip interface l3svc200 service 200 address 10.10.95.3/24 
<vrf vrf1> ip interface l3svc300 service 300 address 10.10.96.3/24 
 
LEAF-4 
<vrf vrf1> ip interface l4svc400 service 400 address 10.10.97.4/24 
<vrf vrf1> ip interface l4svc500 service 500 address 10.10.98.4/24 
 
LEAF-6 
<vrf vrf1> ip interface l6svc600 service 600 address 10.10.99.6/24 
 

<<<PAGE 68>>>
Architecture Guide 
EVPN 
68 
Verification Commands 
We can verify our configuration and status: 
LEAF-1 
vrf1::LEAF-1> show ip interface 
Total 4 interfaces 
 Flags (D=Directly-bound) 
       (A=Anycast IP) 
            Name                 IP Address      Subnet Mask     Status Forward  Device              Flags 
--------------------------------+---------------+---------------+------+-------+--------------------+------ 
Fabric-VPN                       50.50.50.1      255.255.255.0   UP     YES     service 50 
l1svc100                         10.10.94.1      255.255.255.0   UP     YES     service 100 
l1svc200                         10.10.95.1      255.255.255.0   UP     YES     service 200 
l1svc300                         10.10.96.1      255.255.255.0   UP     YES     service 300 
DAG Configuration 
To support host mobility with efficiency in a large scalable network, Distributed Anycast 
Gateway (DAG) can be configured on your Leaf switches. The Anycast IP Address is 
configured on all the PEs that share the EVI. Along with the Anycast IP, an anycast MAC-
address (Vitrual MAC) is configured on all the common PEs. This Anycast MAC must be 
setup per VRF and the same Anycast MAC address is used for all subnet Anycast IP 
interfaces of VRFs. The anycast IP which will be configured in the Leaf switches is the 
default gateway configured on the VM host machines. 
LEAF-1/2/3 
<vrf vrf1> ip anycast-gateway-mac auto 
<vrf vrf1> ip interface l1svc100 anycast-gateway-address 10.10.94.254 
<vrf vrf1> ip interface l1svc200 anycast-gateway-address 10.10.95.254 
<vrf vrf1> ip interface l1svc300 anycast-gateway-address 10.10.96.254 
 
LEAF-4 
<vrf vrf1> ip anycast-gateway-mac auto 
<vrf vrf1> ip interface l4svc400 anycast-gateway-address 10.10.97.254 
<vrf vrf1> ip interface l4svc500 anycast-gateway-address 10.10.98.254 
 
LEAF-6 
<vrf vrf1> ip anycast-gateway-mac auto 
<vrf vrf1> ip interface l6svc600 anycast-gateway-address 10.10.99.254 
 
Verification Commands 
You can verify the DAG configuration using the commands below: 

<<<PAGE 69>>>
Architecture Guide 
EVPN 
69 
LEAF-1/2/3/4/6 
vrf1::LEAF-1> show ip interface 
Total 4 interfaces 
 Flags (D=Directly-bound) 
       (A=Anycast IP) 
            Name                 IP Address      Subnet Mask     Status Forward  Device              Flags 
--------------------------------+---------------+---------------+------+-------+--------------------+------ 
Fabric-VPN                       50.50.50.1      255.255.255.0   UP     YES     service 50 
l1svc100                         10.10.94.1      255.255.255.0   UP     YES     service 100              A 
l1svc200                         10.10.95.1      255.255.255.0   UP     YES     service 200              A 
l1svc300                         10.10.96.1      255.255.255.0   UP     YES     service 300              A 
 
vrf1::LEAF-1> show ip interface l1svc100 
Interface Name = l1svc100 
  SNMP Interface Index           =   13600004, 
  IP Address                     =   10.10.94.1, 
  Subnet Mask                    =   255.255.255.0, 
  Broadcast Address              =   10.10.94.255, 
  Device                         =   service 100, 
  Forwarding                     =   enabled, 
  Administrative State           =   enabled, 
  Operational State              =   up, 
  Maximum Transfer Unit          =   1500, 
  Router MAC                     =   78:24:59:55:25:df, 
  Anycast GW Address             =   10.10.94.254, 
 
vrf1::LEAF-1> show ip config 
IP directed-broadcast   =   OFF, 
IP default TTL          =   64 
Distributed ARP         =   OFF, 
Anycast MAC             =   00:00:5e:00:01:01, 
Proxy-arp aging-time    =   300 
 
vrf1::LEAF-1> show service 100 debug-info 
Legend: * denotes a dynamic object 
VxLAN Service 100 Debug Info 
  Admin : Up,        Oper  : Up,     Stats      : N,        VlanXlation : Y, 
  VNID  : 1000 (0.3.232),            MCast-Mode : Hybrid,  RemoveIngTag: N, 
  VFI   : 2,         McIdx : 5,      StatsHandle: 0         BgpEvpn: Enable 
  Igmp-Proxy: Disable,   Mld-Proxy: Disable,   OISM: Disable,        PEG: Disable, 
  Smet-Capability:  Disable,   Smet-on-Multihome:  DF 
  VRF   : vrf1 (1),                  IPv4 MTU   : 1500,      IPv4 Int: l1svc100 (Addr=10.10.94.1/24 Idx=13600004) 
  AnyCastIp: 10.10.94.254 
                                       Sap Trusted:Priority/         Sap Description /                       VP     Stats  / 
Identifier             Adm  Oper Stats Sdp FarEnd/Group     Intf     Sdp Intf Name                    VP     (ECMP) L2 
McIdx 
----------------------+----+----+-----+--------------------+--------+--------------------------------+------+------+-------- 
sap:0/10:940           Up   Up    N           Y:x           0/10        -                             6       -     0 
sdp:32768:100*         Up   Up    Y    20.20.20.20            -      v11 11.11.11.2 11.11.11.1        1       -     1 
                                                                     v21 21.21.21.2 21.21.21.1               - 
sdp:32769:100*         Up   Up    Y    30.30.30.30            -      v11 11.11.11.2 11.11.11.1        2       -     1 
                                                                     v21 21.21.21.2 21.21.21.1               - 
Total Ports: 3 
 

<<<PAGE 70>>>
Architecture Guide 
EVPN 
70 
External Route Advertisement 
In this section, we will establish OSPF neighborship between border leaf LEAF-5 and the 
external CE switch, which will advertise the external prefixes. These external prefixes will 
be exported from the VRF routing table to the GRT and then imported into the Fabric-VPN 
EVI, which will be imported by the remaining Leaf switches. The import/export 
configuration has been done VRF/Fabric-VPN Configuration section. 
LEAF-5 
<vrf vrf1> ip interface "v50" address 192.168.50.2 mask 255.255.255.0 vlan 50 rtr-port port 1/1/3 tagged 
<vrf vrf1> ip load ospf 
<vrf vrf1> ip ospf area 0.0.0.0 
<vrf vrf1> ip ospf interface "v50" 
<vrf vrf1> ip ospf interface "v50" area 0.0.0.0 
<vrf vrf1> ip ospf interface "v50" type point-to-point 
<vrf vrf1> ip ospf interface "v50" admin-state enable 
<vrf vrf1> ip ospf admin-state enable 
 
Verification Commands 
You can verify the DAG configuration using the commands below: 
LEAF-5 
vrf1::LEAF-5> show ip ospf neighbor 
                                                    Domain   Domain 
  IP Address        Area Id          Router Id       Name     ID      State  Type 
----------------+----------------+----------------+--------+--------+-------+-------- 
192.168.50.1     0.0.0.0          192.168.50.1     Vlan     50         Full  Dynamic 
 
 
LEAF-1/2/3/4/6 
vrf1::LEAF-1> show ip routes 
 + = Equal cost multipath routes 
 Total 12 routes 
  Dest Address       Gateway Addr        Age        Protocol 
------------------+-------------------+----------+----------- 
  10.10.94.0/24        10.10.94.1        02:13:15   LOCAL 
  10.10.95.0/24        10.10.95.1        02:13:15   LOCAL 
  10.10.96.0/24        10.10.96.1        02:13:15   LOCAL 
  10.10.97.0/24        50.50.50.4        02:12:35   IMPORT 
  10.10.97.4/32        50.50.50.4        02:12:35   IMPORT 
  10.10.98.0/24        50.50.50.4        02:12:35   IMPORT 
  10.10.98.4/32        50.50.50.4        02:12:35   IMPORT 
  10.10.99.0/24        50.50.50.6        02:12:28   IMPORT 
  10.10.99.6/32        50.50.50.6        02:12:28   IMPORT 
  50.50.50.0/24        50.50.50.1        03:02:03   LOCAL 
  127.0.0.1/32         127.0.0.1         03:02:38   LOCAL 

<<<PAGE 71>>>
Architecture Guide 
EVPN 
71 
  192.168.50.0/24      50.50.50.5        00:03:51   IMPORT 
 
 
Proxy ARP Configuration 
Enabling the proxy ARP will check for the local proxy-ARP cache and generates an ARP 
reply if target IP is found, otherwise those ARP requests will be flooded in the targeted 
EVPN service. By default, Proxy ARP is enabled for an EVPN enabled service.  
 
Verification Commands 
You can verify the proxy ARP configuration using the command below: 
LEAF-1 
vrf1::LEAF-1> show service 100 proxy-arp config 
  arp-suppression    : complete, 
  arp-unknown-options: discard, 
  unicast-forward    : disable, 
  arp-probe          : enable, 
To view the proxy ARP table, you can use the command below: 
 
LEAF-1 
vrf1::LEAF-1> show ip evpn proxy-arp evi 1000 
*= Local Saps 
#= Static Arps 
@= Inactive Arps 
!= Peer Arps 
(M) Monitored Arps 
(F) Filtered Arps 
EVI        IP Address           Mac-Address        ESI                            ETAG             Adv-PE          Service Id   Interface            SeqNum 
----------+--------------------+------------------+------------------------------+----------------+---------------+------------+--------------------+-------- 
1000       10.10.94.50!         00:50:56:9f:eb:46  03:2c:fa:a2:c0:d4:d3:00:0a:00  940              20.20.20.20     100          10:940               0 
 
Total count: 1 
You can verify the proxy ARP statistics with the command below: 
LEAF-1 
vrf1::LEAF-1> show ip evpn proxy-arp summary 
Type         Count 
-----------+----------- 
Total        3 
Static       0 
Local        1 
Remote       0 
Communication between clients and the external prefix should be working  

<<<PAGE 72>>>
Architecture Guide 
EVPN 
72 
Peer         2 
 
 
Conclusion 
The acceleration of digitalization combined with the increase demand for data has driven 
innovation for virtualization technologies such as VXLAN in the data center. It also allowed 
for multi-tenancy and its scalability features have also driven its use in the enterprise. 
However, VXLAN required complex configuration utilizing underlay multicast technologies 
with proactive flood-and-learn learning model. This has driven an intelligent control plane 
protocol to allow for reactive learning of connected hosts that simplified configuration 
and maintenance. This control plane protocol is EVPN.  
EVPN is a next-generation technology based on MP-BGP, which a proven and stable 
protocol, to provide a single and unified control plane protocol that supports Layer 2 and 
Layer 3 services.  
It has gained popularity as the de facto protocol for the DC but has many other use cases 
in the Enterprise Campus and the DCI. 
It's flexibility in running over multiple data-plane encapsulation such as VXLAN, MPLS, 
PBB, and more along with its advanced features provides an efficient and optimized 
network fabric that can easily scale. 
Some of its advanced features include: 
• 
All-Active Multi-homing at the edge which provides effective utilization of 
resources. 
• 
DAG functionality which allows for host mobility and optimal traffic forwarding. 
• 
ARP suppression which brings optimization to the EVPN fabric 
• 
Mass withdrawal features that provide fast convergence 
• 
MAC mobility feature which allows for seamless host migrations activities 
• 
Native multicast routing support with OISM without additional protocols such as 
PIM 
Add to that the AOS EVPN model which increases the network scalability, simplicity, and 
stability.  
Alcatel-Lucent Enterprise service-defined networking features such as Virtual Chassis (VC) 
technology, Dynamic services, Zero Trust Architecture, and Universal Network Profile 
(UNP) allows for achieving an autonomous multi-technology fabric network from the edge 
to the core that helps simplify operations, thereby improving business agility. 
 
In case Proxy ARP Table is empty, it has probably timed out. Please try to send 
communication between the hosts and this should generate entries in the table. 

<<<PAGE 73>>>
Architecture Guide 
EVPN 
73 
Related Documents 
 
[1] RFC 7432, BGP MPLS-Based Ethernet VPN - 
https://datatracker.ietf.org/doc/html/rfc7432  
[2] RFC 7348, Virtual eXtensible local Area Network (VXLAN): A Framework for 
Overlaying Virtualized Layer 2 Networks over Layer 3 Networks - https://www.rfc-
editor.org/rfc/rfc7348  
[3] RFC 8365, A Network Virtualization Overlay Solution Using Ethernet VPN (EVPN) - 
https://www.rfc-editor.org/rfc/rfc8365  
[4] RFC 9135, Integrated Routing and Bridging in Ethernet VPN (EVPN) - 
https://datatracker.ietf.org/doc/rfc9135/  
[5] RFC 9136, IP Prefix Advertisement in Ethernet VPN (EVPN) - 
https://datatracker.ietf.org/doc/rfc9136/  
[6] RFC 9251, Internet Group Management Protocol (IGMP) and Multicast Listener 
Discovery (MLD) Proxies for Ethernet VPN (EVPN) - 
https://datatracker.ietf.org/doc/html/rfc9251  
[7] RFC 4364, BGP/MPLS IP Virtual Private Networks (VPNs) - https://www.rfc-
editor.org/rfc/rfc4364  
[8] RFC 9625, EVPN Optimized Inter-Subnet Multicast (OISM) Forwarding - 
https://datatracker.ietf.org/doc/rfc9625/  
[9] RFC 4360, BGP Extended Communities Attribute - 
https://datatracker.ietf.org/doc/html/rfc4360  
[10] 
RFC 8584, Framework for Ethernet VPN Designated Forwarder Election 
Extensibility - https://datatracker.ietf.org/doc/html/rfc8584  
[11] 
Data Center Reference Design Solution Guide - https://www.al-
enterprise.com/-/media/assets/internet/documents/a-to-g/data-centre-reference-
design-solution-guide-en.pdf  
 
 
