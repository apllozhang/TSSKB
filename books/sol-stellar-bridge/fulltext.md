<<<PAGE 1>>>
Network Solution Guide for Small-Medium Business 
Page 1 of 32 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
OMNIACCESS STELLAR 
BRIDGING/MULTI-POINT MESHING 
GUIDELINES 
 
Alcatel-Lucent Enterprise OmniAccess® Stellar WLAN AWOS 4.0.4 
Alcatel-Lucent Enterprise OmniVista® Cirrus 4.6.2

<<<PAGE 2>>>
Network Solution Guide for Small-Medium Business 
Page 2 of 32 
 
 
 
 
Table of Contents 
 
 
1. 
Introduction & Objectives......................................................................................... 5 
2. 
Architecting Bridging/Multi-Point Meshing ..................................................................... 5 
2.1 
Auto-Mesh ..................................................................................................... 7 
2.2 
Advanced Wireless Distribution System ................................................................... 7 
3. 
Use cases ............................................................................................................ 8 
3.1 
Outdoor bridging ............................................................................................. 8 
3.2 
Multi-Point outdoor Meshing .............................................................................. 10 
3.3 
Outdoor considerations .................................................................................... 11 
3.4 
Distances in 802.11ac/ax ................................................................................. 13 
3.5 
Multi-Point indoor meshing ............................................................................... 15 
4. 
Survey .............................................................................................................. 18 
4.1 
Ekahau PRO survey tool ................................................................................... 18 
4.2 
Link survey .................................................................................................. 18 
5. 
Configuration & Operation ...................................................................................... 20 
5.1 
Management in Enterprise mode ......................................................................... 20 
5.2 
Management with APUI .................................................................................... 25 
5.3 
Monitoring Mesh ............................................................................................ 27 
6. 
Related documents ............................................................................................... 32

<<<PAGE 3>>>
Network Solution Guide for Small-Medium Business 
Page 3 of 32 
 
 
 
Table of Figures 
 
 
Figure 1: Stellar Bridging/Multi-Point Meshing ........................................................... 6 
Figure 2: Advanced Wireless Distribution System ........................................................ 8 
Figure 9: Outdoor Bridging .................................................................................. 9 
Figure 10: Multi-Point outdoor meshing ................................................................. 10 
Figure 11: Outdoor considerations ....................................................................... 13 
Figure 5: Performances in LoS configurations .......................................................... 14 
Figure 7: Wireless Multi-Point indoor meshing ......................................................... 15 
Figure 13: Wireless Multi-Point meshing at Home ..................................................... 17 
Figure 15: AP placement with Ekahau PRO ............................................................. 19 
Figure 16: Link measurement with AP1361D ............................................................ 19

<<<PAGE 4>>>
Network Solution Guide for Small-Medium Business 
Page 4 of 32 
 
 
 
History 
 
 
Edition 01: 
802.11ax (Wi-Fi 6) Stellar AP1361/1362/1361D, AP1251,  
AP1322, AP1301 release 4.0.4 
OmniVista® Cirrus version 4.6.2 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Disclaimer 
 
This documentation is provided for reference purposes only and does not fully describe the capabilities 
of each Product and related features. Therefore, ALE International declines any liability for inaccuracies 
contained herein.  For an exhaustive view on features list and product limits for the current product 
release please see the required Feature List/Product Limits document available through the ALE eBusiness 
Portal web site. 
In the interest of continued product development, ALE International reserves the right to make 
improvements or other changes to this document and the products it describes at any time without prior 
notice. 
 
 
Copyright 
 
Copyright © ALE International 2022. Distribution of substantively modified versions of this document is 
prohibited without the explicit permission of the copyright holder.  
 
Distribution of the work or derivative of the work in any standard (paper) book form for commercial 
purposes is prohibited unless prior permission is obtained from the copyright holder.

<<<PAGE 5>>>
Network Solution Guide for Small-Medium Business 
Page 5 of 32 
 
 
 
 
1. Introduction & Objectives 
 
OmniAccess Stellar is an advanced wireless meshing solution for the enterprise with WLAN mesh 
technology that supports the latest Wi-Fi standards for mesh links and remote WLAN clients, and comes 
with an easy configuration that allows extensive, secure, scalable and high-speed coverage for areas that 
are difficult to connect to the wired LAN. 
 
Stellar Wi-Fi 6 access points offer versatility for the Bridging/Multi-meshing solution. They are designed 
for demanding environments such as urban, terrains etc. and more specific deployments such as factories, 
warehouses. They offer many options at remote sites such as additional downlink ports and local PoE for 
remote equipment. Stellar mesh with Wi-Fi 6 access points enables the provision of mobility at a 
controlled cost for indoor and outdoor coverages, outdoor Wi-Fi 6 access points can support different 
installations configurations with different antennas and accessories. 
 
A Stellar mesh cluster can be managed in both Wi-Fi Enterprise and Wi-Fi Express modes. Now with Wi-Fi 
Enterprise Mode with Omnivista, it is simply a matter of identifying Stellar access points to be included 
in a meshing configuration to form mesh group from group of APs already managed via Omnivista. The 
Enterprise mode with Omnivista allows you to manage the group of APs for meshing, manage the RF for 
the group, manage the transport of various VLANs to the remote sites, manage SSIDs broadcasted and 
QoS to the remote clients, as well as the management of the different remote ports available on APs. 
 
This guide is intended to help Network engineers, Presales and Sales engineers in the design of Stellar 
solutions incorporating Bridging/Meshing topologies and in implementing and maintaining meshing 
network in their enterprise environment using Omnivista 2500. 
 
 
2. Architecting Bridging/Multi-Point Meshing 
 
OmniAccess Stellar is a Multi-Point mesh architecture in high-availability mode. 
 
The Stellar mesh access points form a cluster of routers but with no cabling between the different access 
points and form Point-to-Point mesh links that do not need to be routed to a LAN port. Each mesh access 
point passes data from one access point to another, transferring it according to the Wi-Fi mesh link 
defined in each access point. The mesh infrastructure thus defined is fixed. 
 
OmniAccess Stellar Access points can have 2 roles in a cluster, a mesh role that defines the access point 
as a mesh node in the cluster and a root role that defines the access point as a gateway to the LAN.

