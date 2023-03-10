from django.contrib import admin
from mainapp.models import Category, SubCategory, Tool
from review.models import Review


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tool)
admin.site.register(Review)
