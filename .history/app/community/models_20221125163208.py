from django.db import models

# Create your models here.


class Community(models.Model):
    community_name = models.CharField(max_length)


    class Meta:
        verbose_name_plural = "Communities"
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
