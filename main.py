import argparse

from usecase.get_access import get_access_with_chrome


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("file", help="Please set a file for testing scenario", type=str)
    # args = parser.parse_args()

    get_access_with_chrome()


if __name__ == "__main__":
    main()
