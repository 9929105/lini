# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('encntr_dt', models.DateTimeField(auto_now_add=True)),
                ('followup_dt', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_encounter_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_encounter_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExternalIdentifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('ext_identifier', models.CharField(max_length=500)),
                ('issued_by', models.CharField(max_length=200)),
                ('unique_pool', models.CharField(max_length=200)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_externalidentifier_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_externalidentifier_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('display', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_medicalservice_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_medicalservice_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('order_identifier', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('price_adjusted_dt', models.DateTimeField(null=True)),
                ('order_dt', models.DateTimeField(auto_now_add=True)),
                ('collect_dt', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('person_identifier', models.CharField(max_length=200)),
                ('name_last', models.CharField(max_length=200)),
                ('name_first', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('birthdate', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_person_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_person_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_personroles_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_personroles_modified_by', to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(related_name=b'personroles_person', to='OrderPlacer.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('price', models.FloatField(default=0.0)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_price_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_price_modified_by', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(related_name=b'price_service', to='OrderPlacer.MedicalService')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('role_name', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_role_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_role_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now_add=True)),
                ('beg_effective_dt', models.DateTimeField(auto_now_add=True)),
                ('end_effecitve_dt', models.DateTimeField(default=datetime.date(2199, 12, 31))),
                ('synonym', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=1000)),
                ('created_by', models.ForeignKey(related_name=b'orderplacer_synonym_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name=b'orderplacer_synonym_modified_by', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(related_name=b'synonym_service', to='OrderPlacer.MedicalService')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personroles',
            name='role',
            field=models.ForeignKey(related_name=b'peresonroles_role', to='OrderPlacer.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='collected_by',
            field=models.ForeignKey(related_name=b'order_collected_by', to='OrderPlacer.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(related_name=b'orderplacer_order_created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='modified_by',
            field=models.ForeignKey(related_name=b'orderplacer_order_modified_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_by',
            field=models.ForeignKey(related_name=b'orders_ordered_by', to='OrderPlacer.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(related_name=b'orders_patient', to='OrderPlacer.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='price_adjusted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(related_name=b'order_service', to='OrderPlacer.MedicalService'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encounter',
            name='patient',
            field=models.ForeignKey(related_name=b'encounter_patient', to='OrderPlacer.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='encounter',
            name='provider',
            field=models.ForeignKey(related_name=b'encounter_physician', to='OrderPlacer.Person'),
            preserve_default=True,
        ),
    ]
