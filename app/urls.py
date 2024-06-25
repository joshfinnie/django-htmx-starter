"""
URL configuration for app project.
"""
from django.contrib import admin
from django.urls import path, include

from app.views import index

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    #path("users/", include("users.urls")),
]
