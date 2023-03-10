from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from common.views import TitleMixin
from review.models import Review
from review.forms import ReviewForm


class ReviewView(TitleMixin, SuccessMessageMixin, FormView):
    template_name = 'review/review_list.html'
    title = 'Аренда инструмента - Отзывы'
    success_message = '%(name)s, Ваш отзыв будет добавлен после проверки.'
    form_class = ReviewForm
    success_url = reverse_lazy('review:reviews')

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews.filter(is_verified=True)
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        review = form.cleaned_data['review']
        Review.objects.create(name=name, review=review)
        return super().form_valid(form)
