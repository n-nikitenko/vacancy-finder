from src.head_hunter_api import HeadHunterAPI

hh_api = HeadHunterAPI()
vacancies = hh_api.get_vacancies('Python')

print(vacancies)