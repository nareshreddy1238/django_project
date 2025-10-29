from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('Male','MALE'),('Female','FEMALE')]
    firstName = forms.CharField(required=False, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    lastName = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()

    """
    def clean_firstName(self):
        self.firstName = self.cleaned_data['firstName']
        if len(self.firstName) > 20:
            raise forms.ValidationError("First Name should be less than 20 characters")
        return self.firstName

    def clean_email(self):
        self.email = self.cleaned_data['email']
        if not self.email.endswith('.com'):
            raise forms.ValidationError("Email should end with .com")
        elif not ('@' in self.email and '.' in self.email):
            raise forms.ValidationError("Email should contain @ and .")
        return self.email

    def clean(self):
        all_clean_data = super().clean()
        firstName = all_clean_data['firstName']
        email = all_clean_data['email']
        if len(firstName) > 20:
            raise forms.ValidationError("First Name should be less than 20 characters")
        if not email.endswith('.com'):
            raise forms.ValidationError("Email should end with .com")
        elif not ('@' in email and '.' in email):
            raise forms.ValidationError("Email should contain @ and .")
    """