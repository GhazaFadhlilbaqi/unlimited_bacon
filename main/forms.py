from main.models import UnlimitedBacon
from django import forms

class UnlimitedBaconForm(forms.ModelForm):
    class Meta:
        model = UnlimitedBacon
        fields = '__all__'