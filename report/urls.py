from django.urls import path
from .views import *

urlpatterns = [
    path('',reportAPI.as_view(),name='report'),
    path('getreport/',get_report,name='getreport'),
]