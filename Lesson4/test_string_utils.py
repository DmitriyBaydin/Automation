import pytest

from string_utils import StringUtils

st_ut = StringUtils()


# Test case 1: Тест функциональности "capitilize",
# которая делает первую букву заглавной
@pytest.mark.parametrize('string, result', [
    # положительные
    ("moscow", "Moscow"),
    ("великий новгород", "Великий новгород"),
    ("мариАнна", "Марианна"),
    ("mary Anne", "Mary anne"),
    ("пример-1", "Пример-1"),
    # негативные
    ("", ""),
    (" ", " "),
    ("Volvo", "Volvo"),
    ("европа ", "Европа "),
    ("123abc", "123abc"),
    (123, 123)
    ])
def test_capitilize(string, result):
    st_ut = StringUtils()
    res = st_ut.capitilize(string)
    assert res == result


# Test case 2: Тест функциональности "trim", которая удаляет пробелы в начале
@pytest.mark.parametrize('string, result', [
    # положительные
    (" Apple", "Apple"),
    ("  dog", "dog"),
    (" АБВГД", "АБВГД"),
    ("  123  ", "123  "),
    (" Mary-Anne", "Mary-Anne"),
    ("   Остров16", "Остров16"),
    # негативные
    ("", ""),
    ("со бака", "со бака"),
    ("лето", "лето"),
    ("123  ", "123  "),
    (1, 1),
    (0, 0)
    ])
def test_trim(string, result):
    st_ut = StringUtils()
    res = st_ut.trim(string)
    assert res == result


# Test case 3: Тест функциональности "to_list",
# которая принимает на вход текст с разделителем и возвращает список строк
@pytest.mark.parametrize('string, divider, result', [
    # положительные
    ("Ivan,Mary,Ann", ",", ["Ivan", "Mary", "Ann"]),
    ("лето,жара,июль", ",", ["лето", "жара", "июль"]),
    ("bus;tram;underground", ";", ["bus", "tram", "underground"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("#^*^!^?^$", "^", ["#", "*", "!", "?", "$"]),
    ("A/nB/nC", "/n", ["A", "B", "C"]),
    # негативные
    ("", None, []),
    ("0,3,7,20 24", None, ["0", "3", "7", "20 24"]),
    ])
def test_to_list(string, divider, result):
    st_ut = StringUtils()
    if divider is None:
        res = st_ut.to_list(string)
    else:
        res = st_ut.to_list(string, divider)
    assert res == result


# Test case 4: Тест функциональности "contains",которая возвращает `True`,
# если строка содержит искомый символ и `False` - если нет
@pytest.mark.parametrize('string, symbol, result', [
    # положительные
    ("Ivan", "a", True),
    (" лето", "е", True),
    ("bus ", "s", True),
    ("12345", "1", True),
    ("#*!?$", "$", True),
    ("", "", True),
    # негативные
    ("Moscow", "m", False),
    ("Moscow", "W", False),
    ("привет", "ы", False),
    ("привет", "?", False),
    ("привет", "", False),
    (" ", "a", False)
    ])
def test_contains(string, symbol, result):
    st_ut = StringUtils()
    res = st_ut.contains(string, symbol)
    assert res == result


# Test case 5: Тест функциональности "delete_symbol",
# которая удаляет все подстроки из переданной строки
@pytest.mark.parametrize('string, symbol, result', [
    # положительные
    ("Ivan", "a", "Ivn"),
    (" лето", "е", " лто"),
    ("bus ", "s", "bu "),
    ("12345", "1", "2345"),
    ("#*!?$", "$", "#*!?"),
    ("SkyPro", "Sky", "Pro"),
    # негативные
    ("Moscow", "A", "Moscow"),
    ("", "", ""),
    ("привет", "ы", "привет"),
    ("привет ", "", "привет "),
    ("привет", "ет", "прив"),
    (" ", "a", " ")
    ])
def test_delete_symbol(string, symbol, result):
    st_ut = StringUtils()
    res = st_ut.delete_symbol(string, symbol)
    assert res == result


# Test case 6: Тест функциональности "starts_with", которая возвращает `True`,
# если строка начинается с заданного символа и `False` - если нет
@pytest.mark.parametrize('string, symbol, result', [
    # положительные
    ("Ivan", "I", True),
    ("лето", "л", True),
    ("bus ", "b", True),
    ("12345", "1", True),
    ("#*!?$", "#", True),
    ("SkyPro", "S", True),
    ("", "", True),
    # негативные
    ("Moscow", "A", False),
    ("Moscow", "w", False),
    ("привет", "ы", False),
    ("привет ", "У", False),
    ("привет", "П", False),
    ("123", "3", False)
    ])
def test_starts_with(string, symbol, result):
    st_ut = StringUtils()
    res = st_ut.starts_with(string, symbol)
    assert res == result


# Test case 7: Тест функциональности "end_with", которая возвращает `True`,
# если строка заканчивается заданным символом и `False` - если нет
@pytest.mark.parametrize('string, symbol, result', [
    # положительные
    ("Ivan", "n", True),
    ("лето", "о", True),
    (" bus", "s", True),
    ("12345", "5", True),
    ("#*!?$", "$", True),
    ("SkyPro", "o", True),
    ("", "", True),
    # негативные
    ("Moscow", "A", False),
    ("Moscow", "m", False),
    ("привет", "ы", False),
    ("привет ", "У", False),
    ("привет", "Т", False),
    ("123", "1", False)
    ])
def test_end_with(string, symbol, result):
    st_ut = StringUtils()
    res = st_ut.end_with(string, symbol)
    assert res == result


# Test case 8: Тест функциональности "is_empty", которая возвращает `True`,
# если строка пустая и `False` - если нет
@pytest.mark.parametrize('string, result', [
    # положительные
    ("", True),
    (" ", True),
    ("  ", True),
    # негативные
    ("Moscow", False),
    (" привет", False),
    ("привет ", False),
    ("123", False)
    ])
def test_is_empty(string, result):
    st_ut = StringUtils()
    res = st_ut.is_empty(string)
    assert res == result


# Test case 9: Тест функциональности "list_to_string",
# которая преобразует список элементов в строку с указанным разделителем
@pytest.mark.parametrize('lst, joiner, result', [
    # положительные
    (["A", "B", "C"], ",", "A,B,C"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Нью", "Йорк"], "-", "Нью-Йорк"),
    # негативные
    ([], None,  ""),
    ([], "^", "")
    ])
def test_list_to_string(lst, joiner, result):
    st_ut = StringUtils()
    if joiner is None:
        res = st_ut.list_to_string(lst)
    else:
        res = st_ut.list_to_string(lst, joiner)
    assert res == result
