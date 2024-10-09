from main.models import UnlimitedBacon
from django import forms
from django.utils.html import strip_tags

class UnlimitedBaconForm(forms.ModelForm):
    class Meta:
        model = UnlimitedBacon
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)