# 🛡️ SecureMind ICMP Packet Crafter

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scapy-Security-red?style=for-the-badge" alt="Scapy">
  <img src="https://img.shields.io/badge/Blue_Team-SecureMind-blue?style=for-the-badge" alt="Blue Team">
</div>

## 📖 Overview
The **ICMP Packet Crafter** is an advanced network utility developed by the **SecureMind (Blue Team)**. This tool allows security professionals and SOC analysts to manually craft and transmit Custom ICMP (Internet Control Message Protocol) packets. 

By enabling users to specify both the **Source IP** and **Destination IP**, this tool is highly effective for testing firewall rules, validating network routing configurations, and simulating IP spoofing scenarios to ensure monitoring systems are properly alerting on suspicious traffic.

## ✨ Features
* **Custom Packet Crafting:** Define specific Source and Destination IP addresses.
* **IP Spoofing Simulation:** Test network defenses by spoofing the source address of the ICMP packets.
* **Deep Packet Inspection:** Automatically captures and displays detailed breakdowns of the received reply packets using Scapy's built-in packet dissection.
* **Continuous Execution:** Send multiple custom packets in a single session without restarting the tool.
* **Cross-Platform:** Works seamlessly on both Linux and Windows environments (requires root/admin privileges).

## 🛠️ Prerequisites
* **Python 3.x**
* **Root/Administrator Privileges:** Modifying network layers and crafting raw IP packets requires elevated OS permissions.
* *(For Windows Users)*: Ensure [Npcap](https://npcap.com/) is installed for Scapy to interact with network interfaces.

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/icmp_package_tool.git](https://github.com/YourUsername/icmp_package_tool.git)
   cd icmp_package_tool
