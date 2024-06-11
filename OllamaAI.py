import ollama # pip install ollama
from SpeechRecognition import SpeechRecognition, driver
from pyttsx3 import speak

def main():
    client = ollama.Client()

    try:
        while True:
            prompt = SpeechRecognition()
            print(f"Recognised text is: {prompt}")

            model = 'llama3'

            response = client.generate(model=model, prompt=prompt)

            TextResponse = response.get('response', "")
            print(f"AI Response: {TextResponse}")
            speak(TextResponse)

    finally:
        driver.quit()

if __name__=="__main__":
    main()
