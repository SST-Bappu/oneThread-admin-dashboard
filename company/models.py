from typing import Optional
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from datetime import timedelta
from django.utils import timezone
import datetime
# Create your models here.

class company(models.Model):

    class company_type(models.TextChoices):
        Manufacturer = 'Manufacturer'
        Trading_Company =  'Trading Company'
        Buying_Office = 'Buying Office'
        Agent = 'Agent'
        Distri =  'Distributor/Wholesaler'
        Gover =  'Government ministry/Bureau/Commission'
        Assoc = 'Association'
        Business =  'Business Service (Transportation, finance, travel, Ads, etc)'
        other = 'other'
    
    class optional_role(models.TextChoices):
        editProfile = 'editProfile'
        cRUD ='cRUDAnnouncement'
        archive ='archiveProject'
        addRemove ='addRemoveModerator'
        message = 'messageAssociate'
        addAccept ='addAcceptRejectAssociate'
        acceptRej = 'acceptRejectProjectFromAssociate'

    class total_employee(models.TextChoices):
        Fewer = 'Fewer than 5 People'
        five = '5 - 10 People'
        eleven = '11 - 50 People'
        fifty = '51 - 100 People'
        hundred = '101 - 200 People'
        two_hundred = '201 - 300 People'
        three_hundred = '301 - 500 People'
        five_hundred = '501 - 1000 People'
        Above = 'Above 1000 People'
    class office_size(models.TextChoices):
        below = 'below 100 square meters'
        hundred = '101 - 500 square meters'
        five_hundred = '501 - 1000 square meters'
        one_thousand = '1001 -2000 square meters'
        above = 'above 2000 square meters'
    image = models.ImageField(null=True,blank=True)
    coverImage = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=32, unique=True)
    uniqueName = models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=60, choices=company_type.choices,default=company_type.other)
    optionalRole = models.CharField(max_length=50,choices=optional_role.choices)
    address = models.CharField(max_length=120)
    about = models.CharField(max_length=2000)
    email = models.EmailField(max_length=255)
    legalOwnerName = models.CharField(max_length=30)
    legalOwnerMail = models.EmailField(max_length=255)

    #products = =>This has to be a reference to the project table

    account = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=120,blank=True)
    websites = models.CharField(max_length=50,blank=True)

    #departments =  =>This has to be a reference to the department table
    
    regisTrationYear = models.DateField()
    totalEmployees = models.CharField(max_length=30,choices=total_employee.choices)
    officeSize = models.CharField(max_length=30,choices=office_size.choices)
    parentcom = models.CharField(max_length=30)
    removed = models.BooleanField(default=0)
    create_at = models.DateField(auto_now=True)
    @property
    def collegues(self):
        colg = self.member_set.all().count()
        return colg
    
    @property
    def projects(self):
        proj = self.project_set.all().count()
        return proj
    @property
    def Subs_activation(self):
        subs = self.subscription
        return subs.isActive
    @property
    def subs_expireDate(self):
        subs = self.subscription
        return subs.expireAt
    @property
    def created_at(self):
        date = str(self.create_at)
        # date = date.split['T']
        return date

    def __str__(self):
        return self.name

class member(models.Model):

    class member_role(models.TextChoices):
        superAdmin = 'superAdmin'
        admin = 'admin'
        employee ='employee'

    account = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comp_member')
    company = models.ForeignKey(company,on_delete=models.CASCADE)
    role = models.CharField(max_length=15,choices = member_role.choices,default=member_role.employee)
    
    designations = models.CharField(max_length=20,blank=True) #This has to be a reference to the designation model

    removed = models.BooleanField(default=0)
    isApproved = models.BooleanField(default=0)
    approvedBy = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.account.first_name

#function to set default deadline to the project
def one_month_from_today():
    return timezone.now() + timedelta(days=30)

class project(models.Model):
    class optional_role(models.TextChoices):
            updateArchiveProject = 'updateArchiveProject'
            updateProjectPreface = 'updateProjectPreface'
            addFileProject =  'addFileProject'
            addRemoveMemberRoom =  'addRemoveMemberRoom'
            createUpdateRoom = 'createUpdateRoom'
            archiveRoom = 'archiveRoom'
            createUpdateBoard = 'createUpdateBoard'
            createUpdateColumn = 'createUpdateColumn'
            assignDeleteMemberBoard = 'assignDeleteMemberBoard'
    
    name = models.CharField(max_length=50)
    descriiption = models.CharField(max_length=2500, blank=True)
    outline = models.CharField(max_length=5000,blank=True)
    deadline = models.DateField(default=one_month_from_today,blank=True)
    color = models.IntegerField(default=0,blank=True)
    status = models.CharField(max_length=30,default='not-started')
    concernedAdmin = models.ForeignKey(member,on_delete=models.CASCADE)
    OptionalRole = models.CharField(max_length=30,default=None,choices=optional_role.choices)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    
    #departments = models.CharField(blank=True) #This has to be a reference to the department model

    files = models.FileField(blank=True)

    #roooms = models.ForeignKey() #This has to be a reference to the room model

    company = models.ForeignKey(company,on_delete=models.CASCADE)
    timeSpent = models.IntegerField(default=0)
    budget = models.IntegerField(blank=True)
    currency = models.CharField(max_length = 15, blank=True)
    version = models.IntegerField(default=0)
    removed = models.BooleanField(default=0)

    #associate = ->This has to be a reference to the associate model

    def __str__(self):
        return self.name

def one_year_from_today():
    return timezone.now() + timedelta(days=365)
class subscription(models.Model):
    company = models.OneToOneField(company,on_delete=models.CASCADE)
    
    #plan = models. => This has to be a reference to the plan table

    expireAt = models.DateField(default=one_year_from_today)
    isActive = models.BooleanField(default=0)
    version = models.IntegerField(default=0)

    def __str__(self):
        return self.company.name