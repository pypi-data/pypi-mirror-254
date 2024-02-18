from time import sleep
from picamera import PiCamera
from io import BytesIO

class RpiZeroCamera(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)


    def take_photo(self):
        photo = BytesIO() 
        self.camera.start_preview()
        self.camera.capture(photo, 'jpeg')
        photo.seek(0)
        return photo

