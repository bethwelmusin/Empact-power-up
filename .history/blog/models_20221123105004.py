from django.db import models

# Create your models here.
class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False,null=)
    body = models.TextField(blank=False,null=)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
