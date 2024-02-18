from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from hollihop_api_client.base import BaseCategory
from hollihop_api_client.tools import dict_to_camel, dict_to_snake

if TYPE_CHECKING:
    from hollihop_api_client.api import AbstractAPI


@dataclass
class Level:
    name: None | str
    disciplines: None | list[str]


@dataclass
class Levels:
    levels: list[Level] = field(default_factory=list)


class LevelsCategory(BaseCategory):

    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    def get_levels(
            self
    ) -> list[Level]:
        data = dict_to_camel(self.handle_parameters(locals()))

        response = self.api.request(
            method='GetLevels',
            http_method='GET',
            data=data
        )

        response = dict_to_snake(response)
        return [Level(**_) for _ in Levels(**response).levels]


__all__ = ['LevelsCategory']
