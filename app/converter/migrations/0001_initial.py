# Generated by Django 4.0.4 on 2022-05-21 10:26

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('currency_code_l', models.TextField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(3)])),
                ('units', models.IntegerField()),
                ('amount', models.FloatField()),
                ('update_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
