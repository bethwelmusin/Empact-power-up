from django.db import models
import uuid

# Create your models here.


class Community(models.Model):
    community_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    community_name = models.CharField(max_length=100, )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Communities"
        odering = "created_at"
    

    def __str__(self):
        return f'{self.}'

    def __unicode__(self):
        return 
