

<<<PAGE 1>>>
OmniVista 2500 NMS 
Version 4.9R2 
Remote Access Point and  
VPN VA Installation Guide 
 
 
 
  
  
  
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
April 2025  
Revision A 
Part Number 060958-00 
ALE USA Inc.  
2000 Corporate Center Drive 
Thousand Oaks, CA 91320  
+1 (818) 880-3500

<<<PAGE 2>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
ii 
Part No. 060958-00, Rev. A 
 
Table of Contents 
Remote Access Points and VPN Tunnel Components ............................................................ 1 
VPN for Management and Data (OVE Managed APs) .............................................................. 1 
VPN for Data Only (OVC Managed APs) .................................................................................. 2 
Prerequisites ............................................................................................................................. 2 
Network Topology ..................................................................................................................... 2 
Remote Access Points and VPN Tunnel Configuration .......................................................... 3 
Creating an OmniVista Cirrus Freemium Account .................................................................... 3 
Adding Remote APs to the Device Catalog ............................................................................... 5 
Adding Remote APs Manually ............................................................................................... 5 
Importing Multiple Remote APs ............................................................................................. 8 
Deploying/Configuring the VPN Tunnel Server ....................................................................... 10 
Recommended VPN VA Configurations .............................................................................. 10 
Known Limitations ................................................................................................................ 11 
Deploying the VPN Virtual Appliance .................................................................................. 11 
Deploying the Virtual Appliance on VMware .................................................................... 11 
Deploying the Virtual Appliance on Hyper-V .................................................................... 21 
Deploying the VPN VA 4.9.2 on Ubuntu 22.04 LTS ......................................................... 34 
Configuring the VPN Virtual Appliance ................................................................................ 48 
Complete the Installation .................................................................................................. 49 
Configure NICs ................................................................................................................. 51 
Configure Routes ............................................................................................................. 53 
Configure Network Settings (DNS, Gateway) .................................................................. 54 
Configure an SSH Service ............................................................................................... 57 
Upload the VPN Settings to the VPN Server ................................................................... 58 
Configure the VPN Service .............................................................................................. 60 
Configure VPN Endpoints ................................................................................................ 62 
Configuring the VPN Data Tunnel ........................................................................................... 64 
Configure VPN Endpoints ................................................................................................ 66 
Create an SSID for the VPN Data Tunnel ........................................................................... 68 
SSID with Tagged VLAN .................................................................................................. 69 
SSID with Untagged VLAN .............................................................................................. 69 
SSID with Local Breakout ................................................................................................ 70 
Creating a Tunnel Profile for 1201H Downlink Ports ........................................................ 71 
Configuring an Access Auth Profile for an AP Downlink Port .......................................... 72

<<<PAGE 3>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
iii 
Part No. 060958-00, Rev. A 
 
Add a Route to Reach the VPN VA from OmniVista ........................................................... 73 
Using Dual Stack Lite ISP Connections with Stellar RAPs ................................................... 75 
Upgrading the VPN VA ............................................................................................................. 76 
Basic Troubleshooting Checklist ............................................................................................ 78 
Useful Logs and Commands ................................................................................................... 78 
Local Breakout Troubleshooting .............................................................................................. 80

<<<PAGE 4>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
1 
Part No.  060958-00, Rev. A 
 
Remote Access Points and VPN Tunnel Components 
A Remote Access Point (RAP) is an AP with a management tunnel and a data tunnel to a 
remote OmniVista Enterprise (OVE) Server. An OmniVista Cirrus (OVC) Managed AP is 
technically not considered a RAP since there are no Management VPN Server details to be 
configured. An OVC managed AP already uses an OpenVPN connection for Management 
communications with a VPN Server in the OVC Cloud infrastructure. However, it is possible that 
an OVC Managed AP might need a Data VPN Tunnel to a VPN Server in the Enterprise.  
Components of the solution include: 
• 
Stellar APs 
• 
OVE/OVC 
• 
RAP VPN Server for Data VPN and/or Management VPN 
• 
Gateways and routers at customer network. 
VPN for Management and Data (OVE Managed APs) 
Typically, a local AP in the Enterprise learns its OV IP address via DHCP option 138. A local AP 
in the Enterprise is managed by OV in the Enterprise directly. An AP at a remote site cannot be 
managed by OV in the enterprise as it will not be reachable directly. The connection and 
communication need to happen via a VPN tunnel. An out-of-the-box AP that is not supplied with 
DHCP option 138 will first register with the OVC Activation Server allowing it to be configured as 
a RAP.  
If the RAP is OVE managed:  
1. The first connection, out-of-the-box, is to the OVC Device Registration Server. It retrieves the 
setup parameters for RAP including the OVE IP to which it will connect.  
2. The keys and parameters are exported to the RAP VPN Server at corporate HQ.  
3. The RAP then establishes a Wireguard VPN tunnel over which it connects to be managed by 
OVE.  
4. A Data VPN tunnel must be setup in OVE between the RAP and the VPN server. The tunnel 
keys and parameters can be exported to the VPN server at corporate HQ.  
5. Once the Data VPN tunnel is established it can be used to tunnel the required end user 
services to corporate HQ. 
Key points when RAP is managed by OVE:  
• 
The OVC Device Catalog provides options to register the AP as a RAP. This is required 
to setup the Management VPN to the RAP Virtual Appliance (VA) appliance located in 
corporate HQ. The administrator should register the AP as a RAP, which allows for pre-
provisioning the RAP VPN VA public IP/OVE on-premise IP/Security Keys etc.  
• 
Data VPN configuration is done from OVE on the managed AP. This is required to setup 
the Data VPN tunnel to the RAP VA appliance located in corporate HQ. 
• 
WLAN Service configuration is done from OVE that is managing the RAP.

<<<PAGE 5>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
2 
Part No.  060958-00, Rev. A 
 
VPN for Data Only (OVC Managed APs) 
An OVC managed AP can be configured for an encrypted Data VPN Tunnel to a remote VPN 
Server. The AP needs to be setup with the Wireguard VPN Server endpoint details allowing the 
AP to tunnel data traffic to the VPN server at corporate HQ.  
If RAP is to be managed by OVC.  
1. The first connection out-of-the-box for the AP is to the OVC Device Registration Server to 
confirm it is an OVC registered AP.  
2. The AP establishes and OpenVPN connection to be managed by OVC.  
3. A Data VPN tunnel from the RAP is setup on the OVC, and the tunnel keys and parameters 
can be exported to the VPN server at corporate HQ. 
4. Once the Data VPN tunnel is established, it can be used to tunnel the required end user 
services to corporate HQ. 
Key points when a RAP is managed by OVC: 
• 
The administrator registers the AP in the OVC Device Catalog as a standard OVC 
managed AP. No Management VPN is required as the AP is managed by OVC.  
• 
Data VPN configuration is done from OVC on the managed AP. This is required to setup 
the Data VPN tunnel to the RAP VA appliance located in corporate HQ. 
• 
WLAN Service configuration is done from OVC that is managing the AP.  
Prerequisites 
• 
ESXi versions 6.5, 6.7, 7.0.2, 8.0 are supported (ESXi 5.5 is not supported). 
• 
Hyper-V 2016, 2019, and 2022 
• 
Supported Stellar RAP version is AWOS 5.0.2 and higher.  
• 
RAP VPN VA version 4.9.2.2 
• 
The virtual appliance version 4.9.2.2 is certified for use with OmniVista 2500 4.9R2 and 
OmniVista Cirrus version 4.9.2. 
Network Topology 
Within this document we will use the following network topology:

<<<PAGE 6>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
3 
Part No.  060958-00, Rev. A 
 
