from django.db import models

# Create your models here.

class EmpactUser(models.Model):
    id = models.CharField(
        primary_key=True, default='', editable=False, unique=True, max_length=200)
    user = models.OneToOneField(
        User, db_column='user_id', null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(db_column='firstname', max_length=50,null=True, blank=True)
    last_name = models.CharField(db_column='lastname', max_length=50,null=True, blank=True)
    mobile_number = models.CharField(max_length=13)
    email = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(
        max_length=100, choices=USER_TYPE_CHOICES, default='Client')
    updated_on = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
