

<<<PAGE 1>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
OMNIACCESS STELLAR WLAN 
ADVANCED TROUBLESHOOTING 
EDITION 01 
PARTICIPANT'S GUIDE

<<<PAGE 2>>>
Proprietary Ownership Declaration 
I agree not to copy, produce, reproduce, transfer, distribute, decode and/or modify any 
ALE material (including any and all documentation, manuals, software presentation, 
student book and software files) made available and/or used as part of the ALE training. 
I acknowledge that sharing of any kind of courseware and media used are strictly forbidden 
without approval from ALE Training Services. 
I represent and warrant that I will not use or not permit to use the courseware and\or 
educational tools supplied by ALE to provide trainings in a private capacity or for my 
employer or any third party. 
I also acknowledge and agree that ALE owns and reserves all copyright in and all other 
intellectual property rights relating to the ALE training material (including courseware and 
all associated documentation) provided during the training. 
I understand that any breach or threat of breach of the above shall entitle ALE to injunctive 
and other appropriate equitable relief (without the necessity of proving actual damages), 
in addition to whatever remedies ALE may have at law. 
Furthermore, I acknowledge and agree that ALE will be entitled to cancel immediately all 
my certifications in case of any breach of the above.

<<<PAGE 3>>>
TROUBLESHOOTING METHODOLOGY 
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 4>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand potential root causes of 
Wireless issues
• Understand and apply the process steps 
when troubleshooting a case

<<<PAGE 5>>>
WIRELESS
POTENTIAL WLAN TROUBLESHOOTING CAUSES
End User
Wi-Fi Device
Client
LAN
WAN Router
Switch
RF Medium
DHCP OmniVista
DNS
Radius
LDAP/AD
Stellar AP
LOCAL NETWORK
INTERNET

<<<PAGE 6>>>
POTENTIAL WLAN TROUBLESHOOTING CAUSES
WIRELESS
End User
Wi-Fi Device
Client
RF Medium
Stellar AP
Different skills
Knowledge perception
Device on/off
Drivers
Radio Capabilities
802.1X Profile
Minimum requested Data Rates
Roaming algorithm
802.11n
• Association (Beacon, probes request/response, 802.11k/v/r)
• Authentication (Open, Pre-Shared Key, 802.1X/RADIUS)
• Encryption (No encryption, TKIP, AES/CPPM)
• Upper Layers (DHCP, IP, DNS, VLAN, Gateway, Captive Portal)
RF Media (RSSI, SNR, Radio Coverage)
Configuration, SSIDs, Minimum basic rates, Band steering, 
Radio capabilities, Roaming, QoS

<<<PAGE 7>>>
POTENTIAL WLAN TROUBLESHOOTING CAUSES
LOCAL NETWORK
PoE, Antenna, AP location, Physical layer issues
Configuration, Firmware, LAN interface
PoE, VLANs, Port speed, Configuration, QoS
OmniVista: Configuration, Firmware, Licensing issues, VLANs
• DHCP: Configuration, Lease duration, Address Pool scope, DHCP options
• DNS: Configuration, Security, Blacklist
• 802.1X/RADIUS: Configuration, Ports, Range, EAP types, Certificate issues
• LDAP/AD: Accounts, Credentials, Custom RADIUS attributes
Firewall Rules, Capacity, Rate Limiting, Bandwidth Shaping 
Size of Internet pipe, Internet destination issues, Costs
LAN
Firewall &
WAN Router
Switch
Servers
Stellar AP
LAN
ACLs, VLANs, Tunnels, NAT
QoS: DSCP, WMM Categories, End-To-End QoS

<<<PAGE 8>>>
POTENTIAL WLAN TROUBLESHOOTING CAUSES – INTERNET
Bandwidth Throttling, Jitter, Latency
External DNS
External Captive Portal
Issues independent from the network administrator
WAN Router
Internet

<<<PAGE 9>>>
TROUBLESHOOTING PROCESS
USE CASE

<<<PAGE 10>>>
TROUBLESHOOTING PROCESS STEPS
Document
Document initial issues, 
processes, diagnostics & 
resolutions
Follow up with those involved
Solve
Formulate & Implement plans
May include changes to drivers, 
configurations or design
Identify
Determine if problem exists
Ask questions & collect infos
Correctly identify issue
Locate
Tied to physical space
Tied to specific devices
Use OSI model to define layer
Verify
Extensive testing to confirm 
and verify the solution did 
indeed solve the issue at hand
Re-Create
If you can’t recreate this 
issue, return to step one and 
ask more questions
Isolate
Identify OSI Layer, Specific
devices, Specific locations, 
Driver versions

<<<PAGE 11>>>
USE CASE
Q&A with the customer in order to Analyze the issue:
• Identifier
• Locate
• Isolate
Gather configuration from the customer topology:
• AP Log file
• Access Switch configuration
Description of the 
issue by the client
«WifFi clients cannot 
log into the SSID 
Employee»
Open the file
“Troubleshooting interview – Use Case” for more details
VLAN 10
VLAN 20
“Employee” 
VLAN
Access switch
“Building_A”
Analyze of the issue
Wrong VLAN configuration on 
the Access Switch “Building_A”
Identify
Locate
Isolate

<<<PAGE 12>>>
USE CASE
Recreate
Gather network configuration 
from customer:
• Access switches: vcboot.cfg
• OmniVista: Access the Organization
• Stellar AP: APs configuration Backup
• Servers: Backup configuration
End User
Wi-Fi 
Device
Client
LAN
WAN Router
Switch
RF Medium
DHCP OmniVista
DNS
Radius
LDAP/AD
Stellar AP
Re-create customer topology 
in your environment
Re-create customer issue 
in your environment
1
1
2
2
3
3

<<<PAGE 13>>>
USE CASE
Solve
Verify
VLAN 10
VLAN 10
“Employee” 
VLAN
Access switch
“Building_A”
Status
Issue has been identified as the wrong « Employee » VLAN configured on the access switch « Building_A ».
Reproduction of the customer’s setup didn’t show an alternate root cause of this issue.
Resolution
Reconfigure the VLAN « Employee » on the Access Switch « Building_A ».
Verification
Test the solution in your environment.
Apply the correction in the customer environment.
Ask the client to test their day-to-day wireless applications
(Rainbow, voice, mail,…) and wireless devices to check the solution stability.

<<<PAGE 14>>>
USE CASE
• Document the troubleshooting case:
• Issue description
• Topology
• Firmware versions
• Diagnostic
• Resolution
• Configuration fixes
• Firmware version to be used
• Hardware replacement
• Follow the case 
• Check that the solution is permanent
• No side effects due to the resolution
• Database example:
ALE Technical Knowledge Center
Documentation

<<<PAGE 15>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 16>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by AL 
Troubleshooting Process 
Interview - Use Case

<<<PAGE 17>>>
1 
Interview - Use Case 
 
 
 1 
Interview 
 
List of questions and answers between you and the customer. 
This is just a partial list as the first answers from the customer will guide you towards more precise questions 
and will close the doors for other generic questions. 
 
The following table contains the questions, answers, deduction from the answers and analyze results. 
 
Description of the issue from the customer: “Wifi client can not log into the SSID Employee” 
 
Question 
Answer 
Deduction from the answer 
Next step 
Same behavior for all 
users? 
Yes 
The issue is not related to a 
specific device/hardware. 
Localized issue? 
Do you observe this issue 
at the same location or 
everywhere in the 
building? 
In the same section of 
the building. 
Not a global OmniVista 
configuration issue. Otherwise, 
all the Stellar APs broadcasting 
the same SSID in the building 
would be impacted. 
Localized on a single 
equipment of the 
network? 
The impacted clients are 
all associated to the 
Stellar APs connected to 
the same access switch? 
Yes, all the impacted 
APs are connected to 
the access switch 
“Building_A”. 
The issue might come from the 
SSID configuration or the access 
switch configuration. 
More than one SSID 
impacted? 
Same issue on other SSIDs 
in the same location? 
No, only the 
connection to the 
Employee SSID is 
impacted. 
The issue might come from the 
“Employee” SSID configuration 
or the access switch 
configuration. 
Analyze logs of a 
Stellar AP connected 
to the switch 
“Building_A”. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Identify 
Isolate 
Locate

<<<PAGE 18>>>
2 
Interview - Use Case 
 
 
 2 
Configuration analysis 
 
In a second step, request to the customer the AP log file from one of the Stellar AP impacted. 
Request also the configuration file from the access switch “Building_A”. 
 
Question 
Answer / 
Configuration analyze 
Deduction from the answer 
Next step 
What is the IP 
configuration of the 
Stellar AP? 
Correct IP. 
Correct mask. 
Correct gateway. 
The issue is not related to the 
dhcp-relay configuration. 
Otherwise, the Stellar AP won’t 
get any IP address. 
Access switch 
configuration issue? 
VLAN assigned to the SSID 
Employee in OmniVista 
compared to the VLAN 
assigned on the Access 
Switch? 
VLAN 10 on the SSID in 
OmniVista and VLAN 
20 on the Access 
Switch: 
“Building_A” 
Wrong VLAN configured on the 
Access Switch. 
Fix the issue on the 
Access Switch. 
 
 
 
 
 
 
 
 
Root cause: 
Wrong VLAN configuration on the Access switch “Building_A” 
 
Resolution: 
Update the tagged VLAN with the ID = 20. 
 
 
VLAN 10 
VLAN 20 
“Employee” 
VLAN 
Access switch 
“Building_A” 
Identify 
Isolate 
Locate

<<<PAGE 19>>>
TROUBLESHOOTING TOOLS
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE

<<<PAGE 20>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand and use the internal 
troubleshooting tools
• Understand and list the external tools used 
to analyze the wireless network and issues

<<<PAGE 21>>>
INTEGRATED DIAGNOSTIC TOOLS

<<<PAGE 22>>>
BEFORE TROUBLESHOOTING
• NTP server configured in the network
• Synchronize all equipment with the same NTP server:
• Stellar APs
• OmniVista
• Access Switches
NTP synchronization
Wi-Fi Device 
Client
LAN
Switch
OmniVista
NTP 
server
Stellar AP
Error 10
11/11/2019 12:09:34 : 
Error 10
15/11/2019 13:15:30 :
Error 10
AP Logs
10/11/2019 08:15:30 : 
Error 10
15/11/2019 13:15:30 :
Error 10
OmniVista Logs
15/11/2019 13:15:30 : 
Error 10
15/11/2019 13:15:30 :
Error 10
Access Switch Logs
• No NTP server
• NTP server

<<<PAGE 23>>>
CONSOLE CONNECTION TO THE STELLAR AP
• Check: Serial port connection
• Check: Serial port configuration
• Speed
: 115 200
• Data bits
: 8
• Stop bits
: 1
• Parity
: None
• Flow ctrl
: None

<<<PAGE 24>>>
SSH CONNECTION TO THE STELLAR AP
• Activate SSH Login & Set a password:
• Check the configuration in CLI
• File: /var/config/public_group.conf
• Use a third-party software (putty, teraterm,…)
• In OmniAccess Stellar WLAN Cloud
• Go to the menu:
ssh_connect = 1
ssh_connect = 0
SSH enabled
SSH disabled

<<<PAGE 25>>>
AP LOG COLLECTION – EXPRESS MODE
• Login to the AP web UI: https://<AP_IP> or http://<AP_IP>:8080
1
2
3
4
a
o
r
4
b

<<<PAGE 26>>>
AP LOG COLLECTION – CLOUD MODE
• In OmniVista Cirrus
• Enable « AP web » in the Provisioning Configuration List
• Log in to the AP Web UI: https://<AP_IP> or http://<AP_IP>:8080

<<<PAGE 27>>>
AP LOG COLLECTION – CLOUD MODE
1
2
3a
3b
or

<<<PAGE 28>>>
AP LOG COLLECTION 
3
=
1
2

<<<PAGE 29>>>
OMNIVISTA CIRRUS AUDIT LOG
• In OmniVista Cirrus, view the audit logs:

<<<PAGE 30>>>
PACKET CAPTURE ON STELLAR AP - TCPDUMP
• Step 2
• Transfer the captured file on 
your PC/laptop
• Step 3
• Open and read the file with 
Wireshark 
• Step 1
• CLI connection to the AP with « support » account
• Enter in CLI:
ssudo tcpdump –i
Use the TCPdump tool
br-wan –w
Select the LAN interface « br-wan »
You are listening to the interface br-wan –
which is the wired interface – connecting 
the Stellar AP to the network.
udp port 53 
Select the traffic
UDP port 53 = DNS
Capture the DNS traffic on the wired 
interface of the access point
testcapture.pcap
Save the capture in the 
file « test-capture.pcap »
SFTP tool 
(WinSCP)
SFTP
Test-capture.pcap
Test-capture.pcap

