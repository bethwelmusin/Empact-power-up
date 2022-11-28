from django.db import models
import uuid
from app.utilities.choices import PROJECT_STATUS_CHOICES
from authentication.models import EmpactUser

# Create your models here.


class Community(models.Model):
    community_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    community_name = models.CharField(max_length=100, )
    community_description = models.CharField(max_length=400, )  
    country = models.CharField(max_length =50, default='Kenya')
    members = models.ForeignKey(EmpactUser, related_name='community', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Communities"
        odering = "created_at"
    

    def __str__(self):
        return f'{self.community_name}'

    def __unicode__(self):
        return 

class Project(models.Model):
    project_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    project_name = models.CharField(max_length=100, )   
    project_description = models.CharField(max_length=400, )   
    project_coodinator =models.one(EmpactUser, related_name='community', on_delete=models.CASCADE)   
    project_status = models.CharField(
        max_length=10, choices=PROJECT_STATUS_CHOICES, default='Running') 
    lifes_impacted = models.CharField(
        max_length=20, null=True, blank=True) 
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        odering = "created_at"
    

    def __str__(self):
        return f'{self.community_name}'

    def __unicode__(self):
        return 

