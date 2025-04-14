# 🐦 Bird Trainer

**Bird Trainer** — это веб-приложение на Django для изучения птиц. Пользователь может просматривать список птиц, добавлять новые, а также проходить квиз, чтобы проверить свои знания.

## Возможности

- Просмотр списка птиц с изображениями
- Добавление новых птиц с проверкой на дубликаты
- Квиз: угадай название птицы по изображению
- Мгновенная проверка ответа в квизе

## 🛠 Установка и запуск проекта

### 1. Клонируй репозиторий:

```bash
git clone https://github.com/Sexeniya/birdtrainer.git
cd birds_project
```

### 2. Создай виртуальное окружение и активируй его:
```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Установи зависимости:
```bash
pip install -r requirements.txt
```

### 4. Примени миграции:
```bash
python manage.py migrate
```
### 5. Запусти сервер разработки:
```bash
python manage.py runserver
```
Перейди в браузере по адресу: http://127.0.0.1:8000/

## Готово!
