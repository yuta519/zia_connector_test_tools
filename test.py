from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="./chromedriver")

# Googleの検索画面を開く
driver.get("https://www.google.co.jp/")
# 5秒間待機
time.sleep(5)
# ブラウザを終了する
driver.close()
