import sys
import os
from scapy.all import IP, ICMP, sr1
import pyfiglet
from rich import print

def check_privileges():
    """Check if the script is running with root/administrator privileges."""
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if not is_admin:
        print("[bold red][!] Error: This tool requires Root/Administrator privileges to craft raw packets.[/bold red]")
        print("[bold yellow]Please run the script using 'sudo python main.py' or as Administrator.[/bold yellow]")
        sys.exit(1)

def secure_mind_banner():
    """Print the professional banner for SecureMind Team."""
    print(f"\n[bold italic white on blue]{'-' * 30} ICMP Packet Crafter {'-' * 30}[/]")
    print("[cyan]*[/cyan]" * 81)
    print(pyfiglet.figlet_format("SecureMind Team", justify="center"))
    print("[cyan]*[/cyan]" * 81)

def craft_and_send():
    """Function to collect IPs, craft the ICMP packet, and send it."""
    while True:
        try:
            print("\n[bold yellow]--- Packet Configuration ---[/bold yellow]")
            src_ip = input("Enter Source IP (Real or Spoofed): ").strip()
            dst_ip = input("Enter Destination IP: ").strip()

            if not src_ip or not dst_ip:
                print("[bold red][!] IP addresses cannot be empty. Please try again.[/bold red]")
                continue

            print(f"\n[bold green][*] Crafting ICMP packet from {src_ip} to {dst_ip}...[/bold green]")
            
            # Crafting the Package
            ip_head = IP(src=src_ip, dst=dst_ip)
            icmp_op = ICMP(id=100)
            full_package = ip_head / icmp_op
            
            # Sending packet and waiting for 1 reply
            packet_reply = sr1(full_package, timeout=3, verbose=False)

            if packet_reply:
                print("\n[bold cyan][+] Reply Received! Packet Details:[/bold cyan]")
                packet_reply.show()
            else:
                print("\n[bold red][-] Request timed out. No reply received.[/bold red]")
                print("[italic yellow](Note: If you spoofed the Source IP, the reply was sent to that spoofed IP, or a firewall blocked the request.)[/italic yellow]")

            op_u = input("\nDo you want to send another packet? (y/n): ").strip().lower()
            if op_u != 'y':
                print("\n[bold green][*] Exiting... Stay Secure![/bold green]\n")
                break

        except KeyboardInterrupt:
            print("\n[bold yellow][!] Interrupted by user. Exiting gracefully...[/bold yellow]")
            break
        except Exception as e:
            print(f"\n[bold red][!] An unexpected error occurred: {e}[/bold red]")
            break

def main():
    check_privileges()
    secure_mind_banner()
    craft_and_send()

if __name__ == "__main__":
    main()
