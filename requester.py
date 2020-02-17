import json
from json import JSONDecodeError
from loguru import logger
import requests
from requests.models import Response
from typing import Union
import urllib.parse


class Requester:
    ResponseCustomType = Union[dict, None]
    headers_json = {'Content-Type': 'application/json'}
    params_pretty = (('pretty', ''),)

    def __init__(self, url: str):
        self.url = url

    @classmethod
    def _response_json(cls, response: Response) -> Union[dict, None]:
        try:
            return response.json()
        except JSONDecodeError:
            print(response.text)
            return

    @classmethod
    def _response_check(cls, response: Response) -> Union[dict, None]:
        if response.status_code in {200, 201}:
            return cls._response_json(response)
        else:
            logger.error(f'Bad response {response.status_code}. Error: {response.text}')
            return

    def _request(self, func):
        def wrapped(*args, **kwargs):
            try:
                r = func(*args, **kwargs)
            except Exception as e:
                logger.error(f'Bad request. Error: {e}')
                return

            return self._response_check(response=r)
        return wrapped

    def _url_make(self, path):
        return urllib.parse.urljoin(self.url, path)

    def get(self, path: str = None, data: dict = None) -> ResponseCustomType:
        url_in = self._url_make(path)

        @self._request
        def request():
            return requests.get(url=url_in, headers=self.headers_json, params=self.params_pretty, data=json.dumps(data))

        return request()

    def put(self, path: str = None, data: dict = None) -> ResponseCustomType:
        url_in = self._url_make(path)

        @self._request
        def request():
            return requests.put(url=url_in, headers=self.headers_json, params=self.params_pretty, data=json.dumps(data))

        return request()

    def post(self, path: str = None, data: dict = None) -> ResponseCustomType:
        url_in = self._url_make(path)

        @self._request
        def request():
            return requests.post(
                url=url_in, headers=self.headers_json, params=self.params_pretty, data=json.dumps(data)
            )

        return request()

    def delete(self, path: str = None) -> ResponseCustomType:
        url_in = self._url_make(path)

        @self._request
        def request():
            return requests.delete(url=url_in, params=self.params_pretty)

        return request()
