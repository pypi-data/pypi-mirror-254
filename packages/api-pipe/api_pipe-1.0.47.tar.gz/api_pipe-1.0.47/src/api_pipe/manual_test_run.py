'''
    Test API
'''
import os
import logging
import httpx
import asyncio

from api_pipe.api import Api
from api_pipe import config
from pathlib import Path

DUMMY_TEST_GROUP_ID = 79866152


def main():
    asyncio.run(async_main())

def create_and_clean_dir(dir_path: Path):
    '''
        Create and clean directory recursively
    '''
    #create
    if not dir_path.exists():
        dir_path.mkdir()

    #clean
    for file in dir_path.iterdir():
        if file.is_file():
            file.unlink()
        elif file.is_dir():
            for sub_file in file.iterdir():
                sub_file.unlink()
            file.rmdir()


async def async_main():
    '''
        Main
    '''
    log_dir_app = Path("../logs_app")
    log_dir_api_pipe_steps = Path("../logs_api_pipe")

    create_and_clean_dir(log_dir_app)
    create_and_clean_dir(log_dir_api_pipe_steps)

    async with httpx.AsyncClient() as client:
        api = Api(
            url="https://gitlab.com/api/v4",
            httpx_async_client=client,
            headers={
                "PRIVATE-TOKEN": os.environ["GL_TOKEN"]
            },
            timeout=(5.0, 5.0),
            retries={
                "initial_delay": 0.5,
                "backoff_factor": 3,
                "max_retries": 7,
            },
            logs={
                "unique_name": "manual_test_run",
                "log_dir": log_dir_app,
                "level": logging.DEBUG,
                "words_to_highlight": config.logger_words_to_highlight,
                "pipe_steps" : {
                    "log_dir": log_dir_api_pipe_steps,
                    "convert_to_json": {
                        "indent": 2
                    }
                }
            }
        )

        api.url = api.url / "groups" / DUMMY_TEST_GROUP_ID / "members"

        await api.fetch_async()

        api.python_object()    \
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
