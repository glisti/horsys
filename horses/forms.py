from django import forms

from horses.models import Horse

class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name','nickname','age','weight','feet','inches','color','breed']