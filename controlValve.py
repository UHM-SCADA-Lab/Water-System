import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Sub Tank Sensor
GPIO.setup(15, GPIO.OUT)                            # Output To Relay 2 (top valve)   
GPIO.setup(18, GPIO.OUT)                            # Output To Relay 3 (bottom valve)   

try:
    while True:
        if (GPIO.input(10) == GPIO.LOW):   # Sub Tank Sensor covered with water
            GPIO.output(15,1)              # Open Relay 2 (close top valve)
            print("TOP CLOSED",end=" ")
            GPIO.output(18,0)              # Close Relay 3 (open bottom valve)
            print("BTM OPEN")
            print("SLEEP")
            time.sleep(2)
        elif (GPIO.input(10) == GPIO.HIGH): # Sub Tank Sensor not cover with water
            GPIO.output(15,0)              # Close Relay 2 (open top valve)
            print("TOP OPEN",end=" ")
            GPIO.output(18,1)              # Open Relay 3 (close bottom valve)
            print("BTM CLOSED")

finally:
    GPIO.cleanup()
