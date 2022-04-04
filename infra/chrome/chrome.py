import time

from selenium import webdriver

chrome_driver_path = "infra/chrome/driver/mac/chromedriver"


def get(url: str) -> None:
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url)
    time.sleep(1)
    driver.close()
