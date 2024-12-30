from django import forms
from .models import Customer

class CustomerSignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        label="Password"
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        }),
        label="Confirm Password"
    )
    
    class Meta:
        model = Customer
        fields = ['username', 'email', 'cash', 'favorite_genres', 'preferred_language', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email address'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your username'
            }),
            'cash': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your cash balance'
            }),
            'favorite_genres': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input'
            }),
            'preferred_language': forms.Select(attrs={
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your password'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
