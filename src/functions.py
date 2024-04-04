from typing import List

from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    ret = []
    for v in vacancies:
        for w in filter_words:
            if w.lower() in str(v).lower():
                ret.append(v)
                break
    return ret


def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    salary_from, salary_to = [int(val) for val in salary_range.split('-')]
    return list(filter(lambda v: salary_from <= v.salary <= salary_to, vacancies))


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    sorted_vacancies = sort_vacancies(vacancies)
    if n > len(vacancies):
        n = len(vacancies)
    return sorted_vacancies[:n]


def print_vacancies(vacancies: List[Vacancy]):
    for index, v in enumerate(vacancies):
        print(f'{index + 1}. {v}')
