#Configration Packet
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1

while True :
    try :
        #Collect Ip
        src_ip = input("Enter source IP: ")
        dst_ip = input("Enter destination IP: ")
        #Make Package
        ip_head = IP(src = src_ip, dst = dst_ip)
        icmp_op = ICMP(id = 100)
        full_package = ip_head/icmp_op
        packet_sender = sr1(full_package)

        if packet_sender:
            print(packet_sender.show())
        op_u = input("Are You Want To Continue? (y/n):").lower().lower()
        if op_u == "y":
            continue
        else:
            break

    except Exception as e:
        print(e)