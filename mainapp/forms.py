from django import forms


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

    tool_name = forms.CharField(widget=forms.HiddenInput(), required=False)


class FeedbackForm(ReservationForm):
    pass
    # name = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'mb-3 form-control',
    #             'placeholder': 'Ваше имя'
    #         }
    #     ),
    # )
    # phone = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'mb-3 form-control',
    #             'placeholder': 'Ваш номер телефона'
    #         }
    #     ),
    # )
    # text = forms.CharField(
    #     required=True,
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'mb-3 form-control',
    #             'placeholder': 'Доп. ниформация'
    #         }
    #     ),
    # )
