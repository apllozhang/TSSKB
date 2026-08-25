# sol-campus-architecture — 解决方案文档合并（页码全册连续）


<<<DOC 1: ale_campus-architecture-guide-en.pdf | 起始页 1 | 43p>>>

<<<PAGE 1>>>
Mobile Campus Architecture Guide 
1 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Mobile Campus 
 Architecture guide 
 
Unlock the potential of modern 
networking 
 
 
 
 
 
 

<<<PAGE 2>>>
Mobile Campus Architecture Guide 
2 
 
Table of contents 
1 About this architecture guide ........................................................................................ 5 
1.1 
Abstract ....................................................................................................... 5 
1.2 Purpose............................................................................................................. 5 
1.3 Audience ........................................................................................................... 5 
2 Introduction ............................................................................................................. 5 
2.1 Digital Age Networking .......................................................................................... 5 
2.2 OmniAccess Stellar ............................................................................................... 5 
2.3 OmniSwitch ........................................................................................................ 6 
3 High Level Campus Design ............................................................................................ 6 
4 Local Area Network (LAN) ............................................................................................ 6 
4.1 Two and Three-Tier Model ...................................................................................... 7 
4.1.1 Two-Layered Collapsed Core Model ...................................................................... 7 
4.1.2 Three-Tier Model ............................................................................................ 7 
4.2 Virtual Chassis..................................................................................................... 8 
4.3 VLANs – Trunks – LACP ........................................................................................... 8 
4.3.1 Virtual Local Area Networks (VLANs) and Multiple VLAN Registration Protocol (MRVP) .......... 8 
4.3.2 Trunking ...................................................................................................... 9 
4.3.3 Link Aggregation Control Protocol (LACP) ............................................................... 9 
4.4 Shortest Path Bridging (SPB) .................................................................................... 9 
4.5 Ethernet VPN (EVPN) ............................................................................................ 10 
4.6 Multiprotocol Label Switching (MPLS) ........................................................................ 10 
4.7 Dynamic Routing ................................................................................................. 11 
4.7.1 Open Shortest Path First (OSPF) ......................................................................... 11 
4.7.2 Border Gateway Protocol (BGP) ......................................................................... 11 
4.7.3 Intermediate System to Intermediate System (IS-IS) ................................................. 12 
4.7.4 Routing Information Protocol (RIP) ...................................................................... 12 
5 Wireless Local Area Network (WLAN) .............................................................................. 12 
5.1 RF Planning ....................................................................................................... 12 
5.1.1 Coverage Planning ......................................................................................... 13 
5.1.2 Capacity Planning .......................................................................................... 13 
5.1.3 Frequency and Channel Selection and interference management. ................................ 13 
5.1.4 AP Mounting, Placement and Density ................................................................... 13 
5.1.5 Power and Antenna Configuration ....................................................................... 14 
5.1.6 Predictive Planning and heatmap ....................................................................... 14 
5.1.7 Radio Dynamic Adjustment ............................................................................... 14 
5.3 AP management, control, and data plane overview ....................................................... 15 
5.3.1 Centralized Management ................................................................................. 15 
5.3.2 Distributed Control Plane ................................................................................. 15 
5.3.3 Data Plane: bridged or tunneled......................................................................... 16 
5.4 Management modes ............................................................................................. 17 

<<<PAGE 3>>>
Mobile Campus Architecture Guide 
3 
 
5.4.1 Wi-Fi Express ............................................................................................... 18 
5.4.2 Wi-Fi Enterprise ............................................................................................ 18 
5.4.3 Wi-Fi Cloud .................................................................................................. 18 
5.5 AP group .......................................................................................................... 18 
5.6 RF profile ......................................................................................................... 18 
5.7 AP to switch interface .......................................................................................... 19 
5.7.1 OmniSwitch ................................................................................................. 19 
5.7.2 Third-party switch ......................................................................................... 19 
5.7.4 AP authentication (secure AP mode) and Trust Tag .................................................. 19 
5.7.5 VLAN interface ............................................................................................. 21 
5.7.6 SPB interface ............................................................................................... 23 
5.9 Roaming concepts ............................................................................................... 25 
5.9.1 Fast Roaming ............................................................................................... 27 
5.9.2 Layer 2 Roaming............................................................................................ 27 
5.9.3 Layer 3 Roaming............................................................................................ 27 
5.10 SSIDs - VLAN pooling ........................................................................................... 28 
5.11 Quality of Service (QoS) ....................................................................................... 28 
5.12 Specific use cases .............................................................................................. 29 
5.12.1 Wi-Fi Mesh ................................................................................................. 29 
5.12.2 Wi-Fi Bridge (Point-to-Point) ........................................................................... 30 
5.12.3 Remote Access Points .................................................................................... 31 
5.12.3 Voice over WLAN.......................................................................................... 32 
5.12.4 Multimedia Consumer device – mDNS .................................................................. 32 
5.12.5 Asset Tracking ............................................................................................. 34 
5.12.6 Stellar APs Downlink Port Capabilities ................................................................ 35 
6 Network Management System (Enterprise/Cirrus) ............................................................... 35 
6.1 Introduction ...................................................................................................... 35 
6.2 OmniVista Enterprise Deployment Modes (Standalone and High-Availability).......................... 35 
6.3 AP Onboarding ................................................................................................... 36 
7.3 Unified Access .................................................................................................... 36 
8 Security ................................................................................................................. 36 
8.1 Network Access Control Solutions ............................................................................. 36 
8.2 Role-Based Access and Access Role Profile (ARP) .......................................................... 37 
8.2.1 Access Guardian ............................................................................................ 37 
8.3 Authentication ................................................................................................... 38 
8.3.1 IoT fingerprinting/MAC .................................................................................... 38 
8.3.2 Employee .................................................................................................... 38 
8.3.3 Guest ......................................................................................................... 39 
8.3.4 SSID........................................................................................................... 40 
8.3.5 BYOD ......................................................................................................... 40 
8.4 Quarantine Manager ............................................................................................. 40 

<<<PAGE 4>>>
Mobile Campus Architecture Guide 
4 
 
8.5 Web Content Filtering (WCF) .................................................................................. 41 
8.5 Wireless Intrusion Prevention System (WIPS)................................................................ 41 
9 Reference documents ................................................................................................ 42 
10 Conclusion ............................................................................................................ 43 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

<<<PAGE 5>>>
Mobile Campus Architecture Guide 
5 
 
1 About this architecture guide 
1.1 Abstract 
The campus network serves as the foundational infrastructure of your organization, facilitating seamless 
communication and access to essential information. It is not merely an assembly of cables and 
connections but a complex, dynamic system that demands meticulous planning and strategic 
consideration. 
The key goals of any campus network architecture are to ensure high availability, scalability, security, 
and performance. A well-designed network must support continuous and reliable access to resources, 
accommodate growth and evolving demands, protect data and communications from internal and 
external threats, and deliver consistent, high-speed connectivity to all users and devices. 
This guide provides a comprehensive exploration of the fundamental components of a reliable and 
adaptable network architecture. It aims to equip you with the essential knowledge to design and 
implement a network infrastructure that not only fulfills current operational needs but also anticipates 
and adapts to future challenges and technological advancements. 
1.2 Purpose  
The purpose of this architecture guide is to provide the OmniSwitch® and OmniAccess® Stellar Wireless 
users guidelines for designing a state-of-the-art campus network. It outlines best practices and high-level 
recommendations to create an intelligent, secure, and modern mobile campus network infrastructure. It 
does not attempt to cover every aspect, nor every architecture option, only the most common, 
validated, and recommended architectures. You are encouraged to refer to the Alcatel-Lucent Operating 
Software (AOS),  OmniAccess Stellar Operating System (AWOS) documentation, ALE application notes and 
user guides for additional details, options, and guidelines. 
1.3 Audience 
The intended audience for this document includes customer and business partner networking 
professionals involved in the design and deployment of enterprise mobile campus network. Providing 
valuable resources for architecting and designing OmniSwitch and OmniAccess Stellar networks within 
the OmniVista network management system. 
2 Introduction 
2.1 Digital Age Networking 
At ALE, we believe that the network should be built on three key pillars: 
• 
An Autonomous Network that easily, automatically, and securely connects people, processes, 
applications, and objects. 
• 
Secure and efficient onboarding of IoT devices using segmentation techniques that minimize the 
risk of having the entire network being compromised. 
• 
Business Innovation through workflow automation simplifying the creation and roll-out of new 
automated digital business processes to enhance productivity and enable new revenue streams. 
 
2.2 OmniAccess Stellar 
The Alcatel-Lucent OmniAccess Stellar is an indoor and outdoor (Ruggedized) access points solution 
based on Wi-Fi 7 (802.11be), Wi-Fi 6/6E (802.11ax) and Wi-Fi 5 (802.11ac) technologies that support 
versatile deployments in any size network.  
OmniAccess Stellar APs are built and designed using Alcatel-Lucent Enterprise innovative distributed 
intelligence that act like a virtual controller. They are managed as a single system or cluster, in a 
distributed and coordinated manner, eliminating the need for physical centralized controllers, and 
therefore offering the best performance and scalability, and ensuring high availability, with operational 
simplicity and low Total Cost of Ownership (TCO). 
The control plane of the OmniAccess Stellar WLAN solution operates based on localized communications 
among neighboring Access Points. Each AP engages with its adjacent counterparts through two primary 
methods of exchange: "over the air" and "over the LAN." The former involves the use of the Neighbor 
Management Protocol, whereby APs broadcast essential information such as AP management IP addresses 

<<<PAGE 6>>>
Mobile Campus Architecture Guide 
6 
 
to facilitate discovery and initial connectivity. The latter method involves a combination of Layer 2 (L2) 
broadcast/multicast and IP connectivity between the AP management IP addresses. This approach allows 
the APs to synchronize on Radio Frequency (RF) parameters, including channel utilization and transmit 
power, and to exchange context information about roaming clients, ensuring seamless client mobility 
and optimized network performance. 
OmniAccess Stellar Product line Matrix 
 
2.3 OmniSwitch 
Our switches run the widely deployed and field-proven Alcatel-Lucent Enterprise Operating system (AOS) 
that offers reliability, performance, easy management, and advanced system- and network-level 
resiliency features. OmniSwitch products are easy to deploy and offer out-of-the-box plug-and-play, 
zero-touch provisioning, network automation and disaster recovery options.  
Simplified installation and service provisioning ensures fast, scalable, and cost-efficient implementation. 
Most of the switches offer virtual chassis technology to combine multiple same-family switches in a 
single entity for unified management and control. All switches can be fully managed from the Alcatel-
Lucent Enterprise OmniVista Enterprise Network Management System and are cloud-ready with 
OmniVista Cirrus, which offers secure, resilient, and scalable cloud-based network management. 
OmniSwitch Product Line matrix 
 
3 High Level Campus Design 
 
 
4 Local Area Network (LAN)  
A Local Area Network (LAN) is a network configuration that connects a group of computers and devices 
within a specific physical location, such as a home, office, or campus. The scope of LANs can range from 

<<<PAGE 7>>>
Mobile Campus Architecture Guide 
7 
 
a modest network serving a single user in a home to extensive networks that support thousands of users 
and devices in large business or educational environments. 
 A LAN is fundamentally characterized by its geographic confinement to a small area, presenting a 
contrast to Wide Area Networks (WANs) or Metropolitan Area Networks (MANs) that span broader 
geographic extents and possess the capacity to interlink numerous LANs over municipal, regional, or 
international boundaries. The architecture of a LAN typically includes essential networking components 
such as cables, access points, switches, router, and others. These elements facilitate connectivity to 
various networks, servers, and the internet. 
4.1 Two and Three-Tier Model 
When considering which network topology to implement, consider the characteristics of your network 
and its specific needs. 
The Core Layer acts as the network's backbone, providing high-speed data transfer and reliable 
connectivity between distribution layer devices. It handles large volumes of traffic and ensures fast, 
fault-tolerant, and highly available connections. 
The Distribution Layer serves as an intermediary, aggregating data from the access layer and managing 
traffic through routing, filtering, and Quality of Service (QoS) policies. This layer plays a key role in 
traffic management, ensuring data is routed efficiently. 
The Access Layer connects end devices, such as end-users, IoT and wireless access points, to the 
network, handling functions like port security, VLAN assignment, and network segmentation. 
The Two-Layered Collapsed Core Model offers simplicity, cost efficiency, and adaptability, making it a 
suitable choice for smaller networks with straightforward requirements. On the other hand, the Three-
Tier Network Topology provides scalability, redundancy, and advanced capabilities, making it more 
suitable for larger, intricate networks that require high performance and reliability. 
4.1.1 Two-Layered Collapsed Core Model 
The Two-Layered Collapsed Core Model is a streamlined network architecture that merges the core and 
distribution layers of the traditional three-tier design into a single layer. This results in a two-tier 
structure, with the Collapsed Core/Distribution Layer handling both core routing and distribution 
functions. This layer provides high-speed, reliable backbone connectivity while aggregating traffic from 
multiple access switches. 
This model offers several advantages. Its simplified design reduces network complexity, making it easier 
to manage and troubleshoot. Cost efficiency is another key benefit, as it requires fewer hardware 
components than the traditional three-tier architecture, leading to lower capital expenditures and 
reduced operational costs. By eliminating an entire layer of switching, the model reduces the number of 
hops data must traverse, which decreases latency and can enhance performance. With fewer devices to 
manage, network administration becomes more straightforward, and centralized management tools can 
be more effectively utilized. The Two-Layered Collapsed Core Model is well-suited for small to medium-
sized networks, making it a versatile choice for various organizational needs. 
4.1.2 Three-Tier Model 
The Three-Tier Network Topology offers several advantages. Its modular structure enhances scalability, 
making it easier to expand the network as the organization grows. The distinct roles of each layer 
optimize traffic flow and reduce congestion, improving network performance. The ability to manage and 
maintain each layer independently further enhances operational efficiency. 
The design also improves redundancy and reliability. The core layer’s high availability and fault 
tolerance ensure continuous network operation even in case of device failure. The distribution layer 
supports advanced security and QoS policies, ensuring secure and efficient data transmission. The 
segmented design provides greater flexibility in implementing network policies, adapting to changing 
requirements, and integrating modern technologies. 
Overall, the Three-Tier Network Topology is ideal for large, complex networks that demand high 
performance, scalability, and robust management capabilities, offering a structured and efficient 
approach to network design. 

