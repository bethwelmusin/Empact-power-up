from django.db import models
import uuid
from app.utilities.choices import PROJECT_STATUS_CHOICES,MEDIA_FILE_TYPE_CHOICES
from authentication.models import EmpactUser
from django.db.models import Count

# Create your models here.


class Community(models.Model):
    community_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    community_admin = models.OneToOneField(EmpactUser, related_name='community', on_delete=models.DO_NOTHING)
    community_name = models.CharField(max_length=100, )
    verified = models.BooleanField(default=True)
    community_description = models.CharField(max_length=400, )  
    country = models.CharField(max_length =50, default='Kenya')
    members = models.ForeignKey(EmpactUser, related_name='community', on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Communities"
        odering = "created_at"

    def membersCount(self):
        members = EmpactUser.objects.annotate(members_count = Count('community'))
        member_count = members[self].members_count
        return member_count

    def projectsCount(self):
        projects = Project.objects.count(commuinty__community_id)
    

    def __str__(self):
        return f'{self.community_name}'

    def __unicode__(self):
        return 

class Project(models.Model):
    project_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    project_name = models.CharField(max_length=100, )   
    project_description = models.CharField(max_length=400, )   
    project_coodinator =models.OneToOneField(EmpactUser, related_name='project', on_delete=models.DO_NOTHING)  
    commuinty = models.ForeignKey('Community', related_name='project', on_delete=models.CASCADE) 
    project_status = models.CharField(
        max_length=10, choices=PROJECT_STATUS_CHOICES, default='Running') 
    lifes_impacted = models.CharField(
        max_length=20, null=True, blank=True) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        odering = "start_date"
    

    def __str__(self):
        return f'{self.project_name} - {self.project_coodinator}'

    def __unicode__(self):
        return 

class CommunityMedia(models.Model):
    commuinty = models.ForeignKey('Community', related_name='project', on_delete=models.CASCADE) 
    media_file = models.CharField(max_length=400, )  
    media_type = models.CharField(max_length=10, choices=MEDIA_FILE_TYPE_CHOICES, default='Image')  
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 

    def __unicode__(self):
        return 


class CommunityComment(models.Model):
    comment_id=models.AutoField(primary_key=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,)
    show = models.BooleanField(default=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(EmpactUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Community', related_name='comments', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=300, blank=True,null=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return f'{self.post} - {self.body}'