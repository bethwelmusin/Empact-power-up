# Generated by Django 4.0.5 on 2022-11-25 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_rename_community_project_commuinity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='commuinity',
            new_name='community',
        ),
    ]
