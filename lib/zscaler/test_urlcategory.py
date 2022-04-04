from infra.chrome import chrome
from utils.zscaler.constants import URLCATEGORY_URLS


def access_allow_url(urlcategory: str):
    for url in URLCATEGORY_URLS[urlcategory]:
        chrome.get("https://" + url)
