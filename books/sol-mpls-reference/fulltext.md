# sol-mpls-reference — 解决方案文档合并（页码全册连续）


<<<DOC 1: mpls-reference-design-guide-en.pdf | 起始页 1 | 45p>>>

<<<PAGE 1>>>
 
 
Design Guide 
MPLS Reference 
 
 
 
 
 
 
 
 
MPLS Reference  
Design Guide  

<<<PAGE 2>>>
 
2 
 
Design Guide 
MPLS Reference 
About This Document ...................................................... 4 
Purpose .......................................................................................................... 4 
Audience ........................................................................................................ 4 
Scope ............................................................................................................. 4 
Introduction ..................................................................... 5 
Benefits of MPLS ........................................................................................... 5 
MPLS Fundamentals ........................................................ 7 
MPLS Terminology ......................................................................................... 7 
MPLS Label Structure .................................................................................... 9 
Control Plane ................................................................. 10 
Label Distribution Protocol ........................................................................ 11 
Targeted-LDP .............................................................................................. 15 
T-LDP, as can be observed from the name “targeted”, uses unicast 
UDP communication for discovery and unicast TCP to establish the 
session. ....................................................................................................... 15 
MP-BGP ........................................................................................................ 15 
Data Plane ...................................................................... 16 
MPLS Operations ......................................................................................... 16 
MPLS QoS ..................................................................................................... 18 
MPLS TTL ..................................................................................................... 19 
LDP Graceful Restart .................................................................................. 19 
MPLS Service Framework/Model .................................. 20 
MPLS VPN Services ........................................................ 21 

<<<PAGE 3>>>
 
3 
 
Design Guide 
MPLS Reference 
VPLS ............................................................................................................. 21 
MPLS OAM ...................................................................... 23 
LSP Ping ....................................................................................................... 23 
LSP Traceroute ............................................................................................ 23 
MPLS Design and Positioning ........................................ 24 
Enterprise Campus Networks ..................................................................... 24 
Metro Ethernet Networks (Smart City) ...................................................... 24 
Implementation Licensing ............................................ 26 
VPLS Configuration Example ........................................ 26 
Best Practices ............................................................................................. 28 
MPLS Backbone Configuration with LDP Signaling .................................... 29 
MPLS VPLS Service with LDP Backbone Signaling ..................................... 33 
MPLS VPLS Service with BGP Signaling ...................................................... 34 
Verification Commands .............................................................................. 35 
VPWS Configuration Example ..................................................................... 40 
MPLS OAM Verification Commands ............................................................ 44 
Conclusion ..................................................................... 44 
Related Documents ....................................................... 45 
 
 

<<<PAGE 4>>>
 
4 
 
Design Guide 
MPLS Reference 
About This Document 
Purpose 
The purpose of this design guide is to present general IP/MPLS fundamentals, 
reference design concepts, positioning, and deployment guidelines for the 
Alcatel-Lucent Operating Software (AOS) implementation of MPLS. 
 
Audience 
The intended audience for this document includes customer and business 
partner networking professionals involved in the design and deployment of 
enterprise networks. 
 
Scope 
This document does not attempt to cover every aspect, nor every possible 
architecture option; but only the most common, validated and recommended 
architectures.  
This document will provide an overview of the technology and some features 
which will be presented but might not be supported in the first release of 
IP/MPLS in AOS. An updated version of this document may be published once 
such features are available.  
IP/MPLS first supported release is 8.9R3 and supported on the OmniSwitch 
6860N platform. Starting 8.10R2, it is also supported on OmniSwitch 6900 
platforms.  
AOS supports installation or removal of AOS MPLS package. MPLS is packaged 
into a Debian package which can be installed on the switch. To configure MPLS 
in AOS, it is required to install the MPLS package using Package Manager 
commands, which are further detailed in the Licensing section.  
You are encouraged to refer to the AOS documentation for additional details, 
supported features, and guidelines which are referenced in the Related 
Documents section. 
 
 
 

<<<PAGE 5>>>
 
 
5 
 
Design Guide 
MPLS Reference 
Introduction 
Multiprotocol Label Switching (MPLS) has been and still is the de-facto 
technology used by Service Providers and enterprises to provide VPN services. 
MPLS is a label-switching technology where forwarding of traffic is based on 
pre-determined labels which are advertised between routers to build a label-to-
label mapping. The MPLS router forwards traffic based on a label value that is 
attached to IP packet headers without looking at the inner IP packet 
destination details.  
AOS implementation of MPLS provides the network architecture that is needed 
to set up a Layer 2 Virtual Private Network (L2 VPN) that uses MPLS labels to 
transport data. L2 VPNs provide multiple types of Layer 2 services to the user 
like Virtual Private LAN Service (VPLS) that allows E-LAN connectivity services 
over the MPLS network, and VPWS (Virtual Private Wire Service) that provides E-
LINE (point-to-point) connectivity. 
Benefits of MPLS 
MPLS introduces many benefits to the network, including: 
BGP-Free Core 
Since MPLS uses labelling as a tunnel mechanism, this allows for a BGP-free 
core network. This saves cost to the service provider since the core routers do 
not need to support a large number of routes. 
Simplicity 
MPLS allows routers to perform a label lookup without examining the IP packet 
details. This results in a simpler lookup process based on exact match rather 
than longest match lookup as in the case of routing. 
Resiliency 
MPLS offers a highly-available, self-healing network and supports fast 
convergence times. This makes it well-suited for mission-critical networks 
where resiliency is a key factor.  
Traffic Engineering 
MPLS technology provides traffic engineering capabilities to distribute traffic 
load more efficiently and optimize resource usage.  

<<<PAGE 6>>>
 
 
6 
 
Design Guide 
MPLS Reference 
Multiple Services Across a Unified Infrastructure 
MPLS can run over many transport technologies. It allows service providers to 
provide Layer 2 or Layer 3 services across a common infrastructure.  
 
 
 

<<<PAGE 7>>>
 
 
7 
 
Design Guide 
MPLS Reference 
MPLS Fundamentals 
We will cover an introduction into MPLS technology and a few fundamental 
concepts.  
 
MPLS Terminology 
 
LER 
The Label Edge Router (LER) is a router that operates at the edge of the MPLS 
network connecting to the Customer Edge (CE) router. It is also called Provider 
Edge (PE) router in Service Provider networking terminology. It is the router 
responsible to “push” or insert an MPLS label into an incoming packet to the 
MPLS network and “pop” or remove an MPLS label from an incoming packet 
exiting the MPLS network. There are two types of LER routers, the ingress LER 
(iLER), and the egress LER (eLER). 
LSR 
The Label Switch Router (LSR) is a router that operates within the MPLS 
network and is connecting to other LSR Routers. An LER is also considered an 
LSR, but usually performs the “push” and “pop” operations. An intermediate LSR 
is responsible to “swap” MPLS label from incoming packets as they transit 
through the MPLS network based on the LSP.  

<<<PAGE 8>>>
 
 
8 
 
Design Guide 
MPLS Reference 
LSP 
The Label Switched Path (LSP) is the transport tunnel or the pre-determined 
path which is defined to switch packets from the iLER to the eLER. LSPs are 
unidirectional as shown in the figure below. This means that two LSPs are 
required for bidirectional traffic flow. 
FEC 
Forward Equivalence Class (FEC) in MPLS terminology, which tends to 
correspond to an LSP, is a set of packets with similar characteristics, such as 
destination IP or Quality of Service (QoS) markings, to be assigned to an MPLS 
label. It is mostly used for destination IP prefixes. 
LDP 
Label Distribution Protocol (LDP) is a signaling protocol used in MPLS for label 
exchange and signaling to create LSP paths using the pre-determined routing 
information provided by the underlying IGP. 
 

<<<PAGE 9>>>
 
 
9 
 
Design Guide 
MPLS Reference 
MPLS Label Structure 
 
MPLS label header is 32 bits (4 bytes) and includes the following fields: 
• 
Label: (20 bits) This is the label value which are in a range of 0-1048575 
with the first 16 values reserved for special use. 
• 
EXP: (3 bits) These are the experimental bits used for QoS applications. 
• 
S Bit or Bottom of Stack (BoS): (1 bit) This value usually refers to the 
bottom of the stack. If it is set to 1, then this is the bottom of the stack. 
Otherwise, it is set to 0. 
• 
Time To Live (TTL): (8 bits) This value is used for loop-prevention similar 
to IP TTL value. It is decremented by 1 at each hop and the packet is 
discarded if it reaches 0. 
The MPLS label sits between the IP Packet and the Ethernet header as a “shim” 
header. This is the reason why it is sometimes referred to as a Layer 2.5 
protocol. 
Reserved Labels 
Labels 0-15 are reserved labels. The currently defined label values are 
mentioned in below table: 
Label 
Purpose 
0 
IPv4 Explicit NULL 
Label 
1 
Router Alert Label 
2 
IPv6 Explicit NULL 
Label 

<<<PAGE 10>>>
 
 
10 
 
