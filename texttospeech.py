import pyttsx3

def texttospeech(text, rate=200):
    engine = pyttsx3.init()
    # rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