Remote Access Points and VPN Tunnel Configuration 
You can configure an offsite, RAP that can be managed by your local OVE installation through a 
VPN Tunnel. Remote APs are added to the Device Catalog using a “Freemium version of 
OmniVista Cirrus, the cloud-based version of OmniVista. You then must deploy a VPN Tunnel 
Server Virtual Appliance (VPN VA). 
When the AP(s) is connected to the network, it automatically contacts the OmniVista Cirrus 
Activation Server, which downloads the necessary IP and VPN configurations, and the AP is 
added to the List of Managed Devices and manageable by your local OVE installation. The 
following sections detail the steps required to deploy RAPs:  
1. Creating an OmniVista Cirrus Freemium Account 
2. Adding Remote APs to the Device Catalog  
3. Deploying/Configuring the VPN Tunnel Server 
Note that when you add Remote APs to the Device Catalog (Step 2) you will need to enter 
information about the VPN Server, which is configured in Step 3. Determine your VPN Server 
configuration before starting. 
Note: The Remote AP feature is supported on Stellar APs running AWOS 5.0.2. and 
higher. For the latest features, AWOS 5.0.2 and higher is required.  
Note: Tagged and untagged traffic can be tunneled through VPN tunnels. 
Creating an OmniVista Cirrus Freemium Account 
OmniVista Cirrus offers a “Freemium” account which is used to add Remote APs. Follow the 
steps below to create an OmniVista Cirrus “Freemium” Account.  
1. Go to the OV Registration Portal. 
 
2. Click on the Create a New Account button. The Create New Account Screen will appear.

<<<PAGE 7>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
4 
Part No.  060958-00, Rev. A 
 
3. Complete the fields. Fields marked with an asterisk (*) are required. At the bottom of each 
screen, click Continue to move to the next screen. Note that the username you enter will be 
used to log into OmniVista Cirrus once your account is created. Also note that the e-mail 
address you enter will be used to verify your account and complete the process. When you have 
completed and reviewed all of the fields, accept the terms and conditions and click on the 
Create Account button. A Confirmation Screen will appear. 
 
4. Go to the e-mail account you entered in Step 3 above. You will receive an e-mail from ALE 
USA Inc (noreply@ovcirrus.com) containing instructions and a verification link. Click on the Go 
to Verify Account link. The Set Password Screen will appear. 
Important Note: There is a link in the body of the email to download the required device 
OS software for OmniVista Cirrus. APs must be running a minimum software version of 
AWOS 5.0.1. Click on the link to download the software. If necessary, you can use this 
software to upgrade your devices. 
5. Create and confirm your password, then click on the Save button. The Confirmation Screen 
below will appear. 
 
6. Click on the Continue to Login Page link and log into OmniVista Cirrus using the username 
and password you created. After successful login, the OmniVista Cirrus Freemium Dashboard 
will appear.

<<<PAGE 8>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
5 
Part No.  060958-00, Rev. A 
 
 
Note: You will continue to log into https://registration.ovcirrus.com using the username 
and password you created to access your OmniVista Cirrus Freemium Account. 
Adding Remote APs to the Device Catalog 
Remote APs are added using the Device Catalog application. You can add APs one-at-a-time or 
import multiple APs at once using a .csv file.  
Adding Remote APs Manually 
1. Select Network - Inventory - Device Catalog to bring up the Device Catalog application.

<<<PAGE 9>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
6 
Part No.  060958-00, Rev. A 
 
 
2. Click on the Add icon (+) in the upper-right corner of the screen to bring up the Add a Device 
Screen. 
 
3. Enter the AP Serial Number, in the Device Type drop-down select Stellar AP, then enable 
the Is this a Remote AP Field to open the Remote AP configuration fields (shown below).

<<<PAGE 10>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
7 
Part No.  060958-00, Rev. A 
 
 
4. Complete the fields as described below, then click on the Save VPN Settings and Create 
Device button to add the AP to the Device Catalog.  
• 
MAC Address - The MAC address of the AP. 
• 
Is This a Remote AP - Click the slider to "Yes". 
• 
VPN Settings - The VPN Tunnel configuration between the VPN Server and the 
OmniVista Enterprise Server. Select the Create New VPN Settings radio button to 
initially configure a Tunnel. Once you configure and save Tunnel Settings, they are 
saved under the VPN Settings Name and you can simply select Choose Existing VPN 
Settings to select an existing VPN configuration when adding Remote APs.  
• 
VPN Settings Name - Enter a name for the VPN configuration.  
• 
Server's Public IP - The VPN Server's Public IP address (configured on one of the 
interfaces when you installed the VPN VA).  This is the IP address used by Remote 
APs to connect to the VPN Server. And this is the interface through which traffic 
originating from inside the Enterprise Network flows to the Remote site. 
• 
Port - The VPN Public IP Server Port. 
• 
Server's VPN IP - The VPN Server's Private IP address within the virtual network 
(must be in the same network as the client pool). This is the tunnel interface through 
which traffic originating from the Remote AP flows to reach a destination inside the 
Enterprise Network.

<<<PAGE 11>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
8 
Part No.  060958-00, Rev. A 
 
• 
OmniVista Enterprise Server IP - The IP address of the OmniVista Enterprise Server 
that will manage the devices.  
• 
Client VPN IP Address Pool - The range of addresses available to assign to 
Remote APs. 
 
IP Range - Enter a starting and ending IP address range. 
 
Shorthand Mask - Enter a shorthand mask for the IP Range  
 
Subnet Mask - Enter the subnet mask for the Client VPN IP Address Pool. 
Importing Multiple Remote APs 
You can add multiple Remote APs at once by importing a .csv file containing the APs and any 
relevant information.  
1. Select Network - Inventory - Device Catalog to bring up the Device Catalog application. 
 
2. Click on the Import button in the upper-right corner of the screen to bring up the Import 
Devices Screen.

<<<PAGE 12>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
9 
Part No.  060958-00, Rev. A 
 
3. Click on the Browse button to locate the .csv file containing the APs, then click on the Import 
button at the bottom of the screen. The APs in the file will be imported into the Device Catalog. 
If necessary, click on the Template button to open or download an import template file (shown 
below).  
 
Modify the Template with AP Serial Numbers and any additional information you want to add. If 
you want to add VPN Setting information (VpnSettingName), the RAP field must be “TRUE”. 
Save the file, and then go to Step 3 to import the file and add the APs to the Device Catalog.  
An example of an import file for Remote APs is shown below.

<<<PAGE 13>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
10 
Part No.  060958-00, Rev. A 
 
 
Deploying/Configuring the VPN Tunnel Server 
A Virtual Private Network (VPN) Virtual Appliance (VA) is required for managing Remote Access 
APs and securely tunneling data from devices at remote locations. The following sections 
details the steps for deploying and configuring a VPN VA.  
Recommended VPN VA Configurations 
The VPN VA and NIC configurations are based on the number of Remote APs being managed. 
The number of Virtual NICs supported by RAP VPN VA are limited only by the hypervisor. RAP 
VPN VA does not impose any limits on this. 
• 
VPN VA Configuration (Based on the number of Remote APs) 
• 
1 - 100 APs - 4 vCPUs, 2GB RAM 
• 
100 - 250 APs - 6 vCPUs, 4GB RAM 
• 
250 - 500 APs - 8 vCPUs, 8GB RAM 
• 
500 - 1,000 APs - 12 vCPUs, 16GB RAM.  
Note: Higher scale is based on CPU/Memory calculated per RAP. For deployments 
with more than 250 RAPs, it is recommended that you deploy a second VPN VA 
Server.

