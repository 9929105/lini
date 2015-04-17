# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0006_auto_20141204_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_identifier',
            new_name='identifier',
        ),
    ]
