from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView

from telegram.views import send_telegram_message

from mainapp.models import Category, SubCategory, Tool
from common.views import TitleMixin
from mainapp.forms import ReservationForm, FeedbackForm
from config import settings
from common.common_variable import CONTACTS, TG_CHAT_ID


class IndexView(TitleMixin, TemplateView):
    template_name = 'mainapp/index.html'
    title = 'Аренда инструмента'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['contacts'] = CONTACTS
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Инструмент'
        return context


class ContactView(TitleMixin, TemplateView):
    template_name = 'mainapp/contacts.html'
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['title'] = 'Контакты'
        context['contacts'] = CONTACTS
        context['disable_footer'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = {
                    'chat_id': TG_CHAT_ID,
                    'text': f"""Клиент: {form.cleaned_data["name"]} ждёт звонка"""
                            f"""\nТелефон: {form.cleaned_data["phone"]}"""
                            f"""\nДоп. информация: {form.cleaned_data["text"]}"""
                }
            if send_telegram_message(data):
                messages.success(request, f'{form.cleaned_data["name"]}, мы свяжемся с вами в ближайшее время.')
            else:
                messages.error(request, 'Что-то пошло не так, попробуйте ещё раз')
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class ReservationView(TemplateView):
    template_name = 'mainapp/reservation.html'
    form_class = ReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        tool_name = self.kwargs.get('tool_name')
        context['tool_name'] = tool_name
        context['title'] = 'Бронирование'

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = {
                    'chat_id': TG_CHAT_ID,
                    'text': f"""Бронирование: {form.cleaned_data['tool_name']}\nИмя: {form.cleaned_data["name"]}"""
                            f"""\nТелефон: {form.cleaned_data["phone"]}"""
                            f"""\nДоп. информация: {form.cleaned_data["text"]}"""
                }

            if send_telegram_message(data):
                messages.success(request, 'Мы свяжемся с вами в ближайшее время.')
            else:
                messages.error(request, 'Что-то пошло не так, попробуйте ещё раз')
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
