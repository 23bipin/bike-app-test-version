# django_project/urls.py

from django.contrib import admin
from django.urls import path, include
from bikes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("bikes.urls")),
]
