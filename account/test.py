from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model
def loader(user):    
    users = get_user_model()
    user = users.objects.create(email = user['email'],
                                password='p@ssw@rd1234',
                                first_name=user['firstName'],
                                last_name=user['lastName'],
                                contactNo = user['contactNo'],
                                username = user['name'],
                                isVerified= user['isAccountVerified'],
                                )
    user.save()
    print(user)