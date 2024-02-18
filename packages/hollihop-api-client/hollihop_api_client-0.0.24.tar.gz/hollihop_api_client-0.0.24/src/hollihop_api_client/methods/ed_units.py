from dataclasses import dataclass, field, asdict
from datetime import datetime, time
from typing import TYPE_CHECKING

from hollihop_api_client.base import BaseCategory
from hollihop_api_client.tools import dict_to_camel, dict_to_snake

if TYPE_CHECKING:
    from hollihop_api_client.api import AbstractAPI


@dataclass
class ScheduleItem:
    begin_date: None | datetime = None
    begin_time: None | str = None
    classroom_id: None | int = None
    classroom_name: None | str = None
    classroom_link: None | str = None
    end_date: None | datetime = None
    end_time: None | str = None
    id: None | int = None
    teacher: None | str = None
    teacher_genders: None | list[str] = None
    teacher_id: None | int = None
    teacher_ids: None | list[int] = None
    teacher_photo_urls: None | list[str] = None
    teachers: None | list[str] = None
    weekdays: None | int = None

    def __post_init__(self):
        if not self.begin_time is None:
            self.begin_date = datetime.fromisoformat(self.begin_date)
        if not self.end_date is None:
            self.end_date = datetime.fromisoformat(self.end_date)


@dataclass
class Day:
    date: None | datetime = None
    minutes: None | float = None
    pass_: None | bool = field(init=False)
    Pass: None | bool = None
    description: None | str = None
    student_payable_minutes: None | float = None
    teacher_payable_minutes: None | float = None
    accepted: bool | None = None
    accepted_description: str | None = None

    def __post_init__(self):
        if not self.date is None:
            self.date = datetime.fromisoformat(self.date)
        self.pass_ = self.Pass
        del self.Pass
        # delattr(self, 'Pass')


@dataclass
class FiscalInfo:
    price_id: None | int = None
    price_name: None | str = None
    price_value: None | str = None
    units: None | str = None
    units28: None | str = None
    units7: None | str = None
    value: None | str = None
    value28: None | str = None
    value7: None | str = None

    def __post_init__(self):
        if not self.price_name is None:
            self.price_name = self.price_name.replace('\xa0', ' ')
        if not self.price_value is None:
            self.price_value = self.price_value.replace('\xa0', ' ')
        if not self.value is None:
            self.value = self.value.replace('\xa0', ' ')
        if not self.value28 is None:
            self.value28 = self.value28.replace('\xa0', ' ')
        if not self.value7 is None:
            self.value7 = self.value7.replace('\xa0', ' ')


@dataclass
class PriceValue:
    students: None | int = None
    value: None | str = None
    value_currency: None | str = None
    value_quantity: None | float = None

    def __post_init__(self):
        if not self.value is None:
            self.value = self.value.replace('\xa0', ' ')


@dataclass
class TeacherPrice:
    price_id: None | int = None
    price_name: None | str = None
    price_units: None | str = None
    price_units_quantity: None | int = None
    price_units_type: None | str = None
    price_values: None | list[PriceValue] = None
    teacher_id: None | int = None

    def __post_init__(self):
        if not self.price_values is None:
            self.price_values = [PriceValue(**_) for _ in self.price_values]


@dataclass
class EdUnit:
    id: int | None = None
    type: str | None = None
    name: str | None = None
    corporative: bool = False
    office_or_company_id: int | None = None
    office_or_company_name: str | None = None
    office_or_company_address: str | None = None
    office_time_zone: time | None = None
    discipline: str | None = None
    level: str | None = None
    maturity: str | None = None
    learning_type: str | None = None
    extra_fields: list | None = None
    students_count: int | None = None
    vacancies: int | None = None
    study_units_in_range: str | None = None
    description: str | None = None
    company_contract_number: str | None = None
    company_contract_date: datetime | None = None
    schedule_items: list | None = None
    days: list[Day] | None = None
    fiscal_info: FiscalInfo | list = None
    teacher_prices: None | list[TeacherPrice] = None
    price_values: None | list = None
    assignee: None | dict = None

    def __post_init__(self):
        if not self.schedule_items is None:
            self.schedule_items = [ScheduleItem(
                **_) for _ in self.schedule_items]
        if not self.days is None:
            self.days = [Day(**_) for _ in self.days]
        if not self.fiscal_info is None:
            self.fiscal_info = FiscalInfo(**self.fiscal_info)
        if not self.teacher_prices is None:
            self.teacher_prices = [TeacherPrice(
                **_) for _ in self.teacher_prices]

    def __eq__(self, other: object):
        if not isinstance(other, EdUnit):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


