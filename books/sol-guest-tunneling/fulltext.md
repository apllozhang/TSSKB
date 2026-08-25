<<<PAGE 1>>>
www.al-enterprise.com 
Alcatel-Lucent and the Alcatel-Lucent Enterprise logo are trademarks of Alcatel-Lucent. To view other trademarks used by affiliated 
companies of ALE Holding, visit: enterprise.alcatel-lucent.com/trademarks. All other trademarks are the property of their respective 
owners. The information presented is subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any  
responsibility for inaccuracies contained herein. 23032701 (April 2023)  
 
 
 
 
Guest Traffic Tunnelling 
Services Application Note

<<<PAGE 2>>>
2 
 
Application Note 
Guest Traffic Tunnelling Services 
Table of Contents 
 
Configuration ........................................................................................ 4 
Global knowledge ....................................................................................... 4 
Prerequisites ............................................................................................ 6 
Requirement : ......................................................................................... 6 
Software & hardware used .......................................................................... 7 
Architecture prerequisites ........................................................................... 7 
Switch configuration ................................................................................... 9 
AP configuration ....................................................................................... 10 
Scenarios............................................................................................ 11 
Guest tunneling toward a Demilitarized Zone.................................................... 11 
Introduction ........................................................................................... 11 
Campus deployment ................................................................................... 12 
Introduction ........................................................................................... 12 
Architecture .......................................................................................... 12 
Multi-tenancy on a single tunnel aggregation switch ........................................... 13 
Introduction ........................................................................................... 13 
Architecture .......................................................................................... 13 
GTTS redundancy designs ............................................................................ 14 
Introduction ........................................................................................... 14 
Redundancy 0 ......................................................................................... 14 
Redundancy 1 – Hairpin redundancy............................................................... 15 
Redundancy 2 – Primary & Secondary ............................................................. 16 
Redundancy 3 – Virtual-Chassis .................................................................... 17 
Redundancy 4 – One switch couple per SSID ..................................................... 18

<<<PAGE 3>>>
3 
 
Application Note 
Guest Traffic Tunnelling Services 
OmniAccess Stellar Traffic Tunnelling 
 
The OmniAccess Stellar WLAN architecture is distributed and controller-less. This presents 
multiple advantages from both performance and cost points of view [1]. There are however 
certain use cases in which traffic can be tunneled and concentrated in a central choke point: 
1. Guest Traffic: Guest users are not corporate users and, therefore, their traffic should 
be completely isolated from corporate traffic. This can be achieved by tunnelling guest 
traffic to a central location, usually in the DMZ, such that this traffic cannot mix with 
corporate traffic and can only access the Internet. 
2. Security Policy: Certain security services, such as IPS, require the security appliance to 
be deployed in-line with traffic or in a “bump in the wire” model. Wireless traffic can 
be tunnelled such that traffic can be scrubbed and security policies can be applied. 
3. Migration: When migrating from a controller-based architecture to a distributed one, it 
may be undesirable to deploy additional VLANs at the edge. By tunnelling wireless traffic 
to a central location, no additional VLANs are required at the edge and any VLAN 
configuration is done only at the central location. 
OmniAccess Stellar and OmniSwitch “Guest Traffic Tunneling Services” (GTTS) allow flexible 
tunnelling of wireless user traffic from the Access to Point to one or more OmniSwitch tunnel 
termination endpoints. This functionality was originally conceived, as the name implies, for 
Guest traffic. Nevertheless, it can also be applied to the other 2 use cases mentioned above. 
This tunnelling is flexible because it allows fine-grained selection of the specific traffic that 
needs to be tunneled: all wireless traffic, at SSID level or even at the ARP (Access Role Profile) 
level. 
 
What’s more: GTTS is configurable at the AP Group level. Because of that, wireless traffic from 
different sites can be tunneled to different points or to a central point. 
Lastly, GTTS is also applicable in multi-tenanted scenarios in which traffic from multiple 
different customers is concentrated on the same GTTS termination end point(s) whilst still 
preserving logical isolation between different customers. 
 
In this application note, we will examine the configuration of the GTTS functionality and its 
different redundancy mechanisms through specific use cases and we will provide configuration 
examples and design guidelines. 
 
[1]: Distributed Wi-Fi Control Architecture

<<<PAGE 4>>>
4 
 