Design Guide 
MPLS Reference 
3 
Implicit NULL 
Label 
14 
OAM Alert Label 
Explicit NULL and Implicit NULL labels are used in Penultimate Hop Popping 
(PHP) operations which will be discussed in the Data Plane section. The 
Operation and Maintenance (OAM) Alert Label differentiates OAM packets from 
normal user data packets, but it is not widely implemented.  
MPLS Label Stacking 
Usually more than one label is required to forward packets through an MPLS 
domain to provide VPN services to customers in a Service Provider network. 
This is implemented through label stacking, which is sorted in a Last-In, First-
Out (LIFO) fashion. The first label which is “pushed” to the packet is called the 
top label, and the last label is called the bottom label. In a VPN implementation, 
the top label is the transport label and the bottom label is the service label.  
The number of labels which can be stacked is unlimited, it depends however on 
the hardware support and the packet size. Most vendors support between 4 
and 6 labels. 
 
Control Plane 
MPLS is tunneling protocol which relies on the underlay network to be pre-
configured with an IGP routing protocol to allow full reachability between LERs 
(PE routers). Open Shortest Path First (OSPF) and Intermediate System to 
Intermediate System (IS-IS) are usually configured in the MPLS backbone 
network.  
Transport label allocation can be done statically or dynamically. The labels can 
be dynamic allocated using a label signaling protocol such as LDP, Resource 
Reservation Protocol (RSVP), or by using an existing protocol for label 
distribution such as Border Gateway Protocol (BGP) or Segment Routing (SR).  
Loopback interfaces are created at each LSR which are used for reachability 
between them. Routers establish peering sessions and after which they start 
exchanging label bindings for FECs. MPLS Forwarding Information Base (FIB) 
comprises of FTN [FEC To Next Hop Label Forwarding Entry (NHLFE)] and tunnel 
entries for requests for a Push operation and Ingress Label Mapping (ILM) 
entries for requests for a Swap/Pop operation. The FIB entries are replicated to 
the Network Interfaces (NIs) in order for the hardware table to be setup with 
the label entries. LSPs will then be established between LERs to allow for full 
reachability. LSPs are established upstream from downstream LERs. 

<<<PAGE 11>>>
 
 
11 
 
Design Guide 
MPLS Reference 
Furthermore, another label signaling protocol is required to advertise the 
service labels between iLER and eLER. The are two main dynamic signaling 
protocols for the service labels are Targeted-LDP (T-LDP), and Multi-Protocol 
BGP (MP-BGP). This can also be done statically through static label 
configuration. Let’s discuss each of these protocols further. 
Label Distribution Protocol 
LDP, which is defined in RFC 5036, is configured on all LSRs and LERs in the 
MPLS domain. Routers establish a peering session between them and a series 
of messages are exchanged. The main categories of messages include: 
• 
Discovery Message: To announce and maintain the presence of an LSR 
in a network 
• 
Session Message: To establish, maintain, and terminate sessions 
between LDP peers 
• 
Advertisement Messages: To create, change, and delete label mappings 
for FECs 
• 
Notification Messages: To provide advisory information and to signal 
error information 
 
The following table lists the message types used by LDP: 
Message 
Name 
Purpose 
Notification        
"Notification Message" 
Hello               
"Hello Message" 
Initialization      
"Initialization Message" 
KeepAlive           
"KeepAlive Message" 
Address             
"Address Message" 
Address 
Withdraw    
"Address Withdraw Message" 
Label Mapping       
"Label Mapping Message" 
Label Request       
"Label Request Message" 
Label Abort 
Request 
"Label Abort Request Message" 
Label 
Withdraw      
"Label Withdraw Message" 

<<<PAGE 12>>>
 
 
12 
 
Design Guide 
MPLS Reference 
Label Release       
"Label Release Message" 
LDP uses the reserved multicast address for “all-routers” 224.0.0.2 and uses 
UDP port 646 for discovery messages to establish sessions between LDP 
neighbors and TCP 646 for the remaining messages. LDP is automated and is 
used to establish both transport tunnel LSPs and T-LDP is used to establish 
service tunnel LSPs. T-LDP is covered in the next section. Each router creates a 
local binding of a label to each IP prefix in its Route Table including the 
loopback interface. It then distributes this binding information to all of its LDP 
peers. Both remote and local bindings are stored in the ILM. A full mesh of 
transport tunnels is created and LSPs based on IGP best paths. LDP associates 
a FEC with each LSP it creates. The FEC associated with an LSP specifies which 
packets are "mapped" to that LSP. 
LDP Operations 
LDP should be enabled on all interfaces in the MPLS domain except towards the 
CE router (in the LER router). When LDP is enabled, LSRs start sending UDP-
based LDP Hello messages on all links where it is enabled to discover any 
directly connected peers. After Hello messages are exchanged and neighbors 
have discovered each other, they attempt to establish an LDP session between 
them using TCP-based messages. LDP message exchanges are accomplished by 
sending LDP protocol data units (PDUs) over LDP session TCP connections. They 
negotiate LDP session parameters by exchanging LDP Initialization messages, 
which contain session parameters such as timer values, the label distribution 
method, and others. If they agree, they maintain the LDP session, otherwise 
they will try to re-negotiate. After the peer relationship is established, Hello 
messages and Keepalive messages are periodically sent.  
Two kinds of notification messages are used in LDP to provide advisory 
information and to inform error information. An LSR maintains a hold-timer 
with each Hello adjacency and if the timer expires without receiving a matching 
hello packet from the peer, LSR concludes that the peer is no longer alive and 
then deletes the Hello adjacency with that peer by sending a Notification 
message and closing the transport connection. Similarly, a keepalive timer is 
used to monitor the integrity of the established session. If this timer expires, 
the LSR concludes that the transport connection is bad or that the peer has 
failed, and it terminates the LDP session by closing the transport connection. 
A pair of LSRs negotiates the hold-timer they use for hellos from each other. 
Each proposes a hold time value, and the LSR uses the lower of the two hold-
time values. The hold-time value set on the interface overrides the hold-time 
value set globally. The same also applies to Keepalive timer and Keepalive 
timeout. 

<<<PAGE 13>>>
 
 
13 
 
Design Guide 
MPLS Reference 
In most cases, one LDP session is established even if multiple links exist 
between the LSRs. LSRs that are running LDP have an LDP Identifier, or LDP ID. 
This LDP ID is a 6-byte field that consists of 4 bytes identifying the LSR uniquely 
(the loopback address) and 2 bytes identifying the label space that the LSR is 
using. If the last two bytes are 0, the label space is the platform-wide or per-
platform label space, which is usually what is implemented. If they are non-
zero, a per-interface label space is used.  
The Label Mapping message is used by an LSR to distribute a label mapping for 
a FEC to an LDP peer. An LSR is responsible for the consistency of the label 
mappings it has distributed and that its peers have these mappings. 
Label Withdraw message is used to signal to an LDP peer to withdraw a FEC-
label mapping that was previously advertised. This could be because the FEC is 
no longer available or was manually configured to be removed. The Label 
Release message is used to respond to a Label Withdraw message or to signal 
to an LDP peer that it does not need a specific FEC-label mapping that was 
previously requested and/or advertised by the peer. 
 
Label Distribution and Management 
An LSR can use different modes to distribute label bindings to LDP neighbors: 
• 
Downstream-on-Demand (DoD) Mode: Router distributes a label to a 
peer only if there is a pending label request from a peer.  
• 
Downstream Unsolicited (DU) Mode: This parameter distributes labels to 
peers without waiting for a label request. This mode is typically used 
with the liberal label retention mode (LLR).  
 
There are also two modes of control for label creation: 
• 
Independent Label Distribution (ILD) Control: Each LSR might advertise 
label mappings to its neighbors at any time. In independent 
downstream-on-demand mode, an LSR might answer requests for label 
mappings immediately, without waiting for a label mapping from the 
next hop. In independent downstream unsolicited mode, an LSR might 
advertise a label mapping for a FEC to its neighbors whenever it is 
prepared to label-switch that FEC.  
It is important that the LSR ID, or the loopback address is unique in the MPLS 
domain to avoid any unpredictable behavior.  
Only Downstream Unsolicited Mode is supported in the current release. 

<<<PAGE 14>>>
 
 
14 
 
Design Guide 
MPLS Reference 
• 
Ordered Label Distribution (OLD) Control: in this mode, an LSR may 
initiate the transmission of label mapping only for an FEC for which it 
has a label mapping for the FEC next hop, or for which the LSR is the 
egress. For each FEC for which the LSR is not the egress, and no 
mapping exists, the LSR must wait until a label from a downstream LSR is 
received. An LSR may be an egress for some FECs and a non-egress for 
others. 
 
