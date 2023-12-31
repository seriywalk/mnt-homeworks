# Домашнее задание к занятию 2 «Работа с Playbook»

## Подготовка к выполнению

1. * Необязательно. Изучите, что такое [ClickHouse](https://www.youtube.com/watch?v=fjTNS2zkeBs) и [Vector](https://www.youtube.com/watch?v=CgEhyffisLY).
2. Создайте свой публичный репозиторий на GitHub с произвольным именем или используйте старый.
3. Скачайте [Playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.
4. Подготовьте хосты в соответствии с группами из предподготовленного playbook.

![ya_cloud.png](img%2Fya_cloud.png)

## Основная часть

1. Подготовьте свой inventory-файл [prod.yml](playbook/inventory/prod.yml).
2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает [vector](https://vector.dev). Конфигурация vector должна деплоиться через template файл jinja2.
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.
4. Tasks должны: скачать дистрибутив нужной версии, выполнить распаковку в выбранную директорию, установить vector.
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе [произведены](playbook/diff.txt).
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
9. Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги. Пример качественной документации ansible playbook по [ссылке](https://github.com/opensearch-project/ansible-playbook).
10. Готовый [playbook](playbook/site.yml) выложите в свой репозиторий, поставьте тег `08-ansible-02-playbook` на фиксирующий коммит, в ответ предоставьте ссылку на него.

#### Playbook производит развертывание необходимых приложений на сервера в yandex cloud.

**Задачи (Tasks)** 

*Clickhous*e

установка clickhouse
настройка удаленных подключений к приложению
создание базы данных и таблиц

_Vector_

установка vector
изменение конфига приложения для отправки логов на сервер clickhouse

**Переменные (Variables)**

Хранятся в каталоге group_vars:

* clickhouse_version, vector_installer_url  - версии, URLs приложений; 
* clickhouse_database_name - имя базы данных clickhouse;
* clickhouse_create_table - структура таблицы для хранения логов;
* vector_config - содержимое конфигурационного файла для vector;

**Тэги (Tags)**

* clickhouse производит полную конфигурацию сервера clickhouse;
* clickhouse_db производит конфигурацию базы данных и таблицы;
* vector производит полную конфигурацию сервера vector;
* vector_config производит изменение в конфиге приложения vector;

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
