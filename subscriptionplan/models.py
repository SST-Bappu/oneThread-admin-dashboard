from django.db import models

# Create your models here.
class plan(models.Model):
    class name_type(models.TextChoices):
        trial = 'Trial'
        enterprise =  'Enterprise'
        Workspaces = 'Workspaces'
    class regions(models.TextChoices):
        BD = 'BD'
        General = 'GENERAL'
    class currency_type(models.TextChoices):
        BDT = 'BDT'
        USD = 'USD'
    name= models.CharField(max_length=15,choices=name_type.choices)
    maxTier= models.IntegerField()
    description = models.CharField(max_length=200)
    region = models.CharField(max_length=15,choices=regions.choices)
    currency = models.CharField(max_length=5,choices=currency_type.choices)
    pricing = models.IntegerField()
    validity = models.IntegerField(default=30)
    company = models.ForeignKey('company.company',related_name='companysubs',on_delete=models.CASCADE)
    version = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
        
    