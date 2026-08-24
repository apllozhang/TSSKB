

<<<PAGE 1>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
OMNIACCESS STELLAR WLAN 
ADVANCED TROUBLESHOOTING
AND UPDATE - EDITION 02 
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
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE

<<<PAGE 4>>>
Upon completion of this module, 
you will be able to:
LESSON SUMMARY
• Troubleshooting methodology
•
Understand potential root causes of Wireless 
issues
•
Understand and apply the process steps when 
troubleshooting a case

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
POTENTIAL WLAN TROUBLESHOOTING CAUSES - WIRELESS
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
•
Association (Beacon, probes request/response, 802.11k/v/r)
•
Authentication (Open, Pre-Shared Key, 802.1X/RADIUS)
•
Encryption (No encryption, TKIP, AES/CPPM)
•
Upper Layers (DHCP, IP, DNS, VLAN, Gateway, Captive Portal)
RF Media (RSSI, SNR, Radio Coverage)
Configuration, SSIDs, Minimum basic rates, Band steering, 
Radio capabilities, Roaming, QoS

<<<PAGE 7>>>
POTENTIAL WLAN TROUBLESHOOTING CAUSES – LOCAL NETWORK
PoE, Antenna, AP location, Physical layer issues
Configuration, Firmware, LAN interface
PoE, VLANs, Port speed, Configuration, QoS
OmniVista: Configuration, Firmware, Licensing issues, VLANs
DHCP: Configuration, Lease duration, Address Pool scope, DHCP options
DNS: Configuration, Security, Blacklist
802.1X/RADIUS: Configuration, Ports, Range, EAP types, Certificate issues
LDAP/AD: Accounts, Credentials, Custom RADIUS attributes
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
Issues independant from the network administrator
WAN Router
Internet

<<<PAGE 9>>>
TROUBLESHOOTING PROCESS
USE CASE

<<<PAGE 10>>>
TROUBLESHOOTING PROCESS STEPS
Identify
Locate
Solve
Document
Re-Create
Isolate
Verify
Determine if problem exists
Ask questions & collect infos
Correctly identify issue
If you can’t recreate this issue, 
return to step one and ask 
more questions
Identify OSI Layer, Specific 
devices, Specific locations, 
Driver versions
Extensive testing to confirm 
and verify the solution did 
indeed solve the issue at hand
Tied to physical space
Tied to specific devices
Use OSI model to define layer
Formulate & Implement plans
May include changes to drivers, 
configurations or design
Document initial issues, processes, 
diagnostics & resolutions
Follow up with those involved

<<<PAGE 11>>>
USE CASE
Q&A with the customer in order to Analyze the issue:
•
Identify
•
Locate
•
Isolate
Gather configuration from the customer topology:
•
AP Log file
•
Access Switch configuration
Description of the issue 
by the client
« Wifi clients cannot 
log into the SSID 
Employee »
Identify
Locate
Isolate
Open the file “Troubleshooting interview –
Use Case” for more details
VLAN 10
VLAN 20
“Employee” 
VLAN
Access switch
“Building_A”
Analyze of the issue
Wrong VLAN configuration on 
the Access Switch 
“Building_A”

<<<PAGE 12>>>
USE CASE
Re-create
Gather network configuration from 
customer:
•
Access switches: vcboot.cfg
•
OmniVista: VM Snapshot (.ovf file)
•
Stellar AP: APs configuration Backup
•
Servers: Backup configuration
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
Re-create customer topology in 
your environment
Re-create customer issue in your 
environment
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
Ask the client to test their day-to-day wireless applications (Rainbow, 
voice, mail,…) and wireless devices to check the solution stability.

<<<PAGE 14>>>
USE CASE
▪Document the troubleshooting case:
▪Issue description
▪
Topology
▪
Firmware versions
▪Diagnostic
▪Resolution
▪
Configuration fixes
▪
Firmware version to be used
▪
Hardware replacement
▪Follow the case 
▪Check that the solution is permanent
▪No side effects due to the resolution
▪Database example: ALE Technical 
Knowledge Center
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
Upon completion of this module, 
you will be able to:
LESSON SUMMARY
• Troubleshooting Tools
•
Understand and use the internal troubleshooting 
tools
•
Understand and list the external tools used to 
analyze the wireless network and issues

<<<PAGE 21>>>
INTEGRATED DIAGNOSTIC TOOLS

<<<PAGE 22>>>
BEFORE TROUBLESHOOTING
• NTP server configured in the network
• Synchronize all equipment with the same NTP server:
• Stellar APs
• OmniVista 2500
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
• Use a third party software (putty, 
teraterm,…)
• In OmniAccess Stellar WLAN Enterprise
• Go to:
• Activate SSH Login & Set a password:
• Check the configuration in CLI
• File: /var/config/public_group.conf
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
AP LOG COLLECTION – ENTERPRISE MODE
• In OmniVista
• Enable « AP web » in the AP Group
• Log in to the AP Web UI: https://<AP_IP> or http://<AP_IP>:8080

<<<PAGE 27>>>
AP LOG COLLECTION – ENTERPRISE MODE
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
OMNIVISTA LOG COLLECTION 
• In OmniVista
• Download all the logs from OmniVista
• Identify the cause of the issue (ex: internal radius error)
• Download the appropriate logs

<<<PAGE 30>>>
• Step 1
• CLI connection to the AP with « support » account
• Enter in CLI:
ssudo tcpdump –i br-wan –w testcapture.pcap udp port 53 
PACKET CAPTURE ON STELLAR AP - TCPDUMP
• Step 2
• Transfer the captured file on your 
PC/laptop
• Step 3
• Open and read the file with 
Wireshark 
Use the 
TCPdump tool
Select the LAN interface « br-wan »
You are listening to the interface br-wan –
which is the wired interface – connecting 
the Stellar AP to the network.
Select the traffic
UDP port 53 = DNS
Capture the DNS traffic on the wired 
interface of the access point
Save the capture in the file 
« test-capture.pcap »
SFTP tool 
(WinSCP)
SFTP
Test-capture.pcap
Test-capture.pcap

<<<PAGE 31>>>
AIR CAPTURE ON STELLAR AP – EXPRESS MODE
• Stellar AP captures the surrounding wireless 
traffic on the selected channel
• Step 1 – Cluster web UI
• In “AP” window, click on the AP which will 
perform the Air capture. New tab opens.
• Step 2 – Stellar AP web UI
• In RF Environment, select the Radio to capture
• Click on Start Capture
• Select the Channel
• Enter the TFTP server where the capture will be 
sent
• Option: Filter the capture (MAC, Frame type)
• Start/Stop the capture
• Warning: Capture file limited to 10MB or 5min of 
capture
• Step 3 – PC/laptop
• Open the file on Wireshark

<<<PAGE 32>>>
AIR CAPTURE ON STELLAR AP – ENTERPRISE MODE
• Stellar AP captures the surrounding wireless 
traffic on the selected channel
• Step 1 – OmniVista
• Activate “AP Web” in the AP Group
• Step 2 – Stellar AP
• Log in
• In RF Environment, select the Radio to capture
• Click on Start Capture
• Select the Channel
• Enter the TFTP server where the capture will 
be sent
• Option: Filter the capture (MAC, Frame type)
• Start/Stop the capture
• Warning: Capture file limited to 10MB or 5min of 
capture
• Step 3 – PC/laptop
• Open the file on Wireshark

<<<PAGE 33>>>
STELLAR AP CONFIGURATION BACKUP – EXPRESS MODE
• Backup the configuration of one or multiple 
Stellar AP
• Used to re-create the issue
• Shared with the technical support
• Step 1 – Cluster web UI
• In “AP” window, click on “Backup All 
Configuration”.
• Download the file “pub-config.tar” locally.
• Step 2 – Re-create the issue
• In your own setup, “Restore All 
Configuration” using the .tar file.
• Step 2 bis – Analyze the configuration
• Extract the config-pub.tar file.
• Check the configuration offline

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
• Open an Air capture trace (wireless 
capture)

<<<PAGE 36>>>
MISCELLANEOUS TOOLS
• Wifi Analyzer (PC, 
smartphone)
• Analyze RF environment
• SSID power
• SSID SNR
• Density of SSIDs
• Channels used
• Wireless Air capture (>5 
minutes)
• Windows: Wifi card supporting 
monitor mode
• MacBook: Native
• TFTP and Syslog servers
• Export logs from the Stellar AP
InSSIDer on Windows
Wifi Analyzer
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
• Troubleshoot:
- The hardware of the Stellar Access Points
- The system of the Stellar Access Points
- The Captive Portal solution
- A cluster in Express mode

<<<PAGE 40>>>
HARDWARE TROUBLESHOOTING

<<<PAGE 41>>>
HARDWARE – LEDS – AP12XX/13XX/14XX/15X1
• Single tri-color LED (Red, Blue, Green)
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
• System tri-color LED STATUS (Red, Blue, Green) & PoE status LED PSE
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
• 7 LEDs
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
• 7 LEDs
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
System and Firmware
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
CLOUD

<<<PAGE 49>>>
SYSTEM TROUBLESHOOTING

<<<PAGE 50>>>
SYSTEM DIAGNOSTIC
• Date
• Check Stellar AP system time and date
• Check Stellar AP synchronization to the NTP 
server. Is it the same time ?
• Uptime
• Check Stellar AP uptime
• Unexpected Stellar AP reboot?
• Restart reason
• Why did the AP reboot?
• Check in the AP log collection:
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
• Check the AP role and status in the cluster
• Is the Stellar AP supposed to be the Primary 
Virtual Controller?
• Is the Stellar AP running in the cluster?
• Check the status of the PVC in the cluster
• Is a PVC found in the cluster? Is it supposed to 
be this PVC?
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
Upon completion of this module, 
you will be able to:
LESSON SUMMARY
• Wireless Troubleshooting
•
Troubleshoot wireless issues
•
Understand wireless troubleshooting through use 
cases

<<<PAGE 63>>>
WIRELESS CONFIGURATION
• Check wireless configuration
• Check List
• SSID broadcasted on the selected 
radio(s)?
• Transmission Power as selected in the RF 
profile?
• Encryption activated?
• BSSID is present?
• If there is no MAC address for « Access 
Point », the SSID is not broadcasted
athXY
X = 0 : 2.4GHz Radio
X = 1 : 5GHz Radio
X = 2 : 6GHz Radio
Y = [1…16] : SSID ID
support@AP-0E:E0:~$ iwconfig
gre0      no wireless extensions.
...
ath01     IEEE 802.11ng  ESSID:"employee0"
Mode:Master  Frequency:2.437 GHz Access Point: DC:08:56:09:83:61
Bit Rate:192 Mb/s   Tx-Power=17 dBm
RTS thr:off   Fragment thr:off
Encryption key:CE75-5424-2E7F-9C74-B8AD-83F4-14EC-03A
Power Management:off
Link Quality=94/94  Signal level=-48 dBm  Noise level=-95 dBm
Rx invalid nwid:12078  Rx invalid crypt:0  Rx invalid frag:0
Tx excessive retries:0  Invalid misc:0   Missed beacon:0
ath11     IEEE 802.11ac  ESSID:"employee0"
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
• Use « iwconfig » to identify the wireless 
interface to monitor: 
ath01 for the employee0 SSID in 2.4GHz
• Check the channel used for the SSID in 2.4GHz
• Check the power of transmission used for the 
SSID in 2.4GHz.
support@AP-0E:E0:~$ iwlist ath01 channel
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
support@AP-0E:E0:~$ iwlist ath01 txpower
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

<<<PAGE 66>>>
WIRELESS TROUBLESHOOTING
USE CASE

<<<PAGE 67>>>
AP CAN’T GENERATE HEAT MAP (1/2)
• Reminder
• AP needs a wireless interface to send/receive a wireless signal and so, generate a Heat Map.
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
ath12     IEEE 802.11ac  ESSID:"guest0"
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
• Reminder:
• To create a Heat Map for a specific radio (ex:2.4GHz), a wireless interface must exist for this radio.
• 2) Heat Map can’t be created for the 2.4GHz radio. Check AP WLAN configuration: 
• Heat Map can’t be generated for the 2.4GHz radio. Select the 5GHz radio:
WLAN configuration only 
for the 5GHz radio
No Heat Map for 2.4GHz.
Select the 5GHz radio.

<<<PAGE 69>>>
REASONS FOR ROAMING FAILURE
• APs must be seen as neighbors 
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
neighbors but can’t see each other (i.e: radio 
waves blocked by corridor with right 
angles,…).
• The client context can't be shared. No roaming.
• Solution:
• On both AP, add statically the neighbor Stellar AP 
from the list of known AP.
• The client context can be shared through the 
LAN and the client can roam.
• Select the AP in the AP Registration > Access 
Point view and click on the hyperlink 
"Neighbor AP"
• Click on the Edit button and select the neighbor 
AP from the list
• Repeat the process for the second AP
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
Upon completion of this module, 
you will be able to:
LESSON SUMMARY
• Client Troubleshooting
•
Troubleshoot client issues in a Stellar solution
•
Understand client troubleshooting through use 
cases

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
2019-12-09 01:19:55 User tid[1638] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] : [TID_DHCP_PROTOCOL] ip:[10.7.0.41], mac:[d4:6e:0e:18:60:38], hostname:[], 
ostype:[iOS]
2019-12-09 01:19:55 User tid[1638] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] : [TID_DHCP_PROTOCOL] ip:[], mac:[d4:6e:0e:18:60:38], 
hostname:[StellarClient0], ostype:[iOS]
2019-12-09 01:19:55 User tid[1638] <NOTICE> [AP DC:08:56:00:0E:E0@10.7.0.101] : [TID_DHCP_PROTOCOL] ip:[10.7.0.41], mac:[d4:6e:0e:18:60:38], 
hostname:[StellarClient0], ostype:[iOS]

<<<PAGE 77>>>
STELLAR AP TO CLIENT ATTRIBUTES
• List the detailed attributes that AP 
sends to the client
• Check List:
• Same parameters as the sta_list command 
→IP address, VLAN, Association Time, 
AccessRole Profile assigned,…
• Depending on the authentication method 
used (802.1X, MAC, Captive Portal), does 
the client receives the correct parameters 
from the Stellar AP?
• Correct Captive Portal URL?
• Is the Authentication a success?
• Correct Access Role Profile after authentication 
success?
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
"redirectURLFromMACAuth": "https:\/\/ov2500-upam-cportal.al-
enterprise.com:443…”
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
• Does the signal received by the client has enough strength? →RSSI, MINRSSI, MAXRSSI
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
Quality impact for voice and 
real-time applications
Perfect
Recommendation for voice and 
real-time application

<<<PAGE 80>>>
CLIENT ACCESS LOGS
• Check the access logs of a specific client
• Check List:
• Check association / disassociation exchange between Stellar AP and client
• Check the disassociation reason in case of an unexpected disconnection of the client.
support@AP-83:60:~$ cat /proc/kes_syslog | grep <client-MAC>
support@AP-83:60:~$ cat /proc/kes_syslog | grep d4:6e:0e:18:60:38
2019-12-03 05:27:21 User tid[1725] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [TID_DHCP_PROTOCOL] ip:[10.7.0.39], mac:[d4:6e:0e:18:60:38], hostname:[], ostype:[]
2019-12-03 05:27:24 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [MLME] [ieee80211_recv_disassoc] [ath12(dc:08:56:09:83:6a)] [d4:6e:0e:18:60:38] Received 
Disassoc with reason 8(OS moved the client to another AP using non-aggressive load balance), recv rssi 63, min rssi 55, max rssi 64       Client manual disconnection
2019-12-03 05:27:24 User calog[4977] <NOTICE> [AP DC:08:56:09:83:60@10.7.0.103] : [MLME] [ieee80211_mlme_recv_disassoc] [ath12(dc:08:56:09:83:6a)] [d4:6e:0e:18:60:38] Call 
MLME indication handler to deliver disassoc event and free the sta node
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
• 2) Which radio does the client support? Compatible with the 
SSID broadcasted?
• 3) Country Code of the AP? Supported by the client?
• Wrong country code: Set manually a compatible channel on the 
AP in RF profile:
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
• 2) High RSSI Threshold?
• Cause client to disconnect if their RSSI is 
below the Threshold
• Modify RSSI threshold value in RF profile:
• 3) Wireless capture and logs
• AP deny the client?
• Check disassociation/deauthentication 
packets?
• Air Capture on the 5GHz radio
• Access Logs:
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
support@AP-83:60:~$ cat /proc/kes_syslog | 
grep <client-MAC>

<<<PAGE 88>>>
802.1X AUTHENTICATION NOT WORKING (1/3)
• 1) On Client side:
• Check:
• Username and 
password
• Encryption type
• Security type/key
• Certificate on 
client (if any)
Wi-Fi Client
Radius 
Server
Stellar AP
802.1X

<<<PAGE 89>>>
802.1X AUTHENTICATION NOT WORKING (2/3)
• 2) On AP side:
• Compare Radius configuration to Radius server
• IP and ports
• Shared Secret key
• Correct Radius server attached to the SSID?
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
• 3) On Radius server side:
• Compare Radius configuration and 
database to client and AP 
configuration:
• Username/password
• Shared Secret
• Radius client IP
• Radius station IP (IP address of the 
Stellar AP)
• Certificate
• Authentication and accounting ports
• Radius service enabled?
• Firewall allows authentication and 
accounts ports? 
• Sample of FreeRadius server configuration:

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
AP CANNOT REGISTER TO LOCAL OMNIVISTA (1/2)
• Reminder: Set AP to Enterprise mode
• With DHCP Option 138. AP registers to 
OmniVista
• In Cluster, use option “Convert to Enterprise”
• 1) Stellar AP mode? OV or CLUSTER?
• Activate DHCP option 138 in the DHCP pool
• Use “Convert to Enterprise” option
• 2) AP get the IP address of OmniVista 
server?
• If not, modify the option 138 in the DHCP 
server
support@AP-83:60:~$ getmode
CLUSTER
Should be “OV” mode
support@AP-83:60:~$ getovinfo
10.130.5.50
Correct OmniVista IP

<<<PAGE 102>>>
AP CANNOT REGISTER TO LOCAL OMNIVISTA (2/2)
• 3) OmniVista reachable from the AP?
• 4) If Registration Status is “Unmanaged”, 
check license count and import new license
support@AP-83:60:~$ ssudo ping 10.130.5.50
PING 10.130.5.50 (10.130.5.50): 56 data bytes
64 bytes from 10.130.5.50: seq=0 ttl=62 time=1.851 ms
64 bytes from 10.130.5.50: seq=1 ttl=62 time=0.595 ms
OmniVista 
reachable

<<<PAGE 103>>>
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

<<<PAGE 104>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 105>>>
WIFI SURVEY
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 106>>>
Upon completion this module, 
you will be able to:
LESSON SUMMARY
• Understand the multiple types of site 
survey
• Understand and identify the causes of WiFi 
signal issues
• Troubleshoot based on the site survey result
• Learn how to perform and analyze a passive 
site survey with Ekahau mapper

<<<PAGE 107>>>
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

<<<PAGE 108>>>
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

<<<PAGE 109>>>
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

<<<PAGE 110>>>
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

<<<PAGE 111>>>
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

<<<PAGE 112>>>
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

<<<PAGE 113>>>
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

<<<PAGE 114>>>
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

<<<PAGE 115>>>
ON-SITE SURVEY GUIDE

<<<PAGE 116>>>
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

<<<PAGE 117>>>
ON-SITE TROUBLESHOOTING
Step 2 – Site Survey observation
• Identify Access Point model: same as original design?
• Identify RF overlap between Access Points: Co/Adjacent channel interference?
• Identify areas with no radio coverage: Access Point down? No Access Point placed?
• Access Point transmission power: Default or customized value?
• Access Point location: Troublesome placement?
Ekahau Site Survey on Windows

<<<PAGE 118>>>
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

<<<PAGE 119>>>
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

<<<PAGE 120>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 121>>>
TECHNICAL KNOWLEDGE CENTER
OMNIACCESS STELLAR WIRELESS LAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 122>>>
Upon completion this module, 
you will be able to:
LESSON SUMMARY
- Log in on the Technical Knowledge Center
- Search use cases in the database
- Understand the structure of a use case

<<<PAGE 123>>>
MY PORTAL
• https://myportal.al-enterprise.com/

<<<PAGE 124>>>
TKC - TECHNICAL SUPPORT ACCESS
1
2

<<<PAGE 125>>>
HOME PAGE
1
2
3
Search
Filters
Dates

<<<PAGE 126>>>
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

<<<PAGE 127>>>
SEARCH OPTIONS
Article Types:
•
Alert: Communication about known issue
•
How To / General Information: 
Configuration guide, procedure, 
explanation
•
Solve My Issue : Cases
•
Technical Communications: Guidelines
Stellar Categories:
•
Network > OmniAccess Stellar
•
OmniVista 2500
•
UPAM
Published Dates:
•
All Dates
•
Within last day
•
Within last week
•
Within last month
•
Within last year

<<<PAGE 128>>>
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

<<<PAGE 129>>>
SEARCH A USE CASE IN TKC

<<<PAGE 130>>>
RESEARCH A USE CASE IN TKC
• Issue description
• After replacing the legacy wifi network with a Wireless LAN Stellar solution, some clients 
experience disconnections while roaming in the building.
• Research TKC database
• Select the use case
• Multiple results: analyze the cases & select the more relevant
Search
&

<<<PAGE 131>>>
IDENTIFY A USE CASE SIMILAR TO YOUR ISSUE
• Use Case description
• Does the description match your issue?
• Yes: Check the case Resolution
• No: Select another Use Case
• Compare version build. 
• Same version: Check the case Resolution
• Older version: Check case Resolution & Solution -> Issue might already be fixed with a build
• Newer version: Check case Resolution & Solution -> Issue might be fixed with the latest build

<<<PAGE 132>>>
CHECK THAT THE SOLUTION SOLVES YOUR ISSUE
• Use Case Resolution
• Repeat the procedure.
• Warning: Do you have the access and rights on the equipment (Stellar AP and client)?
• Do you reach the same conclusions?
• Yes: Apply the solution and validate it
• No: Search for another use case or contact the technical support to create a new one
• Solution
Issue fixed?

<<<PAGE 133>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 134>>>
HARDWARE OVERVIEW
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 135>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the OmniAccess Stellar WLAN 
Portfolio
• Understand the OmniAccess Stellar WLAN 
Accessories

<<<PAGE 136>>>
OVERVIEW
Wi-Fi 5
Indoor
MLE
AP123x
OMNIACCESS STELLAR LINEUP – WI-FI 5

<<<PAGE 137>>>
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

<<<PAGE 138>>>
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

<<<PAGE 139>>>
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

<<<PAGE 140>>>
CHARACTERISTICS

<<<PAGE 141>>>
OMNIACCESS STELLAR AP1230 SERIES
• Tri radio
• First 5GHz radio: 1,733Mbps (with 4SS/VHT80 clients or 
2SS/VHT160 clients)
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
(function reduced when powered by 802.3at 2 pair source)
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

<<<PAGE 142>>>
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

<<<PAGE 143>>>
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

<<<PAGE 144>>>
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

<<<PAGE 145>>>
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

<<<PAGE 146>>>
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

<<<PAGE 147>>>
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

<<<PAGE 148>>>
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

<<<PAGE 149>>>
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

<<<PAGE 150>>>
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

<<<PAGE 151>>>
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

<<<PAGE 152>>>
OMNIACCESS STELLAR AP1511
• Tri radio
• 2.4GHz radio: 688Mbps (2x2:2SS/EHT40)
• 5GHz radio: 2.88Gbps (2x2:2SS/EHT160)
• 6GHz radio: 5.76Gbps (2x2:2SS/ EHT320)
• Up to 32 SSID (16 BSSID per radio)
• 512 clients per AP
• Integrated BLE5.1 / ZigBee radio
• 1 x 1/2.5/5GE multi-gigabit uplink, PoE IEEE 802.3bt 
compliant
• 1 x USB type C Console
• 1x USB2.0, reset button
• 802.3at/bt POE (up to 35W) compliant
• Temperature range 0 to +50 degree C
• Built-in OMNI antenna 
• OAW-AP1511
• Wi-Fi 7 Premium entry range AP
• 802.11be (Wi-Fi 7) – Indoor AP
OAW-AP1511
Wi-Fi 7

<<<PAGE 153>>>
OMNIACCESS STELLAR AP1521
• Tri radio
• 2.4GHz radio: 688Mbps (2x2:2SS/EHT40)
• 5GHz radio: 2.88Gbps (4x4:4SS/EHT160)
• 6GHz radio: 5.76Gbps (2x2:2SS/ EHT320)
• Up to 32 SSID (16 BSSID per radio)
• 512 clients per AP
• Integrated BLE5.1 / ZigBee radio
• 1 x 1/2.5/5/10GE multi-gigabit uplink, PoE IEEE 
802.3bt compliant
• 1 x 1GE downlink
• 1 x USB type C Console
• 1x USB2.0, reset button
• 802.3bt POE (up to 60W) compliant
• 802.3at (up to 15W) in low power mode
• Temperature range 0 to +50 degree C
• Built-in OMNI antenna 
• OAW-AP1521
• Mid-range Wi-Fi 7 AP
• 802.11be (Wi-Fi 7) – Indoor AP
OAW-AP1521
Wi-Fi 7

<<<PAGE 154>>>
PRODUCT LINE MATRIX
Click on this icon to view the full Product Line Matrix documentation

<<<PAGE 155>>>
ACCESSORIES

<<<PAGE 156>>>
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

<<<PAGE 157>>>
ACCESSORIES > MOUNTING KITS
• Mounting Kit
• A mounting kit is used to install an OmniAccess Stellar Access Point on a surface
(ceiling, wall, desk…)
• The Mounting Kit(s) compatible with each OmniAccess Stellar Access Point can be found in each 
Access Point’s datasheet:
• Some OmniAccess Stellar Access Points are shipped with a mounting kit.
Please refer to the Product Line Matrix document to learn more
EXAMPLE > OMNIACCESS STELLAR AP1331 DATASHEET
CEILING MOUNT
WALL MOUNT
PRODUCT LINE MATRIX EXTRACT
CLICK HERE
FOR MORE
DETAILS

<<<PAGE 158>>>
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
• Note: All OmniAccess Stellar Access Points are equipped with an internal antenna
(omni-directional coverage pattern)
EXAMPLE > OMNIACCESS STELLAR AP1322 DATASHEET

<<<PAGE 159>>>
ACCESSORIES > EXTERNAL ANTENNAS
• The External Antennas models and details can also be found in the Product Line Matrix 
documentation:
Click on this icon to view the full Antennas Matrix documentation (p. 4)

<<<PAGE 160>>>
WI-FI TECHNOLOGY

<<<PAGE 161>>>
WI-FI 6 TECHNOLOGY
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

<<<PAGE 162>>>
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

<<<PAGE 163>>>
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

<<<PAGE 164>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 165>>>
FEATURES UPDATE
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 166>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the new Stellar Features
• Update your knowledge of existing features

<<<PAGE 167>>>
UPDATED SCOPE
Watch the updated Stellar videos
Click on the image above to start the first video of the playlist

<<<PAGE 168>>>
OMNIACCESS STELLAR WLAN SOLUTION

<<<PAGE 169>>>
NETWORK MANAGEMENT MODES - OVERVIEW
WiFi Express
Standalone mode
WiFi Enterprise
- In Premise
- Managed mode with OmniVista 2500 NMS
WiFi Cloud
- Cloud based
- Managed mode with OmniVista Cirrus NMS
Move from Express to Enterprise/Cloud when/if needed

<<<PAGE 170>>>
STELLAR EXPRESS MODE

<<<PAGE 171>>>
WIFI EXPRESS – STANDALONE CLUSTER DEPLOYMENT
✓Self managed standalone cluster
✓Integrated secure Web managed 
✓Wizard driven configuration
✓Integrated Guest captive portal
✓External Guest Captive Portal support
✓Distributed intelligence control
✓Self configured AP cluster, up to 255 APs
✓Optimal RF management

<<<PAGE 172>>>
◼Dynamic Frequency Selection
◼Transmit Power Control
◼Extensive Country Code list
◼Channel & Transmission power manual 
assignment
◼Guest Operator Restricted  Role GUI
◼HTTP and Secure Access via HTTPS
◼English, simplified Chinese, German, French, 
Spanish, Korean, Turkish Language Support
◼OXO Connect R2.1 ZTP integration with 
HTTPS 
◼Remote Cluster Management
WIFI EXPRESS – FEATURES LIST
◼Authentication 802.1X, WPA, WPA2, WPA3
◼Encryption WEP, TKIP, AES
◼Built-in User Database
◼External Radius Server Support
◼ACLs per SSID
◼Disconnect/ Blacklist Clients
◼WIPS protection
◼MACSEC for Wireless
◼Syslog & Syslog over TLS support 
◼NTP Client
◼Built-in DHCP/DNS/NAT
◼MESH
◼Certificate Management
WiFi Express
Management
System
Radio
Security

<<<PAGE 173>>>
WIFI EXPRESS – RESILIENCY
• Cluster size > 64
• Resiliency in the network design
• PVM/SVM role assumed by either 
AP123X, AP13xx, AP14xx, AP15x1
• Recommendations
• Max Up to 32 APs per OmniSwitch
• Max Up to 64 APs per stack
• Minimum 2xAP123X, AP13xx, 14xx or 
15X1 in each Stack
WAN
Distribution/Aggregation
Switch
Access Stack 
Switch

<<<PAGE 174>>>
STELLAR ENTERPRISE MODE

<<<PAGE 175>>>
WIFI ENTERPRISE – CENTRAL MANAGED DEPLOYMENT
✓OmniVista 2500/Cirrus
▪
Unified wired-wireless
▪
Access Management (Guest/BYOD)
▪
Role based policy enforcement
✓Smart Analytics
✓Distributed intelligence control
▪
Up to 4000 APs
▪
Scale to support 100K clients per 
devices
✓Advanced wireless features
▪
WLAN topology on a map and heat map
▪
Wireless security (wIDS/wIPS)

<<<PAGE 176>>>
WIFI ENTERPRISE – FEATURES LIST
◼RF Management
◼wIDS/ wIPS - Rogue Containment/ 
Attack Detection
◼Floor Plan/ Heatmap - Planning & 
deployment tools to simplify 
deployment while improving QoE
◼Reports - Uptime, Usage, etc. Reports
◼MESH Topology
◼Controller-less Architecture
◼OmniVista integrated Unified Policy 
Authentication Manager (UPAM)
◼Simplified Management of AP Groups
◼No limit on AP Group Count
◼Max 4000 APs spread across one or 
more AP Groups
◼OmniVista High Availability
◼Support of NaaS Stellar Access Point
WiFi 
Enterprise
Management
Security
System
Radio
◼Secure NAC with Unified Access AG 2.0 
Integration
◼Automated deployment with ALE 
OmniSwitch Integration
◼Smart Analytics Application Monitoring 
& Enforcement/ DPI
◼UPnP/ Bonjour Service Sharing
◼Stellar AP authentication with 802.1X
◼MACSEC for Wireless
◼Unified Policy Authentication Manager
◼Employee - Supplicant/ Non-supplicant 
secure authentication
◼Guest Access - Self Registration/ 
Employee sponsored/ Social Login
◼BYOD
◼Strategy based Policy Enforcement
◼Extensive Captive Portal Customization 
◼External Captive Portal support
◼Syslog and syslog over TLS support

<<<PAGE 177>>>
NETWORK FEATURES

<<<PAGE 178>>>
IPV6 CLIENT SUPPORT – EXPRESS MODE
• IPv6 required for specific verticals
• Education (Research)
• Healthcare (IoT)
• Government (Security)
• IPv6 supported on Client side
• IPv6 Policies supported
• IPv6 QoS/ACL rules to filter client traffic
• IPv6 address on AP management interface
• AP get IPv6 address & gateway
• AP get other parameters (DNS) from DHCPv6 
Server 
• Wireless Client Forwarding
• Client IPv6 traffic forwarded between IPv6 
clients and to IPv6 Gateway
IPv6
IPv6
IPv6

<<<PAGE 179>>>
IPV6 CLIENT SUPPORT – ENTERPRISE MODE
• AP Management through IPv4
• IPv4 for AP/OmniVista communication
• No IPv6 network interface on AP
• DPI support for IPv6 clients
• Client MAC/1X Authentication
• Client authentication request to AP through IPv6
• Radius communication between AP and UPAM through IPv4
• Client Portal Authentication
• Client to portal server through IPv6
• Portal server to Radius Server through IPv4
• Wireless Client Forwarding
• Client IPv6 traffic forwarded between IPv6 clients and to IPv6 
Gateway

<<<PAGE 180>>>
UPAM GUEST - SSID CREATION

<<<PAGE 181>>>
UPAM – GUEST ACCESS SSID
• How it works
• Create a Guest SSID with the usage « Guest 
Network »
• Activate the Captive portal option
• Select the RADIUS server in the Authentication 
Strategy
• Create a Guest account if the UPAM internal 
RADIUS server is used
• In the Guest Access Strategy, define the login 
method (username and password) and Post 
portal enforcement to restrict Guest traffic
• Assign a VLAN to the Guest SSID
• Workflow
Guest SSID
Usage « Guest Network »
Authentication Strategy
Web redirection « Guest » CP 
Guest Access Strategy
Login Method, Post Portal enforcement, 
self-registration  
Optional
Guest account creation in the local DB

<<<PAGE 182>>>
UPAM - BYOD ACCESS

<<<PAGE 183>>>
UPAM – BYOD ACCESS
• How it works
• Employee connects to the BYOD SSID and is 
redirected to the Captive Portal
• BYOD SSID is open with network access restrictions 
• Employee provides its corporate credentials to 
register his personal device
• Employee is now allowed to access the 
corporate network
• Workflow
BYOD SSID
Usage « Employee BYOD Network »
Authentication Strategy
Web redirection « Employee » CP 
BYOD Access Strategy
Authentication source (local DB, external
LDAP/AD, Radius)
Optional
Employee account creation in the local DB

<<<PAGE 184>>>
RECEIVED SIGNAL STRENGTH INDICATOR (RSSI)

<<<PAGE 185>>>
RECEIVED SIGNAL STRENGTH INDICATOR (RSSI)
• How well a device can hear a signal from an access point
• Indicates the quality of the signal received by the access point
CLIENT LIST
CLI
-> wlanconfig ath01 list

<<<PAGE 186>>>
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
Bad
Not recommended for 
Video or Audio applications
OK – not bad
Desired and recommended

<<<PAGE 187>>>
ROAMING GUIDELINES

<<<PAGE 188>>>
IDENTIFY THE ROAMING MODE
• Check the roaming conditions 
• Based on the VLAN ID between the "home" and "foreign" AP, 
select either:
• Layer 2 Roaming
• Layer 3 Roaming
• Check the security level of the SSID (WPA/WPA2, 
Enterprise/Personnal)
• With WPA2 Enterprise only, OKC can be activated
• With WPA2 only, 802.11r (Fast Roaming) can be activated 
(recommended)

<<<PAGE 189>>>
CHECK THE RADIO COVERAGE
• Use the Heat Map application to check the radio coverage
• Select the 2.4GHz and 5GHz in the filters as they don't have exactly the same radio coverage
OK
Radio overlap, Roaming available
KO
No Radio overlap, no Roaming
No overlap
Overlap

<<<PAGE 190>>>
NEIGHBOR AP
• In some cases, Stellar APs are geographical 
neighbors but can’t see each other (i.e: radio 
waves blocked by corridor with right angles,…).
• The client context can't be shared. No roaming.
• Solution:
• On both AP, add statically the neighbor Stellar AP from 
the list of known AP.
• The client context can be shared through the LAN and 
the client can roam.
• Select the AP in the AP Registration > Access Point 
view and click on the hyperlink "Neighbor AP"
• Click on the Edit button and select the neighbor AP 
from the list
• Repeat the process for the second AP
No client 
context
sharing

<<<PAGE 191>>>
STICKY CLIENT AVOIDANCE
• The roaming decision is made by the client device. 
• But some devices will stick to the AP they were previously associated to.
• Use the Roaming RSSI Threshold in the RF profile.
• Use in conjunction with 802.11k and 802.11v
• Value range is 0-100
• Recommended value for 2.4GHz : RSSI = 10
• Recommended value for 5GHz : RSSI = 15
• The Roaming RSSI Threshold controls the signal strength a client needs to see before 
searching for another site.
• If the RSSI threshold is too low, the client remains on a low signal strength site, even with a 
stronger site nearby.
• If the RSSI threshold is too high, the client roams too much that could result to packet loss.

