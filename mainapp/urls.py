from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import CatalogListView, SubCatalogListView, ToolListView, ToolDetailView, ContactView, AboutUsView


app_name = MainappConfig.name


urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('catalog/<int:category_id>/', SubCatalogListView.as_view(), name='category'),
    path('catalog/<int:category_id>/<int:subcategory_id>/', ToolListView.as_view(), name='subcategory'),
    path('catalog/<int:category_id>/<int:subcategory_id>/<int:pk>', ToolDetailView.as_view(), name='tool'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
