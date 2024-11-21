from django import forms
from .models import UserRegistration, ContactForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    class Meta:
        model = UserRegistration
        fields = ['username', 'password']  # confirm_password is manually handled and not part of model fields
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'project_location', 'describe_project']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'email': forms.EmailInput(attrs={'class': 'form-control input-field'}),
            'project_location': forms.Textarea(attrs={'class': 'form-control input-field'}),
            'describe_project': forms.Textarea(attrs={'class': 'form-control input-field'}),
        }
