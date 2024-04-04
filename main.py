from src.functions import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
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

    print("\nФильтрация вакансий по ключевым словам.\n")
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    json_saver = JSONSaver()

    if len(top_vacancies) == 0:
        print("\nНе найдено вакансий,удовлетворяющих заданным условиям.")
    else:
        print_vacancies(top_vacancies)

        print("\nСохранение вакансий.")

        for vacancy in top_vacancies:
            json_saver.add_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()
