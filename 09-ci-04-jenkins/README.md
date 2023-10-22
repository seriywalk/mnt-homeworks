# Домашнее задание к занятию 10 «Jenkins»

## Подготовка к выполнению

1. Создать два VM: для jenkins-master и jenkins-agent.

![instances.png](images%2Finstances.png)

2. Установить Jenkins при помощи playbook.
3. Запустить и проверить работоспособность.
4. Сделать первоначальную настройку.

![jenkins.png](images%2Fjenkins.png)

## Основная часть

1. Сделать Freestyle Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.

![freestyleJob.png](images%2FfreestyleJob.png)
![molecule1.png](images%2Fmolecule1.png)
![freestyle.png](images%2Ffreestyle.png)

2. Сделать Declarative Pipeline Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.

![pipeline.png](images%2Fpipeline.png)
![pipelinestatus.png](images%2Fpipelinestatus.png)

3. Перенести Declarative Pipeline в репозиторий в файл [Jenkinsfile](https://github.com/seriywalk/vector-role/blob/master/Jenkinsfile). 
4. Создать Multibranch Pipeline на запуск `Jenkinsfile` из репозитория.

![multi.png](images%2Fmulti.png)

5. Создать Scripted Pipeline, наполнить его скриптом из [pipeline](./pipeline).
6. Внести необходимые изменения, чтобы Pipeline запускал `ansible-playbook` без флагов `--check --diff`, если не установлен параметр при запуске джобы (prod_run = True). По умолчанию параметр имеет значение False и запускает прогон с флагами `--check --diff`.

![scripted.png](images%2Fscripted.png)

7. Проверить работоспособность, исправить ошибки, исправленный Pipeline вложить в репозиторий в файл `ScriptedJenkinsfile`.
8. Отправить ссылку на репозиторий с ролью и Declarative Pipeline и Scripted Pipeline.

https://github.com/seriywalk/vector-role.git

[Declarative Pipeline](https://github.com/seriywalk/vector-role/blob/master/Jenkinsfile)

[Scripted Pipline](scriptedjenkinsfile)

## Необязательная часть

1. Создать скрипт на groovy, который будет собирать все Job, завершившиеся хотя бы раз неуспешно. Добавить скрипт в репозиторий с решением и названием `AllJobFailure.groovy`.
2. Создать Scripted Pipeline так, чтобы он мог сначала запустить через Yandex Cloud CLI необходимое количество инстансов, прописать их в инвентори плейбука и после этого запускать плейбук. Мы должны при нажатии кнопки получить готовую к использованию систему.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.
---
