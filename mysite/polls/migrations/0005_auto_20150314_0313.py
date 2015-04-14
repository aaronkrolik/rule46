# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150314_0300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default='z', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='middle_name',
            field=models.CharField(default='z', max_length=200),
            preserve_default=False,
        ),
    ]
