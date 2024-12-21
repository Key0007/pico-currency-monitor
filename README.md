# pico-currency-monitor

A Raspberry Pi Pico W project that displays live currency exchange rates on a TM1637 4-digit display. Currently configured for USD/EUR pair.

## Hardware Required

- Raspberry Pi Pico W
- TM1637 4-digit 7-segment display
- 4 wires for connections

## Connections

1. TM1637 CLK → Pico GP1
2. TM1637 DIO → Pico GP2
3. TM1637 VCC → Pico 3.3V
4. TM1637 GND → Pico GND

## Pinout

![image](https://github.com/user-attachments/assets/0dbf1a46-9f78-4ba0-a7f4-ad30bc4eaf4a)



## Setup

1. Get your Pico W ready:

- Hold the BOOTSEL button on your Pico W
- While holding, plug the USB cable into your computer
- Release the button after connecting

2. Install MicroPython:

- Your Pico should appear as a USB drive on your computer
- Download the latest MicroPython firmware (.uf2 file) from Raspberry Pi's official [site](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
- Drag and drop the .uf2 file onto the Pico drive
- The Pico will automatically restart when the file transfer is complete

3. Install tm1637 library

Edit the WiFi credentials in the code to match your network then in the Python shell/REPL, run `install_TM1637.py`. This will install the library on Pico.

4. Upload the code:
   - Download `main.py` from this repository
   - Edit the WiFi credentials in the code to match your network
   - Using Thonny or your preferred editor:
     - Open `main.py`
     - Click "Save As"
     - Select "Raspberry Pi Pico"
     - Save as `main.py`

5. Running the project:
   - After saving `main.py`, power up your Pico W
   - The display will show:
     - '----' (test pattern)
     - Then the current exchange rate

The display will update every 5 minutes with fresh rates from Google Finance.