<<<PAGE 6>>>
Network Solution Guide for Small-Medium Business 
Page 6 of 32 
 
 
 
 
All data traffic of a Stellar mesh infrastructure is forwarded from/to the gateway (access point with root 
role) connected on the LAN. Stellar mesh supports the duplication of the root role, if two access points 
are configured root in the same AP group, the mesh access points will connect to the root access point 
that has the best RSSI for the mesh link. 
 
 
Figure 1: Stellar Bridging/Multi-Point Meshing 
 
 
This architecture allows two configurations: 
 
- The distribution of corporate VLANs over a mesh link. The Bridge configuration is the typical use case 
of a Point-to-Point mesh configuration and certainly the most used configuration in Enterprise that 
enables to extend the corporate LAN to some remote sites or buildings. The Bridge delivers only one mesh 
link and only one mesh access point (Bridge configuration) is attached to the remote site. There is no 
broadcast of SSID to deliver WLAN services to remote Wi-Fi clients and all corporate LAN is bridged at the 
remote site. 
 
- The configuration of a Multi-Point wireless for areas where cabling is not possible. Typical Multi-Point 
installations are outdoor industrial sites, events sites, terrains etc. but also indoor configurations like 
WLAN mesh installations in factories, storage buildings, warehouses or even at home.

<<<PAGE 7>>>
Network Solution Guide for Small-Medium Business 
Page 7 of 32 
 
 
 
 
The bandwidth of a mesh link is shared between mesh backhaul and wireless client traffic. On dual and 
tri-radio 2.4GHz/5GHz Stellar Wi-Fi 6 access points the mesh backhaul can be configured on the 5GHz 
band or the 2.4GHz band and the WLAN services can be delivered on both 2.4GHz/5GHz radios. 
 
In the case of Multi-Point meshing, each mesh access points communicates with the root gateway and 
with WLAN clients using the same channel and radio and therefore the wireless throughput is divided by 
2 at each mesh node for the data traffic that must be retransmitted to reach the wired LAN. 
 
The distances between Stellar access points of a mesh cluster play a crucial role in the performance of 
the mesh link, especially for the bandwidth available for such type of link which is shared. There is always 
a trade-off between distance and link performance, and this point of architecture is developed more 
specifically further for outdoor configurations where the impact of distance is important (see use cases 
outdoors) 
 
 
2.1 Auto-Mesh 
 
To help with configurations from scratch, Stellar access points also support an Auto-Mesh feature where 
the administrator only needs to activate a Stellar access point connected to the LAN/WAN in root mode. 
Any AP from scratch booting without a connection to the LAN and in the neighbourhood of this root AP 
will attempt to connect as a Mesh Access Point using the default mesh link. 
 
2.2 Advanced Wireless Distribution System 
 
OmniAccess Stellar access points operate in advanced Wireless Distribution System (WDS) mode. Each 
access point in the mesh cluster operates as a station in WDS mode, this allows for transparent Ethernet 
bridging across APs, a common broadcast domain for all devices connected across wireless connections 
and the transport of different corporate VLANs. 
 
When WDS is used, the access points switch to 4-MAC addresses format available in 802.11 instead of the 
3 addresses used in a normal client-access point traffic. The LAN device sends a packet to the bridge 
device and the 802.3 frame is relayed through the client WDS AP. 
The WDS AP redirects the frame to the bridged device using the second 802.11 MAC source. The equipment 
responds using 802.3 MAC source as destination. The WDS AP relays the frame to the destination using 
the second 802.11 MAC destination. The connection between the two devices is established at 802.3 level. 
 
The WDS mode is supported for Bridge and Multi-Point mesh configurations.

<<<PAGE 8>>>
Network Solution Guide for Small-Medium Business 
Page 8 of 32 
 
 
 
 
Figure 2: Advanced Wireless Distribution System 
 
 
 
The management of complementary ethernet ports of mesh access points is supported in Enterprise mode, 
it is possible to transport different corporate VLANs, tagged or untagged, and to forward them to different 
defined ports on the AP that will serve as downlink ports for the wired remote client traffic. 
Downlink port functionality managed on Omnivista 2500 will be supported with advantage on Stellar 
access points that have an additional Gigabit Ethernet port such as AP1361/1362/1361D outdoor access 
points. 
 
ENET1 port of AP1361/1362/1361D additionally handles the POE PSE output to provide 802.3af/at POE 
output for remote connected equipment at mesh access point. 
 
 
3. Use cases 
 
3.1 Outdoor bridging 
 
The wireless bridge is the most requested use case in Enterprise, it connects two distant buildings and 
extends the whole enterprise LAN where it is not possible by cabling. This is typically the case when 
crossing a public access like a street or avenue. It is a Point-to-Point configuration and typically an 
external installation. 
 
There is no broadcasting of WLAN services to remote Wi-Fi clients in Bridge mode. Each access point is 
managed in Bridge mode and connects its radio to the ethernet port ENET0 of the AP. The Bridge extends 
the LAN and distributes the corporate VLANs on the different ports of the bridge access point, by default 
on Ethernet port ENET0 but also on the PSE ethernet port ENET1 to power some PoE equipment, typically 
like an IP camera, this without having to use an additional PoE injector. 
 
In Wi-Fi Enterprise mode, Access Role Profiles (ARP) are generally already assigned for each VLAN, which 
allows you to define a role for each VLAN with the appropriate ACLs and QoS enforcements or define a 
role on a particular port on the bridge access point.

<<<PAGE 9>>>
Network Solution Guide for Small-Medium Business 
Page 9 of 32 
 
 
 
The radio topology is typically Line of Sight (LoS) and requires a careful installation of antennas and 
access points. The bridge is usually installed on the roof of a building to meet the installation and height 
requirements for this type of configuration. 
 
 
 
 
 
 
Figure 3: Outdoor Bridging 
 
3.1.1 
Prerequisites 
 
