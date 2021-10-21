# PermissionError: [WinError 32]

```powershell
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'D:\\Python_playground\\Practice\\Django\\loggerproject\\mylog\\log.log' -> 'D:\\Python_playground\\Practice\\Django\\loggerproject\\mylog\\log.log.2021-10-02_13-24-19'
```

As when we are using **TimedRotatingFileHandler** this error occurs because it is open somewhere.

But where? simply it is opened in **TimedRotatingFileHandler** , hmm but we have opened it once!!

yeah but setting.py opened it twice.

When we are using Django Debug mode  settings.py runs twice while starting.. Don't believe me see the starting video where sir used  print statement isetting.py... Or simply add `print("In settings.py")` in settings.py.

That why we are getting error.

Because **TimedRotatingFileHandler** is trying to modify a log file  which is opened in another instance of  **TimedRotatingFileHandler**.

To avoid this use following command

```powershell
python manage.py runserver --noreload
```

If you have added `print("In settings.py")` in settings.py previously, you can see there is only one print on the console.

This will load settings.py once so there will no **PermissionError: [WinError 32]** and you can also delete logs too except the first one which can only deleted when **django_env** is not running.

<div style="page-break-after: always; break-after: page;"></div>

**TimedRotatingFileHandler** 

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'test_logger': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': r'D:\Python_playground\Practice\Django\loggerproject\mylog\log.log',
            'when': 'S',
            'backupCount': 2,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'test_logger': {
            'handlers': ['test_logger'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

As for backup count there is catch it won't old log whatever you do by default it take **backupCount** = 0 so if you want to change it.

You may see more files than **backupCount**.

Created_By = **"Mohammad Sharique"**

