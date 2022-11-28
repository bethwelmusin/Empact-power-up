from django.db import models

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField()
    title = models.CharField(max_length=100, blank=False,null=False)
    body = models.TextField(blank=False,null=False)
    owner = models.ForeignKey('EmpactUser', related_name='posts', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
