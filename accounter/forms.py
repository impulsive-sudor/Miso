# forms.py
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'  # use all fields from the model in the form