<<<PAGE 14>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
11 
Part No.  060958-00, Rev. A 
 
• 
NICs - 1G vs.10G (Based on expected throughput) 
• 
10 - 20Mbps expected VPN throughput per RAP, if local breakout is serving all 
internet needs. 
• 
20 - 100Mpbs expected VPN throughput per RAP, if all traffic is tunneled through 
VPN. 
• 
10G NIC is standard for more than 500 APs. For increased throughput use 2 x 10G 
NIC (NIC Teaming). 
• 
NIC Teaming 
• 
NIC Teaming is supported when deploying the VPN Virtual Appliance. Click here for 
details. 
Known Limitations 
• 
RAP VPN VA does not support redundancy. 
Deploying the VPN Virtual Appliance 
Deploy the VPN VA on your Hypervisor. The VA can be deployed on VMware or Hyper-V. After 
deploying the VA, configure the VA and complete the installation.  
Deploying the Virtual Appliance on VMware 
Note: In the instructions below, the screens are for demonstration purposes. Some of the 
screens shown may depict an older release. 
1. Download and unzip the OVF package. You will be using the OVF File and both VMDK Files 
(disk 1 and disk 2) for the installation. The Zip file also contains an *.mf File. Delete the *.mf 
File from the folder before importing the files in Step 5. 
2. Log into VMware ESXi.

<<<PAGE 15>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
12 
Part No.  060958-00, Rev. A 
 
 
3. Select the Host on which you want to install the VPN VA and click on Create/Register 
VM. The first screen of the New Virtual Machine Wizard appears.  
 
4. Select Deploy a virtual machine from an OVF or OVA file and click Next.

<<<PAGE 16>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
13 
Part No.  060958-00, Rev. A 
 
 
5. Enter a name for the VM (e.g., VPN VA 4.9.2), click to locate and select the downloaded 
installation files (or drag the files into the window), then click Next. Remember, do not include 
the *.mf File; only the *ovf file and the two *vmkd Files.

<<<PAGE 17>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
14 
Part No.  060958-00, Rev. A 
 
6. Select the destination storage where the template is to be deployed, then click Next.  
 
7. Review the License Agreement, click I agree, then click Next.

<<<PAGE 18>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
15 
Part No.  060958-00, Rev. A 
 
8. In the Network mapping field, select the Destination network that the deployed VM will use. 
In the Disk provisioning field, select Thin. Click Next. 
 
9. Review the configuration and click Finish. You will be returned to the main screen with the 
deployment progress displayed in the Recent tasks table.

<<<PAGE 19>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
16 
Part No.  060958-00, Rev. A 
 
10. When the installation is complete (indicated by all three files showing “Completed 
Successfully” in the Result column of the Recent tasks table), click on Virtual Machines in the 
Navigator Tree on the left side of the screen to display a list of VMs. Select the VM you just 
deployed. Basic details for the VM are displayed, as shown below.

<<<PAGE 20>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
17 
Part No.  060958-00, Rev. A 
 
Important Notes: 
• 
On the ESXi VM, configure the VLAN the NIC dedicated to bridged traffic (the interface 
without the managed IP Address), as follows: 
• 
Configure VLAN 0 if you want Untagged VLAN traffic to be tunneled through VPN 
tunnels. 
• 
Configure VLAN 4095 if you want Tagged VLAN traffic to be tunneled through VPN 
tunnels.  
 
• 
On the ESXi VM, enable Promiscuous Mode for the above NIC. If the “Override” 
checkbox is enabled, make sure Promiscuous Mode, MAC address changes, and 
Forged transmits are set to “Accept”. 
 
• 
Inherit from vSwitch means this port group uses the same setting as vSwitch0; so, make 
sure vSwtich0 is set to “Accept” for Promiscuous Mode, MAC address changes, and 
Forged transmits. Or you can set Accept directly in the port group setting.

<<<PAGE 21>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
18 
Part No.  060958-00, Rev. A 
 
 
11. Click on the small Console Screen or click on Console at the top of the screen and select 
Open Browser Console to open a Console and go to Configuring the VPN Virtual Appliance to 
complete the installation.  
Deploying the VPN VA with NIC Teaming 
1. From ESXi Web GUI, go to Networking and select the Virtual switches tab. Choose the 
virtual switch and click on Add Uplink. 
 
2. Select the uplink.

<<<PAGE 22>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
19 
Part No.  060958-00, Rev. A 
 
 
3. Edit the virtual switch and configure the load balancing rule.

<<<PAGE 23>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
20 
Part No.  060958-00, Rev. A

<<<PAGE 24>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
21 
Part No.  060958-00, Rev. A 
 
Deploying the Virtual Appliance on Hyper-V 
Note: In the instructions below, the screens are for demonstration purposes. Some of the 
screens shown may depict an older release. 
1. Download and unzip the OVF package. You will be using the OVF File and both VMDK 
Files (disk 1 and disk 2) for the installation (ovnmse-vpn-4.9.2.2.ovf, ovnmse-vpn-
4.9.2.2-disk001.vmdk and ovnmse-vpn-4.9.2.2-disk002.vmdk). The Zip file also 
contains an *.mf File. Delete the *.mf File from the folder before importing the files 
in Step 2. 
 
2. Import the VM into Hyper-V.  
 
3. Select the location folder to Hyper-V source of VPN VA.

<<<PAGE 25>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
22 
Part No.  060958-00, Rev. A 
 
 
4. Select the Import Type: Copy the Virtual Machine. 
 
5. Choose Destination and Storage Folder. You can use the default or customize the location. 
6. Click Finish to complete the VA import.

<<<PAGE 26>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
23 
Part No.  060958-00, Rev. A 
 
 
7. Edit the Virtual machine and remove the Network interface.

<<<PAGE 27>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
24 
Part No.  060958-00, Rev. A 
 
 
8. Run the commands below on Power shell to create 3 Network Adapters. 
1. For ($Count=0; $Count -le 2; $Count ++) 
2. { 
3. Add-VMNetworkadapter -VMName OmniVista-VPN-4.9.2 -Name "Eth$Count" 
4. } 
 
 
 
9. Create an “External” Hyper-V virtual switch.

<<<PAGE 28>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
25 
Part No.  060958-00, Rev. A 
 
 
10. Attach to the Physical network interface.

<<<PAGE 29>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
26 
Part No.  060958-00, Rev. A 
 
 
11. Use Eth0 for the public interface, Eth1 for the private interface, and Eth2 for the bridge 
interface. 
 
12. Edit the VPN virtual machine. Select Enable virtual LAN identification on Eth0 and map to 
public VLAN (e.g., VLAN 70)

<<<PAGE 30>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
27 
Part No.  060958-00, Rev. A 
 
 
13. Select Enable virtual LAN identification on Eth1 and map to private VLAN (e.g., VLAN  
1000).

<<<PAGE 31>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
28 
Part No.  060958-00, Rev. A 
 
 
14. Expand Eth2, under Advanced Features select the option Enable MAC address 
spoofing.

<<<PAGE 32>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
29 
Part No.  060958-00, Rev. A 
 
 
15. Configure the Trunk Mode for Eth2 using the command below command in the power shell. 
Set-VMNetworkAdaptervlan -VMName OmniVista-VPN-4.9.2 -
VMNetworkAdapterName "Eth2"-Trunk -AllowedVlanIdList "201,202" -
NativeVlanId 0 
16. Verify that Trunk Mode is successfully enabled using the commands below. 
Get-VMNetworkAdapterVlan -VMName OmniVista-VPN-4.9.2 
 
17. Start the VPN virtual machine and perform the setup.

