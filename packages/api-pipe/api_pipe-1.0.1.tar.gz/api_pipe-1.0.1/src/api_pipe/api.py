'''
    API
'''
import httpx
import itertools
from typing import Any, Optional
from pathlib import Path
import inspect
import json

from api_pipe import logger
from api_pipe.url import Url

class Api:
    '''
        API
    '''
    DEFAULT_JSON_INDENT: int = 2

    def __init__(self,
            url: str,
            headers: Optional[dict[str, str]] = {},
            logs: bool = False
        ) -> None:
        '''
            Init
        '''
        self.data = None
        self.url = Url(url)
        self.headers = headers
        self.log_dir = logs["pipe_steps"]["log_dir"] if "pipe_steps" in logs and "log_dir" in logs["pipe_steps"] else Path("./api_pipe_logs")
        self.log_convert_to_json = True if "pipe_steps" in logs and "convert_to_json" in logs["pipe_steps"] else False
        self.log_convert_to_json_indent = logs["pipe_steps"]["convert_to_json"]["indent"] if "pipe_steps" in logs and "convert_to_json" in logs["pipe_steps"] and "indent" in logs["pipe_steps"]["convert_to_json"] else Api.DEFAULT_JSON_INDENT
        self.type = "url"
        self.curr_step = itertools.count(1)

        self.log = logger.stdout(
            name=__class__.__name__
        )

        self.log.debug(
            f"Creating log dir: {self.log_dir}"
        )

        self.log_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.log.debug(
            f"Emptying log dir: {self.log_dir}"
        )

        for file in self.log_dir.glob('*'):
            file.unlink()

    def fetch(self, **kwargs: Any) -> "Api":
        '''
            Fetch
        '''
        # log function name
        self.log.info(
            "-------------------------------------\n"
            f"STEP: {inspect.currentframe().f_code.co_name}\n"
            "-------------------------------------"
        )

        self.log.info(
            f"Fetching from {self.url}"
        )

        self.data = httpx.get(
            str(self.url), headers=self.headers, **kwargs
        ).text

        self.type = "text"

        self.__log(
            f"GET {self.url}\n{json.dumps(self.headers)}",
            self.data,
            kwargs["log"] if "log" in kwargs else self.log
        )

        return self

    def python_object(self, **kwargs: Any) -> "Api":
        '''
            Python Object
        '''
        self.log.info(
            "-------------------------------------\n"
            f"STEP: {inspect.currentframe().f_code.co_name}\n"
            "-------------------------------------"
        )

        self.log.info(
            f"Converting from {self.type} to python object"
        )

        self.data = json.loads(self.data)

        self.type = "python object"

        self.__log(
            f"to python object",
            self.data,
            kwargs["log"] if "log" in kwargs else self.log
        )

        return self

    def json(self, **kwargs: Any) -> "Api":
        '''
            Json
        '''
        self.log.info(
            "-------------------------------------\n"
            f"STEP: {inspect.currentframe().f_code.co_name}\n"
            "-------------------------------------"
        )

        self.log.info(
            f"Converting from {self.type} to json"
        )

        self.data = json.dumps(
            self.data,
            indent=kwargs["indent"] if "indent" in kwargs else Api.DEFAULT_JSON_INDENT
        )

        self.type = "json"

        self.__log(
            f"to JSON",
            self.data,
            kwargs["log"] if "log" in kwargs else self.log
        )

        return self

    def select(self, keys: list[str] = [], **kwargs: Any) -> "Api":
        '''
            selects keys from python object
        '''
        self.log.info(
            "-------------------------------------\n"
            f"STEP: {inspect.currentframe().f_code.co_name}\n"
            "-------------------------------------"
        )

        self.log.info(
            f"Selecting keys from {self.type}.\nKeys: {keys}"
        )

        if isinstance(self.data, dict):
            self.data = {
                key: self.data[key]
                for key in keys if key in self.data
            }
        elif isinstance(self.data, list):
            self.data = [
                {k: v for k, v in d.items() if k in keys} for d in self.data
            ]
        else:
            raise Exception(f"Cannot select keys from {self.type}")

        self.type = self.type   #just for consistency

        self.__log(
            f"select keys: {keys}",
            self.data,
            kwargs["log"] if "log" in kwargs else self.log
        )

        return self

    def filter(self, function: callable, **kwargs: Any) -> "Api":
        '''
            filters python object
        '''
        self.log.info(
            "-------------------------------------\n"
            f"STEP: {inspect.currentframe().f_code.co_name}\n"
            "-------------------------------------"
        )

        function_code = inspect.getsource(function).strip()

        self.log.info(
            f"Filtering {self.type}. \nFilter Function:   \n{function_code}"
        )

        if isinstance(self.data, dict):
            self.data = {
                key: self.data[key]
                for key in self.data if function(key)
            }
        elif isinstance(self.data, list):
            self.data = [
                d for d in self.data if function(d)
            ]
        else:
            raise Exception(f"Cannot filter {self.type}")

        self.type = self.type

        self.__log(
            f"filter function:\n   {function_code}",
            self.data,
            kwargs["log"] if "log" in kwargs else self.log
        )

        return self

    def __log(
            self,
            header: str,
            data: Any,
            log: bool,
            step_name: Optional[str] = None
        ) -> None:
        '''
            Log
        '''
        if not step_name:
            step_name = inspect.stack()[1].function # parent function name

        if log:
            log_path = self.log_dir / f"{next(self.curr_step)}_{step_name}.log"

            self.log.info(
                f"Logging to {log_path}"
            )
            with open(log_path, "a") as file:
                if header:
                    file.write(
                        f"{header}\n"
                    )
                    file.write(
                        f"-------------------------------------\n"
                        f"              {self.type}            \n"
                        f"-------------------------------------\n"
                    )
                if self.log_convert_to_json \
                    and (isinstance(data, dict) or isinstance(data, list)):
                    file.write(
                        json.dumps(
                            data,
                            indent=self.log_convert_to_json_indent
                        )
                    )
                else:
                    file.write(str(data))
