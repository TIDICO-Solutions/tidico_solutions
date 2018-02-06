# Generated by Django 2.0.1 on 2018-01-26 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCard',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('e_reg.user',),
        ),
    ]
