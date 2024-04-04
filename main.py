from src.functions import print_vacancies
from src.head_hunter_api import HeadHunterAPI
from src.json_vacancy_storage import JSONVacancyStorage
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000-150000): ")

    hh_api = HeadHunterAPI()

    print("\nПолучение вакансий с сервера. Пожалуйста, подождите.")

    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_storage = JSONVacancyStorage()
    print("\nСохранение вакансий.")

    for vacancy in vacancies_list:
        json_storage.add_vacancy(vacancy)

    print("\nФильтрация вакансий.")
    filtered_vacancies = json_storage.filter_vacancies(filter_words, salary_range, top_n)

    if len(filtered_vacancies) == 0:
        print("\nНе найдено вакансий,удовлетворяющих заданным условиям.")
    else:
        print_vacancies(filtered_vacancies)


if __name__ == "__main__":
    user_interaction()
