from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadFileForm(forms.Form):
    
    title = forms.CharField(max_length=50, required=False)
    user = forms.CharField(max_length=50, required=False)
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = "User Search"
        