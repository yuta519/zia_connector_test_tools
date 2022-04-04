import json
from typing import Optional


def fetch_allow_urlcategories(
    file: Optional[str] = "test_config/zscaler/zia_urlcategory.json",
) -> list[str]:
    with open(file, mode="rt", encoding="utf-8") as file:
        data = json.load(file)
        return data["allow"]
