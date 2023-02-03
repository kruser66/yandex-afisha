# Интерактивная карта

Проект позволяет создать "свою" интерактивную карту локаций (мероприятий).  


## Где посмотреть и попробовать

Демо-версия сайта находится [тут](http://kruser.pythonanywhere.com/).

Возможность добавить или подкорректировать локацию, добавить изображения,  
описание или название, поменять картинки местами можно в  
[режиме администратора тут](http://kruser.pythonanywhere.com/admin/places/excursion/)  
(тестовый логин: `user` пароль: `Kyg2=Kul6-Ty9`).


## Как установить и запустить

Скачайте код с репозитория.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
```bash
pip install -r requirements.txt
```

### Переменные окружения
Для работы сайта понадобятся следующие переменные окружения:
```bash
SECRET_KEY=YOUR_SECRET_KEY
ALLOWED_HOSTS=127.0.0.1, *.pythonanywhere.com
```
Переменные ниже установлены по-умолчанию, при необходимости установите свои
```bash
DEBUG=False
STATIC_URL=/static/
STATIC_ROOT=static
MEDIA_URL=/media/
MEDIA_ROOT=media
```

## Как запустить

Создайте и примените миграции:
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
Создайте СуперПользователя для доступа в админку:
```bash
python3 manage.py createsuperuser
```

Для запуска сайта локально:
```
python3 manage.py runserver
```
Доступ в админку будет по адресу: http://127.0.0.1:8000/admin/.


## Загрузка локаций

Примеры и шаблоны описания локаций для загрузки приведены на этом [ресурсе](https://github.com/devmanorg/where-to-go-places.git).
Для загрузке необходимо использовать менеджер команд:
```bash
python manage.py load_place place_url
```
где `place_url` - ссылка на json-данные согласно шаблона, [пример](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%20Gravity.json)


# Цель проекта

Код написан в образовательных целях на онлайн-курс для веб-разработчиков:  
[Devman - От новичка до Middle Python/Django разработчика](https://dvmn.org/t/middle-python-dev-before-you-finish-the-course/).