<<<PAGE 192>>>
MISCELLANEOUS
• Background scanning
• When a user roams, his real time traffic can be 
interrupted if the new AP on which he is 
connected is using the background scanning.
• No impact on the voice traffic. 
•
The AP is voice aware and will deactivate the 
background scanning when a voice call is detected.
• Other real-time traffic can be impacted.
• Solution:
• Deactivate the Background scanning on the Stellar 
APs
• Install new Stellar APs in the network, acting as 
dedicated scanning APs
• Please note that this solution requires 
additional Stellar APs in the network

<<<PAGE 193>>>
APPENDIX - ADDITIONAL FEATURES

<<<PAGE 194>>>
BLE BEACONING
BLE Beaconing ready for the AP1230 and AP13XX series with a built-in BLE
• Stellar APs ready for Asset Tracking Solution
• Asset: people or equipment (wheelchair, medical devices, laptop,…)
• Reducing time to find assets: 
improves employees/customer satisfaction
• BLE Beacon is configured per AP Group
• Turned OFF by default
• Configurable parameters are
• Beaconing Mode : iBeacon per default
• Transmission Power
• Frequency/Emission Period
• UUID (Universal Unique Identifier) – ALE specific UUID for all ALE products
• Major and Minor values – used for greater accuracy than UUID alone
OAW-AP1230 Series

<<<PAGE 195>>>
INTEGRATION WITH AEROSCOUT LOCATION ENGINE
AeroScout RTLS (Real Time Location Services) provides location services.
• i.g: Tracking of employees in the building at the plant
• AeroScout solution utilize standard WiFi (802.11) technologies as a 
communication infrastructure
• Customers use the Stellar AP to communicate with AeroScout tags and deliver 
information to the AeroScout Location Engine
• AeroScout LBS Architecture
• AeroScout Tags: Device generating 802.11 messages at a predefined interval
• Stellar APs: Delivers RSSI measurements of tags and WiFi clients to the AeroScout
Engine
• AeroScout Engine Server (AES): Location Engine. Based on RSSI measurements (from 
the Stellar AP), determine position of the clients
• AeroScout Engine Manager (AEM): Configuration of the AES. Displays clients on the 
map, heatmaps, analytics, Geofencing alerts
Stellar AP
AeroScout tags

<<<PAGE 196>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 197>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Connection & Use of the Stellar Remote Lab 
Objectives 
✓ Learn how to connect to the Stellar Remote Lab (R-Lab) 
✓ Discover the equipment available in the Stellar Remote Lab (R-Lab) 
Contents 
1 
Connecting to the Remote Desktop......................................................... 1 
1.1. Connection Method ................................................................................. 1 
1.2. Rlab access URL ..................................................................................... 1 
2 
Discovering the Remote Lab Environment ................................................. 2 
2.1. Topology of the Stellar Remote Lab Pod ........................................................ 2 
2.2. Switch/Access Point Console ..................................................................... 3 
2.3. Wi-Fi Client .......................................................................................... 4

<<<PAGE 198>>>
1 
Connection & Use of the Stellar Remote Lab 
 
 1 
Connecting to the Remote Desktop 
This document lists the usable accounts per POD to use to connect to the Rlab. 
 
 
Warning 
The POD ID or POD list assigned to you (or to your Training session) will be sent by email  
(from: ALE_Knowledge_Hub.Notification@al-enterprise.com ) 
 
You will need the information from the tables given below to set up the connection. 
1.1. 
Connection Method 
A web browser is required to connect to the Rlab 
 
Notes 
Recommended web browsers: 
- 
Chrome  
- 
Edge 
Other web browser may have some issue with copy/paste from a lab guide to the remote terminal session 
Known workaround for FireFox: https://sudoedit.com/firefox-async-clipboard/  
1.2. 
Rlab access URL 
https://rdp.al-mydemo.com/ 
 
 
 
- Username: Refer to the table below to get the corresponding “User Account” to the Rlab type you are using 
- Password: unique per session – sent from our LMS to the Instructor 
 
Use the following table to get the login name of your POD. As well as the correspondence with the variable 
X = [1-8] you will use during the labs. 
 
Value of the variable X 
POD names 
Login(a) to use 
1 
StelLAN - Pod 25 
stellanpod25a 
2 
StelLAN - Pod 26 
stellanpod26a 
3 
StelLAN - Pod 27 
stellanpod27a 
4 
StelLAN - Pod 28 
stellanpod28a 
5 
StelLAN - Pod 29 
stellanpod29a 
6 
StelLAN - Pod 30 
stellanpod30a 
7 
StelLAN - Pod 31 
stellanpod31a 
8 
StelLAN - Pod 32 
stellanpod32a 
 
Ex: If you are connected to the StelLAN POD 25 and asked to configure the IP address 10.130.5.200+X, 
enter the value 10.130.5.201 (X=1).

<<<PAGE 199>>>
2 
Connection & Use of the Stellar Remote Lab 
 
 2 
Discovering the Remote Lab Environment 
In this part, you will find an explanation about the Remote Lab environment that you are going to use during 
this training. 
2.1. 
Topology of the Stellar Remote Lab Pod  
Take a careful look at the topology displayed, as it shows all the equipment that you will use during this 
training.

<<<PAGE 200>>>
3 
Connection & Use of the Stellar Remote Lab 
 
2.2. 
Switch/Access Point Console 
On the R-Lab Windows Desktop, you will find multiple console shortcuts. Each one allows you to connect to 
one of your Lab’s equipment (switch or access point).  
 
 
- Open one of the switch Console terminals used during this training: SW7-OS-6870A, 
SW5-OS-6360A, SW4-OS-2360 
- Check that some messages are displayed 
 
R-Lab Windows Desktop 
Double-click on one shortcut 
to open a switch console: 
- 
SW7-OS-6870A 
- 
SW5-OS-6360A 
- 
SW4-OS-2360 
 
 
 
You have now access to the 
switch console. 
 
 
 
Tips 
If you get a message “Hunting Group Busy” when you open a TeraTerm console, it means that another 
TeraTerm session has already been opened (from your account or another account). Check the console sessions 
currently opened on your session or ask the instructor for help.

<<<PAGE 201>>>
4 
Connection & Use of the Stellar Remote Lab 
 
2.3. 
Wi-Fi Client 
During this Lab, you will have to use a wireless client for tests purpose. This client is a Raspberry Pi and you 
can access it’s remote desktop (RDP) via the shortcut RealVNC Viewer on the desktop. 
 
 
Check the connection to the “WifiClientX” on the Raspberry Pi. 
 
R-Lab Windows Desktop 
Double click on the shortcut 
“WifiClientX”  
Replace X by your POD 
number, X=[1-8] 
 
 
The credentials should be 
already filled.  
If not, the authentication 
window of the VNC Viewer 
application opens.  
Enter the credentials: 
Username: user 
Password: superuser 
 
Click OK. 
 
You are now connected to the 
Raspberry Pi WifiClientX.  
 
 
 
Tips 
The language of the keyboard of the Raspberry Pi is set by the keyboard language of the remote desktop on 
which you are connected.

<<<PAGE 202>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Reinitialization of the Stellar Remote Lab 
Objective 
✓ Reinitialize the R-Lab equipment to its default configuration 
Contents 
1 
Reinitializing the Switches & Access Points ............................................... 1 
2 
Reinitializing the OmniVista 2500 ........................................................... 3 
3 
First login ....................................................................................... 5 
4 
Generating & Installing an Evaluation License ............................................ 7 
4.1. Generating the Evaluation License ............................................................... 7 
4.2. Installing the Evaluation License ................................................................. 8 
4.2.1. Inserting the License File .................................................................................. 8 
4.2.2. Inserting the License Keys ................................................................................. 8 
4.3. Deleting the License File .......................................................................... 8 
5 
Set up the PC Client .......................................................................... 9

<<<PAGE 203>>>
1 
Reinitialization of the Stellar Remote Lab 
 
 1 
Reinitializing the Switches & Access Points  
On the R-Lab Windows Desktop, a shortcut Reset PODX is available on the desktop to reinitialize all the 
equipment (both switches and access points) to their default configuration. 
 
 
In the diagram below, in red, you can see all the equipment that will be reinitialized by using this shortcut: 
 
 
 
Warning 
THE SWITCHES DEFAULT CONFIGURATION IS NOT AN EMPTY CONFIGURATION!   
WHEN CLICKING ON THE SHORTCUT: 
- 
A SPECIFIC CONFIGURATION IS APPLIED TO THE SWITCHES 
- 
ALL THE INTERFACES ARE PUT DOWN. DURING THE LABS, IT WILL BE ASKED TO ENABLE THE INTERFACES 
THAT YOU WILL USE.  
- 
THE OMNISWITCH 6870 IS PRE-CONFIGURED (VLAN, IP INTERFACE,…)  
 
 
Reset all the R-Lab Pod’s equipment by using the Reset PodX script

<<<PAGE 204>>>
2 
Reinitialization of the Stellar Remote Lab 
 
R-Lab Windows Desktop 
On the desktop, double click 
on the Reset PodX shortcut (X 
= Pod number) 
 
Some Windows command 
terminals are displayed, wait 
for them to disappear. 
 
@Switch > The reinitialization 
process takes around 5 
minutes 
 
@Access Point > The 
reinitialization takes around 
1min30 – 2min

<<<PAGE 205>>>
3 
Reinitialization of the Stellar Remote Lab 
 
 2 
Reinitializing the OmniVista 2500  
In this part, we are going to reinitialize the OmniVista 2500 NMS.   
In the diagram below: 
- In red, the equipment that will be reinitialized during this part. 
- In gray, the equipment that have been reinitialized in the previous part.  
 
 
 
 
Reinitialize the OmniVista 2500 to its initial configuration  
 
The OmniVista 2500 is installed in a virtual machine. Therefore, to access and reinitialize it, we will have to 
use the VMware vSphere Client.

<<<PAGE 206>>>
4 
Reinitialization of the Stellar Remote Lab 
 
R-Lab Windows Desktop 
Double click on the vSphere 
Web Console shortcut  
 
Enter the credentials 
- Username: stellarpodX (X = 
R-Lab number) 
- Password: alcatel 
 
Click on Login 
 
Click on the VMs and 
Templates (top left and 
corner) 
 
Browse the tree structure to 
reach the virtual machines, 
then select the OV2500 
 
 means that the client is 
powered off 
 
 means that the client is 
powered on 
 
 
 
Click on ACTIONS > Snapshots 
> Manage Snapshots 
 
Select the snapshot 
DT00CTE26X - Initial State  
 
Click on REVERT TO 
 
Click on OK  
 
Restart the VM > click on the 
button 
 
 
We will continue to configure the OmniVista 2500 in a dedicated lab, later in this course.  
 
 
Tips 
All VM are configured with an English US keyboard, your current keyboard layout is not taken into account. 
Take care of that when you’re typing a command. 
 
 
Notes > What is a snapshot?  
A snapshot preserves the state and data of a virtual machine at a specific point in time. We use it to easily 
revert the OV 2500 back to its initial configuration, to wipe all the previous training configuration.

<<<PAGE 207>>>
5 
Reinitialization of the Stellar Remote Lab 
 
 3 
First login 
From the Windows Desktop, login to the OmniVista 2500 Web Admin Interface: 
 
R-Lab Windows Desktop 
Open a web browser (ex. 
Mozilla Firefox or Google 
Chrome) 
 
Enter the OV 2500 IP address 
in the URL bar: 10.130.5.5X  
(X = Pod number = [1…8])  
 
Username: admin 
Password: switch 
 
Depending on the type of web 
browser being used, a warning 
regarding the website’s 
security certificate will be 
shown. Skip this warning and 
continue to the OmniVista 
login page. 
 
A message informs that the 
default password must be 
changed.  
Click on the Please change 
your password link. 
 
Set the new password to : 
Training123# 
Click on Save.

<<<PAGE 208>>>
6 
Reinitialization of the Stellar Remote Lab 
 
Click on the Continue to 
Login Page link and login 
using the new password. 
 
Login once again with the new 
credentials: 
 
Username: admin 
Password: Training123# 
 
 
A prompt appears to add the 
license(s) 
 
Go to the next part to learn 
how to generate an 
evaluation license

<<<PAGE 209>>>
7 
Reinitialization of the Stellar Remote Lab 
 
 4 
Generating & Installing an Evaluation License 
An Evaluation License provides full OmniVista 2500 NMS feature functionality, but is valid only 
for 90 Days (starting from the date the license is generated). There is one file that contains all of 
the Device (AOS, Third-Party, Stellar APs) and Service Licenses (VM, Guest, BYOD).  
In this part, you will learn how to generate and install an evaluation license 
 
 
- Generate an Evaluation License 
- Install it in your OmniVista 2500 
 
 
Tips > Evaluation License 
This part is NOT dedicated for training. Don’t hesitate to use the same process if you need to generate an 
evaluation license for testing purpose (lab…).  
 
 
Warning 
BEFORE THIS STEP, ENSURE THAT NO LICENSE GENERATED IN A PREVIOUS TRAINING IS AVAILABLE TO AVOID ANY 
POSSIBLE CONFUSION.  
ON THIS WINDOWS DESKTOP, DELETE ANY FILES WITH THE NAME “-EVAL-OV2500…” 
4.1. 
Generating the Evaluation License 
From the Windows Desktop, open a new web browser tab/window: 
 
R-Lab Windows Desktop 
Copy & Paste the following 
URL in your RDP session:  
https://lds.al-
enterprise.com/  
 
Click on OmniVista 2500 NMS 
 
Enter:  
- Customer ID: 99999 
- Order Number: evaluation 
 
Leave the Customer Email 
field blank 
 
 
Click on Submit 
 
Select the License Type: 
EVAL-OV2500-ALL-TYPE_1 
 
Enter the Passcode: omnivista 
 
Click on Submit Entry 
Enter Company Name: ALE (or 
something else) 
 
Click on Generate License 
 
Save the file locally 
 
The sole purpose of entering 
your mail is to receive the 
license information by mail.

<<<PAGE 210>>>
8 
Reinitialization of the Stellar Remote Lab 
 
4.2. 
Installing the Evaluation License 
2 possibilities:  
- Inserting directly the license file obtained in the previous part  
- Inserting the license keys 
 
Don’t do both! 
4.2.1. 
Inserting the License File  
- Go back in the OmniVista 2500 NMS webpage:  
 
> Go back to the OV 2500 Web Admin Interface 
  > Click on Add License 
    > License File: click on Browse 
      > Select the license file downloaded in the previous part 
      > Click on Open 
    > Click on Submit 
 
Software and/or documentation End-User License Agreement “EULA” 
> Check OK (don’t check Enable ProActive Lifecycle Management) 
 
4.2.2. 
Inserting the License Keys 
- Open the file with a text editor (notepad, notepad++…). The licence keys are in clear text.  
- Go back in the OmniVista 2500 NMS webpage:  
 
> Open a Web Browser 
  > Type the following IP address in the URL bar: 10.130.5.5X 
    > Username/Password: admin/switch 
 
> Go to ADMINISTRATION > LICENSE > Add or Import License 
  > In the License Key field, enter all the licenses keys that are in the license file generated in the 
previous step (/!\ remove the license name before inserting them, look at the warning below /!\) 
  > Click on Submit 
 
 
Warning 
COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES! (HIGHLIGHTED THE INFO THAT YOU HAVE 
TO COPY AND PASTE): 
 
EVAL-NM-EX-20-N, KEQWEXRH-VXDJBEUM-4EX$299Z-BBXS7G#4-JC!GW81R-$C8YWB1K-DBE#$LDX-AXVRMLM# 
EVAL-VMM-100-N, WWITUJ#W-EWBU@BSM-@EX$299Z-BBXS7G#4-JC!GWL1R-$CFYWB1L-X5#PC4WT-5UDJU7B# 
EVAL-AP-NM-20-N, G1CUNONJ-YFZ%JX2W-JEX$299Z-BB@S7G#4-JC!GW81R-$CHYWB1L-WAPB3U7!-GDFXMHV& 
EVAL-GA-20-N, 
VTP@GOKN-E53P8#@E-NEX$299Z-BB@S7G#4-JC!GW81R-$C#YWB1L-CJD%PRTF-9GTXNX!1 
EVAL-BYOD-20-N, 
JSQRU%HH-GFFCJUGB-ZEX$299Z-BB@S7G#4-JC!GW81R-$CRYWB1L-EBX5WUFB-8X7HF@5G 
 
Disable Enable ProActive 
Lifecycle Management 
 
Click on OK 
 
 
4.3. 
Deleting the License File 
 
Once the license file correctly inserted, please delete the file (“EVAL…”) from the 
computer.

<<<PAGE 211>>>
9 
Reinitialization of the Stellar Remote Lab 
 
 5 
Set up the PC Client  
In this part, we are going to set up the PC Client. This Linux environment will be used throughout this course 
to test and access the Wi-Fi networks and features that the Stellar products offer.    
In the diagram below: 
- In red, the equipment that will be set up during this part. 
- In gray, the equipment that have been reinitialized in the previous parts.  
 
 
 
Set up the Wi-Fi Linux client: Starting it et resetting the wireless networks 
previously saved.  
 
To access and set up the wireless client, we will have to use a shortcut on the desktop. 
R-Lab Windows Desktop 
Double click on the 
“WifiClientX” shortcut.

<<<PAGE 212>>>
10 
Reinitialization of the Stellar Remote Lab 
 
Type the following 
credentials, if asked :  
- Username : user 
- Password: superuser 
 
Click on OK 
 
You have now access to the 
Linux desktop. 
 
On the desktop, double click 
on the shortcut “Clean 
Wireless Networks” 
 
Select Execute in the new 
window. 
 
This will delete all the known 
wireless networks on this 
client.

<<<PAGE 213>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
Objective 
✓ Learn how to discover the OmniSwitches in the OmniVista 2500 NMS 
Contents 
1 
Briefing ......................................................................................... 1 
2 
Backbone VLAN ................................................................................ 2 
2.1. Backbone VLAN ..................................................................................... 2 
2.2. Backbone VLAN IP Interfaces ..................................................................... 3 
3 
SNMP v3 ......................................................................................... 4 
4 
Discovering the OmniSwitches on the OmniVista 2500 NMS ............................. 5 
5 
Debriefing ...................................................................................... 6 
6 
Troubleshooting ............................................................................... 7 
6.1. Troubleshooting the Level 2 ...................................................................... 7 
6.1.1. Checking the cables ........................................................................................ 7 
6.1.2. Checking the VLAN(s) ...................................................................................... 8 
6.2. L3 Troubleshooting ................................................................................. 8 
6.2.1. Checking the IP Interfaces ................................................................................ 8 
6.2.2. Checking the OmniVista 2500 IP Settings ............................................................... 8 
6.2.3. Pinging the Equipment ..................................................................................... 9 
6.3. Checking the SNMP Configuration ............................................................... 10 
6.4. Discovering the OmniSwitch ..................................................................... 10

<<<PAGE 214>>>
1 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
 1 
Briefing 
Before using all the features offered by the OmniVista 2500 NMS, the network devices must be discovered 
first. In this lab, we are going to discover the 3 OmniSwitches in the OmniVista 2500 NMS. The discovery of 
the 2 Access Points will be covered in another lab.   
 
 
    
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 215>>>
2 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
 2 
Backbone VLAN 
The Backbone VLAN is used to interconnect the network equipment together (OmniSwitches, OmniVista 2500, 
DHCP Server). The SNMP traffic is carried over the Backbone VLAN. 
 
 
The Backbone VLAN and IP Interfaces are pre-configured on each OmniSwitch.  
2.1. 
Backbone VLAN 
The backbone VLAN (VLAN 1305) is pre-configured and connects the following network devices:  
- The 3 OmniSwitches; 
- The OmniVista 2500 (10.130.5.5X); 
- The DHCP Server (10.130.5.7). 
 
 
 
 
Tips > Console Shortcuts 
To access to the OmniSwitches consoles, a shortcut is available for each switch on the Windows Desktop. 
 
 
 
Notes 
The VLAN 1305 is already assigned to the OmniVista 2500 and the DHCP Server.

<<<PAGE 216>>>
3 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
2.2. 
Backbone VLAN IP Interfaces 
Each OmniSwitch requires an IP interfaces on the Backbone VLAN to be able to communicate with the 
OmniVista and DHCP server. These IP interfaces are pre-configured on the OmniSwitches:  
 
 
 
 
 
Check that the Access OmniSwitches can reach the core OmniSwitch 6870, and can reach 
the servers:   
 
OS-6360A 
6360A -> ping 10.130.5.20X (OmniSwitch 6870) 
6360A -> ping 10.130.5.7 (DHCP Server) 
6360A -> ping 10.130.5.5X (OmniVista 2500 NMS) 
 
OS-2360 
2360 -> ping 10.130.5.20X (OmniSwitch 6870) 
2360 -> ping 10.130.5.7 (DHCP Server) 
2360 -> ping 10.130.5.5X (OmniVista 2500 NMS)

<<<PAGE 217>>>
4 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
 3 
SNMP v3  
The OmniVista 2500 uses the SNNMP protocol to discover the network devices and communicate with them. 
The SNMP version 1,2 and 3 are supported.  
In this part, we are going to configure an SNMP version 3 profile on each OmniSwitch. 
 
 
 
 
Configure an SNMP v3 profile on all OmniSwitches. 
 
To create the SNMP v3 profile on the OmniSwitches, use the following command:  
 
OS6870, OS6360, OS2360: 
-> user snmpuserv3 read-write all password “Superuser=1” sha+des 
-> snmp station 10.130.5.5X 162 snmpuserv3 v3 enable

<<<PAGE 218>>>
5 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
 4 
Discovering the OmniSwitches on the OmniVista 2500 NMS 
In this part, we are going to configure an SNMP version 3 profile on the OmniVista 2500, then we will discover 
the 3 OmniSwitches in the OmniVista 2500 (once discovered, OmniSwitches can be managed and supervised 
from the OmniVista 2500 NMS).  
 
 
Configure an SNMP v3 profile on the OmniVista 2500 NMS. 
 
To create the SNMP v3 profile on the OmniVista 2500: 
 
> Open a Web Browser 
  > Type the OV2500 IP address in the URL bar: 10.130.5.5X (X = R-Lab Number) 
    > Username/Password: admin/switch 
 
> Select NETWORK > DISCOVERY > Managed Devices 
    > Click Discover New Devices 
      > Click on the + button (top right) 
        > Enter IP information 
           > Start IP: 10.130.5.20X 
           > End IP: 10.130.5.20X 
           > Subnet Mask: 255.255.255.0 
           > Choose Discovery Profiles: click on the    button to create an SNMPv3 profile 
 
      > SNMPv3 Profile Parameters (leave other parameters blank) 
        > Name: SNMPv3 
        > SNMP Version: SNMPv3 
        > Timeout (msec): 5000  
        > Retry Count: 3  
        > User Name: snmpuserv3  
        > Auth & Priv Protocol: SHA+DES  
        > Auth Password: Superuser=1 
        > Priv Password: Superuser=1 
      > Click on Create 
 
           > Choose Discovery Profiles: select the SNMPv3 profile, click on + to move it to the right 
      > Click on Create 
 
      > Click on the + button to add a new range 
        > Enter IP information 
           > Start IP: 10.130.5.22X 
           > End IP: 10.130.5.22X 
           > Subnet Mask: 255.255.255.0 
           > Choose Discovery Profiles: select the SNMPv3 profile, click on + to move it to the right 
           > Click Create 
 
      > Click on the + button to add a new range 
        > Enter IP information 
           > Start IP: 10.130.5.24X 
           > End IP: 10.130.5.24X 
           > Subnet Mask: 255.255.255.0 
           > Choose Discovery Profiles: select the SNMPv3 profile, click on + to move it to the right 
           > Click Create 
 
 
      > Select the three ranges by clicking on the checkboxes on the left 
 
      > Click on Discover Now to launch the discovery process, then click on Finish. 
 
 
 
 
 
At the end of this part, the 3 OmniSwitches are discovered and are now manageable from the OmniVista 
2500 NMS:  
6360 
2360 
6870

<<<PAGE 219>>>
6 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
 
 
 5 
Debriefing 
The reset script from the previous lab created the “Backbone” VLAN. This VLAN is used to interconnect the 
network equipment together (OmniSwitches, OmniVista 2500, DHCP Server). The SNMP settings were also 
configured with the reset script. And finally, we have discovered the OmniSwitches in the OmniVista 2500 
NMS. These OmniSwitches can now be managed from the OmniVista 2500 GUI.  
 
 
 
 
 
 
OS6870

<<<PAGE 220>>>
7 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
 6 
Troubleshooting 
In this part, we will cover the process to follow if an OmniSwitch is not discovered in the OmniVista 2500. We 
will use the exact same infrastructure as in the lab:  
 
 
6.1. 
Troubleshooting the Level 2 
6.1.1. 
Checking the cables 
First, make sure that the cables are correctly plugged and recognized:  
 
OMNISWITCH 
AOS -> show interfaces 1/1/11  
Operational Status     : up, 
 Last Time Link Changed : Thu Oct 17 06:13:56 2019, 
 Number of Status Change: 1, 
 Type                   : Ethernet, 
 SFP/XFP                : N/A, 
 EPP                    : Disabled, 
 Link-Quality           : N/A, 
 MAC address            : 2c:fa:a2:1b:18:56, 
 BandWidth (Megabits)   :     1000,             Duplex           : Full, 
 Autonegotiation        :   1  [ 1000-F 100-F 100-H 10-F 10-H ], 
 Long Frame Size(Bytes) : 9216, 
 Inter Frame Gap(Bytes) : 12,

<<<PAGE 221>>>
8 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
6.1.2. 
Checking the VLAN(s) 
Then, check that the VLAN(s) is/are correctly configured on each involved port (in this example, the 
management VLAN is the VLAN 1305, and all the equipment are in this VLAN):  
 
OMNISWITCH 
AOS -> show vlan members port 1/1/11 
  vlan      type        status 
--------+-----------+--------------- 
  1305    default     forwarding 
6.2. 
L3 Troubleshooting 
6.2.1. 
Checking the IP Interfaces 
Check that the IP interface is correctly configured on the OmniSwitch, and that its status is UP:  
 
OMNISWITCH 
AOS -> show ip interface 
 Total 6 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_backbone                     10.130.5.200    255.255.255.0       UP     YES vlan 1305 
6.2.2. 
Checking the OmniVista 2500 IP Settings 
Open the OmniVista 2500 CLI (from the VMware vSphere Web Console), then: 
 
OmniVista 2500 Console 
Select the OV2500 virtual 
machine 
 
 
Click Launch Web Console, 
then Web Console 
 
 
 
Enter the credentials defined 
during the OmniVista 2500 
installation:  
- login: cliadmin 
- password: Alcatel.0

<<<PAGE 222>>>
9 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
A menu is displayed.  
 
Choose option [2] Configure 
The Virtual Appliance 
 
Choose option [2] Display 
Current Configuration to 
display all the IP configuration 
(IP@, Mask, Gateway, DNS 
Server…) 
 
Or display each information 
one by one, by using the 
options [2] to [8] 
 
It is also possible to use the 
options [14] and [15] to 
check the Proxy and NTP 
configuration. 
 
6.2.3. 
Pinging the Equipment 
Once the equipment IP configuration checked, make sure that the OmniVista 2500 can ping the 
OmniSwitch:  
 
OmniVista 2500 Console 
Ping from the OmniVista 
2500 to the OmniSwitch 
 
From the Virtual Appliance 
Menu, select [10] Advanced 
Mode 
 
  
 
From the CLI, launch a ping to 
the OmniSwitch IP interface 
address 
 
 
Once the equipment IP configuration checked, make sure that the OmniSwitch can ping the OmniVista 
2500:  
 
PING FROM THE OMNISWITCH 6870 TO OMNIVISTA 2500  
AOS -> ping 10.130.5.5X 
PING 10.130.5.50 (10.130.5.50) 56(84) bytes of data. 
64 bytes from 10.130.5.50: icmp_seq=1 ttl=64 time=0.613 ms 
64 bytes from 10.130.5.50: icmp_seq=2 ttl=64 time=0.571 ms 
64 bytes from 10.130.5.50: icmp_seq=3 ttl=64 time=0.550 ms 
64 bytes from 10.130.5.50: icmp_seq=4 ttl=64 time=0.617 ms

<<<PAGE 223>>>
10 
AOS OmniSwitches Discovery in the OmniVista 2500 NMS 
 
6.3. 
Checking the SNMP Configuration 
Once the IP configuration checked, let’s make sure that the SNMP parameters have been correctly 
entered.  
- On the OmniSwitch, check that the SNMP is enabled:  
 
OMNISWITCH 
AOS -> show aaa authentication 
[…] 
Service type = Snmp 
  Authentication = Use Default, 
  1st authentication server  = local 
[…] 
- On the OmniSwitch, check that the SNMP station and username have been correctly configured:  
 
OMNISWITCH 
AOS -> show snmp station  
ipAddress/port                                      status    protocol user 
---------------------------------------------------+---------+--------+------- 
10.130.5.50/162                                     enable    v3       snmpuserv3 
 
- On the OmniSwitch, re-enter the SNMP password to make sure that this password and the auth&priv 
protocol are the correct ones:  
 
OMNISWITCH 
AOS -> user snmpuserv3 read-write all password Superuser=1 sha+des 
 
- In the OmniVista 2500, re-enter the SNMP settings: 
 
> Open a Web Browser 
  > Type the OV2500 IP address in the URL bar: 10.130.5.5X (X = R-Lab Number) 
    > Username/Password: admin/switch 
 
> Select NETWORK > DISCOVERY > Discovery Profiles 
  > Select the previously created SNMP Profile (ex. SNMPv3) or create a new one 
    > Name: SNMPv3 
      > SNMP Version: SNMPv3 
      > Timeout (msec): 5000  
      > Retry Count: 3  
      > User Name: snmpuserv3  
      > Auth & Priv Protocol: SHA+DES  
      > Auth Password: Superuser=1 
      > Priv Password: Superuser=1 
    > Click on Apply  
6.4. 
Discovering the OmniSwitch 
To launch a new discovery:  
 
> Open a Web Browser 
  > Type the OV2500 IP address in the URL bar: 10.130.5.5X (X = R-Lab Number) 
    > Username/Password: admin/switch 
 
> Select NETWORK > DISCOVERY > Managed Devices 
  > Click Discover New Devices 
      > Click on the + button (top right) 
        > Enter IP information 
           > Start IP: 10.130.5.20X (X = R-Lab Number) 
          > End IP: 10.130.5.20X (X = R-Lab Number) 
           > Subnet Mask: 255.255.255.0 
           > Choose Discovery Profiles: select the SNMPv3 profile created previously 
        > Click on Discover Now to launch the discovery process, then click on Finish.

<<<PAGE 224>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
Objective 
✓ Learn how to discover the Stellar Access Points in the OmniVista 2500 NMS 
Contents 
1 
Briefing ......................................................................................... 2 
2 
Configuring the VLANs & IP Interface ...................................................... 3 
2.1. Creating the VLANs ................................................................................. 3 
2.1.1. Creating the MANAGEMENT VLAN (VLAN 40) ............................................................ 3 
2.1.2. Verifying the VLAN Creation .............................................................................. 4 
2.2. Management VLAN IP Interface ................................................................... 5 
2.2.1. Verifying the IP interface Creation ...................................................................... 5 
3 
OmniSwitch additional Features ............................................................ 6 
3.1. About the IP DHCP Relay address ................................................................ 6 
3.2. About the Interfaces ............................................................................... 6 
3.3. Configuring the Features .......................................................................... 6 
3.3.1. On the Core Switch OS6870 ............................................................................... 6 
3.3.2. On the OS6360 .............................................................................................. 7 
3.3.3. On the OS2360 .............................................................................................. 7 
4 
Discovering the Stellar Access Points ...................................................... 7 
4.1. Registering the Stellar Access Points ............................................................ 7 
4.2. Adding the Stellar Access Points into an AP Group ............................................ 8 
5 
Debriefing ...................................................................................... 9

<<<PAGE 225>>>
1 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
6 
Troubleshooting ............................................................................. 10 
6.1. Troubleshooting the Level 2 ..................................................................... 10 
6.1.1. Checking the PoE ......................................................................................... 10 
6.1.2. Checking the cables ...................................................................................... 10 
6.1.3. Checking the VLAN(s) .................................................................................... 11 
6.2. Troubleshooting the Stellar AP .................................................................. 11 
6.2.1. Reseting the Stellar AP .................................................................................. 11 
6.2.2. Checking the Stellar AP Mode (OV/Cluster) .......................................................... 11 
6.2.3. Checking the Stellar AP DHCP Mode (DHCP/Static) .................................................. 12 
6.2.4. Checking the Option 138/43 in the DHCP Server ..................................................... 12 
6.2.5. Checking the Stellar AP IP Address ..................................................................... 12 
6.2.6. Checking the OV information on the Stellar AP ...................................................... 13 
6.3. Troubleshooting the Level 3 ..................................................................... 13 
6.3.1. Checking the IP Interface ............................................................................... 13 
6.3.2. Pinging the Equipment ................................................................................... 13 
6.4. Discovering the Stellar AP ........................................................................ 14 
7 
Annex: Configuring the Option 138 ....................................................... 15 
7.1. On Windows Server ................................................................................ 15

<<<PAGE 226>>>
2 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 1 
Briefing 
The OmniSwitches are now discovered by the OmniVista 2500, and ready to be configured. During this lab, we 
will first setup some basic settings (VLAN, IP Interface, PoE…) on the Access OmniSwitches, then we will 
launch the discovery process for the Access Points to be discovered in the OmniVista 2500. 
 
 
  
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 227>>>
3 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 2 
Configuring the VLANs & IP Interface 
2.1. 
Creating the VLANs 
First, let’s create the VLAN:  
- VLAN 40 > MANAGEMENT: dedicated VLAN for the Stellar Access Points management.  
 
 
Notes 
The VLAN 1305 (BACKBONE) has already been created in a previous lab. It contains all the management 
equipment (OV2500, DHCP Server…).  
 
 
 
To create this VLAN on the OmniSwitches, we will use the OmniVista 2500 VLAN Manager feature. 
 
 
Configure the VLAN on the Access OmniSwitches 6870, 6360 and 2360. 
2.1.1. 
Creating the MANAGEMENT VLAN (VLAN 40) 
 
> Select CONFIGURATION > VLANS > VLAN 
  > Click on Create VLAN by Devices button 
 
1. Devices Selection 
  > VLAN Overwrite: ENABLED 
  > VLAN IDs: 40  
  > VLAN(s) Description: MANAGEMENT 
    > Click on the Add/Remove Devices 
      > click on Add All 
      > Click on OK  
    > Click on Next 
 
2. VLAN Configuration 
  > Check that Admin Status = Enabled 
  > Click on Next  
 
3. Default Port Assignment 
  > For the OS6360 and OS2360, click on Add Port

<<<PAGE 228>>>
4 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
    > Select the port 1/1/6  
    > Click on OK  
  > Click on Next 
 
4. Q-Tagged Port Assignment 
  > For the OS6870, click on Add Port 
    > Select the ports 1/1/3 and 1/1/8  
    > Click on OK  
  > For the OS2360, click on Add Port 
    > Select the port 1/1/8  
    > Click on OK  
  > For the OS6360, click on Add Port 
    > Select the port 1/1/3  
    > Click on OK  
  > Click on Next 
 
5. Review 
  > Review the information 
  > Click on Create 
 
 
Tips 
The VLANs can also be created on the OmniSwitches via command lines (CLI). Hence, the VLAN Manager feature 
can be very interesting to use if the infrastructure is composed of a lot of OmniSwitches, and the same VLANs 
must be created on some (or all) of them.  
2.1.2. 
Verifying the VLAN Creation 
 
> Select CONFIGURATION > VLANS > VLAN 
  > Next to the information “0 Devices”, click on ADD > Use Switch Picker  
    > Select 1 OmniSwitch (6360 or 2360) 
    > Click on Add  
    > Click on OK  
     
  > Check that the VLAN 40 appears in the list 
  > The VLAN 1305, created in the previous lab, should 
  also appear. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
OS6870

