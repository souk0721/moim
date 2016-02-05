# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('but_moim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit_info',
            name='deposit_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='moim_info',
            name='moim_person_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='moim_info',
            name='moim_total_money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moim_info',
            name='user',
            field=models.ForeignKey(default=1, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moim_info',
            name='moim_deposit_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='tel',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
