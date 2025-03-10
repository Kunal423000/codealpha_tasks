from scapy.all import sniff

# Function to process captured packets
def packet_callback(packet):
    print(packet.summary())  # Display basic packet info

# Sniff packets on all interfaces
print("Starting network sniffer...")
sniff(prn=packet_callback, store=False)  # prn calls packet_callback for each packet


