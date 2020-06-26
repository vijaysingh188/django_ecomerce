from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
class Contactform(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput
                                        (attrs={
                                                'class': 'form-control',
                                                'placeholder':'your full name'}
                                        ))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'your email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','size': '40','placeholder':'my message'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail" not in email:
            raise forms.ValidationError("email should contain gmail.com")
        return email




