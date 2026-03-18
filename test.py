# test.py

def run_test():
    print("Test.py is working!")

def blink_fast(led):
    import time
    for i in range(5):
        led.value(0)
        time.sleep(0.2)
        led.value(1)
        time.sleep(0.2)
