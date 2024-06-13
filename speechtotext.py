import speech_recognition as sr

def speechtotext():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:  
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

