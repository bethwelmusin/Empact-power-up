# Generated by Django 4.0.5 on 2022-11-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_empactuser_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='empactuser',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('EmpactUser', 'EmpactUser')], default='EmpactUser', max_length=100),
        ),
    ]
