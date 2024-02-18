import json

import re

from ciocore import conductor_submit


def main(*args):
    (payload,) = args
    submission_data = json.loads(payload)

    # return "\n" + json.dumps(submission_data, indent=4)

    try:
        remote_job = conductor_submit.Submit(submission_data)
        response, response_code = remote_job.main()
        return json.dumps({"code": response_code, "response": response}, indent=4)
    except BaseException as ex:
        return json.dumps({"code": "undefined", "response": ex.message}, indent=4)


def test_cmd(*args):
    (payload,) = args
    submission_data = json.loads(payload)
    tasks = submission_data["tasks_data"]
    sample = int(len(tasks) / 2)
    return tasks[sample]["command"]
