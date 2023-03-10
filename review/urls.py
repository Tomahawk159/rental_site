from django.urls import path

from review.views import ReviewView


app_name = 'review'

urlpatterns = [
    path('reviews/', ReviewView.as_view(), name='reviews'),
]
