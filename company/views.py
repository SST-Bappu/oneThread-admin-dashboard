from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage
import json
import os
from django.contrib.auth.decorators import login_required
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializer import companySerializer
from .models import company
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import requests
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated

from django.db.models import Value,CharField
from django.db.models.functions import Lower, Replace
CharField.register_lookup(Lower)
# Create your views here.

class CompanyAPIView(APIView):
    serializer_class = companySerializer
    permission_classes = (AllowAny,)
    def get(self,request):
        data = company.objects.all()
        serialized_data = self.serializer_class(data,many=True)
        companies = list(serialized_data.data)
        return JsonResponse(companies, safe=False,status=status.HTTP_200_OK)
    
    def put(self,request):
        search = request.query_params['search']
        # data = company.objects.annotate(
        #     mod_name = Lower(Replace('name',Value(' '),Value('')))
        # ).filter(mod_name=search)

        # data = company.objects.filter(name__unaccent__lower__trigram_similar=search)
        data = company.objects.filter(name__icontains=search)
        serialized_data = self.serializer_class(data,many=True)
        companies = list(serialized_data.data)
        return JsonResponse(companies,safe=False,status=status.HTTP_302_FOUND)
        
    

@login_required(login_url='login')
def companies(request):
    if request.POST:
        body = request.body.decode('utf-8').replace("'", '"')
        body = body.split('&')
        body = body[1].split('=')
        search = body[1]
        search = search.replace(' ','')
        data = requests.put(f'http://localhost:8000/getcompanies/?search={search}')
    else:
        data = requests.get('http://localhost:8000/getcompanies')
    data = data.content.decode('utf8').replace("'", '"')
    data = json.loads(data)
    total_companies = len(data)
    page_num = request.GET.get('page') or 1
    pages = Paginator(data,5)
    try:
        page = pages.page(page_num)
    except EmptyPage:
        page = pages.page(1)
    user = request.user.first_name
    user = (''+user[:2]).upper()
    
    return render(request,'dashboard/company/company.html', {'companies':page,'username':user,'total_companies':total_companies})



