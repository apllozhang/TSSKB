<<<DOC 1: AI-DC-Golden-RFP - Copy.docx|1|1>>>

﻿-90136226710700
Alcatel-Lucent AI DC Solution Golden RFP
Requirements specification for the Data Center fabric, compute, and orchestration platform supporting AI/ML workloads.
Release Version
Date
Comments
1
May 2026
Based on Phase 2 of AI-DC Offer
Table of Contents
TOC \o "2-3" \h \z \t "Heading 1,1" Introduction PAGEREF _Toc230017756 \h 3
Solution Components PAGEREF _Toc230017757 \h 3
AI Compute Servers PAGEREF _Toc230017758 \h 4
ALE OmniCompute OC8100 PAGEREF _Toc230017759 \h 4
Front-end Network Switches PAGEREF _Toc230017760 \h 5
OmniSwitch 6920 PAGEREF _Toc230017761 \h 5
OmniSwitch 6900 PAGEREF _Toc230017762 \h 6
Back-end Network Switches PAGEREF _Toc230017763 \h 7
OmniSwitch 7900 PAGEREF _Toc230017764 \h 7
Management Switches PAGEREF _Toc230017765 \h 8
Network Operating System PAGEREF _Toc230017766 \h 8
AOS-X PAGEREF _Toc230017767 \h 9
ASON (ALE SONiC) PAGEREF _Toc230017768 \h 9
Orchestration and Management Platform PAGEREF _Toc230017769 \h 10
Datasheets PAGEREF _Toc230017770 \h 10
Golden RFP – Minimum Supported Features PAGEREF _Toc230017771 \h 10
Solution-level requirements PAGEREF _Toc230017772 \h 11
AI compute server (GPU server) PAGEREF _Toc230017773 \h 12
Back-end Network PAGEREF _Toc230017774 \h 13
Spine Switch Option 1: 51.2 Tbps PAGEREF _Toc230017775 \h 13
Spine Switch Option 2: 25.6 Tbps 400G PAGEREF _Toc230017776 \h 15
Leaf Switch Option 1: 25.6 Tbps PAGEREF _Toc230017777 \h 15
Leaf Switch Option 2: 12.8 Tbps 400G PAGEREF _Toc230017778 \h 17
Front-end Network PAGEREF _Toc230017779 \h 18
Spine Switch Option 1: 12.8 Tbps 400G PAGEREF _Toc230017780 \h 18
Spine Switch Option 2: 6.4 Tbps 100G PAGEREF _Toc230017781 \h 19
Leaf Switch Option 1: 25G/100G (SFP28) PAGEREF _Toc230017782 \h 19
Leaf Switch Option 2: 10G/100G (SFP+) PAGEREF _Toc230017783 \h 20
Leaf Switch Option 3: 10G/100G (10GBASE-T) PAGEREF _Toc230017784 \h 20
Management network switch PAGEREF _Toc230017785 \h 21
Common switch software features PAGEREF _Toc230017786 \h 22
NOS architecture and lifecycle PAGEREF _Toc230017787 \h 22
Lossless Ethernet for RoCEv2 PAGEREF _Toc230017788 \h 23
EVPN-VXLAN overlay PAGEREF _Toc230017789 \h 23
Layer-3 routing (IPv4 and IPv6) PAGEREF _Toc230017790 \h 24
Layer-2 services PAGEREF _Toc230017791 \h 25
Quality of Service and ACLs PAGEREF _Toc230017792 \h 25
Security and AAA PAGEREF _Toc230017793 \h 26
Telemetry and visibility PAGEREF _Toc230017794 \h 26
Management and programmability PAGEREF _Toc230017795 \h 26
Conclusion PAGEREF _Toc230017796 \h 27
Introduction
ALE AI Data Center (AIDC) is a validated, AIready Data Center solution that provides the network foundation for GPU clusters, including frontend (training/inference &amp; storage), backend (eastwest AI fabric), and outofband management. It combines a reference architecture, proven switching platforms, and an orchestrator to accelerate PoC-to-production deployments.
AI and ML workloads; and large-language-model (LLM) training in particular; generate east-west traffic patterns that are fundamentally different from those of a traditional enterprise DC. Collective communication operations such as all-reduce, all-gather, and all-to-all create synchronized, high-bandwidth bursts between GPUs. A small number of slow or congested flows is sufficient to stall an entire training job. The Job Completion Time (JCT) is therefore a function not of the average throughput but of the tail latency and the loss behaviour of the fabric.
Before the requirements are presented, it is important to understand the design drivers behind them. The compute fabric must deliver lossless Ethernet to support RDMA over Converged Ethernet version 2 (RoCEv2). It must implement adaptive routing and dynamic load balancing to avoid hash-polarization across equal-cost paths. It must provide hardware-based link failover so that the loss of a single link does not pause a long-running training job. It must expose programmable, in-band telemetry so that the operator can diagnose tail-latency events. The front-end network, in turn, must support a standards-based overlay (EVPN-VXLAN) for multi-tenancy and a deterministic Quality of Service (QoS) model for storage traffic. The orchestration platform must provide a single pane of glass for the back-end fabric, the front-end fabric, the management network, and the GPU servers themselves.
The requirements in this document are organized into product-specific chapters and feature-specific chapters. The bidder is expected to answer every line item using the convention shown below:
Code
Meaning
C
Compliant. The proposed product meets the requirement in full.
PC
Partially Compliant. The proposed product meets part of the requirement. The bidder must describe the gap.
NC
Non-Compliant. The proposed product does not meet the requirement.
The bidder must answer every requirement. A blank cell, a dash, or "see datasheet" will be treated as Non-Compliant. The bidder must provide the public datasheet, release-notes reference, or test report that substantiates each "C" answer.
Solution Components
This document specifies the requirements for an end-to-end AI DC solution. The solution covers the GPU compute server, the back-end compute fabric used to interconnect GPUs for distributed training and inference, the front-end network used for storage and general data center connectivity, the out-of-band management network, the Network Operating System (NOS), and the DC orchestration and management platform.
Below are the list of components which are part of the ALE AI-DC solution
AI Compute Servers
ALE OmniCompute OC8100
For the AI GPU compute servers, we have the ALE OmniCompute OC8100. The specifications for this server are:
GPU: AMD 8 x MI325X GPUs with Infinity Fabric
CPU: AMD 2 x EPYC™ 9005/Turin Series Processor
CPU NIC: 2 x BCM957608-P2200GQF00 Dual-Port 200GbE QSFP112
GPU NIC: 8 x BCM957608-P1400GDF00 Single-Port 400G
Storage: 2 x 1.92TB U.2 2.5 NVME4 1DWPD (non SED) + 6 x 7.68TB U.2 2.5 NVME4 1DWPD (non SED)
Form Factor / Cooling: 8U Air Cooling
FP32 TFLOPS: 163.4
FP16 TFLOPS: 1300
FP8 TFLOPS: 2610
Compute Memory per GPU: 256GB HBM3e
Memory Bandwidth: 6 TB/s
Peak Power Consumption per GPU: 1 kW
Actual Working Consumption per Server: 6-8 kW
Compute Fabric Interface: Addition External NIC
The OC8100 hosts eight AMD MI325X GPUs. MI325X is one of the most powerful AI GPUs on the market today. They are connected together inside the server by the AMD Infinity Fabric switch, which is the internal high-bandwidth network that lets the eight GPUs share data without going outside the chassis.
For the host, we have two AMD EPYC 9005 Turin processors. These are the latest generation EPYC CPUs.
For networking, the server has two dual-port 200-gigabit NICs for the CPU side (that is the front-end connection) plus eight single-port 400-gigabit NICs for the GPUs (that is the back-end connection). So the server has both front-end and back-end interfaces built in.
For storage, two 1.92 terabyte and an additional six 7.68 terabyte NVMe drives are available. NVMe is a fast type of solid-state storage.
The form factor is 8U, which means it occupies eight rack units in a standard rack. It uses air cooling, no special liquid cooling required.
The performance numbers are outstanding. Per server, we have 163 teraflops at FP32 precision. At FP16, the more common precision for AI inference, we have 1,300 teraflops. At FP8, an even lower precision used for fast inference, we have 2,610 teraflops.
A teraflop is a trillion floating-point operations per second. FP32, FP16, and FP8 are different ways of representing numbers. FP32 is full precision, with 32 bits per number. FP16 uses 16 bits, which is half as much memory and roughly twice the speed. FP8 is even smaller, eight bits per number. AI training typically uses FP16, and AI inference often uses FP8 to maximize throughput.
Each GPU has 256 gigabytes of HBM3e high-bandwidth memory, with six terabytes per second of memory bandwidth. Per GPU, peak power consumption is one kilowatt. A whole server typically consumes six to eight kilowatts in real workloads.
Front-end Network Switches
For the front-end network, we have models from the OmniSwitch 6900 and 6920 families.
OmniSwitch 6920
The Alcatel-Lucent OmniSwitch® 6920-D32 is a compact, high-density 400 Gigabit Ethernet switch designed for Core LAN and Data Center environments. This 1RU platform delivers exceptional performance with very low latency for both Layer 2 and Layer 3 switching, meeting the needs of modern data center and campus fabric deployments. It provides 32 × 400G ports and is built on an energy-efficient architecture that offers leading power consumption in its class.
The OmniSwitch 6920-D32 is versatile enough to function as a spine, super-spine or border-leaf switch. With support for RoCEv2 and PFC, it enables a fully lossless fabric. The platform is also officially certified for Microsoft Azure Local, ensuring seamless interoperability with Azure Local’s physical network requirements for hybrid and edge environments. In addition, ALE’s Shortest Path Bridging (SPB) implementation on this platform delivers a robust, scalable fabric for VPN services and multi-tenancy.
The following model is positioned for the front-end network:
OmniSwitch 6920-D32
OmniSwitch 6900
The Alcatel-Lucent OmniSwitch® 6900 fixed Core LAN and Data Center (DC) switches are compact, high-density 10, 25, 40 and 100 Gigabit Ethernet (GigE) platforms. They offer high performance and extremely low latency Layer-2 and Layer-3 switching for campus and DC Fabric networks.
They are designed for the most demanding operations in virtualized or physical networks. OmniSwitch 6900s can be positioned as Top- of-Rack (ToR) or spine switches in DC environments, or as core and aggregation devices in campus networks. They support a wide range of protocols and programmable interface (API) for building ALE’s autonomous Service Defined Network or overlay networks based on Software Defined Network architectures.
The OmniSwitch 6900 product family offers a very high port density, with up to 128 x 10 GigE, 80 x 25 GigE and up to 32 x 40/100 GigE ports in a 1RU form factor. The Virtual Chassis feature extends the modularity and reliability of connectivity to address any size of virtualized, highly secured modern and autonomous networks. MACsec is also supported on specific OS6900 models for mission-critical and encrypted communication networks. The OmniSwitch 6900 product family leverages an energy-efficient model with leading low power consumption, making them the most efficient and versatile switches in their class.
The following models are positioned for the front-end network:
OmniSwitch 6900-C32E
OmniSwitch 6900-V48C8
OmniSwitch 6900-X48C6
OmniSwitch 6900-T48C6
Back-end Network Switches
For the back-end network, we have models from the OmniSwitch 7900 family.
OmniSwitch 7900
The Alcatel-Lucent OmniSwitch 7900 switches are 400G/800G compact, high-performance, low latency switches for high-perfomance data centers.
These open network switches are loaded with the Open Network Install Environment (ONIE), which support the installation of compatible Network Operating System software, including open source options, Alcatel-Lucent SONiC (ASON) or Alcatel-Lucent Operating System (AOS-X) NOS offerings.
AI/ML Clusters
One of the main use cases for this switch family is for standards-based Ethernet networking for AI/ML training, fine-tuning &amp; inference, leveraging low latency and high- throughput RoCEv2 (Remote Direct Memory Access (RDMA) over Converged Ethernet). This reduces the Job Completion Time (JCT) by using the cognitive routing and congestion management capabilities of the switch. Fully programmable telemetry enables sophisticated on-chip applications for highest network insight and efficient network management.
High-Performance Computing
The large number of high-capacity Ethernet ports enables server (and switch) interfaces to transition to higher speeds and denser networks. Enables the virtualisation of computer and storage with VxLAN switching and routing.
The following models are positioned for the back-end network:
OmniSwitch 7900-O32
OmniSwitch 7900-O64
OmniSwitch 7900-D32
OmniSwitch 7900-D64
Management Switches
For the OOB management network, we have the following model from the OmniSwitch 6900 family:
OmniSwitch 6900-T48C6
Network Operating System
ALE has a dual operating system strategy for the back-end network: AOS-X and ASON (AOS SONiC). This is important because different customers have different preferences. The features that matter for AI are supported on both NOS:
Modern NOS principles.
Cut-through switching, where the switch starts forwarding the packet before it has fully arrived.
Adaptive routing and dynamic load balancing.
PFC, RoCEv2, and ECN.
Advanced telemetry, for monitoring the fabric in real time.
EVPN-VXLAN for multi-tenancy when one fabric needs to host multiple isolated customers.
AOS-X
AOS-X is our next generation Network Operating System built on modern principles.​ The goal with AOS-X was to make an OS that is ready for the next generation network operations requirements.​ AOS-X will offer:
Vertical Integration: AOS-X provides unified programmable management interfaces across all modules, with future integration into ALE OmniVista and Network Advisor platforms​
Modularity: AOS-X framework is modular. It uses the container technology so the application within the container is independent of the rest of the system.
Scalability: AOS-X supports ALE Switch Abstraction Interface (SAI) built on open SAI hardware abstraction layer framework instead of using closed SAI binary from ASIC vendors like Broadcom. This enables unlocking capabilities of the ASIC in areas of scalability, optimal use of hardware resources​
Reliability: AOS-X is built with years of experience with enterprise customers’ network operational requirements in the areas of fault tolerance both on hardware components and network reliability with features like link fault propagation, link violation monitoring, certified images and config, feature depth and maturity that aligns with enterprise customers. With new capabilities like configuration checkpoint and rollback, warm restart, programmable interfaces​
High Performance: AOS-X is developed cohesively, understanding the relationships between modules, while keeping them independent and modular, thus giving optimal performance.​
Security: AOS-X developed with security first principle – supporting secure boot, signed images, strong encryption algorithms, role based access control, strong network access control features​
Predictable Release Cycle: AOS-X is built with core mature and hardened module from AOS8, with control of the foundation pieces of the architecture – unified management, unified and optimized SAI layer, optimized modular and package management, hardenend image and config management – allows us to have control over releases instead of relying on community roadmap​
​
ASON (ALE SONiC)
​SONiC stands for Software for Open Networking in the Cloud. It is an open-source network operating system. Open source means the source code is publicly available, and a community of vendors and users contributes to it.
SONiC was originally developed by Microsoft for their Azure data centers. Today, it is governed by the Linux Foundation, and it is used by many hyperscalers and large enterprises.
The architecture is modular and container-based, built on top of the Debian Linux operating system. Each function of the switch -- routing, telemetry, management -- runs in its own container. This makes it easy to upgrade, easy to extend, and easy to integrate with modern DevOps tools.
The key innovation in SONiC is something called the Switch Abstraction Interface, or SAI. SAI is a standard programming layer that lets the same SONiC software run on switches from many different vendors. This is what we call hardware-independent programming. It is the same idea as a Linux operating system that can run on any PC, regardless of the manufacturer.
There are multiple hardened distributions of SONiC available from different vendors today. ALE SONiC is our hardened distribution, optimized for the OmniSwitch 7900.
Orchestration and Management Platform
Alcatel-Lucent OmniVista Orchestra® is an AI Data Center Infrastructure Management software platform streamlines operations centrally, empowering data center operational teams. The solution enables robust On-Premises deployment model.
OmniVista Orchestra eliminates the operational complexity of managing distributed network devices by providing centralized configuration, monitoring and lifecycle management – all from a single pane of glass.  It is a data center infrastructure management platform, designed for operators who demand automation, visibility, and control across features, intuitive configuration workflows, zero touch provisioning, comprehensive API interface, easy deployment, integrating natively with SONIC-enabled and AOS-X switches, GPU server support, and AI assistance with real-time and historical monitoring.
OmniVista Orchestra provides streamlined orchestration and management for Alcatel-Lucent OmniSwitch® OS6900, OS7900 devices and Alcatel-Lucent OmniCompute® GPU server platforms. The device manager is a software solution designed to enable seamless, centralized monitoring of all rack devices within a data center. It offers users a one-stop platform to oversee the status of network switches, general servers, GPU servers, and various other types of data center devices, ensuring efficient and streamlined management.
OmniVista Orchestra – On-Premises addresses stringent requirements for local infrastructure management, data sovereignty, and security compliance.
The platform provides security and resiliency, intuitive user interface – ensuring seamless management, faster onboarding, and the flexibility to scale and adapt to evolving business needs.
Datasheets
Links to be added once published.
Golden RFP – Minimum Required Features
The proposed solution shall implement a two-network design: a back-end compute fabric dedicated to inter-GPU traffic, and a front-end network that carries storage and general data-center traffic. In addition, an out-of-band management network shall connect the Baseboard Management Controller (BMC) of every device to the orchestration platform.
Solution-level requirements
#
Requirement
C / PC / NC
1
The proposed solution shall implement separate back-end (compute) and front-end (storage/general) networks, each with its own spine-leaf fabric and its own QoS domain, while remaining manageable from a single orchestration platform.
C / PC / NC
2
The back-end fabric shall be a standards-based Ethernet fabric that supports lossless transport for RDMA over Converged Ethernet version 2 (RoCEv2) as defined in InfiniBand Architecture Specification Volume 1, Annex A17.
C / PC / NC
3
The back-end fabric shall provide cut-through forwarding on all switch ASIC paths used for GPU-to-GPU traffic.
C / PC / NC
4
The back-end fabric shall provide hardware-based dynamic load balancing across equal-cost paths, configurable on a per-egress-queue basis, with rebalancing driven by real-time port load and queue occupancy.
C / PC / NC
5
The back-end fabric shall provide hardware-based link failover that re-steers traffic onto an alternate path within the switch ASIC, without requiring the control plane to reconverge, in less than one millisecond from link-down detection.
C / PC / NC
6
The back-end fabric shall provide programmable, in-band telemetry on the data plane, with line-rate export of per-packet or per-flow records, configurable sampling, and on-chip event triggers (e.g., queue depth threshold, ECN mark, drop) without requiring an external probe.
C / PC / NC
7
The back-end fabric shall support both a rail-optimized topology and a classic Clos topology, and the bidder shall describe both options with explicit cable counts, transceiver SKUs, and oversubscription ratios.
C / PC / NC
8
The front-end network shall implement an EVPN-VXLAN overlay (RFC 7432, RFC 8365) with anycast gateway for east-west routing and integrated routing and bridging (IRB) for L2/L3 services.
C / PC / NC
9
The management network shall be a dedicated Layer-2/Layer-3 network, separate from the front-end and back-end networks, used exclusively for device BMCs, serial console concentrators, and orchestration traffic.
C / PC / NC
10
The complete solution -- back-end fabric, front-end fabric, management network switches, and GPU servers -- shall be managed and observed from a single on-premises orchestration platform delivered by the bidder.
C / PC / NC
11
The bidder shall demonstrate validated scalability from a single-rack pilot (8 GPUs) to an eight-rack production pod (256 GPUs), with documented bills of materials, cabling diagrams, and validated designs for each scale point.
C / PC / NC
12
The back-end compute-fabric switch hardware shall be pre-loaded with the Open Network Install Environment (ONIE) so that the customer retains the option to load either a bidder-provided NOS or a compatible open-source NOS over the life of the solution.
C / PC / NC
13
The back-end compute-fabric NOS shall be a distribution of Software for Open Networking in the Cloud (SONiC), hardened and supported by the bidder, with a Switch Abstraction Interface (SAI) layer for hardware portability across merchant silicon. The bidder shall additionally offer a feature-rich proprietary NOS as a parallel production option on the same back-end hardware.
C / PC / NC
14
The front-end and management-network switches shall be operated under a single, modern, container-based, Linux-distribution-based proprietary NOS with an ASIC Switch Abstraction Interface (SAI), a unified release train, and a single license SKU per device.
C / PC / NC
15
All switch hardware shall be capable of operating in hot-aisle / cold-aisle environments and shall be available in two airflow SKUs: front-to-back (port intake) and back-to-front (port exhaust).
C / PC / NC
16
All switch power supplies shall be hot-swappable, load-sharing, and shall accept either alternating-current (AC) or high-voltage direct-current (HVDC) input on the same chassis.
C / PC / NC
17
All switch and server fans shall be hot-swappable with at least N+1 redundancy.
C / PC / NC
18
All switch power cords for the high-density (1RU and 2RU) back-end compute-fabric and GPU servers shall use the universal IEC 60320 C19/C20 inlet so that a single cable SKU can be deployed worldwide against a customer-owned Power Distribution Unit (PDU).
C / PC / NC
18
The bidder shall provide an on-premises orchestration platform that natively supports the configuration of lossless-Ethernet primitives (Priority Flow Control profiles, Explicit Congestion Notification thresholds, buffer allocation) on the back-end fabric through a graphical user interface and through a REST application programming interface.
C / PC / NC
AI compute server (GPU server)
The AI compute server is the unit of GPU capacity that is replicated across the data center. Each server houses eight GPU modules wired in a full-mesh scale-up fabric and provides eight dedicated 400 Gigabit Ethernet scale-out interfaces -- one per GPU -- for the back-end compute fabric. The server also provides two 200 Gigabit Ethernet interfaces for the front-end network. The requirements below capture both the GPU subsystem and the host subsystem.
#
Requirement
C / PC / NC
1
The server shall be an 8 rack-unit (8RU) form factor with air cooling.
C / PC / NC
2
The server shall include eight GPU modules conforming to the Open Compute Project (OCP) Open Accelerator Module (OAM) specification, packaged on a common Universal Baseboard.
C / PC / NC
3
Each GPU module shall provide a minimum of 256 GB of HBM3e high-bandwidth memory, for an aggregate of 2 TB of GPU memory per server.
C / PC / NC
4
The aggregate HBM memory bandwidth per GPU shall be at least 6 TB/s.
C / PC / NC
5
The eight GPU modules shall be interconnected in a full mesh using a coherent scale-up fabric that provides at least 128 GB/s of bidirectional bandwidth between any pair of GPUs, with seven point-to-point links per GPU.
C / PC / NC
6
Each GPU shall deliver a minimum of 163 TFLOPS of FP32 (matrix) performance, 1300 TFLOPS of FP16 performance, and 2610 TFLOPS of FP8 performance, as measured by the GPU vendor published benchmarks.
C / PC / NC
7
The server shall expose eight dedicated single-port 400 Gigabit Ethernet scale-out Network Interface Cards (NICs), one per GPU, using QSFP112-DD cages, to enable a rail-optimized back-end fabric topology.
C / PC / NC
8
Each scale-out NIC shall implement RoCEv2 in hardware, including hardware support for Priority Flow Control (IEEE 802.1Qbb) and Explicit Congestion Notification (RFC 3168), and shall be programmable from the orchestration platform without an out-of-band tool.
C / PC / NC
9
The server shall expose two dual-port 200 Gigabit Ethernet front-end NICs (QSFP112) for storage and management traffic, independent of the eight scale-out NICs.
C / PC / NC
10
The host CPU complex shall consist of two server-class x86 processors with at least 64 cores per socket, 3.3 GHz base frequency, and 400 W thermal envelope per socket.
C / PC / NC
11
The host shall provide at least 1.5 TB of DDR5 ECC main memory operating at a minimum data rate of 5600 MT/s (e.g., 24 x 64 GB RDIMM 2R 5600).
C / PC / NC
12
The server shall provide a minimum of eight half-height and four full-height PCI Express 5.0 x16 expansion slots, in addition to the slots used by the integrated NICs.
C / PC / NC
13
The server shall provide at least two 1.92 TB U.2 2.5-inch NVMe Gen4 drives rated at 1 DWPD for the boot/OS volume and shall provide front-loadable capacity bays sized for at least six 7.68 TB U.2 NVMe Gen4 drives for high-speed local scratch storage.
C / PC / NC
14
The server shall be powered by six hot-swappable 3300 W power supply units in a 4+2 redundancy configuration; each rated 80 PLUS Titanium.
C / PC / NC
15
The server shall include 15 hot-swappable fan modules in N+1 redundancy.
C / PC / NC
16
The Baseboard Management Controller (BMC) shall be a discrete service processor running an open-source BMC firmware distribution and shall support Serial-over-LAN, Redfish API, and IPMI 2.0.
C / PC / NC
17
The server shall provide an open-source heterogeneous compute software stack compatible with the major AI/ML frameworks (PyTorch, TensorFlow, JAX, ONNX Runtime), available under a permissive license and free of mandatory enterprise subscription.
C / PC / NC
18
The server shall provide a dedicated 1 Gigabit Ethernet RJ-45 port for BMC access, separate from the data-plane NICs.
C / PC / NC
19
The server shall operate in an ambient air temperature range of 10 deg C to 35 deg C and shall conform to ASHRAE Class A2.
C / PC / NC
20
The server peak power draw per rack shall not exceed 10 kW per GPU server envelope; actual working consumption shall be in the 6 to 8 kW range under sustained AI training load.
C / PC / NC
21
The server external dimensions (W x D x H) shall not exceed 448 mm x 850 mm x 351 mm to be compatible with standard 19-inch racks with 1200 mm depth or greater.
C / PC / NC
Back-end Network
Spine Switch Option 1: 51.2 Tbps
The 51.2 Tbps spine switch interconnects the back-end leaf switches in large AI/ML pods. It must deliver high radix at 800 Gigabit Ethernet, expose the congestion-control and adaptive-routing primitives required for lossless RoCEv2 transport, and be built on the most recent generation of high-radix merchant silicon.
#
Requirement
C / PC / NC
1
The switch shall be a 2RU form factor.
C / PC / NC
2
The switch shall provide 64 x OSFP800 switch ports, each natively supporting 1 x 800 GbE using 100 Gb/s PAM4 signaling per electrical lane.
C / PC / NC
3
Each OSFP800 port shall support breakout to 2 x 400 GbE, 4 x 200 GbE, 8 x 100 GbE, 2 x 200 GbE (50G PAM4), 4 x 100 GbE (50G PAM4) and 8 x 50 GbE (50G PAM4) using passive or active breakout cables.
C / PC / NC
4
The switch shall expose a maximum of 320 logical ports on a single switch ASIC die.
C / PC / NC
5
Each OSFP800 port shall provide an electrical power budget of at least 30 W per port to accommodate co-packaged-optics-ready and high-power coherent transceivers.
C / PC / NC
6
The switch ASIC shall be a single monolithic 5 nm die delivering 51.2 Tbps full-duplex non-blocking switching capacity.
C / PC / NC
7
The switch ASIC shall implement Cognitive/Adaptive routing and Dynamic Load Balancing (DLB) per egress queue, as well as Global Load Balancing (GLB) across spine hops, with the rebalancing decision made in hardware on a per-flowlet basis.
C / PC / NC
8
The switch ASIC shall implement hardware-based link failover that re-steers affected flows onto an alternate equal-cost path within the ASIC, without control-plane intervention, in less than one millisecond.
C / PC / NC
9
The switch ASIC shall support VXLAN routing and bridging on the same physical interface (VXLAN RIOT) in hardware at line rate.
C / PC / NC
10
The switch ASIC shall support end-to-end congestion control compatible with RoCEv2 (PFC IEEE 802.1Qbb, ECN RFC 3168, DCQCN, HPCC) without external controllers.
C / PC / NC
11
The switch ASIC shall provide advanced shared buffering accessible by any port and shall expose buffer occupancy on a per-queue basis through telemetry.
C / PC / NC
12
The switch ASIC shall expose programmable, in-band network telemetry (INT) with line-rate header export and on-chip event triggers (queue depth thresholds, ECN-mark events, drop events).
C / PC / NC
13
The switch shall include a discrete BMC module running an open-source BMC firmware distribution, secured by a hardware root-of-trust device, and a Trusted Platform Module conforming to TPM 2.0 over SPI.
C / PC / NC
14
The BMC shall support Serial-over-LAN for out-of-band console access to the NOS shell.
C / PC / NC
15
The switch shall provide timing and synchronization services: Synchronous Ethernet (SyncE) as per ITU-T G.8262, IEEE 1588-2008 Precision Time Protocol version 2, with 1PPS, 10 MHz reference, and Time-of-Day (ToD) physical connectors on the front panel.
C / PC / NC
16
The switch shall include hardware e-fuses to isolate and protect individual transceiver cages and internal components against electrical faults.
C / PC / NC
17
The switch CPU module shall be a quad-core x86 server-class processor with at least 2.2 GHz base clock, at least 32 GB of DDR4 SO-DIMM ECC memory, 240 GB NVMe SSD storage, and dual 64 MB SPI flash banks.
C / PC / NC
18
The switch shall provide on the port side: one RJ-45 serial console, one RJ-45 1000BASE-T management port, two 25 Gigabit Ethernet SFP28 in-band management ports, and one USB 3.0 storage port.
C / PC / NC
19
The switch shall be pre-loaded with the Open Network Install Environment (ONIE) and shall be compatible with multiple Network Operating Systems, including at least one open-source SONiC-based distribution and a feature-rich proprietary NOS hardened and supported by the bidder.
C / PC / NC
20
The switch shall be available in both front-to-back (port-intake / AFO) and back-to-front (port-exhaust / AFI) airflow SKUs.
C / PC / NC
21
The switch shall provide two hot-swappable, load-sharing, redundant 3000 W AC/HVDC power supply units.
C / PC / NC
22
The switch shall provide four hot-swappable fan modules in a 7+1 redundant configuration.
C / PC / NC
23
The switch shall support jumbo frames up to 9416 bytes.
C / PC / NC
24
The switch external dimensions (W x D x H) shall not exceed 44 cm x 64.92 cm x 8.7 cm.
C / PC / NC
25
The switch weight shall not exceed 22 kg with two power supply units and four fan modules installed.
C / PC / NC
26
Operating temperature, front-to-back airflow: 0 deg C to 40 deg C.
C / PC / NC
27
Operating temperature, back-to-front airflow: 0 deg C to 35 deg C.
C / PC / NC
28
Operating humidity: 5 % to 95 %, non-condensing.
C / PC / NC
29
Operating altitude: up to 1800 m.
C / PC / NC
30
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Spine Switch Option 2: 25.6 Tbps 400G
For deployments that do not yet require 800 Gigabit Ethernet on the spine layer, the bidder shall offer an alternative 25.6 Tbps spine switch built on the previous-generation merchant silicon (Tomahawk 4 class or equivalent) with native 400 Gigabit Ethernet port density. This option provides investment protection and a phased migration to 800 GbE.
#
Requirement
C / PC / NC
1
The switch shall be a 2RU form factor.
C / PC / NC
2
The switch shall provide 64 x QSFP56-DD ports, each natively supporting 1 x 400 GbE (8 lanes 50G PAM4).
C / PC / NC
3
Each port shall support 1 x 100 GbE QSFP28, 1 x 40 GbE QSFP+, and breakout modes of 2 x 200 GbE (4 lanes 50G PAM4), 4 x 100 GbE (2 lanes 50G PAM4), 2 x 50 GbE (2 lanes 25G NRZ), 4 x 25 GbE NRZ, and 4 x 10 GbE NRZ.
C / PC / NC
4
The switch ASIC shall deliver 25.6 Tbps full-duplex non-blocking switching capacity at a forwarding rate of at least 10.42 Bpps.
C / PC / NC
5
The switch ASIC shall implement adaptive routing, dynamic load balancing, and hardware support for RoCEv2 congestion control (PFC, ECN).
C / PC / NC
6
The switch ASIC shall support VXLAN RIOT in hardware.
C / PC / NC
7
The switch shall be pre-loaded with the Open Network Install Environment (ONIE), compatible with at least one SONiC-based distribution hardened by the bidder and one feature-rich proprietary NOS.
C / PC / NC
8
The switch CPU module shall be a server-class x86 processor (at least 8 cores, 2.0 GHz base clock), with 32 GB DDR4 SO-DIMM and 128 GB M.2 SSD.
C / PC / NC
9
The switch shall provide two hot-swappable, load-sharing, redundant 2400 W AC/HVDC power supply units.
C / PC / NC
10
The switch shall provide hot-swappable fan modules in 3+1 redundancy.
C / PC / NC
11
The switch shall be available in front-to-back airflow SKU.
C / PC / NC
12
The switch shall support jumbo frames up to 9416 bytes.
C / PC / NC
13
The switch external dimensions (W x D x H) shall not exceed 44 cm x 64.92 cm x 87 mm.
C / PC / NC
14
Operating temperature: 0 deg C to 40 deg C at sea level, 0 deg C to 35 deg C at 1828 m.
C / PC / NC
15
Operating altitude: up to 1828 m.
C / PC / NC
Leaf Switch Option 1: 25.6 Tbps
The 25.6 Tbps leaf switch is the Top-of-Rack switch for the back-end compute fabric. It connects directly to the 400 Gigabit Ethernet scale-out NICs of the GPU server and uplinks to the 51.2 Tbps spine using 800 Gigabit Ethernet ports. It must inherit the same congestion-control, adaptive-routing, and telemetry capabilities as the spine.
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor.
C / PC / NC
2
The switch shall provide 32 x OSFP800 switch ports, each natively supporting 1 x 800 GbE using 100 Gb/s PAM4 signaling per electrical lane.
C / PC / NC
3
Each OSFP800 port shall support breakout to 2 x 400 GbE, 4 x 200 GbE, 8 x 100 GbE, 2 x 200 GbE (50G PAM4), 4 x 100 GbE (50G PAM4), 8 x 50 GbE (50G PAM4), and 1 x 100 GbE (25G NRZ).
C / PC / NC
4
The switch shall expose a maximum of 160 logical ports on a single switch ASIC die.
C / PC / NC
5
Each OSFP800 port shall provide an electrical power budget of at least 30 W per port.
C / PC / NC
6
The switch ASIC shall deliver 25.6 Tbps full-duplex non-blocking switching capacity and shall be implemented on a single monolithic 5 nm die.
C / PC / NC
7
The switch ASIC shall implement Cognitive/Adaptive routing, Dynamic Load Balancing per egress queue, and Global Load Balancing across spine hops in hardware on a per-flowlet basis.
C / PC / NC
8
The switch ASIC shall implement hardware-based link failover with sub-millisecond reaction time and no control-plane involvement.
C / PC / NC
9
The switch ASIC shall support VXLAN routing and bridging on the same physical interface (VXLAN RIOT) in hardware at line rate.
C / PC / NC
10
The switch ASIC shall implement end-to-end congestion control compatible with RoCEv2 (PFC IEEE 802.1Qbb, ECN RFC 3168) and shall expose congestion-control state through programmable telemetry.
C / PC / NC
11
The switch ASIC shall provide programmable, in-band telemetry with line-rate export and on-chip event triggers (queue depth, ECN mark, drop).
C / PC / NC
12
The switch shall include a discrete BMC module running an open-source BMC firmware distribution, secured by a hardware root-of-trust device, and a TPM 2.0 SPI module.
C / PC / NC
13
The switch CPU module shall be a server-class quad-core x86 processor with at least 2.2 GHz base clock, 32 GB DDR4 SO-DIMM ECC, 240 GB NVMe SSD storage, and dual 64 MB SPI flash banks.
C / PC / NC
14
The switch shall provide on the port side: one RJ-45 serial console, one RJ-45 1000BASE-T management port, two 25 Gigabit Ethernet SFP28 in-band management ports, and one USB 3.0 storage port.
C / PC / NC
15
The switch shall be pre-loaded with the Open Network Install Environment (ONIE) and shall be compatible with at least one SONiC-based distribution hardened by the bidder and a feature-rich proprietary NOS.
C / PC / NC
16
The switch shall be available in both front-to-back (AFO) and back-to-front (AFI) airflow SKUs.
C / PC / NC
17
The switch shall provide two hot-swappable, load-sharing, redundant 2400 W AC/HVDC power supply units.
C / PC / NC
18
The switch shall provide seven hot-swappable fan modules in a 6+1 redundant configuration.
C / PC / NC
19
The switch shall contain hardware e-fuses to isolate transceivers and internal rails against electrical faults.
C / PC / NC
20
The switch shall support jumbo frames up to 9416 bytes.
C / PC / NC
21
The switch external dimensions (W x D x H) shall not exceed 43.84 cm x 59.8 cm x 4.3 cm.
C / PC / NC
22
Operating temperature, front-to-back airflow: 0 deg C to 40 deg C.
C / PC / NC
23
Operating temperature, back-to-front airflow: 0 deg C to 35 deg C.
C / PC / NC
24
Operating humidity: 5 % to 95 %, non-condensing.
C / PC / NC
25
Operating altitude: up to 1800 m.
C / PC / NC
Leaf Switch Option 2: 12.8 Tbps 400G
For deployments that do not yet require 800 Gigabit Ethernet at the leaf layer, the bidder shall offer an alternative 12.8 Tbps leaf switch with native 400 Gigabit Ethernet port density. This option provides investment protection for existing 100/400 Gigabit Ethernet GPU servers and a smooth migration path to 800 GbE.
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor.
C / PC / NC
2
The switch shall provide 32 x QSFP56-DD ports, each natively supporting 1 x 400 GbE (8 lanes 50G PAM4).
C / PC / NC
3
Each port shall support 1 x 100 GbE QSFP28, 1 x 40 GbE QSFP+, and breakout modes of 2 x 200 GbE, 4 x 100 GbE, 4 x 25 GbE, and 4 x 10 GbE.
C / PC / NC
4
The upper 16 QSFP56-DD ports shall provide an electrical power budget of at least 24 W per transceiver to support 400 GbE ZR and Open ZR+ coherent transceivers for Data Center Interconnect (DCI) use cases.
C / PC / NC
5
The lower 16 QSFP56-DD ports shall provide an electrical power budget of at least 14 W per transceiver.
C / PC / NC
6
The switch shall be capable of selectively powering off individual ports under NOS control to optimize energy consumption.
C / PC / NC
7
The switch ASIC shall deliver 12.8 Tbps full-duplex non-blocking switching capacity, with a forwarding rate of at least 5.07 Bpps and a port-to-port latency of 650 ns or less.
C / PC / NC
8
The switch ASIC shall provide at least 56 MB of integrated packet buffer.
C / PC / NC
9
The switch ASIC shall support VXLAN RIOT in hardware and shall maintain at least 850 000 IPv4 ALPM routes, 360 000 IPv6 (64-bit) ALPM routes, and 8 192 Virtual Routing and Forwarding (VRF) instances, subject to NOS configuration.
C / PC / NC
10
The switch shall include a discrete BMC module running an open-source BMC firmware distribution, secured by a hardware root-of-trust device, and a TPM 2.0 SPI module.
C / PC / NC
11
The switch shall provide Synchronous Ethernet, IEEE 1588v2 Precision Time Protocol, and a 1PPS connector on the front panel.
C / PC / NC
12
The switch shall include hardware e-fuses to protect individual transceivers.
C / PC / NC
13
The switch shall support a standby power mode for energy efficiency during off-peak periods.
C / PC / NC
14
The switch CPU module shall be a quad-core x86 server-class processor with at least 2.2 GHz base clock, 32 GB DDR4 ECC, 128 GB M.2 SATA SSD with Power-Loss Protection, and dual 512 MB SPI flash banks.
C / PC / NC
15
The switch shall be pre-loaded with the Open Network Install Environment (ONIE), compatible with at least one SONiC-based distribution and one feature-rich proprietary NOS.
C / PC / NC
16
The switch shall be available in both front-to-back and back-to-front airflow SKUs.
C / PC / NC
17
The switch shall provide two hot-swappable, load-sharing, redundant 1500 W AC or 48 V DC power supply units.
C / PC / NC
18
The switch shall provide hot-swappable fan modules in 5+1 redundancy.
C / PC / NC
19
The switch shall support jumbo frames up to 9416 bytes.
C / PC / NC
20
The switch external dimensions (W x D x H) shall not exceed 43.84 cm x 59 cm x 4.35 cm.
C / PC / NC
21
Operating temperature, front-to-back airflow: 0 deg C to 45 deg C.
C / PC / NC
22
Operating temperature, back-to-front airflow: 0 deg C to 30 deg C.
C / PC / NC
23
Operating humidity: 5 % to 95 %, non-condensing.
C / PC / NC
Front-end Network
Spine Switch Option 1: 12.8 Tbps 400G
The 12.8 Tbps 400 Gigabit Ethernet switch is the high-capacity spine switch option for the front-end fabric. It can positioned as a spine, super-spine, or border-leaf switch for storage and general-purpose data-center traffic. It must support lossless transport for high-speed storage protocols and shall be certified for the reference hybrid-cloud platforms relevant to the customer. Unlike the back-end compute-fabric switches, this platform shall run a single, vendor-hardened, production-grade proprietary NOS optimised for the front-end traffic profile, and is not required to expose an open install environment.
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor.
C / PC / NC
2
The switch shall provide 32 x QSFP-DD ports, each natively supporting 1 x 400 GbE.
C / PC / NC
3
Each port shall be configurable for 128 x 10/25 GbE, 128 x 50/100 GbE, or 64 x 200 GbE via breakout cables.
C / PC / NC
4
The switch ASIC shall deliver wire-rate non-blocking 12.8 Tbps switching and routing capacity.
C / PC / NC
5
The switch shall implement RoCEv2 with Priority Flow Control to provide a fully lossless fabric for converged storage and storage-class traffic.
C / PC / NC
6
The switch shall expose a single-command or wizard-driven framework for fabric-wide RoCEv2 enablement that pre-populates Priority Flow Control, Explicit Congestion Notification, Enhanced Transmission Selection, and buffer parameters consistent with a vendor-validated lossless design.
C / PC / NC
7
The switch shall be certified by Microsoft as compliant with the Azure Local (formerly Azure Stack HCI) physical-network requirements.
C / PC / NC
8
The switch shall implement a Link Layer Discovery Protocol (LLDP) Type-Length-Value (TLV) set for Microsoft Azure Local hyperconverged-stack auto-discovery, in addition to the standard IEEE 802.1AB LLDP and the LLDP-MED extensions.
C / PC / NC
9
The switch shall implement an EVPN-VXLAN overlay (RFC 7432, RFC 8365) with a Distributed Anycast Gateway (RFC 9135) and integrated routing and bridging (IRB) for L2/L3 services.
C / PC / NC
10
The switch shall implement a Secure Boot mechanism that verifies the authenticity of the NOS image at every boot using a hardware-anchored root-of-trust and shall ship with signed NOS images.
C / PC / NC
11
The switch shall expose a fully programmable RESTful web services interface with XML and JSON support that exposes every CLI command and every MIB object of the NOS as a programmable data structure.
C / PC / NC
12
The switch shall support eight hardware-based egress queues per port with lossless Virtual Output Queuing and configurable scheduling algorithms.
C / PC / NC
13
The switch shall be available in both front-to-back and back-to-front airflow SKUs with redundant, hot-swappable power supplies and fan trays.
C / PC / NC
14
The switch shall run a single, vendor-hardened, container-based proprietary NOS built on a current long-term-support Linux distribution; the NOS license shall be per-device subscription with one-, three-, and five-year terms.
C / PC / NC
15
The switch shall provide a minimum mean time between failure (MTBF) of 515,000 hours with AC power supplies and 517,000 hours with DC power supplies.
C / PC / NC
16
Operating temperature, front-to-back airflow: 0 deg C to 45 deg C.
C / PC / NC
17
Operating temperature, back-to-front airflow: 0 deg C to 30 deg C.
C / PC / NC
18
Operating humidity: 5 % to 90 %, non-condensing.
C / PC / NC
19
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Spine Switch Option 2: 6.4 Tbps 100G
The 6.4 Tbps 100 Gigabit Ethernet switch is an alternative spine switch for the front-end network. It must provide high-density 100 GbE in a 1RU form factor and the complete set of Data Center features (EVPN-VXLAN with Distributed Anycast Gateway, lossless RoCEv2 transport). It runs the same single proprietary NOS as the 400 Gigabit Ethernet front-end switch.
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor with non-blocking architecture.
C / PC / NC
2
The switch shall provide a minimum of 32 x QSFP28 ports operating at 40 or 100 GbE, with breakout to 4 x 10 GbE or 4 x 25 GbE on every port.
C / PC / NC
3
The switch shall support redundant and hot-swappable AC and DC power supplies.
C / PC / NC
4
The switch shall support hot-swappable transceivers.
C / PC / NC
5
The switch shall support a virtual-chassis architecture with up to six elements stacked through dedicated chassis-interconnect ports, manageable through a single management IP address.
C / PC / NC
6
The switch shall provide a minimum switching capacity of 6.4 Tbps and a maximum port-to-port latency of 600 ns.
C / PC / NC
7
The switch shall support In-Service Software Upgrade (ISSU) of virtual-chassis units without simultaneous reload of every member.
C / PC / NC
8
The switch shall implement a MAC-address retention mechanism that preserves the MAC address of the master unit across virtual-chassis takeovers, in order to avoid Spanning Tree and Link Aggregation re-convergence.
C / PC / NC
9
The switch shall support split-chassis detection to maintain network integrity when one or more virtual-chassis members fail.
C / PC / NC
10
The switch shall implement RoCEv2, Priority Flow Control (IEEE 802.1Qbb), Explicit Congestion Notification (RFC 3168), and the Data Center Bridging Exchange protocol.
C / PC / NC
11
The switch shall run a single, vendor-hardened, container-based proprietary NOS built on a current long-term-support Linux distribution; the NOS license shall be per-device subscription with one-, three-, and five-year terms.
C / PC / NC
12
The switch shall be a maximum of 510 W power consumption under full Layer-2 traffic load with two power supplies installed.
C / PC / NC
13
The switch shall provide a minimum mean time between failure (MTBF) of 371,000 hours with AC power supplies and 382,000 hours with DC power supplies.
C / PC / NC
14
Operating temperature: 0 deg C to 45 deg C.
C / PC / NC
15
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Leaf Switch Option 1: 25G/100G (SFP28)
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor with non-blocking architecture.
C / PC / NC
2
The switch shall provide a minimum of 48 x SFP28 ports operating at 1, 10 or 25 GbE.
C / PC / NC
3
The switch shall provide a minimum of 8 x QSFP28 ports operating at 40 or 100 GbE, with breakout to 4 x 10 GbE or 4 x 25 GbE on every QSFP28 port.
C / PC / NC
4
The switch shall provide a virtual-chassis architecture with up to six elements stacked through dedicated chassis-interconnect ports, manageable through a single management IP address.
C / PC / NC
5
The switch shall implement a MAC-address retention mechanism that preserves the MAC address of the master unit across virtual-chassis takeovers, in order to avoid Spanning Tree and Link Aggregation re-convergence.
C / PC / NC
6
The switch shall support split-chassis detection to maintain network integrity when one or more virtual-chassis members fail.
C / PC / NC
7
The switch shall provide a minimum switching capacity of 4 Tbps and a maximum port-to-port latency of 600 ns.
C / PC / NC
8
The switch shall run a single, vendor-hardened, container-based proprietary NOS built on a current long-term-support Linux distribution; the NOS license shall be per-device subscription with one-, three-, and five-year terms.
C / PC / NC
9
The switch shall support a maximum power consumption of 540 W under full Layer-2 traffic load with two power supplies installed.
C / PC / NC
10
The switch shall provide a minimum MTBF of 203,000 hours with AC power supplies and 208,000 hours with DC power supplies.
C / PC / NC
11
Operating temperature: 0 deg C to 45 deg C.
C / PC / NC
12
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Leaf Switch Option 2: 10G/100G (SFP+)
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor with non-blocking architecture.
C / PC / NC
2
The switch shall provide a minimum of 48 x SFP+ ports operating at 1 or 10 GbE.
C / PC / NC
3
The switch shall provide a minimum of 6 x QSFP28 ports operating at 40 or 100 GbE, with at least 2 QSFP28 ports supporting breakout to 4 x 10 GbE or 4 x 25 GbE.
C / PC / NC
4
The switch shall provide a virtual-chassis architecture with up to six elements stacked through dedicated chassis-interconnect ports, manageable through a single management IP address.
C / PC / NC
5
The switch shall implement a MAC-address retention mechanism that preserves the MAC address of the master unit across virtual-chassis takeovers, in order to avoid Spanning Tree and Link Aggregation re-convergence.
C / PC / NC
6
The switch shall support split-chassis detection to maintain network integrity when one or more virtual-chassis members fail.
C / PC / NC
7
The switch shall provide a minimum switching capacity of 2.16 Tbps and a maximum port-to-port latency of 650 ns.
C / PC / NC
8
The switch shall run a single, vendor-hardened, container-based proprietary NOS built on a current long-term-support Linux distribution; the NOS license shall be per-device subscription with one-, three-, and five-year terms.
9
The switch shall support a maximum power consumption of 400 W under full Layer-2 traffic load with two power supplies installed.
C / PC / NC
10
The switch shall provide a minimum MTBF of 384,000 hours with AC power supplies and 385,000 hours with DC power supplies.
C / PC / NC
11
Operating temperature: 0 deg C to 45 deg C.
C / PC / NC
12
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Leaf Switch Option 3: 10G/100G (10GBASE-T)
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor with non-blocking architecture.
C / PC / NC
2
The switch shall provide a minimum of 48 x 1G/10GBASE-T copper ports with auto-negotiation.
C / PC / NC
3
The switch shall provide a minimum of 6 x QSFP28 ports operating at 40 or 100 GbE, with at least 2 QSFP28 ports supporting breakout to 4 x 10 GbE or 4 x 25 GbE.
C / PC / NC
4
The switch shall provide a virtual-chassis architecture with up to six elements stacked through dedicated chassis-interconnect ports, manageable through a single management IP address.
C / PC / NC
5
The switch shall implement a MAC-address retention mechanism that preserves the MAC address of the master unit across virtual-chassis takeovers, in order to avoid Spanning Tree and Link Aggregation re-convergence.
C / PC / NC
6
The switch shall support split-chassis detection to maintain network integrity when one or more virtual-chassis members fail.
C / PC / NC
7
The switch shall provide a minimum switching capacity of 2.16 Tbps and a maximum port-to-port latency of 650 ns.
C / PC / NC
8
The switch shall run a single, vendor-hardened, container-based proprietary NOS built on a current long-term-support Linux distribution; the NOS license shall be per-device subscription with one-, three-, and five-year terms.
9
The switch shall support a maximum power consumption of 310 W under full Layer-2 traffic load with two power supplies installed.
C / PC / NC
10
The switch shall provide a minimum MTBF of 372,000 hours with AC power supplies and 373,000 hours with DC power supplies.
C / PC / NC
11
The switch shall provide redundant and hot-swappable power supplies and fan trays.
C / PC / NC
12
Operating temperature: 0 deg C to 45 deg C.
C / PC / NC
13
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Management network switch
The management network switch carries device BMC traffic, serial-console concentrator traffic, and orchestration traffic. It must be a copper-port access switch and shall implement the same software feature set as the front-end access switches so that the customer can rationalise the spare-parts inventory and the operational procedures across the front-end and management networks.
#
Requirement
C / PC / NC
1
The switch shall be a 1RU form factor with non-blocking architecture.
C / PC / NC
2
The switch shall provide a minimum of 48 x 1G/10GBASE-T copper ports with auto-negotiation.
C / PC / NC
3
The switch shall provide a minimum of 6 x QSFP28 ports operating at 40 or 100 GbE, with at least 2 QSFP28 ports supporting breakout to 4 x 10 GbE or 4 x 25 GbE.
C / PC / NC
4
The switch shall provide a virtual-chassis architecture with up to six elements stacked through dedicated chassis-interconnect ports, manageable through a single management IP address.
C / PC / NC
5
The switch shall implement a MAC-address retention mechanism that preserves the MAC address of the master unit across virtual-chassis takeovers, in order to avoid Spanning Tree and Link Aggregation re-convergence.
C / PC / NC
6
The switch shall support split-chassis detection to maintain network integrity when one or more virtual-chassis members fail.
C / PC / NC
7
The switch shall provide a minimum switching capacity of 2.16 Tbps and a maximum port-to-port latency of 650 ns.
C / PC / NC
8
The switch shall run a single, vendor-hardened, container-based proprietary NOS built on a current long-term-support Linux distribution; the NOS license shall be per-device subscription with one-, three-, and five-year terms.
9
The switch shall support a maximum power consumption of 310 W under full Layer-2 traffic load with two power supplies installed.
C / PC / NC
10
The switch shall provide a minimum MTBF of 372,000 hours with AC power supplies and 373,000 hours with DC power supplies.
C / PC / NC
11
The switch shall provide redundant and hot-swappable power supplies and fan trays.
C / PC / NC
12
Operating temperature: 0 deg C to 45 deg C.
C / PC / NC
13
Storage temperature: -40 deg C to 70 deg C.
C / PC / NC
Common switch software features
Before the requirements are presented, it is important to understand the design driver behind them. The AI Data Center solution operates two distinct networks with different traffic profiles, and the bidder is allowed to run a different Network Operating System (NOS) on each network. However, in order to deliver a coherent end-to-end fabric, the two NOSes shall converge on a common baseline of architectural, control-plane, data-plane, and operational features. The requirements in this section define that common baseline.
Every requirement in this section applies to both the front-end network and the back-end network. The bidder shall answer every line item twice -- once for the front-end NOS, and once for the back-end NOS -- using the C / PC / NC convention defined below. A blank cell will be treated as Non-Compliant.
NOS architecture and lifecycle
The Network Operating System shall be a modern, modular, container-based Linux distribution. A monolithic, closed-source operating system is not acceptable.
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall be a container-based, modular software distribution running on a current long-term-support Linux base. Each NOS daemon (routing, platform, telemetry, management) shall be packaged as a discrete container that can be started, stopped, upgraded, and monitored independently of the other daemons.
C / PC / NC
C / PC / NC
2
The NOS shall implement an ASIC-abstraction layer that conforms to the Switch Abstraction Interface (SAI), so that the data-plane code is portable across switch ASICs from multiple silicon vendors and the customer is not bound to a single silicon vendor over the lifetime of the deployment.
C / PC / NC
C / PC / NC
3
The NOS shall implement multiple Virtual Routing and Forwarding (VRF) instances on the data plane and the control plane. Each routing instance shall independently maintain its own routing table, forwarding table, peer table, and interface table; per-VRF loopback assignment, per-VRF ping, and per-VRF SSH shall be supported.
C / PC / NC
C / PC / NC
4
The NOS shall implement VRF Route Leaking between any pair of VRFs, controlled by route-target import and export policies, without requiring an external route reflector or service-provider edge platform.
C / PC / NC
C / PC / NC
5
The NOS shall implement configuration persistence, configuration reset, configuration backup, and named configuration-snapshot mechanisms. The operator shall be able to compare two named configuration snapshots (configuration diff) from the CLI.
C / PC / NC
C / PC / NC
6
The NOS shall implement Zero Touch Provisioning, both in-band (data-plane interfaces) and out-of-band (dedicated management interface), with no on-site human intervention at first boot.
C / PC / NC
C / PC / NC
Lossless Ethernet for RoCEv2
RDMA over Converged Ethernet version 2 (RoCEv2) is the foundation of the AI Data Center fabric. Both NOSes shall implement the full set of lossless-Ethernet primitives required to deliver predictable tail latency under collective-communication bursts.
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement Priority Flow Control (PFC) per IEEE 802.1Qbb, including asymmetric PFC (different PFC behavior per direction), with per-Class-of-Service queue PAUSE / UNPAUSE thresholds configurable per port and per QoS group.
C / PC / NC
C / PC / NC
2
The NOS shall implement a PFC watchdog function that detects per-priority PAUSE-frame deadlock on an egress queue and recovers the queue automatically without operator intervention, with operator-configurable detection and recovery timers. Deployments without PFC watchdog are exposed to permanent fabric stall under deadlock conditions.
C / PC / NC
C / PC / NC
3
The NOS shall implement Explicit Congestion Notification (ECN) marking per RFC 3168 and shall expose ECN-mark statistics per queue and per port via streaming telemetry, in addition to per-port aggregate counters.
C / PC / NC
C / PC / NC
4
The NOS shall implement Weighted Random Early Detection (WRED) on egress queues, with operator-configurable marking thresholds per queue.
C / PC / NC
C / PC / NC
5
The NOS shall provide eight hardware-based egress queues per port, with strict-priority and Deficit Weighted Round Robin (DWRR) scheduling algorithms selectable per queue.
C / PC / NC
C / PC / NC
6
The NOS shall implement per-port and per-queue egress traffic shaping with operator-configurable shaped rates and shall implement ingress-port rate limiting (policing).
C / PC / NC
C / PC / NC
EVPN-VXLAN overlay
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement Virtual eXtensible LAN (VXLAN) Tunnel Endpoints (VTEP) in hardware, with line-rate encapsulation and decapsulation. Multi-VTEP per switch shall be supported. IPv4-over-IPv4 and IPv6-over-IPv4 outer encapsulation shall both be supported.
C / PC / NC
C / PC / NC
2
The NOS shall implement BGP-EVPN as the overlay control plane, with every one of the following EVPN route types: Ethernet Auto-Discovery (Type 1), MAC/IP advertisement (Type 2), Ethernet Segment Route (Type 4), and IP Prefix advertisement (Type 5). Implementations that support only Type 2 routes shall be treated as non-compliant.
C / PC / NC
C / PC / NC
3
The NOS shall implement an EVPN anycast gateway with symmetric Integrated Routing and Bridging (IRB), so that any leaf switch can serve as the default gateway for the attached hosts and inter-subnet routing scales horizontally with the number of leaves.
C / PC / NC
C / PC / NC
4
The NOS shall implement EVPN host mobility (VM migration), so that a host that moves between leaves is detected and announced in BGP-EVPN without operator intervention and without flooding.
C / PC / NC
C / PC / NC
5
The NOS shall implement EVPN multi-homing using Ethernet Segment Identifiers (ESI) on the LAG facing the host, so that a host can be dual-homed to two leaf switches with active-active forwarding.
C / PC / NC
C / PC / NC
6
The NOS shall implement ARP/ND suppression on VTEP interfaces, so that ARP and Neighbor Discovery traffic is answered locally on the ingress leaf rather than flooded across the overlay.
C / PC / NC
C / PC / NC
7
The NOS shall implement Ingress Replication for Layer-2 BUM (broadcast, unknown-unicast, multicast) traffic over VXLAN tunnels.
C / PC / NC
C / PC / NC
8
The NOS shall implement EVPN-VXLAN-based Data Center Interconnect (DCI) over a segment VXLAN tunnel between two or more sites.
C / PC / NC
C / PC / NC
Layer-3 routing (IPv4 and IPv6)
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement Open Shortest Path First version 2 (OSPFv2) with all four network types (Broadcast, Non-Broadcast, Point-to-Point, Point-to-Multipoint), multiple OSPF instances, Stub and Not-So-Stubby Areas (NSSA), MD5 authentication, and route redistribution between OSPFv2 and BGP.
C / PC / NC
C / PC / NC
2
The NOS shall implement Open Shortest Path First version 3 (OSPFv3) for IPv6.
C / PC / NC
C / PC / NC
3
The NOS shall implement Border Gateway Protocol version 4 (BGPv4) with Route Reflection, AS-Path replace, IPv4 and IPv6 peer types, and route redistribution. Implementations that lack AS-Path replace shall be treated as non-compliant.
C / PC / NC
C / PC / NC
4
The NOS shall implement BGP Graceful Restart helper.
C / PC / NC
C / PC / NC
5
The NOS shall implement BGP Unnumbered (BGP over IPv6 link-local), so that the operator can build a Layer-3 fabric without provisioning point-to-point IP addresses on every fabric link.
C / PC / NC
C / PC / NC
6
The NOS shall implement Multiprotocol BGP (MP-BGP) with IPv4 and IPv6 address families.
C / PC / NC
C / PC / NC
7
The NOS shall implement Bidirectional Forwarding Detection (BFD) per RFC 5880 with sub-second timers, and BFD shall be supported under all the following routing protocols: static routing, BGP, OSPFv2, OSPFv3.
C / PC / NC
C / PC / NC
8
The NOS shall implement routing-policy primitives: IPv4 Prefix Lists, IPv6 Prefix Lists, and Route Maps with match and set operations.
C / PC / NC
C / PC / NC
9
The NOS shall implement Equal-Cost Multipath (ECMP) load balancing with operator-configurable hash key (IPv4, IPv6, and Ethernet header fields) and operator-configurable hash seed, so that the operator can mitigate ECMP polarization in multi-stage Clos topologies.
C / PC / NC
C / PC / NC
10
The NOS shall implement Policy-Based Routing (PBR) for IPv4 and IPv6.
C / PC / NC
C / PC / NC
11
The NOS shall implement Address Resolution Protocol (ARP) with static ARP, dynamic ARP, configurable aging, Gratuitous ARP, and Proxy ARP.
C / PC / NC
C / PC / NC
Layer-2 services
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement IEEE 802.1Q VLANs and VLAN trunks. The operator shall be able to configure VLAN ranges directly on switch-port commands.
C / PC / NC
C / PC / NC
2
The NOS shall implement IEEE 802.3ad / IEEE 802.1AX Link Aggregation Control Protocol (LACP) with operator-configurable system priority, port priority, LACP key, minimum-active links, and fast / slow rate. LACP fallback shall be supported for graceful degradation when the LACP peer is unavailable at first boot.
C / PC / NC
C / PC / NC
3
The NOS shall expose configurable load-balancing hash keys (non-IP, IPv4, IPv6) and operator-configurable hash seed for Link Aggregation, in addition to the same controls for ECMP (Section 14.4 item 9).
C / PC / NC
C / PC / NC
4
The NOS shall implement IEEE 802.1AB Link Layer Discovery Protocol (LLDP) with neighbor information TLVs (Chassis ID, Port ID, TTL, Port Description, System Name, System Capability, Management Address).
C / PC / NC
C / PC / NC
Quality of Service and ACLs
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement Access Control Lists (ACLs) for Layer-2, IPv4, and IPv6 traffic, with permit and deny actions, and match conditions on at least physical port, Ethernet header (Destination Address, Source Address, EtherType), IPv4 5-tuple, and IPv6 5-tuple fields.
C / PC / NC
C / PC / NC
2
The NOS shall implement IEEE 802.1p Class of Service (CoS) classification and DSCP classification on ingress.
C / PC / NC
C / PC / NC
3
The NOS shall implement CoS and DSCP marking and re-marking on ingress and egress.
C / PC / NC
C / PC / NC
4
The NOS shall implement the DiffServ architecture per RFC 2475.
C / PC / NC
C / PC / NC
Security and AAA
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement Control Plane Policing (CoPP) with operator-configurable rate-limit and burst profiles for management-plane and configuration traffic.
C / PC / NC
C / PC / NC
2
The NOS shall implement administrator authentication via TACACS+ and via RADIUS per RFC 2865. Per-user role assignment shall be sourced from the remote AAA server.
C / PC / NC
C / PC / NC
3
The NOS shall implement Secure Shell version 2 with public-key infrastructure (PKI), SFTP, and HTTPS for management-plane access.
C / PC / NC
C / PC / NC
Telemetry and visibility
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall implement a native streaming-telemetry service that exports platform, interface, queue, buffer, and protocol counters at operator-configurable sample rates, without polling.
C / PC / NC
C / PC / NC
2
The NOS shall implement Syslog with remote-syslog forwarding, log rotation, and configurable severity levels.
C / PC / NC
C / PC / NC
3
The NOS shall implement a sysdump and core-dump collection facility that captures the switch state for offline analysis.
C / PC / NC
C / PC / NC
4
The NOS shall expose Digital Optical Monitoring (DOM) data on every fiber-optic transceiver, including transmit power, receive power, temperature, and supply voltage.
C / PC / NC
C / PC / NC
5
The NOS shall expose a system-health view aggregating platform, thermal, transceiver-sensor, and protocol-state indicators in a single operator interface.
C / PC / NC
C / PC / NC
Management and programmability
#
Requirement
Front-end (C/PC/NC)
Back-end (C/PC/NC)
1
The NOS shall expose a RESTful management API that surfaces the complete platform configuration and operational state as a programmable data structure (e.g., RESTConf / OpenConfig-style YANG models or a documented JSON schema). Read-only CLI scraping is not acceptable.
C / PC / NC
C / PC / NC
2
The NOS shall expose a Console interface, a Telnet interface, and a Secure Shell version 2 interface. TFTP client and TFTP server functionality shall be supported for image and configuration transfer.
C / PC / NC
C / PC / NC
3
The NOS shall implement a Management VRF that separates the management plane from the data-plane forwarding instance, so that management traffic does not transit the production VRFs.
C / PC / NC
C / PC / NC
4
The NOS shall implement Network Time Protocol (NTPv4 and NTPv6) with a configurable loopback as NTP source, and a DNS client over IPv4 and IPv6.
C / PC / NC
C / PC / NC
5
The NOS shall implement SNMP read-only access for compatibility with legacy monitoring systems, in addition to the streaming-telemetry interface required in the “Telemetry and visibility” section.
C / PC / NC
C / PC / NC
Conclusion
The requirements in this document define an AI Data Center solution that is engineered for the specific needs of distributed GPU training and inference workloads. The combination of a high-radix 800 Gigabit Ethernet back-end fabric with a dual Network Operating System strategy, a single modern container-based proprietary NOS on the front-end network, a converged on-premises orchestration platform, and an OAM-based GPU server delivers a standards-based alternative to single-vendor, proprietary AI fabrics, while preserving the operator ability to mix and match merchant silicon, NOS options, and GPU vendors over the life of the platform.
The bidder is expected to answer every line item with the compliance convention defined in the Introduction section, and to provide the public datasheet, release-notes reference, or test report that substantiates each "C" answer. The bidder is also expected to provide a reference Bill of Materials and a reference cabling diagram for at least two scale points: a single-rack pilot (8 GPUs / 16 GPUs) and an eight-rack production pod (256 GPUs), in both classic Clos and rail-optimised variants.