- 
1 access point as bridge 
- 
The Bridge root can be dual 
- 
It is not recommended to configure multiple Bridge APs within a same Bridge, if there is two 
Bridge AP in the setup, the AP downlink will connect to the bridge AP with best RSSI. 
- 
5GHz band is the preferred band to exploit 802.11ac technologies (MIMO, MU-MIMO, TxBF) and 
802.11ax technologies (extended MU-MIMO, OFDMA, Extra Range and long Guard Interval features 
for outdoor infrastructures).  
- 
Bridging mode is intended to connect two distant managed sites over wireless and then intended 
to outdoor infrastructures only  
- 
Use only directional antennas or highly directional antennas for outdoor bridging  
- 
MU-MIMO antennas (usually with dual slant + -45 °, vertical & horizontal polarization) are 
recommended for the performance of bridge APs. It is important to keep the same type of 
antennas and polarization for the two antennas of the link 
- 
Keep same APs series to configure a bridge ie. use 802.11ax access points to benefit to 802.11ax 
technology.  
- 
Due data traffic over the Bridge, share the 5GHz band with wide bandwidth modes, 40MHz mode 
and more are recommended in 802.11ac/ax.  
- 
Transport of 0-4095 tagged VLANs

<<<PAGE 10>>>
Network Solution Guide for Small-Medium Business 
Page 10 of 32 
 
 
 
 
3.1.2 
Supported access points 
 
Outdoor IP67 rated AP1361/AP1362/AP1361D (Wi-Fi 6). Note indoor AP1322 (Wi-Fi 6) with external patch 
antenna are also supported for bridging mode indoors. 
Outdoor IP67 rated AP1251 and indoor AP1222 (Wi-Fi 5).  
 
 
 
3.2 Multi-Point outdoor Meshing 
 
Multi-Point meshing is the use case in Enterprise where we want to carry out extensions of the network 
in places where the cabling remains difficult of access in certain parts of the company. This type of 
deployment can be done outdoors (industrial, event venues, campgrounds etc.) but also indoors (factories, 
warehouses, storage etc) with the necessary prerequisites for outdoor installations. 
Stellar allows Multi-Point mesh configurations from a root access point that can be redundant as in the 
case of the Bridge. In Multi-Point mode the root AP and each mesh access point can broadcast WLAN 
services to remote Wi-Fi clients. Each AP mesh connects its Wi-Fi clients and additionally its different 
ports to connect remote equipment (depending on the model). 
 
 
 
 
 
 
Figure 4: Multi-Point outdoor meshing

<<<PAGE 11>>>
Network Solution Guide for Small-Medium Business 
Page 11 of 32 
 
 
 
3.2.1 
Prerequisites 
 
- 
Maximum of 16 mesh access points for mesh configuration 
- 
The Mesh root can be dual 
- 
There is no combinatory possible between Bridging topologies and Meshing topologies 
- 
5GHz band is the preferred band to exploit 802.11ac technologies (MIMO, MU-MIMO and TxBF) 
and 802.11ax technologies (extended MU-MIMO, OFDMA, Extra Range and long Guard Interval for 
outdoor infrastructures).  
- 
Use only omnidirectional or semi-directional MIMO antennas for mesh root access point 
 
- 
nLoS configurations are possible, in case of semi-directional antenna use for root access point, 
consider a loss of at least 3dB at the limit of beamwidth for the placement of mesh APs. 
- 
MU-MIMO antennas (usually with dual slant + -45 °, vertical & horizontal polarization) are 
recommended for the performance of mesh APs. It is important to keep the same type of 
antennas and polarization for each antennas pair in links 
- 
Keep same APs series to configure a mesh ie. use 802.11ax access points to benefit to 802.11ax 
technology.  
- 
Due data traffic over the mesh link, share the 5GHz band with wide bandwidth modes, 40MHz 
mode and more, are recommended in 802.11ac/ax.  
- 
Transport of 0-4095 tagged VLANs 
 
3.2.2 
Rules at mesh access point 
 
Any Point to Multi-Point meshing deployment comes with some rules on each mesh AP that requires 
attention from the beginning of the deployment:  
- 
Any Mesh AP connector can broadcast 5 client WLAN services maximum.  
- 
Any AP adjacent to the root, with factory setup and without a LAN connection, will attempt to 
connect first as a mesh access point and carry over the client SSIDs of the root access point. 
- 
The Global call transit capacity of a Mesh root AP has to be shared between all mesh access 
points and clients traffics. The bandwidth will be then divided by 2 on a mesh access point for 
each SSID traffic. 
- 
There is no roaming between mesh APs, there is no handling of PMK/OKC or keys exchanges 
handling through mesh access points. 
- 
VoIP and real-time applications are carried in best effort mode only. 
 
3.2.3 
Supported access points 
 
Outdoor IP67 rated AP1361/AP1362/AP1361D (Wi-Fi 6).  
Outdoor IP67 rated AP1251 (Wi-Fi 5). 
AP1361 and AP1251 access points can be mounted on a pole to achieve the same coverage as indoor 
coverage for their Wi-Fi clients, the configuration with root could be nLoS in this case. 
 
 
 
3.3 Outdoor considerations 
 
An outdoor Bridge or Mesh installation needs to be planned and there are several points to consider for 
this type of installation.

<<<PAGE 12>>>
Network Solution Guide for Small-Medium Business 
Page 12 of 32 
 
 
 
3.3.1 
Antennas placement and installation 
 
The placement of the antennas and possible radio obstructions must be considered at the beginning of 
the installation. In the case of a bridge the antennas must be placed as high as possible and comply with 
local regulations in terms of radio emissions. 
 
 
 
The possible obstructions have to be identified (trees or other buildings) and in general the height of the 
installation must take into account the height of the obstructions to which a minimum distance is added 
to have a sufficient clearance of Fresnel zone for the link. Usually at least 60% minimum of clearance is 
considered for the Fresnel zone. Rooftop installations are recommended whenever possible.  
 
The antennas should be aligned in such a way that the main radiation lobes are facing each other, as 
typical Line of Sight (LoS) configuration.  
 
Consider all mounting possibilities and site constraints to make the correct choice of mounting kit for the 
antennas. Specially consider mast/pole, pole/reverb, wall and building facade mounts as necessary with 
accessible heights. 
 
3.3.2 
Regulations 
 
From a regulatory point of view, an installation must comply with the local authorities (civil aviation and 
local administrative authority). The channels used for links also must comply with local legislation. 
 
3.3.3 
Protection 
 
