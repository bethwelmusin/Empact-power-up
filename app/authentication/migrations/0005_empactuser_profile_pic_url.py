# Generated by Django 4.0.5 on 2022-11-12 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_empactuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='empactuser',
            name='profile_pic_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
