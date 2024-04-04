import os
from typing import List

from src.base_saver import BaseSaver
from src.vacancy import Vacancy
from json import dump, load


class JSONSaver(BaseSaver):
    """Класс для сохранения информации о вакансиях в json-файл"""

    path: str

    def __init__(self):
        '''конструктор. создает json-файл, если он не существует. Очищает содержимое json-файла, если он существует.'''
        self.path = os.path.join("data", "vacancies.json")
        mode = 'w+' if os.path.exists(self.path) else 'x+'
        with open(self.path, mode, encoding='utf-8') as f:
            dump([], f)

    def _read(self) -> List[dict]:
        '''возвращает json из файла'''
        with open(self.path, 'r', encoding='utf-8') as f:
            vacancies = load(f)
        return vacancies

    def _write(self, vacancies: List[dict]):
        '''записывает json в файл'''
        with open(self.path, 'w', encoding='utf-8') as f:
            dump(vacancies, f)

    def add_vacancy(self, vacancy: Vacancy):
        '''добавляет вакансию в файл'''
        if not isinstance(vacancy, Vacancy):
            raise ValueError("Возможно сохранение только объектов типа Vacancy")
        vacancies = self._read()
        vacancies.append(vacancy.to_dict())
        self._write(vacancies)

    def delete_vacancy(self, vacancy: Vacancy):
        '''удаляет вакансию из файла'''
        vacancies = self._read()
        try:
            vacancies.remove(vacancy.to_dict())
        except ValueError:
            print(f'Нет такой вакансии: ${vacancy.name}')
        self._write(vacancies)
