import RPi.GPIO as GPIO
import time
from dictionary import characters

def led_control(sleep):
    GPIO.output(message_led, GPIO.HIGH)
    time.sleep(sleep)
    GPIO.output(message_led, GPIO.LOW)
    time.sleep(0.5)


message_led = 7
transmit_indicator = 8
write_indicator = 36#

GPIO.setmode(GPIO.BOARD)
GPIO.setup(message_led, GPIO.OUT)
GPIO.setup(transmit_indicator, GPIO.OUT)
GPIO.setup(write_indicator, GPIO.OUT)



GPIO.output(message_led, GPIO.LOW)
GPIO.output(transmit_indicator, GPIO.LOW)
GPIO.output(write_indicator, GPIO.LOW)

try:
counter = 0
while True:
    GPIO.output(message_led, GPIO.HIGH)
    time.sleep(0.166)
    GPIO.output(message_led, GPIO.LOW)
    time.sleep(0.166)
    GPIO.output(write_indicator, GPIO.HIGH)
    time.sleep(0.166)
    GPIO.output(write_indicator, GPIO.LOW)
    time.sleep(0.166)
    GPIO.output(transmit_indicator, GPIO.HIGH)
    time.sleep(0.166)
    GPIO.output(transmit_indicator, GPIO.LOW)
    time.sleep(0.170)
    counter+=1
    print(counter)
except KeyboardInterrupt:
GPIO.output(message_led, GPIO.HIGH)
GPIO.output(write_indicator, GPIO.HIGH)
GPIO.output(transmit_indicator, GPIO.HIGH)
time.sleep(0.2)
GPIO.output(message_led, GPIO.LOW)
GPIO.output(write_indicator, GPIO.LOW)
GPIO.output(transmit_indicator, GPIO.LOW)
time.sleep(0.2)
GPIO.output(message_led, GPIO.HIGH)
GPIO.output(write_indicator, GPIO.HIGH)
GPIO.output(transmit_indicator, GPIO.HIGH)
time.sleep(0.2)
GPIO.output(message_led, GPIO.LOW)
GPIO.output(write_indicator, GPIO.LOW)
GPIO.output(transmit_indicator, GPIO.LOW)
time.sleep(0.2)
GPIO.cleanup()


GPIO.cleanup();