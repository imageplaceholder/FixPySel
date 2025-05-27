from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import time
import os

# --- Setup virtual display (headless) ---
display = Display(visible=0, size=(1200, 1200))
display.start()

# --- Auto install chromedriver ---
chromedriver_autoinstaller.install()

# --- Setup Chrome options ---
chrome_options = Options()
options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://github.com')
print(driver.title)
with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {driver.title}")

