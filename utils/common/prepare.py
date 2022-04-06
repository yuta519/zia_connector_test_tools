import logging
import os

LOG_DIR = "logs"
SCREENSHOT_DIR = "logs/screenshot"

# TODO@yuta519 Add log time
def _make_directory(DIR: str) -> None:
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        logging.info(f"Made {DIR} directory")

    logging.basicConfig(filename="logs/running.log", level=logging.DEBUG)

    logging.info(f"{DIR} exits.") if os.path.isdir(DIR) else logging.warn(
        f"{DIR} does not exits."
    )


# TODO@yuta519 Add function to run by external files
def make():
    pass


_make_directory(LOG_DIR)
_make_directory(SCREENSHOT_DIR)
