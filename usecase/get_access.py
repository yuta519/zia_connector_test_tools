from lib.zscaler import parse_test_config
from lib.zscaler import test_urlcategory


def get_access_with_chrome() -> None:
    # Make list
    allow_urlcategories: list[str] = parse_test_config.fetch_allow_urlcategories()

    # for test
    for urlcategory in allow_urlcategories:
        test_urlcategory.access_allow_url(urlcategory)

    # done ideal result -> OK
    # if something went wrong -> error and logs
    # chrome.get(url) url.value for url in UrlCategory.ENTERTAINMENT

    # for url in UrlCategory.ENTERTAINMENT.value:
    #     chrome.get("https://" + url)


# TODO@yuta519 future support
def get_access_with_firefox() -> None:
    pass


def get_access_with_edge() -> None:
    pass


def get_access_with_safari() -> None:
    pass
