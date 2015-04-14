# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150314_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sport', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='incident',
            name='players',
            field=models.ManyToManyField(to='polls.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='update',
            name='byline',
            field=models.CharField(default='x', max_length=200),
            preserve_default=False,
        ),
    ]