Voltages and currents caused by lightning or currents and electrostatic charges which can occur on 
outdoor antennas present a safety hazard to outdoor installations, and a possible risk of electric shock or 
fire. These risks are reduced by surge protection and a proper grounding of the installation. Some best 
practices for electrical installations outdoors can be retrieved in TIA drafts listed in TIA-6076B as example. 
 
3.3.4 
Accessories 
 
OmniAccess Stellar AP outdoor mounting kits are supplied separately and can be found in ALE network 
catalog. The mast kit is supplied with AP1251 and AP1361/1362/1361D access points. 
 
POE injectors for outdoor access points must be IP67 rated and must provide enough power to supply 
802.3af/at to the access point but also to the PD equipment if powered by the AP. These devices need a 
local power outlet to provide 802.3af/at but also 802.bt for the newer Wi-Fi 6 access points. They also 
inject Ethernet traffic for the AP and usually have power protection to protect the network. 
 
Lightning arrestors can also be added between the antenna and the access point.

<<<PAGE 13>>>
Network Solution Guide for Small-Medium Business 
Page 13 of 32 
 
 
 
 
 
Nomenclatures in ALE catalog are as follows to help with some kit/accessory references for outdoors: 
- 
AP-MNT-OUT-H  
 
 
Outdoor mount kit for Stellar AP1361/1362/1361D 
- 
PD-9001GO-ET/AC /PD-9601GO/AC  
Outdoor PoE injectors for Stellar AP1361/1362/1361D 
- 
PD-OUT/MBK/ET /PD-OUT/MBK/S  
Pole/Wall mount kit for outdoor PoE injectors 
- 
PWR-CORD-XX          
 
 
Power cords for outdoor PoE injectors (country specific) 
- 
AP-OUT-SFP-KIT        
 
 
SFP outdoor kit for Stellar AP1361/1362/1361D 
 
Note 2” Pole mount kit is included with ANT-O-M2-5/ANT-O-M4-9 antennas. 
 
 
 
 
Figure 5: Outdoor considerations 
 
 
 
3.4 Distances in 802.11ac/ax 
 
The throughput of a mesh link declines significantly with the distance between the access points of the 
link. The installation of an 802.11ac/ax mesh link is often a compromise between distance and link 
performance. 
 
In the table below performances are indicated for Stellar Line of Sight (LoS) configurations on the 5GHz 
band. They are typically the performances for a bridge link with the 40MHz mode considered as the 
minimum channel width to have as shared bandwidth on the link. The values in the table are given as an 
indication for the different Stellar outdoor topologies and are based on:

<<<PAGE 14>>>
Network Solution Guide for Small-Medium Business 
Page 14 of 32 
 
 
 
- 
A RF calculation for the optimal distance between 2 APs. The calculation is based on the RF 
link budget for each Stellar AP and antenna type. The calculation takes in account the RF Free 
Path Loss (RFPL) and a margin of 10dB for the System Margin (SOM) for the receiver. This value 
is usually adopted by default to consider possible radio fluctuations due to external conditions 
encountered on a bridge link, for example like wind, rain etc. 
- 
The capacity of each AP on the 5GHz band in 40MHz mode with a speed estimation (speed 
values are from Ekahau PRO planner) 
 
The 80MHz channel width can also be considered with interest over shorter distances. 
 
 
 
 
 
 
Figure 6: Performances in LoS configurations 
 
 
 
3.4.1 
Long distances considerations 
 
Longer distances (1/5 mile and more) can also be considered but only with high gain, MIMO compatible 
directional antennas, and with also with lower HE/HT data rate negotiation. Long distances may be 
suitable for applications where the data rate is not the priority, pure voice applications may be a use 
case.

<<<PAGE 15>>>
Network Solution Guide for Small-Medium Business 
Page 15 of 32 
 
 
 
 
 
The use of external high gain antennas from the market of the grid/parabolic type can be considered if 
they are compatible with: 
- 
Wi-Fi frequency bands including the 5GHz 
- 
MIMO compatible with polarization diversity (a 2x2 MIMO antenna configuration is minimum for 
polarization diversity) 
- 
Impedance of 50 ohms 
- 
Limited cable loss (< 1.5dB) 
- 
N-type connector 
- 
DC grounding 
 
Always refer to the manufacturer's datasheets for this type of antenna before performing a link budget 
for long distances, as previously done in the table for Stellar installations. 
 
 
 
 
3.5 Multi-Point indoor meshing 
 
 
3.5.1 
Multi-Point indoor meshing Enterprise 
 
Indoor meshing is generally used for wifi deployments and coverage extensions for some hard-to-reach 
parts of buildings. This is the case for factories and certain industrial areas. 
 
 
 
Figure 7: Wireless Multi-Point indoor meshing

<<<PAGE 16>>>
Network Solution Guide for Small-Medium Business 
Page 16 of 32 
 
 
 
 
The RF requirements for indoor meshing are similar to indoor coverage for offices: 
- 
SNR of 20dB, or better for voice  
- 
RSSI of at least -67dBm 
 
It is recommended to use omni-directional and external antennas with sufficient antenna gain to 
guarantee the quality of the mesh links, e.g. the use of the external omni-directional ANT-O-6 antenna 
mounted directly on the Stellar AP1322 (or AP1222) is a good practice. 
The AP1361 or AP1251 are IP67 rated and are also used and mounted on the ceiling in case of harsh 
environment (humidity, dust, etc.). 
Patch antennas are not recommended for indoor mesh, they are more recommended for specific indoor 
coverage. 
 
 
3.5.2 
Multi-Point indoor meshing at Home 
 
It is also possible to have a mesh configuration at home with Enterprise level connectivity in rooms where 
Wi-Fi coverage is desired. This type of deployment is accelerating with homeworking today. With the 
shorter distances in home, Stellar multi-point mesh can provide higher throughput links and set up optimal 
Wi-Fi performance with the latest entry-level Wi-Fi 6 access points, such as AP1301. The Stellar Wi-Fi 6 
mesh provides fast Internet access to equipment with the latest Wi-Fi and security standards. 
 
