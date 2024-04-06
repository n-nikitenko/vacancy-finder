import os
from typing import List

from src.base_vacancy_storage import BaseVacancyStorage
from src.vacancy import Vacancy
from json import dump, load


class JSONVacancyStorage(BaseVacancyStorage):
    """Класс для сохранения информации о вакансиях в json-файл"""

    path: str

    def __init__(self):
        """конструктор. создает json-файл, если он не существует. Очищает содержимое json-файла, если он существует."""
        self.path = os.path.join("data", "vacancies.json")
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        mode = 'w+' if os.path.exists(self.path) else 'x+'
        with open(self.path, mode, encoding='utf-8') as f:
            dump([], f)

    def _read(self) -> List[dict]:
        """возвращает json из файла"""
        with open(self.path, 'r', encoding='utf-8') as f:
            vacancies = load(f)
        return vacancies

    def _write(self, vacancies: List[dict]):
        """записывает json в файл"""
        with open(self.path, 'w', encoding='utf-8') as f:
            dump(vacancies, f, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy):
        """добавляет вакансию в файл"""
        if not isinstance(vacancy, Vacancy):
            raise ValueError("Возможно сохранение только объектов типа Vacancy")
        vacancies = self._read()
        vacancies.append(vacancy.to_dict())
        self._write(vacancies)

    def delete_vacancy(self, vacancy: Vacancy):
        """удаляет вакансию из файла"""
        vacancies = self._read()
        try:
            vacancies.remove(vacancy.to_dict())
        except ValueError:
            print(f'Нет такой вакансии: ${vacancy.name}')
        self._write(vacancies)

    def filter_vacancies(self, filter_words: List[str], salary_range: str, n: int) -> List[Vacancy]:
        """Возвращает топ n вакансий по зарплате в заданном диапазоне salary_range, отфильтрованных по ключевым словам
        из списка filter_words"""
        filtered_vacancies = []
        # фильтрация вакансий по ключевым словам
        for v in self.vacancies:
            for w in filter_words:
                if w.lower() in str(v).lower():
                    filtered_vacancies.append(v)
                    break
        # сортировка отфильтрованных вакансий в заданном диапазоне по зарплате
        salary_from, salary_to = [int(val) for val in salary_range.split('-')]
        sorted_vacancies = sorted(list(filter(lambda v: salary_from <= v.salary <= salary_to, filtered_vacancies)),
                                  reverse=True)
        if n > len(sorted_vacancies):
            n = len(sorted_vacancies)
        return sorted_vacancies[:n]

    @property
    def vacancies(self) -> List[Vacancy]:
        '''список вакансий из файла'''
        vacancies_json = self._read()
        return [Vacancy(**v) for v in vacancies_json]
