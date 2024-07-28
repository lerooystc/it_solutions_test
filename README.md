
  <h3 align="center">API-сервис для получения данных</h3>

Требуется разработать API-сервис для получения данных о первых 10 объявлениях по
ссылке https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/


### Используемый стек технологий в проекте:
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Alembic

### Для работы необходимо:
* Склонировать репозиторий в локальную директорию:
  ```sh
  git clone https://github.com/lerooystc/it_solutions_test
  ```
* Активация виртуального окружения и создание зависимостей:
  ```sh
  python -m venv venv
  ./venv/Scripts/activate
  cd backend
  pip install -r requirements.txt
  ```
* В ./backend создайте ```.env``` и задайте значения переменных:
    ```sh
    DB_NAME =
    DB_USER =
    DB_USER_PASSWORD =
    DB_HOST =
    DB_PORT =
    SECRET_KEY=
    ```
* Запуск сервера:
    ```sh
    uvicorn main:app --reload
    ```
* Перейдите по ссылке в консоли:
  Для удобного использования добавьте в конец адресной строки "/docs".
* Работа с приложением:
  - Создайте пользователя по хуку /users
  - Авторизируйтесь в доках, либо получите токен по хуку /login, а затем передавайте его в хедере Authorization
  - Добавьте объявление по хуку /adverts
  - Получите объявление по хуку /adverts/{id}
