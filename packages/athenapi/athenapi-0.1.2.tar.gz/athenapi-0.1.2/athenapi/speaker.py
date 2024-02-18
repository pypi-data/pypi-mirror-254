import os
import re
import pyaudio
import pygame


class Speaker(object):
    def __init__(self, device_name=None):
        if device_name is not None:
            index = self._find_audio_device(device_name)
            os.environ['AUDIODEV'] = f'hw:{index},0'
            print("audio device:index", index)


    def _find_audio_device(self, pattern):
        pa = pyaudio.PyAudio()
        device_index = None
        for i in range(pa.get_device_count()):
            device_info = pa.get_device_info_by_index(i)
            device_name = device_info.get('name')
            if re.search(pattern, device_name):
                match = re.search(r'\(hw:(\d+),\d+\)', device_name)
                if match:
                    device_index = match.group(1)
                else:
                    device_index = i
                break
        pa.terminate()
        return device_index

    def start(self):
        pygame.mixer.init()

    def stop(self):
        pygame.mixer.quit()

    def play_audio(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def is_playing(self):
        return pygame.mixer.music.get_busy()
