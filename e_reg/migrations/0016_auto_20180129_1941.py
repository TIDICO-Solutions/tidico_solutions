# Generated by Django 2.0.1 on 2018-01-29 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0015_remove_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
