from django.urls import path
from .views import *

urlpatterns = [
    path('',CouponAPI.as_view(),name='coupon'),
]
