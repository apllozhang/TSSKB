<<<PAGE 1>>>
OMNISWITCH GOLDEN RFP - 8.10R4

<<<PAGE 2>>>
OmniSwitch 6360 — Golden RFP — Page 1

<<<PAGE 3>>>
OmniSwitch 6360 — Golden RFP — Page 2
Golden RFP – OS6360
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.7
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.8
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.9
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.10
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.11
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.12
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.13
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.14
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 8 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC

<<<PAGE 4>>>
OmniSwitch 6360 — Golden RFP — Page 3
2.5
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.6
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.7
Virtual chassis
Remote virtual chassis - Up to 10- km fault-tolerant remote stacking supported
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.10
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.11
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.12
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.2
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.3
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.4
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.5
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.6
MAC Forced
Forwarding
MAC Forced Forwarding-Dynamic Proxy ARP used to forward all traffic from L2 clients
to a head-end router
C / PC / NC
3.7
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.8
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.9
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.2
IP interface dhcp-client
C / PC / NC
4.3
Address Resolution Protocol (ARP)
C / PC / NC
4.4
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.5
Local proxy ARP
C / PC / NC
4.6
ARP filtering
C / PC / NC

<<<PAGE 5>>>
OmniSwitch 6360 — Golden RFP — Page 4
4.7
Gratuitous ARP
C / PC / NC
4.8
ECMP
C / PC / NC
4.9
Static routing
C / PC / NC
4.10
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.2
UDPv6 relay
C / PC / NC
5.3
IPv6
C / PC / NC
5.4
IPv6 - DHCPv6 Snooping
C / PC / NC
5.5
IPv6 - Source filtering
C / PC / NC
5.6
IPv6 - DHCP Guard - EA
C / PC / NC
5.7
IPv6 - DHCP Client Guard - EA
C / PC / NC
5.8
IPv6 - RA Guard (RA filter)
C / PC / NC
5.9
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.10
Static routing
C / PC / NC
5.11
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.8
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.9
Eight egress queues allocated for each port on an switch
C / PC / NC
6.10
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.11
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast

<<<PAGE 6>>>
OmniSwitch 6360 — Golden RFP — Page 5
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
Uboot
authentication
Authentication option to access Uboot (provides access to system parameters) only
after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
Super-user
Secure super-user account using password
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC

<<<PAGE 7>>>
OmniSwitch 6360 — Golden RFP — Page 6
11.7
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.8
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.9
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.10
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.11
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.12
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.13
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC
16.5
PoE
Perpetual PoE
C / PC / NC
16.6
PoE
Fast PoE
C / PC / NC
16.7
PoE
Delayed start
C / PC / NC
16.8
PoE
Time-based PoE control (PoE scheduling)
C / PC / NC

<<<PAGE 8>>>
OmniSwitch 6360 — Golden RFP — Page 7
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Port mirroring
C / PC / NC
18.3
Port mirroring - remote
C / PC / NC
18.4
Port monitoring
C / PC / NC
18.5
RMON
C / PC / NC
18.6
SFlow
C / PC / NC
18.7
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/st_vid11404-ci.p
df
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as NDcPP (EAL1) for network
devices
C / PC / NC

<<<PAGE 9>>>
OmniSwitch 6465 — Golden RFP — Page 1
Golden RFP – OS6465
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 4 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC

<<<PAGE 10>>>
OmniSwitch 6465 — Golden RFP — Page 2
2.5
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.6
Virtual chassis
Remote virtual chassis - Up to 10- km fault-tolerant remote stacking supported
C / PC / NC
2.7
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.8
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.9
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.10
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.11
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.12
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.5
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.6
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.7
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.8
MAC Forced
Forwarding
MAC Forced Forwarding-Dynamic Proxy ARP used to forward all traffic from L2 clients
to a head-end router
C / PC / NC
3.9
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.10
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.11
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.2
IP interface dhcp-client
C / PC / NC

<<<PAGE 11>>>
OmniSwitch 6465 — Golden RFP — Page 3
4.3
Address Resolution Protocol (ARP)
C / PC / NC
4.4
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.5
Local proxy ARP
C / PC / NC
4.6
ARP filtering
C / PC / NC
4.7
Gratuitous ARP
C / PC / NC
4.8
ECMP
C / PC / NC
4.9
Static routing
C / PC / NC
4.10
RIP v1/V2
C / PC / NC
4.11
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.2
UDPv6 relay
C / PC / NC
5.3
IPv6
C / PC / NC
5.4
IPv6 - DHCPv6 Snooping
C / PC / NC
5.5
IPv6 - DHCP Guard - EA
C / PC / NC
5.6
IPv6 - DHCP Client Guard - EA
C / PC / NC
5.7
IPv6 - RA Guard (RA filter)
C / PC / NC
5.8
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.9
Static routing
C / PC / NC
5.10
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.11
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.8
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC

<<<PAGE 12>>>
OmniSwitch 6465 — Golden RFP — Page 4
6.9
Eight egress queues allocated for each port on an switch
C / PC / NC
6.10
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.11
QSP
Custom queue profiles
C / PC / NC
6.12
GOOSE Messaging Prioritization
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
IP Multicast VLAN for dedicated VLANs built specifically for multicast traffic distribution
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
Uboot
authentication
Authentication option to access Uboot (provides access to system parameters) only
after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.12
Super-user
Secure super-user account using password
C / PC / NC
Section 11 – Security framework

<<<PAGE 13>>>
OmniSwitch 6465 — Golden RFP — Page 5
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.8
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.9
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.10
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.11
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.12
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.13
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.14
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
12.4
PTP
Precision Time Protocol (PTP 1588v2) Peer-to-Peer Transparent Clock
C / PC / NC
Section 14 – Industrial protocols
The switch must support the following:
#
ALE Name
Description
Pass
14.1
Profinet
Support for PROFINET
C / PC / NC
14.2
Profinet
Class B PROFINET certified
C / PC / NC
14.3
MRP
IEC 62439I2 Media Redundancy Protocol (MRP)
C / PC / NC

<<<PAGE 14>>>
OmniSwitch 6465 — Golden RFP — Page 6
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA UNP
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video as a part of user dynamic role
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC
16.5
PoE
Delayed start
C / PC / NC
16.6
PoE
Time-based PoE control (PoE scheduling)
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
CPE Test head
C / PC / NC
17.2
Metro Ethernet
Ethernet Loopback Test
C / PC / NC
17.3
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.4
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.5
Metro Ethernet
PPPoE Intermediate Agent
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Port mirroring
C / PC / NC
18.3
Port mirroring - remote
C / PC / NC
18.4
Port monitoring
C / PC / NC
18.5
RMON
C / PC / NC
18.6
SFlow
C / PC / NC

<<<PAGE 15>>>
OmniSwitch 6465 — Golden RFP — Page 7
18.7
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
Electric power
substation
IEEE 1613, sections 4 to 8
C / PC / NC
21.2
Electric power
substation
IEC 61850-3
C / PC / NC
21.3
Railway
applications
EN 50121-4
C / PC / NC
21.4
Railway
applications
EN 50155:2017
C / PC / NC
21.5
Railway
applications
EN 61373
C / PC / NC
21.6
Railway
applications
EN 62236-4
C / PC / NC
21.7
Railway
applications
EN61000-6-4
C / PC / NC
21.8
Railway
applications
EN61000-6-2
C / PC / NC
21.9
Intelligent
transportation
(road)
NEMA TS-2
C / PC / NC
21.10
Marine
certifications
DNVGL-CG-0339 (Requires mandatory DNV kit for compliance)
C / PC / NC
21.11
Marine
certifications
IEC 60945:2002 (Requires mandatory DNV kit for compliance)
C / PC / NC
21.12
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/CCRA%20-%20
ALE%20Enterpris
e.pdf
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as EAL2+ for network devices
C / PC / NC
21.13
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/st_vid11404-ci.p
df
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as NDcPP (EAL1) for network
devices
C / PC / NC
21.14
TAA
OS software has passed specified Trade Agreement Act (TAA) to be in accordance with
valid applicable commercial law
C / PC / NC

<<<PAGE 16>>>
OmniSwitch 6465 — Golden RFP — Page 8

<<<PAGE 17>>>
OmniSwitch 6560 — Golden RFP — Page 1
Golden RFP – OS6560
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 8 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC

