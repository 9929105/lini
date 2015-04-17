# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0007_auto_20141204_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalservice',
            old_name='specialty',
            new_name='speciality',
        ),
    ]
