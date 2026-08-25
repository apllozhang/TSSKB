<<<PAGE 1>>>
Release Notes 
                         Alcatel-Lucent Enterprise 
Part Number 033808-00 Rev. A 
                               Copyright © 2025 All rights reserved. 
 
 
Release Notes – Rev. A 
OmniSwitch 6360, 6465, 6560(E), 6570M, 6575, 
6860(E), 6860N, 6865, 6870, 6900, 6920, 9900 
Release 8.10R4 
 
These release notes accompany release 8.10R4. These release notes provide important information on 
individual software features and hardware modules. Since much of the information in these release notes is not 
included in the hardware and software user manuals, it is important that you read all sections of this document 
before installing new hardware or loading new software.  
Released in: December 2025 
 
Note: The OmniSwitch 6575 is referenced in the user documentation, but is not yet available. Availability is 
planned in the future.

<<<PAGE 2>>>
December 2025 
Page 2 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Contents 
Contents ........................................................................................................................... 2 
Related Documentation ......................................................................................................... 3 
System Specifications ........................................................................................................... 4 
[IMPORTANT] *MUST READ*: AOS Release 8.10R4 Prerequisites and Deployment Information ................. 15 
Licensed Features ............................................................................................................... 19 
New Hardware Support ........................................................................................................ 21 
8.10R4 New Feature and Enhancements ................................................................................... 23 
Open Problem Reports and Feature Exceptions .......................................................................... 41 
Hot-Swap/Redundancy Feature Guidelines ................................................................................ 47 
Technical Support ............................................................................................................... 50 
Appendix A: Feature Matrix ................................................................................................... 52 
Appendix B: MACsec Platform Support ..................................................................................... 62 
Appendix C: SPB L3 VPN-Lite Service-based (Inline Routing) / External Loopback Support / BVLAN 
Guidelines ........................................................................................................................ 64 
Appendix D: General Upgrade Requirements and Best Practices ..................................................... 67 
Appendix E: Standard Upgrade -  OmniSwitch Standalone or Virtual Chassis ...................................... 72 
Appendix F: ISSU – OmniSwitch Chassis or Virtual Chassis.............................................................. 74 
Appendix G: FPGA / U-boot Upgrade Procedure .......................................................................... 77 
Appendix H: CPLD/ONIE Upgrade Procedure for ONIE-Based Devices ................................................ 81 
Appendix I: Fixed Problem Reports ......................................................................................... 83 
Appendix J: Installing/Removing Packages .............................................................................. 101 
Appendix K: Fixed CVEs ..................................................................................................... 103 
Appendix L: Secure Boot Behavior Beginning in 8.10R4 .............................................................. 104

<<<PAGE 3>>>
December 2025 
Page 3 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Related Documentation 
These release notes should be used in conjunction with OmniSwitch AOS Release 8 User Guides. The following 
are the titles of the user guides that apply to this release.  
• 
OmniSwitch 6360 Hardware User Guide 
• 
OmniSwitch 6465 Hardware User Guide 
• 
OmniSwitch 6560 Hardware User Guide 
• 
OmniSwitch 6570M Hardware User Guide 
• 
OmniSwitch 6575 Hardware User Guide 
• 
OmniSwitch 6860 Hardware User Guide 
• 
OmniSwitch 6865 Hardware User Guide 
• 
OmniSwitch 6870 Hardware User Guide 
• 
OmniSwitch 6900 Hardware User Guide 
• 
OmniSwitch 9900 Hardware User Guide 
• 
OmniSwitch AOS Release 8 CLI Reference Guide  
• 
OmniSwitch AOS Release 8 Network Configuration Guide  
• 
OmniSwitch AOS Release 8 Switch Management Guide  
• 
OmniSwitch AOS Release 8 Advanced Routing Configuration Guide  
• 
OmniSwitch AOS Release 8 Specifications Guide 
• 
OmniSwitch AOS Release 8 Transceivers Guide

<<<PAGE 4>>>
December 2025 
Page 4 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
System Specifications 
Memory Specifications 
The following are the standard shipped memory configurations. Configuration files and the compressed 
software images—including web management software (WebView) images—are stored in the flash memory. 
Platform 
SDRAM 
Flash 
OS6360 
1GB 
1GB 
OS6465 
1GB 
1GB 
OS6560(E) 
2GB 
2GB 
OS6560-24X4/P24X4 
1GB 
1GB 
OS6570M 
2GB 
8GB 
OS6575 
2GB 
4GB 
OS6860(E) 
2GB 
2GB 
OS6860N 
4GB 
16GB 
OS6865 
2GB 
2GB 
OS6870 
8GB 
32GB 
OS6900-V72/C32 
16GB 
16GB 
OS6900-X48C6/T48C6/X48C4E/T24C2/X24C2 
8GB 
32GB1 
OS6900-V48C8/C32E 
16GB2 
64GB1 
OS6920 
32GB 
64GB 
OS9900 
16GB 
2GB 
1. 
Size of physical memory. Partitioned to 16GB flash memory.  
2. 
Previous release notes incorrectly listed 8GB.  
Bootloader and FPGA Specifications 
The software versions listed below are the MINIMUM required, except where otherwise noted. Switches running 
the minimum versions, as listed below, do not require any U-Boot or FPGA upgrades but it's recommended to 
upgrade to the current version to address any known issues. Use the ‘show hardware-info’ command to 
determine the current versions.  
Switches not running the minimum version required should upgrade to the latest U-Boot or FPGA that is 
available with this AOS release software available from Service & Support.  
Please refer to the Upgrade Instructions section at the end of these Release Notes for step-by-step instructions 
on upgrading your switch. 
OmniSwitch 6360 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
OS6360-10 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
0.11 
0.11 
0.125

<<<PAGE 5>>>
December 2025 
Page 5 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
8.10.114.R027 
8.10.37.R048 
OS6360-P10 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.11 
0.11 
0.125 
OS6360-P10A 
(904324-90) 
8.8.2.R03 
8.8.2.R03 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.1 
0.1 
0.25 
OS6360-24 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.15 
0.171 
0.203 
OS6360-P24 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.15 
0.171 
0.203 
OS6360-P24X 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.12 
0.12 
0.135 
OS6360-PH24 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.12 
0.12 
0.135 
OS6360-48 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.15 
0.171 
0.203 
OS6360-P48 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
0.15 
0.171 
0.203

<<<PAGE 6>>>
December 2025 
Page 6 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
8.10.114.R027 
8.10.37.R048 
OS6360-P48X 
8.7.149.R02 
8.7.30.R032 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.12 
0.12 
0.135 
OS6360-PH48 
8.8.114.R01 
8.8.114.R01 
8.9.85.R024 
8.10.115.R016 
8.10.42.R026 
8.10.114.R027 
8.10.37.R048 
0.12 
0.12 
0.135 
1. FPGA version 0.17 is REQUIRED to address issues CRAOS8X-26370 and CRAOS8X-25033. 
2. Optional U-boot update for CRAOS8X-24464, ability to disable/authenticate U-boot access. 
3. Optional FPGA update for reduced fan speed at boot up. 
4. Highly recommended to address NAND flash corruption issue CRAOS8X-35470. Also adds support for Gowin 
CPLD. 
5. For switches currently shipping from the factory. No upgrade required for existing switches. 
6. Addresses multiple power cycle issues. See FPGA / U-boot Upgrade Procedure.  
7. U-boot version 8.10.114.R02 is mandatory to address CRAOS8X-50729. 
8. Required U-boot upgrade for Secure Boot image support. 
OmniSwitch 6465 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
OS6465-P6 
8.5.83.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.9.85.R025 
8.10.115.R016 
8.10.42.R026 
8.10.37.R047 
0.10 
0.12 
OS6465-P12 
8.5.83.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.9.85.R025 
8.10.115.R016 
8.10.42.R026 
8.10.37.R047 
0.10 
0.12 
OS6465-P28 
8.5.89.R02 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.9.85.R025 
8.10.115.R016 
8.10.42.R026 
8.10.37.R047 
0.5 
0.71

<<<PAGE 7>>>
December 2025 
Page 7 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
OS6465T-12 
8.6.117.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.9.85.R025 
8.10.115.R016 
8.10.42.R026 
8.10.37.R047 
0.4 
0.4 
OS6465T-P12 
8.6.117.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.9.85.R025 
8.10.115.R016 
8.10.42.R026 
8.10.37.R047 
0.4 
0.4 
OS6465-P12  
(ENH-240) 
8.8.33.R01 
8.8.33.R01 
8.9.85.R025 
8.10.115.R016 
8.10.42.R026 
8.10.37.R047 
0.5 
0.5 
1. FPGA version 0.7 is optional to address issue CRAOS8X-12042. 
2. U-boot 8.7.2.R02 is optional to address UBIFS error issues CRAOS8X-4813/13440. 
3. Optional U-boot update for CRAOS8X-24464, ability to disable/authenticate U-boot access. 
4. Optional U-boot update to support boot from USB feature. 
5. Highly recommended to address the NAND flash corruption issue CRAOS8X-35470. 
6. Addresses multiple power cycle issues. See FPGA / U-boot Upgrade Procedure. 
7. Required U-boot upgrade for Secure Boot image support. 
OmniSwitch 6560 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot 
Current  
U-Boot 
Minimum  
FPGA 
Current  
FPGA 
OS6560-24Z24 
8.5.22.R01 
8.7.2.R023 
8.7.30.R037 
8.9.85.R029 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.7 
0.85 
0.99 
OS6560-P24Z24 
8.4.1.23.R02 
8.7.2.R023 
8.7.30.R037 
8.9.85.R029 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.6 
0.71 
0.85 
0.99 
OS6560-24Z8 
8.5.22.R01 
8.7.2.R023 
8.7.30.R037 
8.9.85.R029 
8.10.115.R0110 
8.10.37.R0412 
0.7 
0.85 
0.99

<<<PAGE 8>>>
December 2025 
Page 8 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum  
U-Boot 
Current  
U-Boot 
Minimum  
FPGA 
Current  
FPGA 
OS6560-P24Z8 
8.4.1.23.R02 
8.7.2.R023 
8.7.30.R037 
8.9.85.R029 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.6 
0.71 
0.85 
0.99 
OS6560-24X4 
8.5.89.R02 
8.7.2.R024 
8.7.30.R037 
8.9.85.R028 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.4 
0.4 
OS6560-P24X4 
8.5.89.R02 
8.7.2.R024 
8.7.30.R037 
8.9.85.R028 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.4 
0.4 
OS6560-P48Z16 
(903954-90) 
8.4.1.23.R02 
8.7.2.R023 
8.7.30.R037 
8.9.85.R029 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.6 
0.71 
0.85 
0.99 
OS6560-P48Z16 
(all other PNs) 
8.5.97.R04 
8.7.2.R023 
8.7.30.R037 
8.9.85.R029 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.3 
0.62 
0.76 
OS6560-48X4 
8.5.97.R04 
8.7.2.R024 
8.7.30.R037 
8.9.85.R028 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.4 
0.72 
0.86 
OS6560-P48X4 
8.5.97.R04 
8.7.2.R024 
8.7.30.R037 
8.9.85.R028 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.4 
0.72 
0.86 
OS6560-X10 
8.5.97.R04 
8.7.2.R024 
8.7.30.R037 
8.9.85.R028 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.5 
0.82 
0.911

<<<PAGE 9>>>
December 2025 
Page 9 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum  
U-Boot 
Current  
U-Boot 
Minimum  
FPGA 
Current  
FPGA 
OS6560E-P24Z8 
8.9.85.R02 
8.9.85.R02 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.9 
0.9 
OS6560E-P48Z16 
8.9.85.R02 
8.9.85.R02 
8.10.115.R0110 
8.10.42.R0210 
8.10.37.R0412 
0.7 
0.7 
1. FPGA version 0.7 is optional to address issue CRAOS8X-7207. 
2. FPGA versions are optional to address issue CRAOS8X-16452. 
3. U-boot 8.7.2.R02 is optional to address eUSB issue CRAOS8X-13819.  
4. U-boot 8.7.2.R02 is optional to address UBIFS error issues CRAOS8X-4813/13440. 
5. FPGA version 0.8 is optional to address issue CRAOS8X-22857. 
6. FPGA versions 0.7 and 0.8 are optional to support 1588v2.  
7. Optional U-boot update for CRAOS8X-24464, ability to disable/authenticate U-boot access. 
8. Highly recommended to address the NAND flash corruption issue CRAOS8X-35470. 
9. Ships from factory. No upgrade required, there are no functional changes in this U-boot version for these 
models. 
10. Addresses multiple power cycle issues.  
11. FPGA version 0.9 is optional to address issue CRAOS8X-15666. 
12. Required U-boot upgrade for Secure Boot image support. 
 
OmniSwitch 6570M – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
OS6570M-12 
8.9.25.R02 
8.9.25.R02 
8.9.92.R021 
8.9.139.R033 
8.9.70.R044 
8.10.115.R015 
8.10.42.R025 
8.10.37.R046 
0.11 
0.11 
OS6570M-12D 
8.9.25.R02 
8.9.25.R02 
8.9.92.R021 
8.9.139.R033 
8.9.70.R044 
8.10.115.R015 
8.10.42.R025 
8.10.37.R046 
0.11 
0.11 
OS6570M-U28 
8.9.25.R02 
8.9.25.R02 
8.9.92.R021 
8.9.139.R033 
8.9.70.R044 
8.10.115.R015 
8.10.42.R025 
8.10.37.R046 
0.11 
0.11 
0.122 
1. Adds support for Gowin CPLD. 
2. Addresses power supply interrupt issue. 
3. Addresses CRAOS8X-40924 for disabling U-boot access. 
4. Adds support for signed AOS images.

<<<PAGE 10>>>
December 2025 
Page 10 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
5. Addresses multiple power cycle issues.  
6. Required U-boot upgrade for Secure Boot image support. 
 
OmniSwitch 6575 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot  
Current  
U-Boot  
Minimum  
FPGA 
Current  
FPGA 
OS6575-P12 
8.10.37.R04 
8.10.37.R04 
11.0 
11.0 
OS6575-U28 
8.10.37.R04 
8.10.37.R04 
11.0 
11.0 
OS6575M-MP16 
8.10.37.R04 
8.10.37.R04 
5.0 
5.0 
 
OmniSwitch 6860(E) – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot 
Current  
U-Boot 
Minimum  
FPGA 
Current  
FPGA 
OS6860/OS6860E 
(except U28/P24Z8) 
8.1.1.70.R01 
8.7.30.R032 
8.10.115.R013 
8.10.42.R023 
0.9  
0.101 
OS6860E-U28 
8.1.1.70.R01 
8.7.30.R032 
8.10.115.R013 
8.10.42.R023 
0.20 
0.20 
OS6860E-P24Z8 
8.4.1.17.R01 
8.7.30.R032 
8.10.115.R013 
8.10.42.R023 
0.5  
0.71 
1. FPGA versions .7 and .10 are optional on the PoE models for the fast and perpetual PoE feature support. 
2. Optional U-boot update for CRAOS8X-24464, ability to disable/authenticate U-boot access. 
3. Addresses multiple power cycle issues.  
 
OmniSwitch 6860N – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum 
ONIE 
Current  
ONIE 
Minimum  
CPLD 
Current  
CPLD 
OS6860N-U28 
2019.05.00.10 
2019.05.00.11 
12 
12 
OS6860N-P48Z 
2019.05.00.10 
2019.05.00.11 
12 
131 
OS6860N-P48M 
2019.05.00.10 
2019.05.00.11 
11 
121 
O6860N-P24M 
2019.05.00.11 
2019.05.00.11 
2 
31 
OS6860N-P24Z 
2019.05.00.11 
2019.05.00.11 
2 
31 
1. 
Addresses CRAOS8X-29731/30471 – OS6860N power supply issue. 
Note: These models use the Uosn.img image file.

<<<PAGE 11>>>
December 2025 
Page 11 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
OmniSwitch 6865 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
U-Boot 
Current  
U-Boot 
Minimum  
FPGA 
Current  
FPGA 
OS6865-P16X 
8.3.1.125.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.10.115.R015 
8.10.42.R025 
0.20 
0.251 
OS6865-U12X 
8.4.1.17.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.10.115.R015 
8.10.42.R025 
0.23 
0.251 
OS6865-U28X 
8.4.1.17.R01 
8.7.2.R022 
8.7.30.R033 
8.8.33.R014 
8.10.115.R015 
8.10.42.R025 
0.11 
0.141 
1. FPGA versions 0.25 and 0.14 are optional for the fast and perpetual PoE feature support. 
2. U-boot 8.7.2.R02 is optional to address eUSB issue CRAOS8X-13819. 
3. Optional U-boot update for CRAOS8X-24464, ability to disable/authenticate U-boot access. 
4. Optional U-boot update to support boot from USB feature. 
5. Addresses multiple power cycle issues.  
Note: CRAOS8X-4150 for the OS6865-U28X was fixed with FPGA version 0.12 and higher.  
OmniSwitch 6870 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum  
ONIE 
Current  
ONIE 
Minimum  
CPLD 
Current  
CPLD 
OS6870-24 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.09 
CPLD (LED) - 0.08 
CPLD (CPU) - 0.04 
CPLD - 0.09 
CPLD (LED) - 0.08 
CPLD (CPU) - 0.04 
OS6870-P24M 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.09 
CPLD (LED) - 0.07 
CPLD (CPU) - 0.04 
CPLD - 0.09 
CPLD (LED) - 0.07 
CPLD (CPU) - 0.04 
OS6870-P24Z 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.07 
CPLD (LED) - 0.06 
CPLD (CPU) - 0.04 
CPLD - 0.07 
CPLD (LED) - 0.06 
CPLD (CPU) - 0.04 
OS6870-48 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.09 
CPLD (LED) - 0.08 
CPLD (CPU) - 0.04 
CPLD - 0.09 
CPLD (LED) - 0.08 
CPLD (CPU) - 0.04 
OS6870-P48M 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.11 
CPLD (LED) - 0.09 
CPLD (CPU) - 0.04 
CPLD - 0.011 
CPLD (LED) - 0.09 
CPLD (CPU) - 0.04 
OS6870-P48Z 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.07 
CPLD (LED) - 0.06 
CPLD (CPU) - 0.04 
CPLD - 0.07 
CPLD (LED) - 0.06 
CPLD (CPU) - 0.04 
OS6870-V12 
2019.05.00.12 
 
2019.05.00.12 
 
CPLD - 0.10 
CPLD (LED) - 0.07 
CPLD (CPU) - 0.04 
CPLD - 0.10 
CPLD (LED) - 0.07 
CPLD (CPU) - 0.04

<<<PAGE 12>>>
December 2025 
Page 12 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
OmniSwitch 6900 - AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum 
ONIE 
Current  
ONIE 
Minimum 
CPLD 
Current  
CPLD 
OS6900-V72 
2017.08.00.01 
2017.08.00.01 
CPLD 1 – 5 
CPLD 2 - 6  
CPLD 3 – 8 
CPLD 1 – 5 
CPLD 2 - 6  
CPLD 3 – 8 
OS6900-C32 
2016.08.00.03 
2018.11.00.02 
CPLD 1 – 10 
CPLD 2 – 11 
CPLD 3 – 11 
CPLD 1 – 10 
CPLD 2 – 11 
CPLD 3 – 11 
OS6900-C32E 
2020.02.00.01 
2020.02.00.01 
CPLD 1 – 13 
CPLD 2 – 9 
CPLD 3 – 9 
CPLD 1 – 15 
CPLD 2 – 9 
CPLD 3 – 9 
OS6900-X48C6 
2019.08.00.01 
2019.08.00.01 
CPLD 1 – 2 
CPLD 2 - 2 
CPLD 3 – 2 
CPU CPLD – N/A 
CPLD 1 – 3 
CPLD 2 - 2 
CPLD 3 – 2 
CPU CPLD – 2.141 
OS6900-T48C6 
2019.08.00.01 
2019.08.00.01 
CPLD 1 – 2 
CPLD 2 – 2 
CPLD 3 – 4 
CPU CPLD – N/A  
CPLD 1 – 3 
CPLD 2 – 2 
CPLD 3 – 4 
CPU CPLD – 2.141 
OS6900-X48C4E 
2019.05.00.10 
2019.05.00.10 
CPLD 1 – 3  
CPLD 2 - 2 
CPLD 3 – 3 
CPU CPLD – N/A 
CPLD 1 – 3 
CPLD 2 - 2 
CPLD 3 – 3 
CPU CPLD – 2.141 
CPU CPLD – 2.152 
OS6900-V48C8 
2020.02.00.01 
2020.02.00.01 
CPLD 1 – 2  
CPLD 2 - 3 
CPLD 3 – 2 
CPLD 1 – 3 
CPLD 2 - 4 
CPLD 3 – 3 
OS6900-T24C2 
2019.08.00.03 
2019.08.00.03 
CPLD 1 - 2.0 
CPLD 2 - 2.0 
CPLD CPU - 6.0 
CPLD 1 - 2.0 
CPLD 2 - 2.0 
CPLD CPU - 6.0 
OS6900-X24C2 
2019.08.00.03 
2019.08.00.03 
CPLD 1 - 6.0 
CPLD 2 - 6.0 
CPLD CPU - 6.0 
CPLD 1 - 6.0 
CPLD 2 - 6.0 
CPLD CPU - 6.0 
1. Optional CPU CPLD update to address CRAOS8X-30098. 
2. Required CPLD update to address CRAOS8X-43968 (Hardware revision 6 only). 
 
OmniSwitch 6920 - AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum 
ONIE 
Current  
ONIE 
Minimum 
CPLD 
Current  
CPLD 
OS6900-D32 
2018.11.00.02 
2018.11.00.02 
CPLD1 - 3.4 
CPLD2 - 3.5 
CPLD3 - 3.5 
 
CPLD1 - 3.4 
CPLD2 - 3.5 
CPLD3 - 3.5

<<<PAGE 13>>>
December 2025 
Page 13 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
OmniSwitch 9900 – AOS Release 8.10.86.R04 (GA) 
Hardware 
Minimum 
Coreboot-
Uboot 
Current 
Coreboot-
Uboot 
Minimun 
Control 
FPGA 
Current 
Control 
FPGA 
Minimum/ 
Current 
Power FPGA 
OS99-CMM 
8.3.1.103.R01 
8.3.1.103.R01 
8.7.30.R031 
8.8.152.R01 
2.3.0 
2.3.0 
0.8 
 
OS99-CMM2 
8.9.183.R03 
8.9.183.R03 
1.4.0 
1.4.0 
1.2.0 
OS9907-CFM 
- 
- 
- 
- 
- 
OS9907-CFM2 
- 
- 
- 
- 
- 
OS9912-CFM 
- 
- 
- 
- 
- 
OS99-GNI-48 
8.3.1.103.R01 
8.3.1.103.R01 
8.8.152.R012 
1.2.4 
 
1.2.4 
1.2.52 
0.9 
OS99-GNI-P48 
8.3.1.103.R01 
8.3.1.103.R01 
8.8.152.R012 
1.2.4 
 
1.2.4 
1.2.52 
0.9 
OS99-XNI-48  
(903753-90) 
8.3.1.103.R01 
8.3.1.103.R01 
8.8.152.R012 
1.3.0 
1.3.0 
1.5.02 
0.6 
OS99-XNI-48 
8.6.261.R01 
8.6.261.R01 
8.8.152.R012 
1.4.0 
1.4.0 
1.5.02 
0.7 
OS99-XNI-U48 
(903723-90) 
8.3.1.103.R01 
8.3.1.103.R01 
8.8.152.R012 
2.9.0 
2.9.0 
2.11.02 
0.8 
OS99-XNI-U48 
8.6.261.R01 
8.6.261.R01 
8.8.152.R012 
2.10.0 
2.10.0 
2.11.02 
2.12.03 
0.8 
OS99-GNI-U48 
8.4.1.166.R01 
8.4.1.166.R01 
8.8.152.R012 
1.6.0 
1.6.0 
1.7.02 
1.8.03 
0.2 
OS99-CNI-U8 
8.4.1.20.R03 
8.4.1.20.R03 
8.8.152.R012 
1.7 
1.7 
1.92 
1.103 
N/A 
OS99-XNI-P48Z164 
8.4.1.20.R03 
8.4.1.20.R03 
8.8.152.R012 
1.4 
1.4 
1.62 
0.7 
OS99-XNI-U24 
8.5.76.R04 
8.6.261.R01 
8.8.152.R012 
1.0  
2.9.0 
2.11.02 
2.12.03 
0.8 
OS99-XNI-P24Z84 
8.5.76.R04 
8.6.261.R01 
8.8.152.R012 
1.1  
1.4.0 
1.6.02 
0.7 
OS99-XNI-U12Q4 
8.6.117.R01 
8.6.117.R01 
8.8.152.R012 
1.6.0 
1.5.0 
1.6.02 
N/A 
OS99-XNI-UP24Q24 
8.6.117.R01 
8.6.117.R01 
8.8.152.R012 
1.5.0 
1.5.0 
1.6.02 
N/A 
OS99-CNI-U20 
8.9.183.R03 
8.9.183.R03 
1.2.0 
1.2.0 
0.4 
1. 
Optional U-boot update for CRAOS8X-24464, ability to disable/authenticate U-boot access.

<<<PAGE 14>>>
December 2025 
Page 14 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Hardware 
Minimum 
Coreboot-
Uboot 
Current 
Coreboot-
Uboot 
Minimun 
Control 
FPGA 
Current 
Control 
FPGA 
Minimum/ 
Current 
Power FPGA 
2. 
Optional U-boot/FPGA update for CMM2 and OS9912 compatibility. 
3. 
Optional FPGA upgrade to address CRAOS8X-43592: 1G/10G SFP not recognized. 
4. 
Not currently supported in an OS9912 chassis. 
 
Note: Existing OS9900 NIs that are to be used with a CMM2 or in an OS9912 chassis must first have the Uboot and 
FPGA upgraded before using them with a CMM2 or inserting them into an OS9912 chassis. See footnote #2.

<<<PAGE 15>>>
December 2025 
Page 15 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
[IMPORTANT] *MUST READ*: AOS Release 8.10R4 Prerequisites and Deployment 
Information 
 
General Information 
• 
Early availability features are available in AOS and can be configured. However, they have not gone 
through the complete AOS validation cycle and are therefore not officially supported. 
• 
Please refer to the Feature Matrix in Appendix A for detailed information on supported features for 
each platform.  
• 
Prior to upgrading please refer to Appendix D for important best practices, prerequisites, and step-by-
step instructions.  
• 
Some switches may ship from the factory with a diag.img file. This file is for internal switch diagnostic 
purposes only and can be safely removed.  
 
• 
Switches that ship from the factory will have the Running Configuration set to the /flash/working 
directory upon the first boot up. By default, the automatic VC feature will run and the vcboot.cfg and 
vcsetup.cfg files will be created in the /flash/working directory but not in the /flash/certified 
directory which results in the Running Configuration not being certified. This will result in the Running 
Configuration being set to the /flash/certified directory on the next reboot. Additionally, on the next 
reboot the switch will no longer be in the factory default mode and will have a chassis-id of 1 which 
could cause a duplicate chassis-id issue if the switch is part of a VC. To set the switch back to the 
factory defaults on the next reboot perform the following use the reset-fo-factory command.    
 
• 
The OS6560-P48Z16 (903954-90) supports link aggregation only on the 1G/2.5G multigig and 10G ports 
(33-52). The 1G ports (ports 1-32) do not support link aggregation (CRAOSX-1766). Linkagg 
configuration on unsupported ports in 85R1/841R03 config file will be removed internally from software 
during upgrade reboot. Oversized frames will not be dropped on ingress of ports 1-32 (CRAOS8X-20939).  
 
Note: OS6560-P48Z16 (all other PNs) - This is a new version of the OS6560-P48Z16 which does not have 
 
the limitations mentioned above. The model number (OS6560-P48Z16) remains the same for both 
 
