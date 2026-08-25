# sol-wlan-design — 解决方案文档合并（页码全册连续）


<<<DOC 1: ale-omniaccess-stellar-high-density-design-guidelines-en.pdf | 起始页 1 | 44p>>>

<<<PAGE 1>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
OmniAccess Stellar  
High Density Design Guidelines 
Best practices for deploying high-density Wi-Fi networks  
in dense environments. 
 
 
 

<<<PAGE 2>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Table of Contents 
 
 
1. 
Introduction .......................................................................................................................................... 5 
2. 
Requirements ........................................................................................................................................ 5 
3. 
Recommendations ................................................................................................................................ 8 
3.1 
RF for capacity ............................................................................................................................... 8 
3.2 
Clients ............................................................................................................................................ 9 
3.3 
AP counting ................................................................................................................................. 11 
4. 
End-to-end architecture for high-density ......................................................................................... 18 
4.1 
LAN capacity for HD .................................................................................................................... 20 
4.2 
Advanced analytics in high-density ........................................................................................... 22 
5. 
Conclusion ........................................................................................................................................... 25 
6. 
Annexes ............................................................................................................................................... 26 
6.1 
Appendix A – Fine tuning for guests ......................................................................................... 27 
6.2 
Appendix B – Fine tuning for equipment/video surveillance .................................................. 33 
6.3 
Appendix C – Bill Of Material ..................................................................................................... 39 
6.4 
Appendix D – Related documents ............................................................................................. 44 
 

<<<PAGE 3>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Table of Figures 
 
Figure 1: Design for HD in stadium ............................................................................................... 6 
Figure 2: Very-high density SSIDs ................................................................................................. 9 
Figure 3: SSIDs specific to the site .............................................................................................. 10 
Figure 4: Maximum client HT for VHD in stadium ..................................................................... 11 
Figure 5: AP counting per areas type.......................................................................................... 12 
Figure 6: AP models for high-density ......................................................................................... 13 
Figure 7: AP1361/directional AP1361D outdoor mounting option .......................................... 14 
Figure 8: Directional AP1322 with NEMA enclosure on catwalk-type support ....................... 15 
Figure 9: AP1321 with NEMA enclosure mounted on catwalk-type support .......................... 15 
Figure 10: AP1321 under seat or on handrail with NEMA enclosure ....................................... 15 
Figure 11: AP1331 high-density indoor....................................................................................... 16 
Figure 12: AP layout for 50,000 seats .......................................................................................... 17 
Figure 13: Example of AP coverage on tier 1 ............................................................................. 18 
Figure 14: HD network design for stadium/large arena ........................................................... 20 
Figure 15: HD analytics with Omnivista Cirrus 10 ...................................................................... 22 
Figure 16: Press box dashboard with Omnivista Cirrus 10 ....................................................... 24 
Figure 17: Client density analytics (beta) with Omnivista Cirrus 10 ........................................ 25 

<<<PAGE 4>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Disclaimer 
This documentation is provided for reference purposes only and does not fully describe 
the capabilities of each Product and related features. Therefore, ALE International declines 
any liability for inaccuracies contained herein.  For an exhaustive view on features list and 
product limits for the current product release please see the required Feature List/Product 
Limits document available through the ALE eBusiness Portal web site. 
In the interest of continued product development, ALE International reserves the right to 
make improvements or other changes to this document and the products it describes at 
any time without prior notice. 
  
 
 
Copyright 
Copyright © ALE International 2024. Distribution of substantively modified versions of this 
document is prohibited without the explicit permission of the copyright holder.  
 
Distribution of the work or derivative of the work in any standard (paper) book form for 
commercial purposes is prohibited unless prior permission is obtained from the copyright 
holder.

<<<PAGE 5>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
1. Introduction 
 
The purpose of this technical note is to outline best practices for deploying a high-density 
(HD) Wi-Fi network using OmniAccess Stellar access points, especially in dense 
environments like stadiums or outdoor arenas. 
OmniAccess Stellar 802.11ax technology is well-suited for meeting the requirements of 
such environments, characterized by diverse connectivity needs, high concentrations of 
users typical for this type of deployment, and complex installations. 
The focus of this note is on modern stadiums. The network design, particularly the Wi-Fi 
aspect, requires project oversight for design and installation, including an analysis of 
prerequisites, capacity requirements, and access point deployment. It consistently calls 
for the implementation of a dedicated and autonomous network architecture provided by 
the ALE network solution managed in Enterprise mode. These various points are detailed 
in this note. 
It's always beneficial to refer to the existing OmniAccess Stellar Fine-Tuning Best 
Practices note for indoor Stellar deployments, as it already provides extensive details on 
key RF parameters, SSIDs, and AP group settings.  
This note can also be used with interest for any dense indoor Wi-Fi deployment 
 
2. Requirements 
 
The modern stadium is an extreme case of high-density (HD) wifi in a well-defined space, 
and a typical example of multiple wireless services with the following main characteristics: 
 
- 
Several tens of thousands of seats (the example given in this note is for a stadium 
with up to 50,000 seats) 
- 
+20,000m² surface area for 50,000 seats 
- 
More access points than channels in the 5GHz band  
- 
Different areas and spaces at different tier levels reserved for press, media or VIPs 
- 
Users are mainly guests (up to 2 devices per person) 
- 
Halls and concession areas (stores) around the stands 
- 
Offices, facilities, auditoriums, restaurants or other indoor spaces 
- 
Exceptional concentration of users during events 
- 
High-rise structures, up to 50m high 
- 
Elevated platforms (catwalk-type) to support technical equipment 

<<<PAGE 6>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
 
To setup a high-density WLAN network in a stadium as described above, a WLAN Network 
design project based on capacity planning is essential. This planning enables us to assess 
how the network will be used at high density. Based on the ‘Capacity planning and 
deployment’ figure 1 detailed in the OmniAccess Stellar Fine-Tuning Best Practices notes 
for capacity, the following points will need to be considered in the case of high-density 
design in a stadium: 
 
 
 
 
Figure 1: Design for HD in stadium 
 
A requirements analysis is the first and essential step in high-density Wi-Fi design, that is 
clearly identifying client types and the different applications used: audio/video, data or 
real-time. This part includes a capacity plan to evaluate the potential network load during 
events. In particular the number of concurrent clients per access point, and concurrent 
bandwidth requirements will be determined. 

<<<PAGE 7>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
This step takes also into account network access requirements: Captive Portal/ BYOD 
accesses, Enterprise connections and their associated security, QoS, latency and more. 
The selection of AP models is specifically done during the requirements analysis, with a 
study of APs installation during the deployment phase. The optimal placement of the APs 
on the different zones and levels of the stadium is an essential factor for an optimal 
experience. This includes specific coverage areas such as press and VIP areas, as well as 
halls, high-concentration areas, and stadium facilities. 
An estimation of LAN capacity to support HD Wi-Fi is part of the design requirement and 
is also carried out during this step. 
 
The Design, Deployment and Validation steps depicted in the figure above underline the 
importance of methodology in the implementation of high-density WLAN. Design includes 
the creation of a predictive survey site. An implementation project is recommended, 
including detailed digital maps of the different zones of the stadium to be covered, 
notably: seating areas, halls, indoor areas and other spaces.  
The Design will include the chosen WLAN architecture and its deployment with the 
configuration of access points as well as the testing phases on various applications used 
in a stadium. 
Finally, the post-installation validation phase in the stadium is carried out by analyzing 
network performance in real time, and comparing the results obtained with the 
requirements defined during the planning. Design validation phase can also be carried 
out by means of real user surveys. 
 
Several deliverables will be provided to site managers at the end of the project, following 
documents and services are generally required: 
- 
BOM (Bill of Materials), a complete inventory of WLAN/LAN equipment used: access 
points, switches, servers, accessories, HW/SW support, licenses, end-customer 
services, etc.  
- 
AP layouts showing the location of each access point in the stadium, with 
information on their configuration 
- 
Survey site reports detailing on-site results and coverage measurements made 
- 
Installation guide describing the steps involved in installing, configuring and 
maintaining the wifi network 
- 
Configuration guide detailing network configuration, security parameters, VLANs, 
QoS and access policies, etc.  
- 
Training of staff responsible for managing and maintaining the WLAN network. 
 
 

<<<PAGE 8>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
3. Recommendations 
 
3.1 RF for capacity 
 
Success in deployment of a high-density Wi-Fi network in a stadium relies heavily on 
effective RF management. 
- 
Channel reuse plan: channels available in the 5GHz band in an area are re-used in 
regular patterns, reducing then CCI and ACI interference in the area. 
- 
Force the 5GHz band and balance the load between APs to avoid overloading 
certain APs. 
- 
Define appropriate Tx transmission levels: for high-density indoor areas of stadium 
it's often advisable to set lower Tx transmission levels to reduce interference. For 
outdoors, this Tx level may vary according to the specific needs of the deployment, 
for example external Wi-Fi 6 AP1361 installed 30m above the stands could transmit 
at a power level of around 10 to 15dBm. 
- 
Channel plans: it makes sense to divide a site like a stadium into several channel 
plans and use DFS channels in stands for better use of 5GHz band, and non-DFS 
channels for better performance in indoor areas for example. 
Non-DFS channels are more widely available and can be used in indoor areas such 
as press rooms or catering areas. 
DFS channels are channels that use frequencies shared with other radio services. 
They can be advantageously used in the stands of a stadium where there is a high 
concentration of users. It is important to comply with local regulations for their use. 
- 
Use of 20 MHz bandwidth: 20 MHz channel width greatly minimizes interference in 
outdoor areas, especially CCI (Co-Channel Interference). Use of this base bandwidth 
is well suited to client mix and coverage of tiered areas. 
- 
Airtime fairness: essential in high-density environments, as it efficiently manages a 
number of clients with varying throughput requirements at a single access point, 
guaranteeing fair use of resources for each of them. 
 
  
RF management on Stellar is therefore essential for high-density deployment, and it is 
advisable to refer to the OmniAccess Stellar Fine-Tuning Best Practices note to overview all 
RF parameters. Defining multiple Stellar RF profiles make it easy to manage all the RF 
points just seen previously, including a channel plan selection (DFS channels, non DFS 
channels, channels over DFS etc.) and Auto Channel Selection. OmniAccess Stellar access 
points automatically adjust the channels of the radios to avoid RF interferences (802.11 
and non-802.11) and develop channel plans for the WLAN. Channels can be selectively 
assigned to be used with each RF profile. 

<<<PAGE 9>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Most Stellar Wi-Fi6 APs have a radio dedicated to the scanning and there's no need to 
activate a background scanning on the active channels for access points selected for high 
density, leaving active channels totally free to handle heavy client thoughputs. It is 
therefore recommended to select APs that support a dedicated full-band scanning radio. 
 
 
3.2 Clients 
 
There is a high mix of clients and applications in a stadium. Today's stadium visitors 
generally have the following characteristics: 
- 
Around 90% of equipment/smartphones are dual-band compatible. 
- 
90% are smartphones, 10% are laptops for visitors in the stands 
- 
The percentage of visitors with Wi-Fi 6 phones is estimated 20%-35%, bringing a 
high mix of devices into the stadium. 
- 
The majority of Wi-Fi clients today operate in 2x2:2 MIMO mode. 
- 
Most clients support 5GHz DFS channels, then DFS channels can be included in 
channel plans for visitors. 
- 
Each visitor can have up to two devices. 
 
A stadium requires a variety of Wi-Fi services (up to 7 SSIDs maximum are possible for an 
average channel utilization in the 5 GHz band of around 12%, refer to ‘number of SSIDs 
versus channel reuse’ table in OmniAccess Stellar Fine-Tuning Best Practices note for 
details). These Wi-Fi services need to be specially designed to handle a high density of 
clients, with an average of 0.5 to 1 m² per seat, and 1 to 2 m² of space in high-
concentration areas. 
 
 
SSID 
Usage 
Authentication 
Access 
Visitors 
Internet/email/social network/video 
(roaming optional) 
Mix of smartphones and tablets 
Open SSID with 
Captive Portal 
Captive Portal 
restrictions 
Press, media 
and VIPs 
Internet/files/video 
Mix of laptops, smartphones and tablets, 
legacy devices 
802.1X WPA2 
High QoS 
No rate limit 
 
Figure 2: Very-high density SSIDs 
 

<<<PAGE 10>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
OmniAccess Stellar SSIDs fine-tuning for very-high density must include: 
- 
Dual-band 2.4 GHz/5 GHz SSIDs with band forcing to 5 GHz at RF level. 
- 
Minimum data rates of 12 Mbps to take account of different client types. 
- 
Some devices, notably Apple and Chromebook, may have particular behavior with 
regard to Address Resolution Protocol (ARP) when roaming or associating. The 
application of the ARP broadcast filter is recommended to avoid these problems 
during their roaming/association. 
- 
QoS implementation and application prioritization, particularly for audio/video 
applications. 
 
The “Sticky avoidance" must be managed at RF level for these high-density SSIDs. It 
enables better signal quality for clients and better load balancing between APs. 
 
 
SSID 
Usage 
Authentication 
Access 
Ticketing/points 
of sales 
Real-time (Ticketing system) 
Tablets, smartphones or Scanners 
802.1X WPA2 
QoS 
Back office 
application 
Equipment/video 
surveillance 
Multicast/data/video, IoT 
802.1X WPA2 
Streaming rate 
Employees 
Office/data/collaborative 
Laptops, smartphones, tablets 
802.1X WPA2 and 
more 
Site policies 
BYOD 
IT 
Office/data/collaborative 
Laptops, smartphones, tablets 
802.1X WPA2 and 
more 
Site policies 
 
Figure 3: SSIDs specific to the site 
 
SSIDs for equipment and employees deployed for site operation generally follow the 
same design rules, with a management similar to that found in offices. However, care 
must be taken to optimize broadcast/multicast for wireless video equipment. 

<<<PAGE 11>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
3.2.1 Maximum client throughput in very high-density 
 
 
The following table gives an indication of the maximum throughput that can be expected 
for clients connected in a tier/seat VHD area. The client mode in the table is 2x2:2SS with 
use of MCS8 modulation* (256QAM 3/4). From information available for WLAN use cases in 
stadiums and for users connected to visitors SSIDs we have: 
- 
A measured throughput of 80Mbps (MCS8 modulation*) for a single Wi-Fi 6 user on 
a 5GHz channel using TCP protocol (http protocol to the Internet), dropping to 
40Mbps when there’s a high concentration of clients connected on the same 
channel (average of 60 clients connected simultaneously is depicted in example 
here). 
- 
A 25% ratio, specific to VHD in stadium, is introduced to account CCI/ACI effects 
(interferences from other APs on the same channel), Wi-Fi interference, non-Wi-Fi 
interference and considering a moderate duty cycle for stadium context (time when 
the channel is effectively used). 
 
 
Mode 
Datarate 
Datarate/HT 
for TCP (http) 
Client 
concentratio
n (60) 
VHD in stadium 
802.11ax HE20 
206Mbps 
165/80Mbps 
50Mbps 
37Mbps 
802.11ax VHT20 
173Mbps 
140/70Mbps 
40Mbps 
30Mbps 
 
Figure 4: Maximum client HT for VHD in stadium 
 
 
3.3 AP counting 
 
3.3.1 Metrics in high-density 
 
