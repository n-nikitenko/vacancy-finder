import copy
from typing import Optional, List


class Vacancy:
    """Класс для работы с вакансиями.
    Поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные,
    которыми инициализируются его атрибуты.
    """

    name: str
    salary: int
    key_skills: List[str]
    experience: Optional[str]
    schedule: Optional[str]

    def __init__(self, name, key_skills=None, salary=None, experience=None, schedule=None):
        self._check_values(name, key_skills, salary, experience, schedule)
        self.name = name
        self.key_skills = [] if key_skills is None else copy.deepcopy(key_skills)
        self.salary = 0 if salary is None else salary
        self.experience = experience
        self.schedule = schedule

    @staticmethod
    def _check_values(name, key_skills=None, salary=None, experience=None, schedule=None):
        """метод валидации значений атрибутов экземпляра класса Vacancy"""

        if type(name) is not str:
            raise ValueError('name должно быть строкой')
        if type(key_skills) not in [list, type(None)]:
            raise ValueError('key_skills должно быть списком строк')
        if key_skills is not None and len(key_skills) > 0 and type(key_skills[0]) is not str:
            raise ValueError('key_skills должно быть списком строк')
        if type(salary) not in [int, type(None)]:
            raise ValueError('salary должно быть целым числом')
        if type(experience) not in [str, type(None)]:
            raise ValueError('experience должно быть строкой')
        if type(schedule) not in [str, type(None)]:
            raise ValueError('schedule должно быть строкой')

    def __lt__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.salary < other.salary

    def __eq__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.salary == other.salary

    def __ne__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.salary != other.salary

    def __le__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.salary <= other.salary

    def __ge__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.salary >= other.salary

    def __gt__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.salary > other.salary

    def __str__(self):
        experience_str = '' if self.experience is None else f', опыт работы: {self.experience}'
        schedule_str = '' if self.schedule is None else f', график работы: {self.schedule}'
        salary_str = 'зарплата не указана' if self.salary == 0 else f'зарплата от {self.salary} руб.'
        key_skills = '' if self.schedule is None else f', ключевые навыки: {", ".join(self.key_skills)}'
        return f"\nВакансия: '{self.name}', {salary_str}{experience_str}{schedule_str}{key_skills}\n\n"
