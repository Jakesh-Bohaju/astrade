from django import forms

from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('first_name', 'middle_name', 'last_name', 'username', 'email', 'password',
                  'address', 'image', 'phone_no1', 'phone_no2', 'is_active', 'is_staff', 'is_superuser'
                  )

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Entered password and confirm password not match. Enter password again")
        return confirm_password