Application Note 
Guest Traffic Tunnelling Services 
Configuration 
Global knowledge 
The GTTS is based on the L2 GRE Tunneling protocol. 
Layer 2 Generic Routing Encapsulation (L2 GRE) tunneling is a mechanism that is used to identify 
and isolate device traffic from the rest of the internal network traffic. This implementation of 
L2 GRE tunneling is like the OmniSwitch implementation of VXLAN as follows: 
- 
L2 GRE tunnelling provides a Layer 2 overlay network that is used to tunnel encapsulated 
traffic over an IP network between two L2 GRE tunnels end points. 
- 
L2 GRE is implemented as a service and can also be associated with a UNP profile. 
 
An L2 GRE tunnel is defined by configuring an L2 GRE end point on an Access Point and an L2 
GRE end point on a tunnel aggregation switch. 
- 
Traffic received on the Access Point is classified into a Access Role Profile L2 GRE service 
profile that is mapped to an L2 GRE tunnel service. The profile identifies the device 
traffic that will be encapsulated with a GRE header and carried over an L2 GRE tunnel 
to a tunnel aggregation switch. 
- 
When the tunnelled traffic reaches the tunnel aggregation switch, the GRE 
encapsulation is removed, and the traffic is then forwarded to a VLAN domain. At this 
point, the device traffic can gain access to a perimeter network and/or the Internet. 
- 
On the switch side, a Hairpin is necessary. This is a loop, one cable from one port is 
connected to another port on the same switch. Each side of the Hairpin has a different 
configuration: 
o SAP port: this is where the tunneled traffic will be entered to go out of the 
tunnel. A service must be created and mapped to this specific port. 
o ACCESS port: The ACCESS port is the other side of the Hairpin. This is a legacy 
access port where a VLAN is mapped. Thus, all traffic coming from the tunnel 
will go out to this port, and thus be part of the configured VLAN. 
Of course, the vice versa is also true. All the packets going to the client must first travel 
through the ACCESS port to be tunneled and reach the end client. 
 
Usually, the tunnel aggregation switch is deployed in a place that is logically secured, as a DMZ 
secured by one or multiple firewalls. We want a high security level at this level because this is 
where the tunnel ends, and so where the risks are the highest. 
 
The user traffic is tunneled directly after the SSID association. That means that even DHCP 
flows travel inside the tunnel. Therefore, a DHCP server must be deployed in the same area of 
the tunnel aggregation switch. This is still possible to use protocols to forward DHCP requests 
to a server that is not part of the same subnet, but a dedicated server is still better from a 
security point of view. 
Same idea for the Guest Captive Portal. If an internal Captive Portal is deployed, then it 
should be accessible from the tunnel endpoint while keeping security policies.

<<<PAGE 5>>>
5 
 
Application Note 
Guest Traffic Tunnelling Services 
This is also true for each other’s services. All the traffic destined for the end users must first 
passed in the Hairpin from the ACCESS port, to enter the SAP port and be part of the tunnel. 
Then, the traffic is forwarded to the far-end AP and delivered to the end user. 
Understand that all services like DHCP, Captive Portal, DNS, NTP, …, must be reachable from 
the tunnel aggregation switch. The best would be to have dedicated services for tunneled SSID 
to keep a high security level. 
Through multiple ways, one SSID can be mapped to multiple ARPs, not mentioning the default 
one: 
- 
802.1x authentication using Filter-id field, 
- 
IoT Enforcement, 
- 
Device specific ARP. 
 
In that case, multiple ARPs must be created and mapped to as many of Tunnel Profiles, which 
contains all the parameters to setup the L2 GRE tunnel. 
In this scenario, using only one SSID, different devices traffic can be tunneled to different end 
point tunnels, regarding of their classification.

<<<PAGE 6>>>
6 
 
Application Note 
Guest Traffic Tunnelling Services 
Prerequisites 
 
Requirement : 
Hardware 
The L2 GRE tunnel access and tunnel aggregation functionality are supported on the 
following OmniSwitch platforms: 
 
 
Software 
The GTTS feature needs the following prerequisites: 
AOS release 
8.4.1.R02 or greater 
AWOS release 
3.0.2.19 or greater

<<<PAGE 7>>>
7 
 
