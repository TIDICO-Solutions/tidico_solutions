# Generated by Django 2.0.1 on 2018-11-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0054_auto_20180220_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelproperty',
            name='name',
            field=models.CharField(blank=True, choices=[('Sofitel Legend The Grand Amsterdam', 'Sofitel Legend The Grand Amsterdam')], max_length=255),
        ),
    ]