<<<PAGE 18>>>
OmniSwitch 6560 — Golden RFP — Page 2
2.4
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.5
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.6
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.7
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.8
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.9
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.10
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.11
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.12
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.6
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.7
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.8
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.9
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.10
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.2
IP interface dhcp-client
C / PC / NC

<<<PAGE 19>>>
OmniSwitch 6560 — Golden RFP — Page 3
4.3
Address Resolution Protocol (ARP)
C / PC / NC
4.4
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.5
Local proxy ARP
C / PC / NC
4.6
ARP filtering
C / PC / NC
4.7
Gratuitous ARP
C / PC / NC
4.8
ECMP
C / PC / NC
4.9
Static routing
C / PC / NC
4.10
RIP v1/V2
C / PC / NC
4.11
OSPF v2
C / PC / NC
4.12
BGP
C / PC / NC
4.13
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.2
UDPv6 relay
C / PC / NC
5.3
IPv6
C / PC / NC
5.4
IPv6 - DHCPv6 Snooping
C / PC / NC
5.5
IPv6 - Source filtering
C / PC / NC
5.6
IPv6 - DHCP Guard - EA
C / PC / NC
5.7
IPv6 - DHCP Client Guard - EA
C / PC / NC
5.8
IPv6 - RA Guard (RA filter)
C / PC / NC
5.9
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.10
Static routing
C / PC / NC
5.11
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.12
OSPF v3
C / PC / NC
5.13
BGP IPv6
C / PC / NC
5.14
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC

<<<PAGE 20>>>
OmniSwitch 6560 — Golden RFP — Page 4
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.8
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.9
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.10
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.11
Eight egress queues allocated for each port on an switch
C / PC / NC
6.12
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.13
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
IP Multicast VLAN for dedicated VLANs built specifically for multicast traffic distribution
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
Uboot
authentication
Authentication option to access Uboot (provides access to system parameters) only
after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC

<<<PAGE 21>>>
OmniSwitch 6560 — Golden RFP — Page 5
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.12
Super-user
Secure super-user account using password
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.8
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.9
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.10
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.11
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.12
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.13
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.14
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.15
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:

<<<PAGE 22>>>
OmniSwitch 6560 — Golden RFP — Page 6
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
12.4
PTP
Precision Time Protocol (PTP 1588v2) Peer-to-Peer Transparent Clock
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC
16.5
PoE
Delayed start
C / PC / NC
16.6
PoE
Time-based PoE control (PoE scheduling)
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
CPE Test head
C / PC / NC
17.2
Metro Ethernet
Ethernet Loopback Test
C / PC / NC
17.3
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.4
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.5
Metro Ethernet
PPPoE Intermediate Agent
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Port mirroring
C / PC / NC

<<<PAGE 23>>>
OmniSwitch 6560 — Golden RFP — Page 7
18.3
Port mirroring - remote
C / PC / NC
18.4
Port mirroring – remote over linkagg
C / PC / NC
18.5
Port monitoring
C / PC / NC
18.6
RMON
C / PC / NC
18.7
SFlow
C / PC / NC
18.8
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/CCRA%20-%20
ALE%20Enterpris
e.pdf
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as EAL2+ for network devices
C / PC / NC
21.2
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/st_vid11404-ci.p
df
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as NDcPP (EAL1) for network
devices
C / PC / NC
21.3
JITC - https://jitc.f
hu.disa.mil/tssi/ce
rt_pdfs/ALE_OS6
560-OS6860E-OS
6860N-OS6865-O
S6900_AOS-8-9-
R21_TN2215701
_Initial_06DEC20
23.pdf
OS software hold a valid interoperability test certification, in line with standards set by
Joint Interoperability Test Command (JITC) test agency to ensure the switch is certified
for military uses.(https://jitc.fhu.disa.mil/tssi/cert_pdfs/ALE_OS6560-OS6860E-OS6860
N-OS6865-OS6900_AOS-8-9-R21_TN2215701_Initial_06DEC2023.pdf)
C / PC / NC

<<<PAGE 24>>>
OmniSwitch 6570M — Golden RFP — Page 1
Golden RFP – OS6570M
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 4 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC

<<<PAGE 25>>>
OmniSwitch 6570M — Golden RFP — Page 2
2.4
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.5
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.6
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.7
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.8
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.9
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.10
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.11
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.12
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.6
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.7
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.8
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.9
MAC Forced
Forwarding
MAC Forced Forwarding-Dynamic Proxy ARP used to forward all traffic from L2 clients
to a head-end router
C / PC / NC
3.10
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.11
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.12
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4

<<<PAGE 26>>>
OmniSwitch 6570M — Golden RFP — Page 3
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
ECMP
C / PC / NC
4.10
GRE tunneling
C / PC / NC
4.11
IP-IP tunneling
C / PC / NC
4.12
Static routing
C / PC / NC
4.13
RIP v1/V2
C / PC / NC
4.14
ISIS IPv4
C / PC / NC
4.15
OSPF v2
C / PC / NC
4.16
BGP
C / PC / NC
4.17
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - DHCP Guard
C / PC / NC
5.9
IPv6 - DHCP Client Guard
C / PC / NC
5.10
IPv6 - RA Guard (RA filter)
C / PC / NC
5.11
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.12
Static routing
C / PC / NC
5.13
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.14
ISIS IPv6
C / PC / NC

<<<PAGE 27>>>
OmniSwitch 6570M — Golden RFP — Page 4
5.15
OSPF v3
C / PC / NC
5.16
BGP IPv6
C / PC / NC
5.17
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Tri-Color Marking rate limiting (CIR, PIR, CBS, PBS)
C / PC / NC
6.8
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.9
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.10
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.11
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.12
Eight egress queues allocated for each port on an switch
C / PC / NC
6.13
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.14
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
IP Multicast VLAN for dedicated VLANs built specifically for multicast traffic distribution
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 9 – Service technologies

<<<PAGE 28>>>
OmniSwitch 6570M — Golden RFP — Page 5
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
Uboot
authentication
Authentication option to access Uboot (provides access to system parameters) only
after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC

<<<PAGE 29>>>
OmniSwitch 6570M — Golden RFP — Page 6
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.12
Super-user
Secure super-user account using password
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.8
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.9
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.10
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.11
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.12
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.13
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.14
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC

<<<PAGE 30>>>
OmniSwitch 6570M — Golden RFP — Page 7
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA UNP
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video as a part of user dynamic role
C / PC / NC
15.3
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
CPE Test head
C / PC / NC
17.2
Metro Ethernet
Ethernet Loopback Test
C / PC / NC
17.3
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.4
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.5
Metro Ethernet
Transparent Bridging
C / PC / NC
17.6
Metro Ethernet
PPPoE Intermediate Agent
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC

<<<PAGE 31>>>
OmniSwitch 6570M — Golden RFP — Page 8
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC

<<<PAGE 32>>>
OmniSwitch 6575 — Golden RFP — Page 1
Golden RFP – OS6575
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 4 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC

<<<PAGE 33>>>
OmniSwitch 6575 — Golden RFP — Page 2
2.4
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.5
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.6
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.7
Virtual chassis
Remote virtual chassis - Up to 10- km fault-tolerant remote stacking supported
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.10
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.11
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.12
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.14
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.6
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.7
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.8
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.9
MAC Forced
Forwarding
MAC Forced Forwarding-Dynamic Proxy ARP used to forward all traffic from L2 clients
to a head-end router
C / PC / NC
3.10
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.11
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.12
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC

<<<PAGE 34>>>
OmniSwitch 6575 — Golden RFP — Page 3
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
ECMP
C / PC / NC
4.10
GRE tunneling
C / PC / NC
4.11
IP-IP tunneling
C / PC / NC
4.12
Static routing
C / PC / NC
4.13
RIP v1/V2
C / PC / NC
4.14
OSPF v2
C / PC / NC
4.15
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - DHCP Guard
C / PC / NC
5.9
IPv6 - DHCP Client Guard
C / PC / NC
5.10
IPv6 - RA Guard (RA filter)
C / PC / NC
5.11
Static routing
C / PC / NC
5.12
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.13
OSPF v3
C / PC / NC
5.14
VRRP v3
C / PC / NC

