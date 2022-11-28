from django.db import models
from authentication.models

# Create your models here.
class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False,null=False)
    body = models.TextField(blank=False,null=False)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
