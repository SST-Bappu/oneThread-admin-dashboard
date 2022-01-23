from django.urls import path
from .views import *

urlpatterns = [
    path('',planAPI.as_view(),name='planapi'),
]
