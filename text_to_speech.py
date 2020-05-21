from gtts import gTTS 
import os
text = "Hola Salva"
language = 'es'
speech = gTTS(text = text, lang = language, slow = False)
speech.save('text.mp3')
os.system('start text.mp3')