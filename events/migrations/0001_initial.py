# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '__first__'),
        ('campaigns', '0004_campaignuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaginEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element', models.ForeignKey(related_name='events', to='campaigns.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('creator', models.ForeignKey(related_name='event_organized', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_start'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(related_name='joins', to='events.Event')),
                ('user', models.ForeignKey(related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MonitorableEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element', models.ForeignKey(related_name='events', to='projects.Monitorable')),
                ('event', models.ForeignKey(related_name='Projects', to='events.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaginevent',
            name='event',
            field=models.ForeignKey(related_name='campaigns', to='events.Event'),
            preserve_default=True,
        ),
    ]
