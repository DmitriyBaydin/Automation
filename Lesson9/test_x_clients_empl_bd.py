from EmployeeApi import Employee, Company
from EmployeeTable import EmployeeTable


api = Employee("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


def test_get_list_of_employers():
    db.create_company("LASTONE", "Descr")
    max_id = db.get_max_id_company()
    db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    db_empl_list = db.get_employee_list(max_id)
    api_empl_list = api.get_list(max_id)
    
    db_empl_id = db.get_max_id_employee(max_id)
    db.delete_employee(db_empl_id)
    db.delete(max_id)

    assert len(db_empl_list) == len(api_empl_list)


def test_create_new_employer():

    db.create_company("LASTONE", "Descr")
    max_id = db.get_max_id_company()
    api_empl_before = len(api.get_list(max_id))

    db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    db_empl_id = db.get_max_id_employee(max_id)
    db_empl_list = db.get_employee_list(max_id)
    assert db_empl_list is not None
    api_empl_after = len(api.get_list(max_id))
    
    assert api_empl_after - api_empl_before == 1

    body = api.get_list(max_id)
    len_after = len(body)

    db.delete_employee(db_empl_id)
    api_empl_del = len(api.get_list(max_id))
    assert api_empl_del == api_empl_before

    db.delete(max_id)

    for employee in body:
        if employee["id"] == db_empl_id:
            assert employee["firstName"] == "Name"
            assert employee["lastName"] == "LastName"
            assert employee["phone"] == '+71234567890'
            assert employee["isActive"] == True
    

def test_update_employer():
    db.create_company("LASTONE", "Descr")
    max_id = db.get_max_id_company()
    db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    db_empl_id = db.get_max_id_employee(max_id)
    db.update_employee("NewName", db_empl_id)
    body = api.get_list(max_id)

    for updated in body:
        if updated["id"] == db_empl_id:
            assert updated["firstName"] == "NewName"
            assert updated["lastName"] == "LastName"
            assert updated["phone"] == '+71234567890'
            assert updated["isActive"] == True

    db.delete_employee(db_empl_id)
    db.delete(max_id)


def test_delete_employer():
    db.create_company("LASTONE", "Descr")
    max_id = db.get_max_id_company()
    db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    db_empl_id = db.get_max_id_employee(max_id)
    db.delete_employee(db_empl_id)
    body = api.get_list(max_id)
    assert body == []
    db.delete(max_id)
