from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from common.common_variable import TG_CHAT_ID

from common.views import TitleMixin
from review.models import Review
from review.forms import ReviewForm
from telegram.views import send_telegram_message


class ReviewView(TitleMixin, SuccessMessageMixin, FormView):
    template_name = 'review/review_list.html'
    title = 'Аренда инструмента - Отзывы'
    success_message = '%(name)s, Ваш отзыв будет добавлен после проверки.'
    form_class = ReviewForm
    success_url = reverse_lazy('review:reviews')

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        reviews = Review.objects.all()
        paginator = Paginator(reviews.filter(is_verified=True), 3)  # 3 - количество отзывов на одной странице
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['reviews'] = page_obj
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        review = form.cleaned_data['review']
        data = {
                    'chat_id': TG_CHAT_ID,
                    'text': f"""Оставлен отзыв от: {name}"""
                            f"""\nТекст отзыва: {review}"""
                            f"""\nЗайдите в админку,чтоб подтвердить его"""
                }
        send_telegram_message(data)
        Review.objects.create(name=name, review=review)
        return super().form_valid(form)
