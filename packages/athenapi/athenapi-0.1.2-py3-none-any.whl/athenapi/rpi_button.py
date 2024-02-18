import RPi.GPIO as GPIO
import time


class Button(object):
    def __init__(self, pin_num, press_callback, long_press_callback):
        button_pin = pin_num
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(button_pin, GPIO.BOTH,
                              callback=self._button_callback)
        self.press_time = None
        self._press_callback = press_callback
        self._long_press_callback = long_press_callback

    def _button_callback(self, channel):
        if GPIO.input(channel):
            self._button_rising_callback(channel)
        else:
            self._button_falling_callback(channel)

    def _button_rising_callback(self, channel):
        is_long_press = False
        if self.press_time is not None:
            if time.time() - self.press_time > 1:
                self._long_press_callback()
                is_long_press = True

        if not is_long_press:
            self._press_callback()
        
        self.press_time = None

    def _button_falling_callback(self, channel):
        self.press_time = time.time()
