# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPlacer', '0005_auto_20141128_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalidentifier',
            old_name='ext_identifier',
            new_name='identifier',
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='service',
            field=models.ForeignKey(related_name=b'pricehistories', to='OrderPlacer.MedicalService'),
        ),
    ]
