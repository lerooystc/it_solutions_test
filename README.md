
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
