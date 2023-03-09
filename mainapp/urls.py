from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import (
    CategoryListView,
    SubCategoryListView,
    ToolListView,
    ToolDetailView,
    ContactView,
)


app_name = MainappConfig.name


urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('catalog/', CategoryListView.as_view(), name='catalog'),
    path('catalog/<int:category_id>/',
         SubCategoryListView.as_view(), name='category'),
    path('catalog/<int:category_id>/<int:subcategory_id>/',
         ToolListView.as_view(), name='subcategory'),
    path('catalog/<int:category_id>/<int:subcategory_id>/<int:pk>',
         ToolDetailView.as_view(), name='tool'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
