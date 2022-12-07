#!/bin/python3

import argparse

from utils.read_json import read_json


def base_cli(root_dir):
    cli_data = read_json(root_dir, ".cli.json")
    parser = argparse.ArgumentParser(
        prog=cli_data["name"], description=cli_data["description"], epilog=cli_data["epilog"])
    for arg in cli_data["params"]:
        default = arg.get("default", None)
        metavar = arg.get("metavar", "")
        parser.add_argument(arg["arg_short"], arg["arg_extended"],
                            help=arg["arg_help"], default=default, metavar=metavar)

    args = parser.parse_args()

    return args
