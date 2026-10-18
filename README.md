# API Testing на Python

Учебный проект для практики тестирования REST API с помощью Python, `requests` и `pytest`.

## Что внутри

- `api_client.py` — функция `get_user(user_id)`, которая отправляет GET-запрос к JSONPlaceholder, проверяет HTTP-ошибки и возвращает JSON.
- `test_api.py` — модульные тесты с моками: успешный ответ, HTTP 404, HTTP 500 и тайм-аут.
- `test_api_integration.py` — интеграционные тесты с реальными HTTP-запросами к тестовому API.
- `pytest.ini` — регистрация маркера интеграционных тестов.
- GitHub Actions запускает модульные тесты при push и pull request.

## Запуск локально

Требуется Python 3.12 или новее.

Создай и активируй виртуальное окружение:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v -m "not integration"
```

Запустить все тесты, включая интеграционные (нужен доступ к интернету):

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Интеграционные тесты обращаются к внешнему сервису и могут зависеть от его доступности. Поэтому в CI по умолчанию запускаются детерминированные тесты с моками.

## Стек

- Python
- pytest
- requests
- unittest.mock
- GitHub Actions

## Цель

Учебный портфолио-проект для закрепления основ API-тестирования: проверка ответа, обработка HTTP-ошибок и тайм-аутов, использование моков и автоматический запуск тестов.
