"""Module providing REST client class"""

from pathlib import Path

import logging
import os
import time
import requests

from .rest_object import RESTObject as RO


class RESTClient():

    logging.basicConfig(
        format='%(asctime)s | %(levelname)s | %(message)s', level=logging.DEBUG)
    debug = False
    __app_name = 'rest_client_micro'
    root_dir: str
    output_file: str
    cache_dir: str = os.path.join(
        str(Path.home()), ".config/", __app_name)
    cache_file: str = os.path.join(
        str(Path.home()), ".cache/", __app_name, "app")
    log_dir: str = os.path.join(
        str(Path.home()), ".cache/", __app_name, "logs")
    log_file: str = "log.db"

    cache_s: int = 600
    sleep_ms: int = 1000

    def _debug(self, message):
        if self.debug:
            logging.debug(str(message))

    def __init__(self) -> None:
        pass

    def _get_short_string(self, content):
        if len(str(content)) < 110:
            return content
        else:
            return f"{str(content)[:100]}...{str(content)[-10:]}"

    def _execute_call(self, rest_object: RO) -> dict:
        sleep_time = self.sleep_ms / 1000
        self._debug(f'Starting Sleep for {sleep_time}s {time.time()}')
        time.sleep(sleep_time)
        self._debug(f'Finished for {sleep_time}s {time.time()}')
        try:
            operation = rest_object.operation
            endpoint = rest_object.endpoint
            params = rest_object.params
            payload = rest_object.payload
            headers = rest_object.headers
            if operation == 'get':
                self._debug(f"Running REST Call {operation} {endpoint} {
                            params} {headers} {self._get_short_string(payload)}")
                response = requests.get(
                    url=endpoint,
                    params=params,
                    headers=headers,
                    data=payload,
                    timeout=10
                )
                return {
                    'error': False,
                    'response': response.text,
                }
            return {
                'error': True,
                'description': 'Operation not valid',
            }
        except Exception as e:
            return {
                'error': True,
                'description': str(e),
            }

    def _read_cache(self, config: RO) -> str:
        pass

    def _write_cache(self, config: RO, text: str) -> None:
        pass

    def _set_cache(self, config: RO) -> None:
        pass

    def execute(self, config: RO) -> dict | bool:
        if not config:
            return {
                'error': True,
                'description': 'No config provided'
            }

        return self._execute_call(config)
