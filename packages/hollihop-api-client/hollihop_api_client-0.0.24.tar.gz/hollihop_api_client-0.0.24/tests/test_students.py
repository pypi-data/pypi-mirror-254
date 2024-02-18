from pprint import pprint
from datetime import datetime, timedelta

from pydantic import BaseModel


# def test_get_students(hh_client, test_data):
#     response = hh_client.clients.get_students(term='9226036452', by_agents=False).students
#     response1 = hh_client.ed_unit_students.get_students(student_client_id=response[-1].client_id, query_days=True)
#     res = list(filter(lambda group: group.end_date != None and group.end_date >= datetime.now() and group.ed_unit_discipline != 'Отработка', response1))
#     res1 = hh_client.ed_unit_students.get_students(student_client_id=response[-1].client_id, ed_unit_id=res[-1].ed_unit_id, query_days=True, date_from=datetime.strptime('01-09-2023', '%d-%m-%Y'), date_to=res[-1].end_date)[-1]
    
#     days = res1.days
#     # print(datetime.strptime('01-09-2023', '%d-%m-%Y'), res[-1].end_date)
#     days = list(filter(lambda day: day.date <= datetime.now() and day.date == datetime.strptime('2024-01-13', '%Y-%m-%d'), days))
#     pprint(days)
#     # # # eds = hh_client.ed_units.get_ed_units(id=res[-1].ed_unit_id, query_days=True)
#     # # # print(days[-1].date.year)
#     # print(res1.ed_unit_name, res1.ed_unit_office_or_company_name, response[-1].client_id )
#     # pprint(days[-1].date.strftime('%m–%d–%Y'))


def test_get_working_off_days(hh_client):
    response = hh_client.ed_units.get_ed_units(statuses='Working', location_id=1, disciplines='Отработка', query_days=True )
    workoff_days = []
    for _g in response:
        days = _g.days
        days = list(filter(lambda day: day.date >= datetime.now(), days))
        days = [day.date.strftime('%d-%m-%Y') for day in days]
        workoff_days.append({'name': _g.name, 'days': days, 'ed_unit _id': _g.id, 'office_name': _g.office_or_company_name, 'office_id': _g.office_or_company_id})
    # pprint(workoff_days)




key_not_study_description = ['Ещё не начал заниматься', 'Перенос на другой день']

class WorkOffsResponse(BaseModel):
    name: str 
    days: list[str]
    ed_unit_id: int
    office_name: str
    office_id: int

class PassDaysResponse(BaseModel):
    group_name: str
    groups_of_passes: list[list]


def filter_normal_day(day_obj):
    if not day_obj.description is None:  
        for key in key_not_study_description:
            if key in day_obj.description:
                return False
    if day_obj.date <= datetime.now():
        return True
    else: 
        return False


def test_get_passes(hh_client):
    
    response = hh_client.clients.get_students(term='9226036452', by_agents=False).students[-1]
    print(response.client_id)
    response = hh_client.ed_unit_students.get_students(student_client_id=response.client_id, query_days=True)
    working_groups = list(filter(lambda group: (group.end_date != None) and group.end_date >= datetime.now() and group.ed_unit_discipline != 'Отработка', response))
    
    
    passes_objs = []
    for group in working_groups:
        group_with_days = hh_client.ed_unit_students.get_students(
            student_client_id=group.student_client_id, 
            ed_unit_id=group.ed_unit_id, 
            query_days=True, 
            date_from=group.begin_date, 
            date_to=group.end_date
            )[-1]
        days = group_with_days.days

        # filter by days that the student actually missed or was in, like a paid day 
        days = list(filter(filter_normal_day, days))
        # filter by days on which the student was not present in class 
        missed_days = list(filter(lambda day: day.pass_, days))

        couple_of_passes_day = []
        paired_passes_day = []

        for index, day in enumerate(missed_days):
            if (index + 1) % 2:
                couple_of_passes_day.append(day)
            else:
                couple_of_passes_day.append(day)
                paired_passes_day.append(couple_of_passes_day)
                couple_of_passes_day = []
        else:
            if couple_of_passes_day:
                paired_passes_day.append(couple_of_passes_day)
                
        finally_paired_passes_day = []

        for couple_of_passes in paired_passes_day:
            if couple_of_passes[-1].working_off_to_ed_unit_id is None:
                finally_paired_passes_day.append(couple_of_passes)
        
        paired_passes_day_str = []
        for couple_of_passes in finally_paired_passes_day:
            _pair_str = []
            for pass_day in couple_of_passes:
                _pair_str.append(pass_day.date.strftime('%d-%m-%Y'))
            paired_passes_day_str.append(_pair_str)


        passes_objs.append(PassDaysResponse(group_name=group_with_days.ed_unit_name, groups_of_passes=paired_passes_day_str))
    pprint(passes_objs)