versions, only the part number can be used to differentiate between the versions. 
• 
Improved Convergence Performance 
Faster convergence times can be achieved on models with SFP, SFP+, QSFP+, and QSFP28 ports with 
fiber transceivers.   
 
 
Exceptions:  
• 
Copper ports or ports with copper transceivers do not support faster convergence. 
• 
OS6865-P16X and OS6865-U12X ports 3 and 4 do not support faster convergence. 
• 
VFL ports do not support faster convergence.  
• 
Splitter ports (i.e. 4X10G or 4X25G) do not support faster convergence. 
• 
OS6570M-12/12D ports 9 and 10 do not support fast convergence. 
 
• 
MACsec Licensing Requirement 
Beginning in 8.6R1 the MACsec feature requires a site license, this license can be generated free of 
cost. After upgrading, the feature will be disabled until a license is installed. There is no reboot 
required after applying the license.

<<<PAGE 16>>>
December 2025 
Page 16 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
• 
SHA-1 Algorithm - Chosen-prefix attacks against the SHA-1 algorithm are becoming easier for an 
attacker1. For this reason, we have disabled the "ssh-rsa" public key signature algorithm by default. The 
better alternatives include: 
 
• 
The RFC8332 RSA SHA-2 signature algorithms rsa-sha2-256/512. These algorithms have the 
advantage of using the same key type as "ssh-rsa" but use the safer SHA-2 hash algorithms. 
RSA SHA-2 is enabled in AOS. 
• 
The RFC5656 ECDSA algorithms: ecdsa-sha2-nistp256/384/521. These algorithms are 
supported in AOS by default. 
 
 
To check whether a server is using the weak ssh-rsa public key algorithm, for host authentication, try 
 
to connect to it after disabling the ssh-rsa algorithm from ssh(1)'s allowed list using the command 
 
below:  
         -> ssh strong-hmacs enable 
 
 
If the host key verification fails and no other supported host key types are available, the server 
 
software on that host should be upgraded. 
 
 
1. "SHA-1 is a Shambles: First Chosen-Prefix Collision on SHA-1 and Application to the PGP Web of 
 
Trust" Leurent, G and Peyrin, T (2020) https://eprint.iacr.org/2020/014.pdf  
 
• 
With the continuous goal of preserving the environment in addition to the AOS software being 
preloaded on the switch and available on the Business Portal, we have begun removing the software 
access card previously included in the switch ship kit. For additional information or if in need of special 
assistance, please contact Service & Support.  
 
Deprecated Features / Functionality Changes 
The following table lists deprecated features and key functionality changes by release.  
 
AOS Release 8.5R4 
EVB - Beginning in 8.5R4, support for EVB is being removed. Any switches with an EVB configuration cannot 
be upgraded to 8.5R4 or above. 
NTP - Beginning with AOS Release 8.5R4, OmniSwitches will not synchronize with an unsynchronized NTP 
server (stratum 16), as per the RFC standard. Existing installations where OmniSwitches are synchronizing 
from another OmniSwitch, or any other NTP server which is not synchronized with a valid NTP server, will 
not be able to synchronize their clocks. The following NTP commands have been deprecated:  
- 
ntp server synchronized 
- 
ntp server unsynchronized 
 
AOS Release 8.6R1 
DHCPv6 Guard - Configuration via an IPv6 interface name is deprecated in 8.6.R1.  Commands entered 
using the CLI must use the new 'ipv6 dhcp guard vlan vlan-id’ format of the command.  The old format will 
still be accepted if present in a vcboot.cfg to preserve backwards compatibility. 
IP Helper - The 'ip helper' commands have been deprecated in 8.6R1 and replaced with 'ip dhcp relay'. The 
old format will still be accepted if present in a vcboot.cfg to preserve backwards compatibility. 
SAA - The vlan-priority and drop-eligible parameters have been deprecated from all SAA commands 
beginning in 8.6R1. 
MACsec is now supported on ports 33-48 of the 6560-(P)48X4. CRAOS8X-7910 was resolved in 8.6R1. 
 
AOS Release 8.6R2 
Distributed ARP - Beginning 8.6R2 distributed ARP is no longer supported.  
WRED - Beginning in 8.6R2 WRED is no longer supported. 
QoS - Beginning in 8.6R2 the 'qos dscp-table' command is no longer supported.

<<<PAGE 17>>>
December 2025 
Page 17 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
NTP - The ntp parameter for the 'ip service source-ip' command was deprecated in 8.5R4. Support has been 
added back in 8.6R2. 
 
AOS Release 8.7R1 
MACsec - Static mode is not supported on OS6860N. 
Transceivers - Beginning in AOS release 8.7R1 an error message will be displayed when the unsupported 
QSFP-4X25G-C transceiver is inserted on an OS99-CNI-U8 module. 
SPB - Beginning in 8.7.R01 the default number of BVLANs created via Auto Fabric is reduced from 16 to 4. 
This new default value is only applicable to factory default switches running 8.7R1 with no vcboot.cfg file. 
Upgrading to 8.7.R1 will not change the number of configured BVLANs in an existing configuration. See 
Appendix C for additional information. 
AOS Release 8.7R2 
There are new default user password polices being implemented in 8.7R2. This change does not affect 
existing users.  
- cannot-contain-username: enable 
- min-uppercase: 1 
- min-lowercase: 1 
- min-digit: 1 
- min-nonalpha: 1 
The OmniSwitch 6360 does not contain a real-time clock. 
- It is recommended to use NTP to ensure time synchronization on OS6360s. 
- When the switch is reset, the switch will boot up from an approximation of the last known good time. 
- When the switch is powered off it cannot detect the time left in the powered off state. When it boots up 
it will have the same time as when the switch was last powered off. 
AOS Release 8.7R3 
The Kerberos Snooping is not supported in bridge mode in this release. 
AOS Release 8.8R1 
Unsupported commands (Part of AOS 88R1 but not supported) 
- 
mrp interconnect 
- 
show mrp interconnect 
- 
clear mrp interconnect 
A software check was added in AOS releases 8.7R1, 8.7R2, and 8.7R3 restricting the use of the affected 
power supplies below while awaiting certification on the OS6560. This check was removed in 8.8R1 after 
the power supplies were certified resulting in the minimum AOS version 8.8R1 requirement.     
OS6560-BP-PH - This OS6560 600W power supply, OS6560-BP-PH (904072-90), requires a minimum AOS 
version of 8.8R1. 
OS6560-BP-PX - This OS6560 920W power supply, OS6560-BP-BX (904073-90), requires a minimum AOS 
version of 8.8R1. 
Refer to the OmniSwitch 6560 Hardware Guide for additional power supply information. 
AOS Release 8.8R2 
The French language support is being removed from WebView to help reduce package size. If the default 
language is French it will default to English after upgrade. 
AOS Release 8.9R1 
Metro License Features – Some Metro features are now licensed on the OS6560 beginning in 8.9R1. See 
Metro License for information on re-enabling them after upgrading to 8.9R1.  
AOS Release 8.9R4 
OmniSwitch 6570 signed AOS image support with proper u-boot was added. 
AOS Release 8.10R1 
CRAOS8X-46556 (CVE-2024-6387) fix has been implemented by default in 8.10R1. See Appendix K: Fixed 
CVEs. 
AOS Release 8.10R2 
- Support for OVSDB removed.

<<<PAGE 18>>>
December 2025 
Page 18 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
- The administrative state for the automatic fabric feature is disabled by default. 
 
- The U-boot version on the OS6570M models shipping from the factory is 8.10.42.R02. This U-boot version 
supports signed AOS images only (8.9R4 and above). To use AOS releases prior to 8.9R4 the u-boot version 
must first be downgraded to a version below 8.9.70.R04 before downgrading AOS. 
AOS Release 8.10R3 
Starting with release 8.10R3, it is mandatory to configure VXLAN BGP EVPN services and associated 
configurations within the VRF context. Therefore, after upgrading to 8.10R3, any existing EVPN 
configurations from earlier releases must be manually reconfigured under the appropriate VRF context. 
See EVPN - VRF-based Tenancy Model for AOS EVPN Services. 
AOS Release 8.10R4 
Beginning in 8.10R4 users using the 'admin' account with the default 'switch' password will be required to 
change the password. Any REST APIs or scripts must be modified to account for the required password 
change. See Change Password on First Access. 
Beginning in 8.10R4 a password will need to be set to access the su prompt. 
Secure Boot is being introduced in 8.10R4. This will require a U-boot upgrade on the OS6360, OS6465, 
OS6570 and OS6570 platforms prior to upgrading to AOS 8.10R4. See Secure Boot for more information.

<<<PAGE 19>>>
December 2025 
Page 19 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Licensed Features 
The table below lists the CAPEX licensed features in this release and whether or not a license is required for 
the various models. Refer to the licensing portal.  
 
Data Center License Required 
OmniSwitch 
Licensed Features 
DCB (PFC,ETS,DCBx) 
Not Supported 
FIP Snooping 
Not Supported 
FCoE VxLAN 
Not Supported 
 
 
 
Feature/Performance License Required 
 
OS6360 
OS6465 
OS6560 
OS6570M 
OS6860 
OS6860N 
OS6870 
OS6900 
OS9900 
Licensed Features 
 
 
 
