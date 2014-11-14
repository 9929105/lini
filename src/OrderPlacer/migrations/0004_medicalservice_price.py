# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0003_remove_medicalservice_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalservice',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
