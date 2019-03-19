"""
Modified by : Sharmila Chandrakanth
Modified date : feb-24-2019
File name : views.py
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

# Create your views here.
