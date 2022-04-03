from infra.chrome import chrome
from utils.zscaler.urlcategory import UrlCategory


# def get_access_with_chrome(file: str) -> None:
def get_access_with_chrome() -> None:
    # make test list
    # for test
    # done ideal result -> OK
    # if something went wrong -> error and logs
    # chrome.get(url) url.value for url in UrlCategory.ENTERTAINMENT
    for url in UrlCategory.ENTERTAINMENT.value:
        chrome.get("https://" + url)
