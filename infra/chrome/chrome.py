import platform

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def _decide_chromedriver_by_os():
    os = platform.system()
    if os == "Windows":
        return "infra/chrome/driver/win/chromedriver"
    elif os == "Darwin":
        return "infra/chrome/driver/mac/chromedriver"
    elif os == "Linux":
        return "infra/chrome/driver/linux/chromedriver"


chrome_driver_path = _decide_chromedriver_by_os()


def initialize_driver() -> WebDriver:
    return webdriver.Chrome(executable_path=chrome_driver_path)


def destroy_driver(driver: WebDriver) -> None:
    driver.close()


def get(driver: WebDriver, url: str) -> None:
    driver.get(url)


def take_screenshot(driver: WebDriver) -> None:
    driver.save_screenshot("logs/screenshot/screen.png")


def fetch_pagesource(driver: WebDriver) -> str:
    return driver.page_source


def fetch_page_title(driver: WebDriver) -> str:
    return driver.title
