# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150314_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sport',
            field=models.CharField(max_length=20, choices=[(b'NFL', b'NFL'), (b'NBA', b'NBA')]),
            preserve_default=True,
        ),
    ]
