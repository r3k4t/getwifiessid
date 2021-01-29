import os
import sys
from pythonwifi.iwlibs import Wireless

os.system("clear")

print  ('=====================================')
print  ('|         Get Wifi Essid            |')
print  ('=====================================')
print  ('|  Author : Rahat Khan Tusar(rkt)   |')
print  ('| Github : https://github.com/r3k4t |')
print  ('=====================================')

interface = raw_input("Enter Your Linux Interface(Ex:wlp2s0,wlan0,wlp3s0 etc) : ")
wifi = Wireless(interface)
print
print ('Your wifi essid is : -----------------------///')
print ('                                           ////')
print wifi.getEssid(),'<------------------------///////'  
print                               
print ('   Monitor Mode is : -----------------------///')
print ('                                           ////')
print  wifi.getMode(),'<------------------------//////////'                                 




