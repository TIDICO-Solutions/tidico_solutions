# Generated by Django 2.0.1 on 2018-02-05 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0031_auto_20180205_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestuser',
            name='room_level',
        ),
    ]
