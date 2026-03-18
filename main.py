# This is a test file of the OTA code
from machine import Pin
import time

print('Hello from Git')

# Setup LED on Pin 8
led = Pin(8, Pin.OUT)

while True:
    led.value(1)    # Turn LED on
    time.sleep(0.2) # Sleep for 0.5 seconds
    led.value(0)    # Turn LED off
    time.sleep(0.2) # Sleep for 0.5 seconds