<<<PAGE 8>>>
Mobile Campus Architecture Guide 
8 
 
 
4.2 Virtual Chassis 
Access-layer switches can be configured in a Stack or Virtual Chassis arrangement to extend port density 
at a given location beyond what a single device can support. While Stack and Virtual Chassis technologies 
serve equivalent functions at the Access Layer, they differ in their underlying implementation. Switches 
at this layer are interconnected in a ring topology using dedicated or standard ports, forming a Virtual 
Fabric for the Stack or Virtual Chassis, where each physical unit operates as a virtual slot within the 
system. This configuration acts as a single logical entity with unified control and management planes. An 
election process designates one unit as the Master control module, with another unit serving as a hot-
standby Slave control module, while the remaining units assume Idle roles. In the event of a Master 
failure, the Slave seamlessly assumes control, ensuring control plane resiliency. 
Traffic within the Virtual Chassis or Stack is optimized for performance, employing shortest path routing, 
and pruning mechanisms. Forwarding decisions are made locally at each virtual slot or unit and remain 
unaffected by a transition from Master to Slave. As the point of demarcation between the network and 
end-users or devices, the Access Layer is critical for implementing access policies, whether for wired or 
wireless connections. 
4.3 VLANs – Trunks – LACP 
In a campus network, particularly at the access layer, VLANs, trunking, and LACP play crucial roles in 
ensuring efficient, scalable, and resilient network connectivity. 
4.3.1 Virtual Local Area Networks (VLANs) and Multiple VLAN Registration Protocol (MRVP)  
Virtual Local Area Networks (VLANs) are essential in modern campus network design, providing a means 
to logically segment a physical network into distinct broadcast domains. This segmentation allows for 
more efficient traffic management by reducing broadcast domain sizes, minimizing unnecessary traffic, 
and enhancing security. VLANs enable the grouping of devices based on function, department, or 
project, regardless of their physical location. For example, devices within the Finance department can 
be assigned to a specific VLAN, even if dispersed across multiple buildings. 
VLANs offer significant advantages. They enhance security by isolating traffic between VLANs, preventing 
direct communication between devices in different VLANs unless routed through a Layer 3 device. This 
isolation reduces the risk of unauthorized access and improves overall network security. VLANs also 
contribute to scalability, allowing for easy network expansion by integrating new devices into the 
appropriate VLAN without altering the physical topology. Additionally, by confining broadcast traffic 
within VLAN boundaries, VLANs optimize network performance, reducing congestion and ensuring 
efficient bandwidth usage. 
Two types of VLANs exist at the Access Layer: Management VLANs (used for management access to the 
network device) and User VLANs (for user traffic). Different Management VLANs for Access Switches and 
WLAN Access Points are recommended.  
For Stellar WLAN deployments, configure the Management VLAN as an untagged VLAN for AP 
communication with other APs and the OmniVista Enterprise. This VLAN does not need to be consistent 
across all APs or within the same AP group, but we recommend having a dedicated VLAN ID for AP 
management and a max of 64 APs per VLAN. Each AP can operate on a different Management VLAN as 
needed, allowing for flexible network design and segmentation.  
In Stellar network configurations, it is possible to use the same VLAN ID for both wireless and wired 
clients, though it is recommended to reserve a separate VLAN ID for wireless clients. 
Tagged VLANs are used by WLAN clients for their traffic. This VLAN configuration is linked with the 
Access Role Profile, like a User Network Profile (UNP). Different VLANs can be assigned to the same SSID 
across various AP groups, which can facilitate Layer 3 roaming. This setup allows for seamless roaming 
between AP groups while maintaining VLAN consistency within each group, optimizing network 
performance and user experience. 
Enterprise networks are highly dynamic environments and therefore, static VLAN assignment of User 
VLANs is impractical and not recommended.  

<<<PAGE 9>>>
Mobile Campus Architecture Guide 
9 
 
On access ports, VLAN memberships are dynamically assigned according to specific rules set in a Network 
Profile (implicit from Access Role Profile Vlan mapping configuration). This means that VLANs will 
dynamically change depending on the type of device and the specific user connecting on a port. 
But for the switch to forward traffic on those dynamic VLANs, they need to be created on the switch and 
tagged on the uplink. Creating and tagging all possible VLANs is not recommended because this 
unnecessarily creates large L2 broadcast and STP domains which can lead to network scalability and 
stability problems.  
Multiple VLAN Registration Protocol (MVRP) solves this problem.  When user traffic is bound to a user 
VLAN on an access port according to the rules set in the UNP, the required VLAN is also dynamically 
created on the switch and tagged on the uplink (provided MVRP is enabled and the VLAN is known to the 
core-layer switch). 
This dynamic VLAN assignment in conjunction with MVRP solves the problem of user mobility whilst 
keeping broadcast and STP domains as small as possible, thus eliminating Moves, Adds and Changes. 
4.3.2 Trunking 
Trunking is a networking method that enables the transmission of traffic for multiple VLANs over a single 
network link, typically between switches or between a switch and a router. This is achieved using VLAN 
tagging protocols such as IEEE 802.1Q, where frames are tagged with VLAN identifiers, allowing the 
receiving device to correctly identify and process the traffic associated with each VLAN. 
A port can only be assigned to one untagged VLAN (in every case, this is the default VLAN configuration) 
but it can be assigned to as many 802.1Q-tagged VLANs as necessary. 
Trunking offers several key benefits. It allows for efficient use of bandwidth by enabling multiple VLANs 
to share a single physical link, reducing the need for separate cables for each VLAN. This optimization 
not only conserves bandwidth but also simplifies the overall network design by decreasing the number of 
inter-switch links required. The reduction in physical cabling complexity leads to easier management and 
maintenance of the network infrastructure. Additionally, trunking ensures consistent VLAN distribution 
across the campus, allowing devices to maintain their VLAN assignments as they move within the 
network. This consistency is crucial for maintaining network policies and ensuring seamless 
communication across different areas of the campus. 
4.3.3 Link Aggregation Control Protocol (LACP)  
Link Aggregation Control Protocol (LACP), as defined by IEEE 802.3ad, is a protocol that enables the 
combination of multiple physical network links into a single logical link, known as a Link Aggregation 
Group (LAG). This method, also referred to as "link bundling" or "port-channeling," increases available 
bandwidth and provides redundancy by automatically detecting and aggregating links between two 
devices. LACP balances traffic across these links and reroutes it automatically in case of a link failure. 
LACP plays a vital role by ensuring efficient and resilient connectivity. It increases bandwidth by 
combining multiple physical connections, which is essential for managing large volumes of traffic, 
particularly at the access layer. LACP also enhances redundancy and fault tolerance, as it provides 
automatic failover capabilities; if one link in the LAG fails, traffic is seamlessly redistributed across the 
remaining active links, maintaining network reliability, and minimizing downtime. Additionally, LACP 
simplifies network management by treating multiple links as a single logical connection, making 
configuration, and troubleshooting more straightforward. 
4.4 Shortest Path Bridging (SPB) 
Shortest Path Bridging (SPB), defined by IEEE 802.1aq, enhances mobile campus networks by providing a 
scalable and efficient networking solution. Utilizing the IS-IS protocol and MAC-in-MAC encapsulation, 
SPB creates a loop-free, multi-path topology that maximizes link utilization and optimizes traffic flow. 
This design ensures that all network paths are used efficiently and avoids congestion, crucial for 
supporting a high number of mobile devices and dynamic traffic patterns. 
SPB excels in mobile campus environments by supporting dynamic service instantiation. Integrated with 
Alcatel-Lucent Enterprise’s Access Guardian (AG) framework, SPB enables automatic provisioning and 
deprovisioning of services based on device or user classification. This capability facilitates seamless 
network adaptation for mobile users and devices, ensuring that network services are available when 

<<<PAGE 10>>>
Mobile Campus Architecture Guide 
10 
 
needed and secured against unauthorized access. The dynamic nature of SPB helps manage the mobility 
of users and devices without manual reconfiguration, thus enhancing user experience and network 
efficiency. 
Moreover, SPB’s support for native multi-tenancy allows for the creation of multiple virtual network 
segments or VPNs, isolating different user groups or IoT devices within the same physical infrastructure. 
This is particularly valuable in mobile campus settings where different user types may require distinct 
network services or security policies. 
The implementation of SPB is particularly beneficial in many use cases like data center, service provider 
networks, multitenant environment, industrial networks, IoT networks and more. For large campuses, it 
allows networks to scale efficiently with thousands of VLANs while simplifying management through a 
flat Layer 2 topology. This capacity to dynamically adapt to mobile users, manage traffic efficiently, and 
support extensive virtual segmentation is making it a highly effective solution for mobile campus 
networks, ensuring both performance and scalability in a dynamic environment. 
 
Shortest Path Bridging Architecture guide 
4.5 Ethernet VPN (EVPN)  
Ethernet VPN (EVPN) is a modern network technology that enables layer 2 connectivity over a layer 3 
network, enhancing the capabilities of traditional VPNs. It uses Border Gateway Protocol (BGP) for 
signaling, allowing it to distribute MAC address reachability information among Provider Edge (PE) 
devices efficiently. This setup facilitates the extension of VLANs across a wide area network, providing 
seamless layer 2 services over an IP/MPLS network without the complexity of managing extensive 
tunneling protocols or overlays. 
EVPN operates by leveraging BGP to advertise routes that incorporate both Layer 2 and Layer 3 
information, such as MAC addresses, IP addresses, and Ethernet tags. This method ensures 
comprehensive routing and bridging capabilities on a large scale. Additionally, the support of multi-
homing enables a customer edge device to connect to multiple provider edge devices, which enhances 
network availability and load balancing. 
The primary benefits of EVPN include its scalability and flexibility, supporting a vast number of MAC 
addresses and VLANs while carrying both Layer 2 and Layer 3 traffic. This flexibility is crucial for 
adapting to different network designs and deployment scenarios. Moreover, EVPN simplifies network 
management by centralizing control with BGP and provides enhanced redundancy and resiliency through 
its multi-homing feature, which ensures higher network reliability. 
EVPN offers numerous advantages for campus network deployments due to its security, scalability, and 
manageability. EVPN enables logical network segmentation that isolates and secures traffic for different 
user groups within a campus. Its support for multi-homing enhances network resilience and uptime, 
crucial for maintaining continuous operations. Additionally, EVPN simplifies network expansion and 
management, allowing campuses to dynamically adapt to growth and changes without increasing 
complexity. 
4.6 Multiprotocol Label Switching (MPLS) 
Multiprotocol Label Switching (MPLS) is an advanced networking technology that enhances data routing 
using labels, facilitating rapid and efficient data forwarding decisions across a network. Unlike 
traditional IP routing, which relies on complex network address lookups, MPLS assigns short path labels 
to packets at the ingress router, guiding them through predefined virtual paths to their destination. This 
labeling allows intermediate routers, known as label switch routers, to swiftly forward packets based on 
the label without inspecting the packet's payload, streamlining the routing process. 
MPLS brings several significant advantages to network management, chief among them being its ability 
to improve routing efficiency and quality of service (QoS). By simplifying the routing decisions to mere 
label inspections, MPLS reduces the processing burden on routers, thereby increasing network speed and 
reducing latency. Moreover, MPLS supports sophisticated QoS capabilities, allowing network operators to 
prioritize traffic types, such as real-time voice and video, ensuring their performance remains optimal 
across the network. 

<<<PAGE 11>>>
Mobile Campus Architecture Guide 
11 
 
