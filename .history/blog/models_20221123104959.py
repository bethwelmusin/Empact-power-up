from django.db import models

# Create your models here.
class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, )
    body = models.TextField(blank=False, )
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 