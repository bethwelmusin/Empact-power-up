from django.db import models
from django.contrib.auth.models import User
import uuid

from utilities.choices import MEMBER_TYPE,USER_ROLES
# Create your models here.

class EmpactUser(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        User, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(db_column='firstname', max_length=50,null=False, blank=False)
    last_name = models.CharField(db_column='lastname', max_length=50,null=False, blank=False)
    mobile_number = models.CharField(max_length=13)
    email = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False, default='Kenya')
    profile_pic_url = models.CharField(max_length=100, null=True, blank=True)
    member_type = models.CharField(
        max_length=100, choices=MEMBER_TYPE, default='Community')
    user_type = models.CharField(
        max_length=100, choices=USER_ROLES, default='EmpactUser')
    updated_on = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.first_name} - {}'

    def __unicode__(self):
        return 