<<<PAGE 229>>>
5 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
2.2. 
Management VLAN IP Interface 
The reset script used earlier has already configured an IP interface for the Management VLAN on the core 
switch OS6870. This will be the IP interface for the management VLAN.  
 
 
OS6870 > name: int_management | IP@: 10.7.X.126/27 | VLAN: 40 
 
 
 
Notes 
No IP interface is configured on the OmniSwitch 6360 and 2360 for the VLAN 40 (they will act as a “level 2” 
switch and will redirect all the level 3 traffic to the OmniSwitch 6870).  
2.2.1. 
Verifying the IP interface Creation 
 
> Select CONFIGURATION > VLANS > IP Interface 
  > Click on Select a device 
    > Select the OmniSwitch 6870 
      > Click on OK 
 
The following result should be displayed:

<<<PAGE 230>>>
6 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 3 
OmniSwitch additional Features 
The Stellar Access Points that we are going to use during this training need to:   
- Receive an IP Address from the DHCP Server > IP DHCP Relay;  
- Forward the Wi-Fi clients traffic to a default route > Static route; 
- Have the switch interface where they are connected enabled; 
- Receive power from the OmniSwitches > The Power over Ethernet (PoE) feature must be enabled. 
 
 
Enable the interfaces where the Stellar Access Points are connected; 
Restart the PoE feature on the OmniSwitches 6360 and 2360 to force the Stellar Access 
Points to reboot.  
3.1. 
About the IP DHCP Relay address 
Once powered on, the Stellar Access Points will send a DHCP request on the VLAN 40. This request will be 
relayed by the core switch 6870 to the DHCP Server on the VLAN 1305.  
The DHCP Server will then send a DHCP Offer with the option 138 (IP address of the OmniVista 2500). Once 
this option received, the Stellar Access Point will work in Enterprise mode.  
 
 
Notes 
The DHCP relay feature is not configured on the OmniSwitch 6360 and 2360. These access OmniSwitches will 
act as a “level 2” switch and will send the DHCP request to the OmniSwitch 6870, which will relay it to the 
DHCP Server.  
 
 
Tips > Option 138 
To learn how to configure the Option 138 on a Windows Server, click here. 
3.2. 
About the Interfaces 
The Stellar Access Points are connected to the interface 1/1/6 of each OmniSwitch.  
3.3. 
Configuring the Features 
3.3.1. 
On the Core Switch OS6870 
 
The OS6870 is pre-configured with the DHCP relay and static route. 
 
 
Notes 
For your information, the CLI commands used to configure these two features are the following: 
> ip dhcp relay destination 10.130.5.7 
> ip dhcp relay admin-state enable 
> ip static-route 0.0.0.0/0 gateway 10.130.5.253

<<<PAGE 231>>>
7 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
3.3.2. 
On the OS6360 
 
> Select CONFIGURATION > CLI SCRIPTING > Terminal 
  > Click on Browse 
    > Select 10.130.5.22X (OS6360) 
    > Click on OK 
      > Enter the username/password: admin/switch 
      > Click on OK 
 
You are now connected to the OS6360. Enter the following command to enable the PoE: 
 
         > interfaces 1/1/6 admin-state enable 
        > lanpower slot 1/1 service stop 
        > lanpower slot 1/1 service start 
 
3.3.3. 
On the OS2360 
> Select CONFIGURATION > CLI SCRIPTING > Terminal 
  > Click on Browse 
    > Select 10.130.5.24X (OS2360) 
    > Click on OK 
      > Enter the username/password: admin/switch 
      > Click on OK 
 
You are now connected to the OS2360. Enter the following command to enable the PoE: 
 
         > interfaces 1/1/6 admin-state enable 
        > lanpower slot 1/1 service stop 
        > lanpower slot 1/1 service start 
The Access OmniSwitches are now completely configured. In the next part, we will discover the Stellar Access 
Points in the OmniVista 2500 NMS.  
 4 
Discovering the Stellar Access Points 
 
Discover the Stellar Access Points in the OmniVista 2500 
Add the Stellar Access Points in a new AP Group “APGX” (X = R-Lab Number)  
4.1. 
Registering the Stellar Access Points 
Now, let’s discover the Stellar Access Points.  
 
> Select NETWORK > AP REGISTRATION > Access Points 
  > Select Country/Region = FR-France (selecting your own country code here may lead to compatibility 
problem with the Stellar APs used in this infrastructure! See the WARNING section below to learn why) 
  > Select your Timezone 
  > Click on OK 
 
 
 
 
Warning 
DO NOT CHOOSE THE COUNTRY CODE USA, JAPAN OR ISRAEL AS THE STELLAR ACCESS POINTS USED IN THE 
REMOTE LAB ARE NOT COMPATIBLE WITH THESE COUNTRY CODES. 
 
> Click on Managed AP 
  > Check that 2 APs are displayed (AP1301 & AP1321: 10.7.X… with X = R-Lab number) 
Stop/Start the PoE to force the AP to reboot 
Stop/Start the PoE to force the AP to reboot

<<<PAGE 232>>>
8 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 
IF THEY DON’T APPEAR IN THE MANAGED AP TAB 
 
> Click on Unmanaged AP 
  > Check that 2 APs are displayed (AP1301 & AP1321: 10.7.X… with X = R-Lab number) 
  > Select both 
  > Click on Change to Trust Status  
    > Click on OK 
  > Check that the Operation Status = Successful, then click on OK  
4.2. 
Adding the Stellar Access Points into an AP Group 
 
OmniVista does not manage individual APs. You must first add APs to AP Groups. The attributes configured 
for the AP Group (e.g., Management VLAN, RF Profile) are applied to all APs in the group. 
Once the APs are assigned to a group, you configure the APs in OmniVista (e.g., Notification traps, 
Resource Manager backups) by applying the configuration to the AP Group.  
In OmniVista applications (e.g., Notifications, Resource Manager), rather than presenting the user with 
individual APs when applying a configuration (as is done with AOS Devices), OmniVista presents the user 
with the option of applying a configuration to AOS Devices and/or AP Groups.  
Any configuration applied to an AP Group is applied to all APs in the group. 
 
When an AP initially registers with OmniVista, the AP is placed into a pre-configured “Default” AP Group. 
Let’s begin by creating the AP Group: 
 
> Select NETWORK > AP REGISTRATION > AP Group 
  > Click on the + button  
    > Group name: APGX (X = R-Lab number) 
    > skip all the other parameters, read the Tips section below 
    > Click on Create 
 
 
Tips 
As you can see, several settings can be managed in the AP Group properties. Take the time to learn more about 
each of them by clicking on the Help button  
 
 
 
 
 
 
 
Now, let’s insert the APs in the AP Group:  
 
> Select NETWORK > AP REGISTRATION > Access Points 
> Select both APs  
> Click on 
 then Change Group 
    > Group name: APGX (X = R-Lab number) 
    > Click on Apply 
  > Check the status, then click on OK 
WARNING 
DO NOT ENABLE THE “SSH LOGIN” SETTING

<<<PAGE 233>>>
9 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 5 
Debriefing 
During this lab, we have created the Management VLAN, which contains all the management data used by the 
Access Points. We have also created a “trash” VLAN, which will contain all the “faulty” devices (not 
authenticated, quarantined…). Then, we have enabled the PoE on the OmniSwitches to provide power to the 
Access Points, and the IP Helper feature to redirect the APs DHCP requests to the DHCP Server. And finally, 
we have discovered the Stellar Access Points in the OmniVista 2500 NMS. These Access Points can now be 
managed from the OmniVista 2500 GUI.

<<<PAGE 234>>>
10 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 6 
Troubleshooting 
In this part, we will cover the process to follow if the Stellar AP is not discovered in the OmniVista 2500. We 
will use the exact same infrastructure as above:  
 
 
6.1. 
Troubleshooting the Level 2 
6.1.1. 
Checking the PoE 
Make sure that the PoE is enabled on the port where the Stellar AP is plugged:  
 
OMNISWITCH 
AOS -> show lanpower slot 1/1 
Port Maximum(mW) Actual Used(mW)   Status    Priority   On/Off   Class   Type 
----+-----------+---------------+-----------+---------+--------+-------+---------- 
  1     60000            0       Searching      Low      ON        * 
  2     60000            0       Searching      Low      ON        * 
  6     60000         6800       Powered On     Low      ON        * 
6.1.2. 
Checking the cables 
Make sure that the cables are correctly plugged and recognized:  
 
OMNISWITCH 
AOS -> show interfaces 1/1/6  
Chassis/Slot/Port 1/1/6   : 
 Operational Status     : up, 
 Last Time Link Changed : Thu Oct 17 13:26:55 2019, 
 Number of Status Change: 23, 
 Type                   : Ethernet, 
 SFP/XFP                : N/A, 
 EPP                    : Disabled, 
 Link-Quality           : N/A, 
 MAC address            : 2c:fa:a2:1b:18:58, 
 BandWidth (Megabits)   :     1000,             Duplex           : Full, 
 Autonegotiation        :   1  [ 1000-F 100-F 100-H 10-F 10-H ],

<<<PAGE 235>>>
11 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 Long Frame Size(Bytes) : 9216, 
6.1.3. 
Checking the VLAN(s) 
Then, check that the Management VLAN is set as default VLAN on the port where the Stellar AP is plugged 
(in this example, the Management VLAN is the VLAN 40):  
 
OMNISWITCH 6870 
AOS -> show vlan members port 1/1/6 
  vlan      type        status 
--------+-----------+--------------- 
   40    default     forwarding 
6.2. 
Troubleshooting the Stellar AP  
The Stellar console access is deactivated in Enterprise mode for the application Configuration > CLI 
Scripting > Terminal. 
To activate the SSH console connection on OV2500, go to Network > AP Registration >AP Group, edit the 
AP Group and change the support and root passwords. 
 
 
 
6.2.1. 
Reseting the Stellar AP 
A good way to start the troubleshooting of a Stellar AP is to ensure that it has been reset to its factory 
settings.  
- If you can access to the Stellar AP: 
 
Stellar AP 
  > Plug the AP to a PoE port 
  > Press 6 seconds on the Reset button available at the rear of the AP (until the led blinks red) 
 
- If you can’t access to the Stellar AP, but have access to its Serial port: 
 
PC 
  > Open a serial connection (via a software as Putty, Teraterm…) 
    > Baud rate: 115200 
    > Data bits: 8 
    > Parity: None 
    > Stop bits: 1 
 
  > login: support 
  > password: aos2016 
 
Reset the Stellar AP to its factory settings 
support@AP-0E:E0:~$ ssudo firstboot 
This will erase all settings and remove any installed packages. Are you sure [N/y]? y 
support@AP-0E:E0:~$ ssudo reboot  
6.2.2. 
Checking the Stellar AP Mode (OV/Cluster) 
To register to the OmniVista, the Stellar AP must run in OV mode: 
 
Stellar Serial Console (logged as support) 
support@AP-0E:E0:~$ getmode 
OV 
Use the APs console connections on the desktop and do not change the passwords in the AP Group.

<<<PAGE 236>>>
12 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
6.2.3. 
Checking the Stellar AP DHCP Mode (DHCP/Static) 
The DHCP Server sends the OmniVista IP address to the Stellar AP via a specific option (138/43). To ensure 
that the Stellar AP is in DHCP mode:  
 
Stellar Serial Console (logged as support) 
support@AP-0E:E0:~$ cat /etc/config/network 
 
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
6.2.4. 
Checking the Option 138/43 in the DHCP Server 
Make sure that the option 138/43 has been configured in the DHCP Server, and its value corresponds to 
the OmniVista Server IP address:  
 
 
 
 
Notes 
If at the end of this step, the result of the “getovmode” command is not the IP address of the OmniVista Server 
2500:  
- Launch a tcpdump trace: cd /tmp, then tcpdump -i br-wan -s0 -w trace.pcap 
- Transfer the trace via TFTP on a computer, to open it with Wireshark: tftp -pl trace.pcap 10.130.5.123 
- Check that the option 138 or 43 is available in the DHCP Offer sent to the Stellar AP 
6.2.5. 
Checking the Stellar AP IP Address 
 
Stellar Serial Console (logged as support) 
support@AP-0E:E0:~$ ssudo ifconfig br-wan 
br-wan    Link encap:Ethernet  HWaddr DC:08:56:00:0E:E0 
          inet addr:10.7.0.101  Bcast:10.7.0.127  Mask:255.255.255.224 
          inet6 addr: fe80::de08:56ff:fe00:ee0/64 Scope:Link 
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1 
          RX packets:344756 errors:0 dropped:0 overruns:0 frame:0 
          TX packets:163725 errors:0 dropped:0 overruns:0 carrier:0 
          collisions:0 txqueuelen:0 
          RX bytes:24497756 (23.3 MiB)  TX bytes:27208952 (25.9 MiB)

<<<PAGE 237>>>
13 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
6.2.6. 
Checking the OV information on the Stellar AP 
Once configured in DHCP mode, the Stellar AP should receive the OmniVista IP address information from 
the DHCP server (via the option 138 or 43).  
Make sure that the OmniVista IP address is the correct one on the Stellar AP: 
 
Stellar Serial Console (logged as support) 
support@AP-0E:E0:~$ getovinfo 
10.130.5.50 
6.3. 
Troubleshooting the Level 3 
6.3.1. 
Checking the IP Interface 
Check that the IP interface is correctly configured on the OmniSwitch, and that its status is UP:  
 
OMNISWITCH 6870 
AOS(R6/R8) -> show ip interface 
 Total 6 interfaces 
 Flags (D=Directly-bound) 
 
            Name                 IP Address      Subnet Mask     Status Forward  Device   Flags 
--------------------------------+---------------+---------------+------+-------+---------+------ 
EMP-CMMA-CHAS1                   0.0.0.0         0.0.0.0           DOWN      NO EMP 
Loopback                         127.0.0.1       255.255.255.255     UP      NO Loopback 
int_management                   10.7.0.126      255.255.255.224     UP     YES vlan 40 
6.3.2. 
Pinging the Equipment 
Once the equipment IP configuration checked, make sure that the equipment can ping each other:  
- Ping from the Stellar AP to the OmniVista 2500: 
 
PING FROM THE STELLAR AP TO THE OMNIVISTA 2500  
support@AP-0E:E0:~$ ssudo ping 10.7.0.126 
PING 10.7.0.126 (10.7.0.126): 56 data bytes 
64 bytes from 10.7.0.126: seq=0 ttl=64 time=1.055 ms 
64 bytes from 10.7.0.126: seq=1 ttl=64 time=1.065 ms 
64 bytes from 10.7.0.126: seq=2 ttl=64 time=1.121 ms 
64 bytes from 10.7.0.126: seq=3 ttl=64 time=1.075 ms 
 
- Ping from the OmniVista 2500 Server to the Stellar AP: 
 
OmniVista 2500 Console 
From the Virtual Appliance 
Menu, select [10] Advanced 
Mode 
 
  
 
From the CLI, launch a ping to 
the Stellar AP IP address

<<<PAGE 238>>>
14 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
6.4. 
Discovering the Stellar AP 
To launch a new discovery:  
 
> Open a Web Browser 
  > Type the OV2500 IP address in the URL bar: 10.130.5.5X (X = R-Lab Number) 
    > Username/Password: admin/switch 
 
> Select NETWORK > AP REGISTRATION > Access Points 
  > Click on Managed AP 
      > Check that 2 APs are displayed (AP1301 & AP1321: 10.7.X… with X = R-Lab number) 
 
IF THEY DON’T APPEAR IN THE MANAGED AP TAB 
 
> Click on Unmanaged AP 
  > Check that 2 APs are displayed (AP1301 & AP1321: 10.7.X… with X = R-Lab number) 
  > Select both 
  > Click on Change to Trust Status  
    > Click on OK 
  > Check that the Operation Status = Successful, then click on OK

<<<PAGE 239>>>
15 
Stellar Access Points Discovery in the OmniVista 2500 NMS 
 
 7 
Annex: Configuring the Option 138 
7.1. 
On Windows Server 
 
> Go to Control Panel > Administrative Tools   
  > Double click on DHCP 
    > Right click on IPv4 
      > Select Set Predefined Options… 
 
 
 
> Click on Add…   
  > Name: Stellar-AP 
  > Data type: IP Address 
  > Code: 138 
> Click on OK 
     
> Select <Server FQDN> > Scope > Scope Options  
  > Right click on the main area > Configure Options 
    > Select the option 138 
      > Enter the OmniVista 2500 IP Address 
      > Click on OK

<<<PAGE 240>>>
SSID CREATION
OMNIACCESS STELLAR WIRELESS LAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 241>>>
Upon completion this module, 
you will be able to:
LESSON SUMMARY
• SSID Creation
- At the end of this presentation you will be able to:
Understand the SSID Usage profile
Create a new SSID

<<<PAGE 242>>>
SSID CREATION
• How to create a new SSID?
• WLAN →« SSID » or « WLAN service (expert) »
• SSID
• Wizard driven tool.
• Pre-defined Usage (Guest, Employee, BYOD,…).
• All the configuration is performed from the wizard.
Recommended mode
• WLAN service (expert)
• Manual configuration.
• Profiles, policies, users configured independently and assigned then to the WLAN service.
Limited usage for specific SSIDs.

<<<PAGE 243>>>
SSID

<<<PAGE 244>>>
SSID WIZARD – STEP 1 « CREATE SSID »
• Name the « SSID Service »
• Unique name to identify a wireless service
• Multiple SSID service can share the same SSID name
• Name the SSID
• Unique SSID name broadcasted in the air
• Select the SSID Usage
• Each usage leads to a predefined template
• Depending on the usage selected, one of these 
option can be enabled:
• Enable BYOD Registration
• Use the Captive Portal

<<<PAGE 245>>>
SSID USAGE TEMPLATES
Usage
GuestNetwork
Employee BYOD 
Network
Enterprise 
Network for 
Employees
Protected
Network
Protected
Network for 
Employees
(BYOD))
Captive 
Portal?
SSID Security Level
Captive Portal 
Guest
Open
or MAC
Y
N
Captive Portal 
BYOD
BYOD?
802.1X followed by 
Captive Portal BYOD
802.1X
or MAC followed by 
802.1X 
Y
N
Captive 
Portal?
PSK followed by 
Captive Portal 
Guest
Pre-Shared Key
(PSK)
Y
N
PSK followed by 
Captive Portal BYOD

<<<PAGE 246>>>
SSID WIZARD – STEP 2 « CUSTOMIZE SSID »
• SSID Usage defines the parameters displayed.
• Minimal configuration contains:
• Basic Parameters
• Allowed Band: 2.4GHz, 5GHz, 6GHz
• Optional - Security Settings (Pre-Share Key, Encryption type,…)
• Default VLAN/Network
• VLAN assigned to the SSID
• Optional - ACL/QoS rules applied to the SSID
• Authentication Strategy
• Select the Authentication source in «Advanced Configuration»
(Local Database, External Radius, LDAP/AD)
• Optional - Use the links «Manage Guest Accounts» to create new 
users in the local database 
• Optional – Select the RADIUS server used by the SSID

<<<PAGE 247>>>
SSID WIZARD – STEP 2 « CUSTOMIZE SSID »
• VLAN options:
• Default VLAN
• Single VLAN assigned to the SSID
• VLAN Pooling
• Pool of VLAN assigned to the SSID
• Avoid large broadcast domain with a single VLAN
VLAN 20
VLAN 30
VLAN 40
VLAN 20

<<<PAGE 248>>>
•
QoS :
•
Policy List : Full-Access
•
Bandwidth : 10Mbit/s max
SSID WIZARD – STEP 2 - ACCESS ROLE PROFILE
New User 
« Employee »
Access Role 
Profile
Guest
BYOD
Employee
•
VLAN ID : Employee (20)

<<<PAGE 249>>>
SSID WIZARD – STEP 2 « CUSTOMIZE SSID »
• Based on the SSID Usage, optional strategies:
• Guest Access Strategy
• Configure access attributes for guest users:
• Link Customize Portal Page to change the appearance of the 
Captive Portal
• Customize: Set the Login method (login & password, Access 
code, Terms & Conditions), self registration.
• BYOD Access Strategy
• Configure access attributes for BYOD users:
• Link Manage Employee Account creates new users in the 
local database
• Link Customize Portal Page to change the appearance of the 
Captive Portal
• Customize: Set the Portal Page template, the Employee 
Database used for the authentication, URL Redirection on 
success

<<<PAGE 250>>>
SSID WIZARD – STEP 3 « AP GROUP ASSIGNMENT & 
SCHEDULE »
• Schedule the SSID broadcast: when is the SSID 
broadcasted by the AP?
•
Always available by default
• Apply the SSID to one or multiple AP Group(s)

<<<PAGE 251>>>
WLAN SERVICE - PREREQUISITE
Click on the image above to visualize the video

<<<PAGE 252>>>
WLAN SERVICE - ENTERPRISE
Click on the image above to visualize the video

<<<PAGE 253>>>
WLAN SERVICE - MAC
Click on the image above to visualize the video

<<<PAGE 254>>>
AUTHENTICATION

<<<PAGE 255>>>
AUTHENTICATION SECURITY LEVEL - REMINDER
• Open + Captive Portal
• Cons: No Security
• Pros: Followed by Captive Portal, any type of device can be 
authenticated
• MAC authentication
• Cons: MAC can be spoofed, no traffic encryption
• Pros: Available for basic wireless devices (printers, scanners,…)
• WPA/WPA2/WPA3 Personal = Pre-Shared Key (PSK)
• Pros: Easy set up, strong keys can be difficult to hack
• Cons: But all keys can be hacked or stolen (key shared by all 
users)
• WPA/WPA2/WPA3 Enterprise = 802.1X
• Pros: Strongest security, ease of Management, scalability
• Cons: More configuration during initial setup (server, users)
Level of Trust
Authentication Method

<<<PAGE 256>>>
SECURITY – WPA3
◼Wi-Fi Alliance new Security Standard
◼Released in 2018, available on new end-user devices in 2019
◼All Stellar APs are WPA3 compatible with software upgrade
WLAN PERSONAL
◼WPA/WPA2-Personal PSK (Pre-Shared Key) 
replaced by WPA3-Personal SAE (Simultaneous 
Authentication of Equals)
⚫Stronger Encryption Key (128 bits)
⚫Offline dictionary attack resistance
⚫No additional complexity to connect (user side)
WLAN ENTERPRISE
◼WPA/WPA2-Enterprise replaced by WPA3-
Enterprise
⚫Optional 192-bit security mode (CNSA option)
□
CNSA enabled: Only wpa3 client authorized on the 
SSID
□
CNSA disabled: wpa2 or wpa3 clients authorized on 
the SSID
□
CNSA option not enabled on AP1101 only

<<<PAGE 257>>>
WLAN SERVICE (EXPERT)

<<<PAGE 258>>>
PROFILE AND SERVICE LIST 
AP Group
RF Profile
Specific 
RF Profile
WLAN Service
SSID
Authentication
•
Open
•
Personal
•
Enterprise
Map to 
VLAN ID
AAA 
Profile
802.1X or 
MAC
Authentication 
Strategy
Associate to 
SSID name
Assign
802.1X or MAC
Assign
Assign
Assign
Access 
Role 
Profile
Access Policy

<<<PAGE 259>>>
WLAN SERVICE (EXPERT)
• WLAN Service is used to create specific 
SSIDs not listed in the Simple SSID 
tools. It contains the following 
attributes
• Basic
• Enable SSID
• Hide SSID
• Set the Allowed Bands (2.4G , 5G)
• Security Settings
• Level (Open, Enterprise, Personal)
• MAC Auth
• AAA Profile
• Classification Status
• MAC Pass Alt
• Default Access Role Profile
• Advanced 
• QoS Settings

<<<PAGE 260>>>
WLAN SERVICE SECURITY SETTINGS
• In the Security Settings Section you must choose a Security Level
• Open, Enterprise, Personal
• You must also set a Default Access Role Profile
• A default WLAN Profile already exists
• You can create additional Profiles as needed
• Optional Security Settings are
• MAC Auth
• AAA Profile
• Classification Status
• MAC Pass Alt

<<<PAGE 261>>>
WLAN SERVICE SECURITY SETTINGS PARAMETERS
• The input fields for the Security Settings changes 
depending on which security Level you choice
• Enterprise
• Need to Specify Encryption Type
• DYNAMIC_WEP, WPA_TKIP, WPA_EAS, WPA2__TKIP, WPA2_AES, 
WPA3_AES 
• 802.1x Bypass is option field
• MAC Allow EAP is option
• AAA Profile is a mandatory fields
• Personal
• Encryption type is Mandatory
• WPA_PSK_TKIP, WPA_PSK_AES, WPA_PSK_AES_TKIP, WPA2_PSK_TKIP, 
WPA2_PSK_AES, WPA3_SAE_AES, WPA3_PSK_SAE_AES
• Passphrase is mandatory
• Key Format
• AAA Profile is Mandatory

<<<PAGE 262>>>
WLAN SERVICE AND ACCESS ROLE PROFILE
• The field Default Access Role Profile is mandatory in the WLAN Service
• An Access Role Profile contains the various UNP properties for the users assigned to this 
profile
• QOS Policy List
• Captive Portal Authentication
• Bandwidth Controls
• The Default Access Role Profile is assigned to the VLAN ID of the SSID
• Ex: If Guest SSID uses the VLAN 10 →Assign the Access Role Profile to the VLAN 10

<<<PAGE 263>>>
WLAN SERVICE AND AAA SERVER PROFILE
• An AAA Server Profile is mandatory when the security level is set to Enterprise or Personal
• The AAA Server Profile defines
• 802.1x Authentication Servers
• MAC Authentication Servers
• Captive Portal Authentication Servers
• Accounting Servers
• The Default UPAM Server can be chosen by default

<<<PAGE 264>>>
EXTERNAL CAPTIVE PORTAL INTEGRATION
• Leading hotel groups, large retail chains, restaurant chains, and shopping malls re-enforce 
their brands by leveraging their existing Wi-Fi networks to provide better in-door mobile 
experiences.
• Both Stellar Express and Enterprise supports External Captive Portal with External Captive 
Portal and MAC authentication enabled.
• WLAN Service
• Access Role Profile
CONFIGURATION REQUIRED 
Both External Captive Portal and MAC authentication enabled
⚫If MAC authentication fails : Captive Portal Enforcement
⚫If MAC authentication succeeds : No Captive Portal enforcement

<<<PAGE 265>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 266>>>
S S I D  C R E AT I O N  – A D VA N C E D  O P T I O N S
OMNIACCESS STELLAR
WIRELESS LAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE

<<<PAGE 267>>>
Upon completion this module, 
you will be able to:
LESSON SUMMARY
• SSID Creation – Advanced options
- At the end of this module, you will be able to:
Understand and configure the advanced options of the SSID 
wizard.

<<<PAGE 268>>>
DEFAULT VLAN/NETWORK
• Access Role Profile configuration
• Network: 
• VLAN ID
• Tunnel ID and Tunnel Termination Switch (TTS) IP
• Walled Garden
• Wireless Client Social Login
• Wireless client authenticates through a social media vendor (FaceBook WiFi or Google) 
• Whitelist Domain
• Allow a wireless client to access the URLs of the whitelist without authentication
• Advanced Access Role Configuration
• Location/Period Policy
• Can a client access the network? Based on the time/date and location of the client
• Bandwidth Control Setting
• Bandwidth allocated per user

<<<PAGE 269>>>
ADVANCED WLAN SERVICE CONFIGURATION
• Basic
• Hide SSID
• UAPSD
• Unscheduled Automatic Power Save Delivery is a QoS facility defined in 
IEEE 802.11e that extends the battery life of mobile clients
• Security
• Classification Status
• Role assignement if 802.1X/MAC authentication does not return a role
• Client Isolation
• Traffic between clients on the same AP (in the SSID) is blocked

<<<PAGE 270>>>
ADVANCED WLAN SERVICE CONFIGURATION 
• QoS Setting
• Bandwidth Contract
• Bandwidth limitation shared for all users, per radio
◼Broadcast Optimization
⚫Broadcast Key rotation
Only applicable for Enterprise 
A unicast key (PTK) and a group key (GTK) are used 
to encrypt traffic
Rotate the keys periodically to avoid key cracking
Default period: 15 min – Range 1 min – 24 hours
⚫Broadcast Optimization
Broadcast Filter All
Drop all broadcast packets except DHCP & ARP.
Broadcast Filter ARP
Convert broadcast ARP to unicast ARP
Recommended if no specific multicast application is 
used

<<<PAGE 271>>>
ADVANCED WLAN SERVICE CONFIGURATION 
• Multicast Optimization
• Enabling Multicast Optimization = Convert multicast to unicast
• Unicast key PTK used
• Uses the highest data rate (unicast)
• Limited to IP Multicast and IGMP Snooping traffic
• Multicast Optimization automatically stops on high load
• Upper limit of multicast optimization: 
Channel Utilization (RF environment too poor to have optimization) : default value 90%
Number of Clients (CPU load too high to support optimization) : default value 6 (maximum number of high-
throughput clients)

<<<PAGE 272>>>
ADVANCED WLAN SERVICE CONFIGURATION 
• WMM QoS
• Four categories
• QOS treatment per category
• Uplink 802.1p/DSCP
• Downlink 802.1p/DSCP
DSCP=56
BACKGROUND
DSCP = 8, 16 ?
VIDEO
DSCP = 32, 40 ?
VOICE
DSCP = 48, 56 ?
BEST EFFORT
DSCP = 0, 24 ?
DOWNLINK DSCP
DSCP=56
BACKGROUND
DSCP = 8 
UPLINK DSCP
VIDEO
DSCP = 32 
BEST EFFORT
DSCP = 0 
VOICE
DSCP = 46 
DSCP=46
Ex: DSCP Mapping

<<<PAGE 273>>>
WLAN SERVICE - WMM QOS RECOMMENDATION
• Recommended Settings
• Default OV Settings
WMM
802.1p
DSCP
Best Effort
0
0
Background
2
18 - AF 21
Voice
5
46 – EF
Video
4
34 – AF41
WMM
802.1p
DSCP
Best Effort
0,3
0x00, 0x18 – 0, 24
Background
1,2
0x08, 0x10 – 8, 16
Voice
6,7
0x30, 0x38 – 48, 56
Video
4,5
0x20, 0x28 – 32, 40

<<<PAGE 274>>>
HOTSPOT 2.0 & WIFI4EU
•
WiFi4EU
• European Union Initiative, to provide free WiFi access 
to citizen in public venues
• Networks with WiFi4EU SSID use an HTTPS Captive 
Portal
• Session timeout should be configurable up to 12 hours
◼Insecure, overcrowded public WiFi
◼Offload client traffic from 3G/4G to WiFi services
◼Deliver seamless and secure network
(WPA2 or WPA3 Enterprise) for clients in public spaces
◼Hotspot 2.0 is a WLAN Service option
◼Stellar Access Point support
⚫802.11u (GAS/ANPQ)
⚫EAP-SIM / EAP-AKA
Mobile 
Device
Passpoint 
APs
Switch
ANPQ and EAP
RADIUS
Hotspot 2.0 Network
NAT
DHPC
Firewall
Home 
AAA 
Server
Home 
HLR
ANPQ 
Server
MAP
Client device credentials verified 
against home operator’s HLR

<<<PAGE 275>>>
HOTSPOT 2.0 & WIFI4EU - CONFIGURATION
• Hotspot 2.0
• WPA-2 Enterprise SSID -> Advanced WLAN 
configuration
• WIFI4EU
•
Guest SSID -> Guest Access Strategy

<<<PAGE 276>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 277>>>
USER ROLE AND BANDWIDTH CONTROL
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 278>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand a user role
• Configure the bandwidth contracts and 
understand the precedence system
• Configure the Web Content Filtering

<<<PAGE 279>>>
USER ROLE

<<<PAGE 280>>>
USER ROLE - OVERVIEW
• User Role = Policy List
• List of Policy Rules (QoS, ACLs) 
• Action can be
• Accept/drop
• Bandwidth control
• Priority, 802.1p, DSCP marking
• Application Policy Rules (DPI)
• In Application Visibility, application/application group Policy Rules 
can be set in a Policy List
• Enforcement is bidirectional
• Policy List Assignment
• From RADIUS 
• From Access Role Profile (Default Policy List)
• Built-in roles
• Redirection (UPAM)
• Unauthorized (Time and Location based policy)
• Rule : "http-traffic"
✓Action: Accept
• Rule: "Network-traffic"
✓Action: Deny
• Rule: "Guest-speed"
✓Action: 1Mb/s
• Rule: "Guest-priority"
✓Action: 802.1p=3
Policy List:
"Policy-Guest"
Access Role 
Profile

<<<PAGE 281>>>
USER ROLE - CONSIDERATIONS
• Policy List configuration
• From the application Unified Access – Unified Policy
• From the SSID wizard – in Default WLAN Support “ACL/QoS”
• AP support
• Full Application Visibility signature kit (~2000 applications) 
•
Creation of Policy List, based on the L7 Application (Google, Facebook, …)
• The Application Visibility feature is supported on: 
•
OS6860N & OS6870 switches
• All Stellar APs models (except AP1101 and AP1201H)

<<<PAGE 282>>>
BANDWIDTH CONTROL

<<<PAGE 283>>>
USER ROLE – BANDWIDTH CONTROL
• Bandwidth contract at SSID level
• Configured in “Advanced WLAN Service Configuration”
• Bandwidth shared for all user, per radio
• Bandwidth contract at Access Role Profile level
• Configured in “Advanced Access Role Configuration”
• Bandwidth assigned per user of the profile – Not shared
• Bandwidth contract at Role level
• A Policy List (ACL/QoS) can restrict the Bandwidth as an action
• Bandwidth limited by the ACL/QoS Rule

<<<PAGE 284>>>
USER ROLE – USER BANDWIDTH CONTROL PRECEDENCE
Matches a 
DPI 
application
in the Policy
List?
N
User 
Traffic
Application Specific 
BW Enforcement 
as per DPI Rule
Y
N
ACL Specific BW 
Enforcement 
as per Policy List
Shared BW Enforced
as per WLAN Service/SSID
Other User 
Traffic
Matches 
an ACL in 
the Policy 
List ?
User Role /Policy List
Per User & Application BW Control
Other User 
Traffic
Access Role 
set with BW 
Control ?
User Context
• Role / Policy List
• Access Role Profile
• SSID
Access Role Profile
Per User BW Control
WLAN Service / SSID
All Users shared BW
SSID set with
BW Control ?
Y
Y
N
User BW 
Enforcement 
as per Access Role 
Profile
No BW
Limitation
N
Y
All User 
Traffic

<<<PAGE 285>>>
WEB CONTENT FILTERING - WCF

<<<PAGE 286>>>
WEB CONTENT FILTERING - WCF
Stellar AP DNS Snooping
DNS request
FQDN :
www.facebook.com
Client assigned
to Address
Role Profile
« Guest »
1
FQDN filtered ?
2
FQDN 
category ?
« Social 
Network »
3
ARP
Guest
Social Network
Reject
P2P
Reject
ARP
Employee
Social Network
Accept
P2P
Reject
Web Content Filtering
4
Send action to AP
5
Create Block ACL rule
to IP of the FQDN
6
1
Get Allow/Block status
2
Categorization of FQDN
3
Get status based on ARP/Category
4
Send Allow/Block status to Stellar AP
5
ACL allow/block IP destination
6
STELLAR AP
OMNIVISTA
BRIGHTCLOUD SDK

<<<PAGE 287>>>
WEB CONTENT FILTERING - CONFIGURATION
• Activate WCF
• Per AP Group
• All Stellars AP from the AP Group have WCF activated
•
Edit the AP Group
• Or per Access Point
• Select the Stellar AP, Edit > Web Content Filtering
• Configure DNS
• No DNS -> WCF not in Service
• In the OmniVista CLI, configure DNS
• DNS -> WCF in Service
Not supported:
•
AP1101
•
AP1201H

<<<PAGE 288>>>
WEB CONTENT FILTERING - CONFIGURATION
• Assign WCF profile to Access Role Profile
• Unified Access > Unified Profile > Template > Access 
Role Profile
• Edit the Access Role Profile 
• Of the SSID
• Or Enforced Post-authentication
• Apply the Access Role Profile to the AP Group
• One WCF profile per Access Role Profile
• WCF Profile creation
• UPAM > Web Content Filtering
• Multiple categories
• Action: Accept or Reject

