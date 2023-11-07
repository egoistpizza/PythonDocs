# Kullanıcı tarafından istenen metnin seslendirilmiş halini .mp3 olarak kaydedip oynatan kod.

from gtts import gTTS # pip install gtts
import os
from pygame import mixer # pip install pygame
while True:
    try:
        say = input("Write: ")
        tts = gTTS(say, lang = 'en')
        tts.save(say + ".mp3")
        mixer.init()
        mixer.music.load(say + ".mp3")
        mixer.music.play()
    except:
        mixer.init()
        mixer.music.load(say + ".mp3")
        mixer.music.play()
        continue