from pages.Employee import Company, Employer

company = Company()
employer = Employer()


def test_auth(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)


def test_get_company_id():
    com_id = company.last_active_company_id()
    assert com_id is not None
    assert str(com_id).isdigit()


def test_get_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_empl = {
        "id": 0,
        "firstName": 'Natalya',
        "lastName": 'Baydina',
        "middleName": 'Vladimirovna',
        "companyId": com_id,
        "email": 'ya@mail.ru',
        "url": "string",
        "phone": '+71234567890',
        "birthdate": "1980-05-05T00:00:00.000Z",
        "isActive": 'true'
    }
    new_empl_id = (employer.add_new(token, body_empl))['id']
    assert new_empl_id is not None
    assert str(new_empl_id).isdigit()

    info = employer.get_info(new_empl_id)
    assert info.json()['id'] == new_empl_id
    assert info.status_code == 200


def test_add_employer_without_token():
    token = ""
    com_id = company.last_active_company_id()
    body_empl = {
        "id": 0,
        "firstName": 'Natalya',
        "lastName": 'Baydina',
        "middleName": 'Vladimirovna',
        "companyId": com_id,
        "email": 'ya@mail.ru',
        "url": "string",
        "phone": '+71234567890',
        "birthdate": "1980-05-05T00:00:00.000Z",
        "isActive": 'true'
    }
    new_empl = (employer.add_new(token, body_empl))
    assert new_empl['message'] == 'Unauthorized'


def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_empl = {}
    new_empl = (employer.add_new(token, body_empl))
    assert new_empl['message'] == 'Internal server error'


def test_get_employers_list():
    com_id = company.last_active_company_id()
    list_empl = employer.get_list(com_id)
    assert isinstance(list_empl, list)


def test_get_list_employers_without_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"


def test_get_list_employers_invalide_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(e) == "Employer.get_list () missing 1 required positional argument: 'company_id'"


def test_get_info_new_employer_without_employer_id():
    try:
        employer.get_info()
    except TypeError as e:
        assert str(e) == "Employer.get_info() missing 1 required positional argument: 'employer_id'"


def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_empl = {
        "id": 0,
        "firstName": 'Natalya',
        "lastName": 'Baydina',
        "middleName": 'Vladimirovna',
        "companyId": com_id,
        "email": 'ya@mail.ru',
        "url": "string",
        "phone": '+71234567890',
        "birthdate": "1980-05-05T00:00:00.000Z",
        "isActive": 'true'
    }
    my_empl = employer.add_new(token, body_empl)
    id = my_empl['id']
    body_change_empl = {
        "email": 'yandex@mail.ru',
        "phone": "+79262233445",
        "birthdate": "2000-01-01T00:00:00.000Z",
        "isActive": 'true'
    }
    empl_changed = employer.change_info(token, id, body_change_empl)
    assert empl_changed.status_code == 200
    assert id == empl_changed.json()['id']
    assert (empl_changed.json()["email"]) == body_change_empl.get("email")


def test_employer_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as e:
        assert str(e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"

