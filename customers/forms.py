from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions

from customers.models import ContactInfo, Boarders, Owners

form_actions = FormActions(
    Submit('save_changes', 'Save'),
    Button('cancel', 'Cancel', css_class='btn btn-default',onclick='history.go(-1);'),
)

class ContactInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)

    class Meta:
        model = ContactInfo
        exclude = ['owner_name']

class OwnerContactInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OwnerContactInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.layout.append(form_actions)

    class Meta:
        model = ContactInfo
        exclude = ['boarder_name']

class BoardersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoardersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))

    class Meta:
        model = Boarders
        
class OwnersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OwnersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))

    class Meta:
        model = Owners