The table below lists the following recommended AP count values to be included in the 
capacity plan for high-density stadiums.  

<<<PAGE 12>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Area type 
AP counting 
Notes 
Tiered/seats 
Up to 120 devices per 
AP/radio 
(up to 150 seats/AP) 
AP count method is devices due to client density 
Press/media/VIP 
1 AP/100m² 
Very-high density use with a minimum of 2 APs for a 
correct load balancing. Specific AP counting per seat 
can be applied for the press in the case of very heavy 
use, counting 1 AP/25 seats in this case 
Halls/concessions 
1 AP/100m² 
High-traffic areas with high client density 
Surrounding area 
1 AP/100m² 
Especially with high density at stadium entrances 
Service 
1 AP/100m² 
Density for IT/employees areas is similar to that of 
other zones due to intensive use of thick walls in the 
stadium 
 
Figure 5: AP counting per areas type 
 
 
For tiered/seats areas, a ratio of 30% of connected people to the total number of visitors is 
generally applied, which is value considered in first calculation for a high WLAN usage by 
visiting users in the case of stadiums. For example, in a stadium with a capacity of 52,000 
seats, this equates to a load of 21,000 concurrent devices, or 60 devices per AP and more. 
 
 
3.3.2 Benefits of using Wi-Fi 6 access points 
 
As already mentioned in the OmniAccess Stellar Fine-Tuning Best Practices note, the 
technologies integrated by 802.11ax (Wi-Fi 6), such as OFDMA and BSS coloring, as well as 
the evolution of beamforming, evolution of MU-MIMO and the contribution of fast 
modulation for nearby clients, offer numerous advantages in high-density applications. 
Full use of 802.11ax in high-density installations means: 
 
- 
The support for large numbers of clients  
- 
More efficient use of airtime in high-density applications 
- 
A better channel reuse in the 5GHz band 
- 
A better control of CCI 
 

<<<PAGE 13>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
The recommended Stellar Wi-Fi 6 access points in high-density are: 
 
 
Model 
Recommended use 
LAN capacity 
AP1360 serie 
Outdoor wings, surroundings, entrances, video surveillance 
(poles and walls mounting) 
2.5Gbps 
AP1322 
Stand/seats with 30x30° antennas or 60x60° antennas 
(height less than 15m/structure) 
(catwalk and high structure, walls mounting) 
2.5Gbps 
AP1361D/AP1361 
Stand/seats with catwalk-type structure for installation 
(catwalk and high structure, walls mounting) 
2.5Gbps 
AP1331/AP1351 
Press areas, halls, gates, auditorium 
(ceiling, walls mounting) 
10Gbps 
AP1311/AP1331 
Offices, locations 
(ceiling mounting) 
5Gbps 
 
Figure 6: AP models for high-density 
 
 
For stands/seats areas, other installation strategies are possible upon use cases: 
- 
Seat and handrail installations: some APs can be installed directly under seats, 
which can be useful for providing connectivity to nearby spectators. Handrails also 
enable APs to be positioned at the right height to provide effective coverage for 
visitors seated in the stands.  
- 
Wall and structure installations: stadium walls and other structures can also be 
used to support APs and provide Wi-Fi coverage in areas where stands are not 
present. 
 
For example, the use of AP1321 model with integrated antennas can be envisaged for this 
type of installation, particularly for seats with the use of suitable protective boxes (NEMA 
enclosure protection rating IP3 or IP4). These installations are generally designed to meet 
specific needs, and their implementation must be carefully planned to ensure optimum 
coverage in these areas. 
 
The use of low-performance Wi-Fi 6 APs is not recommended for stadiums with more than 
5,000 seats. 
 

<<<PAGE 14>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
3.3.3 Examples of AP installations 
 
Various installation options are possible for access points in a stadium. Here are the most 
commonly used methods for: conventional outdoor installations with mounting on poles 
and infrastructure walls, rooftop installations for overall coverage and targeted 
configurations for specific areas and sections requiring high throughput. 
 
 
 
Figure 7: AP1361/directional AP1361D outdoor mounting option 
 
For surrounding areas, parking lots, and exposed locations to environmental elements, 
industrial hardened Stellar AP1361/AP1361D, or higher, will be deployed. Installation 
involves mounting on back walls and/or vertical structure pillars. 
 
 
 
 
 
 

<<<PAGE 15>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
          
   
Figure 8: Directional AP1322 with NEMA enclosure on catwalk-type support 
 
AP1322s can be mounted on back walls and/or vertical pillars configured with external 
directional antennas. 
 
 
 
Figure 9: AP1321 with NEMA enclosure mounted on catwalk-type support 
 
 
 
 
 
 
             
 
 
Figure 10: AP1321 under seat or on handrail with NEMA enclosure 

<<<PAGE 16>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Note: This deployment type can be used in front of or in the middle of each spectator 
section on each floor. APs must be protected from intentional destruction when installed 
in this manner. 
 
 
 
Figure 11: AP1331 high-density indoor 
 
 
 
 
Because of the large number of APs to be installed in large spaces or high-density interior 
rooms, it makes sense to carry out AP placement study in false ceilings for a clean visual 
appareance. 
 
The physical placement of each AP depends on the physical site survey, which guarantees 
the strongest signal coverage while minimizing channel interference. An installation 
guide is provided for each type of placement and installation guide document is one of 
the important deliverables to be provided at the end of the project. 
 
 
3.3.4 Example of installation for 50,000 seats 
 
The following map illustrates a stadium with a capacity of 52,000 seats and shows a study 
for the location of 260 AP1322s equipped with ANT-S-M4-60 and ANT-S-M4-30 external 
antennas. The installation strategy is to place these directional access points on the roof 

<<<PAGE 17>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
structure, to ensure complete, high-density coverage of the visitor area on both levels of 
the stadium's stands.     
With this approach, each AP1322 covers an average of up to 180 seats. One telecom 
satellite cabinet is required approximately every 3,200 seats, with each cabinet equipped 
with a 24-port switch in this example. To further improve connectivity in the stands, 
auxiliary installations such as additional access points and reinforcement antennas can be 
considered in high-traffic areas, such as access gates, for example. 
 
Figure 12: AP layout for 50,000 seats 
 
 

<<<PAGE 18>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Figure 13: Example of AP coverage on tier 1 
 
The image above illustrates the coverage of AP1322s access points for an area of 775 
seats on level 1 of the stadium's stands. You can see, the signals from the access points 
are carefully aligned to provide uniform coverage across level 1, ensuring stable and 
consistent connectivity in this area. 
 
4. End-to-end architecture for high-density 
 
Implementing a high-density Stellar WLAN network in a large-capacity stadium, as 
described above, is a complex project requiring a carefully planned network architecture. 
The WLAN and core LAN network is typically an autonomous, mission-critical network 
managed by the Omnivista 2500 management system (NMS). 
  
The architecture illustrated below showcases a multi-service network that has already 
proven its effectiveness in various ‘always-on’, strategic networks scenarios including: 
high-speed rail signalling, CCTV-IP networks for airports, data centers for police, 
governments and so on. This network is designed to support array of services such as 
video-surveillance, diverse network entities, security, access control and notably high-
density WLAN in the case of stadium/large arena. 
 
OmniAccess Stellar high-density WLAN is based here on a network core consisting of two 
redundant Omniswitch 6900s and features the following: 
- 
Virtual chassis 
- 
Autofabric 

<<<PAGE 19>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
- 
VLAN scalability 
- 
Device scalability (288K MACs) 
- 
Low latency 
- 
Application visibility & analytics (real-time Layer 7 application processing) 
- 
Service isolation 
- 
Guaranteed 40Gbps traffic, with the ability to peak at 100Gbps 
 
 
The network core provides full redundancy for all appliances in the data center, with a 
physical location across two separate sites. 
- 
Omnivista 2500 NMS operates in high availability (HA) mode with a duplicated 
database. 
- 
DHCP/DNS servers need to be high-performance and accomodate multiple IP 
scopes and a large database for support of WLAN for visitors. 
- 
The Captive Portal (CP) service can be entirely managed by Omnivista 2500. 
Omnivista 2500 offers a significant advantage due to its ability to handle a large 
number of users while consolidating CP functions and access policies on a same 
server. Omnivista 2500 greatly simplifies the management of visitor access in a 
high-density user environment, such as a stadium.  
 
 
 
It is also possible to manage the CP function with a third-party CP solution, and the 
solution must be able to support at least 15,000 users immediately (for example, the 
UCOPIA Edge solution with on-site controllers and Advanced licenses for a high 
number of users using CP services). 
 

<<<PAGE 20>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
 
Figure 14: HD network design for stadium/large arena 
 
 
4.1 LAN capacity for HD 
 
To perform a proper evaluation of the sizing for 6900 core network, several key 
parameters need to be considered and integrated into the capacity plan. 
 
Let's delve into the core network sizing for WLAN visitor traffic, which represents the most 
significant load in the stadium example. The following aspects should be taken into 
account: 
 
- 
The number of visitors for the guest VLAN. 
- 
The required bandwidth in LAN for the visitor area. 

<<<PAGE 21>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
- 
A proper sizing of visitor DHCP scopes. 
- 
The size of the Omnivista 2500 license for guest users. 
- 
Necessary firewall resources. 
 
 
To estimate the required LAN bandwidth within the seating area, it's important to 
consider the channel reuse factor. This factor represents the ratio of available channels to 
the channels used in a given Very High Density (VHD) area. It depends on the specific 
channel plan defined for the seating areas to be covered and the deployment strategy 
employed, whether it involves rooftop installations or extreme VHD deployments under 
the seats. For instance, selecting a DFS channel plan with a minimum of 8-10 channels 
specified for a particular stadium zone would result in a channel reuse ratio close to 1 (8 
divided by 8). With OmniAccess Stellar DRM in operation, all channels defined in each 
channel plan are available and utilized, and then distributed in an optimized pattern of 
reuse. 
 
In the context of stadium scenarios, it's essential to aim for a channel reuse factor as 
close to 1 as possible, especially within VHD areas. For seating-based installations, the 
channel reuse factor can extend up to a maximum of 3. 
 
 
The estimation of LAN bandwidth to be provided for a WLAN VHD area follows this 
formula: 
LAN BW =   channel reuse factor * number of APs * number of clients per AP * VHD 
bandwidth per client 
 
 
As an example, for a stadium featuring 50,000 seats with the following conditions: 
- 
15,000 users connected simultaneously in the seating areas. 
- 
An average of 1 device per person. 
- 
An average required bandwidth of 2 Mbps per client. 
- 
An average of 60 clients per AP. 
- 
90% of users utilizing the 5GHz band. 
 
In this scenario, the estimated LAN bandwidth for visitors amounts to 1 * 260 * 60 * 2 = 
31,200 Mbps. To account for wired bandwidth, a precautionary additional 50% is included 
in the initial assessment, resulting in a total of 47 Gbps for the core LAN.  
For comprehensive coverage encompassing all areas of the stadium, including halls, 
rooms, outdoors, etc. and for deployments involving seat-based strategies, it is advisable 
to consider an architecture with a 100 Gbps 6900 core. 
 

<<<PAGE 22>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
4.2 Advanced analytics in high-density 
 
Omnivista 2500 in High Availability (HA) mode for a stadium ensures that no access points 
are lost in a high-density WLAN network. Omnivista 2500 handles a variety of AP groups, 
supporting up to 4000 APs per appliance, along with compatibility for all AP models 
suitable for their deployment within a stadium. 
 
 
The combination with an Omnivista Cirrus 10 Cloud instance for statistical and analytical 
tasks, specifically tailored for high-density environments, complements with interest 
Omnivista 2500 NMS management of the site. All Stellar Wi-Fi 6 series AP13XX support 
advanced analytics, reporting and logging, and can send their data to a Cloud instance of 
Omnivista 10 for advanced analytical services on-site, particularly when the WLAN network 
is managed by Omnivista 2500, such as in a stadium. The only prerequisite is to authorize 
access to the Omnivista Cirrus 10 instance in the firewall of stadium for all APs and stadium 
areas to be monitored. 
 
 
Figure 15: HD analytics with Omnivista Cirrus 10 
 
 
Omnivista Cirrus 10 cloud instance provides the ability to manage and deliver various 
dashboards for advanced analysis tasks in high density, covering the entire WLAN of a 
stadium through a single platform and in a variety of table and graph formats. 

<<<PAGE 23>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
In the example of a high-density area such as the press box, Omnivista Cirrus 10 already 
generates a number of interesting statistics on the APs and RF (“Network Analytics” 
menus), including: 
• 
AP uptime 
• 
CPU usage 
• 
Memory and flash usage 
• 
Client distribution accross used channels 
• 
Channel usage 
 
Statistics on connection mode of Omnivista Cirrus 10 (“Client Analytics” and “QoE” menus) 
provide information on: 
• 
Time on connections (with failure reasons) 
• 
Roaming behavior of clients 
• 
Coverage quality 
• 
Successful connections 
 
These statistics can be complemented by statistics on applications: users access to 
domains/URLs, users connections across high-density SSIDs, user access through captive 
portal, connections times for visitors or the number of devices per user. 
 
In the case of a VHD area in a very confined space such as the press box, all these statistics 
can be grouped into a single dashboard (“Custom Dashboard” menu), entirely customized 
for the use of this area. In the example the tools grouped for the area include: 
• 
Top N clients for the press box 
• 
Categorization of clients for the box 
• 
Bandwidth consumption 
• 
Number of successful connections 
• 
Usage of channels 
• 
List of channels and APs in the box 
• 
CPU and memory usage for box APs 
 

<<<PAGE 24>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
 
Figure 16: Press box dashboard with Omnivista Cirrus 10 
 
 
Omnivista Cirrus 10 is enhanced (version 10.4.1+) with WLAN heatmap tool and specifically 
with a client density map tool (“location” menus) allowing for a quick overview of the 
complete WLAN coverage of the site and the current WLAN usage for a particular area.  
 

<<<PAGE 25>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Figure 17: Client density analytics (beta) with Omnivista Cirrus 10 
 
Achieving a QoE score and maintaining control over the density of certain Wi-Fi coverage 
areas is essential for the maintenance of a high-density WLAN with a large user base, and 
Omnivista Cirrus 10 fully meets these requirements. 
 
 
5. Conclusion 
 
In conclusion we have emphasized the importance of a well-planned WLAN network 
design project that encompasses capacity planning, access point selection, and optimal 
placement for deploying a high-density Wi-Fi network using OmniAccess Stellar access 
points, with a specific focus on the challenging environment of modern stadiums. We have 
outlined the best practices for such deployments, recognizing the unique requirements of 
these spaces, including extensive seating, a significant number of access points, and the 
need for various wireless services. 
 
To ensure reliable and robust connectivity in high-density scenarios, it is crucial to 
implement a dedicated network architecture managed by the ALE network solution in 
Enterprise mode. This approach is recommended to address the specific demands of 
stadium environments. 

<<<PAGE 26>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
We have recommended a thorough consideration of RF management, the types of clients 
and applications, and the benefits of using Wi-Fi 6 access points to meet the connectivity 
needs of stadiums. This combination of factors is essential for success in deploying a high-
density Wi-Fi network in challenging conditions. 
 
Furthermore, the use of advanced analytics provided by Omnivista Cirrus 10 offers 
valuable insights into quality of experience and application analytics. These insights are 
indispensable for maintaining a high-quality, high-density network, ensuring seamless 
connectivity for thousands of users in stadium environments. 
 
