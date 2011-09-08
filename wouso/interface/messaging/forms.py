from django import forms
from wouso.core.user.models import Player

class ComposeForm(forms.Form):
    to = forms.ModelChoiceField(queryset=Player.objects.all())
    subject = forms.CharField(max_length=200, required=False)
    text = forms.CharField(max_length=500, required=False)