Multiprotocol Label Switching (MPLS) offers significant benefits for traffic engineering, allowing network 
administrators the flexibility to route data via optimal paths tailored for specific traffic types or network 
conditions, crucial for managing bandwidth and improving latency-sensitive applications. Its protocol-
agnostic nature supports a broad array of network protocols, including IPv6, thereby enhancing 
scalability and future-proofing networks. Widely adopted across various sectors, MPLS is used by Internet 
service providers to deliver multiple services through a single connection, by enterprises to establish 
robust, scalable VPNs linking numerous branches and data centers, and within data centers to ensure 
reliable connectivity crucial for disaster recovery and service availability. 
In addition to its widespread use in various sectors, MPLS can also be effectively utilized in campus 
networks, particularly larger educational or corporate campuses. It enhances network management by 
optimizing traffic flow and prioritizing critical applications through advanced Quality of Service (QoS) 
policies. MPLS supports the creation of Virtual Private Networks (VPNs), enhancing network security by 
segregating sensitive traffic, and provides the scalability necessary for handling increased traffic as 
campus networks expand. Furthermore, its capabilities in ensuring network redundancy and fast 
rerouting contribute to enhanced reliability, making it a foundational technology in modern network 
architectures capable of meeting the diverse demands of today’s data traffic, including those specific to 
campus environments. 
4.7 Dynamic Routing  
Dynamic routing protocols are integral to modern campus network design, offering automated and 
adaptive routing solutions that enhance network scalability and efficiency. These protocols facilitate the 
dynamic adjustment of routes in response to network changes, thereby optimizing data paths and 
reducing the need for manual intervention. This section delineates the principal dynamic routing 
protocols used at the distribution and access layers, their operational mechanisms, and their benefits. 
4.7.1 Open Shortest Path First (OSPF)  
Open Shortest Path First (OSPF) is a link-state routing protocol that utilizes Dijkstra’s Shortest Path First 
(SPF) algorithm to determine the shortest path to each destination within a network. Each OSPF router 
constructs and maintains a Link-State Database (LSDB), which represents the network topology. This 
database is updated through Link-State Advertisements (LSAs), ensuring that all routers within an OSPF 
area have a uniform view of the network, thus enabling them to compute the most efficient routing 
paths. 
OSPF's hierarchical design, which organizes the network into areas and a backbone (Area 0), significantly 
enhances scalability, making it well-suited for large and intricate networks. The protocol’s ability to 
quickly recalculate routes in response to changes in network topology ensures minimal downtime and 
enhances overall network reliability. Additionally, OSPF offers flexible route optimization through 
configurable metrics, allowing for cost-based routing decisions that can be tailored to meet specific 
network performance and efficiency requirements. 
4.7.2 Border Gateway Protocol (BGP)  
Border Gateway Protocol (BGP) is a path-vector routing protocol primarily used for inter-domain routing 
across autonomous systems. BGP maintains a routing table that includes paths and associated attributes 
such as AS-path, next-hop, and prefix length. It exchanges routing information between peers to 
propagate updates and manage routing decisions based on these attributes. 
BGP's scalability is a key advantage, enabling it to handle a vast number of routes and interactions 
between diverse networks, making it essential for complex and expansive network environments. The 
protocol supports policy-based routing, allowing network administrators to implement extensive route 
filtering and policy controls, which enhances flexibility in route selection. Additionally, BGP's ability to 
evaluate multiple attributes for path selection enables optimized routing decisions tailored to specific 
network requirements and policies. 
In a campus network setting, BGP serves several critical functions. It is essential for establishing robust 
interconnections to the internet, managing connections to multiple Internet Service Providers (ISPs). This 
setup enhances network resilience and performance through strategic redundancy and effective load 
balancing. Furthermore, BGP is crucial in environments utilizing Ethernet VPN (EVPN), where it supports 
advanced routing and bridging capabilities. In such scenarios, BGP facilitates the segmentation of several 
types of traffic and services over a unified network infrastructure, enhancing security, traffic 

<<<PAGE 12>>>
Mobile Campus Architecture Guide 
12 
 
engineering, and scalability 
 
4.7.3 Intermediate System to Intermediate System (IS-IS) 
Intermediate System to Intermediate System (IS-IS) is a link-state routing protocol utilized within 
autonomous systems and is essential for managing large-scale network environments. Operating as an 
Interior Gateway Protocol (IGP), IS-IS enables routers, termed Intermediate Systems, to exchange 
topological information via Link State Packets (LSPs). These routers compile a comprehensive database 
that represents the network's topology from the collected LSPs. Utilizing Dijkstra's shortest path first 
(SPF) algorithm, IS-IS calculates the most efficient routes throughout the network, ensuring that each 
router retains an accurate and current map of the network structure. 
IS-IS is a protocol-independent routing protocol that supports both IPv4 and IPv6, ensuring robust 
interoperability in modern networks. Its rapid convergence capabilities also minimize disruptions from 
topology changes, enhancing network reliability and responsiveness. 
Large enterprise networks benefit from IS-IS due to its capability to interconnect extensive network 
segments efficiently and reliably. Internet service providers (ISPs) also favor IS-IS for managing routing 
within their core networks because of its proficient handling of complex routing scenarios and 
scalability. 
4.7.4 Routing Information Protocol (RIP)  
The Routing Information Protocol (RIP) is a distance-vector routing protocol that relies on a hop count to 
determine the optimal path to a destination. RIP routers broadcast their routing tables to adjacent 
routers, which update their own tables accordingly. Although RIP is simple to configure and widely 
compatible, making it suitable for smaller or educational networks, its reliance on hop count as the sole 
metric limits its effectiveness in larger or more complex network environments. Consequently, while RIP 
can be mentioned as an option, it is not recommended for advanced or expansive network setups. 
Refer to configuration guide for further information on those protocols 
5 Wireless Local Area Network (WLAN) 
A Wireless Local Area Network (WLAN) leverages high-frequency radio waves to enable connectivity and 
communication among devices without the use of physical cables. Operating primarily within confined 
spaces such as homes, educational institutions, office buildings, and laboratories, WLANs adhere to the 
IEEE 802.11 standards. These standards are comprehensive, outlining the protocols for data transmission 
and the management of wireless connectivity. 
At the heart of any WLAN is the wireless access point, which functions as the hub of wireless 
communications. The AP not only broadcasts the wireless signal but also manages the connection and 
communication with all wireless-enabled devices within its operational range, including advanced 
computing devices like laptops, smartphones, and tablets, as well as increasingly common IoT devices. 
The primary advantage of WLANs is their ability to support mobile connectivity, which eliminates the 
logistical and aesthetic constraints associated with wired networks. This mobility enhances user 
convenience by allowing seamless internet and network resource access without physical constraints, 
fostering greater productivity and user engagement in various settings. 
5.1 RF Planning 
RF (Radio Frequency) planning in WLAN networks is a critical process of designing and optimizing 
wireless access point deployment to ensure reliable, high-quality wireless coverage, capacity, and 
performance across a designated area. Effective RF planning maximizes network performance by 
addressing factors such as interference, coverage gaps, and signal overlap, leading to a seamless user 
experience. Using OmniVista in conjunction with Stellar APs provides a cohesive solution for achieving 
optimal RF design through planning, verification, and ongoing network management. 
ALE OmniVista "Floor Plan" application is an essential tool for WLAN RF planning, offering design 
capabilities that enhance the RF planning process from initial layout to ongoing adjustments. This tool 
allows administrators to simulate and visualize RF environments accurately, aiding in the prediction and 
verification of network performance. 

<<<PAGE 13>>>
Mobile Campus Architecture Guide 
13 
 
 
Figure 1: OmniVista Floor Plan feature 
5.1.1 Coverage Planning 
RF coverage planning begins with defining the areas that need wireless service, including both indoor 
and outdoor spaces. Using OmniVista, administrators can upload floor plans and simulate coverage to 
determine the necessary signal strength (measured in dBm) for adequate user experience. The 
application helps assess expected coverage per AP location, minimizing the likelihood of dead zones and 
identifying AP placements to achieve continuous, high-quality coverage throughout the environment 
5.1.2 Capacity Planning 
Capacity planning evaluates the network’s ability to support anticipated user, and device demands by 
considering factors such as location, usage patterns, and application types. ALE offers a diverse range of 
Stellar APs designed to meet various deployment needs, from high-density environments to smaller 
coverage areas. 
5.1.3 Frequency and Channel Selection and interference management.  
Frequency and channel selection are essential for minimizing interference and optimizing performance. 
Stellar APs support multiple frequency bands (2.4 GHz, 5 GHz, and 6 GHz) and uses its distributed 
control plan and OmniVista for channel management. The solution automates channel selection that 
minimizes co-channel and adjacent-channel interference, providing a proactive approach to RF spectrum 
management that adapts to changing network demands. 
5.1.4 AP Mounting, Placement and Density 
The physical placement of APs is critical to achieving optimal coverage and capacity. RF planning 
involves creating a layout that ensures even distribution of the wireless signal, avoiding areas of weak 
signal (dead zones) and minimizing areas of excessive overlap that could cause interference. 
Stellar APs can be mounted in various locations such as ceilings, walls, or indoor or outdoor poles, 
depending on the environment and coverage requirements. Ceiling-mounted APs are preferred in indoor 
settings for their ability to provide widespread, unobstructed coverage, while wall-mounted APs are used 
where ceiling installation is impractical, offering more directional coverage. Outdoor APs are typically 
mounted on poles or building exteriors to cover large open areas. 
The mounting hardware, including brackets, mounts, and enclosures, must be selected based on the 
installation surface and environmental conditions. The orientation and angle of the AP are crucial for 
optimal signal propagation, with proper alignment ensuring maximum signal strength and coverage. 
Adjustable antennas or mounting angles may be employed to fine-tune the coverage pattern. 

<<<PAGE 14>>>
Mobile Campus Architecture Guide 
14 
 
AP mounting also involves careful planning of network cable routing and power supply. Stellar APs 
leverage Power over Ethernet (PoE) for simplified installation, allowing flexible placement without 
extensive wiring, a feature also managed and monitored within OmniVista. This configuration enhances 
the deployment process by optimizing both the network’s functionality and its visual impact.  
5.1.5 Power and Antenna Configuration  
The transmission power of each AP and the type of antennas used (omnidirectional or directional) are 
configured based on the specific coverage needs of the environment. Proper power settings help in 
balancing coverage and minimizing interference. OmniVista enables granular control over these settings, 
allowing administrators to fine-tune AP power outputs and antenna alignment based on the unique 
characteristics of each deployment area. 
5.1.6 Predictive Planning and heatmap 
RF planning often involves conducting site surveys and using simulation tools to model the RF 
environment. This allows for the identification of potential issues and adjustments to the design before 
actual deployment. 
OmniVista enhances network planning with its "Floor Plan" application, which serves as a comprehensive 
design, verification, and troubleshooting tool specifically tailored for Stellar Wi-Fi networks. This 
application facilitates the strategic placement of Access Points to optimize wireless coverage. It offers 
both manual and automated capabilities for determining the most effective AP configuration and 
placement within a given location by simulating and assessing the potential Wi-Fi coverage.  
OmniVista also offers a Wi-Fi heatmap feature that provides live visualization of Wi-Fi coverage and user 
density across deployed WLANs. Once a wireless network is set up, the heatmap displays real-time 
insights into signal strength and distribution, allowing administrators to assess and optimize coverage 
areas. Color gradients represent the Wi-Fi signal’s reach and intensity across campus zones, helping to 
identify potential weak spots or areas with potential interference. Additionally, the heatmap displays 
user density by overlaying user locations and connection data, which enables administrators to monitor 
the load on access points and adjust placement or settings to better support high-traffic areas. This 
dynamic visualization supports efficient network management, ensuring reliable and robust Wi-Fi access 
for users throughout the coverage area 
 
Figure 2: OmniVista Wi-Fi Heatmap feature 
 
5.1.7 Radio Dynamic Adjustment 
The Alcatel-Lucent Enterprise OmniAccess Stellar WLAN solution and its distributed virtual controller 
employs advanced Radio Dynamic Adjustment™ (RDA) technology to dynamically manage radio 

<<<PAGE 15>>>
Mobile Campus Architecture Guide 
15 
 
frequencies and power settings, ensuring optimal network performance and reliability. This includes 
features like Dynamic Frequency Selection and Transmit Power Control (DFS/TPC), which automate 
channel selection and power adjustments to minimize interference from other spectrum users and 
optimize coverage. The solution’s distributed control plane allows for autonomous RF setting 
adjustments across APs, even those in different groups or VLANs, facilitated by 'over the air' and 'over 
the LAN' exchanges using the Neighbor Management Protocol. 
This protocol enables APs to share crucial RF context such as channel utilization and interference, 
empowering each AP to make informed decisions to enhance network efficiency. The auto-channel and 
auto-power processes further refine these adjustments by analyzing the local RF environment and 
neighbor feedback to select the best channels and power settings without disrupting connected clients. 
5.3 AP management, control, and data plane overview 
5.3.1 Centralized Management 
In a wireless LAN architecture, the centralization of access point management is essential for ensuring 
consistent and efficient network operations. The Alcatel-Lucent Enterprise OmniAccess Stellar WLAN 
solution exemplifies this approach by providing a centralized management function through the 
OmniVista Network Management System (NMS). This system, equipped with an embedded and secure 
web-based graphical user interface (GUI), allows for the streamlined administration of the entire 
wireless infrastructure, regardless of the deployment model, whether on-premises or cloud-based. 
Centralized management is critical for maintaining the integrity and performance of a wireless network, 
as it ensures that all access points (APs) are uniformly configured and monitored from a single interface. 
This approach not only simplifies the management process but also enhances network security by 
reducing the complexity of managing multiple devices individually. 
5.3.2 Distributed Control Plane 
A distributed control plane model represents the most advanced and efficient approach to designing and 
deploying robust wireless networks. Unlike traditional centralized controller-based architectures, which 
inherently suffer from various limitations such as single points of failure, traffic bottlenecks, and 
increased latency, a distributed control plane significantly enhances network performance, scalability, 
and resilience. 
The distributed control plane architecture decentralizes the control functions, dispersing them across all 
APs within the network. Each AP autonomously handles its control tasks while simultaneously 
communicating with neighboring APs to synchronize essential operations such as RF management and 
client roaming. This design not only eliminates the need for a dedicated controller but also addresses 
the critical issue of network reliability by removing the single point of failure associated with centralized 
control systems. In a distributed control environment, if one AP fails, the neighboring APs can 
dynamically adjust their settings, such as increasing transmit power, to maintain seamless coverage and 
minimize service disruption. 

<<<PAGE 16>>>
Mobile Campus Architecture Guide 
16 
 
 
Figure 3: OmniAccess Stellar Distributed Control Plane 
 
