# Generated by Django 4.0.5 on 2022-11-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empactuser',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
