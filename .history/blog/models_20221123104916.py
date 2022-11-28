from django.db import models

# Create your models here.
class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
