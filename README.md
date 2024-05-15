# Проект по тестированию мобильного приложения <a target="_blank" href="https://telegram.org/">Telegram</a>

![main page screenshot](pictures/telegram_logo.svg)

---
### Список проверок, реализованных в автотестах
1. Нажатие на кнопку "Start messaging" на стартовой странице.
2. Переключение темы со светлой на темную.
3. Ввод номера телефона.

---

### Используемые инструменты
<img title="Python" src="pictures/icons/python.svg" height="40" width="40"/> <img title="Pytest" src="pictures/icons/pytest.svg" height="40" width="40"/> <img title="Allure Report" src="pictures/icons/allure_report.png" height="40" width="40"/> <img title="GitHub" src="pictures/icons/github.svg" height="40" width="40"/> <img title="BrowserStack" src="pictures/icons/browserstack.svg" height="40" width="40"/> <img title="Selene" src="pictures/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="pictures/icons/pycharm-original.svg" height="40" width="40"/> <img title="Appium" src="pictures/icons/appium.svg" height="40" width="40"/> <img title="Jenkins" src="pictures/icons/jenkins-original.svg" height="40" width="40"/> <img title="Jira" src="pictures/icons/jira.svg" height="40" width="40"/>

---

### Для запуска автотестов выполнить следующие команды

* Для запуска на эмуляторе андроида:       pytest -s -v --context=emulator .
* Для запуска на реальном девайсе:         pytest -s -v --context=local_device .
* Для удаленного запуска на BrowserStack:  pytest -s -v --context=browserstack .

> [!IMPORTANT]
> 
> Параметр --context необязателен, по умолчанию тесты запускаются на эмуляторе

### Запуск автотестов осуществляется с использованием Jenkins
> [Ссылка на сборку в Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_telegram_mobile_test/)

#### Для запуска автотестов в Jenkins
1. Открыть [задачу в Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_telegram_mobile_test/)

![jenkins job main page](pictures/Jenkins_job_main_page.png)

2. Нажать "**Build Now**".

---

### Allure отчет

![allure_report main page](pictures/allure_report_main_page.png)

---

### Интеграция с Allure TestOps

> [Job #3993 zmamedov-qa_guru_telegram_mobile_test](https://allure.autotests.cloud/project/4223/jobs)

![allure_testops job](pictures/allure_testops_job.png)

---

### Интеграция с Jira
> [Задача в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1234)
 
![jira task](pictures/jira_task.png)

---

### Уведомления в Телеграм

![telegram_notification](pictures/tg_notification.png)

---

### Прохождение автотеста

![autotest](pictures/test_type_phone_number.gif)
