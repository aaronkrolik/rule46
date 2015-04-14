# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150314_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 3, 55, 7, 977071, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 3, 55, 16, 867093, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='update',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 14, 3, 55, 24, 388883, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
