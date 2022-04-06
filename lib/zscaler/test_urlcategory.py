from infra.chrome import chrome
from utils.zscaler.constants import URLCATEGORY_URLS


def access_allow_url(urlcategory: str):
    for url in URLCATEGORY_URLS[urlcategory]:
        driver = chrome.initialize_driver()
        chrome.get(driver, "https://" + url)
        chrome.take_screenshot(driver)
        chrome.destroy_driver(driver)
