# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------
import exacb
import argparse
import sys


def generate_cmdline_parser_env_gitlab(subparser):
    subparser.add_argument("--output", type=str, required=True, help="Output File")


def generate_cmdline_parser_env(subparser):
    subparsers = subparser.add_subparsers(dest="subcommand", required=True)
    generate_parser = subparsers.add_parser("gitlab", help="Generate Report")
    generate_cmdline_parser_env_gitlab(generate_parser)


def generate_cmdline_parser_report_generate(subparser):
    subparser.add_argument("--pipeline", type=str, required=True, help="Pipeline ID")


def generate_cmdline_parser_report(subparser):
    subparsers = subparser.add_subparsers(dest="subcommand", required=True)
    generate_parser = subparsers.add_parser("generate", help="Generate Report")
    generate_cmdline_parser_report_generate(generate_parser)


def generate_cmdline_parser():
    parser = argparse.ArgumentParser("exacb")
    subparsers = parser.add_subparsers(dest="command", required=True)
    report_parser = subparsers.add_parser("report", help="exacb reporting tools")
    env_parser = subparsers.add_parser("env", help="exacb environment tools")

    generate_cmdline_parser_report(report_parser)
    generate_cmdline_parser_env(env_parser)

    return parser

def main():
    parser = generate_cmdline_parser()
    raw_args = sys.argv[1:]
    args = parser.parse_args(raw_args)

    if args.command == "env":
        if args.subcommand == "gitlab":
            exacb.env.gitlab(args.output)