There is also retention modes which specifies whether a FEC is maintained or 
not if it is learned from an LSR which is not the next-hop for that FEC. These 
retention modes are: 
• 
Conservative Label Retention (CLR) Mode: Maintains only the label 
bindings for valid next hops in an LSP. i.e. delete all unused labels and 
FECs. 
• 
Liberal Label Retention (LLR) Mode: Retain all labels binding to FEC 
received from label distribution peers, even if the LSR is not the current 
next-hop. i.e. retain all labels, regardless of use.  
 
LDP label distribution is propagated and flooded from the eLER upstream 
towards the iLER. After LDP sessions are established and labels are distributed 
between LDP peers, a full-mesh of LSPs (transport tunnels) will be created in 
the MPLS domain. 
LDP Session Authentication 
To maintain integrity of LDP session messages and to prevent introduction of 
spoofed TCP segments in the LDP session connection stream, RFC 5036 
proposes session authentication to be configured. Currently MD5 key based 
authentication is proposed in the RFC but it also mentions that keychains with a 
stronger encryption algorithm like SHA can be implemented. 
 
This key is used to compute and append a MD5 signature for each TCP segment 
carried by the corresponding LDP session to that peer. The peer computes the 
Only Independent Label Distribution control is supported in the current release. 
Only Liberal Label Retention Mode is supported in the current release. 
Only MD5 key-based authentication is supported in the current release. 

<<<PAGE 15>>>
 
 
15 
 
Design Guide 
MPLS Reference 
MD5 digest on the received TCP segment using locally configured shared key 
(password) and silently rejects the TCP segment if the computed MD5 signature 
doesn’t match with received MD5 signature. 
Authentication must be configured on both LDP peers using the same MD5 key 
(password), otherwise the peer session will not be established. 
Targeted-LDP 
Targeted-LDP (T-LDP) is used when labels are required to be exchanged 
between remote LERs. In our case, it is used to establish the service labels and 
the service tunnel. T-LDP is also used to improve convergence time and for 
traffic engineering purposes. This is because when a link between two LSRs in 
an LSP fails without T-LDP, then the LDP session is lost. However, with T-LDP, 
the LDP session stays up since an alternative path may exist and negotiated 
labels are preserved. 
T-LDP is configured between LERs to establish service tunnel LSPs and for 
service de-multiplexing. T-LDP still depends on transport tunnels to establish 
the service tunnels. Transport tunnels can be created using LDP, RSVP-TE, or 
through static configuration. 
T-LDP, as can be observed from the name “targeted”, uses unicast UDP 
communication for discovery and unicast TCP to establish the session. 
We will cover MPLS VPN services in a coming section. 
MP-BGP 
MP-BGP, which is defined in RFC 2283, may be used by the Service Provider to 
exchange routes of a particular service among the LERs that are attached to 
that service. Each route within a VPN is assigned an MPLS Service Label and 
BGP is used to distribute the route and the label.  
The multiprotocol capabilities of BGP mainly focuses on new Network Layer 
Reachability Information (NLRI) which includes the Address Family Identifier 
(AFI) that identifies the set of Network Layer protocols to which the address 
carried in the Next Hop field must belong to and next-hop address to reach the 
NLRI IP prefixes. The multiprotocol capabilities of BGP also enables the auto 
discovery of PE’s or tunnel end point in the same service instance.  
When customer traffic from a certain service instance reaches the iLER, it is 
encapsulated with the Service Label, and then it is further encapsulated with 
the transport label. 
 
 
 

<<<PAGE 16>>>
 
 
16 
 
Design Guide 
MPLS Reference 
Data Plane 
MPLS Operations 
 
As shown in above figure, there are three operations for an LSR to switch 
packets through a LSP: push, pop, and swap. The “push” operation is also 
sometimes referred to as “imposition” and the pop operation is referred to as 
“disposition”. After a FEC lookup is done, the iLER inserts or “push” a label on 
the received packet which is not yet labeled and sends the packet on the data 
link. When an intermediate LSR receives the labeled packet, it “swaps” or 
changes the top label of the stack and switches the packet through the LSP on 
the data link. After the packet reaches the edge of the network towards the 
eLER, all labels are “popped” or removed before the packet is switched out of 
the MPLS network domain. 
Penultimate Hop Popping (PHP) 
An efficiency mechanism called Penultimate Hop Popping (PHP) is performed 
when an eLER assigns the implicit NULL label (label value 3) to a FEC to request 
the upstream LSR to perform a pop operation and remove the transport label. 
This is to avoid performing two lookups in the MPLS FIB. This enhances the 
performance on the eLER. The use of implicit NULL does have some 
implications. When the last LSR removes the top label, the EXP bits are also 
removed, thus removing any QoS values in the header. The explicit NULL can 

<<<PAGE 17>>>
 
 
17 
 
Design Guide 
MPLS Reference 
be used in this case to solve this. The explicit NULL (label value 0 for IPv4, and 2 
for IPv6) is signaled by the eLER to the last LSR. This will cause the upstream 
LSR to swap the transport label to the explicit NULL label. The eLER will not 
perform a lookup on the explicit NULL label, thereby saving on performance, 
and at the same time will preserve the EXP bits in the explicit NULL label.  
 
 
 
Explicit NULL is currently not supported in AOS implementation. 

<<<PAGE 18>>>
 
 
18 
 
Design Guide 
MPLS Reference 
MPLS QoS 
 
Figure 1 - MPLS QoS Modes 
Using the experimental (EXP) bits in the MPLS header, preferential treatment 
can be provided to different packets. Only the EXP bits of the top label 
(transport label) is processed. There are two different modes for QoS: Uniform 
and Pipe Mode. 
In uniform mode, the IP precedence value (first 3 bits of DSCP) in the IP packet 
is copied to the EXP bits in the MPLS header as the packet enters the MPLS 
domain at the iLER and then copied back to the IP Precedence value at the eLER 
as the packet exists the domain. As the label is “swapped” in the MPLS domain, 
the new label EXP value is given the same EXP value as the top label. 
In pipe mode, the EXP value is set according to the Service Provider’s policy and 
is independent of the customer’s QoS markings and classifications. The existing 
DSCP values are unchanged. 

<<<PAGE 19>>>
 
 
19 
 
Design Guide 
MPLS Reference 
QOS over EXP bit is not supported in the current implementation of AOS. 
MPLS TTL 
MPLS TTL field in the MPLS header is used for loop-prevention similar to the IP 
packet TTL field. It is decremented by 1 in each hop and discarded once it 
reaches 0. It is however handled differently in MPLS networks. Similar to how 
only the Transport label EXP bit is processed, only the Transport label TTL is 
decremented as the packet traverses the MPLS network. There are also two 
different modes of processing TTL packets: Uniform and Pipe mode. 
In uniform mode, the IP header TTL field is copied to the MPLS header TTL field 
and is decremented normally as the packet traverses the MPLS domain.  
In pipe mode, the IP header TTL field remains unchanged and the MPLS header 
TTL field is handled independently. In case of a Layer 3 VPN, the TTL is 
decremented by 1 at the iLER and again at the eLER, while for Layer 2 VPN, the 
TTL is not changed since only the Ethernet header is processed and not the IP 
packet header. 
TTL manipulation is not supported for MPLS tag in the current implementation 
of AOS. 
LDP Graceful Restart  
MPLS provides a graceful restart mechanism with non-stop forwarding (NSF) 
for the LDP component of MPLS. This mechanism, as described in RFC 3478, 
helps to minimize disruption on MPLS traffic caused by a control plane restart 
by preserving the forwarding state information. This mechanism is supported 
only for planned takeovers (for example, the users performs the takeover), not 
unplanned takeovers (for example, the primary Chassis Management Modules 
(CMMs) unexpectedly fails) or when a link goes down between the two routers. 
 
 

<<<PAGE 20>>>
 
 
20 
 
Design Guide 
MPLS Reference 
MPLS Service Framework/Model 
 
Figure 2 - MPLS Service Framework 
An MPLS service represents a VPN, or tenant and is uniquely identified by it’s 
service identifier. The service needs to be only created on LER nodes which are 
servicing the locations associated to the service. There are also the following 
components which exist in the LER: 
• 
Attachment Circuit (AC) or Service Access Point (SAP): A UNI-side (PE to 
CE link) logical port which binds a physical port and specific customer 
traffic types to a service. It is the point where the customer traffic 
ingress/egress the MPLS network. Multiple SAPs can be associated to the 
same physical port thus multiplexing and mapping different customer 
traffic encapsulations to different services. 
• 
Virtual Circuit (VC) or Service Distribution Point (SDP): An NNI-side 
unidirectional logical connection which binds a service to a far-end 
router over which MPLS encapsulated packets are distributed. It is 
identified by a unique locally-significant SDP/VC ID.  
• 
Service Tunnel: A virtual link that transparently carries traffic of a 
service. Each service or customer sends traffic through a service tunnel 
within the transport LSP tunnel. 
• 
Transport Tunnel (LSPs): A unidirectional path through an MPLS network 
based on criteria in a FEC.  
There are two FECs associated with providing VPN services. One FEC for the 
service tunnel, which is the service identifier, and another is or the transport 
tunnel, which is the loopback interface for each LSR. Labels are stacked to 
provide VPN services. The iLER binds the customer’s traffic from the SAP to the 
dedicated service and then to the mapped service tunnel. This is done by 

