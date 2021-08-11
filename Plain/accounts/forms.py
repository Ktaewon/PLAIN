from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
<<<<<<< HEAD
from .models import User
=======

from .models import User

>>>>>>> 8a344c846abef330b47cfc3a375ac60101599f5b

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('email', 'instrument','nickname', 'genre','instrument')
=======
        fields = ('email', 'date_of_birth')
>>>>>>> 8a344c846abef330b47cfc3a375ac60101599f5b

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('email', 'password', 'instrument', 'genre','nickname','is_active', 'is_admin')
=======
        fields = ('email', 'password', 'date_of_birth',
                  'is_active', 'is_admin')

>>>>>>> 8a344c846abef330b47cfc3a375ac60101599f5b
    def clean_password(self):
        return self.initial["password"]