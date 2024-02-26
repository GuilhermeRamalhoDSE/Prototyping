from django.urls import path
from prototyping.api.license_api import api as license_api

urlpatterns = [
    path('api/', license_api.urls)
]
