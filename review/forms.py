from django import forms

from review.models import Review


class ReviewForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Ваше имя'
            }
        ),
    )
    review = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'Отзыв о сервисе'
            }
        ),
    )

    class Meta:
        model = Review
        fields = ('name', 'review')
