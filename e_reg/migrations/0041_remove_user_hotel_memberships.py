# Generated by Django 2.0.1 on 2018-02-09 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0040_auto_20180209_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hotel_memberships',
        ),
    ]