<<<PAGE 33>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
30 
Part No.  060958-00, Rev. A 
 
Deploying the VPN VA with NIC Teaming 
1. Open Server Manager - Local Server.  
 
2. Edit NIC Teaming - New Team. 
 
3. Choose NIC members, Teaming mode, and Load balancing mode, then click OK.

<<<PAGE 34>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
31 
Part No.  060958-00, Rev. A

<<<PAGE 35>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
32 
Part No.  060958-00, Rev. A 
 
4. Create a Hyper-V virtual switch and attach to the NIC Teaming interface, then click OK. 
 
5. Edit the VM network interface. Change the Virtual Switch to NIC Teaming.

<<<PAGE 36>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
33 
Part No.  060958-00, Rev. A 
 
 
 
NIC Teaming Compatible Modes 
Layer 2 Switch Mode NIC Teaming Mode Load Balancing Mode Stand-By Adapter Worked? 
Switch Independent 
Switch Independent Address Hash 
None 
Yes 
Switch Independent 
Switch Independent Address Hash 
NIC1/NIC2 
Yes 
Switch Independent 
Switch Independent Hyper-V Port 
None 
No 
Switch Independent 
Switch Independent Hyper-V Port 
NIC1/NIC2 
No 
Switch Independent 
Switch Independent Dynamic 
None 
No 
Switch Independent 
Switch Independent Dynamic 
NIC1/NIC2 
No 
Linkagg static 
Linkagg static 
Address Hash 
None 
Yes 
Linkagg static 
Linkagg static 
Hyper-V Port 
None 
Yes 
Linkagg static 
Linkagg static 
Dynamic 
None 
Yes 
LACP 
LACP 
Address Hash 
None 
Yes

<<<PAGE 37>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
34 
Part No.  060958-00, Rev. A 
 
NIC Teaming Compatible Modes 
Layer 2 Switch Mode NIC Teaming Mode Load Balancing Mode Stand-By Adapter Worked? 
LACP 
LACP 
Hyper-V Port 
None 
Yes 
LACP 
LACP 
Dynamic 
None 
Yes 
Deploying the VPN VA 4.9.2 on Ubuntu 22.04 LTS 
1. Download and unzip the KVM package. You will be using both qcow2 Files (disk 0001 and 
disk 0002) for the installation. You will not be using the *.mf File. 
2. Log into the Linux machine and update Ubuntu 22.04  
a. Start by updating your system to ensure that you have the latest packages and 
dependencies. Execute the command sudo apt update -y in the terminal. 
b. Install KVM packages: Install the necessary KVM packages by running the following 
command in the terminal: 
sudo apt install qemu-kvm libvirt-clients libvirt-daemon-system virtinst 
bridge-utils -y 
c. Deploy the VA and launch the Virtual Machine Manager, as shown below.  
 
The following screen appears. 
 
3. Select File - New Virtual Machine. The Create a New Virtual Machine Screen (Step 1 of 4) 
appears.

<<<PAGE 38>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
35 
Part No.  060958-00, Rev. A 
 
 
4. Select Import existing disk image, and click Forward. The Create a New Virtual Machine 
Screen (Step 2 of 4) appears.

<<<PAGE 39>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
36 
Part No.  060958-00, Rev. A 
 
5. Click Browse to locate the storage disk.  
 
6. Click Browse Local to locate the disk files from the KVM package that you downloaded.  
 
7. Select disk001 and click Open. The Create a New Virtual Machine Screen (Step 2 of 4) 
appears.

<<<PAGE 40>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
37 
Part No.  060958-00, Rev. A 
 
 
8. In the search field at the bottom of the screen, enter linux to bring up Linux versions, and 
select Generic Linux 2022 (linux2022)

<<<PAGE 41>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
38 
Part No.  060958-00, Rev. A 
 
 
The completed Create a New Virtual Machine Screen (Step 2 of 4) appears, as shown below.

<<<PAGE 42>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
39 
Part No.  060958-00, Rev. A 
 
 
9. Click Forward. The Create a New Virtual Machine Screen (Step 3 of 4) appears.

<<<PAGE 43>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
40 
Part No.  060958-00, Rev. A 
 
 
10. The default Memory and CPU values depend on the OS family you select. The list of OS families 
is in KVM by default, so you cannot change it when deploying OV on KVM. Click Forward to continue. 
The Create a New Virtual Machine Screen (Step 4 of 4) appears.

<<<PAGE 44>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
41 
Part No.  060958-00, Rev. A 
 
 
11. Enter a Name for the VA (e.g., ove), check the Customize configuration before install 
checkbox, then click Finish. The following screen will appear.

<<<PAGE 45>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
42 
Part No.  060958-00, Rev. A 
 
 
12. Click on Add Hardware on the bottom left side of the screen. The following screen appears.

<<<PAGE 46>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
43 
Part No.  060958-00, Rev. A 
 
 
13. Make sure the Storage tab is selected, then and click on the Select or create custom 
storage radio button and click on Manage. The following screen appears. 
 
14. Locate the disk002 file, select it, then click on Choose Volume. The following screen 
appears.

<<<PAGE 47>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
44 
Part No.  060958-00, Rev. A 
 
 
15. Click Finish to return to the VM Configuration Window.

<<<PAGE 48>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
45 
Part No.  060958-00, Rev. A 
 
 
16. Select the VA NIC and configure the 3 NICs as shown below, then click Apply: 
To add a new NIC for Virtual Machine, click Add Hardware and then select Network.

<<<PAGE 49>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
46 
Part No.  060958-00, Rev. A 
 
 
Note: You have to setup 3 NICs with the VPN VA. The NIC format is below: 
• 
Network Source: Macvtap device 
• 
Device name: Input the NIC name of Ubuntu 
• 
Device Model: default 
Please click Finish to complete “Add a new NIC”.

<<<PAGE 50>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
47 
Part No.  060958-00, Rev. A 
 
 
17. Before beginning the installation (Step 18), reduce qcow2 disk size. Select VirtIO Disk 1 on 
the left side of the screen. Select Advanced options, then select Performance options and 
set the Discard Mode to unmap. Repeat for the VirtIO Disk 2. 
 
18. Click on Begin Installation at the top-left corner of the window to begin the deployment.

<<<PAGE 51>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
48 
Part No.  060958-00, Rev. A 
 
Configuring the VPN Virtual Appliance 
Note: Keep the default settings in the OVF for Guest OS, VM Compatibility and NIC type 
(E1000), as shown below:

<<<PAGE 52>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
49 
Part No.  060958-00, Rev. A 
 
Once the VPN is deployed, perform the following steps to complete the installation:  
1. Complete the Installation 
2. Configure NICs 
3. Configure Routes 
4. Configure Network Settings (DNS, Gateway) 
5. Configure an SSH Service 
6. Upload VPN Settings to the VPN Server 
7. Configure the VPN Service 
8. Configure VPN Endpoints 
Complete the Installation 
1. Launch the Hypervisor Console for the VPN VA. You will be automatically logged in and the 
Keyboard Layout Prompt will appear. Press Enter if you do not want to change the default 
keyboard layout (US), or enter y then press Enter to change the default keyboard layout 
 
2. The End User Agreement will appear. Press the spacebar to scroll through the agreement. 
When you reach the end of the agreement, enter y and Press Enter to accept the agreement.

<<<PAGE 53>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
50 
Part No.  060958-00, Rev. A 
 
 
3. The Admin Password Prompt will appear. Enter and confirm the Admin Password for the VM 
and press Enter. 
 
4. The VM will reboot. When the reboot is complete, the OmniVista Login Prompt will appear. 
Enter the OmniVista Login (admin) and press Enter; then enter the Admin Password you 
configured in Step 3 and press Enter. 
 