<<<PAGE 21>>>
 
 
21 
 
Design Guide 
MPLS Reference 
“pushing” the Service Label to the packet. Then another Transport label 
(Loopback interface) is added to the stack corresponding to the LSP and the 
packet is forwarded to the next LSR. Once the packet reaches the eLER, the top 
label (transport label) is “popped” and the Service Label is processed and also 
“popped” and the packet is associated to the corresponding Service and traffic 
is forwarded to the customer’s SAP. Intermediate LSR are unaware of the 
service tunnels and labels and only process the transport labels.  
 
MPLS VPN Services 
The two main L2VPN implementations for MPLS are Virtual Private Wire Service 
(VPWS) and Virtual Private LAN Service (VPLS).  
VPLS 
VPLS is an L2VPN service that allows any-to-any (multipoint) connectivity (E-
LAN). The provider network emulates a LAN by connecting all the customer’s 
remote sites at the edge of the provider network to a single bridged LAN. A full-
mesh of PWs needs to be established between LERs to form a VPLS.  
In the case of VPLS, it is assumed that Ethernet is the layer 2 protocol used 
between the CE and the PE. As VPLS is an Ethernet layer 2 service, the PE must 
be capable of MAC learning, bridging and replication on a per-VPLS basis. 
The MPLS core network interconnects the PEs (LERs) and does not really 
participate in the VPN functionality. Traffic is simple switches based on the 
MPLS labels. 
To prevent forwarding loops, the so-called “Split Horizon” rule is used. In the 
VPLS context, this rule basically implies that a PE must never send a packet on a 
PW if that packet has been received from a PW. This ensures that traffic cannot 
form a loop over the backbone network using PWs. The fact that there is always 
a full mesh of PWs between the PE devices ensures that every destination 
within the VPLS will be reached by a broadcast packet. 
 
AOS implementation of MPLS L2VPN including: 
• 
LDP-based VPLS 
• 
BGP-based VPLS 
VPLS is a superset of VPWS. VPWS only provides point-to-point customer 
connectivity without providing any L2/L3 functionality. 

<<<PAGE 22>>>
 
 
22 
 
Design Guide 
MPLS Reference 
The multiprotocol capabilities of BGP enables the auto discovery of PE’s or 
tunnel end-point in the same VPLS instance. The method of establishing VPLS 
with BGP accomplishes both auto-discovery and signaling. 
Since these services are usually configured for a single AS, using MP-BGP will 
require either a full-mesh of peerings between LERs, or using Route Reflectors 
(RR).  
VPWS 
VPWS provides point-to-point VPN connectivity service for customers connected 
to an MPLS network. It allows multiple customers to share one transport leased 
line (LSP) and creates an exclusive virtual channel for each customer on the 
shared LSP. On an Ethernet network, sites in different cities can communicate 
over a P2P VPWS connection on an MPLS network, just like communicating 
within a virtual local area network (VLAN). 
L2VPN services can be emulated over an MPLS backbone by encapsulating 
Layer 2 ethernet frames and transmitting them over a PW service. Defined in 
RFC 8077, a PW service, also called E-pipe, is used to define a virtual wire (E-
LINE) connection between two local SAPs or between two SAPs across the SPB 
network. The SAP that the PW service is associated with serves as an 
attachment point for one end of the point-to-point connection. With a PW 
point-to-point connection, there is no forwarding decision to be made; packets 
simply enter one end of the connection and leave the other end of the 
connection unchanged. As a result, customer MAC addresses are not learned 
on the SAP attachment points. Packets are transparently forwarded, which 
simplifies traffic flow and reduces hardware usage.  
MEF 6.3 defines two types of P2P Ethernet VPWS services - EPL (Ethernet Private 
Line) and EVPL (Ethernet Virtual Private Line). EPL is a per-port service whereas 
EVPL is a VLAN-based multiplexed service. For more details, please refer to the 
MEF 6.3 standard document referenced in the Related Documents section. 
In a EPL Service, all packets (tagged and untagged) ingressing from CE1 on the 
access port of PE1 are transparently sent out on the PW (MPLS encapsulated) 
towards PE2 and vice versa.  
In EVPL services:  
• 
Multiple PWs can be associated with a single Access Port to allow service 
multiplexing. 
• 
Multiplexing is based on the outer VLAN (C-VLAN) tag value in the customer 
packets.  
• 
The service is still point-to-point in nature for a given C-VLAN. 

<<<PAGE 23>>>
 
 
23 
 
Design Guide 
MPLS Reference 
 
 
MPLS OAM 
MPLS OAM helps service providers monitor LSPs and quickly isolate MPLS 
forwarding problems to assist with fault detection and troubleshooting in an 
MPLS network. One of the important MPLS OAM features is LSP ping and 
traceroute, which is used to detect and isolate data plane failures in MPLS LSPs 
when IP reachability and MPLS control plane seem to be working fine. 
AOS implementation supports LSP ping and traceroute in accordance with RFC 
4379 - Detecting MPLS Data Plane Failures. 
LSP Ping 
MPLS LSP ping uses MPLS echo request and reply packets to validate an LSP. 
These are analogous to ICMP echo request and reply messages used to validate 
reachability in IP networks. MPLS OAM echo and reply messages validate data 
plane reachability in MPLS LDP networks. 
MPLS LSP ping function can be used to validate data plane forwarding for IPv4 
LDP FECs. The MPLS echo request packet will be sent to a target router by 
using the label associated with the FEC to be validated. The source address of 
the LSP echo request is the IP address of the LDP router generating the LSP 
request. The destination IP address will be an address from 127.x.x.x/8 subnet, 
which prevents the MPLS echo packets from being IP forwarded and exiting the 
egress provider edge router as an IP packet. 
In response to an MPLS echo request, an MPLS echo reply is sent and 
forwarded as a non-labeled IP packet. The source address of the MPLS echo-
reply packet is an address obtained from the router generating the echo reply. 
The destination address is the source address of the router that originated the 
MPLS echo-request packet. The source and destination UDP ports for MPLS 
echo request and reply packets will be 3503. 
LSP Traceroute 
MPLS LSP traceroute also uses MPLS echo request and reply packets to validate 
forwarding in a LSP hop-by-hop and isolate faults. MPLS LSP traceroute can be 
used to trace the labeled switched path for a LDP IPv4 FEC. 
LSP traceroute uses time-to-live (TTL) field in MPLS to validate the LSP hop-by-
hop. When LSP traceroute is initiated, it incrementally increases the TTL value 
AOS implementation supports both EPL (port-based) and EVPL (VLAN based) VPWS 
services. 

<<<PAGE 24>>>
 
 
24 
 
Design Guide 
MPLS Reference 
in its MPLS echo requests (TTL = 1, 2, 3, 4) to discover the downstream mapping 
of each successive hop. The transit router processing the MPLS echo request 
returns an MPLS echo reply containing information about the transit hop in 
response to the TTL-expired MPLS packet. 
 
MPLS Design and Positioning 
AOS implmentation of IP/MPLS is best suited for enterprise and metro ethernet 
customers such as smart city networks. It provides a very cost-effective 
solution. 
Enterprise Campus Networks 
A two or three-tier architecture for a small and medium campus networks is 
best suited. It will provide VPN services end-to-end and IP/MPLS will be 
implemented from the access to the core layer. 
 
Figure 3 - Enterprise Campus MPLS Design 
Metro Ethernet Networks (Smart City) 
For metro ethernet networks such as smart city networks, IP/MPLS network can 
be configured at the core and distribution layers of a three-tier network 
architecture. At the access layer, ethernet standard switching will be 
configured. 

<<<PAGE 25>>>
 
 
25 
 
Design Guide 
MPLS Reference 
 
Figure 4 - Smart City MPLS Design 
 
 

<<<PAGE 26>>>
 
 
26 
 
