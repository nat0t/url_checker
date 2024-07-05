# URL-checker
Приложение проверяет переданные веб-ссылки и возвращает статус-код.
____
## Развёртывание
Для развёртывания необходимо:
- создать и применить миграции, для чего из директории backend следует выполнить команды
```
python manage.py makemigrations
python manage.py migrate
```
- переименовать файл .env.sample в .env и изменить в нём значения на необходимые
```
mv .env.sample .env
```
- собрать и запустить контейнеры командой из корня проекта
```
docker-compose up --build
```
## API
API приложения доступно по ссылке /api/

Работа с пользователями (доступны методы GET, POST, DELETE): /api/users/

Работа со ссылками (доступны методы GET, POST, PUT, DELETE): /api/checker/