5. The Main Menu will appear with the Network Interfaces option highlighted.

<<<PAGE 54>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
51 
Part No.  060958-00, Rev. A 
 
Configure NICs 
 
1. With the Network Interfaces option highlighted, press Enter to bring up the Menu for 
Network Interfaces Screen.  
 
2. At the Please select NIC to modify prompt at the bottom of the screen, enter the number of 
the NIC you want to configure (e.g., 1), use the Down Arrow to highlight OK and press Enter.  
 
3. Enter the VPN Public IPv4 address (e.g.,10.255.222.97) use the Down Arrow to move to the 
Prefix Length field and enter the prefix length (e.g., 24) for the IP address. Move the Down 
Arrow to highlight Save and press Enter, then press Enter at the OK Confirmation Prompt. The 
following prompt will appear.

<<<PAGE 55>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
52 
Part No.  060958-00, Rev. A 
 
 
4. Repeat the process in Step 3 above to configure the OVE Server IP address. This is the 
interface that will be used to connect to the OVE Server. 
 
Note: To set up a Data Tunnel, you use the third NIC on the VA. You must not configure 
an IP address for this NIC because it will be a Layer 2 Tunnel. You also need to enable 
"Promiscuous Mode" for this NIC in your Hypervisor. 
5. Press Enter to return to the Main Menu.  
 
6. Use the Down Arrow to highlight Apply Configuration Changes and press Enter. 
 
7. The following Confirmation Prompt will appear. Press Enter to apply the configuration. When 
the process is complete, the Main Menu will appear.

<<<PAGE 56>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
53 
Part No.  060958-00, Rev. A 
 
 
Configure Routes 
If necessary, configure a Network Route. 
 
1. On the Main Menu Screen, highlight Network Routes and press Enter. 
 
2. With Add a Network Route highlighted, press Enter. 
 
3. Enter the Network Route Subnet, use the Down Arrow the enter the Prefix Length, and the 
Gateway. Use the Down Arrow to move to Save, then press Enter.  
 
4. At the Confirmation Prompt, with Save highlighted, press Enter, then press OK at the next 
Confirmation Prompt. The Network Route will be added and Main Menu will appear.

<<<PAGE 57>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
54 
Part No.  060958-00, Rev. A 
 
 
5. Use the Down Arrow to highlight Apply Configuration Changes and press Enter. 
 
6. The following Confirmation Prompt will appear. Press Enter to apply the configuration. When 
the process is complete, the Main Menu will appear.  
 
Configure Network Settings (DNS, Gateway) 
If necessary, configure a DNS; and configure a Default Gateway for public network access. 
 
1. On the Main Menu Screen, highlight Network Settings and press Enter.

<<<PAGE 58>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
55 
Part No.  060958-00, Rev. A 
 
 
2. Highlight Configure a Network Setting and press Enter.  
 
3. With Configure DNS highlighted, press Enter. 
 
4. Enter a DNS Server IP address(es), use the Down Arrow to highlight Save, and press 
Enter. 
 
5. Press Enter, then press Enter at the next Confirmation Prompt. 
 
6. Highlight Configure Default Gateway and press Enter. 
 
7. Enter the Gateway IP address, use the Down Arrow to highlight Save and press Enter.

<<<PAGE 59>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
56 
Part No.  060958-00, Rev. A 
 
 
8. Press Enter, then press Enter at the next Confirmation Prompt. 
 
9. Highlight Exit and press Enter until you return to the Main Menu. 
 
10. Use the Down Arrow to highlight Apply Configuration Changes and press Enter. 
 
11. The following Confirmation Prompt will appear. Press Enter to apply the configuration. 
When the process is complete, the Main Menu will appear.

<<<PAGE 60>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
57 
Part No.  060958-00, Rev. A 
 
Configure an SSH Service 
Configure an SSH Service on the VA to enable an SSH connection to upload the VPN Settings 
File. 
 
1. On the Main Menu Screen, highlight Network Services and press Enter. 
 
2. Highlight Configure a Network Service and press Enter. 
 
3. With SSH highlighted, press Enter. 
 
4. Enter the number corresponding to the address (e.g., 1), and use the Down Arrow to enter 
the SSH Port Number. Use the Down Arrow to highlight Save and press Enter.

<<<PAGE 61>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
58 
Part No.  060958-00, Rev. A 
 
 
5. With Yes highlighted, press Enter at the Confirmation Prompt. 
 
6. Press Enter at the final Confirmation prompt and press Enter until you return to the Main 
Menu. 
7. Use the Down Arrow to highlight Apply Configuration Changes and press Enter. 
 
8. The following Confirmation Prompt will appear. Press Enter to apply the configuration. When 
the process is complete, the Main Menu will appear.  
 
Upload the VPN Settings to the VPN Server 
If you have not already done so, you must export the VPN Settings file from your OmniVista 
Freemium account to your computer. You will then SFTP this file to the VPN VA to configure the 
VPN Service. If you have already exported the VPN Settings to your computer, go to Step 4. 
Note: If you add an AP to the Device Catalog in your OmniVista Freemium account after 
exporting the VPN Settings file, you will have to redo the export, SFTP, and reconfigure the 
VPN VA. 
1. Go to the Device Catalog Screen (Network – Device Catalog) of your OmniVista Freemium 
account.

<<<PAGE 62>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
59 
Part No.  060958-00, Rev. A 
 
 
2. Click on the Export VPN Settings button at the top of the screen. Note that you do not have 
to wait until APs reach “Registered” status. Once APs are added to the Device Catalog you can 
export the VPN settings for the APs. 
 
The file must contain the list of all RAPs (peers) with their IP Addresses and Public Keys as 
shown below: 
[Peer]  
PublicKey = w7dRCdRmrC7axxxxxx967Yw3iann3sgT+nbX1T3hlA= 
AllowedIPs = 10.180.2.7/32 
3. Select the VPN Settings that you want to use (e.g., LAB4) and click Export. The file will be 
downloaded to your computer (e.g., LAB4.conf).  
4. SFTP the VPN Settings File (e.g., LAB4.conf) to the vpn_profile Directory (/opt/OmniVista_ 
2500_NMS/data/vpn_conf/vpn_profile) on the VPN VA.  
Important Note: Do not change the name of the VPN Settings file.

<<<PAGE 63>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
60 
Part No.  060958-00, Rev. A 
 
 
Important Note: Any time you modify VPN settings you must generate a New VPN 
Settings File and FTP the file to the VPN Server. 
Configure the VPN Service  
Configure a VPN Management Service on the VA. 
 
1. From the Main Menu, highlight Network Services and press Enter.

<<<PAGE 64>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
61 
Part No.  060958-00, Rev. A 
 
 
2. Highlight Configure a Network Service and press Enter.  
 
3. Highlight VPN and press Enter. 
 
4. Enter a name for the service after the underscore (e.g., vpn_management), then use the 
Down Arrow to select the number of the NIC on which you want to create the service (e.g., 1). 
This is the NIC of the VPN VA Public IP address. Then use the Down Arrow again to enter the 
Port Number. This is the port number of the VPN VA Public IP address. Use the Down Arrow to 
highlight Save and press Enter. 
 
5. Press Enter, then press Enter at the next Confirmation Prompt. Select Exit until you return to 
the Main Menu. 
6. Use the Down Arrow to highlight Apply Configuration Changes and press Enter.

<<<PAGE 65>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
62 
Part No.  060958-00, Rev. A 
 
 
7. The following Confirmation Prompt will appear. Press Enter to apply the configuration. When 
the process is complete, the Main Menu will appear.  
 
