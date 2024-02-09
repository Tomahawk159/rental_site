import random
# from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView

# from aiogram import Bot
# from telegram.config_data.config import config

from mainapp.models import Category, SubCategory, Tool
from review.models import Review
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'mainapp/index.html'
    title = 'Аренда инструмента'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        reviews = Review.objects.filter(is_verified=True)
        context['reviews'] = random.sample(
            list(reviews), 3) if len(reviews) >= 3 else []
        return context


class CategoryListView(TitleMixin, ListView):
    model = Category
    template_name = 'mainapp/catalog.html'
    title = 'Каталог'


class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'mainapp/sub_catalog.html'

    def get_context_data(self, **kwargs):
        context = super(SubCategoryListView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        name = Category.objects.get(id=category_id).name
        context['title'] = f'Каталог - {name}'
        return context

    def get_queryset(self):
        queryset = super(SubCategoryListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category=category_id) if category_id else queryset


class ToolListView(ListView):
    model = Tool
    template_name = 'mainapp/tools.html'

    def get_context_data(self, **kwargs):
        context = super(ToolListView, self).get_context_data(**kwargs)
        subcategory_id = self.kwargs.get('subcategory_id')
        name = SubCategory.objects.get(id=subcategory_id).name
        context['title'] = f'Каталог - {name}'
        return context

    def get_queryset(self):
        queryset = super(ToolListView, self).get_queryset()
        subcategory_id = self.kwargs.get('subcategory_id')
        return queryset.filter(subcategory=subcategory_id) if subcategory_id else queryset


class ToolDetailView(DetailView):
    model = Tool
    template_name = 'mainapp/tool.html'


class ContactView(TitleMixin, TemplateView):
    template_name = 'mainapp/contacts.html'
    title = 'Контакты'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = [
            {
                'map': """https://yandex.ru/map-widget/v1/"""
                       """?um=constructor%3A2c34e08a01345d2486370b7a37c0c6b0e13b34a695f0dbe0bfea7603d1d63826&amp;"""
                       """source=constructor""",
                'city': 'Пермь',
                'phone': '+7-999-11-11111',
                'email': 'perm@mail.ru',
                'adress': 'ул. Ленина 10'
            }
        ]
        return context


class ReservationView(TitleMixin, TemplateView):
    template_name = 'mainapp/reservation.html'
    title = 'Бронирование инструмента'


# async def send_booking_message(request):
#     bot = Bot(token=config.tg_bot.token)
#     await bot.send_message(chat_id=1730221801, text='Бронь')
#     return HttpResponse('Сообщение отправлено в чат телеграм-бота')
