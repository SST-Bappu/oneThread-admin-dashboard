from datetime import datetime
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class report(models.Model):
    class status_type(models.TextChoices):
        Solved = 'Solved',
        Pending = 'Pending'
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    issuetype = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    issuedetails = models.CharField(max_length=500)
    imageurl = models.CharField(max_length=500)
    created_at = models.DateTimeField(default= datetime.now)
    status = models.CharField(max_length=10,choices=status_type.choices,default='Pending')
    def __str__(self):
        return self.title