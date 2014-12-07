# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20141203_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='data',
            field=models.FileField(upload_to=b'/uploads/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='upload',
            name='project',
            field=models.ForeignKey(related_name='uploads', blank=True, to='projects.Monitorable', null=True),
            preserve_default=True,
        ),
    ]
