from hugchat import hugchat # pip install hugchat
from SpeechRecognitionFile import SpeechRecognition
import pyttsx3 # pip install pyttsx3
from datetime import datetime
import speedtest # pip install speedtest-cli
import pywhatkit # pip install pywhatkit
import keyboard # pip install keyboard


def speak(Text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 150)
    engine.say(Text)
    engine.runAndWait()


def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path=r"C:\Users\romme\PycharmProjects\pythonProject\cookie.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    # speak(response)
    return response




while True:
    WakeWord =  SpeechRecognition()
    WakeWord = WakeWord.lower()
    WakeWord = str(WakeWord)
    if "nexus" in WakeWord:
        speak("Yes I am here: ")

        Prompt = SpeechRecognition() + " and please give a short and brief answer"
        Prompt.lower()
        print(Prompt)

        if "what is time" in Prompt or "tell me the time" in Prompt or "tell me time" in Prompt or "what is the time" in Prompt:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print("Current time:", current_time)
            speak(f"Current time is {str(current_time)}")

        elif "play" in Prompt:
            Prompt = Prompt.replace("and please give a short and brief answer", "")
            Prompt = Prompt.replace("play", "")
            pywhatkit.playonyt(Prompt)

        elif "close tab" in Prompt or "close this tab" in Prompt or "Close tab" in Prompt:
            keyboard.press("ctrl + w")
            keyboard.release("ctrl + w")

        elif "your name" in Prompt or "who am I talking to" in Prompt:
            speak("my name is nexus, I was made by Rommel")

        elif "internet speed" in Prompt or "wifi speed" in Prompt:
            speak("please wait a while, I am calculating your internet speed sir")
            test = speedtest.Speedtest()
            down = test.download()
            upd = test.upload()
            print(f"Download speed is {down}")
            print(f"Upload speed is {upd}")
            down_mbps = down * 8 / 1_000_000
            upd_mbps = upd * 8 / 1_000_000
            speak(f"You download speed in {down_mbps} MBPS and upload speed is {upd_mbps} MBPS")


        else:
            response = chatBot(Prompt)
            speak(response)


