<<<PAGE 1>>>
OmniVista UPAM and Palo Alto 
Networks User-ID Integration Guide
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide

<<<PAGE 2>>>
2
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Table of Contents
1. 	 About this Integration Guide ......................................................................................3
2.  	 The Zero-Trust Paradigm...............................................................................................3
3.	
About Palo Alto Networks’ User-ID...........................................................................3
4.	
About Alcatel-Lucent OmniVista UPAM...................................................................3
5. 	 Use case...............................................................................................................................3
6. 	 Mechanism.........................................................................................................................4
7.  	 Procedure overview.......................................................................................................6
8.  	 OmniVista: Configuring the AAA profile..................................................................6
9.  	 OmniVista: Configuring UPAM Access  
	
Policy and Authentication Strategy..........................................................................8
10.  OmniVista: Configuring UPAM for  
	
external syslog logging to PAN firewall..................................................................9
11.  OmniVista: Configuring and applying the Access Auth profile....................10
12.  PAN: Enabling User-ID on the required firewall zones..................................10
13.  PAN: Enabling UDP User-ID Syslog  
	
Listener on Interface Management Profile.........................................................11
14.  PAN: Creating syslog parse profile for UPAM logs...........................................11
15.  PAN: Configuring syslog server monitoring........................................................13
16.  PAN: Enabling User-ID in firewall policies..........................................................14
17.  PAN: Verifying User-ID mappings...........................................................................14
18.  PAN: Verifying User-ID policies...............................................................................14
19.  Conclusion........................................................................................................................15

<<<PAGE 3>>>
3
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
1.  About this Integration Guide 
The purpose of this integration guide is to help ALE Business Partners and customers integrate 
Alcatel-Lucent OmniVista® Unified Policy Authentication Management (UPAM) with Palo Alto 
Networks’ (PAN) next-generation firewall’s User-ID feature. Through this integration, users 
or devices authenticated to the LAN and/or WLAN networks can also be simultaneously and 
seamlessly authenticated to the PAN firewall. OmniVista UPAM can share user or device 
connection status as well as identity or role information with the firewall for enhanced visibility, 
finer policy control and improved logging, reporting and forensic analysis.
2.  The Zero-Trust Paradigm
In a legacy firewall, the “trust” boundary is based on the point of connection: “Inside” users are 
implicitly trusted and “outside” users are not. In an airport analogy, this would be equivalent to 
allowing land-side passengers to go through security unchecked. With trends such as mobility 
and Internet of Things (IoT), that notion of “trust” is completely outdated. Some examples: 
A BYOD device may bring malware into the organization; an IoT device may be intrinsically 
vulnerable and become an attack vector; and even corporate users could be malicious. 
The paradigm today is “Zero Trust”. No matter where the user or device is connected, never trust 
and always verify. Establishing identity is at the core of the Zero-Trust Paradigm. Going back to 
the airport analogy, the first thing an immigration officer will do is check the passport. Other 
checks such as a visa check, database checks and so on, are done after identity is established 
with a passport, a matching fingerprint, etc. And since establishing identity is such a fundamental 
check at the core of the Zero-Trust Paradigm, next-generation firewalls have multiple mechanisms 
of determining identity. 
3.  About Palo Alto Networks User-ID
User-ID is a standard feature on Palo Alto Networks (PAN) firewalls that enables the firewall to 
identify users by leveraging various information repositories and techniques. Knowing users’ 
identities and/or roles, rather than just their IP address, brings several benefits including: Improved 
visibility into usage patterns, finer policy control by only allowing application and/or resource 
access to those users/roles with a legitimate need for it (principle of least privilege) and enhanced 
logging, reporting and forensics by referencing user identity or role rather than just an IP address. 
Please refer to Palo Alto Networks documentation for further information on the User-ID feature.
4.  About Alcatel-Lucent OmniVista UPAM
OmniVista’s Unified Policy Authentication Management module is a unified access management 
platform for both Alcatel-Lucent OmniSwitch® Ethernet switches and Alcatel-Lucent OmniAccess® 
Stellar access points. UPAM includes both a captive portal and a RADIUS server and can 
implement multiple authentication methods such as MAC authentication, 802.1x authentication 
and captive portal authentication. Users can authenticate against UPAM’s local database or 
against external databases including Microsoft Active Directory, LDAP and external RADIUS. 
UPAM’s customizable captive portal can implement flexible authentication strategies for guest 
and BYOD users with integrated credential management through email, SMS and social login 
(Facebook, Google, WeChat and Rainbow).
5.  Use case
There are two main use cases when it comes to wired and wireless users: Corporate (AD) devices 
and BYOD or IoT devices. For corporate devices, such as a corporate user on a corporate laptop, 
OmniVista UPAM can proxy authentication to AD and the preferred point of integration is 
directly on AD, not on UPAM. This guide will not elaborate on this use case. Please refer to  
Palo Alto Networks documentation for further details on the AD-based integration.

