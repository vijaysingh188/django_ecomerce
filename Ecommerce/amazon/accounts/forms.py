from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput
                                        (attrs={
                                                'class': 'form-control',
                                                'placeholder':'enter username'}
                                        ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                'class': 'form-control',
                                                'placeholder':'enter password'}
                                        ))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the username"}))
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                  "placeholder":"Enter Password again"}))

    def clean_password(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2!=password:
            raise forms.ValidationError("password should match")
        return data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)

        if qs.exists():
            raise forms.ValidationError("username already taken")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError("email already taken")
        return email




