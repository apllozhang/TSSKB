<<<DOC 1: AlcatelLucentOmniAccesss-Stellar-WLAN_Golden-RFP_en.docx|1|1>>>

﻿
Alcatel-Lucent OmniAccess® Stellar® WLAN GOLDEN RFP
August 2026
Release Version
Date
Comments
4.0.1
November 2020
Release sync with
AWOS4.0.1.44, OVE 4.5R2, and OVC 4.5.2
4.0.3
January 2022
Release sync with
AWOS 4.0.3.2054, OVE 4.6R2, and OVC 4.6R2
“large deployment” or “cloud deployment” for any deployment (single or multi-site)
with Centralized Management.
4.0.5
November 2022
Release sync with
AWOS 4.0.5.23, OVE 4.7R1, and OVC 4.7R1
AP1451 WiFi 6E access point
4.0.7
November 2023
Release sync with
AWOS 4.0.7.1019, OVC 10.4.1, OVE/OVC 4.8R1
AP1411 WiFi 6E access point
AP1431 WiFi 6E access point
5.0.1
November 2024
Release sync with
AWOS 5.0.1.27, OVC 10.4.3, OVE/OVC 4.9R2
AP1511 WiFi 7 access point
AP1521 WiFi 7 access point
6.0.1
April 2026
Release sync with
AWOS 5.0.4, OVCX 10.5.2, OVE 4.9R3
AP1501       WiFi 7 Access Point
AP1541/42 WiFi 7 Access Points
AP1561       WiFi 7 Access Point
AP1571/72 WiFi 7 Access Points
6.0.2
August 2026
Release sync with
AWOS 5.0.5, OVCX/OVTX 10.6.1, OVE 4.9R3
Contents
TOC \o "1-3" \h \z \u Contents PAGEREF _Toc237446020 \h 3
1Introduction PAGEREF _Toc237446021 \h 4
1.1Glossary PAGEREF _Toc237446022 \h 4
2Management PAGEREF _Toc237446023 \h 6
2.1Self-Management PAGEREF _Toc237446024 \h 6
2.2Centralized Management PAGEREF _Toc237446025 \h 6
2.3Other Manageability Options PAGEREF _Toc237446026 \h 7
3Common Features PAGEREF _Toc237446027 \h 8
3.1Regulatory and industry standards PAGEREF _Toc237446028 \h 8
3.2WLAN solution requirements PAGEREF _Toc237446029 \h 9
3.3Additional Capabilities PAGEREF _Toc237446030 \h 9
4Access Point Specific Requirements PAGEREF _Toc237446031 \h 10
4.1Type A - Entry level, outdoor dual-band WiFi 5 Access Point PAGEREF _Toc237446032 \h 11
4.2Type B - Entry level, indoor dual-band WiFi 6 Access Point PAGEREF _Toc237446033 \h 11
4.3Type C - Entry level, indoor hospitality dual-band WiFi 6 Access Point with integrated RJ45 access ports PAGEREF _Toc237446034 \h 12
4.4Type D - Entry level, premium indoor dual-band WiFi 6 Access Point PAGEREF _Toc237446035 \h 12
4.5Type E1 - Mid-range, indoor dual-band WiFi 6 Access Point PAGEREF _Toc237446036 \h 13
4.6Type E2 - Mid-range, indoor dual-band WiFi 6 Access Point with external antennas PAGEREF _Toc237446037 \h 14
4.7Type F - Mid-range, premium, indoor dual-band WiFi 6 Access Point PAGEREF _Toc237446038 \h 14
4.8Type G - High-end, premium, indoor dual-band WiFi 6 Access Point PAGEREF _Toc237446039 \h 15
4.9Type H1 - Mid-range, outdoor harsh environment dual-band WiFi 6 Access Point PAGEREF _Toc237446040 \h 16
4.10Type H2 - Mid-range, outdoor harsh environment dual-band WiFi 6 AP, integrated directional antenna PAGEREF _Toc237446041 \h 16
4.11Type H3 - Mid-range, outdoor harsh environment dual-band WiFi 6 Access Point with connectors for external antennas PAGEREF _Toc237446042 \h 17
4.12Type I - Entry range premium, indoor tri-band WiFi 6E Access Point PAGEREF _Toc237446043 \h 18
4.13Type J - Mid-range premium, indoor tri-band WiFi 6E Access Point PAGEREF _Toc237446044 \h 19
4.14Type K - High-end, indoor tri-band WiFi 6E Access Point PAGEREF _Toc237446045 \h 19
4.15Type L - Entry level, indoor tri-band WiFi 7 Access Point PAGEREF _Toc237446046 \h 20
4.16Type M - Entry level, premium, indoor tri-band WiFi 7 Access Point PAGEREF _Toc237446047 \h 21
4.17Type N - Mid-range, indoor tri-band WiFi 7 Access Point PAGEREF _Toc237446048 \h 22
4.18Type O1 - High-end, indoor tri-band WiFi 7 Access Point PAGEREF _Toc237446049 \h 23
4.19Type O2 - High-end, indoor tri-band WiFi 7 Access Point with external antennas PAGEREF _Toc237446050 \h 24
4.20Type P - Entry level, premium outdoor harsh environment tri-band WiFi 7 Access Point PAGEREF _Toc237446051 \h 25
4.21Type Q1 - Mid-range, outdoor harsh environment tri-band WiFi 7 Access Point PAGEREF _Toc237446052 \h 26
4.22Type Q2 - Mid-range, outdoor harsh environment tri-band WiFi 7 Access Point with external antennas PAGEREF _Toc237446053 \h 27
Introduction
Alcatel-Lucent Stellar® family of WLAN Access Points offers an extensive array of options in terms of performance, utility features, manageability, scalability and price.
All Access Points are certified by the WiFi Alliance to ensure compatibility and interoperability and compliance with industry standards.
Stellar® APs are capable of independent self-management with a built-in control function while maintaining full WLAN functionality and security.
Stellar®-based WLAN can also be managed by Alcatel-Lucent Enterprise OmniVista network management system. OmniVista server offers unified access management of wired and wireless networks. The servers can be hosted on-premises or in the cloud.
This edition is based on OmniVista Cirrus version 10.6.1, OmniVista Terra version 10.6.1, OmniVista 2500 NMS version 4.9.3 and Stellar AWOS version 5.0.5.
Glossary
ACS
Automatic Channel Selection, ability to dynamically select a channel with lower interference from neighboring radios
AFC
Automated Frequency Coordination, required to operate standard power 6-GHz Access Points. Current regulatory adoption includes FCC (USA) and ISED (Canada).
APC
Automatic Power Control, radio transmit power is adjusted based on scanning for RSSI in the area
CB
Certification Body scheme, IEC certification system of electrical &amp; electronics manufacturing
CE
Conformité Européenne, indicates conformance with European product safety standards
CSA
Channel Switch Announcement, 802.11h, AP notification to clients before changing channel
FCC
Federal Communications Commission, a US agency that regulates wired and wireless communication including radio frequencies
IEC
International Electrotechnical Commission sets industry standards for electrical enclosures
IEEE
Institute of Electrical and Electronics Engineers, sets performance standards for electrical devices
IP67
Ingress Protection (67), IEC standard for moisture and dust resistance
NRTL
Nationally Recognized Testing Laboratory, an accredited product safety testing firm whose results are recognized in US and Canada
REACH
Registration, Evaluation, Authorization, and Restriction of Chemicals, EU chemical use regulation
RoHS
Restriction of Hazardous Substances, standard for restricting industrial use of harmful substances
WEEE
Waste Electrical and Electronic Equipment, European regulatory body that sets requirements for the collection, recycling, and recovery of electrical and electronic waste
WFA
WiFi Alliance, non-profit industry organization that certifies Wi-Fi products
wIDS/wIPS
Wireless Intrusion Detection System/wireless Intrusion Prevention System
Management
Applicable to all APs
Self-Management
Self-managed APs can form independent AP groups or clusters without reliance on any external servers or applications. The management application and services reside within the operating system of the AP.
Each Access Point must have the following manageability capabilities:
2.1.1
An AP must be able to serve as an AP group (cluster) manager. Any AP can provide that functionality.
C/PC/NC
2.1.2
Independent cluster management should not require any additional licenses.
C/PC/NC
2.1.3
Must be able to discover neighboring APs and form or join an independent AP group/cluster.
C/PC/NC
2.1.4
The independent AP group must be able to automatically elect an AP that will act as a cluster manager.
C/PC/NC
2.1.5
The AP group must be able to elect a secondary manager to provide redundancy.
C/PC/NC
2.1.6
The cluster must support deterministic election of cluster manager with preference given to higher-capability Access Points.
C/PC/NC
2.1.7
When a higher-end AP joins the cluster, it must be able to preempt a lower end AP, assume the manager role, and demote the lower end AP to secondary/backup role.
C/PC/NC
2.1.8
The Virtual Manager must be manageable by a web interface.
C/PC/NC
2.1.9
Management of the independent AP group must include the essential functionality of a WLAN
C/PC/NC
2.1.10
Manage RF parameters
C/PC/NC
2.1.11
Configure WLANs (SSID) for standard users, guests and BYOD
C/PC/NC
2.1.12
Configure WLAN performance standards (802.11r, 802.11k, 802.11v, OKC), efficiency features (A-MPDU, A-MSDU) and QoS (WMM, 802.11e)
C/PC/NC
2.1.13
Configure internal or external Captive Portal
C/PC/NC
2.1.14
Manage software upgrades
C/PC/NC
2.1.15
Manage configuration backups and restoration
C/PC/NC
2.1.16
Collect and display incident and activity logs
C/PC/NC
Centralized Management
2.2.1
Manageability by an NMS application running on a server that is hosted locally or in the cloud.
C/PC/NC
2.2.2
Scalability. On premises deployments can scale up to large multi-site environments with multiple VRFs, VLANs and RF environments. Cloud deployments can scale further to global enterprises spanning multiple countries and comply with varied RF regulatory constraints.
C/PC/NC
2.2.3
AP must be capable of easy migration from independent management mode to a larger centralized management mode, either cloud-based or on-premises type.
C/PC/NC
2.2.4
On-premises deployment should scale up to 4000 APs
C/PC/NC
2.2.5
Cloud-based deployment should scale up to at least 10K APs
C/PC/NC
2.2.6
The WLAN solution shall support a distributed data forwarding architecture where client traffic is locally bridged without reliance on a centralized controller for data forwarding.
C/PC/NC
2.2.7
Operational resilience. The APs will continue forwarding traffic even when the management server is down or unreachable.
C/PC/NC
2.2.8
The centralized management system should be capable of “unified management” of both wireless and wired devices.
C/PC/NC
Other Manageability Options
2.3.1
In addition to a centralized management function, all Access Points of the wireless LAN solution shall support a dedicated web interface to monitor and configure a single AP.
C/PC/NC
2.3.2
Access Points shall be capable of providing SSH access to facilitate monitoring and configuration of a single AP.
C/PC/NC
2.3.3
APs must be able to operate as a Remote Access Point (RAP)
C/PC/NC
2.3.4
RAPs must be able to form secure encrypted tunnels with a VPN server. The tunnels can serve as site-to-site VPN connecting remote offices to HQ.
C/PC/NC
2.3.5
RAPs must support split tunneling, routing selected traffic through the VPN tunnels
C/PC/NC
2.3.6
The WLAN solution shall support the secure tunneling of guest traffic to a gateway (GRE tunnel server) to isolate guest traffic from the local network.
C/PC/NC
2.3.7
APs must be recoverable to factory default state, either by management interface or by physical reset button (if access credentials are lost)
C/PC/NC
2.3.8
Bridge mode. The WLAN solution must support connecting two distant sites over a wireless point-to-point link.
C/PC/NC
2.3.9
Mesh network. The WLAN solution must allow connection of multiple distant sites over wireless.
C/PC/NC
2.3.10
The WLAN solution shall support IPv6 for wireless clients.
C/PC/NC
2.3.11
The WLAN solution shall support wIDS/wIPS with no additional equipment or licenses
C/PC/NC
2.3.12
wIDS/wIPS must be able to detect and classify interfering APs
C/PC/NC
2.3.13
wIDS/wIPS must be able to detect, classify, and contain rogue APs
C/PC/NC
2.3.14
wIDS/wIPS must support adding trusted APs classified by MAC address or MAC address prefix into an “allow list”
C/PC/NC
2.3.15
wIDS/wIPS must support adding untrusted APs classified by MAC address or MAC address prefix into a “block list”
C/PC/NC
2.3.16
Channel width can be set manually or optionally selected automatically
C/PC/NC
2.3.17
Short Guard Interval can be enabled or disabled per band
C/PC/NC
2.3.18
AP must collect and provide QoE statistics to the management system
C/PC/NC
Common Features
Applicable to all APs. The requirements in this section define the minimum capabilities supported by all Access Point models. Additional capabilities for specific models are defined in Section 4.
Regulatory and industry standards
3.1.1
CE marked, RoHS, REACH, WEEE compliant
C/PC/NC
3.1.2
IEC CB Scheme safety certified
C/PC/NC
3.1.3
North American safety certified by an NTRL (e.g. cTÜVus)
C/PC/NC
3.1.4
Backwards compatible with 802.11a/b/g/n
C/PC/NC
3.1.5
Each radio can be turned ON/OFF independently
C/PC/NC
3.1.6
Support for 20 MHz, 40 MHz and 80 MHz channels
C/PC/NC
3.1.7
Allows manual channel width configuration on all bands
C/PC/NC
3.1.8
Automatic Channel Selection (ACS) on all bands
C/PC/NC
3.1.9
ACS can be “client aware” to avoid unnecessary channel changes when clients are connected
C/PC/NC
3.1.10
Channel Switch Announcements (CSA) can be enabled or disabled
C/PC/NC
3.1.11
CSA count must be configurable
C/PC/NC
3.1.12
Radio power can be set manually on either 2.4 GHz or 5 GHz
C/PC/NC
3.1.13
Automatic Power Control (APC) can be set on either 2.4 GHz or 5 GHz
C/PC/NC
3.1.14
Power range (min – max) can be set when APC is selected
C/PC/NC
3.1.15
MU-MIMO can be turned ON/OFF per band
C/PC/NC
3.1.16
Beacon interval must be configurable
C/PC/NC
3.1.17
AP can be configured to provide part-time or dedicated air monitoring for spectrum analysis and wireless intrusion
C/PC/NC
3.1.18
Scanning can be enabled on working or non-working channels
C/PC/NC
3.1.19
Scanning interval must be configurable
C/PC/NC
3.1.20
Scanning duration must be configurable
C/PC/NC
3.1.21
The WLAN solution shall be aware of connected voice and video calls (SIP, H.323) and avoid background scanning to prevent interruptions. Activating this feature must be configurable per band.
C/PC/NC
3.1.22
The WLAN solution shall be able to guide a new client to 5 GHz band
C/PC/NC
3.1.23
The WLAN solution shall have the configuration option to force new clients to use 5 GHz, if they support 5 GHz
C/PC/NC
3.1.24
The WLAN solution can be set to balance the client load between APs
C/PC/NC
3.1.25
The WLAN solution can set an RSSI threshold and bar clients from connecting to APs when they do not meet the minimum RSSI value
C/PC/NC
3.1.26
RSSI threshold must be configurable per band
C/PC/NC
3.1.27
The WLAN solution can be set to force connected clients to roam when the RSSI falls below a configurable value
C/PC/NC
3.1.28
The WLAN solution must be able to monitor and fairly allocate bandwidth (airtime slices) between clients. The feature must be configurable per band.
C/PC/NC
WLAN solution requirements
3.2.1
The WLAN solution shall support a distributed control architecture, where control functions are embedded within the Access Points without reliance on a centralized controller.
C/PC/NC
3.2.2
The WLAN solution shall support selective tunneling of traffic based on user roles, SSID, or policies, allowing local breakout for enterprise traffic and centralized tunneling for specific traffic flows.
C/PC/NC
3.2.3
The WLAN solution shall support role-based access control, enabling differentiated network access and traffic handling policies for users, guests, and devices.
C/PC/NC
3.2.4
The WLAN solution shall provide application-level visibility, including identification and categorization of applications and traffic flows.
C/PC/NC
3.2.5
The WLAN solution shall support identification and classification of connected devices, including IoT devices, to enable policy enforcement and segmentation.
C/PC/NC
3.2.6
The WLAN solution shall support a simplified licensing model with a single license per Access Point, including all core WLAN features.
C/PC/NC
3.2.7
The WLAN solution shall support the full interoperability between Access Points when running different firmware versions within a major release or when running adjacent major releases.
C/PC/NC
Additional Capabilities
3.3.1
The WLAN solution shall support on-demand packet capture of wireless client traffic directly from Access Points and export of capture data for external analysis.
C/PC/NC
3.3.2
The WLAN solution shall provide application visibility and classification capabilities based on traffic analysis.
C/PC/NC
3.3.3
The WLAN solution shall support real-time policy enforcement based on application visibility, user roles, and device classification.
C/PC/NC
3.3.4
The Access Point shall provide client, application, and session-level statistics for monitoring and analysis.
C/PC/NC
3.3.5
The WLAN solution shall support device fingerprinting and classification of connected IoT devices.
C/PC/NC
3.3.6
The WLAN solution shall support device classification capabilities without requiring dedicated external appliance-based systems.
C/PC/NC
3.3.7
The WLAN solution shall support over-the-air traffic monitoring and analysis using either dedicated scanning radios or time-sliced radio operation.
C/PC/NC
3.3.8
The WLAN solution shall support enforcement actions including traffic prioritization, rate limiting, redirection, and blocking based on defined policies.
C/PC/NC
Access Point Specific Requirements
Type A *
AP1261
Entry level, outdoor harsh environment dual-band WiFi 5 Access Point
Type B *
AP1301
Entry level, indoor dual-band WiFi 6 Access Point
Type C
AP1301H
Entry level, indoor dual-band WiFi 6 Access Point with RJ45 access ports
Type D **
AP1311
Entry level, indoor dual-band WiFi 6 Access Point
Type E1
AP1321
Mid-range, indoor dual-band WiFi 6 Access Point
Type E2
AP1322
Mid-range, indoor dual-band WiFi 6 Access Point with external antennas
Type F
AP1331
Mid-range, premium, indoor dual-band WiFi 6 Access Point
Type G
AP1351
High-end, premium, indoor dual-band WiFi 6 Access Point
Type H1
AP1361
Mid-range, outdoor harsh environment dual-band WiFi 6 Access Point
Type H2
AP1361D
Mid-range, outdoor harsh environment dual-band WiFi 6 AP, directional antenna
Type H3
AP1362
Mid-range, outdoor harsh environment dual-band WiFi 6 Access Point with connectors for external antennas
Type I
AP1411
Entry range premium, indoor tri-band WiFi 6E Access Point
Type J
AP1431
Mid-range premium, indoor tri-band WiFi 6E Access Point
Type K
AP1451
High-end, indoor tri-band WiFi 6E Access Point
Type L
AP1501
Entry level, indoor tri-band WiFi 7 Access Point
Type M
AP1511
Entry level, premium, indoor tri-band WiFi 7 Access Point
Type N
AP1521
Mid-range, indoor tri-band WiFi 7 Access Point
Type O1
AP1541
High-end, indoor tri-band WiFi 7 Access Point
Type O2
AP1542
High-end, indoor tri-band WiFi 7 Access Point with external antennas
Type P
AP1561
Entry level, premium outdoor harsh environment tri-band WiFi 7 Access Point
Type Q1
AP1571
Mid-range, outdoor harsh environment tri-band WiFi 7 Access Point
Type Q2
AP1572
Mid-range, outdoor harsh environment tri-band WiFi 7 AP with external antennas
* Not available in the USA, RW available, check availability in other regions.
** Planned phase-out in 2026, check availability
Type A - Entry level, outdoor dual-band WiFi 5 Access Point
4.1.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ac Wave 2 operation.
C/PC/NC
4.1.2
The Access Point shall be designed for outdoor deployments and comply with IP67 environmental rating.
C/PC/NC
4.1.3
The Access Point shall support an operating temperature range of at least -20°C to 55°C or wider.
C/PC/NC
4.1.4
The Access Point shall support a storage temperature range of at least -40°C to 85°C or wider.
C/PC/NC
4.1.5
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.1.6
The Access Point shall include integrated omni-directional antennas supporting:
• 2x2:2 MIMO in 2.4 GHz band
• 2x2:2 MU-MIMO in 5 GHz band
C/PC/NC
4.1.7
The Access Point shall support a maximum aggregate data rate of at least 1.2 Gbps.
C/PC/NC
4.1.8
The Access Point shall include at least one 10/100/1000Base-T Ethernet port supporting IEEE 802.3at Power over Ethernet (PoE).
C/PC/NC
4.1.9
The Access Point shall support a minimum of 8 SSIDs per radio.
C/PC/NC
4.1.10
The Access Point shall support a minimum of 384 concurrently associated client devices.
C/PC/NC
4.1.11
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.1.12
The Access Point shall support IEEE 802.11a/b/g/n/ac standards.
C/PC/NC
Type B - Entry level, indoor dual-band WiFi 6 Access Point
4.2.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.2.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.2.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.2.4
The Access Point shall support dual-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 2x2:2 MU-MIMO
C/PC/NC
4.2.5
The Access Point shall support a maximum aggregate data rate of at least 1.7 Gbps under ideal conditions.
C/PC/NC
4.2.6
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.2.7
The Access Point shall include at least two 10/100/1000Base-T Ethernet ports supporting IEEE 802.3af Power over Ethernet (PoE).
C/PC/NC
4.2.8
The Access Point shall include a USB interface for IoT or peripheral connectivity.
C/PC/NC
4.2.9
The Access Point shall support a minimum of 8 SSIDs per radio.
C/PC/NC
4.2.10
The Access Point shall support a minimum of 512 concurrently associated client devices.
C/PC/NC
4.2.11
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.2.12
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
Type C - Entry level, indoor hospitality dual-band WiFi 6 Access Point with integrated RJ45 access ports
4.3.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.3.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.3.3
The Access Point shall support single-gang wall plate mounting.
C/PC/NC
4.3.4
The Access Point shall support dual-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 2x2:2 MU-MIMO
C/PC/NC
4.3.5
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.3.6
The Access Point shall support a maximum aggregate data rate of at least 1.7 Gbps under ideal conditions.
C/PC/NC
4.3.7
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.3.8
The Access Point shall include at least one 10/100/1000Base-T uplink Ethernet port supporting IEEE 802.3at/af Power over Ethernet (PoE).
C/PC/NC
4.3.9
The Access Point shall include multiple downlink Ethernet ports to support wired device connectivity.
C/PC/NC
4.3.10
At least one downlink Ethernet port shall support Power over Ethernet (PoE) output (PSE) to power connected devices.
C/PC/NC
4.3.11
The Access Point shall support RJ45 pass-through ports for analog or legacy telephony integration.
C/PC/NC
4.3.12
The Access Point shall include a USB interface for IoT or peripheral connectivity.
C/PC/NC
4.3.13
The Access Point shall support a minimum of 16 SSIDs per radio.
C/PC/NC
4.3.14
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.3.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.3.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
Type D - Entry level, premium indoor dual-band WiFi 6 Access Point
4.4.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.4.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.4.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.4.4
The Access Point shall support dual-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 2x2:2 MU-MIMO
C/PC/NC
4.4.5
The Access Point shall support a maximum aggregate data rate of at least 1.7 Gbps under ideal conditions.
C/PC/NC
4.4.6
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.4.7
The Access Point shall include at least two 10/100/1000Base-T uplink Ethernet ports supporting IEEE 802.3af/at Power over Ethernet
C/PC/NC
4.4.8
The Access Point shall include at least one additional Ethernet port for local connectivity.
C/PC/NC
4.4.9
The Access Point shall include a USB interface for IoT or peripheral connectivity.
C/PC/NC
4.4.10
The Access Point shall include a dedicated radio for background scanning, spectrum analysis, and wireless intrusion detection.
C/PC/NC
4.4.11
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.4.12
The Access Point shall support a minimum of 8 SSIDs per radio.
C/PC/NC
4.4.13
The Access Point shall support a minimum of 512 concurrently associated client devices.
C/PC/NC
4.4.14
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.4.15
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
4.4.16
The Access Point shall support simultaneous operation of client-serving radios and a dedicated scanning radio without impacting client traffic.
C/PC/NC
Type E1 - Mid-range, indoor dual-band WiFi 6 Access Point
4.5.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.5.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.5.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.5.4
The Access Point shall support tri-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.5.5
The Access Point shall support a maximum aggregate data rate of at least 3 Gbps under ideal conditions.
C/PC/NC
4.5.6
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.5.7
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.5.8
The Access Point shall include at least one multi-gigabit Ethernet port (2.5 Gbps or higher) and one additional Gigabit Ethernet port.
C/PC/NC
4.5.9
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.5.10
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.5.11
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.5.12
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
Type E2 - Mid-range, indoor dual-band WiFi 6 Access Point with external antennas
4.6.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.6.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.6.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.6.4
The Access Point shall support tri-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.6.5
The Access Point shall support a maximum aggregate data rate of at least 3 Gbps under ideal conditions.
C/PC/NC
4.6.6
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.6.7
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.6.8
The Access Point shall include at least one multi-gigabit Ethernet port (2.5 Gbps or higher) and one additional Gigabit Ethernet port.
C/PC/NC
4.6.9
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.6.10
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.6.11
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.6.12
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
4.6.13
The Access Point shall support external antennas.
C/PC/NC
4.6.14
The Access Point shall include RP-SMA connectors for external antenna attachment.
C/PC/NC
4.6.15
The Access Point shall include a minimum of four RF connectors to support dual-band operation.
C/PC/NC
4.6.16
The Access Point shall support deployment scenarios requiring directional or specialized RF coverage.
C/PC/NC
Type F - Mid-range, premium, indoor dual-band WiFi 6 Access Point
4.7.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.7.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.7.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.7.4
The Access Point shall support tri-radio operation:
• 2.4 GHz band: 4x4:4 MIMO
• 5 GHz band: 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.7.5
The Access Point shall support a maximum aggregate data rate of at least 3.5 Gbps under ideal conditions.
C/PC/NC
4.7.6
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.7.7
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.7.8
The Access Point shall include at least two multi-gigabit Ethernet ports supporting 5 Gbps or higher speeds.
C/PC/NC
4.7.9
The Access Point shall support link redundancy and/or load sharing across multiple uplink ports.
C/PC/NC
4.7.10
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.7.11
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.7.12
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.7.13
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
4.7.14
The Access Point shall support dual multi-gigabit uplinks operating simultaneously without performance degradation.
C/PC/NC
Type G - High-end, premium, indoor dual-band WiFi 6 Access Point
4.8.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.8.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.8.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.8.4
The Access Point shall support multi-radio operation including at least:
• One 2.4 GHz radio supporting 4x4:4 MIMO
• Two independent 5 GHz radios supporting high-efficiency MU-MIMO operation
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.8.5
At least one 5 GHz radio shall support 8 spatial streams (8x8:8 MIMO).
C/PC/NC
4.8.6
The Access Point shall support independent channel operation across multiple 5 GHz radios to maximize spectrum utilization in high-density environments.
C/PC/NC
4.8.7
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.8.8
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.8.9
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.8.10
The Access Point shall include at least two multi-gigabit Ethernet ports supporting 10 Gbps speeds.
C/PC/NC
4.8.11
The Access Point shall support link redundancy and/or load sharing across multiple uplink ports.
C/PC/NC
4.8.12
The Access Point shall support a minimum of 24 SSIDs.
C/PC/NC
4.8.13
The Access Point shall support a minimum of 1536 concurrently associated client devices.
C/PC/NC
4.8.14
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.8.15
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
4.8.16
The Access Point shall support simultaneous operation of all client-serving radios without performance degradation.
C/PC/NC
4.8.17
The Access Point shall be optimized for high-density environments such as auditoriums, stadiums, and large enterprise deployments.
C/PC/NC
Type H1 - Mid-range, outdoor harsh environment dual-band WiFi 6 Access Point
4.9.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.9.2
The Access Point shall be designed for outdoor deployments and comply with IP67 or better environmental rating.
C/PC/NC
4.9.3
The Access Point shall include surge protection and be suitable for deployment in environments exposed to electrical and weather-related disturbances.
C/PC/NC
4.9.4
The Access Point shall support an operating temperature range suitable for outdoor environments.
C/PC/NC
4.9.5
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.9.6
The Access Point shall support tri-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.9.7
The Access Point shall support a maximum aggregate data rate of at least 3 Gbps under ideal conditions.
C/PC/NC
4.9.8
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.9.9
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.9.10
The Access Point shall include at least one multi-gigabit Ethernet uplink port.
C/PC/NC
4.9.11
The Access Point shall support fiber uplink connectivity via SFP or equivalent interface for long-distance backhaul.
C/PC/NC
4.9.12
The Access Point shall include at least one additional Ethernet port for wired device connectivity.
C/PC/NC
4.9.13
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.9.14
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.9.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.9.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
Type H2 - Mid-range, outdoor harsh environment dual-band WiFi 6 AP, integrated directional antenna
4.10.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.10.2
The Access Point shall be designed for outdoor deployments and comply with IP67 or better environmental rating.
C/PC/NC
4.10.3
The Access Point shall include surge protection and be suitable for deployment in environments exposed to electrical and weather-related disturbances.
C/PC/NC
4.10.4
The Access Point shall support an operating temperature range suitable for outdoor environments.
C/PC/NC
4.10.5
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.10.6
The Access Point shall support tri-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.10.7
The Access Point shall support a maximum aggregate data rate of at least 3 Gbps under ideal conditions.
C/PC/NC
4.10.8
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.10.9
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.10.10
The Access Point shall include at least one multi-gigabit Ethernet uplink port.
C/PC/NC
4.10.11
The Access Point shall support fiber uplink connectivity via SFP or equivalent interface for long-distance backhaul.
C/PC/NC
4.10.12
The Access Point shall include at least one additional Ethernet port for wired device connectivity.
C/PC/NC
4.10.13
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.10.14
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.10.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.10.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
4.10.17
The Access Point shall include integrated directional antennas.
C/PC/NC
4.10.18
The Access Point shall support focused RF coverage for targeted outdoor deployments.
C/PC/NC
4.10.19
The Access Point shall be suitable for use cases such as corridors, long-range coverage, or sectorized outdoor environments.
C/PC/NC
Type H3 - Mid-range, outdoor harsh environment dual-band WiFi 6 Access Point with connectors for external antennas
4.11.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6) operation.
C/PC/NC
4.11.2
The Access Point shall be designed for outdoor deployments and comply with IP67 or better environmental rating.
C/PC/NC
4.11.3
The Access Point shall include surge protection and be suitable for deployment in environments exposed to electrical and weather-related disturbances.
C/PC/NC
4.11.4
The Access Point shall support an operating temperature range suitable for outdoor environments.
C/PC/NC
4.11.5
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.11.6
The Access Point shall support tri-radio operation:
• 2.4 GHz band: 2x2:2 MIMO
• 5 GHz band: 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.11.7
The Access Point shall support a maximum aggregate data rate of at least 3 Gbps under ideal conditions.
C/PC/NC
4.11.8
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.11.9
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.11.10
The Access Point shall include at least one multi-gigabit Ethernet uplink port.
C/PC/NC
4.11.11
The Access Point shall support fiber uplink connectivity via SFP or equivalent interface for long-distance backhaul.
C/PC/NC
4.11.12
The Access Point shall include at least one additional Ethernet port for wired device connectivity.
C/PC/NC
4.11.13
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.11.14
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.11.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.11.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards.
C/PC/NC
4.11.17
The Access Point shall support external antennas.
C/PC/NC
4.11.18
The Access Point shall include N-type female connectors for antenna attachment.
C/PC/NC
4.11.19
The Access Point shall support deployment scenarios requiring customized RF coverage using external antennas.
C/PC/NC
4.11.20
The Access Point shall support a minimum of four antenna connectors.
C/PC/NC
Type I - Entry range premium, indoor tri-band WiFi 6E Access Point
4.12.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6E) operation.
C/PC/NC
4.12.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.12.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.12.4
The Access Point shall support dual-radio operation with tri-band capability, allowing operation in any two of the following bands:
• 2.4 GHz
• 5 GHz
• 6 GHz
C/PC/NC
4.12.5
The Access Point shall support 2x2:2 MIMO operation on all supported frequency bands.
C/PC/NC
4.12.6
The Access Point shall support a maximum aggregate data rate of at least 3.5 Gbps under ideal conditions.
C/PC/NC
4.12.7
The Access Point shall support 6 GHz operation including channel widths up to 160 MHz.
C/PC/NC
4.12.8
The Access Point shall support flexible radio assignment to optimize use of available spectrum, including prioritization of 6 GHz operation.
C/PC/NC
4.12.9
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.12.10
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.12.11
The Access Point shall include at least one multi-gigabit Ethernet port (2.5 Gbps or higher) and one additional Gigabit Ethernet port.
C/PC/NC
4.12.12
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.12.13
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.12.14
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.12.15
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards including 6 GHz operation.
C/PC/NC
Type J - Mid-range premium, indoor tri-band WiFi 6E Access Point
4.13.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6E) operation.
C/PC/NC
4.13.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.13.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.13.4
The Access Point shall support tri-radio operation with simultaneous operation of the following frequency bands:
• 2.4 GHz
• 5 GHz
• 6 GHz
C/PC/NC
4.13.5
The Access Point shall support 2x2:2 MIMO operation on all radios.
C/PC/NC
4.13.6
The Access Point shall support a maximum aggregate data rate of at least 4.0 Gbps under ideal conditions.
C/PC/NC
4.13.7
The Access Point shall support 6 GHz operation including channel widths up to 160 MHz.
C/PC/NC
4.13.8
The Access Point shall support simultaneous operation of all radios across 2.4 GHz, 5 GHz, and 6 GHz bands without performance degradation.
C/PC/NC
4.13.9
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.13.10
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.13.11
The Access Point shall include at least two multi-gigabit Ethernet ports (2.5 Gbps or higher).
C/PC/NC
4.13.12
The Access Point shall support link redundancy and/or load sharing across multiple uplink ports.
C/PC/NC
4.13.13
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.13.14
The Access Point shall support a minimum of 1024 concurrently associated client devices.
C/PC/NC
4.13.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.13.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards including 6 GHz operation.
C/PC/NC
Type K - High-end, indoor tri-band WiFi 6E Access Point
4.14.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11ax (Wi-Fi 6E) operation.
C/PC/NC
4.14.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.14.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.14.4
The Access Point shall support multi-radio operation including at least:
• One 2.4 GHz radio supporting 4x4:4 MIMO
• One 5 GHz radio supporting 8x8:8 MU-MIMO
• One 6 GHz radio supporting 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.14.5
The Access Point shall support simultaneous operation of all client-serving radios and the dedicated scanning radio.
C/PC/NC
4.14.6
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.14.7
The Access Point shall support 6 GHz operation including channel widths up to 160 MHz.
C/PC/NC
4.14.8
The Access Point shall support simultaneous operation of all radios across 2.4 GHz, 5 GHz, and 6 GHz bands without performance degradation.
C/PC/NC
4.14.9
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.14.10
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.14.11
The Access Point shall include at least two multi-gigabit Ethernet ports supporting 10 Gbps speeds.
C/PC/NC
4.14.12
The Access Point shall support link redundancy and/or load sharing across multiple uplink ports.
C/PC/NC
4.14.13
The Access Point shall support a minimum of 24 SSIDs.
C/PC/NC
4.14.14
The Access Point shall support a minimum of 1536 concurrently associated client devices.
C/PC/NC
4.14.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.14.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax standards including 6 GHz operation.
C/PC/NC
4.14.17
The Access Point shall be optimized for high-density environments such as auditoriums, stadiums, and large enterprise deployments.
C/PC/NC
Type L - Entry level, indoor tri-band WiFi 7 Access Point
4.15.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.15.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.15.3
The Access Point shall support tri-radio operation with simultaneous operation of:
• 2.4 GHz band
• 5 GHz band
• 6 GHz band
C/PC/NC
4.15.4
The Access Point shall support at least 2x2:2 MIMO operation on all frequency bands.
C/PC/NC
4.15.5
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.15.6
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.15.7
The Access Point shall support 4K-QAM modulation
C/PC/NC
4.15.8
The Access Point shall support flexible radio resource management across all three bands.
C/PC/NC
4.15.9
The Access Point shall support simultaneous operation of all radios without performance degradation.
C/PC/NC
4.15.10
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.15.11
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.15.12
The Access Point shall include at least one multi-gigabit Ethernet port (2.5 Gbps or higher).
C/PC/NC
4.15.13
The Access Point shall include at least one additional Gigabit Ethernet port.
C/PC/NC
4.15.14
The Access Point shall support a minimum of 24 SSIDs (8 per radio).
C/PC/NC
4.15.15
The Access Point shall support a minimum of 768 concurrently associated client devices.
C/PC/NC
4.15.16
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.15.17
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.15.18
The Access Point shall support advanced QoS and latency-sensitive traffic handling across multiple links.
C/PC/NC
4.15.19
The Access Point shall support dynamic link selection and load balancing across bands using MLO.
C/PC/NC
Type M - Entry level, premium, indoor tri-band WiFi 7 Access Point
4.16.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.16.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.16.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.16.4
The Access Point shall support tri-radio operation with simultaneous operation of:
• 2.4 GHz
• 5 GHz
• 6 GHz
C/PC/NC
4.16.5
The Access Point shall support at least 2x2:2 MIMO operation on all frequency bands.
C/PC/NC
4.16.6
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.16.7
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.16.8
The Access Point shall support simultaneous operation of all radios across 2.4 GHz, 5 GHz, and 6 GHz bands without performance degradation.
C/PC/NC
4.16.9
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.16.10
The Access Point shall support 4096-QAM modulation where supported by client devices.
C/PC/NC
4.16.11
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.16.12
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.16.13
The Access Point shall include at least one multi-gigabit Ethernet port supporting 5 Gbps or higher speeds.
C/PC/NC
4.16.14
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.16.15
The Access Point shall support a minimum of 768 concurrently associated client devices.
C/PC/NC
4.16.16
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.16.17
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.16.18
The Access Point shall support advanced QoS and latency optimization across multiple links when using Multi-Link Operation (MLO).
C/PC/NC
Type N - Mid-range, indoor tri-band WiFi 7 Access Point
4.17.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.17.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.17.3
The Access Point shall support ceiling and wall mounting options.
C/PC/NC
4.17.4
The Access Point shall support multi-radio operation including:
• One 2.4 GHz radio
• One 5 GHz radio
• One 6 GHz radio
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.17.5
The Access Point shall support at least:
• 2x2:2 MIMO in 2.4 GHz band
• 4x4:4 MU-MIMO in 5 GHz band
• 2x2:2 MU-MIMO in 6 GHz band
C/PC/NC
4.17.6
The Access Point shall support a maximum aggregate data rate of at least 12 Gbps under ideal conditions.
C/PC/NC
4.17.7
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.17.8
The Access Point shall support simultaneous operation of all radios across 2.4 GHz, 5 GHz, and 6 GHz bands without performance degradation.
C/PC/NC
4.17.9
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.17.10
The Access Point shall support 4096-QAM modulation where supported by client devices.
C/PC/NC
4.17.11
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.17.12
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.17.13
The Access Point shall include at least one multi-gigabit Ethernet port supporting 10 Gbps speeds.
C/PC/NC
4.17.14
The Access Point shall include at least one additional Gigabit Ethernet port.
C/PC/NC
4.17.15
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.17.16
The Access Point shall support a minimum of 1200 concurrently associated client devices.
C/PC/NC
4.17.17
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.17.18
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.17.19
The Access Point shall support advanced QoS and latency optimization across multiple links when using Multi-Link Operation (MLO).
C/PC/NC
4.17.20
The Access Point shall be optimized for medium to high-density enterprise environments.
C/PC/NC
Type O1 - High-end, indoor tri-band WiFi 7 Access Point
4.18.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.18.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.18.3
The Access Point shall support multi-radio operation including:
• One 2.4 GHz radio 4x4:4 MIMO
• One 5 GHz radio 4x4:4 MU-MIMO
• One 6 GHz radio 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
• One integrated Bluetooth/Zigbee radio for IoT applications
C/PC/NC
4.18.4
The Access Point shall support a maximum aggregate data rate of at least 18 Gbps under ideal conditions.
C/PC/NC
4.18.5
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.18.6
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.18.7
The Access Point shall support 4096-QAM modulation where supported by client devices.
C/PC/NC
4.18.8
The Access Point shall support simultaneous operation of all radios without performance degradation.
C/PC/NC
4.18.9
The Access Point shall include integrated omni-directional antennas.
C/PC/NC
4.18.10
The Access Point shall include at least two 10 Gigabit Ethernet uplink interfaces, including support for SFP/SFP+ or equivalent.
C/PC/NC
4.18.11
The Access Point shall support link redundancy and/or load sharing across multiple uplink ports.
C/PC/NC
4.18.12
The Access Point shall support IEEE 802.3bt Power over Ethernet (PoE).
C/PC/NC
4.18.13
The Access Point shall support a minimum of 16 SSIDs per radio.
C/PC/NC
4.18.14
The Access Point shall support a minimum of 1500 concurrently associated client devices.
C/PC/NC
4.18.15
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.18.16
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.18.17
The Access Point shall support flexible radio assignment, including the ability to configure the 6 GHz radio to operate in the 5 GHz band where required by regulatory constraints.
C/PC/NC
4.18.18
The Access Point shall support high-density deployment scenarios such as lecture halls, auditoriums, and large enterprise environments.
C/PC/NC
Type O2 - High-end, indoor tri-band WiFi 7 Access Point with external antennas
4.19.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.19.2
The Access Point shall be designed for indoor deployments.
C/PC/NC
4.19.3
The Access Point shall support multi-radio operation including:
• One 2.4 GHz radio 4x4:4 MIMO
• One 5 GHz radio 4x4:4 MU-MIMO
• One 6 GHz radio 4x4:4 MU-MIMO
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
• One integrated Bluetooth/Zigbee radio for IoT applications
C/PC/NC
4.19.4
The Access Point shall support a maximum aggregate data rate of at least 18 Gbps under ideal conditions.
C/PC/NC
4.19.5
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.19.6
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.19.7
The Access Point shall support 4096-QAM modulation
C/PC/NC
4.19.8
The Access Point shall support simultaneous operation of all radios without performance degradation.
C/PC/NC
4.19.9
The Access Point shall support external antennas.
C/PC/NC
4.19.10
The Access Point shall include RP-SMA connectors for external antenna attachment.
C/PC/NC
4.19.11
The Access Point shall include a minimum of eight RF connectors to support tri-band 4x4 operation.
C/PC/NC
4.19.12
The Access Point shall support deployment scenarios requiring customized RF coverage using external antennas.
C/PC/NC
4.19.13
The Access Point shall support Automated Frequency Coordination (AFC) for standard-power 6 GHz operations where required by regulatory domains.
C/PC/NC
4.19.14
The Access Point shall include at least two 10 Gigabit Ethernet uplink interfaces, including support for SFP/SFP+ or equivalent.
C/PC/NC
4.19.15
The Access Point shall support link redundancy and/or load sharing across multiple uplink ports.
C/PC/NC
4.19.16
The Access Point shall support IEEE 802.3bt Power over Ethernet (PoE).
C/PC/NC
4.19.17
The Access Point shall support a minimum of 16 SSIDs per radio.
C/PC/NC
4.19.18
The Access Point shall support a minimum of 1500 concurrently associated client devices.
C/PC/NC
4.19.19
The Access Point shall include LED indicators for system and radio status.
C/PC/NC
4.19.20
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.19.21
The Access Point shall support flexible radio assignment, including the ability to configure the 6 GHz radio to operate in the 5 GHz band where required by regulatory constraints.
C/PC/NC
4.19.22
The Access Point shall be suitable for high-density deployments requiring directional or customized RF coverage.
C/PC/NC
Type P - Entry level, premium outdoor harsh environment tri-band WiFi 7 Access Point
4.20.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.20.2
The Access Point shall be designed for outdoor deployments and comply with IP67 or better environmental rating.
C/PC/NC
4.20.3
The Access Point shall include surge protection and be suitable for deployment in environments exposed to electrical and weather-related disturbances.
C/PC/NC
4.20.4
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.20.5
The Access Point shall support tri-radio operation with simultaneous operation of:
• 2.4 GHz band
• 5 GHz band
• 6 GHz band
C/PC/NC
4.20.6
The Access Point shall support at least 2x2:2 MIMO operation on all frequency bands.
C/PC/NC
4.20.7
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.20.8
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.20.9
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.20.10
The Access Point shall support 4096-QAM modulation, where supported by client devices.
C/PC/NC
4.20.11
The Access Point shall support Automated Frequency Coordination (AFC) for outdoor 6 GHz operations where required by regulatory domains.
C/PC/NC
4.20.12
The Access Point shall support software configuration of the 6 GHz radio for 5 GHz operation in regulatory domains where outdoor 6 GHz operation is not permitted.
C/PC/NC
4.20.13
The Access Point shall include integrated sector antennas suitable for outdoor RF coverage.
C/PC/NC
4.20.14
The Access Point shall include at least one multi-gigabit Ethernet port supporting 5 Gbps or higher speeds.
C/PC/NC
4.20.15
The Access Point shall support IEEE 802.3at Power over Ethernet.
C/PC/NC
4.20.16
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.20.17
The Access Point shall support a minimum of 768 concurrently associated client devices.
C/PC/NC
4.20.18
The Access Point shall include LED indicators for system, radio, and Ethernet status.
C/PC/NC
4.20.19
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.20.20
The Access Point shall support operation across an outdoor temperature range of at least -40°C to 65°C.
C/PC/NC
Type Q1 - Mid-range, outdoor harsh environment tri-band WiFi 7 Access Point
4.21.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.21.2
The Access Point shall be designed for outdoor deployments and comply with IP67 or better environmental rating.
C/PC/NC
4.21.3
The Access Point shall include surge protection and be suitable for deployment in environments exposed to electrical and weather-related disturbances.
C/PC/NC
4.21.4
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.21.5
The Access Point shall support multi-radio operation including:
• One 2.4 GHz radio
• One 5 GHz radio
• One 6 GHz radio
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.21.6
The Access Point shall support at least 2x2:2 MIMO operation on all frequency bands.
C/PC/NC
4.21.7
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.21.8
The Access Point shall support simultaneous operation of all radios across 2.4 GHz, 5 GHz, and 6 GHz bands without performance degradation.
C/PC/NC
4.21.9
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.21.10
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.21.11
The Access Point shall support 4096-QAM modulation, where supported by client devices.
C/PC/NC
4.21.12
The Access Point shall support Automated Frequency Coordination (AFC) for outdoor 6 GHz operations where required by regulatory domains.
C/PC/NC
4.21.13
The Access Point shall support software configuration of the 6 GHz radio for 5 GHz operation in regulatory domains where outdoor 6 GHz operation is not permitted.
C/PC/NC
4.21.14
The Access Point shall include integrated omnidirectional antennas optimized for outdoor RF coverage.
C/PC/NC
4.21.15
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.21.16
The Access Point shall include at least one multi-gigabit Ethernet port supporting 10 Gbps speeds.
C/PC/NC
4.21.17
The Access Point shall include at least one additional Gigabit Ethernet port.
C/PC/NC
4.21.18
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.21.19
The Access Point shall support a minimum of 768 concurrently associated client devices.
C/PC/NC
4.21.20
The Access Point shall include LED indicators for system, radio, and Ethernet status.
C/PC/NC
4.21.21
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.21.22
The Access Point shall support advanced QoS and latency optimization across multiple links when using Multi-Link Operation (MLO).
C/PC/NC
4.21.23
The Access Point shall support operation across an outdoor temperature range of at least -40°C to 65°C.
C/PC/NC
4.21.24
The Access Point shall be optimized for medium to high-density outdoor environments.
C/PC/NC
Type Q2 - Mid-range, outdoor harsh environment tri-band WiFi 7 Access Point with external antennas
4.22.1
The Access Point shall be Wi-Fi Alliance certified for IEEE 802.11be (Wi-Fi 7) operation.
C/PC/NC
4.22.2
The Access Point shall be designed for outdoor deployments and comply with IP67 or better environmental rating.
C/PC/NC
4.22.3
The Access Point shall include surge protection and be suitable for deployment in environments exposed to electrical and weather-related disturbances.
C/PC/NC
4.22.4
The Access Point shall support pole and wall mounting options.
C/PC/NC
4.22.5
The Access Point shall support multi-radio operation including:
• One 2.4 GHz radio
• One 5 GHz radio
• One 6 GHz radio
• One dedicated radio for scanning, spectrum analysis, and wireless intrusion detection
C/PC/NC
4.22.6
The Access Point shall support at least 2x2:2 MIMO operation on all frequency bands.
C/PC/NC
4.22.7
The Access Point shall support a maximum aggregate data rate of at least 9 Gbps under ideal conditions.
C/PC/NC
4.22.8
The Access Point shall support simultaneous operation of all radios across 2.4 GHz, 5 GHz, and 6 GHz bands without performance degradation.
C/PC/NC
4.22.9
The Access Point shall support Multi-Link Operation (MLO) where supported by client devices.
C/PC/NC
4.22.10
The Access Point shall support channel widths up to 320 MHz in the 6 GHz band where regulatory domains allow.
C/PC/NC
4.22.11
The Access Point shall support 4096-QAM modulation, where supported by client devices.
C/PC/NC
4.22.12
The Access Point shall support Automated Frequency Coordination (AFC) for outdoor 6 GHz operations where required by regulatory domains.
C/PC/NC
4.22.13
The Access Point shall support software configuration of the 6 GHz radio for 5 GHz operation in regulatory domains where outdoor 6 GHz operation is not permitted.
C/PC/NC
4.22.14
The Access Point shall support external antennas.
C/PC/NC
4.22.15
The Access Point shall include N-type female connectors for antenna attachment.
C/PC/NC
4.22.16
The Access Point shall include a minimum of six RF connectors to support tri-band operation.
C/PC/NC
4.22.17
The Access Point shall support deployment scenarios requiring customized RF coverage using external antennas.
C/PC/NC
4.22.18
The Access Point shall include integrated lightning protection for outdoor antenna interfaces.
C/PC/NC
4.22.19
The Access Point shall include an integrated Bluetooth Low Energy (BLE) and/or Zigbee radio for IoT applications.
C/PC/NC
4.22.20
The Access Point shall include at least one multi-gigabit Ethernet port supporting 10 Gbps speeds.
C/PC/NC
4.22.21
The Access Point shall include at least one additional Gigabit Ethernet port.
C/PC/NC
4.22.22
The Access Point shall support a minimum of 32 SSIDs.
C/PC/NC
4.22.23
The Access Point shall support a minimum of 768 concurrently associated client devices.
C/PC/NC
4.22.24
The Access Point shall include LED indicators for system, radio, and Ethernet status.
C/PC/NC
4.22.25
The Access Point shall support IEEE 802.11a/b/g/n/ac/ax/be standards.
C/PC/NC
4.22.26
The Access Point shall support advanced QoS and latency optimization across multiple links when using Multi-Link Operation (MLO).
C/PC/NC
4.22.27
The Access Point shall support operation across an outdoor temperature range of at least -40°C to 65°C.
C/PC/NC
4.22.28
The Access Point shall be optimized for medium to high-density outdoor deployments requiring flexible RF design.
C/PC/NC