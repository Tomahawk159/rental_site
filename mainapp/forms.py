from django import forms

from aiogram import Bot
from telegram.config_data.config import config


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
        widget=forms.TextInput(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Ваш номер телефона'
            }
        ),
    )
    text = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Доп. ниформация'
            }
        ),
    )

    async def send_telegram_message(self):
        print('pltcm')
        bot = Bot(token=config.tg_bot.token)
        message = f'Имя: {self.cleaned_data["name"]}\nТелефон: {self.cleaned_data["phone"]}\nДоп. информация: {self.cleaned_data["text"]}'
        await bot.send_message(chat_id=1730221801, text=message)
