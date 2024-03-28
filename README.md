<h2 align="center">PySoNet</h2>

Социальная сеть на Django Rest Framework

### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework == 3.15.1
- PostgreSQL


## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up

##### 3) Перейти по адресу

    http://127.0.0.1:8000/api/v1/swagger/

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=fdastgae2342%qwd@#@%Ffed
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=pysonet
    POSTGRES_USER=pysonet_user
    POSTGRES_PASSWORD=pysonet_pass
    POSTGRES_HOST=pysonet_db
    POSTGRES_PORT=5432

    DATABASE=postgres

##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up

##### 6) Создать суперюзера

    docker exec -it pysonet-pysonet-1 python manage.py createsuperuser

##### 7) Если нужно очистить БД

    docker-compose down -v

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2024-present, mimimichaello - Morozov Alexandr
