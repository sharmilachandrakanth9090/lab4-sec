"""
Modified by : Sharmila Chandrakanth
Modified date : feb-24-2019
File name : Urls.py
"""
from django.urls import path
from .views import ListSongsView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
