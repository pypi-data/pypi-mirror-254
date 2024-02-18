import wave
import pyaudio


class Microphone(object):
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        info = self.audio.get_default_input_device_info()
        print("Default input device: ", info)

    def __del__(self):
        self.audio.terminate()

    def recording(self, file_path, should_stop, on_start):
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024

        # Initialize PyAudio
        stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                 rate=RATE, input=True, start=True,
                                 frames_per_buffer=CHUNK)

        print("Listening...")

        on_start()

        frames = []
        while should_stop() is False:
            data = stream.read(CHUNK)
            frames.append(data)

        # Stop recording
        stream.stop_stream()
        stream.close()
        print('stopped recording')

        # Write the WAV file
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

    def stop(self):
        self.audio.terminate()
