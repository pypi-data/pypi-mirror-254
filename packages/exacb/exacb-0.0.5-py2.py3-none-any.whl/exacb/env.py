# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import os
import json


def gitlab(output: str) -> None:
    env_json = {}

    env_json["gitlab"] = {}

    env_json["gitlab"]["pipeline"] = os.environ["CI_PIPELINE_ID"]
    env_json["gitlab"]["job"] = os.environ["CI_JOB_ID"]
    env_json["gitlab"]["job_name"] = os.environ["CI_JOB_NAME"]
    env_json["gitlab"]["commit"] = os.environ["CI_COMMIT_SHA"]
    env_json["gitlab"]["build_dir"] = os.environ["CI_BUILDS_DIR"]
    env_json["gitlab"]["username"] = os.environ["GITLAB_USER_LOGIN"]
    env_json["gitlab"]["tags"] = os.environ["CI_RUNNER_TAGS"]
    env_json["gitlab"]["runner"] = os.environ["CI_RUNNER_ID"]

    with open(output, "w") as f:
        f.write(json.dumps(env_json, indent=2))
