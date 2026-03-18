from machine import Pin
import time
import test   # 👈 import your new file

print('Hello from Git')

# Setup LED on Pin 8
led = Pin(8, Pin.OUT)

# Call function from test.py
test.run_test()

while True:
    for i in range(5):
        led.value(0)
        time.sleep(1)
        led.value(1)
        time.sleep(1)

    # Optional: call test blink
    test.blink_fast(led)
    
def run_test():
    print("Test.py is working!")

def blink_fast(led):
    import time
    for i in range(5):
        led.value(0)
        time.sleep(0.2)
        led.value(1)
        time.sleep(0.2)