A careful planning, network architecture, RF management, and advanced analytics are keys 
to successfully implement and manage high-density Wi-Fi networks in stadiums. These 
practices are vital to guaranteeing a seamless and reliable experience for users in such 
demanding conditions. 
 
6. Annexes 
 
The following templates are provided here as recommendations and are subject to 
adaptation based on the project's requirements. Here our example applies to the channels 
used in France in the 5GHz band for enterprise Wi-Fi and is transposable worldwide 
according to the channels defined for the country. 
 
We will delve into fine-tuning Stellar for two SSIDs examples: 
- 
One for stadium visitors (HD), including halls and press rooms (VHD) and using DFS 
channels (UNII-2 extended – channels 100 to 140) 
- 
One for equipment and video surveillance using non-DFS channels (UNII-1 and 
UNII-2 – channels 36 to 64) 
 
 
 
 
 
 
 

<<<PAGE 27>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
6.1 Appendix A – Fine tuning for guests 
 
RF profile 
 
Setting 
Default 
Guidelines 
Band Steering 
Disabled 
“OFF” 
For very high-density deployment, this attribute is 
recommended to be enabled.  
Force 5GHz 
Disabled 
This functionality is recommended to be enabled for 
environments where the client population is dense. 
When enabled it will reject all association requests on 
the 2.4Ghz band. 
Association RSSI 
Threshold 
Disabled 
“0” 
Recommended to be enabled for both 2.4Ghz and 
5Ghz bands and set a minimum RSSI threshold of 
22 which translates to -74 dBm (using -96 dBm as 
base noise floor). 
Dynamic Load 
Balance 
Disabled 
“OFF” 
Recommended to be enabled to enable load 
balancing between neighboring APs 
Airtime Fairness 
Disabled 
“Both Bands” 
Recommended to be enabled, the newer devices 
will take advantage of these advanced features 
through the support of the new standards in a fair 
manner since they will have equal airtime as older 
devices while using faster processors, new wi-fi 
standards, etc. 
Background 
Scanning 
Enabled 
“ON” 
Recommended to stay enabled: Background 
scanning is used to examine the radio frequency 
environment in which the wireless network is 
operating, discover neighbor APs, and identify 
interference and attacks. Background scanning is 
the basis of some advanced features such as: 
WIPS, Radio Dynamic Adjustment (ACS/APC) etc. 
Scanning Channel 
“Working 
Channel” 
Wi-Fi 6 APs perform their scan on a dedicated 
radio chipset, and "Working channel and Non-
working Channel" operating mode must be 
selected to make this radio operational. 

<<<PAGE 28>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
DRM Time Control 
Disabled 
“OFF” 
Recommended to be enabled in a high-density 
environment. As the DRM feature makes dynamic 
changes and channel and power adjustments that 
could impact the channel plans, it is preferable 
that these are made outside of heavy load periods 
during events. 
DRM Start Time 
Disabled 
“00:00” 
02:00 setting will start the DRM feature at 2am, it 
will stop it 6h later by default 
Band 
“2.4G, 5G all,  
5G low, 5G 
high, 6G” 
All selected 
All bands are selected by default for their 
management, each AP model applies the 
adaptations made for each:  
Dual-band models: 2.4G, 5G all  
Tri-radio models: 2.4G, 5G low, 5G high 
Channel DRM 
5G All “OFF” 
5G Low “OFF” 
5G High “OFF”  
Recommended to be enabled for 5GHz all (or 5GHz 
low and 5GHz high for the tri-radio model) to 
manage properly these bands in high density. 
 

<<<PAGE 29>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
CSA 
Enabled 
“ON” 
The CSA (Channel Switch Announcement) in high-
density WLAN must stay enabled when using DFS 
channels to allow Wi-Fi devices to detect the 
presence of radars and switch channels to avoid 
interference and comply with regulations. 
Channel List 
0 selected 
Only supported when “Channel DRM” for 5G 
bands is enabled. A channel plan for France with 
DFS can include for example all DFS UNII-2 
channels and UNII-3 channels (i.e. channels 100 to 
165) 
Channel Width 
Enabled 
“Auto” 
Recommended to select the 20MHz band width for 
WLAN in very high-density for both 2.4G and 5G 
bands 
Minimum TX 
Power(dBm) 
Disabled 
“configurable 
range from 3-
40 dBm” 
For very high-density RF, this parameter is 
recommended to be set at minimum Tx at 6 dBm 
for 2.4GHz and 12 dBm for 5GHz bands.  
 
Maximum TX 
Power(dBm) 
Disabled 
“configurable 
range from 3-
40 dBm” 
For very high-density RF, this parameter is 
recommended to be set at maximum Tx power at 
12 dBm for 2.4GHz and 18 dBm for 5GHz bands. 
 
External Antennas 
Gain(dBi) 
Enabled 
“configurable 
range from 1-
16 dBm” 
 Only applicable to APs supporting external 
directional antennas ie. AP1322 (AP1362 also but 
does not apply for visitors areas in general). 
 
Beacon 
Interval(ms) 
Enabled 
“100” ms 
This indicates how often the 802.11 beacon 
management frames are transmitted by the AP, 
the configurable range is from 60-500ms. Default 
value of 100 ms is sufficient in most cases and can 
be increased to 150ms if network load is 
considered really high. 
 
 
 
SSID 

<<<PAGE 30>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Setting 
Default 
Guidelines 
SSID Setting 
Usage 
Guest Network 
(open or CP) 
Users to go through a Captive Portal to be enabled 
Allowed Band 
2.4GHz and 
5GHz  
selected 
Keep the default selection due the mix of clients 
visiting in very high-density 
Roaming Controls 
FDB Update on 
Association 
Disabled 
Overall, 802.11k and 802.11v roaming options 
aren't necessary, given the mix of devices and the 
ability of each to handle this type of protocol, it's 
preferable for devices to stick to a better AP in the 
worst-case scenario. However, FDB update can be 
enabled to allows the switches’ forwarding table 
be updated when devices are moving across APs. 
Client Controls 
Max Number of 
Clients Per Band 
“64” 
The number of clients that can be associated with 
a radio in the case of very high density and high 
client concentration can be very high in the case of 
guests; the recommended value is 128 client max 
for this type of SSID. 
802.11b Support 
Enabled 
Can only stay enabled when the 802.11a/g setting 
is enabled. Recommended to be disabled by 
default. 
Minimum Client Data Rate Controls 
2.4GHz Minimum 
Client Data Rate 
Controller 
Disabled 
Recommended to be enabled. 
2.4GHz Minimum 
Client Data Rate 
Disabled 
Recommended to be enabled, setting the value at 
6 Mbps. 
5GHz Minimum 
Client Data Rate 
Controller 
Disabled 
Recommended to be enabled. 

<<<PAGE 31>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
5GHz Minimum 
Client Data Rate 
Disabled 
Recommended to be enabled, setting the value at 
12 Mbps. 
Minimum MGMT Rate Controls 
2.4GHz Minimum 
MGMT Rate 
Controller 
Disabled 
Recommended to be enabled. 
2.4GHz Minimum 
MGMT Rate 
Disabled 
Recommended to be enabled, setting the value at 
6 Mbps 
5GHz Minimum 
MGMT Rate 
Controller 
Disabled 
Recommended to be enabled. 
5GHz Minimum 
MGMT Rate 
Disabled 
Recommended to be enabled, setting the value at 
12 Mbps 
 

<<<PAGE 32>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Settings 
Default 
Guidelines 
Bandwidth Contract 
Upstream Bandwidth 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Downstream 
Bandwidth 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Upstream Burst 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Downstream Burst 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Broadcast/Multicast Optimization 
Broadcast Key Rotation 
Disabled 
For security purposes and for broadcast handling 
optimization, this attribute recommended to be 
enabled. 
Broadcast Filter All 
Disabled 
Recommended to be enabled to help alleviate issues 
with certain devices that have issues with dynamic 
frequency selected channels. Apple and Google design 
documents recommend 5GHz only SSIDS to support 
these devices. 
Broadcast Filter ARP 
Disabled 
Recommended to be enabled. for the same reasons 
explained above.  
802.1p Mapping 
Uplink/Downlink 802.1p 
markings for AC_BK, 
AC_BE, AC_VI, AC_VO 
categories 
802.1p 
default 
values 
In general 802.1p marker values are those usually 
used by default for such use case.  But can be 
always adapted especially for AC video category, if 
required for guest applications with video. 
DSCP Mapping 
Trust Original DSCP 
Disabled 
The original DSCP can be trusted for all uplink 
traffic returning to the network. Recommended to 
be enabled 
Uplink/Downlink DSCP 
markings for AC_BK, 
DSCP 
default 
values 
In general DSCP marker values are those usually 
used by default for such use case.   They can be 
always adapted or some values added if required. 

<<<PAGE 33>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
AC_BE, AC_VI, AC_VO 
categories 
 
 
AP Group 
 
Setting 
Default 
Guidelines 
SSH 
SSH Login 
Disabled 
“OFF” 
Recommended to be enabled SSH console is 
used for rooftop stadium APs which could not be 
routinely dismounted during maintenance, 
ensuring their efficient access and management. 
Client Behavior Tracking 
Upload To 
SFTP/TFTP 
Server 
Disabled 
“OFF” 
Recommended to be enabled for configuring Wi-
Fi log collection to record user behavior for 
compliance with local regulations. Logs are 
securely transferred via SFTP located in the 
stadium's Data Center at a defined frequency. 
SNMP Setting 
SNMP Agent 
SNMP and Trap 
Service 
“OFF” 
Recommended to be enabled SNMP is employed 
to gather and organize access point information, 
as well as monitor the activity of access points 
registered within the Omnivista 2500. 
 
 
 
6.2 Appendix B – Fine tuning for equipment/video surveillance 
 
RF profile 
 
Setting 
Default 
Guidelines 
Band Steering 
Disabled 
“OFF” 
For very high-density deployment, this attribute is 
recommended to be enabled.  

<<<PAGE 34>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Force 5GHz 
Disabled 
This functionality is recommended to be enabled for 
environments where the client population is dense. 
When enabled it will reject all association requests on 
the 2.4Ghz band. 
Association RSSI 
Threshold 
Disabled 
“0” 
Recommended to be enabled for both 2.4Ghz and 
5Ghz bands and set a minimum RSSI threshold of 
22 which translates to -74 dBm (using -96 dBm as 
base noise floor). 
Dynamic Load 
Balance 
Disabled 
“OFF” 
Recommended to be enabled to enable load 
balancing between neighboring APs 
Airtime Fairness 
Disabled 
“Both Bands” 
Recommended to be enabled, the newer devices 
will take advantage of these advanced features 
through the support of the new standards in a fair 
manner since they will have equal airtime as older 
devices while using faster processors, new wi-fi 
standards, etc. 
Background 
Scanning 
Enabled 
“ON” 
Recommended to stay enabled: Background 
scanning is used to examine the radio frequency 
environment in which the wireless network is 
operating, discover neighbor APs, and identify 
interference and attacks. Background scanning is 
the basis of some advanced features such as: 
WIPS, Radio Dynamic Adjustment (ACS/APC) etc. 
Scanning Channel 
“Working 
Channel” 
Wi-Fi 6 APs perform their scan on a dedicated 
radio chipset, and "Working channel and Non-
working Channel" operating mode must be 
selected to make this radio operational. 
DRM Time Control 
Disabled 
“OFF” 
Recommended to be enabled in a high-density 
environment. As the DRM feature makes dynamic 
changes and channel and power adjustments that 
could impact the channel plans, it is preferable 
that these are made outside of heavy load periods 
during events. 
DRM Start Time 
Disabled 
“00:00” 
02:00 setting will start the DRM feature at 2am, it 
will stop DRM 6h later by default 

<<<PAGE 35>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Band 
“2.4G, 5G all,  
5G low, 5G 
high, 6G” 
All selected 
All bands are selected by default for their 
management, each AP model applies the 
adaptations made for each:  
Dual-band models: 2.4G, 5G all  
Tri-radio models: 2.4G, 5G low, 5G high 
Channel DRM 
5G All “OFF” 
5G Low “OFF” 
5G High “OFF”  
Recommended to be enabled for 5GHz all (or 5GHz 
low and 5GHz high for the tri-radio model) to 
manage properly these bands in high density. 
 
 
Channel List 
0 selected 
Only supported when “Channel DRM” for 5G 
bands is enabled. A channel plan for France with 
non DFS can include for example all non DFS UNII-
1 channels and DFS UNII-2 first channels (i.e. 
channels 36 to 64) 
Channel Width 
Enabled 
“Auto” 
Recommended to select the 20MHz band width for 
WLAN in very high-density for both 2.4G and 5G 
bands 
Minimum TX 
Power(dBm) 
Disabled 
“configurable 
range from 3-
40 dBm” 
For very high-density RF, this parameter is 
recommended to be set at minimum Tx at 6 dBm 
for 2.4GHz and 12 dBm for 5GHz bands.  
 
Maximum TX 
Power(dBm) 
Disabled 
“configurable 
range from 3-
40 dBm” 
For very high-density RF, this parameter is 
recommended to be set at maximum Tx power at 
12 dBm for 2.4GHz and 18 dBm for 5GHz bands. 
 
External Antennas 
Gain(dBi) 
Enabled 
“configurable 
range from 1-
16 dBm” 
 Only applicable to APs supporting external 
directional antennas ie. AP1322 or AP1362. 
 
Beacon 
Interval(ms) 
Enabled 
“100” ms 
This indicates how often the 802.11 beacon 
management frames are transmitted by the AP, 
the configurable range is from 60-500ms. Default 
value of 100 ms is sufficient in most cases for RF 
designed for equipment/video. 
 

<<<PAGE 36>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
 
SSID 
 
Setting 
Default 
Guidelines 
SSID Setting 
Usage 
Guest Network 
(open or CP) 
Protected Network (Pre-Shared Key & optional 
Captive Portal) to be selected 
Allowed Band 
2.4GHz and 
5GHz  
selected 
Keep the default selection  
Encryption Type 
WPA2_PSK_AES 
Keep the default selection 
PSK/Passphrase 
Passphrase  
to confirm 
Enter up to 63 characters passphrase 
Client Controls 
802.11b Support 
Enabled 
Can only stay enabled when the 802.11a/g setting 
is enabled. Recommended to be disabled by 
default. 
Minimum Client Data Rate Controls 
2.4GHz Minimum 
Client Data Rate 
Controller 
Disabled 
Recommended to be enabled. 
2.4GHz Minimum 
Client Data Rate 
Disabled 
Recommended to be enabled, setting the value at 
6 Mbps. 
5GHz Minimum 
Client Data Rate 
Controller 
Disabled 
Recommended to be enabled. 
5GHz Minimum 
Client Data Rate 
Disabled 
Recommended to be enabled, setting the value at 
12 Mbps. 
Minimum MGMT Rate Controls 
2.4GHz Minimum 
MGMT Rate 
Controller 
Disabled 
Recommended to be enabled. 

