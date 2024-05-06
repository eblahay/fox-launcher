#! /usr/bin/env python3

from argparse import ArgumentParser

def main():
    # parse arguments
    parser = ArgumentParser()

    parser.add_argument(
        "--version",
        version="Project Lepus 0.x.y (Pre-Alpha)",
        action="version"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()