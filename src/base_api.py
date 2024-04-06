from abc import ABC, abstractmethod
from typing import List


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, key_phrase) -> List[dict]:
        pass
