from datetime import datetime

def test_get_students(hh_client, test_data):
    response = hh_client.clients.get_students(term='9226036452', by_agents=False).students
    client_id = response[0].client_id
    response = hh_client.ed_unit_students.get_students(student_client_id=client_id, query_days=True)
    response = list(filter(lambda group: group.end_date != None and group.end_date >= datetime.now() and group.ed_unit_discipline != 'Отработка', response))[-1]
    ed_unit_id = response.ed_unit_id
    response = hh_client.ed_units.set_student_passes(
        data=[
                hh_client.ed_units.create_student_pass_data(
                date='2024-01-13', 
                ed_unit_id=ed_unit_id, 
                student_client_id=client_id, 
                pass_=True, overwriteAcceptedManually=True, 
                acceptedDescription='Отработка в 1.4 ОТР 27.01',
                description='test desc 1'
            ),
                hh_client.ed_units.create_student_pass_data(
                date='2024-01-20', 
                ed_unit_id=ed_unit_id, 
                student_client_id=client_id, 
                pass_=True, overwriteAcceptedManually=True, 
                acceptedDescription='Отработка в 1.4 ОТР 27.01',
                description='test desc 2'
            )
        ]
        )
    print(response)