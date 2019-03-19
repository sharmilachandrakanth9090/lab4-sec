from rest_framework import generics
from .models import Pilot
from .serializers import PilotSerializer


class ListPilotView(generics.ListAPIView):
    """
    Provides a get method handler
    """
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