Design Guide 
MPLS Reference 
Implementation Licensing 
MPLS is a licensed feature in AOS. MPLS is packaged into a Debian package, 
which can be installed or removed independently on the switch. To configure 
MPLS in AOS, it is required to install the MPLS package using Package Manager 
commands. Upon installing the MPLS package, MPLS process is loaded. The 
LDP and BGP modules will be loaded only after the load commands - mpls load 
ldp, and ip load bgp. 
Also, it is required to install Site-based or Node-based license for MPLS 
interface to be up and running. Two types of licenses are supported: 
• 
Site-based license - The Site-based licenses can be used as a floating or a 
shared license up to a maximum of four network nodes, without being 
bound to the hardware. For licensing, a network node can be a 
standalone switch or a virtual chassis of up to eight units. Site license 
eliminates the need to support expiry, revocation, or transfer attributes 
on the switch client. All these are handled by the site license server. 
Switch identification can be done using serial numbers and system MAC 
addresses, and so on. 
• 
Node-based license – The Node-based licenses are specific to any MPLS 
node, not bound to the hardware, and are not tied to the Node's Serial 
Number, MAC addresses, and so on. For licensing, an MPLS node can be 
a standalone of a Virtual Chassis of up to eight units. 
The SILOS (Site Local Licensing Server) is available as a ALE Debian software 
package that runs on a switch or a virtual chassis acts as a server issuing the 
site or node licenses to the sites and nodes. SWLIC (Switch Local Licensing 
client) runs on every MPLS-enabled switch in the network and acts as a client 
getting the site or node licenses from the SILOS. 
To install the licenses, download the site or node licenses generated on the ALE 
portal to the SILOS switch. To enable the site or node license in the SILOS, the 
customer must use the current ALE license portal to generate the license and 
install it manually using the SILOS management configuration commands. A 
customer may purchase multiple site or node licenses to support more than 
four MPLS network switches. 
Please refer to the OmniSwitch AOS Switch Management Guide referenced in 
the Related Documents section for more details on how to install the license. 
VPLS Configuration Example 
In this document, we will provide the configuration steps of AOS 
implementation of MPLS L2VPN including: 
• 
LDP-based VPLS 

<<<PAGE 27>>>
 
 
27 
 
Design Guide 
MPLS Reference 
• 
BGP-based VPLS 
We will use the following topology to provide the configuration steps for MPLS 
VPN services. 
Physical Topology 
 
Figure 5 - Physical Topology 
 
 
 

<<<PAGE 28>>>
 
 
28 
 
Design Guide 
MPLS Reference 
Logical Topology 
 
 
Figure 6 - Logical Topology 
Best Practices 
Some best practices which you can consider for your MPLS implementation 
include: 
• 
Configure IGP (OSPF/IS-IS) as an underlay in your network 
• 
Configure a (/32) loopback interface on each switch to be used and 
advertise it into your IGP 
• 
Assign the loopback interface as the Router-ID (make sure it is unique 
for each switch) 
• 
Configure the OSPF/IS-IS network type as point-to-point between your 
switches 
• 
Use routed interfaces 
• 
Use Bidirectional Forwarding Detection (BFD) for fast detection and 
convergence 
• 
Consider using /31 contiguous (/31) addresses for point-to-point links 

<<<PAGE 29>>>
 
 
29 
 
Design Guide 
MPLS Reference 
 
MPLS Backbone Configuration with LDP Signaling 
Refering to the topology figure shown previously, we will detail the steps for 
configuring your MPLS backbone using LDP signaling. The interfaces in green 
are the loopback addresses and will be configured as (/32). These loopback 
interfaces have to be unique in MPLS domain. 
Before configuring the MPLS VPN services, we will configure the backbone 
network with an IGP. It is recommended to consider using (/31) contiguous 
addresses for point-to-point links, but we have used in this configuration (/24). 
To configure the backbone network for MPLS, the below steps need to be 
taken: 
Step 1 - Configure the interfaces as per the topology: 
Below configuration shown is for R1: 
 
Step 2 - Configure single-area OSPF or single-level IS-IS. In this example we 
will configure OSPF. Remember to advertise Loopback0 interface and 
configure the inter-switch links as point-to-point interfaces. Also configure 
BFD to allow for fast convergence of IGP: 
! IP: 
-> ip interface Loopback0 address 1.1.1.1/32 
-> ip interface IFtoR2 address 10.1.2.1/24 vlan 12 rtr-port port 1/1/1 tagged 
-> ip interface IFtoR3 address 10.1.3.1/24 vlan 13 rtr-port port 1/1/2 tagged 
-> ip interface IFtoR4 address 10.1.4.1/24 vlan 14 rtr-port port 1/1/3 tagged 

<<<PAGE 30>>>
 
 
30 
 
Design Guide 
MPLS Reference 
 
Step 3 – Installing MPLS Package 
 
 
 
Step 4 - Configure MPLS interfaces: 
 
Step 5 - Configure LDP interfaces: 
! BFD: 
-> ip bfd transmit 200 
-> ip bfd receive 200 
-> ip bfd echo-interval 200 
-> ip bfd interface IFtoR2 
-> ip bfd interface IFtoR2 admin-state enable 
-> ip bfd interface IFtoR3 
-> ip bfd interface IFtoR3 admin-state enable 
-> ip bfd interface IFtoR4 
-> ip bfd interface IFtoR4 admin-state enable 
-> ip bfd admin-state enable 
! IP Route Manager: 
-> ip router router-id 1.1.1.1 
! OSPF: 
-> ip load ospf 
-> debug ip ospf set subsecond 1 
-> debug ip ospf set bfdsubsecond 1 
-> ip ospf area 0.0.0.0 
-> ip ospf interface Loopback0 
-> ip ospf interface Loopback0 area 0.0.0.0 
-> ip ospf interface Loopback0 admin-state enable 
-> ip ospf interface IFtoR2 
-> ip ospf interface IFtoR2 area 0.0.0.0 
-> ip ospf interface IFtoR2 type point-to-point 
-> ip ospf interface IFtoR2 bfd-state enable 
-> ip ospf interface IFtoR2 admin-state enable  
-> ip ospf interface IFtoR3 
-> ip ospf interface IFtoR3 area 0.0.0.0 
-> ip ospf interface IFtoR3 type point-to-point 
-> ip ospf interface IFtoR3 bfd-state enable 
-> ip ospf interface IFtoR3 admin-state enable  
-> ip ospf interface IFtoR4 
-> ip ospf interface IFtoR4 area 0.0.0.0 
-> ip ospf interface IFtoR4 type point-to-point 
-> ip ospf interface IFtoR4 bfd-state enable 
-> ip ospf interface IFtoR4 admin-state enable  
-> ip ospf spf-timer delay 0 
-> ip ospf spf-timer hold 0 
-> ip ospf bfd-state enable 
-> ip ospf admin-state enable 
! PKGMGR: 
! The Debian package file must be copied to the pkg in the running directory. 
-> pkgmgr install uosn-mpls-v1.deb 
! MPLS: 
-> mpls interface IFtoR2 admin-state enable 
-> mpls interface IFtoR3 admin-state enable 
-> mpls interface IFtoR4 admin-state enable 
It is also required to install Site-based or Node-based license for 
MPLS interface to be up and running. Please refer to the Licensing 
section for more details. 

<<<PAGE 31>>>
 
 
31 
 
Design Guide 
MPLS Reference 
 
MPLS and LDP Verification Commands 
Below is a summary of commands that can be used for verifying the MPLS LDP 
configuration: 
Command 
Description 
show mpls 
Displays the MPLS global attributes of a 
local router. 
show mpls interface 
Displays the MPLS interface 
configuration for the local router. 
show mpls ftn-table  
Displays the FTN table information. 
show mpls ilm-table  
Displays the ILM table entries. 
show mpls forwarding-
table  
Displays the forwarding table entries. 
show mpls ldp  
Displays the basic LDP attributes defined 
for the current router. 
show mpls ldp interface  
Displays the LDP interface information 
for the local router. 
show mpls ldp neighbor  
Displays all the directly connected and 
targeted LDP peers. 
show mpls ldp session rx-
address  
Displays the LDP enabled interface 
address of the peer which connect the 
other LSRs. 
show mpls ldp session rx-
labels  
Displays the labels received from the 
directly connected LDP peer. 
show mpls ldp session tx-
labels  
Displays the labels transmitted to the 
neighbor session. 
 
Below is a sample configuration output to verify MPLS configuration: 
Display the MPLS global attributes of a local router: 
 
! LDP: 
-> mpls load ldp 
-> mpls ldp admin-state enable 
-> mpls ldp interface IFtoR2 admin-state enable 
-> mpls ldp interface IFtoR3 admin-state enable 
-> mpls ldp interface IFtoR4 admin-state enable 
-> show mpls 
MPLS Label-Space             : 0, 
Minimum label configured 
: 16, 
Maximum label configured 
: 1048575 

<<<PAGE 32>>>
 
 
32 
 
Design Guide 
MPLS Reference 
Displays the MPLS interface configuration for the local router: 
 
Display FTN table information: 
 
View ILM table entries: 
 
View forwarding table entries: 
 
 
Below is a sample configuration output to verify LDP configuration: 
Display basic LDP attributes defined for the current router: 
 
-> show mpls interface 
Interface        
Admin-Status Oper-Status 
---------------------+------------+------------ 
intf1                 Enabled      Up 
intf2                 Enabled      Down 
-> show mpls ftn-table 
Legends: 
FTN Code: B - BGP, L - LDP 
OpCode : 1 = PUSH, 2 = POP, 3 = SWAP 
FTN-ID    Code     FEC       Opcode  Tunnel-id  Out-Label  Out-Intf     Nexthop 
-------|------|----------|--------|----------|----------|-----------|---------- 
1 
   L  
 1.1.1.1  
1  
0  
 
3  
intf3     30.30.30.1 
2  
   L  
 20.20.20.0  
1  
0  
 
