#!/usr/bin/python3.11
import argparse
import dataclasses
import os.path
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class ExtractedIpkHandler:
    def __init__(self, pacakge_file: str, destination: str = None):
        self.package_path = BASE_DIR.joinpath(pacakge_file)
        self.package_name = self.package_path.name
        if self.package_name.endswith('.ipk'):
            self.package_name = self.package_name[:-4]
        if destination is None:
            self.destination = BASE_DIR.joinpath(self.package_name)
        else:
            self.destination = Path(destination)

    def run(self):
        print(f"Your package name is: {self.package_name}")
        self.check_destination()

    def check_destination(self):
        print(f"destination folder is {self.destination}")
        if os.path.exists(self.destination):
            print(f"destination folder exist. remove it...")
            shutil.rmtree(self.destination)
        os.mkdir(self.destination)


def parse_arguments(args):
    parser = argparse.ArgumentParser(
        prog="Extract IPK",
        description="Extract IPK from a file",
        epilog="Help me....")
    parser.add_argument("pacakge_file",
                        help="path of package file")
    parser.add_argument("--dst", dest='destination', help="destination path", required=False)
    return parser.parse_args(args)


def main(args=None):
    arguments = parse_arguments(args)
    h = ExtractedIpkHandler(pacakge_file=arguments.pacakge_file, destination=arguments.destination)
    h.run()


if __name__ == "__main__":
    main()