In addition to the router, the Stellar Root mesh communicates with several mesh APs placed in different 
rooms of the house, office, living room or other, with the lightest possible installation. The group of APs 
uses the DHCP server of router and is managed in Wi-Fi Express mode. The management is done by the 
Express mode GUI, access point by access point, from a simple smartphone or tablet. 
With a single SSID broadcast and a password, roaming from room to room is possible for different types 
of equipment on both bands: 
- 
Laptop connecting on the 2.4GHz band 
- 
Smartphones connecting on 5GHz and supporting the latest Wi-Fi 6 standard (802.11ax) 
- 
Connection to Google Chromecast on 5GHz which allows to realize the broadcast of multimedia 
content 
- 
And potentially the connection for other Wi-Fi equipment (gaming consoles etc.) 
- 
Benefit of high data rates on 5GHz band with wide channels (80MHz) for latest smartphones 
(Dual band Wi-Fi 6), connected TV or consoles. 
 
 
Prerequisites at home: 
- 
Root AP must be placed close to existing router box and will be connected on router itself. Wi-
Fi service of router can be disabled. 
- 
Use of standard DHCP server of router 
- 
Once configured the placement of the mesh APs is done where the Wi-Fi coverage is required. 
The recommended distance limit for the mesh link is no more than 2 rooms (5 meters). It is 
important to consider how to connect equipment such as consoles, TVs and other devices for 
the placement.

<<<PAGE 17>>>
Network Solution Guide for Small-Medium Business 
Page 17 of 32 
 
 
 
 
- 
Level-entry AP1301 provides the latest Wi-Fi 6 technology on both radio bands and gives the 
benefit of a high-performance LAN connection at a distance of 3-5 meters with high data rates. 
- 
Wall mounting kit is sold under OAW-AP-MNT-W reference as well as 48V block on the market. 
A power outlet near the installation is sufficient. Both accessories allow a clean and definitive 
installation. 
- 
In case Stellar mesh is used for video streaming, or to connect game consoles, the use of 
specific SSID with QoS specific to these media is recommended. The QoS is directly managed by 
SSID in Stellar Express mode. 
 
 
 
 
 
Figure 8: Wireless Multi-Point meshing at Home 
 
 
3.5.3 
Rules at mesh access point 
 
Rules at each access point are the same as for outdoor Multi-Point meshing:  
 
- 
Maximum of 16 APs in a mesh configuration to one Root AP 
- 
Any Mesh AP connector can broadcast 5 client WLAN services maximum 
- 
Any AP adjacent to the root, with factory setup and without a LAN connection, will attempt to 
connect first as a mesh access point and carry over the client SSIDs of the root access point. 
- 
Global call transit capacity of a Mesh root AP has to be shared between all mesh access points 
and clients traffics. The bandwidth will be then divided by 2 on a mesh access point for each 
SSID traffic. 
- 
There is no roaming between mesh APs, there is no handling of PMK/OKC or keys exchanges 
handling through mesh access points. 
- 
VoIP and real-time applications are carried in best effort mode only. 
 
3.5.4 
Supported access points 
 
Indoor AP1301/AP1311/AP1321/AP1322/AP1331/AP1351/AP1361 (Wi-Fi 6) are supported for Multi-Point 
meshing in indoor.  
Indoor AP1201/AP1221/AP1222/AP1231/AP1232/AP1251 (Wi-Fi 5) are also supported.

<<<PAGE 18>>>
Network Solution Guide for Small-Medium Business 
Page 18 of 32 
 
 
 
 
 
4. Survey 
 
4.1 Ekahau PRO survey tool 
 
A survey is essential for planning an outdoor mesh installation and becomes mandatory in the case of 
bridge installation. It allows a simulation of the mesh links and provides an estimate of the performance 
that can be expected with Stellar meshing, especially concerning throughputs. 
 
Ekahau PRO Site Survey version 10.4 now includes Wi-Fi 6 Alcatel-Lucent Stellar AP1301, AP1301H, 
AP1311, AP1321, AP1322, AP1331, AP1351, AP1360 series with external outdoor and indoor antennas. 
- 
Antennas ANT-O-6, ANT-O-M2-5, ANT-O-M4-9 and ANT-S-M4-60 
 
The Ekahau planner tool is perfectly suited for outdoor mesh link calculation. The site survey software 
can be provided by ALE as a service for a coverage survey and helps the quotation of the installation. 
 
4.2 Link survey 
 
If distances calculation given earlier for a bridge allow to know the distances for a given WLAN technology 
(e.g. an installation with 802.11ax access point) it is possible to obtain specifically requested results in 
terms of throughput and AP placement, and thus evaluate the feasibility of an installation needed for the 
customer. 
 
The Ekahau PRO planner tool allows: 
- 
To simulate the radio propagation of each access point in the mesh group according to: the 
associated antenna parameters, the configuration of the access point, including the transmitted 
power and EIRP (power radiation), the placement to be expected for the access point and the 
radio settings that have been defined for it (number of MU-MIMO spatial streams, guard interval 
value, etc.) 
- 
To provide an estimate of the link in terms of throughput, but also in terms of the quality of the 
link, this estimate is usually based on the received power and the SNR level at the remote AP. 
 
The figure below shows, for example, the placement of a directional AP1361D made with the Ekahau 
Planner tool, for the recommended 802.11ax distance for this outdoor AP with integrated antennas. This 
placement can be fully adapted to the floor plans and site information provided by the partner.

<<<PAGE 19>>>
Network Solution Guide for Small-Medium Business 
Page 19 of 32 
 
 
 
 
Figure 9: AP placement with Ekahau PRO 
 
 
The following figure shows some performance measurements obtained for the AP1361D 
placement seen previously; the configuration here is 802.11ax enabled on the 5GHz band using 
the channel 106 (the shared bandwidth is 80MHz for this channel) and using 4x4 MU-MIMO 
spatial stream with a MCS5 QAM64 modulation negotiated for a wireless HE of more than 1Gbps 
wireless for the link. This clearly shows the performance achieved for this type of link in 
802.11ax. 
 
 
 
Figure 10: Link measurement with AP1361D

<<<PAGE 20>>>
Network Solution Guide for Small-Medium Business 
Page 20 of 32 
 
 
 
 
This type of survey can be carried out for any type of link, for external bridge links or for Multi-point 
mesh links. 
 
5. Configuration & Operation 
 
5.1 Management in Enterprise mode 
 
