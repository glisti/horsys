from django import forms
from django.forms import extras
from django.forms.fields import DateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions
from django.forms import extras
from schedule.models import Shift#, Clock

from select_time_widget import SelectTimeWidget
import time
from datetime import date, datetime, timedelta

form_actions = FormActions(
    Submit('save_changes', 'Save'),
    Button('cancel', 'Cancel', css_class='btn btn-default',onclick='history.go(-1);'),
)

class ShiftAMForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShiftAMForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)
    class Meta:
        model = Shift
        exclude = ['open_haytrap','time_of_day','lights_off','created','modified', 'user']
        widgets = {
        'clock_in': SelectTimeWidget(twelve_hr=True),
        'clock_out': SelectTimeWidget(twelve_hr=True),
        }

class ShiftPMForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShiftPMForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'well form-vertical'
        self.helper.layout.append(form_actions)
    class Meta:
        model = Shift
        exclude = ['open_haytrap','time_of_day','created', 'modified', 'user']
        widgets = {
        'log_in': SelectTimeWidget(twelve_hr=True),
        'log_out': SelectTimeWidget(twelve_hr=True),
        }