<<<PAGE 4>>>
4
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Figure 1. AD-based integration
192.168.10.1: Joe, Finance
192.168.20.1: Jane, Marketing
Internet
AD/NPAS
Joe
Finance
IP: 192.168.10.1
UNP: Finance
UNP: Marketing
OV2500/UPAM
MAC/802.1x/CP
RADIUS
LDAP
MAC/802.1x/CP
Proﬁle
Proﬁle
Jane
Marketing
IP: 192.168.20.1
Marketing
✓VLAN ✓QoS
✓ACL
Finance
✓SVC
✓QoS
✓ACL
In this guide, we focus on the other use case in which a BYOD or IoT device is authenticated 
directly against the UPAM database or proxied to an external RADIUS database (other than 
Microsoft’s Network Policy and Access Services or NPAS) because these devices may not 
be associated with an AD account. This use case is shown in the figure below with IoT as an 
example. This document focuses on this use case because the point of integration is directly  
on OmniVista UPAM.
Figure 2. Syslog-based integration
Syslog Accounting
192.168.10.1: IoT_Camera
192.168.20.1: IoT_Sensor
Internet
Ext RADIUS (optional)
UNP: IoT_Camera
UNP: IoT_Sensor
OV2500/UPAM
802.1x/MAC
RADIUS
802.1x/MAC
Proﬁle
Proﬁle
Sensor
✓VLAN ✓QoS
✓ACL
Camera
✓SVC
✓QoS
✓ACL
 
6.  Mechanism
Once onboarded, wired or wireless devices authenticate against the UPAM RADIUS through MAC 
or 802.1x authentication. UPAM logs authentication and accounting events to the PAN built-in 
syslog receiver. A parse filter is defined on the PAN firewall to extract the role or username from 
these messages. Please refer to the snippet below for some sample syslog messages generated 
by UPAM.

<<<PAGE 5>>>
5
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Figure 3. Sample UPAM syslog logging
Let’s examine some of the relevant fields in these messages:
APMAC: The RADIUS NAS (the switch or access point) MAC address.
authType: This field specifies the authentication mechanism (for example, MAC or 802.1x).
changeType: This can be “Access”, which indicates successful authentication, “Accounting”,  
for periodic RADIUS accounting messages or “Disconnect” for logout/disconnect events.
deviceIP: This is the end device’s IP address.
filterID: The filterID represents the uNP (User Network Profile) or ARP (Access Role Profile)  
or in other words, the role assigned to the device.
username: As the name suggests, this is the username. When using MAC authentication, the 
username is simply the end device’s MAC address.
We want to bring attention to the following aspects:
•	 The device’s IP address, which the firewall needs for policy enforcement, is contained 
in “Accounting” and “Disconnect” messages, but usually not in “Access” messages. This is 
because obtaining an IP address through DHCP can take some time and can only occur after 
authentication.
•	 Therefore, RADIUS interim accounting needs to be enabled in addition to authentication.
•	 Only a single syslog parsing profile can be applied to any given syslog source on the firewall. 
We will create a filter for “Accounting” messages as this is the message type containing all the 
necessary information: deviceIP, username and/or filterID. We will not be able to configure a 
filter for “Disconnect” messages. As a result, users will not be immediately logged out from 
the firewall when they disconnect. Users will be logged out if no “Accounting” updates are 
received before expiration of the User Identification Timeout, which is 45 minutes by default.
•	 For this reason, the RADIUS interim accounting interval should be set lower than the User 
Identification Timeout.

