from django.db import models

# Create your models here.


class Community(models.Model):
    community_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    community_name = models.CharField(max_length=100, )


    class Meta:
        verbose_name_plural = "Communities"
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
