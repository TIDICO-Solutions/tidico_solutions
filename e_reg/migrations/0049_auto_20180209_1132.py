# Generated by Django 2.0.1 on 2018-02-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0048_auto_20180209_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelmembership',
            name='guestuser',
            field=models.ForeignKey(on_delete='CASCADE', related_name='membership', to='e_reg.GuestUser'),
        ),
    ]