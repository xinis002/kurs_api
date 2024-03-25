import requests

from src.vacancy.work_with_api_service import WorkWithAPIService


class VacanciesHH(WorkWithAPIService):
    """
    Класс реализует подключение к сервисам поиска вакансий
    """

    def connect_to_api(self) -> int:
        """
        Функция реализует подключение к сервису hh.ru
        возвращает статус подключения к сервису

        :return: (int) статус подключения
        """
        response = requests.get("https://api.hh.ru/vacancies")

        return response.status_code

    def get_vacancies(self, param: str) -> list[dict, ...] | None:
        """
        Функция извлекает вакансии с сайта hh.ru. В случае отсутствия параметра params,
        функция проводит поиск среди всех доступных вакансий на платформе.
        Если в результате поиска по заданному параметру params совпадений не обнаруживается,
        пользователь получает сообщение об ошибке поиска.


        :param param: (str) Параметры поиска вакансий
        :return: (str) файл json
        """
        try:
            if self.connect_to_api() != 200:
                raise NameError(f"\nОшибка подключения статус ошибки {self.connect_to_api()} ...")

            else:
                if param:
                    response = requests.get("https://api.hh.ru/vacancies", params={
                        "text": param,
                    })
                    if not response.json().get("items"):
                        raise NameError(f"\nПо поисковому запросу ({param}) "
                                        f"не найдено ни одного совпадения!")
                    else:
                        return response.json().get("items")

                else:
                    response = requests.get("https://api.hh.ru/vacancies")
                    return response.json().get("items")

        except NameError as a:
            print(a)