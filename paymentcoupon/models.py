from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class paymentCoupon(models.Model):
    code = models.CharField(max_length=40,unique=True)
    active = models.BooleanField(default=True)
    company = models.ForeignKey('company.company',related_name='ref_coupon',on_delete=models.CASCADE)
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.code