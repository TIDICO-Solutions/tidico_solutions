# Generated by Django 2.0.1 on 2018-01-27 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0014_auto_20180127_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
