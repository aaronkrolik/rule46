# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150314_0215'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accolades',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='incident_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='update',
            old_name='update',
            new_name='incident',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='players',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='title',
        ),
        migrations.AddField(
            model_name='incident',
            name='crime',
            field=models.TextField(default='x'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='update',
            name='headline',
            field=models.CharField(default='x', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='update',
            name='update_text',
            field=models.TextField(default='x'),
            preserve_default=False,
        ),
    ]
