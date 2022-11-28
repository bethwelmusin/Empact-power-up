from django.db import models
import uuid
from authentication.models import EmpactUser

# Create your models here.


class Community(models.Model):
    community_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    community_name = models.CharField(max_length=100, )
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


