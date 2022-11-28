from django.db import models
from authentication.models import EmpactUser

from utilities.choices import POST_STATUS_CHOICES

# Create your models here.

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(status='published')
# class AllUserPostsManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(owner_id=)
class Post(models.Model):
    post_id = models.AutoField(primary_key=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False,null=False)
    image_url = models.CharField(max_length=300, blank=False,null=False)
    body = models.TextField(blank=False,null=False)
    # published = PublishedManager()
    # all_posts = AllUserPostsManager()
    status = models.CharField(
        max_length=10, choices=POST_STATUS_CHOICES, default='draft')
    owner = models.ForeignKey(EmpactUser, related_name='posts', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created_at']
    

    def __str__(self):
        return f'{self.title} - {self.owner}'

    def __unicode__(self):
        return 


class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, default=DateTime)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(EmpactUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=300, blank=True,null=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return f'{self.post} - {self.body}'