@dataclass(frozen=True)
class Statuses:
    Reserve = 'Reserve'
    Forming = 'Forming'
    Working = 'Working'
    Stopped = 'Stopped'
    Finished = 'Finished'


@dataclass
class EdUnits:
    ed_units: list[EdUnit] = field(default_factory=list)
    now: datetime = field(default_factory=datetime.fromtimestamp)


def array_to_one_str(data: dict):
    for key in data.keys():
        if type(data[key]) == list:
            data[key] = ",".join(data[key])
    return data


@dataclass
class SetStudentPasses: 
    date: str | None = None
    ed_unit_id: int | None = None
    student_client_id: int | None = None
    pass_: bool | None = None
    payable: bool | None = None
    description: str | None = None
    acceptedDescription: str | None = None
    overwriteAcceptedManually: bool | None = None


@dataclass
class AddEdUnitStudent:
    ed_unit_id: int | None = None
    student_client_id: int | None = None
    status: str | None = None
    begin: str | None = None
    end: str | None = None


class EdUnitsCategory(BaseCategory):

    def __init__(self, api: 'AbstractAPI'):
        self.api = api

    def get_ed_units(
            self,
            id: None | int = None,
            types: None | str = None,

            date_from: None | str = None,
            date_to: None | str = None,

            statuses: None | str = None,
            office_or_company_id: None | str = None,
            location_id: None | list[int] = None,
            disciplines: None | list[str] = None,
            levels: None | list[str] = None,
            maturities: None | str = None,
            corporative: None | bool = None,
            learning_types: None | list[str] = None,
            teacher_id: None | int = None,
            query_days: None | bool = None,
            query_fiscal_info: None | bool = None,
            query_teacher_prices: None | bool = None,
    ) -> list[EdUnit]:
        data = dict_to_camel(self.handle_parameters(locals()))
        data = array_to_one_str(data)
        response = self.api.request(
            method='GetEdUnits',
            http_method='GET',
            data=data
        )

        response = dict_to_snake(response)

        return [EdUnit(**_) for _ in EdUnits(**response).ed_units]
    
    def create_student_pass_data(
            self,
            date: str | None = None,
            ed_unit_id: int | None = None,
            student_client_id: int | None = None,
            pass_: bool | None = None,
            payable: bool | None = None,
            description: str | None = None,
            acceptedDescription: str | None = None,
            overwriteAcceptedManually: bool | None = True
            ) -> dict:
        return self.handle_parameters(locals())
    
    def set_student_passes(
            self,
            data: list[SetStudentPasses]
            ):
        params = self.handle_parameters(locals())
        
        request_data = []
        for _ in params['data']:
            if 'pass_' in _:
                pass_ = _.pop('pass_')
                _ = {**_, 'pass': pass_}
            request_data.append(dict_to_camel(_))

        response = self.api.json_request(
            method='SetStudentPasses',
            http_method='POST',
            data=request_data,
            headers={'Content-Type':'application/json'}
        )

        response = dict_to_snake(response)

        return response
    

    def add_ed_unit_student(
            self,
            ed_unit_id: int | None = None,
            student_client_id: int | None = None,
            status: str | None = None,
            begin: str | None = None,
            end: str | None = None,
            ):
        request_data = self.handle_parameters(locals())
        request_data = dict_to_camel(request_data)

        response = self.api.json_request(
            method='AddEdUnitStudent',
            http_method='POST',
            data=request_data,
            headers={'Content-Type':'application/json'}
        )

        response = dict_to_snake(response)

        return response
        


    def get_all_ed_units_name(self, **kwargs) -> list[str]:
        ed_units = self.get_ed_units(**kwargs)
        return [ed_unit.name for ed_unit in ed_units]

    def get_all_ed_units_id(self, **kwargs) -> list[int]:
        ed_units = self.get_ed_units(**kwargs)
        return [ed_unit.id for ed_unit in ed_units]


__all__ = ['EdUnitsCategory']