<<<PAGE 289>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 290>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Creation of a Secured Employee SSID 
Objective 
✓ Learn how to create a secured Employee SSID 
Contents 
1 
Briefing ......................................................................................... 2 
2 
Creating the Service VLAN & IP Interface ................................................. 3 
2.1. Creating the Service VLAN ........................................................................ 3 
2.2. Employee IP Interface ............................................................................. 4 
3 
Creating the Employees SSID ................................................................ 4 
3.1. Creating the EmployeesX SSID .................................................................... 5 
3.2. Creating an Employee Account ................................................................... 5 
3.3. Back to… Creating the EmployeesX SSID ........................................................ 6 
3.4. Assigning the SSID to the AP Group .............................................................. 6 
4 
Testing the Employees SSID .................................................................. 6 
4.1. Setting Up the Linux Client to Connect to the EmployeesX SSID ............................ 6 
4.2. Verifying the connection .......................................................................... 7 
5 
Monitoring the Connections .................................................................. 8 
5.1. UPAM Monitoring .................................................................................... 8 
5.2. WLAN Menu .......................................................................................... 9 
5.2.1. Wireless Client List ......................................................................................... 9 
5.2.2. Client Session ............................................................................................... 9 
6 
Debriefing .................................................................................... 10

<<<PAGE 291>>>
1 
Creation of a Secured Employee SSID 
 
7 
Troubleshooting ............................................................................. 11 
7.1. Troubleshooting the Stellar AP .................................................................. 11 
7.1.1. Checking the wireless configuration ................................................................... 11 
7.1.2. Checking the Wi-Fi Channel ............................................................................. 12 
7.1.3. Checking the interface transmission power .......................................................... 12 
7.1.4. Checking the interface bitrate ......................................................................... 12 
7.2. Client Information ................................................................................. 13 
7.2.1. Listing the client(s) associated with the AP .......................................................... 13 
7.2.2. Checking the access logs of a specific client ......................................................... 14 
7.2.3. Checking the 802.1x Authentication ................................................................... 14 
8 
Annex: WLAN Service (Expert) ............................................................ 16 
8.1.1. Creation of a WLAN Service profile (SSID) ............................................................ 17 
8.1.2. AAA Server Profile ........................................................................................ 17 
8.1.3. Access Role Profile ....................................................................................... 18 
8.1.4. Apply the Access Role Profile to the Stellar APs ..................................................... 18 
8.1.5. Authentication Strategy ................................................................................. 19 
8.1.6. Access Policy configuration ............................................................................. 20

<<<PAGE 292>>>
2 
Creation of a Secured Employee SSID 
 
 1 
Briefing 
Now that all the devices have been discovered in the OmniVista 2500 NMS, let’s create multiple SSIDs 
(employee, guest…). In this first lab, we will focus on how to create a secured Employee SSID. 
 
 
 
 
 
Creating an SSID can be decomposed in several steps: 
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 293>>>
3 
Creation of a Secured Employee SSID 
 
1. Create the VLAN 20. This VLAN will service the SSID “EmployeeX” (X = R-Lab Number). It will be 
tagged from the Access Points to the Access OmniSwitches (2360 and 6360), and over the link to the 
OmniSwitch 6870.  
2. Create the SSID and configure its options. 
 2 
Creating the Service VLAN & IP Interface 
Before creating the Employee SSID, let’s create the VLAN and IP interface that will be associated to this SSID 
EmployeeX (X= R-Lab number) and that will carry the employee traffic.  
2.1. 
Creating the Service VLAN 
 
 
Create the VLAN 20 on the OmniSwitches 6870, 6360 and 2360. 
 
 
 
To create the VLAN 20 on both OmniSwitches, we will use the OmniVista 2500 VLAN Manager feature: 
 
> Select CONFIGURATION > VLANS > VLAN 
  > Click on Create VLAN by Devices button 
 
1. Devices Selection 
  > VLAN Overwrite: ENABLED 
  > VLAN IDs: 20 
  > VLAN(s) Description: EMPLOYEES 
    > Click on the Add/Remove Devices 
      > Click on Add All 
      > Click on OK  
    > Click on Next 
 
2. VLAN Configuration 
  > Check that Admin Status = Enabled 
  > Click on Next  
 
3. Default Port Assignment 
  > Skip this step (click Next) 
 
 4. Q-Tagged Port Assignment 
> For the OS6870, click on Add Port 
    > Select the ports 1/1/3 & 1/1/8 
    > Click on OK  
 
  > For the OS6360, click on Add Port 
    > Select the ports 1/1/3 & 1/1/6 
    > Click on OK  
  > For the OS2360, click on Add Port 
OS6870

<<<PAGE 294>>>
4 
Creation of a Secured Employee SSID 
 
    > Select the ports 1/1/8 & 1/1/6 
    > Click on OK 
  > Click on Next 
 
5. Review 
  > Review the information 
  > Click on Create 
 
 
Tips 
The VLANs can also be created on the OmniSwitches via command lines (CLI). Hence, the VLAN Manager feature 
can be very interesting to use if the infrastructure is composed of several OmniSwitches, and the same VLANs 
must be created on some/all of them.  
2.2. 
Employee IP Interface 
The core OmniSwitch 6870 is pre-configured with an IP interface 10.7.X.62/27 for the VLAN Employee.  
This IP interface is required to forward the DHCP requests from the clients to the DHCP server. 
 
 
The IP interface “int_employee” is pre-configured on the OmniSwitch 6870. 
 
 3 
Creating the Employees SSID 
Now that we have the Employee VLAN and the associated IP interface, let’s create the Employee SSID:

<<<PAGE 295>>>
5 
Creation of a Secured Employee SSID 
 
3.1. 
Creating the EmployeesX SSID 
 
 
Create the SSID EmployeesX (X = R-Lab Number) 
 
> Select WLAN > SSIDs > SSIDs 
  > Click on the + button 
    > SSID Service Name: EmployeesX (X = R-Lab number) 
    > SSID: <filled automatically> 
    > Usage: Enterprise Network for Employees (802.1X) 
    > Click on Create & Customize 
 
 
Notes > About the “Usage” 
During the SSID creation, a “Usage” is asked. When you select a Usage, relevant related default configurations 
(Access Policy, Authentication Strategy, …) are automatically created.  
Of course, these configurations can be customized. Check the OV2500 dedicated Help for more information.  
 
  > Allowed Band: 2.4GHz and 5GHz 
  > Encryption Type: WPA3_AES 
 
 
Tips > Help Menu 
As you can see, several settings can be managed in the SSID Creation properties. Take the time to learn more 
about each of them by clicking on the Help button   
 
 
Notes > UPAMRadiusServer 
In this lab, for all the types of authentication, we will use the UPAM platform (Unified Policy Authentication 
Manager) embedded in the OmniVista 2500.  
UPAM is a unified access management platform for both AOS Switch Series devices and Stellar AP Series 
devices. UPAM supports both captive portal server and RADIUS server; and can be used to implement multiple 
authentication methods, such as MAC authentication, 802.1X authentication, and captive portal authentication. 
 
Authentication Strategy   
  > RADIUS Server: UPAMRadiusServer 
  > Click on Manage Employee Accounts 
3.2. 
Creating an Employee Account 
 
 
Create the Employee account 
 
> Click on the + button 
  > Username: Employee  
  > Password: password 
  > Repeat Password: password 
  > Click on Create 
> Click on Close 
 
 
Tips > Importing Employee Accounts Information 
You can automatically import a xls/csv/xlsx file containing Employee Account information 
by clicking on the Import button at the top of the screen. You can also download a template by 
clicking on the import button then clicking on the template Download button.

<<<PAGE 296>>>
6 
Creation of a Secured Employee SSID 
 
3.3. 
Back to… Creating the EmployeesX SSID 
 
Default VLAN/Network 
  > VLAN ID: 20 
> Click on Save and Apply to AP Group 
3.4. 
Assigning the SSID to the AP Group 
 
 
Assign the freshly created SSID EmployeesX to the AP Group APGX created in the 
previous lab 
 
Now that the SSID EmployeeX has been created, the last step consists in assigning it to one or several AP 
Group(s): 
 
AP Group Assignment and Schedule 
> Click on Change Selection 
  > Remove default group from the SELECTED tab 
  > Move APGX (X = R-Lab Number) from AVAILABLE to SELECTED 
  > Click on OK 
> Click on Apply 
> Check the result on the page that is displayed 
 
 
Tips > Setting a Schedule 
By default, the availability schedule for AP Groups is set to "Always Available". However, you can schedule 
availability for specific times/days of the week. You can set the same availability schedule for all selected AP 
Groups, or set different schedules for each group. 
 
Now that we have finished the configuration of the SSID, let’s test it! 
 4 
Testing the Employees SSID 
 
 
Test the EmployeesX SSID by connecting on it via the Employee account 
4.1. 
Setting Up the Linux Client to Connect to the EmployeesX SSID 
Connect to the SSID EmployeesX: 
 
StellarClientX Raspberry Pi 
Left-click on the 
 icon 
(top right) 
 
Select the SSID EmployeesX 
(X = R-Lab Number) 
Check under “More Networks” 
if it is not displayed.

<<<PAGE 297>>>
7 
Creation of a Secured Employee SSID 
 
 
Configure the SSID parameters 
with: 
 
Authentication: ProtectedEAP 
Check No CA certificate 
PEAP version: Automatic 
Inner Auth: MSCHAPv2 
 
Enter the credentials: 
Username: Employee 
Password: password 
 
Click on Connect 
 
A Notification informs you 
that the client is connect to 
the SSID 
 
4.2. 
Verifying the connection 
From the Stellar Wireless Client, check that the connection has been successfully established:  
- The IP Address of the Wi-Fi network card should be in the 10.7.X.32/27 range  
- Ping the DHCP Server (10.130.5.7) and the OmniVista 2500 (10.130.5.5X)  
 
Open a terminal with the icon 
 (top left corner). 
Enter the commands:

<<<PAGE 298>>>
8 
Creation of a Secured Employee SSID 
 
 
 
 
 5 
Monitoring the Connections 
 
 
Display the EmployeesX authentication record  
5.1. 
UPAM Monitoring 
The UPAM platform (Unified Policy Authentication Manager) is embedded in the OmniVista 2500 NMS. This 
module is used to implement authentication (MAC authentication, 802.1x, Captive Portal…) 
 
The Authentication Record Screen displays authentication information for all devices authenticated 
through UPAM:  
 
> Select UPAM > AUTHENTICATION > Authentication Record 
 
 
 
 
In the Authentication Record List information, find the Stellar Access Point where your 
Client Virtual machine (StellarClientX) is connected.   
 
 
Notes > Client associated to a Stellar Access Point 
The information asked in the question above can also be found in the WLAN > CLIENT > Client List 
menu. Go check it out! 
 
 
Tips > Employee Account Creation 
Do you remember the Employee account that you have created? You have done it via a shortcut, during the 
SSID creation process. This shortcut leads to the … UPAM > Authentication > Employee Account menu! Go and 
have a look at this menu. You will find the Employee account that you have created previously. From there, 
you can easily create a new Employee account.  
 
Another interesting feature that the OmniVista 2500 NMS offers is the ability to locate the AP, Switch 
and/or slot/port that is directly connected to a user-specified station: it is the Locator application.

<<<PAGE 299>>>
9 
Creation of a Secured Employee SSID 
 
5.2. 
WLAN Menu 
5.2.1. 
Wireless Client List 
The Wireless Client List Screen displays real time information for wireless clients associated with APs. By 
default, the Distribution of Clients per AP chart at the top of the screen provides a graphical overview of 
the number of clients associated with each AP: 
 
> Select WLAN > Client > Client List 
 
 
From the Client List page, find on which Stellar Access Point the account Employee is 
connected 
5.2.2. 
Client Session 
The Wireless Client Session Screen displays information about current wireless clients associated with APs. 
By default, all wireless client sessions are displayed in the list. 
 
> Select WLAN > Client > Client Session

<<<PAGE 300>>>
10 
Creation of a Secured Employee SSID 
 
 6 
Debriefing 
During this lab, you have learned how to create a secured Employee SSID, and an Employee account. You 
have also used the OmniVista 2500 features to get more information about the account that are connected to 
the Employee SSID.

<<<PAGE 301>>>
11 
Creation of a Secured Employee SSID 
 
 7 
Troubleshooting 
In this part, we will cover the process to follow if there is an issue regarding the connection to an Employee 
SSID (802.1x). We will use the exact same infrastructure as in the lab:  
 
 
 
Notes > Before Beginning  
Before beginning this part, we assume that all the steps available in this lab have been followed correctly and 
checked: SSID creation, employee account creation… 
7.1. 
Troubleshooting the Stellar AP 
The Stellar console access is deactivated in Enterprise mode for the application Configuration > CLI 
Scripting > Terminal. 
To activate the SSH console connection on OV2500, go to Network > AP Registration >AP Group, edit the 
AP Group and change the support and root passwords. 
 
 
 
 
 
 
7.1.1. 
Checking the wireless configuration 
 
Use the APs console connections on the desktop and do not change the passwords in the AP Group.

<<<PAGE 302>>>
12 
Creation of a Secured Employee SSID 
 
support@AP-0E:E0:~$ iwconfig 
[…] 
Ath001    IEEE 802.11ng  ESSID:"Employees0" 
          Mode:Master  Frequency:2.437 GHz  Access Point: DC:08:56:00:0E:E1 
          Bit Rate:192 Mb/s   Tx-Power=17 dBm 
          RTS thr:off   Fragment thr:off 
          Power Management:off 
          Link Quality=94/94  Signal level=-43 dBm  Noise level=-95 dBm 
          Rx invalid nwid:68  Rx invalid crypt:0  Rx invalid frag:0 
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0 
 
eth1      no wireless extensions. 
 
ath101    IEEE 802.11ac  ESSID:"Employees0" 
          Mode:Master  Frequency:5.22 GHz  Access Point: DC:08:56:00:0E:E9 
          Bit Rate:800 Mb/s   Tx-Power=19 dBm 
          RTS thr:off   Fragment thr:off 
          Power Management:off 
          Link Quality=47/94  Signal level=-77 dBm  Noise level=-95 dBm 
          Rx invalid nwid:101  Rx invalid crypt:8  Rx invalid frag:0 
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0 
[…] 
7.1.2. 
Checking the Wi-Fi Channel 
To check which channel is used (ex. ath01 interface): 
 
support@AP-0E:E0:~$ iwlist ath001 channel 
ath01     57 channels in total; available frequencies: 
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
7.1.3. 
Checking the interface transmission power 
 
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
          Current Tx-Power=17 dBm       (50 mW) 
7.1.4. 
Checking the interface bitrate  
 
support@AP-0E:E0:~$ iwlist ath001 bitrate 
ath01     12 available bit-rates : 
          1 Gb/s 
          2 Gb/s 
          5.5 Gb/s 
          11 Gb/s 
          6 Gb/s 
          9 Gb/s 
          12 Gb/s

<<<PAGE 303>>>
13 
Creation of a Secured Employee SSID 
 
          18 Gb/s 
          24 Gb/s 
          36 Gb/s 
          48 Gb/s 
          54 Gb/s 
          Current Bit Rate:192 Mb/s 
7.2. 
Client Information 
7.2.1. 
Listing the client(s) associated with the AP 
It is possible to list:  
- All the clients associated with the AP: 
 
support@AP-0E:E0:~$ ssudo sta_list 
SSID:Employees0 
 
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX             
d4:6e:0e:18:60:38  10.7.0.37                                      89              14869   66489      
FREQ          AUTH     Final_role                          VLANID  TUNNELID  FARENDIP 
2.4GHz       802.1X    __Employees0                          20     0 
 
- All the clients associated with a specific interface (ex. ath01 corresponding to the SSID Employees0 in 
2.4 Ghz):  
 
support@AP-0E:E0:~$ ssudo wlanconfig ath001 list 
ADDR               AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE  TXSEQ  RXSEQ  CAPS XCAPS         
d4:6e:0e:18:60:38    1    6  72M     72M   63      62      67    0      0   65535  EPSs  cORI           
 
ACAPS     ERP    STATE MAXRATE(DOT11) HTCAPS VHTCAPS ASSOCTIME    IEs   MODE                   PSMODE    
0         f              0               P             0gR 00:03:20  RSN WME IEEE80211_MODE_11NG_HT20    
 
RXNSS TXNSS 
0 1 1  
  
 Minimum Tx Power                : 5 
 Maximum Tx Power               : 18 
 HT Capability                  : Yes 
 VHT Capability                 : No 
 MU capable                     : No 
 SNR                            : 63 
 Operating band                 : 2.4 GHz 
 Current Operating class        : 0 
 Supported Rates                : 2  4  11  12  18  22  24  36  48  72  96  108  
 
- The parameters sent from the AP to the Wi-Fi Client(s):  
 
