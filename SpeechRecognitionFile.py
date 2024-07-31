from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

# Path to your local HTML file
Link = r'C:\Users\romme\PycharmProjects\pythonProject\voice.html'  # Your webpage path

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")

# Initialize Chrome driver
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)
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

if __name__ == "__main__":
    try:
        while True:
            Text = SpeechRecognition()
            print(Text)
    finally:
        driver.quit()