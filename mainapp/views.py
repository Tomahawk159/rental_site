from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from mainapp.models import *
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'mainapp/index.html'
    title = 'Аренда инструмента'


class CatalogListView(TitleMixin, ListView):
    model = Category
    template_name = 'mainapp/catalog.html'
    title = 'Каталог'


class ContactView(TitleMixin, TemplateView):
    template_name = 'mainapp/contact.html'
    title = 'Контакты'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/?um=constructor%3A2c34e08a01345d2486370b7a37c0c6b0e13b34a695f0dbe0bfea7603d1d63826&amp;source=constructor',
                'city': 'Пермь',
                'phone': '+7-999-11-11111',
                'email': 'perm@mail.ru',
                'adress': 'ул. Ленина 10'
            }
        ]
        return context


class AboutUsView(TitleMixin, TemplateView):
    template_name = 'mainapp/about_us.html'
    title = 'О нас'


class SubCatalogListView(ListView):
    model = SubCategory
    template_name = 'mainapp/sub_catalog.html'