<<<PAGE 37>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
2.4GHz Minimum 
MGMT Rate 
Disabled 
Recommended to be enabled, setting the value at 
6 Mbps 
5GHz Minimum 
MGMT Rate 
Controller 
Disabled 
Recommended to be enabled. 
5GHz Minimum 
MGMT Rate 
Disabled 
Recommended to be enabled, setting the value at 
12 Mbps 
 
 
Settings 
Default 
Guidelines 
Bandwidth Contract 
Upstream Bandwidth 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Downstream 
Bandwidth 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Upstream Burst 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Downstream Burst 
Disabled 
Configurable in ‘Kbits/s’ from 0-2621440 (Based on 
application parameters) 
Broadcast/Multicast Optimization 
Broadcast Key Rotation 
Disabled 
For security purposes and for broadcast handling 
optimization, this attribute recommended to be 
enabled. 
Broadcast Filter All 
Disabled 
Recommended to be enabled 
Broadcast Filter ARP 
Disabled 
Recommended to be enabled. for the same reasons 
explained above.  
Multicast Optimization 
Disabled 
Recommended to be enabled to allow efficient 
management of video streaming for a group of 
wireless cameras for example. It offers the 
possibility of converting multicast data packets 
into unicast data packets for wireless video 
transmissions. 
802.1p Mapping 

<<<PAGE 38>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Uplink/Downlink 802.1p 
markings for AC_BK, 
AC_BE, AC_VI, AC_VO 
categories 
802.1p 
default 
values 
802.1p marker values are those usually used by 
default for such use case.  But can be always 
adapted especially for AC video category defined 
for the stadium 
DSCP Mapping 
Trust Original DSCP 
Disabled 
The original DSCP can be trusted for all uplink 
traffic returning to the network. Recommended to 
be enabled 
Uplink/Downlink DSCP 
markings for AC_BK, 
AC_BE, AC_VI, AC_VO 
categories 
DSCP 
default 
values 
DSCP marker values are those usually used by 
default for such use case. They can be always 
managed or some values added if required for the 
stadium 
 
 
AP Group 
 
Setting 
Default 
Guidelines 
SSH 
SSH Login 
Disabled 
“OFF” 
Recommended to be enabled SSH console is 
used for rooftop stadium APs which could not be 
routinely dismounted during maintenance, 
ensuring their efficient access and management. 
SNMP Setting 
SNMP Agent 
SNMP and Trap 
Services 
“OFF” 
Recommended to be enabled SNMP is employed 
to gather and organize access point information, 
as well as monitor the activity of access points 
registered within the Omnivista 2500. 
Miscellaneous 
IGMP 
Snooping 
Disabled 
“OFF” 
Recommended to be enabled IGMP Snooping 
enables the switches to direct multicast traffic 
only to the ports where wireless cameras of the 
group are located, thus reducing the load on the 
WLAN network. 
 
 

<<<PAGE 39>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
6.3 Appendix C – Bill Of Material 
 
We give here an example of list of material that could be provided for the wireless LAN of a 
stadium with over 40,000 seats. The stadium has over 40,000 seats for visitors on a 20,000 
m² surface spread over two levels, 16,000 m² of facilities, halls and concession indoors and 
50 seats for a press box. A full 5-years support is provided for the WLAN solution for this 
stadium and HW/SW support is included in the list.  
 
For the wireless LAN of this stadium, we have provided a total of 454 access points, 
distributed as follows: 
- 
262 access points for seating areas. 
- 
192 access points for indoor and outdoor areas, including:  
o 160 access points for facilities and halls  
o 2 access points for the press box 
o 30 outdoor APs for equipment and video. 
 
Note that this BOM does not include: NEMA enclosures, servers appliances, DHCP/DNS 
servers appliances, LAN hardware, LAN core and satellites. 

<<<PAGE 40>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
 
Model 
Description 
Quantity 
Outdoors, equipment 
OAW-AP1361-RW 
OmniAccess Stellar Outdoor AP1361. Dual radio 
5GHz 4x4:4 / 2.4GHz 2x2:2 802.11ax, integrated 
omni. 1x1 scanning radio and BLE radio. 2.5GbE, 
1GbE, 1GbE SFP, USB, 48V DC.  
AP mount order seperately. Not for use in US, Egypt, 
Israel, Japan   
30 
SW5N-
OAWAP1360 
5 Yr End Customer Support Software for OAW-
AP1360 series. Includes 24x7 phone support, 
problem diagnosis, access to support portal, 
software updates and upgrades.  
30 
AP-MNT-OUT 
Outdoor mount kit (Pole/Wall). Standard 
configuration in the AP1251 product packaging. 
Applicable for OmniAccess Stellar AP1251, AP136x 
Outdoor series.  
30 
SW5R-
OAWAP1360 
5 Yr Renew End Customer Support Software for 
OAW-AP1360 series 
30 
Seats tier 1 
OAW-AP1322-RW 
OmniAccess Stellar Indoor AP1322. Dual radio 5GHz 
4x4:4 / 2.4GHz 2x2:2 802.11ax, external antenna 
connectors. 1x1 scanning radio and BLE radio. 1x 
2.5GbE, 1x 1GbE, USB, 48V DC. AP mount order 
seperately. Not for use in US, Egypt, Israel, Japan   
104 
ANT-S-M4-30 
Single band 5GHz, 4-element, Wall-mount, sector 
antenna , 13dBi, H-Plane 37°, E-Plane 37°, includes 
4* 30-35in RF cable (SMA-J/RPSMA-J), includes mount  
104 
OAW-AP-MNT-W 
Mounting kit, Type A wall mount and ceiling mount 
with screws. Applicable for OmniAccess Stellar 
AP1101, AP12xx and AP13xx Indoor series.  
104 
SW5N-
OAWAP1320 
5 Yr End Customer Support Software for OAWAP 
1320 Series. Includes 24x7 phone support, problem 
104 

<<<PAGE 41>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
diagnosis, access to support portal, software 
updates and upgrades.  
SW5R-
OAWAP1320 
5 Yr Renew End Customer Support Software for 
OAW-AP1320 Series. Includes 24x7 phone support, 
problem diagnosis, access to support portal, 
software updates and upgrades.  
104 
Seats tier 2 
OAW-AP1322-RW 
OmniAccess Stellar Indoor AP1322. Dual radio 5GHz 
4x4:4 / 2.4GHz 2x2:2 802.11ax, external antenna 
connectors. 1x1 scanning radio and BLE radio. 1x 
2.5GbE, 1x 1GbE, USB, 48V DC. AP mount order 
seperately. Not for use in US, Egypt, Israel, Japan   
160 
ANT-S-M4-60 
Dual band 2.4/5GHz, 4-element, Wall-mount, sector 
antenna , >5dBi, 60Hx60V 1x) includes 4* 30-35in RF 
cable   
160 
OAW-AP-MNT-W 
Mounting kit, Type A wall mount and ceiling mount 
with screws. Applicable for OmniAccess Stellar 
AP1101, AP12xx and AP13xx Indoor series.  
160 
SW5N-
OAWAP1320 
5 Yr End Customer Support Software for OAWAP 
1320 Series. Includes 24x7 phone support, problem 
diagnosis, access to support portal, software 
updates and upgrades.  
160 
SW5R-
OAWAP1320 
5 Yr Renew End Customer Support Software for 
OAW-AP1320 Series. Includes 24x7 phone support, 
problem diagnosis, access to support portal, 
software updates and upgrades.  
160 
HD indoors 
OAW-AP1331-RW 
OmniAccess Stellar Indoor AP1331. Dual radio 
2.4/5Ghz 4x4+4x4 802.11ax, with integrated omni 
antenna. 1x1 scanning and BLE radio. 2x 5GE up, 1x 
RS-232 Console,  
USB, 48V DC. AP mount to be ordered separately. 
Not for use in US, Egypt, Israel, Japan.   
160 
SW5N-
OAWAP1331 
5 Yr End Customer Support Software for 
OAWAP1331.  
160 

<<<PAGE 42>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Includes 24x7 phone support, problem diagnosis, 
access to support portal, software updates and 
upgrades.  
SW5R-
OAWAP1331 
5 Yr Renew End Customer Support Software for 
OAWAP1331. Includes 24x7 phone support, problem 
diagnosis, access to support portal, software 
updates and upgrades.  
160 
Press box 
OAW-AP1351-RW 
OmniAccess Stellar Indoor AP1351. Tri radio 2.4 + 
Dual 5Ghz 4x4+8x8+4x4 802.11ax, omni antenna. 1x1 
scanning and BLE radio. 2x 10GE up, 1x RS-232 
Console, USB, 48V DC.  
AP mount to be ordered separately. Not for use in 
US, Egypt, Israel, Japan.   
2 
SW5N-
OAWAP1351 
5 Yr End Customer Support Software for 
OAWAP1351. Includes 24x7 phone support, problem 
diagnosis, access to support portal, software 
updates and upgrades.  
2 
SW5R-
OAWAP1351 
5 Yr Renew End Customer Support Software for 
OAWAP1351. Includes 24x7 phone support, problem 
diagnosis, access to support portal, software 
updates and upgrades.  
2 
Omnivista 2500  
OV4-START-NEW 
OV4-START-NEW -OV2500 NMS-Starter Pack-NEW R4. 
Incl 10 ALU-E device lic. 1xlic. /switch in stack/VC 
config) 10 3rd Party Lic. 1x lic. / mgmt IP) VMM lic. 
for 10vm, 10 AP, 10GA, 10 BYOD licenses. Use add EX 
parts for add. config. Req. online activ.   
1 
OV-AP-NM-100-N 
OV-AP-NM-100-N  OV2500 NM R4 Lic - Lic. 100 AP-
NEW for 100 ALU-E  Stellar AP lic. (1lic. /Stellar AP)- 
Covers all Stellar AP models (11, 12xx & 13 series). 
Apply to OV2500 Serv. Pack NEW. Used w/other NM 
ext. NEW for adequate config. Act. Online   
5 
OV-GA-5K-N 
OV-GA-5k-N - OV2500 GA R4 Lic. - Lic. 5000 GA 
NEW for Guest Access Policy Manager enable 5000 
3 

<<<PAGE 43>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Guest Access concurrent active devices on ALU-E 
Network. Used w/other GA ext. NEW for adequate 
config. Act. Onlin 
OV4-NMS-HA 
OV4-NMS-HA - OmniVista 2500 HA (High 
Avaibility) Software license . Apply to OV2500 Serv. 
Pack NEW. Provide HA services for Single Instance 
OV2500 NMS platform including UPAM Service. 
Required Min OV4.3r1 to operate. Act. Online 
1 
SW5N-OV4START 
5YR 24x7 SUPPORT SOFTWARE for OV4-START-NEW / 
OV4-START-UPG. Incl. 24x7 Remote TEL. Supt., 24x7 
Remote Problem Diagnosis, SW. Update, / access to 
supt. portal.  
If MAINT. is ordered on one OV R4 Model No needed 
on all OV Model No for each OV server.   
1 
SW5N-
OVAPNM100N 
5YR 24X7 SUPPORT Software for OV2500 NMS - 
RELEASE 4 OV-AP-NM-100-N. Includes 24x7 Remote 
Tel Support, Problem Diagnosis, SW Updates, 
Support portal access Maintenance to be ordered on 
all OV Model No for each OV server. 
5 
SW5R-OV4START 
5YR Renewal SUPPORT Software OV4-START-NEW 
and OV4-START-UPG.One must submit $0 PO. If 
MAINT. is ordered on one OV Release 4 Model No it 
is needed on all OV Model No for each OV server.  
1 
SW5R-
OVAPNM100N 
5YR Renewal SUPPORT Software for OV2500 NMS - 
RELEASE 4 OV-AP-NM-100-N. Includes 24x7 Remote 
Phone Support, Problem Diagnosis, SW Updates, 
Support portal access Maintenance to be ordered on 
all OV Model No for each OV server.   
5 
SW5R-OVGA5KN 
5YR Renewal SUPPORT Software for OV2500 NMS 
- RELEASE 4 OV-GA-5K-N. Includes 24x7 Remote 
Phone Support, Problem Diagnosis, SW Updates, 
Support portal access Maintenance to be ordered on 
all 
OV Model No for each OV server. 
3 
SW5R-OV4NMS-
HA 
5YR Renewal SUPPORT Software for OV2500 NMS 
- RELEASE 4 OV4-NMS-HA. Includes 24x7 Remote 
1 

<<<PAGE 44>>>
 
 
 
OmniAccess Stellar high-density  
design guidelines 
 
 
 
 
 
 
 
Phone Support, Problem Diagnosis, SW Updates, 
Support portal access Maintenance to be ordered on 
all 
OV Model No for each OV server. 
 
 
 
6.4 Appendix D – Related documents 
 
https://www.al-enterprise.com/-/media/assets/internet/documents/omniaccess-stellar-wireless-
fine-tuning-best-practices-techbrief-en.pdf 
or search ‘best practices fine-tuning stellar’ on https://www.spacewalkers.com 
 
 
 


<<<DOC 2: omniaccess-stellar-wireless-fine-tuning-best-practices-techbrief-en.pdf | 起始页 45 | 28p>>>

<<<PAGE 45>>>
OmniAccess Stellar Wireless
Fine-Tuning Best Practices
Tech Brief
Fine-Tuning Best Practices

<<<PAGE 46>>>
Tech Brief
Fine-Tuning Best Practices
2
Table of Contents
OmniAccess Stellar Wireless Fine-Tuning Guidelines Introduction ................. 3
RF Management, Capacity and Smart Load Balance.......................................... 4
RF Management...................................................................................................... 4
Capacity versus Coverage...................................................................................... 6
Smart Load Balance................................................................................................ 8
Roaming Functionality & Sticky-client Avoidance............................................13
Roaming Functionality.........................................................................................13
Sticky-client Avoidance with IEEE 802.11k & 802.11v 
Standard Amendments........................................................................................13
Multicast Optimization and Broadcast Filter Controls.....................................15
Multicast Optimization ...................................................................................................... 15
Broadcast Filter ARP............................................................................................................ 16
Voice and Multimedia Controls for best QoE.....................................................17
RF Management Tested Recommendations for Voice over WLAN.................... 17
Dynamic Radio Management (DRM) settings............................................................ 18
QoS and Prioritizing Mapping Recommendations.................................................. 19
Wi-Fi Fine-tuning Evolution Under OmniVista Cirrus.......................................20
Analytical Results Fine Tuning Stellar Wi-Fi Solution.......................................20
Conclusion.............................................................................................................21
Appendix A.............................................................................................................22
Stellar WLAN Fine-Tuning Under the RF Profile Configuration Workflow.....23
Appendix B.............................................................................................................25
AP Group................................................................................................................25
Appendix C.............................................................................................................26
SSID Configuration Workflow and Expert Mode options.................................28

<<<PAGE 47>>>
Tech Brief
Fine-Tuning Best Practices
3
OmniAccess Stellar Wireless Fine-Tuning 
Guidelines Introduction
The purpose of this document is to provide specific OmniAccess Stellar Wireless LAN (WLAN) 
parameters to fine-tune the Stellar WLAN access points in Enterprise mode. This document does 
not replace any existing user guides or solution guides; for more detailed feature and functionality 
descriptions refer to the appropriate documentation. In some cases where detail explanations and 
configuration examples are needed, those documents will be referenced throughout this document. 
OmniAccess Stellar WLAN Access Point (AP) lineup described in this document support the most 
recent ratified IEEE 802.11ax standard or also known as Wi-Fi 6 and they are backwards compatible 
with the Wi-Fi 5 (802.11ac) APs. 
These APs have the capability to operate in Express or Enterprise modes; in Enterprise mode 
OmniVista provides a unified network management system (NMS) for both wired OmniSwitch and 
Stellar WLAN networking devices for provisioning, management, and monitoring capabilities from a 
single unified NMS interface. The configuration fine tuning best practices and recommendations are 
based on the Enterprise deployment mode.
The Stellar WLAN family of APs offers ease of management and provisioning via its support for 
a distributed architecture in clusters in Express mode and management via its web interface for 
clusters of up to 256 APs per cluster. Or via AP groups of up to 4000 APs in Enterprise mode to be 
centrally provisioned, managed and monitored via OmniVista NMS.

