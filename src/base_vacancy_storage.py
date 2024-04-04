from abc import ABC, abstractmethod
from typing import List

from src.vacancy import Vacancy


class BaseVacancyStorage(ABC):
    """абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
     получения данных из файла по указанным критериям и удаления информации о вакансиях. """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def filter_vacancies(self, filter_words: List[str], salary_range: str, n: int) -> List[Vacancy]:
        pass

