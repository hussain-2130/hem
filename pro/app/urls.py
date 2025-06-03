from django.contrib import admin
from django.urls import path,include
from .views import create_ticket
urlpatterns = [
    path("admin/", admin.site.urls),
    path("abc/",create_ticket)
]
