from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('catalog/', views.CatalogListView.as_view()),
    path('about_us/', views.AboutUsView.as_view()),
    path('sub_catalog/', views.SubCatalogListView.as_view())
]