From an economic perspective, the distributed control plane reduces both capital expenditures (CapEx) 
and operational expenditures (OpEx). The absence of a centralized controller eliminates the substantial 
initial costs associated with controller hardware and the ongoing expenses related to its maintenance, 
power consumption, and cooling requirements. Moreover, because the distributed model scales naturally 
with the addition of new APs without necessitating additional controllers, it offers a more scalable 
solution for growing networks. 
In the context of future-proofing WLAN deployments, the distributed control plane architecture aligns 
with the evolution towards cloud-based wireless solutions. By eliminating the need for physical 
controllers and leveraging a cloud-centric approach, this architecture positions organizations to 
seamlessly integrate emerging technologies and expand their wireless infrastructure without the 
constraints imposed by traditional models. 
5.3.3 Data Plane: bridged or tunneled 
In a bridged data plane architecture, the wireless access point directly forwards traffic from wireless 
clients to the local Ethernet network without routing it through a central controller. The AP converts 
wireless frames (IEEE 802.11) into Ethernet frames (IEEE 802.3) and sends them directly to the network's 
switching infrastructure. This process is known as local forwarding or bridging. 
Network performances are enhanced by directly bridging most data traffic at the AP level, thereby 
bypassing the need to tunnel traffic through a central controller. This method significantly reduces 
latency, avoids potential throughput bottlenecks, and ensures that high-bandwidth, low-latency 
applications, such as voice and video over IP, operate efficiently.  
On the other hand, tunneling becomes advantageous in scenarios where heightened security or 
centralized management of specific traffic types is required. With Alcatel-Lucent Enterprise's WLAN 
solutions, it is possible to replace a traditional controller with a switch for tunneling purposes. This 
flexibility streamlines the transition from a controller-based architecture to a switch-based model, 
allowing deployment to proceed without altering existing VLANs or subnets. 

<<<PAGE 17>>>
Mobile Campus Architecture Guide 
17 
 
 
Figure 4: OmniAccess Stellar Traffic Tunneling  
 
When security policies demand centralized traffic inspection, tunneling effectively channels traffic 
through a central point, enabling consistent and comprehensive enforcement of security measures. This 
approach is particularly useful for managing guest traffic, which can be isolated from corporate traffic 
and directed solely to the internet, ensuring that sensitive internal data remains protected while 
maintaining robust control over external access. 
To tunnel the traffic ALE network solution relies on Layer 2 Generic Routing Encapsulation (L2 GRE) 
tunneling. An L2 GRE tunnel creates a Layer 2 overlay network that encapsulates and transports traffic 
over an IP network between two L2 GRE tunnel endpoints. This tunneling mechanism functions similarly 
to VXLAN in the OmniSwitch architecture. L2 GRE can also be associated with a UNP profile, making it 
part of the service structure. 
The L2 GRE tunnel is established by configuring an endpoint on both a tunnel access switch and a tunnel 
aggregation switch. Traffic received on the tunnel access switch is classified into a UNP L2 GRE service 
profile, which is mapped to the L2 GRE tunnel service. This profile identifies the device traffic that will 
be encapsulated with a GRE header and forwarded through the L2 GRE tunnel to the aggregation switch. 
When the tunneled traffic arrives at the tunnel aggregation switch, the GRE encapsulation is removed, 
and the traffic is forwarded to a VLAN domain, where it can access either the perimeter network or the 
Internet. 
Device traffic received on a UNP port is classified into a UNP profile through any Layer 2 or Layer 3 UNP 
methods for learning and authenticating users. The resulting profile must be mapped to an L2 GRE 
service, after which the traffic is encapsulated and tunneled to the aggregation switch through the 
corresponding L2 GRE tunnel. 
Alcatel-Lucent Enterprise WLAN technology offers the flexibility to dynamically choose between bridging 
and tunneling based on the Access Role Profile (ARP) assigned to users. This adaptability allows for the 
optimization of both performance and security within the same network, ensuring that the infrastructure 
meets diverse operational requirements. 
5.4 Management modes 
The OmniAccess Stellar WLAN solution can be deployed in different ways. 

<<<PAGE 18>>>
Mobile Campus Architecture Guide 
18 
 
 
Figure 5: OmniAccess Stellar Deployment Modes 
 
5.4.1 Wi-Fi Express 
Stellar Wi-Fi Express mode and is meant for smaller deployments. OmniAccess Stellar WLAN Access 
Points operate by default in Wi-Fi Express mode 
5.4.2 Wi-Fi Enterprise  
In the Wi-Fi Enterprise mode, the Alcatel-Lucent Enterprise OmniVista Enterprise Network Management 
System is deployed on-premises on top of the Access Points infrastructure to take care of management 
and configuration of all the APs for maximum scalability.  
5.4.3 Wi-Fi Cloud  
In Wi-Fi Cloud mode, OmniAccess Stellar Access Points are provisioned and managed by the cloud based 
OmniVista Cirrus Network Management System. OmniVista Cirrus is a scalable, resilient, secure cloud-
based network management for unified access offered as a subscription service. 
5.5 AP group 
Stellar AP Series devices are managed by AP Group. OmniVista does not manage individual APs. 
Creation of AP groups within a WLAN architecture enhances network management by allowing 
centralized configuration and policy enforcement. This method simplifies administration, as changes 
applied to a group are uniformly propagated to all APs within it, ensuring consistent performance and 
security across the network. 
Grouping APs streamlines management by enabling the application of unified policies for Quality of 
Service (QoS), access control, and security. This uniformity improves network stability and optimizes 
resource utilization, while also simplifying troubleshooting. Issues can be addressed at the group level, 
reducing resolution time and minimizing network downtime. 
Furthermore, AP groups support scalability, facilitating the integration of new APs without disrupting 
existing network performance. This organizational approach leads to a more efficient, reliable, and 
scalable WLAN infrastructure. 
5.6 RF profile 
The Radio Frequency (RF) Profiles application is used to define a wireless RF configuration for Stellar 
Access Point. 
An RF profile is crucial in WLAN design for optimizing APs performance. RF profile is to be created 
following the RF planning survey and is linked to an AP group. It sets parameters such as channel 
selection, transmission power, and bandwidth allocation, all of which are key to ensuring optimal 
coverage, minimal interference, and high data throughput. Proper channel selection reduces 
interference, transmission power levels balance coverage with minimal signal overlap, and bandwidth 
allocation impacts data rates.  

<<<PAGE 19>>>
Mobile Campus Architecture Guide 
19 
 
RF Profiles enable network administrator to ensure that transmit power and operating frequencies meet 
the requirements of global regulatory agencies and individual countries but can also be used to adjust 
the wireless parameters and functions according to real network environment to improve the user 
experience of wireless network. 
OmniAccess Stellar Wireless Fine-Tuning Best Practices 
5.7 AP to switch interface 
5.7.1 OmniSwitch 
Deploying OmniAccess Stellar in conjunction with OmniSwitch is highly recommended due to the 
significant advantages offered by this integrated solution. One of the primary benefits is the capability 
to manage the entire network through a unified management interface, which ensures seamless 
integration of both wired and wireless networks within the Alcatel-Lucent Enterprise ecosystem. The 
OmniVista Unified Policy Access Manager (UPAM) provides a centralized platform, facilitating streamlined 
management of network users across different access types. 
UPAM functions as a central RADIUS server, offering consistent access control and policy enforcement 
across the entire network. This unified management framework supports consistent application of guest 
and BYOD access policies, regardless of whether users connect via wired or wireless networks. This 
consolidation simplifies the network management process, reducing the complexity inherent in managing 
separate systems. 
On top of that the combination of OmniAccess Stellar with OmniSwitch also enhances operational 
efficiency by automating essential tasks such as automatic AP discovery, provisioning, and VLAN 
creation. This automation not only accelerates deployment but also increases network reliability by 
minimizing the risk of manual configuration errors. 
Furthermore, OmniVista UPAM strengthens network security and user management through advanced 
features like Access Guardian for network access control, mDNS, and UPnP relay, which enhance service 
discovery and device compatibility. Additionally, for guest access, OmniAccess Stellar with OmniSwitch 
enables secure tunneling of guest traffic, ensuring its isolation from corporate networks and adherence 
to security policies. 
5.7.2 Third-party switch 
In designing a robust and flexible network architecture, it is essential to consider the interoperability 
and integration capabilities of the chosen WLAN solution. The Alcatel-Lucent Enterprise OmniAccess 
Stellar WLAN solution is not only optimized for deployment with OmniSwitch infrastructure but is also 
fully compatible with third-party switches, or a hybrid network consisting of both ALE and non-ALE 
equipment. This flexibility is crucial in diverse and evolving network environments where existing 
infrastructures or specific operational requirements may dictate the use of multi-vendor solutions. 
From an architectural perspective, the OmniVista NMS, cornerstone of the OmniAccess Stellar WLAN 
solution in Wi-Fi Enterprise mode, provides a unified management platform that seamlessly integrates 
with a variety of network components. This unified management framework is designed to offer 
comprehensive oversight and control across both wired and wireless segments of the network, regardless 
of the underlying hardware. 
5.7.4 AP authentication (secure AP mode) and Trust Tag 
The "secure mode" authentication process for APs ensures that only trusted devices are allowed to 
connect and operate within the network. This mode provides an advanced level of security by 
implementing a multi-step verification process that involves the use of the IEEE 802.1x authentication 
framework, as well as device-specific identification through the Link Layer Discovery Protocol for Media 
Endpoint Devices (LLDP-MED). This process not only authenticates the AP but also securely integrates it 
into the network's management system. 

<<<PAGE 20>>>
Mobile Campus Architecture Guide 
20 
 
 
Figure 6: OmniAccess Stellar Authentication Secure Mode Flow 
 
 
The process begins with the AP sending an LLDP-MED Type Length Value (TLV) message, identifying itself 
as an AP. Upon detecting the AP on the User Network Profile (UNP) port, the switch automatically 
classifies the device into the "defaultWLANProfile" based on an LLDP rule within the UNP. The switch 
then transmits LLDP messages back to the AP, which include the Port VLAN ID (associated with the 
defaultWLANProfile) and the AP's location, as derived from the switch's system information. 
At this stage, the AP authentication is initiated. The switch sends an Extensible Authentication Protocol 
(EAP) "Identity Request" frame to the AP to trigger the authentication process. The AP responds with an 
EAP "Identity Response" frame, and the switch forwards this response to the 802.1x server for 
authentication. If the authentication is successful, the server returns an authentication success message, 
confirming that the AP is trusted. 
Once authenticated, the AP requests an IP address from the DHCP server, which also provides the IP 
address of the OmniVista via DHCP Option 138. The AP then establishes a connection with the OmniVista 
server using the Message Queuing Telemetry Transport (MQTT) protocol. After the AP is recognized as 
trusted, the OmniVista server transmits the necessary management information to the AP through the 
same MQTT connection, finalizing the secure integration of the AP into the network. 
The value of this "secure mode" lies in its robust authentication process, which ensures that only verified 
APs are granted access to the network, protecting against unauthorized devices. By using multiple layers 
of verification, including LLDP-MED for device identification and 802.1x for authentication, this mode 
offers a prominent level of security. 

<<<PAGE 21>>>
Mobile Campus Architecture Guide 
21 
 
On top of that if the AP authentication is successful, when a wireless client connects to the network, the 
AP begins sending DHCP traffic that is tagged with the VLAN associated with the client's SSID. The switch 
recognizes and trusts the VLAN tag from the AP's client traffic and attempts to match it with an existing 
VLAN on the switch, this method provided by ALE WLAN solution is known as Trust Tag. If the switch does 
not have a matching VLAN, it will automatically create the necessary VLAN to handle the AP's client 
traffic. 
The Multiple VLAN Registration Protocol (MVRP) then distributes this VLAN configuration—both the 
management VLAN for the AP and any static or dynamically created VLANs carrying client traffic—to 
neighboring switches within the network. This process establishes specific VLAN domains, ensuring that 
both untagged management traffic from the AP and tagged traffic from wireless clients are correctly 
forwarded through the wired network. 
OmniAccess Stellar Access Point authentication and deployment App 
Note 
5.7.5 VLAN interface 
In bridge mode, the AP serves as a bridge in the network architecture, providing the link between the 
wireless domain of the clients and the wired domain of the backbone network. In this case the AP 
transparently forwards traffic from wireless clients to the network infrastructure, enabling devices 
connected to the WLAN to communicate as if they were directly connected to the physical network. 
Each AP is configured with an untagged management VLAN that facilitates essential operational and 
administrative functions. The management interface of the AP acquires its IP address through DHCP on 
this VLAN, streamlining network management by enabling administrators to access the AP’s configuration 
and monitoring tools using standard protocols.  
For client data traffic, APs utilize tagged VLANs specified by the Access Role Profile of each client. This 
configuration segregates different types of traffic, such as separating guest traffic from internal 
administrative traffic, thereby enhancing network security and performance. This structured approach to 
VLAN management ensures that management traffic remains distinct from user data, supporting robust, 
secure, and efficient network operations. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

<<<PAGE 22>>>
Mobile Campus Architecture Guide 
22 
 
Quick Steps for Configuring AP Discovery in the VLAN Domain 
 
 
Figure 7: OmniAccess Stellar AP Discovery Vlan Domain Flow 
 
 

<<<PAGE 23>>>
Mobile Campus Architecture Guide 
23 
 