Configure VPN Endpoints 
Attach the VPN Settings File to the VPN Service. 
 
1. From the Main Menu, highlight VPN Endpoints and press Enter.  
 
2. Highlight Configure a VPN Endpoint and press Enter.

<<<PAGE 66>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
63 
Part No.  060958-00, Rev. A 
 
 
3. Select the number for the VPN Server Configuration (e.g., 1 - vpn_management). This is 
the VPN Service you created in the previous section. Use the Down Arrow to select the VPN 
Settings Configuration File (e.g., 1 - LAB4.conf); then use the Down Arrow to select the 
interface for Regular VPN (e.g., 2 – None); use the Down Arrow to select Save, and press 
Enter.  
 
4. Press Enter at the next Confirmation Prompt. Select Exit until you return to the Main Menu. 
5. Use the Down Arrow to highlight Apply Configuration Changes and press Enter.

<<<PAGE 67>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
64 
Part No.  060958-00, Rev. A 
 
6. The following Confirmation Prompt will appear. Press Enter to apply the configuration. When 
the process is complete, the Main Menu will appear.  
 
Configuring the VPN Data Tunnel 
Once the Management VPN tunnel is configured, follow the steps below to configure a VPN 
Data tunnel. An L2GRE tunnel will be created between the Remote AP and the VPN Server and 
it will be used to tunnel the remote employee’s data traffic. 
1. Go to Network –> AP Registration -> Data VPN Server to add a Data VPN Server.  
 
 
Name  
User-configured name for the VPN configuration. 
Server's Public IP 
The VPN Server's Public IP address (configured when you installed the 
VPN VA). This is the IP address used by Remote APs to connect to the 
VPN Server. And this is the interface through which traffic originating from 
inside the Enterprise Network flows to the Remote site. 
Port 
The VPN Server Port. 
Server's VPN IP 
The VPN Server's Private IP address within the virtual network (must be in 
the same network as the client pool). This is the interface through which 
traffic originating from the Remote AP flows to reach a destination inside the 
Enterprise Network. 
Client VPN IP Address 
Pool 
The range of addresses available to assign to Remote APs. You can select 
IP range and insert a range of IP addresses, or a shorthand mask.

<<<PAGE 68>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
65 
Part No.  060958-00, Rev. A 
 
2. Go to the AP Group Screen (Network - AP Registration - AP Group) and edit the AP Group 
used to manage Remote APs. 
 
3. Assign the Data VPN Server to the AP Group (mandatory to set up the Data VPN Tunnel). 
  
4. Go to the Data VPN Servers Screen and click on the Export VPN Settings button.  
 
 
5. Select the VPN Settings that you want to use and click Export VPN Settings. The file will be 
downloaded to your computer. The file must list all RAPs with their IP Addresses and Public 
Keys as shown below: 
[Peer] 
PublicKey = opNxg1UpN2Pv/9S2HaxxxxxyfJYAIbOHSRDo78r+To= 
AllowedIPs = 192.168.1.2/32

<<<PAGE 69>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
66 
Part No.  060958-00, Rev. A 
 
6. SFTP the VPN Settings File to the vpn_profile Directory (/opt/OmniVista 
2500_NMS/data/vpn_conf/vpn_profile) on the VPN VA. See Upload the VPN Settings to the 
VPN Server. 
Note: Do not change the name of the VPN Settings file. 
7. Configure the VPN service for Data Tunnel. 
 
8. Configure VPN Endpoints. Be sure to select the right ethernet interface for bridging traffic 
(e.g., eth2 without IP Address). 
Configure VPN Endpoints 
Attach the VPN Settings File to the VPN Service. 
 
1. From the Main Menu, highlight VPN Endpoints and press Enter.  
 
2. Highlight Configure a VPN Endpoint and press Enter.

<<<PAGE 70>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
67 
Part No.  060958-00, Rev. A 
 
 
3. Select the number for the VPN Server Configuration (e.g., 1 - vpn_data). This is the VPN 
Service you created in the previous section. Use the Down Arrow to select the VPN Settings 
Configuration File (e.g., 2 – VPN_Server_Conf.conf); then use the Down Arrow to select the 
interface for bridged traffic (e.g., 1 – eth2); use the Down Arrow to select Save, and press 
Enter.  
 
4. Press Enter at the next Confirmation Prompt. Select Exit until you return to the Main Menu. 
5. Use the Down Arrow to highlight Apply Configuration Changes and press Enter. 
 
6. The following Confirmation Prompt will appear. Press Enter to apply the configuration. When 
the process is complete, the Main Menu will appear.

<<<PAGE 71>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
68 
Part No.  060958-00, Rev. A 
 
 
Create an SSID for the VPN Data Tunnel 
Once the VPN Data tunnel is configured an SSID and Access Role Profile must be created to 
tunnel the user traffic. For example: 
1. Create an SSID.  
> Select WLAN > SSIDs > SSIDs 
  > Click on the + button 
    > SSID Service Name: EmployeesX (X = R-Lab number) 
    > SSID: <filled automatically> 
    > Usage: Enterprise Network for Employees (802.1X) 
    > Click on Create & Customize 
 
    > Allowed Band: All 
    > Encryption Type: WPA3_AES  
 
Default VLAN/Network: 
VLAN(s): untagged 
Use Tunnel: checked 
Tunnel ID:0 
GRE Tunnel Server IP Address/data VPN Server: select profile created at previous section 
Support of Entropy: Disabled 
Allow Local Breakout: Disabled (will be supported with AWOS 4.0.1) 
 
Authentication Strategy 
> RADIUS Server: UPAMRadiusServer 
> Click on Manage Employee Accounts 
 
// Employee account creation // 
> Click on the + button 
  > Username: Employee 
  > Password: password 
  > Click on Create 
> Click on Close 
2. Select the SSID and AP Group, save and apply.   
 
 
3. OmniVista 2500 will push the configuration to the Remote Access Point allowing users to 
connect to the SSID just configured.

<<<PAGE 72>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
69 
Part No.  060958-00, Rev. A 
 
 
SSID with Tagged VLAN 
To configure an SSID with a tagged VLAN, configure the VLAN fields in the SSIDs application 
as shown in the example below. 
 
SSID with Untagged VLAN 
To configure an SSID with an untagged VLAN, configure the VLAN fields in the SSIDs 
application as shown in the example below. 
 
Configuring Switches for Tagged/Untagged Traffic 
The CLI Commands below are used to configure AOS 8.x and AOS 6.x Switches for tagged and 
untagged traffic.

<<<PAGE 73>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
70 
Part No.  060958-00, Rev. A 
 
• 
AOS 8.x 
• 
For Tagged VLAN: vlan [vlan_num] member port/linkagg 
[port_num/agg_num] tagged 
• 
For Untagged VLAN: vlan [vlan_num] member port/linkagg 
[port_num/agg_num] untagged 
• 
AOS 6.x 
• 
For Tagged VLAN: vlan [vlan_num] 802.1q [port_num/ agg_num] 
• 
For Untagged VLAN: vlan [vlan_num] port default 
[port_num/agg_num] 
SSID with Local Breakout 
To configure an SSID with a Local Breakout, configure the VLAN fields in the SSIDs application 
as shown in the example below. 
 
