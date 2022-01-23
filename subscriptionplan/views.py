from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from django.core import serializers
from rest_framework.renderers import JSONRenderer

from .models import plan
from .serializers import subsSerializer
from company.models import company

# Create your views here.
class planAPI(APIView):
    def post(self,request):
        companyId = request.headers.get('Companyid')
        Payingcompany = company.objects.get(id=companyId)
        data = request.data
        new_plan=plan.objects.create(
            name=data['name'],
            maxTier = data['maxTier'],
            description = data['description'],
            region = data['region'],
            currency = data['currency'],
            pricing = data['pricing'],
            company = Payingcompany
        )
        new_plan.save()
        serializer=subsSerializer([new_plan],many=True)
        data = list(serializer.data)
        return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        