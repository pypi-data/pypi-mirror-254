from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from hollihop_api_client.base.category import BaseCategory
from hollihop_api_client.tools import dict_to_camel, dict_to_snake


if TYPE_CHECKING:
    from hollihop_api_client.api import AbstractAPI


class Phone(str):
    def __repr__(self):
        return self.replace("'", "", 2)

    def __str__(self):
        return f"{self[:2]}xxxxxx{self[-4:]}"

@dataclass
class UTM:
     source: str | None = None
     medium: str | None = None
     campaign: str | None = None
     term: str | None = None
     content: str | None = None

@dataclass
class StudyRequest:
    id: int | None = None
    created: datetime | None = None
    utm: list[UTM] | None = None
    reffer: str | None = None
    lead_id: int | None = None
    
@dataclass
class ExtraField:
    name: str | None = None
    value: str | None = None
    
@dataclass
class Assignee:
    id: int | None = None
    full_name: str | None = None

@dataclass
class OfficesAndCompany:
    id: int | None = None
    name: str | None = None
     
    
@dataclass
class Discipline:
    discipline: str | None = None
    level: str | None = None


@dataclass
class Agent:
    first_name: None | str = None
    last_name: None | str = None
    middle_name: None | str = None
    who_is: None | str = None
    mobile: None | str = None
    use_mobile_by_system: None | str = None
    phone: None | Phone = None
    email: None | str = None
    use_email_by_system: None | bool = None
    skype: None | str = None
    job_or_study_place: None | str = None
    position: None | str = None
    is_customer: None | bool = None
    birthday: None | datetime = None


@dataclass
class Student:
    client_id: int | None = None
    id: int | None = None
    created: datetime | None = None
    updated: datetime | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    photo_urls: str | None = None
    gender: str | None = None
    address_date: datetime | None = None
    ad_soure: str | None = None
    visit_date_time: datetime | None = None
    status_id: int | None = None
    status: str | None = None
    birthday: datetime | None = None
    mobile: str | None = None
    use_mobile_by_system: bool | None = None
    email: str | None = None
    use_email_by_system: bool | None = None
    skype: str | None = None
    address: str | None = None
    social_network_page: str | None = None
    job_or_study_place: str | None = None
    position: str | None = None
    agents: list[Agent] | None = None
    maturity: str | None = None
    learning_types: list[str] | None = None
    disciplines: list[Discipline] | None = None
    offices_and_companies: list[OfficesAndCompany] | None = None
    assignees: list[Assignee] | None = None
    extra_fields: list[ExtraField] | None = None
    ad_source: str | None = None
    phone: str | None = None


@dataclass
class Students:
    students: list[Student] | None = None
    now: datetime | None = None

    def __post_init__(self):
         if self.students: 
              self.students = [Student(**_) for _ in self.students]

class Clients(BaseCategory):

    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    def get_students(
            self,
            client_id: int | None = None, 
            id: int | None = None, 
            ed_unit_office_or_company_id: int | None = None,
            term: str | None = None,
            by_agents: bool | None = False 
    ) -> Students:
        data = dict_to_camel(self.handle_parameters(locals()))
        response = self.api.request(
            method='GetStudents',
            http_method='GET',
            data=data
        )

        response = dict_to_snake(response)

        return Students(**response)
        