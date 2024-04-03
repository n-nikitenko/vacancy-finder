import json

from src.head_hunter_api import HeadHunterAPI


def test_hh_api():
    """Проверка, что hh_api.get_vacancies возвращает непустой список объектов"""
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies('Python')
    assert type(vacancies) is list
    assert len(vacancies) > 0
    try:
        json.loads(json.dumps(vacancies))
    except ValueError:
        assert False
    else:
        assert True
