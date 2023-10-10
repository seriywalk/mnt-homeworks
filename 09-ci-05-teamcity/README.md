# Домашнее задание к занятию 11 «Teamcity»

## Подготовка к выполнению

1. В Yandex Cloud создайте новый инстанс (4CPU4RAM) на основе образа `jetbrains/teamcity-server`.
2. Дождитесь запуска teamcity, выполните первоначальную настройку.
3. Создайте ещё один инстанс (2CPU4RAM) на основе образа `jetbrains/teamcity-agent`. Пропишите к нему переменную окружения `SERVER_URL: "http://<teamcity_url>:8111"`.

![yacloudVM.png](img%2FyacloudVM.png)

4. Авторизуйте агент.

![agentAuth.png](img%2FagentAuth.png)

5. Сделайте fork [репозитория](https://github.com/aragastmatb/example-teamcity).

Мой [репозиторий](https://github.com/seriywalk/example-teamcity.git)

6. Создайте VM (2CPU4RAM) и запустите [playbook](./infrastructure).

[Ansible-playbook](infrastructure/ansible.txt)

## Основная часть

1. Создайте новый проект в teamcity на основе fork.
2. Сделайте autodetect конфигурации.

![build.png](img%2Fbuild.png)

3. Сохраните необходимые шаги, запустите первую сборку master.

![build_run.png](img%2Fbuild_run.png)

4. Поменяйте условия сборки: если сборка по ветке `master`, то должен происходит `mvn clean deploy`, иначе `mvn clean test`.

![buildsteps.png](img%2Fbuildsteps.png)
 
5. Для deploy будет необходимо загрузить [settings.xml](./teamcity/settings.xml) в набор конфигураций maven у teamcity, предварительно записав туда креды для подключения к nexus.

![settings.png](img%2Fsettings.png)
 
6. В pom.xml необходимо поменять ссылки на репозиторий и nexus.

![pom.png](img%2Fpom.png)

7. Запустите сборку по master, убедитесь, что всё прошло успешно и артефакт появился в nexus.

![nexus.png](img%2Fnexus.png)

8. Мигрируйте `build configuration` в репозиторий.

![build_config.png](img%2Fbuild_config.png)

9. Создайте отдельную ветку `feature/add_reply` в репозитории.

![branch.png](img%2Fbranch.png)
 
10. Напишите новый метод для класса Welcomer: метод должен возвращать произвольную реплику, содержащую слово `hunter`.

![Hi.png](img%2FHi.png)

11. Дополните тест для нового метода на поиск слова `hunter` в новой реплике.

![test.png](img%2Ftest.png)

12. Сделайте push всех изменений в новую ветку репозитория.

![push_feature.png](img%2Fpush_feature.png)

13. Убедитесь, что сборка самостоятельно запустилась, тесты прошли успешно.

![redeploy.png](img%2Fredeploy.png)
14. Внесите изменения из произвольной ветки `feature/add_reply` в `master` через `Merge`.

15. Убедитесь, что нет собранного артефакта в сборке по ветке `master`.

16. Настройте конфигурацию так, чтобы она собирала `.jar` в артефакты сборки.

![artefact.png](img%2Fartefact.png)

17. Проведите повторную сборку мастера, убедитесь, что сбора прошла успешно и артефакты собраны.

![merge.png](img%2Fmerge.png)

![last.png](img%2Flast.png)

18.Проверьте, что конфигурация в репозитории содержит все настройки конфигурации из teamcity.

19. В ответе пришлите ссылку на репозиторий.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
