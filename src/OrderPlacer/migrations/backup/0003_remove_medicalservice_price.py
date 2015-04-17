# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0002_auto_20141112_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalservice',
            name='price',
        ),
    ]