Application Note 
Guest Traffic Tunnelling Services 
Software & hardware used 
For the purpose of creating this document, the following hardware and software were 
used: 
HARDWARE 
SOFTWARE 
OS6900-V48C8 
8.9.78.R01 GA 
OS6900-X48C6 
8.9.78.R01 GA 
OS6900-T48C6 
8.7.98.R03 GA 
OS6900-T24C2 
8.9.78.R01 GA 
OS6900-X24C2 
8.9.78.R01 GA 
AP1201 
AOS R4.0.5.2038 MR 
AP1331 
AOS R4.0.5.2038 MR 
OmniVista 2500 NMS 
4.7R1 GA (Build 30) 
 
Architecture prerequisites 
Important: Carefully read this prerequisite chapter. Some mandatory architecture 
configurations must be followed to have the GTTS feature works. 
One ARP  
Each AP can only have ONE active tunnel at a time toward ONE tunnel aggregation switch. 
One AP can still have multiple active tunnels to as many as distinct tunnel aggregation switches. 
Each SSID is mapped to an Access Role Profile, which is itself mapped to a tunnel, and only one 
tunnel can be active at a time on the switch. 
In a more concrete way, if 3 SSIDs using the GTTS feature are broadcasted from an AP, each of 
them using a different Access Role Profile, this is mandatory to have at least 3 tunnel 
aggregation switches, one for each SSID. 
This is technically possible to have multiple SSIDs using the same Access Role Profile, thus the 
same tunnel at the end. But Access Role Profiles applied ACL and QoS rules, as well as the user 
VLAN, Captive Portal configuration and other more specific options. 
In a real scenario, creating multiple SSIDs using the same Access Role Profile have no benefits 
because all SSIDs will have at the end the same configuration, besides the SSID name and the 
association method. 
 
Layer 3 hop 
A layer 3 hop must exist between the far-ends APs and the tunnel aggregation switch. 
In other words, the management IP address of the AP must not be in the same subnet as the IP 
address sets as the GRE Tunnel Server IP while creating the SSID.

<<<PAGE 8>>>
8 
 
Application Note 
Guest Traffic Tunnelling Services 
 
Hairpin wire rate 
Given that all the traffic transits through the hairpin in the tunnel aggregation switch, the 
maximum bandwidth of the SSID is capped by the hairpin bandwidth. Additional hairpin can be 
configured as explained in the Redundancy chapter also increases the maximum bandwidth used 
for GTTS SSIDs. 
 
MTU size 
The MTU size must be in consideration when adding the GTTS feature. 
Given that GTTS use the L2GRE encapsulation, a total of 24 bytes are added to the packets (4 
bytes for GRE header + 20 bytes for IP header). 
An issue can occurs when the GTTS feature is used across a network belonging to another 
company. In that case, communication between the two network administrators must be done 
to authorize both networks to allow packets that are slightly larger. 
 
Auto-discover 
Before starting, we need to be sure that a very convenient feature is activated. The Auto-
discover feature allows switches to dynamically accepts tunnels for far-ends APs. 
Without this feature enabled, each far-end AP has to be manually set in the switch by adding 
their MAC address. 
By default, the auto-discover is enabled. You can be sure that it’s activated by entering the 
following command: 
service l2gre auto-discover enable 
 
Scalability 
The maximum number of active tunnels on a tunnel aggregation switch depends of the switch 
model. This number doesn’t go up if Virtual-Chassis is used: 
6900-Q32/X72 
1000 
6860; 6860N; 6865; 6900-X/T24C2 
2000 
6900-V72; 6900-C32; 6900-X/T48C6; 6900-X48C4E; 6900-V48C8; 6900-C32E 
6000

<<<PAGE 9>>>
9 
 
Application Note 
Guest Traffic Tunnelling Services 
Switch configuration 
The first thing to do is to create a service profile and disable some protocols that are usually 
used by an Access port: 
service l2profile "profile_name" stp drop gvrp drop mvrp drop 
 
We will now configure the first port of the Hairpin. We select a port and apply the service 
profile just created: 
service access port "X/X/XX" vlan-xlation enable l2profile "profile_name" description 
"description" 
 
The service corresponding to the tunnel has to be created. The service number is the process 
used by the switch locally, so anything can be chosen. The VPN ID, on the other hand, must be 
the same as configured during the SSID creation: 
service "service-id" l2gre vpnid "vpn-id" description "service_description" stats enable vlan-
xlation enable remove-ingress-tag enable 
 
