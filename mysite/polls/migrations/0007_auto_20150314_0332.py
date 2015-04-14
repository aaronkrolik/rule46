# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150314_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accolade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('accolade_text', models.TextField()),
                ('player', models.ForeignKey(to='polls.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='x', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.CharField(default='x', max_length=200),
            preserve_default=False,
        ),
    ]
