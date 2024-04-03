from abc import ABC, abstractmethod


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, key_phrase):
        pass
