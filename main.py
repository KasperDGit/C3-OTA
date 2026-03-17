# This is a test file of the OTA code
from machine import Pin
import time

print('Hello Worl')

# Setup LED on Pin 8
led = Pin(8, Pin.OUT)

while True:
    led.value(1)    # Turn LED on
    time.sleep(0.5) # Sleep for 0.5 seconds
    led.value(0)    # Turn LED off
    time.sleep(0.5) # Sleep for 0.5 seconds
