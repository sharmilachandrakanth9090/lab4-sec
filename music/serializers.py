"""
Modified by : Sharmila Chandrakanth
Modified date : feb-24-2019
File name : serializers.py
"""
from rest_framework import serializers
from .models import Songs


class SongsSerializer(serializers.ModelSerializer):
    """
    This class will have the the fields for the music application
    which includes  
    """
    class Meta:
        model = Songs
        fields = ("title", "artist")
