from datetime import datetime
from dataclasses import dataclass, asdict


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


def test_get_students(hh_client, test_data):
    response = hh_client.clients.get_students(term='9226036452', by_agents=False).students
    client_id = response[-1].client_id
    response = hh_client.ed_units.add_ed_unit_student(
        ed_unit_id=711,
        student_client_id=client_id,
        status='WorkingOff',
        begin='2023-09-23',
        end='2024-01-27'
    )
    print(response)
    response = hh_client.ed_units.set_student_passes(
        data=[
            asdict(SetStudentPasses(date='2024-01-27', ed_unit_id=711, student_client_id=client_id, pass_=True, overwriteAcceptedManually=True, acceptedDescription='Отработка 1.1 СВС 13.01')),
            asdict(SetStudentPasses(date='2024-01-13', ed_unit_id=711, student_client_id=client_id, pass_=True, overwriteAcceptedManually=True, acceptedDescription='Отработка 1.1 СВС 20.01'))
            ]
        )
    print(response)