In this part we cover the procedure for managing an indoor mesh with Omnivista 2500, consisting of 2 
Stellar APs. The topology will be as follows: 
 
 
 
 
5.1.1 
Topology 
 
Stellar access points form by default a standard AP group with the management of one or more AP group(s), 
RF profile(s) and access profiles, which is the management process done usually with Omnivista 2500 for 
Stellar access points. The creation of a mesh group consists of specializing certain APs in the installation 
to operate in root or mesh mode.  
 
Identify the APs that will be part of the mesh group 
OV2500 -> NETWORK -> AP REGISTRATION -> Access Points

<<<PAGE 21>>>
Network Solution Guide for Small-Medium Business 
Page 21 of 32 
 
 
 
If IP configuration for APs is done by DHCP it is recommended to define IP reservations for all the APs of 
the future mesh group, and ideally to manage a static IP configuration in the case of a bridge. 
 
It is recommended to create a dedicated mesh (or bridge) AP group and assign it to the identified APs. 
OV2500 -> NETWORK -> AP REGISTRATION -> AP Group -> + (Create icon) 
 
 
 
- Enter AP Group Name and configure the profile as described below 
Time 
 
 
- Local time with UTC time zone 
SSH login 
 
- Enabled for Support account and for root account 
AP WEB  
 
- Enabled for Administrator account 
 
 
Wireless mesh/bridge working frequency, regulatory, channeling, transmission powers for indoor and 
more (notably for 802.11ax activation and long GIs as necessary) must be the same for all APs of the Mesh 
group (or Bridge).  
It is recommended to create a dedicated RF profile for the mesh (or bridge). 
OV2500 -> WLAN -> RF Management -> RF Profile -> + (Create icon) 
 
 
 
- Enter RF Profile Name and configure the profile as described below ie. FR-France in the example 
Country/region  
- FR-France 
Band steering  
- Enabled Force 5GHz 
Load balance 
 
- Enabled  
 
 
 
Airtime Fairness 
- Enabled on 2.4GHz and 5GHz

<<<PAGE 22>>>
Network Solution Guide for Small-Medium Business 
Page 22 of 32 
 
 
 
Background Scanning  - Disabled select Wi-Fi 6 non-working channel  
Band 
 
 
- Select 2.4GHz and 5GHz all 
Channel DRM 
 
- Enabled for 5G All 
Channel List  
 
- Set list [100,104,108,112] for 5GHz All 
Channel width  
- 80MHz for 5G All 
Power setting  
- Set DFS/TPC to 15dBm for 5G All indoor 
MU-MIMO 
 
- Enabled 
High Efficiency  
- Enabled 
 
- Apply this RF Profile to the Mesh AP Group 
 
 
Manage the SSIDs to broadcast for clients in a Multi-point mesh configuration. Create each SSID to 
broadcast to clients in the mesh configuration and assign them to the Mesh AP Group. 
OV2500 -> WLAN -> SSIDs -> + (Create icon) 
 
 
 
- Enter SSID Service Name and configure the profile as described below.  
SSID 
 
 
- SSID storage 
Security Level  
- Personal 
Allowed Band 
 
- All 
Encryption Type 
- WPA3 SAE AES 
Password 
 
- ********** 
Default VLAN/Network - Set Untagged VLAN and VLAN 94 (example here) 
 
Save and Apply to the AP Group mesh.  
- In Advanced WLAN Service Configuration configure as described below. 
- HT Control 
 
- Enabled for A-MSDU /A-MPDU (by default) 
 
In the case of multiple VLANs identify ARP profile(s) that will handle the VLANs to be distributed over the 
wireless mesh link. Assign the management VLANs to the mesh access points that can authenticate 802.1x 
clients (not the use case here)

<<<PAGE 23>>>
Network Solution Guide for Small-Medium Business 
Page 23 of 32 
 
 
 
5.1.2 
Mesh roles 
 
In this section all identified access points for the meshing are moved to their respective mesh roles. From 
the list of access points, select each access point for meshing (or bridge) and edit the Mesh Configuration 
menu. 
OV2500 -> NETWORK -> AP REGISTRATION -> Access Points -> (Select AP and Edit details /Edit Mesh Configuration) 
 
 
 
- Select Storage1 AP as Root and configure the Mesh configuration as described below.  
MESH Enable 
 
- Yes 
Is Root  
 
- Yes 
SSID 
 
 
- Stellar-MESH 
Band 
 
 
- 5GHz 
 
 
 
 
 
- Select Storage2 AP as Mesh and configure the Mesh configuration as described below.  
MESH Enable 
 
- Yes 
Is Root  
 
- No 
SSID 
 
 
- Stellar-MESH 
Band 
 
 
- 5GHz 
 
 
At this point in the management all mesh APs are configured and can be disconnected from the former 
LAN. They can be placed in their respective locations in the buildings: typically with a ceiling mounting 
in indoor (or roof mounting in the case of the bridge) and powered up. A boot with the initialization of 
the mesh configuration takes several minutes.

<<<PAGE 24>>>
Network Solution Guide for Small-Medium Business 
Page 24 of 32 
 
 
 
 
 
Once each root and mesh AP are managed and running, you can doublecheck mesh configuration is running 
on APs with mesh icons highlighted on Stellar topology. 
 
 
 
5.1.3 
Downlink ports 
 
In the case of a bridge, management of the additional Ethernet ports ENET0/1 of the APs as downlink 
ports for wired traffic from remote sites is done by managing a uNP authentication profile for the bridge. 
A uNP authentication profile allows you to assign a predefined uNP port configuration and to individually 
specify on each port an UNP port status and define the authentication process parameters for the ports. 
 
OV2500 -> UNIFIED ACCESS -> UNIFIED PROFILE -> Template -> Access Auth Profile -> + (Create icon) to create uNP 
configuration for Bridge APs downlink ports.

<<<PAGE 25>>>
Network Solution Guide for Small-Medium Business 
Page 25 of 32 
 
 
 
 
- Enter a Profile Name and configure the profile as described below.  
Default Settings  
 