<<<PAGE 6>>>
6
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
7.  Procedure overview
Here’s a summary of the different steps required on both OmniVista/UPAM and the PAN firewall.
OmniVista UPAM
1.	 Configuring AAA profile for 802.1x/MAC authentication AND accounting against UPAM
2.	 Configuring UPAM Access Policy and Authentication Strategy
3.	 Configuring UPAM for external syslog logging to PAN firewall
4.	 Creating Access Auth profile for MAC/802.1x authentication against UPAM
PAN firewall
1.	 Enabling User-ID on required FW zones
2.	 Enabling UDP syslog listener on interface’s management profile
3.	 Creating syslog parse profile for UPAM logs
4.	 Configuring syslog server monitoring
5.	 Enabling User-ID firewall policies
6.	 Verifying User-ID mappings
7.	 Verifying User-ID policies
8.  OmniVista: Configuring the AAA profile
On OmniVista, go to Unified Access->Template->AAA Server Profile and click “+”.
Create a new AAA server profile pointing to the UPAMRadiusServer for both authentication and 
accounting. You will do this for the required authentication methods: 802.1x, MAC or Captive 
Portal. In the example below, only 802.1x and MAC are shown as IoT devices do not normally 
use Captive Portal authentication.
Figure 4. AAA Server Profile - Authentication

<<<PAGE 7>>>
7
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Figure 5. AAA Server Profile - Accounting
 
You may also specify the Accounting Interim Interval (600 seconds by default) or, alternatively, 
trust the accounting interim interval set by the RADIUS server (UPAM or external) in which case, 
the accounting interim interval must be configured on the RADIUS server. In most cases, the 
first accounting message sent shortly after successful authentication will contain the device’s 
IP address and allow the firewall to identify the user. In other cases, however, the device’s IP 
address will only be present in the second and later accounting messages. In such case, setting  
a lower interim interval will result in this information being updated quicker on the firewall.
Regardless of whether the accounting interim interval is trusted from the RADIUS server or set 
on the AAA Server Profile, it must be lower than the User Authentication Timeout set on the 
firewall, which is 45 minutes by default. The 600 second default setting meets this requirement.
Figure 6. MAC - Accounting Interim Interval

<<<PAGE 8>>>
8
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Figure 7. 802.1x Accounting Interim Interval
 
9.  OmniVista: Configuring UPAM Access Policy and Authentication 
Strategy
As a reminder, the Authentication Strategy defines which authentication database will be used 
and other parameters while the Access Policy routes authentication requests to the right strategy 
based on criteria such as the SSID or the switch NAS IP.
To create an Authentication Strategy, go to UPAM->Authentication->Authentication Strategy  
and click “+”. A sample Authentication Strategy using UPAM’s internal database is shown below. 
The Default Access Role Profile (ARP) is the role to be applied in case no specific role is assigned 
to the device or the specified role is not locally defined on the switch or AP group.
Note: The Default ARP must be created before creating the Authentication Strategy. In addition,  
all relevant ARPs must be created and mapped to switches and AP groups. These steps will not  
be shown in this guide.
Figure 8. Authentication Strategy

<<<PAGE 9>>>
9
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
To create an Access Policy, go to UPAM->Authentication->Access Policy and click “+”. The Access 
Policy maps authentication requests to the previously created Authentication Strategy based on 
criteria such as SSID (shown in the example), NAS IP, Location, etc.
Figure 9. Access policy
 
10.  OmniVista: Configuring UPAM for external syslog logging to  
PAN firewall
Go to UPAM->Settings->External Log Server. Enable logging and select Syslog with default  
port (514) as shown in the example below. Optionally, enter the IP address or hostname of  
an additional syslog logging server.
Figure 10. External syslog logging
 
Note: The PAN firewall does not respond to Syslog connection tests. Connection tests will result in 
“The server cannot connect” messages. This is the expected behavior. You should still verify that 
connectivity on UDP port 514 is possible between UPAM and the firewall.

<<<PAGE 10>>>
10
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
11.  OmniVista: Configuring and applying the Access Auth profile
Go to Unified Access->Unified Profile->Templates->Access Auth Profile and click on “+”. Select the 
previously defined UPAM AAA Server Profile and configure MAC/802.1x authentication options 
as needed. The example below shows MAC authentication with “IOT_Default” profile used as 
default and pass-alternate (used when the returned attribute does not match a locally defined 
profile on the switch or AP group). When done, apply it to required switches and AP groups.
Figure 11. Access Auth profile
 
12.  PAN: Enabling User-ID on the required firewall zones
On the PAN firewall, go to Network->Zones and select the zone or zones where User-ID is to be 
enabled. Enable the checkbox as shown in the example below. Configure include/exclude ACLs  
if needed.
Figure 12. Enabling User-ID on firewall zones

<<<PAGE 11>>>
11
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
13.  PAN: Enabling UDP User-ID syslog listener on interface 
management profile
On the firewall, go to Network->Network Profiles->Interface Management. Add or select an 
existing profile. Enable the checkbox for User-ID Syslog Listener UDP and add UPAM’s IP address 
to the list as shown in the example below. This profile must be applied to the management 
interface where UPAM syslog messages are to be received.
Figure 13. Interface management profile
 
