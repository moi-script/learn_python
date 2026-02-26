# Tell Scapy to use the modern Npcap driver BEFORE importing everything else
from scapy.config import conf
conf.use_pcap = True

from scapy.all import sniff, DNS, DNSQR

def detect_ai_usage(pkt):
    # Check if the packet has a DNS Layer and is a Query (qr=0)
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        try:
            query_name = pkt.getlayer(DNSQR).qname.decode('utf-8')
            
            # List of "Forbidden" AI domains
            ai_domains = ["chatgpt.com", "openai.com", "claude.ai", "gemini.google.com"]
            
            if any(domain in query_name for domain in ai_domains):
                print(f"[!] ALERT: Device {pkt[1].src} is trying to access {query_name}")
        except Exception:
            pass # Ignore packets that can't be decoded properly

print("Monitoring classroom network for AI signatures using Npcap...")

# Start sniffing on port 53 (DNS)
sniff(filter="udp port 53", prn=detect_ai_usage, store=0)