Finally, we must map the service created to the SAP created, associating the correct VPN ID: 
service “service-id” sap port "X/X/XX":"vpn-id" 
 
Now that the SAP is created, the other side of the Hairpin needs to be configured. This is a 
regular Access port where we will add a VLAN: 
vlan “VLAN-ID” members port "X/X/XX" untagged 
 
Here follow you can find a configuration with actual ports, description and IDs, according to 
the configuration figure displayed in the AP Configuration chapter. The SAP port is 1/1/49A, 
and the ACCESS port is 1/1/50. The VLAN 50 is used for the ACCESS port, but this doesn’t have 
to be the same as the VPN ID. This is only for convenience reason: 
service l2profile "guest-l2profile" stp drop gvrp drop mvrp drop 
service access port 1/1/49A vlan-xlation enable l2profile "guest-l2profile" description "L2GRE 
Loopback Port" 
service 100 l2gre vpnid 50 description "guest" stats enable vlan-xlation enable remove-ingress-
tag enable 
service 100 sap port 1/1/49A:50 
vlan 50 members port 1/1/50 untagged

<<<PAGE 10>>>
10 
 
Application Note 
Guest Traffic Tunnelling Services 
AP configuration 
 
Important: The whole process of SSID creation will not be detailed in this document. 
During the SSID creation, instead of choosing a VLAN to be mapped to the SSID, the option Use 
Tunnel must be checked. 
After that, a configuration panel appears: 
- 
Tunnel ID: The Tunnel ID used in the process. This ID must be the same as configured in 
the switch. 
- 
GRE Tunnel Server IP Address/Data VPN Server: the IP address of the tunnel aggregation 
switch 
- 
Backup GRE Tunnel Server IP Address: the IP address of the secondary tunnel aggregation 
switch, in the case of the primary switch is not reachable. 
 
Note: Primary and Backup GRE Tunnel Server IP have no requirements to be or not to be in the 
same IP subnet. 
 
- 
Preemption: enabled to have the Primary switch become Primary again at the end of 
the timer while the Secondary switch is Master. 
- 
Preemption Countdown Timer: the timer which at the end the Primary switch become 
the Master of the tunnel, while the Secondary is currently the Master. 
 
Important: Support of Entropy MUST be Enabled for the used of the GTTS feature.

<<<PAGE 11>>>
11 
 
Application Note 
Guest Traffic Tunnelling Services 
Through multiple ways, one SSID can be mapped to multiple ARPs. In that case, the Expert 
mode must be used to create multiple ARPs and map them to as many of Tunnel Profile, which 
contains all the parameters to setup the L2 GRE tunnel. 
In this scenario, using only one SSID, different devices traffic can be tunneled to different end 
point tunnels, regarding of their classification. 
 
Scenarios 
Guest tunneling toward a Demilitarized Zone 
 
Introduction 
We will first see a very easy architecture to understand better how the GTTS works. We 
will demonstrate a usual case where we want to isolate the Guest traffic from others, by 
tunneling the traffic from the access device -the AP – to the DMZ where security policies 
are applied. 
In this figure, we can see three blocks representing logical 
networks, each of them divided thanks to firewalls: 
- 
Corporate: the internal network of a company. This 
is where corporate employees and external guests will 
connect to the network. 
- 
DMZ: The Demilitarized Zone is the place in 
between the Corporate network and the External 
network. This is where the content is located when it 
needs to be accessible from both Corporate and External 
networks, as web servers and some storage servers. 
- 
External: This is usually the Internet but can also 
be an SD-WAN network or an operator’s network that uses 
SPB or MPLS protocol. 
 
We now want to isolate the Guests traffic from 
Employees. This is not represented in this figure, but you 
can imagine multiple other SSIDs for other usages 
broadcast by the same APs. This can be a security issue if 
no action is taken. 
 
The Guest SSID is mapped to a tunnel configured with the 
tunnel aggregation switch as the endpoint, located in the 
DMZ. A DHCP server is part of this DMZ to deliver IPs to 
Guests located physically in the Corporate block, but their 
first open door is in fact on the tunnel aggregation switch 
inside the DMZ, enclosed by firewalls. All viruses, 
malware, and security breaches thereby are ineffective.

<<<PAGE 12>>>
12 
 
Application Note 
Guest Traffic Tunnelling Services 
Campus deployment 
 
