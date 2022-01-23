from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from django.core import serializers


from company.models import company
from .models import paymentCoupon
from .serializers import couponSerializer
import uuid
# Create your views here.

class CouponAPI(APIView):
    def post(self,request):
        # try:
        companyId = request.headers.get('Companyid')
        Payingcompany = company.objects.get(id=companyId)
        newCoupon = paymentCoupon.objects.create(
            code = str(uuid.uuid4()).replace("-","")[:12],
            company = Payingcompany
        )
        newCoupon.save()
        data = couponSerializer([newCoupon],many=True)
        data = list(data.data)
        return JsonResponse(data, safe=False,status=status.HTTP_200_OK)

        # except:
        #     return JsonResponse({'message':'companyId is required'},safe=False,status=status.HTTP_400_BAD_REQUEST)
