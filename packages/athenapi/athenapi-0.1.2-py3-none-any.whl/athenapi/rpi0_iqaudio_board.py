import time
import pkg_resources
import RPi.GPIO as GPIO
from athenapi.microphone import Microphone
from athenapi.rpi_button import Button
from athenapi.rpi_led import LED
from athenapi.speaker import Speaker
from athenapi.rpi_zero_camera import RpiZeroCamera

beep_up = pkg_resources.resource_filename('athenapi', 'assets/beep-up.wav')
beep_down = pkg_resources.resource_filename('athenapi', 'assets/beep-down.wav')
camera = pkg_resources.resource_filename('athenapi', 'assets/camera.mp3')

class Rpi0IQAudioBoard(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self._button = Button(27, press_callback=self._button_press_callback,
                              long_press_callback=self._button_long_press_callback)
        self._greenLED = LED(23)
        self._redLED = LED(24)
        self._speaker = Speaker('IQaudIO')
        self._microphone = Microphone()
        self._is_recording = False
        self._camera = RpiZeroCamera()
        self._photos = []
        self._started = False

    def _button_press_callback(self):
        self._is_recording = not self._is_recording

    def _button_long_press_callback(self):
        self._speaker.start()
        self._speaker.play_audio(camera)
        self._photos.append(self._camera.take_photo())
        self._is_recording = not self._is_recording

    def start(self):
        self._greenLED.turn_on()
        self._started = True

    def stop(self):
        self._greenLED.turn_off()
        self._microphone.stop()
        GPIO.cleanup()
        self._started = False

    def get_photos(self):
        return self._photos

    def reset_photos(self):
        self._photos = []

    def recording(self, file_path):
        def should_stop():
            return not self._is_recording

        def on_start():
            self._speaker.play_audio(beep_up)
            

        self._speaker.stop()
        while not self._is_recording:
            time.sleep(0.1)
            
        self._speaker.start()
        self._microphone.recording(file_path, should_stop, on_start)
        self._speaker.play_audio(beep_down)

    def play_audio(self, file_path):
        self._speaker.play_audio(file_path)

    def is_playing(self):
        return self._speaker.is_playing()