! Create the VLAN that will serve as the AP management VLAN on each participating 
switch in the network. 
-> vlan 125 name “AP Management VLAN” 
! Tag switch ports that connect to other switches with the VLAN. 
-> vlan 125 members port 1/1/24 tagged 
! Map the VLAN created in Step 1 to the built-in “defaultWLANProfile”. 
-> unp profile defaultWLANProfile map vlan 125 
! Configure any switch port that will connect to a Stellar AP device as a UNP 
bridge port. 
-> unp port 1/1/1 port-type bridge 
! If necessary, enable the UNP AP mode for the UNP bridge port. 
-> unp port 1/1/1 ap-mode 
! Enable MVRP for the switch to facilitate the propagation of the AP management 
VLAN and AP client VLANs. 
-> mvrp enable 
! Optionally disable authentication on the UNP port if authentication of the AP 
device is not required. 
-> no unp port 1/1/1 802.1x-authentication 
-> no unp port 1/1/1 mac-authentication 
! Optionally configure the QoS policy list, authentication flag status, or mobile 
tag status for the UNP profile. For the “defaultWLANProfile” some parameters cannot 
be modified. Only Mobile-Tag, Qos-policylist, Authentication are only allowed. 
-> unp profile defaultWLANProfile qos-policy-list qlist1 
-> unp profile defaultWLANProfile authentication-flag 
! Optionally configure the system name, system location, and port alias. The 
information from one or more of these settings is used to derive the AP Location 
information that is transmitted by the switch to the connected AP device. 
-> system name BWIAPS01 
-> system location BWI Airport Hotel 
-> interfaces port 1/1/1 alias BWI-AP01 
 
5.7.6 SPB interface  
ALE access mode is when OmniAccess Stellar AP is integrated into a SPB service domain. The process 
begins with ensuring that both the AP and its clients are recognized by the SPB domain when connected 
to a UNP access port. The AP device initiates communication by sending an LLDP-MED TLV packet, which 
identifies it as an AP. The first packet received by the UNP access port must also be this LLDP-MED TLV 
from the AP. Once the AP is detected, the switch responds by sending LLDP packets to the AP, providing 
details about the management SPB service (via LLDP Port VLAN ID TLV) and the AP’s location (via LLDP 
Proprietary TLV). The management SPB service is linked to the specific UNP profile associated with the 
AP device. 
The port to which the AP connects is configured as a UNP access port with AP mode enabled. A Layer 2 
profile is assigned to ensure LLDP control frames are processed as "peer." When the AP’s MAC address is 
detected on the port, any previously learned MAC addresses are cleared, prioritizing the AP’s address, 
and designating the port as an AP-detected port. Authentication features, such as 802.1X and MAC 
authentication, are enabled by default but can be disabled if not required. For client devices connected 
through the AP, these authentication mechanisms are bypassed, though other Layer 2 learning 
configurations—such as rule classification and SPB service profile assignment—can still be applied. 

<<<PAGE 24>>>
Mobile Campus Architecture Guide 
24 
 
The AP mode status of the port reflects the global AP mode setting at the time the port is configured, 
but it can be adjusted individually for each port if needed. 
Stellar AP devices are automatically assigned to the "defaultWLANAccessProfile," a built-in profile that 
uses a UNP LLDP classification rule to assign the AP to the appropriate SPB service. This profile serves as 
the management service for the AP and is permanent within the switch configuration, though its 
parameters can be updated as necessary. If changes are made to the default values of configurable 
attributes, the profile settings become visible in the configuration snapshot. 
For AP clients, service profiles within the SPB domain must be created with VLAN tags matching those of 
the client’s frames. Classification rules are then set up to direct this tagged traffic to the corresponding 
service profile. If no such rules are established, the AP client traffic defaults to the SPB System Default 
profile associated with the UNP access port. 
Quick Steps for Configuring AP Discovery in the Service Domain 
 
 
Figure 8: OmniAccess Stellar AP Discovery Service Domain Flow 
 
 
 

<<<PAGE 25>>>
Mobile Campus Architecture Guide 
25 
 
! Configure a Layer 2 profile with a “peer” action defined for 802.1AB control frames.
-> service l2profile “ap-SvcUnp” 802.1ab peer 
! Configure any switch port that will connect to a Stellar AP device as a UNP 
access port and assign the Layer 2 profile created. 
-> unp port 1/1/1 port-type access 
-> unp port 1/1/1 l2-profile ap-SvcUnp 
! Enable the UNP AP mode for the UNP access port. 
-> unp port 1/1/1 ap-mode 
! Optionally disable authentication on the UNP port if authentication of the AP 
device is not required. 
-> no unp port 1/1/1 802.1x-authentication 
-> no unp port 1/1/1 mac-authentication 
! Map SPB service parameters to the built-in “defaultWLANAccessProfile”. 
->unp profile defaultWLANAccessProfile map service-type spb tag-value 0 isid 
1000 bvlan 4000 
! Optionally configure the QoS policy list, authentication flag status, or mobile 
tag status for the UNP profile. For the “defaultWLANAccessProfile” some parameters 
cannot be modified. Only Mobile-Tag, Qos-policylist, Authentication are only 
allowed. 
-> unp profile defaultWLANAccessProfile qos-policy-list qlist1 
-> unp profile defaultWLANAccessProfile authentication-flag 
! Create UNP profiles mapped to SPB service parameters for learning AP client MAC 
addresses. 
-> unp profile spb10 
-> unp profile spb10 map service-type spb tag-value 10 isid 1010 bvlan 4000 
 
-> unp profile spb20 
-> unp profile spb20 map service-type spb tag-value 20 isid 1020 bvlan 4000 
! Create UNP classification rules to capture and assign tagged AP client traffic 
into the UNP service profile configured with a matching VLAN tag value. 
-> unp classification vlan-tag 10 profile1 spb10 
-> unp classification vlan-tag 20 profile1 spb20 
! Optionally configure the system name, system location, and port alias. The 
information from one or more of these settings is used to derive the AP Location 
information that is transmitted by the switch to the connected AP device. 
-> system name BWIAPS01 
-> system location BWI Airport Hotel 
-> interfaces port 1/1/1 alias BWI-AP01 
 
 
5.9 Roaming concepts 
Roaming refers to the seamless transition of a client device, such as a smartphone or laptop, from one 
Access Point to another within a Wi-Fi network without losing connectivity or experiencing significant 
delays. This is a critical feature in environments with multiple APs, ensuring continuous network access 
as the client moves throughout the coverage area. 
In an Alcatel-Lucent Enterprise Stellar deployment, roaming is always transparent and seamless to both 
the client and the network. With remarkably high roaming performances, delay-sensitive and persistent 
applications such as voice and video experience no interruption. 

<<<PAGE 26>>>
Mobile Campus Architecture Guide 
26 
 
Layer 2 roaming between APs facilitates a scenario where a roaming client retains the same VLAN and IP 
address upon associating with a new AP. This type of roaming occurs within the same subnet and involves 
standard Layer 2 learning processes that enable WLAN clients to seamlessly transition from one AP to 
another without IP address alteration. L2 roaming is a default feature that is always active. 
The process of roaming is dependent on the sharing of "client contexts" among adjacent APs enhanced by 
stellar distributed virtual controller capabilities, with decisions between Layer 2 and Layer 3 roaming 
based on the VLAN configurations of the client's originating ("home") and receiving ("foreign") APs. APs 
gain awareness of their neighbors through "over-the-air" and “over-the-LAN” communications, which 
serve to broadcast their respective management IP addresses on the wired network. This exchange 
enables APs to dynamically share client-specific contexts, containing critical information required to 
efficiently manage client transitions and maintain connectivity during roaming. This system ensures a 
cohesive and uninterrupted network experience as clients move spatially across the network landscape. 
 
Figure 9: OmniAccess Stellar Roaming Overview 
 
The roaming conditions for Stellar AP may be summarized as follows: 
Client Context exists 
on the new AP? 
Client Context WLAN service 
and Access Role Profile exist 
on new AP? 
                      
Client Context VLAN ID = 
VLAN ID mapped to the 
Access Role Profile on 
new AP? 
Roaming Results 
No 
- 
- 
No Roaming, 
new client 
Yes 
No 
- 
No Roaming, 
new client 
Yes 
Yes 
Yes 
L2 Roaming 
Yes 
Yes 
No 
L3 Roaming 
 
 

<<<PAGE 27>>>
Mobile Campus Architecture Guide 
27 
 
5.9.1 Fast Roaming 
Fast Roaming is an enhancement that accelerates the roaming process by pre-authenticating clients with 
neighboring APs before the actual handoff occurs. This minimizes the time spent transitioning between 
APs and reduces latency, which is particularly important for applications requiring real-time data 
transmission, such as VoIP or video conferencing. Fast roaming mechanisms, supported by OmniAccess 
Stellar, leverage protocols such as IEEE 802.11r and 802.11k, which streamline the handoff process by 
sharing the client’s security context between APs, enabling quicker reconnections, and reducing the 
likelihood of connection drops during the transition. 
 
Figure 10: OmniAccess Stellar Fast Roaming Flow 
 
5.9.2 Layer 2 Roaming 
L2 Roaming involves the client moving between APs that are part of the same IP subnet or VLAN. In L2 
roaming, the client retains its IP address because it remains within the same broadcast domain. The 
process is straightforward since the network does not need to perform additional operations to maintain 
the client’s session as it moves from one AP to another within the same L2 network. This type of roaming 
is typically faster and more efficient, as it does not require any changes to the client’s IP address or 
additional tunneling mechanisms 
5.9.3 Layer 3 Roaming  
L3 Roaming is more complex and occurs when a client moves between APs that belong to different IP 
subnets or VLANs. In this scenario, the client would ordinarily need to obtain a new IP address, which 
could disrupt ongoing sessions. To prevent this, OmniAccess Stellar APs use a Layer 2 GRE (Generic 
Routing Encapsulation) tunnel to maintain the client’s original IP address while facilitating the transition 
between the "home" AP (the AP where the client initially connected) and the "foreign" AP (the AP to 
which the client roams). This tunneling mechanism allows the client to roam across different subnets 
without needing to reauthenticate or renegotiate its IP address, thereby ensuring a seamless connection. 

<<<PAGE 28>>>
Mobile Campus Architecture Guide 
28 
 
 
Figure 11: OmniAccess Stellar L3 Roaming Overview 
 
5.10 SSIDs - VLAN pooling 
An SSID, or Service Set Identifier, is the network name that wireless clients see when browsing available 
networks. Although multiple Access Points (APs) within the same network may share the same SSID, each 
AP broadcasts a unique Basic Service Set Identifier (BSSID), which serves as a distinct identifier for each 
AP. The SSID helps guide users in selecting the appropriate network to connect to, and it can be 
configured with various security levels. 
Clients use the signal strength of detected BSSIDs to decide when and where to roam between different 
APs. As users move through the network, their devices will automatically connect to the AP that offers 
the strongest signal, ensuring a stable and reliable connection across the network's coverage area. 
Network administrators often prefer to limit subnet sizes to what is commonly known as a class C 
network, characterized by a subnet mask of /24 (255.255.255.0), which supports up to 253 devices per 
subnet. This size is considered optimal for managing network traffic and minimizing the broadcast 
domain. When further logical segmentation is needed, VLANs are utilized to divide the network and 
reduce broadcast traffic. 
A common method for managing large groups of wireless users involves grouping all users connected to a 
specific set of APs into a single VLAN. Each group of APs is then associated with a particular user VLAN. 
While this approach works well if the user count remains below the subnet limit and users do not need to 
move between AP groups, it becomes problematic in situations where large numbers of users congregate 
in a specific location, such as conference hall or large meetings room. 
To overcome these challenges, OmniAccess Stellar VLAN Pooling feature allows administrators to assign 
multiple VLANs to a designated Access Role Profile (ARP). T This flexibility allows network administrators 
to allocate users to existing VLANs within the enterprise. ALE advises using VLAN pools as the preferred 
method for managing user VLANs whenever multiple user VLANs are present in the network. 
5.11 Quality of Service (QoS) 
Quality of Service (QoS) in WLAN networks refers to the ability to prioritize and manage network traffic 
to ensure optimal performance for distinct types of applications, such as voice, video, and data. In an 
OmniAccess Stellar WLAN deployment, QoS is applied dynamically based on the role assigned to each 
user or device upon connecting to the network. This role not only determines the VLAN for the user but 
also defines the QoS policy that governs traffic prioritization, enabling specific treatment for several 

<<<PAGE 29>>>
Mobile Campus Architecture Guide 
29 
 
types of traffic. For instance, real-time applications such as voice and video are prioritized to ensure low 
latency and uninterrupted service. 
OmniAccess Stellar Access Points are WFA 802.11e WMM certified, allowing traffic to be categorized into 
four classes: Voice, Video, Best Effort, and Background. This prioritization ensures that delay-sensitive 
traffic, identified by the AP through the 802.1p or DSCP fields in the traffic headers, is placed into high-
priority queues and transmitted with precedence over lower-priority traffic. On the downstream (AP to 
device) side, the AP ensures that frames marked with higher priority are transmitted before lower-
priority frames. On the upstream (device to AP) side, devices use WMM to tag their traffic, allowing the 
AP to recognize and process the traffic based on its relative priority. 
In Wi-Fi Enterprise mode, the OmniAccess Stellar solution allows for customization of DSCP/802.1p to 
WMM queue mappings, ensuring seamless integration with existing wired LAN QoS policies. Additionally, 
built-in Deep Packet Inspection (DPI) technology enables real-time classification of applications, allowing 
network administrators to monitor traffic and enforce role-based controls through the Application 
Visibility and Enforcement feature. This ensures that business-critical applications receive the necessary 
bandwidth and priority. 
OmniAccess Stellar also offers the capability to define "bandwidth contracts" at the user/device role 
level or the SSID level, based on QoS policies. These contracts specify the upstream and downstream 
bandwidth limits for each user or SSID, ensuring that bandwidth is distributed equitably across users and 
devices. Furthermore, the system allows administrators to configure the maximum number of clients per 
band or per AP for specific SSIDs, which helps manage network performance in high-density 
environments. 
Multicast traffic management is a crucial aspect of QoS in WLAN deployments. OmniAccess Stellar APs 
utilize IGMP snooping to limit multicast traffic replication within the network, ensuring that only APs 
with active subscribers receive the multicast stream. Since multicast traffic is transmitted at lower 
broadcast rates, transforming multicast streams into unicast traffic can improve transmission efficiency 
by leveraging higher unicast data rates. However, this optimization is dynamically adjusted based on 
network load, reverting to multicast transmissions when channel utilization or the number of clients 
exceeds defined thresholds. This approach ensures that the network operates efficiently under varying 
conditions, maintaining high performance for all users. 
5.12 Specific use cases 
5.12.1 Wi-Fi Mesh 
Wi-Fi mesh networks are designed to extend the network without traditional cabling, offering a flexible 
and scalable solution for providing wireless service across extensive areas. 
The OmniAccess Stellar Auto Mesh feature markedly streamlines the deployment of mesh networks by 
automating the traditionally complex and manual configuration process. Within this automated 
framework, APs connected via a wired link to a LAN function as "mesh root" APs, while those without a 
wired connection operate as "pure mesh" APs. These APs are capable of broadcasting up to five WLAN 
services (SSIDs) for client association and can establish up to five direct Point-to-Multipoint connections 
with other APs. The overall mesh network configuration can encompass up to 16 APs, with any given 
transmission chain extending to a maximum of eight APs from a mesh root to the furthest mesh AP. 