3  
intf3     30.30.30.1 
-> show mpls ilm-table 
Legends: 
ILM Code: B - BGP, L - LDP 
OpCode : 1 = PUSH, 2 = POP, 3 = SWAP 
ILM-ID  Code  
 
FEC  
 In-Label  
Out-Label  
Out-Intf  
Nexthop 
------|--------|-------------|-----------|-------------|---------------|------------- 
1  
  L  
   4.4.4.4      53125   
   3  
 
intf3   
30.30.30.2 
2  
  L        50.50.50.0   53122  
   3  
 
intf2   
20.20.20.2 
3  
  L        2.2.2.2      53121  
   3  
 
intf2   
20.20.20.2 
-> show mpls forwarding-table 
Legends: > - installed FTN, * - selected FTN, S - stale FTN, 
B - BGP FTN, L - LDP FTN, 
LSP-ID      Code  
FEC  
     Tunnel-id   Out-Label   Out-Intf     Nexthop 
---------+-------+---------------+-----------+-----------+-----------+------------ 
> 1  
     L   
7.7.7.7  
0  
 
3  
intf5      50.50.50.1 
> 2          L  
80.80.80.0  
0  
 
3  
intf5       50.50.50.1 
-> show mpls ldp 
Router ID = 4.4.4.4, 
LDP Version = 1, 
Admin Status = Enabled, 
Hello Interval = 5, 
Targeted Hello Interval = 15, 
Hold Time = 15, 
Targeted Hold Time = 45, 
Keepalive Interval = 10, 
Keepalive Timeout = 30, 
Graceful Restart = Enabled, 
Neighbor liveness Time = 120, 
Max recovery Time = 120 
Session-protection = Disabled 

<<<PAGE 33>>>
 
 
33 
 
Design Guide 
MPLS Reference 
Display the LDP interface information for the local router: 
 
Display all the neighbours/adjacencies for the current LSR: 
 
Display sessions established between this LSR and other LSRs: 
 
 
MPLS VPLS Service with LDP Backbone Signaling 
Refering to the logical topology figure show previously, we will detail the steps 
for configuring your MPLS VPLS services using T-LDP. After configuring your 
MPLS backbone detailed in the previous section, follow the steps below to 
configure VPLS service with T-LDP (shown configuration for R1): 
Step 1 - Configure access port: 
 
Step 2 - Configure SDP for VPLS: 
-> show mpls ldp interface 
Interface  
   Admin-Status  Hello-Interval      Hold-Time     Oper-Status 
-----------------+------------+----------------+----------------+------------ 
vl11  
 
    Enabled  
 
5  
 
15  
 
Up 
 
-> show mpls ldp interface intf1 
Admin Status = Enabled, 
Primary IP Address = 10.10.10.1, 
Operational Status = Down, 
Hello Interval = 5, 
Hold Time = 15, 
Keepalive Interval = 10, 
Keepalive Timeout = 30, 
-> show mpls ldp neighbor 
IP Address  
Negotiated Holdtime  
LDP ID       Interface Name    Mode 
-------------+---------------------+-----------+------------------+------------ 
10.10.10.1  
 
15  
 
5.5.5.5:0  
intf1   
Targeted 
-> show mpls ldp session 
Peer Address  Interface Name  
TCP State  
Session State       Keepalive 
------------+-------------------+-----------------+------------------+------------ 
5.5.5.5  
intf1   
 
Established  
OPERATIONAL  
 
30 
 
-> show mpls ldp session 5.5.5.5 
Session state = OPERATIONAL, 
Session role = Passive, 
TCP connection = Established, 
IP address for TCP = 5.5.5.5, 
Interface being used = intf1, 
Peer LDP ID = 5.5.5.5:0, 
Adjacencies = 10.10.10.1, 
Advertisement mode = Downstream Unsolicited, 
Label retention mode = Liberal, 
Keepalive timeout = 30, 
Reconnect interval = 15, 
Graceful restart = Enabled, 
Restarting mode = Helper, 
! SVCMGR: 
-> service access port 1/1/4  

<<<PAGE 34>>>
 
 
34 
 
Design Guide 
MPLS Reference 
 
Step 3 - Configure the VPLS service: 
 
Step 4 - Create a SAP on the access port for VPLS service: 
 
Step 5 - Bind SDP tunnels to the VPLS Service: 
 
This configuration is only required on the PE/LER nodes where the full-mesh 
pseudowire service tunnels will be established. In our example topology, this 
will be configured on R1, R6, and R7.  
MPLS VPLS Service with BGP Signaling 
Refering to the topology figure show previously, we will detail the steps for 
configuring your MPLS VPLS services using BGP Signaling. The method of 
establishing VPLS with BGP accomplishes both auto-discovery and signaling. 
After configuring your MPLS backbone detailed in the previous section, follow 
the steps below to configure VPLS service with BGP (shown configuration for 
R1): 
Step 1 - Configure BGP and enable VPLS capability 
 
Step 2 - Configure Access port: 
 
Step 3 - Configure the VPLS service: 
! SVCMGR: 
-> service sdp 102 vpls far-end 1.1.1.6  
-> service sdp 103 vpls far-end 1.1.1.7  
! SVCMGR: 
-> service 1 vpls vplsid 100 signaling ldp 
-> service 1 vlan-xlation enable 
! SVCMGR: 
-> service 1 sap port 1/1/4:0 
! SVCMGR: 
-> service 1 bind-sdp 102 103  
! BGP: 
-> ip load bgp 
-> ip bgp mpls 
-> ip bgp autonomous-system 65724 
-> ip bgp address-family l2vpn-vpls 
-> ip bgp neighbor 1.1.1.6 
-> ip bgp neighbor 1.1.1.6 remote-as 65724 
-> ip bgp neighbor 1.1.1.6 update-source "Loopback0" 
-> ip bgp neighbor 1.1.1.6 activate l2vpn-vpls 
-> ip bgp neighbor 1.1.1.6 admin-state enable 
-> ip bgp neighbor 1.1.1.7 
-> ip bgp neighbor 1.1.1.7 remote-as 65724 
-> ip bgp neighbor 1.1.1.7 update-source "Loopback0" 
-> ip bgp neighbor 1.1.1.7 activate l2vpn-vpls 
-> ip bgp neighbor 1.1.1.7 admin-state enable 
-> ip bgp admin-state enable 
! SVCMGR: 
-> service access port 1/1/4  

<<<PAGE 35>>>
 
 
35 
 
Design Guide 
MPLS Reference 
 
Step 4 - Create a SAP on the access port for VPLS service: 
 
This configuration is only required on the PE/LER nodes where the full-mesh 
pseudowire service tunnels will be established. In our example topology, this 
will be configured on R1, R6, and R7.  
Verification Commands 
Below is a summary of commands that can be used for verifying the VPLS 
configuration: 
Command 
Description 
show service 
Displays information about the VPLS service 
configured on the switch. 
show service ports  
Displays the virtual ports associated with the 
specified VPLS service. 
show service vpls 
sap  
Displays the configuration information for the 
specified SAP ID associated with the specified 
VPLS service. 
show service debug-
info  
Displays debug information for the virtual 
ports associated with the VPLS service 
show service info  
Displays the Service Manager configuration 
for the local switch. 
show service sdp 
mpls  
Displays the SDP configuration for VPLS 
services. 
show service bind-
sdp vpls  
Displays the SDP binding configuration for 
VPLS services. 
show service mesh-
sdp  
Displays the bindings between VPLS service 
and SDPs. 
show service vpls 
mesh-sdp  
Displays SDP bindings with the specified SDP 
ID and/or service ID number. 
 
Below is a sample configuration output to verify VPLS configuration: 
! SVCMGR: 
-> service 2 vpls vplsid 11 signaling bgp ve-id 1 
-> service 2 vlan-xlation enable 
! SVCMGR: 
-> service 2 sap port 1/1/4:0 

<<<PAGE 36>>>
 
 
36 
 
Design Guide 
MPLS Reference 
Display information about the services configured on the switch: 
 
Display debug information for the virtual ports associated with 
the service: 
 
Display the virtual ports associated with the specified VPLS 
service: 
 
 
Display the SDP binding configuration for VPLS services: 
-> show service vpls 
Legend: * denotes a dynamic object , Y - Yes , N - No 
VPLS Service Info 
ServiceId    Adm  Oper Stats SAP Count Bind Count   Vplsid    Mcast mode Protocol 
-----------+----+----+-----+----------+----------+----------+----------+-------- 
100  
     Up   Up   N 
 1  
 
1  
100  
   Headend    LDP 
-> show service vpls 100 debug-info 
Legend: * denotes a dynamic object 
VPLS Service 1 Debug Info 
Admin  
: Up,  
Oper : Down,  
 
Stats : N, 
VPLSID  : 100,  RemoveIngTag : N, 
VFI  
: 1,  
McIdx : 3,  
 
StatsHandle : 0 
 
 
 
 
  Sap Trusted:Priority/  
      Sap Description/ 
       Stats/ 
