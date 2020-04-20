from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import Account


class AccountRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Email Address Required", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'name': 'email',
        'placeholder':
        'E-mail Address',}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'first_name',
        'placeholder': 'First Name'}),)
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'last_name',
        'placeholder': 'Last Name'}),)
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Username'}),)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
         'name': 'password1',
          'placeholder': 'Password'}),)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
         'name': 'password2',
        'placeholder': 'Confirm Password'}),)

    profile_picture = forms.ImageField(max_length=500, label='Profile Photo', required=False)


    

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2', 'profile_picture')

class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text="Email Address Required", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'name': 'email',
        'placeholder':
        'E-mail Address',}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
         'name': 'password',
          'placeholder': 'Password'}),)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