<<<PAGE 30>>>
Mobile Campus Architecture Guide 
30 
 
 
Figure 12: OmniAccess Stellar Mesh Network 
 
Uses cases for mesh deployment scenarios where physical cabling is impractical or costly, and where 
network coverage needs to extend over broad or complex areas as per example a Camping site, Historic 
or listed buildings, outdoor Events and temporary setups.  
5.12.2 Wi-Fi Bridge (Point-to-Point) 
A point-to-point wireless bridge is a network configuration that uses wireless communication technology 
to connect two separate geographic locations without the need for physical cables.  
In point-to-point bridge mode, both access points are set up to function solely to bridge two distinct 
networks. This is especially useful in scenarios where a physical LAN cable connection cannot be 
extended between two points due to geographical constraints or infrastructure limitations. When 
configured in this mode, the access points forego the provision of regular WLAN services for client 
association. Instead, all radio links are aggregated to establish a robust point-to-point radio link. 
OmniAccess Stellar offers a specialized configuration known as the "bridge" mode, which is particularly 
effective for creating point-to-point wireless links between two separate network locations. This mode is 
implemented under the WLAN's Wi-Fi Enterprise configuration, utilizing two OmniAccess Stellar Access 
Points. 
To secure this wireless connection, the access points employ advanced encryption standards such as 
WPA2 or WPA3 Pre-Shared Key (PSK). These standards ensure the integrity and privacy of the data 
transmitted across the wireless bridge. By broadcasting a secure SSID configured with WPA2 or WPA3 
PSK, the point-to-point bridge mode not only facilitates the extension of network connectivity between 
remote sites but also maintains high-security standards to protect the network traffic. This setup is ideal 
for organizations needing to extend their network across buildings or other obstacles without the costs 
and physical restrictions associated with traditional wiring. 

<<<PAGE 31>>>
Mobile Campus Architecture Guide 
31 
 
 
Figure 13: OmniAccess Stellar Point-to-Point Network 
 
  
5.12.3 Remote Access Points 
Remote Access Points (RAPs) are a strategic solution designed to extend corporate network connectivity 
to remote sites, such as satellite offices, retail locations, or temporary event spaces. By utilizing RAPs, 
organizations can ensure secure and reliable access to their corporate network from remote locations, 
allowing for seamless connectivity as if the users were physically present in the head office. 
There are two primary methods for deploying OmniAccess Stellar RAPs depending if the OmniVista 
platform is located on-premises or in the cloud. 
Whether the NMS is OmniVista Cirrus or OmniVista Enterprise combine with the freemium account of 
OmniVista Cirrus. Each method provides a structured approach to establishing secure connections 
between remote sites and VPN termination server sitting in the corporate network. 
The Stellar AP initiates its startup process by connecting to OmniVista Cirrus, where it is identified by its 
MAC address. Once connected, OmniVista Cirrus delivers the necessary configuration, including the VPN 
server's public IP address, the VPN client IP address, and essential AP settings such as SSID and radio 
frequency parameters. Additionally, the IP address of the OmniVista Enterprise NMS server is provided. 
The Stellar AP then establishes a dual VPN connection: first with the VPN server, and subsequently with 
the OmniVista 2500 server. Upon establishing these connections, OmniVista 2500 sends its configuration 
to the RAP, which includes specific SSID and radio frequency settings. With both VPN tunnels securely in 
place, clients at the remote site can connect to the designated SSID and gain secure access to the 
corporate network while offering the possibility to offer remote users split tunnelling for direct access to 
the internet.  

<<<PAGE 32>>>
Mobile Campus Architecture Guide 
32 
 
 
Figure 14: OmniAccess Stellar Remote Access Point Overview 
 
 
5.12.3 Voice over WLAN 
Voice over WLAN (VoWLAN) is a critical application in enterprise wireless networks, enabling mobile 
communication through wireless devices over Wi-Fi. To ensure optimal performance and reliability for 
VoWLAN, specific architectural and configuration considerations are necessary. 
 
For VoWLAN, utilizing the 5GHz frequency band is highly recommended due to its robust performance 
and lower interference compared to the 2.4GHz band, offering more channels and enhancing voice 
transmission quality. By prioritizing 5GHz in RF management policies, networks can achieve more 
reliable voice communications with reduced latency and packet loss, crucial for real-time interactions. 
Capacity planning is also critical; limiting voice clients to 20-25 per Access Point (AP) ensures sufficient 
bandwidth and a stable 36 Mbps throughput, maintaining call quality even at peak times. 
Seamless roaming across APs is essential to prevent call drops as users move, necessitating the activation 
of supported roaming features on OmniAccess Stellar APs and the use of dedicated SSIDs for compatible 
devices to optimize transitions and performance. Proper antenna and channel selection, compliant with 
local regulations and designed to minimize interference, further secures clear communication paths. 
Additionally, meticulously crafted QoS policies prioritize voice traffic to reduce jitter and packet loss, 
vital for VoIP and real-time conferencing. Leveraging Stellar's Deep Packet Inspection (DPI) and 
application monitoring can also enhance voice service quality by ensuring traffic is both prioritized and 
monitored to meet performance standards. 
OmniAccess Stellar Voice over WLAN Design Guidelines 
5.12.4 Multimedia Consumer device – mDNS 
In various campus scenarios, devices need to share content, such as presenting from a laptop to a 
meeting room screen or streaming music from a phone to a Hi-Fi system. These devices use MDNS and 
SSDP protocols for discovery, but traditionally, both the source and destination must be on the same 
SSID, posing a security risk. This setup often involves guest or BYOD devices, which may introduce 
threats to the network. 
The Alcatel-Lucent Enterprise SSDP & MDNS Relay addresses this issue by allowing devices to discover 
each other across different subnets. This enables a firewall to inspect multicast traffic between subnets, 
preventing security threats from spreading.  
This solution also enhances user flexibility, allowing content sharing across different SSIDs without 
requiring users to be on the same network. The relay intercepts multicast messages and transmits them 
over an L2GRE tunnel to a multicast controller, linking source and destination devices securely. There 
are two scenarios regarding SSDP & MDNS relay.  

<<<PAGE 33>>>
Mobile Campus Architecture Guide 
33 
 
The gateway mode for quick and easy configuration and the responder mode which requires more 
configuration but allows for more precise control over which services are shared, enhancing security and 
management.  
In the first mode, the traffic from the edge switch is forwarded to the configured gateway switch. The 
gateway will replicate and forward the received mDNS and SSDP packets on all the VLANs, based on a 
pre-configured VLAN sharing list. 
 
Figure 15: OmniSwitch MDNS Mode Gateway 
 
Whilst in the second mode, Responder is running on an OmniSwitch core switch. The edge switches must 
be configured with type standard with the L2GRE tunnel with the remote tunnel endpoint IP address of 
the OmniSwitch controller configured as the responder. 
In this mode, the server policy and client policies are created independently and linked by the service 
rule. Service sharing rules define the criteria by which the Responder will decide which services 
(Services to share must be known in advance) can be shared with which client requests. 

<<<PAGE 34>>>
Mobile Campus Architecture Guide 
34 
 
 
 
Figure 16: OmniSwitch MDNS Mode Responder 
 
Both gateway and responder modes offer flexibility in network service sharing configurations and can be 
easily implemented through the Alcatel-Lucent OmniVista network management platform. OmniVista 
simplifies the configuration and management of these modes, providing a centralized interface where 
administrators can define VLAN sharing lists, set up L2GRE tunnels, and manage service sharing rules 
seamlessly. 
5.12.5 Asset Tracking 
The OmniVista Asset Tracking solution provides organizations with the capability to track, monitor and 
manage assets efficiently, offering precise insights into how these assets are located and utilized within 
a given environment. Traditionally, enterprises have had to rely on indirect methods such as feedback 
from users or speculative assessments to gauge asset usage. This approach often results in imprecise 
data and can lead to either under-procurement or over-procurement of necessary resources. However, 
with the Asset Tracking solution, each asset is tracked individually over time, providing valuable usage 
data that can be used to address current needs and anticipate future demands, enhancing operational 
efficiency and reducing unnecessary costs. 
OmniVista Asset Tracking solution leverages the existing Stellar infrastructure or can integrate with 
third-party WLAN systems that utilize APs with built-in Bluetooth Low Energy (BLE) interfaces. By 
utilizing BLE tags attached to assets, the solution enables real-time tracking, capturing location data and 
usage patterns. This data is sent to the cloud-based location engine where it is stored and analyzed over 
extended periods, allowing enterprises to identify trends and optimize asset allocation and management 
from a web app or a smartphone app. The assets being tracked can range from equipment such as 
medical devices, laptops, and wheelchairs, to vehicles like golf carts, or even personnel. 
By streamlining asset management and ensuring more effective utilization of resources, the Asset 
Tracking solution plays a crucial role in improving both operational performance and customer 
experiences within a campus. 

<<<PAGE 35>>>
Mobile Campus Architecture Guide 
35 
 
5.12.6 Stellar APs Downlink Port Capabilities 
PSE and PD on Wired ports (phone, etc.) 
Stellar Access Points come equipped with Power over Ethernet (PoE-PSE) capabilities, enabling them to 
not only receive power via Ethernet but also provide power to other connected devices through a 
downlink PoE port. This feature offers significant flexibility in network deployments by allowing the AP 
to power additional devices without the need for additional power outlets or complex cabling 
infrastructure. 
In the context of hospitality, such as in hotels or resorts, this feature can enhance guest experiences and 
operational efficiency. For instance, an AP installed in a guest room can power an IP phone, enabling 
seamless communication between guests and the front desk without the need for separate power 
sources. Additionally, in high-end suites or public areas, the same AP could power security cameras, 
providing enhanced security monitoring without adding extra wiring or requiring dedicated power lines.  
In such use cases, the flexibility provided by the PoE-PSE feature not only reduces the physical footprint 
of the network infrastructure but also contributes to a more streamlined and easily scalable network 
architecture. This capability is particularly valuable in dynamic environments like hotels or schools, 
where network demands evolve and expand frequently, making it essential to have adaptable, cost-
effective solutions. 
6 Network Management System (Enterprise/Cirrus) 
6.1 Introduction 
The OmniVista (OV) Network Management System provides cohesive management and network-wide 
visibility, increasing IT efficiency and business agility. The solution is available on-premises with OV 
Enterprise and in the cloud with OV Cirrus. It provides a full set of management tools for converged 
mobile campus. This single platform enables operators to easily provision, manage and maintain a 
unified Campus Mobile infrastructure with its network elements, alarms, unified access security policies, 
and virtualization. It also provides advanced network analytics for visibility into wired-wireless devices, 
IoT endpoints and applications, as well as predictive analysis for forward planning providing a network-
wide management system for the Alcatel-Lucent Enterprise network portfolio. 
ALE OmniVista Cirrus Network Management System 
ALE OmniVista Network Management System  
 
6.2 OmniVista Enterprise Deployment Modes (Standalone and High-Availability)  
OmniVista Enterprise can be deployed in both Standalone and High-Availability (HA) configurations, 
offering flexibility to meet different network requirements. In a Standalone deployment, a single 
instance of OmniVista operates independently, managing network functions without failover support. 
However, in more critical environments where uninterrupted service is essential, OmniVista can be 
deployed in a High-Availability setup, consisting of two virtual machines (VMs) designated as Node 1 and 
Node 2. In this configuration, one node functions as the Active OmniVista Server (Node 1), while the 
other serves as a Standby server (Node 2). In the event of a failure of Node 1, the system automatically 
shifts to Node 2, ensuring minimal disruption to network management. 
The High-Availability deployment of OmniVista can be configured using either Layer 2 (L2) or Layer 3 (L3) 
HA architectures, each with its own use cases, configurations, and limitations. 
In a Layer 2 HA configuration, both OmniVista Enterprise server VMs must reside within the same subnet. 
This architecture requires the configuration of a virtual Cluster IP address, which serves as the main 
point of communication for network devices. Both the Active and Standby nodes are accessed through 
this shared Cluster IP, making it possible for devices to maintain continuous communication with the 
Active node. If Node 1 (the Active node) fails, Node 2 automatically takes over as the new Active node, 
with devices seamlessly communicating with it through the same Cluster IP. A key advantage of the 
Layer 2 HA setup is its simplicity in transitioning from a Standalone deployment. When converting a 
Standalone installation to a Layer 2 HA configuration, the existing IP address of the Standalone server 

