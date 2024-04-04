import copy
from typing import Optional, List


class Vacancy:
    """Класс для работы с вакансиями.
    Поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные,
    которыми инициализируются его атрибуты.
    """

    __v_id: str
    __name: str
    __salary: int
    __key_skills: List[str]
    __experience: Optional[str]
    __schedule: Optional[str]
    __employer: Optional[str]

    def __init__(self, v_id: str, name: str, key_skills: List[str] = None, salary: int = None, experience: str = None,
                 schedule: str = None, employer: str = None):
        self._check_values(v_id, name, key_skills, salary, experience, schedule, employer)
        self.__v_id = v_id
        self.__name = name
        self.__key_skills = [] if key_skills is None else copy.deepcopy(key_skills)
        self.__salary = 0 if salary is None else salary
        self.__experience = experience
        self.__schedule = schedule
        self.__employer = employer

    @staticmethod
    def _check_values(v_id: str, name: str, key_skills: Optional[List[str]], salary: Optional[int],
                      experience: Optional[str], schedule: Optional[str], employer: Optional[str]):
        """метод валидации значений атрибутов экземпляра класса Vacancy"""

        if type(v_id) is not str:
            raise ValueError('id должно быть строкой')
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
        if type(employer) not in [str, type(None)]:
            raise ValueError('employer должно быть строкой')

    def __lt__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.__salary < other.__salary

    def __eq__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.__salary == other.__salary

    def __ne__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.__salary != other.__salary

    def __le__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.__salary <= other.__salary

    def __ge__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.__salary >= other.__salary

    def __gt__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError('Сравнение вакансии с другим типом невозможно')
        return self.__salary > other.__salary

    def __str__(self):
        experience_str = '' if self.__experience is None else f', опыт работы: {self.__experience}'
        schedule_str = '' if self.__schedule is None else f', график работы: {self.__schedule}'
        salary_str = 'зарплата не указана' if self.__salary == 0 else f'зарплата от {self.__salary} руб.'
        key_skills = '' if not self.__key_skills else f', ключевые навыки: {", ".join(self.__key_skills)}'
        employer_str = '' if not self.__employer else f', работодатель: {self.__employer}'
        return f"Вакансия: '{self.__name}', {salary_str}{employer_str}{experience_str}{schedule_str}{key_skills}.\n"

    @classmethod
    # КАК В АННОТАЦИИ ИСПОЛЬЗОВАТЬ cls а не 'VACANCY'?
    def cast_to_object_list(cls, v_json_list: List[dict]) -> List['Vacancy']:
        """преобразует список словарей, содержащих данные о вакансии, полученных с сервера в список объектов вакансий"""
        vacancies: List['Vacancy'] = []
        for v in v_json_list:
            v_id = v.get('id', '')
            name = v.get('name', '')
            key_skills = [skill['name'] for skill in v.get('key_skills', [])]

            salary_obj = v.get('salary')
            salary = salary_obj['from'] if salary_obj is not None else None

            experience_obj = v.get('experience')
            experience = experience_obj['name'] if experience_obj is not None else None

            schedule_obj = v.get('schedule')
            schedule = schedule_obj['name'] if schedule_obj is not None else None

            employer_obj = v.get('employer')
            employer = employer_obj['name'] if employer_obj is not None else None

            vacancies.append(cls(v_id, name, key_skills, salary, experience, schedule, employer))
        return vacancies

    def to_dict(self):
        '''преобразует объект в словарь'''
        suffix = '__'
        return {key if suffix not in key else key[key.index(suffix)+2:]: value for key, value in self.__dict__.items()}

    @property
    def salary(self):
        return self.__salary

    @property
    def name(self):
        return self.__name
