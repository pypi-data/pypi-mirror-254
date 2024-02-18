from typing import TYPE_CHECKING

from hollihop_api_client.methods import (DisciplinesCategory, EdUnitsCategory,
                                         LeadsCategory, LearningTypesCategory,
                                         LevelsCategory, LocationsCategory,
                                         OfficesCategory, StudentsCategory, Clients)

if TYPE_CHECKING:
    from hollihop_api_client.api import AbstractAPI


class APICategories:
    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    @property
    def locations(self) -> LocationsCategory:
        return LocationsCategory(self.api)

    @property
    def offices(self) -> OfficesCategory:
        return OfficesCategory(self.api)

    @property
    def ed_units(self) -> EdUnitsCategory:
        return EdUnitsCategory(self.api)

    @property
    def ed_unit_students(self) -> StudentsCategory:
        return StudentsCategory(self.api)
    
    @property
    def clients(self) -> Clients:
        return Clients(self.api)

    @property
    def leads(self) -> LeadsCategory:
        return LeadsCategory(self.api)

    @property
    def disciplines(self) -> DisciplinesCategory:
        return DisciplinesCategory(self.api)

    @property
    def levels(self) -> LevelsCategory:
        return LevelsCategory(self.api)

    @property
    def learning_types(self) -> LearningTypesCategory:
        return LearningTypesCategory(self.api)


__all__ = ['APICategories']
