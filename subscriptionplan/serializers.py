from rest_framework import serializers
from .models import *
class subsSerializer(serializers.ModelSerializer):

    class Meta:
        model = plan
        fields = ['name','maxTier','description','region','currency','pricing','validity','version']