<<<PAGE 31>>>
AIR CAPTURE ON STELLAR AP – EXPRESS MODE
• Click on Start Capture
• Select the Channel
• Enter the TFTP server where the capture will be 
sent
• Option: Filter the capture (MAC, Frame type)
• Start/Stop the capture
• Warning: Capture file limited to 10MB or 5min of capture
• Step 3 – PC/laptop
• Open the file on Wireshark
• Stellar AP captures the surrounding wireless 
traffic on the selected channel
• Step 1 – Cluster web UI
• In “AP” window, click on the AP which will perform 
the Air capture. New tab opens.
• Step 2 – Stellar AP web UI
• In RF Environment, select the Radio to capture

<<<PAGE 32>>>
AIR CAPTURE ON STELLAR AP – CLOUD MODE
• Click on Start Capture
• Select the Channel
• Enter the TFTP server where the capture will be 
sent
• Option: Filter the capture (MAC, Frame type)
• Start/Stop the capture
• Warning: Capture file limited to 10MB or 5min of capture
• Step 3 – PC/laptop
• Open the file on Wireshark
• Stellar AP captures the surrounding wireless 
traffic on the selected channel
• Step 1 – OmniVista Cirrus
• Activate “AP Web” in the provisioning configuration 
menu
• Step 2 – Stellar AP
• Log in
• In RF Environment, select the Radio to capture

<<<PAGE 33>>>
STELLAR AP CONFIGURATION BACKUP – EXPRESS MODE
• Step 2 – Re-create the issue
• In your own setup, “Restore All Configuration” 
using the .tar file.
• Step 2 bis – Analyze the configuration
• Extract the config-pub.tar file.
• Check the configuration offline
• Backup the configuration of one or multiple 
Stellar AP
• Used to re-create the issue
• Shared with the technical support
• Step 1 – Cluster web UI
• In “AP” window, click on “Backup All Configuration”.
• Download the file “pub-config.tar” locally.

<<<PAGE 34>>>
THIRD PARTY ANALYSIS TOOLS

<<<PAGE 35>>>
WIRESHARK
• Monitor and analyze
• Stellar AP network protocols (wired capture)
• DHCP
• Wireless Client protocols (wireless capture)
• EAP, AD/LDAP, RTP, DSCP
• Live capture of packets in the Network
(wired capture)
• Open an Air capture trace 
(wireless capture)

<<<PAGE 36>>>
MISCELLANEOUS TOOLS
• WiFi Analyzer (PC, smartphone)
• Analyze RF environment
• SSID power
• SSID SNR
• Density of SSIDs
• Channels used
• Wireless Air capture (>5 minutes)
• Windows: WiFi card supporting monitor mode
• MacBook: Native
• TFTP and Syslog servers
• Export logs from the Stellar AP
InSSIDer on Windows
WiFi Analyzer
On Android
Wireless Packet
Capture on macOS

<<<PAGE 37>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 38>>>
BASIC TROUBLESHOOTING
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 39>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• The hardware of the Stellar Access Points
• The system of the Stellar Access Points
• The Captive Portal solution
• A cluster in Express mode

<<<PAGE 40>>>
HARDWARE TROUBLESHOOTING

<<<PAGE 41>>>
HARDWARE – LEDS – AP12XX/13XX/14XX/15X1
Single tri-color LED (Red, Blue, Green)
Flashing Green
•
System Running
•
Default SSID broadcasted
DEFAULT SSID
Solid Green
•
System Running
•
Single band working
2.4 GHz
OR
5 GHz
OR
6 GHz
Solid Blue
•
System Running
•
Dual band working
2.4 GHz
AND
5 GHz
Flashing Blue & Red
•
System Running
•
OS upgrading
UPGRADE
Flashing Blue, Red & Green
•
System Running
•
Use for location of AP
LOCATION
Solid Red
•
System startup
STARTUP

<<<PAGE 42>>>
HARDWARE – LEDS – AP1201H
System tri-color LED STATUS (Red, Blue, Green) & PoE status LED PSE
Flashing Green
•
System Running
•
Default SSID broadcasted
DEFAULT SSID
Solid Green
•
System Running
•
Single band working
2.4 GHz
OR
5 GHz
Solid Blue
•
System Running
•
Dual band working
2.4 GHz
AND
5 GHz
Flashing Blue & Red
•
System Running
•
OS upgrading
UPGRADE
Flashing Blue, Red & Green
•
System Running
•
Use for location of AP
LOCATION
Solid Red
•
System startup
STARTUP
Flashing Orange
•
PoE enabled
•
Powered Device offline 
Off
•
PSE disabled
Solid Orange
•
PoE enabled
•
Powered Device online

<<<PAGE 43>>>
HARDWARE – LEDS – AP1251
7 LEDs
RSVR1
•
Unused / Reserved 
RSVR0 Flashing
•
AP Location – Blink mode in OV
ENET1 Solid
•
Ethernet1 Link UP
ENET0 Solid
•
Ethernet0 Link UP
5G Solid
•
5GHz SSID created and running
2.4G Solid
•
2.4GHz SSID created and running
SYS Solid
•
Power ON & System running
SYS Flashing
•
OS loading or upgrading
5 GHz
2.4 GHz
LOCATION
LOADING / 
UPGRADE
RUNNING
ENET1 
UP
ENET0 
UP

<<<PAGE 44>>>
HARDWARE – LEDS – AP1360 SERIES
7 LEDs
SYS Flashing
•
OS Loading or Upgrading
SYS ON
•
Power On – System Running
2.4G ON
•
2.4GHz SSID created and running
5G ON
•
5GHz SSID created and running
ENET0 ON
•
Ethernet0 Link Up
ENET1 ON
•
Ethernet1 Link Up
SFP ON
•
SFP Link Up
PSE ON
•
PSE Enabled
5 GHz
2.4 GHz
LOADING / 
UPGRADE
SFP
ON
ENET1 
UP
ENET0 
UP
RUNNING
PSE
ON

<<<PAGE 45>>>
CLI TROUBLESHOOTING
• Next CLI results can also be found in the Log Collection
• Ex: System Info
support@AP-0E:E0:~$ showsysinfo
Company Name:ALE USA Inc.
SN:SSZ171800139
Device Model:OAW-AP1221
MAC:DC:08:56:00:0E:E0
Country:RW
Software Name:AOS-WNG
Software Version:3.0.7
Hardware Version:1.10
Oid:1.3.6.1.4.1.6486
Part Number:903919-90
Revision:0
…
CLI
Log Collection

<<<PAGE 46>>>
CLI TROUBLESHOOTING
• Log in with support account
• Login: support
• Password: aos2016
• In Enterprise mode, activate SSH login in the AP Group and define a custom password
AP-0E:E0 login: support
Password: aos2016
BusyBox v1.23.2 (2019-10-30 18:50:45 CST) built-in shell (ash)
----------------------------------------------------------------------------
#########  #########  #########  ###        ###            ##      ########
########   ########   ########   ###        ###           ####     #########
###           ###     ###        ###        ###          ##  ##    ###   ###
#########     ###     ######     ###        ###         ###  ###   #######
###     ###     ###        ###        ###         ###  ###   #######
########     ###     #########  #########  #########  ###    ###  ###  ###
#########     ###     ########   ########   ########   ###    ###  ###   ###
Where Everything Connects
----------------------------------------------------------------------------

<<<PAGE 47>>>
HARDWARE DIAGNOSTIC
• System and Firmware
support@AP-0E:E0:~$ showsysinfo
Company Name:ALE USA Inc.
SN:SSZ171800139
Device Model:OAW-AP1221
MAC:DC:08:56:00:0E:E0
Country:RW
Software Name:AOS-WNG
Software Version:3.0.7
Hardware Version:1.10
Oid:1.3.6.1.4.1.6486
Part Number:903919-90
Revision:0
Essid Prefix:mywifi
Cluster Describe:AP Group
Website:http://www.al-enterprise.com
Legal:Copyright © 1995-2019 ALE USA Inc.   ALL RIGHTS RESERVED WORLDWIDE
Describe:HOS 30
Serial Number
Device Model 
MAC Address
Country code
Software and Hardware version
support@AP-0E:E0:~$ showver
3.0.7.20
support@AP-0E:E0:~$ iwpriv wifi0 getCountry
wifi0      getCountry:FR

<<<PAGE 48>>>
STELLAR AP MODE
• Get the mode of the Stellar AP
• Get additional information
support@AP-0E:E0:~$ getmode
CLUSTER
Mode Express
Mode Enterprise
support@AP-0E:E0:~$ show_cluster
mac                  ip         prio  state  role auth  name       version    ptype  model
dc:08:56:00:0e:e0    10.7.0.5    0      3     1     1   AP-0E:E0   3.0.7.20   43     OAW-AP1221
List of Stellar APs in the cluster
IP address of the OmniVista server
root@AP-83:60:~# getmode
OV
support@AP-83:60:~# getovinfo
10.130.5.50
Mode Cloud
root@AP-83:60:~# getmode
OVNG

<<<PAGE 49>>>
SYSTEM TROUBLESHOOTING

<<<PAGE 50>>>
SYSTEM DIAGNOSTIC
• Restart reason
• Why did the AP reboot?
• Check in the AP log collection:
• Date
• Check Stellar AP system time and date
• Check Stellar AP synchronization to the NTP server. 
Is it the same time ?
• Uptime
• Check Stellar AP uptime
• Unexpected Stellar AP reboot?
support@AP-0E:E0:~$ date
Sun Dec  1 21:07:37 2019
support@AP-0E:E0:~$ uptime
21:10:20 up 11 days, 17:45, load average: 0.47, 0.37, 0.40

<<<PAGE 51>>>
SYSTEM - CPU AND MEMORY UTILIZATION
• Memory and CPU usage – Linux based command
• High CPU utilization
• Impact performances of the Stellar AP: speed, features not working as intended
support@AP-0E:E0:~$ top
Mem: 160532K used, 83748K free, 11512K shrd, 4624K buff, 25344K cached
CPU:   4% usr   7% sys   0% nic  87% idle   0% io   1% irq   0% sirq
Load average: 0.37 0.48 0.57 1/130 16561
PID    PPID USER    STAT     VSZ %VSZ %CPU   COMMAND
5398       1 root     S     6168   3%   0%   /usr/sbin/eag_app -c
16635       1 root     S    10900   4%   0%   /usr/sbin/drm
10570   10557 root     S     9820   4%   0%   /usr/bin/echo.fcgi
11073       1 root     S     5412   2%   0%   /usr/bin/nbm
16156   19046 support  R     1316   1%   0%   top
29758       2 root     SW       0   0%   0%   [kworker/3:1]
8743       2 root     SW       0   0%   0%   [kworker/0:2]
17135       1 root     S    12272   5%   0%   bg-s -q -X
6173       1 root     S     7056   3%   0%   /sbin/cluster_mgt -I 100 -p 0
6174       1 root     S     6372   3%   0%   /sbin/cluster_cor -I 100 -p 0
1831       1 root     S     5908   2%   0%   /sbin/adme
6710       1 root     S <   4688   2%   0%   wam -g /var/run/wam/global -d -f /var
3786       1 root     S     3188   1%   0%   /usr/sbin/snmpd -Lf /dev/null -f
10588       1 mosquitt S     3132   1%   0%   /usr/sbin/mosquitto -c /etc/mosquitto
2127       1 root     S     1768   1%   0%   /usr/bin/dnsrd
5476       1 root     S     1760   1%   0%   /sbin/configd
Global Memory usage
Global CPU usage
Processes list

<<<PAGE 52>>>
SYSTEM – HIGH CPU UTILIZATION 
• Most common causes for high CPU utilization
• Abnormal process
• Process infinite loop →Probably software issue
• Process extensive calculations →Probably due to extensive logs/traces
• Stellar AP under DoS attack
• Identify the process causing high CPU usage
• Each process is a task running on the CPU
• Share these processes with the Technical Support when opening a ticket
support@AP-0E:E0:~$ top
Mem: 160532K used, 83748K free, 11512K shrd, 4624K buff, 25344K cached
CPU:   4% usr   7% sys   0% nic  87% idle   0% io   1% irq   0% sirq
Load average: 0.37 0.48 0.57 1/130 16561
PID     PPID   USER   STAT     VSZ    %VSZ     %CPU     COMMAND
398       1   root    S      6168     3%       0%      /usr/sbin/eag_app -c
16635
1   root    S     10900     4%      81%
/usr/sbin/drm
10570   10557   root    S      9820     4%       0%      /usr/bin/echo.fcgi
11073       1   root    S      5412     2%       0%      /usr/bin/nbm
Memory usage
CPU usage
Process name
Process ID