• 
Allow Local Breakout - Enables/Disables Local Breakout on the tunnel. If enabled, 
enter the Static Route(s) to be used for entering the Tunnel. All other traffic will go out 
through the local network. Make sure you have applied the relevant Data VPN Server to 
AP Groups in the SSID before choosing Data VPN Server as the Tunnel endpoint. To 
apply a Data VPN Server to an AP Group, go to the AP Groups page (Network - AP 
Registration - AP Group) and edit the Data VPN Setting for the group. Note that only one 
VLAN inside the tunnel (tunnel ID must be set to 0) can be enabled with Local Breakout.  
• 
Static Routes - Specify the static routes to be used for entering the tunnel. All other 
traffic will go out through the local network.  
• 
Avoid specifying static routes pertaining to the VLAN ID of the traffic that enters the 
Tunnel. For example, if VLAN ID = 41 is specified to be carried within the Tunnel and 
if the network subnet that corresponds to VLAN 41 is 192.168.41.0, the AP will 
automatically set up this route and make sure traffic destined for 192.168.41.0 will 
enter the Tunnel. The AP will automatically set up this route and make sure traffic 
with VLAN ID = 41 will enter the Tunnel. Do not specify an explicit Route with 
Destination = 192.168.41.0, as that will confuse the AP and lead to poor 
performance.

<<<PAGE 74>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
71 
Part No.  060958-00, Rev. A 
 
• 
The static routes specified will be accumulated on an AP across all SSIDs assigned 
to the AP. For example, if you have two SSIDs configured on the same AP and 
configure SSID1 to use Tunnel Profile T1 with Static Routes A and B, and configure 
SSID2 to use Tunnel Profile T2 with Static Routes C and D, all of the routes (A, B, C, 
and D) will be applicable for SSID 1 and SSID 2.   
• 
Across all of the routes applied on an AP from the different SSIDs, make sure any 
destination IP subnet is specified only once. Each route applied on an AP should be 
for a different IP subnet, even across the SSIDs. Also, avoid specifying static routes 
pertaining to the VLAN ID of the traffic that enters the tunnel. The AP will 
automatically set up such routes. If a route to IP subnet X already exists in an SSID 
and that SSID is applied to an AP, another route to the same IP subnet X must not 
be specified in the same or a different SSID that is applied to the same AP. 
Note: Local Breakout troubleshooting tips can be found in the Basic Troubleshooting 
Checklist. 
Creating a Tunnel Profile for 1201H Downlink Ports 
1.  Create a Tunnel Profile in Unified Access in OmniVista (Unified Access – Template - Tunnel 
Profile).  
 
2. Go to the Access Role Profile Screen (Unified Access – Template – Access Role), select the 
Tunnel Profile you created in Step 1, and apply the profile to the AP Group with Mapping 
method: “Map to VLAN and Tunnel”.

<<<PAGE 75>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
72 
Part No.  060958-00, Rev. A 
 
 
3. Create an Access Authentication Profile (Unified Access – Template – Access Auth Profile) 
and apply it to the AP (AP Group).  
Configuring an Access Auth Profile for an AP Downlink Port 
If you have a Premium or Business Account, you can assign an Access Auth Profile to a 
Downlink Port on Stellar AP1201H, AP1201HL, and AP1311 Devices. Profiles are 
displayed/configured on the OmniVista Access Auth Profile Screen (Unified Access – Unified 
Profile – Template – Access Auth Profile).  
1. Create a profile in the Access Auth Profile Table and click on the Apply to Devices button.  
2. On the Access Auth Profile Assignments Window (see below) click on the ADD/EDIT button 
next to AP Group and select an AP Group(s).  
3 When assigning the profile to an AP Group, you can select an Ethernet port(s) (up to 3 ports, 
depending on the AP model – Eth1, Eth2, Eth3). OmniVista will apply the profile to the selected 
ports on supported APs/ports in the AP Group and ignore unsupported APs/ports in the Group.

<<<PAGE 76>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
73 
Part No.  060958-00, Rev. A 
 
 
Add a Route to Reach the VPN VA from OmniVista 
 
1. On The Virtual Appliance Menu, select 2 – Configure the Virtual Appliance to bring up the 
Configure The Virtual Appliance Menu.

<<<PAGE 77>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
74 
Part No.  060958-00, Rev. A 
 
 
2. Select 8 – Configure Route.  
 
3. Select 3 – Add Route v4 to add the route. OmniVista should reach the NIC that the VPN VA 
used to connect to the corporate network (e.g., 10.255.255.0/24).  
 
4. Select 2 - Show Current Routes to review the configuration.

<<<PAGE 78>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
75 
Part No.  060958-00, Rev. A 
 
 
 
Using Dual Stack Lite ISP Connections with Stellar RAPs 
In the following network topology, the ISP router is using Dual Stack Lite (DS-Lite) technology: 
 
 
 
When configuring a RAP network that interacts with a DS-Lite router, the following general 
configuration guidelines are recommended: 
 
 
TCPMSS 
GRE 
WG 
WG + DS-Lite 
Management VPN Profile 
N/A 
1380 
1352 
Data VPN Profile 
N/A 
1380 
1300 
MTU 
GRE 
WG 
WG + DS-Lite 
Data VPN/GRE Tunneling 
1500 
1546 
1376 
 
The above values can be modified as follows: 
• 
Management VPN Profile TCPMSS – edit on the OV Cirrus Freemium VPN Servers 
screen. 
• 
Data VPN Profile TCPMSS – edit on the OV 2500/OV Cirrus Data VPN Servers screen 
(Network – AP Registration – Data VPN Server). 
• 
Data VPN/GRE Tunneling MTU – edit on the OV 2500/OV Cirrus SSIDs screen (WLAN – 
SSIDs).

<<<PAGE 79>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
76 
Part No.  060958-00, Rev. A 
 
Upgrading the VPN VA 
The sections below detail upgrading the VPN on VMware and Hyper-V. If you have configured a 
VPN for Remote Access APs, backup VPN Settings Files at the following directory:  
/opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile before upgrading. 
1. Deploy a new VPN VA 4.9.2.2. 
2. Select the port group for 3 Network Adapters same as the old VPN VA but all the statuses are 
disconnected. 
 
3. Configure all options on VPN VA, except the option VPN Endpoints 
a. Configure NICs 
b. Configure Routes 
c. Configure Network Settings (DNS, Gateway) 
d. Configure an SSH Service 
e. Configure the VPN Service 
4. Shutdown the old VPN VA 4.9.1 Build 3. 
5. Change the status of 3 Network Adapters to connected.

<<<PAGE 80>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
77 
Part No.  060958-00, Rev. A 
 
 
6. Import Backup VPN profile to the new VPN VA 4.9.2 Build 2 in the directory 
/opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile. 
7. Configure option VPN endpoints the same as the configuration of the old VPN VA. 
Notes:  
• 
The VPN VA upgrade process applies to VMware and Hyper-V. 
• 
The old VPN VA 4.9.1 Build 3 continues to run until step 4. 
• 
The RAP will be disconnected with the VPN VA from Step 4 to Step 7. The AP downtime 
happens in a short time ( ~ 5 minutes). 
• 
The default Hard Disk size is 8GB for RAP VPN VA 4.9.2.

<<<PAGE 81>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
78 
Part No.  060958-00, Rev. A 
 
