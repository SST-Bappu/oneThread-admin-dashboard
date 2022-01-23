from rest_framework import serializers
from .models import *
class reportSerializer(serializers.ModelSerializer):
    # accountName = serializers.SerializerMethodField('_get_account')
    # def _get_account(self,object):
    #     account = getattr(object,"account")
    #     return account.name
    class Meta:
        model = report
        fields = ['issuetype','title','issuedetails','imageurl','status','created_at']
