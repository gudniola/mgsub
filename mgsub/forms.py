import logging

from django import forms

from mgsub.mailgun import MailgunList

logger = logging.getLogger('mgsub')


class SignupForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, list_email=None, *args, **kwargs):
        self.mailinglist = MailgunList(list_email)
        super(SignupForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        if not super(SignupForm, self).is_valid():
            return False

        if not self.subscribe():
            self.add_error(None, 'There was a failure adding you to the mailing list')
            return False

        return True

    def subscribe(self):
        try:
            return self.mailinglist.subscribe(self.cleaned_data['email'])
        except Exception, e:
            logger.error(e)
            return False

    def unsubscribe(self):
        try:
            return self.mailinglist.unsubscribe(self.cleaned_data['email'])
        except Exception, e:
            logger.error(e)
            return False
