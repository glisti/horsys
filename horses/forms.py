from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from horses.models import Horse

class HorseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HorseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))
    class Meta:
        model = Horse

class MedicalRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))
    class Meta:
        model = MedicalRecord

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))
    class Meta:
        model = Task
