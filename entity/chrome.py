import time

from selenium import webdriver

from infra.chrome import chrome

driver = webdriver.Chrome(executable_path="./infra/chrome/driver/mac/chromedriver")


def get():
    driver.get("https://www.google.co.jp/")
    time.sleep(3)
    driver.close()
