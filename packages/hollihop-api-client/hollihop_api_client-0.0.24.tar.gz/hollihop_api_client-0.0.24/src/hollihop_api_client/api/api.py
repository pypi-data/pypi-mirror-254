from typing import TYPE_CHECKING, NoReturn

from requests import Response, Session
from requests.auth import HTTPBasicAuth

from .abc import AbstractAPI

import json
from urllib.parse import urlencode, quote_plus



class HolliHopAPIError(Exception):
    _response_not_ok = '''Запрос к {url} не выполнен.
    Статус код {status_code}.
    {error_message}'''
    _other_errors = '''{error_message}'''

    def __init__(
            self,
            error_message: str,
            status_code: None | int = None,
            url: None | str = None
    ):
        self._status_code = status_code
        self._error_message = error_message
        self._url = url

    def __str__(self) -> str:
        if self._status_code is None:
            return self._other_errors.format(
                error_message=self._error_message
            )
        else:
            return self._response_not_ok.format(
                url=self._url,
                status_code=self._status_code,
                error_message=self._error_message
            )


class HolliHopAPI(AbstractAPI):
    __api_version__ = 'Api/V2/'

    def __init__(
            self,
            domain: str | None = None,
            api_key: str | None = None
    ):
        if api_key is None:
            raise HolliHopAPIError(
                error_message='Не указан ключ доступа к API'
            )
        if domain is None:
            raise HolliHopAPIError(
                error_message='Не указан домен для доступа к API'
            )
        self._domain = domain
        self._api_key = api_key

        super().__init__(self)

    def request(
            self,
            method: str,
            http_method: str = 'GET',
            headers: dict | None = None,
            data: dict | None = None
    ) -> dict:
        
        url = self._domain + self.__api_version__ + method

        data.update({'authkey': self._api_key})

        with Session() as session:
            response = session.request(
                method=http_method,
                url=url,
                data=data,
                headers=headers
            )

        response = self._validate_response(response)

        return response
    
    def json_request(
            self, 
            method, 
            http_method: str = 'GET', 
            data: dict | list[dict] | None = None,
            headers: dict | None = None,
            ) -> dict | None:
        
        url = self._domain + self.__api_version__ + method

        with Session() as session:
            response = session.request(
                method=http_method,
                url=url + '/?authkey=' + quote_plus(f'{self._api_key}'),
                json=data,
                headers=headers
            )

        response = self._validate_response(response)

        return response

    def _validate_response(
            self,
            response: Response,
    ) -> dict | NoReturn:
        if response.status_code == 200:
            return response.json()
        else:
            from pprint import pprint
            pprint(response.request.__dict__)
            pprint(response.__dict__)
            raise HolliHopAPIError(
                response.url,
                response.status_code,
                'Ошибка выполнения запроса'
            )


__all__ = ['HolliHopAPI', 'HolliHopAPIError']