<<<PAGE 35>>>
OmniSwitch 6575 — Golden RFP — Page 4
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Tri-Color Marking rate limiting (CIR, PIR, CBS, PBS)
C / PC / NC
6.8
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.9
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.10
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.11
Eight egress queues allocated for each port on an switch
C / PC / NC
6.12
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.13
QSP
Custom queue profiles
C / PC / NC
6.14
GOOSE Messaging Prioritization
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
IP Multicast VLAN for dedicated VLANs built specifically for multicast traffic distribution
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 8 – Multi-technology fabric
The switch must support the following:
#
ALE Name
Description
Pass
8.1
Fabric
Fabric support for GRE
C / PC / NC
8.2
Fabric
Fabric support for SPB-M - IEEE 802.1aq Shortest Path Bridging L2/L3 VPN
C / PC / NC

<<<PAGE 36>>>
OmniSwitch 6575 — Golden RFP — Page 5
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
Uboot
authentication
Authentication option to access Uboot (provides access to system parameters) only
after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC

<<<PAGE 37>>>
OmniSwitch 6575 — Golden RFP — Page 6
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.12
MACsec
MACsec on Network Port for SPB/L2GRE/VxLAN
C / PC / NC
10.13
Super-user
Secure super-user account using password
C / PC / NC
10.14
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.13
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC
11.14
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.15
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.16
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC

<<<PAGE 38>>>
OmniSwitch 6575 — Golden RFP — Page 7
11.17
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
Section 14 – Industrial protocols
The switch must support the following:
#
ALE Name
Description
Pass
14.1
Profinet
Support for PROFINET
C / PC / NC
14.2
MRP
IEC 62439I2 Media Redundancy Protocol (MRP)
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC
16.5
PoE
Perpetual PoE
C / PC / NC
16.6
PoE
Fast PoE
C / PC / NC
16.7
PoE
Time-based PoE control (PoE scheduling)
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:

<<<PAGE 39>>>
OmniSwitch 6575 — Golden RFP — Page 8
#
ALE Name
Description
Pass
17.1
Metro Ethernet
CPE Test head
C / PC / NC
17.2
Metro Ethernet
Ethernet Loopback Test
C / PC / NC
17.3
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.4
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.5
Metro Ethernet
Transparent Bridging
C / PC / NC
17.6
Metro Ethernet
PPPoE Intermediate Agent
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
Electric power
substation
IEEE 1613, sections 4 to 8
C / PC / NC
21.2
Electric power
substation
IEC 61850-3
C / PC / NC
21.3
Railway
applications
EN 50121-4
C / PC / NC
21.4
Railway
applications
EN 50155:2017
C / PC / NC

<<<PAGE 40>>>
OmniSwitch 6575 — Golden RFP — Page 9
21.5
Railway
applications
EN 61373
C / PC / NC
21.6
Railway
applications
EN 62236-4
C / PC / NC
21.7
Railway
applications
EN61000-6-4
C / PC / NC
21.8
Railway
applications
EN61000-6-2
C / PC / NC
21.9
Intelligent
transportation
(road)
NEMA TS-2
C / PC / NC
21.10
Marine
certifications
DNVGL-CG-0339 (Requires mandatory DNV kit for compliance)
C / PC / NC
21.11
Marine
certifications
IEC 60945:2002 (Requires mandatory DNV kit for compliance)
C / PC / NC

<<<PAGE 41>>>
OmniSwitch 6860N — Golden RFP — Page 1
Golden RFP – OS6860N
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 8 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
Virtual chassis
Virtual chassis In-Service Software Upgrade (ISSU) for upgrade with minimal network
interruption (VC)
C / PC / NC

<<<PAGE 42>>>
OmniSwitch 6860N — Golden RFP — Page 2
2.5
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.6
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.7
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.10
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.11
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.12
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.14
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.6
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.7
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.8
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.9
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.10
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.11
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:

<<<PAGE 43>>>
OmniSwitch 6860N — Golden RFP — Page 3
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
GRE tunneling
C / PC / NC
4.12
IP-IP tunneling
C / PC / NC
4.13
Static routing
C / PC / NC
4.14
RIP v1/V2
C / PC / NC
4.15
ISIS IPv4
C / PC / NC
4.16
OSPF v2
C / PC / NC
4.17
BGP
C / PC / NC
4.18
VRRP
C / PC / NC
4.19
SLB
a method to logically manage a group of physical servers sharing the same content
(known as a server farm) as one large virtual server (known as an SLB cluster)
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - RA Guard (RA filter)
C / PC / NC
5.9
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.10
Static routing
C / PC / NC
5.11
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.12
ISIS IPv6
C / PC / NC

<<<PAGE 44>>>
OmniSwitch 6860N — Golden RFP — Page 4
5.13
OSPF v3
C / PC / NC
5.14
BGP IPv6
C / PC / NC
5.15
VRRP v3
C / PC / NC
5.16
IPV6 BGP Route Aggregation
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Tri-Color Marking rate limiting (CIR, PIR, CBS, PBS)
C / PC / NC
6.8
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.9
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.10
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.11
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.12
Eight egress queues allocated for each port on an switch
C / PC / NC
6.13
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.14
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
Distance Vector Multicast Routing Protocol (DVMRP)
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC

<<<PAGE 45>>>
OmniSwitch 6860N — Golden RFP — Page 5
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
9.21
MPLS
MPLS – VPLS Point-to-Multipoint service
C / PC / NC
9.22
MPLS
MPLS – VPWS point-to-Point service
C / PC / NC
9.23
VXLAN
VxLAN
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
ONIE
Authentication
Authentication option to access ONIE only after authenticating with the password
C / PC / NC
10.4
Change password
Change Password on First Acces
C / PC / NC

<<<PAGE 46>>>
OmniSwitch 6860N — Golden RFP — Page 6
10.5
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.6
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.7
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.10
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.11
MACsec
MACsec on Network Port for SPB/L2GRE/VxLAN
C / PC / NC
10.12
Super-user
Secure super-user account using password
C / PC / NC
10.13
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.13
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC
11.14
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.15
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC

<<<PAGE 47>>>
OmniSwitch 6860N — Golden RFP — Page 7
11.16
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.17
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
11.18
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in VLAN domain
C / PC / NC
11.19
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in service domain
C / PC / NC
11.20
L2 GRE
2 GRE Tunnel Aggregation switch terminates all tunnels and traffic is stripped from L2
GRE encapsulation and moved from tunnel domain to VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
15.3
Application
Monitoring and
Enforcement
(AppMon)
Real time classification of flows at application level by providing differential QoS
treatment in the form of higher priority marking and security policies at application level
C / PC / NC
15.4
Application
Monitoring and
Enforcement
(AppMon)
Threat-Insight Security in real time classification of flows at application level
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC

<<<PAGE 48>>>
OmniSwitch 6860N — Golden RFP — Page 8
16.5
PoE
Perpetual PoE
C / PC / NC
16.6
PoE
Fast PoE
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.2
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.3
Metro Ethernet
Transparent Bridging
C / PC / NC
17.4
Metro Ethernet
PPPoE Intermediate Agent
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass

<<<PAGE 49>>>
OmniSwitch 6860N — Golden RFP — Page 9
21.1
JITC - https://jitc.f
hu.disa.mil/tssi/ce
rt_pdfs/ALE_OS6
560-OS6860E-OS
6860N-OS6865-O
S6900_AOS-8-9-
R21_TN2215701
_Initial_06DEC20
23.pdf
OS software hold a valid interoperability test certification, in line with standards set by
Joint Interoperability Test Command (JITC) test agency to ensure the switch is certified
for military uses.(https://jitc.fhu.disa.mil/tssi/cert_pdfs/ALE_OS6560-OS6860E-OS6860
N-OS6865-OS6900_AOS-8-9-R21_TN2215701_Initial_06DEC2023.pdf)
C / PC / NC
21.2
TAA
OS software has passed specified Trade Agreement Act (TAA) to be in accordance with
valid applicable commercial law
C / PC / NC

<<<PAGE 50>>>
OmniSwitch 6865 — Golden RFP — Page 1
Golden RFP – OS6865
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 8 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
Virtual chassis
Virtual chassis In-Service Software Upgrade (ISSU) for upgrade with minimal network
interruption (VC)
C / PC / NC