Identifier    Adm Oper Stats  Sdp FarEnd/Group         Intf   Sdp Intf Name          VP    L2 McIdx 
------------+----+----+-----+---------------------+---------+------------------+---------+-------- 
sap:1/1/23:0  Up  Down   N     Y:x       
        1/1/11  
     -   
 1        0 
 
Total Ports: 1 
-> show service vpls 100 ports 
Legend: * denotes a dynamic object 
VPLS Service 1 Debug Info 
Admin  : Up,  Oper : Up,  
 
Stats : N, 
VPLSID  : 100,  RemoveIngTag : N, 
    Sap Trusted:Priority/  
 
Sap Description / 
Identifier  
   Adm Oper Stats  Sdp FarEnd/Group      Intf  
Sdp Intf Name 
----------------+----+----+-----+--------------------+--------+-------------------- 
sap:1/1/11:10     Up   Up    N      Y:x  
 
   1/1/11      - 
 
Total Ports: 1 

<<<PAGE 37>>>
 
 
37 
 
Design Guide 
MPLS Reference 
 
 
Below is a sample configuration output to verify BGP configuration: 
Display the current global settings for the local BGP speaker: 
 
-> show service bind-sdp  
Legend: * denotes a dynamic object 
All Bind-SDP Info 
                          FarEnd/Group Addr 
SvcId    Bind-Sdp         FarEnd SysId:BVlan   Oper SvcType 
--------+----------------+--------------------+----+-------- 
1          5:1                  1.1.1.1              Up   VPLS 
  
-> show service bind-sdp vpls  
Legend: * denotes a dynamic object  
VPLS Bind-SDP Info  
SvcId    Bind-Sdp         VplsId    FarEnd/Group Addr    Oper Intf     InLabel  OutLabel   
--------+----------------+---------+--------------------+----+--------+--------+----------  
100      10:100           100       1.1.1.1              Up   -        52482    52480       
  
Total Bind-SDPs: 1  
  
-> show service bind-sdp 10  
Legend: * denotes a dynamic object  
VPLS Bind-SDP Info  
SvcId   Binds-Sdp    Vplsid    FarEnd/Group Addr   Oper    Intf       Intf Name    Gateway  
------+-----------+---------+--------------------+------+-----------+------------+----------- 
100     10:100        100     1.1.1.1               Up   20.20.20.2   intf2        20.20.20.1   
  
Total Bind-SDPs: 1  
-> show ip bgp 
Admin Status                         = disabled, 
Operational Status                   = down, 
Autonomous System Number             = 1, 
BGP Router Id                        = 0.0.0.0, 
Confederation Identifier             = 0, 
IGP Synchronization Status           = disabled, 
Minimum AS Origin Interval (seconds) = 15, 
Default Local Preference             = 100, 
Route Reflection                     = disabled, 
Cluster Id                           = 0.0.0.0, 
Missing MED Status                   = Best, 
Aspath Comparison                    = enabled, 
Always Compare MED                   = disabled, 
Fast External FailOver               = disabled, 
Log Neighbor Changes                 = disabled, 
Multiple Paths                       = disabled, 
Graceful Restart                     = enabled, 
Graceful Restart Status              = Not Restarting, 
Configured Graceful Restart Interval = 90s, 
IPv4 Unicast                         = enabled, 
IPv6 Unicast                         = disabled, 
BFD Status                           = disabled, 
ASN Output Format                    = asplain, 

<<<PAGE 38>>>
 
 
38 
 
Design Guide 
MPLS Reference 
Display in the last two highlighted fields whether L2VPN VPLS is 
activated for the neighbor and whether L2VPN VPLS capability is 
enabled or disabled between the peers: 
 
Display the configured VPLS info and number of mesh peers 
established: 
 
-> show ip bgp neighbors 120.120.0.2 
 
Neighbor address                  = 120.120.0.2, 
Neighbor autonomous system        = 64740, 
Neighbor Admin state              = enabled, 
Neighbor Oper state               = idle, 
Neighbor passive status           = disabled, 
Neighbor name                     = peer(120.120.0.2), 
… 
<Output Snipped> 
… 
BFD Status                        = enabled, 
Activate IPv4 unicast             = enabled, 
Activate L2VPN vpls               = enabled, 
Neighbor L2VPN vpls               = advertised 
-> show ip bgp l2vpn-vpls 
VPLS-ID    VE-ID        Route-Target   Route-Distinguisher   Discovered-Peers 
----------+----------+---------------+---------------------+---------------- 
50           51          65724:50      65724:50                    1 

<<<PAGE 39>>>
 
 
39 
 
Design Guide 
MPLS Reference 
Display the local and remote VPLS attributes info: 
 
 
The following commands can be used to verify the source learning MAC 
address table information for the switch: 
Display source learning MAC Address Table information for the 
switch: 
 
-> show ip bgp l2vpn-vpls path 
Legends: RD  = Route Distinguisher 
         VBO = VE Block Offset 
         VBS = VE Block Size 
         Nbr = Neighbor 
VPLS-ID    VE-ID  RD              VBO      VBS     LabelBase     Nbr address     Nexthop 
----------+------+-------------+--------+--------+------------+---------------+--------------- 
  50         51    65724:50        -        -          -          <none>          5.5.5.5 
  50         50    65724:50        1       64        53122        4.4.4.4         4.4.4.4 
 
-> show ip bgp l2vpn-vpls path 50 
BGP Path parameters: 
Path neighbor             = <none>, 
Path protocol             = local, 
Path Route Distinguisher  = 65724:50, 
Path VE-ID                = 51 
Path VE Block Offset      = - 
Path VE Block Size        = - 
Path Label Base           = - 
Path nextHop              = 5.5.5.5 
Path origin               = igp 
Path local preference     = 100 
Path Ext Community        = RT: 65724:50, MTU:9194 
Path neighbor             = 4.4.4.4, 
Path protocol             = ibgp, 
Path Route Distinguisher  = 65724:50, 
Path VE-ID                = 50 
Path VE Block Offset      = 1 
Path VE Block Size        = 64 
Path Label Base           = 53122 
Path nextHop              = 4.4.4.4 
Path origin               = igp 
Path local preference     = 100 
Path Ext Community        = RT: 65724:50, MTU:9194 
-> show mac-learning  
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
        ID = ISID/Vnid/vplsid 
  
   Domain    Vlan/SrvcId[:ID]    Mac Address        Type        Operation      Interface 
------------+----------------+-------------------+-----------+-------------+------------------ 
      VLAN       1      
  2c:fa:a2:38:ee:94   dynamic     bridging         3/1/5  
      VLAN      10     
  2c:fa:a2:b5:14:b1   dynamic     bridging         1/1/53  
      VLAN      10     
  2c:fa:a2:b5:14:c7   dynamic     bridging         1/1/53  
      VLAN      10     
  2c:fa:a2:b5:14:c2   dynamic     bridging         3/1/11  
      VPLS      10:100    
  00:00:00:11:11:01   dynamic    servicing       sap:3/1/12:11  
      VPLS      10:100    
  00:00:00:11:11:02   dynamic    servicing       sdp:50:10  
  
Total number of Valid MAC addresses above = 6 

<<<PAGE 40>>>
 
 
40 
 
Design Guide 
MPLS Reference 
Display MAC address table, with optional parameters for filtering: 
 
VPWS Configuration Example 
We will use the following topology to provide the configuration steps for MPLS 
VPWS services. 
 
Physical Topology 
 
Logical Topology 
 
-> show mac-learning domain vpls  
Legend: Mac Address: * = address not valid, 
        Mac Address: & = duplicate static address, 
        ID = ISID/Vnid/vplsid 
  
   Domain     Vlan/SrvcId[:ID]     Mac Address        Type       Operation     Interface 
------------+------------------+------------------+-----------+-------------+-----------------
-------- 
      VPLS      10:100           00:00:00:11:11:01   dynamic    servicing       sap:3/1/12:11  
      VPLS      10:100           00:00:00:11:11:02   dynamic    servicing       sdp:50:10  
  
Total number of Valid MAC addresses above = 2 

<<<PAGE 41>>>
 
 
41 
 
Design Guide 
MPLS Reference 
 
MPLS Backbone Configuration with LDP Signaling 
Configuring the MPLS backbone is similar to the configuration steps details in 
the previous section for VPLS. 
 
MPLS VPWS Service with LDP Backbone Signaling 
Step 1 - Configure VPWS Service 
Create a service for VPWS instance and communicate the VPWS ID to MPLS. 
Beow is the configuration on Routers 1 and 3 (PE1 and PE2): 
 
Step 2 - Configure SDP for VPWS 
Create a static SDP and trigger a message to LDP to establish a target peer with 
the far-end IP address. 
For Router 1 (PE1): 
 
For Router 3 (PE2): 
 
