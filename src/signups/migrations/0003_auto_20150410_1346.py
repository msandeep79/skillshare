# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_signup_for_you'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='phone',
        ),
        migrations.AddField(
            model_name='signup',
            name='phonenumber',
            field=models.CharField(max_length=20, serialize=False, primary_key=True, blank=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='for_you',
            field=models.BooleanField(default=True, verbose_name=b'Is this for you ?'),
        ),
    ]
