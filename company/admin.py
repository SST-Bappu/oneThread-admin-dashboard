from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(company)
admin.site.register(project)
admin.site.register(member)
admin.site.register(subscription)