<<<PAGE 53>>>
SYSTEM – PROCESS STATUS
• Process Status
• Processes list
• Specific process
• Check the Status of the process
• OK: R (Running), S (Interruptible Sleep)
• Issue: X (Dead) and Z (Zombie process)
• Too many Zombie processes will consume large portion of memory
support@AP-0E:E0:~$ ps | grep cluster
3593  support  1304 S    grep cluster
6173  root     7056 S    /sbin/cluster_mgt -I 100 -p 0
6174  root     6372 S    /sbin/cluster_cor -I 100 -p 0
support@AP-0E:E0:~$ ps
PID  USER     VSZ   STAT   COMMAND
1  root    1312     S    /sbin/procd
2  root      0     SW   [kthreadd]
3  root      0     SW   [ksoftirqd/0] ………

<<<PAGE 54>>>
CAPTIVE PORTAL TROUBLESHOOTING

<<<PAGE 55>>>
CAPTIVE PORTAL CLIENT 
• List of all clients on a wireless interface
• Note: « eag » process related to the Captive Portal
• Check List:
• Is the client authenticated on the Captive Portal? →Entry in the list
• For how long is the client connected? →SessionTime
• Does the client send/receive data to the network? →OutputFlow and InputFlow
support@AP-83:60:~$ eag_cli show user all
user num : 1
ID      UserName
UserIP
UserMAC
SessionTime
OutputFlow
InputFlow
AuthType
ESSID
1       guest0       10.7.0.39   D4:6E:0E:18:60:38   0:00:20       489232        30632
PORTAL     guest0

<<<PAGE 56>>>
CAPTIVE PORTAL RELATED LOGS
support@AP-83:60:~$ cat /var/log/eag.log
[2019-12-03 07:59:32]:  eag_stamsg.c:1132:stamsg_recieive usermac D4:6E:0E:18:60:38,userip 0.0.0.0, OP: 0
…
[2019-12-03 07:59:32]:  eag_stamsg.c:510:Receive USER_ADD msg  status:NotAuthed, apmac: 
DC:08:56:09:83:60,usermac:D4:6E:0E:18:60:38,userip 0.0.0.0, wlan service name:guest0, ssid:guest0 ,vlanid:20, 
ARP name: __guest0, redirect URL: https://ov2500-upam-cportal.al-
enterprise.com:443/portal_UI/c0212f425f33993753226f9ddeb55bd1/login.html?mac=D46E0E186038redirect ipv6 
URL:https://ov2500-upam-cportal.al-
enterprise.com:443/portal_UI/c0212f425f33993753226f9ddeb55bd1/login.html?mac=D46E0E186038
[2019-12-03 07:59:33]:  appconn.c:1103:eag_ipinfo_get before userip=10.7.0.39
[2019-12-03 07:59:33]:  appconn.c:1112:eag_ipinfo_get after 
userip=10.7.0.39,usermac=D4:6E:0E:18:60:38,interface=br-vlan20
[2019-12-03 07:59:33]:  appconn.c:1115:appconn_check_is_conflict eag_ipinfo_get userip 10.7.0.39, 
interface(br-vlan20), usermac(D4:6E:0E:18:60:38)
[2019-12-03 07:59:33]:  eag_ipinfo.c:1457:[ip -6 neigh |grep d4:6e:0e:18:60:38|grep br-vlan20 |awk '{print 
$1}' |grep fe80::]:[addr:]
[2019-12-03 07:59:33]:  appconn.c:355:user local llink address  is null
[2019-12-03 07:59:33]:  eag_redir.c:3011:user ip = 10.7.0.39
[2019-12-03 07:59:33]:  eag_redir.c:3055:reget local link addr mac:d4:6e:0e:18:60:38 bridge:br-vlan20
[2019-12-03 07:59:33]:  eag_ipinfo.c:1457:[ip -6 neigh |grep d4:6e:0e:18:60:38|grep br-vlan20 |awk '{print 
$1}' |grep fe80::]:[addr:]
[2019-12-03 07:59:33]:  appconn.c:355:user local llink address  is null
[2019-12-03 07:59:33]:  eag_ins.c:7349:the custon file  not exist
[2019-12-03 07:59:33]:  eag_redir.c:1774:PortalRedirect___UserIP:10.7.0.39,UserMAC:D4-6E-0E-18-60-38,ApMAC:DC-
08-56-09-83-60,SSID:guest0,NasIP:10.7.0.103,Interface:ath12,NasID:,redirURL:https://ov2500-upam-cportal.al-
enterprise.com: 443/portal_UI/c0212f425f33993753226f9ddeb55bd1 
/login.html?mac=D46E0E186038&url=http://www.msftconnecttest.com/connecttest.txt
Client first connection to 
the Captive Portal. 
Client IP address unknown.
Redirection URL
can not be sent.
Client information gathered.
Client IP address retrieved.
Stellar AP sends redirection 
URL to the client.

<<<PAGE 57>>>
CLUSTER TROUBLESHOOTING
EXPRESS MODE

<<<PAGE 58>>>
CLUSTER CONFIGURATION - ROLE
• Check the status of the PVC in the cluster
• Is a PVC found in the cluster? Is it supposed to be 
this PVC?
• Check the AP role and status in the cluster
• Is the Stellar AP supposed to be the Primary Virtual 
Controller?
• Is the Stellar AP running in the cluster?
support@AP-0E:E0:~$ cluster_mgt –x show=self
ClusterID
MAC                 role  priority       status
100        dc:08:56:00:0e:e0   PVC
002b03000ee0
RUN
support@AP-0E:E0:~$ cluster_mgt –x show=pvc
ClusterID
MAC                 role   priority       status
100         dc:08:56:00:0e:e0
PVC    002b03000ee0   RUN

<<<PAGE 59>>>
CLUSTER CONFIGURATION – AP LIST AND PROCESS
• Check the status of all AP members in the cluster
• Are all the AP found in the cluster? 
• Check the « cluster » process on the AP
• Are both processes running?
• Two existing « cluster_mgt » threads indicates abnormal behavior (one running, one sleeping) 
support@AP-0E:E0:~$ show_cluster
mac                 ip         prio state role auth name      version    ptype model
dc:08:56:00:0e:e0   10.7.0.5   0    3     1    1    AP-0E:E0  3.0.7.20   43    OAW-AP1221
dc:08:56:03:e7:80   10.7.0.6   0    3     2    1    AP-E7:80  3.0.7.20   43    OAW-AP1301
support@AP-0E:E0:~$ ps | grep cluster
6173 root      7056 S    /sbin/cluster_mgt -I 100 -p 0
6174 root      6372 S    /sbin/cluster_cor -I 100 -p 0
24942 support   1304 S     grep cluster

<<<PAGE 60>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 61>>>
WIRELESS TROUBLESHOOTING
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE

<<<PAGE 62>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Troubleshoot wireless issues
• Understand wireless troubleshooting 
through use cases

<<<PAGE 63>>>
WIRELESS CONFIGURATION
• Check wireless configuration
• Check List
• SSID broadcasted on the selected radio(s)?
• Transmission Power as selected in the RF profile?
• Encryption activated?
• BSSID is present?
• If there is no MAC address for « Access Point », 
the SSID is not broadcasted
athXYY
X = 0 : 2.4GHz Radio
X = 1 : 5GHz Radio
X = 2 : 6GHz Radio
Y = [1…16] : SSID ID
support@AP-0E:E0:~$ iwconfig
gre0      no wireless extensions.
...
ath001    IEEE 802.11ng  ESSID:"employee0"
Mode:Master  Frequency:2.437 GHz Access Point: DC:08:56:09:83:61
Bit Rate:192 Mb/s   Tx-Power=17 dBm
RTS thr:off   Fragment thr:off
Encryption key:CE75-5424-2E7F-9C74-B8AD-83F4-14EC-03A
Power Management:off
Link Quality=94/94  Signal level=-48 dBm  Noise level=-95 dBm
Rx invalid nwid:12078  Rx invalid crypt:0  Rx invalid frag:0
Tx excessive retries:0  Invalid misc:0   Missed beacon:0
ath101    IEEE 802.11ac  ESSID:"employee0"
Mode:Master  Frequency:5.5 GHz  Access Point: DC:08:56:09:83:69
Bit Rate:1.7333 Gb/s   Tx-Power=24 dBm
RTS thr:off   Fragment thr:off
Encryption key:3F97-C66B-A3DC-2714-DE7C-1986-072E-5356 [2]
Power Management:off
Link Quality=94/94  Signal level=-97 dBm  Noise level=-95 dBm
Rx invalid nwid:13766  Rx invalid crypt:0  Rx invalid frag:0
Tx excessive retries:0  Invalid misc:0   Missed beacon:0

