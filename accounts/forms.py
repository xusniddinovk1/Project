from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ismingiz'})
    )
    phone_number = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+998 90 123 45 67'})
    )
    username = forms.CharField(
        label='Telegram username',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '@username'})
    )

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("Bu telefon raqam allaqachon mavjud.")
        return phone