<<<PAGE 48>>>
Tech Brief
Fine-Tuning Best Practices
4
RF Management, Capacity and Smart Load Balance
RF Management
 
The goal of Radio Frequency (RF) spectrum management is to configure and calibrate radio 
settings for the wireless network; after the radio network is operational, the goal of RF spectrum 
management changes to that of tuning and adjusting radio parameters to maintain a high degree of 
performance. With Stellar WLAN, RF management is mostly automatic, requiring little configuration 
or intervention from the administrator. 
Stellar WLAN provides a set of functions to simplify WLAN operations and provide the relevant 
support for normal to dense 802.11ac/ax environments in addition to being backwards compatible 
with legacy 802.11n and b/g devices.
The key parameters of the Stellar RF management solution, as described in more detail in our 
Voice over WLAN Design Guide and OmniAccess Stellar Wireless User Guide is summarized in the 
Calibration and Optimization, is as follows: 
Calibration: Used continuously throughout the life of a wireless network; calibration functions allow 
network administrators to optimize power and sensitivity settings of the network on an antenna by 
antenna basis.
Optimization: Including DRM (Dynamic Radio Manager) which provides a channel list setting per 
radio that defines a perimeter for automatic channel assignment. Auto Radio Resource Allocation 
which allows individual access points to monitor for RF changes and in conjunction with calibration 
information to make appropriate channel assignment changes.
Note: A complete description of these RF management parameters and setting options, refer to the 
VoWLAN Design Guide and OAW Stellar-AP User Guide.
As stated above, the RF management functions operate automatically and are recommended for 
them to interact and automatically adjust based on the airspace environment, these settings are 
enabled by default and should remain enabled with minor adjustments based on the quality of 
connectivity user experience (QoE) scores that external monitoring tools can analyze. For example, 
deploying OmniVista Cirrus 10.x where one can graphically view reports showing the channel 
distribution information combined with channel utilization metrics to check that there is a fair 
distribution of wireless communications among all channels.
Additional points under this optimization fine tuning parameters to check; for example, adjacent APs 
need to use different radio channels to prevent interference between them. APs within range of each 
other should always be set to non-interfering channels to maximize the capacity and performance of 
the wireless infrastructure.
To avoid mutual interference with adjacent APs, ACS (auto channel selection) can be used to make 
the AP check and select the best channel under the radio environment automatically. The algorithm 
will help the AP to find the channel with the best radio performance available. And when working on 
5G radios, the Radio Dynamic Adjustment™ (RDA) technology can be used to define a “channel list” 
for the AP to select its channels from that recommended list.

<<<PAGE 49>>>
Tech Brief
Fine-Tuning Best Practices
5
Background scanning is the basis for some advanced features such as: wIDS, wIPS, RDA (ACS/APC) 
etc. When it’s turned OFF, the foreign AP detection and rogue suppression will stop, and the RDA 
technology will drop its precision. By default, background scanning is enabled, it is recommended to 
stay enabled. RDA is also used by Stellar WLAN to adjusts the radio working channel and transmitting 
power according to the wireless environment around it. It includes ACS, as referenced above, and 
Auto Power Control (APC) functions.
When RDA is disabled there is more risk that the manually defined values will create channel 
interference for new applications or roaming clients. In some cases, an administrator is tempted to 
set wide channels, but concerns and some design guidelines need to be exercised when widening 
channels. For instance, as stated through an Ekahau blog:
802.11ac or .11ax which allows for 80MHz and 160MHz wide channels… These wide Wi-Fi channels 
are created by bonding 20MHz channels together, using the center frequency to denote the channel. 
For example, channels 36 and 40 (each 20MHz) are bound together to make 40MHz channel 38, etc.
This wide channel implementation sounds good for better throughput; however, as also referenced 
in the Ekahau blog, that implementation introduces the Co-Channel Interference (CCI), plus the 
introduction of an extra 3dB of noise to the channel, doubling the noise. That scenario introduces 
more noise and no gain in signal. It equates to a lower SNR (Signal-to-Noise ratio), which will in turn 
force a lower Modulation Coding Scheme (MCS) rate, shrinking the throughput. This means that 
clients now take longer to transmit, driving up airtime utilization.
To avoid any of these possible ‘pitfalls’ keep the RDA enabled for Stellar APs and let it’s algorithm 
determine the best channels and transmitting power to help with this fine-tuning.

<<<PAGE 50>>>
Tech Brief
Fine-Tuning Best Practices
6
Capacity versus Coverage
Competitor’s recommendations point to two main Wi-Fi design guidelines to offer coverage with less 
access points deployed versus capacity with more Access Points deployed to handle the larger client 
connectivity for throughput capabilities instead of simply connectivity for coverage purposes. ALE 
recommends the capacity designs for a higher density of APs to provide the optimal performance; 
however, radio management needs to be at the forefront to help with the channel interference when 
APs are closer to each other.
To properly plan and deploy a capacity design, one needs to understand the principles of 
deployment. For instance, for the optimal placement of the APs throughout the building or campus, 
a site survey is required this will provide planning information that is required for proper capacity 
planning designs.
Capacity planning involves knowing or anticipating how the network is going to be used. The most 
important part is providing for the expected number and mix of clients connecting to the network. 
There are industry standard capacity numbers, and maximum client numbers per AP that are known, 
but other factors need to be considered. Refer to Figure 1: Capacity and deployment planning 
workflows.
Stellar AP deployment principles in capacity design scenarios
Use fixed objects to isolate APs and improve channel reuse; for example, in a large open floor office 
environment, people are better signal isolation objects, installing the APs on the side walls and 
vertical structural pillars with directional antennas pointing towards the cubicles and office areas are 
the recommended best practices.
In open areas, such as warehouse manufacturing floors where not much isolated objects are 
available and there is an open environment for the clients, one can also choose directional antennas 
to improve the isolation between APs and increase the signal strength to those the mobile Wi-Fi 
devices.
Figure 1: Capacity and deployment planning

<<<PAGE 51>>>
Tech Brief
Fine-Tuning Best Practices
7
Key Wi-Fi 6 feature benefits addressing the 
‘Principles of Deployment’
Wi-Fi 6 inherits the advanced MIMO features of Wi-Fi 5 and offers some new features which is 
optimal for capacity-based network deployments. These include the following key features:
•	
Orthogonal frequency division multiple access (OFDMA) which more efficiently shares 
channels to increase network efficiency and lower latency for both uplink and downlink traffic in high 
demand environments
•	
Multi-user multiple input, multiple output (MU-MIMO) which allows more downlink data to 
be transferred at once and enables an access point to handle a larger number of concurrent clients
•	
160 MHz channel utilization capability which increases bandwidth to deliver greater 
performance with low latency
•	
1024-QAM which enables throughput increases by encoding more data in the same amount of 
spectrum
•	
Target wake time (TWT) which enables scheduled sleep and wake times for better network 
efficiency and longer device battery life
•	
Transmit beam forming which improves signal power resulting in significantly higher rates 
at a given range.
Capacity Wi-Fi design with a balancing approach
To avoid mutual interference in a capacity design with adjacent APs, the ACS is used to make the APs 
check and select the best channel under the radio environment automatically. For 5GHz radio, the 
Radio Dynamic Adjustment™ technology (sometimes referenced in the documentation as RDA) in 
Stellar WLAN can be used to define a “Channel List” to make the AP select the channels from a 
specified list. By default, the working channel and transmitting power are automatically managed by 
the RDA technology. One can specify a channels list/power range applicable for auto selection, which 
reduces the risk of low power transmitting or channel conflict.
The background scanning functionality is used in multiple functions to examine the radio frequency 
environment in which the wireless network is operating, discovering neighbor APs, while identifying 
interference, and attacks. Background scanning is the basis of some advanced features such as, 
wireless IDS/IPS and the RDA technology which in turn leverages the ACS and APC mechanisms.
The ACS is recommended for the AP to check and select best channel for the client communications. 
And the APC checks and selects the best power settings so they does not interfere with other APs, 
especially for this recommended capacity design where more APs have overlapping coverage and 
they must control and keep its signal to noise ratio at lower levels.
In the case of a coverage network design, fewer APs are deployed and spaced significantly apart from 
each other. The APs operate at a higher transmit power and therefore cover larger areas. However, 
in a balanced AP design, which leans towards the capacity-based network design, more APs are 
deployed operating at a lower transmit power to keep the cell size smaller. Through this deployment, 
devices within these cells associate at higher rates and experience better performance.
It is recommended to deploy OmniAccess Stellar WLAN in a balanced-based design or also called 
‘capacity design’ for new deployments to offer better capacity, especially for networks that uses 
wireless as a primary medium to access the network. The Stellar WLAN RF management algorithm 
will configure and calibrate the radio settings for the wireless network to leverage the Wi-Fi Fine 
Tuning of the AP’s radio parameters to maintain a high degree of performance.

<<<PAGE 52>>>
Tech Brief
Fine-Tuning Best Practices
8
Smart Load Balance
The Smart Load Balance (SLB) configuration features improves the user experience when accessing 
wireless connectivity by guiding a user’s client device to connect to a free wireless channel or AP and 
denying access to APs with weak signal. These SLB features default settings and recommended best 
practice adjustments are explained in the following sections. Refer to Figure 2, below for configura-
tion options.
Note: The 5G Low and 5G High configuration options displayed in Figure 2 are only supported in the 
AP1230 models. These configuration options are referenced later in the “Voice and Multimedia Controls” 
section.
Optimize Channel Utilization
One important factor affecting network capacity is channel utilization. If the channel utilization 
reaches 50% or greater before deployment the WLAN capacity will be significantly impacted. Channel 
utilization is driven by the following factors:
•	
Interference from other WLAN systems such as ad-hoc personal Wi-Fi hotspots
•	
Non-Wi-Fi signal interference such as Bluetooth or other wireless technologies
•	
Optimization of low transmission rate data frames and management frames. It is difficult to 
optimize AP configurations in the above points 1 & 2 which makes it very important to optimize the 
channel utilization point. In capacity-based scenarios, it is recommended that the data frames and 
management frames be optimized separately, and the transmission rates for those frames must be 
increased, appropriately.
To help illustrate an ‘over-the-top’ wireless SSID overhead case, we used an external tool planning 
called Revolution Wi-Fi Capacity Planner with multiple SSIDs operating on the same channel, refer to 
Figure 3:
Figure 2: Smart Load Balance Fine Tuning Configurable Options
5G Low and 5G High 
configuration options 
are only supported by 
the AP1230 models

<<<PAGE 53>>>
Tech Brief
Fine-Tuning Best Practices
9
The model results in Figure 3 contain forty percent (40%) of the clients operating based on the 
802.11ac standard and the other sixty percent (60%) are a mixture of legacy .11n and .11g devices. 
This table illustrates the number of SSIDs as to the number of Access Points operating on the same 
channel. As you can see from these results, as one increases the number of SSIDs it contributes to 
the Wi-Fi network overhead based on the added beacons and probe response frames.  Again, this 
is just an extreme case where no competent engineer would design their WLAN in this manner, but 
we are making this point to illustrate the overhead caused when a congested channel is selected and 
when the load balancing algorithm is disabled.
The percentage figures shown in the above table is the airtime overhead caused by the number 
SSIDs enabled in that Wi-Fi environment, to determine what the actual client serving airtime is offe-
red, the overhead is subtracted from the available airtime that can be used by the clients to transmit 
and receive data. For example, based on this analysis, if one configures ten SSIDs on twelve Access 
Points operating on the same channel this will consume 50% of the available airtime. The obvious 
key point here is that all APs are on the same channel, this is where the Auto Channel Selection 
(ACS) and Auto Power Control (APC) functions in Stellar WLAN come into light to help distribute 
these overhead beacons and probe response frames into multiple non-interfering channels. This is a 
great reason to keep the Dynamic Radio Adjustment technology enabled. The analysis for the 2.4Ghz 
band shows worse results, there is over 50% overhead for just three SSIDs for eight APs on the same 
channel. The point is, be careful and do not go overboard in trying to fine-tune certain parameters, 
the Wi-Fi environment will be better served when enabling most of its auto functionality to allow its 
mechanisms to better load balance.
Figure 3: Revolution Wi-Fi Capacity Planner Output
1
2
3
4
5
6
7
8
9
10
11
12
1
0.42%
0.83%
1.25%
1.67%
2.08%
2.50%
2.92%
3.34%
3.75%
4.17%
4.59%
5.00%
2
0.83%
1.67%
2.50%
3.34%
4.17%
5.00%
5.84%
6.67%
7.51%
8.34%
9.17%
10.01%
3
1.25%
2.50%
3.75%
5.00%
6.25%
7.51%
8.76%
10.01%
11.26%
12.51%
13.76%
15.01%
4
1.67%
3.34%
5.00%
6.67%
8.34% 10.01% 11.68%
13.34%
15.01%
16.68%
18.35%
20.02%
5
2.08%
4.17%
6.25%
8.34% 10.42% 12.51% 14.59%
16.68%
18.76%
20.85%
22.93%
25.02%
6
2.50%
5.00%
7.51% 10.01% 12.51% 15.01% 17.51%
20.02%
22.52%
25.02%
27.52%
30.02%
7
2.92%
5.84%
8.76% 11.68% 14.59% 17.51% 20.43%
23.35%
26.27%
29.19%
32.11%
35.03%
8
3.34%
6.67% 10.01% 13.34% 16.68% 20.02% 23.35%
26.69%
30.02%
33.36%
36.70%
40.03%
9
3.75%
7.51% 11.26% 15.01% 18.76% 22.52% 26.27%
30.02%
33.78%
37.53%
41.28%
45.04%
10
4.17%
8.34% 12.51% 16.68% 20.85% 25.02% 29.19%
33.36%
37.53%
41.70%
45.87%
50.04%
11
4.59%
9.17% 13.76% 18.35% 22.93% 27.52% 32.11%
36.70%
41.28%
45.87%
50.46%
55.04%
12
5.00% 10.01% 15.01% 20.02% 25.02% 30.02% 35.03%
40.03%
45.04%
50.04%
55.04%
60.05%
13
5.42% 10.84% 16.26% 21.68% 27.10% 32.53% 37.95%
43.37%
48.79%
54.21%
59.63%
65.05%
14
5.84% 11.68% 17.51% 23.35% 29.19% 35.03% 40.87%
46.70%
52.54%
58.38%
64.22%
70.05%
15
6.25% 12.51% 18.76% 25.02% 31.27% 37.53% 43.78%
50.04%
56.29%
62.55%
68.80%
75.06%
16
6.67% 13.34% 20.02% 26.69% 33.36% 40.03% 46.70%
53.38%
60.05%
66.72%
73.39%
80.06%
17
7.09% 14.18% 21.27% 28.36% 35.44% 42.53% 49.62%
56.71%
63.80%
70.89%
77.98%
85.07%
18
7.51% 15.01% 22.52% 30.02% 37.53% 45.04% 52.54%
60.05%
67.55%
75.06%
82.56%
90.07%
19
7.92% 15.85% 23.77% 31.69% 39.61% 47.54% 55.46%
63.38%
71.31%
79.23%
87.15%
95.07%
20
8.34% 16.68% 25.02% 33.36% 41.70% 50.04% 58.38%
66.72%
75.06%
83.40%
91.74% 100.00%
21
8.76% 17.51% 26.27% 35.03% 43.78% 52.54% 61.30%
70.05%
78.81%
87.57%
96.33% 100.00%
22
9.17% 18.35% 27.52% 36.70% 45.87% 55.04% 64.22%
73.39%
82.56%
91.74% 100.00% 100.00%
23
9.59% 19.18% 28.77% 38.36% 47.95% 57.54% 67.14%
76.73%
86.32%
95.91% 100.00% 100.00%
24
10.01% 20.02% 30.02% 40.03% 50.04% 60.05% 70.05%
80.06%
90.07% 100.00% 100.00% 100.00%
25
10.42% 20.85% 31.27% 41.70% 52.12% 62.55% 72.97%
83.40%
93.82% 100.00% 100.00% 100.00%
26
10.84% 21.68% 32.53% 43.37% 54.21% 65.05% 75.89%
86.73%
97.58% 100.00% 100.00% 100.00%
27
11.26% 22.52% 33.78% 45.04% 56.29% 67.55% 78.81%
90.07% 100.00% 100.00% 100.00% 100.00%
28
11.68% 23.35% 35.03% 46.70% 58.38% 70.05% 81.73%
93.41% 100.00% 100.00% 100.00% 100.00%
29
12.09% 24.19% 36.28% 48.37% 60.46% 72.56% 84.65%
96.74% 100.00% 100.00% 100.00% 100.00%
30
12.51% 25.02% 37.53% 50.04% 62.55% 75.06% 87.57% 100.00% 100.00% 100.00% 100.00% 100.00%
Number of Access 
Points
On The Same Channel
Number of SSIDs