<<<PAGE 64>>>
RF PROFILE CONFIGURATION
• Check the RF configuration applied on
the AP
• Check List:
• Global parameters: same as configured?
• Band Steering
• Load Balance
• Scanning
• Country Code
• Air Time Fairness
• Per Radio parameters: same as configured?
• Channel selection: auto or manual?
• Channel Width?
• Power selection: auto  or manual?
support@AP-0E:E0:~$ cat /tmp/config/rfprofile.conf
{
"RFService":[
{
"bandSteering":"enable",
"bandSteeringForce5g":"disable",
"LoadBalance":"enable",
"backgroundScanning":"enable",
"scanningEnhance":"disable",
"countryCode":"FR",
"scanningInterval":20,
"scanningDuration":50,
"voiceVedioAwareness":"disable",
"airtimeFairnessAt2G":"disable",
"airtimeFairnessAt5G":"disable",
"perBandInfo":{
"2.4G":{
"band":"enable",
"channelSetting":"AUTO",
"channelWidth":20,
"autoChannelWidth":"enable",
"powerSetting":"AUTO",
"shortGuardInterval":"enable",
"signalStrengthThreshold":0,
"roamingSignalStrengthThreshold":0,

<<<PAGE 65>>>
WIRELESS INTERFACE CONFIGURATION
• Check the power of transmission used for the SSID in 
2.4GHz.
• Use « iwconfig » to identify the wireless 
interface to monitor: 
• Check the channel used for the SSID in 2.4GHz
support@AP-0E:E0:~$ iwlist ath001 channel
ath01     57 channels in total; available frequencies :
Channel 01 : 2.412 GHz
Channel 02 : 2.417 GHz
Channel 03 : 2.422 GHz
Channel 04 : 2.427 GHz
Channel 05 : 2.432 GHz
Channel 06 : 2.437 GHz
Channel 07 : 2.442 GHz
Channel 08 : 2.447 GHz
Channel 09 : 2.452 GHz
Channel 10 : 2.457 GHz
Channel 11 : 2.462 GHz
Channel 12 : 2.467 GHz
Channel 13 : 2.472 GHz
Current Frequency:2.437 GHz (Channel 6)
support@AP-0E:E0:~$ iwlist ath001 txpower
ath01     8 available transmit-powers :
0 dBm         (1 mW)
5 dBm         (3 mW)
7 dBm         (5 mW)
9 dBm         (7 mW)
11 dBm        (12 mW)
13 dBm        (19 mW)
15 dBm        (31 mW)
17 dBm        (50 mW)
Current Tx-Power=17 dBm
(50 mW)
ath001 for the employee0 SSID in 2.4GHz

<<<PAGE 66>>>
WIRELESS TROUBLESHOOTING
USE CASE

<<<PAGE 67>>>
AP CAN’T GENERATE HEAT MAP (1/2)
Reminder: AP needs a wireless interface to send/receive a wireless signal 
and so, generate a Heat Map.
• 1) There is no Heat Map generated on OmniVista. Check if the AP has a wireless interface:
support@AP-83:60:~$ iwconfig
gre0      no wireless extensions.
ath01-20  no wireless extensions.
ath11-untag  no wireless extensions.
br-wan    no wireless extensions.
wifi0     no wireless extensions.
eth0-20   no wireless extensions.
ath02-untag  no wireless extensions.
sit0      no wireless extensions.
ath11-20  no wireless extensions.
ath102   IEEE 802.11ac  ESSID:"guest0"
Mode:Master  Frequency:5.3 GHz  Access Point: DC:08:56:00:0E:E2
Bit Rate:1.7333 Gb/s   Tx-Power=3 dBm
RTS thr:off   Fragment thr:off
Power Management:off
Link Quality=94/94  Signal level=-31 dBm  Noise level=-95 dBm
Rx invalid nwid:536  Rx invalid crypt:0  Rx invalid frag:0
Tx excessive retries:0  Invalid misc:0   Missed beacon:0
Wireless interface exists 
for the 5GHz radio

<<<PAGE 68>>>
AP CAN’T GENERATE HEAT MAP (2/2)
Reminder: To create a Heat Map for a specific radio (ex:2.4GHz), a wireless 
interface must exist for this radio.
• 2) Heat Map can’t be created for the 2.4GHz radio. Check AP WLAN configuration:
• Heat Map can’t be generated for the 2.4GHz radio. Select the 5GHz radio:
WLAN configuration only 
for the 5GHz radio
No Heat Map for 2.4GHz.
Select the 5GHz radio.

<<<PAGE 69>>>
REASONS FOR ROAMING FAILURE
• APs must be seen as neighbors 
•
• No Roaming from an untagged VLAN to a tagged VLAN
• RSSI too low between source AP and destination AP
support@AP-83:60:~$ adme show
mac                             ip               ov_ip             tenantId    state     name        version   radiocnt  radioid
channel   rssi    txpower
34:e7:0b:02:c8:70   10.7.4.103       10.130.5.54                       0      AP-C8:70    3.0.7.20    2           0            1
55      17
0            0             0        22
dc:08:56:09:83:60   10.7.0.103       10.130.5.50                       0      AP-83:60    3.0.7.20     2          0             6            64       17
1            48           79       19
Neighbor AP
Bad signal 
from neighbor
support@AP-83:60:~$ adme show
mac                             ip                    ov_ip        tenantId    state     name        version   radiocnt  radioid
channel   rssi    txpower
34:e7:0b:02:c8:70   10.7.4.103       10.130.5.54                       0      AP-C8:70    3.0.7.20    2           0            1
55       17
0            0               0       22
dc:08:56:09:83:60   10.7.0.103       10.130.5.50                       0      AP-83:60    3.0.7.20     2          0             6            15       17
1            48            19       19
SSID “employee0”
Tagged VLAN 20
SSID “employee0”
Untagged VLAN 20

<<<PAGE 70>>>
ROAMING - NEIGHBOR AP
• In some cases, Stellar APs are geographical
neighbors but can’t see each other
(i.e: radio waves blocked by corridor 
with right angles,…).
• The client context can't be shared. No roaming.
• Solution:
• On both AP, add statically the neighbor Stellar AP
from the list of known AP.
• The client context can be shared through 
the LAN and the client can roam.
• Select the AP in the Device Catalog > Action
> View > Neighbor APs. In the new window,
click on Manage neighbor to add a new one. 
No client 
context 
sharing

<<<PAGE 71>>>
CHECK ROAMING SUCCESS
• From AP Log collection, open wam.log
• Search for: « L3 roaming–start », « L3 roaming–success », « L2 roaming–success »
• L2 roaming:
• L3 roaming

<<<PAGE 72>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 73>>>
CLIENT TROUBLESHOOTING
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE

<<<PAGE 74>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Troubleshoot client issues in a Stellar 
solution
• Understand client troubleshooting through 
use cases

<<<PAGE 75>>>
CLIENT LIST
• List all the clients associated to the AP
• Check List:
• Client in the correct VLAN? Client got an IP address in the correct subnet? →VLAN and IPv4
• Stability of the client connection. What is the uptime value of the client? →OnlineTime
• Client receives/transmits data with the Stellar AP? →RX and TX counters
• Correct authentication method used by the client? →AUTH
• Correct Access Role Profile assigned to the client? →Final_role
support@AP-83:60:~$ ssudo sta_list
SSID:employee0
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX            FREQ    AUTH    Final_role                     VLANID  TUNNELID  FARENDIP
d4:6e:0e:18:60:38  10.7.0.39
821
282142 59061933 2.4GHz  802.1X
__employee0
20
0
SSID:employee0
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX            FREQ    AUTH    Final_role                     VLANID  TUNNELID  FARENDIP
SSID:guest0
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX            FREQ    AUTH    Final_role                     VLANID  TUNNELID  FARENDIP
SSID:guest0
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX            FREQ    AUTH    Final_role                     VLANID  TUNNELID  FARENDIP

<<<PAGE 76>>>
CLIENT OS TYPE
• Check the OS type of the clients on the AP
• Check List:
• Is the client listed? No connectivity issue?
• Identification of the client: IP address, Mac address, Hostname.
• Verification of the operating system (ostype).
support@AP-83:60:~$ cat /proc/kes_syslog | grep tid
…
2019-12-09 01:19:55 User tid[1638] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] : [TID_DHCP_PROTOCOL] ip:[10.7.0.41], mac:[d4:6e:0e:18:60:38], 
hostname:[], ostype:[iOS]
2019-12-09 01:19:55 User tid[1638] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] : [TID_DHCP_PROTOCOL] ip:[], mac:[d4:6e:0e:18:60:38], 
hostname:[StellarClient0], ostype:[iOS]
2019-12-09 01:19:55 User tid[1638] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] : [TID_DHCP_PROTOCOL] ip:[10.7.0.41], mac:[d4:6e:0e:18:60:38], 
hostname:[StellarClient0], ostype:[iOS]

<<<PAGE 77>>>
STELLAR AP TO CLIENT ATTRIBUTES
• List the detailed attributes that AP sends to the client
• Check List:
• Same parameters as the
sta_list command →IP address, VLAN, 
Association Time, AccessRole Profile assigned,…
• Depending on the authentication method used 
(802.1X, MAC, Captive Portal),
does the client receive the correct parameters
from the Stellar AP?
• Correct Captive Portal URL?
• Is the Authentication a success?
• Correct Access Role Profile after authentication success?
support@AP-83:60:~$ ssudo wam_debug sta_list
{
"status": "Success!!!",
"wlanServiceData": [
{
"iface": "ath02",
"ssid": "guest0",
"freq": "2.4GHz",
"security": "Open",
"wlanService": "guest0",
"staData": [
{
"staMAC": "d4:6e:0e:18:60:38",
"staIP": "10.7.0.39",
"staGlobalIPv6": "::",
"staLocalIPv6": "::",
"associationTime": 53,
"mappingType": 0,
"assignedVLAN": 20,
"assignedAR": "__guest0",
"assignedPL": "",
"macAuthResult": "SUCCESS",
"ARFromMACAuth": "",
"PLFromMACAuth": "",
"redirectURLFromMACAuth": "https:\/\/ov2500-upam-cportal.al-enterprise.com:443…”
"ARFrom8021xAuth": "",
"PLFrom8021xAuth": "",
"redirectURLFrom8021xAuth": "",
"CPAuthResult": “SUCCESS",
"ARFromCPAuth": “__guest0",
"PLFromCPAuth": "",

<<<PAGE 78>>>
LIST CLIENTS ON A WIRELESS INTERFACE 
• A list of all clients on a specific wireless interface
• Check List:
• Does the signal receive by the client has enough strength? →RSSI, MINRSSI, MAXRSSI
• For VoWLAN deployment in 802.11ac: RSSI must be -67dBm (or better). Meaning RSSI ≥ 29 
•
Is the signal-to-noise too high and degrades the data transmission? →SNR
• For VoWLAN deployment in 802.11AC: SNR ≥ 25
support@AP-83:60:~$ wlanconfig ath12 list
ADDR               AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE  TXSEQ  RXSEQ  CAPS XCAPS        ACAPS     ERP    STATE MAXRATE(DOT11) HTCAPS VHTCAPS 
ASSOCTIME    IEs   MODE                   PSMODE RXNSS TXNSS
d4:6e:0e:18:60:38    1   48 390M    433M     57
55
65
2      0        65535    Es    OI                  0          b          0             WPS            2gGR 00:10:43  WME 
IEEE80211_MODE_11AC_VHT80   0 1 1 Minimum Tx Power              : 5
Maximum Tx Power           : 18
HT Capability                  : Yes
VHT Capability                : Yes
MU capable                     : No
SNR
: 57
Operating band               : 5GHz
Current Operating class   : 0
Supported Rates              : 12  18  24  36  48  72  96  108

<<<PAGE 79>>>
RSSI VALUES
RSSI
dBm
10
-86
11
-85
12
-84
13
-83
14
-82
15
-81
16
-80
17
-79
18
-78
19
-77
20
-76
RSSI
dBm
21
-75
22
-74
23
-73
24
-72
25
-71
26
-70
27
-69
28
-68
RSSI
dBm
29
-67
30
-66
31
-65
32
-64
33
-63
34
-62
35
-61
36
-60
37
-59
38
-58
39
-57
40
-56
41
-55
42
-54
43
-53
Bad - too many packets loss
KO: Voice or real-time applications
OK: Mail or Internet applications
OK  
For most applications
Quality impact for voice 
and real-time applications
Perfect
Recommendation for voice 
and real-time application

<<<PAGE 80>>>
CLIENT ACCESS LOGS
• Check the access logs of a specific client
• Check List:
• Check association / disassociation exchange between Stellar AP and client
• Check the disassociation reason in case of an unexpected disconnection of the client.
support@AP-83:60:~$ cat /proc/kes_syslog | grep <client-MAC>
support@AP-83:60:~$ cat /proc/kes_syslog | grep d4:6e:0e:18:60:38
2019-12-03 05:27:21 User tid[1725] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [TID_DHCP_PROTOCOL] ip:[10.7.0.39], mac:[d4:6e:0e:18:60:38], hostname:[], ostype:[]
2019-12-03 05:27:24 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [MLME] [ieee80211_recv_disassoc] [ath12(dc:08:56:09:83:6a)] [d4:6e:0e:18:60:38] 
Received Disassoc with reason 8(OS moved the client to another AP using non-aggressive load balance), recv rssi 63, min rssi 55, max rssi 64    Client manual disconnection
2019-12-03 05:27:24 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [MLME] [ieee80211_mlme_recv_disassoc] [ath12(dc:08:56:09:83:6a)] [d4:6e:0e:18:60:38] 
Call MLME indication handler to deliver disassoc event and free the sta node
2019-12-03 05:27:24 Network netifd[1530] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : mvlan remove user mac success: d4:6e:0e:18:60:38
2019-12-03 05:27:24 User um[1686] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : Recv the  wam module  notify  data user  [d4:6e:0e:18:60:38] status [0]  AuthType [OPEN} 
Portalname []  SSID  is [guest0]  ipv6 is [] 8021x user name:[]
…
2019-12-03 05:39:42 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [AUTH] [mlme_recv_auth_ap] [ath02(dc:08:56:09:83:62)] [d4:6e:0e:18:60:38] Recv a auth 
frame with algorithm 0(IEEE80211_AUTH_ALG_OPEN) seq 1
2019-12-03 05:39:42 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [AUTH] [ieee80211_send_auth] [ath02(dc:08:56:09:83:62)] [d4:6e:0e:18:60:38] Send auth 
response frame to the client, status 0(SUCCESS), seq 2
2019-12-03 05:39:42 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [ASSOC][ieee80211_ioctl_setmlme] [ath02(dc:08:56:09:83:62)] [d4:6e:0e:18:60:38] Send 
assoc resp for pmf client from WAM
→Client manual connection on the AP

<<<PAGE 81>>>
CLIENT TROUBLESHOOTING
USE CASE

<<<PAGE 82>>>
CLIENT CANNOT SEE THE SSID
• 1) Is the SSID broadcasted by the AP?
• 2) Which radio does the client support? Compatible with the SSID broadcasted?
• 3) Country Code of the AP? Supported by the client?
• Wrong country code: 
Set manually a compatible channel on the AP in RF profile:
support@AP-83:60:~$ iwconfig
…
ath02     IEEE 802.11ng  ESSID:"guest0"
Mode:Master  Frequency:2.437 GHz  Access Point: DC:08:56:00:0E:E2
Bit Rate:192 Mb/s   Tx-Power=3 dBm
RTS thr:off   Fragment thr:off
Power Management:off
Link Quality=94/94  Signal level=-46 dBm  Noise level=-95 dBm
Rx invalid nwid:1301  Rx invalid crypt:0  Rx invalid frag:0
Tx excessive retries:0  Invalid misc:0   Missed beacon:0
SSID “guest0” broadcasted 
on the AP in 2.4GHz

<<<PAGE 83>>>
CLIENT FAILS TO GET AN IP ADDRESS (1/2)
• 1) Capture DHCP messages on the client (wireshark) and the AP (tcpdump):
• Open trace.pcap with wireshark:
• Analyze DHCP packets. Packet loss between AP and client?
support@AP-83:60:~$ cd /tmp
support@AP-83:60:~$ tcpdump –i eth0 –s0 –w trace.pcap
Storage location of the trace
Capture all traffic on the LAN interface

<<<PAGE 84>>>
CLIENT FAILS TO GET AN IP ADDRESS (2/2)
• 2) Client assigned to the correct VLAN?
• Client supposed to get an IP in the scope of the VLAN 20?
• Does the Final_role filter DHCP traffic?
support@AP-83:60:~$ ssudo sta_list
SSID:employee0
STA_MAC                 IPv4            IPv6                    OnlineTime        RX         TX        FREQ    AUTH     Final_role                     VLANID  TUNNELID  FARENDIP
SSID:employee0
STA_MAC                 IPv4            IPv6                    OnlineTime        RX         TX        FREQ    AUTH     Final_role                     VLANID  TUNNELID  FARENDIP
d4:6e:0e:18:60:38  10.7.0.39                                      27              19409   36925     5GHz     802.1X    __employee0                     20         0

