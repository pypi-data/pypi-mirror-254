from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from hollihop_api_client.base import BaseCategory
from hollihop_api_client.tools import dict_to_camel, dict_to_snake

if TYPE_CHECKING:
    from hollihop_api_client.api import AbstractAPI


@dataclass
class Discipline:
    name: None | str


@dataclass
class Disciplines:
    disciplines: list[Discipline] = field(default_factory=list)


class DisciplinesCategory(BaseCategory):

    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    def get_disciplines(
            self
    ) -> list[Discipline]:
        data = dict_to_camel(self.handle_parameters(locals()))

        response = self.api.request(
            method='GetDisciplines',
            http_method='GET',
            data=data
        )

        response = dict_to_snake(response)
        return [Discipline(_) for _ in Disciplines(**response).disciplines]


__all__ = ['DisciplinesCategory']