- AP Mode 
- Disabled 
No Auth/Failure/Alternate  
– Trust tag 
- Enabled 
- Bypass VLAN - [VLAN list to bypass] 
 
 
- Save and Apply this uNP authentication Profile to the Mesh AP Group (with Apply to Devices button) 
 
 
- Select ports on which you want to assign this uNP authentication Profile and apply 
 
 
 
5.2 Management with APUI 
 
For AP groups managed in Express mode, the management of each mesh AP is done directly via their APUI 
interface which is accessible by clicking on @IP of each access point listed in the former cluster. 
WEB GUI (Main Page) -> AP 
 
 
 
Stellar APUI is also accessible in Enterprise mode from the menu OV2500 -> NETWORK -> AP 
REGISTRATION -> Access Points. Select the AP to be managed from the access point list and click on the 
Action -> AP web menu. AP web access has been previously activated in dedicated mesh AP group. APUI 
login is the administrator login for the group.

<<<PAGE 26>>>
Network Solution Guide for Small-Medium Business 
Page 26 of 32 
 
 
 
 
 
 
Edit Mesh Configuration menu with APUI 
 
 
Connect to APUI of AP identified as Root(s)/Mesh(s) and Access to  
APUI -> NETWORK -> AP INTERFACE -> Backhaul0 -> (Click Edit Interface) 
 
 
- Enable and Set AP mesh role you want for this AP (Mesh/Bridge/Is Root) and Mesh SSID settings 
(Band/passphrase) and Save 
 
 
Edit Ports Configuration menu with APUI 
 
 
Connect to APUI of AP identified as Root(s)/Mesh(s) and Access to  
APUI -> NETWORK -> AP INTERFACE -> Enet0/1/2/3 -> (Click Edit Interface) 
 
 
- Enable the Interface you want for this AP and set VLANs you want to trust and bypass and Save

<<<PAGE 27>>>
Network Solution Guide for Small-Medium Business 
Page 27 of 32 
 
 
 
5.3 Monitoring Mesh 
 
During Mesh operation all wireless metrics for each Mesh AP (or Bridge ones) are accessible from SSH 
console of APs. In Enterprise mode Stellar SSH console access must be activated in AP group dedicated to 
Mesh.  
OV2500 -> Network -> AP Registration -> AP Group -> (Select mesh AP Group and click the Edit button) 
 
 
- Configure the AP Group as described below.  
SSH  
- SSH Login 
 
- Enabled 
 
- For Root Account 
- password for root account 
 
 
5.3.1 
RF configuration 
 
Monitoring the RF configuration received by each AP in a Mesh group is done by retrieving rfprofile.conf 
file:

<<<PAGE 28>>>
Network Solution Guide for Small-Medium Business 
Page 28 of 32 
 
 
 
 
 
 
root@Storage 1:~$ cd /tmp/config 
root@Storage 1:~$ more rfprofile.conf 
 
