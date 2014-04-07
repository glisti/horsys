from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from horses.models import ContactInfo, Boarders, Owners

class ContactInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class  = 'well form-vertical'
        self.helper.add_input(Submit('submit','submit'))

    class Meta:
        model = ContactInfo

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
