import copy

from requests import ConnectTimeout, ReadTimeout

from src.base_api import BaseAPI
import requests


class HeadHunterAPI(BaseAPI):
    """
        Класс для работы с API HeadHunter
    """
    __base_url: str
    __headers: dict
    __params: dict
    __vacancies: list

    def __init__(self):
        self.__base_url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def get_vacancies(self, key_phrase: str) -> list:
        self.__vacancies.clear()
        self.__params['text'] = key_phrase
        self.__params['page'] = 0
        while self.__params.get('page') != 1:
            try:
                response = requests.get(self.__base_url, headers=self.__headers, params=self.__params, timeout=1)
            except requests.exceptions.Timeout as e:
                print("Истекло время ожидания ответа сервера. Попробуйте позже.")  # todo: throw Exception
                return copy.deepcopy(self.__vacancies)
            else:
                if response.status_code == 200:
                    vacancies = response.json()['items']
                    self.__vacancies.extend(vacancies)
                    self.__params['page'] += 1
                else:  # todo: throw exception or process errors
                    return copy.deepcopy(self.__vacancies)
        return copy.deepcopy(self.__vacancies)
