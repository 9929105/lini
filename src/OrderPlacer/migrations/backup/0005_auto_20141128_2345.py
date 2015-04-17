# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0004_medicalservice_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encounter',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='externalidentifier',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='medicalservice',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='order',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='person',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='personroles',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='role',
            name='end_effecitve_dt',
        ),
        migrations.RemoveField(
            model_name='synonym',
            name='end_effecitve_dt',
        ),
        migrations.AddField(
            model_name='encounter',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='externalidentifier',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalservice',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personroles',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='synonym',
            name='end_effective_dt',
            field=models.DateTimeField(default=datetime.datetime(2199, 12, 31, 0, 0)),
            preserve_default=True,
        ),
    ]
