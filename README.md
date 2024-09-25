# Module-тест
Тестирование GitHubAPI

## Тест содержит:
 - 3 тестовых маршрута `./__tests__/` с файлами для тестирования
 - 2 FW - `pytest`.
 - В кучестве установщика библиотек используется `Poetry`. 
   - `requirements.txt` результат авто-сборки  от `Poetry`.

### .env
Файл в корне проекта содержит.
```text
GITHUB_TOKEN=token_github
BASE_URL=https://api.github.com
GITHUB_USERNAME=username_of_github-account
```

## Команды
Команды представленные ниже подразумевают:
- у вас есть аккаунт на GitHub;
- знаете как устанавливать зависимости проекта;
- знаете как [создать github-token](https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/).

### Запуск всех тестов
```text
pytest __tests__/test_repository.py
```

