# Generated by Django 3.1.7 on 2021-04-03 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='datefield',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