Introduction 
More than one SSID broadcast across multiple locations can be tunneled from sites to a safe 
place enclosed by firewalls. 
 
The benefit is the same: students and teachers will each have their own SSIDs and tunneled to 
a single place. And while the traffic is tunneled, the malicious software cannot be spread on 
the network. The traffic will end on the switches in the DMZ, where security policies are applied 
which limit the risks of security breaches. 
 
A campus architecture can fit for companies, hospitals, education and more regarding the 
needs. The WLAN is usually the first method to access the network, and is used by multiple user 
populations. 
 
Architecture 
The following figure displays a campus architecture with one Data Center and multiple site 
location. The same SSIDs are most of the time broadcast in all sites to allow roaming for users. 
 
By using OmniVista, this is absolutely possible to tunnel the traffic from all location toward the 
Data Center. All you need to do is to have all APs part of the same AP Group, and apply the 
GTTS SSID configuration to this AP Group. 
All APs will broadcast the same SSID toward the same tunnel endpoint, making the deployment 
of secured tunneled SSID very easy in large environment. 
 
The tunnel aggregation switch configuration is nothing more than explained in the Switch 
configuration chapter.

<<<PAGE 13>>>
13 
 
Application Note 
Guest Traffic Tunnelling Services 
Multi-tenancy on a single tunnel aggregation switch 
 
Introduction 
The GTTS features fits very well with Service Providers. Each customer of a Service Provider 
can tunnel the traffic from their location to the Service Provider tunnel aggregation switch. 
By doing this, security is applied at the Access layer of a customer and ends up in the Service 
Provider network. 
 
Architecture 
This following displays a light view of the way that a Service Provider interacts with his 
customers. 
Each customer has their own AP Group, and potentially their own OmniVista. 
So each AP Group is thus configured with the tunnel aggregation switch IP address of the Service 
Provider. 
The tunneled traffic travels through the already established link between customers and the 
Service Provider. This link can be an SD-WAN network or an operator protocol, such as SPB or 
MPLS.

<<<PAGE 14>>>
14 
 
Application Note 
Guest Traffic Tunnelling Services 
GTTS redundancy designs 
 
Introduction 
One very important aspect of every functional network is the redundancy. The GTTS features 
implies a tunnel aggregation switch to work in the first place. 
We will see in this chapter a few solutions to avoid that this switch become a single point of 
failure of an architecture using the GTTS feature. 
 
Redundancy 0 
 
 
 
In this figure, no redundancy is configured.  
 
There is only one tunnel aggregation switch 
configured as the Primary, and one 
mandatory Hairpin. If either the switch, 
the Hairpin, or the connectivity between 
the Corporate switch and the tunnel 
aggregation switch fails, the GTTS SSID is 
not usable anymore.

<<<PAGE 15>>>
15 
 
Application Note 
Guest Traffic Tunnelling Services 
Redundancy 1 – Hairpin redundancy 
In this first redundancy scenario, a second 
Hairpin is created.  
 
There is still no redundancy regarding the 
switch and the network connectivity, but up 
to 1 SAP port and 1 ACCESS port can fail with 
no impact on the GTTS traffic. 
 
Note that the Hairpin redundancy is fully 
usable 
with 
the 
following 
scenarios 
Redundancy 
2, 
Redundancy 
3 
and 
Redundancy 4. 
 
Moreover, two Hairpins is not the maximum 
number that can be created. 
 
Configuration 
In order to do this, there are two link 
aggregations to create: one for the SAP 
side, the other for the ACCESS side. 
All the configuration regarding the SAP port 
is replaceable by “linkagg” instead of 
“port". 
Here follow you can find a configuration 
with actual ports, description and IDs: 
 
 
linkagg lacp agg 1 size 2 admin-state enable 
linkagg lacp agg 1 name "GTTS-HAIRPIN-1" 
linkagg lacp agg 1 actor admin-key 1 
linkagg lacp port 1/1/25 actor admin-key 1 
linkagg lacp port 1/1/26 actor admin-key 1 
linkagg lacp agg 2 size 2 admin-state enable 
linkagg lacp agg 2 name "GTTS-HAIRPIN-2" 
linkagg lacp agg 2 actor admin-key 1 
linkagg lacp port 1/1/27 actor admin-key 2 
linkagg lacp port 1/1/28 actor admin-key 2

<<<PAGE 16>>>
16 
 
