<<<DOC 1: omnivista-ng-10.5-golden-rfp-en.docx|1|1>>>

﻿-958266-92151200
Alcatel-Lucent Enterprise
OmniVista® NMS 10.5
GOLDEN RFP
Release Version
Date
Comments
10.4.3
December 2024
10.5.1
September 2025
Release sync with OVCX 10.5.1
10.5.2
January 2026
Release sync with OVCX version 10.5.2, OVTX version 10.5.2
Table of Contents
TOC \o "1-3" \h \z \u Introduction PAGEREF _Toc219969928 \h 6
Datasheet PAGEREF _Toc219969929 \h 7
Scope PAGEREF _Toc219969930 \h 7
Golden RFP – Minimum Supported Features PAGEREF _Toc219969931 \h 7
1.Ordering and Activation PAGEREF _Toc219969932 \h 7
2.Architecture and Solution Overview PAGEREF _Toc219969933 \h 11
3.Deployment PAGEREF _Toc219969934 \h 20
4.Multi-tenancy and multi-site services PAGEREF _Toc219969935 \h 23
5.LAN management PAGEREF _Toc219969936 \h 31
6.Programmability PAGEREF _Toc219969937 \h 37
7.Security and data privacy PAGEREF _Toc219969938 \h 39
8.Maintenance and operation PAGEREF _Toc219969939 \h 41
9.Monitoring - Analytics and Reporting PAGEREF _Toc219969940 \h 45
10.IoT Enablement PAGEREF _Toc219969941 \h 57
11.Network Access Control PAGEREF _Toc219969942 \h 60
Introduction
Alcatel-Lucent OmniVista® release 10 platform, a next-generation SaaS Network Management System (NMS) that offers advanced centralized visibility and configuration for Alcatel-Lucent Enterprise LAN and WLAN networks, is a scalable, resilient, secure, native network management system for unified access, offered as a subscription service. OmniVista® release 10 platform is available in 2 versions, the existing cloud-based version, known as OmniVista® Cirrus 10 (OVCX) and a new on-premise deployment option, called OmniVista® Terra 10 (OVTX), both versions form a unique platform architecture and deliver an equivalent feature set for any ALE LAN/WLAN network built with Stellar OmniAccess® access points and Omniswitch®.
Relying on state-of-the-art microservices architecture and developed with the latest DevOps methodologies and tools, OmniVista® release 10 platform facilitates your digital transformation. It allows you to respond to business needs such as real-time analytics, monitoring the Quality of Experience (QoE) for LAN/WLAN User, zero trust access policies, micro-segmentation, and Internet of Things (IoT) total enablement, including identification of network-connected devices.
OmniVista® release 10 provides an easy-to-deploy, effective way to manage and monitor Alcatel Lucent OmniAccess® Stellar Access Point and OmniSwitch® infrastructure. It offers advanced analytics for proactive service assurance and Unified Policies Access Manager (UPAM), a Network Access Control (NAC) module that includes enterprise authentication, role management, policy capabilities for guest access, and BYOD. OmniVista® release 10 is designed to improve wireless/wired user insights by providing detailed user QoE and behaviour analytics.
Alcatel-Lucent OmniVista® release 10 is a subscription-based service that facilitates alignment with your new business imperatives. Ease of purchasing, provisioning and ongoing daily operations are at the core of OmniVista® release 10. Shifting to a on-cloud or on-premise network management solution with OmniVista® release 10 simplifies digital transformation by reducing cost and administrative IT burden.
OmniVista® release 10 sets a new IT experience standard for simple yet powerful capabilities. It can scale and adapt to your business requirements. It offers advanced visibility and control over users and applications. By focusing on core IT operations, the comprehensive management OmniVista® release 10 solution makes it easy to improve application performance and troubleshoot issues in deployments with distributed locations and limited IT staff. OmniVista® release 10 protects your network infrastructure investment by adapting to changing business needs without the expense of “rip and replace”.
OmniVista® release 10, as a native network management platform backed with a microservices architecture, delivers valuable outcomes such as continuous improvement without downtime, always up-to-date management platform, scalability and security. The automatic software update, including critical security patches, improves security and compliance.
Datasheet
https://www.al-enterprise.com/-/media/assets/internet/documents/omnivista-cirrus-network-management-as-a-service-datasheet-en.pdf
Scope
OmniVista® release 10 delivers a single feature set, documented in separate materials. This document identifies the RFP requirements supported by the OmniVista® NMS release 10 platform and helps the customer understand which requirements are covered by the solution.
This document applies to OmniVista® NMS version 10.5 and does not cover Stellar WLAN features. For Wireless LAN–specific requirements, please refer to the Stellar WLAN Enterprise Golden RFP.
The following terms are used interchangeably throughout this document to refer to the OmniVista® release 10 platform: OmniVista, OmniVista NG 10, OmniVista NMS 10, OVNG10, or simply NMS — all referring to the same platform.
Golden RFP – Minimum Supported Features
Ordering and Activation
1.
The NMS platform shall support a seamless Quote-to-Cash process, enabling self-service to simplify the ordering and customization processes for the administrator
C/PC/NC
2.
The NMS platform shall follow a flexible SaaS subscription model
C/PC/NC
3.
The NMS platform shall support its own management interface allowing a flexible management of subscription life cycles, purchased licenses and adapted support for the different offers proposed
C/PC/NC
4.
The licensing and pricing of NMS platform shall be based on devices categories
C/PC/NC
Architecture and Solution Overview
5.
The NMS platform shall be based on a micro-services architecture for high-availability and resiliency
C/PC/NC
6.
The cloud-based NMS platform shall be designed with scalability in mind to allow large number of devices without requiring new equipment or deployment design change.
C/PC/NC
7.
The cloud-based NMS platform shall be hosted in SOC1 and SOC2 compliant and energy-efficient data centers
C/PC/NC
8.
The cloud-based NMS shall comply with data privacy, security and regulatory frameworks in US, EU, and abroad
C/PC/NC
9.
The cloud-based NMS shall be hosted in a public cloud environment based on regional DCs
C/PC/NC
10.
The NMS platform in its on-premise version shall be hosted in a private network environment and thus provide a centralized network management for completely autonomous single/Multi-tenant and single/Multi-site deployments, this without third party additional component
C/PC/NC
11.
The on-premise NMS platform shall be designed with scalability in mind to enable the management of a large number of devices without requiring new equipment or changes to the deployment design.
C/PC/NC
12.
The NMS platform in its on-premise version shall ensure the integrity of the LAN /WLAN network by supporting optimal monitoring, management and security features on the network.
C/PC/NC
13.
The NMS platform shall support any XL/Multi-tenant deployment (single/Multi-tenant, single/Multi-site) and offer advanced management functionalities, this without third party additional component
C/PC/NC
14.
The NMS platform shall propose an centralized management function based on embedded and secure Web GUI
C/PC/NC
15.
The NMS platform shall be able to manage both wired equipment (a) and wireless equipment (WLAN) in a “unified management” approach.
C/PC/NC
Deployment
16.
The NMS platform shall have a simplified deployment process with plug-and-play features
C/PC/NC
17.
The NMS platform shall support Zero-touch Provisioning
C/PC/NC
18.
The NMS platform shall support device objects grouping for easier provisioning of equipment for a given organization or site
C/PC/NC
19.
The NMS platform shall provide a simple migration procedure from a legacy Omnivista deployment to Omnivista release 10
C/PC/NC
Multi-tenancy and multi-site services
20.
The NMS platform shall allow multi-tenancy services for MSP including inventory management, user management control, and alerting capabilities from a single supervisor account and dashboard
C/PC/NC
21.
MSP level shall display organisations, tenants accounts, their roles and manage different tenants accounts
C/PC/NC
22.
Tenant level shall display organisation and manages its organisations upon the role defined
C/PC/NC
23.
The NMS platform shall support Role-Based Access Control (RBAC) of administrators per tenant with external authentication
C/PC/NC
24.
The NMS platform shall support Multi-site and Multi-level configurations with support for geo-location services
C/PC/NC
LAN management
25.
The NMS platform shall support a GRE tunneling service on the LAN layer 2 that offers GRE terminations for all types of devices or clients when crossing the LAN on switches for a given organization or site.
C/PC/NC
26.
The NMS platform shall provide a VLAN manager on LAN layer 2 for easy management of VLANs on the switches for an organization or a given site
C/PC/NC
27.
The NMS platform shall provide a IP manager on LAN layer 3 for easy management of IP Interfaces on the switches for an organization or a given site
C/PC/NC
28.
The NMS platform must provide full support for the IPv6 protocol in managing the LAN infrastructure of a given site or organization.
C/PC/NC
29.
The NMS platform shall support flexible and automated LAN management and updating using switch configurations after their onboarding
C/PC/NC
Programmability
This section focuses on the API-based programmability of the NMS cloud-hosted version.
30.
The cloud-based NMS platform shall provide a secure RESTful programming interface
C/PC/NC
31.
The cloud-based NMS platform shall support 3th-party integration via its programming interface
C/PC/NC
32.
The NMS API shall be protected by authentication and method to access API described
C/PC/NC
33.
The cloud-based NMS platform shall contain OpenAPI documentation with use cases
C/PC/NC
Security and data privacy
This section focuses on the security and data privacy of the NMS cloud-hosted version.
34.
The cloud-based NMS platform shall encrypt management traffic of managed network devices to the cloud
C/PC/NC
35.
The cloud-based NMS shall support certificate-based authentication and encryption
C/PC/NC
36.
The cloud-based NMS shall support RADsec client for user and device authentication
C/PC/NC
37.
The cloud-based NMS shall support two-factor authentication for administrator access
C/PC/NC
38.
The cloud-based NMS shall support single sign-on (SSO) using enterprise identity providers.
C/PC/NC
39.
The cloud-based NMS shall support enforcing a strong password policy
C/PC/NC
Maintenance and operation
40.
The NMS platform should allow automated and scheduled firmware updates for managed devices with latest releases reducing IT involvement and maintenance windows
C/PC/NC
41.
The NMS platform shall support a unified LAN and WLAN topology providing complete visibility of each installation on the sites, and actions on an equipment if required
C/PC/NC
42.
The NMS platform should allow automated and instant configuration backups for managed devices, including all common and security configurations of the device
C/PC/NC
Monitoring - Analytics and Reporting
43.
The NMS platform shall support real-time monitoring of network performance and KPIs through customizable dashboard with visual widgets
C/PC/NC
44.
The NMS solution main dashboard shall support generating user QoE metrics and Network KPIs for WLAN clients
C/PC/NC
45.
The NMS solution main dashboard should provide quick QoE analytics to find root causes of connectivity issues for WLAN clients
C/PC/NC
46.
The NMS platform shall support network analytics to monitor network health and resource utilization on LAN/WLAN, for an organization or a given site
C/PC/NC
47.
The NMS platform shall support live and historical client analytics for at least 30 days
C/PC/NC
48.
The NMS solution shall support generating client distribution reports per channel and per frequency band for WLAN
C/PC/NC
49.
The NMS solution shall support generating user application analytics to monitor usages on LAN/WLAN and manage reporting on clients usages for an organization or a given site
C/PC/NC
50.
The NMS platform shall support generating managed devices live and historical health reports and metrics
C/PC/NC
51.
The NMS platorm shall support analytics data reports with report scheduling option
C/PC/NC
52.
The NMS platform shall support generating built-in template alerts for organizations and sites
C/PC/NC
53.
The NMS platform shall support configurable term data persistency and durations
C/PC/NC
54.
The NMS shall support configuring at least four remote syslog servers
C/PC/NC
IoT Enablement
IoT requirement specific to Stellar WLAN are not described in this document.
55.
The NMS platform shall provide IoT devices inventory management with identification features of contextual information
C/PC/NC
56.
The NMS platform shall provide IoT devices policy enforcement and control
C/PC/NC
57.
The NMS solution shall offer IoT device secure onboarding that is as simple as possible for managed WLAN and without requiring additional third-party component.
C/PC/NC
58.
The NMS platform shall provide a comprehensive and integrated set of diagnostic tools designed to simplify technical support operation for an organization or site
C/PC/NC
Network Access Control
Stellar Guest access is also developed in separated materials. Please refer to the Golden RFP Stellar for additional details on the CP solution designed for Stellar.
59.
The NMS platform shall support an integrated Network Access Control (NAC) with various authentication capabilities, including 802.1x, MAC, and certificate-based authentication.
C/PC/NC
60.
The NMS platform shall support built-in RADIUS server and Captive Portal capabilities. RADIUS must not be proposed as separated feature
C/PC/NC
61.
The NMS platform shall support minimum of one built-in RADIUS instance and one built-in LDAP
C/PC/NC
62.
The NMS platform shall support integration with external authentication and identity providers, including secure RADIUS communication and role-mapping capabilities
C/PC/NC
63.
The NMS platform shall support grouping of attributes such as MAC and IP addresses, ports, or services into lists or profiles for easy policy configuration
C/PC/NC
64.
The built-in RADIUS of NMS shall support dynamically filter ids such as VLANs and Private Groups to respond to extended WLAN user connections usage with dedicated specific groups
C/PC/NC
65.
The NMS platform shall support the configuration of unified LAN/WLAN access with policy-based control, for connected and authenticated users and equipment
C/PC/NC
66.
The NMS platform shall support Deep Packet Inspection (DPI) capabilities for application-level recognition up to Layer 7 (L7). This feature should enable advanced control over applications running on the LAN/WLAN, including those using secure HTTPS protocols. The administrator must be able to monitor application traffic and apply application-level QoS policies (such as bandwidth management or blocking).
C/PC/NC
67.
The NMS platform shall support a built-in local database for company property and user accounts for employees and guests
C/PC/NC
68.
The NMS platform shall support GRE tunneling features such as isolation for WLAN Guest
C/PC/NC
69.
The NMS must provide flexible and open guest access management based on support for external captive portals, including an advanced, predefined embedded captive portal to provide web authentication for guests and visitors
C/PC/NC
70.
The NMS platform shall support unified location and period-based policy configuration when guests and visitors are supported by the embedded captive portal
C/PC/NC
71.
The NMS platform shall support configuring different guest service levels when guests and visitors are supported by the embedded captive portal
C/PC/NC
72.
The NMS platform shall support configuring guest time and data quotas when guests and visitors are supported by the embedded captive portal
C/PC/NC