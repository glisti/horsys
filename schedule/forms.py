from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from schedule.models import Log

class LogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'well'
        self.helper.add_input(Submit('submit','submit'))

    class Meta:
        model = Log