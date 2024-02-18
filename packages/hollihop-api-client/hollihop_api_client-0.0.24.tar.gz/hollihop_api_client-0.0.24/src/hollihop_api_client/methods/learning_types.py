from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from hollihop_api_client.base import BaseCategory
from hollihop_api_client.tools import dict_to_camel, dict_to_snake

if TYPE_CHECKING:
    from hollihop_api_client.api import AbstractAPI


@dataclass
class LearningType:
    name: None | str


@dataclass
class LearningTypes:
    learning_types: list[LearningType] = field(default_factory=list)


class LearningTypesCategory(BaseCategory):

    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    def get_learning_types(
            self
    ) -> list[LearningType]:
        data = dict_to_camel(self.handle_parameters(locals()))

        response = self.api.request(
            method='GetLearningTypes',
            http_method='GET',
            data=data
        )

        response = dict_to_snake(response)
        return [LearningType(_) for _ in LearningTypes(**response).learning_types]


__all__ = ['LearningTypesCategory']
