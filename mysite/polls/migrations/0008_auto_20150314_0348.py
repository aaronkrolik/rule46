# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150314_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('tagline', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='bylines',
            field=models.ManyToManyField(to='polls.Author'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='incidents',
            field=models.ManyToManyField(to='polls.Incident'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='players',
            field=models.ManyToManyField(to='polls.Player'),
            preserve_default=True,
        ),
    ]
