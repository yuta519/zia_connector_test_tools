from infra.chrome import chrome
from utils.zscaler.constants import BLOCK_TITLE
from utils.zscaler.constants import URLCATEGORY_URLS


def access_allow_url(urlcategory: str):
    for url in URLCATEGORY_URLS[urlcategory]:
        try:
            driver = chrome.initialize_driver()
            chrome.get(driver, "https://" + url)
            chrome.take_screenshot(driver)
            if chrome.fetch_page_title(driver) != BLOCK_TITLE:
                print("allowed")
        except:
            print("???")

        chrome.destroy_driver(driver)
