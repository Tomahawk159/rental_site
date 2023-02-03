from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from mainapp.models import *


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class CatalogView(TemplateView):
    template_name = 'mainapp/catalog.html'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


class AboutUsView(TemplateView):
    template_name = 'mainapp/about_us.html'
