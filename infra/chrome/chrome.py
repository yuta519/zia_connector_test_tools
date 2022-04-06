import platform
import time

from selenium import webdriver


def _decide_chromedriver_by_os():
    os = platform.system()
    if os == "Windows":
        return "infra/chrome/driver/win/chromedriver"
    elif os == "Darwin":
        return "infra/chrome/driver/mac/chromedriver"
    elif os == "Linux":
        return "infra/chrome/driver/linux/chromedriver"


chrome_driver_path = _decide_chromedriver_by_os()


def initialize_driver() -> webdriver:
    return webdriver.Chrome(executable_path=chrome_driver_path)


def destroy_driver(driver: webdriver) -> None:
    driver.close()


def get(driver: webdriver, url: str) -> None:
    driver.get(url)
    # driver.save_screenshot("logs/screenshot/screen.png")
    time.sleep(1)


def take_screenshot(driver: webdriver) -> None:
    driver.save_screenshot("logs/screenshot/screen.png")