<<<PAGE 85>>>
CLIENT FREQUENT DISCONNECTION FROM THE AP (1/3)
• 1) AP transmit power is too low?
• Check AP transmit power:
• Check client RSSI:
support@AP-83:60:~$ iwlist ath11 txpower
ath11     6 available transmit-powers :
…
Current Tx-Power=3 dBm        (1 mW)
Transmit power set to minimum value
support@AP-83:60:~$ wlanconfig ath11 list
ADDR               AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE  TXSEQ  RXSEQ  CAPS XCAPS        ACAPS     ERP    STATE MAXRATE(DOT11) HTCAPS VHTCAPS 
ASSOCTIME    IEs   MODE                   PSMODE RXNSS TXNSS
d4:6e:0e:18:60:38    1   48 390M    433M     16      14        17        2      0        65535    Es    OI                  0          b          0             WPS            2gGR 00:10:43  
WME IEEE80211_MODE_11AC_VHT80   0 1 1 Minimum Tx Power              : 5
Maximum Tx Power           : 3
HT Capability                  : Yes
VHT Capability                : Yes
MU capable                     : No
SNR
: 30
Operating band               : 5GHz
Current Operating class   : 0
Supported Rates              : 12  18  24  36  48  72  96  108
Bad signal quality.
High probability of disconnection.
Large amount of Noise.
But above recommendation.

<<<PAGE 86>>>
CLIENT FREQUENT DISCONNECTION FROM THE AP (2/3)
• Increase AP transmit power in RF profile:

<<<PAGE 87>>>
CLIENT FREQUENT DISCONNECTION FROM THE AP (3/3)
• Modify RSSI threshold value in RF profile:
• 3) Wireless capture and logs
• AP deny the client?
• Check disassociation/deauthentication packets?
• Air Capture on the 5GHz radio
• Access Logs:
• 2) High RSSI Threshold?
• Cause client to disconnect if their RSSI is below the 
Threshold
support@AP-83:60:~$ cat /tmp/config/rfprofile.conf
…
"5G_all":{
"band":"enable",
"channelSetting":"AUTO",
"channelWidth":80,
"autoChannelWidth":"enable",
"globalChannelWidth":20,
"powerSetting":"1",
"shortGuardInterval":"enable",
"signalStrengthThreshold":70,
“roamingSignalStrengthThreshold":0,
"powerValMax":"0",
"powerValMin":"0",
"radioMode":"normal",
"scanDuration":"normal",
"Gain":"4",
"chainmask":15,
"clientAwareness":"disable"
}
Threshold too high.
Decrease the value.
support@AP-83:60:~$ cat /proc/kes_syslog | grep <client-MAC>

<<<PAGE 88>>>
802.1X AUTHENTICATION NOT WORKING (1/3)
• 1) On Client side:
• Check:
• Username and password
• Encryption type
• Security type/key
• Certificate on client (if any)
Wi-Fi Client
Radius 
Server
Stellar AP
802.1X

<<<PAGE 89>>>
802.1X AUTHENTICATION NOT WORKING (2/3)
• Correct Radius server attached to the SSID?
• 2) On AP side:
• Compare Radius configuration to Radius server
• IP and ports
• Shared Secret key
support@AP-83:60:~$ cat /var/config/AAA_server.conf
"UnifiedAAAServer":[
{
"accountingPort":1813,
"hostName":null,
"retries":2,
"ipAddress":"10.130.5.250",
"name":“radius",
"type":"Radius",
"timeout":5,
"authenticationPort":1812,
"secret":"a006a626d46117ba078e0ca9ffd5b859"
}  ]
support@AP-83:60:~$ cat /var/config/wlanservice.conf
"WLANService":[
{
"name":"employee0",
"essid":"employee0",
…
"securityLevel":"Enterprise",
"encryptionType":"wpa2-aes",
…
"aaaProfile":"employee0",
support@AP-83:60:~$ cat /var/config/AAA_profile.conf
"name":"employee0",
"macOpts":{
…
"e02d1xAccServer":{
"secondaryServer":null,
"callingStationIdType":"MAC",
"syslogUpdPort":null,
"syslogIpAddress":null,
"primaryServer":“radius“,

<<<PAGE 90>>>
802.1X AUTHENTICATION NOT WORKING (3/3)
• Sample of FreeRadius server configuration:
• 3) On Radius server side:
• Compare Radius configuration and database 
to client and AP configuration:
• Username/password
• Shared Secret
• Radius client IP
• Radius station IP (IP address of the Stellar AP)
• Certificate
• Authentication and accounting ports
• Radius service enabled?
• Firewall allows authentication and accounts ports?

<<<PAGE 91>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 92>>>
NETWORK TROUBLESHOOTING
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE

<<<PAGE 93>>>
Upon completion of this module, 
you will be able to:
LESSON SUMMARY
• Network Troubleshooting
•
Troubleshoot network related issues in a Stellar 
solution
•
Understand network troubleshooting through use 
cases

<<<PAGE 94>>>
IP CONFIGURATION
• IP configuration of the LAN interface of the AP
• Check the IP address and mask of the LAN interface
• Traffic exchanged between the AP and the network? →Sent/Received packets 
• Check the Stellar AP routes
• What is the gateway of the default route? Is it the correct default route?
support@AP-83:60:~$ ifconfig br-wan
br-wan    Link encap:Ethernet  HWaddr DC:08:56:09:83:60
inet addr:10.7.0.103 Bcast:10.7.0.127  Mask:255.255.255.224
inet6 addr: fe80::de08:56ff:fe09:8360/64 Scope:Link
UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
RX packets:688102 errors:0 dropped:0 overruns:0 frame:0
TX packets:391717 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:65241621 (62.2 MiB)  TX bytes:77268512 (73.6 MiB)
support@AP-83:60:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.7.0.126
0.0.0.0             UG    0      0        0   br-wan
10.7.0.96       0.0.0.0         255.255.255.224    U      0      0        0   br-wan
10.7.0.126      0.0.0.0        255.255.255.255   UH     0      0        0   br-wan

<<<PAGE 95>>>
NETWORK TROUBLESHOOTING TOOLS
• Ping another network device from the AP
• Ex: The Stellar AP can ping the OmniVista server
• What about the gateway, NTP/DHCP/DNS servers, firewall? 
• Check the network trace route
• Check the path taken by the traffic.
• Is the traffic send to the gateway first?
• Need to adjust the routing protocols? 
support@AP-83:60:~$ ssudo ping 10.130.5.50
PING 10.130.5.50 (10.130.5.50): 56 data bytes
64 bytes from 10.130.5.50: seq=0 ttl=62 time=0.818 ms
64 bytes from 10.130.5.50: seq=1 ttl=62 time=0.950 ms
64 bytes from 10.130.5.50: seq=2 ttl=62 time=0.587 ms
support@AP-83:60:~$ ssudo traceroute 10.130.5.50
1  10.7.0.126 (10.7.0.126)  0.854 ms  0.700 ms  0.611 ms

<<<PAGE 96>>>
NEIGHBORING APS
• Check the neighbor APs seen by the Stellar AP
• Look for the Stellar APs managed by the same OV or in the same cluster
• If a geographic neighbor : 
• Is not seen, move it closer or increase it’s transmission power.
• Is seen with a weak power signal (RSSI), move it or increase it’s transmission power.
• RSSI < 20 is considered bad signal
• Roaming issue (client disconnection) if the Neighbor AP is not seen or the signal is too weak
support@AP-83:60:~$ adme show
mac                             ip               ov_ip             tenantId    state     name        version   radiocnt  radioid
channel   rssi    txpower
34:e7:0b:02:c8:70   10.7.4.103       10.130.5.54                       0      AP-C8:70    3.0.7.20    2          0            1 
55      17
0            0             0        22
dc:08:56:09:83:60   10.7.0.103       10.130.5.50                       0      AP-83:60    3.0.7.20     2         0             6
64       17
1            48           79       19
AP managed by 
the same OV
0: 2.4GHz
1: 5GHz
Great signal.
Close neighbor.

<<<PAGE 97>>>
SERVERS CONFIGURATION
• Check the DNS server information
• Check the time zone configuration and NTP logs
• Check the time zone.
• Is the AP synchronized with a NTP server? Does it get the correct time?
support@AP-83:60:~$ cat /etc/resolv.conf
# Interface wan
nameserver 10.0.0.51
search ale-training.com
support@AP-83:60:~$ cat /tmp/TZ
UTC+08
support@AP-83:60:~$ cat /proc/kes_syslog | grep ntp
2019-12-04 01:44:42 Ap-Debug ntp_sync[12561] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] :  _GOLSOH_time was synced from pool.ntp.org
2019-12-04 01:45:09 Ap-Debug ntp_sync[13216] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] :  _GOLSOH_time was synced from pool.ntp.org
2019-12-04 02:00:07 Ap-Debug ntp_sync[27565] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] :  _GOLSOH_time was synced from pool.ntp.org
Wrong time zone

<<<PAGE 98>>>
NETWORK TROUBLESHOOTING
USE CASE

<<<PAGE 99>>>
AP FAILS TO GET IP ADDRESS (1/2) 
• 1) IP address assignment? Static or DHCP?
• How to set the IP assignment to DHCP:
• Reset AP to factory default
• Log in to AP web UI and set the IP address mode to 
DHCP
support@AP-83:60:~$ cat /etc/config/network
config interface 'loopback'
option ifname 'lo'
option proto 'static'
option ipaddr '127.0.0.1'
option netmask '255.0.0.0'
config globals 'globals'
option ula_prefix 'fd66:ce37:fd0b::/48'
config interface 'wan'
option ifname 'eth0'
option type 'bridge'
option proto 'dhcp'
option force_link '1'
DHCP assignment

<<<PAGE 100>>>
AP FAILS TO GET IP ADDRESS (2/2) 
• 2) Capture and analyze DHCP packets on 
the uplink port
• What you should see:
• Check network connection between AP and 
DHCP server when no answer is received:
• Check that DHCP server sends at least DHCP-
NAK packet for out-of-pool request:

<<<PAGE 101>>>
SYSLOG MESSAGES NOT SENT TO SYSLOG SERVER
• OmniVista configures the AP to send syslog 
messages to an external syslog server
• 1) Syslog configuration on the AP?
• 2) Syslog process running?
• 3) Test syslog communication:
• “logger” command sends a syslog packet to 
the remote syslog server
• Message received on syslog server?
support@AP-83:60:~$ cat /var/config/syslog.conf
{
"SysLog": {
"log_remote":1,
" log_ip":10.130.5.222,
" log_port":514,
"log_priority":"LOG_NOTICE"
}
}
Syslog enabled
support@AP-83:60:~$ ps | grep 10.130.5.222
911  root        1156 S   /sbin/logread –f –r 10.130.5.222 514 –p /var/run/lo
4031 support   1304 S    grep 10.130.5.222
Syslog process running
support@AP-83:60:~$ logger –p emerg “_GOLSOH_Just for test!”
support@AP-83:60:~$
Syslog server IP configuration
Syslog message 
received from 
the client 
(OmniVista)
Syslog message content 
(Just for test!)

<<<PAGE 102>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 103>>>
WIFI SURVEY
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 104>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the multiple types of site 
survey
• Understand and identify the causes of WiFi 
signal issues
• Troubleshoot based on the site survey result
• Learn how to perform and analyze a passive 
site survey with Ekahau mapper

<<<PAGE 105>>>
WIFI SITE SURVEY
• Goal
• Analyze Radio Frequency (RF) environment 
• Identify Radio Frequency (RF) interferences
• Find optimum locations for Access Points
• Non-existent WiFi network:
• Installing a WiFi network is possible?
• RF environment and interferences
• Plan and design a wireless infrastructure
• Best AP location
• Existing WiFi network
• Assess wireless performance
• Troubleshooting
• Area coverage, weak signal strength, network interferences
?
?
?
?
?

