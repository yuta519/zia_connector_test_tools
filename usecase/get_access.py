from lib.zscaler import parse_test_config
from lib.zscaler import test_urlcategory


# def get_access_with_chrome(file: str) -> None:
def get_access_with_chrome() -> None:
    # make test list
    allow_urlcategories: list[str] = parse_test_config.fetch_allow_urlcategories()

    # for test
    for urlcategory in allow_urlcategories:
        test_urlcategory.access_allow_url(urlcategory)

    # done ideal result -> OK
    # if something went wrong -> error and logs
    # chrome.get(url) url.value for url in UrlCategory.ENTERTAINMENT

    # for url in UrlCategory.ENTERTAINMENT.value:
    #     chrome.get("https://" + url)
