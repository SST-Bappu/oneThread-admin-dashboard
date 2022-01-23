from django.urls import path
from .views import *

urlpatterns = [
    path('',signin,name='login'),
    path('logout',UserLogout,name='logout'),
    path('signup', RegisterView.as_view(),name='signup'),
    path('home', LoginView.as_view(),name='home'),
    path('allusers',allUsers,name='allusers'),
    path('verusers',VerifiedUsers,name='verusers'),
    path('unverusers',UnVerifiedUsers,name='unverusers'),
    path('usergrowth',userGrowth,name='usergrowth'),
]