<<<PAGE 106>>>
TYPES OF SITE SURVEY
Passive
• Listen WLAN traffic
• No authentication and 
802.11 association
• All frequencies are 
scanned
• Detects Access Points
• Measure signal strength
• Measure noise
Active
• Associate survey tool to 
(multiple) access point
• Same measures as 
passive survey
• Measure packets loss
• Measure retransmission
• Measure physical rates
Predictive
• Simulation tool
• Import site plan & RF 
characteristics of 
objects
• Model RF environment
• Deploy (automatically) 
AP on the map
On-site survey
No field measurements

<<<PAGE 107>>>
SITE SURVEY PROJECT
Passive Site survey
RF analysis
Deploying New 
Wireless Network
Replacing Wireless 
Network
Troubleshooting 
Wireless Network
Site Survey
Predictive: Pre-deployment, place new APs 
Passive: Post-deployment, RF analysis 
Active: Post-deployment, clients performance analysis
Active Site Survey
Performance analysis

<<<PAGE 108>>>
ENVIRONMENT AND CHALLENGES
Offices
Walls, 
attenuation
Open offices
High density of 
population
Industry 
(Factory, Warehouse)
Shelves, machine tools
Healthcare
(Hospital, Clinic)
Walls, RF interferences

<<<PAGE 109>>>
WIFI SIGNAL ISSUES - CAUSES
Access Point placement: bad location (wall, pillar)
Concrete 
pillar
Placement of AP in front of obstructing object 
Concrete wall
Dead 
zone
Add a new AP
Place an AP on both side of the obstructing wall
Ekahau Site Survey on Windows

<<<PAGE 110>>>
WIFI SIGNAL ISSUES - CAUSES
Physical obstruction: Environment (multiple walls, materials).
Ekahau Site Survey on Windows
• Distance = 4 meters
• 1 to 4 walls crossed
• RSSI = -70dBm
• Not enough for VoWLAN
• Signal degrades when going 
through:
• Concrete (walls)
• Wood (doors)
• Metal (cabinet, shelves,…)
• Steel (building structure)
• Glass & Mirrors
• Brick (fireplace)
• Water (liquid: fish tank; 
vapor: bathroom)

<<<PAGE 111>>>
WIFI SIGNAL ISSUES - CAUSES
Access Point Antennas: directional or omnidirectional
Directional 
antenna
Small
Area covered
Wrong type of antennas
20 meters
Omnidirectional 
antenna
No 
Area covered
Use the appropriate type of antenna based on the environment

<<<PAGE 112>>>
WIFI SIGNAL ISSUES - CAUSES
Access Point placement: RF interference
Co-channel Interference
Adjacent channel 
Interference
WiFi Analyzer on Android
Ekahau Site 
Survey on 
Windows
OR
- Loss of throughput
→Change AP channel
- Packets loss
- Corrupted data
→Change AP channel

<<<PAGE 113>>>
ON-SITE SURVEY GUIDE

<<<PAGE 114>>>
ON-SITE TROUBLESHOOTING
• Issue definition: “WiFi network is underperforming”
• Where? When? Who? How?
• Define the issue, scope and test locations 
• Step 1 – Get the floor plans
• Identify potential issues: obstacles, walls, ceiling height,…
• Identify areas where WiFi is required: offices, labs, welcome desk,…
• Locate Access Point
High 
priority area
Medium 
priority area
Obstacles
Access Points

<<<PAGE 115>>>
ON-SITE TROUBLESHOOTING
Step 2 – Site Survey observation
• Identify Access Point model: same as original design?
• Identify RF overlap between Access Points: Co/Adjacent channel interference?
• Identify areas with no radio coverage: Access Point down? No Access Point placed?
• Access Point transmission power: Default or customized value?
• Access Point location: Troublesome placement?
Ekahau Site Survey on Windows

<<<PAGE 116>>>
ON-SITE TROUBLESHOOTING
Step 2 – Site Survey observation
No Adjacent / Co-channel 
Interference
No coverage
AP missing
Obstructed 
areas
Stellar AP1511
As originally planned
1
2
3
Move AP to 
optimize RF 
coverage
5
Default transmit power (17dBm)
Increase for best coverage
4

<<<PAGE 117>>>
ON-SITE TROUBLESHOOTING
Step 3 – Corrective actions
• Change Access Point model: AP with better antenna, outdoor AP,…
• Rework RF wireless design: modify transmit powers, change radio channels,…
• Rework channel width: limit adjacent / co-channel interference
• Remove lower data rates: force devices to use closer APs with better signal strength
• Improve AP placement: improve RF signal delivery
• Use Case
• Modify transmit power of an AP
• Add a new Stellar AP
• Move a Stellar AP

<<<PAGE 118>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 119>>>
TECHNICAL KNOWLEDGE CENTER
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 120>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Log in on the Technical Knowledge Center
• Search use cases in the database
• Understand the structure of a use case

<<<PAGE 121>>>
MY PORTAL
• https://myportal.al-enterprise.com/

<<<PAGE 122>>>
TKC - TECHNICAL SUPPORT ACCESS
1
2

<<<PAGE 123>>>
HOME PAGE
1
2
3
Search
Filters
Dates

<<<PAGE 124>>>
HOME PAGE - DOCUMENTATION
Video
1
1
2
2
Article
3
3
Article
Click on the image 
and log in with your 
MyPortal account to 
visualize the video
If you want to learn how to get 
better results from the 
Technical Knowledge Center, 
you can look for the following:
•
TKC Video tutorial
•
Improve the search's result using 
Wildcards & Operators
•
What is the Technical Knowledge 
Center? and how to use it?

<<<PAGE 125>>>
SEARCH OPTIONS
Article Types:
•
Alert: Communication about known issue
•
How To / General Information:
Configuration guide, procedure, explanation
•
Solve My Issue : Cases
•
Technical Communications: Guidelines
Solution > Network :
•
OmniAccess > OmniAccess Stellar
•
OmniVista Cirrus
•
OmniVista Network Advisor
•
Fleet Supervision
•
…
Published Dates:
•
All Dates (by default)
•
Within last day
•
Within last week
•
Within last month
•
Within last year

<<<PAGE 126>>>
USE CASE STRUCTURE
Use Case name
Case Description:
•
Topology
•
Scenario
•
Environment
•
Diagnosis
•
…
Version build : Stellar, OmniVista
Resolution:
•
Configuration
•
Hot Fix
•
Firmware upgrade

<<<PAGE 127>>>
SEARCH A USE CASE IN TKC

<<<PAGE 128>>>
RESEARCH A USE CASE IN TKC
• Issue description
• After replacing the legacy wifi network with a Wireless LAN Stellar solution, some clients 
experience disconnections while roaming in the building.
• Research TKC database
• Select the use case
• Multiple results: analyze the cases & select the more relevant
Search
&

<<<PAGE 129>>>
IDENTIFY A USE CASE SIMILAR TO YOUR ISSUE
• Use Case description
• Does the description match your issue?
• Yes: Check the case Resolution
• No: Select another Use Case
• Compare version build. 
• Same version: Check the case Resolution
• Older version: Check case Resolution & Solution -> Issue might already be fixed with a build
• Newer version: Check case Resolution & Solution -> Issue might be fixed with the latest build

<<<PAGE 130>>>
CHECK THAT THE SOLUTION SOLVES YOUR ISSUE
• Use Case Resolution
• Repeat the procedure.
• Warning: Do you have the access and rights on the equipment (Stellar AP and client)?
• Do you reach the same conclusions?
• Yes: Apply the solution and validate it
• No: Search for another use case or contact the technical support to create a new one
• Solution
Issue fixed?

<<<PAGE 131>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 132>>>
HARDWARE OVERVIEW
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 133>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the OmniAccess Stellar WLAN 
Portfolio
• Understand the OmniAccess Stellar WLAN 
Accessories

<<<PAGE 134>>>
OVERVIEW
Wi-Fi 5
Indoor
MLE
AP123x
OMNIACCESS STELLAR LINEUP – WI-FI 5

<<<PAGE 135>>>
OVERVIEW
OMNIACCESS STELLAR LINEUP – WI-FI 6
Wi-Fi 6
Indoor
MLE
AP132x
Wi-Fi 6
Outdoor
Rugged
AP136x
Wi-Fi 6
Indoor
SMB
AP1311
Wi-Fi 6
Indoor
SMB
AP1301
Wi-Fi 6
Indoor
MLE
AP1351
Wi-Fi 6
Indoor
MLE
AP1331
Wi-Fi 6
Indoor
Hosp.
AP1301H

<<<PAGE 136>>>
OVERVIEW
OMNIACCESS STELLAR LINEUP – WI-FI 6E
Wi-Fi 6E
Indoor
MLE
AP1431
Wi-Fi 6E
Indoor
SMB
AP1411
Wi-Fi 6E
Indoor
MLE
AP1451

<<<PAGE 137>>>
OVERVIEW
OMNIACCESS STELLAR LINEUP – WI-FI 7
Wi-Fi 7
Indoor
MLE
AP1521
Wi-Fi 7
Indoor
SMB
AP1511
Wi-Fi 7
Outdoor
Rugged
AP157x

<<<PAGE 138>>>
CHARACTERISTICS

<<<PAGE 139>>>
OMNIACCESS STELLAR AP1230 SERIES
• Tri radio
• First 5GHz radio: 1,733Mbps (with 4SS/VHT80 clients 
or 2SS/VHT160 clients)
• Second Multiband radio: 1,733Mbps (with 4SS/VHT80 
clients or 2SS/VHT160 clients)
• Third 2.4GHz radio: 800Mbps 2.4GHz (4SS/VHT40)
• MU-MIMO
• Integrated BLE radio
• Up to 24 SSID (8 per radio)
• 768 client devices per AP
• 1xGbE + 1x2.5GbE network interfaces, RJ-45 
console, USB port, reset button
• 802.3at POE (4pair - 60W) compliant/ 48V DC 
(function reduced when powered by 802.3at 2 pair 
source)
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in antenna (OAW-AP1231)
• External antenna connectors (OAW-AP1232)
• OAW-AP1231/1232
• High-end AP
• 802.11ac Wave 2 MU-MIMO
• 802.11ac 4x4:4SS VHT160 and Integrated BLE
OAW-AP1231
OAW-AP1232
Wi-Fi 5

