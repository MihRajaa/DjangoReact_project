from django.urls import path, re_path
from .views import article_list

urlpatterns = [
    path('', article_list)
]