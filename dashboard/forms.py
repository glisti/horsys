from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions

from dashboard.models import Message

form_actions = FormActions(
    Submit('save_changes', 'Save'),
    Button('cancel', 'Cancel', css_class='btn btn-default',onclick='history.go(-1);'),
)

class DashboardMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HorseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)
    class Meta:
        model = Horse
        exclude = ['created','modified']