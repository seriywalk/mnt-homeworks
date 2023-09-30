# Домашнее задание к занятию 3 «Использование Ansible»

## Подготовка к выполнению

1. Подготовьте в Yandex Cloud три хоста: для `clickhouse`, для `vector` и для `lighthouse`.

2. ![ya-cloud.png](img%2Fya-cloud.png)

2. Репозиторий LightHouse находится [по ссылке](https://github.com/VKCOM/lighthouse).

## Основная часть

1. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает LightHouse.
2. При создании tasks рекомендую использовать модули: `get_url`, `template`, `yum`, `apt`.
3. Tasks должны: скачать статику LightHouse, установить Nginx или любой другой веб-сервер, настроить его конфиг для открытия LightHouse, запустить веб-сервер.
4. Подготовьте свой inventory-файл [prod.yml](my/playbook/inventory/prod.yml).
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.

Результат ansible-playbook -i inventory/prod.yml site.yml --diff > [diff.txt](my/playbook/diff.txt)

9. Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.

Playbook производит развертывание необходимых приложений на сервера в yandex cloud.

**Задачи (Tasks)** 
*Clickhous*e
установка clickhouse
настройка удаленных подключений к приложению
создание базы данных и таблиц
_Vector_
установка vector
изменение конфига приложения для отправки логов на сервер clickhouse
_Lighthouse_
установка lighthouse
настройка nginx

**Переменные (Variables)**
Хранятся в каталоге group_vars:

clickhouse_version, vector_installer_url, lighthouse_distrib - версии, URLs приложений; 
clickhouse_database_name - имя базы данных clickhouse;
clickhouse_create_table - структура таблицы для хранения логов;
vector_config - содержимое конфигурационного файла для vector;
блок конфигурации nginx для работы с lighthouse;

**Тэги (Tags)**
clickhouse производит полную конфигурацию сервера clickhouse;
clickhouse_db производит конфигурацию базы данных и таблицы;
vector производит полную конфигурацию сервера vector;
vector_config производит изменение в конфиге приложения vector;
lighthouse производит установку lighthouse.

10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-03-yandex` на фиксирующий коммит, в ответ предоставьте ссылку на него.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
