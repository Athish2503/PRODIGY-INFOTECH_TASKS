import scapy.all as scapy

def packet_sniffer(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        print(f"IP Source: {ip_src} --> IP Destination: {ip_dst} | Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Payload: {payload}")

def start_sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=packet_sniffer)

if __name__ == "__main__":
    interface = input("Enter the interface to sniff (e.g., eth0): ")
    print("\nPacket Sniffing started...\n")
    start_sniffing(interface)

