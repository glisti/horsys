from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions

from horses.models import Horse, MedicalRecord, Task, Note

form_actions = FormActions(
    Submit('save_changes', 'Save'),
    Button('cancel', 'Cancel', css_class='btn btn-default',onclick='history.go(-1);'),
)

class HorseForm(forms.ModelForm):
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

class MedicalRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)
    class Meta:
        model = MedicalRecord
        exclude = ['created','modified']

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)
    class Meta:
        model = Task
        exclude = ['completed','created','modified']

class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)
    class Meta:
        model = Note
        exclude = ['created','modified']