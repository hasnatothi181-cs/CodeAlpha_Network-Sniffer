!pip install scapy    # python library for packet capturing.

from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):         #process_packet(packet) will run every time a packet comes

    if IP in packet:            #chechking ip
        ip = packet[IP]

        src_ip = ip.src          #sender address
        dst_ip = ip.dst     #receiver address

        if TCP in packet:         #detecting protocols here
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "Other"

        print("Packet Found!")      #printing packets information
        print("From:", src_ip)
        print("To:", dst_ip)
        print("Protocol:", protocol)


        if Raw in packet:           #chechking packet data (if any present)
            data = packet[Raw].load
            print("Data:", data[:20])  # for printinf only first 20 characters

        print("\n=======================\n")

print("Capturing packets...\n")

sniff(prn=process_packet,

      timeout=5)       #sniff is listening to packets for 5 sec

print("\nFinished!")