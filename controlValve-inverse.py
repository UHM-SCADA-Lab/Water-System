import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Sub Tank Sensor
GPIO.setup(15, GPIO.OUT)                            # Output To Relay 2 (valve 1)   

try:
    GPIO.output(15,0)
    while True:
        if (GPIO.input(10) == GPIO.HIGH):   # Sub Tank Sensor covered with water
            GPIO.output(15,1)              # Open Relay 2 (close valve)
            print("CLOSED")
        elif (GPIO.input(10) == GPIO.LOW): # Sub Tank Sensor not cover with water
            print("SLEEP")
            time.sleep(2)
            GPIO.output(15,0)              # Close Relay 2 (open valve)
            print("OPEN")

        time.sleep(0.1)

finally:
    GPIO.cleanup()
