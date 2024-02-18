'''
    Test API
'''
import os
import logging
import httpx

from api_pipe.api import Api
from pathlib import Path

DUMMY_TEST_GROUP_ID = 79866152

def main():
    '''
        Main
    '''
    with httpx.Client() as client:
        api = Api(
            url="https://gitlab.com/api/v4",
            httpx_client=client,
            headers={
                "PRIVATE-TOKEN": os.environ["GL_TOKEN"]
            },
            timeout=(5.0, 5.0),
            logs={
                "level": logging.INFO,
                "pipe_steps" : {
                    "log_dir": Path("../api_pipe_logs"),
                    "convert_to_json": {
                        "indent": 2
                    }
                }
            }
        )

        api.url = api.url / "groups" / DUMMY_TEST_GROUP_ID / "members"

        api                     \
            .fetch()            \
            .python_object()    \
            .json(indent=2)

        print(api.data)
    # api = Api(
    #     url="https://gitlab.com/api/v4",
    #     headers={
    #         "PRIVATE-TOKEN": os.environ["GL_TOKEN"]
    #     },
    #     logs={
    #         "level": logging.DEBUG,
    #         "pipe_steps" : {
    #             "log_dir": Path("../api_pipe_logs"),
    #             "convert_to_json": {
    #                 "indent": 2
    #             }
    #         }
    #     }
    # )

    # api.url = api.url / "groups" / DUMMY_TEST_GROUP_ID / "variables"

    # api                     \
    #     .fetch()            \
    #     .python_object()    \
    #     .select([
    #         "key",
    #         "value",
    #         "masked",
    #     ])                  \
    #     .filter(
    #         lambda item: item["key"] == "Var2"
    #     )                   \
    #     .json(indent=2)

    # print(api.data)
