# joyoussync

[joyous](https://github.com/linuxsoftware/ls.joyous) is a calendar app for the wagtail CMS.
It supports ical import from file,
but unfortunately not subscription to ical URLs.
This is an attempt to add this support for a very narrow usecase.

Subscription a managed via a settingsmenu in wagtail admin.
The sync is done using Django Q to execute sync functions continuously in the background.
This means you also have to setup Django Q, but all you have to do for that is described here.

## Istallation and setup

1. Setup [joyous](https://github.com/linuxsoftware/ls.joyous)
2. Install `joyoussync`

        pip install joyoussync

3. Add it to and Django Q `INSTALLED_APPS`
   ```python
   INSTALLED_APPS = [
       ...
       'django_q',
       'joyoussync',
       ...
   ]
   ```
4. Configure Django Q in the django settings
   ```python
   Q_CLUSTER = {
       'name': 'Django',
       'timeout': 30,
       'retry': 60,
       'workers': 1,
       'orm': 'default',
       'catch_up': False,
       'has_replica': True,
   }
   ```
5. Start a qcluster

        python manage.py qcluster