Application Note 
Guest Traffic Tunnelling Services 
 
service l2profile "guest-l2profile" stp drop gvrp drop mvrp drop 
service access linkagg 1 vlan-xlation enable l2profile "guest-l2profile" description "L2GRE 
Loopback Port" 
service 100 l2gre vpnid 50 description "guest" stats enable vlan-xlation enable remove-ingress-
tag enable 
service 100 sap linkagg 1:50 
 
vlan 50 members linkagg 2 untagged 
 
Redundancy 2 – Primary & Secondary 
 
The next layer of redundancy is adding by 
using the Backup GRE Tunnel. 
 
At any point, if the AP cannot reach 
anymore the Primary tunnel aggregation 
switch, the tunnel mapped to the SSID 
will be opened on another tunnel 
aggregation switch. 
 
The convergence time in case of a 
failover from Primary to Secondary takes 
a few seconds. 
 
Configuration 
 
The Secondary tunnel aggregation switch 
configuration is the same as the Primary 
Switch. Be only sure that the VPN ID is 
the same as the Primary Switch, because 
this is the one used by the AP to open 
tunnels with the endpoints.

<<<PAGE 17>>>
17 
 
Application Note 
Guest Traffic Tunnelling Services 
To enable this redundancy, while configuring the SSID, the field “Backup GRE Tunnel Server IP 
Address” must be specified: 
 
 
 
The Preemption option can also be enabled if you want the Primary Switch to become Primary 
again after a first failover occurred. At the end of the specified timer, the AP will try again to 
reach the Primary Switch and transferred all current session to it. 
 
Redundancy 3 – Virtual-Chassis 
 
This redundancy scenario is similar to the previous 
one. We replace the Backup feature by using the 
Virtual-Chassis protocol. 
 
With this architecture, a failure can occur at the 
Hairpin, at the network connectivity, and at the 
tunnel aggregation switch level. All these parts are 
redundant. 
 
The use of the Virtual-Chassis instead of a Primary-
Secondary couple achieve a sub-second convergence 
time. 
 
Configuration 
A Virtual-Chassis first need to be created between the 
two tunnel aggregation switch. 
Then, we will again configure two link aggregations: 
one for the SAP side, the other for the ACCESS side. 
But the link aggregations will be configured across the 
members of the Virtual-Chassis.

<<<PAGE 18>>>
18 
 
Application Note 
Guest Traffic Tunnelling Services 
Here follow you can find a configuration with actual ports, description and IDs: 
 
linkagg lacp agg 1 size 2 admin-state enable 
linkagg lacp agg 1 name "GTTS-HAIRPIN-1" 
linkagg lacp agg 1 actor admin-key 1 
linkagg lacp port 1/1/25 actor admin-key 1 
linkagg lacp port 2/1/25 actor admin-key 1 
linkagg lacp agg 2 size 2 admin-state enable 
linkagg lacp agg 2 name "GTTS-HAIRPIN-2" 
linkagg lacp agg 2 actor admin-key 1 
linkagg lacp port 1/1/27 actor admin-key 2 
linkagg lacp port 2/1/27 actor admin-key 2 
 
service l2profile "guest-l2profile" stp drop gvrp drop mvrp drop 
service access linkagg 1 vlan-xlation enable l2profile "guest-l2profile" description "L2GRE 
Loopback Port" 
service 100 l2gre vpnid 50 description "guest" stats enable vlan-xlation enable remove-ingress-
tag enable 
service 100 sap linkagg 1:50 
 
vlan 50 members linkagg 2 untagged 
 
Redundancy 4 – One switch couple per SSID 
The highest level of redundancy is reached by having a couple of switches for each SSID. 
Couples of switches should be in different locations to prevent geographical failure. 
In that case, if a succession of failure occurred at the same time, or if an entire location is shut 
down due to external causes, only the SSID associated to it will be impacted. 
Both Primary-Backup and Virtual-Chassis features can be used to achieve this level of 
redundancy.

<<<PAGE 19>>>
19 
 
Application Note 
Guest Traffic Tunnelling Services 
 
Configuration 
The configuration is very 
similar to the previous cases 
we explored. 
 
There 
is 
the 
need 
of 
creating multiple Virtual-
Chassis, 
the 
link 
aggregations for SAP and 
ACCESS ports, and each SSID 
need to be configured to 
tunneled 
traffic 
toward 
each switch.