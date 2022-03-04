from django import forms
from bookapp.models import UserAccount

class UserForm(forms.ModelForm):
    class Meta:
        model= UserAccount
        fields=['username','password','rights']