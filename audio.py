import pyaudio
import wave
import gpio
import os
from transcript import transcript

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "test.wav"

audio = pyaudio.PyAudio()
led_blue = gpio.GPIO(gpio.led_blue, 'out')

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, frames_per_buffer=CHUNK)
print(str('음성 녹음 시작...'))
led_blue.write_value(1)
frames = []

threshold = 800
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
   data = stream.read(CHUNK)
   frames.append(data)
print('음성 녹음 완료')
led_blue.write_value(0)

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

data = open('./test.wav', 'rb').read()
data = transcript(data)
print('you said : ', data)

def hasWord(script, word):
    word = word.replace(' ', '')
    for result in script['results']:
        for alternative in result['alternatives']:
            if alternative['transcript'].replace(' ', '').find(word) is not -1:
                return True
    return False


if hasWord(data, '자기소개'): 
    os.system('aplay introduce.wav')
elif hasWord(data, '비트박스'):
    os.system('aplay bitbox.wav')
else :
    os.system('aplay unknown.wav')
