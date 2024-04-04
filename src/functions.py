from typing import List

from src.vacancy import Vacancy


def print_vacancies(vacancies: List[Vacancy]):
    for index, v in enumerate(vacancies):
        print(f'{index + 1}. {v}')
