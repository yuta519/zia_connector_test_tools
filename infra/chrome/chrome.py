import os
import platform
import time

from selenium import webdriver

# chrome_driver_path = "infra/chrome/driver/mac/chromedriver"
def _detect_os():
    os = platform.system()
    if os == "Windows":
        return "infra/chrome/driver/win/chromedriver"
    elif os == "Darwin":
        return "infra/chrome/driver/mac/chromedriver"
    elif os == "Linux":
        return "infra/chrome/driver/linux/chromedriver"


chrome_driver_path = _detect_os()


def get(url: str) -> None:
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url)
    driver.save_screenshot("logs/screenshot/screen.png")
    time.sleep(1)
    driver.close()
