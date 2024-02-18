"""cmdo"""

import argparse


def main():
    """cmdo"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-echo", help="echo the string you use here", type=str, required=True
    )
    print(
        "This program is being run by itself, with the following arguments: ",
        parser.parse_args(),
    )


if __name__ == "__main__":
    main()
