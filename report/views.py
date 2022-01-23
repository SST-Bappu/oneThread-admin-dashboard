from email import message
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from django.core import serializers
from rest_framework.renderers import JSONRenderer
import requests

from .models import report
from .serializers import reportSerializer
# Create your views here.
class reportAPI(APIView):
    def post(self,request):
        data = request.data
        newReport = report.objects.create(
            account = request.user,
            issueType = data['issueType'],
            title = data['title'],
            issueDetails = data['issueDetails'],
            imageUrl = data['imageUrl']
        )
        newReport.save()
        data = reportSerializer([newReport],many=True)
        data = list(data.data)
        return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
    def get(self,request):
        data = report.objects.all()
        # data = reportSerializer([data],many=True)
        # data = list(data.data)
        return data
        
        # return JsonResponse({'data':'analyzing'}, safe=False,status=status.HTTP_200_OK)

def get_report(request):
    data = requests.get('http://localhost:8000/report')
    print(data)
    user = request.user.first_name
    user = (''+user[:2]).upper()
    return render(request,'dashboard/company/company.html', {'reports':data,'username':user})
    



