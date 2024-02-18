# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import argparse


def generate_cli_parser():
    parser = argparse.ArgumentParser(description="A CI Generator")
    parser.add_argument("--platform-dir", help="Platform Directory", required=True)
    parser.add_argument("--profile-dir", help="Profile Directory", required=True)
    parser.add_argument("--output", help="Output File", required=True)
    return parser


def main():
    parser = generate_cli_parser()
    args = parser.parse_args()
    print(args)