support@AP-83:60:~$ ssudo wam_debug sta_list 
{ 
        "status": "Success!!!", 
        "wlanServiceData": [ 
                { 
                        "iface": "ath01", 
                        "ssid": "Employees0",                               SSID Name 
                        "freq": "2.4GHz",                                   Frequency 
                        "security": "Enterprise(WPA3_AES)",                 Security  
                        "wlanService": "Employees0",                        Assoc. WLAN Service 
                        "staData": [ 
                                { 
                                        "staMAC": "d4:6e:0e:18:60:38",      Wi-Fi Client MAC@ 
                                        "staIP": "10.7.0.37",               Wi-Fi Client IP@ 
                                        "staGlobalIPv6": "::", 
                                        "staLocalIPv6": "::", 
                                        "associationTime": 473,             Assoc. Time (seconds) 
                                        "mappingType": 0, 
                                        "assignedVLAN": 20,                 Wi-Fi Client Assigned VLAN 
                                        "assignedAR": "__Employees0",       Wi-Fi Client Assigned ARP 
                                        "assignedPL": "", 
                                        "macAuthResult": "",

<<<PAGE 304>>>
14 
Creation of a Secured Employee SSID 
 
                                        "ARFromMACAuth": "", 
                                        "PLFromMACAuth": "", 
                                        "redirectURLFromMACAuth": "", 
                                        "ARFrom8021xAuth": "", 
                                        "PLFrom8021xAuth": "", 
                                        "redirectURLFrom8021xAuth": "", 
                                        "CPAuthResult": "FAILED", 
                                        "ARFromCPAuth": "", 
                                        "PLFromCPAuth": "", 
                                        "ARFromRoaming": "", 
                                        "PLFromRoaming": "", 
                                        "redirectURLFromRoaming": "", 
                                        "classificationMatched": "none" 
                                } 
[…] 
 
7.2.2. 
Checking the access logs of a specific client 
Find the MAC address of the client (ex. d4:6e:0e:18:60:38), then: 
 
support@AP-0E:E0:~$ cat /proc/kes_syslog | grep “d4:6e:0e:18:60:38” 
7.2.3. 
Checking the 802.1x Authentication 
 
 
Notes > Before Beginning  
Before beginning this part, we assume that all the settings on the Client side (802.1x enabled, credentials 
correct…) and OmniVista 2500 side (account created, UPAM settings checked…) have been verified (if not sure, 
go back to the client settings instructions available in this lab) 
 
- Check that the Radius configuration and AAA server profile have been correctly retrieved by the Stellar 
AP: 
 
support@AP-83:60:~$ cat /var/config/wlanservice.conf 
{ 
        "WLANService":[ 
                { 
                        "wlanDeviceConfigType":"SSIDs", 
                        "upstreamBurst":0, 
                        "maxClientsPerBand":64, 
                        "downstreamBandwidth":0, 
                        "multicastOptimization":"enable", 
                        "macAuthPassProfileName":"", 
                        "wepKeyIndex":null, 
                        "broadcastKeyRotation":"disable", 
                        "dscpMappingEnable":"enable", 
                        "clientsNumber":6, 
                        "minBasicDataRate5G":6000, 
                        "dot1pUplinkBestEffort":0, 
                        "bypassStatus":"disable", 
                        "dot1pDownlinkVideo":[ 
                                4, 
                                5 
                        ], 
                        "minSupportedDataRate24GStatus":"disable", 
                        "downstreamBurst":0, 
                        "a_msdu":"enable", 
                        "e0211gClientSupport":"enable", 
                        "broadcastFilterAll":"disable", 
                        "defaultARPName":"__Employees0", 
                        "dot1pDownlinkBackground":[ 
                                1, 
                                2 
                        ], 
                        "essid":"Employees0", 
 
  
 
    […]

<<<PAGE 305>>>
15 
Creation of a Secured Employee SSID 
 
                        "operationName":null, 
                        "broadcastFilterARP":"disable", 
                        "trustOriginalDSCP":"disable", 
                        "dscpUplinkBackground":8, 
                        "aaaProfile":"Employees0", 
                        "dscpDownlinkBackground":[ 
                                8, 
                                16 
 
support@AP-83:60:~$ cat /var/config/AAA_profile.conf 
{ 
"AAAProfile": [ 
  
[...] 
 
    "e02d1xAuthServer":{ 
      "secondaryServer":null, 
      "primaryServer":"UPAMRadiusServer", 
      "thirdServer":null, 
      "fourthServer":null 
 
support@AP-83:60:~$ cat /var/config/AAA_server.conf 
{ 
        "UnifiedAAAServer":[ 
                { 
                        "accountingPort":1813, 
                        "hostName":null, 
                        "retries":2, 
                        "ipAddress":"10.130.5.50", 
                        "name":"UPAMRadiusServer", 
                        "secret":"a006a626d46117ba078e0ca9ffd5b859", 
                        "type":"Radius", 
                        "timeout":5, 
                        "authenticationPort":1812, 
                        "deviceId":{ 
                                "inc":-1501300046, 
                                "timeSecond":1571817254, 
                                "machine":-458191393, 
                                "new":false, 
                                "time":1571817254000, 
                                "timestamp":1571817254, 
                                "date":1571817254000 
[…] 
 
 
Notes > Still a Problem?  
If the radius authentication still fails: 
- Capture and analyze the data by using the following command: tcpdump -i br-wan –s 0 host radiusIP 
- Check the Radius server configuration

<<<PAGE 306>>>
16 
Creation of a Secured Employee SSID 
 
-ANNEXES- 
 8 
Annex: WLAN Service (Expert) 
- The deployment of an SSID consists in several steps: 
- Creation of a "WLAN Service" profile (SSID) 
- Creation of an "AAA Server Profile" (if do not exist) 
- Creation of an "Access Role Profile" (if do not exist) 
- Creation of an Access Policy (if do not exist) 
- Definition of an Authentication Strategy (if do not exist) 
- Create a Radius local employee account (if do not exist) 
- Deployment of the profiles (templates) to AP-Group(s)

<<<PAGE 307>>>
17 
Creation of a Secured Employee SSID 
 
8.1.1. Creation of a WLAN Service profile (SSID) 
 
OV2500 -> WLAN -> WLAN Service -> + (Create icon)  
 
 
 
- 
Enter a Service Name and configure the profile as described below: 
ESSID   
 
- EmployeeX 
Hide SSID  
 
- Disable 
Enable SSID  
 
- Enable 
Allowed Band  
 
- 2.4GHz and 5GHz 
Security Level 
 
- Enterprise 
Encryption type  
- WPA2_AES 
AAA Profile 
 
- AAA-Server-PODX 
Default Access Role Profile - Access-role-employeeX 
 
 
Notes: AAA server and Access role profiles can be created first prior to setup WLAN services but for 
this exercise you will create specific profiles through the WLAN Service configuration screen. 
 
8.1.2. AAA Server Profile 
 
 
 
Tips: UPAM supports both captive portal and RADIUS server and can be used to implement multiple 
authentication methods: MAC, 802.1X and captive portal authentication. User Profiles can be 
supported in the OmniVista database or on external servers. 
 
 
AAA Server Profile 
- 
In the Security section, click on the “AAA Profile” field, select “+ Add New” and create the following 
AAA Server Profile “AAA-Server-PODX”: 
Authentication Servers 
802.1X 
Primary: UPAMRadiusServer 
Captive Portal 
Primary: UPAMRadiusServer 
MAC 
Primary: UPAMRadiusServer 
    
Accounting Servers 
802.1X 
Primary: UPAMRadiusServer 
Captive Portal 
Primary: UPAMRadiusServer 
MAC 
Primary: UPAMRadiusServer 
 
Click on the Create icon. 
You are then sent back to the WLAN Service page. In the Security section, select “AAA-Server-PODX” as the AAA 
Profile. 
 
 
Notes: In UPAM, there is a system-defined NAS Client Item (All Managed Devices). It cannot be 
deleted and is used to indicate that all the devices managed by OmniVista are automatically added 
into the NAS Client Database of UPAM and perform the AAA process.  
The shared secret in the system-defined “All Managed Devices” NAS profile is “123456”.

<<<PAGE 308>>>
18 
Creation of a Secured Employee SSID 
 
 
8.1.3. Access Role Profile 
 
Access Role Profile 
 
Notes: In this exercise you will create a specific access role “Access-role-employeeX” profile even 
if the use of the “defaultWLANprofile” should be enough for the test. 
 
- In the Security section, click on the “Default Access Role Profile” field, select “+ Add New” and create 
the Access Role Profile Access-role-employeeX.  
- Keep the default values for all parameters. 
- Click on the Create icon. 
 
- Back to the WLAN Service page, in the Security section, select “Access-role-employeeX” as the Default 
Access Role Profile. 
- Click on the Create icon. 
 
8.1.4. Apply the Access Role Profile to the Stellar APs 
 
- Go to the submenu Access Role Profile on the left Panel. 
- Select the checkbox next to the Access role profile “Access-role-employeeX” and click on the Apply to 
Devices button to assign this profile to your APs.  
 
- Do not change the Mapping method and enter the Vlan number “20” which is the EmployeeX VLAN. 
 
- Click on AP Group “Add”.  
- Select the AP Group APGX from the list on the left, add it to the section on the right and click on OK. 
 
 
- Click on Apply. 
- Check for success message.

<<<PAGE 309>>>
19 
Creation of a Secured Employee SSID 
 
 
- This is how the AP will map the Employee VLAN (20) to the EmployeeX SSID. 
 
When the SSID uses Enterprise authentication, assign a AAA Server Profile and then create an Authentication 
Strategy and Access Policy. 
At this step, the AAA Server Profile is already assigned to the SSID. The Authentication policy and Access Policy 
must be created. 
8.1.5. Authentication Strategy 
 
 
 
Notes: Authentication Strategy is used to set up a user profile source and login method (web page 
or not) for authentication, as well as the network attributes applied after a successful 
authentication. 
 
 
 
 
 
 
OV2500 -> UPAM -> Authentication -> Authentication Strategy -> + (Create icon)  
 
- Name the Strategy “User-PODX”, select the Authentication source as “local database”, “Access-role-
employeeX” as the default Access role profile and keep Web Authentication to none:

<<<PAGE 310>>>
20 
Creation of a Secured Employee SSID 
 
8.1.6. Access Policy configuration 
 
 
Notes: Authentication Access Policies are used to define the mapping conditions for an 
authentication strategy. Through Access Policy configuration, authentication strategy can be 
applied to different user groups, which can be divided by SSID or other attributes. 
 
 
 
 
OV2500 -> UPAM -> Authentication -> Access Policy -> + (Create icon)  
 
- Create the access policy “User-PODX” that will define the previous strategy to apply for employee 
authentication connected to SSID “EmployeeX”. The employeeX profile will use 802.1X with the UPAM 
internal RADIUS server. 
 
 
- In the Mapping Condition, select the SSID attribute and EmployeeX. Click on the + button. 
- Keep “User-PODX” as the Authentication Strategy and click on Create.

<<<PAGE 311>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Microsoft Active Directory Authentication 
Objective 
✓ Learn how to configure Microsoft Active Directory Authentication 
Contents 
1 
Briefing ......................................................................................... 1 
2 
Declaring the Active Directory Server ...................................................... 2 
3 
Modifying the Authentication Strategy ..................................................... 2 
4 
Testing the AD Authentication .............................................................. 3 
4.1. Verifying the connection .......................................................................... 4 
5 
Monitoring the Connections .................................................................. 4 
5.1. UPAM Monitoring .................................................................................... 4 
6 
Debriefing ...................................................................................... 5

<<<PAGE 312>>>
1 
Microsoft Active Directory Authentication 
 
 1 
Briefing 
In the previous lab, we have learned how to create an Employee SSID, with the UPAM Server (embedded in 
the OmniVista 2500) in charge of authenticating the clients.  
In this lab, we will learn how to declare the Active Directory in the OmniVista 2500, and we will use it during 
the authentication of clients on the SSID Employee.  
 
 
 
 
During this lab, we will: 
- Reuse the Employee SSID 
- Use an Active Directory already installed and configured to test this feature. 
 
 
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 313>>>
2 
Microsoft Active Directory Authentication 
 
 2 
Declaring the Active Directory Server 
First, let’s declare the Microsoft Active Directory Server in the OmniVista 2500 NMS: 
 
 
Modify the Employee SSID’s authentication strategy to use the Active Directory as 
Authentication Server.  
 
> Select UPAM > SETTINGS > LDAP/AD Configuration 
  > LDAP/AD Server: Enable 
  > Server Type: AD 
  > TLS/LDAPS: NS 
  > NETBIOS Domain Name: COMPANY 
  > DNS Domain Name: company.com 
  > FQDN/IP address of Domain Controller: 10.130.5.130 
  > Username: ov2500 
  > Password: Alcatel.0 
  > AD Port: 389 
 
  > Click on Test Connection to test the connection to the AD 
  > If OK (result on top of the screen), click on Apply 
 3 
Modifying the Authentication Strategy 
Now that the Active Directory server has been declared, go back Employee SSID settings and modify the 
Authentication Strategy. 
 
 
Modify the Employee SSID’s authentication strategy to use the Active Directory as 
Authentication Server.  
 
> Select WLAN > SSIDs > SSIDs  
  > In the EmployeesX SSID column, click on the link Authentication Strategy Name: EmployeeX 
    > Click on Edit 
 
      > Select External LDAP/AD 
      > Click on Apply 
    > Click on Close

<<<PAGE 314>>>
3 
Microsoft Active Directory Authentication 
 
 4 
Testing the AD Authentication  
To test that the Active Directory authentication is working correctly, let’s try to connect to the EmployeesX 
SSID.  
First, remove the SSID EmployeesX from the known networks:  
 
On the desktop, double click 
on the shortcut “Clean 
Wireless Networks” 
 
Select Execute in the new 
window. 
This will delete all the known 
wireless networks on this 
client. 
 
 
Then, login with the account Employee, already created in the Active Directory database.  
 
Left-click on the 
 icon 
(top right) 
 
Select the SSID EmployeesX 
(X = R-Lab Number) 
Check under “More Networks” 
if it is not displayed. 
 
 
 
 
 
Configure the SSID parameters 
with: 
 
Authentication: ProtectedEAP 
Check No CA certificate 
PEAP version: Automatic 
Inner Auth: MSCHAPv2 
 
Enter the credentials: 
Username: Employee 
Password: Alcatel.0 
 
Click on Connect 
 
A Notification informs you 
that the client is connect to 
the SSID

<<<PAGE 315>>>
4 
Microsoft Active Directory Authentication 
 
4.1. 
Verifying the connection 
From the Stellar Client virtual machine, check that the connection has been successfully established:  
- The IP Address of the Wi-Fi network card should be in the 10.7.X.32/27 range  
- Ping the DHCP Server (10.130.5.7) and the OmniVista 2500 (10.130.5.5X)  
Open a terminal with the icon 
 (top left corner). 
Enter the commands: 
 
 
 
 
 
 5 
Monitoring the Connections 
 
 
Display the Employee authentication record  
5.1. 
UPAM Monitoring 
The UPAM Authentication Record Screen displays authentication information for all devices authenticated 
through UPAM:  
 
> Select UPAM > AUTHENTICATION > Authentication Record

<<<PAGE 316>>>
5 
Microsoft Active Directory Authentication 
 
 6 
Debriefing 
In this lab, we have learned how to declare the Active Directory in the OmniVista 2500. Then, we have 
modified the Employee SSID settings in order to use the Active Directory to authenticate the clients which 
connect to this SSID.

<<<PAGE 317>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Creation of a Guest SSID 
Objective 
✓ Learn how to create a Guests SSID 
Contents 
1 
Briefing ......................................................................................... 2 
2 
Creating the Guest VLAN ..................................................................... 3 
2.1. Creating the Service VLAN ........................................................................ 3 
2.2. Guest IP Interface .................................................................................. 4 
3 
Creating the Guests SSID ..................................................................... 4 
3.1. Creating the GuestsX SSID ......................................................................... 4 
3.2. Creating a Guest Account ......................................................................... 5 
3.3. Back to… Creating the GuestsX SSID ............................................................. 5 
3.4. Assigning the SSID to the AP Group .............................................................. 6 
4 
Testing the Guests SSID ...................................................................... 7 
4.1. Connecting to the “WifiClient” Raspberry Pi ................................................... 7 
4.2. Setting Up the Wifi Client to Connect to the GuestXs SSID ................................... 7 
4.3. Verifying the connection .......................................................................... 8 
5 
Monitoring the Connections .................................................................. 9 
5.1. Monitoring the UPAM ............................................................................... 9 
5.1.1. Viewing the Authentication Record ...................................................................... 9 
5.1.2. Checking the Captive Portal Access Record ............................................................ 9 
5.2. WLAN Menu ......................................................................................... 10 
5.2.1. Wireless Client List ....................................................................................... 10 
5.2.2. Client Session ............................................................................................. 10

<<<PAGE 318>>>
1 
Creation of a Guest SSID 
 
6 
Kicking/Banning a Device .................................................................. 10 
6.1. Kicking out a Device .............................................................................. 10 
6.2. Banning/Blacklisting a Device ................................................................... 10 
7 
Debriefing .................................................................................... 11 
8 
Troubleshooting ............................................................................. 12 
8.1. Troubleshooting the OmniVista 2500 ........................................................... 12 
8.1.1. Checking the date and time ............................................................................ 12 
8.2. Troubleshooting the Stellar AP .................................................................. 13 
8.2.1. Checking the date and time ............................................................................ 13 
8.2.2. Checking the DNS configuration ........................................................................ 13 
8.2.3. Checking the wireless configuration ................................................................... 14 
8.2.4. Checking the Wi-Fi Channel ............................................................................. 14 
8.2.5. Checking the interface transmission power .......................................................... 14 
8.2.6. Checking the interface bitrate ......................................................................... 15 
8.3. Client Information ................................................................................. 15 
8.3.1. Listing the client(s) associated with the AP .......................................................... 15 
8.3.2. Checking the access logs of a specific client ......................................................... 16 
8.4. Checking the Captive Portal settings ........................................................... 16 
8.4.1. Checking the Captive Portal process .................................................................. 16 
8.4.2. Listing the clients authenticated via the Captive Portal ............................................ 17 
8.4.3. Checking the Captive Portal logs ....................................................................... 17 
9 
Annex: Restricting the Services ........................................................... 18 
9.1. Creating Policies ................................................................................... 18 
9.1.1. Service Group ............................................................................................. 18 
9.1.2. Create & Select the Services ........................................................................... 18 
9.1.3. Back to… Service Group ................................................................................. 19 
9.2. Back to… Create a new Policy ................................................................... 19 
9.3. Creating a Policy List ............................................................................. 19 
9.4. Pushing the Policy List & Policies on the Network Devices .................................. 20 
9.5. Applying the Policy List to a User ............................................................... 21 
9.6. Testing the Configuration ........................................................................ 21

<<<PAGE 319>>>
2 
Creation of a Guest SSID 
 
 1 
Briefing 
In the previous Lab, we have learned how to create a secured Employee SSID, dedicated for the company’s 
employee. Now, let’s see how to create a Guests SSID, dedicated for the guests.  
 
 
 
 
  
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 320>>>
3 
Creation of a Guest SSID 
 
Creating an SSID can be decomposed in several steps (same way as in the previous lab “Creation of a Secured 
Employee SSID”): 
1. Create the VLAN 30. This VLAN will service the SSID “GuestsX” (X = R-Lab Number). It will be tagged 
from the Access Points to the access OmniSwitches (OS2360 and OS6360), and over the link towards 
the core OmniSwitch (OS6870).  
2. Create the SSID and configure its options. 
 2 
Creating the Guest VLAN 
Before creating the Guests SSID, let’s create the VLAN that will be associated to this SSID GuestsX (X= R-Lab 
number) and that will carry the guests’ traffic.  
2.1. 
Creating the Service VLAN 
 
 
Create the VLAN 30 on the OmniSwitches OS6870, OS6360 and OS2360. 
 
 
 
To create the VLAN 30 on the OmniSwitches, we will use the OmniVista 2500 VLAN Manager feature: 
 
> Select CONFIGURATION > VLANS > VLAN 
  > Click on Create VLAN by Devices button 
 
1. Devices Selection 
  > VLAN Overwrite: ENABLED 
  > VLAN IDs: 30 
  > VLAN(s) Description: GUESTS 
    > Click on the Add/Remove Devices 
      > Click Add All 
      > Click on OK  
    > Click on Next 
 
2. VLAN Configuration 
  > Check that Admin Status = Enabled 
  > Click on Next  
 
3. Default Port Assignment 
  > Skip this step (click Next) 
 
 4. Q-Tagged Port Assignment 
 > For the OmniSwitch OS6870, click on Add Port 
    > Select the ports 1/1/3 & 1/1/8 
OS6870

<<<PAGE 321>>>
4 
Creation of a Guest SSID 
 
    > Click on OK   
 > For the OmniSwitch OS6360, click on Add Port 
    > Select the ports 1/1/3 & 1/1/6 
    > Click on OK  
  > For the OmniSwitch OS2360, click on Add Port 
    > Select the ports 1/1/8 & 1/1/6 
    > Click on OK  
  > Click on Next 
 
5. Review 
  > Review the information 
  > Click on Create 
 
 
Tips 
The VLANs can also be created on the OmniSwitches via command lines (CLI). Hence, the VLAN Manager feature 
can be very interesting to use if the infrastructure is composed of several OmniSwitches, and the same VLANs 
must be created on some/all of them.  
2.2. 
Guest IP Interface 
The core OmniSwitch 6870 is pre-configured with an IP interface 10.7.X.94/27 for the VLAN Guest.  
This IP interface is required to forward the DHCP requests from the clients to the DHCP server. 
 
 
The IP interface “int_guest” is pre-configured on the OmniSwitch 6870. 
 3 
Creating the Guests SSID 
Now that we have the Guest VLAN and associated IP interface managed, let’s create the GuestsX SSID: 
 
 
3.1. 
Creating the GuestsX SSID 
 
 
Create the SSID GuestsX (X = R-Lab Number) 
 
> Select WLAN > SSIDs > SSIDs 
  > Click on the + button 
    > SSID Service Name: GuestsX (X = R-Lab number) 
    > SSID: <filled automatically> 
    > Usage: Guest Network (Open or Captive Portal)  
    > Do you want users to go through a Captive Portal? YES  
    > Captive Portal Type: OV-UPAM Captive Portal

<<<PAGE 322>>>
5 
Creation of a Guest SSID 
 
    > Click on Create & Customize 
 
 
Notes > About the “Usage” 
During the SSID creation, a “Usage” is asked. When you select a Usage, relevant related default configurations 
(Access Policy, Authentication Strategy, …) are automatically created.  
Guest Network creates a network for Guest Users. It is suitable for setting up an Open Network with or without 
a Captive Portal. This is typically used for Guests.  
Of course, these configurations can be customized. Check the OV2500 dedicated Help for more information.  
 
  > Allowed Band: 2.4GHz and 5GHz 
 
 
Tips > Help Menu 
As you can see, several settings can be managed in the SSID Creation properties. Take the time to learn more 
about each of them by clicking on the Help button   
 
Authentication Strategy   
  > RADIUS Server: UPAMRadiusServer 
  > Click on Manage Guest Accounts 
 
 
Notes > UPAMRadiusServer 
In this lab, for all the types of authentication, we will use the UPAM platform (Unified Policy Authentication 
Manager) embedded in the OmniVista 2500.  
UPAM is a unified access management platform for both AOS Switch Series devices and Stellar AP Series 
devices. UPAM supports both captive portal server and RADIUS server; and can be used to implement multiple 
authentication methods, such as MAC authentication, 802.1X authentication, and captive portal authentication. 
3.2. 
Creating a Guest Account 
 
 
Create the Guest account  
 
> Click on the + button 
  > Guest name: Guest  
  > Password: password 
  > Repeat Password: password 
  > Data Quota: Disable 
  > Click on Create 
> Click on Close 
 
3.3. 
Back to… Creating the GuestsX SSID 
 
Guest Access Strategy 
  > Portal Page: DefaultPortal 
  > Login by: Username & Password 
 
Default VLAN/Network 
  > VLAN ID: 30 
> Click on Save and Apply to AP Group 
 
 
Tips > Customize Portal Page 
The Captive Portal (the webpage where the guests are redirected when they try to connect to the network) is 
customizable. By clicking on the Customize Portal Page option, you can choose between different templates 
(=predefined Captive Portal styles). To fully customize the Captive Portal, go to UPAM > SETTINGS > Captive 
Portal. 
You can test it if you are ahead of schedule!

<<<PAGE 323>>>
6 
Creation of a Guest SSID 
 
3.4. 
Assigning the SSID to the AP Group 
 
 
Assign the freshly created SSID GuestsX to the AP Group APGX created in the previous 
lab 
 
Now that the SSID GuestsX has been created, assign it to the AP Group(s) APGX: 
 
AP Group Assignment and Schedule 
> Click on Change Selection 
  > Remove default group from the SELECTED tab 
  > Move APGX (X = R-Lab Number) from AVAILABLE to SELECTED 
  > Click on OK 
> Click on Apply 
> Check the result on the page that is displayed (notice the differences between EmployeesX and GuestsX 
SSIDs) 
 
Now that we have finished the configuration of the SSID, let’s test it!

<<<PAGE 324>>>
7 
Creation of a Guest SSID 
 
 4 
Testing the Guests SSID 
 
Test the GuestsX SSID by connecting on it via the Guest account 
4.1. 
Connecting to the “WifiClient” Raspberry Pi  
 
R-Lab Windows Desktop 
Double click on the Real VNC 
Viewer shortcut  
 
 
4.2. 
Setting Up the Wifi Client to Connect to the GuestXs SSID 
 
WifiClientX Raspberry Pi 
Left-click on the 
 icon 
(top right) 
 
Select the SSID GuestsX (X = 
R-Lab Number) 
Check under “More Networks” 
if it is not displayed. 
 
 
 
 
Open a Web Browser with the 
icon 
 in the top left 
corner. 
Enter any non-https URL (ex: 
http://2.2.2.2) and you are 
redirected to the Captive 
Portal 
Enter the credentials: 
 
Username: Guest 
Password: password 
 
Check I accept the Terms of 
Use 
  
Click on Login

<<<PAGE 325>>>
8 
Creation of a Guest SSID 
 
 
Notes > Web redirection 
Depending on the Operating System you are using, a web browser can automatically be opened when you 
connect to the Guest SSID. 
With the Raspberry Pi (running on a Debian OS), it is not the case. This is why you have to open your web 
browser manually and open any non-https URL to be redirected to the Captive Portal.  
4.3. 
Verifying the connection 
From the Stellar Client, check that the connection has been successfully established:  
- The IP Address of the Wi-Fi network card should be in the 10.7.X.64/27 range  
- Ping the DHCP Server (10.130.5.7), the OmniVista 2500 (10.130.5.5X) and the UPAM Server 
(10.130.5.7X) 
 
Open a terminal with the icon 
 (top left corner). 
Enter the commands:

<<<PAGE 326>>>
9 
Creation of a Guest SSID 
 
 5 
Monitoring the Connections 
 
 
Display the Guest authentication record  
5.1. 
Monitoring the UPAM  
5.1.1. 
Viewing the Authentication Record 
The Authentication Record Screen displays authentication information for all devices authenticated 
through UPAM:  
 
> Select UPAM > AUTHENTICATION > Authentication Record 
 
 
 
 
In the Authentication Record List information, find the Stellar Access Point where your 
Client Virtual machine (StellarClientX) is connected.   
 
 
Notes > Client associated to a Stellar Access Point 
The information asked in the question above can also be found in the WLAN > CLIENT > Client List 
menu. Go check it out! 
 
 
Tips > Guest Account Creation 
Do you remember the Guest account that you have created? You have done it via a shortcut, during the SSID 
creation process. This shortcut leads to the … UPAM > Guest Account menu! Go and have a look at this menu. 
You will find the Guest account that you have created previously. From there, you can easily create a new 
Guest account.  
5.1.2. 
Checking the Captive Portal Access Record 
To monitor the Captive Portal access: 
 
> Select UPAM > AUTHENTICATION > Captive Portal Access Record 
 
 
 
Another interesting feature that the OmniVista 2500 NMS offers is the ability to locate the AP, Switch 
and/or slot/port that is directly connected to a user-specified station: it is the Locator application.

<<<PAGE 327>>>
10 
Creation of a Guest SSID 
 
5.2. 
WLAN Menu 
5.2.1. 
Wireless Client List 
The Wireless Client List Screen displays real time information for wireless clients associated with APs. By 
default, the Distribution of Clients per AP chart at the top of the screen provides a graphical overview of 
the number of clients associated with each AP: 
 
> Select WLAN > Client > Client List 
> Scroll down to the List of Clients on All APs section 
 
 
From the Client List page, find on which Stellar Access Point the Guest account is 
connected 
5.2.2. 
Client Session 
The Wireless Client Session Screen displays information about current wireless clients associated with APs. 
By default, all wireless client sessions are displayed in the list. 
 
> Select WLAN > Client > Client Session 
 6 
Kicking/Banning a Device 
Now that we are sure that the StellarClient virtual machine is correctly connected to the Guests SSID, let’s 
see how to kick him out from the network, and blacklist it.  
 
 
- Try to kick out the StellarClient. Check that you can reconnect to the Guest SSID 
- Try to ban/blacklist the StellarClient. Check that it is not possible to reconnect to 
the Guests SSID until the StellarClient is removed from the blacklist.  
6.1. 
Kicking out a Device 
Use the Kickoff option to de-authenticate a user from the SSID he is connected to : 
 
> Select UPAM > GUEST ACCESS > Guest Device 
  > Select the Client  
    > Click on KickOff   
    > Click OK to confirm 
6.2. 
Banning/Blacklisting a Device 
If you have kicked out the StellarClient, reconnect it to the Guest SSID before testing the blacklist 
feature. 
 
To blacklist a device from the OmniVista 2500:  
 
> Select WLAN > CLIENT > Client List > Wireless Client List 
> Scroll down to the List of Clients on All APs section 
  > Select the Client  
    > Click on Add to Blocklist   
    > Click OK to confirm

<<<PAGE 328>>>
11 
Creation of a Guest SSID 
 
To remove the client from the blacklist:  
 
> Select WLAN > CLIENT > Client BlockList 
  > Select the Client  
    > Click on 
  
 7 
Debriefing 
During this lab, we have created a VLAN dedicated for the Guests data traffic. Then, we have created the 
Guests SSID and configured it to force the Guests to authenticate via a Captive Portal. Finally, we have 
monitored the Guest (StellarClient virtual machine) connection, and we’ve seen that it was possible de 
kick/ban a device from the OmniVista 2500.

<<<PAGE 329>>>
12 
Creation of a Guest SSID 
 
 8 
Troubleshooting 
In this part, we will cover the process to follow if there is an issue regarding the connection to a Guests SSID. 
We will use the exact same infrastructure as in the lab:  
 
 
 
Notes > Before Beginning  
Before beginning this part, we assume that all the steps available in this lab have been followed correctly and 
checked: SSID creation, guest account creation… 
8.1. 
Troubleshooting the OmniVista 2500 
8.1.1. 
Checking the date and time 
A guest account has an expiration date. It is important to check that the date and time are correctly set 
up: 
OmniVista 2500 Console 
Select the OV2500 virtual 
machine

<<<PAGE 330>>>
13 
Creation of a Guest SSID 
 
Click Launch Web Console, 
then Web Console 
 
 
 
Enter the credentials defined 
during the OmniVista 2500 
installation:  
- login: cliadmin 
- password: Alcatel.0 
 
A menu is displayed.  
 
Choose option [10] Advanced 
Mode 
 
From the CLI, use the 
command date 
 
8.2. 
Troubleshooting the Stellar AP 
 
The Stellar console access is deactivated in Enterprise mode for the application Configuration > CLI 
Scripting > Terminal. 
To activate the SSH console connection on OV2500, go to Network > AP Registration >AP Group, edit the 
AP Group and change the support and root passwords. 
 
 
8.2.1. 
Checking the date and time 
A guest account has an expiration date. It is important to check that the date and time are correctly set 
up: 
 
support@AP-0E:E0:~$ date 
Thu Oct 24 09:25:08 2019 
8.2.2. 
Checking the DNS configuration 
A valid DNS configuration is mandatory in order to redirect successfully the client(s) to the Captive Portal 
page: 
 
support@AP-0E:E0:~$ cat /etc/resolv.conf 
# Interface wan 
nameserver 10.0.0.51 
search ale-training.com 
Use the APs console connections on the desktop and do not change the passwords in the AP Group.

<<<PAGE 331>>>
14 
Creation of a Guest SSID 
 
8.2.3. 
Checking the wireless configuration 
 
support@AP-0E:E0:~$ iwconfig 
[…] 
Ath002    IEEE 802.11ng  ESSID:"Guests0" 
          Mode:Master  Frequency:2.437 GHz  Access Point: DC:08:56:00:0E:E2 
          Bit Rate:192 Mb/s   Tx-Power=17 dBm 
          RTS thr:off   Fragment thr:off 
          Power Management:off 
          Link Quality=94/94  Signal level=-42 dBm  Noise level=-95 dBm 
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0 
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0 
 
gretap0   no wireless extensions. 
 
ath102    IEEE 802.11ac  ESSID:"Guests0" 
          Mode:Master  Frequency:5.22 GHz  Access Point: DC:08:56:00:0E:EA 
          Bit Rate:800 Mb/s   Tx-Power=19 dBm 
          RTS thr:off   Fragment thr:off 
          Power Management:off 
          Link Quality=50/94  Signal level=-76 dBm  Noise level=-95 dBm 
          Rx invalid nwid:4  Rx invalid crypt:0  Rx invalid frag:0 
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0  
[…] 
8.2.4. 
Checking the Wi-Fi Channel 
To check which channel is used (ex. ath12 interface): 
 
support@AP-0E:E0:~$ iwlist ath102 channel 
ath12     157 channels in total; available frequencies: 
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
          Current Frequency:5.22 GHz (Channel 44) 
8.2.5. 
Checking the interface transmission power 
 
support@AP-0E:E0:~$ iwlist ath102 txpower 
ath12     8 available transmit-powers : 
          0 dBm         (1 mW) 
          7 dBm         (5 mW) 
          9 dBm         (7 mW) 
          11 dBm        (12 mW) 
          13 dBm        (19 mW) 
          15 dBm        (31 mW) 
          17 dBm        (50 mW) 
          19 dBm        (79 mW) 
          Current Tx-Power=19 dBm       (79 mW)

<<<PAGE 332>>>
15 
Creation of a Guest SSID 
 
8.2.6. 
Checking the interface bitrate  
 
support@AP-0E:E0:~$ iwlist ath102 bitrate 
ath12     8 available bit-rates : 
          6 Gb/s 
          9 Gb/s 
          12 Gb/s 
          18 Gb/s 
          24 Gb/s 
          36 Gb/s 
          48 Gb/s 
          54 Gb/s 
          Current Bit Rate:800 Mb/s 
8.3. 
Client Information 
8.3.1. 
Listing the client(s) associated with the AP 
It is possible to list:  
- All the clients associated with the AP: 
 
support@AP-0E:E0:~$ ssudo sta_list 
SSID:Employees0 
 
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX             
d4:6e:0e:18:60:38  10.7.0.69                                      326             280008  830034      
FREQ          AUTH     Final_role                          VLANID  TUNNELID  FARENDIP 
5GHz          OPEN     __Guests0                             30       0 
 
- All the clients associated with a specific interface (ex. ath12 corresponding to the SSID Guests0 in 5 
Ghz):  
 
support@AP-0E:E0:~$ ssudo wlanconfig ath102 list 
ADDR               AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE  TXSEQ  RXSEQ  CAPS XCAPS         
d4:6e:0e:18:60:38    1   44   6M     72M   64      63      67    0      0   65535    Es    OI           
 
ACAPS     ERP    STATE MAXRATE(DOT11) HTCAPS VHTCAPS ASSOCTIME    IEs   MODE                   PSMODE    
0          b              0             WPS   2gGR    00:10:10    WME IEEE80211_MODE_11AC_VHT40  0  
RXNSS TXNSS 
 1      1  
  
 Minimum Tx Power                : 5 
 Maximum Tx Power               : 18 
 HT Capability                  : Yes 
 VHT Capability                 : Yes 
 MU capable                     : No 
 SNR                            : 64 
 Operating band                 : 5GHz 
 Current Operating class        : 0 
 Supported Rates                : 12  18  24  36  48  72  96  108

<<<PAGE 333>>>
16 
Creation of a Guest SSID 
 
- The parameters sent from the AP to the Wi-Fi Client(s):  
 
support@AP-83:60:~$ ssudo wam_debug sta_list 
{ 
        "status": "Success!!!", 
        "wlanServiceData": [ 
                { 
                        "iface": "ath12", 
                        "ssid": "Guests0",                                  SSID Name 
                        "freq": "5GHz",                                     Frequency 
                        "security": "Open",                                 Security  
                        "wlanService": "Guests0",                           Assoc. WLAN Service 
                        "staData": [ 
                                { 
                                        "staMAC": "d4:6e:0e:18:60:38",      Wi-Fi Client MAC@ 
                                        "staIP": "10.7.0.69",               Wi-Fi Client IP@ 
                                        "staGlobalIPv6": "::", 
                                        "staLocalIPv6": "::", 
                                        "associationTime": 724,             Assoc. Time (seconds) 
                                        "mappingType": 0, 
                                        "assignedVLAN": 30,                 Wi-Fi Client Assigned VLAN 
                                        "assignedAR": "__Guests0",          Wi-Fi Client Assigned ARP 
                                        "assignedPL": "", 
                                        "macAuthResult": "SUCCESS", 
                                        "ARFromMACAuth": "", 
                                        "PLFromMACAuth": "", 
                                        "redirectURLFromMACAuth": "https:\/\/ov2500-upam-cportal.al-
enterprise.com:443\/portal_UI\/27d977d4f77a4a0783d5a76a8d5ab077\/login.html?mac=D46E0E186038", 
                                        "ARFrom8021xAuth": "", 
                                        "PLFrom8021xAuth": "", 
                                        "redirectURLFrom8021xAuth": "", 
                                        "CPAuthResult": "SUCCESS", 
                                        "ARFromCPAuth": "__Guests0", 
                                        "PLFromCPAuth": "", 
                                        "ARFromRoaming": "", 
                                        "PLFromRoaming": "", 
                                        "redirectURLFromRoaming": "", 
                                        "classificationMatched": "none"  
[…] 
 
8.3.2. 
Checking the access logs of a specific client 
Find the MAC address of the client (ex. d4:6e:0e:18:60:38), then: 
 
support@AP-0E:E0:~$ cat /proc/kes_syslog | grep “d4:6e:0e:18:60:38” 
8.4. 
Checking the Captive Portal settings 
 
 
Notes > Before Beginning  
Before beginning this part, we assume that all the settings on the Client side (Wi-Fi network card up and 
running, firewall checked…) and OmniVista 2500 side (account created, Captive Portal settings…) have been 
verified (if not sure, go back to the client settings instructions available in this lab) 
8.4.1. 
Checking the Captive Portal process  
 
support@AP-83:60:~$ ps |grep eag 
4499 support   1300 S    grep eag 
 4662 root      7860 S    /usr/sbin/eag_app

<<<PAGE 334>>>
17 
Creation of a Guest SSID 
 
8.4.2. 
Listing the clients authenticated via the Captive Portal 
 
support@AP-83:60:~$ eag_cli show user all //or// eag_cli show user list 
 
user num : 1 
ID      UserName           UserIP                                   UserMAC              SessionTime   
1       Guest              10.7.0.69                                D4:6E:0E:18:60:38    0:16:18       
OutputFlow         InputFlow          AuthType           ESSID  
 3091809            659705             PORTAL       Guests0 
 
 
Notes > Kicking a Client  
It is also possible to kick a client authenticated via the Captive Portal from the Stellar AP CLI (to use this 
command, the user ID must be known: it is displayed by using the eag_cli command (see above)):  
 
support@AP-83:60:~$ ssudo eag_cli kick user index 1 
the command is successful! 
8.4.3. 
Checking the Captive Portal logs 
The Captive Portal logs can be displayed:  
 
support@AP-83:60:~$ tail -f /tmp/log/eag.log 
support@AP-83:60:~$ cat /proc/kes_syslog |grep eag 
support@AP-83:60:~$ cat /var/log/eag.log

<<<PAGE 335>>>
18 
Creation of a Guest SSID 
 
-ANNEXES- 
 9 
Annex: Restricting the Services 
To configure network access control, we need to:  
• 
Create policies to define what we will be authorized and what will not (telnet, SSH).  
• 
Create a policy list which will contain the policies, and a precedence for each. 
• 
Apply automatically the policy list to the guests  
9.1. 
Creating Policies 
 
 
Create a policy which will regroup the forbidden services: telnet, SSH 
 
 
 
 
Let’s begin with the creation of the Policy. In this Policy, we will deny the telnet and SSH protocols: 
 
> Select UNIFIED ACCESS > UNIFIED POLICY 
  > Click on 
 to add a new Policy 
 
1. Config  
      > Name: DeniedServ 
      > Click on Next 
 
2. Device Selection 
      > Click on both ADD buttons to apply the policy on the network device OS6870 and AP Group APGX. 
Note: OS2360 and OS6360 are not supported. 
      > Click on Next 
 
3. Set Condition 
      > Select L4 Services 
        > Select Group 
          > Service Group: click on   
9.1.1. 
Service Group 
Now, let’s create a group containing the denied services: 
 
Service Group 
      > Group Name: DeniedSrv 
9.1.2. 
Create & Select the Services 
 
Services 
      > Click on 
      > Service Name: telnet 
      > Destination Port: select TELNET (23) 
      > Click on Create 
      > Click on Finish 
 
Services

<<<PAGE 336>>>
19 
Creation of a Guest SSID 
 
      > Click on 
      > Service Name: SSH 
      > Protocol: TCP 
      > Destination Port: select  
        > Name: SSH 
        > Port Number: 22 
        > Click on Create 
        > Click on Finish 
      
      > Destination Port: SSH 
      > Click on Create 
      > Click on Finish 
9.1.3. 
Back to… Service Group 
 
Service Group 
      > Select Services: Click on 
 to add all the services 
      > Click on Create 
9.2. 
Back to… Create a new Policy 
 
3. Set Condition 
      > Service Group: DeniedSrv 
      > Click on Next 
 
4. Set Action 
      > Click on QOS 
        > Disposition: DROP 
      > Click on Next 
 
5. Validity Period 
      > Validity Periods: AllTheTime 
      > Click on Next 
 
6. Review 
      > Review the information, then click on Create 
    > Click on OK 
 
At the end of this step, a Policy has been created. This Policy contains the services that will be denied to 
the users, when they will be authenticated. Creating a list of authorized services is not necessary, as one 
“AcceptAllPolicy” is created by default (we will use it in the next part). 
9.3. 
Creating a Policy List 
Now that we have created the policy containing the denied services, let’s create a policy list that will 
regroup and order the policies (1 – Deny services chosen in the previous part, 2 – Authorized the other 
services) 
 
 
 
 
> Select Unified Policy List in the left menu 
  > Click on 
 to create a new Policy List

<<<PAGE 337>>>
20 
Creation of a Guest SSID 
 
 
1. Config for Policy List 
    > Name: GuestsPolicy 
    > Add Unified Policy: select DeniedServ 
     
    > In the drop-down list at the bottom of the area (“Device-Default”), select OV-L3-AcceptAllPolicy 
    > Click on Next 
 
 
 
2. Device Selection 
    > Click on ADD, then add the devices OS6870 and the AP Group APGX 
    > Click on Create, then OK 
 
 
9.4. 
Pushing the Policy List & Policies on the Network Devices 
Once the Policies and the Policy List created, they must be pushed to the network devices: 
 
> On the left menu, select:  
  > Unify Policies  
    > Click on Notify All (top right corner) 
    > Click on OK  
 
  > Unify Policy List 
    > Click on Notify All (top right corner) 
    > Click on OK  
 
At the end of this step, we have:  
- Created the Policy  
- Created the Policy List  
 
 
 
 
We have also pushed them on the network devices (OmniSwitch 6870 and Stellar APs contained in the 
AP Group APGX).

<<<PAGE 338>>>
21 
Creation of a Guest SSID 
 
9.5. 
Applying the Policy List to a User 
Once all the settings are configured, we will set up the OmniVista 2500 to apply the Access Role Profile 
to the authenticated users (WLAN or LAN): 
- Once authenticated, an Access Role Profile is applied to the guest;  
- We want, in this part, to apply the policies to the guest, once authenticated;   
- Hence, we are going to insert the Policy List created previously in the Access Role Profile which is 
automatically applied to the guests, once authenticated. 30 
 
> Select UNIFIED ACCESS > UNIFIED PROFILE > Template 
  > Select Access Role Profile 
    > Select the Access Role Profile “__GuestsX” (X = R-Lab Number) 
    > Click on 
 
      > Select Policy List = GuestsPolicy 
      > Click on Apply 
  > Click on Apply to Devices (top right and corner) 
    > Insert VLAN Number = 30  
    > Select the OmniSwitchs OS6870 and the AP Group APGX (X = R-Lab Number) 
    > Click on Apply 
 
 At the end of this step, we have:  
- Created a Policy  
- Created a Policy List  
- The Policy List has been inserted in the Access Role Profile 
which is applied to the employees once authenticated on the 
SSID « EmployeeX » (X = R-Lab Number) 
 
 
 
 
 
9.6. 
Testing the Configuration 
Connect to GuestsX and try to perform a telnet and SSH connection to the gateway:  
 
WIRELESS CLIENT “WifiClientX” 
> Open a console terminal on the Raspberry Pi.  
  > Launch an SSH connection with the command > “ssh 10.7.X.62” (X = R-Lab Number [1…8])  
 
 
Warning 
BEFORE PERFORMING THE TEST, BE SURE TO DISCONNECT AND RECONNECT THE VIRTUAL MACHINE FROM THE 
NETWORK TO FORCE THE RE AUTHENTICATION AS THE POLICY IS APPLIED ONCE THE CLIENT AUTHENTICATION IS 
SUCCESSFUL.

<<<PAGE 339>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Web Content Filtering 
Objective 
✓ Learn how to configure the Web Content Filtering 
Contents 
1 
Briefing ......................................................................................... 1 
2 
Activate Web Content Filtering ............................................................. 2 
3 
Configure Web Content Filtering ........................................................... 3 
3.1. WCF operational status ............................................................................ 3 
3.2. WCF Profile creation ............................................................................... 3 
3.3. Assign WCF Profile to Access Role Profile ....................................................... 4 
4 
Test and validation ........................................................................... 5 
4.1. Connect to the GuestsX SSID ...................................................................... 5 
4.2. Verifying the connection > On the WLAN Client ............................................... 6 
4.3. Verify the Web Content Filtering ................................................................ 7 
5 
Debriefing ...................................................................................... 8 
6 
Troubleshooting ............................................................................... 9

<<<PAGE 340>>>
1 
Web Content Filtering 
 
 1 
Briefing 
Now that the Stellar solution is broadcasting the EmployeesX and GuestsX SSID, the company wants to filter 
the guest traffic from specific websites. 
In this example, “Social Network” and “Gambling” traffic will be rejected, whereas all the other internet 
traffic will be accepted on the GuestsX SSID. 
The WCF feature will be implemented on the network and will be then tested.

<<<PAGE 341>>>
2 
Web Content Filtering 
 
 2 
Activate Web Content Filtering 
 
 
Web Content Filtering can either be activated per AP Group or per Access Point. 
It will be activated per AP Group in this lab but look at the tip to know how to activate 
it per Access Point.  
 
We will activate the WCF feature for the AP Group APGX – attached to all our Access Points. 
 
> Select NETWORK > AP REGISTRATION > AP Group 
  > Select APGX – replace X by your pod n°. 
    > Click on 
 
      > In the category Web Content Filtering, activate WCF: 
        
 
      > Click on Commit 
    > Review the Success logs and click on OK 
 
 
Alternate Method: WCF Activation per Access Point 
> Select NETWORK > AP REGISTRATION > Access Point 
  > Select the Access Points where the WCF must be activated. 
    > Click on 
 > Web Content Filtering 
      > Activate Use Private Config and Web Content Filtering: 
        
 
      > Click on Apply

<<<PAGE 342>>>
3 
Web Content Filtering 
 
 3 
Configure Web Content Filtering 
As the WCF is now active for all the Access Points in our AP Group APGX, we will configure it. We will create 
a profile, select the categories of web traffic to be rejected and assign this profile to our users.  
3.1. 
WCF operational status 
 
 
Check the status of the WCF feature.  
 
> Select UPAM > Web Content Filtering > WCF Profile 
 
 
3.2. 
WCF Profile creation 
 
In this lab, we will create a profile that will reject all the traffic categorized as “Social Networking” 
(Facebook, Twitter, Linkedin,…) and “Gambling” (unibet, bet 365,…). 
All the traffic that does not belong to one of these categories will be accepted. 
 
> Select UPAM > WEB CONTENT FILTERING > WCF Profile 
  > Click on 
 
    > Name: WCF-guests 
     > Category: Social Networking  
     > Action: Reject  
     > Click on 
 to add this rule  
 
     > Category: Gambling  
     > Action: Reject  
     > Click on 
 to add this rule  
 
     
 
         
      > Click on Create 
    
 
By default, all the traffic is accepted. It means that on the traffic from these two 
categories are rejected.

<<<PAGE 343>>>
4 
Web Content Filtering 
 
3.3. 
Assign WCF Profile to Access Role Profile 
 
 
The WCF profile is assigned to one – or multiple – Access Role Profile. All the users 
assigned to this Access Role Profile can have their web traffic filtered.  
 
For our GuestsX SSID, the users are attached to the Access Role Profile “__GuestsX”. The WCF profile will 
therefore be attached to this Access Role Profile. 
 
> Select WLAN > SSIDs > SSID 
  > In the GuestsX column, click on the Access Role Profile “__GuestsX” – replace X by your POD n°.   
    > Select “__GuestsX” and click on 
 
     > Under the category Web Content Filtering (WCF), select WCF-Guests from the drop-down menu  
      
 
     > Click on Apply  
 
 
As we have modified the Access Role Profile, we must apply it to the AP Group. 
Otherwise, the modification is just changed locally on the OmniVista server and not pushed to the Access 
Points. 
 
> Select __GuestsX and click on the button Apply to Devices (in the Access Role Profile window) 
  > In the Mapping Method, select Map to VLAN  
    > In the VLAN(s), select “30” (the Guests VLAN) 
    > Click on ADD in front of “0 AP Groups”   
     > Move the AP Group APGX to the column on the right and click on OK 
    > Click on Apply 
  > Review the success logs, click on OK and then on Close  
 
 
The WCF profile is assigned to the Access Role Profile __GuestsX, which is then applied 
to the AP Groups. All the Guests authenticated are assigned to this Access Role Profile 
and will have their Social Network and Gambling web traffic filtered.

<<<PAGE 344>>>
5 
Web Content Filtering 
 
 4 
Test and validation 
 
We will use the StellarClient, connect to the GuestsX SSID and use our Guest credentials. 
We will then generate web traffic for different websites (google, facebook, bet 365,…) and observe the 
behavior of the traffic. 
4.1. 
Connect to the GuestsX SSID 
 
WifiClientX Raspberry Pi 
Left-click on the 
 icon 
(top right) 
 
Select the SSID GuestsX (X = 
R-Lab Number) 
Check under “More Networks” 
if it is not displayed. 
 
Click on Connect 
 
 
 
Open a Web Browser with the 
icon 
 in the top left 
corner. 
 
Enter any non-https URL (ex: 
http://2.2.2.2) and you are 
redirected to the Captive 
Portal 
 
Enter the credentials: 
 
Username: Guest 
Password: password 
 
Check I accept the Terms of 
Use 
  
Click on Login

<<<PAGE 345>>>
6 
Web Content Filtering 
 
4.2. 
Verifying the connection > On the WLAN Client 
From the Stellar Client virtual machine, check that the connection has been successfully established:  
- The IP Address of the Wi-Fi network card should be in the 10.7.X.94/27 range  
- Ping the DHCP Server (10.130.5.7) and the OmniVista 2500 (10.130.5.5X)  
 
Open a terminal with the icon 
 (top left corner). 
Enter the commands:

<<<PAGE 346>>>
7 
Web Content Filtering 
 
4.3. 
Verify the Web Content Filtering 
On the StellarClient, open a new tab in your web browser for each of these URLs: 
- 
www.google.com : OK, can be reached. 
o 
Google.com is not part of the Social Network or Gambling category. As all the traffic (not 
part of these categories) is accepted by default, the URL can be reached. 
- 
www.facebook.com: KO, can’t be reached. 
 
 
URL Facebook (Social Network category) is rejected 
The ACL used to reject the traffic for this URL has been pushed to the Access Point. Any HTTP/HTTPS request 
for this URL is rejected by the Access Point. 
The Access Point will not forward anymore the DNS requests of the client for this website. This is why you can 
see this error message in your browser.  
- 
www.twitter.com: KO, can’t be reached. 
o 
The rule that rejects the guest’s traffic for this category has been applied and you can’t 
reach the website. 
- 
www.unibet.com : KO, can’t be reached. 
o 
The ACL rule rejecting the traffic for the Gambling websites has been written. And all the 
subsequent Gambling traffic is rejected by the Access Point.

<<<PAGE 347>>>
8 
Web Content Filtering 
 
 5 
Debriefing 
At the end of this lab, the Guest’s web traffic for the Social Network and Gambling categories is rejected. 
These rules, rejecting this traffic, are applied to all the users belonging to the Access Role Profile __GuestsX.

<<<PAGE 348>>>
9 
Web Content Filtering 
 
 6 
Troubleshooting 
 
The Web Content Filtering feature requires the DNS configuration on the OmniVista server. 
If the DNS configuration is missing in the OmniVista 2500, the status of the WCF feature will be “Not in 
service” and the OmniVista won’t be able to join the Brightcloud API. 
 
 
Check that the DNS servers are configured on the OmniVista server.  
 
OmniVista 2500 Console 
On the left panel of vSphere 
Client, select the OmniVista 
2500 VM. 
 
 
To open the virtual machine, 
click on the link Launch Web 
Console in the summary page 
 
Log in with the credentials 
entered earlier: 
• 
Login: cliadmin 
• 
Password: Alcatel.0 
 
 
Enter the option [2] to check 
the configuration of the 
server.

<<<PAGE 349>>>
10 
Web Content Filtering 
 
Enter the option [6] to check 
the DNS configuration of the 
server. 
 
Would you like to use dns 
server: y 
 
Please input dns server 1: 
- 
If 10.130.5.130 is 
configured, press 
Enter. 
- 
If nothing is 
configured, type 
10.130.5.130 and 
Enter. 
 
Would you like to use dns 
server 2: y 
 
Please input dns server 2: 
- 
If 10.0.0.51 is 
configured, press 
Enter. 
- 
If nothing is 
configured, type 
10.0.0.51 and 
Enter. 
 
Would you like to configure: y 
 
Press Enter to complete the 
configuration. 
 
As the service was already 
running, it must now restart 
to take effect. 
Press y to validate.

<<<PAGE 350>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Creation of an Employee SSID for BYOD 
Objective 
✓ Learn how to create an SSID dedicated for Employees with personal 
devices (BYOD: Bring Your Own Device) 
Contents 
1 
Briefing ......................................................................................... 2 
2 
Creating the BYOD SSID ...................................................................... 3 
2.1. Creating the BYODX SSID .......................................................................... 3 
2.2. Back to… Creating the BYODX SSID............................................................... 4 
2.3. Assigning the SSID to the AP Group .............................................................. 4 
3 
Testing the BYOD SSID ........................................................................ 4 
3.1. Setting Up the Linux Client to Connect to the BYODX SSID ................................... 4 
3.2. Verifying the connection > After the Web Authentication ................................... 6 
4 
Monitoring the Connections .................................................................. 6 
4.1. UPAM Monitoring .................................................................................... 6 
4.1.1. Authentication Record ..................................................................................... 6 
4.1.2. Captive Portal Access Record ............................................................................. 6 
5 
Debriefing ...................................................................................... 7

<<<PAGE 351>>>
1 
Creation of an Employee SSID for BYOD 
 
6 
Troubleshooting ............................................................................... 8 
6.1. Troubleshooting the Stellar AP ................................................................... 8 
6.1.1. Checking the DNS configuration .......................................................................... 8 
6.1.2. Checking the wireless configuration ..................................................................... 9 
6.1.3. Checking the Wi-Fi Channel ............................................................................... 9 
6.1.4. Checking the interface transmission power ............................................................ 9 
6.1.5. Checking the interface bitrate ......................................................................... 10 
6.2. Client Information ................................................................................. 10 
6.2.1. Listing the client(s) associated with the AP .......................................................... 10 
6.2.2. Checking the access logs of a specific client ......................................................... 11

<<<PAGE 352>>>
2 
Creation of an Employee SSID for BYOD 
 
 1 
Briefing 
In the previous Labs, we have learned how to create a secured Employees SSID and a Guests SSID. Now, let’s 
see how to create an Employees BYOD SSID, dedicated for the employees who want to bring and use their 
personal device within the company network.  
 
 
 
 
 
 
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 353>>>
3 
Creation of an Employee SSID for BYOD 
 
Creating a BYOD SSID can be decomposed in several steps:  
1. 
For this SSID, no additional VLANs need to be created: we will reuse the VLAN 20 (Employee) and 30 
(Guest). The BYOD employee device will be placed first in the Guest VLAN (pre-authentication). Once 
authenticated via a Captive Portal, it will be moved to the Employee VLAN(post-authentication). 
 
2. 
Create the SSID and configure its options. 
 2 
Creating the BYOD SSID 
Let’s create the BYODX SSID: 
 
 
2.1. 
Creating the BYODX SSID 
 
Create the SSID BYODX (X = R-Lab Number) 
 
> Select WLAN > SSIDs > SSIDs 
  > Click on the + button 
    > SSID Service Name: BYODX (X = R-Lab number) 
    > SSID: <filled automatically> 
    > Usage: Employee BYOD Network  
     > Enable BYOD Registration: YES 
    > Click on Create & Customize 
 
 
Notes > About the “Usage” 
During the SSID creation, a “Usage” is asked. When you select a Usage, a relevant related default configuration 
(Access Policy, Authentication Strategy, …) is automatically created.  
Employee BYOD Network > create a network for employees connecting with their own devices. Suitable for 
setting up an Open Network for Employee BYOD devices. Access to the network is granted after BYOD portal 
authentication. 
 
  > Allowed Band: 2.4GHz and 5 GHz

<<<PAGE 354>>>
4 
Creation of an Employee SSID for BYOD 
 
 
Tips > Help Menu 
As you can see, several settings can be managed in the SSID Creation properties. Take the time to learn more 
about each of them by clicking on the Help button.  
 
BYOD Access Strategy   
  > Click on Customize 
  > Scroll down to the Post Portal Authentication Enforcement section  
  > Select Fixed Access Role Profile: _EmployeesX (X = R-Lab Number) 
  > click Apply 
 
 
Tips > Fixed Access Role Profile 
Access Role Profile assigned to the BYOD device after it is authorized. After being authenticated, the client will 
have the “employee rights”. It will be, for example, moved to the VLAN Employee (VLAN 20) 
 
 
Tips > Employee Account 
During this lab, we will not create a new employee account, as we already have created one (“EmployeeX”) in 
the “secured Employee SSID” lab.  
2.2. 
Back to… Creating the BYODX SSID 
Default VLAN/Network 
  > VLAN ID: 30 
> Click on Save and Apply to AP Group 
 
 
Notes > VLAN ID 
The VLAN ID to insert is the default VLAN: by default, the personal device will be put in the VLAN 
30 (Guest VLAN). Then, after the authentication via the Captive Portal, the personal device will be 
transferred to the VLAN 20 (Employee VLAN). 
2.3. 
Assigning the SSID to the AP Group 
 
Assign the freshly created SSID BYODX to the AP Group APGX created in the previous lab 
 
Now that the SSID BYODX has been created, assign it to one or several AP Group(s): 
 
AP Group Assignment and Schedule 
> Click on Change Selection 
  > Remove default group from the SELECTED tab 
  > Move APGX (X = R-Lab Number) from AVAILABLE to SELECTED 
  > Click on OK 
> Click on Apply 
> Check the result on the page that is displayed  
 
Now that we have finished the configuration of the SSID, let’s test it! 
 3 
Testing the BYOD SSID 
 
Test the BYODX SSID by connecting on it via the BYODX account 
3.1. 
Setting Up the Linux Client to Connect to the BYODX SSID 
StellarClientX Raspberry Pi 
Left-click on the 
 icon 
(top right)

<<<PAGE 355>>>
5 
Creation of an Employee SSID for BYOD 
 
Select the SSID BYODX (X = R-
Lab Number) 
Check under “More Networks” 
if it is not displayed. 
 
 
 
Open a Web Browser with the 
icon 
 in the top left 
corner. 
 
Enter any non-https URL (ex: 
http://2.2.2.2) and you are 
redirected to the Captive 
Portal 
Enter the credentials: 
 
Username: Employee 
Password: password 
 
Check I accept the Terms of 
Use 
  
Click on Login 
 
The following message is then 
displayed 
 
 
 
Notes > Add more personal devices 
By clicking on this link, it is possible for the employee to manually add additional devices in the 
OmniVista 2500 database. After clicking this link: 
- Login with the employee credentials:  
 
 
 
Once logged, a page appears, where 2 tabs are available:  
- The Online Devices tab which displays all authenticated devices currently connected with this 
account

<<<PAGE 356>>>
6 
Creation of an Employee SSID for BYOD 
 
- The Remembered Devices which displays all authenticated BYOD devices saved in UPAM. It is 
also possible to manually add new Remembered devices by clicking on the 
 button (useful for 
headless devices, for example).  
3.2. 
Verifying the connection > After the Web Authentication  
From the OmniVista 2500, check that the StellarClientX virtual machine is now in the VLAN 20 (Employee): 
  
> Select WLAN > CLIENT > Client List 
  > Browse to the List of Clients on All APs section 
    > Locate the Client StellarClientX, then find the VLAN information 
 
 
 4 
Monitoring the Connections 
 
 
Display the BYODX authentication record  
4.1. 
UPAM Monitoring 
4.1.1. 
Authentication Record 
The UPAM platform (Unified Policy Authentication Manager) is embedded in the OmniVista 2500 NMS. This 
module is used to implement authentication (MAC authentication, 802.1x, Captive Portal…) 
The Authentication Record Screen displays authentication information for all devices authenticated 
through UPAM:  
> Select UPAM > AUTHENTICATION > Authentication Record 
 
4.1.2. 
Captive Portal Access Record 
To monitor the Captive Portal access: 
> Select UPAM > AUTHENTICATION > Captive Portal Access Record  
 
Another interesting feature that the OmniVista 2500 NMS offers is the ability to locate the AP, Switch 
and/or slot/port that is directly connected to a user-specified station: it is the Locator application.

<<<PAGE 357>>>
7 
Creation of an Employee SSID for BYOD 
 
 5 
Debriefing 
In this Lab, we have learned how to create an Employee SSID, dedicated for the employees who want to use 
their personal device within the company network (BYOD, Bring Your Own Device).

<<<PAGE 358>>>
8 
Creation of an Employee SSID for BYOD 
 
 6 
Troubleshooting 
In this part, we will cover the process to follow if there is an issue regarding the connection to a BYOD SSID. 
We will use the exact same infrastructure as in the lab:  
 
 
 
Notes > Before Beginning  
Before beginning this part, we assume that all the steps available in this lab have been followed correctly and 
checked: SSID creation, employee account creation…  
6.1. 
Troubleshooting the Stellar AP 
 
The Stellar console access is deactivated in Enterprise mode. 
To activate it, go to Network > AP Registration >AP Group, select APGX and click the Edit button. 
Under the Category SSH, activate the SSH Login option and enter: 
 
 
 
 
 
Click on Commit. Review the Success logs and click OK. 
6.1.1. 
Checking the DNS configuration 
A valid DNS configuration is mandatory in order to redirect successfully the client(s) to the Captive Portal 
Use exactly the following passwords: 
For Support Account: 
 
Password: Superuser=1 
For Root Account: 
 
Password: Stellar

<<<PAGE 359>>>
9 
Creation of an Employee SSID for BYOD 
 
page. To check the DNS configuration: 
 
support@AP-0E:E0:~$ cat /etc/resolv.conf 
# Interface wan 
nameserver 10.0.0.51 
search ale-training.com 
6.1.2. 
Checking the wireless configuration 
 
support@AP-0E:E0:~$ iwconfig 
[…] 
ath003    IEEE 802.11ng  ESSID:"BYOD0" 
          Mode:Master  Frequency:2.437 GHz  Access Point: DC:08:56:00:0E:E3 
          Bit Rate:192 Mb/s   Tx-Power=17 dBm 
          RTS thr:off   Fragment thr:off 
          Power Management:off 
          Link Quality=94/94  Signal level=-51 dBm  Noise level=-95 dBm 
          Rx invalid nwid:6  Rx invalid crypt:0  Rx invalid frag:0 
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0 
 
ath01-30  no wireless extensions. 
 
ath01-20  no wireless extensions. 
 
ath103    IEEE 802.11ac  ESSID:"BYOD0" 
          Mode:Master  Frequency:5.22 GHz  Access Point: DC:08:56:00:0E:EB 
          Bit Rate:800 Mb/s   Tx-Power=19 dBm 
          RTS thr:off   Fragment thr:off 
          Power Management:off 
          Link Quality=94/94  Signal level=-28 dBm  Noise level=-95 dBm 
          Rx invalid nwid:9  Rx invalid crypt:0  Rx invalid frag:0 
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0 […] 
6.1.3. 
Checking the Wi-Fi Channel 
To check which channel is used (ex. ath03 interface): 
 
support@AP-0E:E0:~$ iwlist ath003 channel 
ath03     57 channels in total; available frequencies : 
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
6.1.4. 
Checking the interface transmission power 
 
support@AP-0E:E0:~$ iwlist ath003 txpower 
ath03     8 available transmit-powers : 
          0 dBm         (1 mW) 
          5 dBm         (3 mW) 
          7 dBm         (5 mW) 
          9 dBm         (7 mW) 
          11 dBm        (12 mW) 
          13 dBm        (19 mW) 
          15 dBm        (31 mW) 
          17 dBm        (50 mW) 
          Current Tx-Power=17 dBm       (50 mW)

<<<PAGE 360>>>
10 
Creation of an Employee SSID for BYOD 
 
6.1.5. 
Checking the interface bitrate  
 
support@AP-0E:E0:~$ iwlist ath003 bitrate 
ath03     12 available bit-rates : 
          1 Gb/s 
          2 Gb/s 
          5.5 Gb/s 
          11 Gb/s 
          6 Gb/s 
          9 Gb/s 
          12 Gb/s 
          18 Gb/s 
          24 Gb/s 
          36 Gb/s 
          48 Gb/s 
          54 Gb/s 
          Current Bit Rate:192 Mb/s 
6.2. 
Client Information 
6.2.1. 
Listing the client(s) associated with the AP 
It is possible to list:  
- All the clients associated with the AP: 
 
support@AP-0E:E0:~$ ssudo sta_list 
SSID:Employees0 
 
STA_MAC                 IPv4            IPv6                    OnlineTime        RX       TX             
d4:6e:0e:18:60:38     10.7.0.38                                  242             237758  2121880 
FREQ          AUTH     Final_role                          VLANID  TUNNELID  FARENDIP 
2.4GHz        OPEN    __Employees0                           20     0 
 
- All the clients associated with a specific interface (ex. ath03 corresponding to the SSID BYOD0 in 2.4 
Ghz):  
 
support@AP-0E:E0:~$ ssudo wlanconfig ath003 list 
ADDR               AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE  TXSEQ  RXSEQ  CAPS XCAPS         
d4:6e:0e:18:60:38    1    6  72M     86M   63      60      64    0      0   65535   ESs  cORI           
 
ACAPS     ERP    STATE MAXRATE(DOT11) HTCAPS VHTCAPS ASSOCTIME    IEs   MODE                   PSMODE    
0          f              0              P        0gR 00:07:01    WME IEEE80211_MODE_11NG_HT20   0  
RXNSS TXNSS 
 1      1  
  
 Minimum Tx Power                : 5 
 Maximum Tx Power               : 18 
 HT Capability                  : Yes 
 VHT Capability                 : No 
 MU capable                     : No 
 SNR                            : 63 
 Operating band                 : 2.4 GHz 
 Current Operating class        : 0 
 Supported Rates                : 2  4  11  12  18  22  24  36  48  72  96  108.

<<<PAGE 361>>>
11 
Creation of an Employee SSID for BYOD 
 
- The parameters sent from the AP to the Wi-Fi Client(s):  
 
support@AP-83:60:~$ ssudo wam_debug sta_list 
{ 
        "status": "Success!!!", 
        "wlanServiceData": [ 
                { 
                        "iface": "ath03", 
                        "ssid": "BYOD0",                                   SSID Name 
                        "freq": "2.4GHz",                                  Frequency 
                        "security": "Open",                                Security  
                        "wlanService": "BYOD0",                            Assoc. WLAN Service 
                        "staData": [ 
                                { 
                                        "staMAC": "d4:6e:0e:18:60:38",      Wi-Fi Client MAC@ 
                                        "staIP": "10.7.0.38",               Wi-Fi Client IP@ 
                                        "staGlobalIPv6": "::", 
                                        "staLocalIPv6": "::", 
                                        "associationTime": 539,             Assoc. Time (seconds) 
                                        "mappingType": 0, 
                                        "assignedVLAN": 20,                 Wi-Fi Client Assigned VLAN 
                                        "assignedAR": "__Employees0",       Wi-Fi Client Assigned ARP 
                                        "assignedPL": "", 
                                        "macAuthResult": "SUCCESS", 
                                        "ARFromMACAuth": "__Employees0", 
                                        "PLFromMACAuth": "", 
                                        "redirectURLFromMACAuth": "", 
                                        "ARFrom8021xAuth": "", 
                                        "PLFrom8021xAuth": "", 
                                        "redirectURLFrom8021xAuth": "", 
                                        "CPAuthResult": "FAILED", 
                                        "ARFromCPAuth": "", 
                                        "PLFromCPAuth": "", 
                                        "ARFromRoaming": "", 
                                        "PLFromRoaming": "", 
                                        "redirectURLFromRoaming": "", 
                                        "classificationMatched": "none"  
[…] 
 
6.2.2. 
Checking the access logs of a specific client 
Find the MAC address of the client (ex. d4:6e:0e:18:60:38), then: 
 
support@AP-0E:E0:~$ cat /proc/kes_syslog | grep “d4:6e:0e:18:60:38”

<<<PAGE 362>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Radio Frequency Settings Configuration 
Objective 
✓ Learn how to configure the RF (Radio Frequency) Settings 
Contents 
1 
Briefing ......................................................................................... 2 
2 
Creating an RF Profile ........................................................................ 2 
2.1. General Settings .................................................................................... 2 
2.2. Smart Load Balance ................................................................................ 2 
2.2.1. Band Steering ............................................................................................... 2 
2.2.2. Exclude MAC OUI ........................................................................................... 2 
2.2.3. Force 5 GHz ................................................................................................. 2 
2.2.4. Association RSSI Threshold ................................................................................ 2 
2.2.5. Roaming RSSI Threshold ................................................................................... 3 
2.3. Per Band Info ........................................................................................ 4 
2.3.1. Default Setting .............................................................................................. 4 
2.3.2. Band .......................................................................................................... 4 
2.3.3. Channel Setting ............................................................................................. 4 
2.3.4. Client-aware ................................................................................................ 4 
2.3.5. Channel DRM ................................................................................................ 4 
2.3.6. Channel List ................................................................................................. 4 
2.3.7. Channel Width .............................................................................................. 4 
2.3.8. Power Setting ............................................................................................... 4 
2.3.9. Minimum and Maximum TX Power........................................................................ 4 
2.3.10. 
External Antenna Gain ................................................................................. 4 
2.3.11. 
Beacon interval ......................................................................................... 4 
2.3.12. 
Short Guard Interval ................................................................................... 5 
2.3.13. 
MU-MIMO ................................................................................................. 5 
2.3.14. 
High Efficiency .......................................................................................... 5

<<<PAGE 363>>>
1 
Radio Frequency Settings Configuration 
 
3 
Assigning the RF Profile to an AP/AP Group ............................................... 5 
3.1. Assigning the RF Profile ........................................................................... 5 
3.2. Connect to an SSID ................................................................................. 6 
3.3. Revert the RF Profile configuration .............................................................. 6 
4 
Debriefing ...................................................................................... 6 
5 
Troubleshooting ............................................................................... 7 
5.1. Troubleshooting the Stellar AP ................................................................... 7 
5.1.1. Checking the RF Profile configuration ................................................................... 8 
5.1.2. Displaying the client(s) RSSI value: ...................................................................... 9 
5.1.3. Checking the ACS and APC logs ........................................................................... 9

<<<PAGE 364>>>
2 
Radio Frequency Settings Configuration 
 
 1 
Briefing 
In the OmniVista 2500, and for Stellar Access Points, the Radio Frequency settings management is done via 
“RF Profiles”. A RF Profile contains all the radio frequency settings. Once created, it must be assigned to an 
AP or AP Group.  
 2 
Creating an RF Profile 
2.1. 
General Settings  
 
> Select WLAN > RF > RF Profile 
  > Click on the + button 
    > Name: My_RF_Profile 
    > Country/Region: <select your country/region> 
2.2. 
Smart Load Balance 
Smart Load Balance (SLB) is a feature that improves the user experience when accessing wireless 
connectivity by guiding a user's client device to connect to a free wireless channel or AP and denying 
access to APs with weak signal. 
2.2.1. 
Band Steering 
Band Steering controls the behavior of dual band clients and encourage them to use the 5 GHz band, 
which is generally less congested and provides higher speed. 
 
 
Warning > Why Band Steering is disabled by default? 
To function properly, band steering generally assumes that the coverage areas on both the 2.4 GHz bands and 5 
GHz bands are the same, or at least roughly equivalent. However, band steering will prove problematic if 
coverage on 5 GHz is significantly weaker and has coverage holes, as compared to coverage for 2.4 GHz. 
 
It can also cause problems. For example, a 5 GHz-capable device is automatically redirected to the 5 Ghz band 
by the band steering feature, even if the 5 GHz signal is low. 
 
Solution:  
- Design your networks for simultaneous 5 GHz and 2.4 GHz coverage.  
- For existing deployments where this may not be feasible, and your coverage is quite different on both bands, 
avoid using band steering or use the Exclude MAC OUI feature explained below.  
2.2.2. 
Exclude MAC OUI 
Excludes MAC OUI for band-steering (if Band Steering is enabled). The client will not utilize Band Steering 
and will be allowed to connect to the wireless band. This setting may be preferable for certain legacy and 
latency sensitive clients (e.g., scanners, MIPT Phones). 
2.2.3. 
Force 5 GHz 
With force 5 GHz, a dual-band client device will only be allowed to connect to the network on the 5 GHz 
band, and any requests to connect on the 2.4 GHz band will be ignored. This mode works quite well when 
the signal strength is good on the 5 GHz band but will prove problematic if there are weak coverage areas 
on 5 GHz because the network will not allow the client device to “fall back” to the 2.4 GHz network. 
2.2.4. 
Association RSSI Threshold 
This feature is used to set thresholds to optimize connectivity when associating with an AP by forbidding 
client access to networks with a weak wireless signal (RSSI, Received Signal Strength Indicator). Clients 
with an RSSI value lower that the Association RSSI Threshold will not be allowed to connect to the AP.

<<<PAGE 365>>>
3 
Radio Frequency Settings Configuration 
 
 
- Find the RSSI value of your StellarClient virtual machine (we will consider in the lab 
that this RSSI value is too low to connect to the SSIDs created previously) 
- Modify the Association RSSI Threshold to make StellarClient RSSI too low to connect 
the SSIDs created previously 
 
- Find the StellarClient signal strength Value 
 
> Before doing this, be sure that the StellarClientX virtual machine is connected to one of the SSIDs 
created in the previous labs! 
 
> Select WLAN > CLIENT > Client List  
  > Click on the Client in List of Clients on All APs 
  > Check (and note) the RSSI value (ex. -18 dBm) 
 
 
 
- Now, we are going to assume that the StellarClient signal strength (ex. -18 dBm) must be considered 
too weak to connect to the AP. To do so, we will set the Association RSSI Threshold to a value greater 
than the client RSSI value: 
 
 
Notes > RSSI vs dBm 
dBm and RSSI are different units of measurement that both represent the same thing: signal strength. The 
difference is that RSSI is a relative index, while dBm is an absolute number representing power levels in mW 
(milliwatts). 
 
In the OmniVista 2500 NMS:  
- The clients signal strength is given in dBm 
- The Stellar AP’s RF settings are configured in RSSI 
 
For this exercise, we need to translate the client signal strength from dBm to RSSI. To do so, please refer to 
the following table (to convert the RSSI value to dBm you just need to subtract 96 to the RSSI value):  
 
dBm 
-20 
-19 
-18 
-17 
-16 
-15 
… 
-10 
RSSI 
76 
77 
78 
79 
80 
81 
… 
86 
 
> Go back to WLAN > RF > RF Profile 
  > Select the profile My_RF_Profile 
  > Scroll down to the Smart Load Balance section 
  > Modify the Association RSSI Threshold for all the bands to a value much higher than the Client 
value (ex. 90, which is higher than -18 dBm = 78) and click Apply 
 
 
 
Notes 
We will test this feature in the next section, as the RF Profile must be first applied to the desired AP or AP 
Group.  
 
2.2.5. 
Roaming RSSI Threshold 
This feature is used to set thresholds to optimize connectivity when roaming by forbidding client access to 
networks with a weak wireless signal (RSSI). Clients with an RSSI value lower than the Roaming RSSI 
Threshold value will be guided to roam to another AP with a better transmission signal.

<<<PAGE 366>>>
4 
Radio Frequency Settings Configuration 
 
2.3. 
Per Band Info 
 
 
Disable all the 5G Band (All, Low, High) 
2.3.1. 
Default Setting 
Disable it to set custom bandwidth settings. Enable it to reset bandwidth settings to default values. 
2.3.2. 
Band 
Configures the working radio for the AP. 
2.3.3. 
Channel Setting 
Configures the working channel of the radio (auto = dynamically assigned via ACS, Auto Channel Selection) 
2.3.4. 
Client-aware 
When enabled, the Auto Channel Selection does not change channels for Stellar APs with connected client. 
When disabled, the Stellar AP may change to a more optimal channel but may disrupt connected clients. 
2.3.5. 
Channel DRM 
Enables/Disables the channel scope specification definition that will be applicable for Auto-Channel 
Selection. 
2.3.6. 
Channel List 
Specifies the channel list that will be applicable for Auto-Channel Selection. 
2.3.7. 
Channel Width 
Configures the channel width for 2.5 and 5G radio. Channel width is used to control how broad the signal 
is for transferring data. By increasing the channel width, you can increase the speed and throughput of a 
wireless broadcast. However, larger channel width brings more unstable transmission in crowded areas 
with a lot of frequency noise and interference. 
2.3.8. 
Power Setting 
Configures the transmit power of the wireless radio. 
2.3.9. 
Minimum and Maximum TX Power 
Specify the minimum and maximum transmit power for auto power setting. 
2.3.10. External Antenna Gain 
Specify the gain value of the external AP antenna. Only the Stellar APs with external antennas (AP1222, 
AP1332,…) will be configured with this attribute. 
2.3.11. Beacon interval 
Beacon period for the AP. Indicates how often the 802.11 beacon management frames are transmitted by 
the AP.

<<<PAGE 367>>>
5 
Radio Frequency Settings Configuration 
 
2.3.12. Short Guard Interval 
Guard Interval is used to ensure that distinct transmissions occur between the successive data symbols 
transmitted by a device. This would provide approximately an 11% increase in data rates. However, using 
the Short Guard Interval will result in higher packet error rates when the delay spread of the RF channel 
exceeds the Short Guard Interval, or if timing synchronization between the transmitter and receiver is not 
precise. 
Validate the creation of the RF Profile:  
 
> Click on Create 
2.3.13. MU-MIMO 
Enables/Disables Multi-User, Multiple-Input, Multiple-Output feature. If enabled, the AP can communicate 
with multiple users simultaneously. It decreases the time each device has to wait for a signal and speeds 
up the network 
2.3.14. High Efficiency 
Enables/Disables 802.11ax high efficiency wireless feature. If disabled, a High Efficiency mode capable AP 
will downgrade to VHT (Very High Throughput) mode.  
 3 
Assigning the RF Profile to an AP/AP Group  
3.1. 
Assigning the RF Profile 
 
> Select NETWORK > AP REGISTRATION > AP Group 
  > Select the AP Group APGX (X = R-Lab Number) 
  > Click on Edit 
  > In the General section:  
    > RF Profile: My_RF_Profile  
    > Click on Commit 
 
 
Notes 
Note that it is also possible to assign an RF Profile to a specific AP (instead of an AP Group). To do so, go to the 
NETWORK > AP REGISTRATION > Access Points menu. 
 
 
Tips 
The RF Profile can also be created directly from the AP/AP Group, in the Edit mode, by clicking on Add New:  
 
 
 
 
Now that the RF Profile My_RF_Profile is applied to the APGX Group, try to connect to 
one SSID from the StellarClient virtual machine.

<<<PAGE 368>>>
6 
Radio Frequency Settings Configuration 
 
3.2. 
Connect to an SSID 
As the StellarClient RSSI = 70 is less than the Association RSSI Threshold = 90, then it is not possible for the 
StellarClient (and other devices with a RSSI less than 90) to connect to any SSID broadcasted by the APGX 
Group.  
 
Connect you Wi-Fi client to one of your SSID. 
The client tries to associate to the SSID but is not able to. The Stellar AP will ignore all association requests 
from the Wi-Fi client as the power of its signal is lower than the threshold. 
 
3.3. 
Revert the RF Profile configuration 
In the current state, no Wi-Fi clients can connect to any of your SSID. 
Assign the default RF Profile back to the AP Group APGX: 
 
> Select NETWORK > AP REGISTRATION > AP Group 
  > Select the AP Group APGX (X = R-Lab Number) 
  > Click on Edit 
  > In the General section:  
    > RF Profile: default profile  
    > Click on Commit 
 4 
Debriefing 
During this lab, we have learned that the OmniVista 2500 provides an easy way to manage the Stellar Access 
Points radio frequency settings.  
We have also learned that a lot of settings are available and can be enabled or disabled depending on the 
infrastructure deployed.

<<<PAGE 369>>>
7 
Radio Frequency Settings Configuration 
 
 5 
Troubleshooting 
In this part, we will cover the process to follow if there is an issue regarding the RF Profile and RF Profile 
settings assignment. We will use the exact same infrastructure as in the lab:  
 
 
5.1. 
Troubleshooting the Stellar AP 
 
The Stellar console access is deactivated in Enterprise mode. 
To activate it, go to Network > AP Registration >AP Group, select APGX and click the Edit button. 
Under the Category SSH, activate the SSH Login option and enter: 
 
 
 
 
 
Click on Commit. Review the Success logs and click OK. 
 
 
 
Use exactly the following passwords: 
For Support Account: 
 
Password: Superuser=1 
For Root Account: 
 
Password: Stellar

<<<PAGE 370>>>
8 
Radio Frequency Settings Configuration 
 
5.1.1. 
Checking the RF Profile configuration 
 
support@AP-83:60:/tmp$ cat /tmp/config/rfprofile.conf 
{ 
        "RFService":[ 
                { 
                        "bandSteering":"disable", 
                        "bandSteeringForce5g":"disable", 
                        "LoadBalance":"disable", 
                        "backgroundScanning":"enable", 
                        "scanningEnhance":"disable", 
                        "countryCode":"FR", 
                        "scanningInterval":20, 
                        "scanningDuration":50, 
                        "voiceVedioAwareness":"enable", 
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
                                        "signalStrengthThreshold":90, 
                                        "roamingSignalStrengthThreshold":0, 
                                        "powerValMax":"0", 
                                        "powerValMin":"0", 
                                        "radioMode":"normal", 
                                        "scanDuration":"normal", 
                                        "Gain":"3", 
                                        "clientAwareness":"disable" 
                                }, 
                                "5G_high":{ 
                                        "band":"enable", 
                                        "channelSetting":"AUTO", 
                                        "channelWidth":20, 
                                        "autoChannelWidth":"enable", 
                                        "globalChannelWidth":20, 
                                        "powerSetting":"AUTO", 
                                        "shortGuardInterval":"enable", 
                                        "signalStrengthThreshold":90, 
                                        "roamingSignalStrengthThreshold":0, 
                                        "powerValMax":"0", 
                                        "powerValMin":"0", 
                                        "radioMode":"normal", 
                                        "scanDuration":"normal", 
                                        "Gain":"4", 
                                        "clientAwareness":"disable" 
                                }, 
                                "5G_low":{ 
                                        "band":"enable", 
                                        "channelSetting":"AUTO", 
                                        "channelWidth":20, 
                                        "autoChannelWidth":"enable", 
                                        "globalChannelWidth":20, 
                                        "powerSetting":"AUTO", 
                                        "shortGuardInterval":"enable", 
                                        "signalStrengthThreshold":90, 
                                        "roamingSignalStrengthThreshold":0, 
                                        "powerValMax":"0", 
                                        "powerValMin":"0", 
                                        "radioMode":"normal", 
                                        "scanDuration":"normal", 
                                        "Gain":"4", 
                                        "clientAwareness":"disable" 
                                }, 
                                "5G_all":{ 
                                        "band":"enable", 
                                        "channelSetting":"AUTO", 
                                        "channelWidth":40,

<<<PAGE 371>>>
9 
Radio Frequency Settings Configuration 
 
                                        "autoChannelWidth":"enable", 
                                        "globalChannelWidth":20, 
                                        "powerSetting":"AUTO", 
                                        "shortGuardInterval":"enable", 
                                        "signalStrengthThreshold":90, 
                                        "roamingSignalStrengthThreshold":0, 
                                        "powerValMax":"0", 
                                        "powerValMin":"0", 
                                        "radioMode":"normal", 
                                        "scanDuration":"normal", 
                                        "Gain":"4", 
                                        "chainmask":15, 
                                        "clientAwareness":"disable" 
                                } 
                        }, 
                        "scanRadioInfo":{ 
                                "radioMode":"normal", 
                                "scanDuration":"normal" 
[…] 
 
5.1.2. 
Displaying the client(s) RSSI value:  
 
support@AP-0E:E0:~$ ssudo wlanconfig ath102 list 
ADDR               AID CHAN TXRATE RXRATE RSSI MINRSSI MAXRSSI IDLE  TXSEQ  RXSEQ  CAPS XCAPS         
d4:6e:0e:18:60:38    1   44   6M     72M   64      63      67    0      0   65535    Es    OI           
 
ACAPS     ERP    STATE MAXRATE(DOT11) HTCAPS VHTCAPS ASSOCTIME    IEs   MODE                   PSMODE    
0          b              0             WPS   2gGR    00:10:10    WME IEEE80211_MODE_11AC_VHT40  0  
RXNSS TXNSS 
 1      1  
[…] 
5.1.3. 
Checking the ACS and APC logs 
 
support@AP-83:60:/tmp$ cat /proc/kes_syslog | grep DRM

<<<PAGE 372>>>
REMOTE ACCESS POINT (RAP)
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 373>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Identify the role and advantages of the RAP 
feature
• List the equipment required for the 
deployment of the RAP feature
• Summarize the steps to configure the RAP 
feature

<<<PAGE 374>>>
INTRODUCTION
• Use Cases
• Shops > Access to the corporate network to check 
the inventory
• Booth > Events (forum, exhibition…) 
• RAP = Remote Access Point
• Goal 
• Extend the corporate network to remote site(s)
INTERNET
STELLAR AP (RAP)
ROUTER
USER
BRANCH/HOME OFFICE
COMPANY HQ
CORPORATE
NETWORK
FIREWALL
CORPORATE SSID
CORPORATE SSID

<<<PAGE 375>>>
* AP1101 not compatible with the RAP Feature
EQUIPMENTS
• OmniVista Cirrus 4 > Freemium Account
with OmniVista 2500
• OmniVista Cirrus 4 > Premium Account
BRANCH/HOME OFFICE
STELLAR AP (RAP)*
ALE VPN SERVER
COMPANY HQ
OMNIVISTA 2500
OMNIVISTA CIRRUS 4
CLOUD
FREEMIUM
BRANCH/HOME OFFICE
STELLAR AP (RAP)*
ALE VPN SERVER
COMPANY HQ
OMNIVISTA CIRRUS 4
CLOUD
PREMIUM

<<<PAGE 376>>>
COMMISSIONING > OMNIVISTA CIRRUS 4 
(PREMIUM ACCOUNT)

<<<PAGE 377>>>
COMMISSIONING STEPS & TOPOLOGY
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – Configuration Settings Retrieval
3 - VPN Tunnel (Client Traffic) Establishment
4 – Client Connection
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET

<<<PAGE 378>>>
[PRE] – SETTINGS TO BE ENTERED BY THE ADMINISTRATOR
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – Configuration Settings Retrieval
3 - VPN Tunnel (Client Traffic) Establishment
4 – Client Connection
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET
SETTINGS (OV CIRRUS 4)
• STELLAR AP MAC@ 
• VPN SERVER PUB. IP@ 
• VPN CLIENT IP@ 
• AP SETTINGS
SETTINGS (VPN SERVER)
• PUBLIC IP@
• PRIVATE IP@
• VPN SETTINGS (KEYS…)
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)

<<<PAGE 379>>>
1 – STELLAR ACCESS POINT STARTUP & REGISTRATION
• The Stellar AP starts up
• The Stellar AP automatically tries to reach the 
OmniVista Cirrus 4
• The OmniVista Cirrus 4 identify the Stellar AP by its MAC 
address. 
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
3 - VPN Tunnel (Management Traffic) Establishment
4 – Client Connection
2 – Configuration Settings Retrieval
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET
•
MAC ADDRESS
SETTINGS (OV CIRRUS 4)
• STELLAR AP MAC@

<<<PAGE 380>>>
2 – CONFIGURATION SETTINGS RETRIEVAL
• The Stellar AP connects to the OmniVista Cirrus 4
• The OmniVista Cirrus 4 sends to the Stellar AP: 
• VPN Server public IP Address
• IP Address (VPN Client)
• AP Settings (SSID(s) to broadcast , radiofrequency
settings…)
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – Configuration Settings Retrieval
3 - VPN Tunnel (Client Traffic) Establishment
4 – Client Connection
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET
•
IP@ (CLIENT VPN)
•
VPN SERVER PUBLIC IP@
•
AP CONFIG. SETTINGS
SETTINGS (OV CIRRUS 4)
• STELLAR AP MAC@ 
• VPN SERVER PUB. IP@ 
• VPN CLIENT IP@ 
• AP SETTINGS
•
IP@ (CLIENT VPN)
•
VPN SERVER PUBLIC IP@
•
AP SETTINGS
INFORMATION RECEIVED BY THE AP

<<<PAGE 381>>>
3 - VPN TUNNEL (CLIENT TRAFFIC) ESTABLISHMENT
• The Access Point connects to the VPN Server
• A VPN is established between the RAP <> VPN Server
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – Configuration Settings Retrieval
3 - VPN Tunnel (Client Traffic) Establishment
4 – Client Connection
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
•
IP@ (CLIENT VPN)
•
VPN SERVER PUBLIC IP@
•
AP SETTINGS
INFORMATION RECEIVED BY THE AP
VPN TUNNEL

<<<PAGE 382>>>
4 – CLIENT CONNECTION
• Client on remote site
• Connection on the SSID reserved for employees
• Access to the corporate network
• Client’s data traffic > VPN tunnel
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – Configuration Settings Retrieval
3 - VPN Tunnel (Client Traffic) Establishment
4 – Client Connection
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
•
IP@ (CLIENT VPN)
•
VPN SERVER PUBLIC IP@
•
AP SETTINGS
INFORMATION RECEIVED BY THE AP
VPN TUNNEL
CORPORATE
NETWORK
CORPORATE SSID
EMPLOYEE

<<<PAGE 383>>>
COMMISSIONING > OMNIVISTA 2500
> OMNIVISTA CIRRUS 4 (FREEMIUM ACCOUNT)

<<<PAGE 384>>>
COMMISSIONING STEPS & TOPOLOGY
2 - VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM

<<<PAGE 385>>>
[PRE] – SETTINGS TO BE ENTERED BY THE ADMINISTRATOR
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
SETTINGS (OV CIRRUS 4)
• STELLAR AP MAC@ 
• MODE > RAP
• VPN SERVER PUB. IP@ 
• OV 2500 SERVER IP@ 
• VPN CLIENT IP@ 
SETTINGS (VPN SERVER)
• PUBLIC IP@
• PRIVATE IP@
• VPN SETTINGS (KEYS…)
SETTINGS (OV 2500)
• AP SETTINGS

<<<PAGE 386>>>
1 – STELLAR ACCESS POINT STARTUP & REGISTRATION
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
• The Stellar AP starts up
• The Stellar AP automatically tries to reach the 
OmniVista Cirrus 4
• The OmniVista Cirrus 4 identify the Stellar AP by its
MAC address. 
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
•
MAC ADDRESS
SETTINGS (OV CIRRUS 4)
• STELLAR AP MAC@

<<<PAGE 387>>>
2 – VPN & OMNIVISTA 2500 SETTINGS RETRIEVAL
• The Stellar AP connects to the OmniVista Cirrus 4
• The OmniVista Cirrus 4 sends to the Stellar AP: 
• Mode (RAP) 
• IP Address (Client VPN)
• VPN Server public IP Address
• OmniVista 2500 NMS Server IP Address
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
SETTINGS (OV CIRRUS 4)
• STELLAR AP MAC@ 
• MODE > RAP
• VPN SERVER PUB. IP@ 
• OV 2500 SERVER IP@ 
• VPN CLIENT IP@ 
•
Mode = RAP
•
IP@ (VPN Client)
•
VPN Server pub. IP@ 
•
IP@ OV 2500
•
MODE = RAP
•
IP@ (VPN CLIENT)
•
VPN SERVER PUB. IP@ 
•
OV 2500 IP@ 
INFORMATION RECEIVED BY THE AP

<<<PAGE 388>>>
3 - VPN TUNNEL (MANAGEMENT TRAFFIC) ESTABLISHMENT
• The Remote Access Point (RAP) connects to the
VPN Server
• A VPN is established between the RAP <> VPN Server
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
VPN TUNNEL
•
MODE = RAP
•
IP@ (VPN CLIENT)
•
VPN SERVER PUB. IP@ 
•
OV 2500 IP@ 
INFORMATION RECEIVED BY THE AP

<<<PAGE 389>>>
4 – CONFIGURATION SETTINGS RETRIEVAL
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
2 – VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
• RAP connects to the OmniVista 2500 server 
• The OmniVista 2500 sends its configuration to the RAP: 
• SSID(s) to broadcast 
• Radio frequency settings 
• …
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
SETTINGS (OV 2500)
• AP SETTINGS
VPN TUNNEL
•
MODE = RAP
•
IP@ (VPN CLIENT)
•
VPN SERVER PUB. IP@ 
•
OV 2500 IP@ 
•
AP SETTINGS
INFORMATION RECEIVED BY THE AP

<<<PAGE 390>>>
5 – VPN TUNNEL (CLIENTS TRAFFIC) & CLIENT CONNECTION
• 2nd VPN tunnel is established (clients data traffic)
• Client on remote site
• Connects to the Clients SSID
• Access to the corporate network
• Client data traffic > VPN Tunnel
2 – VPN & OmniVista 2500 Settings Retrieval
3 - VPN Tunnel (Management Traffic) Establishment
4 – Configuration Settings Retrieval
5 – VPN Tunnel (Clients Traffic) & Client Connection
1 – Stellar Access Point Startup & Registration
[PRE] – Settings to be Entered by the Administrator
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
CORPORATE
NETWORK
CORPORATE SSID
EMPLOYEE

<<<PAGE 391>>>
USE CASE > RAP & REMOTE WORKING
REMOTE WORKERS
RAP
LAB SSID
EMPLOYEES SSID
INTERNET
ALE VPN 
SERVER
COMPANY HQ
LAB SSID
EMPLOYEES SSID
VISITORS SSID
VPN TUNNEL
CORPORATE
NETWORK
Local Breakout
VLAN tagging
EMPLOYEES VLAN
LAB VLAN

<<<PAGE 392>>>
CONFIGURATION STEPS

<<<PAGE 393>>>
> Connecting the Remote AP
2 – Deploying & Configuring the "VPN Server" VM
1 – Configuring the OmniVista Cirrus 4
• Declaring the Remote AP (Serial Nb / MAC@)
• Configuring the VPN settings (VPN > clients traffic)
• Public IP@ / Port
• VPN Server IP@
• IP@ / IP@ range of VPN clients
• Exporting the VPN settings (VPN > clients traffic)
• Configuring the AP settings
• SSID(s) to broadcast
• Radio frequency settings
• …
• Deploying the « VPN Server » VM (provided by ALE)
• Configuring the network interfaces
• Interface 1 (ex. eth0) > public IP@ 
• Importing the VPN settings
• Interface 2 (ex. eth1) > VPN « clients traffic »
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
CIRRUS 4
CLOUD
PREMIUM
INTERNET
CONFIGURATION STEPS
OmniVista Cirrus 4 (Premium Account)

<<<PAGE 394>>>
> Connecting the Remote AP
• Declaring the Remote AP (Serial Nb / MAC@)
• Configuring the VPN settings (management traffic) 
• Public IP@ / Port
• VPN Server IP@
• IP@ / IP@ range of VPN clients
• Exporting the VPN settings 
• Deploying the « VPN Server » VM (provided by ALE)
• Configuring the network interfaces
• Interface 1 (ex. eth0) > public IP@ 
• Interface 2 (ex. eth1) > private IP@ 
• Importing the VPN settings
• Configuring the 2nd VPN (clients traffic) settings in the 
OV2500 and importing it in the VPN server
(Interface 3, ex. eth2)
• Configuring the AP settings
• SSID(s) to broadcast
• Radio frequency settings
• …
BRANCH/HOME OFFICE
STELLAR AP 
(RAP)
INTERNET
ALE VPN 
SERVER
COMPANY HQ
OMNIVISTA
2500
OMNIVISTA
CIRRUS 4
CLOUD
FREEMIUM
CONFIGURATION STEPS
OmniVista Cirrus 4 (Freemium Account) & OmniVista 2500
1 – Configuring the OmniVista Cirrus 4
3 – Configuring the OmniVista 2500
2 – Deploying & Configuring the "VPN Server" VM

<<<PAGE 395>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 396>>>
WIFI BRIDGE & WIFI MESH
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 397>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Define the purpose of a WiFi Bridge 
topology
• Define the purpose of a WiFi Mesh topology
• Discover the Auto Mesh feature 
• Configure a WiFi Bridge or WiFi Mesh 
topology on OmniAccess Stellar Access 
Points

<<<PAGE 398>>>
AIM
• Replace physical cabling
* AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge.
WIFI BRIDGE VS WIFI MESH 
• WiFi Mesh
• WiFi Bridge
USE CASE
• Coverage of a camping
PROPERTIES
• VLANs can be used to separate & secure traffic over the 
bridge*
• Cannot provide service (WiFi) to WiFi clients
USE CASE
• Buildings separated by a street
LAN EXTENSION NOT POSSIBLE
WIFI BRIDGE
PROPERTIES
• VLANs can be used to separate & secure traffic coming
from Wi-FI clients connected on different SSID. 
• Can provide service (WiFi) to WiFi clients

<<<PAGE 399>>>
WIFI BRIDGE - ATTRIBUTES
• SSID
• WLAN used to setup wireless bridge connection
• Must be the same on both APs
• Band
• Wireless bridge working frequency
• Must be the same on both APs
• Is Root
• Specify the root AP of the wireless bridge
• 1 AP must be set as Root
• Passphrase
• Password of the WLAN
• Must be the same on both APs
WIFI BRIDGE
SSID: STELLAR-BRIDGE
BAND: 5 GHZ
IS ROOT: YES
PASSPHRASE: ALCATEL123!
SSID: STELLAR-BRIDGE
BAND: 5 GHZ
IS ROOT: NO
PASSPHRASE: ALCATEL123!
WIFI MESH – BEST PRACTICE
• BAND: 5 GHZ (OR 6GHZ)
• CHANNEL > 100

<<<PAGE 400>>>
SSID: WIFI GUESTS
BAND: 2.4 GHZ & 5 GHZ
SECURITY: OPEN
WIFI MESH - ATTRIBUTES
• SSID
• WLAN used to setup wireless Mesh connection
• Must be the same on both APs
• Band
• Wireless Mesh working frequency
• Must be the same on both APs
• Is Root
• Specify the root node of the wireless Mesh
• Multiple APs can be defined as root 
• Passphrase
• Password of the WLAN
• Must be the same on both APs
SSID: WIFI GUESTS
BAND: 2.4 GHZ & 5 GHZ
SECURITY: OPEN
SSID: STELLAR-MESH 
BAND: 5 GHZ
IS ROOT: YES
PASSPHRASE: ALCATEL123!
SSID: STELLAR-MESH 
BAND: 5 GHZ
IS ROOT: NO
PASSPHRASE: ALCATEL123!
WIFI MESH – LIMITATIONS
• UP TO 4 HOPS
• UP TO 5 APS IN A SINGLE HOP IN A PEER TO MULTI PEER CONNECTION
• UP TO 16 APS IN THE MESH NETWORK
• ALL APS CAN BROADCAST UP TO 5 SSIDS FOR CLIENTS
WIFI MESH – BEST PRACTICE
• BAND: 5 GHZ (OR 6GHZ)
• CHANNEL > 100

<<<PAGE 401>>>
AUTO MESH
• Aim: quick & easy deployment of a Mesh topology
ROOT
DEFAULT SSID: STELLAR-MESH
DEFAULT BAND: 5 GHZ
• If a Stellar AP is: 
• Connected to the LAN   
• Configured as MESH root
• It will
• Broadcast an hidden SSID « Stellar-MESH »
• Band: 5 GHz
• If a Stellar AP is: 
• Not connected to the LAN   
• It will
• Have MESH enabled as non-root
• Broadcast an hidden SSID « Stellar-MESH »
• Band: 5 GHz
DEFAULT SSID: STELLAR-MESH
DEFAULT BAND: 5 GHZ

<<<PAGE 402>>>
CONFIGURATION

<<<PAGE 403>>>
EXPRESS MODE
Mesh & Bridge Configuration Videos
Bridge Configuration
MESH Configuration
Auto MESH Configuration

<<<PAGE 404>>>
ENTERPRISE MODE
Mesh & Bridge Configuration Videos

<<<PAGE 405>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 406>>>
OMNIVISTA CIRRUS 4 - SOLUTION OVERVIEW
OMNIACCESS STELLAR WLAN
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 407>>>
Upon completion this module, 
you will be able to:
OBJECTIVES
• Understand the OmniVista CIRRUS 4 
subscription and licensing model 
• Register a network device on OmniVista 
CIRRUS 4

<<<PAGE 408>>>
OVERVIEW

<<<PAGE 409>>>
OMNIVISTA CIRRUS 4 ?
• Cloud based OmniVista NMS
• Software as a Service (SaaS) mode
• Subscription based service
• Zero Deployment/Zero Footprint
• Full Network Control
• Unified LAN & WLAN management
• Central Management for Provisioning, Maintenance, Monitoring,…
• Limit per OmniVista instance:
• Up to 5000 devices
• Up to 4000 APs 
OmniVista® CIRRUS 
instances in Cloud
OmniAccess® Stellar 
OmniSwitch®
Secured Internet 
(HTTPs & VPN tunnels)
Web 
Client

<<<PAGE 410>>>
SUBSCRIPTION MODEL
Freemium
Self Registration
Free of charge
No device capacity limitation 
No duration limitation
No network Configuration
On-time Network Device Upgrade
Restricted OV CIRRUS capabilities
Can be upgraded to Premium
Premium
All OV CIRRUS capabilities 
Based on OV CIRRUS Subscription
Flexible Device type, capacity and Duration 
Subscription done through 
ALE Business Store/CPQ or eBUY/OVCirrus
Max amount of licenses: 5000 included 
Stellar APs and OmniSwitch
Subscription Expansion, reduction or renewal

<<<PAGE 411>>>
LICENSES
OV CIRRUS
LAN Core
OS6900
Stellar AP 
All AP models
LC
SA
LE
LA
LAN Essential 
OS2260
OS2360
OS6360
OS6465
OS6560 
LAN Advanced
OS6860N
OS6865 
OS6870
Duration of 1, 3 or 5 Years
1 license per Access Point
50xGuest and 50xBYOD licenses
included per AP license
OV CIRRUS Premium Subscription
4000 AP licences
Max 5000 Device licences

<<<PAGE 412>>>
NETWORK DEPLOYMENT

<<<PAGE 413>>>
DEVICE REGISTRATION STEPS
Customer network minimum configuration
OV CIRRUS Account Creation
Network device required OS upgrade
Customer Network
Restarting Activation Process
Adding devices to OV Catalog
Freemium
OmniVista CIRRUS 4
Premium
Device Registration Completion
Assigning OV CIRRUS Licenses to devices
Setting Pre-Provisioning parameters
Restarting Activation Process
Restarting Activation Process

<<<PAGE 414>>>
CUSTOMER NETWORK
• Minimal Software version
• OmniVista CIRRUS 4 Subscription validated
• Freemium or Premium account created
OV CIRRUS Account creation
OS version required on Network Device 
Device Software
Product
AOS 8.4.1.R03 +
OS6560, OS6860N, OS6865, 
OS6870, OS6900
AOS 6.7.2.R03 +
OS6350, OS6450
AOS 5.1R1 +
OS2260, OS2360
AWOS 3.0.2 +
All Stellar Access Point models

<<<PAGE 415>>>
CUSTOMER NETWORK
Customer network minimum configuration
Factory default
(DHCP process) 
or 
Manual Configuration
or Auto-config
(greenfield)
or
Pre-configured
(brownfield)
Factory default
(DHCP process)

<<<PAGE 416>>>
ADDING DEVICES TO OV CATALOG
Click on the image above to visualize the video

<<<PAGE 417>>>
RESTARTING ACTIVATION PROCESS
Device Re-activation
AOS
Waiting For First Contact
Registered
Restart the Cloud Agent
-> cloud-agent admin-state disable force
or
Manually Reboot the Device
-> reload from working no rollback-timeout
# firstboot –y
# reboot
AP Powered on
After ~20s of the boot sequence
Press the [f] key and it [enter] 
to enter failsafe mode

<<<PAGE 418>>>
ASSIGNING OV CIRRUS LICENSES TO DEVICES
1
2

<<<PAGE 419>>>
SETTING PRE-PROVISIONING PARAMETERS
Click on the image above to visualize the video

<<<PAGE 420>>>
SETTING PRE-PROVISIONING PARAMETERS
Stellar AP

<<<PAGE 421>>>
Restarting Activation Process
AOS
Waiting For First Contact
Registered
Device Registration Completion
Device Catalog
Managed devices
DEVICE ACTIVATION

<<<PAGE 422>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 423>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Backup, Restore & Upgrade 
Objective 
✓ Backup & Restore and Upgrade the Network Devices 
Contents 
1 
Briefing ......................................................................................... 2 
2 
Saving the Current Configuration ........................................................... 3 
2.1. From the Notification Area........................................................................ 3 
3 
Backing Up the Devices Configuration ..................................................... 3 
3.1.1. Backing Up AOS OmniSwitches ............................................................................ 3 
3.1.2. Backing Up Stellar APs Devices ........................................................................... 4 
4 
Restoring the Devices Configuration ....................................................... 5 
4.1. Restoring an AOS Device Configuration ......................................................... 5 
4.1.1. Briefing ...................................................................................................... 5 
4.1.2. Modifying the OmniSwitches Configuration ............................................................. 5 
4.1.3. Restoring the OmniSwitch 6870 Configuration ......................................................... 6 
4.1.4. Checking the Result ........................................................................................ 6 
4.2. Restoring a Stellar Device Configuration ........................................................ 6 
5 
Debriefing ...................................................................................... 7

<<<PAGE 424>>>
1 
Backup, Restore & Upgrade 
 
6 
Annex: Upgrading an Image (Resource Manager) ......................................... 8 
6.1. Importing the Upgrade Files ...................................................................... 8 
6.2. Installing the Upgrade Files ....................................................................... 8 
7 
Annex: Upgrading an Image (Access Point Web Page) ................................... 9 
7.1. Enabling the Web Management ................................................................... 9 
7.2. Accessing to the Web Management Interface .................................................. 9 
7.3. Upgrading the Firmware ........................................................................... 9

<<<PAGE 425>>>
2 
Backup, Restore & Upgrade 
 
 1 
Briefing 
At this stage of the training, we have a fully operational infrastructure with the devices deployed, SSID 
broadcasted, and QoS & ACLs setup. In this lab, we will learn how to backup and restore the devices 
configuration.  
 
 
 
 
 
 
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 426>>>
3 
Backup, Restore & Upgrade 
 
 2 
Saving the Current Configuration 
 
Save all the management done during this training as Running configuration 
2.1. 
From the Notification Area 
Let’s begin by saving the current configuration as Running. 
 
> Click on the bell icon on the top right and corner 
  > Click on the floppy icon    Save All 
    > Click on OK to confirm  
 
Check that the operation has been successfully completed. Then click on Finish 
 
 
 
 
Notes > Save to Running 
It is also possible to save the configuration to the running directory from the Topology application. This feature 
will be covered in the next lab.  
 3 
Backing Up the Devices Configuration 
A dedicated application is available in the OmniVista 2500 to perform the backup and restore operations of 
AOS: The Resource Manager.  
 
 
Backup the configuration files of all the devices 
3.1.1. 
Backing Up AOS OmniSwitches  
 
> Select CONFIGURATION > RESOURCE MANAGER > Backup/Restore 
  > Click on the BACKUP button  
 
1. Backup Method 
    > Select Backup By Devices 
    > Click on Next 
 
2. Device Selection 
    > Click on ADD > Use Switch Picker 
      > Click on Add All to add all the OmniSwitches 
      > Click on OK 
    > Click on Add FTP Authentication  
      > Username: admin 
      > Password: switch 
      > Check Apply FTP Authentication for all missed devices 
      > Click on Apply 
      > Click on Close 
    > Click on Next

<<<PAGE 427>>>
4 
Backup, Restore & Upgrade 
 
3. Configuration 
    > Backup Type: Configuration Only  
    > Click on Next 
 
4. Review 
    > Review the information, then click on Backup to launch the backup process 
 
Check that the 3 lines “SUCCESS” appear in the Result screen. Click on OK. 
 
 
Tips > Summary View 
The CONFIGURATION > RESOURCE MANAGER > Backup/Restore > Summary View displays the list of the backups 
that have been performed on each device, and their result.  
 
 
Notes > Backup Method 
3 Backup Methods are available:  
- 
Backup by Devices: select specific AOS Devices from a list of discovered devices. 
- 
Backup by Maps: select a map(s) to backup all devices in the map(s). Note that if a map contains AOS 
Devices and Stellar APs, the Stellar APs will not be backed up. Stellar APs can only be backed up by 
AP Group. 
- 
Backup by AP Group: backup Stellar AP Series Devices. 
 
 
Notes > Backup Types 
3 Backup Types are available:  
- 
Full Back up: backs up both configuration files and image files. 
- 
Configuration Only: backs up all configuration-related files in all directories (including user 
credentials, banner, time zone, etc.). 
- 
Images Only: backs up image files only. Image files will not be FTPed from a device. OmniVista will 
only record file version(s). 
 
 
 
Tips > Schedule Setting 
During the Backup configuration (AOS or Stellar Devices), it is possible to enable the Schedule Setting option. 
This option allows you to schedule a single or recurring backup. Several options are available:  
- 
Start At to select the time when you want to begin the scheduled backup 
- 
Recurrence Pattern (daily, weekly, monthly…) 
- 
Range of Recurrence (start date of the recurring backup, end date of the recurring backup) 
3.1.2. 
Backing Up Stellar APs Devices 
 
> Select CONFIGURATION > RESOURCE MANAGER > Backup/Restore 
  > Click on the BACKUP button  
 
1. Backup Method 
    > Select Backup By AP Groups 
    > Click on Next 
 
2. AP Group Selection 
    > Click on ADD 
      > Select the APGX (X = R-Lab Number), then click on Add >  
      > Click on OK 
    
3. Configuration 
    > Backup Type: Configuration Only  
    > Click on Next 
 
4. Review 
    > Review the information, then click on Backup to launch the backup process 
 
Check that the 2 lines “SUCCESS” appear in the Result screen. Click on OK.

<<<PAGE 428>>>
5 
Backup, Restore & Upgrade 
 
 4 
Restoring the Devices Configuration 
To test the Restore operation feature, we will first modify the configuration of one OmniSwitch (ex. 6870), 
then we will restore the backup created in the previous part.  
 
 
- Modify the configuration of the OmniSwitch 6870 (create VLAN 70-80) 
- Restore the backup created in the previous part 
4.1. 
Restoring an AOS Device Configuration 
4.1.1. 
Briefing 
In this part, we are going to:  
- Create VLANs 70 to 80 on the OmniSwitch OS6870 
- Restore the backup 
- Check that the VLANs 70 to 80 have been removed 
 
 
4.1.2. 
Modifying the OmniSwitches Configuration 
 
> Select CONFIGURATION > VLANS > VLAN 
  > Click on Create VLAN by Devices button 
 
1. Devices Selection 
  > VLAN IDs: 70-80  
  > VLAN(s) Description: TEMP-VLANS 
    > Click on the Add/Remove Devices 
      > Select the Add the OS6870  
      > Click on OK  
    > Click on Next 
 
2. VLAN Configuration 
  > Check that Admin Status = Enabled 
  > Click on Next  
 
4. Q-Tagged Port Assignment 
  > Click on Next (skip this part) 
 
5. Review 
  > Review the information 
  > Click on Create 
 
 
Tips 
You can check that the VLANs have been created by connecting on the OS6870 CLI console, or via the CLI 
Scripting.

<<<PAGE 429>>>
6 
Backup, Restore & Upgrade 
 
4.1.3. 
Restoring the OmniSwitch 6870 Configuration 
Now that we have created VLANs, let’s restore the previous backup. After this step, the VLANs 70 to 80 
should be removed:   
 
> Select CONFIGURATION > RESOURCE MANAGER > Backup/Restore 
  > Select the OS6870 in the list 
  > Click on the RESTORE button  
 
1. File Selection 
    > Click on OmniSwitch 6870  
    > Select only the 2 vcboot.cfg files  
    > Click on Restore 
 
Check that the restore is successful in the Result page, then click OK 
4.1.4. 
Checking the Result 
Now, the backup has been restored in the WORKING and CERTIFIED status, let’s check that the temporary 
VLANs have been deleted:  
 
> Select CONFIGURATION > VLANS > VLAN 
  > Click on ADD > Switch Picker 
    > Select the OS6870, then click on Add >  
    > Click on OK 
 
And the VLANs 70 to 80 are … still here!  
 
 
Why are the VLANs 70-80 still displayed?  
 
As you may have guessed, the configuration files are transferred in the WORKING and CERTIFIED folders 
but are NOT applied on the RUNNING configuration (could cause major problems in real cases scenarios if 
it was the case).  
To force the configuration restored in the WORKING directory to be used by the OmniSwitch, launch the 
following command (via the console, or the OV 2500 CLI SCRIPTING application):  
 
CLI SCRIPTING application or CONSOLE 
> reload from working no rollback-timeout 
Confirm Activate (Y/N): y 
 
Wait for the OmniSwitch to reboot (~3 min), then use the VLAN Manager application to check that the 
VLANs 70-80 have been correctly removed:  
 
> Select CONFIGURATION > VLANS > VLAN 
  > Click on ADD > Switch Picker 
    > Select the OS6870, then click on Add >  
    > Click on OK 
 
And the VLANs 70 to 80 are … deleted! 
 
 
 
Notes > VLANs are still here? 
To force the VLAN Manager to update, you can click on the Poll option on the left menu. It will force the 
OmniVista 2500 to poll the selected device(s) and retrieve the updated information.  
4.2. 
Restoring a Stellar Device Configuration 
It is not possible to perform a restore on a Stellar AP, as most of the configuration is pushed when the 
Access Points is inserted in an AP Group. However, backup files of Stellar APs can be used to 
analyze/troubleshoot problems with APs. See the Troubleshooting lab for more information.

<<<PAGE 430>>>
7 
Backup, Restore & Upgrade 
 
 5 
Debriefing 
During this lab, we have learned how to backup the configuration of each device (AOS or Stellar) available in 
the network. We have also learned that it is possible to schedule the backup operation, and that the restore 
operation can be done only on AOS Devices (not on Stellar APs).

<<<PAGE 431>>>
8 
Backup, Restore & Upgrade 
 
-ANNEXES- 
 6 
Annex: Upgrading an Image (Resource Manager) 
From the Resource Manager, it is also possible to upgrade an OmniSwitch or an Access Point. 
 
DO NOT upgrade the OmniSwitches. This is only a procedure.  
6.1. 
Importing the Upgrade Files 
All upgrade files supplied by Alcatel-Lucent Enterprise Customer Service are packaged as WinZip 
executables and have a *.zip file extension. Do not attempt to unzip the firmware files manually. When 
you Import the WinZip executable, OmniVista automatically unzips the executable as part of the import 
process. 
 
> Go to RESOURCE MANAGER > Upgrade Image 
  > Click on Import 
    > Click on Browse and select the desired firmware file 
    > Once the upload finish, click on OK  
 
The list of uploaded firmware is displayed in the Upgrade Image main page:  
 
 
6.2. 
Installing the Upgrade Files  
 
> Go to RESOURCE MANAGER > Upgrade Image 
  > Select the firmware to install with the Import button 
  > Click on install 
 
 
 
1. 
Firmware File Selection 
    > Check that the Access Points models that you have are available in the list 
    > Click on Next 
 
2. 
Devices Selection  
> In case of AP upgrade 
    > To install a firmware only on specific AP(s): Click on ADD > Use Switch Picker 
    > To install a firmware on all the APs of an AP Group: Click on ADD 
> In case of OmniSwitch upgrade 
    > Select one or several OmniSwitch(es) 
 
3. 
Software Installation 
    > Review the information, then click on Install Software

<<<PAGE 432>>>
9 
Backup, Restore & Upgrade 
 
 7 
Annex: Upgrading an Image (Access Point Web Page) 
The upgrade of an Access Point can also be done via its webpage.  
7.1. 
Enabling the Web Management 
The Web Management must be enabled in order to be able to access the Access Point webpage: 
 
> Go to NETWORK > AP REGISTRATION > AP Group 
  > Select the AP Group APGX (X=R-Lab Number) 
    > AP Web: ON 
    > Password: Alcatel.0   
7.2. 
Accessing to the Web Management Interface 
Check what is the IP address of the Access Point:  
 
> Go to NETWORK > AP REGISTRATION > Access Points 
  > Note the IP address of the desired AP 
 
 
 
> Open a web browser 
  > URL: https://<IP address of the AP> 
    > Username: Administrator 
    > Password: Alcatel.0 
    > Click on Login 
7.3. 
Upgrading the Firmware 
Finally, upload the firmware to be installed: 
 
> Go to System  
  > Select Image File (or Image File URL if the Image File/Firmware is located on a web server) 
  > Click on Browse, then select the firmware/image file

<<<PAGE 433>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Monitoring the Network Infrastructure 
Objective 
✓ Monitor the Network Devices from the OmniVista 2500 
Contents 
1 
Briefing ......................................................................................... 1 
2 
Checking the Topology & Devices Status .................................................. 2 
2.1. Saving the Configuration .......................................................................... 3 
2.2. Monitoring the Devices & Links Status ........................................................... 4 
2.2.1. Device Information ......................................................................................... 4 
2.2.2. Device Status ................................................................................................ 4 
2.2.3. Notification Status ......................................................................................... 5 
2.2.4. Links Status .................................................................................................. 6 
3 
Being Notified in case of Critical Event .................................................... 7 
3.1. Using the Notification Application ............................................................... 7 
3.1.1. Using the Filters ............................................................................................ 7 
3.1. Using the Trap Responder ......................................................................... 8 
3.1.1. Setting Up the Trap Responder ........................................................................... 8 
3.1.2. Declaring the Mail Server .................................................................................. 8 
3.1.3. Testing the Mail Server Configuration ................................................................... 8 
3.1.4. Testing the Notification ................................................................................... 9 
4 
Debriefing .................................................................................... 10

<<<PAGE 434>>>
1 
Monitoring the Network Infrastructure 
 
 1 
Briefing 
Let’s see how to monitor all the network devices from one platform, the OmniVista 2500. 2 applications will 
be used:  
- The Topology Application which provides a view of all discovered devices in the network; 
- The Notification Application which displays the notification generated by the network devices. 
 
 
 
 
CURRENT 
TOPOLOGY 
END OF LAB 
TOPOLOGY

<<<PAGE 435>>>
2 
Monitoring the Network Infrastructure 
 
 2 
Checking the Topology & Devices Status 
The Topology application enables you to view the topology of all discovered devices in the network, view 
information about a specific device and perform certain actions on those devices (e.g., edit a device, telnet 
to a device, reboot a device). 
 
> Select NETWORK > TOPOLOGY 
  > Click on Create Site (top right corner) 
    > Site Name: <your company name> (ex. ALE) 
    > Location: <your company address> (ex. Rue Antoine de St Exupéry, 29490 Guipavas, France) 
    > Devices: click on >> to add all the devices (5) 
    > Click on Create  
 
A pointer indicates the location entered with the number of devices:  
 
 
 
> Click on Go To Topology 
 
The network topology containing all the previously discovered devices is displayed:

<<<PAGE 436>>>
3 
Monitoring the Network Infrastructure 
 
2.1. 
Saving the Configuration 
 
 
Save all the management done during this training as Running configuration 
 
To save the management of all the devices at once: 
 
> Click on the Select All button   
  > Select Action > Device  
    > Click on Save to Running 
 
  > A new tab is automatically opened  
    > Check that the task is completed successfully, then click on Finish 
 
 
Notes 
It is also possible to save the management of each device (one by one):  
 
OMNISWITCH 
> Click on the OmniSwitch 
  > Click on Actions > Device  
    > Click on Copy Working/Running to Certified 
    > Check that the save process has been completed successfully 
    > Click on Finish 
 
STELLAR ACCESS POINT 
> Click on the Stellar AP 
  > Click on Actions > Device  
    > Click on Save to Running 
    > Check that the save process has been completed successfully 
    > Click on Finish 
 
 
Notes 
If the links between the OmniSwitches and the Stellar Access Points don’t appear in the 
diagram, manually poll the links:  
 
> Select both Stellar Access Points by clicking on Multiple Selection  
  > Select Action > Device  
    > Select Poll Link 
 
  > A new tab is automatically opened  
    > Check that the task is completed successfully, then click on Finish 
 
Result: the links should now appear:

<<<PAGE 437>>>
4 
Monitoring the Network Infrastructure 
 
2.2. 
Monitoring the Devices & Links Status 
From the Topology application, it is also possible to check the Devices & Links Status.  
2.2.1. 
Device Information 
 
 
Display the MAC Address, version and device model of the OmniSwitch 6360. 
 
To display detailed device information, click on the device. A Detail panel appears on the right. A list of 
information is displayed. The information displayed may vary depending on the device: 
 
 
 
2.2.2. 
Device Status 
 
 
- Discover why the OmniSwitch are in Warning state, and solve the problem; 
- Display the OmniSwitches & Access Points notifications 
- Check that the links are ups, and that the correct ports are used; 
 
Device status is displayed by the device status circle around the device: 
• 
Green = Up (Device is up) 
• 
Orange = Warning (indicates that traps have been received on the device. The highest level of 
trap received by the device is displayed (Green, Orange, Red) in the Notifications Status). 
• 
Red = Down (Device is down) 
 
 
 
Notice that your OmniSwitches are in the Orange “Warning” state, meaning that a notification has been 
generated on these devices. The Notification Status part (next part) shows how to acknowledge the(se) 
notification(s).

<<<PAGE 438>>>
5 
Monitoring the Network Infrastructure 
 
2.2.3. 
Notification Status 
Notifications status displayed in the small circle in the upper right corner of the device, indicating the 
highest level of trap received by the device: 
• 
No Circle = Alarm status is Normal. 
• 
Orange = Alarm status is Warning. 
• 
Purple = Alarm status is Minor. 
• 
Yellow = Alarm status is Major. 
• 
Red = Alarm status is Critical. 
 
 
 
To clear/acknowledge the notification and pass the Device & Notification status to Green status:  
 
OMNISWITCH 
> Click on the OmniSwitch (ex: 6360) 
  > Click on Actions > Notifications > View Traps 
    > Select the first checkbox to select all the lines  
    > Click on ACK (blue button) to acknowledge the notifications or CLEAR (red button) to delete the 
notifications from the database 
You may have to repeat the operation to acknowledge/clear all the notifications. A maximum of 1000 
notifications can be acknowledged/cleared at the same time.  
 
The OmniSwitch 6360 should now be displayed in Green: 
 
 
 
 
 
In order to clear all the notifications, you could use the following procedure: 
 OMNISWITCH 
> Click on the OmniSwitch 
  > Click on Actions > Notifications > View Traps 
    > On the top right corner, click the button Actions  
    > Click Ack All to acknowledge the notifications and click OK to validate. 
You can then click Clear All to delete all the notifications from the database

<<<PAGE 439>>>
6 
Monitoring the Network Infrastructure 
 
2.2.4. 
Links Status 
Links between devices are displayed as a single line, whether there is a single link or multiple links. 
- Green - Link is up. If there are multiple links, Green indicates all the links are up. 
- Orange - There are multiple links and at least one of the links is down. 
- Red - Link is down. If there are multiple links, Red indicates all the links are down. 
- Blue - Link status is unknown. 
 
 
 
To display link information, move the mouse over the link until the pointer turns into a finger. Link 
information will be displayed in table form as shown below:  
 
 
 
 
You can also click on a link to display link information:  
 
 
 
 
Tips 
Several shortcuts to the other OmniVista 2500  
applications are available when a device (OmniSwitch,  
Access Point) is selected or by right clicking on a device.  
We will discover these applications and learn  
how to use them in the next labs.

<<<PAGE 440>>>
7 
Monitoring the Network Infrastructure 
 
 3 
Being Notified in case of Critical Event 
During the last part, we saw that notifications are sent from the devices to the OmniVista 2500. These 
notifications are displayed in the Topology application. In this part, we are going to learn how to perform an 
action (send a mail, execute a script…) when a notification is received.   
3.1. 
Using the Notification Application 
Open the Notification Home menu:  
 
> Go to NETWORK > NOTIFICATIONS > Notifications Home 
 
The Notifications Home Screen displays all traps received from network devices and provides basic trap 
information (e.g., severity level, date/time received). You can also use this screen to acknowledge, 
renounce, and clear traps, as well as poll devices for traps. 
3.1.1. 
Using the Filters 
 
 
Filter the traps to display only traps: 
- Coming from the AP Group AGPX (X=Remote-Lab Number); 
- With a severity = Critical  
 
> Go to NETWORK > NOTIFICATIONS > Notifications Home 
  > Click on the Filters area (top) 
    > Filter By: AP Group 
    > Select APGX   
    > Select Severity: Critical 
    > Click on Apply to apply the filter  
 
In the result, the reboot operations done during this training should be displayed.

<<<PAGE 441>>>
8 
Monitoring the Network Infrastructure 
 
3.1. 
Using the Trap Responder 
3.1.1. 
Setting Up the Trap Responder 
A Trap Responder enables you to specify a response (send a mail, execute a program, forward trap) that 
you want OmniVista to take when specified traps are received by OmniVista. In this Lab, we will learn how 
to automatically send a mail when a critical alarm is generated by a network device.  
 
 
- Configure the OmniVista 2500 to send an e-mail if a critical alarm is generated by an 
AP  
- Test your management 
 
> Go to NETWORK > NOTIFICATIONS > Trap Responder 
  > Click on  
     
1. Agent 
    > Agent Type: AP Group 
    > AP Group Selection: APGX (X=Remote-Lab Number) 
    > Click on Next 
 
2. Trap Type 
    > Traps which match these severities: Critical 
    > Click on Next 
 
3. Response 
    > Action: Send an e-mail 
    > E-mail To: adminX@company.com (X = R-Lab Number) 
> Click on Next 
 
> Click on Next to review the information, then click on Create 
 
 
Notes > Trap Variables 
Trap variables can be used to customize the E-mail Subject and E-mail Body fields.  
 
For example, you can use the following fields and variables:  
- E-mail Subject: Warning! Critical Trap Received on $TrapAgent$ ($TrapAgentName$)! 
 
The $TrapAgent$ displays the IP address of the device.  
The $TrapAgentName$ displays the name of the device. 
3.1.2. 
Declaring the Mail Server 
The next step consists in declaring the mail server in the OmniVista 2500: 
 
> Go to ADMINISTRATION > PREFERENCES > System Settings 
  > Click on Email (left menu) 
    > SMTP Server: 10.130.5.6 
    > ‘From’ Address: ov2500@company.com 
    > SMTP Authentication: OFF 
    > ‘To’ Address to Test: adminX@company.com 
    > Click on Apply 
3.1.3. 
Testing the Mail Server Configuration 
Now, let’s test the configuration. Let’s begin by testing the mail server configuration:  
 
> Open a Web Browser (or a new tab/page)  
  > URL: mail.company.com 
    > Name: adminX@company.com 
    > Password: password   
 
The “test” mail sent by the OmniVista 2500 should be in the Inbox:

<<<PAGE 442>>>
9 
Monitoring the Network Infrastructure 
 
3.1.4. 
Testing the Notification 
First, let’s force the generation of a Critical notification by restarting one of the AP: 
 
> Go to NETWORK > TOPOLOGY 
  > Select an AP 
    > In the Action panel (on the right), click on Device > Reboot… 
      > Are you sure? Yes 
 
 
Notes > Trap Responder on OmniSwitches 
The same steps can be followed in order to be notified by mail if an OmniSwitch generates a critical 
notification (except 4.2.1: Agent Type: Device instead of AP).  
 
Check that a notification has been generated by the AP and sent to the OmniVista 2500:  
 
    > In the Action panel (on the right), click on Actions > Notification > View Traps 
 
 
 
Now, check that a mail has been send to adminX@company.com (wait a few minutes if needed, as the 
mail server doesn’t send mails in real time):

<<<PAGE 443>>>
10 
Monitoring the Network Infrastructure 
 
 4 
Debriefing 
In this lab, we saw that the OmniVista 2500 provides powerful application to monitor the network devices 
(OmniSwitches/Access Points).

<<<PAGE 444>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Configuring Heat Map & Floor Plan 
Objective 
✓ Learn how to create and configure a Heat Map and a Floor Plan 
Contents 
1 
Configuring a Heat Map ...................................................................... 1 
1.1. Creating the Building Hierarchy .................................................................. 1 
1.2. Configuring the Plan Map .......................................................................... 2 
1.2.1. Scaling the Plan ............................................................................................. 2 
1.2.2. Laying Down the Obstacles ................................................................................ 2 
1.2.3. Placing the Access Points .................................................................................. 3 
1.2.4. Displaying the Result ....................................................................................... 3 
2 
Configuring a Floor Plan ...................................................................... 4 
2.1. Creating the Floor Plan ............................................................................ 4 
2.2. Configuring the Plan Map .......................................................................... 4 
2.2.1. Scaling the Plan ............................................................................................. 4 
2.2.2. Laying Down the Obstacles ................................................................................ 5 
2.2.3. Launching the Auto Deployment ......................................................................... 5 
2.2.4. Displaying the Result ....................................................................................... 6

<<<PAGE 445>>>
1 
Configuring Heat Map & Floor Plan 
 
 1 
Configuring a Heat Map 
The Heat map function is to display the current work of the AP signal intensity distribution, through different 
colors showing the signal coverage.  
The Heat Map feature permits the administrator to create Campus, Building and floor map, to set up 
obstacles in the Map and put APs into the Floor to observe the wireless signal coverage. 
In this lab, the Stellar APs will be placed on a custom map. 
 
Create a Heat Map with the given office plan document. 
1.1. 
Creating the Building Hierarchy 
The Heat Map always respect the following structure: 
Campus 
  > Building 
     > Floor Map 
Let’s create each level:  
 
> Select WLAN > HEAT MAP 
  
Campus 
 > Click on the + button 
    > Campus Name: My_Campus 
> Double click on the My_Campus that is now displayed  
 
Building 
> Click on the + button 
    > Building Name: My_Building 
> Double click on the My_Building that is now displayed  
 
Floor 
> Click on the + button 
    > Floor Name: First_Floor 
    > Floor Number: 1 
    > File Name: click on Select File > Select the Office-Plan.jpg file in the C:\Resources folder 
    > Click on OK 
> Double click on the First_Floor that is now displayed to access the Floor map

<<<PAGE 446>>>
2 
Configuring Heat Map & Floor Plan 
 
1.2. 
Configuring the Plan Map 
From this point, 3 main actions are required to visualize the wireless signal:  
- Scaling the plan;  
- Laying down obstacle;  
- Placing the APs. 
1.2.1. 
Scaling the Plan 
From the Floor Map Editor 
 > Click on Operation > Edit Floor Map  
   > Click on Scale the Map 
     > Trace a line on the map  
     > Enter a distance for this segment. In the example below, the red line is 5 meters long. 
 
 
 
1.2.2. 
Laying Down the Obstacles 
The next step is to lay down the obstacles on the map.  
 
From the Floor Map Editor 
 > Click on Operation > Edit Floor Map  
   > Click on Draw:WallsHeavy 
     > Start drawing the obstacles on the map to obtain the result below: 
 
 
 
 
Tips 
Pre-defined obstacles can be selected by clicking on the       button and each one with a different absorption 
coefficient (dB). 
It is also possible to create custom obstacles via the Operation > Obstacle Manage link.

<<<PAGE 447>>>
3 
Configuring Heat Map & Floor Plan 
 
1.2.3. 
Placing the Access Points 
The last step is to lay the Stellar APs to the Floor.  
 
From the Floor Map Editor 
 > Click on Operation > Adding AP To The Floor  
   > Select both Aps 
   > Click on OK 
     > Place the APs on the Map 
 > In Edit Floor Map, click on Stop to exit from the Edit Floor Map menu 
 
> Do you want to save the modified heat map? Yes 
1.2.4. 
Displaying the Result 
Once the Layout has been saved, the Heat Map Application will display the signal power on the map based 
on the actual signal power transmitted by the APs. 
 
Observe the Heat Map as well as the absorption of the walls. 
 
 
 
 
 
Notes 
Go back to Edit Floor Map and place the APs in different places to cover the cold areas. 
Changing the APs on the map will simulate the new Wi-Fi coverage based on the real band and power of 
emission of the APs.  
 
 
Go back to the Survey Toggle section 
Select the Frequency 2.4 Ghz only, then 5GHz only. Notice the difference between the 
2. Read the explanation below. It will be mentioned again in another lab (RF Profile). 
 
 
Important > Difference Between 2.4 GHz and 5 GHz 
- 
The 2.4 GHz band is quite crowded, because it is used by more than just Wi-Fi (old cordless doors, baby 
monitors…). The longer waves used by the 2.4 GHz band are better suited to longer ranges and transmission 
through walls and solid objects. 
- 
The 5 GHz band is much less congested, which means you will likely get more stable connections, and 
higher speeds. On the other hand, the shorter waves used by the 5 GHz band makes it less able to 
penetrate walls and solid objects.

<<<PAGE 448>>>
4 
Configuring Heat Map & Floor Plan 
 
 2 
Configuring a Floor Plan 
The main functions of the Floor Plan are to import the floor map and mark the relevant obstacle. Then, 
calculate the placement of the AP by a relevant algorithm, and automatically generate the functions of the 
AP plan. 
With Floor Plan, the admin can import a map into a floor plan, scale it and perform the AP auto Deployment. 
2.1. 
Creating the Floor Plan 
> Select WLAN > FLOOR PLAN 
  
> Click on the + button 
    > Floor Plan Name: My Floor Plan 
    > File Name: click on Select File > Select the Office-Plan.jpg file in the C:\Resources folder 
    > Click on Create 
2.2. 
Configuring the Plan Map 
From this point, 3 main actions are required to visualize the wireless signal:  
- Scaling the plan;  
- Laying down obstacle;  
- Placing the APs. 
2.2.1. 
Scaling the Plan 
From the Floor Map Editor 
 > Click on Operation > Edit Floor Plan  
   > Click on Scale the Map 
     > Trace a line on the map  
     > Enter a distance for this segment. In the example below, the red line is 5 meters long.

<<<PAGE 449>>>
5 
Configuring Heat Map & Floor Plan 
 
2.2.2. 
Laying Down the Obstacles 
The next step is to lay down the obstacles on the map.  
 
From the Floor Map Editor 
 > Click on Operation > Edit Floor Plan 
   > Click on Draw:WallsHeavy 
     > Start drawing the obstacles on the map to obtain the result below: 
 
 
 
 
Tips 
Pre-defined obstacles can be selected by clicking on the       button and each one with a different absorption 
coefficient (dB). 
It is also possible to create custom obstacles via the Operation > Obstacle Manage link. 
2.2.3. 
Launching the Auto Deployment 
Now, let’s auto deploy the Access Points on the map:  
 
From the Floor Map Editor 
 > Click on Operation > Auto Deployment  
   > Quality: Excellent 
   > AP Model: OAW-AP1231 
   > TX Power: 14 
   > Click on OK

<<<PAGE 450>>>
6 
Configuring Heat Map & Floor Plan 
 
2.2.4. 
Displaying the Result 
Once the Auto Deployment done, the Access Points are automatically placed on different location to 
provide the optimal coverage:  
 
 
 
 
 
Tips 
The result will vary based on the following parameters: 
- 
Scale of the map 
- 
Number and type of obstacles placed 
- 
AP Model 
- 
Quality (General, Good, Excellent) 
 
Change some of these parameters (AP Model, Quality…) and click on Save the Layout. 
 
 
Notes  
In Edit Floor Plan, APs can be added manually on the map to fill the cold areas. After clicking on “Save The 
Layout”, the Floor Plan application will process and display the Wi-Fi coverage based on all the APs located on 
the map.

<<<PAGE 451>>>
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. 
 
OmniAccess Stellar WLAN 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
Objective 
✓ Learn how to setup the different equipment in order to deploy an 
OmniAccess Stellar Access Point as Remote Access Point (RAP) 
Contents 
1 
Topology ........................................................................................ 2 
2 
Configuring the OmniVista Cirrus 4 ......................................................... 2 
2.1. Logging into the OmniVista Cirrus 4 ............................................................. 3 
2.2. Declaring the OmniAccess Stellar AP as Remote AP Point .................................... 3 
2.2.1. Retrieving the Stellar AP Serial Number & MAC Address .............................................. 3 
2.2.2. Declaring the Stellar AP in the OmniVista Cirrus 4 .................................................... 4 
2.3. Configuring the VPN Settings ..................................................................... 5 
3 
Connecting the OmniAccess Stellar Access Point ......................................... 6 
4 
Importing the VPN Configuration ........................................................... 6 
5 
Configuring the VPN Server Virtual Appliance ............................................ 7 
5.1. Configuring the VPN Server Virtual Appliance Basic Settings ................................ 8 
5.2. Configuring the VPN Server Virtual Appliance Settings ....................................... 8 
5.2.1. Configuring the Network Interfaces...................................................................... 9 
6 
Checking the VPN Status ................................................................... 14

<<<PAGE 452>>>
1 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
7 
Configuring the OmniVista 2500 NMS ..................................................... 15 
7.1. Adding a Default Route in the OmniVista 2500 NMS .......................................... 16 
7.2. Discovering the Remote Access Point in the OmniVista 2500 NMS.......................... 17 
7.3. Filling the VPN Tunnel (client’s traffic) Settings ............................................. 18 
7.4. Exporting the VPN Tunnel (client’s traffic) settings .......................................... 19 
7.5. Assigning the VPN Tunnel (client’s traffic) to the Remote AP .............................. 19 
7.6. Creating an Employee SSID ....................................................................... 20 
7.7. On the Remote site................................................................................ 21 
8 
Configuring the VPN Server Virtual Appliance .......................................... 21 
9 
On the Remote Site ......................................................................... 25 
10 
[Add-On] Creating an OmniVista Cirrus 4 Account ..................................... 27 
10.1. Logging into the OmniVista Cirrus 4 ............................................................ 27 
10.2. Verify Your Account ............................................................................... 28 
11 
[Add-On] Deploying the ALE VPN Server on VMware ESXi ............................. 29 
11.1. Deploying the Virtual Appliance ................................................................. 29

<<<PAGE 453>>>
2 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
 1 
Topology 
During this lab, we will use the following topology:  
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 2 
Configuring the OmniVista Cirrus 4 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
The OmniAccess Stellar Access Point to be deployed as Remote Access Point (RAP) must be first declared in 
the OmniVista Cirrus 4.  
CLOUD 
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
OMNIVISTA  
CIRRUS 4 
FREEMIUM 
CLOUD 
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
OMNIVISTA  
CIRRUS 4 
FREEMIUM 
VPN Server 
- Public IP@: x.x.x.x (hidden) 
- Private IP@: 10.130.5.251 
- VPN Server IP@ (vpn_mgmt): 192.168.0.1 
- VPN Client IP@ (vpn_mgmt): 192.168.0.2-20 
- VPN Server IP@ (vpn_data): 10.7.0.61 
- VPN Client IP@ (vpn_data): 10.7.0.55-60 
10.130.5.50 
192.168.1.76 
192.168.1.1

<<<PAGE 454>>>
3 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
The OmniVista Cirrus 4 is a cloud-based network management system. To log into this application, an account 
is necessary. 2 types of accounts are available:  
- Freemium: free account that provides limited features for an unlimited number of registered devices. 
- Paid: full OmniVista Cirrus 4 functionalities for the subscribed number of devices and services for the 
length of your contract.  
 
In this lab, we will use a Freemium account. To learn how to create a freemium account, please refer to the 
dedicated part available in the add-on section of this lab.  
2.1. 
Logging into the OmniVista Cirrus 4 
 
Web Browser 
Access to the OmniVista Cirrus 
4 webpage 
https://registration.ovcirrus.com/ 
Enter your credentials 
(Freemium account) 
 
 
2.2. 
Declaring the OmniAccess Stellar AP as Remote AP Point 
2.2.1. 
Retrieving the Stellar AP Serial Number & MAC Address 
First, retrieve the Stellar AP serial number and MAC address information. You will need it in the next part. 
This information can be found on the label at the rear of your Stellar Access Point:

<<<PAGE 455>>>
4 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
2.2.2. 
Declaring the Stellar AP in the OmniVista Cirrus 4 
 
Go to Network > Inventory > 
Device Catalog 
 
Click on 
 (upper right 
corner of the screen) 
 
Enter the AP Serial Number 
 
Select Device Filters = AP 
 
See the Tips below to learn 
where to find the AP Serial 
Number 
Desired Software Version 
From this field, you can select a software version for the AP to be upgraded.  
Enter the AP MAC Address  
 
Select Is this a Remote AP ? 
YES

<<<PAGE 456>>>
5 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
2.3. 
Configuring the VPN Settings 
VPN settings and the OmniVista 2500 NMS IP address must be configured on the OmniVista Cirrus 4. The 
OmniVista Cirrus 4 will then send these information to the Remote Access Point for it to be able to reach 
the OmniVista 2500 NMS through a VPN tunnel.  
 
 
 
 
 
 
 
 
 
 
 
 
 
Enter the VPN Settings 
 
Then, click on Save VPN 
Setting & Create Device  
 
VPN Settings Name  
User-configured name for the VPN configuration. 
Server's Public IP 
The VPN Server's Public IP address (configured when you installed the VPN VM). This is the IP 
address used by Remote APs to connect to the VPN Server. And this is the interface through 
which traffic originating from inside the Enterprise Network flows to the Remote site. 
Port 
The VPN Server Port. 
Server's VPN IP 
The VPN Server's Private IP address (configured when you installed the VPN VM). This is the 
interface through which traffic originating from the Remote AP flows to reach a destination 
inside the Enterprise Network. 
OmniVista Enterprise Server 
IP 
The IP address of the OmniVista 2500 NMS that will manage the devices. 
Client VPN IP Address Pool 
The range of addresses available to assign to Remote APs. You can select IP range and insert 
a range of IP addresses, or a shorthand mask.  
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
PUBLIC IP@: 6550 
10.130.5.50 
VPN SETTINGS :  
- CLIENT IP@ RANGE: 192.168.0.2 TO .20 
- SERVER IP@: 192.168.0.1 
VPN > MGMT TRAFFIC

<<<PAGE 457>>>
6 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
 3 
Connecting the OmniAccess Stellar Access Point 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
Connect the OmniAccess Stellar Access Point that must act as Remote Access Point to Internet. After a few 
moments, the OmniAccess Stellar Access Point is seen as registered on the OmniVista Cirrus 4:  
 
Check the AP’s Device status  
 
 4 
Importing the VPN Configuration 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
Now that the Remote Access Point has been registered in the OmniVista Cirrus 4, let’s export the VPN 
settings. In the next part (5 -  
Configuring the VPN Server Virtual Appliance), we will import these VPN 
settings in order to configure the VPN server.  
MAIN SITE 
CLOUD 
REMOTE SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
OMNIVISTA  
CIRRUS 4 
FREEMIUM 
CLOUD 
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
OMNIVISTA  
CIRRUS 4 
FREEMIUM 
192.168.1.79 
192.168.1.1 
VPN SETTINGS 
(.CONF FILE)

<<<PAGE 458>>>
7 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
OmniVista Cirrus 4 Web Administration Interface 
Click on Export VPN Settings 
 
Select the line corresponding 
to the VPN Server configured 
previously (ex. VPN_Server)  
 
Click on Export 
 
A new window appears, asking 
you to download a <VPN 
Server name>.conf file 
 
Download the file 
 
 
 
Warning 
KEEP THE CONF FILE PRECIOUSLY, AS WE WILL NEED TO IMPORT IT IN THE VPN SERVER VIRTUAL APPLIANCE AT 
THE END OF THE NEXT PART.  
 5 
Configuring the VPN Server Virtual Appliance 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Tips 
To learn how to deploy the ALE “VPN Server” virtual appliance, please refer to the dedicated add-on part 
available at the end of this lab.  
CLOUD 
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
OMNIVISTA  
CIRRUS 4 
FREEMIUM 
PUBLIC IP@ 
10.130.5.251

<<<PAGE 459>>>
8 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
5.1. 
Configuring the VPN Server Virtual Appliance Basic Settings 
 
Web Browser 
Click on  
 to start the VM 
 
Click on the 
 icon to open 
a console window 
 
Select the language (ex. 
English) 
 
Enter y to confirm 
 
If necessary, configure a new 
keyboard layout 
 
Accept the end-user license 
agreement 
 
Enter, then confirm, the 
password for the admin 
account (ex. Alcatel.0) 
 
 
The virtual machine reboots to take the basic settings into account. 
5.2. 
Configuring the VPN Server Virtual Appliance Settings 
 
VPN Server Console 
Log into the VPN Server VA 
- login: admin 
- password: <password set at 
previous step> 
 
The Main Menu is displayed

<<<PAGE 460>>>
9 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
5.2.1. 
Configuring the Network Interfaces 
- Configure the Network Interface 1 (Public IP@): 
 
VPN Server Console 
Select Network Interfaces in 
the menu then press Enter 
 
- Enter 1 to configure the 
NIC1 (eth0) 
- Select OK and press Enter 
 
Enter the VPN Public IP@ and 
its prefix length 
 
Select Save, then press Enter 
 
Press Enter to confirm 
 
 
- Configure the Network Interface 2 (Private IP@): 
 
VPN Server Console 
Select Network Interfaces in 
the menu then press Enter 
 
- Enter 2 to configure the 
NIC2 
- Select OK and press Enter 
 
Enter the VPN Private IP@ 
and its prefix length 
 
Select Save, then press Enter 
 
Press Enter to confirm 
 
 
- Configure the gateway:  
 
VPN Server Console 
Go to Network Settings… > 
Configure a network setting… 
 
Press Enter 
 
 
Select Configure Default 
Gateway 
 
Press Enter

<<<PAGE 461>>>
10 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Enter the Gateway IP@  
 
Select Save, then press Enter 
 
Press Enter to confirm 
 
 
- Configure the DNS server(s): 
 
VPN Server Console 
Select Configure Default 
Gateway 
 
Press Enter 
 
 
Enter the DNS IP@  
 
Select Save, then press Enter 
 
Press Enter to confirm 
 
 
- Enable the SSH feature: 
 
VPN Server Console 
From the main menu 
 
Select Network Services… > 
Configure a network service 
 
Press Enter 
 
 
Select ssh  
 
Press Enter

<<<PAGE 462>>>
11 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Select the option 
corresponding to your 
private IP@ (ex. 2)  
 
Enter the port number (ex. 
6550) 
 
Select Save, then press Enter 
 
Confirm, then press Enter 
 
Press Enter to confirm 
 
 
- Apply the configuration changes:  
 
VPN Server Console 
From the main menu 
 
Select Apply Configuration 
Changes 
 
 
Select OK, then press Enter 
 
 
- Now that the SSH/SFTP is enabled, upload the VPN server configuration (.conf file) to the VPN server 
VM:  
 
Windows 
Open FileZilla Client  
 
Connect to the VPN Server by 
entering the following 
information: 
- Host: VPN Server Private IP 
@ (ex. 10.130.5.251) 
- Username: admin 
- Password: VPN Server 
password (ex. Alcatel.0) 
- Port : 22 
 
Click Quickconnect

<<<PAGE 463>>>
12 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Transfer the <VPN Server 
name>.conf file in the folder 
 
/opt/OmniVista_2500_NMS/d
ata/vpn_conf/vpn_profile 
 
 
- Configure the VPN service: 
 
VPN Server Console 
From the main menu 
 
Select Network Services… > 
Configure a network service 
 
Press Enter 
 
 
Select vpn_  
 
Press Enter 
 
Enter the appended name 
(ex. vpn_mgmt) 
 
Select the Public IP@ 
 
Enter the desired port

<<<PAGE 464>>>
13 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
- Apply the VPN configuration transferred from the OmniVista Cirrus 4:  
 
VPN Server Console 
From the main menu 
 
Select Network Endpoints… 
 
Press Enter 
 
 
Select Configure a VPN 
endpoint 
 
Select the VPN server 
configuration (ex. vpn_mgmt) 
 
Select the configuration file 
(ex. VPN_Server.conf) 
 
Select the interface (ex. None 
(Layer 3 VPN)  
 
Select Save, then press Enter 
 
Press Enter to save the 
configuration 
 
Press Enter to confirm

<<<PAGE 465>>>
14 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
- Apply the configuration changes:  
 
VPN Server Console 
From the main menu 
 
Select Apply Configuration 
Changes 
 
 
Select OK, then press Enter 
 
Press Enter to confirm 
 
 6 
Checking the VPN Status 
 
 
 
 
 
 
 
 
 
 
 
- Now that the VPN Server configuration is complete, reboot the OmniAccess Stellar Access Point to 
reinitialize the VPN connection process.  
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
AP 
VPN SERVER 
IP@: 192.168.0.2 
IP@: 192.168.0.1 
VPN > MGMT TRAFFIC

<<<PAGE 466>>>
15 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
- To check the VPN status:  
 
VPN Server Console 
From the main menu 
 
Select Maintenance… 
 
Press Enter 
 
 
Select VPN Status 
 
Press Enter 
 
 
A “peer” section should 
appear with a public IP@, the 
latest handshake operation, 
and transfer information. 
 
 7 
Configuring the OmniVista 2500 NMS 
Now that the OmniVista Cirrus 4 and VPN Server are configured, and the VPN tunnel created between the VPN 
Server and the remote OmniAccess Stellar Access Point, let’s configure the OmniVista 2500 NMS. In this 
server, we will configure the settings that will be sent to the remote OmniAccess Stellar Access Point. 
 
 
Notes 
In this part, we consider that the OmniVista 2500 NMS Virtual Appliance has already been deployed and that the 
initial configuration has already been done (IP address, gateway, password…) 
If not done, please refer to the lab dedicated to the installation of the OmniVista 2500 NMS.  
 
 
 
 
 
 
 
 
 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER

<<<PAGE 467>>>
16 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
7.1. 
Adding a Default Route in the OmniVista 2500 NMS 
To make it possible for the OmniVista 2500 NMS to reach the Remote Access Point, a default route must 
be created:  
 
Web Browser 
Select the OV2500 VA, then 
click on the 
 icon 
 
Enter the login and password 
(ex. cliadmin/Alcatel.0) 
 
Select [2] Configure the 
Virtual Appliance 
 
Select [8] Configure Route 
 
Select [3] Add Route v4 
 
Enter your default route 
information 
 
Ex:  
- subnet: 192.168.0.0 
- netmask: 255.255.255.0 
- gateway: 10.130.5.251 
 
Enter y to confirm 
 
Press [0] Exit several times to go back to the main menu

<<<PAGE 468>>>
17 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
7.2. 
Discovering the Remote Access Point in the OmniVista 2500 NMS 
 
OmniVista 2500 NMS Web Admin Interface 
Log into the OmniVista 2500 
NMS (ex. 10.130.5.50) 
 
 
Go to NETWORK > AP 
REGISTRATION > Access 
Points 
 
Select your Country/Region 
and Timezone 
 
The Remote AP should appear 
in the Managed AP tab

<<<PAGE 469>>>
18 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
7.3. 
Filling the VPN Tunnel (client’s traffic) Settings 
Let’s now create a L2GRE tunnel. The L2GRE tunnel will be created between the Remote AP and the VPN 
Server. It will carry the remote employee’s data traffic. 
 
 
 
 
 
 
 
 
 
 
 
OmniVista 2500 NMS Web Admin Interface 
Go to NETWORK > AP 
REGISTRATION > Data VPN 
Servers 
 
Click on 
 to create a new 
VPN Server 
 
Enter the VPN Settings 
 
Click Apply  
 
Name  
User-configured name for the VPN configuration. 
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
VPN > MGMT TRAFFIC 
VPN SETTINGS (VPN > CLIENT DATA TRAFFIC):  
- CLIENT IP@ RANGE: 10.7.0.55 TO .60 
- SERVER IP@: 10.7.0.61

<<<PAGE 470>>>
19 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Server's Public IP 
The VPN Server's Public IP address (configured when you installed the VPN VM). This is the IP 
address used by Remote APs to connect to the VPN Server. And this is the interface through 
which traffic originating from inside the Enterprise Network flows to the Remote site. 
Port 
The VPN Server Port. 
Server's VPN IP 
The VPN Server's Private IP address (configured when you installed the VPN VM). This is the 
interface through which traffic originating from the Remote AP flows to reach a destination 
inside the Enterprise Network. 
Client VPN IP Address Pool 
The range of addresses available to assign to Remote APs. You can select IP range and insert 
a range of IP addresses, or a shorthand mask.  
7.4. 
Exporting the VPN Tunnel (client’s traffic) settings 
 
OmniVista 2500 Web Administration Interface 
Click on Export VPN Settings 
 
A new window appears, asking 
you to download a <VPN 
Server name>.conf file 
 
Download the file 
 
 
 
Warning 
KEEP THE CONF FILE PRECIOUSLY, AS WE WILL NEED TO IMPORT IT IN THE VPN SERVER VIRTUAL APPLIANCE AT 
THE END OF THE NEXT PART.  
7.5. 
Assigning the VPN Tunnel (client’s traffic) to the Remote AP 
 
OmniVista 2500 Web Administration Interface 
Go to NETWORK > AP 
REGISTRATION > AP Group 
 
Select the Remote Access 
Point’s AP Group (ex. default 
group) 
 
Click 
 (top right of the 
screen) 
 
 
 
 
In the Data VPN Setting, 
select the Data VPN Server(s) 
previously created.  
 
Click Commit 
 
 
 
Tips 
During this lab, the default AP Group is used. If desired, it is also possible to create an AP Group dedicated for 
Remote Access Points and insert in it all the settings that will be sent to these Remote APs.

<<<PAGE 471>>>
20 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
7.6. 
Creating an Employee SSID 
For test purpose, we will create an SSID dedicated to Employees that will be broadcasted by the Remote 
Access Point.  
 
 
Notes 
This part is designed as a quick reminder, as the Employee SSID creation is viewed in details in a dedicated lab.  
 
> Select WLAN > SSIDs > SSIDs 
  > Click on the + button 
    > SSID Service Name: EmployeesX (X = R-Lab number) 
    > SSID: <filled automatically> 
    > Usage: Enterprise Network for Employees (802.1X) 
    > Click on Create & Customize 
 
    > Allowed Band: 2.4GHz and 5GHz 
    > Encryption Type: WPA3_AES  
 
Authentication Strategy 
> RADIUS Server: UPAMRadiusServer 
> Click on Manage Employee Accounts 
 
// Employee account creation // 
> Click on the + button 
  > Username: Employee 
  > Password: password 
  > Click on Create 
> Click on Close 
 
Default VLAN/Network 
 
Select Use Tunnel 
 
Enter the Tunnel ID (must be 
0) 
 
Double click in the field, then 
select the VPN Server 
configured in a previous step.  
 
 
Select the desired AP Group 
(ex. default group) 
 
Click on Save and Apply to AP 
Group

<<<PAGE 472>>>
21 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
7.7. 
On the Remote site 
The OmniVista 2500 then push its configuration to the Remote Access Point. The SSID created in the 
previous step should now be broadcasted on the remote site: 
  
 
 8 
Configuring the VPN Server Virtual Appliance 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
- As in one of the previous steps, upload the VPN server configuration (.conf file) to the VPN server VM:  
 
Windows 
Open FileZilla Client  
 
Connect to the VPN Server by 
entering the following 
information: 
- Host: VPN Server Private IP 
@ (ex. 10.130.5.251) 
- Username: admin 
- Password: VPN Server 
password (ex. Alcatel.0) 
- Port : 22 
 
Click Quickconnect 
 
REMOTE SITE 
MAIN SITE 
OMNIVISTA 2500 
ROUTER 
AP 
VPN SERVER 
VPN SETTINGS 
(.CONF FILE)

<<<PAGE 473>>>
22 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Transfer the <VPN Server 
name>.conf file in the folder 
 
/opt/OmniVista_2500_NMS/d
ata/vpn_conf/vpn_profile 
 
 
- Configure a new network service: 
 
VPN Server Console 
From the main menu 
 
Select Network Services… > 
Configure a network service 
 
Press Enter 
 
 
Select vpn_  
 
Press Enter 
 
Enter the appended name 
(ex. vpn_data) 
 
Select the Public IP@ 
 
Enter the desired port (ex. 
6551) 
 
Select Save, then press Enter 
 
Save the configuration 
 
 
In this lab, on the main site, we are using 2 different networks: 
- One dedicated to the management equipments (ex. OV2500) > VLAN 1305, IP@ range: 10.130.5.x 
- The other one dedicated for the clients/employees > VLAN 30, IP@ range: 10.7.0.x

<<<PAGE 474>>>
23 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
The VLANs are tagged on the virtual machine interfaces: 
 
 
 
MAIN SITE 
OMNIVISTA 2500 
VPN SERVER 
VPN Server 
- Public IP@: x.x.x.x (hidden) 
- Private IP@: 10.130.5.251 
- VPN Server IP@ (vpn_mgmt): 192.168.0.1 
- VPN Client IP@ (vpn_mgmt): 192.168.0.2-20 
- VPN Server IP@ (vpn_data): 10.7.0.61 
- VPN Client IP@ (vpn_data): 10.7.0.55-60 
10.130.5.50 
MGMT NETWORK  
> VLAN 1305 
 > 10.130.5.X 
CLIENTS NETWORK  
> VLAN 30 
 > 10.7.0.X 
PUBLIC INTERFACE 
> X.X.X.X (HIDDEN) 
ETH0 
ETH1 
ETH2

<<<PAGE 475>>>
24 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
- Import the VPN Endpoints configuration:  
 
VPN Server Console 
From the main menu 
 
Select Network Endpoints… 
 
Press Enter 
 
 
Select Configure a VPN 
endpoint 
 
Select the VPN server 
configuration (ex. vpn_data) 
 
Select the configuration file 
(ex. VPN_Server_Conf.conf) 
 
Select the eth2 interface  
 
Select Save, then press Enter 
 
Press Enter to save the 
configuration 
 
Press Enter to confirm 
 
 
- Apply the configuration changes:

<<<PAGE 476>>>
25 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
VPN Server Console 
From the main menu 
 
Select Apply Configuration 
Changes 
 
 
Select OK, then press Enter 
 
Press Enter to confirm 
 
 9 
On the Remote Site 
If a client connects to the SSID broadcasted by the Remote Access Point, it is now able to connect to the 
company network.  
 
Client (ex. Windows 10) 
Click on the 
 icon 
(bottom right) 
 
Select the SSID EmployeesX 
(X = R-Lab Number) 
 
Click on Connect 
 
 
 
Enter the credentials 
 
Username: Employee 
Password: password 
 
Click on OK

<<<PAGE 477>>>
26 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Click on Connect 
 
 
In our example, the client has received an IP address in the range dedicated to the employees:

<<<PAGE 478>>>
27 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
 10 [Add-On] Creating an OmniVista Cirrus 4 Account 
10.1. Logging into the OmniVista Cirrus 4 
 
Web Browser 
Access to the OmniVista Cirrus 
4 webpage 
https://registration.ovcirrus.com/ 
Click Create New Account 
 
1 – Fill the personal 
information

<<<PAGE 479>>>
28 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Fill the information about 
your company 
 
Check the 2 boxes 
 
Click Create Account 
 
10.2. Verify Your Account 
Then, a mail is automatically sent to the mail address filled during the account creation process.  
 
Mail 
Click the link GO TO VERIFY 
ACCOUNT 
 
 
Your account is now ready for use.

<<<PAGE 480>>>
29 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
 11 [Add-On] Deploying the ALE VPN Server on VMware ESXi 
11.1. Deploying the Virtual Appliance 
The VPN Server Virtual Appliance can be downloaded from the ALE Business Partner Web Site (BPWS). 
In this lab, we will deploy the VPN Server on a VMWare infrastructure. This virtual appliance can also be 
deployed on a Hyper-V infrastructure.  
 
VMware Web Console 
Log into the VMware ESXi 
 
Right click and select Deploy 
OVF Template… in the 
contextual menu 
 
Select Local File  
 
Click on Browse… 
 
 
 
Select the .ovf and .vmdk 
files 
 
Click Open, then click Next

<<<PAGE 481>>>
30 
Remote Access Point (RAP) Deployment – OV Cirrus 4 (Freemium) & OV 2500 
 
Insert a name for the VPN 
Server VA, then a folder 
where this VA will be 
deployed. 
 
Select a compute resource 
(depends on your 
infrastructure) 
 
Click Next 
 
Review the details 
 
Click Next 
 
Check the box “I accept all 
license agreements”  
 
Click Next 
 
Select a storage (depends on 
your infrastructure) 
 
Click Next 
 
Select the destination 
network for the network cards  
 
Click Next 
 
Click on Finish to launch the 
deployment

<<<PAGE 482>>>
CL A SSRO O M SESSIO N  O R VIRTUA L C L A SS SESSIO N
END OF TRAINING EVALUATIONS

<<<PAGE 483>>>
YOUR FEEDBACKS ARE 
IMPORTANT!
Thank you to complete the training 
evaluation online survey before leaving 
your session. This will take you 2 minutes! 
You must complete the end of training 
evaluation to be able to download your 
training certificate of attendance.

<<<PAGE 484>>>
LOGIN TO ALE KNOWLEDGE HUB
• Connect to ALE Knowledge Hub (https://enterprise-education.csod.com ) with your usual 
credentials

<<<PAGE 485>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (1/2)
• Click on My Training on the home page
• Search for the training course by the reference provided by your instructor

<<<PAGE 486>>>
ACCESS TO THE ONLINE EVALUATION SURVEY (2/2)
• From the session, select Evaluate in the dropdown menu and follow the instructions
OR
• From the curriculum, select Open Curriculum
• Then select Evaluate in the dropdown menu associated to the session and follow the 
instructions

<<<PAGE 487>>>
THANK YOU
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE.

<<<PAGE 488>>>
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