<<<PAGE 51>>>
OmniSwitch 6865 — Golden RFP — Page 2
2.5
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.6
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.7
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.8
Virtual chassis
Remote virtual chassis - Up to 10- km fault-tolerant remote stacking supported
C / PC / NC
2.9
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.10
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.11
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.12
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.14
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.15
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.6
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.7
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.8
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.9
MAC Forced
Forwarding
MAC Forced Forwarding-Dynamic Proxy ARP used to forward all traffic from L2 clients
to a head-end router
C / PC / NC
3.10
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.11
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.12
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC

<<<PAGE 52>>>
OmniSwitch 6865 — Golden RFP — Page 3
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
GRE tunneling
C / PC / NC
4.12
IP-IP tunneling
C / PC / NC
4.13
Static routing
C / PC / NC
4.14
RIP v1/V2
C / PC / NC
4.15
ISIS IPv4
C / PC / NC
4.16
OSPF v2
C / PC / NC
4.17
BGP
C / PC / NC
4.18
VRRP
C / PC / NC
4.19
SLB
a method to logically manage a group of physical servers sharing the same content
(known as a server farm) as one large virtual server (known as an SLB cluster)
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - DHCP Guard - EA
C / PC / NC
5.9
IPv6 - DHCP Client Guard - EA
C / PC / NC
5.10
IPv6 - RA Guard (RA filter)
C / PC / NC

<<<PAGE 53>>>
OmniSwitch 6865 — Golden RFP — Page 4
5.11
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.12
Static routing
C / PC / NC
5.13
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.14
ISIS IPv6
C / PC / NC
5.15
OSPF v3
C / PC / NC
5.16
BGP IPv6
C / PC / NC
5.17
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Tri-Color Marking rate limiting (CIR, PIR, CBS, PBS)
C / PC / NC
6.8
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.9
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.10
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.11
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.12
Eight egress queues allocated for each port on an switch
C / PC / NC
6.13
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.14
QSP
Custom queue profiles
C / PC / NC
6.15
GOOSE Messaging Prioritization
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC

<<<PAGE 54>>>
OmniSwitch 6865 — Golden RFP — Page 5
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
Distance Vector Multicast Routing Protocol (DVMRP)
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC

<<<PAGE 55>>>
OmniSwitch 6865 — Golden RFP — Page 6
10.3
Uboot
authentication
Authentication option to access Uboot (provides access to system parameters) only
after authenticating with the password
C / PC / NC
10.4
Change password
Change Password on First Acces
C / PC / NC
10.5
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.6
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.7
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.10
Super-user
Secure super-user account using password
C / PC / NC
10.11
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.13
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC
11.14
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.15
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC

<<<PAGE 56>>>
OmniSwitch 6865 — Golden RFP — Page 7
11.16
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.17
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
11.18
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in VLAN domain
C / PC / NC
11.19
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in service domain
C / PC / NC
11.20
L2 GRE
2 GRE Tunnel Aggregation switch terminates all tunnels and traffic is stripped from L2
GRE encapsulation and moved from tunnel domain to VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA UNP
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video as a part of user dynamic role
C / PC / NC
15.3
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC
16.5
PoE
Perpetual PoE
C / PC / NC
16.6
PoE
Fast PoE
C / PC / NC
16.7
PoE
Time-based PoE control (PoE scheduling)
C / PC / NC

<<<PAGE 57>>>
OmniSwitch 6865 — Golden RFP — Page 8
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
Ethernet Loopback Test
C / PC / NC
17.2
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.3
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.4
Metro Ethernet
Transparent Bridging
C / PC / NC
17.5
Metro Ethernet
PPPoE Intermediate Agent
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/CCRA%20-%20
ALE%20Enterpris
e.pdf
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as EAL2+ for network devices
C / PC / NC

<<<PAGE 58>>>
OmniSwitch 6865 — Golden RFP — Page 9
21.2
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/st_vid11404-ci.p
df
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as NDcPP (EAL1) for network
devices
C / PC / NC
21.3
FIPS - https://csrc
.nist.gov/Projects/
Cryptographic-Mo
dule-Validation-Pr
ogram/Certificate/
2996
OS software hold a valid Federal Information Processing Standards (FIPS) certification,
meeting the designated FIPS publication 140-2. (https://csrc.nist.gov/Projects/Cryptogra
phic-Module-Validation-Program/Certificate/2996)
C / PC / NC
21.4
JITC - https://jitc.f
hu.disa.mil/tssi/ce
rt_pdfs/ALE_OS6
560-OS6860E-OS
6860N-OS6865-O
S6900_AOS-8-9-
R21_TN2215701
_Initial_06DEC20
23.pdf
OS software hold a valid interoperability test certification, in line with standards set by
Joint Interoperability Test Command (JITC) test agency to ensure the switch is certified
for military uses.(https://jitc.fhu.disa.mil/tssi/cert_pdfs/ALE_OS6560-OS6860E-OS6860
N-OS6865-OS6900_AOS-8-9-R21_TN2215701_Initial_06DEC2023.pdf)
C / PC / NC
21.5
TAA
OS software has passed specified Trade Agreement Act (TAA) to be in accordance with
valid applicable commercial law
C / PC / NC

<<<PAGE 59>>>
OmniSwitch 6870 — Golden RFP — Page 1
Golden RFP – OS6870
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Bloetooth USB
Access to the console via USB adapter with Bluetooth technology provides wireless
management access to the switch, eliminating the use of console cables
C / PC / NC
1.5
Dying Gasp
Dying Gasp support via SNMP and syslog message
C / PC / NC
1.6
Dying Gasp
Dying Gasp propagated by efm-oam/link-oam
C / PC / NC
1.7
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.8
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.9
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.10
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.11
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.12
USB
Automatically Copying Code Using a USB Flash Drive
C / PC / NC
1.13
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.14
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.15
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 8 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
Virtual chassis
Virtual chassis In-Service Software Upgrade (ISSU) for upgrade with minimal network
interruption (VC)
C / PC / NC

<<<PAGE 60>>>
OmniSwitch 6870 — Golden RFP — Page 2
2.5
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.6
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.7
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.10
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.11
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.12
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.14
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.6
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.7
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.8
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.9
MAC Forced
Forwarding
MAC Forced Forwarding-Dynamic Proxy ARP used to forward all traffic from L2 clients
to a head-end router
C / PC / NC
3.10
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.11
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.12
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC

<<<PAGE 61>>>
OmniSwitch 6870 — Golden RFP — Page 3
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
GRE tunneling
C / PC / NC
4.12
IP-IP tunneling
C / PC / NC
4.13
Static routing
C / PC / NC
4.14
RIP v1/V2
C / PC / NC
4.15
ISIS IPv4
C / PC / NC
4.16
OSPF v2
C / PC / NC
4.17
BGP
C / PC / NC
4.18
VRRP
C / PC / NC
4.19
SLB
a method to logically manage a group of physical servers sharing the same content
(known as a server farm) as one large virtual server (known as an SLB cluster)
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - DHCP Guard
C / PC / NC
5.9
IPv6 - DHCP Client Guard
C / PC / NC
5.10
IPv6 - RA Guard (RA filter)
C / PC / NC

<<<PAGE 62>>>
OmniSwitch 6870 — Golden RFP — Page 4
5.11
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.12
Static routing
C / PC / NC
5.13
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.14
ISIS IPv6
C / PC / NC
5.15
OSPF v3
C / PC / NC
5.16
BGP IPv6
C / PC / NC
5.17
VRRP v3
C / PC / NC
5.18
IPV6 BGP Route Aggregation
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Tri-Color Marking rate limiting (CIR, PIR, CBS, PBS)
C / PC / NC
6.8
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.9
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.10
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.11
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.12
Eight egress queues allocated for each port on an switch
C / PC / NC
6.13
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.14
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC

<<<PAGE 63>>>
OmniSwitch 6870 — Golden RFP — Page 5
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
IP Multicast VLAN for dedicated VLANs built specifically for multicast traffic distribution
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 8 – Multi-technology fabric
The switch must support the following:
#
ALE Name
Description
Pass
8.1
Fabric
Hardware-ready fabric support for Ethernet VPN over VxLAN
C / PC / NC
8.2
Fabric
Hardware-ready fabric support for MPLS
C / PC / NC
8.3
Fabric
Fabric support for GRE
C / PC / NC
8.4
Fabric
Fabric support for Virtual eXtensible LAN (VXLAN)
C / PC / NC
8.5
Fabric
Hardware-ready fabric support for SPB-M - IEEE 802.1aq Shortest Path Bridging L2/L3
VPN
C / PC / NC
8.6
Fabric
Fabric support for SPB-M - IEEE 802.1aq Shortest Path Bridging L2/L3 VPN
C / PC / NC
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC

<<<PAGE 64>>>
OmniSwitch 6870 — Golden RFP — Page 6
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
9.21
EVPN
EVPN VXLAN
C / PC / NC
9.22
VXLAN
VxLAN
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Hardware-ready for performing authentication checks during startup so the switch boots
only with verified and trusted software.
C / PC / NC
10.4
ONIE
Authentication
Authentication option to access ONIE only after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.12
MACsec
MACsec on Network Port for SPB/L2GRE/VxLAN
C / PC / NC
10.13
Super-user
Secure super-user account using password
C / PC / NC
10.14
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC

<<<PAGE 65>>>
OmniSwitch 6870 — Golden RFP — Page 7
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.13
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC
11.14
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.15
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.16
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.17
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
11.18
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in VLAN domain
C / PC / NC
11.19
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in service domain
C / PC / NC
11.20
L2 GRE
2 GRE Tunnel Aggregation switch terminates all tunnels and traffic is stripped from L2
GRE encapsulation and moved from tunnel domain to VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC

<<<PAGE 66>>>
OmniSwitch 6870 — Golden RFP — Page 8
15.2
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
15.3
Application
Monitoring and
Enforcement
(AppMon)
Real time classification of flows at application level by providing differential QoS
treatment in the form of higher priority marking and security policies at application level
C / PC / NC
15.4
Application
Monitoring and
Enforcement
(AppMon)
Threat-Insight Security in real time classification of flows at application level
C / PC / NC
Section 16 – PoE
The switch must support the following:
#
ALE Name
Description
Pass
16.1
PoE
Auto Negotiation of PoE Class-power upper limit
C / PC / NC
16.2
PoE
Display of detected power class
C / PC / NC
16.3
PoE
LLDP/802.3at power management TLV
C / PC / NC
16.4
PoE
HPOE support
C / PC / NC
16.5
PoE
Perpetual PoE
C / PC / NC
16.6
PoE
Fast PoE
C / PC / NC
16.7
PoE
Delayed start
C / PC / NC
16.8
PoE
Time-based PoE control (PoE scheduling)
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
CPE Test head
C / PC / NC
17.2
Metro Ethernet
Ethernet Loopback Test
C / PC / NC
17.3
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.4
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.5
Metro Ethernet
Transparent Bridging
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC

<<<PAGE 67>>>
OmniSwitch 6870 — Golden RFP — Page 9
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC

<<<PAGE 68>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 1
Golden RFP – OS6900-V72/C32
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.5
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.6
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.7
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.8
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.9
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.10
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.11
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 6 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
Virtual chassis
Virtual chassis In-Service Software Upgrade (ISSU) for upgrade with minimal network
interruption (VC)
C / PC / NC
2.5
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.6
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC

<<<PAGE 69>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 2
2.7
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.10
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.11
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.12
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.14
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.4
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.5
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.6
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.7
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.8
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.9
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC

<<<PAGE 70>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 3
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
GRE tunneling
C / PC / NC
4.12
IP-IP tunneling
C / PC / NC
4.13
Static routing
C / PC / NC
4.14
RIP v1/V2
C / PC / NC
4.15
ISIS IPv4
C / PC / NC
4.16
OSPF v2
C / PC / NC
4.17
BGP
C / PC / NC
4.18
VRRP
C / PC / NC
4.19
SLB
a method to logically manage a group of physical servers sharing the same content
(known as a server farm) as one large virtual server (known as an SLB cluster)
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - RA Guard (RA filter)
C / PC / NC
5.9
Static routing
C / PC / NC
5.10
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.11
ISIS IPv6
C / PC / NC
5.12
OSPF v3
C / PC / NC
5.13
BGP IPv6
C / PC / NC
5.14
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC

<<<PAGE 71>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 4
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.8
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.9
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.10
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.11
Eight egress queues allocated for each port on an switch
C / PC / NC
6.12
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.13
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
Distance Vector Multicast Routing Protocol (DVMRP)
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC

<<<PAGE 72>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 5
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
9.21
VXLAN
VxLAN
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
ONIE
Authentication
Authentication option to access ONIE only after authenticating with the password
C / PC / NC
10.4
Change password
Change Password on First Acces
C / PC / NC
10.5
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.6
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.7
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.10
Super-user
Secure super-user account using password
C / PC / NC
10.11
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework

<<<PAGE 73>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 6
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.13
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.14
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.15
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.16
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
11.17
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in service domain
C / PC / NC
11.18
L2 GRE
2 GRE Tunnel Aggregation switch terminates all tunnels and traffic is stripped from L2
GRE encapsulation and moved from tunnel domain to VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass

<<<PAGE 74>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 7
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.2
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.3
Metro Ethernet
Transparent Bridging
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass

<<<PAGE 75>>>
OmniSwitch 6900-V72/C32 — Golden RFP — Page 8
21.1
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/CCRA%20-%20
ALE%20Enterpris
e.pdf
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as EAL2+ for network devices
C / PC / NC
21.2
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/st_vid11404-ci.p
df
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as NDcPP (EAL1) for network
devices
C / PC / NC
21.3
FIPS - https://csrc
.nist.gov/Projects/
Cryptographic-Mo
dule-Validation-Pr
ogram/Certificate/
2996
OS software hold a valid Federal Information Processing Standards (FIPS) certification,
meeting the designated FIPS publication 140-2. (https://csrc.nist.gov/Projects/Cryptogra
phic-Module-Validation-Program/Certificate/2996)
C / PC / NC
21.4
JITC - https://jitc.f
hu.disa.mil/tssi/ce
rt_pdfs/ALE_OS6
560-OS6860E-OS
6860N-OS6865-O
S6900_AOS-8-9-
R21_TN2215701
_Initial_06DEC20
23.pdf
OS software hold a valid interoperability test certification, in line with standards set by
Joint Interoperability Test Command (JITC) test agency to ensure the switch is certified
for military uses.(https://jitc.fhu.disa.mil/tssi/cert_pdfs/ALE_OS6560-OS6860E-OS6860
N-OS6865-OS6900_AOS-8-9-R21_TN2215701_Initial_06DEC2023.pdf)
C / PC / NC
21.5
TAA
OS software has passed specified Trade Agreement Act (TAA) to be in accordance with
valid applicable commercial law
C / PC / NC

<<<PAGE 76>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 1
Golden RFP –
OS6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.5
The Lightning
Configuration
Quick configuration wizard for an out-of-the-box, factory-default switch to be quickly and
easily deployed using a WEB interface
C / PC / NC
1.6
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.7
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.8
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.9
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.10
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.11
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 6 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.4
Virtual chassis
Virtual chassis In-Service Software Upgrade (ISSU) for upgrade with minimal network
interruption (VC)
C / PC / NC
2.5
Virtual chassis
The automatic virtual chassis feature will allow a brand new chassis shipped from the
factory or a chassis with no configuration to be setup as a virtual chassis without user
configuration
C / PC / NC
2.6
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC

<<<PAGE 77>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 2
2.7
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC
2.10
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.11
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.12
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.14
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
DHL
Fast failover initiated by edge switch over active-active or active-standby links between
core and edge switches without using Spanning Tree
C / PC / NC
3.4
Private VLAN
Ability to isolate Layer 2 data between devices that are on the same VLAN (Private
VLANs)
C / PC / NC
3.5
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.6
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.7
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.8
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.9
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.10
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.11
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC

<<<PAGE 78>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 3
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
GRE tunneling
C / PC / NC
4.12
IP-IP tunneling
C / PC / NC
4.13
Static routing
C / PC / NC
4.14
RIP v1/V2
C / PC / NC
4.15
ISIS IPv4
C / PC / NC
4.16
OSPF v2
C / PC / NC
4.17
BGP
C / PC / NC
4.18
VRRP
C / PC / NC
4.19
SLB
a method to logically manage a group of physical servers sharing the same content
(known as a server farm) as one large virtual server (known as an SLB cluster)
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - RA Guard (RA filter)
C / PC / NC
5.9
Static routing
C / PC / NC
5.10
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.11
ISIS IPv6
C / PC / NC
5.12
OSPF v3
C / PC / NC
5.13
BGP IPv6
C / PC / NC
5.14
VRRP v3
C / PC / NC
5.15
IPV6 BGP Route Aggregation
C / PC / NC

<<<PAGE 79>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 4
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.8
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.9
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.10
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.11
Eight egress queues allocated for each port on an switch
C / PC / NC
6.12
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.13
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
Distance Vector Multicast Routing Protocol (DVMRP)
C / PC / NC
7.6
Multicast
PIM - Anycast RP
C / PC / NC
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC

<<<PAGE 80>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 5
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
9.21
EVPN
EVPN VXLAN
C / PC / NC
9.22
EVPN
Route Redistribution for Prefix Route Advertisement for Symmetric IRB
C / PC / NC
9.23
EVPN
BGP NBR Template and Scalability
C / PC / NC
9.24
EVPN
Multicast Routing Over an EVPN Fabric (RFC 9625) - OISM & PIM Support
C / PC / NC
9.25
EVPN
Distributed Anycast Gateway (DAG) for EVPN
C / PC / NC
9.26
EVPN
BGP Route reflector for EVPN
C / PC / NC
9.27
EVPN
VRF-based Tenancy Model for EVPN Services
C / PC / NC
9.28
EVPN
Manual RT (Route-Target) configuration
C / PC / NC
9.29
EVPN
EVPN Multi-site topology
C / PC / NC
9.30
MPLS
MPLS – VPLS Point-to-Multipoint service
C / PC / NC
9.31
MPLS
MPLS – VPWS point-to-Point service
C / PC / NC
9.32
VXLAN
VxLAN
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC

<<<PAGE 81>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 6
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
ONIE
Authentication
Authentication option to access ONIE only after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.7
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.10
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.11
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes (X48C4E)
C / PC / NC
10.12
Super-user
Secure super-user account using password
C / PC / NC
10.13
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC

