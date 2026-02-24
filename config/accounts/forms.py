from django import forms
from accounts.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}