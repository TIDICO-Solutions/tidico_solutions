# Generated by Django 2.0.1 on 2018-01-29 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0023_auto_20180126_2005'),
        ('e_reg', '0017_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
