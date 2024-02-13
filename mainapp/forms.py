from django import forms
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{9,15}$',
    message='Введите корректный номер телефона.'
)


class ReservationForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Ваше имя'
            }
        ),
    )
    phone = forms.CharField(
        required=True,
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Ваш номер телефона без пробелов'
            }
        ),
    )
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Доп. ниформация'
            }
        ),
    )

    tool_name = forms.CharField(widget=forms.HiddenInput(), required=False)


class FeedbackForm(ReservationForm):
    pass
