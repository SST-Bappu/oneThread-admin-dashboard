import code
from rest_framework import serializers
from .models import *
class couponSerializer(serializers.ModelSerializer):
    companyName = serializers.SerializerMethodField('_get_company')
    def _get_company(self,object):
        company = getattr(object,"company")
        return company.name

    class Meta:
        model = paymentCoupon
        fields = ['id','code','companyName']