MACsec (OS-SW-MACSEC) 
N/A 
Yes 
Yes 
Yes 
Yes 
Yes 
Yes 
Yes3 
Yes 
10G Support (OS6560-SW-PERF) 
N/A 
N/A 
Yes1 
N/A 
N/A 
N/A 
N/A 
N/A 
N/A 
10G Support (OS6360-SW-PERF) 
Yes2 
N/A 
N/A 
N/A 
N/A 
N/A 
N/A 
N/A 
N/A 
10G Support (OS6570-SW-PERF4) 
N/A 
N/A 
N/A 
Yes4 
N/A 
N/A 
N/A 
N/A 
N/A 
MPLS Support (OS####-MPLS-#) 
N/A 
N/A 
N/A 
N/A 
N/A 
Yes 
N/A 
Yes 
N/A 
50G Support (OS6870-SW-PERF) 
N/A 
N/A 
N/A 
N/A 
N/A 
N/A 
Yes5 
N/A 
N/A 
1. Performance software license is optional allowing ports 25/26 (OS6560-24X4/P24X4) and ports 49/50 (OS6560-48X4/P48X4) to 
operate at 10G speed. Ports support 1G by default. 
2. Performance software license is optional allowing the 2 RJ45/SFP+ combo ports (25/26 or 49/50) of the OS6360-PH24 or 
OS6360-PH48 models to operate at 10G speed. Ports support 1G by default. 
3. MACsec is supported on the OS6900-X48C4E. 
4. Performance software license is optional allowing the OS6570M-U28 ports 25-28 to operate at 10G speed. Ports support 1G by 
default. 
5. Performance software license is optional allowing the OS6870-LNI-U6 ports to operate at 50G speed. Ports support up to 25G 
by default. 
 
Metro License Required 
OmniSwitch 6560 
Licensed Features 
 
 
CPE Test Head 
Yes 
PPPoE-IA 
Yes 
Ethernet OAM 
Yes 
SAA 
Yes 
Link OAM 
Yes 
VLAN Stacking 
Yes 
DPA 
Yes 
Hardware Loopback 
Yes 
IPMVLAN 
Yes 
Note: Starting in 8.9R1 the features above require a Metro license.

<<<PAGE 20>>>
December 2025 
Page 20 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
 
 
Advanced Routing License Required 
OmniSwitch 6570M 
(OS6570M-SW-AR) 
OmniSwitch 6560  
(OS6560-SW-AR) 
Licensed Features 
 
 
 
 
OSPFv2 and OSPFv3 
Yes 
Yes (Up to 2 Areas) 
PIM Multicast Routing (IPv4 & IPv6) 
Yes 
Yes 
Multiple VRFs 
Yes 
Not Supported 
ISIS (IPv4 and IPv6) 
Yes 
Not Supported 
GRE Tunneling 
Yes 
Not Supported 
IP-IP Tunneling 
Yes 
Not Supported 
Route Redistribution 
Yes 
Yes 
VRF Route Leaking 
Yes 
Not Supported 
BGP 
Yes 
Supported 
Note: The table above lists the features supported with the Advanced Routing license.  
 
 
 
Premium Licenses 
License 
Platform 
Sub-license 
Behavior 
VC Parity 
Notes 
OS6570-SW-PRM12 
OS6570M-12 
OS6570M-12D 
SPB 
AR 
Per Node 
Per Node 
Match 
Match 
 
OS6570-SW-PRM28 
OS6570M-U28 
SPB 
AR 
25G 
Per Node 
Per Node 
Per Node 
Match 
Match 
Local-Only 
 
OS6870-SW-PRM1 
OS6870-P24M 
OS6870-P48M 
OS6870-V12 
VxLAN-EVPN 
50G 
Per Node 
Per Node 
Match 
Local-Only (LNI) 
 
Supports VxLAN-L2 
without license. 
OS6870-SW-PRM2 
OS6870-P24Z 
OS6870-P48Z 
OS6870-24 
OS6870-48 
VxLAN-EVPN 
 
Per Node 
Match 
Supports VxLAN-L2 
without license. 
25G - Enables SFP28 (25G) support on the OS6570M-U28 uplink/VFL.  
50G (OS6870-SW-PERF) - Enables the OS6870-LNI-U6 ports to operate at 50G speed.  
SPB - Enables Shortest Path Bridging support. 
AR (OS6570M-SW-AR) - Enables Advanced Routing features   
VxLAN-EVPN - Enables VxLAN-EVPN support. 
Match - Sub-Licenses on all units of a VC must match for feature to be operational. 
Local-Only - Sub-License applies only to local-unit for feature to be operational. 
Premium Licenses  - Introduced in 8.10R4

<<<PAGE 21>>>
December 2025 
Page 21 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
New Hardware Support 
 
The OmniSwitch 6575 is a next generation, hardened, industrial product line supporting operating environments 
from -40°C to 75°C. 
OS6575-P12 - Fixed-configuration, fanless, din-mountable chassis with: 
• 
1 - Console Port 
• 
1 - EMP Port 
• 
1 - USB port 
• 
1 - Alarm Relay 
• 
8 - 10/100/1000Base-T 802.3bt Ports 
• 
4 - SFP+ Uplink / VFL Ports 
• 
Supports a VC of up to 4 chassis  
• 
Supports up to 360W of PoE 
 
OS6575-U28 - Fixed-configuration, fanless, rack-mountable chassis in a 1U form factor with: 
• 
1 - Console Port 
• 
1 - EMP Port 
• 
1 – USBPort 
• 
1 - Alarm Relay 
• 
4 - 10/100/1000BaseT PoE+ or 100FX/1G SFP Combo Ports 
• 
20 - 100FX/1G SFP Ports 
• 
4 - SFP+ Uplink / VFL Ports 
• 
Supports a VC of up to 4 chassis  
• 
Supports up to 210W of PoE  
 
OS6575-MP16 - Fixed-configuration, fanless, wall-mountable chassis with: 
• 
1 - Console Port - M12 A-code Connector 
• 
1 - USB Port - M12 A-code Connector 
• 
1 - Alarm Relay - M12 A-code Connector 
• 
4 - 10/100BaseT Ports - M12 D-code Connectors 
• 
4 - 10/100BaseT 802.3at PoE Ports - M12 D-code Connectors 
• 
4 - 10/100/100 BaseT 802.3bt - M12 X-code Ports 
• 
4 - 10/100/1000BaseT - M12 X-code Ports (With Bypass function) 
• 
No VC support 
• 
Supports up to 120W of PoE 
 
The Alcatel-Lucent OmniSwitch 6920 is a compact, energy-efficient 1RU 400-Gigabit switch designed for high-
performance and low-latency Layer 2/3 networking. 
OS6920-D32 – Fixed configuration, high-density, 400-Gigabit Ethernet platform in a 1RU form factor with: 
• 
1 - Console Port 
• 
1 - USB Port 
• 
32 - 400G QSFP-DD ports 
• 
No VC support in this release

<<<PAGE 22>>>
December 2025 
Page 22 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
The following new types of transceivers are being introduced in this release.  
Transceivers 
Description 
OmniSwitch 
QSFPD-400G-C 
 
400G QSFP-DD Passive Direct Attach Cable. Available in 
50cm, 1m, and 3m lengths. 
6920 
QSFPD-400G-DR4  
 
400G QSFP-DD Transceiver with an MPO-12 connector. 
Supports a maximum length of 500m. 
6920 
QSFPD-400G-FR4  
 
400G QSFP-DD Transceiver with an LC connector. 
Supports a maximum length of 2km. 
6920 
QSFPD-400G-LR4  
 
400G QSFP-DD Transceiver with an LC connector. 
Supports a maximum and length 10km. 
6920 
QSFPD-400G-A10M  
 
400G QSFP-DD Active Optical Cable. Supports a maximum 
length of 10m. 
6920 
QSFP-400G-SR4.2 
 
400G QSFP-DD SR4.2 Transceiver with an MPO-12 
connector. Supports a maximum length of 100m. Support 
4x breakout to QSFP-100G-SR1.2. 
6920 
QSFP-2XQ200-C 
 
400G QSFP-DD to 2x200G QSFP56 Passive Direct Attach 
Cable. Available in lengths of 1m and 3m. 
6920 
QSFPD-2Q100-C 
200G QSFP-DD to 2x 100G QSFP28 Passive Direct Attached 
Cable. Available in 1m and 3m lengths.  
6920 
QSFP-2XQ100-C 
 
200G QSFP56 to 2x100G QSFP56 Passive Direct Attach 
Cable. Available in 1m and 3m lengths. 
6920 
QSFP-100G-SR1.2 
 
100G QSFP28 Optical Transceiver with an LC connector. 
Supports maximum length of 70m over OM3 and 100m 
over OM4. Connects to QSFPD-400G-SR4.2 breakout. 
6860N, 6870, 6900, 
6920, 9900 
QSFP-100G-PSM4 
100G QSFP28 PSM4 Transceiver with an MPO connector. 
Supports a maximum length of 2km. 
6870, 6900, 6920, 9900

<<<PAGE 23>>>
December 2025 
Page 23 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
8.10R4 New Feature and Enhancements 
The following software features are being introduced in this release, subject to the feature exceptions and 
problem reports described later in these release notes.  
Summary Table 
Feature 
OmniSwitch Platform 
 
 
Management Features 
 
Router Mode Support 
6870 
Extension of Session Prompt to 64 Characters 
All 
Certificate Import with Different Format 
All 
Secure su Account 
All 
LACP Support to 96 Groups 
6570M 
Change Password on First Access 
All 
ALE CA Signed Certificates 
All 
Disable Weak Encryption Algorithm 
All 
Support for Static IP on EMP ports [Lightning Config 
Mode] 
Models with EMP Ports 
NAAS Support 
6575 
Add Linux Commands in AOS 
All 
Advanced Routing License - BGP Support 
6560 
 
 
Layer 3 Features 
 
IPV6 BGP Route Aggregation 
6860N, 6870, 6900, 9900 
Dynamic-Proxy-ARP-MAC-Forced-Forwarding 
6560, 6570M 
PIM over GRE 
6860(E),6860N, 6900, 6920 
IPv6 Parity - AAA Profile: Support IPv6 for all IP address 
attributes 
All 
sFlow BGP Gateway 
6560, 6570M, 6575, 6860, 6860N, 6865, 6870, 
6900, 6920, 9900 
 
 
Service Features 
 
EVPN Scalability (Multi-site) 
6900-
X48C6/T48C6/X48C4E/V48C8/C32E/X24C2/T24
C2 
VXLAN EVPN Support 
6870 
ERP Over SPB for Unicast Client 
6570M, 6575, 6860, 6860N, 6865, 6870, 6900, 
6920 9900

<<<PAGE 24>>>
December 2025 
Page 24 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
OmniSwitch Platform 
SPB Support 
6570M, 6575 
IPv6 Parity - ISFv6 Support on SAPs 
6860N, 6870, 6900 (all), 9900 
Multiple ERP ring over SPB 
6570M, 6575, 6860, 6860N, 6865, 6870, 6900, 
6920, 9900 
Learned Port Security on VXLAN 
 
OmniSwitch 6900 
X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24
C2, 6870 
Premium (bundle) Licenses 
6570M, 6870 
Manual RD/RT Configuration 
6900 
X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24
C2 
PIM EVPN Gateway (PEG) 
 
 
6900 
X48C6/T48C6/X48C4E/V48C8/C32E/T24C2/X24
C2 
 
 
QoS/Security Features 
 
JITC Support - CAC Authentication STIGS for Webview 
All 
PC fails 802.1x Authentication due to delayed EAP 
response 
All 
TLS 1.3 Support 
All (AOS) 
6575, 6860, 6860N, 6865, 6870, 6920, 9900 
(Webview) 
IP Fragmentation Attacks Enhancement 
All 
Celona Auto Class Detection 
6465 
Secure Boot 
6360, 6465, 6560, 6570M, 6575, 6860N,  6870, 
6900 (except V72/C32), 6920 
MKA VLAN Tag and TPID on NNI ports 
6465, 6560, 6570M, 6575, 6860(E), 6860N, 
6870, 6900-X48C4E, 9900 
 
 
Other Features 
 
Threat-Insight Security in AppMon 
6860E, 6860N, 6870 
RoCEv2 - DCQCN + LLDP-TLV Update (DCBx) 
6900, 6920 
RoCEv2  Lossless Ethernet  Fabric - DCQCN (ECN+PFC) 
6900, 6920 
PROFINET Support and Certification 
6575 
DHL Active Standby 
All 
Auto Enabling of Device Profiling on Edge Ports 
All (except OS6920) 
Edge-router Mode  
OS6900 (except V72/C32) 
 
 
Parity Features

<<<PAGE 25>>>
December 2025 
Page 25 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
OmniSwitch Platform 
IPv6 Denial of Service (DoS) Detection 
 
6575, 6860, 6860N, 6865, 6870, 6900, 6920, 
9900  
HAVLAN 
PVLAN 
Transparent Bridging 
Port mirroring – remote over linkagg 
 
6570M 
TDR Support 
 
6570M 
Role-based Authentication for Routed Domains 
6570M 
Application Monitoring and Enforcement  
 
6870 
EA Features 
 
Telemetry Support 
6870 
Multi-Site SPB scalability (PoC Only) 
6570M, 6575, 6860, 6860N, 6865, 6870, 6900, 
6920, 9900

<<<PAGE 26>>>
December 2025 
Page 26 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Management Features 
 
Router Mode Support 
The OS6870 supports Router Mode beginning in 8.10R4 and supports the following:  
• 
Number of MAC addresses - 64K 
• 
Number of IPv4 routes - 312K 
• 
Number of IPv6 routes - 156K 
• 
ARP entries - 24K 
• 
IPv6 host entries - 8K 
 
The following CLI commands are associated with this feature: 
• 
capability profile router 
• 
show capability profile 
 
Extension of Session Prompt to 64 Characters 
The session prompt has been extended from 32 to 64 characters. 
The following CLI commands are associated with this feature: 
• 
session prompt default  
 
Certificate Import with Different Format 
This enhancement provides the ability to convert certificates in CER, CRT, DER, P7B and PKCS#12 to PEM 
format. 
The following CLI commands are associated with this feature: 
• 
aaa certificate convert-cert 
 
Secure su Account 
A password must be configured to restrict access to the super-user su account.  
• 
The ability to configure the super-user password is restricted to the admin user only.  
• 
Other users may access the su account if granted permission by the admin user. 
• 
The super-user password is reset when the reset-to-factory command is executed.  
• 
The super-user password cannot be recovered. In the case of a forgotten password a factory reset will 
need to be performed. 
The following CLI commands are associated with this feature: 
• 
super-user-password set 
• 
user example-user super-user enable 
 
LACP Support to 96 Groups 
This enhancement increase the supported LACP groups from 32 to 96 on OS6570M platforms.

<<<PAGE 27>>>
December 2025 
Page 27 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
The following CLI commands are associated with this feature: 
• 
linkagg lacp agg size  
 
Change Password on First Access 
Beginning in 8.10R4 users using the admin account with the default switch password will be required to change 
the password. The password must adhere to the password-policy. Any REST APIs or scripts must be modified to 
account for the required password change. 
The following CLI commands are associated with this feature: 
• 
user password-policy 
• 
show user password-policy 
 
ALE CA Signed Certificates 
Beginning in 8.10R4 an OmniSwitch will use certificates generated by the ALE Internal Certificate Authority 
(CA). The Public Key Infrastructure (PKI) consists of: 
• 
PKI Data Format: All security-related artifacts, including the certificate, private key, and optional 
certificate chain, are stored in a single PEM-encoded file format to simplify management and 
deployment. 
• 
Key Pair Generation: Each device will generate a unique public/private key pair. 
• 
Certificate Issuance: The ALE Internal CA signs the CSR and issues an X.509 certificate specific to the 
device family. 
• 
Validity: Certificates are valid for a period of 5 years from the issuance date. 
• 
Renewal Policy: Devices are required to update their certificates within 1 year prior to expiry, ensuring 
continuous secure operation without downtime. 
The new ALE CA signed certificates are used by default starting in 8.10R4 and are stored in the following 
location:  
• 
/flash/switch/cert.d/aleSupplicantCert.pem 
• 
/flash/switch/cert.d/aleSupplicantPrivate.key 
The new certificates replace the previous self-signed certificates:  
• 
/flash/switch/cert.d/defaultCert.pem 
• 
/flash/switch/cert.d/defaultPrivate.key 
If custom CA certificates were already installed they will continue to be used after upgrading to 8.10R4 and 
will not be replaced by the ALE CA signed certificate. 
Renewal 
There are two methods for renew the ALE CA signed certificates: 
• 
Obtain a new CA-signed certificate included in an updated AOS image.

<<<PAGE 28>>>
December 2025 
Page 28 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
• 
Download a CA certificate from the ALE website and configure it on switches either manually using 
the aaa certificate update-supplicant-certificate command or through OmniVista (OV).  
The following CLI commands are associated with this feature: 
• 
aaa certificate update-supplicant-certificate 
 
Disable Weak Encryption Algorithm 
The Crypto Strong Security feature controls the use of weak encryption algorithms, such as SHA, MD5, SHA-DES, 
MD5-DES, and SHA-AES in user creation. This can be used to mitigate the potential security risks when using 
weaker encryption algorithms. When this feature is enabled only the use of stronger encryption algorithms can 
be used.  
The following table displays which algorithms are allowed and not allowed when this feature is enabled. if the 
feature is disabled there are no restrictions on which algorithms are allowed. 
Allowed  
Not Allowed 
SHA224, SHA256, SHA384, SHA224AES, SHA256AES, 
SHA384AES 
 
SHA, MD5, SHADES, MD5DES, SHAAES 
 
The following CLI commands are associated with this feature: 
• 
system security crypto-strong-security enable 
• 
show system security 
 
Lightning Config Mode 
This enhancement adds support for Lightning Config Mode on the new OS6575 and OS6920 models.  
• 
OS6575 Models – Support added on ports 1/1/1 and 1/1/2. 
• 
OS6920 Models – Support added on EMP port.  
 
NAAS Support 
The NAAS 2.0 Licensing framework has been enhanced to support newly introduced platform OS6575. 
 
Add Linux Commands in AOS 
AOS now exposes selected Linux commands directly in the CLI via a wrapper, eliminating the need to enter su 
mode for these utilities. Initial commands include watch, cut, paste, and tee. 
The following Linux CLIs are added: 
• 
watch 
• 
cut 
• 
paste 
• 
tee

<<<PAGE 29>>>
December 2025 
Page 29 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
 
OS6560 Advanced Routing License with BGP Support 
Beginning in 8.10R4 BGP support is being added to the OS6560 Advanced Routing License (OS6560-SW-AR). 
 
Layer 3 Features 
IPV6 BGP Route Aggregation 
Aggregate routes reduce the size of routing tables by combining the attributes of several more-specific routes 
so that a single aggregate can be advertised to peers. This support is extended for IPv6 addresses in this 
release. 
The following CLI commands are associated with this feature: 
• 
ipv6 bgp aggregate-address admin-state 
• 
ipv6 bgp aggregate-address as-set 
• 
ipv6 bgp aggregate-address community 
• 
ipv6 bgp aggregate-address local-preference 
• 
ipv6 bgp aggregate-address metric 
• 
ipv6 bgp aggregate-address summary-only 
• 
show ipv6 bgp aggregate-address 
 
Dynamic-Proxy-ARP-MAC-Forced-Forwarding 
Dynamic Proxy ARP (DPA/MAC Forced Forwarding) is now supported on OS6560 and OS6570M as part of AOS 
8.10R4. 
The following CLI commands are associated with this feature: 
• 
port-mapping dynamic-proxy-arp 
• 
show ip dynamic-proxy-arp 
 
PIM over GRE  
This enhancement supports Protocol Independent Multicast (PIM) to operate over IP GRE tunnels, allowing 
multicast routing adjacency formation and traffic forwarding between remote networks where native multicast 
is not supported. 
PIM can be enabled on tunnel interfaces and once the adjacencies are established, multicast traffic can be 
forwarded through the virtual link that is created. 
 
IPv6 Parity - AAA Profile: Support IPv6 for all IP address attribute 
This enhancement introduces full IPv6 support for all NAS (Network Access Server) address attributes used in 
AAA configurations. 
Prior to this release, only IPv4 NAS addresses (NAS-IP-Address) could be configured and included in RADIUS 
Access-Request packets. The administrators can now configure and manage both IPv4 and IPv6 NAS addresses at 
both the global RADIUS client level and within individual AAA profiles. 
The following CLI commands are associated with this feature:

<<<PAGE 30>>>
December 2025 
Page 30 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
• 
aaa radius nas-ipv6-address 
• 
aaa profile radius nas-ipv6-address 
• 
show aaa radius config 
• 
show aaa profile 
 
 
sFlow BGP Gateway 
sFlow is enhanced to include extended gateway fields in flow samples. These gateway fields add BGP-related 
attributes to a sampled flow (when available) such as next-hop, AS information, gateway communities and 
local-pref which enables richer attribution of flows to route AS data before they reach the sFlow collector. 
The following CLI commands are associated with this feature: 
• 
sflow agent extended gateway-info admin-state {enable | disable}  
• 
show sflow agent 
 
Services Features 
EVPN Scalability (Multi-site) 
AOS supports various deployment models of EVPN VXLAN in Data Center Interconnectivity (DCI) and multisite 
network. Clos-3, Collapsed Core, Clos-5 (Super Spine, Spine and Leaf), Data Center Interconnectivity and Multi-
PoD, Multi-site Deployment Model (Data Center Interconnectivity) are some models of implementing EVPN 
VXLAN architectures. These are not the exhaustive set of models, but the ones that are weighed in as best 
practice. 
The choice of deployment depends on following factors: Scalability, flood domain, seamless layer 2 and ;ayer 3 
switching across PoD (Point of Delivery) or site in case of greenfield networks, and seamless layer 3 switching 
from VXLAN to VLAN in case of brownfield networks. 
The following CLI commands are associated with this feature: 
• 
service bgp-evpn node-type 
• 
service site-id pod-id 
• 
show service site-info 
• 
show service info 
• 
ip bgp evpn-fabric-autonomous-system 
• 
ip bgp neighbor evpn-nbr-type-fabric 
• 
ip bgp nbr-template 
• 
ip bgp neighbor nbr-template 
• 
show ip bgp nbr-template 
 
VXLAN EVPN Support 
VXLAN-EVPN feature is supported on OmniSwitch 6870. The overall functionality support currently available on 
OmniSwitch 6900 based platforms for EVPN remains same for OmniSwitch 6870 as well. 
It is mandatory to install Premium (Bundle) License for OmniSwitch 6870 to activate the feature on OmniSwitch 
6870.

<<<PAGE 31>>>
December 2025 
Page 31 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
PIM EVPN Gateway (PEG) 
A PIM-EVPN Gateway (PEG) acts as the bridge between an EVPN network and an external Protocol-Independent 
Multicast (PIM) domain, while OISM (Optimized Inter-Subnet Multicast) is a feature that optimizes multicast 
traffic routing within the EVPN fabric by selectively forwarding traffic only to interested receivers. The PEG 
feature enables the border leaf nodes in the EVPN network to interwork with external PIM enabled networks so 
that multicast receivers or senders in the EVPN will be able to receive or send multicast traffic from or to the 
senders/receivers in external PIM network, while OISM improves efficiency for traffic between subnets inside 
the fabric. 
AoS supports both Native PIM hello based DR election and DR election based on DF election algorithm. 
The following CLI commands are associated with this feature. 
• 
service pim-gateway 
• 
show service debug-info 
• 
show service evpn evi 
 
ERP Over SPB for Unicast Client 
MAC flush occurs correctly on SAP ports but does not propagate to SDP ports on BEBs. This results in stale MAC 
entries in the SDP forwarding table, causing traffic drops as packets are forwarded to an incorrect or non-
existent path. This occurs with unidirectional unicast traffic, where MAC learning does not happen dynamically, 
leading to persistent stale entries. 
Stale MAC entries flush can be achieved by enabling the SPB remote flush feature for MAC flush. This approach 
ensures that MAC flush events propagate correctly to SDP ports, preventing traffic drops in unidirectional 
unicast traffic scenarios. 
The following CLI commands are associated with this feature. 
• 
erp-ring spb-remote-flush 
• 
show erp 
 
SPB Support 
SPB feature is supported on OmniSwitch OS6570M and OmniSwitch 6575. On OS6570M, premium bundle license 
will be required to support SPB. On OS6575, SPB will be supported by default (without license).  
SPB will be supported on both ‘default’ as well as ‘Fabric’ TCAM profiles on OmniSwitch 6570M and OmniSwitch 
6575. It is recommended to use ‘Fabric’ TCAM for better performance and scalability.  
 
IPv6 Parity - ISFv6 Support on SAPs 
As part of this enhancement, IPv6 source filtering capability is supported on service domain. 
The following CLI commands are associated with this feature. 
• 
dhcpv6-snooping ipv6-source-filter service 
• 
show dhcpv6-snooping ipv6-source-filter

<<<PAGE 32>>>
December 2025 
Page 32 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Multiple ERP ring over SPB 
Multiple ERP rings are supported over SPB in both single BEB (SAP-SAP) and between two BEBs (SAP-SDP). 
The following CLI commands are associated with this feature: 
• 
There are no new CLIs added for this feature 
 
Learned Port Security on VXLAN 
As part of this enhancement, the LPS support on a Service Access port or Linkagg will be extended to SAP with 
EVPN VXLAN service. All the LPS SAP configuration CLIs are allowed to be configured on EVPN VXLAN SAP. 
The LPS feature support on EVPN VXLAN SAP will be limited to single-homing solution only. 
 
Premium (bundle) Licenses 
This feature introduces premium software licenses. A premium (bundle) software license is a single license that 
contains a set of more than one software license to help simplify the implementation of licenses on an 
OmniSwitch.  
The premium software license file will be generated on the ALE licensing portal using an individual switch MAC 
address and/or Serial Number. This license file can be intalled on the switch, using existing CLI commands. 
The following premium licenses are available:  
License 
Platform 
Sub-license 
Behavior 
VC Parity 
Notes 
OS6570-SW-PRM12 
OS6570M-12 
OS6570M-12D 
SPB 
AR 
Per Node 
Per Node 
Match 
Match 
 
OS6570-SW-PRM28 
OS6570M-U28 
SPB 
AR 
25G 
Per Node 
Per Node 
Per Node 
Match 
Match 
Local-Only 
 
OS6870-SW-PRM1 
OS6870-P24M 
OS6870-P48M 
OS6870-V12 
VxLAN-EVPN 
50G 
Per Node 
Per Node 
Match 
Local-Only (LNI) 
 
Supports VxLAN-L2 
without license. 
OS6870-SW-PRM2 
OS6870-P24Z 
OS6870-P48Z 
OS6870-24 
OS6870-48 
VxLAN-EVPN 
 
Per Node 
Match 
Supports VxLAN-L2 
without license. 
25G - Enables SFP28 (25G) support on four OS6570M-U28 uplink/VFL ports. 
50G (OS6870-SW-PERF) - Enables the OS6870-LNI-U6 ports to operate at 50G speed.  
SPB - Enables Shortest Path Bridging support. 
AR (OS6570M-SW-AR) - Enables Advanced Routing features   
VxLAN-EVPN - Enables VxLAN-EVPN support. 
Match - Sub-Licenses on all units of a VC must match for feature to be operational. 
Local-Only - Sub-License applies only to local-unit for feature to be operational. 
 
The following CLI commands are associated with this feature: 
• 
license apply file 
• 
show license-info  
• 
show license-info detail

<<<PAGE 33>>>
December 2025 
Page 33 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Manual RD/RT Configuration 
Manual RT (Route-Target) configuration is required to control the establishment of tunnel paths between nodes 
in an EVPN port network. The ability to associate multiple manual RT values for a service is especially useful 
when deploying EVPN services in a brownfield multi-site EVPN environment. With manual RTs, EVPN routes can 
be selectively imported and exported between multiple sites or PoDs, each operating with its own RT 
configuration. This flexibility simplifies service extension across different administrative domains. 
In addition, manual RT configuration enables the deployment of E-Tree-based service topologies, which are 
often used in Clos architectures. By applying RT-based filtering, unnecessary east-west tunnels between leaf 
nodes within a PoD can be avoided, leading to better scalability and more efficient resource utilization. 
The following CLI commands are associated with this feature: 
• 
service bgp-evpn route-target 
• 
show service evpn evi 
 
 
QoS/Security Features 
JITC Support - CAC Authentication STIGS for Webview 
CAC/PIV based SSH Authentication (PKIX SSH) adds a dedicated PKIX SSH server to support CAC/PIV smart card 
logins over SSH using X.509v3 certificates or public keys extracted from the card. Access requires mapping the 
certificate/Key to a local user; certificates are validated against a persistent trust store with CRL based 
revocation checks. 
The following new CLI commands are added: 
• 
ip service ssh-pkix admin-state 
• 
ip service ssh-pkix port 
• 
show ssh-pkix 
 
PC fails 802.1x Authentication Due to Delayed EAP Response 
This feature expands the 802.1X max-req range from 1–3 to 1–50—at the port/LAG and port-template levels to 
accommodate slow or delayed EAP-Response scenarios observed during PC boot or transient network 
conditions. 
The following CLI commands are associated with this feature: 
• 
unp 802.1x-authentication max-req 
 
TLS 1.3 Support 
Adds TLS 1.3 as a configurable protocol version for OmniSwitch TLS client services (RADIUS, LDAP, SYSLOG NG, 
SNMP) and Webview application. The default TLS version is also changed from 1.0 to 1.2. 
The following CLI commands are associated with this feature: 
• 
ssl pki tls version 
• 
webview tls version

<<<PAGE 34>>>
December 2025 
Page 34 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
IP Fragmentation Attacks Enhancement 
This enhancement introduces a new IP Fragmentation Attack Defense mechanism within the IPv4/IPv6 DoS 
framework to protect against fragmentation-based Denial-of-Service (DoS) attacks. 
The feature detects and drops malformed, overlapping, or excessive IP fragments that could otherwise lead to 
reassembly buffer exhaustion, CPU overload, or system instability. 
The update adds new DoS attack control options: 
• 
tear-drop – The overlapping fragments and malformed or incomplete sequences are detected and 
dropped. 
• 
icmp-frag-drop – The fragmented ICMP packets are detected and dropped. 
The following CLI commands are associated with this feature: 
• 
ip dos type 
 
Celona Auto Class Detection 
CRAOS8X-50838 – Celona AP failed to be detected by OS6465-P12 and OS6465H-P12 as a Class 6 PD. 
When Celona PDs are connected to OmniSwitch, although the PoE devices support Class 6 and Class 8, the 
switch was detecting them as Class 4 devices, when the autoclass was enabled on switch. As a result, the 
switch was limiting power delivery to 30W as per the Class 4 limitations. 
Since PoE autoclass was enabled on the switch, the incorrect signaling led to the PD being assigned Class 4. 
Since this is a hardware behavior on the Celona side and cannot be corrected by the switch, the workaround is 
to disable autoclass on the switch. Disabling autoclass ensures that the switch does not downgrade the PD class 
due to faulty autoclass measurements. 
The autoclass can be disabled using the following CLI: 
• 
lanpower {slot chassis/slot | port chassis/slot/port-port} autoclass {enable | disable} 
 
Secure Boot 
Secure Boot is a important security mechanism that ensures an OmniSwitch boots with only verified and trusted 
software. By performing authentication checks during startup, an OmniSwitch safeguards the integrity and 
authenticity of critical system components such as the bootloader and operating system. Support of the Secure 
Boot feature requires upgrades to U-boot, ONIE, and BIOS as well as using an AOS Secure Boot image. 
The following CLI commands are associated with this feature: 
• 
show microcode 
 
See Secure Boot Behavior Beginning in 8.10R4 for the required software updates and platform behavior prior to 
upgrading to 8.10R4.

<<<PAGE 35>>>
December 2025 
Page 35 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
MKA VLAN Tag and TPID on NNI ports 
Currently MKA packets are exchanged in default VLAN.  In some cases, like the setup shown in the below 
diagram, when MACsec is enabled between two NNI ports where the intermediate node does not support 
MACsec, the MKA packets need to be tunneled. In order to tunnel the MKA packets in the intermediate node, 
these packets need to be carried on the NNI/service VLAN. In the 8.10.R03 release, the MKA packets are 
exchanged in the default VLAN, these packets are getting dropped on the intermediate NNI interfaces. 
 
Provider
Network
CE-1
CE-2
PE-1
PE-2
Intermediate 
Network Node
MACSEC Capable/Enabled Interface
MACSEC Incapable/Disabled Interface
NNI Port
NNI Port
NNI Port
NNI Port
 
 
An enhancement in 8.10R4 allows the user to configure whether these MKA packets should have VLAN tag 
added and to which VLAN these MKA control packets belong. This provides flexibility as to what should be the 
TPID for these VLAN tags.  
The following CLI commands and MIB attriubutes are introduced:  
• 
alaSecyMkaVlan 
• 
alaSecyMkaTpid 
 
To configure: 
-> interfaces <c/s/p> macsec mode dynamic mka-vlan <vid> [mka-tpid <tpid>] 
To remove the VLAN tagging use the following action to undo the configuration: 
-> no interfaces <c/s/p> macsec mka-vlan  
To show: 
-> show interfaces macsec mka-info 
Chas/Slot/Port     Vlan Tagged         VLAN          TPID            MKA Profile       
----------------+------------------------+-------------+-------------+------------------- 
1/1/1               
Yes                 1000            0x88a8             default  
1/1/2                 No          
     0                 0        
 mkaprofile1 
 
The MKA VLAN Tag and TPID configuration is only applicable to the network topology shown above. It is 
intended for the MACsec-enabled NNI interfaces to tunnel the MKA packets over the intermediate NNI nodes. 
Note: This information will be captured in the next revision of the 8.10R4 user guides.

<<<PAGE 36>>>
December 2025 
Page 36 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Other Features 
Threat-Insight Security in AppMon 
Threat-Insight Security is now integrated into AppMon (Application Monitoring), providing enhanced visibility 
into SSL/TLS traffic anomalies via per-flow threat intelligence. This feature adds support for the following 
attributes: 
• 
DGA Score – Detects domains likely generated algorithmically (e.g., by malware). 
• 
MITM Score – Indicates probability of man-in-the-middle interception in TLS sessions. 
• 
JA3 Fingerprint – A TLS Client Hello fingerprint used to identify client types or anomalies. 
These attributes are analyzed in real time using the new CLI commands for IPv4 and IPv6 flow tables. 
The following CLI commands are associated with this feature: 
• 
show app-mon ipv4-flow-table monitor threat-insight 
• 
show app-mon ipv4-flow-table enforcement threat-insight 
• 
show app-mon ipv6-flow-table monitor threat-insight 
• 
show app-mon ipv6-flow-table enforcement threat-insight 
 
RoCEv2 - DCQCN + LLDP-TLV update (DCBx) 
This enhancement extends the LLDP (Link Layer Discovery Protocol) module to support Data Center Bridging 
Exchange (DCBX) protocol TLVs and the IEEE 802.3 Maximum Frame Size TLV. These additions enable LLDP to 
advertise DCBX-related parameters and the maximum frame size capability of a port, improving 
interoperability and diagnostics in data-center bridging environments. 
The following CLI commands are associated with this feature: 
• 
lldp <chassis/slot/port | chassis/slot | chassis> tlv management dcbx <enable | disable> 
• 
show lldp config 
 
RoCEv2  Lossless Ethernet  Fabric - DCQCN (ECN+PFC) 
Adds the support of PFC, ETS, DCBX for OS6900 and OS6920 to comply with MSFT requirements. 
The following CLI commands are associated with this feature: 
• 
lldp lldpdu 
• 
lldp nearest-edge mode 
• 
lldp transmit interval 
• 
lldp tlv dot1 
• 
show lldp statistics 
• 
show lldp remote-system 
• 
qos qsi dcb dcbx admin-state 
• 
qos qsi dcb dcbx ets 
• 
qos qsi dcb dcbx pfc 
• 
qos qsp dcb import 
• 
qos qsi qsp dcb 
• 
qos qsp dcb tc 
• 
qos qsp dcb ecn-profile

<<<PAGE 37>>>
December 2025 
Page 37 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
• 
show qos qsp dcb 
• 
show qos qsi dcb dcbx 
• 
show qos qsi dcb ets 
• 
show qos qsi dcb pfc stats 
• 
qos ecnp import ecnp 
• 
qos ecnp value 
• 
qos qsp ecn-profile 
• 
qos qsi qp ecn 
• 
show qos qsi stats 
 
PROFINET Support and Certification 
Adds OS6575 family support for PROFINET IO-Device.  
 
DHL Active Standby 
The DHL Active-Standby feature introduces deterministic link redundancy for Link Aggregation Control Protocol 
(LACP)–based connections in Dual-Home Link (DHL). This enhancement allows one LACP member link to operate 
as Active while another remains Standby, providing seamless failover without relying on Spanning Tree Protocol 
(STP). 
Upon detection of failure, the standby port instantly becomes Active, maintaining the aggregate’s operational 
state and ensuring uninterrupted traffic forwarding. The feature also supports pre-emption and pre-empt timer 
configuration to allow automatic reversion to the preferred (primary) link after recovery, ensuring 
deterministic and stable network behavior. 
The following CLI commands are associated with this feature: 
• 
linkagg lacp port chassis/slot/port[-port2] standby {enable | disable} 
• 
linkagg lacp agg agg_num-agg_num/agg_num pre-empt {enable | disable} 
• 
linkagg lacp agg agg_num-agg_num/agg_num pre-empt timer seconds 
• 
show linkagg 
• 
show linkagg port 
 
Auto Enabling of Device Profiling on Edge Ports 
As a part of this enhancement, when Device Profiling feature is enabled globally on the switch, Device Profiling 
will be enabled by default on all edge ports. 
The following CLI commands are associated with this feature. 
• 
device-profile admin-state 
• 
device-profile port linkagg 
• 
show device-profile config 
• 
show device-profile ports 
 
Edge-router Mode on OS6900 
The OS6900 models (except V72/C32) now support edge-router mode with increased MAC Scalability as 
compared to router-mode. Once edge-router mode is enabled the configuration must be saved and the switch

<<<PAGE 38>>>
December 2025 
Page 38 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
rebooted for the configuration to take effect. OS6900 models that do not support the edge-router mode 
(V72/C32) cannot be mixed in a VC with other OS6900 models that have edge-router mode enabled. 
The following CLI commands are associated with this feature. 
• 
capability profile {switch | router | edge-router} 
 
 
Parity Features 
IPv6 Denial of Service (DoS) Detection 
Introduces IPv6 Denial of Service (DoS) detection. This enhancement enables the switch to detect, count, and 
report multiple IPv6-based DoS attack types, improving control-plane protection and operational visibility in 
IPv6-enabled networks. IPv6 DoS detection operates on the Network Interface (NI) and reports events to the 
Chassis Management Module (CMM), where statistics, logs, and SNMP traps are generated. The following IPv6 
DoS attack types are supported in this release: 
• 
Ping of Death – Oversized ICMPv6 packets exceeding the IPv6 maximum datagram size (65,535 bytes). 
• 
Land Attack – Packets with identical IPv6 source and destination addresses. 
• 
Loopback Source – Packets received with ::1 as the source IPv6 address. 
• 
Invalid IPv6 Address – Packets with invalid or malformed source or destination IPv6 addresses. 
• 
Ping Overload – High-rate ICMPv6 flooding intended to exhaust control-plane resources. 
• 
NDP Flood – Excessive Neighbor Solicitation and/or Neighbor Advertisement traffic. 
• 
IPv6 Fragmentation Tear-Drop – Overlapping or malformed IPv6 fragments. 
• 
IPv6 ICMP Fragmentation Drop – Detection and dropping of fragmented ICMPv6 packets. 
 
The following new CLI commands are introduced: 
• 
ipv6 dos type 
• 
show ipv6 dos config 
• 
show ipv6 dos statistics 
 
OS6570M Parity - L2 Features 
The following features are supported on the OS6570M starting in 8.10R4.  
• 
HAVLAN 
• 
PVLAN 
• 
Transparent Bridging 
• 
Port mirroring – remote over linkagg 
 
OS6570M Parity - TDR Support 
Time Domain Reflectometry (TDR) is supported on the following OS6570M ports.  
• 
OS6570M-12/12D - Ports 1 through 8. 
• 
OS6570-U28 - Hybrid ports 21 through 24 if hybrid-mode is set to copper.

<<<PAGE 39>>>
December 2025 
Page 39 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
The following CLI commands are associated with this feature: 
• 
interfaces tdr 
• 
show interfaces tdr-statistics 
 
OS6570M Parity - Role-based Authentication for Routed Domains 
Role-based Authentication for Routed Domains is supported on the OS6570M starting in 8.10R4.  
The following CLI commands are associated with this feature: 
• 
unp network-group 
• 
unp router-auth user-group 
• 
unp router-auth cp-profile 
• 
unp router-auth user flush 
• 
show unp network-group 
• 
show unp router-auth user-group 
• 
show unp router-auth configuration 
• 
show unp router-auth users 
 
Application Monitoring and Enforcement (DPI/Appmon) 
The Application Monitoring and Enforcement feature is supported on the OS6870 beginning in 8.10R4.  
 
EA Features 
 
Telemetry Support 
Telemetry support adds a push-based telemetry exporter on the OmniSwitch that collects DPI/flow data from 
the switch (stored locally in Redis), formats it as IPFIX (RFC-7011) and exports it to an external collector (for 
example: Telegraf → InfluxDB → Grafana). It enables near-real-time visibility for monitoring, troubleshooting, 
and feeding automation/AI systems. 
The telemetry agent on the OmniSwitch gathers DPI or flow data (stored in a local Redis DB), bundles it into 
IPFIX messages, and exports to a collector (e.g., Telegraf), DB (InfluxDB), visualization (Grafana). 
The key benefits are: 
• 
Real-Time Monitoring: Immediate insights into network behavior, allowing faster detection of 
anomalies, congestion, or failures. 
• 
Better Performance: Continuous data streaming reduces overhead compared to traditional polling 
methods, improving scalability. 
• 
Proactive Network Management: Identify trends and potential issues before they impact services. 
• 
Enhanced Visibility: Granular metrics on traffic, packet drops, jitter, latency, application identification, 
etc., to aid troubleshooting and optimization. 
• 
Supports Automation and AI: Streamed telemetry feeds can be consumed by AI or ML systems for 
predictive analytics and automated remediation.

<<<PAGE 40>>>
December 2025 
Page 40 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
The following CLI commands are associated with this feature: 
• 
telemetry admin-state 
• 
telemetry destination 
• 
show telemetry config 
• 
show telemetry destination 
• 
show telemetry template 
 
 
Multi-Site SPB Scalability (PoC)  
The current deployments of the SPB network operate in a flat topology (Level 1 network). The bridge nodes 
form Level 1 adjacencies in order to establish the SPB network. While this allows simplicity of configuration 
and maintenance, it also imposes limits to the scalability of the network. The limitations arise in both the 
control plane and the data plane. The control plane limitations arise from the resource and computation 
required by the SPB ISIS protocol to establish and actively manage the reachability for all nodes in the network. 
The data plane limitation is from the amount of service tunnels that can be established between the nodes in 
the network. The overall limitation for number of nodes supported in a flat SPB network typically is in the 
range of 500 to 1000 nodes depending on the CPU and switching ASIC associated with the nodes in the SPB 
network. 
 
When the number of bridge nodes in the SPB network exceeds the capacity, typically the network will need to 
be provisioned as distinct networks. A bridge interface must be introduced in between these isolated SPB 
networks to provide a crude fabric interconnect. This interface is agnostic to the SPB protocol and resource. 
The result is a suboptimal network for both operations and management. Such a network configuration is also 
not feasible for networks that require hyper scalable solutions. 
 
The solution implemented here is to provision a hierarchical SPB network that operates in a multi-site topology 
of the SPB network with the ability to provide both hyper scalability and secure access between these isolated 
sites (or areas) of the SPB network. The intra-site nodes operate in the SPB ISIS Level 1 network while the 
inter-site connecting nodes will operate in the SPB ISIS Level 2 network. Each site in a multi-site network is 
identified by a unique site-id usually based on geographic location of a set of nodes. Each site will have special 
inter-site gateway nodes designated as Site Border Nodes (SBN) to provide the inter-site communication. The 
site border nodes from multiple sites will interconnect at circuits designated for Level 2 operation to form a 
Level 2 adjacencies of the SPB network. Inter-site connectivity is provided by this Level 2 network while intra-
site connectivity is provided in the Level1 network of each local site. The topology supports provisioning of 
both L2 VPN and L3 VPN based services along with support for Multicast Snooping with inter-site connectivity. 
 
This proposed hyper-scalable design and implementation will accomplish both the scalability and security 
requirements for a large topology network. This solution will provide both ECT-based load-balancing and also 
seamless failover redundancy from the intra-site bridge nodes to the transition points (SBNs) of the multi-site 
hierarchical SPB network. The provisioning requirements can be limited to only the Site Border Nodes where 
adjacency links have to be designated as Level1 SPB -ISIS interface, Level 2 SPB -ISIS interface or a Level1Level 
2 SPB -ISIS interface. Additionally, the SBN needs to be provisioned with the 3-byte site-id that will identify the 
segment of the multi-site network. 
 
The following CLI commands are associated with this feature. 
• 
spb isis interface port chassis/slot/port level level 
• 
service spb site-id <site_id >

<<<PAGE 41>>>
December 2025 
Page 41 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Open Problem Reports and Feature Exceptions 
The problems listed here include problems known at the time of the product’s release.  
CR 
Description 
Workaround 
System / General / Display 
CRAOS8X-41328 
On an OS9912 if a member port of a link 
aggregate with hashing/load-balancing 
enabled is disabled all the traffic may be 
sent on just one of the other ports 
instead of being load-balanced across the 
link aggregate.  
There is no known workaround at this 
time. 
CRAOS8X-52134 
 
PTP time stamping does not happen 
correctly when PTP packets ingress on 
PHY-based ports and egress on PHYLESS 
ports and vice versa. 
PTP traffic ingressing on OS6870-V12 
ports 1/1/1-12 and egressing on ports 
1/1/13-14, CNI-U2 or LNI-U6 ports or vice 
versa, PTP timestamping does not happen 
correctly and causes the high 
2wayTimeError. 
PTP traffic ingressing on OS6570-U28 
ports 1/1/1-24 and egressing on ports 
1/1/25-30 ports or vice versa, PTP 
timestamping does not happen correctly 
and causees the high 2wayTimeError.  
There is no known workaround at this 
time. 
CRAOS8X-56176 
In breakout configuration, LED1 
corresponding to subport A behavior 
differs from that of the other subports.  
Its link and activity status might not be 
properly reflected.  
Check subport A status using the CLI. 
CRAOS8X-11084 
Packet drop seen in BFD config when 
VRRP VLAN interface is toggled. 
There is no known workaround at this 
time. 
CRAOS8X-34219 
With CFM2 and XNI-U48 board, port 
recovery after violation takes additional 2 
mins with WTR of 15 secs. 
There is no known workaround at this 
time. 
CRAOS8X-54665 
On an OS6575, a load-balancing issue 
occurs after disabling the primary port on 
a Link Aggregation Group (LAG) with 8 
members when handling multicast and 
broadcast traffic. When the LAG member 
count is reduced to 7, one of the 
remaining LAG member ports stops 
forwarding broadcast packets, resulting in 
There is no known workaround at this 
time.

<<<PAGE 42>>>
December 2025 
Page 42 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
imbalanced packet counters across the 
LAG members. 
Hardware / Transceivers 
CRAOS8X-35816 
 
SFP-10G-T supports only 10G peer links. 
Link will be down when peer speed is 
either 1G or 100M. If peer 1G or 100M is 
left connected, after some idle time, 
some quick down>up toggles may be seen 
locally. When peer is changed to 10G, 
port will operate as expected. However, 
it has been observed, if peer is left at 
100M for a lengthy period, and multiple 
down>up toggles are seen, port may not 
recover even after reverting back to 10G. 
Recommend peer end to be strictly at 
10G. 
CRAOS8X-36381 
 
It is possible with SFP-GIG-T , when speed 
is configured to 10M, multiple admin 
disable/enable toggles can cause port 
instability (including false local linkup 
and no traffic through port). 
Issue is seen with repeated consecutive 
local admin disable/enable toggles. 
Issue is not seen with 1G and 100M speed 
configurations. 
 
There is no known workaround at this 
time. 
CRAOS8X-41611 
 
On an OS99-CNI-U8 with 4x25G DAC link 
sometimes does not come up for certain 
lanes. 
 
Use the QSFP-100G-SR4 fiber 
transceiver with 4X25G capability. 
CRAOS8X-36440 
 
OS6570M-U28 port 25 with SFP-10G-T 
transceiver may see a local only linkup or 
a LED up with link down when peer side is 
admin toggled repeatedly. 
 
There is no known workaround at this 
time. 
CRAOS8X-46185 
 
Fiber ports with SFP-GIG-T connected to 
peer at 10M speed is operational as 
expected. However, when the peer link 
changes from 10M to 100M or 1G speed, 
user may (intermittently) see link down 
with peer side link up. 
 
On OS6570M-U28 a hot-swap of the 
SFP-GIG-T recovers the port. On 
OS6570M-12/12D a switch reload may 
be required to recover port. 
CRAOS8X-46195 
 
VFL links using 4X25G splitters require 
additional configuration to prevent CRC 
errors being seen on the link. 
 
The preferred method is configuring 
inter-frame-gap to 13 on both sides of 
the link. An alternate method is 
configuring FEC to FC and 
autonegotiation 
disable on both sides of the 
link. Note: Configuring FEC and 
disabling auto-negotiation will cause 
link to reset.

<<<PAGE 43>>>
December 2025 
Page 43 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
CRAOS8X-49465 
 
SFP-DUAL-BX-U/D transceivers do not link 
up on OS6870-P24Z/P48Z/LNI-U6. They 
may be used on 6870-24/48/V12 ports at 
1G speed. 
 
There is no known workaround at this 
time. 
CRAOS8X-56108 
On an OS6575-MP16 there is 
approximately a 1 minute delay in 
updating the “Power Supply Unplugged” 
status.  
There is no known workaround at this 
time. 
CRAOS8X-52863 
On an OS6860N-U28 a message similar to 
“smgrOpenLicenseFile@6844 Unable to 
open License file(fd: 0x0)” may be 
displayed on the console.  
There is no functionality impact. 
 
 
 
Layer 2 
CRAOS8X-41707 
 
When configuring erp ring and verify 
convergence with port down/up and node 
down/up events, the convergence 
number is high for an average 10 
iterations. 
 
There is no known workaround at this 
time. 
Layer 3 
CRAOS8X-44230 
 
When IPMVLAN is enabled 
on a switch with rvlan configured on the 
receiver port, after a write memory 
flashsynchro 
and reload, when the ipmvlan 
configs are removed the slave unit still 
retains the routing mode on it. Now if 
IPMVLAN is enabled without rvlan on 
receiver port and the current slave 
becomes the master due to VC-takeover, 
it starts behaving like L3 mode with 
forward and source table getting 
populated when source traffic flows. 
 
There is no known workaround at this 
time. 
CRAOS8X-54726 
The OS6920 cannot redirect ICMP packet 
type 5 code 1. 
There is no known workaround at this 
time. 
CRAOS8X-54919 
On an OS6920 ARP cannot be resolved 
after sending traffic with ICMP request 
packet for different subnets scenario with 
Snap header.  
There is no known workaround at this 
time. 
CRAOS8X-55042 
An OS6920 does not forward ICMPv6 
packet with IPv6 tunnel configuration. 
IP-IP, GRE, Configured IPv6 and 6to4 
tunnels are not supported on OS6920 in 
8.10R4. 
Multicast

<<<PAGE 44>>>
December 2025 
Page 44 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
CRAOS8X-56622 
Cannot config ip/ipv6 multicast vlan 
source-timeout value on na OS6920. 
There is no known workaround at this 
time. 
CRAOS8X-54771 
On na OS6920 IPMSv6 traffic is received 
on nack port although querying status is 
disabled. 
There is no known workaround at this 
time. 
CRAOS8X-54917 
An OS6920 does not send out ICMP reply 
packets type with correct ID for packet 
with IP Options.  
There is no known workaround at this 
time. 
CRAOS8X-55219 
An OS6920 is not able to forward 
broadcast traffic with multicast MAC. 
There is no known workaround at this 
time. 
CRAOS8X-55891 
On an OS6575, counters are not getting 
updated on multicast unp policy lists for 
IPv4 and IPv6 rules.  
This is a display issue Only, there is no 
impact on functionality. 
Services 
CRAOS8X-51356 
 
The ‘show ip multicast evpn’ and ‘show ip 
multicast evpn details’ CLI commands 
show display the same output. 
 
There is no known workaround at this 
time. 
CRAOS8X-55868 
On an OS6920, an intermittent packet 
drop is sometimes seen in SPB test cases 
when traffic is sent with a very small 
packet (10 packets).  
With typical traffic patterns this issue 
will not seen.  
CRAOS8X-56485 
On a port with multiple SAPs configured, 
if port-security is configured on some 
SAPs the ARP packets may be trapped for 
learning for all the SAPs configured on 
the port. 
There is no known workaround at this 
time 
CRAOS8X-51356 
The commands ‘show ip multicast evpn’ 
and ‘show ip multicast evpn details’ 
display the same output.  
There is no known workaround at this 
time. 
CRAOS8X-55637 
In an EVPN symmetric configuration, 
traffic drop may be seen for symmetric 
routing after a service toggle.  
There is no known workaround at this 
time.  
CRAOS8X-55755 
In an EVPN PIM & Asymmetric 
configuration, internal source and 
asymmetric traffic drop may be seen 
after toggling the BGP admin-state.  
There is no known workaround at this 
time. 
CRAOS8X-55757 
In an EVPN Asymmetric routing 
configuration, asymmetric traffic drop 
may be seen after toggling the OSPF 
admin-state.  
There is no known workaround at this 
time. 
CRAOS8X-55851 
On an OS6870 with an EVPN symmetric 
configuration IRB traffic drops may be 
seen after service toggle.  
There is no known workaround at this 
time. 
CRAOS8X-56261 
For an EVPN multi-site configuration 
dynamic learned services are not going 
down after removing the BL from the site 
or changing pod id or disabling ip bgp.  
There is no known workaround at this 
time.

<<<PAGE 45>>>
December 2025 
Page 45 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
 
 
 
Virtual Chassis 
CRAOS8X-41294 
 
After 2nd vc-takeover, sometimes sdp or 
sap MACs are missing from 'show mac-
learning' output. 
 
Re-send traffic for missing MACs. 
CRAOS8X-53703 
On an OS9900 chassis-2 will sometimes 
get split after a cmm-takeover.  
There is no known workaround at this 
time. 
QoS / Security 
CRAOS8X-34758 
 
Port violation recovery takes additional 5 
secondss sometimes. 
 
There is no known workaround at this 
time. 
CRAOS8X-40989 
 
On an OS99-XNI-P24Z8 the dynamic 
MACsec port status is down after a 
reload.The issue is only specific to the 
first 8 ports. 
 
Toggle the MACsec admin state on the 
port. 
CRAOS8X-41038 
 
When configuring static MACsec without 
encryption and keys are mismatched, the 
traffic can still go through. Works as 
expected with encryption enabled. 
 
There is no known workaround at this 
time. 
CRAOS8X-52283 
 
Compared to previous releases, there can 
be a behavior change for CLI ‘policy mac 
group alaPhones <>’ on CMM2 NI cards of 
OS9912 where traffic of MAC addresses 
that are part of the policy mac group 
alaPhones are not trusted for ingress 
802.1p priority as per its default behavior. 
 
Applying the CLI command ‘qos apply’ 
resolves the issue. 
CRAOS8X-56165 
On an OS6900-V48 some observed packet 
loss and ingress traffic rate slow down is 
not at the expected rate. 
Maximum of 40 Traffic Classes (TCs) 
can be configured as lossless. 
Configuring more than 40 lossless TCs 
is not recommended. 
 
Recommendation: 
DCB-2 and DCB-4 profiles support all 
TCs as lossless. These profiles should 
be used for a maximum of 5 ports. 
If more ports need to be scaled, it is 
recommended to use a custom QSP 
DCB profile with only the required TCs 
configured as lossless. 
 
Default DCB Profiles: 
 
Default DCB profile 1 (SP) and 3 (WRR): 
All TCs are lossy.

<<<PAGE 46>>>
December 2025 
Page 46 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Default DCB profile 2 (SP) and 4 (WRR): 
All TCs are lossless. 
 
Basic CLI Commands for configuring 
selected TCs as lossless: 
qos qsp dcb import qsp dcb "1/2/3/4" 
qos qsp dcb tc pfc flow-type LL 
qos qsi port 
CRAOS8X-53627 
On na OS6575 traffic drops may be seen 
after enabling policy rule Redirect_All.  
There is no known workaround at this 
time.

<<<PAGE 47>>>
December 2025 
Page 47 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Hot-Swap/Redundancy Feature Guidelines 
Hot-Swap Feature Guidelines 
Refer to the table below for hot-swap/insertion compatibility. If the modules or power supplies are not 
compatible a reboot of the chassis is required after inserting the new component. 
• 
When connecting or disconnecting a power supply to or from a chassis, the power supply must first be 
disconnected from the power source.  
• 
All NI module extractions must have a 30 second interval before initiating another hot-swap activity. 
CMM module extractions should have between a 15 and 20 minute interval.  
• 
All new module insertions must have a 5 minute interval AND the LEDs (OK, PRI, VC, NI) have returned 
to their normal operating state.   
 
Existing Expansion Slot  
Hot-Swap/Hot-Insert compatibility 
Empty 
All modules can be inserted 
OS68-XNI-U4 
OS68-XNI-U4 
OS68-VNI-U4 
OS68-VNI-U4 
OS68-QNI-U2 
OS68-QNI-U2 
OS68-CNI-U1 
OS68-CNI-U1 
OS6860N-P48M Hot-Swap/Insertion Compatibility  
 
Existing Slot  
Hot-Swap/Hot-Insert compatibility 
Empty 
All modules can be inserted 
OS99-CMM 
OS99-CMM 
OS99-CMM2 
OS99-CMM2 
OS9907-CFM 
OS9907-CFM 
OS99-GNI-48 
OS99-GNI-48 
OS99-GNI-P48 
OS99-GNI-P48 
OS99-XNI-48 
OS99-XNI-48 
OS99-XNI-U48 
OS99-XNI-U48 
OS99-XNI-P48Z16 
OS99-XNI-P48Z16 
OS99-CNI-U8 
OS99-CNI-U8 
OS99-GNI-U48 
OS99-GNI-U48 
OS99-XNI-U24 
OS99-XNI-U24 
OS99-XNI-P24Z8 
OS99-XNI-P24Z8

<<<PAGE 48>>>
December 2025 
Page 48 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
OS99-XNI-U12Q 
OS99-XNI-U12Q 
OS99-XNI-UP24Q2 
OS99-XNI-UP24Q2 
OS99-CNI-U20 
OS99-CNI-U20 
OS9900 Hot-Swap/Insertion Compatibility  
 
Existing Expansion Slot  
Hot-Swap/Hot-Insert compatibility 
Empty 
All modules can be inserted 
OS6870-LNI-U6  
OS6870-LNI-U6 
OS6870-CNI-U2 
OS6870-CNI-U2 
OS6870 Hot-Swap/Insertion Compatibility  
 
 
Hot-Swap Procedure 
The following steps must be followed when hot-swapping modules.  
1. Disconnect all cables from transceivers on module to be hot-swapped. 
2. Extract all transceivers from module to be hot-swapped. 
3. Extract the module from the chassis and wait approximately 30 seconds before inserting a 
replacement.  
4. Insert replacement module of same type. For a CMM wait approximately 15 to 20 minutes after 
insertion.  
5. Follow any messages that may displayed. 
6. Re-insert all transceivers into the new module.  
7. Re-connect all cables to transceivers. 
8. Hot-swap one CFM at a time. Please ensure all fan trays are always inserted and operational. CFM hot-
swap should be completed with 120 seconds. 
VC Hot-Swap / Removal Guidelines 
Elements of a VC are hot-swappable. They can also be removed from, or added to, a VC without disrupting 
other elements in the VC. Observe the following important guidelines:  
• 
Hot-swapping an element of a VC is only supported when replaced with the same model element (i.e. 
an OS6900-V72 must be replaced with an OS6900-V72).  
• 
Replacing an element with a different model element requires a VC reboot. 
Fast/Perpetual PoE Unlike Power Supply Swapping 
When swapping unlike power supplies on an OS6860N-P48M follow the procedure below to ensure continued 
PoE functionality when fast or perpetual PoE is enabled. 
1. Disable fpoe and ppoe (Only needs to be executed if lanpower is started).  
2. Save and synchronize the configuration.

<<<PAGE 49>>>
December 2025 
Page 49 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
3. Swap the power supplies.  
4. Reload chassis. 
5. Start lanpower. 
6. Enable fpoe and ppoe as required.  
7. Save and synchronize the configuration.

<<<PAGE 50>>>
December 2025 
Page 50 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Technical Support 
ALE technical support is committed to resolving our customer’s technical issues in a timely manner. Customers 
with inquiries should contact us at: 
Country 
Supported Language 
Toll Free Number 
France, Belgium, Luxembourg 
French 
+800-00200100 
Germany, Austria, Switzerland 
German 
United Kingdom, Italy, Australia, Denmark, Ireland, 
Netherlands, South Africa, Norway, Poland, Sweden, 
Czech Republic, Estonia, Finland, Greece, Slovakia, 
Portugal 
English 
Spain 
Spanish 
India 
English 
+1 800 102 3277 
Singapore 
English 
+65 6812 1700 
Hong-Kong 
English 
+852 2104 8999 
South Korea 
English 
+822 519 9170 
Australia 
English 
+61 2 83 06 51 51 
USA 
English 
+1 800 995 2696 
Your questions answered in English, French, German or 
Spanish. 
English 
French 
German 
Spanish 
+1 650 385 2193 
+1 650 385 2196 
+1 650 385 2197 
+1 650 385 2198 
Fax: +33(0)3 69 20 85 85 
Web : myportal.al-enterprise.com 
 
Internet: Customers with service agreements may open cases 24 hours a day via the support web page. Upon 
opening a case, customers will receive a case number and may review, update, or escalate support cases on-
line. Please specify the severity level of the issue per the definitions below. For fastest resolution, please have 
hardware configuration, module types and version by slot, software version, and configuration file available for 
each switch. 
Severity 1 - Production network is down resulting in critical impact on business—no workaround available. 
Severity 2 - Segment or Ring is down or intermittent loss of connectivity across network. 
Severity 3 - Network performance is slow or impaired—no loss of connectivity or data. 
Severity 4 - Information or assistance on product feature, functionality, configuration, or installation.

<<<PAGE 51>>>
December 2025 
Page 51 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Third Party Licenses and Notices 
Legal Notices applicable to any software distributed alone or in connection with the product to which this 
document pertains, are contained in files within the software itself located at: /flash/foss. 
The following is in addition to the information found in the /flash/foss/Legal_Notice.txt file. 
FOSS Name : FOSS Version : Name of Applicable License : Pointer to file containing License 
Text 
 
libatomic           : 1.0.0      : GPLv3+ & GPLv3+      : /flash/foss/gpl-3.0.txt + 
                                   with exceptions &      /flash/foss/gpl-2.0.txt + 
                                   GPLv2+ with exceptions /flash/foss/lgpl-2.1.txt + 
                                   & LGPLv2+ & BSD        /flash/foss/bsd1.txt 
openvswitch         : 2.12.0     : Apache License 2.0   : /flash/foss/Apache-License-2.0.txt 
The Alcatel-Lucent name and logo are trademarks of Nokia used under license by ALE. To view other 
trademarks used by affiliated companies of ALE Holding, visit: www.al-enterprise.com/en/legal/trademarks-
copyright. All other trademarks are the property of their respective owners. The information presented is 
subject to change without notice. Neither ALE Holding nor any of its affiliates assumes any responsibility for 
inaccuracies contained herein. © Copyright 2024 ALE International, ALE USA Inc. All rights reserved in all 
countries.

<<<PAGE 52>>>
December 2025 
Page 52 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Appendix A: Feature Matrix 
The following is a feature matrix for AOS Release 8.10R4.  
Note: Early availability features are available in AOS and can be configured. However, they have not gone through the complete AOS validation cycle and are therefore not officially supported. 
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
Management Features 
 
 
 
 
 
 
 
 
 
 
 
AAA IPv6 Address Support 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
8.10R3 
AOS Micro Services (AMS) 
8.7R2 
8.6R1 
8.6R1 
8.9R2 
8.10R4 
8.6R1 
8.7R1 
8.6R1 
8.10R2 
8.6R1 
8.7R1 
N 
8.6R1 
Automatic Remote Configuration 
Download (RCL) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
Y 
Automatic/Intelligent Fabric 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R2 
Y 
8.10R2 
Y 
Y 
8.10R4 
Y 
Automatic VC 
8.7R2 
N 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
N 
N 
Bluetooth - USB Adapter with Bluetooth 
Technology 
8.7R2 
8.6R2 
8.6R2 
8.9R2 
8.10R4 
Y 
8.7R1 
8.6R2 
8.10R2 
8.6R2 
N 
N 
N 
Certify On Reboot 
8.10R2 
8.10R2 
8.10R2 
8.10R2 
8.10R4 
8.10R2 
N 
8.10R2 
8.10R2 
N 
N 
N 
N 
Console Disable 
8.7R2 
8.6R2 
8.6R2 
8.9R2 
8.10R4 
8.6R2 
8.7R1 
8.6R2 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
8.6R2 
Dying Gasp 
8.9R3 
Y 
Y 
8.9R3 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
N 
N 
Dying Gasp (EFM OAM / Link OAM) 
N 
8.6R1 
8.6R1 
8.9R3 
8.10R4 
8.6R1 
8.7R1 
8.6R1 
8.10R2 
N 
N 
N 
N 
EEE support  
Y 
8.9R1 
8.9R1 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R3 
Y 
Y 
N 
Y 
Embedded Python Scripting / Event 
Manager 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R2 
8.7R2 
8.10R4 
Y 
IP Managed Services 
N 
N 
N 
Y 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Hitless Security Patch Upgrade 
8.7R2 
8.7R1 
8.7R1 
8.9R2 
8.10R4 
8.7R1 
8.7R1 
8.7R1 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
8.7R1 
IPv4 In-Band Management over SPB 
N 
N 
N 
8.10R4 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
IPv6 In-Band Management over SPB 
N 
N 
N 
8.10R4 
8.10R4 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
N 
8.10R3 
ISSU 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Lightning Configuration 
8.9R4 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
N 
N 
NaaS 
8.8R1 
8.8R1 
8.8R1 
8.9R2 
8.10R4 
8.8R1 
8.8R1 
8.8R1 
8.10R2 
8.8R1 
8.8R1 
N/S 
8.8R1 
NAPALM Support 
8.7R2 
8.5R1 
8.5R1 
8.9R2 
8.10R4 
8.5R1 
8.7R1 
8.5R1 
8.10R3 
8.7R2 
8.7R2 
8.10R4 
N 
NTP - Version 4.2.8.p11 
8.7R2 
8.5R4 
8.5R4 
8.9R2 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
NTP - IPv6 
8.7R3 
8.7R3 
8.7R3 
8.9R2 
8.10R4 
8.7R3 
8.7R3 
8.7R3 
8.10R2 
8.7R3 
8.7R3 
8.10R4 
8.7R3 
OpenFlow 
N 
N 
N 
N 
N 
Y 
N 
N 
N 
N 
N 
N 
N

<<<PAGE 53>>>
December 2025 
Page 53 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
OV Cirrus – Zero touch provisioning 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R3 
8.7R2 
8.7R2 
8.10R4 
N 
OV Cirrus – Configurable NAS Address 
8.7R2 
8.5R4 
8.5R4 
8.9R2 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R3 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
OV Cirrus – Default Admin Password 
Change 
8.7R2 
8.5R4 
8.5R4 
8.9R2 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R3 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
OV Cirrus – Managed 
8.7R2 
8.5R4 
8.5R4 
8.9R2 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R3 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
OVSDB 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
Package Manager 
8.7R2 
8.6R2 
8.6R2 
8.9R2 
8.10R4 
8.6R2 
8.7R1 
8.6R2 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
8.6R2 
Profinet 
N 
8.10R3 
N 
N 
8.10R4 
N 
N 
N 
N 
N 
N 
N 
N 
Readable Event Log 
8.7R2 
8.6R1 
8.6R1 
8.9R2 
8.10R4 
8.6R1 
8.7R1 
8.6R1 
8.10R2 
8.6R1 
8.7R1 
8.10R4 
8.6R1 
Remote Chassis Detection (RCD) 
N 
N 
N 
N 
8.10R4 
8.6R2 
8.7R1 
N 
8.10R2 
N 
8.7R1 
8.10R4 
Y 
Reset to Factory Default 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
 
SAA 
8.7R2 
8.5R1 
8.9R1 
Metro 
8.9R2 
8.10R4 
Y 
8.7R2 
Y 
8.10R2 
8.7R1 
8.7R1 
N 
Y 
SAA SPB 
N 
N 
N 
8.10R4 
8.10R4 
Y 
8.7R2 
Y 
8.10R2 
8.7R1 
8.7R1 
N 
8.6R2 
SAA UNP 
N 
Y 
N 
8.10R4 
N 
Y 
N 
Y 
N 
N 
N 
N 
N 
Signed AOS Image 
8.10R1 
8.10R1 
8.10R1 
8.9R4 
8.10R4 
8.10R1 
8.10R1 
8.10R1 
8.10R2 
8.10R1 
8.10R1 
8.10R4 
8.10R1 
Site License Client/Manager (SILOS) 
N 
N 
N 
N 
N 
N 
N 
N 
Y 
N 
Y 
N 
N 
SNMP v1/v2/v3 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Thin Client 
8.8R1 
8.8R1 
8.8R1 
8.9R2 
8.10R4 
8.8R1 
8.8R1 
8.8R1 
8.10R3 
8.8R1 
8.8R1 
8.10R4 
8.8R1 
Secure Boot 
8.10R4 
8.10R4 
8.10R4 
8.10R4 
8.10R4 
N 
8.10R4 
N 
8.10R4 
N 
8.10R4 
8.10R4 
N 
Onie Authentication 
N 
N 
N 
N 
N 
N 
Y 
N 
Y 
Y 
Y 
Y 
N 
U-boot Enable/Disable/Authenticate 
8.7R3 
8.7R3 
8.7R3 
8.9R2 
8.10R4 
8.7R3 
N 
8.7R3 
N 
N 
N 
N 
8.7R3 
UDLD 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
X48C4E 
8.10R4 
EA 
USB Disaster Recovery 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
(onie) 
Y 
8.10R2 
(onie) 
8.7R1 
(onie) 
8.7R1 
(onie) 
8.10R4 
Y 
USB Flash (AOS) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
N 
N 
Virtual Chassis (VC) 
8.7R2 
8.5R2 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
N 
Y (9907) 
N (9912) 
Virtual Chassis Split Protection (VCSP) 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
N 
Y 
VRF 
N 
N 
N 
8.9R4 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y

<<<PAGE 54>>>
December 2025 
Page 54 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
VRF – IPv6 
N 
N 
N 
8.9R4 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
VRF – DHCP Client 
N 
N 
N 
8.9R4 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Web Services & CLI Scripting 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
 
 
 
 
 
 
 
 
 
 
 
Layer 3 Feature Support 
 
 
 
 
 
 
 
 
 
 
 
ARP 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
BFD 
N 
N 
8.10R4 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
BGP/MP-BGP 
N 
N 
8.10R46 
8.10R26 
N 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
DHCP Client / Server  
8.7R2 
8.6R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
Y 
DHCP Relay 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
Y 
DHCPv6 Server 
N 
N 
N 
Y 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
DHCPv6 Relay 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
DHCP Snooping / IP Source Filtering 
8.7R2 
8.5R4 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
Y 
ECMP 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
IGMP v1/v2/v3 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
GRE Tunneling 
N 
N 
N 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
N 
8.5R2 
IP-IP Tunneling 
N 
N 
N 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
N 
8.5R2 
IPv6 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
IPv6 - DHCPv6 Snooping 
8.7R2 
8.6R1 
8.6R1 
8.9R2 
8.10R4 
8.5R3 
8.7R1 
8.5R4 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
8.7R1 
IPv6 - Source filtering 
8.7R2 
N 
8.6R1 
8.9R2 
8.10R4 
8.5R3 
8.7R1 
8.5R4 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
8.7R1 
IPv6 - DHCP Guard 
EA 
EA 
EA 
8.9R2 
8.10R4 
EA 
N 
EA 
8.10R2 
N 
N 
8.10R4 
N 
IPv6 - DHCP Client Guard 
EA 
EA 
EA 
8.9R2 
8.10R4 
EA 
N 
EA 
8.10R2 
N 
N 
8.10R4 
N 
IPv6 - RA Guard (RA filter) 
Y 
Y 
8.5R2 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
Y 
Y 
8.10R4 
Y 
IPv6 - DHCP relay and Neighbor 
discovery proxy 
8.7R2 
8.5R1 
Y 
Y 
N 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
8.10R4 
Y 
IP Multinetting 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y

<<<PAGE 55>>>
December 2025 
Page 55 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
IPSec 
N 
N 
N 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
Y 
Y 
8.10R4 
N 
ISIS IPv4/IPv6 
N 
N 
N 
8.9R46 
N 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
8.5R2 
M-ISIS 
N 
N 
N 
N 
N 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
8.5R2 
OSPFv2 
N 
N 
8.9R41 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
OSPFv3 
N 
N 
8.9R41 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
RIP v1/v2 
N 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
RIPv2 RFC-4822 
N 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R3 
8.10R4 
8.10R3 
RIPng 
N 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
UDP Relay (IPv4) 
8.7R2 
8.5R4 
8.5R4 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
UDP Relay (IPv6) 
8.7R2 
8.6R1 
8.6R1 
8.9R2 
8.10R4 
8.6R1 
8.7R1 
8.6R 
8.10R2 
8.6R1 
8.7R1 
8.10R4 
8.6R1 
VRRP v2 
8.7R2 
8.5R2 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
VRRP v3 
8.7R2 
8.5R2 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Server Load Balancing (SLB) 
N 
N 
N 
N 
N 
Y 
8.9R4 
Y 
8.10R3 
8.9R4 
8.9R4 
N 
N 
Static routing  
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
 
 
 
 
 
 
 
 
 
 
 
Multicast Features 
 
 
 
 
 
 
 
 
 
 
 
DVMRP 
N 
N 
N 
N 
N 
Y 
8.7R1 
Y 
N 
8.5R2 
8.7R1 
N 
N 
IP Multicast VLAN (IPMVLAN) 
N 
8.9R3 
8.9R3 
Metro 
8.9R3 
8.10R4 
N 
N 
N 
8.10R2 
N 
N 
N 
N 
IPv4 Multicast Switching 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Multicast *,G 
8.7R2 
Y 
8.5R2 
8.9R2 
8.10R4 
8.5R2 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
IPv6 Multicast Switching 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
PIM-DM 
N 
N 
8.10R16 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
PIM-SM 
N 
N 
8.10R16 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
PIM-SSM 
N 
N 
8.10R16 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y

<<<PAGE 56>>>
December 2025 
Page 56 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
PIM-SSM Static Map 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
PIM-BiDir 
N 
N 
8.10R16 
8.9R46 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
PIM Message Packing 
N 
N 
8.10R16 
8.9R46 
8.10R4 
8.6R1 
8.7R1 
N 
8.10R2 
8.6R1 
8.7R1 
8.10R4 
N 
PIM - Anycast RP 
N 
N 
8.10R16 
8.9R46 
8.10R4 
8.6R2 
8.7R1 
8.6R2 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
8.6R2 
 
 
 
 
 
 
 
 
 
 
 
Monitoring/Troubleshooting Features 
 
 
 
 
 
 
 
 
 
 
 
Ping and traceroute 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Policy based mirroring 
N 
N 
N 
Y 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
8.5R4 
Port mirroring 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Port monitoring 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Port mirroring - remote 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R2 
8.7R2 
N 
8.6R1 
Port mirroring – remote over linkagg 
N 
N 
8.9R3 
8.10R4 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R2 
8.7R2 
N 
8.6R1 
RMON 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.8R2 
Y 
8.10R2 
8.8R2 
8.8R2 
8.10R4 
Y 
SFlow 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
Switch logging / Syslog 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
TDR 
8.9R3 
8.9R3 
8.9R3 
8.10R4 
8.10R4 
Y 
8.9R3 
Y 
8.10R3 
N 
N 
N 
N 
 
 
 
 
 
 
 
 
 
 
 
Layer 2 Feature Support 
 
 
 
 
 
 
 
 
 
 
 
802.1q 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
DHL 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
Y 
8.10R4 
N 
ERP v2 
8.9R3 
8.5R1 
8.5R2 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
N 
8.5R3 
HAVLAN 
N 
EA 
N 
8.10R4 
8.10R4 
Y 
8.8R1 
Y 
8.10R2 
8.6R2 
8.7R1 
N 
EA 
Link Aggregation (static and LACP) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
LLDP (802.1ab) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Loopback detection – Edge (Bridge) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
Y 
Loopback detection – SAP (Access) 
N 
N 
N 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
Y

<<<PAGE 57>>>
December 2025 
Page 57 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
MAC Forced Forwarding / Dynamic Proxy 
ARP 
8.7R2 
8.7R1 
N 
8.9R2 
8.10R4 
8.6R1 
N 
8.6R1 
8.10R2 
N 
N 
N 
N 
MPLS – VPLS 
N 
N 
N 
N 
N 
N 
8.9R3 
N 
N 
N 
8.10R2 
N 
N 
MPLS – VPWS 
N 
N 
N 
N 
N 
N 
8.10R2 
N 
N 
N 
8.10R2 
N 
N 
MRP 
N 
8.7R2 
N 
N 
8.10R4 
N 
N 
8.7R2 
N 
N 
N 
N 
N 
Port mapping 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
N 
Private VLANs (PVLAN) 
N 
N 
8.10R3 
8.10R4 
8.10R4 
Y 
8.7R2 
Y 
8.10R2 
N 
8.7R2 
N 
N 
SIP Snooping 
N 
N 
N 
N 
N 
Y 
N 
N 
N 
N 
N 
N 
N 
Spanning Tree (1X1, RSTP, MSTP) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Spanning Tree (PVST+, Loop Guard) 
N 
Y 
Y 
8.9R2 
8.10R4 
Y 
Y 
Y 
8.10R2 
Y 
Y 
N 
Y 
MVRP 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
Y 
SPB2 
N 
N 
N 
8.10R4 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
SPB - Over Shared Ethernet 
N 
N 
N 
8.10R4 
8.10R4 
8.7R1 
8.7R1 
8.7R1 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
8.7R1 
SPB – HW-based LSP flooding  
N 
N 
N 
N 
N 
8.6R1 
N 
8.6R1 
8.10R2 
N 
N 
N 
8.5R4 
QoS Feature Support 
 
 
 
 
 
 
 
 
 
 
 
802.1p / DSCP priority mapping 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
IPv4 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
IPv6 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Auto-Qos prioritization of NMS/IP Phone 
Traffic 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Auto-Qos – New MAC range 
8.7R2 
8.5R2 
8.5R2 
8.9R2 
8.10R4 
8.5R2 
8.7R1 
8.5R2 
8.10R2 
8.5R2 
8.7R1 
N 
8.5R2 
Groups - Port 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Groups - MAC 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Groups - Network 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Groups - Service 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Groups - Map 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Groups - Switch 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Groups – VLAN 
8.10R1 
8.10R1 
8.10R1 
8.10R1 
8.10R4 
8.10R1 
8.10R1 
8.10R1 
8.10R2 
8.10R1 
8.10R1 
8.10R4 
8.10R1

<<<PAGE 58>>>
December 2025 
Page 58 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
Ingress/Egress bandwidth limit 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
Per port rate limiting 
N 
N 
N 
Y 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
N 
Policy Lists 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
Policy Lists - Egress 
N 
N 
N 
Y 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
N 
Policy based routing 
N 
N 
Y 
8.9R4 
N 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
8.10R4 
8.9R4 
Tri-color marking 
N 
N 
N 
Y 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
8.10R4 
N 
QSP Profiles 1 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
QSP Profiles 2/3/4 
N 
N 
N 
QSP-2 
Only 
QSP-2 
Only 
Y 
QSP-2 
only 
Y 
QSP-2 
only 
QSP-2 
only 
QSP-2 only 
QSP-2 
Only 
N 
QSP Profiles 5 
8.7R2 
8.5R1 
Y 
Same as 
QSP-2 
Same as 
QSP-2 
8.7R1 
Same as 
QSP-2 
8.7R1 
Same as 
QSP-2 
Same as 
QSP-2 
Same as QSP-2 
Same as 
QSP-2 
Y 
RoCEv2 
N 
N 
N 
N 
N 
N 
N 
N 
N 
8.7R2 
8.10R3 (EA) 
8.10R4 
N 
Custom QSP Profiles 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
Y 
Y 
8.10R2 
Y 
Y 
8.10R4 
Y 
GOOSE Messaging Prioritization 
N 
8.7R1 
N 
N 
8.10R4 
N 
N 
8.7R1 
N 
N 
N 
N 
N 
Services Support 
N 
N 
N 
N 
8.10R4 
N 
Y 
N 
Y 
Y 
Y 
8.10R4 
Y 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Metro Ethernet Features 
 
 
 
 
 
 
 
 
 
 
 
CPE Test Head 
N 
8.6R1 
8.9R1 
Metro 
8.9R2 
8.10R4 
N 
N 
N 
8.10R3 
(EA) 
8.10R4 
(GA) 
N 
N 
N 
N 
Ethernet Loopback Test 
N 
Y 
8.9R1 
Metro 
8.9R2 
8.10R4 
8.6R1 
N 
8.6R1 
8.10R3 
N 
N 
N 
N 
Ethernet Services (VLAN Stacking) 
N 
8.5R1 
8.9R1 
Metro 
8.9R2 
8.10R4 
Y 
8.7R2 
Y 
8.10R2 
8.5R4 
8.7R1 
N 
N 
Ethernet OAM (ITU Y1731 and 802.1ag) 
N 
8.5R1 
8.9R1 
Metro 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
N 
EA 
EFM OAM / Link OAM (802.3ah) 
 
N 
8.6R1 
8.9R1 
Metro 
8.9R2 
8.10R4 
8.5R4 
8.7R2 
8.5R4 
8.10R2 
N 
N 
N 
N 
Transparent Bridging 
N 
N 
N 
8.10R4 
8.10R4 
Y 
Y 
Y 
8.10R2 
Y 
Y 
N 
N 
PPPoE Intermediate Agent 
N 
8.6R1 
8.9R1 
Metro 
8.9R2 
8.10R4 
N 
N 
8.6R1 
N 
N 
N 
N 
N 
Precision Time Protocol (PTP 1588v2) 
End-to-End Transparent Clock 
N 
8.5R1 
8.7R2 
8.10R3 
8.10R4 
Y 
8.9R3 
Y 
8.10R2 
N 
8.9R3 
(except C32E) 
N 
N

<<<PAGE 59>>>
December 2025 
Page 59 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
Precision Time Protocol (PTP 1588v2) 
Peer-to-Peer Transparent Clock 
N 
8.8R2 
8.7R2 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
Precision Time Protocol (PTP 1588v2) 
Across VC 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
Access Guardian / Security Features 
 
 
 
 
 
 
 
 
 
 
 
802.1x Authentication 
8.7R2 
8.5R2 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
Access Guardian – Bridge 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R1 
8.7R1 
8.10R4 
Y 
Access Guardian - Access 
N 
N 
N 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R4 
8.7R1 
N 
Y 
Application Fingerprinting 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
Application Monitoring and Enforcement 
(Appmon / DPI) 
N 
N 
N 
N 
N 
Y 
8.7R2 
N 
8.10R27 
(EA) 
8.10R4 
(GA) 
N 
N 
N 
N 
ARP Poisoning Protection 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R2 
8.7R1 
8.10R4 
Y 
BYOD - COA Extension support for 
RADIUS 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
N 
Y 
BYOD - mDNS Snooping/Relay 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R3 
8.6R2 
8.7R1 
N 
Y 
BYOD - UPNP/DLNA Relay 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R3 
8.6R2 
8.7R1 
N 
Y 
BYOD - Switch Port location information 
pass-through in RADIUS requests  
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
N 
Y 
Captive Portal 
8.7R2 
8.5R4 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R2 
8.7R1 
N 
Y 
IoT Device Profiling 
8.7R2 
8.5R2 
8.5R2 
8.9R2 
8.10R4 
8.5R2 
8.7R1 
8.5R2 
8.10R3 
8.6R1 
8.7R1 
N 
8.5R2 
IoT Device Profiling (IPv6) 
8.7R2 
8.7R1 
8.7R1 
8.9R2 
8.10R4 
8.7R15 
8.9R3 
8.7R15 
 
8.10R3 
8.9R3 
8.9R3 
N 
8.7R1 
Directed Broadcasts – Control 
8.7R2 
8.5R2 
8.5R2 
8.9R2 
8.10R4 
8.5R2 
8.7R1 
8.5R2 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
Interface Violation Recovery 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R1 
8.7R1 
8.10R4 
Y 
Kerberos Snooping 
8.7R2 
Y 
8.6R2 
N 
8.10R4 
8.6R2 
Y 
8.6R2 
8.10R2 
8.6R2 
Y 
N 
8.6R2 
L2 GRE Tunnel Access (Edge) (bridge 
ports) 
N 
N 
Y 
N 
N 
Y 
8.9R1 
Y 
8.10R2 
N 
N 
N 
Y 
L2 GRE Tunnel Access (Edge) (access 
ports) 
N 
N 
N 
N 
N 
8.6R1 
8.9R1 
8.6R1 
8.10R2 
8.7R1 
8.7R2 
N 
8.6R1 
L2 GRE Tunnel Aggregation 
N 
N 
N 
N 
N 
Y 
8.9R1 
Y 
8.10R2 
8.7R1 
8.7R2 
N 
Y 
Learned Port Security (LPS) 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
Y

<<<PAGE 60>>>
December 2025 
Page 60 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
MACsec3 
N 
8.5R1 
8.5R4 
8.10R2 
8.10R4 
Y 
8.7R1 
N 
8.10R2 
N 
X48C4E 
N 
8.5R2 
MACsec on Network Port for 
SPB/L2GRE/VxLAN 
N 
N 
N 
N 
8.10R4 
8.9R1 
(6860E) 
8.9R1 
N 
8.10R2 
N 
8.9R1 
(X48C4E) 
N 
N 
Quarantine Manager 
N 
8.7R2 
8.7R2 
8.9R2 
8.10R4 
Y 
8.7R2 
Y 
8.10R2 
8.7R2 
8.7R2 
N 
8.7R2 
RADIUS - RFC-2868 Support 
8.7R2 
8.5R4 
8.5R4 
8.9R2 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R2 
8.5R4 
8.7R1 
8.10R4 
8.5R4 
Role-based Authentication for Routed 
Domains 
N 
N 
N 
8.10R4 
8.10R4 
8.5R4 
8.7R1 
8.5R4 
8.10R2 
8.6R1 
8.7R1 
N 
8.5R4 
Storm Control (flood-limit) 
8.7R2 
Y 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
Y 
8.7R1 
8.10R4 
Y 
Storm Control (Unknown unicast with 
action trap/shutdown) 
N 
N 
N 
N 
8.10R4 
Y 
N 
Y 
8.10R2 
N 
N 
N 
N 
TACACS+ Client 
8.7R2 
8.5R1 
Y 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.6R1 
8.7R1 
8.10R4 
Y 
TACACS+ command based authorization 
8.7R2 
N 
N 
8.9R2 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
8.7R2 
8.7R2 
8.10R4 
N 
TACACS+ - IPv6 
8.7R3 
8.7R3 
8.7R3 
8.9R2 
8.10R4 
8.7R3 
8.7R3 
8.7R3 
8.10R2 
8.7R3 
8.7R3 
8.10R4 
8.7R3 
PoE Features 
 
 
 
 
 
 
 
 
 
 
 
802.3af and 802.3at 
8.7R2 
8.5R1 
Y 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
N 
Y 
802.3bt 
8.7R2 
Y 
8.6R2 
N 
8.10R4 
N 
8.7R1 
Y 
8.10R2 
N 
N 
N 
N 
Auto Negotiation of PoE Class-power 
upper limit 
8.7R2 
8.5R1 
Y 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
N 
Y 
Display of detected power class 
8.7R2 
8.5R1 
Y 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
N 
Y 
LLDP/802.3at power management TLV 
8.7R2 
8.5R1 
Y 
N 
8.10R4 
Y 
8.7R1 
Y 
8.10R2 
N 
N 
N 
Y 
HPOE support 
8.7R2 
(95W) 
8.5R1 
(60W) 
Y (95W) 
N 
8.10R4 
Y  
(60W) 
8.7R1 
(95W) 
Y (75W) 
8.10R2 
N 
N 
N 
Y (75W) 
Time Of Day Support 
8.7R2 
8.5R1 
Y 
N 
8.10R4 
Y 
 
Y 
8.10R2 
N 
N 
N 
Y 
Perpetual PoE 
8.7R2 
N 
N 
N 
8.10R4 
Y 
Y 
Y 
8.10R2 
N 
N 
N 
N 
Fast PoE 
8.7R2 
N 
N 
N 
8.10R4 
Y 
Y 
Y 
8.10R2 
N 
N 
N 
N 
Delayed Start 
8.9R3 
8.9R3 
8.9R3 
N 
N 
N 
N 
N 
8.10R2 
N 
N 
 
N 
Data Center Features (License May Be 
Required) 
 
 
 
 
 
 
 
 
 
 
 
CEE DCBX Version 1.01 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
Data Center Bridging (DCBX/ETS/PFC) 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
DCBX 
with 
LLDP 
 
N 
EVB 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
FCoE / FC Gateway 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N

<<<PAGE 61>>>
December 2025 
Page 61 of 105 
 
 
 
 
                                 OmniSwitch AOS Release 8.10R4 - Rev. A  
Feature 
6360 
6465 
6560 
OS6570M 
6575 
6860(E) 
6860N 
6865 
6870 
6900- 
V72/ 
C32 
6900- 
X48C6/ 
T48C6/X48C4E/V48C8/C32E
T24C2/X24C2 
6920 
9900 
VxLAN4 
N 
N 
N 
N 
N 
N 
8.8R1 
N 
8.10R2 
8.5R3 
8.8R1 
N 
N 
EVPN VxLAN 
N 
N 
N 
N 
N 
N 
N 
N 
8.10R4 
N 
8.10R1 
N 
N 
EVPN - Route Redistribution for Prefix 
Route Advertisement for Symmetric IRB 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
8.10R3 
N 
N 
EVPN - BGP NBR Template and 
Scalability 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
8.10R3 
N 
N 
EVPN - VRF-based Tenancy Model for 
AOS EVPN Services 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
8.10R3 
N 
N 
EVPN - Multicast Routing Over an EVPN 
Fabric (RFC 9625) - OISM & PIM Support 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
8.10R3 (EA) 
8.10R4 (GA) 
N 
N 
VM/VxLAN Snooping 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
FIP Snooping 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
N 
Notes: 
1. OS6560 supports 2 OSPF areas with Advanced Routing license. 
2. See protocol support table in Appendix C. 
3. Site license required beginning in 8.6R1. 
4. L2 head-end only on OS6900-V72/C32. 
5. HTTP IPv6 only supported on OS6860(E) and OS6865 
6. Advanced Routing license required. 
7. Monitoring functionality only. Enforcement is not supported.

<<<PAGE 62>>>
December 2025 
Page 62 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Appendix B: MACsec Platform Support 
The following table lists the platforms and modules that support the MACsec functionality.  
MACsec Support 
(MACsec site license required) 
 
 
OmniSwitch 9900 
 
OS99-CMM 
4X10G mode only -  Static and Dynamic (128-bit) modes 
OS99-CMM2 
Ports 1-4 (40G, 100G,4x10G,4x25G) – Dynamic (256-bit) mode 
OS99-GNI-48/P48 
10M/100M/1G ports - Static and Dynamic (128-bit) modes 
OS99-XNI-48/P48 
10G ports - Static and Dynamic (128-bit) modes 
OS99-XNI-U48 
10G ports - Static and Dynamic (128-bit) modes 
OS99-XNI-P48Z16 
1G/2.5G/5G/10G (16x) - Static and Dynamic (128-bit) modes 
1G/10G (32x) - Static and Dynamic (128-bit) modes 
OS99-GNI-U48 
1G ports - Static and Dynamic (128-bit) modes 
OS99-XNI-U24 
10G ports -  Static and Dynamic (128-bit) modes 
OS99-XNI-P24Z8 
1G/2.5G/5G/10G (8x) - Static and Dynamic (128-bit) modes 
1G/10G (16x) - Static and Dynamic (128-bit) modes 
OS99-XNI-U12Q 
10G / 4x10G Uplink -  Static and Dynamic (128-bit) modes 
OS99-XNI-UP24Q2 
10G(Fiber)/4x10G Uplink -  Static and Dynamic (128-bit) modes 
10G (Copper) -  Static and Dynamic (128-bit) modes 
OS99-CNI-U8 
Not Supported 
OS99-CNI-U20 
40G/100G - Static and Dynamic (256-bit) modes 
 
 
OmniSwitch 6900 
 
OS6900-X48C4E 
Dynamic mode only on all ports. Supports 256-bit key length. 
 
 
OmniSwitch 6870 
Dynamic (256-bit) mode 
OS6870-24  
Port 1-24 (10M,100M,1G)  
Port 25-26 - Not Supported 
Port 27-30 (10G, 25G) 
OS6870-P24M 
Port 1-24 (1G, 2.5G, 5G, 10G)  
Port: 25-26 (40G, 100G, 200G, 4X10G, 4X25G)  
OS6870-P24Z 
Port 1-24 (100M,1G,2.5G) 
Port: 25-26 (40G, 100G,4x10G,4x25G) 
Port 27-32 (10G, 25G) 
OS6870-48 
Port 1-48 (10M,100M,1G) 
 
Port 49-50 - Not Supported 
Port 51-54 (10G, 25G) 
OS6870-P48M 
Port 1-48 (1G, 2.5G, 5G, 10G)  
Port: 49-50 (40G, 100G, 200G, 4X10G, 4X25G) 
OS6870-P48Z 
Port 1-48 (100M,1G,2.5G) 
Port: 49-50 (40G, 100G, 4x10G, 4x25G) 
Port 51-56 (10G, 25G) 
OS6870-V12 
Port 1-12 (10G, 25G) 
 
Port: 13-14 (40G, 100G, 200G, 4X10G, 4X25G) 
OS6870-CNIU2 
Port 1-2  (40G, 100G, 4x10G, 4x25G) 
OS6870-LNIU6 
Port 1-6 (10G,25G,50G) 
Note: The OS6870 does not support MACsec on ports in VFL mode. 
 
 
OmniSwitch 6860(E) 
 
OS6860(E)  
All models support MACsec on 10G ports. 
OS6860E-P24  
1G/10G ports. 
OS6860E-P24Z8 
1G/10G ports (not supported on 2.5G ports).

<<<PAGE 63>>>
December 2025 
Page 63 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
 
 
 
OmniSwitch 6860N 
Dynamic mode only. All OS6860N models support 128-bit key length. 
OS6860N-U28 
SFP (1-24), SFP+ (25-28) and SFP28 (31-34) ports 
OS6860N-P48Z 
SFP28 (51-54) ports 
OS6860N-P48M 
- Expansion modules (Not supported on any 4X10G splitter transceivers). 
- Multi-rate Gigabit Ports (37-48) 
OS6860N-P24Z 
SFP28 (27-30) ports 
OS6860N-P24M 
- Expansion modules (Not supported on any 4X10G splitter transceivers) 
- Multi-rate Gigabit Ports (1-24) 
 
 
OmniSwitch 6570M 
Dynamic (256-bit) mode 
OS6570M-12/12D 
Ports 1-8 (10M/100M/1G) 
Ports 9-10 (1G) 
Ports 11-12 (1G/10G) 
OS6570M-U28 
Ports 1-24 (1G) 
Ports 25-30 (1G/10G) 
 
 
OmniSwitch 6575 
Dynamic (256-bit) mode 
OS6575-P12 
Ports 1-8 (10M/100M/1G) 
Ports 9-12 (1G/10G) 
OS6575-MP16 
Ports 1-8 (10M/100M) 
Ports 9-16 (10M/100M/1G) 
OS6575-U28 
Ports 1-4 (1G Hybrid) 
Ports 5-24 (1G) 
Ports 25-28 (1G/10G) 
 
 
OS6560-P24X4/24X4 
 
- Ports 1-24 (Static and Dynamic modes) 
- Ports 25-30 (Not Supported) 
OS6560-P48X4/48X4 
- Ports 1-48 (Static and Dynamic modes) 
- Ports 49-52 (Dynamic mode only)  
- Ports 53-54 (Not Supported) 
OS6560-P48Z16  
(904044-90 only) 
 
- Ports 1-32 (Static and Dynamic Modes) 
- Ports 33-48 (Static and Dynamic modes) 
- Ports 49-52 (Dynamic mode only) 
- Ports 53-54 (Not Supported) 
OS6560E-P48Z16 
 
- Ports 1-32 (Static and Dynamic Modes) 
- Ports 33-48 (Static and Dynamic modes) 
- Ports 49-52 (Dynamic mode only) 
- Ports 53-54 (Not Supported) 
OS6560-X10 
 
- Ports 1-8 (10G ports only. Dynamic mode only) 
- Ports 9-10 (Not Supported) 
 
 
OmniSwitch 6465 
- OS6465-P28 - Supported on all ports except ports 27 and 28. 
- OS6465T-12 and OS6465T-P12 – Not supported on ports 11 and 12. 
- All other models support MACsec on all ports.

<<<PAGE 64>>>
December 2025 
Page 64 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Appendix C: SPB L3 VPN-Lite Service-based (Inline Routing) / External Loopback Support 
/ BVLAN Guidelines 
The OmniSwitch supports SPB L3 VPN-Lite using either service-based (inline routing) or external loopback. The 
tables below summarize the currently supported protocols for each method in this release.  
 
 
OmniSwitch Inline Routing Support 
 
 
9900 
6900-
V72/C32 
(Front panel 
port) 
6900-
T48C6/X48C6 
6900-
X48C4E/V48C8 
6900-C32E 
6860N 
6900-
X/T24C2 
6870 
IPv4 
Protocols 
 
 
 
 
 
 
 
 
Static 
Routing 
Y 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
RIP v1/v2 
Y 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
OSPF 
Y 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
BGP 
Y 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
VRRP 
Y 
8.7R1 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IS-IS 
N 
N 
N 
N 
N 
N 
N 
N 
PIM-SM/DM 
8.5R3 
8.6R2 
Y 
Y 
8.8R1 
Y 
8.9R1 
8.10R2 
DHCP Relay 
8.5R3 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
UDP Relay 
8.5R4 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
DVMRP  
N 
N 
N 
N 
N 
N 
N 
N 
BFD 
8.7R2 
8.7R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IGMP 
Snooping 
Y 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IP Multicast 
Headend 
Mode 
Y 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IP Multicast 
Tandem 
Mode 
8.5R4 
8.6R2 
8.8R1 
8.8R1 
8.8R1 
8.8R1 
8.9R1 
8.10R2 
 
 
 
 
 
 
 
 
 
IPv6 
Protocols 
 
 
 
 
 
 
 
 
Static 
Routing 
8.5R4 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
RIPng 
8.5R4 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
OSPFv3 
8.5R4 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
BGP 
8.5R4 
8.6R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
VRRPv3 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IS-IS 
N 
N 
N 
N 
N 
N 
N 
N 
PIM-SM/DM 
8.5R4 
8.6R2 
8.8R1 
8.8R1 
8.8R1 
8.8R1 
8.9R1 
8.10R2 
DHCP Relay 
8.6R1 
8.7R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
UDP Relay 
8.6R1 
8.7R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
BFD 
8.7R2 
8.7R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IPv6 MLD 
Snooping 
Y 
8.7R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IPv6 
Multicast 
Headend 
Mode 
Y 
8.7R2 
8.7R2 
8.7R3 
8.8R1 
8.7R2 
8.9R1 
8.10R2 
IPv6 
Multicast 
Tandem 
Mode 
8.5R4 
8.7R2 
8.8R1 
8.8R1 
8.8R1 
8.8R1 
8.9R1 
8.10R2

<<<PAGE 65>>>
December 2025 
Page 65 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
 
 
SPB BVLAN Scalability and Convergence Guidelines 
If services are distributed across more than 4 BVLANs in the network it is recommended to consolidate them 
among just 4 BVLANs. This will reduce the scale of address updates that will happen in the control plane and 
also help improve network scalability, stability and convergence. Modifying the service BVLAN association is 
currently not supported. The service will need to be deleted and recreated on the new BVLAN, therefore it's 
suggested that the consolidation be done during a maintenance window to prevent network disruption. 
 
In most SPB networks this is not a local operation on a single switch. The BVLAN is configured on all the 
switches in the network. A check must be performed to see if any service has been attached to the BVLAN. The 
check does not have to be on a local switch, the service attachment to the BVLAN can be on any switch in the 
network. 
External Loopback Support 
 
 
OmniSwitch 
9900 
OmniSwitch 
6860/6865 
OmniSwitch 
6860N 
OmniSwitch  
6900-V72/ 
C32 
OmniSwitch  
6900-X48C6/ 
T48C6 
OmniSwitch  
6900-X48C4E 
OmniSwitch  
6900-V48C8 
OmniSwitch  
6900-X/T48C2 
IPv4 Protocols 
Static Routing 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
RIP v1/v2 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
OSPF 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
BGP 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
VRRP 
8.6R1 
8.5R4 
8.7R1 
8.7R1 
8.7R2 
8.7R2 
8.7R3 
8.9R1 
IS-IS 
Y 
Y 
Y 
Y 
Y 
8.7R2 
8.7R3 
8.9R1 
PIM-SM/DM 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
DHCP Relay 
8.5R4 
8.5R4 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
UDP Relay 
8.5R4 
8.5R4 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
DVMRP  
N 
N 
N 
N 
N 
N 
N 
N 
BFD 
Y 
Y 
Y 
Y 
Y 
8.7R2 
8.7R3 
8.9R1 
IGMP Snooping 
8.5R4 
Y 
8.7R1 
8.6R1 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
IP Multicast 
Headend Mode 
8.5R4 
Y 
8.7R1 
8.6R1 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
IP Multicast 
Tandem Mode 
8.5R4 
Y 
8.7R1 
8.6R1 
Y 
Y 
Y 
8.9R1 
 
 
 
 
 
 
 
 
 
IPv6 Protocols 
 
 
 
 
 
 
 
 
Static Routing 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
RIPng 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
OSPFv3 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
BGP 
8.5R4 
Y 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
VRRPv3 
8.5R4 
8.5R4 
8.7R1 
8.7R1 
8.7R2 
8.7R2 
8.7R3 
8.9R1 
IS-IS 
Y 
Y 
Y 
Y 
Y 
8.7R2 
8.7R3 
8.9R1 
PIM-SM/DM 
8.5R4 
8.5R4 
8.7R1 
8.5R4 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
DHCP Relay 
8.6R1 
8.6R1 
8.7R1 
8.6R1 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
UDP Relay 
8.6R1 
8.6R1 
8.7R1 
8.6R1 
8.7R1 
8.7R2 
8.7R3 
8.9R1 
BFD 
Y 
Y 
Y 
Y 
Y 
8.7R2 
8.7R3 
8.9R1 
IPv6 MLD 
Snooping 
8.5R4 
Y 
8.7R1 
Y 
8.7R2 
8.7R2 
8.7R3 
8.9R1 
IPv6 Multicast 
Headend Mode 
8.5R4 
Y 
8.7R1 
Y 
8.7R2 
8.7R2 
8.7R3 
8.9R1 
IPv6 Multicast 
Tandem Mode 
8.5R4 
Y 
8.7R1 
Y 
Y 
Y 
Y 
8.9R1

<<<PAGE 66>>>
December 2025 
Page 66 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
This will indicate that this is an active BVLAN. 
Even if the service is not local to a node the node can act as a transit node for the active BVLAN. For this 
reason the BVLAN cannot be deleted from the network.  
 
To determine if a BVLAN is active use the following command. If there is a service associated with the BVLAN 
then In Use will show as Yes.  This is a network wide view so even if the services are active on a remote node, 
this local node will show that the BLVAN is active even if the services are not configured on the local node. 
 
OS6860-> show spb isis bvlans 
SPB ISIS BVLANS: 
                                                              Services  Num    Tandem     
Root Bridge 
BVLAN   ECT-algorithm     In Use  mapped    ISIDS  Multicast  (Name : MAC Address) 
-------+-----------------+-------+---------+------+----------+-------------------------------
--------- 
  4000  00-80-c2-01       YES     YES           5  SGMODE 
  4001  00-80-c2-02       NO      NO            0  SGMODE 
 
After the services have been consolidated the idle BVLANs can be deleted across the entire network. 
Deleting idle BVLANs will have no eﬀect on the existing network.

<<<PAGE 67>>>
December 2025 
Page 67 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Appendix D: General Upgrade Requirements and Best Practices 
This section is to assist with upgrading an OmniSwitch. The goal is to provide a clear understanding of the steps 
required and to answer any questions about the upgrade process prior to upgrading. Depending upon the AOS 
version, model, and configuration of the OmniSwitch various upgrade procedures are supported.  
 
Standard Upgrade - The standard upgrade of a standalone chassis or virtual chassis (VC) is nearly 
 
identical. All that’s required is to upload the new image files to the Running directory and reload the 
 
switch. In the case of a VC, prior to rebooting the Master will copy the new image files to the Slave(s) 
 
and once the VC is back up the entire VC will be synchronized and running with the upgraded code. 
 
ISSU - The In Service Software Upgrade (ISSU) is used to upgrade the software on a VC or modular 
 
chassis with minimal network disruption. Each element of the VC is upgraded individually allowing 
 
hosts and switches which are dual-homed to the VC to maintain connectivity to the network. The 
 
actual downtime experienced by a host on the network should be minimal but can vary  depending upon 
 
the overall network design and VC configuration. Having a redundant configuration is suggested and 
 
will help to minimize recovery times resulting in sub-second convergence times. 
 
 
Virtual Chassis - The VC will first verify that it is in a state that will allow a successful ISSU  
 
 
upgrade. It will then copy the image and configuration files of the ISSU specified directory  
 
 
to all of the Slave chassis and reload each Slave chassis from the ISSU directory in order from  
 
 
lowest to highest chassis-id. For example, assuming chassid-id 1 is the Master, the Slave  
 
 
with chassis-id 2 will reload with the new image files. When Slave chassis-id 2 has rebooted  
 
 
and rejoined the VC, the Slave with chassis -id 3 will reboot and rejoin the VC. Once the  
 
 
Slaves are complete they are now using the new image files. The Master chassis is now   
 
 
rebooted which causes the Slave chassis to become the new Master chassis. When the original  
 
 
Master chassis reloads it comes back as a Slave chassis. To restore the role of Master to the  
 
 
original Master chassis the current Master can be rebooted and the original Master will   
 
 
takeover, re-assuming the Master role. 
 
 
Modular Chassis - The chassis will first verify that it is in a state that will allow a successful  
 
 
ISSU upgrade. It will then copy  the image and configuration files of the ISSU specified directory 
 
 
to the secondary CMM and reload the secondary CMM which becomes the new primary CMM.  
 
 
The old primary CMM becomes the secondary CMM and reloads using the upgraded code. As a  
 
 
result of this process both CMMs are now running with the upgraded code and the primary and  
 
 
secondary CMMs will have changed roles (i.e., primary will act as secondary and the secondary  
 
 
as primary). The individual NIs can be reset either manually or automatically (based on the NI  
 
 
reset timer).

<<<PAGE 68>>>
December 2025 
Page 68 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Supported Upgrade Paths and Procedures 
The following releases support upgrading using ISSU. All other releases support a Standard upgrade only.   
Platform 
AOS Releases Supporting ISSU to 8.10R4 (GA) 
OS6360 
ISSU not supported. 
OS6465 
ISSU not supported. 
OS6560 
ISSU not supported. 
OS6560E 
ISSU not supported. 
OS6570M 
ISSU not supported. 
OS6860(E) 
8.10.91.R03 (GA) 
8.10.105.R02 (GA) 
8.10.115.R01 (MR) 
8.10.102.R01 (GA) 
8.9.144.R04 (MR2)  
8.9.130.R04 (MR1)  
8.9.94.R04 (GA)  
8.9.92.R04 (GA)  
OS6860N 
8.10.91.R03 (GA) 
8.10.105.R02 (GA) 
8.10.115.R01 (MR) 
8.10.102.R01 (GA) 
8.9.144.R04 (MR2)  
8.9.130.R04 (MR1)  
8.9.94.R04 (GA)  
8.9.92.R04 (GA)  
OS6865 
8.10.91.R03 (GA) 
8.10.105.R02 (GA) 
8.10.115.R01 (MR) 
8.10.102.R01 (GA) 
8.9.144.R04 (MR2)  
8.9.130.R04 (MR1)  
8.9.94.R04 (GA)  
8.9.92.R04 (GA)  
OS6870 
8.10.91.R03 (GA) 
8.10.105.R02 (GA) 
OS6900-V72/C32/C32E 
X48C6/T48C6/V48C8/ 
X24C2/T24C2/X48C4E 
8.10.91.R03 (GA) 
8.10.105.R02 (GA) 
8.10.115.R01 (MR) 
8.10.102.R01 (GA) 
8.9.144.R04 (MR2)  
8.9.130.R04 (MR1)  
8.9.94.R04 (GA)  
8.9.92.R04 (GA)

<<<PAGE 69>>>
December 2025 
Page 69 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
OS9900 
8.10.91.R03 (GA) 
8.10.106.R02 (GA) 
8.10.102.R01 (GA) 
8.9.144.R04 (MR2)  
8.9.130.R04 (MR1)  
8.9.94.R04 (GA)  
Note: ISSU is not supported on the OS6360, OS6465, OS6560 or OS6570M platforms due to U-boot upgrade 
requirement for Secure Boot.  
8.10R4 ISSU Supported Releases 
Prerequisites 
These upgrade instructions require that the following conditions exist, or are performed, before upgrading. The 
person performing the upgrade must: 
• 
Be the responsible party for maintaining the switch’s configuration. 
• 
Be aware of any issues that may arise from a network outage caused by improperly loading this 
code. 
• 
Understand that the switch must be rebooted and network access may be affected by following this 
procedure. 
• 
Have a working knowledge of the switch to configure it to accept an FTP connection through the 
EMP or Network Interface (NI) Ethernet port. 
• 
Read the GA Release Notes prior to performing any upgrade for information specific to this release.  
• 
Ensure there is a current certified configuration on the switch so that the upgrade can be rolled-
back if required.  
• 
Verify the current versions of U-Boot and FPGA. If they meet the minimum requirements, (i.e. they 
were already upgraded during a previous AOS upgrade) then only an upgrade of the AOS images is 
required.  
• 
Depending on whether a standalone chassis or VC is being upgraded, upgrading can take from 5 to 
20 minutes. Additional time will be needed for the network to re-converge.  
• 
The examples below use various models and directories to demonstrate the upgrade procedure.  
However, any user-defined directory can be used for the upgrade.  
• 
If possible, have EMP or serial console access to all chassis during the upgrade. This will allow you to 
access and monitor the VC during the ISSU process and before the virtual chassis has been re-
established. 
• 
Knowledge of various aspects of AOS directory structure, operation and CLI commands can be found 
in the Alcatel-Lucent OmniSwitch User Guides. Recommended reading includes: 
o 
Release Notes - for the version of software you’re planning to upgrade to. 
o 
The AOS Switch Management Guide 
 
Chapter – Getting Started  
 
Chapter - Logging Into the Switch 
 
Chapter - Managing System Files 
 
Chapter - Managing CMM Directory Content 
 
Chapter - Using the CLI

<<<PAGE 70>>>
December 2025 
Page 70 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
 
Chapter - Working With Configuration Files 
 
Chapter - Configuring Virtual Chassis 
 
Do not proceed until all the above prerequisites have been met. Any deviation from these upgrade procedures 
could result in the malfunctioning of the switch. All steps in these procedures should be reviewed before 
beginning. 
Switch Maintenance  
It’s recommended to perform switch maintenance prior to performing any upgrade. This can help with 
preparing for the upgrade and removing unnecessary files. The following steps can be performed at any time 
prior to a software upgrade. These procedures can be done using Telnet and FTP, however using SSH and 
SFTP/SCP are recommended as a security best-practice since Telnet and FTP are not secure. 
 
1. Use the command ‘show system’ to verify current date, time, AOS and model of the switch.  
 
 
OS6860-> show system 
 
System: 
   
 Description:  Alcatel-Lucent OS6860-P24 8.9.94.R04 GA, March 28, 2024., 
  
 Object ID:    1.3.6.1.4.1.6486.801.1.1.2.11.1.2, 
   
 Up Time:      88 days 2 hours 1 minutes and 44 seconds, 
   
 Contact:      Alcatel-Lucent, https://www.al-enterprise.com, 
   
 Name:         OS6860, 
   
 Location:     Unknown, 
   
 Services:     78, 
   
 Date & Time:  FRI OCT 11 2024 06:55:43 (PDT) 
 
Flash Space: 
     
 Primary CMM: 
         Available (bytes):  1084694528, 
          Comments         :  None 
 
2.  Remove any old tech_support.log files, tech_support_eng.tar files: 
 
 
OS6860-> rm *.log 
 
OS6860-> rm *.tar 
 
3. Verify that the /flash/pmd and /flash/pmd/work directories are empty. If they have files in them check the 
date on the files. If they are recently created files (<10 days), contact Service & Support. If not, they can be 
deleted.  
 
4. Use the ‘show running-directory’ command to determine what directory the switch is running from and that 
the configuration is certified and synchronized: 
 
 
OS6860-> show running-directory 
 
CONFIGURATION STATUS 
   
Running CMM              : MASTER-PRIMARY, 
   
CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
   
Current CMM Slot         : CHASSIS-1 A, 
   
Running configuration    : vc_dir, 
   
Certify/Restore Status   : CERTIFIED 
 
SYNCHRONIZATION STATUS 
   
Running Configuration    : SYNCHRONIZED

<<<PAGE 71>>>
December 2025 
Page 71 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
If the configuration is not certified and synchronized, issue the command ‘write memory flash-synchro’: 
 
 
OS6860-> write memory flash-synchro 
 
6. If you do not already have established baselines to determine the health of the switch you are upgrading, 
now would be a good time to collect them. Using the show tech-support series of commands is an excellent 
way to collect data on the state of the switch. The show tech support commands automatically create log files 
of useful show commands in the /flash directory. You can create the tech-support log files with the following 
commands: 
 
 
OS6860-> show tech-support  
 
OS6860-> show tech-support layer2 
 
OS6860-> show tech-support layer3 
 
Additionally, the ‘show tech-support eng complete’ command will create a TAR file with multiple tech-
support log files as well as the SWLOG files from the switches. 
 
 
OS6860-> show tech-support eng complete  
 
It is a good idea to offload these files and review them to determine what additional data you might want to 
collect to establish meaningful baselines for a successful upgrade. 
 
• 
If upgrading a standalone chassis or VC using a standard upgrade procedure please refer to Appendix E 
for specific steps to follow.  
• 
If upgrading a VC using ISSU please refer to Appendix F for specific steps to follow.

<<<PAGE 72>>>
December 2025 
Page 72 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Appendix E: Standard Upgrade -  OmniSwitch Standalone or Virtual Chassis 
These instructions document how to upgrade a standalone or virtual chassis using the standard upgrade 
procedure. Upgrading using the standard upgrade procedure consists of the following steps. The steps should 
be performed in order:  
1. Download the Upgrade Files 
Go to the Service and Support website and download and unzip the upgrade files for the appropriate model and 
release. The archives contain the following: 
• 
OS6360 – Nosa.img  
o 
Refer to Appendix G for recommended/required FPGA/U-boot upgrades. 
• 
OS6465 – Nos.img  
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6560 – Nos.img   
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6570M – Wos.img   
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6860 – Uos.img 
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6860N – Uosn.img 
o 
Refer to Appendix H for recommended CPLD upgrades.  
• 
OS6870 – Kaos.img 
o 
Refer to Appendix H for recommended CPLD upgrades.  
• 
OS6865 – Uos.img  
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6900 – Yos.img. 
o 
Refer to Appendix H for recommended CPLD upgrades.  
• 
OS9900 – Mos.img, Mhost.img, Meni.img 
• 
imgsha256sum (not required) –This file is only required when running in Common Criteria mode. Please 
refer to the Common Criteria Operational Guidance Document for additional information.  
2. FTP the Upgrade Files to the Switch 
FTP the image files to the Running directory of the switch you are upgrading. The image files and directory will 
differ depending on your switch and configuration. 
 
3. Upgrade the image file

<<<PAGE 73>>>
December 2025 
Page 73 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Follow the steps below to upgrade the image files by reloading the switch from the Running directory. 
 
 
OS6860-> reload from working no rollback-timeout 
 
Confirm Activate (Y/N) : y 
 
This operation will verify and copy images before reloading. 
 
It may take several minutes to complete.... 
If upgrading a VC the new image file will be copied to all the Slave chassis and the entire VC will reboot. After 
approximately 5-20 minutes the VC will become operational. 
4. Verify the Software Upgrade 
Log in to the switch to confirm it is running on the new software. This can be determined from the login banner 
or the show microcode command.  
 
-> show microcode 
    
/flash/working 
    
Package           Release                 Size      Description          Secure Boot 
---------------+-----------------------+---------+---------------------+------------ 
Uos.img          8.10.86.R04            119368578 Alcatel-Lucent OS     No 
 
 
OS6860-> show running-directory 
 
CONFIGURATION STATUS 
   
Running CMM              : MASTER-PRIMARY, 
   
CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
   
Current CMM Slot         : CHASSIS-1 A, 
   
Running configuration    : WORKING, 
   
Certify/Restore Status   : CERTIFY NEEDED 
 
SYNCHRONIZATION STATUS 
   
Running Configuration    : SYNCHRONIZED 
 
Note: If there are any issues after upgrading the switch can be rolled back to the previous certified version by 
issuing the reload from certified no rollback-timeout command. 
  
5. Certify the Software Upgrade 
After verifying the software and that the network is stable, use the following commands to certify the new 
software by copying the Running directory to the Certified directory.   
 
OS6860-> copy running certified 
 
 
-> show running-directory 
 
CONFIGURATION STATUS 
  
Running CMM              : MASTER-PRIMARY, 
   
CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
   
Current CMM Slot         : CHASSIS-1 A, 
   
Running configuration    : WORKING, 
   
Certify/Restore Status   : CERTIFIED 
 
SYNCHRONIZATION STATUS 
   
Running Configuration    : SYNCHRONIZED

<<<PAGE 74>>>
December 2025 
Page 74 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Appendix F: ISSU – OmniSwitch Chassis or Virtual Chassis   
These instructions document how to upgrade a virtual chassis using ISSU. Upgrading using ISSU consists of the 
following steps. The steps should be performed in order: 
  
1. Download the Upgrade Files 
Go to the Service and Support Website and download and unzip the ISSU upgrade files for the appropriate 
platform and release. The archive contains the following: 
• 
OS6360 – Nosa.img  
o 
Refer to Appendix G for recommended/required FPGA/U-boot upgrades.  
• 
OS6465 – Nos.img  
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6560 – Nos.img  
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6570M – Wos.img  
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6860 – Uos.img 
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6860N – Uosn.img 
o 
Refer to Appendix H for recommended CPLD upgrades.  
• 
OS6870 – Kaos.img 
o 
Refer to Appendix H for recommended CPLD upgrades.  
• 
OS6865 – Uos.img  
o 
Refer to Appendix G for recommended FPGA/U-boot upgrades.  
• 
OS6900 – Yos.img.  
o 
Refer to Appendix H for recommended CPLD upgrades.  
• 
OS9900 – Mos.img, Mhost.img, Meni.img 
• 
ISSU Version File – issu_version 
• 
imgsha256sum (not required) –This file is only required when running in Common Criteria mode. Please 
refer to the Common Criteria Operational Guidance Document for additional information.  
Note: The following examples use issu_dir as an example ISSU directory name. However, any directory name 
may be used. Additionally, if an ISSU upgrade was previously performed using a directory named issu_dir, it 
may now be the Running Configuration, in which case a different ISSU directory name should be used.   
2. Create the new directory on the Master for the ISSU upgrade:  
 
OS6860-> mkdir /flash/issu_dir

<<<PAGE 75>>>
December 2025 
Page 75 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
3. Clean up existing ISSU directories  
(Note: If upgrading a standalone (VC-of-1), modular OS9900 with dual CMMs, skip to step 7). 
 It is important to connect to the Slave chassis and verify that there is no existing directory with the path 
/flash/issu_dir on the Slave chassis. ISSU relies upon the switch to handle all of the file copying and directory 
creation on the Slave chassis. For this reason, having a pre-existing directory with the same name on the Slave 
chassis can have an adverse effect on the process. To verify that the Slave chassis does not have an existing 
directory of the same name as the ISSU directory on your Master chassis, use the internal VF-link IP address to 
connect to the Slave. In a multi-chassis VC, the internal IP addresses on the Virtual Fabric Link (VFL) always use 
the same IP addresses: 127.10.1.65 for Chassis 1,127.10.2.65 for Chassis 2, etc. These addresses can be found 
by issuing the debug command ‘debug show virtual-chassis connection’ as shown below: 
 
 
OS6860-> debug show virtual-chassis connection 
                                       Address             Address 
  
Chas  MAC-Address          Local IP             Remote IP          Status 
 
-----+------------------+---------------------+-------------------+------------- 
  
1       e8:e7:32:b9:19:0b  127.10.2.65       127.10.1.65       Connected 
 
4. SSH to the Slave chassis via the internal virtual-chassis IP address using the password ‘switch’: 
 
OS6860-> ssh 127.10.2.65 
 
Password:switch 
 
5.  Use the ls command to look for the directory name being used for the ISSU upgrade. In this example, we’re 
using /flash/issu_dir so if that directory exists on the Slave chassis it should be deleted as shown below. Repeat 
this step for all Slave chassis: 
 
OS6860-> rm –r /flash/issu_dir 
6. Log out of the Slave chassis: 
 
OS6860-> exit 
 
logout 
 
Connection to 127.10.2.65 closed. 
 
7. On the Master chassis copy the current Running configuration files to the ISSU directory: 
 
OS6860-> cp /flash/working/*.cfg /flash/issu_dir 
8. FTP the new image files to the ISSU directory. Once complete verify that the ISSU directory contains only the 
required files for the upgrade:  
 
OS6860-> ls /flash/issu_dir 
 
Uos.img       issu_version  vcboot.cfg    vcsetup.cfg 
 
9. Upgrade the image files using ISSU: 
 
OS6860-> issu from issu_dir 
 
Are you sure you want an In Service System Upgrade? (Y/N) : y 
During ISSU ‘show issu status’ gives the respective status (pending, complete, etc) 
 
OS6860-> show issu status 
 
Issu pending

<<<PAGE 76>>>
December 2025 
Page 76 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
This indicates that the ISSU is completed 
 
OS6860-> show issu status 
 
Issu not active 
Allow the upgrade to complete. DO NOT modify the configuration files during the software upgrade. It normally 
takes between 5 and 20 minutes to complete the ISSU upgrade. Wait for the System ready or [L8] state which 
gets displayed in the ssh/telnet/console session before performing any write-memory or configuration changes. 
 
OS6860-> debug show virtual-chassis topology 
 
Local Chassis: 1 
 
Oper                                        Config   Oper                      System 
 
Chas  Role         Status              Chas ID  Pri   Group  MAC-Address        Ready 
 
-----+------------+-------------------+--------+-----+------+------------------+------- 
 
1     Master        Running             1        100   19     e8:e7:32:b9:19:0b  Yes 
 
2     Slave         Running             2        99    19     e8:e7:32:b9:19:43  Yes 
 
10. Verify the Software Upgrade 
Log in to the switch to confirm it is running on the new software. This can be determined from the login banner 
or the show microcode command.  
 
-> show microcode 
    
/flash/working 
    
Package           Release                 Size      Description          Secure Boot 
---------------+-----------------------+---------+---------------------+------------ 
Uos.img          8.10.86.R04            119368578 Alcatel-Lucent OS     No 
 
11. Certify the Software Upgrade 
After verifying the software and that the network is stable, use the following commands to certify the new 
software by copying the Running directory to the Certified directory:  
 
OS6860-> write memory flash-synchro 
 
 
OS6860-> show running-directory 
 
CONFIGURATION STATUS 
   
Running CMM              : MASTER-PRIMARY, 
   
CMM Mode                 : VIRTUAL-CHASSIS MONO CMM, 
   
Current CMM Slot         : CHASSIS-1 A, 
   
Running configuration    : issu_dir, 
   
Certify/Restore Status   : CERTIFIED 
 
SYNCHRONIZATION STATUS 
   
Flash Between CMMs       : SYNCHRONIZED 
   
Running Configuration    : SYNCHRONIZED 
 
12. [Optional] Restore the Running Configuration 
After completing the ISSU procedure the Running Configuration can be restored by setting it back to the 
directory used prior to the ISSU procedure. For example to change the Running Configuration back to the 
working directory enter the following:  
 
OS6860-> copy certified working make-running-directory

<<<PAGE 77>>>
December 2025 
Page 77 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Appendix G: FPGA / U-boot Upgrade Procedure 
The following CRs or features can be addressed by performing an FPGA/CPLD or U-boot upgrade on the 
respective models.  
CR / Feature 
Summary 
CRAOS8X-12042 
Description 
Switch does not shutdown after crossing danger threshold temperature.  
FPGA Version 
0.7 
Platforms 
OS6465-P28 
CRAOS8X-7207 
Description 
Chassis reboots twice to join a VC.  
FPGA Version 
0.7 
Platforms 
OS6560-P24Z24,P24Z8,P48Z16 (903954-90) 
CRAOS8X-4150 
Description 
VC LED status behavior. 
U-boot Version 
0.12 
Platforms 
OS6865-U28X 
8.7R1 Release 
CRAOS8X-16452 
Description 
Port remains UP when only SFP is connected. 
FPGA Version 
- 0.6 (OS6560-P48Z16 (904044-90)) 
- 0.7 (OS6560-48X4, OS6560-P48X4) 
- 0.8 (OS6560-X10) 
Platforms 
OS6560-P48Z16 (904044-90), OS6560-48X4, OS6560-P48X4, OS6560-X10 
Fast/Perpetual PoE 
Description 
Fast and Perpetual PoE Support 
FPGA Version 
0.7 (OS6860E-P24Z8) 
0.10  
0.14 (OS6865-U28X) 
0.25 (OS6865-P16X/U12X) 
Platforms 
OS6860/OS6865 
8.7R2 Release 
CRAOS8X-
4813/13440 
Description 
U-boot unable to mount NAND flash with UBIFS errors 
U-boot Version 
8.7.2.R02 
Platforms 
OS6465(T), 6560-24X4/P24X4/48X4/P48X4/X10 
CRAOS8X-13819 
Description 
U-boot unable to mount eUSB flash 
U-boot Version 
8.7.2.R02 
Platforms 
OS6560-24Z24/P24Z24/24Z8/P24Z8/P48Z16 (all PNs), 6865 
CRAOS8X-22857 
Description 
OS6560-P24Z24 reloads continuously with pmds 
FPGA Version 
0.8 
Platforms 
OS6560-24Z24/P24Z24/24Z8/P24Z8/P48Z16 (903954-90) 
1588v2 Support 
Description 
1588v2 Support 
FPGA Version 
0.7 (OS6560-P48Z16 (904044-90)) 
0.8 (OS6560-48X4/P48X4) 
Platforms 
OS6560-48X4/P48X4/P48Z16(904044-90) 
Supported on 1G and 10G ports only.  Not supported 2.5G ports. 
U-boot Password 
Authentication 
Description 
U-boot password support (Early Availability)  
U-boot Version 
8.7.2.R02 
Platforms 
OS6465

<<<PAGE 78>>>
December 2025 
Page 78 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
8.7R3 Release 
 
 
CRAOS8X-26370 
CRAOS8X-25033 
Description 
Required upgrade to enable 12V Power Fail Interrupt (CRAOS8X-26370). 
Required upgrade to address fan speed issue. (CRAOS8X-25033) 
FPGA Version 
0.17 
Platforms 
OS6360-24/P24/48/P48 
CRAOS8X-24464 
Description 
U-boot update for CRAOS8X-24464, ability to disable / authenticate U-
boot access. 
U-boot Version 
8.7.30.R03 
Platforms 
OS6360, 6465, 6560, 6860, 6865, 9900. (Not applicable for platforms 
that use ONIE) 
8.8R1 Release 
 
 
Boot from USB 
 
Description 
U-boot update to allow switch to boot from USB. 
U-boot Version 
8.8.33.R01 
Platforms 
OS6465, OS6865 
8.8R2 Release 
 
 
Future 
compatibility 
 
Description 
U-boot/FPGA update to allow future CMM2/OS9912 NI compatibility. 
U-boot/FPGA Versions 
See OS9900 Table for versions. 
Platforms 
9907 
8.9R1 Release 
 
 
N/A 
There are no U-boot/FPGA upgrade requirements in this release. 
8.9R2 Release 
 
 
Fan Speed 
Description 
Reduced fan speed at boot-up 
FPGA Version 
0.20 
Platforms 
OS6360-(P)24/(P)48/PH48 
CRAOS8X_35470 
and CPLD Support 
Description 
U-boot fix for NAND flash bad file system block. 
Support of Gowin CPLD1 
U-boot 
8.9.85.R02  
Platforms 
OS6360 (All) 
CPLD Support 
Description 
Support of Gowin CPLD1 
U-boot 
8.9.92.R02  
Platforms 
OS6570M-12/12D/U28 
CRAOS8X_35470 
Description 
U-boot fix for NAND flash bad file system block 
U-boot/FPGA Versions 
8.9.85.R02 
Platforms 
OS6465 (All), OS6560-(P)24X4/(P)48X4/X10 
1. Existing switches do not contain the new CPLD component and do not need to upgrade. Switches with the new CPLD 
component will ship from the factory with the correct version.  
8.9R3 Release 
 
 
CRAOS8X-40924 
 
Description 
Address issue when disabling U-boot access. 
U-boot Version 
8.9.139.R03 
Platforms 
OS6570M-12/12D/U28 
Power Supply 
Interrupt 
 
Description 
Address power supply interrupt issue. 
FPGA Version 
0.12 
Platforms 
OS6570M-U28

<<<PAGE 79>>>
December 2025 
Page 79 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
8.9R4 Release 
 
 
Signed AOS Images 
 
Description 
Adds support for signed images when used with AOS 8.9R4 GA release. 
U-boot Version 
8.9.70.R04 
Platforms 
OS6570M-12/12D/U28 
8.10R1 Release 
 
 
CRAOS8X-43592 
Description 
1G/10G SFP not recognized. 
U-boot Version 
XNI_U24 - 2.12.0 
XNI_U48 - 2.12.0 
GNI_U48 - 1.8.0 
CNI_U8 - 1.10 
Platforms 
OS9907/OS9912 
8.10R2 Release 
 
 
CRAOS8X-44063 
Description 
Switches stuck in Marvel mode during bootup. 
U-boot Version 
8.10.42.R02 
Platforms 
6360, 6465, OS6560-24X4/P24X4/48X4/P48X4/X10 
CRAOS8X-44607 
Description 
Switch stuck in Marvel mode after power cycle. 
U-boot Version 
8.10.42.R02 
Platforms 
6360, 6465, 6560, 6570M, 6860(E), 6865 
CRAOS8X-46275 
 
Description 
Switch stuck in Marvel mode after power cycle. 
U-boot Version 
8.10.42.R02 
Platforms 
6360, 6465, OS6560-24Z8/P24Z8(E)/24Z24/P24Z24/P48Z16(E), 6570M, 
6860(E), 6865 
Note: The CRs above were also fixed with U-boot version 8.10.115.R01 in the 8.10R1 maintenance release. Switches 
running 8.10.115.R01 do not need to upgrade to 8.10.42.R02. 
8.10R3 Release 
 
 
There are no FPGA or U-boot upgrades required.  
8.10R4 Release 
 
 
Secure Boot 
 
Description 
Adds support for the Secure Boot image. This is a required upgrade for 
AOS release 8.10R4.  
U-boot Version 
8.10.37.R04 
Platforms 
OS6360, OS6465, OS6560, OS6570M 
 
1. Download and extract the upgrade archive from the Service & Support website. In addition to the AOS 
images, the archive will also contain an FPGA upgrade kit or U-boot file, for example.  
• 
CPLD File - fpga_kit_9631 (if required) 
• 
u-boot.8.10.R04.37.tar.gz 
2. FTP (Binary) the files to the /flash directory on the primary CMM. 
3. Enter the following to upgrade the FPGA. The ‘all’ parameter should be used when upgrading with an FPGA 
kit. Additionally, this will update all the elements of a VC, for example:   
  
-> update fpga-cpld cmm all file fpga_kit_9022 
 
Parse /flash/fpga_kit_9631

<<<PAGE 80>>>
December 2025 
Page 80 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
 
fpga file: OS6360-10_CPLD_V19_20230110.vme 
 
Please wait... 
 
fpga file: OS6360-10_CPLD_V19_20230110.vme 
 
update chassis 1 
 
Starting CMM ALL FPGA Upgrade 
 
CMM 1/1 
 
Successfully updated 
 
Reload required to activate new firmware. 
 
4. If required, a U-boot upgrade can then be performed, for example:  
 
-> update uboot cmm all file /flash/u-boot.8.10.R04.37.tar.gz 
 
Starting CMM ALL UBOOT Upgrade  
 
Please wait... 
 
 
CMM 1/1 
 
u-boot-ppc_2040.bin: OK 
 
U-boot successfully updated 
 
Successfully updated 
 
 
5. Once complete, a reboot is required.

<<<PAGE 81>>>
December 2025 
Page 81 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Appendix H: CPLD/ONIE Upgrade Procedure for ONIE-Based Devices 
The following CRs or features can be addressed by performing a CPLD or ONIE upgrade on the respective 
models. Follow the guidelines in the General Upgrade Requirements and Best Practices appendix prior to 
upgrading. 
8.8R2 Release 
OS6860N-P48M/P48Z/P24M/P24Z 
CRAOS8X-29731/30471 
Description 
OS6860N power supplies  
CPLD File 
os6860n_p48m_p48z_u28_maincpu_20220318.updater 
os6860n_p24m_p24z_maincpld_22020309.updater 
8.9R1 Release 
OS6900-T48C6 
CRAOS8X-30098 
Description 
Fixed I2C lockup issue on CPU board. 
(Please refer to CRAOS8X-30098 for additional details) 
CPLD File 
denverton_cpucpld_v0b.02.0eh_20211124.jbc.updater 
No CR 
Description 
Improved power down sequence when PSU shut down. 
CPLD File 
os6900_t48c6_mainpld_v1.03.02.04.jbc.updater 
OS6900-X48C6 
CRAOS8X-30098 
Description 
Fixed I2C lockup issue on CPU board.  
(Please refer to CRAOS8X-30098 for additional details) 
CPLD File 
denverton_cpucpld_v0b.02.0eh_20211124.jbc.updater 
No CR 
Description 
Improved power down sequence when PSU shut down. 
CPLD File 
os6900_x48c6_mainpldall_bp_v1.03.02.02h.jbc.updater 
OS6900-X48C4E 
CRAOS8X-30098 
Description 
Fixed I2C lockup issue on CPU board. 
(Please refer to CRAOS8X-30098 for additional details) 
CPLD File 
OS6900_XC48C4E_MAIN_CPU_FAN_CPLD_2e3228_20220322.updater 
8.9R4 Release 
OS6900-X48C4E 
CRAOS8X-43968 
Description 
Fixed temperature error on OS6900-X48C4E (Hardware revision: 6) with 
a single power supply.  
CPLD File 
updater_kit_8629 (version 2.15) 
8.10R4 Release 
OS6860N, OS6870 
 
Secure Boot 
Description 
Adds support for the Secure Boot feature. This is an optional upgrade. 
ONIE File 
OS6860N - uosn-onie-v1.deb 
OS6870 - kaos-onie-v1.deb 
Notes:  
1. Upgrading the CPLD on ONIE-based models using an updater kit is supported beginning with AOS Release 8.9.R03. 
2. The updater kit contains all the necessary individual updater files.  
 
Note: AOS must be upgraded to at least 8.9R4 prior to performing a CPLD upgrade using the updater kit. 
ONIE-based platforms contain multiple CPLDs. The upgrade process will pick the correct updater file from the 
kit based on the platform and the CPLD type. The procedure will check for a version mismatch and upgrade the 
CPLD one at a time (i.e. Main board or CPU board). The CPLD will be upgraded one at a time so it may be

<<<PAGE 82>>>
December 2025 
Page 82 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
necessary to run the command multiple times. If no upgrade is required, the command will display a message 
indicating there are no pending upgrades. See example below (file and product names will vary).  
1. Download and extract the upgrade archive from the Service & Support website. In addition to the AOS 
images, the archive will also contain a CPLD upgrade kit, for example.  
• 
CPLD Kit – updater_kit_8629 
• 
ONIE Package – *-onie-v1-deb (use appropriate package based on platform) 
2. Ensure the configuration is certified and synchronized prior to upgrading the CPLD. It’s recommended to 
have a console connection in case there are any issues during the CPLD upgrade procedure. 
3. FTP (Binary) the updater kit to the /flash directory on the primary CMM. 
4. Enter the following to upgrade the CPLD. Use the ‘all’ parameter to upgrade each element in a VC, for 
example:   
-> update fpga-cpld cmm all file updater_kit_8629 
Starting CMM 1/1  FPGA Upgrade  
CMM 1/1 
starting onie update 
Removing firmware update results: 
OS6900_XC48C4E_MAIN_CPU_FAN_CPLD_2f3238_20240315.updater 
Staging firmware update: /flash/ 
OS6900_XC48C4E_MAIN_CPU_FAN_CPLD_2f3238_20240315.updater 
onie update successful 
Successfully updated 
Reload required to activate new firmware. 
 
5. If multiple CPLDs have to be upgraded the command must be run several times.  
6. Once the CPLDs have been upgraded a manual reload is required. This will boot each of the units to “ONIE: 
Update ONIE” mode. Note: Do not press any keys while in ONIE mode. 
7. The switch will update the CPLD and then reboot to the Certified directory. Note: The switch will not boot 
back to the last running directory. 
8. OS6860N models (except U28) will then automatically power cycle. For all other models manually power 
cycle the units to refresh the CPLD image. The switch will then again boot back to the Certified directory.  
9. To update ONIE, use the pkgmgr command, for example: 
-> pkgmgr install uosn-onie-v1.deb 
10. Reload to the running-directory.

<<<PAGE 83>>>
December 2025 
Page 83 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Appendix I: Fixed Problem Reports 
The following problem reports were closed in this release. 
CR/PR 
NUMBER 
Description 
Case: 
00794355 
CRAOS8X-51038 
Summary: 
DHCP Snooping Binding Entry Not Retained During IP Renew Process. 
 
Explanation: 
During the DHCP IP renew process, the DHCP snooping binding entry is not retained in the 
binding table. This leads to intermittent connectivity issues due to the absence of valid 
binding entries until the DHCP renewal is fully processed. 
 
Click for Additional Information 
Case: 
00798118 
CRAOS8X-51038 
Summary: 
With IPv6 Link-Local address (fe80::/10) configuration on a VRRP instance, the switch does 
not transmit IPv6 Router Advertisements (RAs). 
 
Explanation: 
When an IPv6 Link-Local address (fe80::/10) is configured on a VRRP instance, the switch 
does not transmit IPv6 Router Advertisements (RAs). Router Advertisements are transmitted 
correctly when a Global Unicast Address (GUA) is configured on the same VRRP instance. 
 
Click for Additional Information 
Case: 
00814949 
CRAOS8X-52699 
Summary: 
OS6860E-P48: IPv6 RA-RDNSS Server Address Update Issue. 
 
Explanation: 
When modifying the RA-RDNSS server IPv6 address, the switch sends Router Advertisements 
without including any RA-RDNSS server address. 
 
Click for Additional Information 
Case: 
00827812 
CRAOS8X-53076 
Summary: 
Traffic Loss Observed During QoS Disable/Flush. 
 
Explanation: 
On the OS6900-X48C6 distribution switch, a configuration involving approximately 3000 
Access Control List (ACL) policy rules has been observed to cause transient traffic drops 
during disabling or deletion of rules. 
 
Click for Additional Information

<<<PAGE 84>>>
December 2025 
Page 84 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Case: 
00820336 
CRAOS8X-53158 
Summary: 
Error When Configuring IPv6 Prefix on SPB Service Interface. 
 
Explanation: 
When assigning an IPv6 address to a service-mapped interface and then attempting to 
apply an IPv6 prefix for Router Advertisement (RA), the following error is returned: ERROR: 
Interface <ID> does not exist. 
 
Click for Additional Information 
Case: 
00822938 
CRAOS8X-53510 
Summary: 
IGMP not working over EVPN VXLAN tunnel. 
 
Explanation: 
IGMP control packets like IGMP Query packets are not transmitted over EVPN tunnel. As the 
multicast control frames are not forwarded, the Querier does not receive the IGMP reports, 
so it does not forward the multicast stream. 
 
Click for Additional Information 
Case: 
00825165 
CRAOS8X-53675 
Summary: 
IPv6 Interface on EMP Port Remains Active After Link Down. 
 
Explanation: 
When both IPv4 and IPv6 addresses are configured on the EMP port, the following behavior 
is observed upon physical link disconnection: 
 
The IPv4 interface status correctly transitions from UP to DOWN. 
The IPv6 interface status remains ACTIVE, even though the physical link is no longer 
present. 
 
This results in an inconsistent interface state between IPv4 and IPv6, potentially impacting 
network monitoring, automation, or failover mechanisms that rely on accurate interface 
status reporting. 
 
Click for Additional Information 
Case: 
00825283 
CRAOS8X-53694 
Summary: 
IPv6 Loopback0 Not Included in Default Network Group "Switch6". 
 
Explanation: 
On OmniSwitch platforms, the IPv4 Loopback0 interface is automatically included in the 
built-in network group 'Switch'. However, the IPv6 Loopback0 interface is not automatically 
included in the corresponding network group 'Switch6'. 
This behavior results in the IPv6 Loopback0 address being omitted from policy applications 
or configurations that depend on the Switch6 group. 
 
Click for Additional Information

<<<PAGE 85>>>
December 2025 
Page 85 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Case: 
00823054 
CRAOS8X-53698 
Summary: 
Default Route Advertisement via SPB Without Explicit Configuration. 
 
Explanation: 
A default route (0.0.0.0/0) is observed being advertised over an SPB (Shortest Path 
Bridging) network between two nodes without any explicit default route configuration on 
the devices. 
 
Click for Additional Information 
Case: 
00836545 
CRAOS8X-55158 
Summary: 
OS6860N-P48Z: Omniswitch intermittently fail to respond to CLI commands with ERROR: 
System is busy, please try again later. 
 
Explanation: 
Some switches may intermittently fail to respond to operational commands. In affected 
cases, standard CLI commands (for example, show mac-learning) return an error message 
such as: 
 
Please wait... 
ERROR: System is busy, please try again later. 
 
Click for Additional Information 
Case: 
00821681 
CRAOS8X-52281 
Summary: 
OS6900: With DHCP Snooping enabled, DHCP OFFER packets are dropped by EVPN node. 
 
Explanation: 
When DHCP Snooping is enabled, the DHCP OFFER packets from the DHCP Server dropped 
on node OS6900_2. The issue persists even after configuring the port on which 
DHCP_Server is connected as TRUST. 
 
Click for Additional Information 
Case: 
00809648 
CRAOS8X-52231 
 
Summary: 
The Ports on OS6465T-P12 randomly stop working. The erroneous behavior includes ports 
showing UP without the cable, or the ports with valid devices connected do not show any 
Rx counters. 
 
Explanation: 
The switch has PTP end-to-end transparent mode enabled in the configuration. When the 
PTP feature is enabled, it's enabled at the PHY level; during this, the port settings were 
altered, which led to inconsistent behavior on the ports. There is a fix in AOS 8.10 R04 GA, 
which makes sure the port settings at PHY level are intact when the PTP is enabled.  
Click for Additional Information

<<<PAGE 86>>>
December 2025 
Page 86 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Case: 
00821372 
CRAOS8X-53294 
  
Summary: 
The ISIS+MACSEC packets are not being sent out of NNI on an OS6465 switch. 
 
Explanation: 
During the bootup, the NNI and UNI ports are assigned to a TCAM rule that drops the ISIS 
packets. Ideally, NNI and UNBI ports should not be part of that TCAM rule. A workaround is 
to remove and reconfigure those ports. 
 
Click for Additional Information  
Case: 
00823181 
CRAOS8X-53798 
  
Summary: 
The OS6860N ERP nodes are stuck in “Pending” state following link flaps on the ERP ports 
in a VC.  
 
Explanation 
Due to the race condition caused by very quick flap of the ERP ports, the ERP port state is 
not updated properly across the units in VC. Hence the ERP status in the Master and slave 
is not in sync. 
 
Click for Additional Information 
Case: 
00827193 
CRAOS8X-53967 
  
Summary: 
Auto-LACP is not working on OS6860 in AOS 8.10 R03 and AOS 8.10 R02. 
 
Explanation: 
The check to add the auto VFL support for OS6860E-P24M is missing in the AOS. The issue is 
fixed in AOS 8.10 R04 GA. 
 
Click for Additional Information 
Case: 
00837492 
CRAOS8X-55293 
  
Summary: 
The OS6570M switches keeps rebooting every 21 days. 
 
Explanation: 
The switches are rebooting because of the kernel memory leak due to the kernel version in 
AOS 8.10 R03 GA. This issue is very specific to the OS6570M models. No other platforms are 
affected by this issue. 
 
Click for Additional Information  
 
Case: 
00840727 
CRAOS8X-55829 
 
Summary: 
The PTP transparent end-to-end feature is not working on the VC of OS6900-C32E. 
 
Explanation: 
The PTP Transparent feature is supported only on standalone switches or a VC of 1. The CLI 
guides are updated, reflecting the support of this feature on a standalone unit only. 
 
Click for Additional Information 
Case: 
00830366 
Summary: 
Some AOS logs are missing the year field.

<<<PAGE 87>>>
December 2025 
Page 87 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
CRAOS8X-54381 
  
Explanation: 
Added the year to some logs 
  
Click for Additional Information 
Case: 
00827482 
CRAOS8X-54315 
 
  
Summary: 
OS6865P16: The port numbering for swlog LpNi POE Fault message is erroneous. 
 
Explanation: 
The first four ports on this model are non-POE and the port numbering used in the swlog 
LpNi message did not take this offset of 4 into account. Show lanpower CLI output was 
indicating the correct Faulty port, though. 
 
 Click for Additional Information  
Case: 
00808406 
CRAOS8X-51898 
  
Summary: 
OS6560 & OS6465 switches frequently print "API_ERR errCode 3 api msg". 
 
 Explanation: 
In SLNI, aging events would be received from FDBmgr. SLNI Deletes Mac from SLNI DB, and 
sends del req to fdbmgr to remove entry from FDB, and SLNI inform AG about Mac del. AG 
Process this MAC Del msg received from SLNI and then, it sends Mac del Req to SLNI for the 
Mac, which is already deleted by SLNI. SLNI send this del req to fdbmgr and as the entry 
already deleted, the "FdbmgrRx:API_ERR" got printed. 
 
Click for Additional Information 
Case: 
00824197 
CRAOS8X-53494 
 
 
  
Summary: 
OS6360-48 captive portal internal DHCP. if clients initiate more than the allowed number of 
login attempts, the Client does not get any more valid IP addresses. 
  
Explanation: 
When a client is connected to an captive portal using internal DHCP, if the client fails the 
logins and exceeds the maximum number of 4 times.  The clients will get locked up and 
can't get any more valid IP addresses.  Instead, it got a Microsoft default IP address 
instead. Therefore, the clients will forever not be able to join the network until an 
administrator manually resets the port.  This is not user friendly.  The new code will let the 
user retry about 10-15 minutes later. 
 
 Click for Additional Information 
Case: 
00838479 
CRAOS8X-55419 
  
Summary: 
PKI authentication not working after VC failover. 
 
Explanation: 
Enabling PKI authentication is a two-step process. 
First, the Private Key for the user certificate needs to be uploaded to the switch. 
Second, the Private Key needs to be associated with the specific user using the 
installsshkey command: 
"installsshkey user <path_to_cert>" 
The root cause of the issue is that neither the private key nor the installsshkey command 
are being propagated from the Master to the Slave chassis.

<<<PAGE 88>>>
December 2025 
Page 88 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
This issue is resolved in 810.R04, The certificates are copied to the 
/flash/switch/.profiles directory and the installsshkey command is applied to all chassis. 
 
Click for Additional Information 
Case: 00836720 
CRAOS8X-55178 
Summary:  
ERROR: Unable to retrieve DA-UNP snapshot on show configuration snapshot and write 
memory flash-synchro. 
 
Explanation:  
On OS6860N-P48Z running AOS 8.10.93R03, configuration snapshot and flash-sychro 
operations fail after enabling DHCP Snooping at the SPB service level and Port Security on 
the same SAP port. During flush events, the agCmm process stalls while attempting to 
locate the SAP port, causing DA-UNP snapshot retrieval to fail. This results in CLI timeouts 
and snapshot errors. The issue is reproducible and occurs only with this specific feature 
combination. Rebooting the switch temporarily clears the condition, and removing Port 
Security prevents recurrence. The issue is fixed in AOS 8.10R04 GA. 
 
 Click for Additional Information 
Case:  
00827672 
CRAOS8X-54077 
Summary:  
OS6860N-P48Z: DHCP clients on slave chassis are not getting IP addresses after power 
outage. 
 
Explanation:  
After an unplanned site-wide power outage, a virtual chassis rebooted with a version 
mismatch between the master runtime image and its working directory. The master was 
running AOS 8.9R04 while the working directory contained AOS 8.9R03. Due to UDP relay 
packet structure changes introduced in AOS 8.9R04, slave units failed to forward DHCP 
traffic over the uplink. DHCP DISCOVER packets were received on access ports but not 
forwarded upstream, and no snooping bindings were created. Reloading the master chassis 
immediately restored normal DHCP forwarding. A detection and warning log enhancement is 
added in AOS 8.10R04 GA. 
 
  Click for Additional Information 
Case:  
00830614 
CRAOS8X-54431 
Summary:  
TDR test results discrepancy between CLI output and switch logs in AOS 8.10R02. 
 
Explanation:  
When running a TDR test on copper ports, the CLI output correctly reports all cable pairs as 
OK, while switch logs incorrectly report faults for all pairs. This discrepancy is caused by an 
incorrect fault-to-status mapping in the switch logging logic, not by an actual cabling issue. 
The TDR hardware measurement and CLI output are accurate, but internal numeric fault 
codes are misinterpreted in summary log messages, resulting in misleading fault indications. 
This is a logging defect only and is resolved in AOS 8.10R04. 
 
 Click for Additional Information 
Case:  
00833718 
CRAOS8X-54877 
Summary:  
MSTP topology change notifications propagate incorrectly across multiple MST regions.

<<<PAGE 89>>>
December 2025 
Page 89 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
 Explanation:  
In a topology with multiple independent MST regions, a topology change occurring within 
one region is incorrectly propagated to other MST instances. When a BPDU is received from 
a port outside the local MST region, the system incorrectly sets the topology change flag for 
all MSTIs instead of limiting it to the CIST. This results in unnecessary STP convergence, MAC 
flushing, and topology change processing in unaffected regions. The logic was corrected in 
AOS 8.10R04 so that topology changes from external regions are processed only at the CST 
level. 
 
 Click for Additional Information 
Case: 
00733580 
CRAOS8X-43988 
  
Summary: 
Mac flooding in the OS9900 switch in some VLANs.  
 
Explanation: 
Upon mac flush due to STP event, the switch would fail to update the newly learned mac 
address in one of the NI which leads to flooding the unicast traffic.  
 
Click for Additional Information 
Case: 
00802212 
CRAOS8X-51113 
 
Summary: 
OS6865-U28X: State change in ERP ring frequently. 
  
Explanation: 
This is due to limitation in the software implementation in combination to ERP with SPB as 
per the above topology from below KCS article. Enhancement has been down to fix the 
behavior. 
 
Click for Additional Information 
Case: 
00811584 
CRAOS8X-52453 
 
Summary: 
OS6900: VC Split and SPB network flapping due to STP loop. Rebooting the whole VC has 
fixed the split scenario. 
 
Explanation: 
From the logs it could be seen that no proper VFL re-registration and no VFL multi-node 
sync happened. Further, portmgrcmm too couldn’t find the peer connected chassis 1 with 
the VFL L2 down state. Code enhancements have been made to print the relevant logs in 
such VC split scenarios.  
 
Click for Additional Information 
Case: 
00835122 
CRAOS8X-55011 
  
Summary: 
AOS 8x: Hidden control characters in configuration files may be interpreted during file 
application. 
  
Explanation: 
 Applying a configuration file containing special control characters (for example, "Ctrl^A" 
and similar non-printable characters) is accepted unlike when applying the same via CLI 
were these control characters are stripped out. 
  
Click for Additional Information 
Case: 
Summary:

<<<PAGE 90>>>
December 2025 
Page 90 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
00813672 
CRAOS8X-52583 
The 'show health all memory' output is missing from the tech_support.log file. 
  
Explanation: 
The output of "show health all memory" command is added to tech_support.log starting 
from 8.10R04GA 
  
Click for Additional Information 
Case: 
00823321 
CRAOS6X-54029 
Summary: 
OS6450: The age for dynamic routes resets after the switch uptime crosses 828.5 days. 
 
Explanation: 
Dynamic routes flapping after the switch uptime crosses 828.5 days. The issue is seen 
only after the switch is UP for more than 828.5 days. The routes flap leading to temporary 
connectivity loss. The connectivity is automatically restored as the routes are repopulated 
(without user intervention). 
 
 Click for Additional Information  
 
Case: 
00823321 
CRAOS6X-54029 
Summary: 
sFlow caused VRRP egress packets to be trapped to the CPU and incorrectly treated as 
ingress traffic, leading to false VRRP violations and repeated port disconnects. 
 
Explanation: 
Removing sFlow from affected ports mitigates the issue, and a permanent fix is included in 
8.10R04 GA to ensure correct packet handling. 
 
 Click for Additional Information  
Case: 
00830848 
CRAOS6X-54772 /  
CRAOS8X-55312 
 
Summary: 
VFL link flapping and CRC errors were observed on VFL port interfaces using SFP+ (1G/10G) 
uplink ports and DAC. 
 
Explanation: 
Fix included in 8.10R04 GA to improve DAC fine-tuning behavior and preventing similar VFL 
CRC issues in the future. 
 
 Click for Additional Information  
Case: 
00833798 
CRAOS8X-54901 
Summary: 
booting an out-of-the-box switch, the RCD feature starts as expected; however, the 
provisioned switch does not receive a DHCP offer. Issue was fixed only for 6570M switch 
model. 
 
Explanation: 
Same fix that was included for 6570M in 8.10R03GA has been extended to all other 8x 
switch models in 8.10R04GA. 
 
 Click for Additional Information  
 
Case: 
00830065 
CRAOS8X-54974 
Summary: 
ERP Ring status across all nodes returned to Idle, with the RPL blocking port returning to a 
blocking state, even though a MACsec session was down between ERP ports. 
  
Explanation:

<<<PAGE 91>>>
December 2025 
Page 91 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
A documentation update will be provided in 8.10R04GA to clearly and describe the 
interaction between ERP and MACsec, including the expected ERP state transitions and 
traffic behavior when a MACsec session or MKA is disabled on one side of the link. 
  
Click for Additional Information  
Case: 
00810859 
CRAOS8X-52486 
Summary: 
The issue occurs when the slave switch boots with a newer AOS version (8.10.93.R03) that 
is downloaded from master working directory while the master switch is running an older 
AOS version (8.9.221.R03). 
  
Explanation: 
An improvement was made in 8.10R04GA to allow the slave to join the VC without copying 
the image from the master’s running directory if the master’s running image differs from 
the one loaded in the working directory. 
 
Click for Additional Information  
Case: 
00837130 
CRAOS8X-55256 
Summary: 
When MACsec or MKA is disabled on one side of a link, ERP state transitions may still occur 
due to R-APS packets being exchanged over unaffected ERP ports. 
  
Explanation: 
This behavior is expected, and documentation will be updated in 8.10R04GA to clarify the 
interaction between ERP and MACsec. 
 
Click for Additional Information  
Case: 
00837130 
CRAOS8X-55256 
Summary: 
If a switch boots with a vcboot.cfg that contains a plain-text key, the value will not be 
hashed correctly. As a result, even though the output of show configuration snapshot aaa 
may display a hash-key, the sessio will not establish with the RADIUS server because the 
value is not correct. 
  
Explanation: 
A documentation note will be added in 8.10 R04GA to clarify this behavior, emphasizing 
that vcboot.cfg files containing plain-text keys should not be loaded directly, and the 
generated hash-key and hash-salt from the switch must be used. 
 
Click for Additional Information  
Case: 
00837140 
CRAOS8X-55290 
Summary: 
In the documentation for the remote configuration section (RCD, Switch Management 
Guide 8.10 R03), the accepted syntax and maximum user name length seem to be not 
indicated anywhere in the documentation. 
  
Explanation: 
As per the specification the FTP username max length is 15 characters, this will be added 
in the 8.10R04GA document. 
  
Click for Additional Information  
Case: 
00827652 
CRAOS8X-54294 
Summary: 
In AOS 8.10R03, IP interfaces configured via the Extra CLI field during Lightening 
configuration are not applied correctly.

<<<PAGE 92>>>
December 2025 
Page 92 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
 
  
  
Explanation: 
In AOS 8.10R03, IP interfaces configured via the Extra CLI field during Lightening 
configuration are not applied correctly. While VLANs and interface names appear, the 
actual IP address is overwritten, leaving the interface unbound. 
  
Click for Additional Information 
Case: 
00835273 
CRAOS8X-55320 
 
Summary: 
MacSec deployments over WAN were failing because MKA packets were sent untagged and 
dropped by service provider networks.  
 
Explanation: 
A new configuration option allows specifying VLAN and TPID for MKA packets. 
  
Click for Additional Information 
Case: 
00837996 
CRAOS8X-55321 
 
Summary: 
Enabling an inward loopback test can cause LLDP frames to be dropped due to loopback 
related TCAM rules. 
 
Explanation: 
Packet analysis showed LLDP control frames being dropped in the egress pipeline by TCAM 
rules automatically inserted when the loopback test is active. 
  
Click for Additional Information 
 
Case: 
00825660 
CRAOS8X-53815 
  
Summary: 
The OS6900-X24C2 switch was rebooted and found that it was stuck in ONIE mode. 
  
Explanation: 
During testing, one of the switches in the VC of 5 got stuck in ONIE mode with the auto-
boot time stopped after 3 seconds. When the switch boots up in ONIE mode, the boot 
directory can be selected. If it's not manually selected after five seconds, the switch will 
auto select and boot up. In this case, the switch autotimer was interrupted without any 
manual input, causing the issue. 
 
Click for Additional Information 
Case: 
00811146 
CRAOS8X-52174 
  
Summary: 
During the migration of the core OS6900-X72 switch with the OS6900-V48C8 switch, when 
the QOS from the core was loaded, the error "Rule space exhausted on chassis/slot/tcam" 
was observed after loading 90% of the QOS rules.  
  
Explanation: 
The hardware design and how the TACM space is used by the OS6900-V48C8 switch is 
different from the OS6900-X72, so the QoS rules can't be completely ported to the 
customer scenario. So a new profile "EM Mode" is created to store all the QOS to the 
switch. 
 
Click for Additional Information 
Case: 
00805023 
Summary:

<<<PAGE 93>>>
December 2025 
Page 93 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
CRAOS8X-52120 
 
When performing an upgrade from the microcode version 8.9R03 to 8.10R02, app-mon 
configurations are auto-populating. In this case, the user tried from 8.9R03 Build to 
8.10R02 Build 105. 
 
Explanation: 
When an upgrade is performed from 8.9.R03 (kit version: 3.7.13) to 8.10.R02 (3.9.3), 
Appmon cmm checks if /flash/switch/afn/app_mon have kit zip. If yes, it will unzip and 
take aging value (3.7.13) to appAgeout.tcp/udp. It is different from the default kit 
appAgeout.defaultTcp/Udp (3.9.3), so the snapshot is getting the aging value of the old kit 
and causing the issue of adding the aging enforcement configs in the snapshot. 
 
Code changes were made to use the correct Kit. 
 
Click for Additional Information 
Case: 
00815749 
CRAOS8X-52836 
Summary: 
AOS 6860E, running 8.9R04 Build 94 platform, switch up time shows incorrectly in Web 
view (15 days 11 hours 36 minutes 26 seconds) whereas CLI view was correct (380 days 11 
hours 36 minutes and 12 seconds) 
 
Explanation: 
If the uptime of an AOS 8X switch exceeds 365 days, WebView currently increments the 
year by 1 and resets the day count to 0. In this case, Year info was hidden. Code changes 
were made to display correct info. 
 
Click for Additional Information 
 
Case: 
00824194 
CRAOS8X-53496 
Summary: 
If a switch user wants to perform exit operation from the console session via CLI command 
typing shortform of “ex” or “exi” instead of the full “exit” command, the session hangs 
and displays the message shown below. The session does not return to the prompt until the 
user manually interrupts it with Ctrl+C. This is observed in 8.10R03 platform. 
6860N-Core-> ex 
Please wait... 
^C 
 
Explanation: 
Exit is a shell built-in command. It must be typed fully. No short forms are allowed. 
Changes were made to display the error message when exit command is incomplete. 
“Error: Incomplete command”. 
 
Click for Additional Information 
 
Case: 
00823946 
CRAOS8X-53800 
Summary: 
In OS6860N-P48Z, running 8.10R03 Build 93, Lightning Config does not work. The switch 
does not get the IP address 192.168.0.1, and the DHCP server also does not appear to 
function. According to the Lightning Configuration Mode process, this mode should 
automatically run on an out-of-the-box, factory-default switch. The issue occurs only when 
resetting the switch using the "reset-to-factory all" command and is not seen on an out-of-
the-box switch.

<<<PAGE 94>>>
December 2025 
Page 94 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Explanation: 
The EMP OLC mode on the switch uses the GRUB environment variable EMP IP address (EI) 
to trigger Lightning Config mode. When the reset-to-factory command is executed, it 
resets the NVRAM parameters, setting the GRUB EI parameter to 0x0. However, the OLC 
initialization script expects the EI parameter in the format 0.0.0.0, which causes it to fail 
in triggering OLC mode. Code changes made to have the parameter format as 0.0.0.0 
 
Click for Additional Information 
 
Case:  
00831119 
CRAOS8X-54485 
Summary: 
Post an upgrade from 8.9 R2 to 8.10 R2, SPB adjacency was lost between peers. The SPB 
control MAC (09:00:2b:xx:xx:xx) configured for IS-IS hello message has been changed to 
default (01:80:c2:xx:xx:xx). 
 
Explanation: 
ISIS meta code changes had been introduced from 8.10.R02 build. In this change, the 
system was set to use control MAC based on L1 & L2 info. Code changes were made to 
use the configured control MAC instead of default control MAC. 
 
Click for Additional Information 
Case:  
00839858 
CRAOS8X-55752 
Summary: 
In OS6560, running 8.10R03 Build 93 microcode, users are unable to access the switch via 
SSH. Observing memory leak in SU mode, SSH being the top task consuming. Also, the 
following error messages are seen in the swlog continuously. 
 
SW sshd[3292] error: ssh_msg_send: write: Broken pipe 
SW sshd[3292] error: send_rexec_state: ssh_msg_send failed 
SW sshd[3292] error: fork: Cannot allocate memory 
SW sshd[3292] error: send_rexec_state: ssh_msg_send failed 
 
Similar issue was reported in CRAOS8X-47797/fix provided in 8.10R03 did not work. 
 
Explanation: 
It was confirmed that there was memory leak in the SSHD handling process. Code 
corrections were made. 
 
Click for Additional Information 
Case:  
00834623 
CRAOS8X-55076 
Summary: 
In OS6560, running AOS 8.10R03 Build 93 microcode, users are unable to save the switch 
configuration. The following error was seen: 
 
SW -> write memory flash-synchro 
File /flash/working/vcsetup.cfg replaced. 
Please wait... 
ERROR: no answer received (timeout)-18 (CLI-mip_msg_nowait_response) 
SW -> 
Write Memory failed! Unable to retrieve PVLAN configuration.

<<<PAGE 95>>>
December 2025 
Page 95 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Explanation: 
The issue was because of MIP TCP socket disconnect between pvlanCmm and mipgwd. A 
reconnection mechanism in the PVLAN and keep-alive for the socket are implemented to 
address this graceful disconnection. 
 
Click for Additional Information 
Case:  
00839512  
CRAOS8X-53881 
Summary: 
Missing characters in interface alias after firmware upgrade 
 
Explanation: 
After upgrading to AOS 8.10R03, some switch ports randomly show alias names with the 
last two characters missing in the show interface alias output, even though the full alias 
is still correct in the vcboot.cfg file. 
 
Click for Additional Information 
Case:  
00816577 
CRAOS8X-52928 
Summary: 
Error: Unable to retrieve the IPMS snapshot when running the write terminal command. 
Command execution fails, preventing snapshot information from being displayed. 
 
Explanation: 
Fix is given in AOS 8.10R04 to ensure the IPMS module is not impacted by changes in any 
other module. 
 
Click for Additional Information 
Case:  
00800345 
CRAOS8X-51384  
Summary: 
Intermittent EBGP Peering Issues Following OS6465 Switch Upgrade to Version 8.9.R04. 
 
Explanation: 
There are flaps noticed BGP peer connection between the OS6865 switch (running with 
AOS 8.9R04) and the Nokia SAR-8. Issue is notice after being upgraded from AOS 8.7R02.  
 
Click for Additional Information 
Case:  
00815759 
CRAOS8X-52800 
Summary: 
SPB and Ethernet-Service adjacency has been lost when configured shared NNI. 
 
Explanation: 
SPB adjacency down on NNI interface On OS6870 . 
 
Click for Additional Information 
Case:  
00823976 
CRAOS8X-53673 
Summary: 
OS6900-X48C6 Port LED Shows Green with 1G device connected to SFP-10G-T Link.  
 
Explanation: 
In OS6900-X48C6 runing 8.10.93.R03, If SFP-10G-T SFP is connected and other end device 
is 1G speed.LED of the switch port is Green.As per guide RJ45/SFP+ Amber - 1G link and 
Green-10G link.

<<<PAGE 96>>>
December 2025 
Page 96 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Click for Additional Information 
Case:  
00830042 
CRAOS8X-54356 
Summary: 
Assigning an interface to an OSPF area is allowed even without explicitly creating the 
area. 
 
Explanation: 
Assigning an interface to an OSPF area is allowed even without explicitly creating the 
area, and no errors are displayed; however, OSPF does not function correctly until the 
area is created. 
 
Click for Additional Information 
 
Case:  
00798962 
CRAOS8X-52823  
Summary: 
After the upgrade from 8.8.56.R02 to 8.9.94.R04 GA, chassis 2 of the VC is facing rate 
limited traffic forwarding.  
There is Qos policy condition with action to rate limit are configured for source port and 
destination port in both chassis in VC. However, the ports configured in Qos were down 
and the Qos seems applied for rest of the ports that are not configured for rate limiting. 
 
Explanation: 
During reload the Qos policies with destination port are not updated properly in TCAM. 
There is a difference in the TCAM configuration during the upgrade/reload scenario, with 
that of policy configured after the system is in ready state. Multicast packets are trapped 
to cpu/matching the destination port pointing to Slave chassis port in Qos policy 
condition are rate-limited thus bandwidth reduction is noticed. 
Fix is given in AOS 8.10R04. 
 
Click for Additional Information 
Case:  
00816683 
CRAOS8X-52982 
 
Summary: 
PTP feature is not available in model OS6465H-P12. 
 
Explanation: 
AOS 8.10.R04 will support PTP feature in OS6465H-P12. 
 
Click for Additional Information 
Case:  
00821257 
CRAOS8X-53295 
 
Summary: 
SPB SAP port statistics are not incrementing on AOS8x switch in AOS 8.10R03. 
 
Explanation: 
An OS6860E-24 switch running AOS 8.10R03 was found to have SPB SAP statistics counters 
stuck at zero, with no increment observed despite active traffic. In recent changes to

<<<PAGE 97>>>
December 2025 
Page 97 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
the VPLS statistics code were overwriting SPB counters, effectively disabling their 
updates.  
The issue has been corrected in AOS 8.10R04, where both VPLS and SPB statistics now 
function as expected. 
 
Click for Additional Information 
Case:  
00834464, 
00823784 
CRAOS8X-54948, 
CRAOS8X-53474 
 
Summary: 
DHL Failover Behavior with 4000 VLANs and MAC Scaling in AOS 8.X switches and the need 
for preemption timer to be increased. 
 
Explanation: 
DHL supports up to 128 VLANs and 1000 MACs for seamless failover. 
Exceeding these may cause stale MAC issues if ports flap within 1 minute. 
Increasing the DHL preempt timer (e.g., to 60s) helps prevent this. 
CRAOS8X-23137 highlights traffic drops when using “RAW” MAC-flush mode with 4000 
VLANs/MACs. 
The issue occurred during rapid port flaps; increasing the preempt timer from default 30 
seconds to 60s resolved it. 
 
Click for Additional Information 
Case:  
00829447 
CRAOS8X-54482 
 
Summary: 
DHCP Option 66 is not sent to DHCP clients by AOS 8.X switches as DHCP servers. 
 
Explanation: 
Fix is available in AOS 8.10R04 to update the Option TFTP Server name in the Option 66 
Field of DHCP offer and continue to send server host name as well. 
 
Click for Additional Information 
Case:  
00813567 
CRAOS8X-52587 
Summary: 
AD users with a long password is unable to login via SSH to the switch and authentication 
failed. 
 
Explanation: 
Windows NPS radius server used, where an AD user having a 38-character password is 
unable to login to the switch but another AD user having a 10-character password is 
having no issues logging in via SSH to the switch.  
This issue is fixed in AOS 8.10R04 
 
Click for Additional Information

<<<PAGE 98>>>
December 2025 
Page 98 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Case:  
00825564 
CRAOS8X-53881 
 
Summary: 
Missing characters in interface alias after firmware upgrade. 
 
Explanation: 
After upgrading to AOS 8.10R03, some switch ports randomly show alias names with the 
last two characters missing in the “show interface alias” output, even though the full 
alias is still correct in the vcboot.cfg file. 
In AOS 8.10R04, this issue is corrected.  
 
Click for Additional Information 
 
Case:  
00824682 
CRAOS8X-53913 
 
Summary: 
During ISSU from 8.9.94.R04 to 8.9.130.R04 there were syslog-ng errors logged, and the 
switch rebooted. 
 
Explanation: 
Sometimes syslog-ng fetches log messages having unreasonably large sizes because the 
program accesses invalid memory - resulting in crash. 
Fix is given in AOS 8.10R04 such that syslog-ng will validate memory and drop messages if 
their lengths are unreasonably large, before access. 
 
Click for Additional Information 
Case:  
00827663 
CRAOS8X-54613 
 
Summary: 
High CPU issues in a 6860E switch after upgrading it to 8.10.R03 version. 
Logs noticed were: 
swlogd slCmm GENERAL INFO: macCountTimeoutHandler[1169] => Mac Count timeout ... 
 
Explanation: 
slNi & slCmm processes were in issue state of being stuck while doing some comparison. 
The issue is a very specialized case where some snmp polling to OID of 'dot1qTpFdbTable' 
caused the slNi and slCmm processes to get into an infinite loop, effectively rising CPU. 
This issue is fixed in AOS 8.10R04. 
 
Click for Additional Information 
Case:  
00822773 
CRAOS8X-54905 
 
Summary: 
Dying gasp trap not being received on OV/monitoring tool for non-default SNMP port. 
 
Explanation: 
Issue of dying gasp trap not being received on OV/monitoring tool after cold/warm 
reboot for non-default SNMP port like UP port 3162. No issues for default port of UDP 
port 162.  
 
Code changes in AOS 8.10R04 is done to support sending the Dying gasp trap for SNMP as 
well SYSLOG for non-default UDP Destination port. 
 
Click for Additional Information 
Case: 
00800345 
Summary:

<<<PAGE 99>>>
December 2025 
Page 99 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
CRAOS8X-51384  
Intermittent EBGP Peering Issues Following OS6465 Switch Upgrade to Version 8.9.R04. 
  
Explanation: 
In the 8.7AOS version, if there is no EVPN or MPLS configuration, routes with extended 
community attributes are treated as unknown routes and forwarded. However, in version 
8.9, these routes are forwarded only when EVPN MPLS is enabled. Since the OS6465 
switch does not have EVPN or MPLS configured, the extended community length is 
returned as ‘0’. 
Fix is given in AOS 8.10R04 for forwarding routes with extended community attributes 
without requiring EVPN or MPLS and this fix has been backported to the next 
maintenance release of 8.9.R04. 
 
 Click for Additional Information 
Case: 
00815759 
CRAOS8X-52800 
Summary: 
SPB and Ethernet-Service adjacency has been lost when configured shared NNI  
Explanation: 
 
1. ISIS packet without s-vlan encapsulated is not copying to CPU 
Fix is done to retain the network port in ISIS trap rule.  
 
2. ISIS packet with s-vlan encapsulated is not   tunnelling the packet to NNI port  
Fix is done to add a new condition with bvlan in ISIS trap rule when configured 
SPB ISIS. 
 
Click for Additional Information 
Case: 
00823976 
CRAOS8X-53673 
Summary: 
OS6900-X48C6 Port LED Shows Green with 1G device connected to SFP-10G-T Link. 
The link should be Amber as per hardware guide specification for 1G link negotiation. 
 
Explanation: 
Code changes were implemented to align the MAC speed with the SFP PHY speed during 
1G connections, ensuring accurate speed detection when the SFP properly reports 1G.  
 
Click for Additional Information 
 Case: 
00830042 
CRAOS8X-54356 
Summary: 
Assigning an interface to an OSPF area is allowed even without explicitly creating the 
area in AOS 8.X switches. 
! OSPF: 
ip load ospf 
ip ospf interface "vlan13" 
ip ospf interface "vlan13" area 0.0.0.0 
ip ospf interface "vlan13" admin-state enable 
 
Explanation: 
Assigning an interface to an OSPF area is allowed even without explicitly creating the 
area, and no errors are displayed; however, OSPF does not function correctly until the 
area is created. Fix is given in AOS 8.10R04 to throw a warning as given below. 
 
Click for Additional Information

<<<PAGE 100>>>
December 2025 
Page 100 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Case: 
00824914, 
00837005, 
00842793 
CRAOS8X-53666 
  
Summary: 
The “Password Expiration” and “Password Allow to be Modified” dates observed under 
the show user command are shown as expired, with the “Allow to Modify” date also 
reflecting a past date. 
 
Explanation: 
The OS6560 has upgraded from 8.10.105.R02 to 8.10.93.R03. After executing the user 
password-min-age days and user password-expiration commands, the user was found to 
be locked out and displaying past date. 
If configured password expiration for a specific user using the command user snmpv3 
expiration 100, the change will not be reflected in the output of the show user password-
policy command. 
Across all AOS 8 switches, only the admin account can modify itself.  
Maximum days cannot exceed 365 days for password expiration/validity period. 
 
Fix is given in AOS 8.10R04 to reflect the correct expired date for individual password for 
both fields. 
 
Click for Additional Information 
Case: 
00825092  
CRAOS8X-55058 
Summary: 
PXE Client is not receiving DHCP offer when dhcp-snooping is enabled in AOS 8.X 
switches. 
 
Explanation: 
Fix is given in AOS 8.10R04. 
  
Click for Additional Information 
Case: 
00832304 
CRAOS8X-54654 
  
Summary: 
The “write-memory” fails with the error “Unable to retrieve SYSS configuration”. 
 
Explanation: 
The SSAPP module is going into the loop when the switch is trying to resolve the DNS for 
a big URL. The fix to avoid SSSAPP module going into the loop.  
 
Click for Additional Information  
Case: 
00829170 
CRAOS8X-54595 
 
Summary: 
Redirect URL is NOT sent for the user mapped to SPB service on a OS6860E. 
 
Explanation: 
To support IP page redirect services, such as BYOD and captive portal, an IP interface on 
the classified VLAN is required. To support this IP redirection, inline routing is used for 
the service domain. The inline routing is not supported on the device OS 6860; therefore, 
BYOD and captive portal in the service domain for the 6860 switches are not supported.  
The CLI user guide is updated with the details.  
 
Click for Additional Information

<<<PAGE 101>>>
December 2025 
Page 101 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Appendix J: Installing/Removing Packages 
The package manager provides a generic infrastructure to install AOS or non-AOS third party Debian packages 
and patches. The following packages are supported. The package files are kept in the flash/working/pkg 
directory or can be downloaded from the Service & Support website.  
Package 
Package Description 
uos-mrp-v1.deb 
nos-mrp-v1.deb 
MRP Application 
*-ams-v#.deb 
*-ams-apps-v#.deb 
AOS Micro Services Application 
uosn-mpls-v5.deb 
uosn-sitemgr-v3.deb 
uosn-siteend-v2.deb 
yos-mpls-v5.deb 
yos-sitemgr-v3.deb 
yos-siteend-v2.deb 
MPLS Application and Licensing 
yos-nutanix-v3.deb 
Nutanix Prism Plug-in Package 
ovng-agent-v.1.10.deb                   
OmniVista Cirrus 10 
kaos-sitemgr-v3.deb 
kaos-siteend-v2.deb 
Licensing for SW-PERF for 6870 
nos-pnet-v1.deb 
Profinet Application 
uosn-onie-v1.deb 
kaos-onie-v1.deb 
ONIE upgrade package 
- If a package is not committed it can result in image validation errors when trying to reload the 
switch. 
- Some packages are included as part of the AOS release and do not have to be installed separately. 
- Applications should be stopped prior to upgrading a package. 
 
Installing Packages 
Verify the package prior to install. Then install and commit the package to complete the installation. For 
example:   
-> pkgmgr verify nos-mrp-v1.deb 
  Verifying MD5 checksum.. OK 
-> pkgmgr install nos-mrp-v1.deb 
-> write memory 
-> show pkgmgr 
Legend: (+) indicates package is not saved across reboot 
        (*) indicates packages will be installed or removed after reload 
Name                Version           Status             Install Script 
-------------+---------------------+------------------+-----------------------------    ams           
default               installed          default 
ams-apps      default               installed          default 
mrp 
 
 8.7.R03-xxx  
   installed      /flash/working/pkg/mrp/install.sh 
 
Removing Packages 
Find the name of the package to be removed using the show pkgmgr command, then remove and commit the 
package to complete the removal. Remove the Debian installation file. For example: 
-> pkgmgr remove mrp

<<<PAGE 102>>>
December 2025 
Page 102 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Purging mrp (8.7.R03-xxx)... 
Removing package mrp.. OK 
Write memory is required complete package mrp removal 
-> write memory 
Package(s) Committed 
 
-> show pkgmgr 
Legend: (+) indicates package is not saved across reboot 
        (*) indicates packages will be installed or removed after reload 
Name                Version           Status             Install Script 
---------------+---------------------+------------------+--------------------------------- 
  ams           default               installed          default 
  ams-apps      default               installed          default 
  mrp         8.7.R03-xxx           removed            /flash/working/pkg/mrp/install.sh 
 
Remove the Debian package installation file. For example:  
 
  
-> rm /flash/working/pkg/nos-mrp-v#.deb  
 
AOS Upgrade with Encrypted Passwords 
AMS 
The ams-broker.cfg configuration file for AMS contains plain text passwords. The passwords can be stored as 
encrypted beginning with the 8.7R1 release. Follow the steps below prior to upgrading to 8.7R1 or later release 
to store encrypted passwords. 
 
1. Remove ams-broker.cfg file present under path /flash/<running-directory>/pkg/ams/ prior to 
upgrading AOS.  
2. This will remove the broker configuration which must be re-configured after the upgrade. 
3. Remove this file from each VC node. 
4. Upgrade the switch. 
5. Once the switch comes up after the upgrade, the password present under/flash/<running-
directory>/pkg/ams/ams-broker.cfg file will be encrypted. 
 
IoT-Profiler 
The ovbroker.cfg configuration file for AMS-APPS/IoT-Profiler contains plain text passwords. The passwords can 
be stored as encrypted beginning with the 8.7R1 release. Follow the steps below prior to upgrading to 8.7R1 or 
later release to store encrypted passwords. 
 
1. Remove the install.sh file present under path /flash/<running-directory>/pkg/ams-apps/ for AMS-APPS 
prior to upgrading AOS.  
2. Remove this file from each VC node. 
3. Upgrade the switch. 
4. Once the switch comes up after the upgrade, the password present under/flash/<running-
directory>/pkg/ams-apps/ovbroker.cfg file will be encrypted.

<<<PAGE 103>>>
December 2025 
Page 103 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Appendix K: Fixed CVEs 
The following CVE CRs were fixed in this release. 
 
CVE CRs 
CVE 
CVSS 
CRAOS8X-53303 
9.8 
 
 
CVE-2025-49794  
CVE-2025-49795 
CVE-2025-49796 
CRAOS8X-53564 
9.8 
CVE-2025-6965 
CRAOS8X-53764 
9.8 
CVE-2025-3277 
CRAOS8X-55096 
 
9.9 
 
CVE-2025-49844 
CVE-2025-46817 
CRAOS8X-55854 
9.8 
CVE-2025-1861

<<<PAGE 104>>>
December 2025 
Page 104 of 105 
 
                
 
 
 
OmniSwitch AOS Release 8.10R4 - Rev. A  
Appendix L: Secure Boot Behavior Beginning in 8.10R4  
Review the following for important software and Secure Boot behavior on each OmniSwitch platform prior to 
upgrading to AOS Release 8.10R4.  
• 
Supported ONIE Platforms - Secure Boot is supported by enabling the feature in BIOS.  
• 
Supported U-boot Platforms - Secure Boot is supported by upgrading U-boot to an 8.10R4 version.  
Beginning in 8.10R4: 
• 
OS6900 -  Two AOS images will be available. One is an image that supports the Secure Boot feature. The 
other is an image that does not support the Secure Boot feature. Both images are named yos.img but 
will be made available in separate download locations on MyPortal. 
o 
OS6900-V72/C32/V48C8/C32E – Requires the non-Secure Boot image. 
 
OS6900-V48C8/C32E – These platforms require a BIOS upgrade to support the Secure 
Boot image which is not yet available.  
o 
OS6900-X48C6/T48C6/X48C4E/T24C2/X24C2 – Can use either the Secure Boot image or the non-
Secure Boot image.  
o 
If an OS6900-V72/C32/V48C8/C32E needs to be mixed with other OS6900 platforms in a VC 
then the non-Secure Boot image must be used on all platforms. 
• 
OS6360, OS6465, OS6560, OS6570M , OS6860N, OS6870, OS6920 and OS6575 – One image will be 
available that supports the Secure Boot image.  
o 
The OS6360, OS6465, OS6560 and OS6570M platforms must upgrade the U-boot to the 8.10R4 
version prior to upgrading AOS to 8.10R4.  
• 
Secure Boot is not supported on OS6860(E), OS6865, OS6900-V72/C32/V48C8/C32E (without BIOS 
upgrade) or OS9900 in 8.10R4. 
ONIE Platform Behavior: 
• 
OS6860N, OS6870, OS6900 – Non-Secure Boot images can be loaded on switches that have Secure Boot 
enabled in BIOS, this includes releases prior to 8.10R4. This is for a temporary transition period. This 
will be disabled in a future release.  
• 
OS6860N, OS6870, OS6900-X48C6/T48C6/X48C4E/T24C2/X24C2 - Secure Boot images can be loaded on 
switches that don't have Secure Boot enabled in BIOS. 
• 
OS6900-V72/C32/V48C8/C32E – Only non-Secure Boot images can be loaded on these switches. If a 
Secure Boot image is loaded on these switches it will reboot from the Certified image. 
U-boot Platform Behavior 
• 
OS6360, OS6565, OS6560, OS6570M – Only Secure Boot images can be loaded on these switches and the 
U-boot must be upgraded to 8.10R4.  
• 
If a Secure Boot image is loaded on a switch that doesn't have the 8.10R4 U-boot version installed, it 
will reboot from the Certified image. 
Secure Boot Upgrade Procedure  
Depending on the platform, support of the Secure Boot feature may require upgrades to U-boot, ONIE, or BIOS 
as well as using an AOS Secure Boot image.

<<<PAGE 105>>>
December 2025 
Page 105 of 105 
 
 
 
 
                                     
OmniSwitch AOS Release 8.10R4 - Rev. A 
Platform 
Files 
OS6860N 
Secure Boot image - Uosn.img 
Debian Package for ONIE and Diag images  - uosn-onie-v1.deb 
OS6870 
Secure Boot image – Kaos.img 
Debian Package for ONIE and Diag images  -  kaos-onie-v1.deb 
OS6900-
X48C6/T48C6/X48C4E/T24C2/X24C2 
Secure Boot image - Yos.img 
 
1. Upgrade AOS to 8.10R4 using the Secure Boot image.  
2. Reboot and enable the Secure Boot option in BIOS. 
3. (OS6860N/OS6870 Only) Reboot and upgrade ONIE and Diag images by installing the proper ONIE 
package, for example:  
-> pkgmgr install uosn-onie-v1.deb 
-> write memory flash-synchro 
 
Platform 
Files 
OS6900-V48C8/C32E 
Secure Boot image – yos.img 
Notes: 
These platforms require a BIOS upgrade to support the Secure Boot feature. 
BIOS Version:  
OS6900-C32E - v40.01.01.03  
OS6900-V48C8 - v40.01.01.04  
 
1. Upgrade BIOS to the proper version. (Contact Service & Support for additional information) 
2. Upgrade AOS to 8.10R4 using the Secure Boot image.  
3. Reboot and enable the Secure Boot option in BIOS. 
 
Platform 
Files 
OS6360 
Secure Boot image - Nosa.img 
OS6465 
Secure Boot image - Nos.img 
OS6560 
Secure Boot image - Nos.img 
OS6570M 
Secure Boot image - Wos.img 
U-boot Version: 8.10.37.R04 
 
1. Upgrade to the 8.10R4 version of U-boot.  
2. Upgrade AOS to 8.10R4 using the Secure Boot image.