<<<PAGE 36>>>
Mobile Campus Architecture Guide 
36 
 
can be reused as the Cluster IP, ensuring that no additional reconfiguration of devices is needed after 
the conversion. 
In contrast, a Layer 3 HA configuration allows OmniVista Enterprise servers to reside on different 
subnets, each with its own unique IP address. In this architecture, network devices must be configured 
to communicate with both the Active and Standby nodes simultaneously, ensuring that in the event of a 
failover, devices can continue to function by automatically switching communication to the newly active 
node. While the Layer 3 setup offers geographic and network flexibility by allowing the two nodes to be 
on different subnets, it introduces some limitations. Certain features, such as sFlow, policy 
enforcement, and specific device management functions, are not fully supported in a Layer 3 HA setup. 
Moreover, for Layer 3 HA configurations, redundancy settings such as setting a Preferred Node must be 
made through the CLI admin menu and are required to ensure the proper functioning of the L3 HA 
environment. For more information refer to the OmniVista Installation and Upgrade Guide.  
6.3 AP Onboarding  
The onboarding process of Stellar AP in OmniVista is designed to simplify the deployment and 
management of wireless network devices within an organization. Upon initial connection to the network, 
the AP automatically reaches out to the OmniVista Cirrus Activation Server. This call-home process is 
authenticated by verifying the device’s serial number against the organization’s Device Catalog, ensuring 
that only registered devices are permitted to join the network. Once the AP is validated, it is issued the 
necessary certificates to establish a secure VPN connection with OmniVista, enabling encrypted 
communication between the device and the management platform. Following successful VPN 
establishment, the AP is registered, licensed, and automatically provisioned with the appropriate 
configuration templates, which include the network settings and policies defined for the AP group. 
7.3 Unified Access 
Security must be inherently integrated into the network infrastructure from the outset and consistently 
applied across all access modalities, whether wired or wireless. Security configurations at the network 
edge are dynamically applied based on "roles" assigned to each user or device, such as IP phones or 
wireless Access Points, rather than being statically linked to specific switch ports. 
Utilizing role-based network profiles, individuals or devices connecting to the network undergo 
authentication processes, after which a specific network profile is assigned. This profile delineates the 
assigned VLAN along with comprehensive network security protocols, including access control lists (ACLs) 
and Quality of Service (QoS) rules. This framework ensures that unique security measures are maintained 
consistently, regardless of the physical location of the user or device within the network. 
Embedded within the access layer switches and APs, a distinctive feature exclusive to Alcatel-Lucent 
Enterprise systems, known as the User Network Profile (UNP) or Access Role Profile (ARP), facilitates this 
advanced level of security customization. This feature underscores a sophisticated approach to network 
security, ensuring that adaptive, role-specific safeguards are in place to protect the integrity and 
functionality of the network environment. 
8 Security 
8.1 Network Access Control Solutions  
 
A Network Access Control (NAC) solution is a security framework designed to manage, monitor, and 
secure devices and users as they connect to a network by enforcing policies on access and device 
compliance. NAC solutions ensure that only authorized and compliant devices and users are granted 
access to network resources, thereby enhancing security, and maintaining control over network activity. 
For organizations deploying Alcatel-Lucent OmniAccess Stellar APs, access management can be 
efficiently achieved through the Alcatel-Lucent Unified Policy Authentication Management (UPAM) 
module included in OmniVista. UPAM serves as an integrated, in-house access management platform, 
specifically designed to complement Alcatel-Lucent OmniSwitch Ethernet switches and OmniAccess 
Stellar APs. This module encompasses a captive portal and RADIUS server, supporting multiple 
authentication protocols, including MAC-based authentication, 802.1X, and configurable captive portal 
access for guest and Bring Your Own Device (BYOD) users. Furthermore, UPAM allows for authentication 

<<<PAGE 37>>>
Mobile Campus Architecture Guide 
37 
 
against either its internal database or external sources such as Microsoft Active Directory, LDAP, or 
external RADIUS servers, thus providing a versatile solution to accommodate dynamic access control and 
comprehensive policy enforcement. 
In addition to UPAM, OmniAccess Stellar APs are also compatible with third-party NAC solutions using 
UPAM as a proxy or without, including Microsoft Network Policy Server (NPS), Aruba ClearPass, and Cisco 
Identity Services Engine (ISE). These integrations allow organizations to leverage their preferred NAC 
platform for secure authentication, access control, and policy compliance, ensuring that Stellar APs can 
adapt to diverse security infrastructures and requirements.  
OmniVista UPAM architecture Guide 
ALE & Cisco ISE Application Note 
ALE & Aruba ClearPass Implementation Guide 
8.2 Role-Based Access and Access Role Profile (ARP) 
Security must be inherently integrated into the network infrastructure and applied consistently across all 
access methods, whether wired or wireless. Rather than being tied to a specific switch port, security 
settings at the network edge are applied dynamically to each user or device based on predefined "roles." 
These roles assign security policies to devices such as IP phones or wireless Access Points, ensuring that 
security settings are tailored to the specific needs of each user or device. 
Upon connecting to the network, users and devices are authenticated, and a role-based network profile 
is assigned. This profile defines the VLAN and includes all relevant security configurations, such as access 
control lists (ACLs) and Quality of Service (QoS) rules. This approach ensures that security policies are 
consistently applied, regardless of the physical location of the user or device within the network. A 
distinctive feature of the Alcatel-Lucent Enterprise solution is the integration of the User Network 
Profile (UNP for OmniSwitch) or Access Role Profile (ARP for Stellar) within the access layer switches and 
Access Points. This allows for flexible and dynamic application of security policies, ensuring that users 
and devices maintain appropriate security protections throughout the network. 
 
Figure 17: Alcatel-Lucent Enterprise Access Role Profile 
 
8.2.1 Access Guardian 
Access Guardian, implemented within OmniSwitch & Stellar equipment, represents a comprehensive 
access control framework that melds authentication with access control functionalities to offer a 
proactive network security solution. This framework is embedded within both the hardware and software 

<<<PAGE 38>>>
Mobile Campus Architecture Guide 
38 
 
components of the network devices, enabling administrators to effectively authenticate users and 
manage their access privileges across the network. 
The policies under Access Guardian are designed with significant flexibility, allowing for a uniform 
configuration across all access ports on a switch or WLAN networks. This uniformity ensures that devices 
can be connected, disconnected, and relocated between ports without disruption; appropriate VLAN 
settings and other configurations are dynamically applied regardless of the port used. Such a setup not 
only simplifies network management but also enhances security by ensuring consistent policy 
enforcement across the network. 
Furthermore, Access Guardian plays a crucial role in the integration of wireless and wired network 
infrastructures. It facilitates the detection, learning, and management of OmniAccess Stellar APs when 
they connect to an OmniSwitch. Traffic from wireless clients is seamlessly forwarded from the APs to the 
OmniSwitch and then onto the wired network, creating a unified access solution that bridges wireless 
and wired environments.  
8.3 Authentication  
Authentication, broadly, is the process of verifying the identity of a device or user. within the network is 
achieved through integration with a RADIUS server, which can either be an external server or the 
embedded UPAM server within OmniVista. This setup is pivotal for validating device credentials and 
ensuring that only authorized devices gain access to network resources. Stellar and OmniVista offer the 
organization different authentication methods to suit any WLAN deployment and needs.  
UPAM workflows provide a guided, wizard-based approach for deploying authentication policies, 
addressing the three most common network authentication scenarios: BYOD access, guest access, and 
MAC or 802.1X authentication. Through a step-by-step process, these workflows enable unaccustomed 
users to efficiently and swiftly configure the necessary policies to implement their desired 
authentication methods, thereby streamlining the deployment process and reducing the time required. 
While workflows offer a simplified and user-friendly option, they are optional, as more experienced 
users have the flexibility to manually configure the policies and strategies according to their specific 
requirements. 
 
8.3.1 IoT fingerprinting/MAC 
As the number of IoT devices continues to increase across businesses, ensuring their secure and seamless 
integration into the network is essential. IoT fingerprinting authentication allows organizations to 
identify and authenticate IoT devices based on their unique network behavior and characteristics, such 
as device type, MAC address, and traffic patterns. This form of authentication is particularly beneficial 
in environments where many different IoT devices, such as smart thermostats, security cameras, or 
point-of-sale systems, are connected to the network. 
Through IoT fingerprinting, the network can automatically recognize the device as a trusted entity, 
preventing unauthorized devices from accessing sensitive information or network resources. This method 
helps in avoiding the manual configuration of each device while maintaining robust security. IoT 
fingerprinting is ideal for industries like healthcare, where many medical devices must connect to the 
network without disrupting service or compromising security. 
8.3.2 Employee 
In a corporate setting, the network must ensure that employees can easily and securely access the 
resources they need, whether from a corporate office, remote location, or on-site. This seamless access 
is facilitated by solutions such as 802.1X.  
802.1x uses an authentication server, such as a Radius server, to authenticate users or devices before 
granting access to the network. This ensures that only authorized devices are allowed onto the network 
and helps to prevent unauthorized access and security breaches. 
One of the most used authentication sources used today is Microsoft’s Active Directory.  Using UPAM as 
the central source for authentication requests via RADIUS, it is possible to map the final ARP to an LDAP 
(or AD) field.  Multiple mapping conditions can be declared to produce granular differentiation between 
users and chosen policies. 

<<<PAGE 39>>>
Mobile Campus Architecture Guide 
39 
 
Once the device is authenticated and granted access, the communication between the device and the 
network is encrypted using protocols like WPA2 or WPA3. This ensures that data transmitted over the 
WLAN is secure, protecting sensitive corporate information from unauthorized interception or 
eavesdropping. 
WPA3 is preferred when higher security is a priority, particularly in environments where sensitive data 
might be transmitted over the network. It provides more robust encryption than WPA2, offering 
protections against offline dictionary attacks and implementing "Simultaneous Authentication of Equals" 
(SAE). SAE ensures that each user's session is uniquely encrypted, even if a shared password is used. This 
individualized encryption enhances security, making it difficult for attackers to exploit shared 
credentials. 
despite WPA3 offering stronger security features. WPA2 is widely supported by nearly all Wi-Fi-enabled 
devices, including older equipment, ensuring compatibility across a diverse range of devices without 
requiring costly upgrades. 
8.3.3 Guest  
Guest authentication is essential for organizations that want to provide visitors, such as business 
partners, clients, or customers, with temporary network access. While offering guest access, companies 
often want to restrict the duration and extent of access to ensure that guests cannot access internal 
corporate resources. OmniVista simplifies the creation of guest accounts and provides flexibility in how 
these accounts are authenticated. 
There are several ways for guests to authenticate, ensuring compatibility with various network policies 
and use cases. For instance, guests can self-register via the embedded Captive Portal, allowing them to 
create their own network access accounts without any intervention from staff.  
In addition to self-registration, organizations can enable social media logins (e.g., Facebook, Google, 
Rainbow, WeChat), which provides a familiar and convenient method for users to authenticate using 
their existing social media credentials. This can be particularly useful in environments like hotels or 
cafes, where visitors may prefer quick access without the need for manual account creation. 
Further flexibility is provided through "Self-registration Sponsored by Corporate Employee or Guest 
Operator." This method allows guests to create their accounts autonomously, but approval from a 
corporate employee or designated guest operator is required to authorize network access.  
Additionally, "Self-registration with SMS – Plivo" enables the guest to receive login credentials via an SMS 
message, ensuring easy access while maintaining secure authentication. 
By default, OmniVista retains guest records for one month, though external log servers can be configured 
to store records for longer durations based on organizational needs or regulatory requirements. This 
versatility in guest authentication is particularly valuable, where managing visitor access and ensuring 
security while offering convenience is a top priority. 
In terms of encryption, some guest networks the most used encryption standards include WPA2, WPA3, 
and Enhanced Open. 
Enhanced Open is used for guest networks when ease of access is the primary concern, and user 
authentication is not required. It automatically encrypts data between the user’s device and the access 
point without the need for a password, providing encryption like WPA2 but without requiring user 
credentials. This is ideal for environments such as cafés, airports, or public spaces, where the goal is to 
offer easy access to guests while still maintaining some level of security. 
WPA3 is an ideal choice for guest networks where security is paramount, such as in corporate or 
healthcare environments, but it may require newer hardware or device compatibility, which could limit 
its use for guests with older devices. 
Finally, WPA2 is often used for guest networks because it provides a good balance of security and ease of 
implementation. 

<<<PAGE 40>>>
Mobile Campus Architecture Guide 
40 
 
