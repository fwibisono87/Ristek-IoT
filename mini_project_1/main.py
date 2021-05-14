import RPi.GPIO as GPIO
import time
from dictionary import characters

def led_control(sleep):
    GPIO.output(message_led, GPIO.HIGH)
    time.sleep(sleep)
    GPIO.output(message_led, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup();

message_led = 7
transmit_indicator = 8
write_indicator = 11##

GPIO.setmode(GPIO.BOARD)
GPIO.setup(message_led, GPIO.OUT)
GPIO.setup(transmit_indicator, GPIO.OUT)
GPIO.setup(write_indicator, GPIO.OUT)

print("welcome to the Raspi Morse Encoder")
print("Enter your message")
GPIO.output(write_indicator, GPIO.HIGH)
message = (raw_input(">>> ")).upper()
if message == "DEMOMODE":
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

if message == "TRAFFIC":
    red_led = write_indicator
    yellow_led = message_led
    green_led = transmit_indicator

    try:
        while True:
            GPIO.output(red_led, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(red_led, GPIO.LOW)
            GPIO.output(yellow_led, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(yellow_led, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(yellow_led, GPIO.HIGH)
            time.sleep(0.4)
            GPIO.output(yellow_led, GPIO.LOW)
            GPIO.output(green_led, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(green_led, GPIO.LOW)
            GPIO.output(yellow_led, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(yellow_led, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(yellow_led, GPIO.HIGH)
            time.sleep(0.4)
            GPIO.output(yellow_led, GPIO.LOW)
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

GPIO.setmode(GPIO.BOARD)
GPIO.output(write_indicator, GPIO.LOW)
GPIO.output(transmit_indicator, GPIO.HIGH)

for char in message:
    time.sleep(2)
    morse_char = characters[char]
    print(morse_char)
    for instruction in morse_char:
        if instruction == "-":
            led_control(0.5)
        elif instruction == ".":
            led_control(0.2)
        elif instruction == "/":
            time.sleep(1)

GPIO.cleanup();