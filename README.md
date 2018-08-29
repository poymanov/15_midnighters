# Night Owls Detector

Скрипт получает список пользователей [DEVMAN.org](https://devman.org), которые отправляли задания на проверку после полуночи.

# Предварительные настройки

- Установить и запустить [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для Python
- Установить дополнительные пакеты:
```
pip install -r requirements.txt
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора **Python** версии **3.5**.

**Запуск на Linux**

```bash
$ python seek_dev_nighters.py # или python3, в зависимости от настроек системы

# результат выполнения скрипта
user1
26-05-2018 00:35

user2
22-07-2018 03:38
23-08-2018 02:59

# в случае ошибки запроса/обработки данных
Failed to load attemps info

# в случае если пользователей-полуночников нет
There are not any midnighters

```

Запуск на **Windows** происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
