from django import forms
from django.forms import extras
from django.forms.fields import DateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from schedule.models import Shift, Clock
from select_time_widget import SelectTimeWidget
#import select_time_widget


class ShiftForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShiftForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'well'
        self.helper.add_input(Submit('submit','submit'))

    class Meta:
        model = Shift
        #exclude = ['lights_off',]

class ClockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClockForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'well'
        self.helper.add_input(Submit('submit','submit'))

    class Meta:
        model = Clock
        widgets = {
        'date': extras.SelectDateWidget,
        'log_in': SelectTimeWidget(twelve_hr=True),
        'log_out': SelectTimeWidget(twelve_hr=True),
        }