<<<PAGE 82>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 7
11.13
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC
11.14
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.15
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.16
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.17
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
11.18
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in service domain
C / PC / NC
11.19
L2 GRE
2 GRE Tunnel Aggregation switch terminates all tunnels and traffic is stripped from L2
GRE encapsulation and moved from tunnel domain to VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
12.3
PTP
Precision Time Protocol (PTP 1588v2) End-to-End Transparent Clock
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
Section 17 – Metro Ethernet
The switch must support the following:
#
ALE Name
Description
Pass
17.1
Metro Ethernet
Ethernet Services (VLAN Stacking)
C / PC / NC
17.2
Metro Ethernet
Ethernet OAM (ITU Y1731 and 802.1ag
C / PC / NC
17.3
Metro Ethernet
Transparent Bridging
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:

<<<PAGE 83>>>
OmniSwitch 6900-X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24C2 — Golden RFP — Page 8
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
TAA
OS software has passed specified Trade Agreement Act (TAA) to be in accordance with
valid applicable commercial law
C / PC / NC

<<<PAGE 84>>>
OmniSwitch 6920 — Golden RFP — Page 1
Golden RFP – OS6920
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.5
Reset to Factory
Default
Removing all switch configurations (vcboot.cfg, vcsetup.cfg), packages, user
configurations, switch logs and user-created files with a single command
C / PC / NC
1.6
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.7
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.8
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.9
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.10
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.2
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.3
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.4
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.5
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.6
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass

<<<PAGE 85>>>
OmniSwitch 6920 — Golden RFP — Page 2
3.1
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.2
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.3
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.4
Port mapping
Controlling communication between predefined user and network ports users in a way
that user ports can communicate with network ports only (Port Mapping)
C / PC / NC
3.5
Port mapping
Possibility to enable or disable communication between network ports (Port Mapping)
C / PC / NC
3.6
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
Static routing
C / PC / NC
4.12
RIP v1/V2
C / PC / NC
4.13
ISIS IPv4
C / PC / NC
4.14
OSPF v2
C / PC / NC
4.15
BGP
C / PC / NC
4.16
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC

<<<PAGE 86>>>
OmniSwitch 6920 — Golden RFP — Page 3
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - DHCP Guard
C / PC / NC
5.9
IPv6 - DHCP Client Guard
C / PC / NC
5.10
IPv6 - RA Guard (RA filter)
C / PC / NC
5.11
Pv6 - DHCP relay and Neighbor discovery proxy
C / PC / NC
5.12
Static routing
C / PC / NC
5.13
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.14
ISIS IPv6
C / PC / NC
5.15
OSPF v3
C / PC / NC
5.16
BGP IPv6
C / PC / NC
5.17
VRRP v3
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Tri-Color Marking rate limiting (CIR, PIR, CBS, PBS)
C / PC / NC
6.8
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.9
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC
6.10
A QoS policy list applied to traffic egressing on switch ports
C / PC / NC
6.11
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.12
Eight egress queues allocated for each port on an switch
C / PC / NC
6.13
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.14
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC

<<<PAGE 87>>>
OmniSwitch 6920 — Golden RFP — Page 4
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
PIM - Anycast RP
C / PC / NC
Section 8 – Multi-technology fabric
The switch must support the following:
#
ALE Name
Description
Pass
8.1
Fabric
Fabric support for GRE
C / PC / NC
8.2
Fabric
Fabric support for SPB-M - IEEE 802.1aq Shortest Path Bridging L2/L3 VPN
C / PC / NC
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC
9.18
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.19
SPB
Multiple ERP ring over SPB
C / PC / NC

<<<PAGE 88>>>
OmniSwitch 6920 — Golden RFP — Page 5
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Secure boot
Performing authentication checks during startup so the switch boots only with verified
and trusted software.
C / PC / NC
10.4
ONIE
Authentication
Authentication option to access ONIE only after authenticating with the password
C / PC / NC
10.5
Change password
Change Password on First Acces
C / PC / NC
10.6
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.7
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.9
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.10
Super-user
Secure super-user account using password
C / PC / NC
10.11
Internet Protocol Security (Ipsec) - a set of protocols that secures network
communication at the IP layer (Layer 3
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.5
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC
11.6
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.7
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.8
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.9
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.10
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC

<<<PAGE 89>>>
OmniSwitch 6920 — Golden RFP — Page 6
11.11
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.12
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port monitoring
C / PC / NC
18.5
RMON
C / PC / NC
18.6
SFlow
C / PC / NC
18.7
Switch logging / Syslog
C / PC / NC
Section 19 – Data Center
The switch must support the following:
#
ALE Name
Description
Pass
19.1
Support for RoCEv2 and PFC for losless network
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC

<<<PAGE 90>>>
OmniSwitch 9900 — Golden RFP — Page 1
Golden RFP – OS9900
Section 1 – Management
The switch must support the following:
#
ALE Name
Description
Pass
1.1
Automatic
Remote
Configuration
Download (RCL)
Automating and simplifying the deployment of large network installations eliminating the
need for manual configuration of each switch (Automatic Remote Configuration
Download
C / PC / NC
1.2
Automatic/Intellig
ent Fabric
Dynamic recognition of the neighboring elements allows for a quick, out-of-the-box
configuration of the switch
C / PC / NC
1.3
Automatic/Intellig
ent Fabric
Automatic discovery and configuration for LACP, SPB, and MVRP and IP protocols
C / PC / NC
1.4
Phyton scripting
Embedded Python Scripting
C / PC / NC
1.5
SNMP
Full configuration and reporting using Simple Network Management Protocol (SNMP)
v1/2/3
C / PC / NC
1.6
Thin Client
The equipment can work in a “thin client” mode. In this mode no configuration can be
saved in the “Running” directory of the switch. A basic configuration with minimal
network reachability configuration is stored on the switch running directory. The final
configuration of a thin client is pushed by a Network Management System (NMS).
C / PC / NC
1.7
USB
Disaster Recovery Using a USB Flash Drive
C / PC / NC
1.8
Linux commands
Support for specific OS Linux commands
C / PC / NC
1.9
Prompt
Session Prompt up to 64 Characters
C / PC / NC
Section 2 – Resiliency and high availability
The switch must support the following:
#
ALE Name
Description
Pass
2.1
Virtual chassis
Multiple physical switches connected using the virtual-fabric links with unified
management & control, acting as a single device and providing node and link level
redundancy without protocols such as STP or VRRP - “virtual chassis”
C / PC / NC
2.2
Virtual chassis
Virtual chassis up to 2 nodes
C / PC / NC
2.3
Virtual chassis
Virtual chassis on 11-slot chassis
C / PC / NC
2.4
Virtual chassis
Virtual chassis 1+N redundant supervisor manager (VC)
C / PC / NC
2.5
Virtual chassis
Virtual chassis In-Service Software Upgrade (ISSU) for upgrade with minimal network
interruption (VC)
C / PC / NC
2.6
RCD
Detecting that a split of virtual chassis has occurred and preventing duplicate MAC and
IP addresses on the network
C / PC / NC
2.7
VCSP
A protocol used by virtual chassis to detect and protect against network disruption when
a VC splits. VC split condition has been determined, the sub-VC will put its front-panel
ports into an operationally down state preventing traffic forwarding and avoiding loops
and possible traffic disruption
C / PC / NC
2.8
STP
Spanning Tree (1X1, RSTP, MSTP)
C / PC / NC
2.9
STP
Spanning Tree (PVST+, Loop Guard)
C / PC / NC

<<<PAGE 91>>>
OmniSwitch 9900 — Golden RFP — Page 2
2.10
LACP
IEEE 802.3ad/802.1AX Link Aggregation Control Protocol (LACP) and static LAG
groups across modules
C / PC / NC
2.11
LBD
Automatically detection of the loop and shutdown the port involved in the loop
preventing Layer 2 forwarding loop functionality (non xSTP based)
C / PC / NC
2.12
LBD
Automatically detection of the loop on the bridge port or linkagg (LBD)
C / PC / NC
2.13
LBD
Automatically detection of the loop on the service port or linkagg(LBD)
C / PC / NC
2.14
VRRP
Virtual Router Redundancy Protocol (VRRP) with tracking capabilities
C / PC / NC
Section 3 – Layer 2
The switch must support the following:
#
ALE Name
Description
Pass
3.1
802.1ad
Ethernet services support using IEEE 802.1ad Provider Bridges (also known as Q-in-Q
or VLAN stacking)
C / PC / NC
3.2
802.1q
Ethernet services support using IEEE 802.1q VLAN tagging
C / PC / NC
3.3
HAVLAN
VLAN allowing for sending traffic to send traffic intended for a single destination MAC
address to multiple switch ports for Layer 2 clusters such as MS-NLB and active-active
Firewall clusters
C / PC / NC
3.4
LLDP
IEEE 802.1AB Link Layer Discover Protocol (LLDP) used to detect adjacent devices in a
network
C / PC / NC
3.5
LLDP
IEEE 802.1AB LLDP with Media Endpoint Discover (MED) extensions
C / PC / NC
3.6
ERPv2
ITU-T G.8032/Y.1344 2010: Ethernet Ring Protection (ERPv2)
C / PC / NC
3.7
MVRP
Multiple VLAN Registration Protocol (MVRP), IEEE standard LayerI2 protocol used for
automatic VLAN registration and propagation across switches
C / PC / NC
Section 4 – IPv4
The switch must support the following:
#
ALE Name
Description
Pass
4.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
4.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv4
C / PC / NC
4.3
IP interface dhcp-client
C / PC / NC
4.4
Address Resolution Protocol (ARP)
C / PC / NC
4.5
Adding/deleting a permanent entry to the ARP table
C / PC / NC
4.6
Local proxy ARP
C / PC / NC
4.7
ARP filtering
C / PC / NC
4.8
Gratuitous ARP
C / PC / NC
4.9
Bidirectional Forwarding Detection (BFD) for fast failure detection and reduced
re-convergence times in a routed environment including VRRP
C / PC / NC
4.10
ECMP
C / PC / NC
4.11
GRE tunneling
C / PC / NC
4.12
IP-IP tunneling
C / PC / NC

<<<PAGE 92>>>
OmniSwitch 9900 — Golden RFP — Page 3
4.13
Static routing
C / PC / NC
4.14
RIP v1/V2
C / PC / NC
4.15
OSPF v2
C / PC / NC
4.16
BGP
C / PC / NC
4.17
VRRP
C / PC / NC
Section 5 – IPv6
The switch must support the following:
#
ALE Name
Description
Pass
5.1
Multiple Virtual Routing and Forwarding (VRF) instances
C / PC / NC
5.2
Dynamic Host Configuration Protocol (DHCP) relay for IPv6
C / PC / NC
5.3
UDPv6 relay
C / PC / NC
5.4
DHCP server v6
C / PC / NC
5.5
IPv6
C / PC / NC
5.6
IPv6 - DHCPv6 Snooping
C / PC / NC
5.7
IPv6 - Source filtering
C / PC / NC
5.8
IPv6 - RA Guard (RA filter)
C / PC / NC
5.9
Static routing
C / PC / NC
5.10
RIPng (Routing Information Protocol next generation)
C / PC / NC
5.11
ISIS IPv6
C / PC / NC
5.12
OSPF v3
C / PC / NC
5.13
BGP IPv6
C / PC / NC
5.14
VRRP v3
C / PC / NC
5.15
IPV6 BGP Route Aggregation
C / PC / NC
Section 6 – Quality of Service (QoS)
The switch must support the following:
#
ALE Name
Description
Pass
6.1
Ingress classification and marking
C / PC / NC
6.2
Classification based on IP precedence
C / PC / NC
6.3
Classification based on 802.1p priority
C / PC / NC
6.4
Automatic QoS Prioritization for IP Phone Traffic
C / PC / NC
6.5
Prioritizing CPU Packets
C / PC / NC
6.6
Maximum bandwidth on ingress and egress ports
C / PC / NC
6.7
Condition groups made up of multiple IPv4 addresses, MAC addresses, services, ports,
or VLANs
C / PC / NC
6.8
A QoS policy list providing a method for grouping multiple policy rules together and
applying the group of rules to specific types of traffic
C / PC / NC

<<<PAGE 93>>>
OmniSwitch 9900 — Golden RFP — Page 4
6.9
Policy based routing defining QoS policies that override the normal routing mechanism
for traffic matching the policy condition
C / PC / NC
6.10
Eight egress queues allocated for each port on an switch
C / PC / NC
6.11
QSP
Predefined queue profiles defining the output scheduling behavior
C / PC / NC
6.12
QSP
Custom queue profiles
C / PC / NC
Section 7 – Multicast
The switch must support the following:
#
ALE Name
Description
Pass
7.1
Multicast
IPMS supported within VLAN or service or system domain
C / PC / NC
7.2
Multicast
IGMPv1/v2/v3 snooping and Multicast Listener Discovery (MLD) v1/v2 for fast client
joins and leaves of multicast streams and limit bandwidth-intensive video traffic to only
the requestors
C / PC / NC
7.3
Multicast
Protocol Independent Multicast – Sparse- Mode (PIM-SM), Source Specific Multicast
(PIM-SSM)
C / PC / NC
7.4
Multicast
Protocol Independent Multicast – Dense-Mode (PIM-DM), Bidirectional Protocol
Independent Multicast (PIM-BiDir)
C / PC / NC
7.5
Multicast
PIM - Anycast RP
C / PC / NC
Section 9 – Service technologies
The switch must support the following:
#
ALE Name
Description
Pass
9.1
SPB
Fabric support for SPB-M – IEEE 802.1aq Shortest Path Bridging
C / PC / NC
9.2
SPB
Provider Backbone Bridge (PBB) IEEE 802.1ah
C / PC / NC
9.3
SPB
Minimum Equal Cost Tree (ECT) for the backbone VLAN (BVLAN): 16
C / PC / NC
9.4
SPB
Configurable Control BVLAN
C / PC / NC
9.5
SPB
Head-end replication multicast mode
C / PC / NC
9.6
SPB
Tandem replication multicast mode
C / PC / NC
9.7
SPB
SPB service VLAN translation
C / PC / NC
9.8
SPB
Layer 2 profile that specifies how control packets are processed on service access ports
C / PC / NC
9.9
SPB
Configurable SAP encapsulation
C / PC / NC
9.10
SPB
SAP trust mode
C / PC / NC
9.11
SPB
SPBM Pseudo-Wire (E-LINE Transparent) Service
C / PC / NC
9.12
SPB
SPBM Point-to-Multipoint (E-LAN) Service
C / PC / NC
9.13
SPB
SPBM Root-Leaves (E-Tree) Service
C / PC / NC
9.14
SPB
SPBM L3 VPN Service over routing protocols
C / PC / NC
9.15
SPB
SPBM L3 VPN Service over I-SID
C / PC / NC
9.16
SPB
SPBM backbone over a Service Provider (shared) network
C / PC / NC
9.17
SPB
SPBM In-Band management with Ipv4 interface over BVLAN
C / PC / NC

<<<PAGE 94>>>
OmniSwitch 9900 — Golden RFP — Page 5
9.18
SPB
SPBM In-Band management with Ipv6 interface over BVLAN
C / PC / NC
9.19
SPB
ERP Over SPB for Unicast Client
C / PC / NC
9.20
SPB
Multiple ERP ring over SPB
C / PC / NC
Section 10 – Security
The switch must support the following:
#
ALE Name
Description
Pass
10.1
Console Disable
Possibility to disable the access to the switch configuration shell through the console
port
C / PC / NC
10.2
Signed AOS
Image
Ability for an switch to determine if the OS software comes from a trusted source and to
detect if it has been tampered with after signing. Using RSA-2048 and SHA-256, OS
images are signed with a private key allowing OS to verify the signature with a
corresponding public key during reload
C / PC / NC
10.3
Change password
Change Password on First Acces
C / PC / NC
10.4
ALE CA signed
certificates
Switch will use certificates generated by the company's Internal Certificate Authority
(CA)
C / PC / NC
10.5
Diversified code
Secured diversified code enhances security at both the software source code and binary
executable level to improve overall network security and address current and future
threats
C / PC / NC
10.6
LPS
Mechanism for authorizing source learning of MAC addresses on Ethernet ports or
service ports
C / PC / NC
10.7
LPS
Mechanism for authorizing source learning of MAC addresses based on time limit
C / PC / NC
10.8
LPS
Mechanism for authorizing source learning of MAC addresses based on the number of
MAC addresses
C / PC / NC
10.9
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes
C / PC / NC
10.10
MACsec
MACsec provides point-to-point security on Ethernet links between directly connected
nodes (X48C4E)
C / PC / NC
10.11
Super-user
Secure super-user account using password
C / PC / NC
Section 11 – Security framework
The switch must support the following:
#
ALE Name
Description
Pass
11.1
UNP
Network profile logical entity for physical devices attached to a LAN port providing
authentication, device compliance, and access control functions
C / PC / NC
11.2
UNP
Network profile logical entity - MAC authentication
C / PC / NC
11.3
UNP
Network profile logical entity - 802.1ax authentication
C / PC / NC
11.4
UNP
Network profile logical entity - internal captive portal authentication
C / PC / NC
11.5
UNP
Network profile logical entity - external captive portal authentication
C / PC / NC
11.6
UNP
Network profile logical entity applicable to VLAN domains
C / PC / NC
11.7
UNP
Network profile logical entity applicable to service domains
C / PC / NC
11.8
UNP
Applying VLAN or service through network profile after authentication
C / PC / NC

<<<PAGE 95>>>
OmniSwitch 9900 — Golden RFP — Page 6
11.9
UNP
Applying QoS parameters through network profile after authentication
C / PC / NC
11.10
Controlled
Directed
Broadcasts
Controlled Directed Broadcasts - allowing directed broadcast only from trusted source to
the desination network
C / PC / NC
11.11
ARP Poisoning
Protection
Detecting the presence of ARP poisoning host on a network and not sending ARP
response
C / PC / NC
11.12
Denial of Service
(DoS) Filtering
Filtering denial of service (DoS) attacks
C / PC / NC
11.13
Denial of Service
(DoS) Filtering
IPv6 Denial of Service (DoS) Detection
C / PC / NC
11.14
IoT Device
Profiling
allows the network administrators to support and manage smart phones, Tablets and
other devices connecting to the network through identifying IoT devices using DHCP
fingerprinting and MAC OUI
C / PC / NC
11.15
Quarantine
Manager
Switch-based application that restricts the network access of known quarantined users
C / PC / NC
11.16
Storm control
storm control through flood rate limiting for broadcast, unknown unicast, and multicast
traffic
C / PC / NC
11.17
Storm control
storm control (Unknown unicast with action trap/shutdown)
C / PC / NC
11.18
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in VLAN domain
C / PC / NC
11.19
L2 GRE
L2 GRE tunneling provides a Layer 2 overlay network that is used to tunnel
encapsulated traffic over an IP network in service domain
C / PC / NC
11.20
L2 GRE
2 GRE Tunnel Aggregation switch terminates all tunnels and traffic is stripped from L2
GRE encapsulation and moved from tunnel domain to VLAN domain
C / PC / NC
Section 12 – Timing and synchronization protocols
The switch must support the following:
#
ALE Name
Description
Pass
12.1
NTP
NTP - Version 4
C / PC / NC
12.2
NTP
NTP - IPv6
C / PC / NC
Section 15 – Network performance
The switch must support the following:
#
ALE Name
Description
Pass
15.1
SAA
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video
C / PC / NC
15.2
SAA SPB
Measurement of network performance and health by generating traffic in a continuous,
reliable, and predictable manner to assure business-critical applications, as well as
services that utilize data, voice, and video within SPB network
C / PC / NC
Section 18 – Monitoring/Troubleshooting
The switch must support the following:

<<<PAGE 96>>>
OmniSwitch 9900 — Golden RFP — Page 7
#
ALE Name
Description
Pass
18.1
Ping and traceroute
C / PC / NC
18.2
Policy based mirroring
C / PC / NC
18.3
Port mirroring
C / PC / NC
18.4
Port mirroring - remote
C / PC / NC
18.5
Port mirroring – remote over linkagg
C / PC / NC
18.6
Port monitoring
C / PC / NC
18.7
RMON
C / PC / NC
18.8
SFlow
C / PC / NC
18.9
Switch logging / Syslog
C / PC / NC
Section 20 – Software Defined Networking (SDN)
The switch must support the following:
#
ALE Name
Description
Pass
20.1
Programmable OS RESTful API
C / PC / NC
Section 21 – Certifications
The switch must support the following:
#
ALE Name
Description
Pass
21.1
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/CCRA%20-%20
ALE%20Enterpris
e.pdf
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as EAL2+ for network devices
C / PC / NC
21.2
CC - https://www.
commoncriteriapo
rtal.org/files/epfile
s/st_vid11404-ci.p
df
OS software has passed Common Criteria certification, ensuring compliance with
internationally recognized security standards such as NDcPP (EAL1) for network
devices
C / PC / NC
21.3
FIPS - https://csrc
.nist.gov/Projects/
Cryptographic-Mo
dule-Validation-Pr
ogram/Certificate/
2996
OS software hold a valid Federal Information Processing Standards (FIPS) certification,
meeting the designated FIPS publication 140-2. (https://csrc.nist.gov/Projects/Cryptogra
phic-Module-Validation-Program/Certificate/2996)
C / PC / NC
21.4
JITC - https://jitc.f
hu.disa.mil/tssi/ce
rt_pdfs/ALE_OS6
560-OS6860E-OS
6860N-OS6865-O
S6900_AOS-8-9-
R21_TN2215701
_Initial_06DEC20
23.pdf
OS software hold a valid interoperability test certification, in line with standards set by
Joint Interoperability Test Command (JITC) test agency to ensure the switch is certified
for military uses.(https://jitc.fhu.disa.mil/tssi/cert_pdfs/ALE_OS6560-OS6860E-OS6860
N-OS6865-OS6900_AOS-8-9-R21_TN2215701_Initial_06DEC2023.pdf)
C / PC / NC

<<<PAGE 97>>>
OmniSwitch 9900 — Golden RFP — Page 8
21.5
TAA
OS software has passed specified Trade Agreement Act (TAA) to be in accordance with
valid applicable commercial law
C / PC / NC