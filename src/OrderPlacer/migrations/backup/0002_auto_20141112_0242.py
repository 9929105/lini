# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OrderPlacer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('price', models.FloatField(default=0.0)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_pricehistory_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_pricehistory_modified_by', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(related_name=b'price_service', to='OrderPlacer.MedicalService')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='price',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='price',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='price',
            name='service',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
