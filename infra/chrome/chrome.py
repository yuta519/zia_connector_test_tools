import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="infra/chrome/driver/mac/chromedriver")


def get(url: str) -> None:
    driver.get(url)
    time.sleep(3)
    driver.close()
