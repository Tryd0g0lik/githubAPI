# Module-тест
Тестирование GitHub REST API

## Тест содержит:
 - 3 тестовых маршрута `./__tests__/` с файлами для тестирования
 - 2 FW - `pytest`.
 - В качестве установщика библиотек сам использую `Poetry`. \
Можно использовать `pip`
   - `requirements.txt` результат авто-сборки от `Poetry`.

### .env
Файл в корне проекта содержит.
```text
GITHUB_TOKEN=token_github
BASE_URL=https://api.github.com
GITHUB_USERNAME=username_of_github-account
```
Остаётся только вставить секретные данные. После импорт из файла `dotenv_.py`

## Команды
Команды представленные ниже подразумевают:
- у вас есть аккаунт на GitHub;
- вы клонировали проект на локальный диск;
- знаете как [создать github-token](https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/).

### Установить зависимости
Установщик `pip` весьма популярен. Команды будут завязаны на `pip`, поэтому \
удалите файл `pyproject.toml` (файл для поклонников `Poetry`). \
Далее как обычно. \
```text
# Обновление pip - для работы с последними версиями библиотек
py -m pip install --upgrade pip

# Устанавливаем зависимости
pip install -r  requirements.txt
```


### Запуск всех тестов
```text
pytest __tests__/test_repository.py
```