{ 
          “RFService”:[ 
                          { 
                                     “bandSteering”:”enable”, 
                                     “bandSteeringForce5g”:”enable”, 
                                     “LoadBalance”:”enable”, 
                                     “backgroundScanning”:”enable”, 
                                     “bgsmode”:”workChannel”, 
                                     “ScanningEnhance”:”disable”, 
                                     “countryCode”:”FR”, 
                                     “ScanningInterval”:20, 
                                     “ScanningDuration”:110, 
                                     “neighborCount”:64, 
                                     “VoiceVedioAwareness”:”enable”, 
                                     “airtimeFairnessAt2G”: ”enable”, 
                                     “airtimeFairnessAt5G”: ”enable”, 
                                     “perBandInfo”: { 
                                               “2.4G”:{ 
                                                              “band”:”enable”, 
                                                              “radioOff:”disable”, 
                                                              “channelSetting”:”AUTO”, 
                                                              “channelWidth”:20, 
                                                              “autoChannelWidth”:”enable”, 
                                                              “powerSetting”:”21”, 
                                                              “shortGuardInterval”:”disable”, 
                                                              “shortGuardIntervalPeriod”:1, 
                                                              “signalStrengthThreshold”:0, 
                                                              “roamingSignalStrengthThreshold”:0, 
                                                              “powerValMax”:”0”, 
                                                              “powerValMin”:”0”, 
                                                              “radioMode”:”normal”, 
                                                              “scanDuration”:”normal”, 
                                                              “Gain”:”4”, 
                                                              “clientAwareness”:”enable”, 
                                                              “MuMIMO”:”enable”, 
                                                              “highEfficiency”:”enable”, 
                                                              “beaconInterval”:100 
                                               }

<<<PAGE 29>>>
Network Solution Guide for Small-Medium Business 
Page 29 of 32 
 
 
 
 
 
 
 
Knowing channels used for mesh links, their current utilization and the possible radio detections on 
specific channels enables to refine channels settings as best as possible for the better mesh experience. 
Note Stellar DRM is handled at Root level only for remote clients on mesh SSIDs. 
 
Monitoring channels for a mesh link is done with iwlist athXX channel command: 
 
 
 
 
                                               “5G_all”:{ 
                                                              “band”:”enable”, 
                                                              “radioOff:”disable”, 
                                                              “channelSetting”:”AUTO”, 
                                                              “channelWidth”:80, 
                                                              “autoChannelWidth”:”disable”, 
                                                              “globalChannelWidth”:20, 
                                                              “autoGlobalChannelWidth”:”enable”, 
                                                              “powerSetting”:”21”, 
                                                              “shortGuardInterval”:”disable”, 
                                                              “shortGuardIntervalPeriod”:1, 
                                                              “signalStrengthThreshold”:0, 
                                                              “roamingSignalStrengthThreshold”:0, 
                                                              “channelLists”:[ 
                                                                        100, 
                                                                        104, 
                                                                        108, 
                                                                        112 
                                                              ], 
                                                              “powerValMax”:”0”, 
                                                              “powerValMin”:”0”, 
                                                              “radioMode”:”normal”, 
                                                              “scanDuration”:”normal”, 
                                                              “Gain”:”4”, 
                                                              “chainmask”:15, 
                                                              “clientAwareness”:”enable”, 
                                                              “MuMIMO”:”enable”, 
                                                              “highEfficiency”:”enable”, 
                                                              “beaconInterval”:100 
                                               } 
                                     } 
                           } 
                 }

<<<PAGE 30>>>
Network Solution Guide for Small-Medium Business 
Page 30 of 32 
 
 
 
 
 
 
Stellar access points handle radio detections on UNII-2 DFS sub-band, all detections are directly displayed 
on AP console.  
 
 
 
5.3.2 
Monitoring links 
 
The link quality metric is an evaluation of the robustness of a mesh link and is based on signal strenght 
and SNR levels, it can decrease dramatically if prerequisites are not observed for the link (distance or no 
observations in configuration: frequencies, wrong installation, nLoS configurations in outdoors etc.). The 
Bit Rate negociated between two nodes is an estimation of the speed of the link. 
 
Monitoring a link in a Mesh group is done with iwconfig athXX (BSSID or ESSID) command: 
 
root@Storage 1:~$ iwlist athap1 channel 
athap1 109 channels in total; available frequencies: 
Channel 36 : 5.18 GHz 
Channel 40 : 5.2 GHz 
Channel 44 : 5.22 GHz 
Channel 48 : 5.24 GHz 
Channel 52 : 5.26 GHz 
Channel 56 : 5.28 GHz 
Channel 60 : 5.3 GHz 
Channel 64 : 5.32 GHz 
Channel 100 : 5.5 GHz 
Channel 104 : 5.52 GHz 
Channel 108 : 5.54 GHz 
Channel 112 : 5.56 GHz 
Channel 116 : 5.58 GHz 
Channel 120 : 5.6 GHz 
Channel 124 : 5.62 GHz 
Channel 128 : 5.64 GHz 
Channel 132 : 5.66 GHz 
Channel 136 : 5.68 GHz 
Channel 140 : 5.7 GHz 
Current Frequency:5.52 GHz (Channel 104) 
root@Storage 1:~$ [ 305.332833] _GOLSOH_Radar found on channel 52 (5260MHz) 
root@Storage 1:~$ iwconfig athap1 
athap1   IEEE 802.11ac ESSID:"Stellar-MESH" 
                Mode:Master Frequency:5.52 GHz Access Point: DC:08:56:13:3A:49 
                Bit Rate:780 Mb/s Tx-Power=17 dBm 
                RTS thr:off Fragment thr:off 
                Power Management:off 
                Link Quality=50/94 Signal level=-76 dBm Noise level=-95 dBm 
                Rx invalid nwid:67037 Rx invalid crypt:0  Rx invalid frag:0 
                Tx excessive retries:0  Invalid misc:0  Missed beacon:0

<<<PAGE 31>>>
Network Solution Guide for Small-Medium Business 
Page 31 of 32 
 
 
 
 
 
 
5.3.3 
Monitoring mesh SSIDs 
 
List all the interfaces of a Mesh group in order to retrieve interfaces used for SSIDs broadcasted on 2.4GHz 
and 5GHz bands for Mesh clients is done via wlanconfig command. In our scenario, these are the ath01 
and ath11 interfaces that handle SSID “SSID_storage” on both bands. 
 
 
 
 
root@Storage 1:~$ iwconfig 
… 
ath01      IEEE 802.11ng ESSID:"SSID storage" 
                Mode:Master Frequency:2.437 GHz Access Point: DC:08:56:35:28:81 
                Bit Rate:173 Mb/s Tx-Power=3 dBm 
                RTS thr:off Fragment thr:off 
                Power Management:off 
                Link Quality=53/94 Signal level=-75 dBm Noise level=-95 dBm 
                Rx invalid nwid:47691 Rx invalid crypt:0  Rx invalid frag:0 
                Tx excessive retries:0  Invalid misc:0  Missed beacon:0 
 
eth1        no wireless extensions 
 
eth0-94  no wireless extensions 
 
ath11    IEEE 802.11ac ESSID:"SSID storage" 
                Mode:Master Frequency:5.52 GHz Access Point: DC:08:56:35:28:81 
                Bit Rate:780 Mb/s Tx-Power=17 dBm 
                RTS thr:off Fragment thr:off 
                Power Management:off 
                Link Quality=94/94 Signal level=-23 dBm Noise level=-95 dBm 
                Rx invalid nwid:56940 Rx invalid crypt:0  Rx invalid frag:0 
                Tx excessive retries:0  Invalid misc:0  Missed beacon:0 
… 
…

<<<PAGE 32>>>
Network Solution Guide for Small-Medium Business 
Page 32 of 32 
 
 
 
 
Monitoring the clients served on final mesh nodes is done with wlanconfig athXX list command. Metrics 
here are the usual measures on clients associated with a specific BSSID interface, with clients data rates, 
RSSI, operating band and clients capabilities 
 
 
 
6. Related documents 
 
LAN/WLAN Datasheets & Networks Guides:   
  
Stellar AP1360 datasheet 
https://myportal.al-enterprise.com/a4F5I000000YNnKUAW 
 
User guide for OmniVista 2500 NMS 
https://myportal.al-enterprise.com/a4F5I000000HIIRUA4 
 
AWOS 4.0.4 Stellar User Guide 
https://myportal.al-enterprise.com/a4F5I000000HIS7UAO 
 
 
Product Line matrix & Installation Guides:   
 
Stellar Product Line matrix /Stellar antennas matrix  
https://myportal.al-enterprise.com/a4F5I000000Y6ezUAC 
 
Stellar AP1361 Installation Guide  
https://myportal.al-enterprise.com/a4F5I000000Y6glUAC 
 
 
 
root@Storage 1:~$ wlanconfig ath01 list 
ADDR              AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE TXSEQ RXSEQ CAPS XCAPS 
d4:6e:0e:18:60:38 1   6    72M    72M    63   62      67      0    0     65535 EPSs cORI 
ACAPS ERP STATE MAXRATE(DOT11) HTCAPS   VHTCAPS ASSOCTIME IEs      MODE                      PSMODE 
0     f   0     P              0        gR      00:03:20  RSN WME  IEEE80211_MODE_11NG_HT20  0 
RXNSS TXNSS 
1     1 
Minimum Tx Power : 5 
Maximum Tx Power : 18 
HT Capability : Yes 
VHT Capability : No 
MU capable : No 
SNR : 63 
Operating band : 2.4 GHz 
Current Operating class : 0 
Supported Rates : 2 4 11 12 18 22 24 36 48 72 96 108