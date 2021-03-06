Mailgun list subscription for Django
====================================

This Django module provides a `FormView` and a `Form` that subscribe the user
to a list on `Mailgun`_.

.. _Mailgun: https://www.mailgun.com/

Usage
-----

0. Install::

    pip install django-mgsub
    pip freeze | grep django-mgsub >> requirements.txt

1. Add to Django::

    # settings.py
    INSTALLED_APPS += 'mgsub',

2. Configure credentials::

    # settings.py
    MGSUB_DEFAULT_MAILINGLIST = 'mylist@example.com'
    MAILGUN_API_KEY = '<secret>'

   or::

    export MGSUB_DEFAULT_MAILINGLIST='mylist@example.com' MAILGUN_API_KEY=...

3. Add urls::

    # urls.py
    urlpatterns = [
      ...
        url('^mailinglist/', include('mgsub.urls', namespace='mgsub')),
      ...
    ]

4. Configure::

    ## settings.py

    # Setting this to False will disable email sending and the following
    # settings
    MGSUB_SEND_WELCOME = True

    MGSUB_WELCOME_FROM = 'noreply@example.com'    # defaults to settings.SERVER_EMAIL
    MGSUB_WELCOME_REPLY_TO = 'me@example.com'     # nothing by default

    # Subscription email templates
    MGSUB_WELCOME_SUBJECT = 'Welcome to my list!' # Defaults to: Welcome!
    MGSUB_WELCOME_TEMPLATE = 'myapp/welcome.html' # HTML template
    MGSUB_WELCOME_TEMPLATE_PLAIN = 'myapp/w.txt'  # Plain text template