14.  PAN: Creating syslog parse profile for UPAM logs
The syslog parse profile helps the firewall identify username and address fields in OmniVista UPAM’s 
syslog log messages. To create the parse profile, go to Device->User Identification and within the 
“User Mapping” tab, click on the gear icon to the right of “Palo Alto Networks User ID Agent Setup”.
Once on the “Palo Alto Networks User ID Agent Setup” window, click on the “Syslog Filters” tab 
and then on “Add”.
Figure 14. User mapping

<<<PAGE 12>>>
12
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Figure 15. Syslog filters
 
The first example below maps the username and deviceIP fields in accounting messages. For the 
PAN firewall to apply policies based on those usernames, a user group containing those users 
must be created in the firewall’s local database or, each username must be listed within the 
firewall policy. This may be problematic particularly when using MAC authentication because  
the username would simply be the device’s MAC address. 
A simpler alternative is to map the filterId (that is, the UNP, ARP, or “role”) instead. This is 
shown in the second example. In that case, firewall policies can simply reference the UNP/ARP 
or device’s role (for example, “sensor”) and there is no need to create users in the firewall’s 
database. The downside of this alternative is that firewall logs will not contain the actual 
username but rather the role. However, OmniVista UPAM can log messages to another server 
in addition to the PAN firewall. This can help retrieve the actual username associated to an IP 
address at a given time, if required for forensic purposes, etc. Time synchronization between 
OmniVista, the PAN firewall and the syslog server will be required for log correlation.
Figure 16. Syslog parse profile – user mapping

<<<PAGE 13>>>
13
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
Figure 17. Syslog parse profile – role mapping
 
15.  PAN: Configuring syslog server monitoring
Go to Device->User Identification->Server Monitoring and click “Add”. Provide a name, select 
“Syslog Sender” as the type, fill in the UPAM IP address, select connection type “UDP” and the 
syslog parse filter defined in the previous step. Optionally, enter a domain name to prepend 
to the username if the log entry has no domain name, which is the case when authenticating 
against UPAM’s local database.
Figure 18. User identification monitored server
 
Optionally, define subnetworks to include or exclude from user mapping.

<<<PAGE 14>>>
14
Application Note
OmniVista UPAM and Palo Alto Networks User-ID Integration Guide
16.  PAN: Enabling User-ID in firewall policies
Go to Policies->Security and create or select an existing policy. Select the “User” tab and on the 
left-hand side panel, click “Add”. If you configured the syslog parse filter to map the filter-id 
(that is, the role), you will simply add it to the list. In the example below, the filter-id is “iot_stb”, 
where stb stands for “set-top box”. Note that usernames containing upper-case characters will  
be turned into lower case. Therefore, you should use lower-case characters in the policy.
If you configured the syslog parse filter to map usernames, you will need to list each username 
in the policy or, create a local user group with all required usernames.
Figure 19. User-ID policies
 
17.  PAN: Verifying User-ID mappings
User mappings can be verified through the CLI with the command “show user ip-user-mapping 
all”. Please refer to the example below. You can verify that the username received (or the role  
in this case) is shown in lower case even though upper case is used within OmniVista.
Figure 20. Verifying User-ID mappings
 
18.  PAN: Verifying User-ID policies
To verify firewall policies are identifying users correctly, go to Monitor->Logs->Traffic. Configure 
a filter if required. In the example below, the “integration_test” policy is configured to block ping 
for the “iot_stb” user, or role.

<<<PAGE 15>>>
www.al-enterprise.com The Alcatel-Lucent name and logo are trademarks of Nokia used under license 
by ALE. To view other trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.
com/en/legal/trademarks-copyright. All other trademarks are the property of their respective owners.  
The information presented is subject to change without notice. Neither ALE Holding nor any of  
its affiliates assumes any responsibility for inaccuracies contained herein. © Copyright 2020  
ALE International, ALE USA Inc. All rights reserved in all countries. DID20062901EN (July 2020)
Figure 21. Verifying User-ID policies
 
19.  Conclusion
By integrating OmniVista UPAM with the PAN firewall’s User-ID feature, we get better visibility 
into wired and wireless users and devices and the resources and applications that they consume. 
It enables finer control by allowing access only to those users and devices with a legitimate 
business need, thus reducing the attack surface. Logging and reporting is enhanced with user or 
device information. Reporting can benefit from filtering activity for a specific user, role or device 
and forensic analysis can quickly identify the username or role, not just the IP address.