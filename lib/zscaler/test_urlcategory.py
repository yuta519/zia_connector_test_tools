import logging
from urllib.parse import urlparse

from infra.chrome import chrome
from utils.zscaler.constants import BLOCK_TITLE
from utils.zscaler.constants import URLCATEGORY_URLS


def access_allow_url(urlcategory: str):
    for url in URLCATEGORY_URLS[urlcategory]:
        try:
            url = urlparse(f"https://{url}")
            print(f'{url.netloc.replace(".", "_")}.png')
            driver = chrome.initialize_driver()
            chrome.get(driver, f"{url.scheme}://{url.netloc}")
            chrome.take_screenshot(driver, f'{url.netloc.replace(".", "_")}.png')
            logging.info(
                f"{url}[{urlcategory}] is correctly allowed"
            ) if chrome.fetch_page_title(driver) != BLOCK_TITLE else logging.warn(
                f"{url}[{urlcategory}] is unexpectedly blocked"
            )
        except:
            print("???")

        chrome.destroy_driver(driver)
