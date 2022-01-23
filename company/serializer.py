from rest_framework import serializers
from .models import *
class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        # fields = ['__all__']
        fields = ['name','uniqueName','collegues','projects','Subs_activation','subs_expireDate','created_at']
