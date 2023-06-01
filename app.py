import pyttsx3

def SpeakText(text):
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',rate+45)
    engine.say(text)
    engine.runAndWait()

def StopProgram():
    import sys
    sys.exit()
