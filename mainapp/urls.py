from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import ContactView, CatalogListView, AboutUsView, SubCatalogListView


app_name = MainappConfig.name


urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('sub_catalog/', SubCatalogListView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