<<<PAGE 54>>>
Tech Brief
Fine-Tuning Best Practices
10
Band Steering
Although most clients support 5GHz connection there are still some clients that select the 2.4GHz 
band. Band steering technology enables clients that support 5GHz to connect to 5GHz first. For 
newer Wi-Fi device deployments, this attribute is recommended to be enabled. 
Note: Apple ios devices can have issues with the ‘band steering’ variable when enabled where it may blacklist the SSID 
for a few minutes. Caution when enabling for heavy Apple ios device deployments.
Force 5G
When the “Force 5G” parameter is enabled (disabled by default), it forces dual band capable wireless 
clients to connect to 5GHz and does not allow them to connect at 2.4GHz. This functionality is 
recommended stay disabled for environments where the client population has a mixture of 2.4GHz 
and 5GHz clients. When enabled it will reject all association requests from 2.4Ghz clients.
Association & Roaming Received Signal Strength Indicator (RSSI)
The Association RSSI Threshold setting is used to set thresholds at the RF Profile level for optimizing 
connectivity when associating with an AP by denying client access with a weak signal. Clients with a 
signal strength value lower that the association signal threshold will not be allowed to connect to the 
AP. By default, the RSSI threshold is disabled (0). These thresholds can be applied to 2.4G or 5G bands 
separately; or for newer (802.11ax and .11ac) capable devices, the association parameters can also be 
set per SSID basis through the “Minimum Client Data Rate Controller” for both bands.
Before we get into more details of these types of RSSI Thresholds, let’s clarify how Stellar Wireless 
Received Signal Strength Indicator is converted to decibel to milliwatt measurements. The RSSI 
recommendations listed below can be converted to decibels in relation to a milliwatt or also referred 
as to dBm.  The mathematical formula used for this calculation is based on the RSSI value (in a range 
from 0 through 99 supported in Stellar WLAN), the RSSI value is subtracted from -96 dBm which is 
the base noise floor for this calculation to obtain the desired value in dBm’s to support the VoIP and 
streaming video applications, as illustrated in Figure 4, below. This reference for “Acceptable Signal 
Strengths” table comes from various industry sources.
Signal 
Strength
Signal Rating
Applications
Supported
-30dBm
Outstanding – Not typical since the Wi-Fi client is only a few 
feet away from the Access Point to achieve this signal strength.
N/A
-67 dBm
Very good – Minimum signal strength for applications that 
require time-sensitive communications.
VoIP / VoWLAN, Video 
streaming
-70 dBm
Minimum signal strength for non-sensitive packet-delay 
delivery.
Email, web
-80 dBm
Minimum signal strength for device connectivity. 
Packet delivery is unreliable.
N/A
Figure 4: Acceptable Signal Strengths

<<<PAGE 55>>>
Tech Brief
Fine-Tuning Best Practices
11
For the Stellar WLAN, we are using -96 dBm as the base noise floor less the RSSI threshold value of 
(29) it provides the value of -67 dBm’s for a minimum very good signal strength converted to decibels 
to a milliwatt representation to support good QoE for VoIP and video streaming applications.
These fine-tuning recommendation parameters help with issues related to “time-to-connect” and 
“unsuccessful connectivity attempts” and the overall QoE for a positive Wi-Fi connectivity experience. 
The recommended minimum “Association RSSI Threshold” setting is (22) for both 2.4G and 5G bands. 
This threshold allows clients to associate to the Access Point at minimum signal strength of -74 dBm 
using the -96 dBm as the base noise floor for conversion from the RSSI value.
Another mechanism support for client association to Access Points is via the Minimum Client Data 
Rate parameters, this option is enabled in the SSID configuration level through the minimum data 
rate controller parameters for each of the bands. For example, for the 2.4GHz Minimum Client Data 
Rate the recommended minimum rate is (12), which means 12 Mbps, and the way this mechanism 
works is when a client’s data speed is lower than those settings, the client will be denied association 
to that SSID. A similar process happens for the 5Ghz clients, the recommended minimum associating 
data rate is 24 Mbps.
For device roaming purposes, minimal adjusting of parameters is required since the Stellar Access 
Points support 802.11r, 802.11k and 802.11v supplemental standards which are better mechanisms 
to handle roaming decisions. However, for this functionality to work the client side needs to support 
those supplemental standards, as well.  The roaming RSSI thresholds can be used in conjunction with 
.11k and .11v standards for the devices that support them. These options will be discussed further is 
a separate section when addressing the sticky-client issue.
But first, let’s address the Roaming RSSI Threshold recommendations based on RSSI values in the 
same manner as discussed for the association mechanism. When the client’s RSSI value is lower 
than the threshold value that client will be guided to roam to another AP with a stronger signal.
By default, the Roaming RSSI is disabled with a value of zero. This functionality is also applied to the 
2.4G or 5G bands separately.
These roaming decisions can best be enabled for coverage-based network designs since there will be 
less Access Points deployed and weaker signals at the coverage edges; however, for ALE’s best design 
practices, the capacity-based design is recommended with a higher AP density to eliminate most 
weak signals between APs. With this scenario minimal fine-tuning of those thresholds is required.  
Nevertheless, for those legacy devices that still need the system control then the Roaming RSSI 
threshold is recommended to be (25) for both 2.4G and 5G bands to trigger roaming at -71 dBm to 
an AP that can deliver better signal strength to maintain the best QoE connectivity.
Note: In certain time-sensitive applications supported by Stellar WLAN, the roaming thresholds need to be more 
aggressive on a per band basis. For instance, at one of our customer deployments we configured roaming RSSI 
thresholds of 34 for 2.4G and 28 for 5G bands. Those thresholds will trigger roaming at 62 dBm for 2.4G and at 68 
dBm for 5G clients with those minimum signal strength thresholds.
The “Minimum MGMT Rate Controls” parameters can also help with roaming decisions when 
working with or without the 802.11k and 11v standards. The recommended minimum MGMT rate 
setting is also 12 Mbps for the 2.4G and 24 Mbps for the 5G bands. These controller fields can be 
enabled or disabled for each of the radio bands through the “Minimum MGMT Rate Controller” 
settings. 
The higher the value means less coverage; the lower value means larger coverage, but since ALE 
recommends the capacity-based design there will be more Access Points to serve, offering stronger 
signals to minimize roaming. But once devices need to roam, they will maintain their 
high-performance based on those minimum rate requirements.
Note: The association Minimum Client Data Rate setting needs to be equal or higher than the Minimum MGMT Rate.  
These configuration options can be set at the SSID configuration level (as referenced in Appendix C).

<<<PAGE 56>>>
Tech Brief
Fine-Tuning Best Practices
12
Airtime Fairness
The airtime fairness attribute enables or disables (disabled by default) the airtime fairness 
functionality on 2.4G and 5G bands. The airtime fairness feature provides equal access to all 
wireless clients, regardless of client type, capability (802.11ax, 802.11ac, 802.11n, 802.11a, 802.11g, 
802.11b), thus delivering uniform performance to all clients. This feature prevents the clients from 
monopolizing resources. When enabled or disabled, its status change requires a reboot of the AP for 
the change to take effect. This parameter is recommended to be enabled, this functionality provides 
equal time slices in the air to all clients, and since the latest 802.11ax/ac standards in devices 
supporting faster processors will be able to take advantage of those airtime slices in a more efficient 
manner than the legacy devices.
Background Scanning 
The Background Scanning configurable parameters are under the umbrella of the Smart Load 
Balancing features, it contains the enablement options for some advanced features such as, the 
Radio Dynamic Adjustment (RDA) technology;  Auto Channel Selection/Auto Power Control  
(ACS/APC), wireless Intrusion detection and prevention systems (wIDS & wIPS), and among other 
functionality that may be required to be adjusted to present the best quality of connectivity 
experience. When background scanning is turned OFF, the rogue AP detection and suppression will 
stop and the Radio Dynamic Adjustment™ technology will drop its precision. By default, background 
scanning is Enabled, and it is recommended to stay that way.
For the RF fine-tuning purposes, let’s look at the Radio Dynamic Adjustment technology and how 
Stellar wireless architecture implements it.  RDA technology adjusts the radio working channel 
and transmitting power according to the wireless environment around it. It includes Auto Channel 
Selection (ACS) and Auto Power Control (APC) functions. RDA is Enabled by default. The scanning 
interval of Background Scanning can be configured from 5 seconds to 3 hours. For highly sensitive 
packet delay use cases, it is recommended to increase the setting to 20 seconds. Keep in mind that 
an interval longer than 60 seconds loses RDA accuracy, and it affects the wIPS functionality, 
it recommended to keep it under 40 seconds.
The Radio Dynamic Adjustment technology is also controlling adjacent APs, so they use different 
radio channels to prevent interference. APs within range of each other should always be set to non-
interfering channels to maximize the capacity and performance.  And this where the auto channel 
selection setting can be used to make the AP check and select the best channel under its radio 
environment automatically. The algorithm will help the AP find the channel with the least overhead.
In relation to the Band Steering and Force 5G variables that were discussed, previously, these RDA, 
ACS, and APC features work together to reduce the co-channel interference and increase available 
bandwidth for the connected devices.

<<<PAGE 57>>>
Tech Brief
Fine-Tuning Best Practices
13
Roaming Functionality & Sticky-client Avoidance
Roaming Functionality
 
There are two options to handle device roaming more efficiently; for example, one is through 
the Roaming RSSI Threshold, as discussed in the previous section, which sets thresholds to deny 
clients access to Access Points with weak wireless signals. The Roaming RSSI variables are used 
in conjunction with the supplemental standards 802.11k and 802.11v. Clients that support those 
standards will be informed to which AP to roam to when the threshold is reached, this functionality is 
addressed later in the solution to avoid the sticky-client problem (more details in the next section).
The Layer 2 roaming parameter is recommended to always be enabled; similarly, for L3 Roaming it 
is recommended to be enabled. The functionality of Layer 3 roaming is that it allows clients to move 
between APs with access to other subnets and VLANs. We recommend for this parameter to also be 
enabled; this will assist the wired side of the network to enforce the routing for better controls via 
policies and ACLs through higher performing Layer 3 switches.
One may be asking what does the Forwarding Database (FDB) Update on Association attribute have 
to do with roaming, well, when enabled and when a client roams to a new AP, the new associated AP 
will send ARP packets to the uplink switch to notify the switch to change the downstream forwarding 
port for the wireless client’s traffic. Therefore, to keep the network’s forwarding tables, the client’s 
location and network path updated this parameter is recommended to be enabled.
The Opportunistic Key Caching (OKC) is also related to roaming, when enabled it triggers a cached 
Pairwise Master Key (PMK) to be used when the client roams to a new Access Point. This also helps 
with the Sticky-Client avoidance functionality. If re-authentication happened every time a client 
roamed it would defeat the purpose for device mobility while using the wireless environment, this 
OKC functionality allows for faster roaming of clients without the need for a complete 802.1x re-
authentication.  
Sticky-client Avoidance with IEEE 802.11k & 802.11v 
Standard Amendments
The sticky-client issue happens when Wi-Fi clients attempt to roam; those clients tend to hang on 
to the original access point they associated with, rather than moving to a nearby AP that has better 
signal strength. Clients must monitor indicators of the health of their wireless connection, such 
as the signal strength (RSSI), their signal to noise ratio, and the number of errors/retries they are 
experiencing on that connection.  Once these indicators start to degrade, they must start to probe 
for alternative access points, ready to make the jump to a new access point that will provide a better 
quality connection. The IEEE 802.11k and 802.11v standard amendments forces roaming when 
connection speeds hit low rates. 
It is recommended to have the 802.11k and 11v controls enabled. These advanced controls include 
mechanisms for performing various measurements of the WLAN station’s environment; for example, 
the 802.11k controls allow a client to request information about that environment. One of the most 
useful mechanisms from a client’s roaming perspective is the neighbor report. A neighbor report 
is requested by a client which contains a list of the APs the APs each of the knows about. Since the 
client has this information, it improves its ability to make the roaming decision. However, keep in 
mind that use of 802.11k functionality is dependent on the client’s support for that feature.

<<<PAGE 58>>>
Tech Brief
Fine-Tuning Best Practices
14
The 802.11v defines a service that allows stations on WLAN devices to exchange data that provides 
them with awareness of the network conditions. One of the mechanisms provided in 802.11v is ‘BSS 
Transition Management’. This mechanism allows an access point to request that a client roam to a 
specific AP, or it provides a set of preferred APs.  This mechanism also provides the client with better 
data to improve its roaming decisions. 
In addition to the .11k and .11v parameters, the 802.11r is also recommended to be enabled to sup-
port the Fast BSS Transition mechanism to minimize the delay when a client transitions from one BSS 
to another within the same group.
Even though, when the load balancing algorithm is enabled supporting band steering, RSSI 
thresholds for client’s connections, and client count based load balancing among neighboring APs; 
none of that functionality solves the problem of sticky clients or guarantees that the Wi-Fi network is 
providing optimal performance to all its connected clients. Therefore, the enabling of the 802.11k / 
802.11v supplemental standards to force roaming when connection speeds reach low rates is a requi-
rement to avoid the ‘sticky-client’ issues. But keep in mind the lowest common denominator is that 
the client needs to support those standard amendments to force the roaming gracefully and to avoid 
those issues.