<<<PAGE 140>>>
OMNIACCESS STELLAR AP1301
• Dual radio
• 2.4GHz radio: 573Mbps (2x2:2SS/HE40)
• 5GHz radio: 1.2Gbps (2x2:2SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• Improving network security and Wi-Fi quality
• MU-MIMO
• Up to 16 SSID (8 per radio)
• 512 clients per AP
• 2 x 1GE, 1 x RS-232 console, USB2.0
• PoE 802.3af compliant
• Full function at 802.3af PoE source
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in OMNI directional antenna
• OAW-AP1301
• Wi-Fi 6 entry level Access Point
• 802.11ax (Wi-Fi 6) - Indoor AP
OAW-AP1301
Wi-Fi 6

<<<PAGE 141>>>
OMNIACCESS STELLAR AP1301H
• Dual radio
• 2.4GHz radio: 573.5Mbps (2x2:2SS/HE40)
• 5GHz radio: 1.2Gbps (2x2:2SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• Improving network security and Wi-Fi quality
• MU-MIMO
• Up to 32 SSID (16 per radio)
• 1024 clients per AP
• 1 x 1GE PoE (802.3at/af) uplink port
• 1 x 1GE PoE-PSE (802.3af) downlink port
• 3 x 1GE downlink port
• 1 x USB2.0, 1 x RJ45 console passthrough 
• PoE 802.3at/af compliant
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in OMNI directional antenna
• OAW-AP1301H
• Indoor Hospitality Wi-Fi 6 Access Point
OAW-AP1301H
Wi-Fi 6

<<<PAGE 142>>>
OMNIACCESS STELLAR AP1311
• Dual radio
• 2.4GHz radio: 573Mbps (2x2:2SS/HE40)
• 5GHz radio: 1.2Gbps (2x2:2SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• Improving network security and Wi-Fi quality
• Integrated BLE 5.1 / ZigBee radio
• MU-MIMO
• Up to 16 SSID (8 per radio)
• 512 clients per AP
• 2 x 1GE uplink, 1 x 1GE downlink, 1 x RS-232 
console/Modbus IoT, USB2.0
• PoE 802.3af/at compliant
• Full function at 802.3at PoE source
• Disable private PSE and USB with 802.3af PoE source
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in OMNI directional antenna
• OAW-AP1311
• Wi-Fi 6 entry level AP
• 802.11ax (Wi-Fi 6) - Indoor AP
OAW-AP1311
Wi-Fi 6

<<<PAGE 143>>>
OMNIACCESS STELLAR AP1320 SERIES
• Dual radio
• 2.4GHz radio: 573.5Mbps (2x2:2SS/HE40)
• 5GHz radio: 2.402Gbps (4x4:4SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• MU-MIMO
• Up to 32 SSID (16 per radio)
• 1024 clients per AP
• Integrated BLE 5.1 / ZigBee radio
• 1 x 2.5GE & 1 x 1GE uplink, RJ45 console, USB2.0
• Support 802.3at PoE (with PoE backup)
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in antenna (OAW-AP1321)
• External antenna connectors (OAW-AP1322)
• OAW-AP1321/1322
• Mid-range AP
• 802.11ax (Wi-Fi 6)
OAW-AP1322
OAW-AP1321
Wi-Fi 6

<<<PAGE 144>>>
OMNIACCESS STELLAR AP1331
• Dual radio
• 2.4GHz radio: 1.15Gbps (4x4:4SS/HE40)
• 5GHz radio: 2.4Gbps (4x4:4SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• MU-MIMO
• Up to 32 SSID (16 per radio)
• 1024 clients per AP
• Integrated BLE 5.1 / ZigBee radio
• 2 x 5GE PoE (802.3bt/at) 
• RJ45 console, 1 x USB3.0
• Support 802.3bt/at PoE
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in OMNI directional antenna
• OAW-AP1331
• Mid-range AP
• 802.11ax (Wi-Fi 6)
Wi-Fi 6
OAW-AP1331

<<<PAGE 145>>>
OMNIACCESS STELLAR AP1351
• Tri radio
• 2.4GHz radio: 1.147 Gbps (4x4:4SS/HE40)
• 5GHz Low radio : 4.8 Gbps (4x4:4SS/HE160)
• 5GHz High radio: 4.8 Gbps (8x8:8SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• Improving network security and Wi-Fi quality
• Integrated BLE 5.1 / ZigBee radio
• Up to 24 SSID (8 per radio)
• 1536 clients per AP
• 2 x 10GE uplink, 1 x RS-232 console, USB3.0
• PoE 802.3at/bt compliant
• Full function at 802.3bt PoE source
• Enterprise temperature range, plenum rated
• Operating Temp: 0°C to 45°C
• Built-in OMNI directional antenna
• No mount kit in box
• OAW-AP1351
• High-end Wi-Fi 6 AP
• 802.11ax (Wi-Fi 6) - Indoor AP
OAW-AP1351
Wi-Fi 6

<<<PAGE 146>>>
OMNIACCESS STELLAR AP1360 SERIES
• Dual radio
• 2.4GHz radio: 573.5Mbps (2x2:2SS/HE40)
• 5GHz radio: 2.402Gbps (4x4:4SS/HE80)
• 1 full band (radio) dedicated to radio scanning
• MU-MIMO
• Up to 32 SSID (16 per radio)
• 1024 clients per AP
• Integrated BLE 5.1 / ZigBee radio
• 1 x 2.5GE uplink, 802.3at PoE
• 1 x 1GE downlink, 802.3at PoE 
• 1 x SFP
• 1x USB2.0, reset button
• Temperature range -40 to +65 degree C
• Built-in omni-antenna (OAW-AP1361)
• Built-in directional antenna (OAW-AP1361D)
• External antenna connectors (OAW-AP1362)
• OAW-AP1361/62/D
• Rugged outdoor AP
• 802.11ax (Wi-Fi 6)
OAW-AP1361
Wi-Fi 6

<<<PAGE 147>>>
OMNIACCESS STELLAR AP1411
• Dual radio
• 2.4GHz radio: 574Mbps (2x2:2SS/HE40)
• 5GHz radio: 1.2Gbps (2x2:2SS/HE80)
• OR (configurable)
• 6GHz radio: 2.4Gbps (2x2:2SS/HE160)
• Up to 16 SSID
• 512 clients per AP
• Integrated BLE5.1 / ZigBee radio
• 2 x 1/2.5GE uplink + 1 x 1GE uplink (IoT)
• 1 x RJ45 Console
• 1x USB3.0 Type A, reset button
• Temperature range 0 to +45 degree C
• Built-in omni-antenna 
• Cert: Generic global cert, WFA 6E, EN60601-1-1, 
EN60601-1-2, UL2043
• OAW-AP1411
• Entry level Wi-Fi 6E AP
• 802.11ax (Wi-Fi 6E) – Indoor AP
OAW-AP1411
Wi-Fi 6E

<<<PAGE 148>>>
OMNIACCESS STELLAR AP1431
• Tri radio
• 2.4GHz radio: 574Mbps (2x2:2SS/HE40)
• 5GHz radio: 1.2Gbps (2x2:2SS/HE80)
• 6GHz radio: 2.4Gbps (2x2:2SS/HE160)
• Up to 16 SSID
• 512 clients per AP
• Integrated BLE5.1 / ZigBee radio
• 2 x 2.5GE uplink (multi speed port: 1/2.5 gigabit) 
• PoE IEEE 802.3bt Type 3 compliant 
• 1 x RJ45 Console
• 1x USB3.0, reset button
• Temperature range 0 to +45 degree C
• Built-in omni-antenna 
• Cert: Generic global cert, WFA 6E, EN60601-1-1, 
EN60601-1-2, UL2043
• OAW-AP1431
• Mid range Wi-Fi 6E AP
• 802.11ax (Wi-Fi 6E) – Indoor AP
OAW-AP1431
Wi-Fi 6E

<<<PAGE 149>>>
OMNIACCESS STELLAR AP1451
• Tri radio
• 2.4GHz radio: 1.147Gbps (4x4:4SS/HE40)
• 5GHz radio: 4.8Gbps (8x8:8SS/HE80)
• 6GHz radio: 4.8Gbps (4x4:4SS/HE160)
• 1 full band (radio) dedicated to radio scanning
• MU-MIMO
• Up to 48 SSID (16 BSSID per radio)
• 1536 clients per AP
• Integrated BLE5.1 / ZigBee radio
• 2 x 10GE uplink, PoE IEEE 802.3bt compliant
• 1 x RJ45 Console
• 1x USB3.0, reset button
• Temperature range 0 to +45 degree C
• Built-in omni-antenna 
• OAW-AP1451
• High-end Wi-Fi 6E AP
• 802.11ax (Wi-Fi 6E) – Indoor AP
OAW-AP1451
Wi-Fi 6E

<<<PAGE 150>>>
OMNIACCESS STELLAR AP1511
• Tri radio
• 2.4GHz radio: 688Mbps (2x2:2SS/EHT40)
• 5GHz radio: 2.88Gbps (2x2:2SS/EHT160)
• 6GHz radio: 5.76Gbps (2x2:2SS/ EHT320)
• Up to 48 SSID (16 BSSID per radio)
• 768 clients per AP (256 clients per radio)
• Integrated BLE5.1 / ZigBee radio
• 1 x 1/2.5/5GE multi-gigabit uplink, PoE IEEE 802.3bt 
compliant
• 1 x USB type C Console
• 1x USB2.0, reset button
• 802.3bt POE compliant
• Temperature range 0 to +50 degree C
• Built-in OMNI antenna 
• OAW-AP1511
• Wi-Fi 7 Premium entry range AP
• 802.11be (Wi-Fi 7) – Indoor AP
OAW-AP1511
Wi-Fi 7

<<<PAGE 151>>>
OMNIACCESS STELLAR AP1521
• Tri radio
• 2.4GHz radio: 688Mbps (2x2:2SS/EHT40)
• 5GHz radio: 2.88Gbps (4x4:4SS/EHT160)
• 6GHz radio: 5.76Gbps (2x2:2SS/ EHT320)
• Up to 48 SSID (16 BSSID per radio)
• 1280 clients per AP
• Integrated BLE5.1 / ZigBee radio
• Dedicated scanning Tri-Band Radio
• 1 x 1/2.5/5/10GE multi-gigabit uplink, PoE IEEE 
802.3bt compliant
• 1 x 1GE uplink/downlink
• 1 x USB type C Console
• 1x USB2.0, reset button
• 802.3bt POE compliant
• 802.3at (up to 15W) in low power mode
• Temperature range 0 to +50 degree C
• Built-in OMNI antenna 
• OAW-AP1521
• Mid-range Wi-Fi 7 AP
• 802.11be (Wi-Fi 7) – Indoor AP
OAW-AP1521
Wi-Fi 7

<<<PAGE 152>>>
OMNIACCESS STELLAR AP1570 SERIES
• Tri radio
• 2.4GHz radio: 688Mbps (2x2:2SS/EHT40)
• 5GHz radio: 2.88Gbps (2x2:2SS/EHT160)
• 6GHz radio: 5.76Gbps (2x2:2SS/ EHT320)
• Up to 48 SSID (16 BSSID per radio)
• 768 clients per AP (256 per adio)
• Integrated BLE5.1 / ZigBee radio
• Dedicated scanning Tri-Band Radio
• 1 x 1/2.5/5/10GE multi-gigabit uplink, PoE IEEE 
802.3bz compliant
• 1 x 1GE uplink/downlink, PSE 802.3at
• 1x USB2.0, reset button
• 802.3at/bt PoE compliant
• Temperature range -40° to +65° degree C
• Integrated omni antenna (OAW-AP1571)
• External antenna connectors (OAW-AP1572)
• IP67 certified
• OAW-AP1571/1572
• Rugged outdoor AP
• 802.11be (Wi-Fi 7) – Outdoor AP
OAW-AP1571
Wi-Fi 7

<<<PAGE 153>>>
PRODUCT LINE MATRIX
Click on this icon to view the full Product Line Matrix documentation

<<<PAGE 154>>>
ACCESSORIES

<<<PAGE 155>>>
ACCESSORIES > POE INJECTORS & POWER ADAPTERS
• PoE Injector
• A PoE injector, also called midspan or PoE adapter, 
can be implemented to provide power to an 
OmniAccess Stellar Access Point, if it is connected to
a non-PoE compatible network device.
• Power Adapter
• A power adapter is plugged into a power outlet and
provide power to OmniAccess Stellar Access Points.
• A list of PoE Injectors and Power Adapters models compatible with each OmniAccess 
Stellar Access Point can be found in the Access Point’s datasheet:
EXAMPLE > OMNIACCESS STELLAR AP1331 DATASHEET
SWITCH
POWER
RESET
POE
SPEED/LINK/ACT
POE
SPEED/LINK/ACT
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
1
3
5
7
2
4
6
8
9
10
Letacla
DATA
POWER + DATA
NON-POE SWITCH
AP
POWER OUTLET
POWER
OUTLET
AP

<<<PAGE 156>>>
ACCESSORIES > MOUNTING KITS
• Mounting Kit
• A mounting kit is used to install an OmniAccess Stellar Access Point on a surface
(ceiling, wall, desk…)
• The Mounting Kit(s) compatible with each OmniAccess Stellar Access Point can be found in each 
Access Point’s datasheet:
• Some OmniAccess Stellar Access Points are shipped with a mounting kit.
Please refer to the Product Line Matrix document to learn more
EXAMPLE > OMNIACCESS STELLAR AP1331 DATASHEET
CEILING MOUNTING KITS
WALL MOUNTING KITS
PRODUCT LINE MATRIX EXTRACT
CLICK HERE
FOR MORE
DETAILS
outdoor mount kit

<<<PAGE 157>>>
ACCESSORIES > EXTERNAL ANTENNAS
• External Antennas
• Some OmniAccess Stellar Access Points can be equipped with external antennas to: 
•
Gain more control over the energy radiated
•
Tailor the shape based on the coverage needed
• Access points compatible with external antennas have their reference ends with “2” (ex.  AP1322, 
AP1362)
• The external antenna(s) compatible with each OmniAccess Stellar Access Point can be found in 
each Access Point’s datasheet:
EXAMPLE > OMNIACCESS STELLAR AP1322 DATASHEET

<<<PAGE 158>>>
ACCESSORIES > EXTERNAL ANTENNAS
• The External Antennas models and details can also be found in the Product Line Matrix 
documentation:
Click on this icon to view the full Antennas Matrix documentation (p. 4)

<<<PAGE 159>>>
WI-FI TECHNOLOGY

<<<PAGE 160>>>
WI-FI TECHNOLOGY
• Wi-Fi 6 – Challenges
• Designed to address dense growing capacity and IoT 
efficiency needs for the next generation of 
Enterprise wireless network.
• Stellar WLAN brings integrated Bluetooth/Zigbee, 
dedicated Wi-Fi scanning radio technology providing 
a framework for expanded IoT, security and location 
analytic services.
• Wi-Fi 6 - Improvements
• Increased network throughput
• Increased efficiency in dense environments
• Increased robustness outdoors
• Reduced power consumption
• Enhanced Wi-Fi coexistence
• Reduced overhead (user/device contention)
24 years evolution
Wi
Fi
6E
20
21
11ax
20
23
.11be
7
24 years evolution
Wi
Fi
6E

<<<PAGE 161>>>
WI-FI 7 TECHNOLOGY
Increased Wireless Efficiency for Enhanced Speed & Seamless Connectivity
Preamble 
Puncturing
Improved 
Spectrum 
Efficiency
Reduced 
Latency
Multi 
Resource 
Unit (MRU)
Reduced 
Latency,
Increased 
Capacity
Enhanced 
Efficiency
R
U
1
R
U
2
R
U
3
Automated 
Frequency 
Coordination
Coordinating 
Channel 
Mechanism
Effective use 
of the 6 GHz 
AFC
4096-QAM
More Capacity,
Higher Data 
Rates
+20% raw 
speed 
increase
Wider 
Channel 
Bandwidth
Increased 
Throughput,
5x faster
46 Gbps vs. 9.6 
in Wi-Fi 6E
320 MHz
MU-MIMO 
up to 
(16x16:16)
More Devices 
Simultaneously
Enhanced 
Efficiency
Multi-Link 
Operation
(MLO)
Reliability, 
Efficiency & 
Performance
Better quality 
in dense 
areas
2.4GHz
5GHz
6GHz

<<<PAGE 162>>>
WI-FI GENERATION PERFORMANCES
Wi-Fi Generations
Wi-Fi 4
Wi-Fi 5
Wi-Fi 6
Wi-Fi 6E
Wi-Fi 7
Launch date
2007
2013
2019
2021
2024
IEEE std.
802.11n
802.11ac
802.11ax
802.11be
Latency/Resiliency
MLO
Max data rate
1.2 Gbps
3.5 Gbps
9.6 Gbps
46 Gbps
Bands
2.4/5 GHz
2.4/5 GHz
2.4/5 GHz
2.4/5/6 GHz
2.4/5/6 GHz
Security
WPA 2
WPA 2
WPA 3
WPA 3
Channel width
20,40 MHz
20,40,80,80+80,
160 MHz
20,40,80,80+80,160 MHz
Up to 320 MHz
Modulation
64-QAM, 
OFDM
256-QAM, OFDM
1024-QAM, OFDMA
4096-QAM, OFDMA
MIMO
4x4 MIMO
4x4 MIMO,
DL MU-MIMO
8x8 UL/DL MU-MIMO
16x16 MU-MIMO
Power Saving
TWT
RTWT
Lower latency
Higher Efficiency
More Connected Devices
Higher Power Efficiency
Interference Management
Higher Capacity
Higher Data Rates
Higher Performance
Higher Spectrum Efficiency
Improved Reliability

<<<PAGE 163>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 164>>>
OVERVIEW
OMNIVISTA CIRRUS
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 165>>>
Upon completion this module, 
you will be able to:
OVERVIEW
•
Explain what is Omnivista Cirrus and its 
benefits

<<<PAGE 166>>>
CLOUD-BASED NETWORK MANAGEMENT PLATFORM
OmniVista Cirrus
Software as a Service (SaaS) model
 
 
Cloud-based service
 
Zero Deployment 
OmniVista Cirrus 
Stellar AP
WLAN 
Mgmt
UPAM 
Features
Wi-Fi 
QoE &
analytics
OmniSwitch
Analytics 
& 
Statistics
AOS 
Mgmt
Stellar 
AP Mgmt
Maintain & 
Monitor

<<<PAGE 167>>>
PRESENTATION
• OmniVista Cirrus
• Central & unified cloud management
• Open framework platform 
• High availability and resiliency
• Up to 12.000 Network devices supported
• 10.000 Access Points + 2.000 OmniSwitches
• Advanced Analytics
• Advanced Wireless features
• Advanced wireless and security (WIPS) 
solutions
• SSID scheduling
OmniVista Cirrus
AP Group 1
AP Group 2

<<<PAGE 168>>>
WIRED AND WIRELESS FEATURES LIST
Troubleshooting
Advanced Analytics
▪
LAN & WLAN Unified 
Management
▪
Inventory and topology map
▪
AP Groups Management
▪
Site & Geo Maps
▪
Heatmap
▪
Advanced SSID schedule
▪
RAP support
▪
MESH/ Bridge AP support
▪
VLAN Management
▪
LAN Template base 
provisioning (CLI script)
▪
Application visibility
▪
Optimizing Data storage
▪
Configurable duration for 
Event records (default 
30days / up to 1Yr)
Network Management
▪
Dashboard
▪
Audit / Syslog
▪
Critical Resources, Alarms, 
Monitoring
▪
Network Health & statistics
▪
Traffic metrics of Wired 
Network
▪
Reports
▪
Network statistics
▪
LAN and WLAN clients list
▪
LAN & WLAN Collect 
support info

<<<PAGE 169>>>
WIRED AND WIRELESS FEATURES LIST
Guest
Security
SSID Management
▪
Company Property / MAC 
Auth
▪
Employee User DB
▪
802.1X Auth
▪
BYOD Portal Auth
▪
External Radius/LDAP
▪
Authentication of clients 
on AP and AOS wired port 
▪
Azure AD integration
▪
Device Specific PSK
▪
Dynamic Private Group PSK
▪
RadSec
▪
Guest Self-Registration
▪
Guest Social Login 
Facebook/Rainbow
▪
Social Login Office365
▪
External Captive Portal
▪
Guest Tunneling
▪
Access Auth Profile
▪
Wi-Fi Enhanced Open
▪
Employee Account & 
Guest Account 
▪
Username and password 
strength policy
▪
WIDS / WIPS Policy
▪
Interference / Rogue AP
▪
IoT Visibility & 
Enforcement
▪
BLE and ZigBee Radio
▪
MacSec support
▪
IPv6 support
▪
Portal / PSK  / WPA2 / 
WPA3
▪
VLAN Map per AP group
▪
Roaming
▪
Time – Based SSID
UPAM Authentication

<<<PAGE 170>>>
NETWORK PREREQUISITES
OmniVista Cirrus
WAN
All Stellar models 
supported, except:
•
AP1101
•
AP1201L/H/HL
Software version:
AWOS 4.0.6 GA or higher
Open Firewall ports
•
9093
•
30123
•
30124
•
30125
And to allow outbound
traffic from local network:
•
443
•
80
•
123
•
53
Enable DHCP standard 
options:
1, 2, 6, 28, 42, 43
And, when using proxy:
129, 130, 131, 132, 133, 138
NTP server:
At least 1 configured.
Stellar Access Points
OmniSwitch
All OmniSwitch 
models running in 
8.9RX and 8.10RX 
supported
Software version:
AOS 8.9R1 or higher

<<<PAGE 171>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 172>>>
OVERVIEW
OMNIVISTA TERRA
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 173>>>
Upon completion this module, 
you will be able to:
OVERVIEW
•
Explain what is Omnivista Terra and its 
benefits

<<<PAGE 174>>>
ON-PREMISES NETWORK MANAGEMENT PLATFORM
Stellar AP
WLAN 
Mgmt
UPAM 
Features
Wi-Fi 
QoE &
analytics
OmniSwitch
Analytics 
& 
Statistics
AOS 
Mgmt
Stellar 
AP Mgmt
Maintain & 
Monitor
OmniVista Terra
On-Premises customer hosted
Software as a Service (SaaS) model

<<<PAGE 175>>>
OMNIVISTA TERRA PRESENTATION
• Features parity with OmniVista Cirrus
• Deployment
• On-premises customer hosted
• Virtualized infrastructure – cluster of VMs
• Single tenant
• High availability resiliency
• Scalability
• Up to 2.000 Network devices supported
▪Up to 1.600 Stellar APs and 400 OmniSwitches
OmniVista Terra
Network Admin
AP Group 1
AP Group 2
OmniVista Terra
Cluster

<<<PAGE 176>>>
WIRED AND WIRELESS FEATURES LIST
Troubleshooting
Advanced Analytics
▪
LAN & WLAN Unified 
Management
▪
Inventory and topology map
▪
AP Groups Management
▪
Site & Geo Maps
▪
Heatmap
▪
Advanced SSID schedule
▪
RAP support
▪
MESH/ Bridge AP support
▪
VLAN Management
▪
LAN Template base 
provisioning (CLI script)
▪
Application visibility
▪
Optimizing Data storage
▪
Configurable duration for 
Event records (default 
30days / up to 1Yr)
Network Management
▪
Dashboard
▪
Audit / Syslog
▪
Critical Resources, Alarms, 
Monitoring
▪
Network Health & statistics
▪
Traffic metrics of Wired 
Network
▪
Reports
▪
Network statistics
▪
LAN and WLAN clients list
▪
LAN & WLAN Collect 
support info

<<<PAGE 177>>>
WIRED AND WIRELESS FEATURES LIST
Guest
Security
SSID Management
▪
Company Property / MAC 
Auth
▪
Employee User DB
▪
802.1X Auth
▪
BYOD Portal Auth
▪
External Radius/LDAP
▪
Authentication of clients 
on AP and AOS wired port 
▪
Azure AD integration
▪
Device Specific PSK
▪
Dynamic Private Group PSK
▪
RadSec
▪
Guest Self-Registration
▪
Guest Social Login 
Facebook/Rainbow
▪
Social Login Office365
▪
External Captive Portal
▪
Guest Tunneling
▪
Access Auth Profile
▪
Wi-Fi Enhanced Open
▪
Employee Account & 
Guest Account 
▪
Username and password 
strength policy
▪
WIDS / WIPS Policy
▪
Interference / Rogue AP
▪
IoT Visibility & 
Enforcement
▪
BLE and ZigBee Radio
▪
MacSec support
▪
IPv6 support
▪
Portal / PSK  / WPA2 / 
WPA3
▪
VLAN Map per AP group
▪
Roaming
▪
Time – Based SSID
UPAM Authentication

<<<PAGE 178>>>
OMNIVISTA TERRA HIGH LEVEL ARCHITECTURE
Identical features than OVCX
Consistent User Interface & Experience
Same commercial structure than OVCX
Common Edge Services
A virtualized environment supporting: 
VMware environment
Support up to 5000 devices
Multi-servers for high availability & scalability
High availability: Active-Active L3
Customer site
OmniVista Terra
Network Admin
Kubernetes cluster
OmniVista Terra
VM/Server VM/Server VM/Server
Customer devices
VPN Server
Load balancer
Server
Kafka / MQTT
HTTPS
HTTPS

<<<PAGE 179>>>
NETWORK PREREQUISITES
OmniVista Terra
WAN
All Stellar models 
supported, except:
•
AP1101
•
AP1201L/H/HL
Software version:
AWOS 4.0.7.14 or higher
Open the following Firewall ports to allow outbound
traffic from local network:
•
443
•
80
•
123
•
53
Enable DHCP standard 
options:
1, 2, 6, 28, 42, 43
And, when using proxy:
129, 130, 131, 132, 133, 138
NTP server:
At least 1 configured.
Stellar Access Points
OmniSwitch
All OmniSwitch 
models running in 
8.9RX and 8.10RX 
supported
Software version:
AOS 8.9.82R01 or higher

<<<PAGE 180>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 181>>>
CLASSROOM SESSION 
OR VIRTUAL CLASS SESSION
END OF TRAINING EVALUATIONS
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 182>>>
YOUR FEEDBACKS ARE 
IMPORTANT!
Thank you to complete the training 
evaluation online survey before 
leaving your session. This will take 
you 2 minutes! 
You must complete the end of 
training evaluation to be able to 
download your training certificate of 
attendance.

<<<PAGE 183>>>
LOGIN TO ALE KNOWLEDGE HUB
• Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual 
credentials

<<<PAGE 184>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (1/2)
• Click on My Training on the home page
• Search for the training course by the reference provided by your instructor

<<<PAGE 185>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (2/2)
• From the session, select Evaluate in the dropdown menu and follow the instructions
• OR
• From the curriculum, select Open Curriculum
• Then select Evaluate in the dropdown menu associated to the session and follow 
the instructions

<<<PAGE 186>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 187>>>
Find a Course 
Browse our catalog available on https://enterprise-education.csod.com/ to find your training path 
and course detail. 
Feedback 
In order to improve the quality of the documentation, please report any feedback and address to: 
Alcatel-Lucent Enterprise 
115-225 rue Antoine de Saint-Exupéry 
ZAC Prat Pip – Guipavas 
29806 BREST CEDEX 9 – France 
FAX: (33) 2 98 28 50 03 
or mail to: 
training-services@al-enterprise.com