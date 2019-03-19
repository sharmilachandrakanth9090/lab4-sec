from django.urls import path
from .views import ListPilotView


urlpatterns = [
    path('pilots/', ListPilotView.as_view(), name="pilots-all")
]
