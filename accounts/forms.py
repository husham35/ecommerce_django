from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    first_name = forms.CharField(
        max_length=30,
        required=True,  # Mark this field as required
        help_text='First name is required',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,  # Mark this field as required
        help_text='Last name is required',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError('First name should only contain letters.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError('Last name should only contain letters.')
        return last_name