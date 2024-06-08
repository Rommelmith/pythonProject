from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


# Path to your local HTML file
Link = r'C:\Users\romme\PycharmProjects\pythonProject\voice.html'

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")

# Initialize Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)
sleep(2)

def SpeechRecognition():
    driver.find_element(by=By.ID, value="start").click()
    print("Listening....")

    while True:
        Text = driver.find_element(by=By.ID, value="output").text
        if Text:
            driver.find_element(by=By.ID, value="end").click()
            return Text
        else:
            sleep(0.222)

try:
    while True:
        Text = SpeechRecognition()
        print(Text)
finally:
    driver.quit()
