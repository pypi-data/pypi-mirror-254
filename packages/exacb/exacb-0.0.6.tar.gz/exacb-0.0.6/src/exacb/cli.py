# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------
import exacb
import argparse
import sys


def generate_cmdline_parser_env_gitlab(subparser):
    subparser.add_argument("--output", type=str, required=True, help="Output File")
    subparser.add_argument(
        "--output-version", type=str, default=exacb.metadata.semver.major, help="Output Version"
    )


def generate_cmdline_parser_env(subparser):
    subparsers = subparser.add_subparsers(dest="subcommand", required=True)
    generate_parser = subparsers.add_parser("gitlab", help="Generate Env for Gitlab CI/CD")
    generate_cmdline_parser_env_gitlab(generate_parser)


def generate_cmdline_parser_record_generate(subparser):
    subparser.add_argument("--env", type=str, default=None, help="Path to Env File in JSON format")
    subparser.add_argument(
        "--env-version", type=str, default=exacb.metadata.semver.major, help="Env Version"
    )
    subparser.add_argument(
        "--result", type=str, required=True, help="Path to Result File in CSV format"
    )
    subparser.add_argument(
        "--result-version",
        type=str,
        default=exacb.metadata.semver.major,
        help="Result Version",
    )
    subparser.add_argument("--output", type=str, required=True, help="Output File")
    subparser.add_argument(
        "--output-version", type=str, default=exacb.metadata.semver.major, help="record Version"
    )


def generate_cmdline_parser_record(subparser):
    subparsers = subparser.add_subparsers(dest="subcommand", required=True)
    generate_parser = subparsers.add_parser("generate", help="Generate record")
    generate_cmdline_parser_record_generate(generate_parser)


class exacb_commandline_parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write("error: %s\n" % message)
        self.print_help()
        sys.exit(2)


def generate_cmdline_parser():
    parser = exacb_commandline_parser("exacb")
    subparsers = parser.add_subparsers(dest="command", required=True)
    record_parser = subparsers.add_parser("record", help="exacb record tools")
    env_parser = subparsers.add_parser("env", help="exacb environment tools")

    generate_cmdline_parser_record(record_parser)
    generate_cmdline_parser_env(env_parser)

    return parser


def main():
    parser = generate_cmdline_parser()
    raw_args = sys.argv[1:]
    args = parser.parse_args(raw_args)

    if args.command == "env":
        if args.subcommand == "gitlab":
            exacb.env.gitlab(args.output)
    elif args.command == "record":
        if args.subcommand == "generate":
            exacb.record.generate(
                args.env,
                args.env_version,
                args.result,
                args.result_version,
                args.output,
                args.output_version,
            )
