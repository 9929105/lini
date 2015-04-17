# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0010_auto_20150209_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encounter',
            name='id',
        ),
        migrations.RemoveField(
            model_name='externalidentifier',
            name='id',
        ),
        migrations.RemoveField(
            model_name='medicalservice',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.RemoveField(
            model_name='personroles',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.RemoveField(
            model_name='synonym',
            name='id',
        ),
        migrations.AddField(
            model_name='encounter',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='externalidentifier',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalservice',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personroles',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='synonym',
            name='my_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