Step 3 – Create a binding of the SDP to the VPWS service 
Create a binding of an SDP to the VPWS service (VPWS) and trigger a message 
to establish a VC label. 
For Router 1 (PE1): 
! SVCMGR: 
-> service 1 vpws vcid 100 description "VPWS service" admin-state enable 
! SVCMGR: 
-> service sdp 20 mpls far-end 9.1.1.3 description "VPWS Peer" 
! SVCMGR: 
-> service sdp 20 mpls far-end 9.1.1.1 description "VPWS Peer" 

<<<PAGE 42>>>
 
 
42 
 
Design Guide 
MPLS Reference 
 
For Router 3 (PE2): 
 
Step 4 – Configure access ports and create SAP on the access port for MPLS-VPWS 
service 
Set a switch port as an access port, and configure a SAP by associating a SAP ID 
with a VPWS service. 
For Router 1 (PE1): 
 
For Router 3 (PE2): 
 
The above configuration will setup a virtual bridge between port 1/1/1 on PE1 
and port 1/1/2 on PE2. 
 
Verification Commands 
Below is a summary of commands that can be used for verifying the VPLS 
configuration: 
Command 
Description 
show service 
Displays information about the VPLS service 
configured on the switch. 
show service ports  
Displays the virtual ports associated with the 
specified VPLS service. 
show service vpls 
sap  
Displays the configuration information for the 
specified SAP ID associated with the specified 
VPLS service. 
show service debug-
info  
Displays debug information for the virtual 
ports associated with the VPLS service 
show service info  
Displays the Service Manager configuration 
for the local switch. 
! SVCMGR: 
-> service 1 bind-sdp 20 spoke description "Bind SDP to VPWS service" 
! SVCMGR: 
-> service 1 bind-sdp 20 spoke description "Bind SDP 20 to VPWS service" 
! SVCMGR: 
-> service access port 1/1/1 
-> service 1 sap port 1/1/1:0 
! SVCMGR: 
-> service access port 1/1/2 
-> service 1 sap port 1/1/2:0 

<<<PAGE 43>>>
 
 
43 
 
Design Guide 
MPLS Reference 
show service sdp 
mpls  
Displays the SDP configuration for VPLS 
services. 
show service bind-
sdp vpls  
Displays the SDP binding configuration for 
VPLS services. 
show service mesh-
sdp  
Displays the bindings between VPLS service 
and SDPs. 
show service vpls 
mesh-sdp  
Displays SDP bindings with the specified SDP 
ID and/or service ID number. 
 
Below is a sample configuration output to verify VPWS configuration: 
Display only the VPWS services: 
 
Display additional details about the specified service: 
 
Display the SDP configuration for the bridge: 
 
-> show service vpws 
Legend: * denotes a dynamic object 
VPWS Service Info 
                            SAP   Bind 
ServiceId    Adm Oper Stats Count Count    VcId    Mcast mode Protocol 
-----------+----+----+-----+-----+-----+----------+----------+-------- 
1  
      Up   Up   N     1      1      100  
   -        LDP 
 
Total Services: 1 
-> show service 1 
VPWS Service Detailed Info 
  Service Id : 100,  
 
 
Description: VPWS Peer 
  VCID : 100,   
 
 
VPWS Name : VPWS_00100, 
  Multicast-Mode : Headend,   
Vlan Translation : No, 
  Admin Status : Up,   
 
Oper Status Up, 
  Stats Status : No,   
 
Service Type : VPWS, 
  Allocation Type : Static,   
MTU : 9194, 
  VPWS Type : Ethernet,  
 
Signaling : LDP, 
  SAP Count : 1,  
 
 
SDP Bind Count : 1, 
  Mgmt Change : 01/12/2008 20:34:36,  Status Change : 01/14/2008 15:17:30 
-> show service sdp 
Legend: * denotes a dynamic object 
SDP Info 
             FarEnd/Group Ip Addr 
SdpId       FarEnd SysId:BVlan    Adm Oper  SvcType 
-----------+---------------------+----+----+-------- 
20  
 
     9.1.1.3       Up   Up   VPWS 
Total SDPs: 1 

<<<PAGE 44>>>
 
 
44 
 
Design Guide 
MPLS Reference 
Display the SDP binding configuration for VPWS services: 
 
MPLS OAM Verification Commands 
You can use the “mpls ping ldp” command to initiate an LSP ping to check the 
data plane connectivity for MPLS LDP LSPs. For example: 
 
You can also use the “mpls traceroute ldp” command to trace the path 
traversed by a specified echo request packet in an MPLS LDP LSP. For example: 
 
 
Conclusion 
MPLS is a mature and proven technology and remains crucial for service 
providers and enterprise mission-critical networks. This is due to its fast-
covergence, traffic engineering capabilities, and its ability to provide multiple 
services (Layer 2 or Layer 3) over a single unified infrastructure. It’s complexity 
is proportional to it’s performance. ALE IP/MPLS implementation 
 
 
 along with it’s service-defined networking allows for achieving an autonomous 
multi-technology fabric network. 
-> show service bind-sdp vpws 
Legend: * denotes a dynamic object 
VPWS Bind-SDP Info 
SvcId     Bind-Sdp     VCId   FarEnd/Group Addr Oper   Intf    InLabel  OutLabel 
--------+----------+---------+------------------+----+--------+--------+--------- 
1  
     20:1  
 100  
    9.1.1.1  
     Up     -       52482   52480 
-> mpls ping ldp 1.1.1.4/32 
Please wait... 
Sending 5 MPLS Echos to 1.1.1.4, timeout is 5 seconds 
Codes: 
'!' - Success, 'Q' - request not sent, '.' - timeout, 
'F' No FEC Found, 'R' - Transit (LBL Switched),'X' - Unknown code 
Type 'Ctrl+C' to abort 
! seq_num = 1 1.1.1.4 1.94 ms 
! seq_num = 2 1.1.1.4 0.75 ms 
! seq_num = 3 1.1.1.4 0.67 ms 
! seq_num = 4 1.1.1.4 0.75 ms 
! seq_num = 5 1.1.1.4 0.76 ms 
Success Rate is 100.00 percent (5/5) 
round-trip min/avg/max = 0.67/1.30/1.94 
-> mpls trace ldp 1.1.1.4/32 
Please wait... 
Tracing MPLS Label Switched Path to 1.1.1.4, timeout is 5 seconds 
Codes: 
'!' - Success, 'Q' - request not sent, '.' - timeout, 
'F' No FEC Found, 'R' - Transit (LBL Switched),'X' - Unknown code 
Type 'Ctrl+C' to abort 
0 20.2.1.2 [Labels: implicit-null] 
! 1 1.1.1.4 0.93 ms 

<<<PAGE 45>>>
 
 
45 
 
Design Guide 
MPLS Reference 
 
Related Documents 
[1] RFC 3031 – MPLS Architecture - https://datatracker.ietf.org/doc/rfc3031/ 
[2] RFC 3036 – LDP Specification - https://datatracker.ietf.org/doc/rfc3036/ 
[3] RFC 5036 – LDP Specification - https://datatracker.ietf.org/doc/rfc5036/ 
[4] RFC 2283 – Multiprotocol Extensions for BGP-4 - 
https://datatracker.ietf.org/doc/html/rfc2283  
[5] RFC 4761 - Virtual Private LAN Service (VPLS) Using BGP for Auto-Discovery and 
Signaling - https://datatracker.ietf.org/doc/rfc4761/  
[6] RFC 4762 - Virtual Private LAN Service (VPLS) Using Label Distribution Protocol 
(LDP) Signaling - https://datatracker.ietf.org/doc/rfc4762/  
[7] RFC 3478 - Graceful Restart Mechanism for Label Distribution Protocol - 
https://datatracker.ietf.org/doc/rfc3478/  
[8] RFC 4379 – Detecting MPLS Data Plane Failures - 
https://datatracker.ietf.org/doc/html/rfc4379  
[9] RFC 4456 - BGP Route Reflection: An Alternative to Full Mesh Internal BGP (IBGP) - 
https://datatracker.ietf.org/doc/rfc4456/  
[10] 
AOS 8.10 R03 Network Configuration Guide - https://www.al-enterprise.com/-
/media/assets/internet/documents/aos-release-810r3-network-configuration-user-
guide-rev-a-en.pdf  
[11] 
AOS 8.10 R03 CLI Reference Guide – https://www.al-enterprise.com/-
/media/assets/internet/documents/omniswitch-aos-release-810r3-cli-reference-user-
guide-rev-a-en.zip  
[12] 
AOS 8.10 R03 Switch Management Guide - https://www.al-enterprise.com/-
/media/assets/internet/documents/omniswitch-aos-release-810r3-switch-
management-user-guide-rev-a-en.zip  
[13] 
AOS 8.10 R03 Advanced Routing Guide - https://www.al-enterprise.com/-
/media/assets/internet/documents/omniswitch-aos-release-810r3-advanced-routing-
user-guide-rev-a-en.pdf  
[14] 
MEF 6.3 – Subscriber Ethernet Services Definitions -  https://www.mef.net/wp-
content/uploads/2019/11/MEF-6-3.pdf  
 