<<<PAGE 59>>>
Tech Brief
Fine-Tuning Best Practices
15
Multicast Optimization and Broadcast Filter Controls
Multicast Optimization 
 
In a networking environment where IP multicast traffic is used, destination hosts signal their in-
tent to receive a specific IP multicast stream by sending an Internet Group Management Protocol 
(IGMP) request to a nearby networking switch and Access Point. This process is referred to as IGMP 
Snooping. This functionality is very important for large subnets and for layer 2 roaming functionality 
because of the limited airspace for data transmission. Before we begin with the fine-tuning of the 
broadcast and multicast optimization recommendations for the broadcast key rotation and filters, 
the IGMP snooping parameters needs to be enabled per AP Group basis, see Figure 5, below:
The Multicast Optimization parameter per SSID is enabled by default and the “Number of Clients” 
attribute is defaulted to six clients to support high throughput via the multicast services. This num-
ber is configurable under the QoS section settings on a per SSID basis. The “Multicast Based Channel 
Utilization” attribute is used to configure the based channel utilization optimization percentage; the 
range is (0 – 100) and the default is (90). For the limited number of devices supporting multicast 
services, these defaults are the recommended with minor adjustments depending on the increase or 
decrease of the number of multicast clients joining the multicast services over the WLAN.
In reference to the “Broadcast Key Rotation” attribute, this is used to enable/disable (disabled by 
default) the broadcast key rotation function. When enabled, the broadcast key will be rotated after 
every interval time. The key rotation time interval is defined in minutes; the rotation key range is (1 
– 1440), the default is 15 minutes (when enabled). This parameter is recommended to be enabled to 
assist in the multicast optimization and fine-tuning options.
Figure 5: Turning ‘ON’ IGMP Snooping

<<<PAGE 60>>>
Tech Brief
Fine-Tuning Best Practices
16
Broadcast Filter ARP
The “Broadcast Filter ARP“ enables/disables broadcast filtering. When enabled, all broadcast frames 
are dropped, except DHCP and ARP frames. The Broadcast Filter ARP attribute is recommended to 
be enabled so the AP can act as an “ARP Proxy“. If the ARP-request packet requests a client’s MAC 
address and the Stellar AP knows the client’s MAC and IP address, the AP will respond to the ARP-
request but not forward the ARP-request (broadcast) to all broadcast domains. This reduces ARP 
broadcast packet forwarding and significantly improves network performance. The APs do not act as 
ARP proxy for gratuitous ARP packets. When the device gets an IP from DHCP or IP release/ renew, 
the station will send gratuitous ARP packets; the AP will not respond to those special ARP packets, but 
will broadcast them normally.
The Broadcast Filter ARP attribute while enabled helps alleviate issues with Wi-Fi devices (such as, 
iPhones & Chromebooks) which do not play well in some cases with dynamic frequency selected 
channels. These problems may cause iPhones and Chomebooks to have issues when roaming, 
sticky-client, and randomness poor performance. Apple and Google design documents recommend 
5GHz only SSIDS to support these devices; therefore, enabling band steering and force 5G are 
requirements for these types of devices which fall in line with ALE’s recommendations from an earlier 
section when those parameters were discussed.

<<<PAGE 61>>>
Tech Brief
Fine-Tuning Best Practices
17
Voice and Multimedia Controls for best QoE
The Voice and Video Awareness attribute is used to enable/disable (disabled by default) voice and 
video awareness services. This functionality is used in conjunction with background scanning, this 
function allows it to be aware of existing traffic on the APs. If there is an ongoing voice/video service, 
scanning should not be performed to ensure uninterrupted traffic; scanning resumes once there are 
no active voice/video sessions and this is controlled via this attribute.
Refer to the “vowlan-guidelines-stellar-awos4.0.2” design guide for detailed configuration options 
for the QoS parameter settings to handle the voice and multimedia applications over an OmniAccess 
Stellar WLAN network, below are specific settings that we would like to highlight in this document, 
but a explained in greater detail in the VoWLAN guide.
RF Management Tested Recommendations for Voice over WLAN
 
The key settings for the voice and video awareness are at the RF Profile level by enabling 
Band Steering and 5G AirTime Fairness, these are the basic prerequisites for guaranteeing QoE for 
these types of applications.
While Band Steering is a useful feature allowing APs to recommend users to use the 5GHZ instead of 
the 2.4 GHz band, the experience shows that for Time Sensitive applications, (like Voice over WLAN) 
we should dedicate a SSID with only the 5 GHz enabled and no Band Steering. Such configuration 
improves the quality of experience for voice users Wi-Fi optimizing the band usage, the roaming, and 
the compatibility with some devices (like Apple which recommends such configuration).
The other prerequisites include Background Scanning and Voice and Video Awareness buttons which 
are already enabled by default. Make certain the background scanning duration is configured for 110 
milli seconds, as denoted in Figure 6. 
Figure 6: RF Management for VoWLAN

<<<PAGE 62>>>
Tech Brief
Fine-Tuning Best Practices
18
Dynamic Radio Management (DRM) settings
Dynamic Radio Management (DRM) settings are configured through the ‘RF Profile’ menu on a per 
AP Group basis, refer to Figure 7 for the configuration recommendations. As referenced previously, 
the 5G Low and 5G High configuration options displayed in the Figure 7 are only supported in the 
AP1230 models. In most cases, selecting 20MHz channel width for the 5G band is recommended for 
this application.
When configuring the 5G Low and 5G High options, do the following: 1) select all 8 channels for the 
5G Low and once again, 2) leave the channel width and power setting on Auto for both options; and 
3) then select 11 channels to have sufficient isolation between them for the 5G High option, change 
the channel width from Auto to 20MHz, but leave the power setting on Auto; and leave the Multi-
MIMO (MU-MIMO) setting as factory default which is already enabled.
Figure 7: RF Management for VoWLAN & DRM

<<<PAGE 63>>>
Tech Brief
Fine-Tuning Best Practices
19
QoS and Prioritizing Mapping Recommendations
In the SSID configuration options, under the “Advanced WLAN Service Configuration”, one can 
configure the 802.1p Mapping and the DSCP Mapping attributes. The 802.1p Mapping attribute is 
used to configure the uplink and downlink mapping mechanism between Wi-Fi Multimedia (WMM) 
access categories and 802.1p priority. The uplink traffic can only be mapped to a single value; 
however, the downlink traffic can be mapped to multiple values. The fields are already populated with 
the default values but can be changed based the application requirements.
The DSCP Mapping attribute is used to configure the uplink and downlink mapping mechanism 
between Wi-Fi Multimedia (WMM) access categories and DSCP priority. The uplink traffic can only be 
mapped to a single value; however, the downlink traffic can be mapped to multiple values. The fields 
are already populated with the default values but can be changed based on the required mapping 
value. 
The Trust Original DSCP attribute, if enabled, the original DSCP mapping for uplink traffic is trusted 
(disabled by default).
Mapping ranges and default values:
- Video - WMM Video will be mapped to the 802.1p value.
•	
Uplink - Maps uplink traffic (from AP to network), default = 32.
•	
Downlink - Maps downlink traffic (from network to AP), default = 32, 40)
- Voice - WMM Voice will be mapped to the 802.1p value.
•	
Uplink - Maps uplink traffic (from AP to network), default = 48
•	
Downlink - Maps downlink traffic (from network to AP), default = 48, 56)
For the detailed configuration guidelines and explanations for fine tuning voice and WMM 
parameters for these Stellar WLAN attributes please refer to the latest VoWLAN Design Guide for the 
OmniAccess Stellar Wireless.

<<<PAGE 64>>>
Tech Brief
Fine-Tuning Best Practices
20
Wi-Fi Fine-tuning Evolution Under OmniVista Cirrus
Analytical Results Fine Tuning Stellar Wi-Fi Solution
 
