# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import csv
import json


def csv_to_json(csv_file) -> dict:
    """
    Convert CSV file to JSON
    """

    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        dictionary = {}
        index_header_map = [None] * len(headers)
        for index, header in enumerate(headers):
            dictionary[header] = []
            index_header_map[index] = header

        for line in reader:
            for index, value in enumerate(line):
                dictionary[index_header_map[index]].append(value)

        return dictionary


def parse_env(env, env_version):
    """
    Parse the environment file
    """


def parse_result(result, result_version):
    """
    Parse the result file
    """
    return csv_to_json(result)


def generate(env_file, env_version, result_file, result_version, record_file, record_version):
    if env_file is None:
        env = {
            "pipeline": "unknown",
            "job": "unknown",
        }
    else:
        env = parse_env(env, env_version)

    result = parse_result(result_file, result_version)

    record = {}
    record["id"] = str(env["pipeline"]) + str("-") + str(env["job"])

    record["env"] = env
    record["result"] = result

    with open(record_file, "w") as f:
        json.dump(record, f, indent=4)
