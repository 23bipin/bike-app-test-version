# bikes/urls.py
from django.views.generic import TemplateView
from django.urls import path
from . import views
from .views import datatable, HomePageView, SearchPageView, datatable
from . import models

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("datatable/", datatable, name="datatable"),
    path("search/", SearchPageView.as_view(), name="search"),
    # path("maps/", MapsPageView.as_view(), name="maps"),
]
