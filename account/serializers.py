
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=150, min_length=2)
    last_name = serializers.CharField(max_length=150, min_length=2)
   
    # username = serializers.SerializerMethodField('_get_username')
    # def _get_username(self,user_object):
    #     mail = getattr(user_object,"email")
    #     return mail


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('There is already an account with this email')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),

    class Meta:
        model = User
        fields = ['email', 'password']


class retrieveUserSerializer(serializers.ModelSerializer):
    
    is_verified = serializers.SerializerMethodField('_get_user')
    def _get_user(self,user_object):
        Verified = getattr(user_object,"isVerified")
        return 1 if Verified==True else 0

    class Meta:
        model = User
        fields = ['first_name','email','birthDate','createdAt','is_verified']

