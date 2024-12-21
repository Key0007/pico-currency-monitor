import network
import urequests
import tm1637
from machine import Pin
import time

tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
tm.show('    ')
time.sleep(0.2)
tm.show('----')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# connect to wifi
wlan.connect('SSID', 'password')

def scrape_exchange_rate():
    
    """Scrapes current USD/EUR exchange rate from Google finance"""

    url = "https://www.google.com/finance/quote/USD-EUR"
    response = urequests.get(url)
    chunk_size = 100
    buffer = bytearray(chunk_size)
    
    data_last_price = b'data-last-price="'
    closing_quote = b'"'
    found_start = False
    rate = ""
    
    while True:
        bytes_read = response.raw.readinto(buffer)
        if not bytes_read:
            break
        
        if not found_start:
            start_index = buffer.find(data_last_price)
            if start_index != -1:
                found_start = True
                start_index += len(data_last_price)
                end_index = buffer.find(closing_quote, start_index)
                if end_index != -1:
                    rate = buffer[start_index:end_index].decode('utf-8')
                    break
                else:
                    rate += buffer[start_index:].decode('utf-8')
        else:
            end_index = buffer.find(closing_quote)
            if end_index != -1:
                rate += buffer[:end_index].decode('utf-8')
                break
            else:
                rate += buffer.decode('utf-8')
    
    response.close()
    return round(float(rate), 2)

def display():
    num = scrape_exchange_rate()
    result = str(num).replace('.', '')
    tm.show('    ')
    time.sleep(0.1)
    tm.show(result, True)

while True:
    try:
        display()
        time.sleep(300)
    except:
        tm.show('Err')
        time.sleep(5)