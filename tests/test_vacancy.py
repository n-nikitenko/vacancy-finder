import pytest

from src.vacancy import Vacancy


@pytest.fixture
def python_vacancy_100k():
    return Vacancy("Python Developer", salary=100000, experience="от 3 лет...")


@pytest.fixture
def python_vacancy_200k():
    return Vacancy("Python Developer", salary=200000, experience="от 3 лет...")


def test_vacancies_comparison(python_vacancy_100k, python_vacancy_200k):
    assert python_vacancy_200k > python_vacancy_100k
    assert python_vacancy_200k >= python_vacancy_100k
    assert python_vacancy_100k <= python_vacancy_200k
    assert python_vacancy_100k < python_vacancy_200k
    assert python_vacancy_100k == python_vacancy_100k
    assert python_vacancy_100k != python_vacancy_200k
