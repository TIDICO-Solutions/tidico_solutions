# Generated by Django 2.0.1 on 2018-02-09 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0049_auto_20180209_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotelmembership',
            options={'ordering': ['-guestuser']},
        ),
    ]