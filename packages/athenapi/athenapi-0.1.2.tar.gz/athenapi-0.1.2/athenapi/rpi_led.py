import RPi.GPIO as GPIO


class LED(object):
    def __init__(self, pinNum):
        self.pin = pinNum
        self.isOn = False
        GPIO.setup(pinNum, GPIO.OUT)

    def turn_on(self):
        self.isOn = True
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        self.isOn = False
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        if self.isOn:
            self.turn_off()
        else:
            self.turn_on()