Basic Troubleshooting Checklist 
• 
If the AP Management VPN Tunnel is down: 
• 
Check if tunnel interface was created using command “wg” on VPN VA (we assume 
we cannot action this command on RAP because it is not reachable). 
• 
Verify that the AP’s IP Address is present in the VPN.conf file imported to VPN-VA. 
• 
Verify that the firewall is not blocking traffic in both ways (from outside company, 
from VPN-VA). 
• 
If the AP Management VPN Tunnel is UP but AP is not registered in OV: 
• 
Check if you can ping the AP’s IP Address from OV. 
• 
Check if you have configured the static route on OV for AP wg0 IP subnets. 
• 
If AP Data VPN Tunnel is down: 
• 
Check if the tunnel interface was created by using command “wg” on VPN VA and on 
RAP. At this stage, the VPN config must be pushed to AP in 
/tmp/config/datavpn.conf. 
• 
Check the Data VPN Server is mapped to respective AP Group. 
• 
check if the AP has received IP on wg1 interface with command “ifconfig wg1”. 
• 
Check that the IP Address is present in the Data-VPN.conf file imported to VPN-VA. 
• 
Verify that the firewall is not blocking traffic in both ways (from outside company, 
from VPN-VA). 
• 
If both tunnels are UP but client does not get DHCP lease: 
• 
Check if the client is present in the AP association list with command “ssudo sta_list” 
and he mapped to the tunnel ID of the Data VPN Server, command “brctl show” 
could be action to have additional information (ath0x interface must be associated to 
br-g1 interface). 
• 
Check if the Client’s MAC Address is learnt on the corporate access switch where we 
bridge the traffic. 
• 
Check the switch config for DHCP replay (ip helper, dhcp-snooping). 
• 
If client is not able to access LAN network: 
• 
Client is not able to ping any device or gateway within same subnet. Make sure that 
Promiscuous Mode is enabled and set to “Accept” on the vswitch (by default this is 
set to reject). 
• 
Promiscuous Mode is enabled but it is not working. Check if the Override checkbox 
is disabled. If enabled ensure the setting is set to “Accept”. 
Useful Logs and Commands 
• 
Collect VPN VA logs from VA menu. 
• 
Collect RAP logs from OmniVista (OVE or OVC) -> Administration -> Audit -> Collect 
Support Info. 
• 
Check if RAP received DATA Management config files from OV Cirrus.

<<<PAGE 82>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
79 
Part No.  060958-00, Rev. A 
 
• 
cat /etc/config/rap.conf 
• 
Check if RAP received DATA VPN config files from OVE or OVC. 
• 
cat /var/config/datavpn.conf 
• 
Check the sta_list, wg show and ip -d link command outputs.  
 
For sta_list output, check the TUNNELID and FARENDIP of the VPN VA Server. 
STA_MAC                 IPv4             
IPv6                     
OnlineTime 
b0:72:bf:d0:63:de  172.28.1.51       fe80::8389:64ed:fbd4:e730    
  
8 
 
RX       TX        FREQ    AUTH    Final_role   VLANID  TUNNELID  FARENDIP 
4237     5860      5GHz  
PSK      __RAP3        0       
 0           DVPN-132 
 
For wg show check the public key, listening port, peer endpoint, allowed ips, the time 
since handshake and that transfer and received are incrementing. 
root@AP-D2:00_RAP2:~# wg show 
interface: wg0 
  public key: BOpBbWqvxFKEZ8gAVJACaVY4Lp5d6cKSK5y1+QH05i4= 
  private key: (hidden) 
  listening port: 58161 
 
peer: hfbchhiCJHOZz5UMh1BVbvDfWqRICpgwm7I1o6Jh1QI= 
  endpoint: 198.206.185.132:9093 
  allowed ips: 172.16.198.254/32, 172.20.0.155/32 
  latest handshake: 3 seconds ago 
  transfer: 267.09 KiB received, 625.22 KiB sent 
  persistent keepalive: every 5 seconds 
 
For ip -d link check that the interfaces gre0, gretap0, wg0 are present with an MTU 
lower than 1500. 
root@AP-D2:00_RAP2:~# ip -d link 
… 
gre0@NONE: <NOARP> mtu 1476 qdisc noop state DOWN mode DEFAULT group 
default 
    link/gre 0.0.0.0 brd 0.0.0.0 promiscuity 0 
    gre remote any local any ttl inherit nopmtudisc

<<<PAGE 83>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
80 
Part No.  060958-00, Rev. A 
 
gretap0@NONE: <BROADCAST,MULTICAST> mtu 1462 qdisc noop state DOWN 
mode DEFAULT group default qlen 1000 
    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff promiscuity 0 
    gretap remote any local any ttl inherit nopmtudisc 
 
wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state 
UNKNOWN mode DEFAULT group default 
    link/none  promiscuity 0 
    wireguard 
Local Breakout Troubleshooting 
The following scenarios may be encountered when enabling the Local Breakout function if 
certain configurations are incorrect.  
AP May Get Improper DNS Server IP Address 
Problem Description: After enabling Local Breakout, an AP will get an IP address from 
Corporate HQ, which also contains the DNS server IP. This DNS server IP will cause problems 
with the AP.  
Example: 
An AP powers up, gets its IP address and DNS Server IP address “A” from its local network, 
and registers with OVC. The AP gets the Data VPN configuration with Local Breakout enabled 
from OVC, and the AP gets its IP address and DNS Server IP address “B” from the Corporate 
HQ via data tunnel. 
At this moment, the AP has two DNS Server IP addresses - A and B. When the AP tries to 
access OVC'FQDN, it will randomly use DNS Server A or B. If DNS Server B cannot resolve 
OVC'FQDN, the AP will be down in OVC.   
Solution: 
Configure the correct Corporate HQ DNS Server.  
Client May Get Improper DNS Server IP Address 
Problem Description: After enabling Local breakout, a client will get its IP address from 
Corporate HQ which also contains a DNS Server IP address. The DNS Server IP may affect the 
client Internet access speed.  
Example 1: 
A client gets its IP address (e.g.,192.168.41.10/24) and DNS Server IP address (e.g., 
192.168.10.177/24 from Corporate HQ. The Local Breakout configuration contains route 
192.168.10.0/24. When a client attempts to access youtube.com, it first must send a DNS 
request, then then DNS request could be forwarded to Corporate HQ via tunnel. 
Example 2:  
A client gets its IP address (e.g., 192.168.41.10/24, and DNS Server IP address (e.g., 
192.168.10.177/24 from Corporate HQ. The Local Breakout configuration does not contain route 
192.168.10.0/24. When the client attempts to access youtube.com, it must first send a DNS

<<<PAGE 84>>>
OmniVista 4.9R2 Remote Access Point and VPN VA Installation Guide 
 
 
 
81 
Part No.  060958-00, Rev. A 
 
request to the AP's local network. If there is a DNS Server with IP 192.168.10.177 and it cannot 
be found, the client will fail to access the website.  
Example 3: 
A client gets its IP address (e.g., 92.168.41.10/24) and DNS Server IP address (e.g., 
219.141.136.10) from Corporate HQ.  
The DNS IP address is from a network operator in China. There are three network operators; 
and if your local network is from network operator A, the client can send a DNS request to the 
DNS Server belonging to network operator B, but it would be slow. 
If the client's local network is from network operator A, but it gets the DNS Server IP address 
belonging network operator B (assume that 219.141.136.10 belongs to network operator B), 
when the client attempts to access youtube.com or any other URL, it will be slow.  
Solution: 
Configure the correct DNS Server from Corporate HQ; the client needs to configure its DNS 
Server. 
AP May Disconnect with its Local Network 
Problem Description: After enabling Local breakout, the AP controls client traffic based on a 
static route configured with Local Breakout, but the AP traffic packet is also controlled by a static 
route. 
Example: 
The Local Breakout configuration contains route 192.168.10.0/24, but there is also subnet -  
192.168.10.0/24 within AP's local network. If the AP attempts to access to 192.168.10.100, 
which is contained in AP's local network, it will fail because the packet will be forward to the 
tunnel and sent to Corporate HQ. 
Solution: 
Caution must be taken when configuring the Local Breakout to avoid overlap with the AP’s local 
network.