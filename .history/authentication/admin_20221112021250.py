from django.contrib import admin

# Register your models here.
from authentication.models import EmpactUser

admin.site.register(EmpactUser)