from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"[+] Packet: {ip_src} -> {ip_dst} | Protocol: {protocol}")
        
        if Raw in packet:
            payload = packet[Raw].load
            print(f"[+] Payload: {payload}")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
