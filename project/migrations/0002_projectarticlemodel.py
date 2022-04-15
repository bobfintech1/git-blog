# Generated by Django 4.0.3 on 2022-04-15 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('primer', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
