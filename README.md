##Модуль email_sender

### Класс EmailSender включает в себя
- Шаблоны писем с возможностью быстрого расширения
- Метод send_email принимает как аргументы имя шаблона письма, содержание и адресатов, отсылает письмо

### Файл tasks.py содержит функцию - задачу celery в которой вызвается метод send_email

### Инициализация приложения celery в файле main/celery.py
Разрабатывалась на версии celery 5.2.6

### Добавить в settings.py
```
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
```

### Команда запуск celery
```
celery -A main worker -l info --pool=solo
```

### Пример использования в запросе на регистрацию пользователя
```
if email_re is not None:
    msg = render_to_string("mail.html", {"link": link})
    send_email_task.delay(
        "user_registration",
        msg,
        [user.email],
    )
```