OmniVista Cirrus 10.1 is the first phase of this Artificial Intelligence driven tool to simplify monitoring 
and troubleshooting of a Stellar Wireless network through detailed QoE measurements and Wi-Fi 
Analytics in an easy-to-read dashboard displays.
• OmniVista Cirrus provides advanced data analytics powered by its Cloud Analytics Engine 
that processes raw data and presents it in useful information for the various stakeholders to 
provide insights for proactive service assurance.
•	QoE encompasses many connectivity factors from successful connectivity attempts, to 
time-to-connect, to roaming, to capacity availability; airtime-fairness, and among other key QoE 
attributes which help influence the quality of the user’s experience while securely connecting 
and roaming on a Stellar wireless network.
This NMS tool aids with the “Successful Connects” metrics, this functionality helps track failures 
during Wi-Fi device: Association, Authorization, DHCP phases and Captive Portal.
All the fine-tuning recommendations discussed in this document can serve as a great training tool 
for OmniVista Cirrus 10.x. The evolution of this tool will provide self-provisioning decisions to fine-
tune the network in the future; however, for today, we can help it by fine-tuning parameters based 
on the analytics data collected by OmniVista Cirrus and converted to information through its AI-
driven Cloud Analytics Engine to be presented via usable widgets (refer to the OmniVista Cirrus 10.x 
documentation for a complete explanation about this evolving NMS tool. For instance, in reference 
to the Revolution SSIDs overhead capacity planning tool that we referenced earlier when dealing 
with a single channel overhead problem.  OmniVista Cirrus 10.x provides us with widgets to see the 
Channel Distribution under the Network Analytics Dashboard section. As shown in Figure 8, these 
widgets show the 2.4GHz and 5GHz frequency bands with the channels that are being used within 
each frequency band; for example, Figure 8 illustrates the 5GHz distribution.
Figure 8: Channel distribution and utilization Sample

<<<PAGE 65>>>
Tech Brief
Fine-Tuning Best Practices
21
If the QoE scores are low, then the administrator can use this information combined with the 
Channel Utilization metrics to check and adjust to accomplish a fair distribution of the wireless 
communications among all the channels. As illustrated in Figure 8, all the clients are well distributed, 
utilizing 9.1% of each of the 5GHz channels except for channel 40 which is being utilized by more 
clients than the other channels. 
ALE understands that there are many Wi-Fi parameters that can be adjusted or simply left as 
defaults, so they can operate according to the standard’s thresholds.  The purpose of this document 
is to address specific parameters that are recommended to be fine-tuned based on the application 
and the device requirements. 
Refer to the following appendices for the Wi-Fi configuration fine-tuning options referenced 
throughout the document. These appendices provide a more structured reference of the parameter 
setting, the default state, and the recommended fine-tuning guidelines to help deliver the best 
quality of connectivity experience in the same order as displayed through configuration screen 
options in OmniVista 2500 4.6R1 and OmniVista Cirrus 4.6.1 versions.
Conclusion

<<<PAGE 66>>>
Tech Brief
Fine-Tuning Best Practices
22
Settings
Default
Guidelines Reasons to Enable/Disable
Band Steering
Disabled 
“OFF”
For newer Wi-Fi device deployment, this attribute is 
recommended to be enabled.
Force 5GHz
Disabled
This functionality is recommended stay disabled for 
environments where the client population has a mixture 
of 2.4GHz and 5GHz clients. When enabled it will reject all 
association requests from 2.4Ghz clients.
Exclude MAC OUI
Disabled
When enabled, the MACs OUI entered in the list and when 
matched, those MACs will be excluded from the Band Steering 
algorithm.
Association RSSI 
Threshold
Disabled “0”
Recommended to be enabled for both bands and set a 
minimum RSSI threshold of 22 which translates to -74 dBm 
(using -96 dBm as base noise floor).
Roaming RSSI 
Threshold
Disabled “0”
Recommended to be enabled for both bands and set the RSSI 
threshold of 25 which translates to -71 dBm (using -96 dBm 
as base noise floor), when signal strength drops to -71 dBm 
roaming is triggered.
Dynamic Load 
Balance
Disabled 
“OFF”
Recommended to be enabled.
Airtime Fairness
Disabled 
“Both 
Bands”
Recommended to be enabled, the newer devices will take 
advantage of these advanced features through the support of 
the new standards in a fair manner since they will have equal 
airtime while using faster processors, new Wi-Fi standards, 
etc.
Background
Scan-ning
Enabled 
“ON”
Recommended to stay enabled: Background scanning is used 
to examine the radio frequency environment in which the 
wireless network is operating, discover neighbor APs, and 
identify inter-ference and attacks. Background scanning is the 
basis of some advanced features such as: WIPS, Radio 
Dynamic Adjustment (ACS/APC) etc.
Scanning Channel
“Working 
Channel”
This setting is modifiable to be for “Working channel” or both 
“Working channel and Non-working Channel” options; 
recommended to leave as default.
Scanning Interval
“20” sec
Recommended to leave as default.
Scanning Duration
Enabled 
“50” ms
Recommended to leave as default.
Voice and Video 
Awareness
Enabled 
“ON”
Recommended to leave as default. Background scanning 
must be aware of existing traffic on APs. If there is an ongoing 
voice/video service, scanning should not be performed to 
ensure uninterrupted traffic; and scanning should resume 
there is no active voice/video session.
Appendix A
Stellar WLAN Fine-Tuning Under the RF Profile Configuration 
Workflow
Per Band Info

<<<PAGE 67>>>
Tech Brief
Fine-Tuning Best Practices
23
Settings
Default
Guidelines Reasons to Enable/Disable
Default Setting
Disabled 
“OFF”
Disable to set custom bandwidth settings. Enable to reset 
bandwidth settings to default values. Recommended to stay 
disabled “OFF” for the APs to be configured with minimum 
and maximum TX power since there will be a mixture of AP 
models with different radio capacities.
Band
Enabled
“All bands are 
checked”
Recommended for all bands to stay checked. Regarding the 
“5G High” and “5G Low” options, they are exclusively used to 
set the 5.8G and 5.2G radios on Stellar AP-1230 series. The 
“5G All” is used to set the full band 5G radio on the other AP 
series. When “Default Setting is “ON” all Bands are enabled.
Channel Setting
Enabled
“Auto” for all 
bands
Recommended to stay on default “Auto”. When “Default 
Setting is “ON” all Bands are on “Auto” and they cannot be 
changed.
Client-aware
Enabled
“ON” for all 
bands
Recommended to stay on default “ON”. When “Default Setting 
is “ON” all Bands are on “ON” and they cannot be changed.
Channel DRM
Disabled
“OFF”
Only supported for 5G bands. Recommended to stay “OFF” 
to allow the Radio Dynamic Adjustment technology to 
automatically set the ACS based on its algorithm.
Channel List
Disabled
Only supported when “Channel DRM” for 5G bands is enabled.
Channel Width
Enabled
“Auto”
Recommended to stay on “Auto” for most or 20MHz for most 
WLAN applications.
Power Setting
Enabled
“Auto”
Recommended for this setting to stay on Auto, but the 
‘Minimum TX’ and “Maximum TX’ power parameters below 
need to be adjusted. 
Note: The maximum transmitting power varies from different 
models on each band. If manually configured, and when the 
setting value exceeds the capability of the model, the AP will 
work with a maximum transmitting power rather than the 
setting value.
Stellar WLAN Fine-Tuning Under the RF Profile Configuration 
Workflow
Per Band Info

<<<PAGE 68>>>
Tech Brief
Fine-Tuning Best Practices
24
Stellar WLAN Fine-Tuning Under the RF Profile Configuration 
Workflow
Per Band Info
Settings
Default
Guidelines Reasons to Enable/Disable
Maximum TX 
Power (dBm)
Disabled
“configurable 
range from 
3-40 dBm”
For most applications, this parameter is recommended to be 
set at maximum Tx power at “15” dBm for 2.4GHz and “18” dBm 
for 5GHz bands. 
Note: For this parameter be configurable, the “De-
fault Setting” button at the top of the configuration screen 
needs to stay “OFF”.
External 
Antennas Gain 
(dBi)
Enabled
“configurable 
range from 
1-16 dBm”
Only applicable to APs supporting external antennas. 
It is recommended that these types of APs be divided into seve-
ral AP Groups when using different types of
external antenna (e.g., Group A with an antenna gain value of 
3-dBi, and Group B with an antenna gain value of 6-dBi).
Beacon 
Interval (ms)
Enabled
“100” ms
This indicates how often the 802.11 beacon management 
frames are transmitted by the AP, the configurable range is 
from 60-500 milli seconds (ms). It is recommended to keep at 
the default of 100 ms.
Short Guard 
Interval
Enabled
“ON”
Recommended to remain enabled.
MU-MIMO
Enabled
“ON”
Recommended to remain enabled.
High Efficiency
Enabled
“ON”
Recommended to remain enabled for High-Efficiency (HE) 
802.11ax APs; when disabled, HE 802.11ax capable APs will 
downgrade to VHT (Very High Throughput) mode.

<<<PAGE 69>>>
Tech Brief
Fine-Tuning Best Practices
25
AP Group
The IGMP Snooping parameter is recommended to be enabled to work with the Multicast 
Optimization parameter as configured in the SSIDs Configuration section. To enable IGMP 
Snooping, open the AP Group configuration screen, scroll down to the bottom of the screen 
to enable this parameter.
Enabling IGMP Snooping
Settings
Default
Guidelines Reasons to Enable/Disable
IGMP Snooping
Disabled
“OFF”
Recommended to be Enabled when the Multicast Opti-
mization parameter is enabled in the SSIDs Configura-
tion section.
Appendix B

<<<PAGE 70>>>
Tech Brief
Fine-Tuning Best Practices
26
SSID Configuration Workflow and Expert Mode options
Advanced WLAN Service Configuration
To minimize radio interference in these today’s high-performing Wi-Fi Access Point 
deployments, minimal AP settings (mostly handled via the OV-2500 NMS Stellar RF 
management on a per AP group basis).  However, the initial deployment needs to be 
configured and adjusted as per the physical site survey recommendations and based on the 
applications, performance requirements, and types of devices connecting to this wireless 
network.
Appendix C
Settings
Default
Guidelines Reasons to Enable/Disable
SSID Setting
Hide SSID
Disabled
UAPSD
Enabled
When enabled, the MACs OUI entered in the list and when 
matched, those MACs will be excluded from the Band Steering 
algorithm.
Security
Classification Status
Disabled
When enabled, traffic will be classified to a role based on the 
configured classification rules. Note that the precedence of 
role assignment methods is important. Classification Rules 
are only used if 802.1x/MAC authentication does not return a 
role, or the returned role is not matched with any configured 
roles in the device.
Client Isolation
Disabled
Recommended to be Enabled, this adds another layer of 
security. 
Protected
Management Frame
Optional
Configures whether connections are accepted from clients 
supporting Protected Management Frame for certain Security 
Levels/Encryption Types (Enterprise - WPA2_AES/WPA3_
AES256/ WPA3AES).
Roaming Controls
L3 Roaming
Disabled
Recommended to be Enabled. This will help keeping the FDB 
updated.
FDB Update on Asso-
ciation
Disabled
Recommended to be enabled. Allows the switch to update 
the downstream forwarding port based on the new generated 
ARP. This option will help to keep the switches’ forwarding 
table updated.
802.11r
Disabled
Recommended to be enabled to assist with device roaming 
decisions when this standard is supported end-to-end.
OKC
Disabled
Recommended to be enabled to allow for faster roaming for 
Windows clients without a complete 802.1x re-authentication.
802.11k Status
Disabled
Recommended to be enabled, helps to resolve the Sticky-
Client issue. Works with these standards’ compliant clients to 
help deliver excellent QoE scores.

<<<PAGE 71>>>
Tech Brief
Fine-Tuning Best Practices
27
802.11v Status
Disabled
Recommended to be enabled to help eliminate the Sticky-
Client issue through the support of Fast BSS.
Protected 
Management Frame
Optional
Configures whether connections are accepted from clients 
supporting Protected Management Frame for certain Security 
Levels/Encryption Types (Enterprise - WPA2_AES/WPA3_
AES256/ WPA3AES).
Client Controls
Max Number of 
Clients Per Band
“64”
802.11b Support
Enabled
Can only stay enabled when the 802.11a/g setting is enabled. 
Recommended to be disabled by default.
802.11a/g Support
Enabled
Minimum Client Data Rate Controls
2.4GHz Minimum 
Client Data Rate 
Controller
Disabled
Recommended to be enabled.
2.4GHz Minimum 
Client Data Rate
Disabled
Recommended to be enabled, setting the value at 12 Mbps.
5GHz Minimum 
Client Data Rate 
Controller
Disabled
Recommended to be enabled.
5GHz Minimum 
Client Data Rate
Disabled
Recommended to be enabled, setting the value at 24 Mbps.
Minimum MGMT Rate Controls
2.4GHz Minimum 
MGMT Rate Control-
ler
Disabled
Recommended to be enabled.
2.4GHz Minimum 
MGMT Rate
Disabled
Recommended to be enabled, setting the value at 12 Mbps, 
working with the IEEE 802.11k and .11v supplemental 
standards.
5GHz Minimum 
MGMT Rate 
Controller
Disabled
Recommended to be enabled.
5GHz Minimum 
MGMT Rate
Disabled
Recommended to be enabled, setting the value at 24 Mbps, 
working with the IEEE 802.11k and .11v supplemental 
standards for time-sensitive applications over WLAN.
Power Save Controls
DTIM Interval
Default is “1” The Delivery Traffic Indication Message (DTIM) period in 
beacons. Note: Recommended for Apple interoperability to be 
set at a value of 3.

<<<PAGE 72>>>
SSID Configuration Workflow and Expert Mode options
QoS Setting
Settings
Default
Guidelines Reasons to Enable/Disable
Bandwidth Contract
Upstream Bandwidth
Disabled
Configurable in ‘Kbits/s’ from 0-2621440 (Based on application 
parameters)
Downstream 
Bandwidth
Disabled
Configurable in ‘Kbits/s’ from 0-2621440 (Based on application 
parameters)
Upstream Burst
Disabled
Configurable in ‘Kbits/s’ from 0-2621440 (Based on application 
parameters)
Downstream Burst
Disabled
Configurable in ‘Kbits/s’ from 0-2621440 (Based on application 
parameters)
Broadcast/Multicast Optimization
Broadcast Key 
Rotation
Disabled
For security purposes and for broadcast handling optimiza-
tion, this attribute recommended to be enabled.
Broadcast Filter All
Disabled
Recommended to be enabled to help alleviate issues with cer-
tain devices that have issues with dynamic frequency selected 
channels. Apple and Google design documents recommend 
5GHz only SSIDS to support these devices.
Broadcast Filter ARP
Disabled
Recommended to be enabled. Refer to the “Broadcast Filter 
ARP” section in this document for additional details.
Multicast 
Optimization
Enabled
Recommended to keep enabled.
Multicast Based 
Channel Utilization
“90”
Configures based channel utilization optimization percentage. 
(Range = 0 - 100, Default = 90)
Number of Clients
“6”
Configure the threshold for multicast optimization. This is the 
maximum number of high throughputs.
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view
other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trademarks-copyright.
All other trademarks are the property of their respective owners. The information presented is subject to change without
notice. Neither ALE Holding nor any of its affiliates assumes any responsibility for inaccuracies contained herein.
© 2021 ALE International. All rights reserved.  DID22022301  (March 2022)


<<<DOC 3: omniaccess-stellar-wlan-specific-deployment-assistance-datasheet-en.pdf | 起始页 73 | 3p>>>

<<<PAGE 73>>>
Datasheet 
Alcatel-Lucent OmniAccess Stellar WLAN Specific Deployment Assistance
Alcatel-Lucent OmniAccess  
Stellar WLAN Specific  
Deployment Assistance 
Benefit from vendor integration expertise
The Alcatel-Lucent 
OmniAccess®  Stellar WLAN 
is a best-in-class Wi-Fi, 
future-proof solution, with 
a superior user experience, 
including IoT onboarding, 
and innovative services 
enablement to provide 
new revenue streams. It 
also offers operational 
simplicity, with flexible 
deployment models 
that adapt to customers’ 
financial  requirements, and 
it  optimises existing IT resources.
Alcatel-Lucent OmniAccess Stellar WLAN Specific Deployment Assistance lets Business Partners 
feel confident implementing their first project with Voice over Wi-Fi, or Video on Demand, in special 
locations such as warehouses or industrial sites, or outdoor configurations such as sports venues 
or leisure parks.
Partners benefit from Alcatel-Lucent Enterprise Professional Services experience and expertise  
to acquire the skills they need to succeed, including project preparation, coaching, and  
deployment assistance.
Customers benefit from a complete turn-key solution, as well as vendor engagement to ensure the 
highest performance and optimisation, including deployment assistance.

<<<PAGE 74>>>
2
Datasheet
Alcatel-Lucent OmniAccess Stellar WLAN Specific Deployment Assistance
Business Partner benefits
Securing a deal
•	 Vendor expertise, by your side, to secure 
deployment projects while improving 
implementation speed and reducing risks
•	 Complete “on-shelf” assistance at a 
predictable price
•	 ALE assistance to create Technical 
Support services requests and ensure 
quick resolution 
Resources empowerment
•	 Increase your experts’ skills to enable 
autonomy
•	 Obtain official ALE expert certification 
and grant Technical Support access for 
the solution
Methodology and experience 
sharing
•	 Ensure successful deployment through 
preparation, coaching, and assistance, 
provided by an ALE expert
Customer benefits 
Performance
•	 Get the highest solution performance 
with ALE Professional Services’ 
methodology, expertise, and experience
Optimisation  
•	 Optimise the solution to adapt to your 
environment, configuration, and best 
practices, to maximise your ROI and 
increase adoption by end-users
Complete turnkey solution
•	 Get a complete turn-key solution with 
ALE assistance services included, to 
simplify and optimise deployment
Key features 
Project preparation
•	 Project discovery kick-off meeting to 
define methodology and action plan, 
identify prerequisites and necessary 
data, and help collect information
•	 Project analysis focussing on data 
collection and first recommendations 
presentation
•	 Wi-Fi predictive survey to define the 
access points map and high-level 
implementation plan
•	 Staging assistance before deployment (if 
necessary)
Coaching, deployment 
assistance, Wi-Fi survey on-site
•	 Coaching to identify relevant 
documentation, explain configuration 
procedures and theoretical topics
•	 Remote assistance during access 
points deployment and configuration: 
Explanation of the methodology, the 
use of the configuration interfaces, as 
well as best practices and experience 
sharing
•	 Wi-Fi Survey on-site performed by the 
ALE Expert using ALE Wi-Fi Survey tools 
(software and hardware)
• 	Proactive troubleshooting to provide a 
first-level resolution and help Partner 
experts execute a Technical Support 
service request, when necessary, allowing 
quick issue resolution and bug fix
Training and certification
•	 The Post Sales online course, 
DT00WTE278 - OmniAccess Stellar 
WLAN Advanced Troubleshooting, 
is part of the service. This course 
enables participants to ensure advanced 
troubleshooting of the OmniAccess 
Stellar WLAN Enterprise solution, as well 
as describe and implement the latest 
software features. It is available to two 
Business Partner expert(s) allocated to 
the project. Experts can then practice 
the acquired knowledge during the 
project deployment.
•	 Once deployment is complete two 
slot are provided for the expert(s) 
certification. The ACSE Stellar WLAN 
Enterprise online certification validates 
the expert(s) skills and knowledge 
acquired during the project and 
provides them access to Technical 
Support for this solution.
Figure 1. Prediction of the access points placement on the floor plan
 
•	 Predictive analysis made on plan with the information provided by the data collection
•	 Preparation before the predictive survey using dedicated tools (for example, Ekahau Pro®)
High priority area
Medium priority area
Obstacles
Predictive Access Points placement

<<<PAGE 75>>>
© 2024 ALE International, ALE USA Inc. All rights reserved in all countries. The Alcatel-Lucent name and logo are trademarks 
of Nokia used under license by ALE. To view a list of proprietary ALE trademarks, visit: www.al-enterprise.com/en/legal/
trademarks-copyright. DID22010601ES (July 2024)
Figure 2. Access points placement: RF interferences (Ekahau Pro and Android Wi-Fi Analyser)
 
•	 Co-channel interference (left): Loss of throughput > Change AP channel
•	 Adjacent channel interference (right): Packets loss and corrupted data > Change AP channel
Key features
Benefits
Integrated online Post-Sales 
Training
Provides experts with the right knowledge before starting the project
Project discovery
Prerequisites, methodology, action plan defined, assistance with data collection
Data analysis
First recommendations provided based on data collection
Wi-Fi predictive survey
Estimation of the coverage area and prepositioning of the access points on map
Off-site staging assistance
If necessary, ALE assistance with tests definition for testing certain features in a laboratory prior  
to deployment
Coaching
Experts trained on the job by ALE expert. Best practices and reference documents sharing
Wi-Fi Survey on-site
Validate and optimise the access points placement. Done by the ALE expert using ALE Wi-Fi Survey tools
Deployment assistance
Help with methodology, expertise, and experience sharing during the deployment phase
Integrated online Post-Sales 
Certification
Experts are certified on the solution at the end of the process, enabling access to Technical Support for 
the solution
Key options
•	 The Wi-Fi Survey included in the 
service is limited to a certain surface 
coverage and number of access points 
to deploy (for example: 10 APs/day for 
a project of approximately 20 Aps, and 
a surface of 6000 m2). If the project is 
larger additional ALE assistance can be 
requested using a quote request, or by 
using additional PAER days left on the 
account, if any.
•	 The service is delivered partly remotely. 
For full on-site assistance, please 
request a quote
Technical specifications 
Prerequisites
•	 Your expert(s) assigned to the project 
must be ACFE certified, at a minimum, on 
the OmniAccess Stellar WLAN Enterprise 
latest release(s), as a basic prerequisite 
prior to the project start-ups
•	 The partner expert should have 
deployed an OmniAccess Stellar WLAN 
at least once in Office configuration
•	 The solution High-Level Design (HLD) 
must be done prior to subscribing to 
this service
Services and support  
•	 This service is based on delivery over a 
five-day period
•	 Worldwide availability 
Pricing and Ordering  
•	 This service must be ordered using 
eBuy part number PS-PAER-5-NET
•	 Alcatel-Lucent Enterprise Professional 
Services can provide an additional quote 
for service options
Contact us
For more information about this solution, please initiate a request on the ALE ALE MyPortal website: 
 Welcome Page >QUICK ACCESS  >Professional Services Offer request.
