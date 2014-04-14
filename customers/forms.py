from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from customers.models import Feeder, Boarder, ContactInfo

class BoarderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoarderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))
    class Meta:
        model = Boarder