8.3.4 SSID 
SSID-based authentication relies on the configuration of specific network segments (SSIDs) to determine 
access levels. This is commonly used in both enterprise and educational settings, where different SSIDs 
are configured for various groups of users, such as students, faculty, or staff in educational institutions, 
or employees and visitors in a business setting. Each SSID may have different security settings, VLANs, 
and access controls, depending on the level of access required. 
For example, in a university setting, the SSID "Faculty" might allow access to internal academic resources 
and research servers, while the SSID "Student" may restrict access to only general internet resources or 
specific student portals. The SSID configuration helps ensure that users are placed on appropriate 
network segments based on their role or function within the organization. This is also beneficial in 
environments like healthcare, where staff and patients are separated into different network segments to 
protect sensitive patient data while providing internet access to guests. 
SSIDs can also be used in conjunction with additional authentication methods, such as 802.1X or WPA2-
Enterprise, to enforce robust security measures for specific groups or locations. This multi-layered 
approach ensures that only authorized users can access the intended resources, while maintaining 
flexibility for diverse types of users or devices on the network. 
8.3.5 BYOD 
Bring Your Own Device (BYOD) is a policy that enables an organization to implement a network access 
strategy for external devices. Device authentication or authorization encompasses two categories: 
corporate-issued devices and external devices. Corporate devices, issued by the company, have known 
hardware configurations and contents. These devices can be pre-provisioned in the Unified Policy Access 
Management (UPAM) system to assign a specific Access Role Profile upon network connection. Such 
devices may have unique Access Role Profiles, granting individualized network access rights, although 
multiple devices can share the same profile if desired. 
In contrast, external devices have unknown hardware configurations and software contents. For these 
devices, a different strategy may be required, such as restricting their network access, even when used 
by a corporate user. 
An Access Role Profile can be defined for BYOD devices that complies with the company’s security 
policy, allowing users to access the network using their preferred or personal devices. This scenario may 
arise in cases where the organization does not provide corporate devices but allocates a budget for 
employees to purchase their own. 
In such instances, users can declare their devices through a dedicated login page, utilizing UPAM’s 
Captive Portal functionality, to gain network access. Devices registered in this manner may be subject to 
additional restrictions, such as time limits on network access and session timeout values. The number of 
devices a user can register may be configured, typically ranging from 1 to 10 devices per user. 
As with all authentication methods in UPAM, the Authentication Source can be selected from UPAM’s 
local database, an Active Directory (AD)/LDAP) server or proxied to an external RADIUS server. 
Additionally, administrators have the capability to monitor the devices currently connected to the 
network, as well as those recently declared for network access 
8.4 Quarantine Manager 
The Quarantine Manager application of OmniVista enables the network administrator to quarantine 
devices to protect the network from attacks. The application works with like an external Intrusion 
Prevention System but with Alcatel-Lucent Enterprise AOS switch or AWOS Stellar APs, which sends 
either a Syslog message or SNMP trap to Quarantine Manager containing the IP or MAC address of the 
offending device. (If an IP address is received, Quarantine Manager uses its Locator function to 
determine the device's MAC address.) These messages trigger Quarantine Manager Rules. Depending on 
the rule that is written for the event, the device can be immediately quarantined or placed on a 
Candidate List that can be reviewed by the Network Administrator for further action. 
The application also includes the optional Quarantine Manager Remediation (QMR) feature. QMR is a 
switch-based application that interacts with Quarantine Manager to restrict network access of 
quarantined clients and provide a remediation path for these clients to regain their network access. 

<<<PAGE 41>>>
Mobile Campus Architecture Guide 
41 
 
 
Figure 18: OmniVista Quarantine Manager Feature 
 
8.5 Web Content Filtering (WCF) 
Web content filtering is a technology used to monitor and block access to web content deemed 
inappropriate, harmful, or unsafe within a network environment. This technology is primarily employed 
to enhance cybersecurity, ensure compliance with regulatory requirements, and maintain productivity in 
workplace or educational settings. 
Web content is typically filtered based on a variety of criteria to ensure security and appropriateness 
within a network. This includes blocking specific URLs known to host malicious or inappropriate content, 
which helps prevent access to potentially harmful websites. Content filtering also involves scanning for 
keywords or phrases that might indicate banned or undesirable content, allowing for the regulation of 
information based on textual analysis. Furthermore, filtering can be categorized by types of websites, 
such as those related to adult content, gambling, social media, or gaming, which organizations may 
deem inappropriate for their network environments. 
The OmniVista UPAM Web Content Filtering (WCF) can be configured to allow/deny client access through 
Stellar APs to web sites based on specific security or content conditions. When a client tries to access a 
restricted website, the page will fail to load, and the browser will display an error. A single WCF profile 
can contain multiple filtering conditions. To configure Web Content Filtering on an AP, you create a WCF 
Profile, configure an Access Role Profile or SSID with the WCF Profile, and then apply the Access Role 
Profile or SSID to APs. 
8.5 Wireless Intrusion Prevention System (WIPS) 
A Wireless Intrusion Prevention System functions at Layer 2, or data link layer. WIPS can detect rogue or 
improperly configured devices and prevent their operation within wireless enterprise networks. It 
achieves this by continuously scanning the network's radio frequencies to identify and mitigate potential 
security threats.  
The Alcatel-Lucent Enterprise OmniAccess Stellar WLAN solution incorporates wireless Intrusion 
Detection and Prevention (wIDS/wIPS) capabilities, reducing the need for additional hardware by 
allowing APs to both serve clients and mitigate wireless threats simultaneously. This integration 
enhances security by analyzing and correlating 802.11 frames in real-time, a capability superior to 
traditional overlay deployments. The system actively monitors the wireless spectrum to detect unsafe 
APs or clients, enabling proactive countermeasures against potential intrusions. 
Two main types of foreign APs can negatively impact the wireless network: interfering APs and rogue 
APs. An interfering AP is visible within the wireless environment but is not connected to the wired 

<<<PAGE 42>>>
Mobile Campus Architecture Guide 
42 
 
network. While it may cause RF interference, it is not considered a direct security threat. However, such 
APs can degrade network performance by interfering with legitimate client connections. A rogue AP, on 
the other hand, poses a significant security threat. This can occur when an unauthorized AP is physically 
connected to the wired network or when a foreign AP broadcasts an SSID that mimics one from the 
authorized WLAN network. In such cases, the MAC address of the rogue AP can be identified in the 
Forwarding Database of the monitoring AP. 
If an AP is classified as rogue, and containment is enabled (default is disabled), the detecting AP will 
send DEAUTH frames to clients associated with the rogue AP, effectively preventing them from 
connecting to the compromised network.  
In Wi-Fi Enterprise mode, the OmniAccess Stellar solution enables the creation of flexible policies for 
detecting and responding to AP-based wireless attacks. Upon detection, details of the attack are 
displayed for further review and action. Additionally, the system can respond to client-based wireless 
attacks by automatically blacklisting compromised clients, preventing them from associating with the 
network through the wIDS/wIPS application. 
 
9 Reference documents 
Architecture Guide 
OmniVista UPAM Architecture Guide 
Network Infrastructure Solutions Security Guide 
EVPN Architecture Guide 
MPLS Reference Design Guide 
Shortest Path Bridging Architecture Guide 
Data Centre Reference Design Solution Guide 
Application Note: 
Alcatel-Lucent Enterprise & Cisco ISE Application Note 
Alcatel-Lucent OmniVista UPAM and Fortinet Single Sign-On Application Note 
OmniVista IoT Inventory Integration with Google Workspace Application Note 
Augmented Intelligence and Device Fingerprinting Enabled Networks Application Note 
Guest Traffic Tunnelling Services Application Note 
OmniVista UPAM and Palo Alto Networks User-ID Application Note 
Alcatel-Lucent Enterprise & Aruba Clearpass Application Note 
OmniAccess Stellar Access Point Authentication and Deployment Application Note 
 
Technical Tips: 
OmniAccess Stellar Wireless Fine-Tuning Best Practices 
Layer 2 Generic Routing Encapsulation – L2GRE 
OmniAccess Stellar Bridging/Multi-Point Meshing GuidelinesVirtual Extensible LAN 
Using Alcatel-Lucent OmniVista UPAM RADIUS Server with third-party switches 
OmniAccess Stellar High Density Design Guidelines 

<<<PAGE 43>>>
Mobile Campus Architecture Guide 
43 
 
 
10 Conclusion 
To summarize, this Mobile Campus Architecture Guide presents a comprehensive framework for 
establishing a robust, secure, and scalable mobile campus network architecture. This architecture is 
vital for a variety of environments, including educational institutions, corporate offices, healthcare or 
governmental facilities, and public venues. By combining centralized and distributed management, 
seamless roaming capabilities, and advanced security measures, organizations can ensure reliable and 
efficient connectivity across their campuses. 
Alcatel-Lucent Enterprise OmniSwitch, OmniAccess Stellar and OmniVista solutions are specifically 
designed to provide the flexibility and comprehensive control needed to adapt to evolving technology 
landscapes and the diverse demands of users. As digital transformation continues to reshape how we 
connect and communicate, establishing a resilient network infrastructure becomes crucial for all sectors. 
This architecture guide not only addresses current operational needs but also establishes a future-proof 
foundation capable of integrating emerging technologies, meeting stringent security requirements, and 
promoting an adaptable, high-performance network. 
By prioritizing these principles and leveraging Alcatel-Lucent Enterprise's innovative solutions, 
organizations can cultivate an agile network that supports enhanced user experiences, improves 
operational efficiency, and remains competitive in an increasingly interconnected world. Embracing this 
robust mobile campus network infrastructure will enable organizations to not only meet present 
challenges but also seize future opportunities. 


<<<DOC 2: ale-hybrid-pol-solution-brochure-en.pdf | 起始页 44 | 4p>>>

<<<PAGE 44>>>
Hybrid Passive Optical LAN  
for business critical network
Alcatel-Lucent Enterprise Hybrid POL is a mixed architecture  
that takes advantage of Passive Optical LAN and Ethernet  
LAN to provide cost savings and better network performance.
Brochure
Hybrid Passive Optical LAN for business critical network

<<<PAGE 45>>>
Brochure
Hybrid Passive Optical LAN for business critical network
2
Alcatel-Lucent Enterprise Hybrid POL solution
Alcatel-Lucent Enterprise Hybrid POL (Passive Optical LAN) solution leverages a single fiber link to deliver 
enterprise services with high bandwidth and low latency to large customer premises across long 
distances. Hybrid POL solution connects the core and the access layers of an ALE Ethernet LAN through 
a Nokia POL infrastructure, with one or several split levels.
For customers with large premises and demanding networking services, Hybrid POL results in an 
optimization of the cabling and active equipment infrastructure, while retaining all the Ethernet services  
for enterprises.
State of the art networking 
services
The access switches at the edge of the 
POL provide for LAN networking services, 
and for higher IP port density and HPoE 
budget where needed. The option of 
redundant uplinks in the switches makes 
the network redundancy possible at all 
network layers.
Hybrid POL benefits
Easy network management
Centralized management for both POL 
and Ethernet LAN with the Nokia & Alcatel-
Lucent Enterprise network powerful and 
user-friendly management systems.  
Provides highly scalable network 
evolution capabilities. 
Cabling reduction
The use of Optical Network Terminals 
(ONTs) and small-factor access switches 
at the POL edge, which can be installed 
closer to the endpoints, leads to a 
reduction of the copper cabling 
horizontal runs, and eliminates the 
need of dedicated telecom closets  
and cooling systems. 
Last generation Wi-Fi for enterprises
The OmniAccess Stellar WLAN access points 
provide enterprise-grade Wi-Fi with the latest 
Wi-Fi standards supported in top of the POL.
Infrastructure cost savings
The point-to-multipoint optical 
infrastructure leads to the removal of 
the distribution switching layer in 
dense installations, with the consequent 
reduction of costs in switching 
infrastructure. 
Superior performance, optimized infrastructure

<<<PAGE 46>>>
3
Brochure
Hybrid Passive Optical LAN for business critical network
.
Do you need Hybrid POL? 
ALE HPOL is the ideal solution for enterprises and organizations with large premises. Typically  
for networks in one or several buildings, over long distances, for medium to high user density,  
and with advanced networking and Wi-Fi requirements.
Large installations
Customers with large and 
extra-large premises, in one 
or several buildings, and long 
distances, require an optimization 
of the underlying network 
infrastructure.
Hybrid POL 
benefits
Reduces installation 
and maintenance costs 
with less cabling and active 
equipment.
High performance
Customers with high density  
of users, applications and IoT 
devices have demanding  
requirements regarding  
bandwidth, reliability,  
security and services.
Hybrid POL 
benefits
Guarantees evolution from 2.5 Gbps 
to 10/40 Gbps networks. Imple-
ments state-of-the-art security 
standards and advanced networking 
services, with full redundancy at 
all network levels.
Enterprise grade 
Wi-Fi
Customers needing perva-
sive Wi-Fi, capable to support 
real-time applications, with 
high performance in dense 
environments and high-quality 
outdoor coverage.
Hybrid POL 
benefits
Supports Wi-Fi 5 and Wi-Fi 
6, with an efficient Wi-Fi 
backhaul today and in the 
future.
Recommended architectures
Nokia POL solution (with SFP ONT) 
combined with Alcatel-Lucent OmniSwitch access  
switches and OmniAccess Stellar access points. 
Nokia POL solution (with ONT) 
combined with OmniAccess Stellar  
access points. 
Full redundancy at all network layers
Advanced networks features (SPB, ERP, MACsec etc)
Unified access
PoE/PoE+ and Hi-PoE
High IP port density
IoT enablement, management and inventory
Redundancy at all network layers is not required
Basic network features
Unified access is not required
Only PoE/PoE+
Low IP port density
IoT connectivity

<<<PAGE 47>>>
Alcatel-Lucent Enterprise
Hybrid POL key 
differentiators
Combined benefits
•	 Future-proof fiber investment
•	 LAN and WLAN enterprise-grade features
•	 Redundancy possible at all layers
•	 Flexible and scalable design
•	 Centralized management
Cost savings
•	 Active equipment, fiber and copper  
cabling optimization
•	 Power consumption and real estate  
space savings
Single vendor for  
end-to-end solution
The most complete offer  
in the market combining 
Alcatel-Lucent Enterprise  
and Nokia technologies
© 2023 ALE International, ALE USA Inc. All rights reserved in all countries.  
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by 
ALE. To view a list of proprietary ALE trademarks, visit: www.al-enterprise.com/en/
legal/trademarks-copyright. DID23100302EN (October 2023)
