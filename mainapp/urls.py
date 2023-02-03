from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('catalog/', views.CatalogView.as_view()),
    path('about-us/', views.AboutUsView.as_view())
]
