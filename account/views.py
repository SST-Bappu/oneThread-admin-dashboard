from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.generics import GenericAPIView,RetrieveAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import jwt
from .form import SignUpForm
from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from django.contrib import messages
import requests
import json
import os
from django.core.paginator import Paginator, EmptyPage
from django.core import serializers


User= auth.get_user_model()
# Create your views here.



# @permission_classes([AllowAny])
def signup(request):
    form = SignUpForm
    return render(request,'signup.html',{'form':form})

# @permission_classes([AllowAny])
def signin(request):
    return render(request,'onlogin.html')

def UserLogout(request):
    auth.logout(request)
    return redirect('login')
   
        

class RegisterView(GenericAPIView):
    permission_classes([AllowAny])
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(request,username=username, password=password)
        print(user)
        if user:
            auth_token = jwt.encode(
                {'username': username}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}
            auth.login(request,user)
            name = request.user.first_name
            name = (''+name[:2]).upper()
            return render(request, 'dashboard/main.html',{'username':name}, status=status.HTTP_200_OK)

            # SEND RES
        else:
            messages.info(request, "Username or Password is incorrect!")
            return render(request,'onlogin.html')

        #return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@login_required(login_url='login')
def allUsers(request):
    data = open(os.path.join(settings.BASE_DIR,'accounts.json'))
    users = data.read()
    users = json.loads(users)
    # User = auth.get_user_model()
    # users = User.objects.all()
    page_num = request.GET.get('page') or 1
    pages = Paginator(users,10)
    try:
        page = pages.page(page_num)
    except EmptyPage:
        page = pages.page(1)
    user = request.user.first_name
    user = (''+user[:2]).upper()
    return render(request,'dashboard/users/users.html', {'users':page,'link':'allusers','username':user})

@login_required(login_url='login')
def VerifiedUsers(request):
    data = open(os.path.join(settings.BASE_DIR,'accounts.json'))
    users = data.read()
    users = json.loads(users)
    ver_users = []
    for user in users:
        if user['isAccountVerified']==True:
            ver_users.append(user)
    page_num = request.GET.get('page') or 1
    pages = Paginator(users,10)
    try:
        page = pages.page(page_num)
    except EmptyPage:
        page = pages.page(1)
    
    user = request.user.first_name
    user = (''+user[:2]).upper()
    return render(request,'dashboard/users/VerifiedUsers.html', {'users':users,'link':'verusers','username':user})

@login_required(login_url='login')
def UnVerifiedUsers(request):
    data = open(os.path.join(settings.BASE_DIR,'accounts.json'))
    users = data.read()
    users = json.loads(users)
    ver_users = []
    for user in users:
        if user['isAccountVerified']==False:
            ver_users.append(user)
    page_num = request.GET.get('page') or 1
    pages = Paginator(ver_users,10)
    try:
        page = pages.page(page_num)
    except EmptyPage:
        page = pages.page(1)

    user = request.user.first_name
    user = (''+user[:2]).upper()
    return render(request,'dashboard/users/UnverifiedUsers.html', {'users':page,'link':'unverusers','username':user})


@login_required(login_url='login')
def userGrowth(request):
    user = request.user.first_name
    user = (''+user[:2]).upper()
    return render(request,'dashboard/users/userGrowth.html',{'username':user})