# API Testing на Python

[![Python tests](https://github.com/AllChe10/api-testing/actions/workflows/tests.yml/badge.svg)](https://github.com/AllChe10/api-testing/actions/workflows/tests.yml)

Учебный портфолио-проект по тестированию REST API на Python. Демонстрирует работу с HTTP-запросами, обработку ошибок, unit- и интеграционные тесты, а также автоматический запуск тестов через GitHub Actions.

## Возможности

- GET-запрос к JSONPlaceholder для получения пользователя по ID.
- Проверка HTTP-ошибок через `raise_for_status()`.
- Тайм-аут запроса.
- Unit-тесты с `pytest`, `unittest.mock`, `Mock` и `patch`.
- Параметризация тестов для HTTP-статусов 400, 404 и 500.
- Отдельный интеграционный тест с реальным API.
- Отчёт о покрытии кода через `pytest-cov`.
- GitHub Actions запускает unit-тесты при push и pull request; интеграционные тесты запускаются отдельно, чтобы CI не зависел от доступности внешнего сервиса.

## Структура проекта

```text
api-testing/
├── .github/
│   └── workflows/
│       └── tests.yml
├── api_client.py
├── test_api.py
├── test_api_integration.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Требования

- Python 3.12+
- Доступ к интернету для интеграционного теста

## Установка

Создай виртуальное окружение:

```bash
python -m venv .venv
```

Установи зависимости.

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS / Linux:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Запуск тестов

### Unit-тесты

Эти тесты используют моки и не отправляют реальные запросы в интернет.

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pytest -v -m "not integration"
```

macOS / Linux:

```bash
.venv/bin/python -m pytest -v -m "not integration"
```

### Интеграционные тесты

Эти тесты обращаются к реальному JSONPlaceholder, поэтому зависят от сети и доступности сервиса.

```bash
python -m pytest -v -m integration
```

### Все тесты

```bash
python -m pytest -v
```

### Отчёт о покрытии

```bash
python -m pytest --cov=api_client --cov-report=term-missing -m "not integration"
```

## Что проверяют unit-тесты

- Возвращаемые данные пользователя.
- URL и параметры HTTP-запроса.
- Вызов `raise_for_status()` и декодирование JSON.
- Проброс HTTP-ошибок со статусами 400, 404 и 500.
- Проброс исключения при тайм-ауте.

## Технологии

- Python
- requests
- pytest
- unittest.mock
- pytest-cov
- GitHub Actions

## Цель проекта

Закрепить практические навыки тестирования API: изоляция unit-тестов с помощью моков, проверка ожидаемого поведения при ошибках, написание интеграционных тестов и настройка CI.
