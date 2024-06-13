import texttospeech
import speechtotext
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        texttospeech.texttospeech("My name is virtual assistant", rate=200)
        return "My name is virtual assistant"

    elif "hello" in user_data or "hye" in user_data:
        texttospeech.texttospeech("i am fine, how can i help you", rate=200)
        return "i am fine, how can i help you"

    elif "good morning" in user_data:
        texttospeech.texttospeech("good morning sir", rate=200)
        return "good morning sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time) + "Minute"
        texttospeech.texttospeech(Time, rate=200)
        return Time

    elif "shutdown" in user_data:
        texttospeech.texttospeech("ok sir", rate=200)
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        texttospeech.texttospeech("ganna.com is ready for you", rate=200)
        return "ganna.com is ready for you"

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        texttospeech.texttospeech("youtube.com is ready for you", rate=200)
        return "youtube.com is ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        texttospeech.texttospeech("google.com is ready for you", rate=200)
        return "google.com is ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        texttospeech.texttospeech(ans, rate=200)
        return ans

    else:
        texttospeech.texttospeech("I am not able to understand", rate=200)
        return "I am not able to understand"
