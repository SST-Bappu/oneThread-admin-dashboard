from django.urls import path
from .views import *

urlpatterns = [
    path('getcompanies/',CompanyAPIView.as_view(),name='getcompanies'),
    path('company/',companies,name='company'),
]
