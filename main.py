# This is a test file of the OTA code
from machine import Pin
import time

print('Hello from Git')

# Setup LED on Pin 8
led = Pin(8, Pin.OUT)

while True:
    led.value(1)    # Turn LED on
    time.sleep(1) # Sleep for 1 seconds
    led.value(0)    # Turn LED off
    time.sleep(1) # Sleep for 1 seconds
