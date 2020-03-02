import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="cs-CS")
        print("Řekl jsi: {}".format(text))

    except:
        print("Co kurva? Nauč se mluvit!")
