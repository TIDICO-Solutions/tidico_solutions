# Generated by Django 2.0.1 on 2018-01-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0022_auto_20180129_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
