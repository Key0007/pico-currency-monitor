import mip
import network   
import urequests 
import ure as re

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# connect to wifi
wlan.connect('SSID', 'password')
mip.install("github:mcauser/micropython-tm1637")
