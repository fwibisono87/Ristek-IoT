import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

readPin = 17
ledPin = 21
global ledIsOn
ledIsOn = False

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def home():
        return f"""<html><body><p>{detectLight()}</p></body></html>"""
@app.get("/led")
def led():
        return f"""<html><body><p>{ledSwitch()}</p></body></html>"""
def detectLight():
        data = GPIO.input(readPin)
        if data != 1:
                return True
        else:
                return False

def ledSwitch():
        if GPIO.input(ledPin):
                GPIO.output(ledPin, GPIO.LOW)
        else:
                GPIO.output(ledPin, GPIO.HIGH)
        #ledIsOn = not ledIsOn
        #return ledIsOn
        return GPIO.input(ledPin)

if __name__ == "__main__":
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(readPin, GPIO.IN)
        GPIO.setup(ledPin, GPIO.OUT)

        uvicorn.run(app, host='127.0.0.1', port=5555, debug=True)
